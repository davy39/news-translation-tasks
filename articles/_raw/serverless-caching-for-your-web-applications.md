---
title: How to Cache Expensive Database Queries Using the Momento Serverless Cache
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-22T20:45:05.000Z'
originalURL: https://freecodecamp.org/news/serverless-caching-for-your-web-applications
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-tiger-lily-4483610.jpg
tags:
- name: caching
  slug: caching
- name: database
  slug: database
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Andrew Brown

  When to Use a Cache

  When you are building a web-application, you''ll need to fetch data from a database.
  As your traffic and the size of your database grows, you will find that querying
  your database gets slower and slower.

  In order to...'
---

By Andrew Brown

## When to Use a Cache

When you are building a web-application, you'll need to fetch data from a database. As your traffic and the size of your database grows, you will find that querying your database gets slower and slower.

In order to return requests to users quickly, a cache can be a cost-effective and easy solution rather than having to upgrade your database.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-22-at-10.37.53-AM.png)
_Diagram showing how a cache works_

A cache is an in-memory database which can store simple data as a key and value data structure.

Popular open-source caching solutions that already exist are Memcache and Redis.

## What is Momento?

Momento Serverless Cache is a Caching-as-a-Service (CaaS) that you can integrate as a caching solution. It will reduce expensive or unnecessary queries against your primary database.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-22-at-12.54.33-PM.png)

Momento has an SDK for the eight most popular programming languages. Here's an example of using the Ruby SDK to do a simple get and set of a cache item:

```ruby
require 'momento'

client = Momento::SimpleCacheClient.new(
  auth_token: ENV['MOMENTO_AUTH_TOKEN'],
  default_ttl: ENV['MOMENTO_TTL']
)

response = client.set ENV['MOMENTO_CACHE_NAME'], "Hello", "World"
response = client.get ENV['MOMENTO_CACHE_NAME'], key
if response.hit?
  puts "Cache returned: #{response.value_string}"
elsif response.miss?
  puts "The item wasn't found in the cache."
end

```

Just a quick note: the company is called Momento and the caching product is called the Momento Serverless Cache, but we'll just say "Momento" to refer to the product to keep it simple.

## Why Use Momento?

Momento is a Serverless Cache, and as a result has the following benefits:

* Creating a new cache is nearly instant
* You pay based on usage ($0.15/GB per transfer cost)
* It has a very generous free-tier (first 50GB per month free)
* No credit card required to start using the cache
* It just scales, no server configuration or tuning required
* It just works from anywhere

Momento is ideal for developers who just need a simple caching solution, and want to focus on their code instead of having to mange caching infrastructure.

## Why Not Use a Managed Open Source Service?

Their are already open-source managed cloud services.

For example:

* AWS has ElasticCache which allows you to run Memcached or Redis
* Amazon MemoryDB for Redis
* Azure has an Azure Cache for Redis
* Redis has its own Redis Cloud offering

These existing cloud services can simplify some aspects of hosting and scaling a caching layer for your web-applications. But there are some things to consider:

* you have to choose the right size compute
* there are additional application integration steps
* it takes time (up to an hour) to provision a cache
* there are limitations on where a cache must live in your network

The Redis opens-source in memory database, for example, has a variety of complex data structures and data operations. It could be suited to more advanced use cases, where it goes beyond being a cache and can act (and is marketed as) a primary database.

There is no wrong answer when choosing a cache. What you have are trade-offs and you need to choose the best solution for your use-case.

## How to Install Momento CLI 

Momento (at the time of writing this article) is an API-only service. 

So in order to use Momento you need to create an account by using their CLI tool.

**Windows Install Instructions:**

```bash
brew tap momentohq/tap
brew install momento-cli
```

**Linux Install Instructions:**

```bash
wget https://github.com/momentohq/momento-cli/releases/download/v0.22.8/momento-cli-0.22.8.linux_x86_64.tar.gz
tar -xvf momento-cli-0.22.8.linux_x86_64.tar.gz --strip-components 3
sudo mv momento /usr/local/bin
rm momento-cli-0.22.8.linux_x86_64.tar.gz
```

Once installed, test that the CLI is working with the following command:

```bash
momento --version
> momento 0.22.6
```

## How to Create a Momento Account

To create an account, enter the following command: 

```bash
momento account signup aws \
--email YOUR_EMAIL \
--region us-east-1

> Signing up for Momento...
> Success! Your access token will be emailed to you shortly.
```

Remember to replace `YOUR_EMAIL` with your own email address (for example, andrew@example.com).

Momento is **going to email an access token** and this access token is how Momento will identify and authorize our future API calls to use the cache.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-21-at-9.55.07-PM.png)
_Example email with provided token_

### Why did I need to type "aws" when creating an account?

Notice that we specified **aws** and the AWS region **us-east-1** on creation.

When you create an account, you need to say which Cloud Service Provider (CSP) that the cache will be hosted on. 

You might think, do I need to have and connect my own AWS account? 

The answer is no. The cache is being setup within Momento's AWS account. 

The reason Momento allows you to choose the CSP is because some companies have data policies about what part of the world and what CSP their data must reside on. 

## How to Configure the CLI to Use the Access Token

We need to configure the CLI to use the access token that was emailed.

Type the `momento configure` command to prompt the configuration wizard:

```bash
momento configure
Token: XXXXXXXXXXXXXXXXX
Default Cache [default-cache]: 
Default Ttl Seconds [600]: 
default-cache successfully created as the default with default TTL of 600s
```

* **Token**: Enter the token by copying and pasting it from the previous email
* **Default Cache**: Hit enter
* **Default TTL:** Hit enter

The `momento configure` will generate two TOML configuration files:

1. `~/.momento/credentials` – stores sensitive configuration, for example: access token

```toml
[default]
token=XXXXXXXX
```

2.  `~/.momento/config` – stores common configuration, for example: ttl default

```toml
[default]
cache=default-cache
ttl=600
```

## How to Set and Get Cache Data

To set cache data is straightforward. You have the `cache set` and the `cache get` subcommands:

```bash
momento cache set --key "andrew" --value "brown" 
momento cache get --key "andrew"
> brown
```

## How to Create a New Cache

We can create a another cache instantly with the `cache create` command. And we'll supply the `--name` flag to the `cache get` and `cache set`:

```bash
momento cache create --name freecodecamp
momento cache set --name freecodecamp --key "Quincy" --value "Larson" 
momento cache get --name freecodecamp --key "Quincy" 
> Larson
```

## How to Integrate Momento Directly into Your Web Application Code

To use Momento within backend web-application code, we need to use one of the provided SDKs.

Let's write an example of using Momento in a Flask (Python) web-application using the Momento Python SDK.

Here is what our Flask app looks without using caching:

```python
import os
import psycopg2
from flask import Flask, render_template
import json

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

@app.route('/')

def index():
    json_data = get_free_courses()

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    return response

def get_free_courses():
  json_data = None
  conn = get_db_connection()
  cur = conn.cursor()

  cur.execute('SELECT * FROM free_courses;')
  free_courses = cur.fetchall()

  json_data = json.dumps(free_courses)

  cur.close()
  conn.close()
  return json_data
```

Here is what our application would look like implementing Momento:

```python
import os
import psycopg2
from flask import Flask, render_template
import json
from momento import simple_cache_client as scc

_MOMENTO_AUTH_TOKEN  = os.getenv('MOMENTO_AUTH_TOKEN')
_MOMENTO_TTL_SECONDS = os.getenv('MOMENTO_TTL_SECONDS')
_MOMENTO_CACHE_NAME  = os.getenv('_MOMENTO_CACHE_NAME')

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

@app.route('/')
def index():
  with scc.SimpleCacheClient(_MOMENTO_AUTH_TOKEN, _MOMENTO_TTL_SECONDS) as cache_client:
    key = 'get_free_courses'
    get_resp = cache_client.get(_CACHE_NAME, 'get_free_courses')
    if get_resp.status() == 'hit':
      json_data = get_resp.value()
    elif get_resp.status() == 'miss':
      json_data = get_free_courses()
      cache_client.set(_CACHE_NAME, 'get_free_courses', json_data)

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    return response

def get_free_courses():
  json_data = None
  conn = get_db_connection()
  cur = conn.cursor()

  cur.execute('SELECT * FROM free_courses;')
  free_courses = cur.fetchall()

  json_data = json.dumps(free_courses)

  cur.close()
  conn.close()
  return json_data
```

## Summary

If you want to give Momento a go, visit their website documentation for more information.

%[https://docs.momentohq.com/]



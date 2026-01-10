---
title: How to Create Better Policy with Open Policy Agent and the Apache APISIX OPA
  Plugin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-24T19:28:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-open-policy-agent-and-apache-apisix-opa-plugin
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-357514.jpg
tags:
- name: apache
  slug: apache
- name: 'Back end development '
  slug: back-end-development
- name: backend
  slug: backend
- name: Policy
  slug: policy
seo_title: null
seo_desc: "By Njoku Samson Ebere\nOne common thing in every organisation is policy.\
  \ Policies define how an organisation operates. \nThey are essential to the long-term\
  \ success of an organisation. They preserve significant knowledge about how to comply\
  \ with matter..."
---

By Njoku Samson Ebere

One common thing in every organisation is [policy](https://www.openpolicyagent.org/docs/latest/philosophy/#policy). Policies define how an organisation operates. 

They are essential to the long-term success of an organisation. They preserve significant knowledge about how to comply with matters such as legal requirements, work within technical constraints, and avoid repeating mistakes.   
  
Softwares follow the same pattern by adhering to rules that govern its behavior. These rules (or policies) may specify the application's environments, permitted network routes, dependencies versions allowed, and when micro-services receive API requests. Usually, developers create them manually using documents like spreadsheets.   
  
The issue with this method is that it gradually becomes bulky. If each part of an application has its policy, things like authorization will be hard to manage across the whole application. There might also be the unnecessary repetition of policies across different parts of the application. 

Aside from that, updating any policy will require the redeployment of the whole application. Fortunately, **Open Policy Agent**(OPA) found a way to fix these issues.  
  
This article will explain what OPA is, how it works, what the OPA plugin entails, and how to use it.   
  
Let’s get started!

## What is OPA?

[OPA](https://www.openpolicyagent.org/docs/latest/) is an open-source general-purpose policy engine. It can replace built-in policy function modules in software and help users decouple services from the policy engine.

OPA provides a way to build applications separate from their policies and for them to be reusable in many applications.   
  
The OPA policy handling method reduces complexities and gives more control to the application owner. OPA allows users to integrate it with other services, such as program libraries, and HTTP APIs.

## How OPA Works

OPA mediates between applications and policies to decide the rule to apply in handling a request. The image below describes its operation:

![Image](https://paper-attachments.dropboxusercontent.com/s_EFDBAAA4A6A8765E2C2CBACA1FE670A8A1A3C4F3B2852B5E7907B18C06560424_1662070285391_opa-service.svg)

Here is a breakdown of the image above:

1. A service (let’s say it is an authentication micro-service) receives a request (like a login request). For the service to decide how to handle the request, it needs to get the policy guiding authentication. That takes us to the next step.
2. The service sends a query (this can be in any JSON format) to OPA requesting for the policy to be adhered to in handling the request received.
3. OPA now compares the data and policies it has access to and makes the right decision.
4. Finally, OPA returns the policy decision (this can be in any JSON format) reached to the service.

That is a summary of how OPA works. You can imagine many services attached to OPA and OPA helping them decide how to handle requests or events instead of each service managing its policies. It provides a more robust system that is easy to maintain. 

[Apache APISIX](https://dev.to/ebereplenty/introduction-to-apache-apisix-5b4) decided to integrate with OPA by providing the OPA plugin. That's what we'll discuss now.

## Apache APISIX OPA Plugin

The plugin allows [Apache APISIX](https://apisix.apache.org/) users to conveniently introduce the policy capabilities provided by OPA when using Apache APISIX. It enables flexible authentication and access control features.

### How It Works

Apache APISIX OPA Plugin follows two main steps to carry out its task:

First, APISIX re-constructs any request data it receives into acceptable JSON data and makes a policy query to OPA with it. The query is usually referred to as an **APISIX to OPA service** request. See the following example:

```

{
    "type": "http",
    "request": {
        "scheme": "http",
        "path": "\/get",
        "headers": {
            "user-agent": "curl\/7.68.0",
            "accept": "*\/*",
            "host": "127.0.0.1:9080"
        },
        "query": {},
        "port": 9080,
        "method": "GET",
        "host": "127.0.0.1"
    },
    "var": {
        "timestamp": 1701234567,
        "server_addr": "127.0.0.1",
        "server_port": "9080",
        "remote_port": "port",
        "remote_addr": "ip address"
    },
    "route": {},
    "service": {},
    "consumer": {}
}
```

The JSON data above tells OPA that a user has made an HTTP request using the GET method via `127.0.0.1:9080/get` at `1701234567` timestamp (Wednesday, 29 November 2023 05:09:27).  
  
OPA now has to help Apache APISIX decide how to handle the request.

Next, OPA checks the policies and data available, compares them, and reaches the decision in JSON format below:

```json
{
    "result": {
        "allow": true,
        "reason": "test",
        "headers": {
            "an": "header"
        },
        "status_code": 401
    }
}
```

The policy decision above is an **OPA service to APISIX** response. It tells APISIX to accept the request due to the reason (test) given. When allow is false, Apache APISIX rejects it.  
  
The following is an explanation of some of the keys in the request and response above:

* `type` indicates the request type (`HTTP` or `stream`).
* `request` is used when the `type` is `HTTP` and contains the basic request information like URL and headers.
* `var` holds the basic information about the requested connection (IP, port, server details, and request timestamp).
* `route`, `service`, and `consumer` contain the same data stored in APISIX. They require configuration for a user to see them after a transaction.
* `allow` is required and indicates whether the request is authorised to pass through APISIX.
* `reason`, `headers`, and `status_code` are optional and are returned when you configure a custom response.

### How to Use the Plugin

This section will introduce you to some of the features of the plugin. You will see how to use Docker to build OPA services, create policy, create users’ data, create a custom route, test requests, and enable and disable the plugin.

#### How to use [docker](https://www.docker.com/) to build OPA services

Use the command below to launch the OPA environment on port `8181`

```
docker run -d --name opa -p 8181:8181 openpolicyagent/opa:0.35.0 run -s
```

We will be using [CURL](https://curl.se/) for the rest of this article. If you are new to it or you are coming from other programming languages, copy the requests or response code and [paste the code here](https://curlconverter.com/) to convert it to your preferred language.

We will also stick to the `-H` and `-d` flags instead of `--header` and `--data-raw` respectively.

#### How to create a policy

Creating a policy follows the format below:

```
curl -X PUT '127.0.0.1:8181/v1/policies/example1' \
    -H 'Content-Type: text/plain' \
    -d 'package example

import input.request

default allow = false

allow {
    # HTTP method must GET
    request.method == "GET"
}'
```

The code above came about through the following steps:

* State the route: 127.0.0.1:8181/v1/policies/example1.
* Import Request: import input.request.
* State that no request is allowed: default allow = false.
* Specify what is permissible:

```

allow {
    # HTTP method must GET
    request.method == "GET"
}
```

The code above instructs that the only acceptable HTTP method is GET. Every line in the allow object gets implemented as policies asides from the lines that begin with a # because they are comments.   
  
You can add as many rules as you want based on the policies you have in mind. For example, the code below contains five rules that must be adhered to:

```
# Create policy
curl -X PUT '127.0.0.1:8181/v1/policies/example1' \
    -H 'Content-Type: text/plain' \
    -d 'package example

import input.request
import data.users

default allow = false

allow {
    # has the name test-header with the value only-for-test request header
    request.headers["test-header"] == "only-for-test"

    # The request method is GET
    request.method == "GET"

    # The request path starts with /get
    startswith(request.path, "/get")

    # GET parameter test exists and is not equal to abcd
    request.query["test"] != "abcd"

    # GET parameter user exists
    request.query["user"]
}'
```

With the configuration we have made so far, everything will work fine. But what happens when our users get something wrong and an error they don’t understand is returned to them? They will become frustrated and left with a bad user experience. We can avoid that by adding a **custom response.**  
  
A custom response provides extra details (body, header, and status code) about the result of a transaction. Our request now becomes:

```

# Create policy
curl -X PUT '127.0.0.1:8181/v1/policies/example1' \
    -H 'Content-Type: text/plain' \
    -d 'package example

import input.request
import data.users

default allow = false

allow {
    # has the name test-header with the value only-for-test request header
    request.headers["test-header"] == "only-for-test"
    # The request method is GET
    request.method == "GET"
    # The request path starts with /get
    startswith(request.path, "/get")
    # GET parameter test exists and is not equal to abcd
    request.query["test"] != "abcd"
    # GET parameter user exists
    request.query["user"]
}

# custom response body (Accepts a string or an object, the object will respond as JSON format)
reason = users[request.query["user"]].reason {
    not allow
    request.query["user"]
}

# custom response header (The data of the object can be written in this way)
headers = users[request.query["user"]].headers {
    not allow
    request.query["user"]
}

# custom response status code
status_code = users[request.query["user"]].status_code {
    not allow
    request.query["user"]
}'
```

When a user gets an error, it becomes easier to debug because the error comes with a `reason`, `headers` details, and `status_code`.

#### How to create users’ data

The users' data is an object of objects. Each user data is an object of custom details (body, header, and status code) that help with user authorization. 

The code below is an example of users data containing four (4) users with different details:

```
# Create test user data
curl -X PUT '127.0.0.1:8181/v1/data/users' \
    -H 'Content-Type: text/plain' \
    -d '{

    "alice": {
        "headers": {
            "Location": "http://example.com/auth"
        },
        "status_code": 302
    },

    "bob": {
        "headers": {
            "test": "abcd",
            "abce": "test"
        }
    },

    "carla": {
        "reason": "Give you a string reason"
    },

    "dylon": {
        "headers": {
            "Content-Type": "application/json"
        },
        "reason": {
            "code": 40001,
            "desc": "Give you a object reason"
        }
    }
}'
```

Notice that each user’s custom details are optional and may differ for every user.

#### How to create a custom route and enable the plugin

The APISIX OPA plugin's flexibility makes it possible for users to customize their route like in the code below:

```
curl -X PUT 'http://127.0.0.1:9080/apisix/admin/routes/r1' \
    -H 'X-API-KEY: <api-key>' \
    -H 'Content-Type: application/json' \
    -d '{
    "uri": "/*",
    "methods": [
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ],
    "plugins": {},
    "upstream": {
        "nodes": {
            "httpbin.org:80": 1
        },
        "type": "roundrobin"
    }
}'
```

For this to work, the plugin has to be enabled. Enter the needed configuration into the `plugins` object to turn it on. So we have:

```

curl -X PUT 'http://127.0.0.1:9080/apisix/admin/routes/r1' \
    -H 'X-API-KEY: <api-key>' \
    -H 'Content-Type: application/json' \
    -d '{
    "uri": "/*",
    "methods": [
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ],
    "plugins": {
        "opa": {
            "host": "http://127.0.0.1:8181",
            "policy": "example1"
        }
    },
    "upstream": {
        "nodes": {
            "httpbin.org:80": 1
        },
        "type": "roundrobin"
    }
}'
```

Now that the plugin is enabled, you can use your route as you see fit.

#### How to test the requests

We have been able to create policies, users’ data, and custom routes and enabled the Apache APISIX OPA plugin so far. Let’s now test these setups and see the response we get for different scenarios:

Here's a test for when a request is allowed:

Request:

```

curl -XGET '127.0.0.1:9080/get?test=none&user=dylon' \
    --header 'test-header: only-for-test'
```

  
Response:

```
{
    "args": {
        "test": "abcd1",
        "user": "dylon"
    },
    "headers": {
        "Test-Header": "only-for-test",
        "with": "more"
    },
    "origin": "127.0.0.1",
    "url": "http://127.0.0.1/get?test=abcd1&user=dylon"
}
```

Here's a test for when a request is rejected and the status code and response headers are re-written:

Request:

```

curl -XGET '127.0.0.1:9080/get?test=abcd&user=alice' \
    --header 'test-header: only-for-test'
```

Response:

```

HTTP/1.1 302 Moved Temporarily
Date: Mon, 20 Dec 2021 09:37:35 GMT
Content-Type: text/html
Content-Length: 142
Connection: keep-alive
Location: http://example.com/auth
Server: APISIX/2.11.0
```

Here's a test for when a request is rejected and a custom response header is returned:

Request:

```

curl -XGET '127.0.0.1:9080/get?test=abcd&user=bob' \
    --header 'test-header: only-for-test'

```

Response:

```

HTTP/1.1 403 Forbidden
Date: Mon, 20 Dec 2021 09:38:27 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 150
Connection: keep-alive
abce: test
test: abcd
Server: APISIX/2.11.0

```

Here's a test for when a request is rejected and a custom response (string) is returned:

Request:

```

curl -XGET '127.0.0.1:9080/get?test=abcd&user=carla' \
    --header 'test-header: only-for-test'
```

Response:

```

HTTP/1.1 403 Forbidden
Date: Mon, 20 Dec 2021 09:38:58 GMT
Content-Type: text/plain; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Server: APISIX/2.11.0

Give you a string of reason
```

And here's a test for when a request is rejected and a custom response (JSON) is returned:

Request:

```

curl -XGET '127.0.0.1:9080/get?test=abcd&user=dylon' \
    --header 'test-header: only-for-test'
```

Response:

```

HTTP/1.1 403 Forbidden
Date: Mon, 20 Dec 2021 09:42:12 GMT
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive
Server: APISIX/2.11.0

{"code":40001,"desc":"Give you a object reason"}
```

#### How to disable the plugin

To disable the APISIX OPA plugin, remove all the configurations we added when we set up a custom route and enabled the plugin. We now have:

```

curl -X PUT 'http://127.0.0.1:9080/apisix/admin/routes/r1' \
    -H 'X-API-KEY: <api-key>' \
    -H 'Content-Type: application/json' \
    -d '{
    "uri": "/*",
    "methods": [
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ],
    "plugins": {},
    "upstream": {
        "nodes": {
            "httpbin.org:80": 1
        },
        "type": "roundrobin"
    }
}'
```

The `plugins` object being empty indicates that the plugin cannot work. It is that easy because of Apache APISIX’s dynamic nature.

## **Conclusion**

This article aimed to introduce you to the Apache APISIX OPA plugin and walk you through some of its features. 

We began by looking at what OPA is and why APISIX adopted it by employing a plugin. Then we discussed how the plugin works and how we can use it.  
  
Apache APISIX currently has more than ten authentication and authorization-related plugins that support interfacing with mainstream authentication/authorization services in the industry.  

If you need to interface with other authentication authorities, you can visit [Apache APISIX's GitHub](https://github.com/apache/apisix/issues) and leave your suggestions via an issue or subscribe to [Apache APISIX's mailing list](https://apisix.apache.org/zh/docs/general/subscribe-guide) to express your ideas.  
  
I hope this article helps you understand how to use OPA in Apache APISIX so you can start adopting it yourself. I also encourage you to take the time to visit the [Apache APISIX OPA plugin documentation](https://apisix.apache.org/docs/apisix/plugins/opa/) to see other use cases for the plugin. The more you practice with it, the better you get at using it.  
  
Happy Policy Making!  


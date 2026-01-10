---
title: How to customize Node.js .env files for different environment stages
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-05T14:11:53.000Z'
originalURL: https://freecodecamp.org/news/nodejs-custom-env-files-in-your-apps-fa7b3e67abe1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s20L9h0d1TmrZGrxLZAZ7Q.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Erisan Olasheni


  Have you ever found yourself in a situation where you needed custom environment
  variables for different development stages of your app? Here is a one-line solution.


  Development has been much easier since the invention of the .env...'
---

By Erisan Olasheni

> **_Have you ever found yourself in a situation where you needed custom environment variables for different development stages of your app? Here is a one-line solution._**

Development has been much easier since the invention of the `.env` file. You can easily set your environment variables and values with the syntax `ENV_VARIABLE=VALUE` and boom! These variables got loaded as your environment variables, making it possible to get quick access to them:

```bash
console.log(process.env.ENV_VARIABLE)
```

In case you are still wondering what all this means, well, you are probably new to the `.env` file. It’s actually a simple configuration text file that is used to define some variables you want to pass into your application’s environment.

This file needs a something like a **parser** to make it work. The parser reads the variable definitions **one-by-one** and parses them to the environment. It uses the format **ENV_VARIABLE=VALUE** (in the case of Node.js: `process.env[ENV_VARIABLE]=VALUE`).

Of course, this is not a built-in feature in Node.js. You have to engineer it with a popular module called **dotenv**.

It’s a nice workaround, as it has really made development easier between co-developers and across the dev community as a whole. I personally had been using the **dotenv** module, until I got stranded trying to get a solution that could make me use a different configuration file for a particular environment. That would be even cooler…right? Yes! But unfortunately, the **dotenv** module doesn’t provide us with this goody.

**So what’s next? We need this thing to make development and testing easier across different development stages!**

### How about custom .env files for different environment stages?

Don’t you think that would be a good solution? Defining custom environment variables by just creating a _.env.envname_ file? Cool! That is what **custom-env** has come to do.

**Custom env is a library built to make development easier by allowing multiple .env configuration for different environments.** This is done by loading environment variables from a .env.envname file into the node’s `process.env` object.

#### Installation

Just grab it with the following command:

```bash
npm i custom-env
```

#### Usage

```bash
require('custom-env').env()
```

By default, _custom-env_ picks the .env file for your dev stage. However, to customize for a different stage, add the name as a suffix as in _.env.envname._

**Example**

We can define a custom environment variable for a **staging development.**

* Create a .env.staging file
* Define your variables

```bash
APP_ENV=staging
APP_NAME=custom environment app
DB_HOST=localhost
DB_USER=user
DB_PASS=pass
```

* Access your variables

```js
// Require custom-env and set your preferred env file

require ('custom-env').env('staging')

console.log(process.env.APP_ENV)

console.log(process.env.APP_NAME)

console.log(process.env.DB_HOST)

console.log(process.env.DB_PASS)
```

**Expected Output**

```bash
staging
custom environment app
localhost
user
pass
```

That’s it, pretty easy. Feel free to define more variables for different stages you think you have, like:

_.env.testing, .env.staging, .env.server1, .env.server2, .env.localhost_

### Set to the Current Environment

You can tell _custom-env_ to use a configuration that matches your current development stage by passing **true** to the `_env()_` method.

**Example**

**File: index.js**

```js
// Pass true to env() to make it use the current environment stage.

require('custom-env').env(true)

console.log(process.env.APP_NAME)
console.log(process.env.USERNAME)
console.log(process.env.PASSKEY)
```

Now let’s define a staging configuration file:

**File: .env.staging**

```bash
APP_NAME=Staging Node App
USER_NAME=John
PASSKEY=J*h*
```

Now let’s serve node with the staging environment:

```bash
NODE_ENV=staging node index.js
```

**Expected Output**

![Image](https://cdn-media-1.freecodecamp.org/images/7tb8GikXlYKDDLXQoSaVwvOKfAxsG9iOVcNz)
_Gets the variables according to the **staging** environment._

**There you go!**

### Full Documentation

For the full documentation of _custom-env,_ visit the **npm page** [https://www.npmjs.com/package/custom-env](https://www.npmjs.com/package/custom-env)

### Source Code

You can get or contribute to the _custom-env_ source code at [https://github.com/erisanolasheni/custom-env](https://github.com/erisanolasheni/custom-env)

**_Happy Coding!_**


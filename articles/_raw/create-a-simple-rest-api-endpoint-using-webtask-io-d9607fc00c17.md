---
title: Create a simple REST API endpoint using Webtask.io
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-01T09:18:04.000Z'
originalURL: https://freecodecamp.org/news/create-a-simple-rest-api-endpoint-using-webtask-io-d9607fc00c17
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NeGT5gT1GaOUWOC-ZSRlag.jpeg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By ismapro

  Webtask.io is a service by Auth0 that allows you to run single pieces of code in
  the cloud through HTTP calls.

  Each deployed piece will run under a sandbox with some limitations:


  limited processor time

  a limited amount of libraries availa...'
---

By ismapro

Webtask.io is a service by Auth0 that allows you to run single pieces of code in the cloud through HTTP calls.

Each deployed piece will run under a sandbox with some limitations:

* limited processor time
* a limited amount of libraries available per task
* limited storage

But these limitations serve to present an environment where you can expose your application through _HTTP_, in easy and scalable way, without getting into the nitty-gritty of server administration or environment configurations.

There are many other features available like token validation to control access, secret data, and metadata. If you want to know more of how Webtask works, [their documentation](https://webtask.io/docs/how) has examples of what you can do with this technology.

#### Let’s start to code the basic REST API

To create a webtask, you’ll need to use the _webtask-cli._ This is a command line application that allows you to manage your webtasks.

So first install it in your enviroment:

```
npm install wt-cli -g
```

Then initialize your session, using this email login process:

```
wt init your_email@something.com
```

Once you do so, you should receive a code to activate your account.

Now you can proceed to create the file that will be logic of our webtask. You can name it whatever you want, but remember that it will be part of the URL the service will later provide. Let’s name it:

```
basic-rest.js
```

and lets add the following code to it:

Navigate from the command line to the location where you saved the file and run this command:

```
wt create basic-rest.js
```

You will receive a URL that you can use to check your webtask, similar to this:

```
https://webtask.it.auth0.com/api/run/wt-myemail-gmail_com-0/basic-rest?webtask_no_cache=1
```

From your browser navigate to the your url and you will see the response of your application:

```
{"error":"GET method not implemented"}
```

Which is the response we expected from our code. Now you can add any logic you want to each one of the methods. You can then test the other methods (POST, DELETE, PUT) using postman or curl.

And that’s it. You have deployed a service without any additional configuration or administration. The great thing about this service is the ability to integrate webhooks from external APIs and interact with the data or query using other backends.

There are many features and options I didn’t explored but you can check their [webpage](https://webtask.io) and now more about them.

_Hope you liked, let me know what you think in the comments sections. Happy coding!_


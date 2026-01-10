---
title: 'Serverless NodeJS: the fast, inexpensive way to build your next microservice'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-04T22:22:31.000Z'
originalURL: https://freecodecamp.org/news/true-er-functional-programming-on-serverless-nodejs-e532079b40d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HH3q_1O71DPFAip-v34jeg.jpeg
tags:
- name: aws lambda
  slug: aws-lambda
- name: google cloud functions
  slug: google-cloud-functions
- name: Microservices
  slug: microservices
- name: Node.js
  slug: nodejs
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Filipe Tavares

  I love Node.js. I’ve re-discovered Javascript through it, and I’m never going back.

  Its lightweight character, non-blocking nature, and quick development experience
  shine in Microservices.

  I also love Express — it makes writing serv...'
---

By Filipe Tavares

I love [Node.js](https://nodejs.org). I’ve re-discovered Javascript through it, and I’m never going back.

Its lightweight character, non-blocking nature, and quick development experience shine in Microservices.

I also love [Express](http://expressjs.com) — it makes writing server applications so simple. And its [Connect](https://github.com/senchalabs/connect)-based middleware stack approach makes extending applications easy and fun. Couple it with Docker and the sky’s the limit. Or, better yet, go serverless.

### Smaller than small…

![Image](https://cdn-media-1.freecodecamp.org/images/1*HH3q_1O71DPFAip-v34jeg.jpeg)

First they gave us Servers, so we built Service-Oriented Architectures.

Then they gave us Containers, so we built Microservices.

Now they give us **Serverless Event Handlers**, so we’ll build **Functions**.

Our hosting platforms have become more amenable to deploying smaller units. And so have our applications broken down into smaller software packages. There are many reasons for this, and there are diverging opinions on whether it’s a good thing.

But if we look back at the original concepts behind cloud computing, there was a dream of having code distributed infinitely in a network of connected computation nodes. We’re getting a little closer with the emergence of serverless platforms.

Plus: they allow us to scale _infinitely_, while only paying for what we use.

### …but not too small

Sequences of computational steps (procedures) need shared memory to execute efficiently. We wrap those around a function definition, that defines a contract for its input and output. And this allows composition with other such functions.

This approach has been very successful in the architecture of [Unix](http://www.linfo.org/unix_philosophy.html), and is one of the reasons for its longevity and ubiquity. I don’t mean to suggest that Web applications should follow a comparable cloud-based shared eco-system (though [some](https://stdlib.com/) are trying). But we can benefit from applying similar principles when building Web applications.

Beyond function definitions, we also group closely related functions in modules. An example could be the CRUD operations for data within a given domain, such as user management. Those tend to share code, like data models, parsing logic and formatting. So when we deploy individual functions to serverless environments, we end up with lots of duplicated code.

Current serverless environments encourage single-function deployment. But, when applied to Microservices, that leads to messy stacks that are hard to manage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SBCdivCfxRGAk_ShI9h6iw.jpeg)

But let’s assume we don’t mind duplicated code deployments. After all, we can deal with it in our code repositories. We still want to share temporary resources, though, such as database connections. We also want to make sure that we deploy and manage all operations for the same domain as a single unit. We’re better off managing **function modules**.

It fits well with the [Single Responsibility Principle](http://programmer.97things.oreilly.com/wiki/index.php/The_Single_Responsibility_Principle):

> Gather together those things that change for the same reason, and separate those things that change for different reasons.

### Going serverless

So, Node.js is great for Microservices. And it’s also great for writing smaller function modules. And Express is great for building Web application in Node.js.

Yet, most serverless environments already handle many common Web server functions out of the box. And for these **Nanoservices**, that provide a mere handful of functions, we shouldn’t bother with the overhead of complex Web server logic. We must leverage HTTP, as it is the ubiquitous transport mechanism between Web services. But we should do it in a more [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) (Remote Procedure Call) kind of way.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bHajXlOuEmcVMYoW7_wLOg.jpeg)

This is where most current frameworks offer a sledgehammer to crack a nut. If anything, I’d argue that going serverless frees us from _frameworks_, to focus instead on building _purer_ functions.

Yet, there is a need for basic routing within a Nanoservice, to map incoming requests to the appropriate handler function. Also, because of the proprietary nature of these commercial serverless environments, we can make a case for having a certain level of abstraction, to decouple our functions from the specifics of the platform they’re executed in.

Functional programming applied to serverless deployments is likely to surface in more applications. Which I’m very hopeful about, because it feels like a step in the right direction. We still need to address many real-world considerations like latency, performance, and memory usage. But like with Microservices, we’ll find the right set of tools and practices to make this not just practical, but also highly performant on real-world applications.

### Modules in Cloud Functions

I wrote a small Node.js package to address these needs. It’s called [modofun](https://modofun.js.org).

![Image](https://cdn-media-1.freecodecamp.org/images/1*h555w9EzrmhNvKg_3FtagQ.png)

It carries no extra dependencies, because we want our deployments to be as small as possible. It adds minimal functionality to simplify deployments of function modules on serverless platforms. It also allows extensibility through existing middleware, such as authentication, logging, and others. Here are a few of its features:

* Basic routing to functions
* Parameter parsing
* Automatic HTTP response building
* Support for ES6 Promises (or any other then-able)
* Connect/Express-like middleware support
* **Google Cloud Functions**
* **AWS Lambda** (with AWS API Gateway events)
* Automatic error handling

Support for Azure Functions coming shortly.

### Using Modofun

Modofun makes it easy to expose functions as serverless cloud request handlers:

![Image](https://cdn-media-1.freecodecamp.org/images/1*caoa_S2By0fMnsyAErSDOA.png)

A simplistic router maps incoming requests to functions. It applies the trailing components of the URL path as function arguments. Other request data is also available as context (_this_) for the function invocation.

We can specify middleware that will run for every incoming request. Or apply it selectively to individual functions (more details in the [documentation](https://modofun.js.org/#configuration)). Modofun returns the appropriate handler for events generated by the serverless platform.

Get it with [npm](https://www.npmjs.com/package/modofun):

```
npm install modofun
```

For more examples and detailed documentation, head to the [official website](https://modofun.js.org). You can also find the full source code on [GitHub](https://github.com/modofunjs/modofun).


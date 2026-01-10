---
title: 'NodeJS: Best Practices for Production'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-15T10:18:21.000Z'
originalURL: https://freecodecamp.org/news/nodejs-best-practices-for-production-5b173983d14b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7wN5t9ILU0fpnhbMX2vtng.jpeg
tags:
- name: Design
  slug: design
- name: Microservices
  slug: microservices
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Saurabh Rayakwar

  This is an attempt to enlist the most important practices for developing and deploying
  on NodeJs.

  I have been working on this technology for a while myself. I realize its huge potential
  and place in the development process. With t...'
---

By Saurabh Rayakwar

This is an attempt to enlist the most important practices for developing and deploying on NodeJs.

I have been working on this technology for a while myself. I realize its huge potential and place in the development process. With tough competition from languages like Python and Golang, NodeJS has proven its utility in appropriate use cases.

Before I delve into the best practices ?, I would like to do a brief introduction to what a microservice pattern is. Then take the conversation further from there.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7wN5t9ILU0fpnhbMX2vtng.jpeg)

#### So, what are microservices?

Microservices - also known as the microservice architecture - is an architectural style that structures an application as a collection of services that are:

* Highly maintainable and testable
* Loosely coupled
* Independently deployable
* Organized around business capabilities.

The microservice architecture enables the continuous delivery/deployment of large, complex applications. It also enables an organization to evolve its technology stack.

#### How to decide if you need microservices

Initially, when you are just starting out to work on your MVP, you might not need to use microservices. The Y-axis scaling might not be your agenda right now. But when the product starts to mature and sometimes too early where you have to deal with scaling, the decomposition into functional modules makes more sense as the business itself is decomposing. This will be the right point to start looking into the microservices architecture pattern.

A book that I highly recommend is by Chris Richardson here: [http://bit.ly/2EmJDYt](http://bit.ly/2EmJDYt).

Microservices are most commonly considered while replacing a monolithic application that used to be pretty common until recently when containerization solutions like Docker started ruling the DevOps world. But more on that later.

It would be unfair if I continue without mentioning Domain Driven Design (DDD). It is a very popular strategy for decomposing your product into functional modules. Hence it is very useful to create microservices.

#### So, what is a domain as per DDD?

Each problem that you are trying to solve is a domain.

Each domain is subdivided into mutually exclusive bounded contexts. These contexts are nothing but separate areas of that particular problem.

In a microservice pattern, each bounded context correlates to a microservice. DDD patterns help you understand the complexity in the domain. For the domain model for each Bounded Context, you identify and define the   
entities, value objects, and aggregates that model your domain.

Depending on the complexity of your software you can choose the DDD principles or perform a simpler approach.

The goal is to achieve a highly cohesive and loosely coupled domain model. For that follow this approach:

![Image](https://cdn-media-1.freecodecamp.org/images/1*RSnJbXxdqGt-uAoumCmHzA.jpeg)

This was a brief intro on the DDD. To learn more about it, I highly recommend reading Eric Evans’s excellent book [http://bit.ly/2Eoy17l](http://bit.ly/2Eoy17l).

Moving on.

I hope you are holding on with me. ?

So from here on, I will talk more about practices specific to NodeJS. And what I mean is that microservices and DDD help you benchmark the true potential of NodeJS nevertheless. It’s complete in itself. How? We will see.

#### Which Design Pattern to use while using NodeJs

![Image](https://cdn-media-1.freecodecamp.org/images/1*waWi1Kb0zt6GptBNVQ6ikQ.jpeg)

Design Patterns are about designing software using certain standards that are known to a number of developers.

There are various design patterns we can use. I would like to introduce and/or recap for developers who already know about a pattern called the Repository Pattern.

This pattern makes it easier to separate the MVC logic while also making it easier to handle model definition and model interaction with the rest of the logic.

It consists of:

1. **Controller**: It only handles the request and response and associated attributes. It will not have any business logic or model definition or model associations too. (folder name: controllers)
2. **Service**: It contains business logic for your microservice. The control passes from controller to a service. It’s a 1:1 relationship between a controller and its service and a 1: many relationships between service and repositories. (folder name: services)
3. **Repository**: It interacts with the models that are part of the model folder. Any query to the database through the model layer will be formed here. It will not have any business logic. (folder name: repositories)
4. **Model**: It contains the model definition, associations, virtual functions (eg. in mongoose)
5. **Utilities**: This will contain helper classes/functions that can be used as services. Eg: a Redis utility that has all the functions required to interact with Redis. (folder name: utilities)
6. **Test case**: This will include unit test cases against controller methods to ensure maximum code coverage. (folder name: spec)

To read more on this, you can refer to this link: [http://bit.ly/2TrSyRS](http://bit.ly/2TrSyRS)

#### Ok, Tell me about cluster modules

A single instance of Node.js runs in a single thread. To take advantage of multi-core systems, the user will sometimes want to launch a cluster of Node.js processes to handle the load.

The cluster module allows easy creation of child processes that all share server ports.

> Please note that it’s ideal to use one process per container while using Docker containerization for deployment through microservices. Hence, cluster modules aren’t useful when using docker-ization.

#### How to handle control flow in NodeJS

While using callbacks or promises, the following libraries could be useful:

1. Async ([https://www.npmjs.com/package/async](https://www.npmjs.com/package/async))
2. Vasync( with better tracking of operation) [https://www.npmjs.com/package/vasync](https://www.npmjs.com/package/vasync)
3. Bluebird ( handle promises eg. Promise.all etc.) [https://www.npmjs.com/package/bluebird](https://www.npmjs.com/package/bluebird)

#### And Loops?

* Series loop: executing each step one by one in order

* Delayed loop: loop with a timeout

* Parallel loop: collecting all promises in a loop and execute in parallel

#### And what are some useful linting tools?

Linting tools analyze your code statically (without running it). They identify potential bugs or dangerous patterns. Patterns like the use of undeclared variables, or “case” statements inside a switch without a “break” statement.

Enabling strict mode on your codebase with ‘use strict’ can help your code fail fast if the JavaScript parser can identify a leaked global or similar bad behaviour.

Examples of linters are Javascript lint and JS lint.

#### Ok, how do we handle Logging?

Some commonly used npm packages are:

* Winston (https://www.npmjs.com/package/winston)
* Bunyan (https://www.npmjs.com/package/bunyan)

Possible logging format:

For distributed systems like microservices, you would like to explore distributed tracing using ZipKin etc.

> A note on NPM packages : You should use a package only if it solves a problem for you that you can’t solve yourself. Regularly perform npm audits to find critical issues with your npm dependencies.

#### Handling uncaught exceptions

By default, Node.js handles such exceptions by printing the stack trace to stderr and exiting with code 1, overriding any previously set process.exitCode

Note: Adding a handler for the 'uncaughtException' event overrides this default behaviour.

Alternatively, change the process.exitCode in the 'uncaughtException' handler which will result in the process exiting with the provided exit code. Otherwise, in the presence of such a handler, the process will exit with 0.

process.exit(0) – successful termination   
process.exit(1) – unsuccessful termination

#### Handling unhandled rejections

Promises are ubiquitous in Node.js code and sometimes chained to a very long list of functions that return promises and so on.

Not using a proper .catch(…) rejection handler will cause an unhandledRejection event to be emitted. If not properly caught and inspected, you may rob yourself of your only chance to detect and possibly fix the problem.

#### Extra Tip:

#### console.time() and console.timeEnd()

The console object has time() and timeEnd() methods that help with analyzing the performance of pieces of your code.

This is not a solution for production but it can be used when you don’t have better tools.

**Thank you very much for your time.**  
**[Sign Up For My Newsletter](https://forms.gle/SWVTMcdgnqdecD3t9)**

Other wonderful articles on similar topic(s) :

1. [https://microservices.io](https://microservices.io) ?
2. [https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/ddd-oriented-microservice](https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/ddd-oriented-microservice)


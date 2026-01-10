---
title: Matterhorn in Depth — Project Aspects Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-01T20:25:08.000Z'
originalURL: https://freecodecamp.org/news/matterhorn-in-depth-project-aspects-explained-3348f569f30a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1eutc7Qqi17u6Ll0E4wKoA.jpeg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Testing
  slug: testing
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Ethan Arrowood

  Recently, I published an article on my new project, Matterhorn ?, a Node.js API
  server boilerplate. It provides a set of opinionated configuration files and some
  basic example code. These help developers get up and running faster wi...'
---

By Ethan Arrowood

Recently, I published an [article](https://medium.freecodecamp.org/announcing-matterhorn-a-node-js-api-server-boilerplate-4994759f1bf6) on my new project, [Matterhorn ?,](https://github.com/Ethan-Arrowood/matterhorn) a Node.js API server boilerplate. It provides a set of opinionated configuration files and some basic example code. These help developers get up and running faster with Node.js and TypeScript.

Matterhorn is inspired by projects like Create React App and Gatsby CLI. The project's goal is to eliminate the barrier of entry required to use programming tools such as type systems, testing and linting frameworks, and even basic continuous integration.

This blog post will review each of the core aspects in Matterhorn. I will discuss details and the opinionated decision behind the framework of choice.

### Runtime & Type System

The core of this project is built with Node.js, a JavaScript runtime built on [Chrome’s V8 JavaScript engine](https://developers.google.com/v8/). It is recommended you use the latest stable version of Node.js to run this project. At the time of writing this post, it is **11.7.0**.

Node.js is driven by a non-blocking event loop which makes it a great choice for building scalable network applications. For more information on Node.js check out their [website](https://nodejs.org/en/).

Many Node.js projects are written in JavaScript. However, TypeScript, a type system for JavaScript, has witnessed a spike in attention at the end of 2018. Many developers are interested in learning TypeScript in 2019. Its adoption in open source JavaScript projects is increasing. The original purpose for Matterhorn was to jump start developers interested in building backend Node.js applications with TypeScript. As such, Matterhorn itself is written in TypeScript.

As a type system, TypeScript is very comprehensive. While it may have a steep learning curve at first, the benefits from using it are paramount. It helps you, the developer, write cleaner, less buggy code. And once you’re familiar with the ecosystem and configuration process, you’ll be writing new features faster than you would with native JavaScript. Editors such as [VSCode](https://code.visualstudio.com/) have TypeScript enabled by default. It provides an extensive set of developer tooling to further improve the developer experience.

### API Framework

While it is possible to write an HTTP API using just Node.js, if a developer wants to achieve ecosystem maintainability, security, and scalability, they should use an API framework. When it comes to Node.js API frameworks, there are many to chose from such as Express, Koa, and Hapi. But there is one framework faster and more resilient than all the rest: [Fastify](https://www.fastify.io/).

![Image](https://cdn-media-1.freecodecamp.org/images/Q8r068DOB8vOuyi-G1DtNEQWMUW-so1bn6xN)
_Fastify logo from [https://www.fastify.io](https://www.fastify.io" rel="noopener" target="_blank" title=")_

Fastify is a fast and low overhead web framework, for Node.js. It is inspired by Hapi and Express and operates on a plugin based architecture. It has a very healthy open source community, and over 90 public plugins from authentication to database bindings and everything in between. Additionally, Fastify maintains its own set of TypeScript bindings that are shipped with the module directly from NPM.

### Test Runner and Linter

Backing up your code with unit tests is a standard in today’s programming ecosystem. Matterhorn comes with Jest, a popular JavaScript test runner. It is configured to work with TypeScript and even contains some examples for testing your Fastify API. Take note of Fastify’s `inject` method; it is very useful for testing your routes behavior.

In addition to running tests, Jest is also configured to output code coverage documents. While code coverage is not the most important metric to consider when writing unit tests, it is valuable and can assist you in verifying you’re at least covering as much of your code base as possible.

In the open source community, code linters are a popular choice for enforcing a certain style of programming. They negate the need for stylistic code reviews. They can help developers catch errors in their code before they run it.

Matterhorn is equipped with ESLint, a popular choice for JavaScript linting. The project was originally shipped with TSLint. However, this was swapped out in favor of ESLint because TypeScript [officially announced](https://github.com/Microsoft/TypeScript/issues/29288) plans to directly support the ESLint project. The linter is configured to suit the project maintainers opinions. It can easily be reconfigured for your own stylistic guidelines.

### Continuous Integration

The final aspect of Matterhorn is the inclusion of a fully configured continuous integration pipeline. For many developers, especially those learning or just tinkering, this feature may not have much use. However, for those trying to develop a complete application and want the stability of enterprise development, this CI is for them.

The pipeline is built on Azure DevOps (previously named Visual Studio Team Services). Azure DevOps is free for public repositories, and the pipeline utilities are extensive. It can be configured programmatically ([Matterhorn](https://github.com/Ethan-Arrowood/matterhorn/blob/master/azure-pipelines.yml)) or through a visual editor (in a browser). You can check out Matterhorn’s CI pipeline [here](https://dev.azure.com/arrowoode/matterhorn/_build?definitionId=3). It automatically builds for pull request updates and any new commits on _master_.

### Conclusion

Thank you for taking the time to read about the various aspects of Matterhorn. A lot went into consideration when picking services and utility modules for this project. The project is open source, and there is plenty of room for improvement so if you’d like to contribute check it out below.

[**Ethan-Arrowood/matterhorn**](https://github.com/Ethan-Arrowood/matterhorn)  
[_An API boilerplate project built on Node.js and TypeScript ? - Ethan-Arrowood/matterhorng_ithub.com](https://github.com/Ethan-Arrowood/matterhorn)


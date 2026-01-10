---
title: How to get up and running with Fastify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T09:18:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-up-and-running-with-fastify-8b7e23781844
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pBOfD2cpJNoFUcVA0Kj-zg.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ethan Arrowood


  Fast and low overhead web framework, for Node.js


  Fastify version 1 was released on March 7th. This post will show you how to get
  it set up, and we’ll discuss some of the incredible features Fastify has to offer.
  No configuration i...'
---

By Ethan Arrowood

> Fast and low overhead web framework, for Node.js

Fastify version 1 was [released on March 7th](https://medium.com/@fastifyjs/fastify-goes-lts-with-1-0-0-911112c64752). This post will show you how to get it set up, and we’ll discuss some of the incredible features Fastify has to offer. No configuration is necessary — Fastify’s code base will run on Node versions 6.x, 8.x, and 9.x.

#### Ready?

Start with `npm i fastify` and then:

```
const fastify = require('fastify')()
```

```
fastify.get('/', (request, reply) => {  reply.send({ hello: 'world' })})
```

```
fastify.listen(3000, err => {  if (err) {    fastify.log.error(err)    process.exit(1)  }  fastify.log.info(    `server listening on ${fastify.server.address().port}`  )})
```

Now launch your server with: `node server`

? That’s it! You’ve got your first Fastify server up and running.

### What’s going on here?

```
const fastify = require('fastify')()
```

Line 1 is importing the Fastify framework into the JavaScript project and instantiating it. Your server instance is now stored in the `fastify` variable. You can pass additional options to this line like so:

```
const fastifyWithOptions = require('fastify')({  logger: {    prettyPrint: true   }})
```

Powered by the [Pino logger](https://getpino.io/#/), this option makes the console output easy to read and colorful. Check out the Pino documentation for more logger options, and the Fastify documentation for more Fastify instance options.

#### Next up: Routing

```
fastify.get('/', (request, reply) => {  reply.send({ hello: 'world' })})
```

Lines 3 through 5 define a very basic [Route](https://www.fastify.io/docs/latest/Routes/). Routes are the core to any Node.js backend server. Fastify supports two methods of defining routes: the shorthand method used above, or a general `.route` method as shown below.

```
fastify.route({  method: 'GET',  url: '/',  handler: function (request, reply) {    reply.send({ hello: 'world' })  }})
```

Both of these implementations do the exact same thing and have the same performance, so simply use whichever makes the most sense to you.

Route declaration has many more options available that aren’t shown here.

* Provide a [JSON Schema](http://json-schema.org/) for the request and response objects, which can increase throughput by 10–20%
* Define a `beforeHandler` method that is called just before the `handler` function. This is great for authentication, and I demonstrate how to use it in my [JWT Auth plugin](https://github.com/Ethan-Arrowood/fastify-jwt-authz) (more on Fastify plugins later).

#### Start your engines! 3…2…1…GO!

```
fastify.listen(3000, err => {  if (err) {    fastify.log.error(err)    process.exit(1)  }  fastify.log.info(    `server listening on ${fastify.server.address().port}`  )})
```

Finally, start the Fastify instance on localhost port 3000. This is the **last** step required to create your own Fastify instance. Internally this method will wait for `.ready()` (which is called after loading plugins). No new routes can be defined after calling the `.listen()` method.

### Whats next? Plugins!

One of the best features of Fastify is how easy it is to write and incorporate plugins into a server instance. To start, define a function:

```
function superPlugin (fastify, opts, next) {  fastify.decorate('superMethod', () => {    console.log(`Secret code: ${opts.secretCode}`)  })  next()}
```

Now using the `fastify-plugin` module, export your new plugin.

```
const fp = require('fastify-plugin')
```

```
module.exports = fp(superPlugin, {  fastify: '>=1.0.0',  name: 'super-plugin'})
```

Finally register your plugin onto your Fastify instance:

```
/* Inside the main server.js file */const superPlugin = require('super-plugin')
```

```
fastify.register(superPlugin, {  secretCode: 'JavaScript is awesome!'})
```

Now you can call the `superMethod` anywhere you have access to your Fastify instance.

```
/* server.js */
```

```
fastify.listen(3000, err => {  fastify.superMethod()})
```

Just to note: you can register plugins within other plugins, which locks that child plugin’s scope to the parent plugin only. This topic is too advanced for this article, so I won’t be covering it any more detail. You can read more about [Fastify plugins here](https://www.fastify.io/docs/latest/Plugins/). Check out the full example files in a [Github gist here](https://gist.github.com/Ethan-Arrowood/35e54c688e290e8e6a996ccc5c711c2f).

### Go forth and conquer

Fastify is fast. Really really fast ??

![Image](https://cdn-media-1.freecodecamp.org/images/7kA4wH6-mzlDXSub9GMnjkXyhrhPwml4x64i)
_[Fastify Benchmarks v1.1.x](https://www.fastify.io/benchmarks/" rel="noopener" target="_blank" title=")_

After this brief introduction, I encourage you to check out all that [Fastify has to offer](https://www.fastify.io/docs/latest/). If you enjoy open source programming, Fastify is a great project to [contribute to](https://github.com/fastify/fastify/issues) as well. There is also a great [ecosystem of plugins](https://www.fastify.io/ecosystem/) to check out and contribute to!

Keep up the great work ~ Ethan Arrowood

[**Ethan Arrowood ??? (@ArrowoodTech) | Twitter**](https://twitter.com/arrowoodtech)  
[**Th**e _latest Tweets from Ethan Arrowood ??? (@ArrowoodTech). always listening to music. probably contributing to open…twitte_r.com](https://twitter.com/arrowoodtech)  [**Ethan-Arrowood (Ethan Arrowood)**](https://github.com/Ethan-Arrowood)  
[_Ethan-Arrowood has 80 repositories available. Follow their code on GitHub._github.com](https://github.com/Ethan-Arrowood)


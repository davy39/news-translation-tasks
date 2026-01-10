---
title: How  to write a production-ready Node and Express app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T21:07:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-production-ready-node-and-express-app-f214f0b17d8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-1tLk1cFdmcEQfNhQ7LIUg.jpeg
tags:
- name: Express.js
  slug: expressjs
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Shailesh Shekhawat

  Project Structuring

  When I started building Node & Express applications, I didn’t know how important
  it was to structure your application. Express doesn’t come with strict rules or
  guidelines for maintaining the project structur...'
---

By Shailesh Shekhawat

### Project Structuring

When I started building Node & Express applications, I didn’t know how important it was to structure your application. Express doesn’t come with strict rules or guidelines for maintaining the project structure.

You are free to use any structure you want. When your codebase grows you end up having long `route` handlers. This makes your code hard to understand and it contains potential bugs.

If you’re working for a startup, most of the time you won’t have time to refractor your project or modularize it. You can end up with an endless loop of bug fixing and patching.

<iframe src="https://giphy.com/embed/6csVEPEmHWhWg" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

Over time, while working with both small teams and large teams, I realized what kind of structure can grow with your project and still be easy to maintain.

#### Model View Controller

The [MVC](https://en.wikipedia.org/wiki/Model–view–controller) pattern helps in rapid and parallel development. For example, one developer can work on the view, while another one can work on creating the business logic in the controller.

Let’s take a look at an example of a simple user CRUD application.

```
project/
  controllers/
    users.js
  util/
    plugin.js
  middlewares/
    auth.js
  models/
    user.js
  routes/
    user.js
    router.js
  public/
    js/
    css/
    img/
  views/
    users/
      index.jade
  tests/
    users/
      create-user-test.js 
      update-user-test.js
      get-user-test.js
  .gitignore
  app.js
  package.json
```

* **controllers:** Define your app route handlers and business logic
* **util:** Writes utility/helper functions here which can be used by any controllers. For example, you can write a function like `mergeTwoArrays(arr1, arr2)`.
* **middlewares:** You can write middlewares to interpret all incoming requests before moving to the route handler. For example,   
 `router.post('/login', auth, controller.login)` where `auth` is a middleware function defined in `middlewares/auth.js`.
* **models:** also a kind of middleware between your controller and the database. You can define a schema and do some validation before writing to the database. For example, you can use an ORM like [Mongoose](https://mongoosejs.com/) which comes with great features and methods to use in the schema itself
* **routes:** Define your app routes, with HTTP methods. For example, you can define everything related to the user.

```js
router.post('/users/create', controller.create)
router.put('/users/:userId', controller.update)
router.get('/users', controller.getAll)
```

* **public:** Store static images in`/img`, custom JavaScript files, and CSS `/css`
* **views:** Contains templates to be rendered by the server.
* **tests:** Here you can write all the unit tests or acceptance tests for the API server.
* **app.js:** Acts as the main file of the project where you initialize the app and other elements of the project.
* **package.json:** Takes care of the dependencies, the scripts to run with the `npm` command, and the version of your project.

### **Exceptions and Error Handling**

This is one of the most important aspects to think about when creating any project with any language. Let’s see how to handle errors and exceptions gracefully in an Express app.

#### **Using promises**

One of the advantages of using promises over callbacks is they can handle implicit or explicit exceptions/errors in asynchronous code blocks as well as for synchronous code defined in `.then()`, a promise callback

Just add `.catch(next)` at the end of the promise chain. For example:

```js
router.post('/create', (req, res, next) => {

   User.create(req.body)    // function to store user data in db
   .then(result => {
   
     // do something with result
    
     return result 
   })
   .then(user => res.json(user))
   .catch(next)
})
```

#### **Using try-catch**

Try-catch is a traditional way of catching exceptions in asynchronous code.

Let’s take a look at an example with a possibility of getting an exception:

```js
router.get('/search', (req, res) => {
 
  setImmediate(() => {
    const jsonStr = req.query.params
    try {
      const jsonObj = JSON.parse(jsonStr)
      
      res.send('Success')
    } catch (e) {
      res.status(400).send('Invalid JSON string')
    }
  })
})
```

#### **Avoid using synchronous code**

Synchronous code also known as blocking code, because it blocks the execution until they are executed.

So avoid using synchronous functions or methods that might take milliseconds or microseconds. For a high traffic website it will compound and may lead to high latency or response time of the API requests.

Don’t use them in production especially :)

Many Node.js modules come with both `.sync` and `.async` methods, so use async in production.

But, if you still want to use a synchronous API use `--trace-sync-io` command-line flag. It will print a warning and a stack trace whenever your application uses a synchronous API.

For more on the fundamentals of error handling, see:

* [Error Handling in Node.js](https://www.joyent.com/developers/node/design/errors)
* [Building Robust Node Applications: Error Handling](https://strongloop.com/strongblog/robust-node-applications-error-handling/) (StrongLoop blog)

> _What you should **not** do is to listen for the `uncaughtException` event, emitted when an exception bubbles all the way back to the event loop. Using it is generally [not preferred](https://nodejs.org/api/process.html#process_event_uncaughtexception)._

### **Logging properly**

Logging is essential for debugging and app activity. It is used mainly for development purposes. We use `console.log` and `console.error` but these are [synchronous functions](https://nodejs.org/api/console.html#console_console_1).

#### **For Debugging purposes**

You can use a module like [debug](https://www.npmjs.com/package/debug). This module enables you to use the DEBUG environment variable to control what debug messages are sent to `console.err()`, if any.

#### **For app activity**

One way is to write them to the database.

Check out [How I used mongoose plugins to do auditing of my application](https://medium.freecodecamp.org/how-to-log-a-node-js-api-in-an-express-js-app-with-mongoose-plugins-efe32717b59) .

Another way is to write to a file **OR** use a logging library like [Winston](https://www.npmjs.com/package/winston) or [Bunyan](https://www.npmjs.com/package/bunyan). For a detailed comparison of these two libraries, see the StrongLoop blog post [Comparing Winston and Bunyan Node.js Logging](https://strongloop.com/strongblog/compare-node-js-logging-winston-bunyan/).

### require(“./../../../../../../”) mess

There are different workarounds for this problem.

If you find any module getting popular and if it has logical independence from the application, you can convert it to private npm module and use it like any other module in package.json.

OR

```js
const path  = require('path');
const HOMEDIR  = path.join(__dirname,'..','..');
```

where `__dirname` is the built-in variable that names the directory that contains the current file, and `..` ,`..`is the requisite number of steps up the directory tree to reach the root of the project.

From there it is simply:

```js
const foo = require(path.join(HOMEDIR,'lib','foo'));
const bar = require(path.join(HOMEDIR,'lib','foo','bar'));
```

to load an arbitrary file within the project.

Let me know in the comment below if you have better ideas :)

### Set NODE_ENV to “production”

The **NODE_ENV** environment variable specifies the environment in which an application is running (usually, development or production). One of the simplest things you can do to improve performance is to set `**NODE_ENV**`to “production.”

Setting **NODE_ENV** to “**production**” makes Express:

* Cache view templates.
* Cache CSS files generated from CSS extensions.
* Generate less verbose error messages.

[Tests indicate](http://apmblog.dynatrace.com/2015/07/22/the-drastic-effects-of-omitting-node_env-in-your-express-js-applications/) that just doing this can improve app performance by a factor of three!

### **Using Process Manager**

For production, you should not simply use `node app.j` — if your app crashes, it will be offline until you restart it.

The most popular process managers for Node are:

* [StrongLoop Process Manager](http://strong-pm.io/)
* [PM2](https://github.com/Unitech/pm2)
* [Forever](https://www.npmjs.com/package/forever)

I personally use **PM2.**

For a feature-by-feature comparison of the three process managers, see [http://strong-pm.io/compare/](http://strong-pm.io/compare/). For a more detailed introduction to all three, see [Process managers for Express apps](https://expressjs.com/en/advanced/pm.html).

### Run your app in a cluster

In a multi-core system, you can increase the performance of a Node app by many times by launching a cluster of processes.

A cluster runs multiple instances of the app, ideally one instance on each CPU core. This distributes the load and tasks among the instances.

#### Using Node’s cluster module

Clustering is made possible with Node’s [cluster module](https://nodejs.org/dist/latest-v4.x/docs/api/cluster.html). This enables a master process to spawn worker processes. It distributes incoming connections among the workers.

However, rather than using this module directly, it’s far better to use one of the many tools out there that do it for you automatically. For example [node-pm](https://www.npmjs.com/package/node-pm) or [cluster-service](https://www.npmjs.com/package/cluster-service).

#### Using PM2

For pm2 you can use cluster directly through a command. For example,

```js
# Start 4 worker processes
pm2 start app.js -i 4

# Auto-detect number of available CPUs and start that many worker processes
pm2 start app.js -i max 
```

If you encounter any problems, feel free to _get in [touch](https://101node.io) or comment below._  
I would be happy to help :)



_Don’t hesitate to clap if you considered this a worthwhile read!_

References: [https://expressjs.com/en/advanced/best-practice-performance.html](https://expressjs.com/en/advanced/best-practice-performance.html)

_Originally published at [101node.io](https://101node.io/blog/how-to-write-production-ready-node-express-app/) on September 30, 2018._


---
title: What's Async Local Storage in Node.js v14?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-23T22:32:05.000Z'
originalURL: https://freecodecamp.org/news/async-local-storage-nodejs
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b7a740569d1a4ca2c15.jpg
tags:
- name: node js
  slug: node-js
seo_title: null
seo_desc: "By Mehul Mohan\nNode.js 14 is out now, and with that release, it brings\
  \ in Async Local Storage support. Now you might thing, \"Meh, okay. Local storage\
  \ has been around for awhile,\" but this time, it's different. \nFor starters, this\
  \ is the Node runtime ..."
---

By Mehul Mohan

Node.js 14 is out now, and with that release, it brings in Async Local Storage support. Now you might thing, "Meh, okay. Local storage has been around for awhile," but this time, it's different. 

For starters, this is the Node runtime we're talking about and not the browser. Thus, having a "localStorage" browser-like concept doesn't really make sense for Node. And the fact is, it is not the localStorage you're probably thinking of either. So what is it then?

## Introducing Async Local Storage – Storage for asynchronous tasks

Consider a web server like Apache running PHP for hosting a website. When PHP receives a request from a client, your web server makes sure to spin off a new thread. It lets that thread manage all the resources, local variables, function call stack, and so on for that particular request. Simple and easy. But a problem arises with JavaScript.

JavaScript is single threaded – that means you cannot have multiple threads of JS running together under a same parent process. But don't let that fool you – JS is as fast (even faster) as mature solutions like a Java backend in handling web server requests. 

How does that happen? Well, that's something for another article. But the important thing here is that **Node is single threaded**, so you do not have the benefits of **thread local storage**. Thread local storage is nothing but variables and functions local to a particular thread - in our case, for handling a particular user on the webpage.

## Why is single thread a problem?

Single thread is a problem in this case as Node keeps executing synchronous code in one go as long as it doesn't exhaust all synchronous operations in the event loop. Then it'll keep a check on events and callbacks and execute that code whenever necessary. 

In Node, a simple HTTP request is nothing but an event fired by the `http` library to the node to handle the request – hence it is asynchronous. 

Now let's say you want to associate some data with this asynchronous operation. How would you do that?

Well, you can create some sort of "global" variable and assign your special data to it. Then, when another request comes from the same user, you can use the global variable to read whatever you had stored earlier. 

But it would fail spectacularly when you have more than one request on hand as Node would not execute asynchronous code serially (of course, that's the definition of asynchronous!). 

Let's consider this dummy code (assume Node runtime):

```js
server.listen(1337).on('request', (req) => {
  // some synchronous operation (save state)
  // some asynchronous operation
  // some asynchronous operation
})
```

Consider this sequence of events:

1. User 1 hits the server on port 1337
2. Node starts running the synchronous operation code
3. While node was running that synchronous code, another User 2 hits the server.
4. Node would keep on executing the synchronous code, meanwhile the request to process the second HTTP request is waiting in the task queue.
5. When Node finishes the synchronous operation and comes to the asynchronous operation, it throws it off in the task queue and then starts processing the first task sitting in the task queue – the second HTTP request.
6. This time it's running that synchronous piece of code, but on the behalf of User 2's request. When that synchronous code for User 2 is done, it resumes the asynchronous execution of User 1, and so on.

Now what if you want to persist specific data with that specific user whenever the asynchronous code specific to them is being called? Here's when you use **AsyncStorage – storage for asynchronous flows in Node.**

Consider this example straight from the official docs:

```js
const http = require('http');
const { AsyncLocalStorage } = require('async_hooks');

const asyncLocalStorage = new AsyncLocalStorage();

function logWithId(msg) {
  const id = asyncLocalStorage.getStore();
  console.log(`${id !== undefined ? id : '-'}:`, msg);
}

let idSeq = 0;
http.createServer((req, res) => {
  asyncLocalStorage.run(idSeq++, () => {
    logWithId('start');
    // Imagine any chain of async operations here
    setImmediate(() => {
      logWithId('finish');
      res.end();
    });
  });
}).listen(8080);

http.get('http://localhost:8080');
http.get('http://localhost:8080');
// Prints:
//   0: start
//   1: start
//   0: finish
//   1: finish
```

This example is showing nothing but the "stickyness" of the `idSeq` with the respective request. You can imagine how express populates the `req.session` object with the correct user every time. In a similar fashion, this is a low level API using a lower level construct in Node called `async_hooks` which is still experimental, but is pretty cool to know!

## Performance

Before you try to roll this out in production, beware – this is not something I would really recommend anybody do if not absolutely needed. This is because it comes with a non-negligible performance hit on your application. This is primarily because the underlying API of `async_hooks` is still a WIP, but the situation should improve gradually. 

## Conclusion

That's basically it! A very simple brief introduction to what AsyncStorage is in Node 14 and what's the high level overall idea for it. If you want to learn all about new features in Node.js, check out this video:

%[https://www.youtube.com/watch?v=osFz798wIaQ]

Also, if you're an early adopter, try out [codedamn](https://codedamn.com) – a platform for developers to learn and connect. I've been rolling out some sweet features there for you to try! Stay tuned.

Peace!


---
title: How to use Web Workers to schedule consistent asynchronous tasks in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T19:46:24.000Z'
originalURL: https://freecodecamp.org/news/how-web-workers-can-help-with-consistent-asynchronous-tasks-in-javascript-cd6d728fa4ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tMKwMb5J5ETFpeOUYQyMKQ.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Danny Mcwaves

  With the continuous improvements being made to Javascript engines, and the ever-expanding
  list of deprecated and new API’s to the ECMASCRIPT specification, the quest for
  blazing fast web applications has never been more on the rise.

  ...'
---

By Danny Mcwaves

With the continuous improvements being made to Javascript engines, and the ever-expanding list of deprecated and new API’s to the ECMASCRIPT specification, the quest for blazing fast web applications has never been more on the rise.

#### What is the Javascript Engine?

The Javascript engine is a virtual machine. A `virtual machine` refers to the software-driven emulation of a given computer system. The basic job of a Javascript engine is to take the Javascript code that a developer writes and convert it to fast, optimized code that can be interpreted by a browser.

![Image](https://cdn-media-1.freecodecamp.org/images/FcPt2Ss0kkGpIIgxjRSIxcRA7vWL-NJBdTOm)
_To read more javascript engines, check out the [v8 javascript engine.](https://developers.google.com/v8/" rel="noopener" target="_blank" title=")_

Usually, this process runs on a single **thread** (more on threads later), with each statement of the developer’s code executed one at a time. The problem with single-threaded applications/architecture is that if any statement or block of statements takes a long time to complete, all subsequent statements hang up until that statement/block of statements finishes. This is known as `BLOCKING`. To avoid blocking, a program has to be multi-threaded.

#### Threading

A thread is an execution context, which is all the information a CPU needs to execute a stream of instructions.

Suppose you’re reading a book, and you want to take a break right now, but you want to be able to come back and resume reading from the exact point where you stopped. One way to achieve that is by jotting down the page number, line number, and word number. So your execution context for reading a book is these three numbers.

If you have a roommate, and she’s using the same technique, she can take the book while you’re not using it, and resume reading from where she stopped. Then you can take it back, and resume it from where you were.

Threads work in the same way. A CPU is giving you the illusion that it’s doing multiple computations at the same time. It does that by spending a bit of time on each computation. It can do that because it has an execution context for each computation.

Just like you can share a book with your friend, many tasks can share a CPU. This process is called multi-threading and it solves `BLOCKING`. To support multi-threading on the frontend, web workers were created.

![Image](https://cdn-media-1.freecodecamp.org/images/iSMf2nmgE9KBYdaUbT8fUvcwsYcR13DXyvwi)
_for more on threading, visit [here](https://en.wikipedia.org/wiki/Thread_(computing)" rel="noopener" target="_blank" title=")._

#### Web Workers

![Image](https://cdn-media-1.freecodecamp.org/images/-TZuLkY4dl1q3ngPdl3bAy-95GDku8xF105H)
_image credit to [html5schools](http://www.html5schools.com/html5-api-tutorials/webworkers-introduction//" rel="noopener" target="_blank" title=")._

> The simplest use of workers is for performing a computationally expensive task without interrupting the user interface. ([Source](https://en.wikipedia.org/wiki/Web_worker))

Web workers enable multi-threading on the front end by spawning new background threads and running scripts in isolation. As a result, scripts executed by workers need to be contained in separate files. Because web workers execute scripts in isolated threads, scripts do not interfere with the main thread and consequently do not interrupt the UI.

#### **Creating a Web Worker**

For didactic purposes, the excerpted script below is to be run in a separate thread.

```js
### fetch.js

self.addEventListener(‘message’,  e => {
    let url = e.data;
    
    fetch(url).then(res => {
        if (res.ok) {
            self.postMessage(res);
        } else {
            throw new Error(’error with server’);
        }
    }).catch(err => {
        self.postMessage(err.message);
    });
})
```

> The `[Worker()](https://www.w3.org/TR/workers/#dom-worker)` constructor call creates a worker and returns a `[Worker](https://www.w3.org/TR/workers/#worker)` object representing that worker, which is used to communicate with the worker.

```js
let worker = new Worker('fetch.js');
```

The constructor takes the name of the script as an argument. If the specified file exists, the worker spawns a new thread and then completely downloads and executes the script. If the file is unavailable, the worker fails silently.

#### **Using Web Workers**

Web workers communicate with the parent thread (the creator of the worker) using an [event](https://developer.mozilla.org/en-US/docs/Web/Events) model and messages. It uses `[MessagePort](http://www.w3.org/TR/webmessaging/#message-ports)` objects behind the scenes, and thus supports all the same features, such as sending structured data and transferring binary data.

To receive messages from a worker, use the `[onmessage](https://www.w3.org/TR/workers/#handler-worker-onmessage)` event handler on the `Worker` object.

```js
worker.onmessage = (e) => { // block statements }
```

You can also use the `addEventListener` method.

```js
worker.addEventListener('message', (e) => { // block statements })
```

To receive a message inside of the worker, the `onmessage` event handler method is used.

```js
onmessage = (e) => { // blocks of statements }
```

You can also use an `addEventListener` method as exemplified in `fetch.js`.

To send data to and from a worker, use the `[postMessage()](https://www.w3.org/TR/workers/#dom-worker-postmessage)` method. Structured data such as text and JSON can be sent over this communication channel. Read more on data types that are supported by `messagePort` over [here](https://www.html5rocks.com/en/tutorials/workers/basics/#toc-transferrables).

```js
worker.postMessage('some-lousy-data');
// in the parent thread

self.postMessage('some-resulting-data');
// in the worker thread.
```

This particular message-passing limitation is in place for a number of reasons: it keeps the child worker running securely (since it can’t, blatantly, affect a parent script) and it keeps the parent page thread-safe (having the DOM be thread safe would be a logistical nightmare for browser developers).

#### **Terminating a worker and handling errors**

If you need to immediately terminate a running worker from the main thread, you can do so by calling the worker’s terminate method:

```js
worker.terminate();
```

In the worker thread, workers may close themselves by calling their own close method:

```js
close();
```

The worker thread is killed immediately without an opportunity to complete its operations or clean up after itself.

Runtime errors can be handled by explicitly listening for an error event that might be fired by the `Worker` object.

```js
worker.addEventListener('error', (e) => { // block of statements })
```

#### **Web Worker Limitations**

1. All web worker scripts must be served from the same domain.
2. You cannot have direct access to the DOM and the global document.
3. The window object exposes limited API. For instance, `location` and `navigator` and `XMLHttpRequest` objects.
4. Restricted local access. Web workers do not work on static files. For instance `file://my/file/on/my/computer`.

If you are using a worker to handle a task that ultimately needs to update the main user interface, you will need to use the messaging system to pass the data between the worker and the main application. The main application is then responsible for updating the UI.

Similarly, if your worker needs access to data from the document, window, or parent objects, you will need to send it in the `postMessage()` call that is used to start the worker.

#### Conclusion

Creating web workers will spawn real OS-level threads that consume system resources. Just be conscious that this will affect the performance of the user’s whole computer, not just the web browser. As such, web workers should be used responsibly and closed when they are no longer in use to free up resources for other applications.

Using web workers can have a significant impact on the performance of web applications; and more responsive applications have a good effect on user experience.

For a more in-depth information on web workers such as importing scripts in workers and the scopes of web workers, please visit [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) or [WHATWG](https://www.w3.org/TR/workers/).

For a fully functional example of web workers, visit [here](https://github.com/DannyMcwaves/web-workers).


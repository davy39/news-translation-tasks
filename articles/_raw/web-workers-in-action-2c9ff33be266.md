---
title: 'Web workers in action: why they’re helpful, and how you should use them'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T20:39:37.000Z'
originalURL: https://freecodecamp.org/news/web-workers-in-action-2c9ff33be266
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f1HRu4YeZDn3PAS81QjuNg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webworker
  slug: webworker
seo_title: null
seo_desc: 'By The Hungry Brain

  Javascript is single threaded and multiple scripts can not execute at the same time.
  So if we execute any heavy computation task, then sometimes our page become unresponsive
  and the user can not do anything else until that executi...'
---

By The Hungry Brain

Javascript is single threaded and multiple scripts can not execute at the same time. So if we execute any heavy computation task, then sometimes our page become unresponsive and the user can not do anything else until that execution gets completed.

For example:

```js
average = (numbers) => {
    let startTime = new Date().getTime();
    let len = numbers,
        sum = 0,
        i;

    if (len === 0) {
        return 0;
    }

    for (i = 0; i < len; i++) {
        console.log('i :: ', i)
        sum += i;
    }

    let endTime = new Date().getTime();
    alert('Average - ', sum / len);
}

hello = () => {
    alert("Hello World !!");
}

/*
Paste the above code in browser dev tool console
and try to call average(10000) and hello one by one
*/
```

In the above example, if you call _average_ before the _hello_ method, then your page will become unresponsive and you won’t be able to click on _Hello_ until the execution of _average_ gets completed.

You can see that when _average_ is called with 10000 as input first, it took ~1.82 seconds. For that amount of time the page becomes unresponsive and you were not able to click on the hello button.

### Asynchronous Programming

Javascript gives the way to developers to write **async code**. By writing asynchronous code you can avoid this kind of issue with in your application as it enables your app UI to be responsive, by “scheduling” parts of the code to be executed a bit later in the event loop.

A good example of async programming is `XHR request`, in this we hit an API asynchronously and while waiting for the response, other code can be executed. But this is limited to certain use cases related to web APIs mostly.

Another way of writing async code is by using `setTimeout` method. In some cases, you can achieve good results in unblocking the UI from longer-running computations by using `setTimeout`. For example, by batching a complex computation in separate `setTimeout` calls.

For example:

```js
average = (numbers) => {
    let startTime = new Date().getTime();
    var len = numbers,
        sum = 0,
        i;

    if (len === 0) {
        return 0;
    }

    let calculateSumAsync = (i) => {
        if (i < len) {
            // Put the next function call on the event loop.
            setTimeout(() => {
                sum += i;
                calculateSumAsync(i + 1);
            }, 0);
        } else {
            // The end of the array is reached so we're invoking the alert.
            let endTime = new Date().getTime();
            alert('Average - ', sum / len);
        }
    };

    calculateSumAsync(0);
};

hello = () => {
    alert('Hello World !!')
};
```

In this example, you can see that after you click on the _Calculate Average_ button, you can still click on the _Hello_ button (which in turn shows an alert message). This way of programming is surely non-blocking but takes too much time, and is not feasible in real world applications.

Here, for the same input 10000, it took ~60 seconds, which is very inefficient.

**So, how do we solve these kinds of issues efficiently?**

The answer is **Web Workers.**

### What are web workers ?

Web workers in Javascript are a great way to execute some task which is very laborious and time taking into a thread separate from the main thread. They run in background and perform tasks without interfering with the user interface.

Web Workers are not the part of JavaScript, they’re a browser feature which can be accessed through JavaScript.

Web workers are created by a constructor function **Worker()** which runs a named JS file.

```js
// create a dedicated web worker
const myWorker = new Worker('worker.js');
```

If the specified file exists then it will be downloaded asynchronously and if not then worker will fail silently, so your application will still work in case of 404.

We will learn more about creation and working of web workers in the next section.

Worker thread has its own context and therefore you can only access selected features inside a worker thread like - web sockets, indexed DB.

There are some **restrictions** with web workers -

1. You can't directly manipulate the DOM from inside a worker.
2. You can not use some default methods and properties of the window object since window object is not available inside a worker thread.
3. The context inside the worker thread can be accessed via **_DedicatedWorkerGlobalScope or SharedWorkerGlobalScope_** depending upon the usage.

### Features of Web Workers

There are two types of web workers -

1. **Dedicated web worker** - A dedicated worker is only accessible by the script that called it.
2. **Shared web worker** - A shared worker is accessible by multiple scripts — even if they are being accessed by different windows, iframes or even workers.

Let us discuss more about those two types of web workers -

#### Creation of a web worker

Creation is pretty much same for both a Dedicated and Shared web worker.

**Dedicated web worker**

* Creating a new worker is simple, just call the Worker constructor and pass the path of the script you want to execute as worker.

```js
// create a dedicated web worker
const myWorker = new Worker('worker.js');
```

**Shared web worker :**

* Creating a new shared worker is pretty much the same as that of dedicated worker, but with a different constructor name.

```js
// creating a shared web worker
const mySharedWorker = new SharedWorker('worker.js');
```

#### Communication between main and worker thread

Communication between main thread and worker thread happens via _postMessage_ method and _onmessage_ event handler.

**Dedicated web worker**  
In case of a dedicated web worker, communication system is simple. You just need to use postMessage method whenever you want to send message to the worker.

```js
(() => {
  // new worker
  let myWorker = new Worker('worker.js');

  // event handler to recieve message from worker
  myWorker.onmessage = (e) => {
    document.getElementById('time').innerHTML = `${e.data.time} seconds`;
  };

  let average = (numbers) => {
    // sending message to web worker with an argument
    myWorker.postMessage(numbers);
  }

  average(1000);
})();
```

And inside a web worker you can respond when the message is received by writing an event handler block like this:

```js
onmessage = (e) => {
    let numbers = e.data;
    let startTime = new Date().getTime();
    let len = numbers,
        sum = 0,
        i;

    if (len === 0) {
        return 0;
    }

    for (i = 0; i < len; i++) {
        sum += i;
    }

    let endTime = new Date().getTime();
    postMessage({average: sum / len, time: ((endTime - startTime) / 1000)})
};
```

The `onmessage` handler allows to run some code whenever a message is received. 

Here we are calculating average of numbers and then use `postMessage()` again, to post the result back to the main thread.

As you can see on _<ins>line 6 in main.js</ins>_ we have used onmessage event on the worker instance. So whenever worker thread use postMessage, onmessage in the main thread gets triggered.

* **Shared web worker**  
In case of a shared web worker, communication system is little different. As one worker is shared between multiple scripts, we need to communicate via the port object of worker instance. This is done implicitly in case of dedicated workers. You need to use postMessage method whenever you want to send message to the worker.

```js
(() => {
  // new worker
  let myWorker = new Worker('worker.js');

  // event handler to recieve message from worker
  myWorker.onmessage = (e) => {
    document.getElementById('time').innerHTML = `${e.data.time} seconds`;
  };

  let average = (numbers) => {
    // sending message to web worker with an argument
    myWorker.postMessage(numbers);
  }

  average(1000);
```

Inside a web worker (_main-shared-worker.js_) it is a little complex. First, we use an `onconnect` handler to fire code when a connection to the port happens (_line 2_).  
We use the `ports` attribute of this event object to grab the port and store it in a variable (_line 4_).  
Next, we add a `message` handler on the port to do the calculation and return the result to the main thread (_line 7 and line 25_) like this:

```js
onmessage = (e) => {
    let numbers = e.data;
    let startTime = new Date().getTime();
    let len = numbers,
        sum = 0,
        i;

    if (len === 0) {
        return 0;
    }

    for (i = 0; i < len; i++) {
        sum += i;
    }

    let endTime = new Date().getTime();
    postMessage({average: sum / len, time: ((endTime - startTime) / 1000)})
};
```

#### Termination of a web worker

If you need to immediately terminate a running worker from the main thread, you can do so by calling the worker’s _terminate_ method:

```js
// terminating a web worker instance
myWorker.terminate();
```

The worker thread is killed immediately without an opportunity to complete its operations.

### Spawning of web worker

Workers may spawn more workers if they wish. But they must be hosted within the same origin as the parent page.

### Importing Scripts

Worker threads have access to a global function, `importScripts()`, which lets them import scripts.

```js
importScripts();                         /* imports nothing */
importScripts('foo.js');                 /* imports just "foo.js" */
importScripts('foo.js', 'bar.js');       /* imports two scripts */
importScripts('//example.com/hello.js'); /* You can import scripts from other origins */
```

### Working Demo

We have discussed some of the approaches above to achieve async programming so that our UI doesn’t get blocked due to any heavy computational task. But there are some limitations to those approaches. So we can use web workers to solve these kind of problems efficiently.

> _Click [here](https://bhushangoel.github.io/webworker-demo-1/) to run this live demo._

Here, you will see 3 sections:

1. **Blocking Code**:  
When you click on _calculate average_, the loader does not display and after some time you see the final result and time taken. This is because as soon as the _average method_ gets called, I have triggered the _showLoader_ method also. But since JS is single threaded, it won’t execute showLoader until the execution of average gets completed. So, you won’t be able to see the loader in this case ever.
2. **Async Code**:  
In this I tried to achieve the same functionality by using the setTimeout method and putting every function execution into an event loop. You will see the loader in this case, but the response takes time as compared to the method defined above.
3. **Web worker**:  
This is an example of using a web worker. In this you will see the loader as soon as you click on calculate average and you will get a response in the same time as of method 1, for the same number.

You can access the source code for the same [here](https://github.com/bhushangoel/webworker-demo-1/tree/master).

### Advanced concepts

There are some advanced concepts related to web workers. We won’t be discussing them in detail, but its good to know about them.

1. **Content Security Policy —**   
Web workers have their own execution context independent of the document that created them and because of this reason they are not governed by the Content Security Policy of the parent thread/worker.   
The exception to this is if the worker script's origin is a globally unique identifier (for example, if its URL has a scheme of data or blob). In this case, the worker inherit the content security policy of the document or worker that created it.
2. **Transferring data to and from workers** —   
Data passed between main and worker thread is **copied** and not shared. Objects are serialized as they're handed to the worker, and subsequently, de-serialized on the other end. The page and worker **do not share the same instance**, so the end result is that **a duplicate** is created on each end.   
Browsers implemented [**<ins>Structured Cloning</ins>**](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) algorithm to achieve this.
3. **Embedded workers —**   
You can also embed the code of worker inside a web page (html). For this you need to add a script tag without a src attribute and assign a non-executable MIME type to it, like this:

```js
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>embedded worker</title>
  <!--script tag with un-identified MIME and w/o src attr -->
  <script type="text/js-worker">
    // This script WON'T be parsed by JS engines because its MIME type is text/js-worker.
    var myVar = 'Hello World!';
    
    // worker block
    function onmessage(e) {
      // worker code
    }
  </script>
</head>
<body></body>
</html>
```

There are a lot of use cases to use web workers in our application. I have just discussed a small scenario. Hope this helps you understand the concept of web workers.

#### [Links]

Github Repo : [https://github.com/bhushangoel/webworker-demo-1](https://github.com/bhushangoel/webworker-demo-1) Web worker in action : [https://bhushangoel.github.io/webworker-demo-1/](https://bhushangoel.github.io/webworker-demo-1/)JS demo showcase : [https://bhushangoel.github.io/](https://bhushangoel.github.io/)

Thank you for reading.

Happy Learning :)

_Originally published at [www.thehungrybrain.com](https://www.thehungrybrain.com/home/web-workers)._


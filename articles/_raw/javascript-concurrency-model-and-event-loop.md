---
title: JavaScript Concurrency Model and Event Loop
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-13T21:46:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-concurrency-model-and-event-loop
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9de6740569d1a4ca3a44.jpg
tags:
- name: concurrency
  slug: concurrency
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: Javascript runtime is single threaded which means that it can execute one
  piece of code at a time. In order to understand the concurrency model and the event
  loop in Javascript we have to first get to know some common terms that are associated
  with i...
---

Javascript runtime is single threaded which means that it can execute one piece of code at a time. In order to understand the concurrency model and the event loop in Javascript we have to first get to know some common terms that are associated with it. 

## The call stack

First let’s learn about what a call stack is.

A call stack is a simple data structure that records where in the code we are currently. So if we step into a function that is a function invocation it is pushed to the call stack. When we return from a function it is popped out of the stack.

Let’s look at a code example to understand the call stack:

```javascript
function multiply(x,y) {
   return x * y;
}

function squared(n) {
     return multiply(n,n)
  }

function printSquare(n) {
   return squared(n)
}

let numberSquared = printSquare(5);
console.log(numberSquared);
```

First when the code executes the runtime will read through each of the function definitions. But when it reaches the line where the first function **printSquare(5)** is invoked it will push this function into the call stack. 

Next, this function will execute. Before returning it will encounter another function, **squared(n)**, so it will suspend its current operation and push this function on top of the existing function. 

It executes the function (in this case the squared function) and finally it encounters another function **multiply(n,n)**. Then it suspends its current executions and pushes this function into the call stack. The function multiply executes and it returns with the multiplied value. 

Finally the squared function returns and is popped off the stack and then the same goes with printSquare. The final squared value is allocated to the numberSquared variable. 

We encounter again a function invocation (in this case it’s a console.log() statement) so the runtime pushes this to the stack. This executes it thus printing the squared number on the console. 

Note that the first function that gets pushed into the stack before any of the above code runs is the main function. In the runtime this is denoted as an ‘anonymous function’.

So to summarize: whenever a function is invoked it is pushed into the call stack where it executes. Finally when the function is done with its execution and is returning either implicitly or explicitly it will be popped off the stack. 

The call stack just records at what point in time which function was executing. And it keeps track of which function is currently executing.

## The browser

Now we know from this that Javascript can execute one thing at a time but that’s not the case with the Browser. The Browser has its own set of APIs like setTimeout and XMLHttpRequests which are not specified in the Javascript runtime. 

In fact if you look through the source code of V8, the popular Javascript runtime that powers browsers like Google Chrome, you won’t find any definitions for it. That's because these special web API’s exist in the browser environment not inside the javascript environment. So you can say that these APIs introduce concurrency into the mix. 

Let’s look at a diagram to understand the whole picture.

![Concurrency and Event Loop Model](https://i.imgur.com/rnQEY7o.png)

Some more terms are introduced here, so let's go through them:

**Heap**: It’s mostly the place where objects are allocated.

**Callback Queue**: It’s a data structure that stores all the callbacks. Since it’s a queue, the elements are processed based on FIFO which is First in First Out.

**Event Loop**: This is where all these things come together. The event loop simply checks the call stack, and if it is empty (which means there are no functions in the stack) it takes the oldest callback from the callback queue and pushes it into the call stack which eventually executes the callback.

Let’s understand this with a code example:

```javascript
console.log('hi');

setTimeout(function() {
     console.log('freecodeCamp')
},5000);

console.log('JS')
```

When the first line executes it’s a console.log(). This is a function invocation which means that this function is pushed into the call stack where it executes printing ‘hi’ to the console. Finally it’s returned and is popped off the stack. 

Then when the runtime goes to execute setTimeout() it knows that this is a web API. Therefore it gives it off to the browser to handle its execution. The browser starts the timer and then JS runtime pops the setTimeout() out of the stack. It encounters another console.log() invocation and so it pushes this into the call stack, the message ‘JS’ is logged into the console, and then it’s finally returned. Then the last console.log() is popped off the stack. Now the call stack is empty. 

Meanwhile while all of this was going on the timer finishes. When 5 seconds have elapsed the browser goes ahead and pushes the callback function into the callback queue. 

Next the event loop checks if the call stack is free or not. Since it is free it takes the callback function and pushes it again back to the call stack which executes the code inside it. 

Again inside the code there is a console.log() invocation so this function goes to the top of the stack executes which logs ‘freecodecamp’ into the console and finally it returns. This means it gets popped off the stack and finally the callback gets popped off the stack and we are done.

To visualize this better try this tool by Phillip Roberts: [Loupe Event Loop Visualizer](http://latentflip.com/loupe/?code=!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D)


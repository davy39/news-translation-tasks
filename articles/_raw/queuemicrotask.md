---
title: An Introduction to JavaScript's queueMicrotask
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-08T18:11:45.000Z'
originalURL: https://freecodecamp.org/news/queuemicrotask
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca077740569d1a4ca48d3.jpg
tags:
- name: api
  slug: api
- name: asynchronous programming
  slug: asynchronous-programming
- name: Browsers
  slug: browsers
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Ujjwal Gupta\nIntroduction\nqueueMicrotask is a new browser API which\
  \ can be used to convert your synchronous code into async:\nqueueMicrotask(() =>\
  \ {\n    console.log('hey i am executed asychronously by queueMicrotask');\n});\n\
  \nIt's similar to what we ..."
---

By Ujjwal Gupta

## Introduction

**queueMicrotask** is a new browser API which can be used to convert your synchronous code into async:

```javascript
queueMicrotask(() => {
    console.log('hey i am executed asychronously by queueMicrotask');
});
```

It's similar to what we were doing using setTimeout:

```javascript
setTimeout(() => {
    console.log('hey i am executed asychronously by setTimeout');
}, 0);
```

So what's the use of **queueMicrotask** when we already have **setTimeout** ?

> **queueMicrotask** adds the function (task) into a queue and each function is executed one by one (FIFO) after the current task has completed its work and when there is no other code waiting to be run before control of the execution context is returned to the browser's event loop.

Basically the tasks of **queueMicrotask** are executed just after current callstack is empty before passing the execution to the event loop.

> In the case of **setTimeout**, each task is executed from the event queue, after control is given to the event loop.

So if we execute **setTimeout** first and then **queueMicrotask**, which will be called first?  Execute the below code and check out yourself:

```javascript
setTimeout(() => {
    console.log('hey i am executed asychronously by setTimeout');
},0);

queueMicrotask(() => {
    console.log('hey i am executed asychronously by queueMicrotask');
}); 
```

Node.js does the same thing with "process.nextTick".

## When to Use **It**

There is no rule for when to use **queueMicrotask,** but it can be used cleverly to run a piece of code without stopping the current execution.

For example, let's say we have an array where we are maintaining list of values. After every value is inserted, we sort the array so that searching for values is faster.

```
var arr=[];

function add(value){
  arr.push(value);
  arr.sort();
}
```

However, searching for an element is done whenever someone uses a search input box. This means the event handler will be called after control is transferred to the event loop, so sorting the data blocks the execution of other important synchronous code.

Here's how we can use **queueMicrotask** to improve our code:

```javascript
var arr = [];

function add(value) {
  arr.push(value);
  queueMicrotask(() => {
    arr.sort();
  })
}
```

## References

* [https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/queueMicrotask](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/queueMicrotask)


---
title: The differences between JavaScript’s asynchronous API timers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-10T16:28:59.000Z'
originalURL: https://freecodecamp.org/news/the-differences-between-javascripts-asynchronous-api-timers-d916e0596716
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iF8uCp-Dx8BfuCSgkbHvnQ.jpeg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Rajika Imal

  JavaScript is a single-threaded language, which makes use of asynchronous constructs
  to handle tasks concurrently. Interestingly, it handles concurrent tasks efficiently
  with a different approach compared to traditional languages likes...'
---

By Rajika Imal

JavaScript is a single-threaded language, which makes use of asynchronous constructs to handle tasks concurrently. Interestingly, it handles concurrent tasks efficiently with a different approach compared to traditional languages likes Java and C#.

#### Event loop

Whether it’s a browser environment or Node.js, JavaScript is asynchronous due to the fact that it’s using the event loop. In the Node environment, it’s implemented using a libuv library. Originally libuv was developed as a wrapper to libev. In Node version 0.9.0, the dependency of libev was removed.

#### Phases in event loops

```
   ┌───────────────────────────┐┌─>│           timers          ││  └─────────────┬─────────────┘│  ┌─────────────┴─────────────┐│  │     pending callbacks     ││  └─────────────┬─────────────┘│  ┌─────────────┴─────────────┐│  │       idle, prepare       ││  └─────────────┬─────────────┘      ┌───────────────┐│  ┌─────────────┴─────────────┐      │   incoming:   ││  │           poll            │<─────┤  connections, ││  └─────────────┬─────────────┘      │   data, etc.  ││  ┌─────────────┴─────────────┐      └───────────────┘│  │           check           ││  └─────────────┬─────────────┘│  ┌─────────────┴─────────────┐└──┤      close callbacks      │   └───────────────────────────┘
```

> source: [https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)

Event loops can be divided into a few phases as illustrated above. Each phase will be executed in each iteration. One such iteration is called a tick in the event loop. Every phase has a first in first out queue (FIFO) which will register different tasks. To understand how setTimeout, setImmediate and nextTick work, we'll go through the relevant important phases.

#### Timers phase

Callbacks registered by _setTimeout_ and _setInterval_ will be executed in this phase. It’s important to notice that callbacks will not be executed immediately but rather after a certain threshold of the time expiring.

#### Check phase

If the poll phase which handles I/O callbacks becomes idle or the maximum number of executions exceed it will move to check phase, where it’ll execute callbacks registered by _setImmediate_.

#### Microtask queue and macrotask queue

These two queues are important to understand the order of tasks executed through different APIs. Macrotasks are executed in each of the phases shown in the diagram above.

_setImmediate_ is part of the macrotask queue. Microtasks will be executed until the queue is empty before moving on to the next iteration or the tick of the event loop.

process.nextTick callbacks will be registered in the microtask queue and they will be executed until it is empty. Therefore, having recursive calls in the process.nextTick can starve the event loop, prevent it from going to the next tick. Macro tasks won’t starve the event loop as it will move on the next tick once the maximum number of executions is reached.

Let’s look at a few examples to see how each of the APIs behave in the real world to get a better understanding.

In the rest of the examples shown in this article, Node.js will be used as the execution environment.

#### setTimeout vs setImmediate

Notice that the calls aren’t within an I/O cycle. Because of this fact, the execution will depend on the performance of the CPU. Therefore logs will be printed out randomly in this case.

In this example, they are within an I/O cycle. _setImmediate_ callback will get executed every time since the macrotask queue (check phase) will be executed following the tick. setTimeout will be called in the timers phase once the threshold gets exceeded.

#### setImmediate vs process.nextTick

_nextTick_ is part of the microtask queue, and it will get executed before event loop moves on to the next tick. Following nextTick in the next tick setImmediate will fire off its callback in the macrotask queue in the check phase.

nextTick executes the recursive function which will get executed until it enters the base condition (if num > 5). Only after the execution of nextTick, setImmediate will fire its callback. Continuous recursive behavior is due to nextTick being a part of the microtask queue which doesn’t allow the event loop to proceed to the next tick.

#### setImmediate vs setTimeout vs process.nextTick

As expected nextTick gets called first, followed by setImmediate and setTimeout. It’s important to note that the functions are called in an I/O cycle. If they are not within an I/O cycle output will be different and will be dependant on the process performance.

> Follow up resources

[**Concurrency model and Event Loop**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)  
[_JavaScript has a concurrency model based on an "event loop". This model is quite different from models in other…_developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)[**The Node.js Event Loop, Timers, and process.nextTick() | Node.js**](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)  
[_Edit on GitHub The event loop is what allows Node.js to perform non-blocking I/O operations - despite the fact that…_nodejs.org](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)[**Tasks, microtasks, queues and schedules**](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)  
[_When I told my colleague Matt Gaunt I was thinking of writing a piece on microtask queueing and execution within the…_jakearchibald.com](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)


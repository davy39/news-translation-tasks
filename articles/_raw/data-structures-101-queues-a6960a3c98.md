---
title: 'Data Structures 101: Queues'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:18:47.000Z'
originalURL: https://freecodecamp.org/news/data-structures-101-queues-a6960a3c98
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EhimF7dL04AkpisbKM2LJg.jpeg
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Turney

  Starting with a Queue

  When you go the Shake Shack, most often there are other people on the line waiting
  to be served. The customers are arranged in a particular order, First In, First
  Out. Other real-life scenarios are toll booths or...'
---

By Kevin Turney

### Starting with a Queue

When you go the Shake Shack, most often there are other people on the line waiting to be served. The customers are arranged in a particular order, First In, First Out. Other real-life scenarios are toll booths or wedding chapels in Vegas. This method of ordering data for service, in our case, people, is what Queues are all about.

Queues are very similar to Stacks regarding interface, with the difference being Stacks process data Last In, First Out.

So we have differences in the order of processing — why? We need a different method of processing data that preserves the order. For example, suppose we have a stream of data in the node. As it comes in, we need to do something to it and then write it to a file to read later. For simplicity sake, let’s say we need to capitalize every letter streamed. What would happen if we used a LIFO, or stack data structure?

![Image](https://cdn-media-1.freecodecamp.org/images/YqhoftqFVXVQ0XQ22oh6Ds0IQgObVjsd1eNQ)

The main reason is queues process data fairly and preserve the order of the collection. This also happens when we iterate over items with a for or while loop, forEach(), or map() method. Each item in the array gets processed in the order it was inserted, from index 0 to index.length — 1.

**In Queues, items are processed in the order they are inserted.**

### Implementation

A simple implementation using arrays is with the method shift() to remove from the front and unshift() to add the front.

Like my [post on Stacks](https://medium.freecodecamp.org/data-structures-101-stacks-696b3282980), we will describe the API for a Queue. Then we’ll start with an implementation using the pseudoclassical method and a base object.

When an item is inserted into a queue, it’s called **enqueued**. When an item is removed, it is **dequeued**. Other methods include peek, contains, until, and count.

![Image](https://cdn-media-1.freecodecamp.org/images/aQcmAeS9hN4ormkWg3L00rJZEfk3mmJdx6Pk)

To track our items, we use the head for the front of the queue and tail for the back. The difference between the two gives the queue size.

Our Storage mechanism is as follows:

```
// _underscores indicate "private variables" to other engineers
```

```
const Queue = function(capacity) {  this.storage = {};  this.capacity = capacity || Infinity;  this._head = 0;  this._tail = 0}
```

```
let q = new Queue();q; // Queue { storage: {}, capacity: Infinity, _head: 0, _tail: 0 }
```

To Enqueue:

```
Queue.prototype.enqueue = function(value) {  if (this.count() < capacity) {    this.storage[this._tail++] = value;    return this.count();  }  return "Max capacity reached, please remove a value before enqueuing"}
```

To Dequeue:

```
Queue.prototype.dequeue = function() {    if (this.count() === 0) {      return "Nothing in the queue";    }    else {      let element = this.storage[this._head];      delete this.storage[this._head];      if (this._head < this._tail) {        this._head++;      }      return element;    }}
```

The remaining API:

```
Queue.prototype.peek = function() {  return this.storage[this._head]}
```

```
Queue.prototype.contains = function(value) {  for (let i = this._head; i < this._tail; i++) {    if (this.storage[i] === value) {      return true;    }  }  return false;}
```

```
Queue.prototype.until = function(value) {  for (let i = this._head; i < this._tail; i++) {    if (this.storage[i] === value){      return i - this._head + 1;    }  }  return null;}
```

```
Queue.prototype.count = function() {  return this._tail - this._head;}
```

```
let q = new Queue();q.enqueue('ww');q.enqueue('aa');q; // Queue {capacity: Infinity, storage: { 0: 'ww', 1: 'aa' }, _head: 0, _tail: 2 }q.enqueue('bb');q.peek(); // 'ww'q.dequeue(); // 'ww'q; //Queue {capacity: Infinity, storage: { 1: 'aa', 2: 'bb' }, _head: 1, _tail: 3 }q.contains('bb'); // trueq; //Queue {capacity: Infinity,storage: { 1: 'aa', 2: 'bb' }, _head: 1, _tail: 3 }q.until('bb'); // 2q.count(); // 2
```

Under the hood, we learned in [my post on Stacks](https://medium.freecodecamp.org/data-structures-101-stacks-696b3282980), that any time a function is called it creates an execution context and is allocated a stack frame on the execution stack. Is there anything similar in JavaSrcipt that utilizes Queues? Yes: the event loop.

### The Event Loop and Queues

Before we get to what the event loop is, we need to understand a few terms first.

**Concurrency** — In computer science, parts of a computer program can run out of order without affecting the outcome. In the context of JavaScript, it refers to the event loop’s ability to execute callback functions after completing other work.

**Runtime** — the time in which a program is running.

**Non-blocking vs. blocking** — blocking is when the execution of a JavaScript program must wait until another part of the program is completed, sometimes non-JavaScript operations. Essentially, synchronous, do one thing at a time.p

Non-blocking operations, on the other hand, work asynchronously. They employ callbacks that allow operations to continue, and when the work is completed, the callback associated with that particular function or event fires.

**System kernel** — is the central part of an Operating System. It manages the operations of the computer and memory and hardware, specifically the CPU. To be more efficient, the event loop offloads certain operations to the kernel.

#### Now to the event loop.

JavaScript is a single threaded language. This means the flow of execution goes in order, and it does one thing at a time. Node.js is built off of the [Chrome V8 engine](https://developers.google.com/v8/intro), and it employs a continually spinning loop waiting for incoming connections.

When an asynchronous function executes, it enters the event loop. A message associated with this function enters the **message queue** in the order it was received. Other functions already in the loop are executed or are processing. When the message is dequeued, the callback function executes and is placed on the execution stack.

All the while, the event loop keeps spinning, waiting for more connections. This is how queues are used behind the scenes in JavaScript.

### Time complexity

Queue operations are very efficient. Enqueue, Dequeue, Peek, and Count are the fastest working in constant time. Contains and Until take longer as our input size increases operating in linear time O(N);

Enqueue O(1)  
Dequeue O(1)  
Peek O(1)  
Count O(1)  
Contains O(N)  
Until O(N)

Thanks for reading. If you are unfamiliar with stacks, please check out my [other article](https://medium.freecodecamp.org/data-structures-101-stacks-696b3282980) on them for more context.


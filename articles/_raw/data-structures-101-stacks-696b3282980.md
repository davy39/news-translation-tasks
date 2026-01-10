---
title: 'Data Structures 101: Stacks'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:23:39.000Z'
originalURL: https://freecodecamp.org/news/data-structures-101-stacks-696b3282980
coverImage: https://cdn-media-1.freecodecamp.org/images/0*NEPg2w2qm-aTdb1a
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

  A Stack is the most elemental of the data structures in computer science.

  Data structures are a way to organize our information. They provide a means of storing
  different types of data in unique ways and methods to access either all o...'
---

By Kevin Turney

### A Stack is the most elemental of the data structures in computer science.

Data structures are a way to organize our information. They provide a means of storing different types of data in unique ways and methods to access either all or distinct parts of it.

### Starting with a Stack

Have you ever used a stack? Of course! Your email is a form of a stack, new mail comes in and is placed on top. When you finish reading the latest email, you remove it from the top. In development, whenever you call a function, that is placed on a stack in the engine that processes the code.

How we use stacks is a **Last In, First Out** processing system.

An analogy would be a recipe. Suppose we want to make a bowl of spaghetti. What are the steps?

1. Get a pot
2. Add water
3. Bring water to a boil
4. Add salt to the water
5. Add spaghetti
6. Cook spaghetti till tender

Now when the spaghetti is done, we have to get back to where we started, a clean kitchen. We need a method to organize our task list and help us get back to where we left off.

JavaScript is a single threaded language. In the simplest terms, it means it can only do one thing at a time, just like us. So how does our language of choice handle this in an organized way, Stacks?

![Image](https://cdn-media-1.freecodecamp.org/images/K4D9kYqy74hwfMaEvoj6TMVAioUxmyUY5vfG)

As you can see, the stack is a clean way of handling tasks, removing them, and eventually getting back to the beginning.

Stacks come with a cost: memory. For every item we place on the stack, we allocate a stack frame to it. Think of an array index. Each index is allocated space to hold something. If we keep adding and adding to a stack, we hold the possibility of running out of space, like a parking lot that is full. When that happens, we have an overflow, hence, the term “stack overflow”. This can lead to crashes and stuck processes.

![Image](https://cdn-media-1.freecodecamp.org/images/2oeYQbArqT5t5TfIjqkI5i86QjaFUynSqyY5)

How do we reclaim memory? When an item is removed from the stack, JavaScript uses “garbage collection” to free up resources and reclaim the storage space previously used.

### Implementation

First, how do we store the data? What can we use in JavaScript to hold data? We can use native objects like arrays, which we are familiar with and use built-in methods, push and pop. Ok, I guess we’re done, see you later…

Nah, to understand how a stack works under the hood, we use the base Object form.

We need a constructor to establish the storage mechanism and properties upon its invocation.

```
const Stack = function(capacity) {  this.storage = {};  this.capacity = capacity || Infinity;  this._count = 0;}
```

This constitues a stack storage mechanism. How can we push data into the stack in a LIFO manner? Add push to the prototype of Stack.

```
Stack.prototype.push = function(value) {  if (this._count < this._capacity){    this.storage[this._count++] = value;    return this._count;  }  return "Max capacity reached, please remove a value before inserting a new value";}
```

The push method checks our capacity. If true, we add the value to storage and return how many items are in the stack.

[this._count++] is first evaluated as 0, and we use the postfix operator, ++ to increment the count. Our stack has a value at this.storage[‘0’], and we return 1 because we have one item in our stack.

Let’s remove items or ‘pop’ them off the stack.

```
Stack.prototype.pop = function() {  let value = this.storage[--this._count];  delete this.storage[this._count];  if (this._count < 0) {    this._count = 0;  }  return value;}
```

With pop, we store the last value on the stack. If we remove it first, we won’t have it as a return value. Because of the prefix operator, — , we find the value of this.count and decrement it first before evaluating it. If we have this.count === 1, this.storage[ — this.count] is evalutated as this.storage[‘0’].

What about seeing what’s on the top of the stack? The interface for that is ‘peek’.

```
Stack.prototype.peek = function() {  return this.storage[this._count -1]}
```

Lastly, count…

```
Stack.prototype.count = function(){  return this._count;}
```

The full implementation ES6 style with class Stack:

```
class Stack {  constructor(capacity) {    this.storage = {};    this._count = 0;    this.capacity = capacity || Infinity;  }
```

```
  push(value) {    if (this._count < this.capacity){    this.storage[this._count++] = value;    return this._count;    }    return "Max capacity reached, please remove a value before inserting a new value";  }
```

```
  pop() {    let value = this.storage[--this._count];    delete this.storage[this._count];    if (this._count < 0) {      this._count = 0;    }    return value;  }  peek() {    return this.storage[this._count - 1];  }  count() {    return this._count;  }};let stack = new Stack();stack; // Stack { storage: {}, _count: 0, capacity: Infinity }stack.push('yea')stack.push('oh yea');
```

```
stack; // Stack {storage: { 0: 'yea', 1: 'oh yea' },  _count: 2,  capacity: Infinity }
```

```
stack.pop(); // 'oh yea'stack; // Stack { storage: { 0: 'yea' }, _count: 1, capacity: Infinity }
```

```
stack.push('nope');stack.push('yup');stack; // Stack {storage: { 0: 'yea', 1: 'nope', 2: 'yup' },  _count: 3,  capacity: Infinity }
```

```
stack.count(); // 3stack.peek(); // 'yup'stack; // Stack {storage: { 0: 'yea', 1: 'nope', 2: 'yup' },  _count: 3,  capacity: Infinity }
```

Thank you for reading this article. My goal was to give a clear uncluttered explanation of Stacks, their use, and why we need them. [Next up: Queues](https://medium.freecodecamp.org/data-structures-101-queues-a6960a3c98).


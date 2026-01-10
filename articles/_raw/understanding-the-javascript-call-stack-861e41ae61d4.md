---
title: The JavaScript Call Stack - What It Is and Why It's Necessary
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T07:12:22.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-javascript-call-stack-861e41ae61d4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-WOpjPy_2Idl4jIAzPokRQ.jpeg
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Charles Freeborn

  The JavaScript engine (which is found in a hosting environment like the browser),
  is a single-threaded interpreter comprising of a heap and a single call stack. The
  browser provides web APIs like the DOM, AJAX, and Timers.

  This ar...'
---

By Charles Freeborn

The JavaScript engine (which is found in a hosting environment like the browser), is a single-threaded interpreter comprising of a heap and a single call stack. The browser provides web APIs like the DOM, AJAX, and Timers.

This article is aimed at explaining what the call stack is and why it is needed. An understanding of the call stack will give clarity to how “function hierarchy and execution order” works in the JavaScript engine.

The call stack is primarily used for function invocation (call). Since the call stack is single, function(s) execution, is done, one at a time, from top to bottom. It means the call stack is synchronous.

The understanding of the call stack is vital to Asynchronous programming (which we will look at in a later article).

In Asynchronous JavaScript, we have a callback function, an event loop, and a task queue. The callback function is acted upon by the call stack during execution after the call back function has been pushed to the stack by the event loop.

But before we jump the gun, let us first attempt to answer the question - What is the call stack?

At the most basic level, a call stack is a data structure that uses the Last In, First Out (LIFO) principle to temporarily store and manage function invocation (call).

Let’s break down our definition:

**LIFO:** When we say that the call stack, operates by the data structure principle of Last In, First Out, it means that the last function that gets pushed into the stack is the first to be pop out, when the function returns.

Let us take a look at a code sample to demonstrate LIFO by printing a stack trace error to the console.

```js
function firstFunction(){
  throw new Error('Stack Trace Error');
}

function secondFunction(){
  firstFunction();
}

function thirdFunction(){
  secondFunction();
}

thirdFunction();
```

When the code is run, we get an error. A stack is printed showing how the functions are stack on top each other. Take a look at the diagram.

![Image](https://cdn-media-1.freecodecamp.org/images/zOINLHPC8E56ac8yyINYOFWeImsjM2Wk2rdU)
_Stack trace error_

You will notice that the arrangement of the functions as a stack begins with the `firstFunction()` (which is the last function that got into the stack, and is popped out to throw the error), followed by the `secondFunction()`, and then the `thirdFunction()` (which is the first function that gets pushed into the stack when the code is executed).

**Temporarily store**: When a function is invoked (called), the function, its parameters, and variables are pushed into the call stack to form a stack frame. This stack frame is a memory location in the stack. The memory is cleared when the function returns as it is pop out of the stack.

![Image](https://cdn-media-1.freecodecamp.org/images/QgR2uIk7tW0YNz0Xm8g0jAPeRFI0e4sCejsv)
_Image Credit: [CMU](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html" rel="noopener" target="_blank" title=")_

**Manage function invocation (call)**: The call stack maintains a record of the position of each stack frame. It knows the next function to be executed (and will remove it after execution). This is what makes code execution in JavaScript synchronous.

Think of yourself standing on a queue, in a grocery store cash point. You can only be attended to after the person in front of you have been attended to. That’s synchronous.

This is what we mean by “manage function invocation”.

### **How does the call stack handle function calls?**

We will answer this question by looking at a sample code of a function that calls another function. Here is the example code:

```js
function firstFunction(){
  console.log("Hello from firstFunction");
}

function secondFunction(){
  firstFunction();
  console.log("The end from secondFunction");
}

secondFunction();
```

![Image](https://cdn-media-1.freecodecamp.org/images/oEp65Ec9CD4CnL7t0uSPoyzrkA1i1BR-Ij1n)
_Here is the output_

This is what happens when the code is run:

1. When `secondFunction()` gets executed, an empty stack frame is created. It is the main (anonymous) entry point of the program.  
2. `secondFunction()` then calls `firstFunction()`which is pushed into the stack.  
3. `firstFunction()` returns and prints “Hello from firstFunction” to the console.  
4. `firstFunction()` is pop off the stack.  
5. The execution order then move to `secondFunction()`.  
6. `secondFunction()` returns and print “The end from secondFunction” to the console.  
7. `secondFunction()` is pop off the stack, clearing the memory.

### What causes a stack overflow?

A stack overflow occurs when there is a recursive function (a function that calls itself) without an exit point. The browser (hosting environment) has a maximum stack call that it can accomodate before throwing a stack error.

Here is an example:

```js
function callMyself(){
  callMyself();
}

callMyself();
```

The `callMyself()` will run until the browser throws a “Maximum call size exceeded”. And that is a stack overflow.

![Image](https://cdn-media-1.freecodecamp.org/images/lvjT-ud6XfVQ5KYVWxZZWkKeVTgtJqFD0pWv)
_Maximum call stack error_

### In summary

The key takeaways from the call stack are:  
1. It is single-threaded. Meaning it can only do one thing at a time.  
2. Code execution is synchronous.  
3. A function invocation creates a stack frame that occupies a temporary memory.  
4. It works as a LIFO — Last In, First Out data structure.

We have used the call stack article to lay the foundation for a series we will be looking at on Asynchronous JavaScript (which we will be looking at in another article).

All code samples can be found in this GitHub [repo](https://github.com/charlesfreeborn/JS-CallStack-CodeSamples/blob/master/codesamples.md).

_Thank you for reading. If this article was helpful please give it some claps ? so others can find it. I will like to read your comments also._


---
title: Asynchronous Programming in JavaScript – Callbacks, Promises, & Async/Await
  Examples
subtitle: ''
author: Musab Habeeb
co_authors: []
series: null
date: '2024-02-02T16:04:52.000Z'
originalURL: https://freecodecamp.org/news/asynchronous-programming-in-javascript-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Await-2.png
tags:
- name: async/await
  slug: asyncawait
- name: asynchronous programming
  slug: asynchronous-programming
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: null
seo_desc: 'All programming languages have runtime engines that execute their code.
  In JavaScript, the runtime engine is single-threaded, which means that it runs code
  line by line or sequentially.

  The JavaScript runtime engine makes it a synchronous programming...'
---

All programming languages have runtime engines that execute their code. In JavaScript, the runtime engine is single-threaded, which means that it runs code line by line or sequentially.

The JavaScript runtime engine makes it a synchronous programming language where programs run sequentially. Programming languages that are not synchronous are called asynchronous programming languages, which are programming languages where programs run concurrently.

Although JavaScript is synchronous, you can perform asynchronous programming with it. In this article, you will learn about asynchronous programming in JavaScript and how to use it.

## What is Asynchronous Programming?

Asynchronous programming is a technique that allows your program to run its tasks concurrently. You can compare asynchronous programming to a chef with multiple cookers, pots, and kitchen utensils. This chef will be able to cook various dishes at a time.

Asynchronous programming makes your JavaScript programs run faster, and you can perform asynchronous programming with any of these:

* Callbacks
    
* Promises
    
* Async/Await
    

In the upcoming sections, you will learn about these techniques and how to use them.

## Callbacks

A callback is a function used as an argument in another function. Callbacks allow you to create asynchronous programs in JavaScript by passing the result of a function into another function.

```javascript
function greet(name) {
    console.log(`Hi ${name}, how do you do?`);
}

function displayGreeting(callback) {
    let name = prompt("Please enter your name");
    callback(name);
};

displayGreeting(greet);
```

In the code above, the `greet` function is used to log a greeting to the console, and it needs the name of the person to be greeted.

The `displayGreeting` function gets the person's name and has a callback that passes the name as an argument to the `greet` function while calling it. Then the `displayGreeting` function is called with the greet function passed to it as an argument.

### Callback hell

Although callbacks make it easy to control and make your program asynchronous, you'll eventually run into a problem called callback hell while using them.

This problem arises when you perform multiple asynchronous tasks with callbacks, which might result in nesting callbacks in callbacks.

Here's an example:

```javascript
function greet(callback) {
    setTimeout(function() {
        console.log("Hi Musab");
        callback();
    }, 1000);
}

function introduce(callback) {
    setTimeout(function() {
        console.log("I am your academic advisor");
        callback();
    }, 1000);
}

function question(callback) {
    setTimeout(function() {
        console.log("Are you currently facing any challenge in your academics");;
        callback();
    }, 1000);
}

// callback hell
greet(function() {
    introduce(function() {
        question(function() {
            console.log("Done");
        });
    });
});
```

In the code above, the `greet`, `introduce`, and `question` functions are nested to create a callback hell, which makes error handling difficult. You should change your asynchronous programming technique from callbacks to `Promise` to avoid the callback hell.

## Promise

Most programs consist of a producing code that performs a time-consuming task and a consuming code that needs the result of the producing code.

A `Promise` links the producing and the consuming code together. In the example below, the `displayGreeting` function is the producing code while the `greet` function is the consuming code.

```javascript
let name;

// producing code
function displayGreeting(callback) {
    name = prompt("Please enter your name");
}

// consuming code
function greet(name) {
    console.log(`Hi ${name}, how do you do?`);
}
```

In the example below, the `new Promise` syntax creates a new `Promise`, which takes a function that executes the producing code. The function either resolves or rejects its task and assigns the `Promise` to a variable named `promise`.

If the producing code resolves, its result will be passed to the consuming code through the `.then` handler.

```javascript
let name;

function displayGreeting() {
    name = prompt("Please enter your name");
}

let promise = new Promise(function(resolve, reject) {
    // the producing code
    displayGreeting();
    resolve(name)
});

function greet(result) {
    console.log(`Hi ${result}, how do you do?`);
}

promise.then(
    // the consuming code
    result => greet(result),
    error => alert(error)
);
```

You can convert the previous callback hell's example to a promise by returning a promise from each function and chaining the function calls together with the `.then` handler.

You can also use the `.catch` handler to catch any error thrown during the function execution.

```javascript
function greet() {
    return new Promise(resolve => {
        setTimeout(function() {
            console.log("Hi Musab");
            resolve();
        }, 1000);
    });  
}

function introduce() {
    return new Promise(resolve => {
        setTimeout(function() {
            console.log("I am your academic advisor");
            resolve();
        }, 1000);
    });
}

function question() {
    return new Promise(resolve => {
        setTimeout(function() {
            console.log("Are you currently facing any challenge in your academics");;
            resolve();
        }, 1000);
    });
}

greet()
    .then(() => introduce())
    .then(() => question())
    .then(() => console.log("Done"))
    .catch(error => console.error("An error occured: ", error));
```

### What are the States of a Promise in JavaScript?

A promise can be in any of these three states:

* Pending: This is the initial state of the promise and its state while it's still running.
    
* Fulfilled: This is the state of the promise when it resolves successfully.
    
* Rejected: This is the state of the promise when errors make it not to be resolved.
    

## Async/Await

`async`/`await` is syntactic sugar for creating a `Promise` — it makes creating promises easier.

To make a function asynchronous using `async`/`await`, you have to write the `async` keyword before the function declaration. Then, you can write the `await` keyword before the producing code's execution call.

Here's an example:

```javascript
let name;

function displayGreeting() {
    name = prompt("Please enter your name");
    return name;
}

function greet(result) {
    console.log(`Hi ${result}, how do you do?`);
}

async function greeting() {
    // the producing code
    let result = await displayGreeting();
    // the consuming code
    greet(result);
};

greeting();
```

In the example above, the producing code is the `displayGreeting` function, and the consuming code is the `greet` function. The `greeting` function is the `Promise` that connects the producing and the consuming code. It waits for the result returned from the `displayGreeting` function and passes that result to the greet function.

### Error Handling in Async/Await

You can easily handle errors that arise when you perform asynchronous operations with `async`/`await` using the `try...catch` statement. The asynchronous operation executes in the `try` block, and you can handle errors in the `catch` block.

That is:

```javascript
async function greeting() {
    try {
        let result = await displayGreeting();
        greet(result);
    } catch(err) {
        console.error(err)
    }
};
```

## Conclusion

Asynchronous programming in JavaScript is used to make tasks in a program run concurrently and uses techniques such as callbacks, `Promise`, or `async`/`await`.

This article explains how to use these asynchronous programming techniques and how to handle errors with them.

You can check the [promises and async/await section on the JavaScript.info website](https://javascript.info/async) to learn more about asynchronous programming in JavaScript.

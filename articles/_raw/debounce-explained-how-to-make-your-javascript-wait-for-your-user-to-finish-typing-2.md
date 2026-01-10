---
title: Debounce Explained – How to Make Your JavaScript Wait For Your User To Finish
  Typing
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-07T20:31:24.000Z'
originalURL: https://freecodecamp.org/news/debounce-explained-how-to-make-your-javascript-wait-for-your-user-to-finish-typing-2
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/pexels-photo.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristian Vega

  Debounce functions in JavaScript are higher-order functions that limit the rate
  at which another function gets called.


  A higher-order function is a function that either takes a function as an argument
  or returns a function as part o...'
---

By Cristian Vega

Debounce functions in JavaScript are higher-order functions that limit the rate at which another function gets called.

> A higher-order function is a function that either takes a function as an argument or returns a function as part of its return statement. Our debounce function does both.

The most common use case for a debounce is to pass it as an argument to an event listener attached to an HTML element. To get a better understanding of what this looks like, and why it is useful, let’s look at an example.

Say that you have a function named `myFunc` that gets called each time you type something into an input field. After going through the requirements for your project, you decide that you want to change the experience. 

Instead, you want `myFunc` to execute when at least 2 seconds have passed since the last time you typed something in.

This is where a debounce can comes into play. Instead of passing `myFunc` to the event listener, you would pass in the debounce. The debounce itself would then take `myFunc` as an argument, along with the number 2000.

Now, whenever you click the button, `myFunc` will only execute if at least 2 seconds have elapsed before the last time `myFunc` was called.

## How to implement a debounce function

From start to finish, it only takes 7 lines of code to implement a debounce function. The rest of this section focuses on those 7 lines of code so that we can see how our debounce function works internally.

```javascript
function debounce( callback, delay ) {
    let timeout;
    return function() {
        clearTimeout( timeout );
        timeout = setTimeout( callback, delay );
    }
}
```

Starting with line 1, we've declared a new function named `debounce`. This new function has two parameters, `callback` and `delay`.

```javascript
function debounce( callback, delay ) {

}

```

`callback` is any function that needs to limit the number of times it executes.

`delay` is the time (in milliseconds) that needs to elapse before `callback` can execute again.

```javascript
function debounce( callback, delay ) {
    let timeout;
}
```

On line 2, we’re declaring an uninitialized variable named `timeout`.  
This new variable holds the `timeoutID` returned when we call `setTimeout` later on in our `debounce` function.

```javascript
function debounce( callback, delay ) {
    let timeout;
    return function() {
    }
}
```

On line 3, we’re returning an anonymous function. This anonymous function will close over the `timeout` variable so that we can retain access to it even after the initial call to `debounce` has finished executing.

> A closure in JavaScript occurs whenever an inner function retains access to the lexical scope of its outer function, even though the outer function has finished executing. If you want to learn more about closures, you can read [Chapter 7 of “You Don’t Know JS”](https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch7.md) by Kyle Simpson

```javascript
function debounce( callback, delay ) {
    let timeout;
    return function() {
        clearTimeout( timeout );
    }
}
```

On line 4, we are calling the `clearTimeout` method of the `WindowOrWorkerGlobalScope` mixin. This will make sure that each time we call our `debounce` function, `timeout` is reset, and the counter can start again.

The `WindowOrWorkerGlobalScope` mixin of JavaScript gives us access to a few well-known methods, like `setTimeout`, `clearTimeout`, `setInterval`, `clearInterval`, and `fetch`. 

You can learn more about it by [reading this article](https://www.freecodecamp.org/news/an-introduction-to-scope-in-javascript-cbd957022652/).

```javascript
function debounce( callback, delay ) {
    let timeout;
    return function() {
        clearTimeout( timeout );
        timeout = setTimeout( callback, delay );
    }
}
```

On line 5, we have reached the end of our `debounce` function implementation.

That line of code does a few things. The first action is assigning a value to the `timeout` variable that we declared on line 2. The value is a `timeoutID` that gets returned when we call `setTimeout`. This will allow us to reference the timeout created by calling `setTimeout` so that we can reset it each time our `debounce` function is used.

The second action performed is calling `setTimeout`. This will create a timeout that will execute `callback` (the function argument passed to our `debounce` function) once `delay` (the number argument passed to our `debounce` function) has elapsed.

Since we are using a timeout, `callback` will only execute if we allow the timeout to reach 0. This is where the heart of our `debounce` function comes into play since we are resetting the timeout each time `debounce` is called. This is what allows us to limit the execution rate of `myFunc`.

Lines 5 and 6 contain only brackets, so we won’t go over them.

That’s it. That is how our `debounce` function works internally. Now let’s add on to our previous example from the beginning. We’re going to create an input field and attach an event listener with our `debounce` function as one of its arguments.

## Real World Example

First, we need to create an input field.

```html
<label for="myInput">Type something in!</label>
<input id="myInput" type="text">
```

Next, we need to create a function that we want to execute whenever we type something into our input field.

```javascript
function helloWorld() {
    console.log("Hello World!")
}
```

Finally, we need to select the input field we created above and attach a `keyup` event listener to it.

```javascript
const myInput = document.getElementById("myInput");

myInput.addEventListener(
    "keyup",
    debounce( helloWorld, 2000 )
);
```

That concludes our real world example! Each time we type something into our input field, `helloWorld` will execute if at least 2 seconds have passed since the last time we typed something in.

> Special thanks to Reddit user **stratoscope** for helping to fix some of the initial code in this article. [Here is a working demo](https://repl.it/@geary/JsDebounce#script.js) he created of this `debounce` function on Repl.it.

## Closing Notes

Debounce functions are simple, yet powerful, functions that can have a noticeable impact on most JavaScript applications.

While our example was fun and straightforward, many large organizations use debounce functions to increase the performance of their applications. 

If you want to learn more about JavaScript, check out my website! I am working on some cool stuff at [https://juanmvega.com](https://juanmvega.com).


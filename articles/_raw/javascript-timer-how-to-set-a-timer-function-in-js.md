---
title: JavaScript Timer – How to Set a Timer Function in JS
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2024-09-16T18:59:45.207Z'
originalURL: https://freecodecamp.org/news/javascript-timer-how-to-set-a-timer-function-in-js
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726513174015/54470912-08b3-4a23-9a0c-9b6f9b57617b.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: In Javascript, the timer function prevents your code from running everything
  at once when an event triggers or the page loads. This gives you more control over
  the timing of your program's actions and can enhance the user experience by creating
  smoot...
---

In Javascript, the timer function prevents your code from running everything at once when an event triggers or the page loads. This gives you more control over the timing of your program's actions and can enhance the user experience by creating smoother interactions or animations.  

In this tutorial, you'll learn how to use the set timer functions.

## **How to Set a Timer Function**

There are various ways of setting a timer function, such as the `setTimeout`, `setInterval`, `clearTimeout`, and `setImmediate` functions. You'll learn about each of them in this article.

### **How to Use** `setTimeout` **and** `setInterval`

The `setTimeout` function executes an expression after a specified delay in milliseconds while the `setInterval` function executes an expression after a specified interval in milliseconds.

You can use the `setTimeout()` function when you want to execute code block with a specific delay, but just once.

The setTimeout function is denoted by `setTimeout()`. Here's an example of how you can use it:

```javascript
// Execute a function after 3 seconds
⁠ const timeoutId = setTimeout(() => {
    console.log('Timeout executed after 3 seconds');
}, 3000);
```

The above code block shows how to use the `setTimeout` syntax to execute a function after 3 seconds. The name of the variable is `timeoutId` which stores the execution of the setTimeout. The time set is 3000 milliseconds (or 3 seconds).

You can use the `setInterval()` function when you want to execute a code block repeatedly but at specific intervals – for instance, when animating elements.

The setInterval function is denoted by `setInterval()`. Here's how you can use it:

```javascript
// Execute a function every 1 second
const intervalId = setInterval(() => {
    console.log('Interval executed every 1 second');
}, 1000);
```

The above code block shows how to use the `setInterval` syntax to execute a function after 1 second. The name of the variable is `intervalId` which stores the execution of the setInterval. The time is set to 1000 milliseconds (1 second).

### **How to Use** `clearTimeout` **and** `clearInterval`

The `clearTimeout` function cancels a timeout previously scheduled with  the `setTimeout` function. `clearInterval` cancels an interval previously set with ⁠`setInterval` .

The clearTimeout function is denoted by `clearTimeout();`. It accepts an argument that stores the `setTimeout` function.

Here's an example of how it works:

```javascript
const timeoutId = setTimeout(() => {
    console.log('Timeout executed after 3 seconds');
}, 3000);

clearTimeout(timeoutId);
console.log('Timeout cleared');
```

The `clearTimeout` function takes the variable name `timeoutID` which stores the `setTimeout` function and clears the function.

The `clearInterval function` is denoted by `clearInterval();`.  It accepts an argument that stores the `setInterval` function under the block of the `setTimeout` function.

Here's an example of how it works:

```javascript
const intervalId = setInterval(() => {
    console.log('Interval executed every 1 second');
}, 1000);

setTimeout(() => {
    clearInterval(intervalId);
    console.log('Interval cleared. Function will no longer execute.');
}, 5000); 
```

In the above code block, the `setTimeout` function is introduced. The `clearInterval` function is passed into the code block, the argument `intervalId` is passed, and then the function is executed. 

Another timer function is `setImmediate` which executes a function asynchronously as soon as possible after the current code block finishes executing. But it’s not universally supported across all browsers, so it’s rarely used.

## Wrapping Up

It's important to know how to use JavaScript timer functions and when to apply them to your code. And remember that the timer is set to milliseconds, so whatever number you use, divide it by 1000 to determine how many seconds it is.

If you have any questions, you can reach out to me on [Twitter](https://twitter.com/HeritageAlabi1) 💙.

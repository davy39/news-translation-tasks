---
title: 'JavaScript Timing Events: setTimeout and setInterval'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-timing-events-settimeout-and-setinterval
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ce8740569d1a4ca34d2.jpg
tags:
- name: events
  slug: events
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Programmers use timing events to delay the execution of certain code, or
  to repeat code at a specific interval.

  There are two native functions in the JavaScript library used to accomplish these
  tasks: setTimeout() and setInterval().

  setTimeout

  setTim...'
---

Programmers use timing events to delay the execution of certain code, or to repeat code at a specific interval.

There are two native functions in the JavaScript library used to accomplish these tasks: `setTimeout()` and `setInterval()`.

### setTimeout

`setTimeout()` is used to delay the execution of the passed function by a specified amount of time.

There are two parameters that you pass to `setTimeout()`: the function you want to call, and the amount of time in milliseconds to delay the execution of the function.

Remember that there are 1000 milliseconds (ms) in a 1 second, so 5000 ms is equal to 5 seconds.

`setTimeout()` will execute the function from the first argument one time after the specified time has elapsed.

**Example:**

```javascript
let timeoutID;

function delayTimer() {
  timeoutID = setTimeout(delayedFunction, 3000);
}

function delayedFunction() {
  alert(“Three seconds have elapsed.”);
}
```

When the `delayTimer` function is called it will run `setTimeout`. After 3 seconds (3000 ms) pass, it will execute `delayedFunction` which will send an alert.

**setInterval**

Use `setInterval()` to specify a function to repeat with a time delay between executions. 

Again, two parameters are passed to `setInterval()`: the function you want to call, and the amount of time in milliseconds to delay each call of the function . 

`setInterval()` will continue to execute until it is cleared.

**Example:**

```javascript
let intervalID;

function repeatEverySecond() {
  intervalID = setInterval(sendMessage, 1000);
}

function sendMessage() {
  console.log(“One second elapsed.”);
}
```

When your code calls the function `repeatEverySecond` it will run `setInterval`. `setInterval` will run the function `sendMessage` every second (1000 ms).

### clearTimeout and clearInterval

There are also corresponding native functions to stop the timing events: `clearTimeout()` and `clearInterval()`.

You may have noticed that each timer function above is saved to a variable. When either the `setTimeout` or `setInterval` function runs, it is assigned a number which is saved to this variable. Note that JavaScript does this all in the background.

This generated number is unique for each instance of timers. This assigned number is also how timers are identified when you want to stop them. For this reason, you must always set your timer to a variable.

For clarity of your code, you should always match `clearTimeout()` to `setTimeout()` and `clearInterval()` to `setInterval()`.

To stop a timer, call the corresponding clear function and pass it the timer ID variable that matches the timer you wish to stop. The syntax for `clearInterval()` and `clearTimeout()` are the same.

**Example:**

```javascript
let timeoutID;

function delayTimer() {
  timeoutID = setTimeout(delayedFunction, 3000);
}

function delayedFunction() {
  alert(“Three seconds have elapsed.”);
}

function clearAlert() {
  clearTimeout(timeoutID);
}
```


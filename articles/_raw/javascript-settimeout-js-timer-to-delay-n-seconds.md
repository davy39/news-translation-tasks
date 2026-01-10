---
title: JavaScript setTimeout() – JS Timer to Delay N Seconds
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-08-26T23:57:34.000Z'
originalURL: https://freecodecamp.org/news/javascript-settimeout-js-timer-to-delay-n-seconds
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/erik-mclean-7lyRKyKIdJY-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Have you ever wondered if there is a method to delay your JavaScript code\
  \ by a few seconds? \nIn this article, I will explain what the setTimeout() method\
  \ is with code examples and how it differs from setInterval(). \nWhat is setTimeout()\
  \ in JavaScript..."
---

Have you ever wondered if there is a method to delay your JavaScript code by a few seconds? 

In this article, I will explain what the `setTimeout()` method is with code examples and how it differs from `setInterval()`. 

## What is `setTimeout()` in JavaScript?

`setTimeout()` is a method that will execute a piece of code after the timer has finished running. 

Here is the syntax for the `setTimeout()` method.

```js
let timeoutID = setTimeout(function, delay in milliseconds, argument1, argument2,...);
```

 Let's break down the syntax. 

### Function

`setTimeout()` will set a timer and once the timer runs out, the function will run. 

### Delay in milliseconds

Inside this method, you can specify how many milliseconds you want the function to delay. 1,000 milliseconds equals 1 second. 

In this example, the message will appear on the screen after a delay of 3 seconds. (3,000 milliseconds) 

%[https://codepen.io/jessica-wilkins/pen/NWgqKKa?editors=0011]

```js
const para = document.getElementById("para");

function myMessage() {
  para.innerHTML = "I just appeared";
  console.log("message appeared");
}
setTimeout(myMessage, 3000);
```

If the delay is not present in the `setTimeout()` method then it is set to zero and the message will appear immediately. 

%[https://codepen.io/jessica-wilkins/pen/eYRNOgX?editors=1111]

```js
const para = document.getElementById("para");

function myMessage() {
  para.innerHTML = "No delay in this message";
  console.log("message appeared immediately");
}
setTimeout(myMessage);
```

### Arguments

You can also have optional arguments that are passed into the function.

In this example conversation, Britney will ask a question and Ashley's response will be delayed by 3 seconds. It will include the two optional arguments from the `lunchMenu` function. 

%[https://codepen.io/jessica-wilkins/pen/YzQXzZa?editors=1010]

```js
const ashley = document.getElementById("ashley");

function lunchMenu(food1, food2) {
  ashley.innerHTML = `<strong>Ashley: </strong>I had ${food1} and ${food2}.`;
}

setTimeout(lunchMenu, 3000, "pizza", "salad");
```

### timeoutID

`setTimeout()` will return the `timeoutID` which is a positive integer and unique ID for the timer. 

### clearTimeout()

This method is used to cancel a `setTimeout()`.  Inside the method you have to reference the `timeoutID`.

Here is the basic syntax. 

```js
clearTimeout(timeoutID)
```

In this example, the message will appear after a 10 second (10,000 millisecond) delay. But if the user clicks on the `Stop Timer` button, then the `setTimeout()` will be cancelled. 

%[https://codepen.io/jessica-wilkins/pen/JjJdoWm]

```js
const timerMsg = document.getElementById("message1");
const stopBtn = document.getElementById("stop");

function timerMessage() {
  timerMsg.innerHTML = "Thanks for waiting!";
}

let timeoutID = setTimeout(timerMessage, 10000);

stopBtn.addEventListener("click", () => {
  clearTimeout(timeoutID);
  timerMsg.innerHTML = "Timer was stopped";
});
```

## Should you pass in a string instead of a function for setTimeout()?

It is considered bad practice and a security risk to pass in a string instead of a function. 

Avoid writing `setTimeout()` like this:

```js
setTimeout("console.log('Do not do this');", 1000);


```

Some code editors will warn you and suggest using a function instead. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-26-at-3.32.04-AM.png)

Always use a function instead of a string in this case. 

```js
setTimeout(function () {
  console.log("Do this instead");
}, 1000);
```

If you want to learn more about the security risks for an implied eval, please read about it in the MDN docs section on [Never Use Eval](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#never_use_eval!). 

## How does `setInterval()` differ from `setTimeout()`?

Unlike `setTimeout()` which executes a function just once after a delay, `setInterval()` will repeat a function every set number of seconds. If you want to stop `setInterval()`, then you use `clearInterval()`.

The syntax for `setInterval()` is the same as `setTimeout()`. 

```js
let intervalID = setInterval(function, delay in milliseconds, argument1, argument2,...);
```

In this example, we have a sales message that is being printed to the screen every second.

%[https://codepen.io/jessica-wilkins/pen/wveaaYX]

```js
let intervalID = setInterval(() => {
  salesMsg.innerHTML += "<p>Sale ends soon. BUY NOW!</p>";
}, 1000);
```

Inside the `setTimeout()` method, we use `clearInterval()` to stop printing the message after 10 seconds. 

```js
setTimeout(() => {
  clearInterval(intervalID);
}, 10000);
```

Just like with `setTimeout()`, you have to use the unique ID for the timer inside the `clearInterval()` method. 

## Real Project Examples

Now that we understand how `setTimeout()` and `setInterval()` work, let's take a look at an example of how it can apply to a real feature on a website.

%[https://codepen.io/jessica-wilkins/pen/yLXNojz?editors=0011]

In this example, we have a progress bar that will start 2 seconds after the page loads. Inside the `setTimeout()`, we have a `setInterval()` that will execute the `animate()` function as long as the bar width is not 100%. 

```js
setTimeout(() => {
  let intervalID = setInterval(() => {
    if (barWidth === 100) {
      clearInterval(intervalID);
    } else {
      animate();
    }
  }, 100);//this sets the speed of the animation
}, 2000);
```

 Inside the `animate()` function, we have another `setTimeout()` that will display 100% Completed when the progress bar is full. 

```js
const animate = () => {
  barWidth++;
  progressBar.style.width = `${barWidth}%`;
  setTimeout(() => {
    loadingMsg.innerHTML = `${barWidth}% Completed`;
  }, 10100);
};
```

A progress bar is just one of many animations you can create with `setTimeout()` and `setInterval()`. You can also use these methods when building online games.

In Beau Carnes' [How to Build A Simon Game](https://www.youtube.com/watch?v=n_ec3eowFLQ) you can see how `setTimeout()` and `setInterval()` are used in the game logic. 

## Conclusion

`setTimeout()` is a method that will execute a piece of code after the timer has finished running. 

```js
let timeoutID = setTimeout(function, delay in milliseconds, argument1, argument2,...);
```

The delay is set in milliseconds and 1,000 milliseconds equals 1 second. 

If the delay is omitted from the `setTimeout()` method, then the delay is set to 0 and the function will execute. 

You can also have optional arguments that are passed into the function.

`setTimeout()` will return the `timeoutID` which is a positive integer and unique ID for the timer. 

It is important not to use a string in place of the function for security reasons. 

```js
setTimeout("console.log('Do not do this');", 1000);
```

If you want to cancel `setTimeout()` then you need to use `clearTimeout()`

```js
clearTimeout(timeoutID)
```

If you want to repeatedly execute a piece of code for a set amount of seconds then you would use `setInterval()`. 

```js
let intervalID = setInterval(() => {
 // this code runs every second
}, 1000);
```

`setTimeout()` can be used in building basic JavaScript animations and online games.

I hope you enjoyed this article on `setTimeout()`. 


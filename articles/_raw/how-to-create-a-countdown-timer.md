---
title: How to Create a Countdown Timer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-21T21:59:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-countdown-timer
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e90740569d1a4ca3dc5.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Building a simple countdown timer is easy with JavaScript''s native timing
  events. You can read more about those in this article.

  Building the countdown timer

  Start by declaring an empty function called startCountdown that takes seconds as
  an argument...'
---

Building a simple countdown timer is easy with JavaScript's native timing events. You can read more about those in [this article](https://www.freecodecamp.org/news/p/50cdf5da-8359-4bd2-8718-d5bd7c0de03d/www.freecodecamp.org/news/javascript-timing-events-settimeout-and-setinterval/).

### Building the countdown timer

Start by declaring an empty function called `startCountdown` that takes `seconds` as an argument:

```javascript
function startCountdown(seconds) {
    
};
```

We want to keep track of the seconds that pass once the timer is started, so use `let` to declare a variable called `counter` and set it equal to `seconds`:

```js
function startCountdown(seconds) {
  let counter = seconds;
}
```

Remember that it's best practice to save your timing event function to a variable. This makes it much easier to stop the timer later. Create a variable called `interval` and set it equal to `setInterval()`:

```js
function startCountdown(seconds) {
  let counter = seconds;
    
  const interval = setInterval();
}
```

You can pass a function directly to `setInterval`, so let's pass it an empty arrow function as the first argument. Also, we want the function to run every second, so pass 1000 as the second argument:

```js
function startCountdown(seconds) {
  let counter = seconds;
    
  const interval = setInterval(() => {
    
  }, 1000);
}
```

Now the function we passed to `setInterval` will run every second. Every time it runs, we want to log the current value of `counter` to the console before deincrementing it:

```js
function startCountdown(seconds) {
  let counter = seconds;
    
  const interval = setInterval(() => {
    console.log(counter);
    counter--;
  }, 1000);
}
```

Now if you run the function, you'll see that it works, but doesn't stop once `counter` is less than 0:

```js
startCountdown(5);

// Console Output // 
// 5
// 4
// 3
// 2
// 1
// 0 
// -1
// -2 
```

To fix this, first write an `if` statement that executes when `counter` is less than 0:

```js
function startCountdown(seconds) {
  let counter = seconds;
    
  const interval = setInterval(() => {
    console.log(counter);
    counter--;
      
    if (counter < 0 ) {
      
    }
  }, 1000);
}
```

Then inside the `if` statement, clear the `interval` with `clearInterval` and log an alarm sound string to the console:

```js
function startCountdown(seconds) {
  let counter = seconds;
    
  const interval = setInterval(() => {
    console.log(counter);
    counter--;
      
    if (counter < 0 ) {
      clearInterval(interval);
      console.log('Ding!');
    }
  }, 1000);
}
```

### **Execution**

Now when you start the timer, you should see the following:

```javascript
startCountdown(5);

// Console Output // 
// 5
// 4
// 3
// 2
// 1
// 0 
// Ding!
```

### **More Resources**

[JavaScript Timing Events: setTimeout and setInterval](https://www.freecodecamp.org/news/p/50cdf5da-8359-4bd2-8718-d5bd7c0de03d/www.freecodecamp.org/news/javascript-timing-events-settimeout-and-setinterval/)


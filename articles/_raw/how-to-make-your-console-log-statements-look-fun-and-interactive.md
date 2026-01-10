---
title: How to Make your Console Output Fun and Interactive in JavaScript and Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-02T21:11:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-console-log-statements-look-fun-and-interactive
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60190c1a0a2838549dcbcd11.jpg
tags:
- name: console
  slug: console
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: null
seo_desc: 'By Vasyl Lagutin

  In this tutorial, you''ll learn how to add a randomized delay to the console.log
  statements in JavaScript and Node.js.


  Why would you want to do this?

  First of all, programming should be fun. And making a boring thing like console.log...'
---

By Vasyl Lagutin

In this tutorial, you'll learn how to add a randomized delay to the `console.log` statements in JavaScript and Node.js.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/ezgif.com-gif-maker.gif)

## Why would you want to do this?

First of all, programming should be fun. And making a boring thing like `console.log` look nice is very pleasing.

If you want to get quick access to the source code, you can check out this [GitHub repository](https://github.com/AgileNix/funkylog/).

## Step 1: Create a function that takes the string and passes it into console.log

To make sure that every step is clear, we'll start small and create a function that accepts a string as a parameter and logs it to the console.

```javascript
const log = (s) => {
  console.log(s);
}
```

## Step 2: Log characters of the string one-by-one

Before we can add a delay between the output of the individual chars, we need to make sure that they're actually split.

Let's add a `for` loop that iterates over each letter of the string and prints it to the console.

```javascript
const log = (s) => {
  for (const c of s) {
    console.log(c);
  }
}
```

## Step 3: How to fix the newline issue

Now, each letter is printed on a new line as every call to `console.log` adds an empty line.

We'll replace the `console.log` with `_**process**_.stdout.write` which essentially does the same thing, but doesn't add a new line after the output.

Now, however, we've lost the newline in the very end of the output, which is still desirable. We'll add it by explicitly printing the `\n` character.

```javascript
const log = (s) => {
  for (const c of s) {
    process.stdout.write(c);
  }
  process.stdout.write('\n');
}
```

## Step 4: Implement the `sleep` function

In JavaScript we can't simply stop the execution of the synchronous code for some amount of time. To make this happen, we need to write our own function. Let's call it sleep.

It should accept a single parameter `ms` and return a Promise that resolves after the delay of `ms` milliseconds.

```javascript
const sleep = (ms) => {
  return new Promise(resolve => setTimeout(resolve, ms));
};
```

## Step 5: Add the delay

So, we're ready to add a delay to our output! We need a couple of things here:

* add a parameter `delay` to the function `log`
* make the function `log` asynchronous by adding the keyword `async`
* call a `sleep` function that will delay the next loop iteration by `delay` milliseconds

```javascript
const sleep = (ms) => {
  return new Promise(resolve => setTimeout(resolve, ms));
};

const log = async (s, delay) => {
  for (const c of s) {
    process.stdout.write(c);
    await sleep(delay);
  }
  process.stdout.write('\n');
}
```

## Step 6: Implement randomized delay

The output will look even better if we randomize the timing.

Let's add another boolean parameter `randomized` to the function `log`. If it's true, then the argument passed into `sleep` should be in the range from `0` to `delay` milliseconds.

```javascript
const sleep = (ms) => {
  return new Promise(resolve => setTimeout(resolve, ms));
};

const log = async (s, delay, randomized) => {
  for (const c of s) {
    process.stdout.write(c);
    await sleep((randomized ? Math.random() : 1) * delay);
  }
  process.stdout.write('\n');
}
```

I've used a ternary operator, but you can replace it with a regular `if` statement:

```javascript
if (randomized) {
  sleep(Math.random * delay);
} else {
  sleep(delay);
}
```

## Step 7: Make the log configurable

Right now, we've implemented pretty much everything we wanted to. But calling it isn't very clean as we have to pass the `delay` and randomization flag every time we want to print something to the console.

```javascript
log('Hello, world!', 100, true);
log('What\'s up?', 100, true);
log('How are you?', 100, true);
```

It'd be nice if we could have a configurable log that could be called with a single parameter - a string that we want to output.

To do this, we'll have to rewrite our code. Here's the plan:

* wrap all current functionality into a single function `funkylog` that accepts an object with 2 fields, `delay` and `randomized`
* `funkylog` should return the anonymous arrow function. Its implementation should be the same as `log`, that we've implemented on steps 1 through 6
* parameters `delay` and `randomized` should be removed from the `log` function as now they'll be passed down from the `funkylog`

```javascript
const funkylog = ({ delay, randomized }) => {
  const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
  };
    
  return async (s) => {
    for (const c of s) {
      process.stdout.write(c);
      await sleep((randomized ? Math.random() : 1) * delay);
    }
    process.stdout.write('\n');
  }
};
```

## Step 8: Add the finishing touch

Let's take a look at what we've got:

```javascript
const log = funkylog({ delay: 100, randomized: true });

log('Hello, world!');
log('What\'s up?');
log('How are you?');
```

* We can create a configurable logger using the function `funkylog`
* We can select any delay we want
* Using the logger doesn't require us to pass the `delay` every time we call it

One more improvement that we can make is providing a default value for the `delay` parameter.

```javascript
const funkylog = ({ delay = 100, randomized }) => {
    ..
    ..
```

So, now we can create the `funkylog` without any arguments and it will still work!

```javascript
const log = funkylog();

console.log('Hello, world!');
```

## Improvement ideas

As I've said from the very beginning, first of all, programming should be fun. Otherwise it'll become a routine and you won't enjoy doing it.

Do make further improvements to the `funkylog` and let me know what your results look like! For example, you can spice up the output by colorizing it. You can use the `npm` module `chalk` for it.

Then, once you have implemented different colors, you can add another flag that would add an additional delay between the words in the string.

Thank you for staying with me, throughout the whole tutorial!  
I write a programming blog at [learn.coderslang.com](https://learn.coderslang.com) and build a [Full Stack JS course](https://js.coderslang.com).

### If you have feedback or questions on this tutorial, feel free to Tweet me **@coderslang** or jump into the discussion on Telegram **@coderslang_chat**


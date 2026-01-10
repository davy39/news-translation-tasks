---
title: Debounce – How to Delay a Function in JavaScript (JS ES6 Example)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-18T18:16:53.000Z'
originalURL: https://freecodecamp.org/news/javascript-debounce-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/teaser.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Ondrej Polesny\nIn JavaScript, a debounce function makes sure that your\
  \ code is only triggered once per user input. Search box suggestions, text-field\
  \ auto-saves, and eliminating double-button clicks are all use cases for debounce.\
  \ \nIn this tutoria..."
---

By Ondrej Polesny

In JavaScript, a debounce function makes sure that your code is only triggered once per user input. Search box suggestions, text-field auto-saves, and eliminating double-button clicks are all use cases for debounce. 

In this tutorial, we'll learn how to create a debounce function in JavaScript.

## What is debounce?

The term **debounce** comes from electronics. When you’re pressing a button, let’s say on your TV remote, the signal travels to the microchip of the remote so quickly that before you manage to release the button, it bounces, and the microchip registers your “click” multiple times.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/debounce-button.png)

To mitigate this, once a signal from the button is received, the microchip stops processing signals from the button for a few microseconds while it’s physically impossible for you to press it again.

## Debounce in JavaScript

In JavaScript, the use case is similar. We want to trigger a function, but only once per use case. 

Let's say that we want to show suggestions for a search query, but only after a visitor has finished typing it. 

Or we want to save changes on a form, but only when the user is not actively working on those changes, as every "save" costs us a database trip. 

And my favorite—some people got really used to Windows 95 and now double click everything 😁.

This is a simple implementation of the _debounce_ function ([CodePen here](https://codepen.io/ondrabus/pen/WNGaVZN)):

```js
function debounce(func, timeout = 300){
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => { func.apply(this, args); }, timeout);
  };
}
function saveInput(){
  console.log('Saving data');
}
const processChange = debounce(() => saveInput());
```

It can be used on an input:

```html
<input type="text" onkeyup="processChange()" />
```


Or a button:

```html
<button onclick="processChange()">Click me</button>
```

Or a window event:

```js
window.addEventListener("scroll", processChange);
```

And on other elements like a simple JS function.

So what’s happening here? The `debounce` is a special function that handles two tasks:

* Allocating a scope for the _timer_ variable
* Scheduling your function to be triggered at a specific time

Let’s explain how this works in the first use case with text input. 

When a visitor writes the first letter and releases the key, the `debounce` first resets the timer with `clearTimeout(timer)`. At this point, the step is not necessary as there is nothing scheduled yet. Then it schedules the provided function—`saveInput()`—to be invoked in 300 ms. 

But let's say that the visitor keeps writing, so each key release triggers the `debounce` again. Every invocation needs to reset the timer, or, in other words, cancel the previous plans with `saveInput()`, and reschedule it for a new time—300 ms in the future. This goes on as long as the visitor keeps hitting the keys under 300 ms. 

The last schedule won’t get cleared, so the `saveInput()` will finally be called.

## The other way around—how to ignore subsequent events

That’s good for triggering auto-save or displaying suggestions. But what about the use case with multiple clicks of a single button? We don’t want to wait for the last click, but rather register the first one and ignore the rest ([CodePen here](https://codepen.io/ondrabus/pen/bGwmXjN)).

```js
function debounce_leading(func, timeout = 300){
  let timer;
  return (...args) => {
    if (!timer) {
      func.apply(this, args);
    }
    clearTimeout(timer);
    timer = setTimeout(() => {
      timer = undefined;
    }, timeout);
  };
}
```

Here we trigger the `saveInput()` function on the first `debounce_leading` call caused by the first button click. We schedule the timer destruction for 300 ms. Every subsequent button click within that timeframe will already have the timer defined and will only push the destruction 300 ms to the future.

## Debounce implementations in libraries

In this article, I showed you how to implement a debounce function in JavaScript and use it to, well, debounce events triggered by website elements. 

However, you don’t need to use your own implementation of _debounce_ in your projects if you don’t want to. Widely used JS libraries already contain its implementation. Here are a few examples:

<table style="border-spacing: 0; border-collapse: collapse;"><tbody><tr><td style="padding: 4px; border: 1px solid black;"><em><strong>Library</strong></em></td><td style="padding: 4px; border: 1px solid black;"><em><strong>Example</strong></em></td></tr><tr><td style="padding: 4px; border: 1px solid black;"><a href="http://benalman.com/projects/jquery-throttle-debounce-plugin/">jQuery (via library)</a></td><td style="padding: 4px; border: 1px solid black;"><code>$.debounce(300, saveInput);</code></td></tr><tr><td style="padding: 4px; border: 1px solid black;"><a href="https://lodash.com/docs/4.17.15#debounce">Lodash</a></td><td style="padding: 4px; border: 1px solid black;"><code>_.debounce(saveInput, 300);</code></td></tr><tr><td style="padding: 4px; border: 1px solid black;"><a href="https://underscorejs.org/#debounce">Underscore</a></td><td style="padding: 4px; border: 1px solid black;"><code>_.debounce(saveInput, 300);</code></td></tr></tbody></table>


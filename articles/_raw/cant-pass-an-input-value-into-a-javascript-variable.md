---
title: Can't Pass an Input Value Into a JavaScript Variable
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:16:00.000Z'
originalURL: https://freecodecamp.org/news/cant-pass-an-input-value-into-a-javascript-variable
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa4740569d1a4ca26d3.jpg
tags:
- name: error
  slug: error
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
- name: variables
  slug: variables
seo_title: null
seo_desc: 'Imagine the following scenario – you have a simple input and a button.
  When a user types into the input and presses the button, the text from the input
  should be logged to the console.

  Here''s what you have so far:

  <input id="search" placeholder="Sear...'
---

Imagine the following scenario – you have a simple input and a button. When a user types into the input and presses the button, the text from the input should be logged to the console.

Here's what you have so far:

```html
<input id="search" placeholder="Search for..."></input>
<button value='send' id="submit" onclick="myFunction()">Search</button>

<div id="alpha"></div>
```

```js
function myFunction() {
  const test = document.getElementById("search").value;
}

console.log(test);
```

But when you load the page you see `Uncaught ReferenceError: test is not defined` in the console.

What's going on here, and why can't you access the `test` variable outside of `myFunction`?

## Scope in JavaScript

The reason you can't access `test` outside of `myFunction` is due to [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope). Another way to describe scope is context. 

Because `test` was defined or created within `myFunction`, it's only available in the context or scope of `myFunction` itself. Trying to log `test` outside of `myFunction` will cause an error.

Another way to put it is that the `test` variable is function scoped, and can only be logged from within `myFunction`.

An easy way to fix this is to log `test` from within `myFunction`. Then whenever the button is pressed, the current value of the input will be logged to the console:

```js
function myFunction() {
  const test = document.getElementById("search").value;
  console.log(test);
}
```

You can read more about scope in JavaScript here: [An introduction to scope in JavaScript](https://www.freecodecamp.org/news/an-introduction-to-scope-in-javascript-cbd957022652/)

## How to access a variable outside a function

While it's not possible to directly access a function scoped variable from outside the function it was defined in, there are some ways to use the value of `test` throughout the rest of the program.

### Store the value of `test` as a global variable

The global scope is the very top level of your program, outside of all other functions. Variables in the global scope are available throughout the rest of your program.

So an easy way to make `test` available everywhere is to save it as a global variable. For example:

```js
let test = '';

function myFunction() {
  test = document.getElementById("search").value;
}

function myOtherFunction() {
  console.log(test);
}
```

Then you'd be able to access the value of `test` when `myOtherFunction` is called. But this is assuming that the input already has some text in it, and that `myFunction`, which set's the value of `test`, is called before `myOtherFunction`.

That's where a solid understanding of asynchronous JavaScript comes in handy. Read more about it in this article: [The Evolution of Async JavaScript: From Callbacks, to Promises, to Async/Await](https://www.freecodecamp.org/news/the-evolution-of-async-javascript-from-callbacks-to-promises-to-async-await-e73b047f2f40/)

### Return test from the function

Another way you can access `test` from outside the original function it's defined in is to simply return it from that function. Then, when you call it from another function, you'll have access to `test`. 

Then you can create another button to append the value of `test` to the page and attach `myOtherFunction` to that button.

For example:

```html
<input id="search" placeholder="Search for..."></input>
<button value='send' id="submit" onclick="myFunction()">Search</button>
<button value='append' id="append" onclick="myOtherFunction()">Append</button>

<div id="alpha"></div>
```

```js
function myFunction() {
  const test = document.getElementById("search").value;
  return test;
}

function myOtherFunction() {
  const myDiv = document.getElementById("alpha");
  myDiv.innerText = myFunction();
}
```

And here it is in action:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Peek-2020-06-10-20-46.gif)


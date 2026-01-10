---
title: Pure vs Impure Functions in Functional Programming – What's the Difference?
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2021-08-09T21:06:46.000Z'
originalURL: https://freecodecamp.org/news/pure-function-vs-impure-function
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pure-function-vs-impure-function-codesweetly.png
tags:
- name: Functional Programming
  slug: functional-programming
seo_title: null
seo_desc: 'Pure functions and impure functions are two programming terms you will
  often see in functional programming.

  One core difference between these two types of functions is whether or not they
  have side effects.

  In this article, you will learn what side e...'
---

Pure functions and impure functions are two programming terms you will often see in functional programming.

One core difference between these two types of functions is whether or not they have side effects.

In this article, you will learn what side effects are and we'll discuss the differences between pure and impure functions.

Without any further ado, let's get started with side effects.

## What is a Side Effect?

A **side effect** occurs in a program whenever you use _external code_ in your function — which, as a result, impacts the function’s ability to perform its task.

So what exactly does this mean? Let's see with some examples.

### Side Effect Example 1: How to add an old value to a new one

```js
let oldDigit = 5;

function addNumber(newValue) {
  return oldDigit += newValue;
}
```

In the snippet above, `oldDigit`’s usage within the function gives `addNumber()` the following side effects:

#### First side effect: Dependency on oldDigit

The fact that `addNumber()` depends on `oldDigit` to successfully perform its duties means that whenever `oldDigit` is not available (or `undefined`), `addNumber()` will return an error.

#### Second side effect: Modifies external code

As `addNumber()` is programmed to mutate `oldDigit`’s [state](https://www.codesweetly.com/state-in-programming/), which implies that `addNumber()` has a side effect of manipulating some external code.

#### Third: Becomes a non-deterministic function

Using external code in `addNumber()` makes it a non-deterministic function — as you can never determine its output by solely reading it.

In other words, to be sure of `addNumber()`’s return value, you must consider other external factors — such as the current state of `oldDigit`.

Therefore, `addNumber()` is not independent — it always has strings attached.

### Side Effect Example 2: How to print text to your console

```js
function printName() {
  console.log("My name is Oluwatobi Sofela.");
}
```

In the snippet above, `console.log()`’s usage within `printName()` gives the function side effects.

#### How does console.log cause a function to have side effects?

A `console.log()` causes a function to have side effects because it affects the state of external code — that is, the [console object](https://developer.mozilla.org/en-US/docs/Web/API/console)'s state.

In other words, `console.log()` instructs the computer to alters the `console` object's state.

As such, when you use it within a function, it causes that function to:

1. Be dependent on the `console` object to perform its job effectively.
2. Modify the state of an external code (that is, the `console` object’s state).
3. Become non-deterministic — as you must now consider the `console`’s state to be sure of the function’s output.

Therefore, whenever you use _external code_ in your function, that code will cause **side effects**.

So how do side effects relate to pure and impure functions?

Let’s find out by looking at the definition of a pure function and its impure alternative.

## What is an Impure Function?

So now that we know what side effects in functions are, we can talk about impure (and pure) functions.

First, an **impure function** is a function that contains one or more side effects. 

Consider the JavaScript code below:

```js
const myNames = ["Oluwatobi", "Sofela"];

function updateMyName(newName) {
  myNames.push(newName);
  return myNames;
}
```

In the snippet above, `updateMyName()` is an impure function because it contains code (`myNames`) that mutates an external [state](https://www.codesweetly.com/state-in-programming/) — which gives `updateMyName()` some side effects.

## What is a Pure Function?

A **pure function** is a function without any side effects.

Consider the JavaScript code below:

```js
function updateMyName(newName) {
   const myNames = ["Oluwatobi", "Sofela"];
   myNames[myNames.length] = newName;
   return myNames;
}
```

In the snippet above, notice that `updateMyName()` does not depend on any external code to accomplish its duties. This makes it a _pure function_.

Wherever possible, you should use pure functions in your applications. Let's discuss some of the advantages you get by doing so.

## Advantages of Pure Functions

The following are some advantages of pure functions.

### Pure functions are independent

Pure functions do not affect any external state, and they are also not affected by external code.

In other words, all external data a pure function uses gets received as parameters — they are not _explicitly used internally_.

Therefore, what you see within is what you get — there are absolutely no strings attached.

As such, you don’t need to look for external conditions (states) that might impact your pure function's effective operation as all activities happen within.

### Pure functions are easier to read

Pure functions are easier to read and debug than their impure alternatives.

Pure functions are so readable because they are solely dependent on themselves — they neither affect nor are they impacted by external states.

## Important Stuff to Know about Pure Functions

Keep these three essential pieces of info in mind whenever you choose to use pure functions.

### You can clone an external state into a pure function

Cloning an external state into a pure function does not make the function impure.

State duplication is simply a copy-and-paste operation that does not leave any strings attached between the source and its clone.

**Example:**

```js
const myBio = ["Oluwatobi", "Sofela"];

function updateMyBio(newBio, array) {
  const clonedBio = [...array];
  clonedBio[clonedBio.length] = newBio;
  return clonedBio;
}

console.log(updateMyBio("codesweetly.com", myBio));
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-blhtpi?file=script.js)

In the snippet above, `updateMyBio()` used the [spread operator](https://www.codesweetly.com/spread-operator/) to duplicate `myBio`’s state into `clonedBio`. However, it is still a pure function because it is neither dependent on `myBio` nor does it modify any external code.

Instead, it is an exclusively deterministic function programmed to use the cloned version of its array parameter.

### Avoid code mutations in pure functions

Technically, you can mutate variables defined locally within a pure function’s scope. However, it is best to avoid doing so.

For instance, consider the code below:

```js
const compBio = ["code", "sweetly"];

function updateCompBio(newBio, array) {
  const clonedBio = [...array];
  clonedBio[clonedBio.length] = newBio;
  return clonedBio;
}

console.log(updateCompBio(".com", compBio));
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-dprdlf?file=script.js)

In the snippet above, `updateCompBio()` is a pure function that uses `clonedBio[clonedBio.length] = newBio` to alter its local state.

Although such an operation does not make `updateCompBio()` impure, it is not the best practice.

The recommended way to write a pure function is to make it receive _all_ its values as parameters like so:

```js
const compBio = ["code", "sweetly"];

function updateCompBio(newBio, array) {
  return [...array, newBio];
}

console.log(updateCompBio(".com", compBio));
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-gyl8sy?file=script.js)

Notice how clean and portable our code now looks. This is an advantage of making your pure function receive all its values as parameters. By so doing, you will also find it easier to debug your code.

### The same input will always return the same output

A vital trait about pure functions is that they will always return the same value with the same set of inputs — no matter how many times you invoke them.

## Wrapping it up

Your function is **pure** if it does not contain any external code. Otherwise, it is **impure** if it includes one or more side effects.

In this article we discussed what pure and impure functions are, and we learned about the advantages using pure functions can bring to your code.

Thanks for reading!


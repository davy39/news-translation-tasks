---
title: JavaScript Promises – The promise.then, promise.catch and promise.finally Methods
  Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-16T18:30:06.000Z'
originalURL: https://freecodecamp.org/news/javascript-promise-methods
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-pixabay-532414.jpg
tags:
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: null
seo_desc: 'By Dillion Megida

  A promise is an object in JavaScript that will produce a value sometime in the future.
  This usually applies to asynchronous operations.

  In applications, asynchronous operations happen a lot. This can be API requests,
  delayed data pr...'
---

By Dillion Megida

A promise is an object in JavaScript that will produce a value sometime in the future. This usually applies to asynchronous operations.

In applications, asynchronous operations happen a lot. This can be API requests, delayed data processing, and much more. 

Instead of having to block code execution until the data loads, you can define them as promises, so that code execution continues with other parts of the code. And when the promises complete, you can use the data in them.

You can learn more about [promises in this simplified article](https://dillionmegida.com/p/javascript-promises/).

In some cases a promise passes, and in other cases it fails. How do you handle the result from each outcome?

For the rest of this article, we will understand the `then`, `catch` and `finally` methods of promises.

## The states of promises in JavaScript

A promise has three states:
* **pending**: the promise is still in the works
* **fulfilled**: the promise resolves successfully and returns a value
* **rejected**: the promise fails with an error

The **fulfilled** and **rejected** states have one thing in common: whether a promise is fulfilled or rejected, the promise is **settled**. So a settled state could either be a fulfilled or a rejected promise.

## When a promise is fulfilled

When a promise is fulfilled, you can access the resolved data in the `then` method of the promise:

```js
promise.then(value => {
 // use value for something
})
```

Think of the `then` method as "this works and **then** do this with the data returned from the promise". If there is no data, you can skip the `then` method.

It's also possible that the `then` method can return another promise, so you can chain another `then` method like this:

```js
promise
  .then(value => {
    return value.anotherPromise()
  })
  .then(anotherValue => {
    // use this value
  })
```

## When a promise is rejected

When a promise is rejected (that is, the promise fails), you can access the error information returned in the `catch` method of the promise:

```js
promise.catch(error => {
  // interpret error and maybe display something on the UI
})
```

Promises can fail for different reasons. For API requests, it can be a failed network connection, or a returned error from the server. Such promises will be rejected if they get errors.

Think of the `catch` method as "this does not work so I **catch** the error so that it does not break the application". If you do not catch the error, this can break your application in some cases.

## When a promise settles

There's a last stage of the promise. Whether the promise is fulfilled or is rejected, the promise has been completed (has been **settled**). At this completed stage, you can `finally` do something.

The `finally` method of promises is useful when you want to do something after the promise has settled. This can be cleanup or code you may want to duplicate in the `then` and `catch` methods.

For example, instead of doing:

```js
let dataIsLoading = true;

promise
  .then(data => {
    // do something with data
    dataIsLoading = false;
  })
  .catch(error => {
   // do something with error
   dataIsLoading = false;
  })
```

You can use the `finally` method like this:

```js
let dataIsLoading = true;

promise
  .then(data => {
    // do something with data
  })
  .catch(error => {
   // do something with error
  })
  .finally(() => {
    dataIsLoading = false;
  })
```

The `finally` method is called regardless of the outcome (fulfilled or rejected) of the promise.

## Wrap up

Promises have the `then`, `catch` and `finally` methods for doing different things depending on the outcome of a promise. In summary:

* `then`: when a promise is successful, you can **then** use the resolved data
* `catch`: when a promise fails, you **catch** the error, and do something with the error information
* `finally`: when a promise settles (fails or passes), you can **finally** do something



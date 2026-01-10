---
title: Callbacks and Promises Living Together in API Harmony
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-19T23:38:01.000Z'
originalURL: https://freecodecamp.org/news/callbacks-and-promises-living-together-in-api-harmony-7ed26204538b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Xc0Degaa5ZyZGmnVAI5_eQ.png
tags:
- name: api
  slug: api
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ethan Arrowood

  In this article, we''ll learn how to update a callback-based API to support Promises
  as well.

  First, what is an API, or application programming interface? It''s sometimes referred
  to as a module. It is a collection of methods and vari...'
---

By Ethan Arrowood

In this article, we'll learn how to update a callback-based API to support Promises as well.

First, what is an API, or application programming interface? It's sometimes referred to as a _module_. It is a collection of methods and variables developers can utilize in their own application.

Watch the accompanying Real Coding episode [here](https://youtu.be/6DphXwRbPlo).

### Callback Functions

Many JavaScript API’s and modules provide a final parameter in their methods for something called a callback method. Most of the time you’ll see this defined as `done`, `next`, `callback`, or `cb` (abbreviation for callback). Callback functions are incredibly useful because they enable other developers get more out of your function such as error handling and asynchronous requests. 

For example, an API method may produce a variety of errors and these errors, if not properly handled, can bring down an entire application. An API utilizing callback methods **should** be returning all `Error` objects as the first parameter in the callback. It is assumed that the first parameter in a callback function is always an error instance.

The function below is a simple example. Its purpose is to double the parameter `x` and return it via the specified `callback` function. `error` starts as `null`. If any of the conditional checks fail, an `Error` instance is assigned to `error` . Then if `error` exists (it is not null or undefined), then we do not double `x` and we set the variable `double` as `null`; otherwise, `x` is doubled and assigned to the `double` variable. After everything is done the function `doublePositiveOnly` will return the callback method with the first parameter referencing the `error` variable and the second parameter referencing the `double` variable.

```js
function doublePositiveOnly(x, callback) {
  let error
  if ( !x )
    error = new Error('x must be defined')
  if ( typeof x !== 'number' )
    error = new Error('x must be a number')
  if ( x < 0 )
    error = new Error('x must be positive')
    
  const double = error ? null : x * 2
  
  return callback(error, double)
}
```

How would you use this function?

```js
doublePositiveOnly(16, function (err, result) {
  if (err) console.error(err.message)
  console.log(result)
})
```

### Promise Functions

Promise functions in production are easy to recognize as they utilize `.then` and `.catch` methods to return information back to the user. Nearly all callback functions can be replaced by promises, so lets rebuild our `doublePositiveOnly` method using promises.

```js
function doublePositiveOnly( x ) {
  return new Promise(function (resolve, reject) {
    let error
    if ( !x )
      error = new Error('x must be defined')
    if ( typeof x !== 'number' )
      error = new Error('x must be a number')
    if ( x < 0 )
      error = new Error('x must be positive')
      
    error ? reject(error) : resolve(x * 2)
  })
}
```

The above function serves the exact same purpose of the callback implementation. However, this version no longer takes a callback method as a parameter. Instead it either `rejects` an error or `resolves` the result. You can use this method like so:

```js
doublePositiveOnly(16).then(function (result) {
  // do cool stuff with the result
  console.log(result)
}).catch(function (err) {
  // oh no an error! Handle it however you please
  console.error(err.message) 
})
```

The readability of a Promise function is much clearer than a callback function as you can easily handle the result as well as any potential errors. There is a lot more to Promises functions I did not cover here, and I encourage you to [learn](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) as much as you can about them.

### Callbacks and Promises Together

We have callbacks and we have promises. They are interchangeable and both satisfy similar needs. Now consider the scenario where we have an API that only supports callback methods. This API is downloaded 1000x times and is now running in production on countless applications. But now the maintainer wants to support Promises as well. Can they do this while also maintaining callback support? **YES!**

Lets look at the callback implementation of `doublePositiveOnly` once again, but now also with promise support:

```js
function doublePositiveOnly(x, callback) {
  const func = this.doublePositiveOnly
  
  if ( callback === undefined ) {
    return new Promise(function (resolve, reject) {
      func(x, function (err, result) {
        err ? reject(err) : resolve(result)
      })
    })
  }
  
  let error
  if ( !x )
    error = new Error('x must be defined')
  if ( typeof x !== 'number' )
    error = new Error('x must be a number')
  if ( x < 0 )
    error = new Error('x must be positive')
  
  const double = error ? null : x * 2
  
  return callback(error, double)
}
```

And just like that the `doublePositiveOnly` method now supports promises as well. It works because first it stores the reference to the function in the `func` variable. Next, it checks if a callback was passed to the function. If not it returns a promise that passes down the `x` parameter to another `doublePositiveOnly` call, and it includes a callback function. This callback function either `rejects` or `resolves` the promise just like the promise-only implementation did.

What is great about this solution is you can use just about anywhere and you don’t have to edit any parts of the original function! You can see it in action in a module I recently contributed to called [fastify-jwt](https://github.com/fastify/fastify-jwt/). Both the `[requestVerify](https://github.com/fastify/fastify-jwt/blob/master/jwt.js#L108-L114)` and `[replySign](https://github.com/fastify/fastify-jwt/blob/master/jwt.js#L79-L85)` methods support both callbacks and promises.

If you have any questions please reach out!

You can follow me on [Github](https://github.com/Ethan-Arrowood) and [Twitter](https://twitter.com/ArrowoodTech) or check out my [website](https://ethanarrowood.com).

Keep up the good work.

~Ethan Arrowood


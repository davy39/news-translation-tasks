---
title: How to go from Callbacks to Async Await in Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T18:03:44.000Z'
originalURL: https://freecodecamp.org/news/moving-from-callbacks-to-async-await-in-node-c3da26460dd1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ImJyPIRNLiLXjGSfJQl_dA.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nitish Phanse

  I recently got a chance to work with Node again. Being a huge fan of promises, I
  never tried async await. Why? Because promises worked fine for me, that’s why.

  Sure thing promises work fine for simple controllers. Couple database que...'
---

By Nitish Phanse

I recently got a chance to work with Node again. Being a huge fan of promises, I never tried async await. Why? Because promises worked fine for me, that’s why.

Sure thing promises work fine for simple controllers. Couple database querying and error handling, then promises can be nasty. Yes even if you chain them. What if some resolved value in your second promise chain was needed in your fourth promise? But again I’d usually hack my way through (_define a let variable at the top of the function scope and reassign it and then use it further_).

### Use Case Definition

I am creating a simple API spec, where the route is `**POST /users**` . The post body has some user details. If the user exists in the database, its values get updated else a new entry is created in the database.

For the sake of simplicity, I am not using any ORM / database. I am creating a dummy user model and using `setTimeout` to mock API calls and DB queries. I am also using `Math.random()` to decide whether to throw an error for the case of error handling.

> I will be making these calls first via callbacks, then promises, and lastly using async/await.

Ok time for some code now.

#### **Simple express server**

#### **User Model**

This user model code is a dummy user object which will make mock API calls. There are two types of calls being made: one with callbacks and the other with promises. Both are effectively doing the same thing. Again I’ve hardcoded a lot of stuff here for the sake of simplicity.

### Callbacks

The traditional way of doing any sort of non-blocking I/O was with a callback where any I/O call was of the form

```
someAsyncOperation(dataObject, function(error, success) {
```

```
  if (error) {    // handle error  } else {    // do something with success  }})
```

This works well if you are performing one async operation. If you end up doing multiple async ops with callbacks, you will end up with what is known as the _callback pyramid of hell_.

#### **_Pros:_**

1. Handy for single async operations. Allow easy data and error control.
2. Should work on every node version and almost all packages of node. As callbacks are functions, they don’t need any transpilers.

#### **_Cons:_**

1. For multiple nested async operations this creates a callback hell
2. Error handling has to be done for each operation (no global exception handler)

### Promises

Promises are objects which have 3 main states — pending, resolved and rejected. Depending on the response of an async action a promise is either resolved or rejected. Multiple promises can be chained one below the other. A single catch handler at the bottom is sufficient for an error in any promise.

#### **_Pros:_**

1. Allows for easy chaining of async operations. Whatever is returned in the `.then` function, can be chained in the next `.then` function.
2. One catch handler at the bottom will catch an error if either of the chained promises throws an exception.

#### **_Cons:_**

1. Most libraries may require a promisify wrapper around it like bluebird, unless they support promises out of the box.
2. The scope of a chained function is isolated to that function itself. So some data resolved in the second chain cannot be used in the 4th chain unless a global let variable is declared.

### Async / Await

Async / await at the end of the day is still a promise. It’s just a way of writing asynchronous code in a sort of synchronous manner.

Each async function has to be prefixed with `async`. Every asynchronous action in it has to be prefixed with the word `await` . Also, every async function returns a promise which can be resolved further.

#### **_Pros:_**

1. CLEAN LOOKIN CODE. I cannot stress on this point enough. All of the resolved bit can be accessed within the try block.
2. Entire block can be treated as a synchronous bit of code. (Though it is async in nature).
3. Adding try, catch to asynchronous code.
4. One unified error handler in the catch block.

#### **_Cons:_**

1. Node 8+ comes with async await built in. For older versions, a babel transpiler is needed for server-side code.
2. Adding the async keyword is not very intuitive.
3. Using async/await inside a promise constructor is an anti-pattern.

4. Again, for some libraries supporting only callbacks, a global promisify library may be needed to support async / await

### **Conclusion**

In conclusion, I’d say we converted a particular use case from one form of callbacks to promises to finally async await.

Overall, my take on this is that I found the async await code to be really clean and easy to understand. Since people want to learn Node, they find the asynchronous bit an intimidating task. Also, people from a Java, PHP or even a Python background can easily get started with making apps in node without worrying about callbacks / promises.

Hope this article was helpful. In case there are any errors, please let me know. Would be happy to correct them.


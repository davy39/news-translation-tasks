---
title: How to Use JavaScript Promises – Callbacks, Async/Await, and Promise Methods
  Explained
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2023-08-15T16:03:55.000Z'
originalURL: https://freecodecamp.org/news/javascript-promises-async-await-and-promise-methods
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/promises_async_methods.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'In this tutorial, you will learn everything you need to know about using
  promises and async/await in JavaScript.

  So let''s get started.

  If you''d like to learn along with a video version of this tutorial, you can also
  check out my YouTube playlist.

  Why...'
---

In this tutorial, you will learn everything you need to know about using promises and async/await in JavaScript.

So let's get started.

If you'd like to learn along with a video version of this tutorial, you can also check out my [YouTube playlist](https://www.youtube.com/watch?v=4jaiXP6vU2w&list=PLSJnlFr3D-mGIHFpo80ylsaBErtueSpYS&index=14).

## Why Use Promises in JavaScript?

ES6 introduced promises as a native implementation. Before ES6 we were using callbacks to handle asynchronous operations.

Let’s understand what callbacks are and what problem related to callbacks is solved by promises.

Let's say we have a list of posts and their respective comments, like this:

```js
const posts = [
  { post_id: 1, post_title: 'First Post' },
  { post_id: 2, post_title: 'Second Post' },
  { post_id: 3, post_title: 'Third Post' },
];

const comments = [
  { post_id: 2, comment: 'Great!'},
  { post_id: 2, comment: 'Nice Post!'},
  { post_id: 3, comment: 'Awesome Post!'},
];
```

Now, we will write a function to get a post by passing the post id. If the post is found, we will retrieve the comments related to that post.

```js
const getPost = (id, callback) => {
 const post = posts.find( post => post.post_id === id);
 if(post) {
   callback(null, post);
 } else {
   callback("No such post found", undefined);
 }
};

const getComments = (post_id, callback) => {
 const result = comments.filter( comment => comment.post_id === post_id);
 if(result) {
   callback(null, result);
 } else {
   callback("No comments found", undefined);
 }
}
```

In the above `getPost` and `getComments` functions, if there is an error we will pass it as the first argument. But if we get the result, we will call the callback function and pass the result as the second argument to it.

If you are familiar with Node.js, then you will know that this is a very common pattern used in every Node.js callback function.

Now let’s use those functions:

```js
getPost(2, (error, post) => {
    if(error) {
     return console.log(error);
    }
    console.log('Post:', post);
    getComments(post.post_id, (error, comments) => {
        if(error) {
          return console.log(error);
        }
        console.log('Comments:', comments);
    });
});
```

After executing the above code, you will see the following output:

![Image](https://www.freecodecamp.org/news/content/images/2023/08/posts.jpg)
_Result of calling getPost and getComments function_

Here's a [CodePen Demo](https://codepen.io/myogeshchavan97/pen/PoweVgR?editors=0011#0).

As you can see, we have the `getComments` function nested inside the `getPost` callback. 

Now imagine if we also wanted to find the likes of those comments. That would also get nested inside `getComments` callback, creating more nesting. This will eventually make the code difficult to understand.

This nesting of the callbacks is known as **callback hell.**

You can see that the error handling condition also gets repeated in the code, which creates duplicate code – this is not good.

So to fix this problem and allow asynchronous operations, promises were introduced.

## What are Promises in JavaScript?

Promises are one of the most important parts of JavaScript – but they can be confusing and difficult to understand. Many new devs, as well as experienced ones, struggle to fully grasp them.

So what is a promise? A promise represents an asynchronous operation whose result will come in the future.

Before ES6, there was no way to wait for something to perform some operation. For example, when we wanted to make an API call, there was no way to wait until the results came back.

For that, we used to use external libraries like JQuery or Ajax which had their own implementation of promises. But there was no JavaScript implementation of promises.

But then promises were added in ES6 as a native implementation. And now, using promises in ES6, we can make an API call ourselves and wait until it's done to perform some operation.

## How to Create a Promise

To create a promise we need to use the `Promise` constructor function like this:

```js
const promise = new Promise(function(resolve, reject) {
 
});
```

The `Promise` constructor takes a function as an argument and that function internally receives `resolve` and `reject` as parameters.

The `resolve` and `reject` parameters are actually functions that we can call depending on the outcome of the asynchronous operation.

A `Promise` can go through three states:

* Pending
* Fulfilled
* Rejected

When we create a promise, it’s in a pending state. When we call the `resolve` function, it goes in a fulfilled state, and if we call `reject` it will go into the rejected state.

To simulate the long-running or asynchronous operation, we will use the `setTimeout` function.

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve(sum);
 }, 2000);
});

```

Here, we've created a promise which will resolve to the sum of `4` and `5` after a 2000ms (2 second) timeout is over.

To get the result of the successful promise execution, we need to register a callback handler using `.then` like this:

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve(sum);
 }, 2000);
});

promise.then(function(result) {
 console.log(result); // 9
});

```

So whenever we call `resolve`, the promise will return back the value passed to the `resolve` function which we can collect using the `.then` handler.

If the operation is not successful, then we call the `reject` function like this:

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5 + 'a';
  if(isNaN(sum)) {
    reject('Error while calculating sum.');
  } else {
    resolve(sum);
  }
 }, 2000);
});

promise.then(function(result) {
 console.log(result);
});

```

Here, if the `sum` is not a number, then we call the `reject` function with the error message. Otherwise, we call the `resolve` function.

If you execute the above code, you will see the following output:

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promises_fcc.png)
_Result of rejecting promise without catch handler_

As you can see, we're getting an uncaught error message along with the message we've specified because calling the `reject` function throws an error. But we have not added an error handler for catching that error.

To catch the error, we need to register another callback using `.catch` like this:

```js
promise.then(function(result) {
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

You will see the following output:

![Image](https://www.freecodecamp.org/news/content/images/2023/08/error_catch.png)
_Result of rejecting promise with catch handler_

As you can see, we have added the `.catch` handler, so we're not getting any uncaught error – we're just logging the error to the console.

This also avoids stopping your application abruptly.

So it's always recommended to add the `.catch` handler to every promise so your application will not stop running because of the error.

### When to Use `resolve` and `reject`

Let's take an example of an API call.

If you're making an API call and the API call is successful, then you call the `resolve` function by passing the result of the API as an argument to it.

And if the API is unsuccessful, then you call the `reject` function by passing any message as an argument to it.

So to indicate that the operation is successful, we call the `resolve` function and for indicating an unsuccessful operation, we call the `reject` function.

## What is Promise Chaining and Why is it Useful?

Promise chaining is a technique used to manage asynchronous operations in a more organized and readable way.

In promise chaining, we can attach multiple `.then` handlers in which result of previous `.then` handler is automatically passed to the next `.then` handler.

Using promise chaining helps to avoid the problem of callback hell which we have seen previously.

Promise chaining also allows us to write asynchronous code in a more linear and sequential manner, which is easier to read and understand.

Also, when using promise chaining, we can attach only one`.catch` handler at the end of all the `.then` handlers. If any of the in-between promises fail, the last `.catch` handler will be automatically executed.

So we don't need to add multiple `.catch` handlers. This eliminates multiple error check as we did in the callback hell example previously.

## How Promise Chaining Works

We can add multiple `.then` handlers to a single promise like this:

```js
promise.then(function(result) {
 console.log('first .then handler');
 return result;
}).then(function(result) {
 console.log('second .then handler');
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

When we have multiple `.then` handlers added, the return value of the previous `.then` handler is automatically passed to the next `.then` handler.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_chaining.png)
_Result of promise chaining_

As you can see, adding `4 + 5` resolves a promise and we get that sum in the first `.then` handler. There we're printing a log statement and return that sum to the next `.then` handler.

And inside the next `.then` handler, we're adding a log statement and then we're printing the result we got from the previous `.then` handler.

This way of adding multiple `.then` handlers is known as promise chaining.

## How to Delay a Promise's Execution in JavaScript

Many times we don't want the promise to execute immediately. Rather, we want it to delay until after some operation is completed.

To achieve this, we can wrap the promise in a function and return that promise from that function like this:

```js
function createPromise() {
 return new Promise(function(resolve, reject) {
  setTimeout(function() {
   const sum = 4 + 5;
   if(isNaN(sum)) {
     reject('Error while calculating sum.');
   } else {
    resolve(sum);
   }
  }, 2000);
 });
}

```

This way, we can use the function parameters inside the promise, making the function truly dynamic.

```js
function createPromise(a, b) {
 return new Promise(function(resolve, reject) {
  setTimeout(function() {
   const sum = a + b;
   if(isNaN(sum)) {
     reject('Error while calculating sum.');
   } else {
    resolve(sum);
   }
  }, 2000);
 });
}

createPromise(1,8)
 .then(function(output) {
  console.log(output); // 9
});

// OR

createPromise(10,24)
 .then(function(output) {
  console.log(output); // 34
});
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/general_function.png)
_Result of delaying promise execution_

**Note:** When we create a promise, it will be either resolved or rejected but not both at the same time. So we cannot add two `resolve` or `reject` function calls in the same promise.

Also, we can pass only a single value to the `resolve` or `reject` function.

If you want to pass multiple values to a `resolve` function, pass it as an object like this:

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve({
   a: 4,
   b: 5,
   sum
  });
 }, 2000);
});

promise.then(function(result) {
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/object_resolve.png)
_Passing object to resolve function to return multiple values_

## How to Use Arrow Functions in JavaScript

In all the above code examples, we've used regular ES5 function syntax while creating promises. 

But it's a common practice to use arrow function syntax instead of ES5 function syntax.

So let's first understand what is an arrow function and how to use it.

### What are arrow functions?

Before ES6, there were two main ways of declaring functions.

1. Function Declaration Syntax:

```js
function add(a, b) {
 return a + b;
}
```

2. Function Expression Syntax:

```js
const add = function(a, b) {
 return a + b;
};
```

**The** main visible **difference between the** regular **function and arrow function is the syntax of writing the function.**

Using arrow function syntax, we can write the above adding function like this:

```js
const add = (a, b) => {
 return a + b;
};
```

You might not see much difference here, apart from the arrow. But if we have a single line of code in the function body we can simplify the above arrow function like this:

```js
const add = (a, b) => a + b;
```

Here we are implicitly returning the result of `a + b`, so there is no need for a `return` keyword if there is a single statement.

So using the arrow functions will make your code much shorter.

If you want to learn other features of arrow functions, you can check out [this video](https://www.youtube.com/watch?v=tI87o_kDKN4&list=PLSJnlFr3D-mGIHFpo80ylsaBErtueSpYS&index=4).

Using an arrow function, we can write the previous code as shown below:

```js
const promise = new Promise((resolve, reject) => {
 setTimeout(() => {
  const sum = 4 + 5 + 'a';
  if(isNaN(sum)) {
    reject('Error while calculating sum.');
  } else {
    resolve(sum);
  }
 }, 2000);
});

promise.then((result) => {
 console.log(result);
});

```

You can either use ES5 or ES6 function syntax depending on your preferences and needs.

## How to Use Async/Await in JavaScript

In this section, we'll explore everything you need to know about async/await.

Async/await gives developers a better way to use promises.

To use async/await, you need to create a function and add the `async` keyword before the function name using ES5 function declaration syntax like this:

```js
async function someFunction() {
  // function body
}
```

or using function expression syntax like this:

```js
const someFunction = async function () {
  // function body
};
```

or using an arrow function like this:

```js
const someFunction = async () => {
  // function body
};
```

Always remember that, when you add the async keyword to the function, it always returns a promise.

Take a look at the below code:

```js
const sayHello = async function () {
  return 'Hello';
};

sayHello();
```

What do you think the output of the above code will be?

![Image](https://www.freecodecamp.org/news/content/images/2023/08/async_1.png)
_Result of calling function marked as async_

The output is a promise fulfilled with the string `Hello`.

So the below code:

```js
const sayHello = async function () {
  return 'Hello';
};
```

is the same as this:

```js
const sayHello = function() {
 return new Promise((resolve, reject) => {
  resolve('Hello');
 });
}
```

which is the same as this:

```js
const sayHello = function () {
  return Promise.resolve('Hello');
};
```

`Promise.resolve('Hello')` is just a shorter way of creating a promise which resolves to the string `Hello`.

So to get the actual string `Hello`, we need to add the `.then` handler like this:

```js
sayHello().then(function (result) {
  console.log(result); // Hello
});
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/async_hello.png)
_Getting result of async function using .then handler_

Now, where do we use the `await` keyword?

It's used inside the function which is declared as `async`. So the `await` keyword should only be used inside the `async` function.

You will get an error if you try to use it in non-async functions.

Suppose, we have a promise which returns the product of two numbers like this:

```js
function getProduct(a, b) {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      resolve(a * b);
    }, 1000);
  });
}
```

and we're using it like this:

```js
getProduct(2, 4)
  .then(function (result) {
    getProduct(result, 2)
      .then(function (finalResult) {
        console.log('final_result', finalResult);
      })
      .catch(function (error) {
        console.log(error);
      });
  })
  .catch(function (error) {
    console.log(error);
  });
```

In the above code, we're first getting the product of `2` and `4`. Then we're using that result to multiply it by `2` again, and then finally printing the product.

If you execute the above code, you will see the final result as 16 which is 2 * 4 = 8 and 8 * 2 = 16.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/async_product.png)
_Result of nesting .then callback handlers_

The above code of  `.then` and `.catch` looks pretty complicated and difficult to understand at one glance.

So using async/await we can simplify the above code to this:

```js
const printResult = async () => {
  try {
    const result = await getProduct(2, 4); // line 1
    const finalResult = await getProduct(result, 2); // line 2
    console.log('final_result', finalResult); // line 3
  } catch (error) {
    console.log(error);
  }
};

printResult();
```

This looks much cleaner and easy to understand.

Here, to use the `await` keyword, we're declaring a function with the `async` keyword. Then to get the result of each promise, we're adding the `await` keyword in front of it.

Also, note that we've added try/catch inside the function. You always need to add a try block around the code which uses `await` so the catch block will be executed if the promise gets rejected.

There is a very important thing you need to remember: The above async/await code will work exactly the same as when we use `.then` – so the next `await` line (line 2) will not be executed until the previous `await` call (line 1) is successful.

Therefore, as the `getProduct` function is taking 1 second to execute because of the setTimeout call, line 2 will have to wait for 1 second before executing the `getProduct` function again.

But there is one exception to this behavior, which you can check out in [this article](https://levelup.gitconnected.com/common-gotcha-with-promises-693a993568c2?source=friends_link&sk=32d92e34511f72cbcc399cded49348c8).

Also, if there is an error while executing line 1 (because of some error that occurred in the `getProduct` function), the next code after line 1 will not be executed. Instead, the catch block will be executed.

Now, if you compare the code of promise chaining and async/await, you will see the difference.

```js
// code using async/await

const printResult = async () => {
  try {
    const product = await getProduct(2, 4); // line 1
    const finalResult = await getProduct(product, 2); // line 2
    console.log('final_result', finalResult); // line 3
  } catch (error) {
    console.log(error);
  }
};

printResult();
```

```js
// code using .then and .catch

getProduct(2, 4)
  .then(function (result) {
    getProduct(result, 2)
      .then(function (finalResult) {
        console.log('final_result', finalResult);
      })
      .catch(function (error) {
        console.log(error);
      });
  })
  .catch(function (error) {
    console.log(error);
  });
```

As you can see, the code using async/await is much cleaner and easy to understand as compared to the promise chaining.

As the nesting gets deeper, the code using promise chaining gets more complicated. So async/await just provides a way to write the same code but with better clarity.

Using async/await also reduces the need of adding multiple `.catch` handlers to handle the errors.

We can avoid the nesting in the above promise chaining by writing the previous code like this:

```js
getProduct(2, 4)
  .then(function (result) {
    return getProduct(result, 2);
  })
  .then(function (finalResult) {
    console.log('final_result', finalResult);
  })
  .catch(function (error) {
    console.log(error);
  });
```

Here, from the first `.then` handler, we're returning the result of `getProduct(result, 2)`.

Whatever returned from the previous `.then` handler will be passed to the next `.then` handler.

As the `getProduct` function returns a promise so we can attach `.then` again to it and avoid the need for a nested `.catch` handler.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/avoid_nested_handlers.png)
_using promise chaining_

But still async/await syntax looks cleaner and easier to understand than the promise chaining syntax.

## Promise Methods

In this section, we'll explore the various methods provided by the Promise API.

All these methods are useful when you want to execute multiple asynchronous tasks at the same time when those tasks are not dependent on each other (which saves a lot of time).

Because if you execute each task one after the other, then you have to wait for the previous task to finish before you can start with the next task.

And if the tasks are not related to each other, there is no point in waiting for the previous task to finish before executing the next task.

### The `Promise.all` method

This method is used to execute multiple asynchronous tasks simultaneously without having to wait for another task to finish.

Suppose we have three promises and all are resolved successfully:

```js
const promise1 = new Promise((resolve, reject) => resolve('promise1 success'));
const promise2 = new Promise((resolve, reject) => resolve('promise2 success'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));
```

Now, let's use the `Promise.all` method.

`Promise.all` needs an array of promises as its argument.

```js
Promise.all([promise1, promise2, promise3])
  .then((result) => {
    console.log('resolved', result); // resolved ["promise1 success", "promise2 success", "promise3 success"]
  })
  .catch((error) => {
    console.log('rejected', error);
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_all.png)

As all the promises are resolved, `result` will be an array containing the results of the resolved promises.

Now, what if any of the promises get rejected?

```js
const promise1 = new Promise((resolve, reject) => resolve('promise1 success'));
const promise2 = new Promise((resolve, reject) => reject('promise2 failure'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));

Promise.all([promise1, promise2, promise3])
  .then((result) => {
    console.log('resolved', result);
  })
  .catch((error) => {
    console.log('rejected', error); // rejected promise2 failure
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_all_rejected.png)

In the above code, promise2 is rejected so the catch handler will be executed, and in the case of `Promise.all`:

*  If one of the promises is rejected, the `error` will contain the error message of the failed promise (as in our case above)
*  If multiple promises are rejected, the `error` will be the error message of the first failed promise.

Note: Even though the intermediate promise gets rejected, all next promises will not be stopped from executing. They will all be executed – but only the first rejected promise value will be available in the error parameter of the catch block.

### The `Promise.race` method

Consider again the three resolved promises:

```js
const promise1 = new Promise((resolve, reject) => resolve('promise1 success'));
const promise2 = new Promise((resolve, reject) => resolve('promise2 success'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));

Promise.race([promise1, promise2, promise3])
  .then((result) => {
    console.log('resolved', result); // resolved promise1 success
  })
  .catch((error) => {
    console.log('rejected', error);
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_race_success.png)

As you can see here, as soon as the first promise gets resolved, the `Promise.race` method will return the result of that resolved promise. 

Now, take a look at the below code:

```js
const promise1 = new Promise((resolve, reject) => reject('promise1 failure'));
const promise2 = new Promise((resolve, reject) => resolve('promise2 success'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));

Promise.race([promise1, promise2, promise3])
  .then((result) => {
    console.log('resolved', result);
  })
  .catch((error) => {
    console.log('rejected', error); // rejected promise1 failure
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_race_failed.png)

As you can see here, the first promise itself is rejected so the `.catch` handler will be executed.

So when we use the `Promise.race` method, it will wait until the first promise gets resolved or rejected and then:

*  If the first promise in the promise chain gets resolved, the `.then` handler will be executed and the result will be the result of the first resolved promise.
*  If the first promise in the promise chain gets rejected, the `.catch` handler will be executed and the result will be the result of the first failed promise.
* If multiple promises are rejected, the `.catch` handler will be executed and the result will be the result of the first failed promise.

### The `Promise.allSettled` method

This method is useful when you want to know the result of each task even though they are rejected.

Because in `Promise.all` and `Promise.race`, we get only the result of the first rejected promise and there is no way to get the result of other successful or failed promises.

So using `Promise.allSettled` we can get the result of all the promises, even if they failed.

Take a look at the below code:

```js
const promise1 = new Promise((resolve, reject) => resolve('promise1 success'));
const promise2 = new Promise((resolve, reject) => resolve('promise2 success'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));

Promise.allSettled([promise1, promise2, promise3]).then((result) => {
  console.log('resolved', result);
});

/* output from `.then`:
resolved [
  {
    "status": "fulfilled",
    "value": "promise1 success"
  },
  {
    "status": "fulfilled",
    "value": "promise2 success"
  },
  {
    "status": "fulfilled",
    "value": "promise3 success"
  }
]
*/
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_allsettled_success.png)

As you can see, the `Promise.allSettled` method waits until all the promises are resolved or rejected and the `result` will contain the result of each promise.

```js
const promise1 = new Promise((resolve, reject) => reject('promise1 failure'));
const promise2 = new Promise((resolve, reject) => resolve('promise2 success'));
const promise3 = new Promise((resolve, reject) => resolve('promise3 success'));

Promise.allSettled([promise1, promise2, promise3]).then((result) => {
  console.log('resolved', result);
});

/* output from `.then`:
resolved [
  {
    "status": "rejected",
    "reason": "promise1 failure"
  },
  {
    "status": "fulfilled",
    "value": "promise2 success"
  },
  {
    "status": "fulfilled",
    "value": "promise3 success"
  }
]
*/
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_allsettled_failure.png)

In the above case, even though the first promise is rejected, we get the result of all the promises inside the `.then` handler.

```js
const promise1 = new Promise((resolve, reject) => reject('promise1 failure'));
const promise2 = new Promise((resolve, reject) => reject('promise2 failure'));
const promise3 = new Promise((resolve, reject) => reject('promise3 failure'));

Promise.allSettled([promise1, promise2, promise3]).then((result) => {
  console.log('resolved', result);
});

/* output from `.then`:
 resolved [
  {
    "status": "rejected",
    "reason": "promise1 failure"
  },
  {
    "status": "rejected",
    "reason": "promise2 failure"
  },
  {
    "status": "rejected",
    "reason": "promise3 failure"
  }
] 
*/
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/promise_allsettled_multiple_failure.png)

Here, even though all the promises are rejected, still the `.then` handler will be executed and we get the result of each promise.

Want to learn how to use these promise methods in an actual React application? Check out my [previous article](https://www.freecodecamp.org/news/how-to-build-a-hacker-news-clone-using-react/).

## **Thanks for Reading!**

That's it for this tutorial. I hope you learned a lot from it.

Want a video version of this tutorial, check out my Y[ouTube playlist](https://bit.ly/3E00PlH).

If you want to master JavaScript, ES6+, React and Node.js with easy-to-understand content, do check out my [YouTube channel](https://www.youtube.com/@codingmastery_dev/) and don't forget to subscribe.

Want to stay up to date with regular content regarding JavaScript, React, Node.js? [Follow me on LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).


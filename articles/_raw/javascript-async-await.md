---
title: How to Use Async/Await in JavaScript – Explained with Code Examples
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-12-15T15:33:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-async-await
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/js-async-await.png
tags:
- name: async/await
  slug: asyncawait
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Hello friends! In this article, I''m going to show you how to use the “async/await”
  special syntax when handling JavaScript Promises.

  If you don''t know or need a refresher on JavaScript promises, you can read my previous
  article: How JavaScript Promis...'
---

Hello friends! In this article, I'm going to show you how to use the “async/await” special syntax when handling JavaScript Promises.

If you don't know or need a refresher on JavaScript promises, you can read my previous article: [How JavaScript Promises Work – Tutorial for Beginners](https://www.freecodecamp.org/news/javascript-promise-object-explained/).

You'll need to understand JavaScript promises well before learning the async/await syntax.

## How async/await Works

The async/await syntax is a special syntax created to help you work with promise objects. It makes your code cleaner and clearer.

When handling a `Promise`, you need to chain the call to the function or variable that returns a `Promise` using `then/catch` methods.

When you have many promises, you will also need lots of `then` method chains. For example, here's how you might retrieve data using the `fetch()` function:

```js
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(json => console.log(json))
  .catch(error => console.log(error));
```

In the code above, the `fetch()` function returns a `Promise`, which we handle using the `then()` method. Inside the first `then()` method, we accept the `response` from the request and convert it into an object using the `json()` method.

In the second `then()` method, we receive the returned `json` data from the call to the `json()` method, then log that data to the console.

We also add the `catch()` method to handle any error that might happen when running the request.

The code is really not hard to understand, but we can make it even prettier by removing the `.then()` and `.catch()` chains, which also removes the callback functions.

### The Await Keyword

The `await` keyword basically makes JavaScript wait until the `Promise` object is resolved or rejected. Instead of having to use the callback pattern inside the `then()` method, you can assign the fulfilled promise into a variable like this:

```js
const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
const json = await response.json();
console.log(json)

```

The `await` keyword is placed before the call to a function or variable that returns a promise. It makes JavaScript wait for the promise object to settle before running the code in the next line.

Now if you run the code above, you might get an error like this:

```txt
SyntaxError: await is only valid in async functions and the top level bodies of modules

```

This error occurs because the `await` keyword must be used inside an asynchronous function or a module.

### The Async Keyword

To create an asynchronous function, you need to add the `async` keyword before your function name. Take a look at line 1 in the example below:

```js
async function runProcess() {
  const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  const json = await response.json();
  console.log(json)
}

runProcess();

```

Here, we created an asynchronous function called `runProcess()` and put the code that uses the `await` keyword inside it. We can then run the asynchronous function by calling it, just like a regular function.

## How to Handle Errors in Async/Await

To handle an error that might occur from the async/await syntax, you can use the try/catch block to catch any rejection from your promise.

See the example below:

```js
async function runProcess() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.log(error);
  }
}

runProcess();

```

The try/catch block, put inside the `runProcess()` function, will handle the rejection that comes from the promise objects.

Now we have a complete async/await version of the standard Promise code we created earlier. Here's a comparison between the two:

![Image](https://www.freecodecamp.org/news/content/images/2023/12/PROMISE---ASYNC.png)
_Promise vs Async/Await Code Comparison_

In the async/await version, the result of the promise is directly assigned to a variable. In the standard promise version, the result of the promise is passed as an argument to the `.then()` method. 

Most developers prefer the async/await version as it looks more straightforward.

## How to Use Async/Await in IIFE and Arrow Functions

An Immediately Invoked Function Expression (IIFE) is a technique used to execute a function immediately as soon as you define it.

Unlike regular functions and variables, IIFEs will be removed from the running process once they are executed.

Aside from the standard function, you can also make an asynchronous IIFE. This is useful when you need to run the asynchronous function only once:

```js
(async function () {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.log(error);
  }
})();

```

You can also use the arrow syntax when creating an asynchronous function as follows:

```js
const runProcess = async () => {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.log(error);
  }
};

runProcess();

```

Feel free to use the syntax you want in your code.

## Why Use the async/await Syntax?

The async/await syntax enables you to handle promises without using `.then()` and `.catch()` method chaining, which also removes the need for nested callbacks.

This benefit is significant when you have a complex process after the promise is settled. 

Going back to our example above, suppose you have a conditional statement inside the `.then()` method as follows:

```js
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(json => {
    if (json.userId == 1) {
      json.completed == false;
    } else {
      json.completed == true;
    }
  })
  .catch(error => console.log(error));
```

Here, you can see that the callback function that accepts the `json` data has an if/else block inside it. 

This code is hard to reason with and modify when compared to the async/await version as follows:

```js
(async function () {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const json = await response.json();
    if (json.userId == 1) {
      json.completed == false;
    } else {
      json.completed == true;
    }
    console.log(json);
  } catch (error) {
    console.log(error);
  }
})();
```

By using the async/await syntax, you reduce the need for method chaining and nested callbacks. This impact the readability of your code, especially when you have nested code like if/else and a for loop block.

## Conclusion

Now you've learned how the async/await syntax works. The syntax makes working with promises much easier by removing the need for `.then()` and `.catch()` method chaining, which also removes the need for nested callbacks.

Even though the `await` keyword can only be used inside an `async` function, you can use an IIFE to invoke the async function only once.

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!


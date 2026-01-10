---
title: How JavaScript Promises Work – Tutorial for Beginners
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-11-29T15:55:31.000Z'
originalURL: https://freecodecamp.org/news/javascript-promise-object-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/js-promise.png
tags:
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: null
seo_desc: 'Hi everyone! In this article, I’m going to teach you one of the most confusing
  JavaScript topics, which is the Promise object. Promises may seem difficult at first,
  but they''re actually quite simple once you understand how they work.

  Here''s what we''l...'
---

Hi everyone! In this article, I’m going to teach you one of the most confusing JavaScript topics, which is the Promise object. Promises may seem difficult at first, but they're actually quite simple once you understand how they work.

Here's what we'll cover:

1. [How a Promise Works](#heading-how-a-promise-works)
2. [Callbacks vs Promises](#heading-callbacks-vs-promises)
3. [When to Use Promises Instead of Callbacks](#heading-when-to-use-promises-instead-of-callbacks)
4. [Promises and the Fetch API](#heading-promises-and-the-fetch-api)
5. [The `Promise.all()` Method](#heading-the-promiseall-method)
6. [The `Promise.allSettled()` Method](#heading-the-promiseallsettled-method)
7. [The `Promise.any()` Method](#heading-the-promiseany-method)
8. [The `Promise.race()` Method](#heading-the-promiserace-method)
9. [Conclusion](#heading-conclusion)

## How a Promise Works

Basically, a `Promise` object represents a “pending state” in the most common sense: the promise will eventually be fulfilled at a later date.

To give you an illustration, suppose you want to buy a new phone to replace your old phone, so you open a messaging app to contact a phone store. This is similar to how you access a variable or a function that returns a promise:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/access-a-promise.png)
_Illustration 1: Sending a message to a store is like how you access a Promise object in JavaScript_

After you send a message explaining what you want, you get an automated message saying that a representative will answer your message shortly. This is similar to receiving a Promise object:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/promise-pending-state.png)
_Illustration 2: An automated message from the store you contacted before. This is the Promise object that you receive in JavaScript_

A minute later, you get a new message from a human representative, saying that the phone model you want to buy is available for purchase. This is when the Promise was resolved:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/promise-resolved.png)
_Illustration 3: A store representative replied to your message. This is like when a Promise gets resolved_

Or, in a completely different scenario, the representative tells you that the store doesn’t sell phones, because the store is a food store and not a phone store. This means the Promise was rejected:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/promise-rejected.png)
_Illustration 4: The representative replied that the store doesn't sell phones. This is like when a Promise gets rejected_

This illustration shows how the `Promise` object in JavaScript works:

* A Promise is like the automated message that we saw earlier. It represents a pending state that must be fulfilled at some point later.
* The human representative saying that the phone model is available is similar to the `resolve()` method, which shows that the Promise is fulfilled.
* The representative telling you that you’re contacting the wrong store is like the `reject()` method, which is the method used to show that the Promise can’t be fulfilled because of an error.

A typical promise implementation looks like this:

```js
let p = new Promise((resolve, reject) => {
  let isTrue = true;
  if (isTrue) {
    resolve('Promise resolved');
  } else {
    reject('Promise rejected');
  }
});

```

When creating a new Promise object, we need to pass a callback function that will be called immediately with two arguments: the `resolve()` and `reject()` functions.

Depending on the result of the `Promise`, either the `resolve()` or the `reject()` function will be called to end the pending state.

To handle the `Promise` object, you need to chain the function call with the `then()` and `catch()` functions as shown below:

```js
let p = new Promise((resolve, reject) => {
  let isTrue = true;
  if (isTrue) {
    resolve('Success');
  } else {
    reject('Error');
  }
});

p
.then(message => console.log(`Promise resolved: ${message}`))
.catch(message => console.log(`Promise rejected: ${message}`));

```

The `resolve()` function corresponds to the `then()` function, while `reject()` corresponds to the `catch()` function. You can change the `isTrue` value to `false` to test this.

Here’s an illustration of the promise process:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/promise-object--1-.png)
_The Process happening inside a Promise. Depending on the code run inside the Promise, it will settle as resolved or rejected._

Using the promise pattern, you can call your functions sequentially by placing the next process inside the `then()` or `catch()` methods.

## Callbacks vs Promises

The promise pattern was created to replace the use of callbacks in certain situations. By using promises, the code we write is more intuitive and maintainable.

Going back to the messaging illustration, let’s create an example of using callbacks to handle the situation. 

First, we declare the two variables required for this situation, called `isPhoneStore` and `isPhoneAvailable`:

```js
const isPhoneStore = true;
const isPhoneAvailable = true;

```

Next, we write a function that will process incoming messages. This function will mimic the promise pattern, and it will resolve only when `isPhoneStore` and `isPhoneAvailable` are `true`:

```js
function processMessage(resolveCallback, rejectCallback) {
  if (!isPhoneStore) {
    rejectCallback({
      name: 'Wrong store',
      message: 'Sorry, this is a food store!',
    });
  } else if (!isPhoneAvailable) {
    rejectCallback({
      name: 'Out of stock',
      message: 'Sorry, the X phone is out of stock!',
    });
  } else {
    resolveCallback({
      name: 'OK',
      message: 'The X phone is available! How many you want to buy?',
    });
  }
}

```

Here, you can see that the function `processMessage` accepts two callback functions: `resolveCallback` and `rejectCallback`.

When we call the function, we need to provide the callback functions, similar to how we need to chain the `then()` and `catch()` methods when accessing a promise:

```js
processMessage(
  value => console.log(value),
  reason => console.log(reason)
);

```

In the call to `processMessage` above, the first argument is the `resolveCallback()` function, and the second argument is the `rejectCallback()` function.

If you run the code above, then the `resolveCallback()` function will be called. You can change one of the two variables to `false` to trigger the `rejectCallback()` function.

Now that we have a working callback example, let’s rewrite the code using a promise as follows:

```js
const isPhoneStore = true;
const isPhoneAvailable = true;

function processMessage() {
  return new Promise((resolve, reject) => {
    if (!isPhoneStore) {
      reject({
        name: 'Wrong store',
        message: 'Sorry, this is a food store!',
      });
    } else if (!isPhoneAvailable) {
      reject({
        name: 'Out of stock',
        message: 'Sorry, the X phone is out of stock!',
      });
    } else {
      resolve({
        name: 'OK',
        message: 'The X phone is available! How many you want to buy?',
      });
    }
  });
}

processMessage()
  .then(response => console.log(response))
  .catch(error => console.log(error));

```

Here, you can see that the `processMessage()` function returns a `Promise` object that gets resolved only when both `isPhoneStore` and `isPhoneAvailable` are `true`.

When one of the two variables is `false`, then the `Promise` object will be rejected.

Here you can see that you don’t need to add two extra parameters to the `processMessage()` function just for the callbacks. Also, when calling the function, you use the `then()` and `catch()` methods to handle the result of the promise.

The use of a promise makes the code easier to understand. Here’s the comparison of the two side by side:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/callback-vs-promise.png)
_Callbacks vs Promises code comparison_

I don’t know about you, but I sure love writing and reading the promise pattern more than the callback pattern. 😉

### When to Use Promises Instead of Callbacks

As I've mentioned before, the promise object is created to replace callback functions in certain situations.

And if you examine the code for the promise object above closely, you'll see that even promises use callbacks inside the `then()` and `catch()` methods. This means Promises don't eliminate the need for callbacks.

Promises are used when you need to wait for a certain task to finish before running the next process.

For example, suppose you have three functions that need to run sequentially from one to three.

Each function runs for a few seconds. We simulate this using the `setTimeout()` method:

```js
function stepOne(value){
  setTimeout(() => {
    console.log(value);
  }, 3000);
}

function stepTwo(value){
  setTimeout(() => {
    console.log(value);
  }, 2000);
}

function stepThree(value){
  setTimeout(() => {
    console.log(value);
  }, 1000);
}
```

Using callbacks, you can define parameters on the `stepOne()` and `stepTwo()` functions, then call those functions sequentially like this:

```js
function stepOne(value, callback) {
  setTimeout(() => {
    console.log(value);
    callback();
  }, 3000);
}

function stepTwo(value, callback) {
  setTimeout(() => {
    console.log(value);
    callback();
  }, 2000);
}

function stepThree(value, callback) {
  setTimeout(() => {
    console.log(value);
    callback();
  }, 1000);
}

// Run the functions sequentially with callbacks
stepOne(1, () => {
  stepTwo(2, () => {
    stepThree(3, () => {
      console.log("All steps completed.");
    });
  });
});
```

The nested callbacks where you pass the next function inside the previous function is famously known as the "callback hell". This code pattern is hard to read and it's messy.

With promises, you can rewrite the code above as follows:

```js
function stepOne(value) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(value);
      resolve();
    }, 3000);
  });
}

function stepTwo(value) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(value);
      resolve();
    }, 2000);
  });
}

function stepThree(value) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(value);
      resolve();
    }, 1000);
  });
}

// Run the functions sequentially with Promises
stepOne(1)
  .then(() => stepTwo(2))
  .then(() => stepThree(3))
  .then(() => {
    console.log("All steps completed.");
  });
```

Here, you can see that each function returns a promise that resolves when the timeout is finished. The function calls using `then()` methods maintain a clear order of steps.

In a real-world project where you have many lines of code inside the callback functions, using Promises provides a massive gain in your ability to read, extend, and maintain the code.

But if you're running code that doesn't have to wait for certain processes, then you can use callbacks just fine.

For example, the array methods like `forEach()` use callbacks, so there's no need for promises there:

```js
const myArray = [1, 2, 3, 4];

myArray.forEach(value => console.log(value + 5));

```

Another use of promises is when you use the Fetch API, which is used to run network requests. Let's see how that works now.

## Promises and the Fetch API

The Fetch API always returns a `Promise` object, so you need to handle it using the `then()` and `catch()` methods as shown below:

```js
fetch('<Your API URL>')
  .then(response => console.log(response))
  .catch(error => console.log(error));

```

If you run a `fetch()` function and assign the result to a variable, the variable will contain a `Promise` object:

```js
const response = fetch('<Your API URL>');
console.log(response); // Promise {<pending>}

```

As you can see, the `Promise` object is assigned to the `response` variable in a pending state. If you wait a while and then log the object again, the output will be fulfilled:

```txt
Promise {<fulfilled>: Response}

```

The Fetch API will return a `Response` object when the promise is fulfilled. This is also why I usually name the parameter inside the `then()` method as `response` . Feel free to name the response as `message` , `value` , or anything your team agreed on.

Now that you’ve learned how the `Promise` object works, it’s time to learn some extra methods related to this object.

### The `Promise.all()` method

More than just replacing the callback pattern, JavaScript also provides some methods that you can use to work with `Promise` objects. For example, suppose you deal with three different promises in your project like this:

```js
const p1 = Promise.resolve('Success');
const p2 = Promise.resolve(200);
const p3 = Promise.resolve('Finished');

```

Now, suppose you need all three promises to resolve before moving to the next step. Knowing what we know about promises, we can chain the promises using the `then()` method like this:

```js
p1.then(message1 => {
  return p2.then(message2 => {
    return p3.then(message3 => {
      return [message1, message2, message3];
    });
  });
}).then(messages => {
  console.log(messages);
});

```

In this example, each `then()` method returns another promise, creating nested callbacks. When the `p3` promise is resolved, the messages are returned as a single array.

The last `then()` method would then log the `messages` array returned by the promises. This approach works, but this is exactly the type of code we want to avoid when using promises.

Instead of using nested callbacks, we can use the `Promise.all()` method instead. See the example below:

```js
const p1 = Promise.reject('Error From Promise One');
const p2 = Promise.resolve(200);
const p3 = Promise.resolve('Finished');

Promise.all([p1, p2, p3])
  .then(messages => console.log(messages))
  .catch(error => console.log(error));

```

The `Promise.all()` method accepts an array of promises, and when all promises are resolved, the method will pass the `messages` returned by the promises as an array and pass it to the `then()` method.

If one of the promises is rejected, then the method returns the first rejection it encounters and stops any further process.

This method enables you to work with many promises without having to create nested callbacks. You should use this method when you need all promises to resolve.

### The `Promise.allSettled()` method

The `Promise.allSettled()` method is similar to the `Promise.all()` method, but instead of  proceeding to `catch()` when one of the promises got rejected, the method will store the reject result and continue processing other promises.

When all promises are settled, the method will return an array of objects that contains the details of each promise. For example, suppose you run the following code:

```js
const p1 = Promise.reject('Error From Promise One');
const p2 = Promise.resolve(200);
const p3 = Promise.resolve('Finished');

Promise.allSettled([p1, p2, p3]).then(response => {
  console.log(response);
});

```

Then the result would be:

```txt
[
  { status: 'rejected', reason: 'Error From Promise One' },
  { status: 'fulfilled', value: 200 },
  { status: 'fulfilled', value: 'Finished' }
]

```

As you can see, the `response` variable is an array of objects showing the status and the value or reason for that status. When calling this method, you don't need to chain the `catch()` method.

You should use this method when you always need to know the result of each promise.

### The `Promise.any()` method

The `Promise.any()` method is similar to the `Promise.all()` method, except that it returns only a single value from any promise that calls the `resolve()` function first. If you try the method as follows:

```js
const p1 = Promise.reject('Error From Promise One');
const p2 = Promise.resolve(200);
const p3 = Promise.resolve('Finished');

Promise.any([p1, p2, p3]).then(response => {
  console.log(response);
});

```

The output will be:

```txt
200

```

This is because the first promise is rejected, and once the second promise is resolved, the `any()` method stops any further execution of promises and returns the resolved value.

This method returns an error only when all promises are rejected. You should use this method only when you need to get a single promise resolved out of many promises.

### The `Promise.race()` method

The `Promise.race()` method is like the `Promise.any()` method, with one difference: the promise is settled when any promise is resolved or rejected:

```js
const p1 = Promise.reject('Error From Promise One');
const p2 = Promise.resolve(200);
const p3 = Promise.resolve('Finished');

Promise.race([p1, p2, p3])
  .then(response => console.log(response))
  .catch(reason => console.log(reason));

```

Since `p1` returns a rejection, then the `Promise.race()` method returns the rejection instead of continuing the process:

```txt
Error From Promise One

```

You should use this method only when you need to get a single promise to settle, no matter if the result is resolved or rejected.

As you can see, these four methods of the `Promise` object provides you with a powerful composition tool that helps you decide how to handle multiple promises in your project.

## Conclusion

And now you’ve learned how the `Promise` object works in JavaScript. A promise is easy to understand when you grasp the three states that can be generated by the promise: pending, resolved, and rejected.

You’ve also learned how promises can be used to replace callbacks, when to use promises instead of callbacks, and how to use promise methods when you need to handle many promises in your project.

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!


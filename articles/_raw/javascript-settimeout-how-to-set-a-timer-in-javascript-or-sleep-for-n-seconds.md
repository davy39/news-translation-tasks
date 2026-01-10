---
title: JavaScript setTimeout() – How to Set a Timer in JavaScript or Sleep for N Seconds
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-04-27T17:45:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-settimeout-how-to-set-a-timer-in-javascript-or-sleep-for-n-seconds
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/set-timeout.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'This tutorial will help you to understand how the built-in JavaScript method  setTimeout()
  works with intuitive code examples.

  How to Use setTimeout() in JavaScript

  The setTimeout() method allows you to execute a piece of code after a certain amount
  ...'
---

This tutorial will help you to understand how the built-in JavaScript method  `setTimeout()` works with intuitive code examples.

## How to Use setTimeout() in JavaScript

The `setTimeout()` method allows you to execute a piece of code after a certain amount of time has passed. You can think of the method as a way to set a timer to run JavaScript code at a certain time.

For example, the code below will print "Hello World" to the JavaScript console after 2 seconds have passed:

```js
setTimeout(function(){
    console.log("Hello World");
}, 2000);

console.log("setTimeout() example...");
```

The code above will first print "setTimeout() example..." to the console, and then print "Hello World" once two seconds have passed since the code has been executed by JavaScript.

The `setTimeout()` method syntax is as follows:

```js
setTimeout(function, milliseconds, parameter1, parameter2, ...);
```

The first parameter of the `setTimeout()` method is a JavaScript `function` that you want to execute. You can write the `function` directly when passing it, or you can also refer to a named function as shown below:

```js
function greeting(){
  console.log("Hello World");
}

setTimeout(greeting);
```

Next, you can pass the `milliseconds` parameter, which will be the amount of time JavaScript will wait before executing the code. 

One second is equal to one thousand milliseconds, so if you want to wait for 3 seconds, you need to pass `3000` as the second argument:

```js
function greeting(){
  console.log("Hello World");
}

setTimeout(greeting, 3000);
```

If you omit the second parameter, then `setTimeout()` will immediately execute the passed `function` without waiting at all.

Finally, you can also pass additional parameters to the `setTimeout()` method that you can use inside the `function` as follows:

```js
function greeting(name, role){
  console.log(`Hello, my name is ${name}`);
  console.log(`I'm a ${role}`);
}

setTimeout(greeting, 3000, "Nathan", "Software developer");
```

Now you may be thinking, "why not just pass the parameters directly to the function?"

This is because if you pass the parameters directly like this:

```js
setTimeout(greeting("Nathan", "Software developer"), 3000);
```

Then JavaScript will immediately execute the `function` without waiting, because you're passing a _function call_ and not a _function reference_ as the first parameter. 

This is why if you need to pass any parameters to the function, you need to pass them from the `setTimeout()` method.

But honestly, I never found the need to pass additional parameters to the `setTimeout()` method in my role as a Software Developer, so don't worry about it 😉

## How to Cancel the setTimeout Method

You can also prevent the `setTimeout()` method from executing the `function` by using the `clearTimeout()` method.

The `clearTimeout()` method requires the `id` returned by `setTimeout()` to know which `setTimeout()` method to cancel:

```js
clearTimeout(id);
```

Here's an example of the `clearTimeout()` method in action:

```js
const timeoutId = setTimeout(function(){
    console.log("Hello World");
}, 2000);

clearTimeout(timeoutId);
console.log(`Timeout ID ${timeoutId} has been cleared`);
```

If you have multiple `setTimeout()` methods, then you need to save the IDs returned by each method call and then call `clearTimeout()` method as many times as needed to clear them all.

## Conclusion

The JavaScript `setTimeout()` method is a built-in method that allows you to time the execution of a certain `function` . You need to pass the amount of time to wait for in `milliseconds` , which means to wait for one second, you need to pass one thousand `milliseconds`.

To cancel a `setTimeout()` method from running, you need to use the `clearTimeout()` method, passing the ID value returned when you call the `setTimeout()` method.

## **Thanks for reading this tutorial**

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!

## 


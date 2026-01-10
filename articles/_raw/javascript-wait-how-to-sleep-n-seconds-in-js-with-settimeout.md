---
title: JavaScript Wait – How to Sleep N Seconds in JS with .setTimeout()
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-04-26T19:14:41.000Z'
originalURL: https://freecodecamp.org/news/javascript-wait-how-to-sleep-n-seconds-in-js-with-settimeout
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/nikita-kachanovsky-OVbeSXRk_9E-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Sometimes you might want to delay the execution of your code. \nYou may\
  \ need certain lines of code to execute at a point in the future, when you explicitly\
  \ specify, rather than all the code executing synchronously.\nSomething like that\
  \ is possible with..."
---

Sometimes you might want to delay the execution of your code. 

You may need certain lines of code to execute at a point in the future, when you explicitly specify, rather than all the code executing synchronously.

Something like that is possible with JavaScript.

In this article, you will learn about the `setTimeout()` method – what it is and how you can use it in your programs.

Here is what we will cover in this quick guide:

1. [What is `setTimeout()` in JavaScript](#intro)
2. [JavaScript `setTimeout()` syntax](#syntax)
3. [How to wait N seconds in JavaScript](#wait)
    1. [How to use the `clearTimeout()` method](#clear)
5. [`setTimeout` vs `setInterval` - What is the difference?](#difference)

## What is `setTimeout()` in JavaScript? <a name="intro"></a>

The role of `setTimeout()`, an asynchronous method of the window object, is to set a timer that will execute an action. That timer indicates a specific moment when there will be a trigger for that particular action.

Since `setTimeout()` is part of the window object, it can also be written as `window.setTimeout()`. That said, the `window` prefix is implied and therefore is usually omitted and not specified. 

## The `setTimeout()` Method - A Syntax Overview <a name="syntax"></a>

The general syntax for the `setTimeout()` method looks like this:

```js
setTimeout(function_name, time);
```

Let's break it down:

- `setTimeout()` is a method used for creating timing events.
- It accepts two **required** parameters.
- `function_name` is the first required parameter. It is the name of a callback function that contains the code you want to execute. The name of the function acts as a reference and pointer to the function definition that contains the actual block of code.
- `time` is the second required parameter, and it is defined in **milliseconds** (for reference, `1 second = 1000 milliseconds`). It represents the specified amount of time the program has to wait for the function to be executed. 

Overall, this means that `setTimeout()` will execute the code contained in a given function *once*, and only after a specified amount of time.

At this point, it is worth mentioning that instead of passing a function name, you can pass an *anonymous* function to `setTimeout()`. 

This is convenient when the function doesn't contain many lines of code.

*Anonymous* function means that you embed the code directly as the first parameter in `setTimeout()`, and don't reference the function name like you saw above.

```js
setTimeout(function() {
    // function code goes here
}, time);
```

Another thing to note is that `setTimeout()` returns a `timeoutID` – a positive integer that identifies the timer created by `setTimeout()`. 

Later on you will see how the value of `timeoutID` is used with the `clearTimeout()` method.

## How To Wait N Seconds In JavaScript <a name="wait"></a>

Let's take a look at an example of how `setTimeout()` is applied:

```js
//this code is executed first

console.log("Where can I learn to code for free and get a developer job?");

// this line indicates that the function definition will be executed once 3ms have passed

setTimeout(codingCourse, 3000);


//function definition

function codingCourse() {
  console.log("freeCodeCamp");
}
```

![js2](https://www.freecodecamp.org/news/content/images/2022/04/js2.gif)

JavaScript code is executed from top to bottom.

The first line of code, `console.log("Where can I learn to code for free and get a developer job?");`, is executed immediately once I press run.

The second line of code indicates that there needs to be a scheduled delay of 3000ms (or 3 seconds) before the code in the `codingCourse()` function is executed.

Once the 3000ms have passed, you see that the code inside the function (`console.log("freeCodeCamp")`) executes successfully.

Let's take a look at another example:

```js
console.log("Good Morning!");

setTimeout(function() {
  console.log("Good Night!");
}, 1000);

console.log("Good Afternoon!");
```

![js4-1](https://www.freecodecamp.org/news/content/images/2022/04/js4-1.gif)

In the example above, the first line of code, `console.log("Good Morning!");`, executes immediately. 

So does the line `console.log("Good Afternoon!");`, even though it is the last line of code in the file. 

The code in `setTimeout()` indicates that there needs to be a one-second delay before it runs.

However, during that time, the execution of the rest of the code in the file is not put on hold.

Instead, that line is skipped for the time being, and the line `console.log("Good Afternoon!");` is executed.

Once that one second has passed, the code in `setTimeout()` runs.

You can also pass further *optinal* parameters to `setTimeout()`.

In the example below, the `greeting` function accepts two argumnets, `phrase` and `name`.

```js
function greeting(phrase,name) {
  console.log(`${phrase}, my name is ${name}` );
}

setTimeout(greeting, 3000,"Hello world","John Doe");
```

Those are then passed to the `setTimeout()` method, and there will be a delay of 3 seconds once the function is called:

![js6](https://www.freecodecamp.org/news/content/images/2022/04/js6.gif)


### How to Use the `clearTimeout()` Method in JavaScript  <a name="clear"></a>

What if you want to cancel the timing event you have already created? 

You are able to stop the code in `setTimeout()` from running by using the `clearTimeout()` method. Here is where the `timeoutID` mentioned earlier comes in handy.

The general syntax for `clearTimeout()` is the following:

```js
clearTimeout(timeoutID)
```

The way this works is that you have to save the `timeoutID`, that is returned with every `setTimeout()` call, to a variable.

Then, `timeoutID` is used as a parameter to `clearTimeout()`, as seen below:

```js
let timeoutID = setTimeout(function(){
    console.log("Good Night");
}, 2000);

clearTimeout(timeoutID);

console.log("Good Morning!");
```

![js5](https://www.freecodecamp.org/news/content/images/2022/04/js5.gif)

Now, the code in `setTimeout()` will not execute.

## What Is the Difference Between `setTimeout` and `setInterval` ? <a name="difference"></a>

`setTimeout()` and `setInterval()` have very similar syntax. 

Here is the syntax for `setInterval()`:

```js
setInterval(function_name, time);
```

However, it's not a good idea to use them interchangeably since they work in different ways. 

`setTimeout()` triggers an action **once**, whereas `setInterval()` triggers an action **repeatedly**.

In the example below, the function `codingCourse` is called every three seconds:

```js
console.log("Where can I learn to code for free and get a developer job?");


setInterval(codingCourse, 3000);


//function definition
function codingCourse() {
  console.log("freeCodeCamp");
}
```

![js3](https://www.freecodecamp.org/news/content/images/2022/04/js3.gif)

`setInterval()` is a good choice for when you want to repeat something regularly.

## Conclusion

And there you have it! You now know the basics of how `setTimeout()` works and how to create timing events in JavaScript.

To learn more about JavaScript, head over to freeCodeCamp's [JavaScript Algorithms and Data Structures Certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/).

It's a free, well-thoughtout, and structured curriculum where you will learn interactively. In the end, you will also build 5 projects to claim your certification and solidify your knowledge by putting your new skills to practice.

Thanks for reading!



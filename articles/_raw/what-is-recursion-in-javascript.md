---
title: What is Recursion? A Recursive Function Explained with JavaScript Code Examples
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-02-04T00:03:39.000Z'
originalURL: https://freecodecamp.org/news/what-is-recursion-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/recursion-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Recursion
  slug: recursion
seo_title: null
seo_desc: "Recursion is a technique used to solve computer problems by creating a\
  \ function that calls itself until your program achieves the desired result. \n\
  This tutorial will help you to learn about recursion and how it compares to the\
  \ more common loop.\nWhat ..."
---

Recursion is a technique used to solve computer problems by creating a function that calls itself until your program achieves the desired result. 

This tutorial will help you to learn about recursion and how it compares to the more common loop.

## What is recursion?

Let's say you have a function that logs numbers 1 to 5. Here's how you write it using recursion:

```js
function log(num){
    if(num > 5){
        return;
    }
    console.log(num);
    log(num + 1);
}

log(1);
```

When you run the code above, the `log` function will simply call itself as long as the value of the `num` variable is smaller than `5`. 

A recursive function must have at least one condition where it will stop calling itself, or the function will call itself indefinitely until JavaScript throws an error.

The condition that stops a recursive function from calling itself is known as **the base case**. In the `log` function above, the base case is when `num` is larger than `5`.

## Why don't you just use a loop?

Any problems that you can solve using a recursive function will always have an alternative looping solution. The example above can be replaced with the following code:

```js
for(let i = 1; i <= 5; i++){
    console.log(i);
}
```

Modern programming languages like JavaScript already have the `for` and `while` statements as alternatives to recursive functions. But some languages like Clojure do not have any looping statements, so you need to use recursion to repeatedly execute a piece of code.

Also, a `for` loop requires you to know how many times you will repeat the code execution. But a recursive function and a `while` loop can be used to execute a piece of code without knowing how many times you need to repeat it. You just need to know the condition that stops the execution.

For example, suppose you have a task as follows:

* Randomly select a number between 1 to 10 until you get the number 5. 
* Log how many times you need to execute the code until the random method returns 5.

Here's how you do it with a recursive function:

```js
function randomUntilFive(result = 0, count = 0){
    if(result === 5){
        console.log(`The random result: ${result}`);
        console.log(`How many times random is executed: ${count}`);
        return;
    }
    result = Math.floor(Math.random() * (10 - 1 + 1) + 1);
    count++;
    randomUntilFive(result, count);
}

randomUntilFive();
```

You can't replace the code above with the `for` loop, but you can replace it with a `while` loop:

```js
let result = 0;
let count = 0;

while (result !== 5) {
  result = Math.floor(Math.random() * (10 - 1 + 1) + 1);
  count++;
}

console.log(`The random result: ${result}`);
console.log(`How many times random is executed: ${count}`);
```

Aside from coding interview questions where you are required to solve the problem using recursion, you can always find an alternative solution that uses either the `for` or `while` loop statement.

## How to read a recursive function

A recursive function is not intuitive or easy to understand at first glance. The following steps will help you to read and understand a recursive function more quickly:

* Always identify **the base case** of the function before anything else.
* Pass arguments to the function that will immediately reach the base case.
* Identify the arguments that will at least execute the recursive function call once.

Let's try these steps using the `randomUntilFive()` example above. You can identify the base case for this function inside the `if` statement above:

```js
function randomUntilFive(result = 0, count = 0){
    if(result === 5){
        // base case is triggered
    }
    // recursively call the function
}

randomUntilFive();
```

This means you can reach the base case by passing the number `5` into the `result` parameter as follows:

```js
function randomUntilFive(result = 0, count = 0){
    if(result === 5){
        console.log(`The random result: ${result}`);
        console.log(`How many times random is executed: ${count}`);
        return;
    }
}

randomUntilFive(5);
```

While the `count` parameter shouldn't be zero, passing the number `5` as an argument to the function call above fulfills the requirement of step two.

Finally, you need to find an argument that will at least execute the recursive function call once. In the case above, you can pass any number other than `5` or nothing at all:

```js
function randomUntilFive(result = 0, count = 0){
    if(result === 5){
        console.log(`The random result: ${result}`);
        console.log(`How many times random is executed: ${count}`);
        return;
    }
    result = Math.floor(Math.random() * (10 - 1 + 1) + 1);
    count++;
    randomUntilFive(result, count);
}

randomUntilFive(4); 
// any number other than five 
// will execute the recursive call
```

And you're done. Now you understand that the function `randomUntilFive()` will recursively call itself until the value of `result` equals five. 

## How to write a recursive function

Writing a recursive function is almost the same as reading one:

* Create a regular function with a base case that can be reached with its parameters
* Pass arguments into the function that immediately trigger the base case
* Pass the next arguments that trigger the recursive call just once.

Let's say you are writing a function to calculate [factorials](https://en.wikipedia.org/wiki/Factorial). Here's the factorial of five:

**5*4*3*2*1 = 120**

First, the base case for this function is one, so let's create a `factorial` function that returns one:

```js
function factorial(num){
    if(num === 1){
        return num;
    }
    
}

console.log(factorial(1));
```

Now on to step three. We need to get a recursive call in the function and call it at least once. Since the factorial calculation decreases the number by one on each multiplication, you can simulate it by passing `num-1` into the recursive call:

```js
function factorial(num){
    if(num === 1){
        return num;
    }
    return num * factorial(num-1) 
}

console.log(factorial(2));
```

And now you're done. You can test the function by passing five to the call:

```js
console.log(factorial(5));
```

## Conclusion

You've just learned what a recursive function is and how it compares to the common `for` and `while` loop statements. A recursive function must always have at least one base case to make it stop calling itself or it will cause an error. 

When reading a recursive function, you need to simulate a situation where the base case is immediately executed without executing the recursive call. 

Once you have the base case covered, go back one step and try to execute the recursive call at least once. This way, you brain will walk through the recursive code and understand intuitively what it does.

The same goes for writing a recursive function. Always create the base case first and then write an argument that runs the recursive call at least once. The rest will be easier from there.

## Thanks for reading this tutorial

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!


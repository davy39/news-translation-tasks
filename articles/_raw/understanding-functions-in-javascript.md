---
title: How Functions Work in JavaScript – JS Function Code Examples
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-01-20T17:52:37.000Z'
originalURL: https://freecodecamp.org/news/understanding-functions-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/kevin-ku-w7ZyuGYNpRQ-unsplash-1.jpg
tags:
- name: functions
  slug: functions
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'JavaScript is a widely-used programming language that is essential for
  web development. Its ability to run on both client-side and server-side makes it
  a versatile tool that has become an essential tool for web developers.

  JavaScript is a high-level,...'
---

JavaScript is a widely-used programming language that is essential for web development. Its ability to run on both client-side and server-side makes it a versatile tool that has become an essential tool for web developers.

JavaScript is a high-level, interpreted language used on the client side, meaning it runs in the user's web browser. You can use it to create web and mobile applications, browser extensions, and other software. 

It is supported by all major web browsers, and it is an essential technology for front-end web development. 

**Functions** are one of the building blocks of JavaScript programming for creating web applications. 

You can think of functions as a way to group a set of instructions together and execute them as a single unit. 

In this article, we will explore the basics of functions in JavaScript and how you can use them effectively in your code.

## Function Syntax

A function is a block of code that performs a specific task. JavaScript functions are basically used to encapsulate logic, making that code more reusable and easier to understand. 

The syntax for creating a function in JavaScript is quite simple. Functions can take input in the form of parameters and can return a value or output. 

Functions help you organize and structure your code. They also allow for code reuse and make it easier to understand and maintain large codebases.

### How to Write a Function in JavaScript

You start by using the keyword "**function**," followed by the function name and a set of parentheses. 

Inside the parentheses, you can specify any input parameters that the function will take in, also known as arguments. The arguments are usually optional. 

Next, you include a block of code inside curly braces that defines the instructions the function will execute when it is called. 

Here is an example of a basic function that takes in two numbers and returns their sum:

```.js
//index.js

function addNumbers(a, b) {
  return a + b;
}

```

The function above, named "**addNumbers**," takes in two parameters, **a** and **b**. The code inside the function body simply adds these two parameters together and returns the result.

## How to Declare a Function in JavaScript

Apart from the regular way of declaring a function as seen above, you can also define functions using **function expressions** or **arrow functions**. 

The arrow function syntax is a shorthand version of the regular function syntax. Here is the same function as above, but written with an arrow function:

```js
//index.js
const addNumbers = (a, b) => a + b;
```

In the example above, the function is assigned to the variable **addNumbers**. The arrow **=>** is used to define the function, and the code inside the curly braces is the body of the function.

Function expressions in JavaScript are similar to regular function declarations. The difference between them is that the function expression is always assigned to a variable. Here is an example of a function expression:

```js
//index.js
let multiplyNumbers = function(a, b) {
    return a * b;
}

```

In this example, the function is assigned to the variable **multiplyNumbers**. This variable can be used to call the function, just like a regular function.

## How to Use Callback Functions

Functions can also be passed as arguments to other functions, known as **callback functions**. Here is an example of a callback function being used to log the result of a multiplication operation:

```js
//index.js

function multiplyByTwo(n, callback) {
  var result = n * 2;
  callback(result);
}

function logResult(result) {
  console.log(result);
}

multiplyByTwo(5, logResult); // logs 10
```

In this example, the **multiplyByTwo** function takes two arguments: a number and a callback function. The function multiplies the number by 2 and then invokes the callback function, passing the result as an argument. The **logResult** function is then executed, which logs the result to the console.

## How to Use Default Parameters

JavaScript functions also have a feature called default parameters. They allow you to set default values for parameters in case they are not passed when the function is called. 

This is helpful in situations where you want to provide a default value for a parameter in case it is not passed. Here is an example:

```js
//index.js

function greet(name = "John Doe") {
    console.log(`Hello, ${name}!`);
}

greet(); // Hello, John Doe!
greet("Jane Smith"); // Hello, Jane Smith
```

In this example, the `greet` function takes in a single parameter `name`, which is set to "John Doe" by default. If the function is called without passing any arguments, it will use the default value "John Doe". But if an argument is passed, it will use that value instead.

## How to Use the Constructor Function

JavaScript has a special type of function called a constructor function, which is used to create objects. 

You define a constructor function using the keyword "function" followed by a name that starts with an uppercase letter (called using the "new" keyword). 

For example, the following code defines a constructor function named "Person" that creates an object with a name and age property:

```js
//index.js

function Person(name, age) {
  this.name = name;
  this.age = age;
}

let person = new Person("John Smith", 30);
console.log(person.name); // Output: "John Smith"
console.log(person.age); 
```

## How to Use Closures

A **closure** is a function that has access to variables in its parent scope, even after the parent function has returned. This allows for variables to be preserved between function calls, and it is a powerful feature that allows for more advanced programming patterns such as object-oriented programming. 

Here's an example of a closure function that creates a counter:

```js
//index.js

function createCounter() {
  let count = 0;
  return function() {
    return count++;
  }
}
const myCounter = createCounter();
console.log(myCounter()); // Output: 0
console.log(myCounter()); /
```

## How to Use Higher-Order Functions

Functions can also be passed as arguments to other functions, which is known as a "higher-order" function. For example:

```js
//index.js

function performOperation(a, b, operation) {
    return operation(a, b);
}

let result = performOperation(5, 10, addNumbers);
console.log(result);  // 15
```

In this example, the **performOperation** function takes in three arguments: **a**, **b**, and **operation**. 

The **operation** argument is a function that takes in two arguments and returns a result. In this case, we are passing the **addNumbers** function as the operation argument, so the result of the **performOperation** function will be the result of calling the **addNumbers** function with the arguments **a** and **b**.

## Conclusion

In this article, we have covered the basics of functions in JavaScript, including how to define, call, and use them in our codes. 

With a solid understanding of functions, you can write more efficient and maintainable code in JavaScript.

You can check the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions) to read more about functions in JavaScript. If you want to start learning the fundamentals of JavaScript, freeCodeCamp has a free [JavaScript Algorithms and Data Structures Certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) course for you.  
  
Happy coding!


---
title: What does => Mean in JavaScript? The Equals Greater Than Symbol aka Hashrocket
  Explained
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-03-21T22:16:00.000Z'
originalURL: https://freecodecamp.org/news/what-does-the-hashrocket-symbol-mean-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/markus-spiske-AaEQmoufHLk-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Prior to the introduction of arrow functions, function expressions in JavaScript\
  \ had a verbose syntax that often made code harder to read and understand. \nAs\
  \ a more concise way of writing function expressions in JavaScript, arrow functions\
  \ were intro..."
---

Prior to the introduction of arrow functions, function expressions in JavaScript had a verbose syntax that often made code harder to read and understand. 

As a more concise way of writing function expressions in JavaScript, arrow functions were introduced in ECMAScript 6 (ES6). They quickly gained popularity among developers due to their simplicity and readability.

Arrow functions are a shorthand way of defining functions in JavaScript, and they have a unique syntax that is different from traditional functions. The => symbol is used to define the function while the function's body is enclosed in curly braces. The "=>" symbol is known as the "equals greater than" symbol or the **hashrocket**.

In this article, we will take an in-depth look at what the "**=>**" symbol means in JavaScript and how it is used to create arrow functions. We will explore the syntax and structure of arrow functions, as well as their advantages. I hope you enjoy it.

## What the "=>" Symbol Means

The "=>" symbol, also known as the equals greater than symbol or **hashrocket**, is a shorthand notation for defining functions in JavaScript. It is used to create a new type of function called an arrow function.

Arrow functions have a simpler and more concise syntax than traditional function expressions. You can use them to define anonymous functions or to pass functions as arguments to other functions.

Here is a basic example of where the hashrocket is used and how it is used.

```js
const square = x => x * x;
```

The code above shows how the hashrocket is used in an arrow function that takes a parameter and returns its square. 

The arrow function is defined using the "=>" symbol, which has a parameter, x. The function body, which calculates the square of "x", is not enclosed in curly braces and follows the arrow operator. This is the most concise way to write an arrow function.

Arrow functions can also have multiple parameters enclosed in parentheses and a function body enclosed in curly braces. Here is an example of an arrow function that takes two parameters and returns their sum:

```js
const sum = (a, b) => {
  return a + b;
};

```

In the code above, the arrow function is defined using the "**=>**" symbol, with the parameters "**a**" and "**b**". The function body, which calculates the sum of "**a**" and "**b**", is enclosed in curly braces and follows the hashrocket.

## Advantages of Arrow Functions

### Lexical Scoping

Arrow functions in JavaScript have lexical scoping, which means they inherit variables from their parent scope. This feature makes them useful in certain programming tasks where you need to access variables in the parent scope.

Here's a simple example to illustrate this concept:

```js
function outerFunction() {
  var outerVariable = "Hello, ";
  
  function innerFunction(name) {
    var innerVariable = "world!";
    
    var message = () => {
      console.log(outerVariable + name + " " + innerVariable);
    };
    
    return message();
  }
  
  innerFunction("John");
}

outerFunction(); //output: "Hello, John world!"
```

In this example, we have an outer function called `outerFunction()` that declares a variable called `outerVariable` and assigns it the value of "Hello, ". The outer function also declares an inner function called `innerFunction(name)`, which has its own variable `innerVariable` and an arrow function called `message()`.

The arrow function `message()` logs a message to the console that includes the value of `outerVariable`, name (which is passed as an argument to `innerFunction()`), and `innerVariable`. When `message()` is called, it has access to all of these variables, even though they are defined in different scopes.

Finally, we call the outer function `outerFunction()`, which in turn calls `innerFunction("John")`. This results in the message "Hello, John world!" being logged to the console.

The example shows that the arrow function `message()` has access to variables defined in the outer and inner functions, thanks to **lexical scoping**. This feature makes arrow functions useful for accessing variables in the parent scope, which can simplify code and make it more readable.

### Useful for callbacks

Arrow functions are useful for callbacks. Callback functions are functions that are passed as arguments to other functions. Arrow functions are usually preferred as callback functions because arrow functions can be written more concisely and clearly than traditional function expressions.

For example, consider this code that uses the traditional function expression to filter an array of numbers:

```js
const numbers = [1, 2, 3, 4, 5];

const filteredNumbers = numbers.filter(function(number) {
  return number % 2 === 0;
});

```

In this code, the function expression is a bit long and hard to read. We can simplify it using an arrow function as seen below.

```js
const numbers = [1, 2, 3, 4, 5];

const filteredNumbers = numbers.filter(number => number % 2 === 0);
```

In this version of the code, the arrow function is much shorter and easier to read, making it a great choice for callbacks.

## Conclusion

In conclusion, the arrow function syntax in JavaScript provides a more concise and simpler way of writing function expressions. It simplifies the syntax for simple functions using the **=>** symbol and makes it easier to deal with scoping.

I hope this article was useful. Happy coding!

  


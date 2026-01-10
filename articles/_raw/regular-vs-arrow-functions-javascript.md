---
title: JavaScript Arrow Functions vs Regular Functions
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-01-16T22:19:05.000Z'
originalURL: https://freecodecamp.org/news/regular-vs-arrow-functions-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-6.53.58-PM.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: functions
  slug: functions
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In JavaScript, there are two main ways of writing functions. You can create
  functions using the regular function syntax. Or you can use the arrow function syntax.

  In this article, you will learn how to use both options. You''ll also learn about
  the di...'
---

In JavaScript, there are two main ways of writing functions. You can create functions using the regular function syntax. Or you can use the arrow function syntax.

In this article, you will learn how to use both options. You'll also learn about the differences between the two and when it's appropriate to use each of them.

## Table of Contents

* [Regular Function Syntax vs Arrow Function Syntax](#regular-function-syntax-vs-arrow-function-syntax)
    
* [How to Access the Arguments Passed to Functions](#how-to-access-the-arguments-passed-to-functions)
    
* [Duplicate Named Parameters](#duplicate-named-parameters)
    
* [Function Hoisting](#function-hoisting)
    
* [How to Handle "this" Binding in Functions](#how-to-handle-this-binding-in-functions)
    
* [How to Use Functions as Constructors](#how-to-use-functions-as-constructors)
    
* [So Which One Should You Use?](#so-which-one-should-you-use)
    

## Regular Function Syntax vs Arrow Function Syntax

To understand the difference between the two options, let's begin by looking at their syntax.

### Regular function syntax

The ordinary way of declaring functions in JavaScript is to use the `function` keyword. Here is an example:

```javascript
function sayHello(name) {
  return 'Hello ' + name
}
```

To return a value from a regular function, you have to explicitly use the `return` keyword. Otherwise the function will return `undefined`.

### Arrow function syntax

Arrow functions were introduced with ECMAScript 6 (ES6). They give you a more concside way of defining functions in JavaScript.

Using the same `sayHello` function from the previous example, let's see how to create it with the arrow function syntax.

```javascript
const sayHello = (name) => {
  return 'Hello ' + name
}
```

Unlike regular functions, you don't have to use an explicit return if there's only one statement like the above example. You can write the function on a single line like so.

```javascript
const sayHello = (name) => 'Hello ' + name
```

Note how the curly braces are also removed to implicitly return the result of the expression. You can even remove the parenthesis too if there is only one argument. See the example below:

```javascript
const sayHello = name => 'Hello ' + name
```

The `name` is the only argument the function takes. And this means you can remove the parenthesis from the argument and it will still work fine.

## How to Access the Arguments Passed to Functions

JavaScript provides a way to access all arguments passed to a function. But the way you acess these arguments depends on the type of function you are working with.

### How to access arguments with regular functions

You can access all the arguments passed to a regular function using the `arguments` object. The `arguments` object is an array-like object that holds all the arguments passed to the function.

Example:

```javascript
function logNumbers(num1, num2) {
  console.log(arguments)
}

logNumbers(8, 24)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-11-at-5.01.51-PM.png align="left")

*Log results of the arguments object*

As you can see from the log result, the `arguments` object contains the two numbers passed as arguments to the `logNumbers` function.

### How to access arguments with arrow functions

The `arguments` object is not available in arrow functions. If you try to access it in arrow functions, JavaScript will throw a reference error.

```javascript
const logNumbers = (num1, num2) => {
  console.log(arguments)
}

logNumbers(8, 24) // Uncaught ReferenceError: arguments is not defined
```

To access the arguments passed to an arrow function, you can use the rest parameter syntax (`...`).

Example:

```javascript
const logNumbers = (...args) => {
  console.log(args)
}

logNumbers(8, 24)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-11-at-11.13.39-PM.png align="left")

*Log results for the arguments from an arrow function*

Using the rest parameter syntax (`...`), you get access to all the arguments passed to the `logNumbers` function.

## Duplicate Named Parameters

Another difference between regular functions and arrow functions is how they handle duplicates in the named parameters.

### Duplicate named parameters in regular functions

When a regular function has duplicate names in the parameters, the last parameter with the duplicate name will take precedence. Let's see an example:

```javascript
function exampleFunction(a, b, a) {
  console.log(a, b)
}

exampleFunction("first", "second", "third")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-9.50.00-AM.png align="left")

*Log results for named duplicate parameters*

In the example above, the `third` argument overrides the value of the `first` argument because the last duplicate parameter is the one that takes precedence.

But in "strict mode", using a duplicate named parameter will result in a syntax error.

```javascript
"use strict"

function exampleFunction(a, b, a) {
  console.log(a, b)
}

exampleFunction("first", "second", "third")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-10.29.11-AM.png align="left")

*Strict mode doesn't allow using a parameter name more than once*

### Duplicate named parameters in arrow functions

Arrow functions don't allow for the same parameter name to be used more than once in the parameter list. Doing so will result in a syntax error.

Example:

```javascript
const exampleFunction = (a, b, a) => {
  console.log(a, b)
}

exampleFunction("first", "second", "third")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-10.29.11-AM-1.png align="left")

*Arrow functions do not allow duplicate parameter names*

## Function Hoisting

Hoisting in JavaScript is a behaviour where variables and functions are moved to the top of their containing scope during compilation, before the code is executed.

### Hosting in regular functions

Regular functions are hoisted to the top. And you can access and call them even before they are declared.

```javascript
regularFunction()

function regularFunction() {
  console.log("This is a regular function.")
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-11.50.43-AM.png align="left")

*Log result of calling the regular function before it's declared*

The above is an example of calling a regular function before it is declared. And it works fine without throwing any error because of function hoisting.

### Hoisting in arrow functions

Arrow functions, on the other hand, cannot be accessed before they are initialised.

```javascript
arrowFunction()

const arrowFunction = () => {
  console.log("This is an arrow function.")
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-12.07.39-PM.png align="left")

*Log result of calling the arrow function before it's declared*

Unlike regular functions, attempting to call an arrow function before it's declared will result in a reference error, as you can see from the output above.

## How to Handle `this` Binding in Functions

Regular functions have their own `this` context. And this is determined dynamically depending on how you call or execute the function.

Arrow functions, on the other hand, do not have their own this context. Instead, they capture the `this` value from the surrounding lexical context in which the arrow function was created.

The following are two different scenarios using both regular functions and arrow functions. You'll see how the `this` context is determined.

### 1\. Setting the `this` value during a simple function call

For regular functions, a simple function call sets the `this` value to the `window` object (or to `undefined` if you're using the "strict mode"):

```javascript
function myRegularFunction() {
  console.log(this)
}
    
myRegularFunction()
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-4.15.11-PM.png align="left")

*A simple invocation of a regular function sets* `this` to the window object

```javascript
"use strict"

function myFunction() {
  console.log(this)
}
    
myFunction() // udefined
```

With arrow functions, a simple function call sets the `this` value to the surrounding context whether you're using strict mode or not. In the example below, the surrounding context is the global window object.

```javascript
const myArrowFunction = () => {
  console.log(this);
};

myArrowFunction()
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-4.15.11-PM-1.png align="left")

*A simple invocation of an arrow function sets* `this` to the window object

### 2\. When invoking or calling a method on an object

When you invoke a method whose value is a regular function, the `this` value is set to the object on which the method is called. But when the value of the method is an arrow function, the `this` value is set to the global window object.

```javascript
const myObject = {
  regularExample: function() {
    console.log("REGULAR: ", this)
  },
    
  arrowExample: () => {
    console.log("ARROW: ", this)
  }
}
    
myObject.regularExample()
myObject.arrowExample()
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-5.46.04-PM.png align="left")

*Log result for a method with a regular function and another with an arrow function*

While the method with the regular function logs the object to the console, the one with the arrow function logs the global window object instead.

## How to Use Functions as Constructors

For regular functions, you can create a new instance using the `new` keyword. And this sets the `this` value to the new instance you've created.

For arrow functions, you cannot use them as constructors. This is because the value of `this` in arrow functions is lexically scoped – that is, determined by the surrounding execution context. This behaviour does not make them suitable to be used as constructors.

Here's an example:

```javascript
function RegularFuncBird(name, color) {
  this.name = name
  this.species = color
  console.log(this)
}

const ArrowFuncBird = (name, color) => {
  this.name = name
  this.color = color
  console.log(this)
}

new RegularFuncBird("Parrot", "blue") 
new ArrowFuncBird("Parrot", "blue")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-5.53.17-PM.png align="left")

*Log results for attempting to use regular and arrow functions as constructors*

The `RegularFuncBird` constructor works fine with the `new` keyword, but the `ArrowFuncBird` results in a type error.

## So Which One Should You Use?

There is no straightforward answer to this. Whether you use a regular function or arrow function depends on the specific use case.

It's recommended to use regular function in any of the following cases:

* when you need to use a constructor with the `new` keyword
    
* when you need the `this` binding to be dynamically scoped
    
* when you want to use the `arguments` object
    

And you can use arrow functions in any of the following cases:

* when you want a more concise syntax for the function
    
* when you need to maintain the lexical scope of `this`
    
* for non-method functions (in most cases)
    

As you've learned from this article, both are valid ways of defining functions in JavaScript. Remember that choosing between them is not always a matter of personal preference. Rather, it's dependent on the kind of behaviour you expect from the function.

Thanks for reading and happy coding!

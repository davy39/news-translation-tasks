---
title: JavaScript Functions Tutorial – IIFE, Function Parameters, and Code Blocks
  Explained
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2022-10-05T16:06:29.000Z'
originalURL: https://freecodecamp.org/news/javascript-function-iife-parameters-code-blocks-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/programming-image-by-mohamed-hassan-from-pixabay-javascript-function-iffe-parameters-blocks-explained-codesweetly.png
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Functions are one of the most widely-used features in programming. So,
  it helps to have a solid understanding of how they work.

  This tutorial discusses everything you need to know to use JavaScript functions
  like a pro.

  Table of Contents


  What Is a F...'
---

Functions are one of the most widely-used features in programming. So, it helps to have a solid understanding of how they work.

This tutorial discusses everything you need to know to use JavaScript functions like a pro.

## Table of Contents

1. [What Is a Function?](#heading-what-is-a-function)
2. [Why Functions?](#heading-why-functions)
3. [Syntax of a JavaScript Function](#heading-syntax-of-a-javascript-function-1)
4. [What Is a `function` Keyword?](#heading-what-is-a-function-keyword)
5. [What Is a Function Name?](#heading-what-is-a-function-name)
6. [What Is a Parameter?](#heading-what-is-a-parameter)
7. [What Is a Code Block?](#heading-what-is-a-code-block)
8. [What Is a Function Body?](#heading-what-is-a-function-body)
9. [Types of JavaScript Functions](#heading-types-of-javascript-functions)
10. [What Is a JavaScript Function Declaration?](#heading-what-is-a-javascript-function-declaration)
11. [What Is a JavaScript Function Expression?](#heading-what-is-a-javascript-function-expression)
12. [What Is a JavaScript Arrow Function Expression?](#heading-what-is-a-javascript-arrow-function-expression)
13. [What Is a JavaScript Immediately Invoked Function Expression?](#heading-what-is-a-javascript-immediately-invoked-function-expression)
14. [Overview](#heading-overview)

So, let's get started from the basics.

## What Is a Function?

A **JavaScript function** is an executable piece of code developers use to bundle a block of zero or more statements.

In other words, a function is an executable subprogram (mini-program).

A JavaScript function is a subprogram because its body consists of a series of statements (instructions) to computers—just like a regular program.

The instructions in a function's body can be a [variable](https://codesweetly.com/javascript-variable#example-3-javascript-variable) declaration, [return](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return) call, [console.log()](https://developer.mozilla.org/en-US/docs/Web/API/console/log) invocation, [function](#heading-syntax-of-a-javascript-function-1) definition, or any other JavaScript [statements](https://codesweetly.com/javascript-statement).

**Note:**

* A program is a list of instructions written for computers to execute.
* Unlike other [object types](https://codesweetly.com/javascript-non-primitive-data-type#types-of-javascript-objects), you can invoke a function without storing it in a variable.
* A JavaScript function is similar to other programming languages' procedures or subroutines.

## Why Functions?

Functions provide a way to bundle pieces of code together and reuse them anytime, anywhere, for an unlimited period. This helps you eliminate the burden of writing the same set of code repeatedly.

For instance, [alert()](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert) is a [built-in window function](https://developer.mozilla.org/en-US/docs/Web/API/Window) that someone wrote once for all developers to use anytime, anywhere.

## Syntax of a JavaScript Function

```js
function nameOfFunction(parameter1, parameter2, ..., parameterX) {
  // function's body
}
```

A function is composed of five elements:

1. A `function` keyword
2. The function's name
3. A list of zero or more parameters
4. A code block (`{...}`)
5. The function's body

Let's discuss each element.

## What Is a `function` Keyword?

We use the `function` keyword to declare to browsers that a specific piece of code is a JavaScript function—not a mathematical or other generic function.

## What Is a Function Name?

A **function's name** allows you to create an identifier for your function, which you can use to reference it.

## What Is a Parameter?

A **parameter** specifies the name you wish to call your function's [argument](https://codesweetly.com/javascript-arguments).

A parameter is an optional component of a function. In other words, you do not need to specify a parameter if your function does not accept any argument.

For instance, JavaScript's [pop()](https://codesweetly.com/javascript-pop-method) method is a function without any parameter because it does not accept arguments.

On the other hand, [forEach()](https://codesweetly.com/javascript-foreach-method) has two parameters that accept two arguments.

### Example of a JavaScript parameter

```js
// Define a function with two parameters:
function myName(firstName, lastName) {
  console.log(`My full name is ${firstName} ${lastName}.`);
}

// Invoke myName function while passing two arguments to its parameters:
myName("Oluwatobi", "Sofela");

// The invocation above will return:
"My full name is Oluwatobi Sofela."
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-edvj3g?devToolsHeight=33&file=index.js)

The `myName()` function in the snippet above has two parameters: `firstName` and `lastName`.

Suppose you wish to pre-define values for your parameters that browsers can use if users do not invoke the function with the required arguments. In that case, you can create default parameters.

### What is a default parameter?

**Default parameters** allow you to initialize your function's parameters with default values.

For instance, suppose users invoke your function without providing a required argument. In such a case, browsers will set the parameter's value to `undefined`.

However, default parameters allow you to define the values browsers should use instead of `undefined`.

### Examples of default parameters

Below are examples of how default parameters work in JavaScript.

#### How to define a function with no default parameters

```js
// Define a function with two parameters:
function myName(firstName, lastName) {
  console.log(`My full name is ${firstName} ${lastName}.`);
}

// Invoke myName function while passing one argument to its parameters:
myName("Oluwatobi");

// The invocation above will return:
"My full name is Oluwatobi undefined."
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-9ce3xt?devToolsHeight=33&file=index.js)

The computer automatically set the `lastName` parameter to `undefined` because we did not provide a default value.

#### How to define a function with an `undefined` argument and no default parameter

```js
// Define a function with two parameters:
function myName(firstName, lastName) {
  console.log(`My full name is ${firstName} ${lastName}.`);
}

// Invoke myName function while passing two arguments to its parameters:
myName("Oluwatobi", undefined);

// The invocation above will return:
"My full name is Oluwatobi undefined."
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-csbxta?devToolsHeight=33&file=index.js)

The computer set the `lastName` parameter to `undefined` because we provided `undefined` as `myName()`'s second argument.

#### How to define a function with a default parameter

```js
// Define a function with two parameters:
function myName(firstName, lastName = "Sofela") {
  console.log(`My full name is ${firstName} ${lastName}.`);
}

// Invoke myName function while passing one argument to its parameters:
myName("Oluwatobi");

// The invocation above will return:
"My full name is Oluwatobi Sofela."
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ghiyzm?devToolsHeight=33&file=index.js)

Instead of `undefined`, JavaScript used `"Sofela"` as the `lastName` parameter's default argument.

#### How to define a function with an `undefined` argument and a default parameter

```js
// Define a function with two parameters:
function myName(firstName, lastName = "Sofela") {
  console.log(`My full name is ${firstName} ${lastName}.`);
}

// Invoke myName function while passing two arguments to its parameters:
myName("Oluwatobi", undefined);

// The invocation above will return:
"My full name is Oluwatobi Sofela."
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-umqgqp?devToolsHeight=33&file=index.js)

Instead of `undefined`, JavaScript used `"Sofela"` as the `lastName` parameter's default argument.

Let's now discuss the fourth element of a JavaScript function: a **code block.**

## What Is a Code Block?

A **block** is a pair of braces (`{...}`) used to group multiple statements together.

**Here's an example:**

```js
{
  const hourNow = new Date().getHours();
}
```

The block in the snippet above encased one JavaScript [statement](https://codesweetly.com/javascript-statement).

**Here's another example:**

```js
if (new Date().getHours() < 18) {
  const hourNow = new Date().getHours();
  const minutesNow = new Date().getMinutes();
  console.log(`The time is ${hourNow}:${minutesNow}.`);
}
```

The `if` condition's code block grouped three JavaScript statements together.

**Now, consider this snippet:**

```js
function getTime() {
  const hourNow = new Date().getHours();
  const minutesNow = new Date().getMinutes();
  console.log(`The time is ${hourNow}:${minutesNow}.`);
}
```

The `getTime()` function's code block grouped three JavaScript statements. Note that the "function body" is the space inside the function's code block. Let's talk more about it now.

## What Is a Function Body?

A **function body** is where you place a sequence of statements you want to execute.

### Syntax of a JavaScript function body

```js
function nameOfFunction() {
  // function's body
}

```

### Function body examples

Below are examples of how we use the function body.

#### How to define a function with three statements in its body

```js
function getName() {
  const firstName = "Oluwatobi";
  const lastName = "Sofela";
  console.log(firstName + " " + lastName);
}

```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-flz5tf?devToolsHeight=33&file=index.js)

In the snippet above, the function's body contains three statements that the computer will execute whenever the function gets invoked.

**Note:** `console.log()` is a [method](https://codesweetly.com/web-tech-terms-m#method) we use to log (write) messages to a web console.

#### How to define a function with two statements in its body

```js
const bestColors = ["Coral", "Blue", "DeepPink"];

function updateMyBestColors(previousColors, newColor) {
   const mybestColors = [...previousColors, newColor];
   return mybestColors;
}

updateMyBestColors(bestColors, "GreenYellow");
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-nb9sr6?devToolsHeight=33&file=index.js)

In the snippet above, the function's body contains two statements that the computer will execute whenever the function gets invoked.

**Note:**

* The three dots we prepended to `previousColors` is called a [spread operator](https://codesweetly.com/spread-operator). We used it to expand the [array](https://codesweetly.com/javascript-array-object) argument into individual elements.
* You can also prepend the `newColor` parameter with a [rest operator](https://codesweetly.com/javascript-rest-operator) if you wish to add two or more new colors.
* The `return` keyword ends its function's execution and returns the specified [expression](https://codesweetly.com/javascript-statement#what-is-a-javascript-expression-statement) (or `undefined` if you provide no expression).

So, now that we know the components of a JavaScript function, we can discuss its types.

## Types of JavaScript Functions

The four types of JavaScript functions are:

* Function declaration
* Function expression
* Arrow function expression
* Immediately invoking function expression

Let's discuss each type.

## What Is a JavaScript Function Declaration?

A **function declaration** is a function created without assigning it to a [variable](https://codesweetly.com/javascript-variable).

**Note:** We sometimes call function declaration a "function definition" or "function statement."

**Here's an example:**

```js
function addNumbers() {
  return 100 + 20;
}

```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-pwh2jr?devToolsHeight=33&file=index.js)

The function above is a function declaration because we defined it without storing it in a variable.

## What Is a JavaScript Function Expression?

A **function expression** is a function you create and assign to a variable.

**Here's an example:**

```js
const myFuncExpr = function addNumbers() {
  return 100 + 20;
};

```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-hjg1iq?devToolsHeight=33&file=index.js)

The function above is a **named** function expression that we assigned to the `myFuncExpr` variable.

You can also write the snippet above as an **anonymous** function expression like so:

```js
const myFuncExpr = function() {
  return 100 + 20;
};

```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-pmeqy4?devToolsHeight=33&file=index.js)

The function above is an anonymous function expression that we assigned to the `myFuncExpr` variable.

**Note:**

* An **anonymous function** is a function with no name.
* A **named function** is a function with a name.

A named function's main advantage is that the name makes it easier to trace an error's origin.

In other words, suppose your function threw an error. In such a case, if the function is named, a debugger's [stack trace](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack) will contain the function's name. Therefore, you will find it easier to identify the error's origin.

## What Is a JavaScript Arrow Function Expression?

An **arrow function expression** is a shorthand way to write a function expression.

### Syntax of an arrow function

We define an arrow function with the equality and the greater-than symbols (`=>`). Here is the syntax:

```js
const variableName = () => {
  // function's body
}

```

### Example of an arrow function

```js
const myFuncExpr = () => {
  return 100 + 20;
};

```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-1euhch?devToolsHeight=33&file=index.js)

You can see that we defined the function without a `function` keyword and a function name.

You have to omit the `function` keyword and function name while writing an arrow function expression. Otherwise, JavaScript will throw a `SyntaxError`.

### Important stuff to know about the JavaScript arrow function expression

Here are three essential facts to remember when using an arrow function expression.

#### 1. The parameters' parentheses are optional

Suppose your arrow function contains only a single parameter. In such a case, you can omit its parentheses.

```js
const myFuncExpr = a => {
  return a + 20;
};

```

[**Try it on CodePen**](https://codepen.io/oluwatobiss/pen/OJQJejr)

#### 2. The curly brackets and `return` keyword are optional

Suppose your arrow function contains only a single statement. In that case, you can omit its curly brackets and the `return` keyword.

```js
const myFuncExpr = (x, y) => x + y;
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-8t2udu?devToolsHeight=33&file=index.js)

In the snippet above, we implicitly returned the sum of parameters `x` and `y` by removing the curly brackets and the `return` keyword.

**Note:** Whenever you choose to omit the curly brackets, also make sure that you remove the `return` keyword. Otherwise, the computer will throw a `SyntaxError`.

#### 3. Use parentheses to wrap any implicit object return

Suppose you wish to return an object implicitly. In such a case, wrap the object in a [grouping operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping) `(...)`.

For instance, consider the code below:

```js
const myFuncExpr = () => {
  carColor: "White",
  shoeColor: "Yellow",
};

```

[**Try it on CodeSandbox**](https://codesandbox.io/s/wrong-way-to-use-an-arrow-function-expression-to-return-an-object-implicitly-s8w132?file=/src/index.js)

The snippet above will throw a `SyntaxError` because JavaScript assumed the curly brackets (`{}`) to be the function body's code block—not an [object literal](https://codesweetly.com/javascript-properties-object).

Therefore, whenever you wish to return an object literal implicitly–without using the `return` keyword explicitly–make sure to encase the object literal in a grouping operator.

**Here's an example:**

```js
const myFuncExpr = () => ({
  carColor: "White",
  shoeColor: "Yellow",
});

```

[**Try it on CodeSandbox**](https://codesandbox.io/s/correct-way-to-use-an-arrow-function-expression-to-return-an-object-implicitly-p61l5c?file=/src/index.js)

Note that you can use the grouping operator to return any single value. For instance, the snippet below grouped the sum of `x` and `56`.

```js
const myFuncExpr = x => (x + 56);
```

[**Try it on CodePen**](https://codepen.io/oluwatobiss/pen/rNJNXeG)

Let's now discuss the fourth type of JavaScript function.

## What Is a JavaScript Immediately Invoked Function Expression?

An **immediately invoked function expression (IIFE)** is a function expression that invokes itself automatically.

**Note:** We sometimes call an IIFE a "Self-Invoking Function Expression" or "Self-Executing Anonymous Function Expression."

### Syntax of an IIFE

```js
(function() {
  /* ... */
})();

```

An IIFE is composed of three main components:

1. **A grouping operator:** The first pair of parentheses `()`
2. **A function:** Enclosed within the grouping operator
3. **An invocator:** The last pair of parentheses `()`

### Examples

Below are examples of an IIFE.

#### How to define a named IIFE

```js
(function addNumbers() {
  console.log(100 + 20);
})();

```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-nkjjnz?devToolsHeight=33&file=index.js)

The function in the snippet above is a named self-invoking function expression.

#### How to define an anonymous IIFE

```js
(function() {
  console.log(100 + 20);
})();

```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ywrmkt?devToolsHeight=33&file=index.js)

The function in the snippet above is an anonymous self-invoking function expression.

#### How to define an arrow function IIFE

```js
(() => console.log(100 + 20))();
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-xqlfgi?devToolsHeight=33&file=index.js)

The function in the snippet above is an arrow self-invoking function expression.

#### How to define an async IIFE

```js
(async () => console.log(await 100 + 20))();
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-ryxftq?devToolsHeight=33&file=index.js)

The function in the snippet above is an [asynchronous](https://codesweetly.com/asynchronous-javascript) self-invoking function expression.

So, now that we know what an Immediately Invoked Function Expression is, we can discuss how it works.

### How does an IIFE work?

By default, the computer does not know what [data type](https://codesweetly.com/javascript-data-types) [code](https://codesweetly.com/document-vs-data-vs-code#what-exactly-is-code) is until it evaluates it.

For instance, suppose you ask the computer to process `4`. In such a case, the system won't know if `4` is a number type until it evaluates it.

Therefore, JavaScript will throw a `SyntaxError` if you use any number method directly on `4`.

**Here's an example:**

```js
// Convert 4 to a string value:
4.toString();

// The invocation above will return:
"Uncaught SyntaxError: Invalid or unexpected token"

```

[**Try it on CodeSandbox**](https://codesandbox.io/s/how-iife-works-example-1-kc8g5b)

The computer threw a `SyntaxError` because it does not recognize `4` as a number data type.

However, suppose you assign `4` to a variable. In such a case, the computer will first convert it to a number data type before storing it into the variable.

Afterward, JavaScript will allow you to use any number methods on the number variable.

**Here's an example:**

```js
// Assign 4 to a variable:
const myNum = 4;

// Convert myNum's content to a string value:
myNum.toString();

// The invocation above will return:
"4"

```

[**Try it on CodeSandbox**](https://codesandbox.io/s/how-iife-works-example-2-jz4kwi)

The snippet above did not return any error because JavaScript evaluated `myNum` as a number data type.

But you don't have to assign `4` to a variable before the computer can evaluate its data type appropriately.

You can alternatively put your value in [parentheses](https://www.computerhope.com/jargon/p/parenthe.htm) to force the computer to evaluate its data type before using it for other things.

For instance, consider this snippet:

```js
// Evaluate 4's data type and turn it into a string value:
(4).toString();

// The invocation above will return:
"4"

```

[**Try it on CodeSandbox**](https://codesandbox.io/s/how-iife-works-example-3-rz4j9b)

The snippet above enclosed `4` in parentheses to make the computer evaluate its data type before using the [`toString()`](https://codesweetly.com/javascript-number-tostring-method) method to convert it to a string value.

Using parentheses to make JavaScript evaluate your code's data type first is what happens in an Immediately Invoking Function Expression (IIFE).

For instance, consider this example:

```js
// Evaluate the function's data type and immediately invoke it:
(function addNumbers() {
  console.log(100 + 20);
})();

// The invocation above will return:
120

```

[**Try it on StackBlitz**](https://stackblitz.com/edit/js-nkjjnz?devToolsHeight=33&file=index.js)

The snippet above enclosed the `addNumbers` function in parentheses to make the computer evaluate its data type before invoking it immediately after the evaluation.

## Overview

In this article, we discussed what a JavaScript function object is. We also used examples to see how it works.

Thanks for reading.

### **And here's a useful ReactJS resource:**

I wrote a book about React!

* It's beginner friendly ✔
* It has live code snippets ✔
* It contains scalable projects ✔
* It has plenty of easy-to-grasp examples ✔

The [React Explained Clearly](https://www.amazon.com/dp/B09KYGDQYW) book is all you need to understand ReactJS.

[![React Explained Clearly Book Now Available at Amazon](https://www.freecodecamp.org/news/content/images/2022/01/Twitter-React_Explained_Clearly-CodeSweetly-Oluwatobi_Sofela.jpg)](https://www.amazon.com/dp/B09KYGDQYW)



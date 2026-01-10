---
title: Function Declaration vs Function Expression
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-26T12:11:48.000Z'
originalURL: https://freecodecamp.org/news/function-declaration-vs-function-expression
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/26-function-declaration-vs-expression.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  When creating functions, you can use two approaches: declaration and expression.
  What''s the difference?

  When talking about functions in JavaScript, you would often hear function declarations
  and function expressions. Though these ap...'
---

By Dillion Megida

When creating functions, you can use two approaches: **declaration** and **expression**. What's the difference?

When talking about functions in JavaScript, you would often hear function declarations and function expressions. Though these approaches are almost similar, they have notable differences.

We'll look at the differences in this article.

I have [a video version of this topic](https://www.youtube.com/watch?v=cozcCZjkjto) you can also check out.

## Function Declaration

To declare a function, you use the `function` keyword and specify a name for the function. For example:

```js
function generateIntro(name) {
  return `Hi, my name is ${name}`
}

const dillion = generateIntro("Dillion")
console.log(dillion)

// Hi, my name is Dillion
```

Here, we have "declared" a function called `generateIntro`. You see we use the `function` keyword followed by the name of the function: "generateIntro"

Now let's look at function expression.

## Function Expression

Here, you create a function expression and assign it to a variable that can be called. You can do this in two ways.

### Function Expressions with the `function` keyword

One way to do this is to use the function keyword without a name, which makes it an anonymous function. Here's how:

```js
const generateIntro = function(name) {
  return `Hi, my name is ${name}`
}

const dillion = generateIntro("Dillion")
console.log(dillion)

// Hi, my name is Dillion
```

As you see here, we have the `function` keyword without a name for the function. This makes it an expression, which you have to assign to a variable (as we have done to `generateIntro` here).

**Note:** you can use `const`, `let` or `var` to declare the variable. You can learn more about the differences between these keywords [in this article](https://www.freecodecamp.org/news/differences-between-var-let-const-javascript/)

If we use the `function` keyword without a name, we create a function expression, which we have to assign to a variable, else we get an error. Here's what I mean:

```js
function(name) {
  return `Hi, my name is ${name}`
}

// SyntaxError: Function statements require a function name
```

We get an error: **SyntaxError: Function statements require a function name**. Without assigning it to a variable, JavaScript assumes it is a statement, and as the error says, you must provide a function name.

But when you assign it to a variable, you assign the expression, and when you call the variable (`variable()`), it will execute the logic of the function expression assigned to it.

### Arrow function expressions

You can also create function expressions with arrow functions. Arrow functions, introduced in ES6 allow you to write functions in a short manner. But **arrow functions cannot be declared; they can only be expressed**. Here's an example:

```js
const generateIntro = (name) => {
  return `Hi, my name is ${name}`
}

const dillion = generateIntro("Dillion")
console.log(dillion)

// Hi, my name is Dillion
```

The arrow function here is `(args) => {...}`. This is a function expression that we have assigned to `generateIntro`.

For the rest of this article, I'll focus on function expressions created with the `function` keyword but know that it also applies to arrow functions.

## Function Declarations vs Function Expressions

So what's the difference between these ways of creating functions and why does it matter?

It matters because these functions have different behaviors. And depending on what you want to achieve, one may be preferred over the other.

### 1. Expressed functions cannot be used before initialization

You can use a declared function before the line it was initialized. Here's what I mean:

```js
const result = sum(20, 50)
console.log(result)

console.log("hello")

function sum(num1, num2) {
  return num1 + num2
}

// 70
// "hello"
```

As you see here, we used `sum` on line 1, which is actually before the line was declared. What happens here is **hoisting**. `sum` is hoisted to the top of the code before the whole code is executed. This makes `sum` accessible before the line where it was actually created in the code.

When it comes to hoisting, **all functions and variables are hoisted**. But, functions created with function expressions cannot be "used" before their initialization.

Let's see an example using a function expression created with the `function` keyword:

```js
const result = sum(20, 50)
console.log(result)

console.log("hello")

const sum = function(num1, num2) {
  return num1 + num2
}

// ReferenceError: Cannot access 'sum' before initialization
```

We get an error: **ReferenceError: Cannot access 'sum' before initialization**. We get this error because when you declare variables with `let` or `const` (like we did for `sum` here), they are hoisted, but without a default initialization. You can learn more about what happens here in this article: [the hoisting behavior in let and const](https://www.freecodecamp.org/news/javascript-let-and-const-hoisting/)

Let's say we create the variable with `var` instead:

```js
const result = sum(20, 50)
console.log(result)

console.log("hello")

var sum = function(num1, num2) {
  return num1 + num2
}

// TypeError: sum is not a function
```

Now we get a new error: **TypeError: sum is not a function**. Although `var` variables are hoisted, they are hoisted with a default initialization of `undefined`. So attempting to call it like a function, that is `undefined()`, throws the error that "sum is not a function".

The same error would occur if it were an arrow function.

Therefore, **only declared functions can be used before initialization**.

### 2. Expressed functions need to be assigned to be used later

With declared functions, you already have the name: `function name...`. So you can use the function later: `name()`. But with function expressions, there's no name as we saw. It would be impossible to use such a function later unless we assigned it to a variable:

```js
const printName = function(firstname, lastname) {
  console.log(`${firstname} ${lastname}`)
}
```

Here, we assigned the function expression to `printName`. Now we can use that function logic later by calling `printName()`.

### 3. Anonymous functions are useful for anonymous operations

There are cases where you do not need to use a function later. You can execute the function instantly. In such cases, you do not need a name, so you can use a function expression instead of a declaration.

Let's see some examples.

#### Immediately Invoked Function Expressions (IIFEs)

IIFEs are functions that are immediately invoked after creation. Here's an example:

```js
(function() {
  console.log('deeecode')
})()

// deeecode
```

Or the arrow function equivalent:

```js

(() => {
  console.log('deeecode')
})()

// deeecode
```

This is an IIFE where we create a function that executes `console.log('deeecode')`. Immediately after creating the function, we execute it as you see at the end (`()`). Here, we do not intend to use the function later, so a function expression works fine.

Using a function declaration here will not throw an error, but the name of the function will be inaccessible:

```js
(function print(){
  console.log('deeecode')
})()

print()

// deeecode
// ReferenceError: print is not defined
```

Using a function declaration, the IIFE is executed, but you cannot access the name of the function outside the parenthesis.

#### Callback Functions

When using callback functions, you can also pass anonymous functions (function expressions). For example, using the `forEach` method of arrays which expects a callback function, we can use an anonymous function.

The syntax of the `forEach` method is:

```js
array.forEach(callbackFn)
```

`forEach` loops through each item in an array and executes the callback function on them. Let's see how we use a function expression for this:

```js
const array = [1, 2, 3]

array.forEach(function(value) {
  console.log(value)
})

// 1
// 2
// 3
```

As you see here, we passed a function expression (anonymous function) as an argument to `forEach`.

You can pass a function declaration instead, and the callback function will work. But, as we saw earlier, you won't be able to access the function later:

```js
const array = [1, 2, 3]

array.forEach(function print(value) {
  console.log(value)
})

// 1
// 2
// 3

// ReferenceError: print is not defined
```

As you see here, `print` is declared and used as the callback function, but you cannot access `print` afterward.

## Wrap up

Function declarations and function expressions are terms you would hear a lot around functions in JavaScript You can use function expressions to perform similar logic with function declarations, but it is worth noting the differences.

In this article, we've seen how function expressions and different from function declarations.

If you enjoyed this article, please give it a share :)



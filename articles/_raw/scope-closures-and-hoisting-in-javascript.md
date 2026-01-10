---
title: Scope, Closures, and Hoisting in JavaScript – Explained with Code Examples
subtitle: ''
author: Chidera Humphrey
co_authors: []
series: null
date: '2024-06-26T08:13:12.000Z'
originalURL: https://freecodecamp.org/news/scope-closures-and-hoisting-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/How-to-connect-Firebase-Authentication-with-Golang-app_20240625_101105_0000-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In the dynamic world of JavaScript, understanding the intricacies of scope,
  closures, and hoisting is fundamental for mastering the language and building robust
  applications.

  These concepts, though often misunderstood, play a crucial role in determin...'
---

In the dynamic world of JavaScript, understanding the intricacies of scope, closures, and hoisting is fundamental for mastering the language and building robust applications.

These concepts, though often misunderstood, play a crucial role in determining how variables and functions behave within the code.

Scope dictates the accessibility of variables, closures enable powerful programming patterns, and hoisting can lead to unexpected results if not understood properly.

In this comprehensive guide, we will delve deep into the realms of scope, closures, and hoisting in JavaScript, unraveling their complexities, providing practical examples, and offering best practices to empower you in your journey as a JavaScript developer.

So, buckle up as we embark on this enlightening exploration of JavaScript's dynamic trio.

## Table Of Contents

* [Prerequisites](#prerequisites)
    
* [Scope in JavaScript](#scope-in-javascript)
    
* [Types of scope in JavaScript](#types-of-scope-in-javascript)
    
* [Closures](#closures)
    
* [Hoisting](#hoisting)
    
    * [Variable hoisting](#variable-hoisting)
        
    * [Function hoisting](#function-hoisting)
        
    * [Class hoisting](#class-hoisting)
        
    * [Import hoisting](#import-hoisting)
        
* [Best practices](#best-practices)
    
* [Conclusion](#conclusion)
    

## Prerequisites

You should have a basic understanding of the JavaScript language to follow along with this article.

## Scope in JavaScript

In programming, scope refers to the context in which variables and functions are declared and accessed.

Scope determines the visibility and lifecycle of these variables and functions within a program, ensuring that they are used in the intended context.

In JavaScript, scope follows the concept of lexical scope. In lexical scope, the visibility of variables and functions are determined by the context in which the variables and functions are defined.

## Types of scope in JavaScript

In JavaScript, there are three main types of scope:

### Global scope

Variables and functions defined in the global scope can be accessed by any part of the program. Variables and functions that are declared in the global scope are said to be global-scoped.

```js

let globalScopeVariable = "I'm in the global scope";

  

function logScope(){

console.log(globalScopeVariable)

}

logScope(); // I'm in the global scope

  

for(let i=0; i<3; i++){

console.log(globalScopeVariable);

}

// I'm in the global scope

// I'm in the global scope

// I'm in the global scope

  

if(true){

console.log(globalScopeVariable);

}

// I'm in the global scope

  

console.log(globalScopeVariable); // "I'm in the global scope"
```

In the code above, the `globalScopeVariable` can be accessed by any part of the program, whether it's inside a function, loop, conditional statements, or in the global scope itself.

You can think of global scope as your local supermarket – everyone has access to it.

**Note**: when building real-world applications, it is recommended to minimize the number of variables that are global-scoped. This is to reduce unpredictability in your code which can lead to bugs.

### Function scope

When variables and functions are declared within functions, the variables and functions are in the function scope.

These variables and functions can only be accessed within the function they were declared in.

Variables declared in function scope are said to be function-scoped.

```js

function doubleNum(){

let num = 23;

console.log(num * 2)

}

doubleNum(); // 46

  

console.log(num); // Reference error: "num" is not defined
```

In the code above, logging `num` will result in a `Reference error` as `num` can only be accessed within `doubleNum` function.

You can think of function scope as a message sent to a group chat – only the group participants can view and interact with the message.

### Block scope

Curly braces, `{}`, denote a code block. Variables declared within these curly braces cannot be accessed outside the curly braces.

```js

{

let blockScopedVariable = "I'm block-scoped";

console.log(blockScopedVariable); // I'm block-scoped

}

  

console.log(blockScopedVariable); // ReferenceError: blockScopedVariable is not defined
```

In the code above, `blockScopedVariable` can only be accessed within the curly braces as it was defined inside the curly braces.

Though block scope seems similar with function scope, there's a little difference.

The key difference between block scope and function scope is that function scope refers to variables defined within functions, while block scope refers to variables defined in a pair of curly braces.

You can say that function scope is a subset of block scope.

**Note**: variables declared within a function using `var` cannot be accessed outside that function.

```js

function logScope(){

var x = 4;

}

console.log(x); // ReferenceError: x is not defined
```

## Closures

A closure is the combination of a function and its lexical scope. In other words, a closure is a function defined in another function that remembers its lexical environment.

Remembering its lexical environment means that closure function has access to variables declared within the parent function, even after the parent function has finished executing.

```js

function parentFunction(){

let x = 3;

function childFunction(y){

return x + y

}

return childFunction

}

  

let res = parentFunction();

  
  

console.log(res(6));
```

In the code above, `childFunction` forms a closure inside `parentFunction`. `childFunction` has access to variables defined in the `childFunction`'s lexical environment even after `parentFunction` has finished executing in `let res = parentFunction()`. This is why `console.log(res(6))` gives `9`.

## Hoisting

Hoisting in JavaScript refers to the process by which the JavaScript interpreter moves the declaration of variables, functions, classes, and imports to the top of the code before execution.

You can view hoisting as declarations being "lifted" up before code execution.

### Variable hoisting

Only variables declared using `var` are hoisted. This is because `var` is not block-scoped, meaning that the `var`\-declared variable can be referred to anywhere in its scope regardless of the position of the variable's declaration.

```js

console.log(x); // undefined

var x = 4;
```

Running the code above will log `undefined` to the console. This is because only variable declarations are hoisted or 'lifted up' and not the initializations.

Prior to code execution, the code will look like this:

```js

var x;

console.log(x);

x = 4
```

**Tip**: `var x` is the variable declaration. `x = 4` is the initialization.

Variables declared with `let` and `const` are not hoisted. This means that referring to the variables before declaration results in `ReferenceError`.

```js

console.log(y); // ReferenceError: Cannot access "y" before initialization

let y = 3;
```

### Function hoisting

Functions are hoisted just like `var`\-declared variables.

```js

console.log(addNums(1,3)); // 4

  

function addNums(a,b){

return a + b;

}
```

During execution, the code looks like this:

```js

function addNums(a,b){

return a + b;

}

  

console.log(addNums(1,3));
```

However, it's important to know that only function declarations are hoisted. Function expressions are not hoisted.

```js

console.log(addNums(1,3)); // ReferenceError: cannot access "addNums" before initialization

  

const addNums = function (a,b) {

return a + b;

}
```

Running the code above will result in a `ReferenceError`.

### Class hoisting

Unlike function declaration, class declarations are not hoisted. This means you cannot accessed a class before its declaration.

```js

new Car(); // ReferenceError: cannot access "Car" before initialization

class Car{}
```

### Import hoisting

Import declarations are hoisted. This means that all methods and functions of an imported value are accessible in another module even before its declaration.

```js
const sum = f.add(2+3);

import f from './library/package'
```

In the code above, `f` functions and methods are accessible even though the declaration comes later.

## Best practices

### Keep scope as local as possible

You should keep your scope local as possible.

When creating variables, you should aim to create the variables where you want to use them. This is especially true if you are going to be using the variables in only one or few parts of your code.

```js
const num = 3;

function addNum(){
	return 2 + num; // 3
}

function multiplyNum(a){
	return 3 * a;
}
```

In the code above, `num` is used only once, in the `addNum` function. It is a better practice to declare `num` inside of the `addNum` function.

```js
function addNum(){
	const num = 3;
	return 2 + num;
}

// rest of code
```

For better modularity, you can pass `num` as an argument to the `addNum` function.

```js
function addNum(num){
	return 2 + num
}
addNum(3); //5
```

### Use closures to protect data

In programming, there are times you may want to protect some variables from being accessed from outside of an object. This is where closures can be very useful.

Use closures to protect private data from outside functions and other parts of your code.

```js
function encapsulateData(){
	const user = {
		name: 'Chidera',
		age: 23
	}
	return updateUserAge(){
		return data.age++;
	}
}

const updateHandler = encapsulateData();
const updatedAge = updateHandler(); // 24
console.log(user); // undefined
```

In the code above, `updateAge` increases the age of the user without `user` being accessible from the outside.

### Declare variables and functions before using them

It is recommended to always declare variables before using them. This helps to avoid unpredictability and unwanted bugs in your code.

### Always use `let` and `const` to create variables

`let` and `const` are the standard way of declaring variables in JavaScript. They remove the unpredictable code behavior that comes with using `var`.

There is almost no reason to use `var` to declare variables in modern JavaScript.

## Conclusion

In summary, scopes determine where a variable can be accessed.

Scope can be divided into three: global, local, and block scopes.

Closures are functions inside a function. Closure functions have access to parent function variables, even after the parent function has returned. Closure is a crucial part of asynchronous JavaScript.

Hoisting makes variables accessible even before their creation.

Remember to adhere to best practices when working with closures and hoisting. Declaring variables before usage and using closures to encapsulate data can help to prevent code unpredictability and protect private data.

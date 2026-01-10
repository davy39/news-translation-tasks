---
title: What is a Function? JavaScript Function Examples
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-07T23:46:55.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-function-javascript-function-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/blake-connally-B3l0g6HLxr8-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Functions are one of the main parts of computer programs.

  They are widely used and are one of JavaScript''s fundamental building blocks.

  In this article, we''ll go over the definition of functions and why they are so
  important. I''ll also show you how t...'
---

Functions are one of the main parts of computer programs.

They are widely used and are one of JavaScript's fundamental building blocks.

In this article, we'll go over the definition of functions and why they are so important. I'll also show you how to get started writing functions in JavaScript.

Let's dive in!

## What is a function in JavaScript?

A function is a block of code that encapsulates one isolated, self-contained behavior for the computer to perform.

Functions are a set of of organised instructions that correspond to a certain task or specific functionality a user wants to implement in their program to achieve a single desired outcome.

The code inside a function runs only when it is needed, meaning only when it is *called*.

Functions are an important and useful part of programming because they create reusable code.

Instead of copying, pasting, and repeating the same code throughout different parts of your program, you can write that code only in one place using a function. Then you can use it over and over again whenever you have to.

This also helps when you want to implement changes to your program or debug and try to fix an error.

Instead of looking for the different parts where your code could be, you only have to look at one particular place which makes your code more readable.

## How to declare functions in JavaScript

The general syntax for creating a function in JavaScript looks like this:

```Javascript
function name(parameter1,parameter2,...) {
    // the code statements to be executed
}
```

Let's break it down:

- You declare a function with the `function` keyword.
- Next, you give the function a name of your choosing. Function names in JavaScript are case sensitive and a convention and best practice is to use `camelCase`.
- The function name is followed by a set of opening and closing parentheses. 

Functions are able to take in data by taking *inputs*. These inputs are enclosed in the parentheses and are called *parameters*. 

Parameters act as local placeholder variables for the values that will be passed into the function as inputs when the function is called. They are entirely optional and if there is more than one, you separate them by a comma.
- Lastly comes the curly braces, and inside them the main body of the function with the code statements to be executed when the function is called. This is where the inputs to the function are processed.

### How to declare and call a simple function in JavaScript

```javascript

function greeting() {
  console.log('Hello World!');
}
```

Above, we created a function called `greeting`. 

This function is a very basic one and you can't do much with it. It doesn't take in any inputs and the only thing that happens is the text `Hello World!` gets printed to the console.

Defining a function in and of itself doesn't run the code inside the function's body. For the code to be executed, and in order to see that message in the console, the function has to be called. This is also known as a *function invocation*.

To call a function that doesn't accept inputs, you just write the function's name followed by parentheses and a semicolon at the end.

```javascript
greeting();

//output
//Hello World!
```

Now you can reuse this function many times by just calling the function itself many times. This helps you avoid repeating code:

```javascript
greeting();
greeting();
greeting();

//output
// Hello World!
// Hello World!
// Hello World!
```


### How to declare and call functions with parameters in JavaScript

We can modify the previous example to take inputs. We'll do this with parameters, as mentioned earlier.

Parameters are values that you pass in to the function when the function is being *declared*. 

```javascript
function greeting(name) {
  console.log('Hello ' + name + ' !' );
}
```

The function named `greeting` now accepts one parameter,`name`. That string is being concatenated (`+`) with the string `Hello ` and an exclamation mark at the end.

When calling functions that accept paraemeters, you need to pass arguments in.

Arguments are values that you supply when calling the function and they correspond with the parameters that have been passed in the function's decalaration line.

For example:

```javascript
greeting('Jenny');
//Output
// Hello Jenny !
```

The argument is the value `Jenny` and you can think of it as `name = 'Jenny'`. `name`, the parameter, is the placeholder variable, and `Jenny` is the value you pass in when you call the function.

Functions can accept more than one parameter and can also return data back to the user of the program:


```javascript
function addNums(num1,num2) {
    return num1 + num2;
}
```

The above code created a function named `addNums` that takes in two parameters – `num1` and `num2`, separated by a comma. 

The same way functions have inputs, they also outputs *outputs*

The function *returns* as its output the sum of `num1` and `num2`. This means that it processes the two parameters, does the requested calculation, and returns the end value as a result back to the user.

When the function is called, two arguments have to be passed in since it accepts two parameters:

```javascript
addNums(10,20);
//Output
// 30
// think of it as num1 = 10 and num2 = 20
```

Each time the function is called, you can pass in different arguments:

```javascript
addNums(2,2);
// 4
addNums(3,15);
//18
```

### Variable scope in JavaScript functions

Variable scope refers to how *visible* variables are to different parts of the program.

A variable defined *outside* and *before* a function block has a global scope and can be accessed from inside a function:

```javascript
const num = 7;

function myFunc() {
  console.log(num);
}

//Access the variable with a global scope from anywhere in the program:
console.log(num);
//Output
//7

//Call the function with the variable with global scope
myFunc();
//Output
// 7
```

But if that variable was defined *inside* the function, it would have local scope and it would be limited and visible only in the function where it was defined.

You cannot access it from outside the function:

```javascript
function myFunc() {
  const num = 7;
  console.log(num);
}

// Try to access the variable with local scope from outside the function scope:
console.log(num);
//Otput:
//Uncaught ReferenceError: num is not defined

//Call the function with the variable defined inside the function:
myFunc();
//Ouput
//7
```

### Function Expressions

You can also create functions using expressions. 

These functions are created inside an expression instead of being created  with a function declaration like you've seen so far.

```javascript
const name = function(firstName) {
  return 'Hello ' + firstName ;
  }
```

Here, we use the variable `name` to store the function.

To call the function, you use the variable name like this:

```javascript
console.log(name('Jenny'));
//Output
//"Hello Jenny"
```

This type of function is also called an Anonymous function because they do not require a name.

The differences between a Named function and an Anonymous one are listed below:

```javascript

//named
function name(firstName) {
    console.log('Hello ' + firstName);
 }
 
name('Jenny');
 
//anonymous
const name = function(firstName) {
  return 'Hello ' + firstName ;
  }
 console.log(name('Jenny')); 
```

The variables in anonymous functions can be used as values to other variables too:

```javascript
const name = function(firstName) {
  return 'Hello ' + firstName ;
  }
  
const myName = name('Timmy');
console.log(myName);
//Ouput
//"Hello Timmy"
```

## Conclusion

And there you have it! This marks the end of our introduction to JavaScript functions and some of the ways you can create them.

If you want to learn more, [arrow functions](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) are a new and more efficient way to create functions in JavaScript and they were introduced with ES6.

If you want to start learning the fundamentals of JavaScript interactively and gain a well-rounded understanding of the language while building  projects along the way, freeCodeCamp has a free [JavaScript Algorithms and Data Structures Certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/).

Thanks for reading and happy learning!





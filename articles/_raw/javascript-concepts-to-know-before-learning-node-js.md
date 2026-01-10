---
title: JavaScript Concepts to Know Before Learning Node.js
subtitle: ''
author: Musab Habeeb
co_authors: []
series: null
date: '2023-09-19T15:12:57.000Z'
originalURL: https://freecodecamp.org/news/javascript-concepts-to-know-before-learning-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/JavaScript-Concepts-to-master-before-Node.js.png
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: null
seo_desc: 'Before Node.js came into existence, JavaScript could only be run on the
  browser. It could only be used as a scripting language for frontend web development.

  Then, Node.js came to free JavaScript from this confinement. It made JavaScript
  ubiquitous (m...'
---

Before Node.js came into existence, JavaScript could only be run on the browser. It could only be used as a scripting language for frontend web development.

Then, Node.js came to free JavaScript from this confinement. It made JavaScript ubiquitous (meaning it could now be run everywhere).

Node.js is a JavaScript runtime environment that allows JavaScript developers to write command line tools and server side scripts outside of a browser.

Learning Node.js enables JavaScript developers to write server side code and code for embedded systems. This opens up opportunities in backend development and hardware programming.

But, before diving into Node.js, a JavaScript developer has to learn and understand some JavaScript concepts.

In this article, you are going to learn the JavaScript concepts you need to understand before learning Node.js.

Before you continue with the article, check the prerequisites.

## Prerequisites

To follow along with this article, you should have some basic knowledge of:

* JavaScript
    
* The browser console (this is where you will run your code).
    

Now that we have those out of our way, let's dive into the article, starting with expressions.

## Expressions

An expression is a unit or block of code that evaluates to a value.

There are five basic categories of expressions in JavaScript: primary expressions, arithmetic expressions, string expressions, logical expressions, and left-hand side expressions.

### Primary expressions

Primary expressions consist of basic keywords in JavaScript. A common example is the `this` keyword:

```js
this['item'];

this.item;
```

Later on in this article you will learn more about the `this` keyword.

### Arithmetic expressions

An arithmetic operator takes numerical values as its operands and returns a numerical value. The operands and the operator make up the arithmetic expression:

```js
2 + 3;

2 * 3;

2 ** 3;
```

### String expressions

When strings are concatenated they form string expressions:

```js
console.log('My name is' + 'Peter');
```

### Logical expressions

Logical expressions are expressions in which various values are compared:

```js
10 > 2;
2 < 10;
c === 2 || d === 10;
```

### Left-hand side expressions

Left-hand side expressions are expressions where values are assigned to a variable:

```js
// variables
a = 2;

// object properties
obj = {};
obj.name = 'Paul';
```

## Data Types

There are 8 data types in JavaScript: String, Number, Boolean, Object, Null, Undefined, Symbol, and BigInt.

### String

The string type represents textual data. A string is surrounded by a single quote or a double quote.

Each element in a string occupies a certain position in the string. The first element is at index 0, and the second and third are at index 1 and 2 respectively.

Here is an example of a string:

```js
let name = 'Yusuf';
let newName = "Joseph";
```

### Number

The number types are stored in 64-bit format, also known as double-precision floating point numbers.

They consist of numbers that are within the range of -(2<sup>53</sup> - 1) and (2<sup>53</sup> – 1), with both of these numbers inclusive. These two numbers are known as the `MIN_SAFE_INTEGER` and the `MAX_SAFE_INTEGER` respectively.

Numbers that exceed this range, belong to another data type called BigInt.

Here is an example of a positive integer, a float and a negative integer:

```js
let number = 15;
let anotherNumber = 1.5;
let lastNumber = -3;
```

### Boolean

The boolean type is logical, and it has only two values: true or false. It is commonly used in loops and conditional statements.

In the example below, I declared variables and assigned them a value of true and false respectively.

Then, I created a conditional statement that returns 1 if the `bool` variable is true or -1 if it is false. It returns zero if it is neither true nor false.

```js
let positive = true;
let negative = false;
let bool = false;

// conditional statement
if (bool) {
    return 1;
} else if (bool) {
    return -1;
} else {
    return 0;
}
```

### Object

An object type allows you to store collections of data. The data are stored in a pair of curly braces and a key-value pair format. Object keys must be textual (for example a string).

An object can store any of the other data types, like string, number, arrays, booleans, and so on.

In the example below I created an object named `myObject`, and gave it three keys with their corresponding values:

```js
let myObject = {
    name: "Gabriel",
    number: 15,
    developer: [true, "Daniel", 1]
}
```

### Null

Null data types are special data types. They have the value null which means that the value is unknown or empty:

```js
let unknown = null;
```

### Undefined

Unlike null, undefined means that a variable is declared and not assigned a value. A variable can also be assigned undefined specifically:

```js
let name = undefined;

let newName;
console.log(newName);
```

### Symbol

Symbols are used to create unique values. They are created by calling the `Symbol()` function. Every time the `Symbol()` function is invoked it creates a new unique value.

Symbols are kept hidden or private and they can only be used internally. For instance, they can be used as keys in an object. When you try to get the list of keys in an object where a symbol is part of its keys the symbol key will not be displayed.

You can pass a parameter to the symbol function to serve as a description for the symbol when debugging it in the console:

```js
let firstSymbol = Symbol();

let anotherSymbol = Symbol(anotherSymbol);
```

### BigInt

BigInt is a special type of number that provides support for numbers with a length that a normal number type can not hold (such as numbers that exceed the safe integer limit).

It can be created by appending n to the end of an integer or passing a number into the `BigInt` function:

```js
let bigNumber = 175337823472347884278247898427427427642n;
let newBigNumber = BigInt(1624743724724724898718247248744774227422n);

let anotherBigNumber = BigInt(14);
```

## Classes

A JavaScript class is a template for creating objects. It contains data and functions that manipulate data.

Classes were introduced to JavaScript in the ECMAScript 2015 (ES6) version of JavaScript.

The functions used in classes are called methods.

There is a basic syntax for declaring classes looks something similar to the following:

```js
class TemplateClass {
    constructor() {...};
    method() {...};
    method() {...};
}
```

From the syntax you can create a class named `Visitor`:

```js
class Visitor {
    constructor(name) {
        this.name = name;
    }
    introduce() {
        console.log(`My name is ${this.name} and I am a visitor`)
    }
}
```

You can create a new class from this class by using the new class syntax. The newly created class can access any method from its parent class:

```js
let visitor = new Visitor("Jeff");

// visitor can call the introduce method in its parent class.
visitor.introduce();
```

## Variables

A variable is a named storage for JavaScript data. JavaScript variables can be declared in three ways:

* Using the `var` keyword
    
* Using the `let` keyword
    
* Using the `const` keyword
    

### How to declare variables using the `var` keyword

Variables declared with the `var` keyword are function scoped and they can be redeclared:

```js
var num = 1;

// num can be redeclared
var num = 2;
```

### How to declare variables using the `let` keyword

Variables declared with the `let` keyword are block scoped and they cannot be redeclared – they can only be reassigned:

```js
let fruit = "banana";

// fruit can only be reassigned
fruit = "orange";
```

### How to declare variables using the `const` keyword

Variables declared with the const keyword are block scoped and they cannot not be redeclared or reassigned (meaning they are constant):

```js
const bestStudent = "Daniel";
```

## Functions

A function is a block of code that performs a specific task. It can be declared using the `function` keyword:

```js
function doSomething() {
    return "Does Something";
}
```

A function takes inputs called arguments and outputs results.

To execute a function you will invoke the function by calling the function name with enclosed brackets:

```js
function addNumbers(a, b) {
    return a + b;
}

addNumbers();
```

You can assign a function to a variable and call the variable when you want to invoke the function:

```js
function addNumbers(a, b) {
    return a + b;
}

let numberAddition = addNumbers(2, 3)
numberAddition();
```

## Arrow Functions

Arrow functions are a concise and compact way to write a function. They have some deliberate limitations in their usage:

* They cannot be used as a method.
    
* They cannot be used as a constructor.
    
* Arrow functions cannot use yield within their own bodies.
    

Below is the syntax for an arrow function:

```js
const doSomething = () => {
    return "Do something";
}
```

An arrow function can also take an argument.

```js
const multiplyNumbers = (a, b) => {
    return a * b;
}
```

## `this` keyword

The `this` keyword in JavaScript refers to an object that is executing a function or a code.

The `this` keyword can be used in different contexts – the context in which the `this` keyword is used determines what it refers to.

The `this` keyword can be used:

* In an object method.
    
* Alone.
    
* In object method bindings.
    

### How to use the `this` keyword in an object method

The `this` keyword refers to the object whenever it is used as an object method:

```js
intro : function() {
    return "My name is" + this.name "and, I am a" + this.occupation;
}
```

### How to use the `this` keyword alone

When `this` is used alone it refers to the global object:

```js
let wes = this;
```

### How to use the `this` keyword in object method bindings

When `this` is used in an object method, it refers to the object:

```js
let student = {
  firstName  : "Juliana",
  lastName   : "Carpe",
  myFunction : function() {
    return this;
  }
};
```

## Loops

Loops are useful for executing a block of code for a specified number of times based on some specified conditions. There are different types of loops in JavaScript:

* `for` loops
    
* `for ... in` loops
    
* `for ... of` loops
    
* `while` loops
    
* `do ... while` loops
    

### How to use `for` loops

`for` loops are used to execute a block of code a number of times:

```js
for (let i = 0; i < 5; i++) {
    return i;
}
```

### How to use `for ... in` loops

`for ... in` loops are used to loop through the properties of an object:

```js
for (let prop in obj) {
    return obj.prop;
}
```

### How to use `for ... of` loops

`for ... of` loops are used to loop through the values of iterable objects like arrays, strings, maps, and so on:

```js
let numArr = [2, 4, 6, 8]
for (let val of numArr) {
    return val ** 2
}
```

### How to use `while` loops

`while` loops are used to execute a block of code while a certain condition still holds true:

```js
while (i < 20) {
    return i;
    i++;
}
```

### How to use `do ... while` loops

`do ... while` loops execute a block of code first without any conditions. For as long as a certain condition still holds true it continues to execute the block of code:

```js
let i = 3;
do {
    return i;
    i++;
} 
while (i < 4)
```

## Scopes

The scope is the current context of execution. It is where variables and expressions can be accessed.

There is an hierarchical arrangement of scope in JavaScript. This makes it possible for lower scopes to access higher scopes.

The scopes in JavaScript are:

* Global scope
    
* Module scope
    
* Function scope
    
* Block scope
    

The global scope is the default scope for all codes running in script mode while the module scope is the default scope for all codes running in module mode.

The function scope is created by functions while the block scope is created by variables.

Here is an example of function and block scope:

```js
// function scope
function introduce(name) {
    let age = 12;
    console.log(`My name is ${name}`);
    console.log(`I am ${age} years old`);
}

let firstAge = 13

// block scope
if (firstAge === 13) {
    let secondAge = 20;
    console.log(`I am ${secondAge} years old`);
}
```

## Arrays

An array is a special type of an object that stores data in an ordered form.

Arrays can be declared in two ways:

* Using square brackets.
    
* Using the the `Array()` constructor.
    

### How to declare arrays using square brackets

This is the common way of creating an array. It is done by wrapping the array's items in a pair of square brackets:

```js
  let array = [1, 3, "a", "c"];
```

### How to declare arrays using the the `Array()` constructor

The `Array()` constructor does the same thing as the bracket notation. It can be called with or without the `new` keyword:

```js
  let anotherArray = Array(1, 2, 3, "go");
```

### How to access array elements

Array elements can be accessed in three ways:

* using their index.
    
* using the array's `length` property.
    
* using a loop
    

#### How to access an array element using its index

You call the name of the array with a square bracket containing the index you want to access:

```js
 let newArray = ["Idris", "Daniel", "Joseph"];

  // To access first element
  let firstElement = newArray[0]; 
  console.log(firstElement);  // Idris

  // To access second element 
  let secondElement = newArray[1];  
  console.log(secondElement);  // Joseph
```

### How to access an array element using the array's `length` property

You can get the length of the array using the `length` property. Then, you will subtract any number from it to get the index of the element you want to access:

```javascript
let newArray = ["Idris", "Daniel", "Joseph"];

  let length = newArray.length;

  let firstElement = newArray[length - 3]; 
  console.log(firstElement);  // Idris

  let secondElement = newArray[length - 2];
  console.log(secondElement);  // Joseph
```

#### How to access an array element using a loop

Array elements can be accessed using loops. You can make use of a `for` loop, `while` loop, or a `for ... of` loop:

```js
  let newArray = ["Idris", "Daniel", "Joseph"];
  for (let i = 0; i < newArray.length; i++) {
      return newArray[i]
  }
```

### Important Array methods

There are over fifteen array methods in JavaScript. In this article, you will learn the ones that are most useful in Node.js:

* `push()` and `pop()`
    
* `shift()` and `unshift()`
    
* `map()`
    
* `sort()`
    
* `forEach()`
    

#### How to use the `push()` and `pop()` methods

The `push()` method is used to add an item to the end of an array, while the `pop()` method is used to remove an item from the end of an array:

```js
let arr = [1, 2, 3, 9]

arr.push(21);

console.log(arr)    // [1, 2, 3, 9, 21]

arr.pop()

console.log(arr)    // [1, 2, 3, 9]
```

#### How to use the `unshift()` and `shift()` methods

The `unshift()` method is used to add an item to the beginning of an array, while the `shift()` method is used to remove an item from the beginning of an array:

```js
let arr = [1, 2, 3];

arr.unshift(0);

console.log(arr);	// [0, 1, 2, 3]

arr.shift();

connsole.log(arr);	// [1, 2, 3]
```

#### How to use the `map()` method

The `map()` method iterates through the elements of an array and calls a function on each element of the array. It returns a new array that contains the result of each function call:

```javascript
let fruits = ["Apple", "Grape", "Cashew"];

let mappedFruits = fruits.map(item => item + "s");
console.log(mappedFruits); // ["Apples", "Grapes", "Cashews"]
```

#### How to use the `sort()` method

The `sort()` method sorts an array in place and returns the same array in a sorted form.

The default order of the `sort()` method is ascending order. Strings are sorted in alphabetical order:

```javascript
let numbers = [8, 7, 5];
let fruits = ["Apple", "Grape", "Cashew"];

let sortedNumbers = numbers.sort();
let sortedFruits = fruits.sort()

console.log(sortedNumbers);  // [5, 7, 8]
console.log(sortedFruits);  // ["Apple", "Cashew", "Grape"]
```

#### How to use the forEach() method

The `forEach()` method loops through the array and calls a function for every element of the array:

```javascript
let fruits = ["Apple", "Grape", "Cashew"];

fruits.forEach(fruit => console.log(fruit));
//  "Apple"
//  "Grape"
//  "Cashew"
```

## Template Literals

Template literals are enclosed in backticks, just like strings are enclosed in quotes. They allow you to store multiline strings and also interpolate strings with embedded expressions.

The example below shows a basic template literal:

```js
let basic = `I write codes`
```

You can write a template literal that stores multiline strings like this:

```js
let multiLine = `I write codes                     
		I debug codes`;
```

You can use the dollar sign and curly braces to embed expressions in template literals.

In the example below, the function `myName` is embedded in the display variable with a template literal:

```js
function myName(Musab, Habeeb) {        
    alert("Musab Habeeb");    
}    

let display = `This displays my name ${myName()}`
```

## Strict mode

JavaScript is a sloppy language in the sense that it allows you to write code that is not allowed in other languages. Some of the code you write in JavaScript has errors but, JavaScript does not throw an error.

Strict mode does the following:

* It throws errors for JavaScript silent errors.
    
* It fixes mistakes that makes it difficult for JavaScript engines to perform optimizations.
    
* It prohibits some syntax likely to be defined in future versions of the ECMAScript.
    

Strict mode works in an entire script file and functions, but it does not work in block scopes.

To invoke script mode you will add the `"use strict";` syntax to the top of the code you want to apply it to. You can apply strict mode to a script like this:

```js
"use strict";

let name = "Musab";

console.log(name);
```

Also, you can apply strict mode to a function like this:

```js
function sayHi(name) {
    "use strict";
    console.log(`Hi ${name}`);
}
```

## Conclusion

Finally, you are done with learning the JavaScript concepts you need to understand before learning Node.js.

All these concepts are important concepts that a JavaScript Developer aspiring to learn Node.js should understand. Understanding these concepts will make learning Node.js easier.

But, to understand these concepts in depth, you can do more research on each of them and read other articles. Keep learning, keep building.

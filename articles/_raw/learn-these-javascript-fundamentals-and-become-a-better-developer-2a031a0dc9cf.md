---
title: Learn these JavaScript fundamentals and become a better developer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-28T21:46:32.000Z'
originalURL: https://freecodecamp.org/news/learn-these-javascript-fundamentals-and-become-a-better-developer-2a031a0dc9cf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2K1k1leVNAnXnscL1KBjEQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  JavaScript has primitives, objects and functions. All of them are values. All are
  treated as objects, even primitives.

  Pr...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

JavaScript has primitives, objects and functions. All of them are values. All are treated as objects, even primitives.

### Primitives

Number, boolean, string, `undefined` and `null` are primitives.

#### Number

There is only one number type in JavaScript, the 64-bit binary floating point type. Decimal numbers’ arithmetic is inexact.

As you may already know, `0.1 + 0.2` does not make `0.3` . But with integers, the arithmetic is exact, so `1+2 === 3` .

Numbers inherit methods from the `Number.prototype` object. Methods can be called on numbers:

```
(123).toString();  //"123"
(1.23).toFixed(1); //"1.2"
```

There are functions for converting strings to numbers : `Number.parseInt()`, `Number.parseFloat()` and `Number()`:

```
Number.parseInt("1")       //1
Number.parseInt("text")    //NaN
Number.parseFloat("1.234") //1.234
Number("1")                //1
Number("1.234")            //1.234
```

Invalid arithmetic operations or invalid conversions will not throw an exception, but will result in the `NaN` “Not-a-Number” value. `Number.isNaN()` can detect `NaN` .

The `+` operator can add or concatenate.

```
1 + 1      //2
"1" + "1"  //"11"
1 + "1"    //"11"
```

#### String

A string stores a series of Unicode characters. The text can be inside double quotes `""` or single quotes `''`.

Strings inherit methods from `String.prototype`. They have methods like : `substring()`, `indexOf()` and `concat()` .

```
"text".substring(1,3) //"ex"
"text".indexOf('x')   //2
"text".concat(" end") //"text end"
```

Strings, like all primitives, are immutable. For example `concat()` doesn’t modify the existing string but creates a new one.

#### Boolean

A boolean has two values : `true` and `false` .  
The language has truthy and falsy values.  
`false`, `null`, `undefined`, `''`(empty string), `0` and `NaN` are falsy. All other values, including all objects, are truthy.

The truthy value is evaluated to `true` when executed in a boolean context. Falsy value is evaluated to `false`. Take a look at the next example displaying the `false` branch.

```
let text = '';
if(text) {
  console.log("This is true");
} else {
  console.log("This is false");
}
```

The equality operator is `===`. The not equal operator is `!==` .

### Variables

Variables can be defined using `var`, `let` and `const`.

`var` declares and optionally initializes a variable. Variables declared with `var` have a function scope. They are treated as declared at the top of the function. This is called variable hoisting.

The `let` declaration has a block scope.

The value of a variable that is not initialize is `undefined` .

A variable declared with `const` cannot be reassigned. Its value, however, can still be mutable. `const` freezes the variable, `Object.freeze()` freezes the object. The `const` declaration has a block scope.

### Objects

An object is a dynamic collection of properties.

The property key is a unique string. When a non string is used as the property key, it will be converted to a string. The property value can be a primitive, object, or function.

The simplest way to create an object is to use an object literal:

```
let obj = {
  message : "A message",
  doSomething : function() {}
}
```

There are two ways to access properties: dot notation and bracket notation. We can read, add, edit and remove an object’s properties at any time.

* get: `object.name`, `object[expression]`
* set: `object.name = value,` `object[expression] = value`
* delete: `delete object.name`, `delete object[expression]`

```
let obj = {}; //create empty object
obj.message = "A message"; //add property
obj.message = "A new message"; //edit property
delete obj.message; //delete property
```

Objects can be used as maps. A simple map can be created using `Object.create(null)` :

```
let french = Object.create(null);
french["yes"] = "oui";
french["no"]  = "non";
french["yes"];//"oui"
```

All object’s properties are public. `Object.keys()` can be used to iterate over all properties.

```
function logProperty(name){
  console.log(name); //property name
  console.log(obj[name]); //property value
}
Object.keys(obj).forEach(logProperty);
```

`Object.assign()` copies all properties from one object to another. An object can be cloned by copying all its properties to an empty object:

```
let book = { title: "The good parts" };
let clone = Object.assign({}, book);
```

An immutable object is an object that once created cannot be changed. If you want to make the object immutable, use `Object.freeze()` .

#### Primitives vs Objects

Primitives (except `null` and `undefined`) are treated like objects, in the sense that they have methods but they are not objects.

Numbers, strings, and booleans have object equivalent wrappers. These are the `Number`, `String`, and `Boolean` functions.

In order to allow access to properties on primitives, JavaScript creates an wrapper object and then destroys it. The process of creating and destroying wrapper objects is optimized by the JavaScript engine.

Primitives are immutable, and objects are mutable.

### Array

Arrays are indexed collections of values. Each value is an element. Elements are ordered and accessed by their index number.

JavaScript has array-like objects. Arrays are implemented using objects. Indexes are converted to strings and used as names for retrieving values.

A simple array like `let arr = ['A', 'B', 'C']` is emulated using an object like the one below:

```
{
  '0': 'A',
  '1': 'B',
  '2': 'C'
}
```

Note that `arr[1]` gives the same value as `arr['1']` : `arr[1] === arr['1']` .

Removing values from the array with `delete` will leave holes. `splice()` can be used to avoid the problem, but it can be slow.

```
let arr = ['A', 'B', 'C'];
delete arr[1];
console.log(arr); // ['A', empty, 'C']
console.log(arr.length); // 3
```

JavaScript’s arrays don’t throw “index out of range” exceptions. If the index is not available, it will return `undefined`.

Stack and queue can easily be implemented using the array methods:

```
let stack = [];
stack.push(1);           // [1]
stack.push(2);           // [1, 2]
let last = stack.pop();  // [1]
console.log(last);       // 2

let queue = [];
queue.push(1);           // [1]
queue.push(2);           // [1, 2]
let first = queue.shift();//[2]
console.log(first);      // 1
```

## Functions

Functions are independent units of behavior.

Functions are objects. Functions can be assigned to variables, stored in objects or arrays, passed as an argument to other functions, and returned from functions.

There are three ways to define a function:

* Function Declaration (aka Function Statement)
* Function Expression (aka Function Literal)
* Arrow Function

## The Function Declaration

* `function` is the first keyword on the line
* it must have a name
* it can be used before definition. Function declarations are moved, or “hoisted**”,** to the top of their scope.

```
function doSomething(){}
```

The Function Expression

* `function` is not the first keyword on the line
* the name is optional. There can be an anonymous function expression or a named function expression.
* it needs to be defined, then it can execute
* it can auto-execute after definition (called “IIFE” Immediately Invoked Function Expression)

```
let doSomething = function() {}
```

## Arrow Function

The arrow function is a sugar syntax for creating an anonymous functionexpression.

```
let doSomething = () => {};
```

Arrow functions don’t have their own `this` and `arguments`.

## Function invocation

A function, defined with the `function` keyword, can be invoked in different ways:

* Function form

```
doSomething(arguments)
```

* Method form

```
theObject.doSomething(arguments)
theObject["doSomething"](arguments)
```

* Constructor form

```
new Constructor(arguments)
```

* Apply form

```
 doSomething.apply(theObject, [arguments])
 doSomething.call(theObject, arguments)
```

Functions can be invoked with more or fewer arguments than declared in the definition. The extra arguments will be ignored, and the missing parameters will be set to `undefined`.

Functions (except arrow functions) have two pseudo-parameters: `this` and `arguments`.

## this

Methods are functions that are stored in objects. Functions are independent. In order for a function to know on which object to work on`this` is used. `this` represents the function’s context.

There is no point to use `this` when a function is invoked with the function form: `doSomething()`. In this case `this` is `undefined` or is the `window` object, depending if the strict mode is enabled or not.

When a function is invoked with the method form `theObject.doSomething()`,`this` represents the object.

When a function is used as a constructor `new Constructor()`, `this`represents the newly created object.

The value of `this` can be set with `apply()` or `call()`:`doSomething.apply(theObject)`. In this case `this` is the object sent as the first parameter to the method.

The value of `this` depends on how the function was invoked, not where the function was defined. This is of course a source of confusion.

## arguments

The `arguments` pseudo-parameter gives all the arguments used at invocation. It’s an array-like object, but not an array. It lacks the array methods.

```
function log(message){
  console.log(message);
}

function logAll(){
  let args = Array.prototype.slice.call(arguments);
  return args.forEach(log);
}

logAll("msg1", "msg2", "msg3");
```

An alternative is the new rest parameters syntax. This time `args` is an array object.

```
function logAll(...args){
  return args.forEach(log);
}
```

## return

A function with no `return` statement returns `undefined`. Pay attention to the automatic semi-colon insertion when using `return`. The following function will not return an empty object, but rather an `undefined` one.

```
function getObject(){ 
  return 
  {
  }
}
getObject()
```

To avoid the issue, use `{` on the same line as `return` :

```
function getObject(){ 
  return {
  }
}
```

## Dynamic Typing

JavaScript has dynamic typing. Values have types, variables do not. Types can change at run time.

```
function log(value){
  console.log(value);
}

log(1);
log("text");
log({message : "text"});
```

The `typeof()` operator can check the type of a variable.

```
let n = 1;
typeof(n);   //number

let s = "text";
typeof(s);   //string

let fn = function() {};
typeof(fn);  //function
```

## A Single Thread

The main JavaScript runtime is single threaded. Two functions can’t run at the same time. The runtime contains an Event Queue which stores a list of messages to be processed. There are no race conditions, no deadlocks.However, the code in the Event Queue needs to run fast. Otherwise the browser will become unresponsive and will ask to kill the task.

## Exceptions

JavaScript has an exception handling mechanism. It works like you may expect, by wrapping the code using the `try/catch` statement. The statement has a single `catch` block that handles all exceptions.

It’s good to know that JavaScript sometimes has a preference for silent errors. The next code will not throw an exception when I try to modify a frozen object:

```
let obj = Object.freeze({});
obj.message = "text";
```

Strict mode eliminates some JavaScript silent errors. `"use strict";` enables strict mode.

## Prototype Patterns

`Object.create()`, constructor function, and `class` build objects over the prototype system.

Consider the next example:

```
let servicePrototype = {
 doSomething : function() {}
}

let service = Object.create(servicePrototype);
console.log(service.__proto__ === servicePrototype); //true
```

`Object.create()` builds a new object `service` which has the`servicePrototype` object as its prototype. This means that `doSomething()` is available on the `service` object. It also means that the `__proto__` property of `service` points to the `servicePrototype` object.

Let’s now build a similar object using `class`.

```
class Service {
  doSomething(){}
}

let service = new Service();
console.log(service.__proto__ === Service.prototype);
```

All methods defined in the `Service` class will be added to the`Service.prototype` object. Instances of the `Service` class will have the same prototype (`Service.prototype`) object. All instances will delegate method calls to the `Service.prototype` object. Methods are defined once on`Service.prototype` and then inherited by all instances.

## Prototype chain

Objects inherit from other objects. Each object has a prototype and inherits their properties from it. The prototype is available through the “hidden” property `__proto__` .

When you request a property which the object does not contain, JavaScript will look down the prototype chain until it either finds the requested property, or until it reaches the end of the chain.

## Functional Patterns

JavaScript has first class functions and closures. These are concepts that open the way for Functional Programming in JavaScript. As a result, higher order functions are possible.

`filter()`, `map()`, `reduce()` are the basic toolbox for working with arrays in a function style.

`filter()` selects values from a list based on a predicate function that decides what values should be kept.

`map()` transforms a list of values to another list of values using a mapping function.

```
let numbers = [1,2,3,4,5,6];

function isEven(number){
  return number % 2 === 0;
}

function doubleNumber(x){
  return x*2;
}

let evenNumbers = numbers.filter(isEven);
//2 4 6
let doubleNumbers = numbers.map(doubleNumber);
//2 4 6 8 10 12
```

`reduce()` reduces a list of values to one value.

```
function addNumber(total, value){
  return total + value;
}

function sum(...args){
  return args.reduce(addNumber, 0);
}

sum(1,2,3); //6
```

Closure is an inner function that has access to the parent function’s variables, even after the parent function has executed. [Look at the next example](https://jsfiddle.net/cristi_salcescu/wxzy52mq/?source=post_page---------------------------):

```
function createCount(){
   let state = 0;
   return function count(){
      state += 1;
      return state;
   }
}

let count = createCount();
console.log(count()); //1
console.log(count()); //2
```

`count()` is a nested function. `count()` accesses the variable `state` from its parent. It survives the invocation of the parent function `createCount()`.`count()` is a closure.

A higher order function is a function that takes another function as an input, returns a function, or does both.

`filter()`, `map()`, `reduce()` are higher-order functions.

A pure function is a function that returns a value based only of its input. Pure functions don’t use variables from the outer functions. Pure functions cause no mutations.

In the previous examples `isEven()`, `doubleNumber()`, `addNumber()` and `sum()`are pure functions.

## Conclusion

The power of JavaScript lies in its simplicity.

Knowing the JavaScript fundamentals makes us better at understanding and using the language.

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** **[Functional React](https://www.amazon.com/dp/B088FZQ1XN).**

[Follow on Twitter](https://twitter.com/cristi_salcescu)


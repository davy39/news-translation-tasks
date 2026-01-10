---
title: An introduction to Functional JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-20T17:31:24.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-functional-javascript-e8dab63bb51d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DxjfBur9XKUWgSgceIv11Q.jpeg
tags:
- name: books
  slug: books
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cristian Salcescu

  Hey everybody! I’ve written a book called Discover Functional JavaScript, and it’s
  now ready in both paperback and Kindle formats.

  After publishing several articles on Functional Programming in JavaScript, at some
  point I realize...'
---

By Cristian Salcescu

Hey everybody! I’ve written a book called [Discover Functional JavaScript](https://www.amazon.com/dp/B07PBQJYYG), and it’s now ready in both paperback and Kindle formats.

After publishing several articles on Functional Programming in JavaScript, at some point I realized I have enough material to think about a book. So, I started from my previous writings, filled in the missing parts and created a book on Functional Programming in JavaScript.

What I tried to do in this book was to give practical examples of the core functional concepts. I think that if we master the fundamentals then it will be easier to handle more complex situations. And this is what this book is for.

I looked into a deeper understanding of pure functions other than that they are great. If they are so good, why don’t we write the whole application using only pure functions?

The other reason behind the book is to emphasize the new way of building encapsulated objects without classes and prototypes in JavaScript. I even saw classes presented as a way to bring encapsulation to objects. Encapsulation means hiding information. Objects built with classes in JavaScript are built over the prototype system. All their properties are public, they are not encapsulated.

I tried and hope I have succeeded to present the fundamental functional programming concepts in an easy to learn and practical manner. After reading the book you will understand better concepts like first-class functions, closures, currying, and partial application. You will understand what pure functions are and how to create them. You will better understand immutability and how it can be achieved in JavaScript.

Another thing not taken so much into account is naming. With the rise of arrow functions, more and more anonymous functions are created. The pretext behind all this is the fact that arrow functions have no `this` and have a shorter syntax. I don’t challenge that, I just challenge the fact that meaningful names are what we understand best. Removing that will make code harder to understand.

The book is pretty condensed, so you can even read it a few times. In regard to the core JavaScript concepts, it aims to make an overview of them, not to enter into great detail. There are a lot of resources for that.

For me, it was a great experience trying to organize my thoughts to express these ideas in a simple, practical way. I tried to focus on the main practical concepts and just eliminate everything that ads no value to the reader.

A deeper understanding of the fundamental concepts in JavaScript makes us better at resolving complex problems. I hope you will like it.

Here is what you can find inside:

#### Chapter 1: A brief overview of JavaScript

JavaScript has primitives, objects and functions. All of them are values. All are treated as objects, even primitives.

Number, boolean, string, `undefined` and `null` are primitives.

Variables can be defined using `var`, `let` and `const`. The `let` declaration has a block scope.

Primitives, except `null` and `undefined`, are treated like objects, in the sense that they have methods but they are not objects.

Arrays are indexed collections of values. Each value is an element. Elements are ordered and accessed by their index number.

JavaScript has dynamic typing. Values have types, variables do not. Types can change at run time.

The main JavaScript runtime is single threaded. Two functions can’t run at the same time.

#### Chapter 2: New features in ES6+

ES6 brings more features to the JavaScript language. Some new syntax allows you to write code in a more expressive way, some features complete the functional programming toolbox, and some features are questionable.

`let` declaration has block scope.

```
function doTask(){   
  let x = 1;   
  {       
    let x = 2;   
  }
   
  console.log(x); 
}  
doTask(); //1
```

`var` declaration has function scope. It doesn't have block scope.

```
function doTask(){   
  var x = 1;   
  {       
    var x = 2;   
  }
   
  console.log(x); 
}  
doTask(); //2
```

#### Chapter 3: First-class functions

Functions are first-class objects. Functions can be stored in variables, objects or arrays, passed as arguments to other functions or returned from functions.

A higher-order function is a function that takes another function as an input, returns a function, or does both.

`map()` transforms a list of values to another list of values using a mapping function.

```
let numbers = [1,2,3,4,5];

function doubleNo(x){
  const result = x*2;
  console.log(`${x} -> ${result}`)
  return result;
}

const doubleNumbers = numbers.map(doubleNo);
//1 -> 2
//2 -> 4
//3 -> 6
//4 -> 8
//5 -> 10
//[2, 4, 6, 8, 10]
```

#### Chapter 4: Closures

![Image](https://cdn-media-1.freecodecamp.org/images/JSAYSH9IZCpQfKGWJdklasvq1VmXf7aLpBB5)

A closure is an inner function that has access to the outer scope, even after the outer scope container has executed.

The `count()` function in the next example is a closure:

```
const count = (function(){
  let state = 0;
  return function(){
    state = state + 1;
    return state;
  }
})();

count(); //1
count(); //2
count(); //3
```

#### Chapter 5: Function decorators

> A function decorator is a higher-order function that takes one function as an argument and returns another function, and the returned function is a variation of the argument function — Reginald Braithwaite, author of [Javascript Allongé](https://leanpub.com/javascript-allonge/read#decorators)

The `unary()` decorator returns a new version of the function that accepts only one argument. It may be used to fix problems when the function is called with more arguments than we need.

```
function unary(fn){
 return function(first){
   return fn(first);
 }
}

const numbers = ['1','2','3','4','5','6'];
numbers.map(parseInt); 
//[1, NaN, NaN, NaN, NaN, NaN]

numbers.map(unary(parseInt)); 
//[1, 2, 3, 4, 5, 6]
```

#### Chapter 6: Pure functions

![Image](https://cdn-media-1.freecodecamp.org/images/6XNeBIiQldZ1bK7AK3-5GrQuUyEprm50TNq8)

A pure function is a function that, given the same input, always returns the same output and has no side effects.

You may have seen examples of pure functions like the ones below and want to look at some practical examples of pure functions.

```
function double(x){
  return x * 2;
}

function add(a, b){
  return a + b;
}

function multiply(a, b) {
  return a * b;
}
```

Like other programming paradigms, Pure Functional Programming promises to make code easier to read, understand, test, debug, and compose. Can it deliver its promise? If it can, can we build an application using only pure functions? These are questions this chapter tries to answer.

#### Chapter 7: Immutability

An immutable value is a value that, once created, cannot be changed.

Does immutability have to do with variables that cannot change or values that cannot change? And how can we make that happen? Why do we even care about that? This chapter tries to answers these questions.

![Image](https://cdn-media-1.freecodecamp.org/images/THSwkY8IPNQ0UjMPr5yzQG0vij3fEhdeaoIp)

#### Chapter 8: Partial application and currying

Partial application refers to the process of fixing a number of parameters by creating a new function with fewer parameters than the original.

Currying is the process of transforming a function with many parameters into a series of functions that each takes a single parameter.

Usually we find examples using currying to add or multiply a few numbers, like in the code below:

```
function add(a) {
  return function(b){
    return function(c){
      return a + b + c;
    }
  }
}

add(1)(2)(3);
//6
```

Does currying have a practical application? This chapter shows some practical examples of using partial application and currying.

#### Chapter 9: Function composition

Function composition is applying one function to the result of another.

```
function compose(...functions){
  return function(x){
    return functions.reduceRight((value, f) => f(value), x);
  }
}

f(g(x)) === compose(f,g)(x);
```

#### Chapter 10: Intention revealing names

Functions can be created with or without a name. The arrow syntax usually creates anonymous functions.

```
(() => {
    /*code*/
    (() => {
        /*code*/
    })();
})();
```

Anonymous functions appear as “(anonymous)” in the CallStack.

Intention revealing names improve code readability.

#### Chapter 11: Making code easier to read

This chapter shows examples of refactoring imperative code with functional programming techniques and looks at the readability of the final code.

#### Chapter 12: Asynchronous programming

In an application, there are two kinds of functions: synchronous and asynchronous. We take a look at the asynchronous programming model in JavaScript.

#### Chapter 13: Objects with prototypes

Objects are dynamic collections of properties, with a “hidden” property to the object’s prototype.

Objects inherit from other objects.

`class` is a sugar syntax from creating objects with a custom prototype.

```
class Counter {
  constructor(){
    this.state = 0;
  }
  
  increment(){
    this.state = this.state + 1;
    return this.state;
  }
  
  decrement(){
    this.state = this.state - 1;
    return this.state;
  }
}

const counter = new Counter();
counter.increment(); //1
counter.increment(); //2
counter.increment(); //3
counter.decrement(); //2
```

#### Chapter 14: Objects with closures

With closures we can create encapsulated and flexible objects. Consider the same counter object created with closures:

```
function Counter() {
  let state = 0;
  
  function increment(){
    state = state + 1;
    return state;
  }
  
  function decrement(){
    state = state - 1;
    return state;
  }
  
  return Object.freeze({
    increment, 
    decrement
  })
}

const counter = Counter();
counter.increment(); //1
counter.increment(); //2
counter.increment(); //3
counter.decrement(); //2
```

This chapter presents more encapsulated objects and discusses the difference between objects built with closures and prototypes.

#### Chapter 15: Method decorators

Method decorators are a tool for reusing common logic.

#### Chapter 16: Waiting for the new programming paradigm

The last chapter contains thoughts on Functional and Object Oriented Programming in JavaScript.

[**Enjoy the book**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_j0hTCbF0B1230)**!**

You can find me on [Twitter](https://twitter.com/cristi_salcescu).


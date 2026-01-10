---
title: 'JavaScript ES6 Functions: The Good Parts'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-20T17:54:26.000Z'
originalURL: https://freecodecamp.org/news/es6-functions-9f61c72b1e86
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nND_xhKn-rWHi8nBShTH-Q.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Bhuvan Malik

  ES6 offers some cool new functional features that make programming in JavaScript
  much more flexible. Let’s talk about some of them — specifically, default parameters,
  rest parameters, and arrow functions.

  Fun tip: you can copy and pas...'
---

By Bhuvan Malik

ES6 offers some cool new functional features that make programming in JavaScript much more flexible. Let’s talk about some of them — specifically, default parameters, rest parameters, and arrow functions.

**Fun tip**: you can copy and paste any of these examples/code into [Babel REPL](https://babeljs.io/repl/) and you can see how ES6 code transpiles to ES5.

![Image](https://cdn-media-1.freecodecamp.org/images/NIpmekw9kO1zjEdmWmnWAvnmoFQ8Eh96Jcgk)

### **Default Parameter Values**

JavaScript functions have a unique feature that allows for you to pass any number of parameters during function call (actual parameters) regardless of the number of parameters present in the function definition (formal parameters). So you need to include default parameters just in case someone forgets to pass one of the parameter.

#### **How default parameters would be implemented in ES5**

The above seems fine when we run it. `number2` wasn’t passed and we checked this using the ‘`||`’ operator to return the second operand if the first is falsy. Thus, ‘10’ was assigned as a default value since `number2` is undefined.

There’s just one problem though. What if someone passes ‘0’ as the second argument? ⚠

The above approach would fail because our default value ‘10’ would be assigned instead of the passed value, such as ‘0’. Why? Because ‘0’ is evaluated as falsy!

Let’s improve the above code, shall we?

Agh! That’s too much code. Not cool at all. Let’s see how ES6 does it.

#### **Default parameters in ES6**

```
function counts(number1 = 5, number2 = 10) {  // do anything here}
```

`number1` and `number2` are assigned default values of ‘5’ and ‘10’ respectively.  
Well yeah, this is pretty much it. Short and sweet. No extra code to check for a missing parameter. This makes the body of the function nice and short. ?

NOTE: When a value of `undefined` is passed for a parameter with default argument, as expected the value passed is **invalid** and the **default parameter value is assigned**. But if `null` is passed, it is considered **valid** and the **default parameter is not used** and null is assigned to that parameter.

A nice feature of default parameters is that the default parameter doesn’t necessarily have to be a primitive value, and we can also execute a function to retrieve the default parameter value. Here’s an example:

Previous parameters can also be default parameters for the parameters that come after them like so:

```
function multiply(first, second = first) {  // do something here}
```

But the inverse will throw an error. That is, if second parameter is assigned as the default value for the first parameter, it results in an error because the second parameter is not yet defined while being assigned to the first parameter.

```
function add(first = second, second) {  return first + second;}console.log(add(undefined, 1)); //throws an error
```

### Rest Parameters

> A _rest_ parameter is simply a named parameter which is preceded by three dots(…). This named parameter becomes an array which contains rest of the parameters(i.e apart from the named parameters) passed during function call.

Just keep in mind that there can only be one _rest_ parameter, and it has to be the last parameter. We can’t have a named parameter after a rest parameter.  
Here’s an example:

As you can see we’ve used the rest parameter to get all the keys/properties to be extracted from the passed object, which is the first parameter.

The difference between a rest parameter and the ‘arguments object’ is that the latter contains all the actual parameters passed during the function call, while the ‘rest parameter’ contains only the parameters that are not named parameters and are passed during the function call.

### Arrow Functions ➡

![Image](https://cdn-media-1.freecodecamp.org/images/9n5l6egKPj2FuvrmoTHpTfNcS0jRzOa-0Ap5)

Arrow Functions, or “fat arrow functions,” introduce a new syntax for defining functions that is very concise. We can avoid typing keywords like `function`, `return` and even curly brackets `{ }` and parentheses `()`.

#### Syntax

The syntax comes in different flavors, depending on our usage. All the variations have one thing in **common**, i.e they begin with the **arguments**, followed by **the** **arrow** (`=&`gt;), followed by t**he function b**ody.

The arguments and the body can take different forms. Here’s the most basic example:

```
let mirror = value => value;
```

```
// equivalent to:
```

```
let mirror = function(value) {  return value;};
```

The above example takes a single argument “value” (before the arrow) and simply returns that argument(`=> val`ue;). As you can see**, there’s just the return value, so no need for return keyword or curly bra**ces to wrap up the function body.

Since there is only **one argument**, there’s **no need for parentheses** “( )” as well.

Here’s an example with more than one argument to help you understand this:

```
let add = (no1, no2) => no1 + no2;
```

```
// equivalent to:
```

```
let add = function(no1, no2) {  return no1 + no2;};
```

If there are no arguments at all, you must include empty parentheses like below:

```
let getMessage = () => 'Hello World';
```

```
// equivalent to:
```

```
let getMessage = function() {  return 'Hello World';}
```

For a function body with just a return statement, curly braces are **optional**.  
For a function body having more than just a return statement, you need to wrap the body in curly braces just like traditional functions.

Here’s a simple calculate function with two operations — add and subtract. Its body must be wrapped in curly braces:

```
let calculate = (no1, no2, operation) => {    let result;    switch (operation) {        case 'add':            result = no1 + no2;            break;        case 'subtract':            result = no1 - no2;            break;    }    return result;};
```

Now what if we want a function that simply returns an object? The compiler will get confused whether the curly braces are of the object (`()=&**g**t;{id: num**b**`er} ) or curly braces of the function body.

The solution is to wrap the object in parentheses. Here’s how:

```
let getTempItem = number =&gt; ({ id: number});
```

```
// effectively equivalent to:
```

```
let getTempItem = function(number) {    return {        id: number    };};
```

Let’s have a look at the final example. In this we’ll use filter function on a sample array of numbers to return all numbers greater than 5,000:

```
// with arrow functionlet result = sampleArray.filter(element => element > 5000);
```

```
// without arrow functionlet result = sampleArray.filter(function(element) {  return element > 5000;});
```

We can see how much less code is necessary compared to the traditional functions.

A few things about arrow functions to keep in mind though:

* They can’t be called with _new_, can’t be used as constructors (and therefore lack prototype as well)
* Arrow functions have their own scope, but there’s no ‘_this’_ of their own.
* No _arguments_ object is available. You **can use** rest parameters however.

Since JavaScript treats functions as first-class, arrow functions make writing functional code like lambda expressions and currying much easier.

> “Arrow functions were like rocket fuel for the functional programming explosion in JavaScript.” — Eric Elliott

Well, there you go! Perhaps it’s time for you to start using these features.

ES6 features like these are a breath of fresh air, and developers just love using them.

![Image](https://cdn-media-1.freecodecamp.org/images/fRbQopusRfJej7QpnRe6umezaPKn-cWs6vgO)

Here’s the [link](https://medium.com/@bhuvanmalik/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d) to my previous post on variable declarations and hoisting!  
I hope this motivates you to take ES6 head on if you haven’t already!

Peace ✌️️


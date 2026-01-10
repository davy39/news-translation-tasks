---
title: Function Hoisting & Hoisting Interview Questions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-06T22:20:40.000Z'
originalURL: https://freecodecamp.org/news/function-hoisting-hoisting-interview-questions-b6f91dbc2be8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*v7kHrep8UBwgPvFz0gWutw.jpeg
tags:
- name: interview
  slug: interview
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

  This is a part 2 for my previous article on Hoisting titled “A guide to JavaScript
  variable hoisting ? with let and const”. So make sure you read that before diving
  into this one.

  Previously I talked about variable hoisting only becau...'
---

By Bhuvan Malik

This is a part 2 for my previous article on Hoisting titled “[A guide to JavaScript variable hoisting ? with let and const”](https://medium.freecodecamp.org/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d). So make sure you read that before diving into this one.

Previously I talked about variable hoisting only because function hoisting in JavaScript is not the same as variable hoisting, it is unique in its own way. I’ll expand on function hoisting in this one along with some common and tricky interview questions on hoisting (variable and function) which anyone giving JavaScript interviews is almost certain to encounter.

Hopefully, after finishing these 2 parts, you will be ready to cross off Hoisting from your JavaScript prep checklist!

Let’s get to it.

### Function Hoisting

There are 2 ways of creating functions in JavaScript, through **Function Declaration** and through **Function Expression**. Let’s see what these are and how hoisting affects them.

#### Function Declaration

The **function declaration** defines a function with the specified parameters.  
Syntax:

```
function name(param1, param2, ...) {  [statements]}
```

In JavaScript, function declarations hoist the function definitions.

Therefore, these functions can be **used** before they are declared.  
Example:

```
hoisted() // output: "Hoisted"
```

```
function hoisted() {  console.log('Hoisted')}
```

Behind the scenes, this is how the JavaScript interpreter looks at the above code:

```
// Hoisted codefunction hoisted() {  console.log('Hoisted')}
```

```
// Rest of the codehoisted() // output: "Hoisted"
```

This behavior is true if you have function declarations in the Global Scope or Functional Scope (basically Local Scope in JavaScript).

This can be helpful because you can use your higher-level logic at the beginning of the code making it more readable and understandable.

**Note:** Never use function declarations inside if/else blocks.

#### Function Expression

The `**function**` keyword can also be used to define a function inside an expression.  
Syntax:

```
const myFunction = function [name](param1, param2, ...) {  [statements]}
```

The `[name]` is optional, therefore these can be anonymous functions. We can use arrow functions as well like so:

```
const myFunction = (param1, param2, ...) => {  [statements]}
```

Function expressions in JavaScript are not hoisted.

Therefore, you cannot use function expressions before defining them.  
Example:

```
notHoisted() // TypeError: notHoisted is not a function
```

```
const notHoisted = function() {  console.log('foo')}
```

This is all there is to be kept in mind for creating functions from a hoisting point of view.   
Now on to some interview questions!

### Hoisting Interview Questions

Hoisting and it’s erratic behavior is a hot topic during interviews. Using the knowledge from my [previous article](https://medium.freecodecamp.org/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d) and this one, one can sail through any questions on the topic. With that said, let’s look at some common questions.

#### Question 1

```
var a = 1;
```

```
function b() {  a = 10;  return;
```

```
  function a() {}}
```

```
b();
```

```
console.log(a);
```

**Output: 1,** What the?! ?

This is because the `function a() {}` statement has now created a local `a` that has a functional/local scope. This new `a` now gets hoisted to the top of its enclosing function `b()` with it’s declaration and definition. This is what is happening behind the scenes:

```
var a = 1;
```

```
function b() {  // Hoisted  function a() {}
```

```
  a = 10;  return;}
```

```
b();
```

```
console.log(a)
```

Therefore, the statement `a = 10;` is no longer changing the value of the global `a` which remains to be 1, but rather it is changing the local `a` from a function to an integer value of 10. Since we are logging the global `a`, the output is 1.

Had the statement `function a() {}` not been there, the output would have been 10.

#### Question 2

```
function foo(){    function bar() {        return 3;    }    return bar();    function bar() {        return 8;    }}alert(foo());
```

**Output: 8**

Both the `bar()` functions are function declarations and will therefore be hoisted to the top of `foo()` local scope. However, the `bar()` returning 8 will be hoisted after the one returning 3. Therefore, the one returning 8 will be executed.

Behind the scenes:

```
function foo(){    //Hoisted before    function bar() {        return 3;    }    // Hoisted after    function bar() {        return 8;    }
```

```
    return bar();    }alert(foo());
```

#### Question 3

```
function parent() {    var hoisted = "I'm a variable";    function hoisted() {        return "I'm a function";    }    return hoisted(); }console.log(parent());
```

**Output: “TypeError: hoisted is not a function”**

This one’s tricky. Its Function vs. Variable! Let’s break it down.

We know that when it comes to variable hoisting, only the declaration(with a value of “undefined”) is hoisted, not the definition!

In the case of function declarations, the definitions are hoisted as well!

Now, in such a case of multiple declarations(variable and function in the same scope) with the same identifier, the hoisting of variables is simply **IGNORED**. The the interpreter comes across the function declaration and hoists it.   
Finally, the statement of variable assignment (which was not hoisted) is executed and “I’m a variable” is assigned to `hoisted`, which is a simple string value and not a function. Hence the error!

Here’s the behind the scenes for this problem:

```
function parent() {
```

```
    // Function declaration hoisted with the definition    function hoisted() {        return "I'm a function";    }
```

```
    // Declaration ignored, assignment of a string    hoisted = "I'm a variable"; 
```

```
    return hoisted(); 
```

```
}console.log(parent());
```

#### Question 4

```
alert(foo());function foo() {  var bar = function() {    return 3;  };  return bar();  var bar = function() {    return 8;  };}
```

**Output: 3**

This one’s easy. The function `foo()` itself will be hoisted in the global scope as its a function declaration. As for inside `foo()`, its a clear case of function expression for both the `bar()`functions.

The second `bar()` will not be read by the interpreter ahead of time (no hoisting). The first one will be executed and returned.

#### Question 5

```
var myVar = 'foo';
```

```
(function() {  console.log('Original value was: ' + myVar);  var myVar = 'bar';  console.log('New value is: ' + myVar);})();
```

**Output: “Original value was: undefined”, “New value is: bar”**

In this one, again the global value of `myVar` `(‘foo’)` is out of the picture. This is because variable `myVar` is being declared and defined inside the local function scope and is therefore hoisted to the top of the [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE) with a value of ‘undefined’ which is logged first. The value ‘bar’ is then assigned and logged subsequently.

This concludes JavaScript Hoisting from my side. ?

Hope [both](https://medium.freecodecamp.org/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d) the articles are of help to you.

Please check out the article below if you want to learn arrow functions and other ES6 functionality related to functions.

[**JavaScript ES6 Functions: The Good Parts**](https://medium.freecodecamp.org/es6-functions-9f61c72b1e86)  
[_ES6 offers some cool new functional features that make programming in JavaScript much more flexible. Let’s talk about…_medium.freecodecamp.org](https://medium.freecodecamp.org/es6-functions-9f61c72b1e86)

Peace ✌️


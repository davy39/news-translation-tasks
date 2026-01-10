---
title: An introduction to scope in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-01T18:01:35.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-scope-in-javascript-cbd957022652
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4YCJhT2ZeEMP7YxQbgVCyg.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cristian Salcescu

  Scope defines the lifetime and visibility of a variable. Variables are not visible
  outside the scope in which they are declared.

  JavaScript has module scope, function scope, block scope, lexical scope and global
  scope.

  Global Sco...'
---

By Cristian Salcescu

Scope defines the lifetime and visibility of a variable. Variables are not visible outside the scope in which they are declared.

JavaScript has module scope, function scope, block scope, lexical scope and global scope.

### Global Scope

Variables defined outside any function, block, or module scope have global scope. Variables in global scope can be accessed from everywhere in the application.

When a module system is enabled it’s harder to make global variables, but one can still do it. By defining a variable in HTML, outside any function, a global variable can be created:

```
<script>
  let GLOBAL_DATA = { value : 1};
</script>

console.log(GLOBAL_DATA);
```

When there is no module system in place, it is a lot easier to create global variables. A variable declared outside any function, in any file, is a global variable.

Global variables are available for the lifetime of the application.

Another way for creating a global variable is to use the `window` global object anywhere in the application:

```
window.GLOBAL_DATA = { value: 1 };
```

At this point, the `GLOBAL_DATA` variable is visible everywhere.

```
console.log(GLOBAL_DATA)
```

As you can imagine these practices are bad practices.

### Module scope

Before modules, a variable declared outside any function was a global variable. In modules, a variable declared outside any function is hidden and not available to other modules unless it is explicitly exported.

Exporting makes a function or object available to other modules. In the next example, I export a function from the `sequence.js` module file:

```
// in sequence.js
export { sequence, toList, take };
```

Importing makes a function or object, from other modules, available to the current module.

```
import { sequence, toList, toList } from "./sequence";
```

In a way, we can imagine a module as a self-executing function that takes the import data as inputs and returns the export data.

### Function Scope

Function scope means that parameters and variables defined in a function are visible everywhere within the function, but are not visible outside of the function.

Consider the next function that auto-executes, called IIFE.

```
(function autoexecute() {
    let x = 1;
})();

console.log(x);
//Uncaught ReferenceError: x is not defined
```

IIFE stands for Immediately Invoked Function Expression and is a function that runs immediately after its definition.

Variables declared with `var` have only function scope. Even more, variables declared with `var` are hoisted to the top of their scope. This way they can be accessed before being declared. Take a look at the code below:

```
function doSomething(){
  console.log(x);
  var x = 1;
}

doSomething(); //undefined
```

This does not happen for `let`. A variable declared with `let` can be accessed only after its definition.

```
function doSomething(){
  console.log(x);
  let x = 1;
}

doSomething();
//Uncaught ReferenceError: x is not defined
```

A variable declared with `var` can be re-declared multiple times in the same scope. The following code is just fine:

```
function doSomething(){
  var x = 1
  var x = 2;
  console.log(x);
}

doSomething();
```

Variables declared with `let` or `const` cannot be re-declared in the same scope:

```
function doSomething(){
  let x = 1
  let x = 2;
}
//Uncaught SyntaxError: Identifier 'x' has already been declared
```

Maybe we don’t even have to care about this, as `var` has started to become obsolete.

### Block Scope

Block scope is defined with curly braces. It is separated by `{` and `}`.

Variables declared with `let` and `const` can have block scope. They can only be accessed in the block in which they are defined.

Consider the next code that emphasizes `let` block scope:

```
let x = 1;
{ 
  let x = 2;
}
console.log(x); //1
```

In contrast, the `var` declaration has no block scope:

```
var x = 1;
{ 
  var x = 2;
}
console.log(x); //2
```

Another common problem with not having block scope is the use of an asynchronous operation like `setTimeout()` in a loop. The flowing loop code displays the number 5, five times.

```
(function run(){
    for(var i=0; i<5; i++){
        setTimeout(function logValue(){
            console.log(i);         //5
        }, 100);
    }
})();
```

The `for` loop statement, with the `let` declaration, creates a new variable locale to the block scope, for each iteration. The next loop code shows `0 1 2 3 4 5`.

```
(function run(){
  for(let i=0; i<5; i++){
    setTimeout(function log(){
      console.log(i); //0 1 2 3 4
    }, 100);
  }
})();
```

### Lexical Scope

Lexical scope is the ability of the inner function to access the outer scope in which it is defined.

[Consider the next code](https://jsfiddle.net/cristi_salcescu/pcg6fab7/):

```
(function autorun(){
    let x = 1;
    function log(){
      console.log(x);
    };
    
    function run(fn){
      let x = 100;
      fn();
    }
    
    run(log);//1
})();
```

The `log` function is a closure. It refers the `x` variable from its parent function `autorun()`, not the one from the `run()` function.

The closure function has access to the scope in which it was created, not the scope in which it was executed.

The local function scope of `autorun()` is the lexical scope of the `log()` function.

### Scope chain

Every scope has a link to the parent scope. When a variable is used, JavaScript looks down the scope chain until it either finds the requested variable or until it reaches the global scope, which is the end of the scope chain.

[Look at the next example](https://jsfiddle.net/cristi_salcescu/udq46asp/):

```
let x0 = 0;
(function autorun1(){
 let x1 = 1;
  
 (function autorun2(){
   let x2 = 2;
  
   (function autorun3(){
     let x3 = 3;
      
     console.log(x0 + " " + x1 + " " + x2 + " " + x3);//0 1 2 3
    })();
  })();
})();
```

The `autorun3()` inner function has access to the local `x3` variable. It has also access to the `x1` and `x2` variables from the outer functions and the `x0` global variable.

If it cannot find the variable, it will return an error in strict mode.

```
"use strict";
x = 1;
console.log(x)
//Uncaught ReferenceError: x is not defined
```

In non-strict mode, referred to as “sloppy mode”, it will do a bad thing and create a global variable.

```
x = 1;
console.log(x); //1
```

### Conclusion

Variables defined in global scope are available everywhere in the application.

In a module, a variable declared outside any function is hidden and not available to other modules unless it is explicitly exported.

Function scope means that parameters and variables defined in a function are visible everywhere within the function

Variables declared with `let` and `const` have block scope. `var` doesn’t have block scope.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)


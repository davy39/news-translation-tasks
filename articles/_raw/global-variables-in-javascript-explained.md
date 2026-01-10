---
title: Global Variables in JavaScript Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T22:41:00.000Z'
originalURL: https://freecodecamp.org/news/global-variables-in-javascript-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d77740569d1a4ca37e7.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: Global variables are declared outside of a function for accessibility throughout
  the program, while local variables are stored within a function using var for use
  only within that function’s scope. If you declare a variable without using var,
  even if...
---

Global variables are declared outside of a function for accessibility throughout the program, while local variables are stored within a function using `var` for use only within that function’s [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope). If you declare a variable without using `var`, even if it’s inside a function, it will still be seen as global:

```javascript
var x = 5; // global

function someThing(y) {
  var z = x + y;
  console.log(z);
}

function someThing(y) {
  x = 5; // still global!
  var z = x + y;
  console.log(z);
}


function someThing(y) {
  var x = 5; // local
  var z = x + y;
  console.log(z);
}
```

A global variable is also an object of the current scope, such as the browser window:

```javascript
var dog = “Fluffy”;
console.log(dog); // Fluffy;

var dog = “Fluffy”;
console.log(window.dog); // Fluffy
```

It’s a best practice to minimize global variables. Since the variable can be accessed anywhere in the program, they can cause strange behavior.

References:

* [var -Javascript|MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
* [You Don’t Know JavaScript: Scopes & Closures](https://github.com/getify/You-Dont-Know-JS/tree/master/scope%20%26%20closures)

## **[What’s the difference between a global var and a window.variable in javascript?](https://stackoverflow.com/questions/6349232/whats-the-difference-between-a-global-var-and-a-window-variable-in-javascript)**

The scope of JavaScript variables are either global or local. Global variables are declared OUTSIDE the function and its value is accessible/changeable throughout the program.

You should ALWAYS use **var** to declare your variables (to make locally) else it will install GLOBALLY

Take care with the global variables because they are risky. Most of the time you should use closures to declare your variables. Example:

```javascript
(function(){
  var myVar = true;
})();
```

## **More Information:**

* [Visual guide to JavaScript variable definitions and scope](https://www.freecodecamp.org/news/the-visual-guide-to-javascript-variable-definitions-scope-2717ad9f0169/)
* [Intro to JavaScript variable definitions and hoisting](https://www.freecodecamp.org/news/a-basic-introduction-to-javascript-variable-definitions-and-hoisting-93aa38e742eb/)


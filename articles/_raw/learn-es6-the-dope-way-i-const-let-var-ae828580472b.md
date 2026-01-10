---
title: 'Learn ES6 The Dope Way Part I: const, let & var'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-01T05:40:02.000Z'
originalURL: https://freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RuxaPPPrL6K09eF4pFhISw.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mariya Diminsky

  Welcome to Part I of Learn ES6 The Dope Way, a series created to help you easily
  understand ES6 (ECMAScript 6)!

  First up, what’s the deal with const, let, and var?

  You’ve probably been a witness to one of these situations — let and...'
---

By Mariya Diminsky

Welcome to Part I of **Learn ES6 The Dope Way,** a series created to help you easily understand ES6 (ECMAScript 6)!

First up, what’s the deal with _const_, _let_, and _var_?

You’ve probably been a witness to one of these situations — _let_ and/or _const_ being substituted for _var_, or _let_ and _const_ being used in the same code at the same time, or even more perplexing, _let_, _const_ AND _var_ all being used at the once!?

Hey no worries, I got you. Let’s clear this fog together:

#### const

Benefits:

* Useful if you’re setting a variable that you don’t plan on changing.
* Protects and prevents your variables from reassignment.
* In compiled languages, there is an increase in runtime efficiency of your code and thus an overall performance boost vs using plain ‘ol _var_.

Beware:

* Works as it should in Chrome and Firefox. But not in Safari. Instead it acts as a normal variable, as if it were _var,_ and thus can be reassigned.
* Generally there is programming convention to set the name in all caps to show others reading your code that the value of the _const_ value should not be changed — you will witness both lowercase and caps _const_ coding situations. Just something to be aware of.

Examples:

```js
// sometimes used as lowercase as when setting up your server.
const express = require(‘express’);
const app = express();

// sometimes uppercase.
const DONT_CHANGE_ME_MAN = “I ain’t changing for no one, man.”

// change attempt #1 
const DONT_CHANGE_ME_MAN = “I told I ain’t changing for no one.”
// change attempt #2
var DONT_CHANGE_ME_MAN = “Still not changing, bro.”
// change attempt #3
DONT_CHANGE_ME_MAN = “Haha, nice try, still not happening.”

// same error for all 3 attempts, const value stays the same:
Uncaught TypeError: Identifier ‘const DONT_CHANGE_ME_MAN’ has already been declared.

// DONT_CHANGE_ME_MAN still results in “I ain’t changing for no one, man.”
```

Does that make sense?

> Think of const, like the constant sea — _never-ending, never-changing…_  
>   
> …except in Safari.

#### let

Students and experienced programmers coming from a Ruby or Python background will love _let,_ as it enforces block scoping!

As you migrate over to ES6 country, you may notice yourself adjusting to a new _let_ metamorphosis taking over your coding style, and find yourself less likely to using _var_ anymore. With _let_ it’s so much more clear now where your values are coming from without worrying about them being hoisted!

Benefits:

* Block-Scoping, your variable’s values are exactly as they should be in that current scope and they are not hoisted as with _var_.
* Super useful if you don’t want your values to be overwritten, like in a for loop.

Beware:

* You may not always want to use _let_. For example in situations where variables aren’t as easily block scoped, _var_ may be more convenient.

Examples:

```js
// When using var what do we get?
var bunny = "eat carrot";

if(bunny) {
  var bunny = "eat twig";
  console.log(bunny) //  "eat twig"
}

console.log(bunny)// "eat twig"

// When using let what do we get?
let bunny = "eat carrot";

if(bunny) {
  let bunny = "eat twig";
  console.log(bunny) // "eat twig"
}

console.log(bunny)// "eat carrot"
```

Do you see the difference? It’s all about scope. With _var_, it has access to it’s parent/outer scope and thus can change the value inside the if statement. Unlike _let_ which is block-scoped and can only be altered within the current scope it’s in.

_let_ is super straight-forward. It’s like a person who speaks straight to your face and tells you exactly what they need right then and there while _var_ does this as well but may occasionally reply with unexpected answers — due to hoisting and access to outer scope variables. Depending on the situation either one may be in your favor.

Another great example on the benefits of _let_:

Say you want to create a game board of 30 divs and each one has their own value. If you were to do this with _var_, the _i_ index would be overwritten for every iteration — every single div would have the value of 30! Yikes!

On the other hand, with _let_, every div has its own value, as its own div scope is maintained for each iteration! See the difference:

```js
// with var. See example live: https://jsfiddle.net/maasha/gsewf5av/
for(var i= 0; i<30; i++){
  var div = document.createElement('div');
  div.onclick = function() {
    alert("you clicked on a box " + i);
   };
   document.getElementsByTagName('section')[0].appendChild(div);
}

// with let. See example live: https://jsfiddle.net/maasha/xwrq8d5j/
for(let i=0; i<30; i++) {
  var div=document.createElement(‘div’);
  div.onclick = function() {
    alert("you clicked on a box " + i);
   };
   document.getElementsByTagName('section')[0].appendChild(div);
}
```

Congrats! You’ve made it through **Learn ES6 The Dope Way** Part I and now you know the main differences between const, let and var! Woohoo! You rockstar, you :)

Keep your knowledge updated by liking and following as more **Learn ES6 The Dope Way** is coming soon to Medium!

**[Part I: const, let & var](https://www.freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b/)**

**[Part II: (Arrow) => functions and ‘this’ keyword](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)**

**[Part III: Template Literals, Spread Operators & Generators!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294/)**

**[Part IV: Default Parameters, Destructuring Assignment, and a new ES6 method!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9/)**

**[Part V: Classes, Transpiling ES6 Code & More Resources!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661/)**

You can also find me on github ❤ [https://github.com/Mashadim](https://github.com/Mashadim)


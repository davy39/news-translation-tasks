---
title: 'Learn ES6 The Dope Way Part II: Arrow functions and the ‘this’ keyword'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-16T10:40:45.000Z'
originalURL: https://freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qb02fqNhhC5mRIdzLA83Hg.png
tags:
- name: education
  slug: education
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mariya Diminsky

  Welcome to Part II of Learn ES6 The Dope Way, a series created to help you easily
  understand ES6 (ECMAScript 6)!

  So, what the heck is =>; ?

  You’ve probably seen these strange Egyptian-looking hieroglyphics symbols here and
  there, e...'
---

By Mariya Diminsky

Welcome to Part II of **Learn ES6 The Dope Way,** a series created to help you easily understand ES6 (ECMAScript 6)!

#### **So, what the heck is =>**; ?

You’ve probably seen these strange Egyptian-looking hieroglyphics symbols here and there, especially in someone else’s code, where you’re currently debugging a ‘_this’_ keyword issue. After an hour of tinkering, you’re now roaming the Google search bar and stalking Stack Overflow. Sound familiar?

Together, let’s cover three topics in **Learn ES6 The Dope Way** Part II:

* How the ‘_this_’ keyword relates to **=>**.
* How to migrate functions from ES5 to ES6.
* Important quirks to be aware of when using **=>**.

#### Arrow Functions

Arrow functions were created to simplify function scope and make using the ‘_this_’ keyword much more straightforward. They utilize the **=&**gt; syntax, which looks like an arrow. Even though I don’t think it needs to go on a diet, people call i_t “the fat arr_ow” (and Ruby enthusiasts may know it better as th_e “hash rock_et” ) — something to be aware of.

#### How the ‘this’ keyword relates to Arrow Functions

Before we dive deeper into ES6 arrow functions, it’s important to first have a clear picture of what ‘_this_’ binds to in ES5 code.

If the ‘_this_’ keyword were inside an object’s **method** (a function that belongs to an object), what would it refer to?

```js
// Test it here: https://jsfiddle.net/maasha/x7wz1686/
var bunny = {
  name: 'Usagi',
  showName: function() {
    alert(this.name);
  }
};

bunny.showName(); // Usagi
```

Correct! It would refer to the object. We’ll get to why later on.

Now what about if the ‘_this_’ keyword were inside of method’s function?

```js
// Test it here: https://jsfiddle.net/maasha/z65c1znn/
var bunny = {
  name: 'Usagi',
  tasks: ['transform', 'eat cake', 'blow kisses'],
  showTasks: function() {
    this.tasks.forEach(function(task) {
      alert(this.name + " wants to " + task);
    });
  }
};

bunny.showTasks();
// [object Window] wants to transform
// [object Window] wants to eat cake
// [object Window] wants to blow kisses

// please note, in jsfiddle the [object Window] is named 'result' within inner functions of methods.

```

What did you get? Wait, what happened to our bunny…?

Ah, did you think ‘_this_’ refers to the method’s inner function?

Perhaps the object itself?

You are wise to think so, yet it is not so. Allow me to teach you what the coding elders had once taught me:

Coding Elder**:** “_Ah yes,_ t_he code is strong with this one._ _It is indeed practical to think that the ‘this’ keyword binds to the function but the truth is, ‘this’ has now fallen out of scope…It now belongs to…”,_ he pauses as if experiencing inner turmoil_, “the window object._”

That’s right. That’s exactly how it happened.

Why does ‘_this_’ bind to the window object? **Because ‘_this_’, always references the owner of the function it is in, for this case — since it is now out of scope — the window/global object.**

When it is inside of an object’s method — the function’s owner is the object. Thus the ‘_this_’ keyword is bound to the object. Yet when it is inside of a function, either stand alone or within another method, it will always refer to the window/global object.

```js
// Test it here: https://jsfiddle.net/maasha/g278gjtn/
var standAloneFunc = function(){
  alert(this);
}

standAloneFunc(); // [object Window]
```

But why…?

This is known as a JavaScript quirk, meaning something that just happens within JavaScript that isn’t exactly straightforward and it doesn’t work the way you would think. This was also regarded by developers as a poor design choice, which they are now remedying with ES6's arrow functions.

Before we continue, it’s important to be aware of two clever ways programmers solve the ‘_this_’ problem within ES5 code, especially since you will continue to run into ES5 for awhile (not every browser has fully migrated to ES6 yet):

**#1** Create a variable outside of the method’s inner function. Now the ‘forEach’ method gains access to ‘_this_’ and thus the object’s properties and their values. This is because ‘_this_’ is being stored in a variable while it is still within the scope of the object’s direct method ‘showTasks’.

```js
// Test it here: https://jsfiddle.net/maasha/3mu5r6vg/
var bunny = {
  name: 'Usagi',
  tasks: ['transform', 'eat cake', 'blow kisses'],
  showTasks: function() {
    var _this = this;
    this.tasks.forEach(function(task) {
      alert(_this.name + " wants to " + task); 
    });
  }
};

bunny.showTasks();
// Usagi wants to transform
// Usagi wants to eat cake
// Usagi wants to blow kisses
```

**#2** Use bind to attach the ‘_this_’ keyword that refers to the method to the method’s inner function.

```js
// Test it here: https://jsfiddle.net/maasha/u8ybgwd5/
var bunny = {
  name: 'Usagi',
  tasks: ['transform', 'eat cake', 'blow kisses'],
  showTasks: function() {
    this.tasks.forEach(function(task) {
      alert(this.name + " wants to " + task);
    }.bind(this));
  }
};

bunny.showTasks();
// Usagi wants to transform
// Usagi wants to eat cake
// Usagi wants to blow kisses
```

And now introducing…Arrow functions! Dealing with ‘_this_’ issue has never been easier and more straightforward! The simple ES6 solution:

```js
// Test it here: https://jsfiddle.net/maasha/che8m4c1/

var bunny = {
  name: 'Usagi',
  tasks: ['transform', 'eat cake', 'blow kisses'],
  showTasks() {
    this.tasks.forEach((task) => {
      alert(this.name + " wants to " + task);
    });  
  }
};

bunny.showTasks();
// Usagi wants to transform
// Usagi wants to eat cake
// Usagi wants to blow kisses
```

While in ES5 ‘_this_’ referred to the parent of the function, in ES6, arrow functions use lexical scoping — ‘_this_’ refers to it’s current surrounding scope and no further. Thus the inner function knew to bind to the inner function only, and not to the object’s method or the object itself.

#### How to migrate functions from ES5 to ES6.

```js
// Before
let bunny = function(name) {
  console.log("Usagi");
}

// After
let bunny = (name) => console.log("Usagi")

// Step 1: Remove the word ‘function’.
let bunny = (name) {
  console.log("Usagi");
}

// Step 2: If your code is less than a line, remove brackets and place on one line.
let bunny = (name) console.log("Usagi");

// Step 3. Add the hash rocket.
let bunny = (name) => console.log("Usagi");
```

You did it! Great job! Simple enough right? Here are a few more examples utilizing the fat — er skinny arrow, to get your eyes accustomed:

```js
// #1 ES6: if passing one argument you don't need to include parenthesis around parameter.
var kitty = name => name;

// same as ES5:
var kitty = function(name) {
  return name;
};

// #2 ES6: no parameters example.
var add = () => 3 + 2;

// same as ES5:
var add = function() {
  return 3 + 2;
};

// #3 ES6: if function consists of more than one line or is an object, include braces.
var objLiteral = age => ({ name: "Usagi", age: age });

// same as ES5:
var objLiteral = function(age) {
  return {
    name: "Usagi",
    age: age
  };
};

// #4 ES6: promises and callbacks.
asyncfn1().then(() => asyncfn2()).then(() => asyncfn3()).then(() => done());

// same as ES5:
asyncfn1().then(function() {
  asyncfn2();
}).then(function() {
  asyncfn3();
}).done(function() {
  done();
});
```

#### Important quirks to be aware of when using Arrow functions

If you use the ‘new’ keyword with => functions it will throw an error. Arrow functions can’t be used as a constructor — normal functions support the ‘new’ via the property prototype and internal method [[Construct]]. Arrow functions don’t use neither, thus the new (() => {}) throws an error.

Further quirks to consider:

```js
// Line breaks are not allowed and will throw a syntax error
let func1 = (x, y)
=> {
  return x + y;
}; // SyntaxError

// But line breaks inside of a parameter definition is ok
let func6 = (
  x,
  y
) => {
	return x + y;
}; // Works!

// If an expression is the body of an arrow function, you don’t need braces:
asyncFunc.then(x => console.log(x));

// However, statements have to be put in braces:
asyncFunc.catch(x => { throw x });

// Arrow functions are always anonymous which means you can’t just declare them as in ES5:
function squirrelLife() {
  // play with squirrels, burrow for food, etc.
}

// Must be inside of a variable or object property to work properly:
let squirrelLife = () => {
  // play with squirrels, burrow for food, etc.
  // another super squirrel action.
}
```

Congrats! You’ve made it through **Learn ES6 The Dope Way** Part II and now you have a basis for arrow function knowledge, the lexical benefits it gives to ‘_this_’ and also snagged yourself some JavaScript quirk skills! :)

Keep your wisdom updated by liking and following as more **Learn ES6 The Dope Way** is coming soon to Medium!

**[Part I: const, let & var](https://www.freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b/)**

**[Part II: (Arrow) => functions and ‘this’ keyword](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)**

**[Part III: Template Literals, Spread Operators & Generators!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294/)**

**[Part IV: Default Parameters, Destructuring Assignment, and a new ES6 method!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9/)**

**[Part V: Classes, Transpiling ES6 Code & More Resources!](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661/)**

You can also find me on github ❤ [https://github.com/Mashadim](https://github.com/Mashadim)


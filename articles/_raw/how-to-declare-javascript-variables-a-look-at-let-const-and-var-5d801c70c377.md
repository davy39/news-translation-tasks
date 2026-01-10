---
title: 'How to declare JavaScript variables: a look at let, const, and var'
subtitle: ''
author: Shirshendu Bhowmick
co_authors: []
series: null
date: '2019-03-11T14:49:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-declare-javascript-variables-a-look-at-let-const-and-var-5d801c70c377
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f5NxsWhcLjKe4GYjw74adg.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: With the old JavaScript, we had only one way to declare a variable, and
  that was with var, like var x = 10. It will create a variable called x and assign
  a value 10 to it. Now with modern ES6 JavaScript, we have 3 different ways to declare
  a variable...
---

With the old JavaScript, we had only one way to declare a variable, and that was with `var`, like `var x = 10`. It will create a variable called x and assign a value 10 to it. Now with modern ES6 JavaScript, we have 3 different ways to declare a variable: `let`, `const` and `var`. We will talk about `let` & `const` later. For now, let's focus on `var`.

## var

We already know how to declare a variable with `var`. Let us now refer to some code to understand `var` properly.

```js
var x = 20;
function foo() {
    var y = 10;
    console.log(x);
    console.log(y);
}
foo(); // will print 20 and 10
console.log(x); // will print 20
console.log(y); // will throw a reference error
```

Those who are familiar with C or C++ might understand why the output is like so. This is because `x` is in global scope and `y` is in the function foo’s scope. As function `foo` has access to the global scope, from the inside of the function we can access both `x` and `y`. Printing `x` also goes fine because as `x` is in global scope, we can access it from everywhere. Things go wrong when we try to access `y` from the global scope because `y` is limited to the function scope only.

Similar to C or C++ right? No. Let’s see why not.

```js
var x = 20;
function foo() {
    var y = 10;
    {
        var z = 30;
    }
    console.log(x);
    console.log(y);
    console.log(z);
}
foo();
```

What do you think the output of the code will be? If you think that there will be a reference error at the line `console.log(z)`, then you are correct from a C or C++ point of view. But with JavaScript, that’s not the case. The above code will print 20 10 30.

This is because in JavaScript with `var`, unlike in C and C++, we don’t have any block level scope. We have only global and function level scope. So `z` falls under function foo’s scope.

Now we have one more example:

```js
var x = 20;
var x = 30;
console.log(x); // this will print 30
```

In C or C++ if we declare a variable more than once in the same scope we get an error. But that’s not the case with `var` in JavaScript. In the above example, it just redefines `x` and assigns a value of 30.

Let’s consider the below code snippets:

```js
function foo() {
    x = 20;
    console.log(x);
}
foo();
console.log(x);
```

The above code will print 20 20. So what happens here? If you declare a variable anywhere without the `var` keyword it becomes a part of the global scope. It is accessible from both inside and outside of `foo`.

```js
'use strict'
function foo() {
    x = 20;
    console.log(x);
}
foo();
console.log(x);
```

In the above code, we are using strict mode. In strict mode, an `x = 20` kind of declaration is not allowed. It will throw a reference error. You have to declare a variable using `var`, `let` or `const`.

## let

Now it’s time to have a look at `let`. `let` is the new var in ES6 but with some differences.

```js
let x = 20;
function foo() {
    let y = 10;
    {
        let z = 30;
    }
    console.log(x);
    console.log(y);
    console.log(z);
}
foo();
```

Remember that in JavaScript, `var` doesn’t have any block-level scope? Now block level scopes are back with `let`. If you execute the above code you will get a reference error at the line `console.log(z)`. The variable `z` declared with `let` is now in a different block-level scope and is not accessible outside of this scope.

```js
let x = 10;
let x = 20; // will throw an error
```

Re-declaration of variables with `let` is not allowed.

```js
var x = 10;
let y = 20;
console.log(window.x); // 10
console.log(window.y); // undefined
```

Global variables declared globally with `var` are added to the `global` object, the `window` in case of browsers. Variables declared globally with let are not added to `window` (global object). Though they are accessible globally, it's like it’s there but you can’t see it.

```js
console.log(x); //undefined
console.log(y); //reference error
var x;
let y;
```

Unlike `var`, `let` variables are not initialized with undefined before their definitions are evaluated. If you try to access the variable before that you will encounter a reference error. This is also known as the temporal dead zone. In simple words, hoisting is only available with `var`, not with `let` & `const`.

## const

`const` stands for constant, it is very similar to `let`. The only differences are its value cannot be changed and it needs to be initialized where you are declaring it.

```js
const x = 20;
console.log(x); // will print 20
x = 30 // will throw an error
```

It’s not that in the case of `const` objects you can change the property of that object — it’s just that you can’t reassign a `const` variable.

```js
const obj = {firstName: "James", lastName: "Bond"}
console.log(obj); // will print the obj object
obj.firstName = "Ruskin";
console.log(obj); // will print the obj object, it has new firstName
obj = {firstName: "James", lastName: "Bond"}; // will throw an error
```

Also as mentioned earlier you have to initialize a `const` variable, you can’t keep it uninitialized.

```js
const x; // will throw an error
some other code;
```

That’s all for this article — see you later!

## Thank you for reading :)

## 


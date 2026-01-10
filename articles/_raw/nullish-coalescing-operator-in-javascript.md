---
title: How the Nullish Coalescing Operator Works in JavaScript
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2020-12-22T17:41:22.000Z'
originalURL: https://freecodecamp.org/news/nullish-coalescing-operator-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/nullish-2.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: "ES11 has added a nullish coalescing operator which is denoted by double\
  \ question marks, like this: ??. \nIn this article, we will explore why it's so\
  \ useful and how to use it.\nLet's get started.\nBackground Information\nIn JavaScript,\
  \ there is a short-c..."
---

ES11 has added a nullish coalescing operator which is denoted by double question marks, like this: `??`. 

In this article, we will explore why it's so useful and how to use it.

Let's get started.

## Background Information

In JavaScript, there is a short-circuit logical OR operator `||`.

> The || operator returns the first `truthy` value.

The following are the `only six` values that are considered to be `falsy` values in JavaScript.

* false
* undefined
* null
* ""(empty string)
* NaN
* 0

So if anything is not in the above list, then it will be considered a `truthy` value.

`Truthy` and `Falsy` values are the non-boolean values that are coerced to `true`   
or `false` when performing certain operations.

```js
const value1 = 1;
const value2 = 23;

const result = value1 || value2; 

console.log(result); // 1
```

As the || operator returns the first `truthy` value, in the above code, the `result` will be the value stored in `value1` which is `1`.

If `value1` is `null`, `undefined`, `empty` or any other `falsy` value, then the next operand after the || operator will be evaluated and that will the result of the total expression.

```js
const value1 = 0;
const value2 = 23;
const value3 = "Hello";

const result = value1 || value2 || value3; 

console.log(result); // 23
```

Here, because `value1` is 0, `value2` will be checked. As it's a truthy value, the result of the entire expression will be the `value2`.

> The issue with the || operator is that it doesn’t distinguish between `false` , `0` , an empty string `""`, `NaN` , `null` and `undefined` . They all are considered as `falsy` values. 

If any of these is the first operand of || , then we’ll get the second operand as the result.

## Why JavaScript Needed the Nullish Coalescing Operator

The || operator works great but sometimes we only want the next expression to be evaluated when the first operand is only either `null` or `undefined`.

Therefore, ES11 has added the nullish coalescing operator.

In the expression `x ?? y`,

* If x is either `null` or `undefined` **then only** result will be `y`.
* If x is **not** `null` or `undefined` then the result will be `x`.

This will make the conditional checks and debugging code an easy task.

## Try it yourself

```js
let result = undefined ?? "Hello";
console.log(result); // Hello

result = null ?? true; 
console.log(result); // true

result = false ?? true;
console.log(result); // false

result = 45 ?? true; 
console.log(result); // 45

result = "" ?? true; 
console.log(result); // ""

result = NaN ?? true; 
console.log(result); // NaN

result = 4 > 5 ?? true; 
console.log(result); // false because 4 > 5 evaluates to false

result = 4 < 5 ?? true;
console.log(result); // true because 4 < 5 evaluates to true

result = [1, 2, 3] ?? true;
console.log(result); // [1, 2, 3]

```

So from all of the above examples, it’s clear that the result of the operation `x ?? y` is `y` only when `x` is either `undefined` or `null`. 

In all the other cases, the result of the operation will always be `x`.

## Conclusion

As you have seen, the nullish coalescing operator is really useful when you only care about the `null` or `undefined` value for any variable.

Starting with ES6, there are many useful additions to JavaScript like 

* ES6 Destructuring
* Import and Export Syntax
* Arrow functions
* Promises
* Async/await 
* Optional chaining operator

and a lot more.

You can learn everything about all the ES6+ features in detail in the [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/) book.

You can [get the Mastering Modern JavaScript book at 40% discount](https://modernjavascript.yogeshchavan.dev/).

**Subscribe to my [weekly newsletter](https://yogeshchavan.dev/) to join 1000+ other subscribers to get amazing tips, tricks, articles and discount deals directly in your inbox.**


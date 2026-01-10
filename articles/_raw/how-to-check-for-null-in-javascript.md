---
title: JS Check for Null – Null Checking in JavaScript Explained
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-29T20:16:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-for-null-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover-template--22-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Null is a primitive type in JavaScript. This means you are supposed to
  be able to check if a variable is null with the typeof() method. But unfortunately,
  this returns “object” because of an historical bug that cannot be fixed.

  let userName = null;


  ...'
---

Null is a primitive type in JavaScript. This means you are supposed to be able to check if a variable is `null` with the `typeof()` method. But unfortunately, this returns “object” because of an [historical bug](https://www.turbinelabs.com/blog/the-odd-history-of-javascripts-null) that cannot be fixed.

```js
let userName = null;

console.log(typeof(userName)); // object
```

So how can you now check for null? This article will teach you how to check for null, along with the difference between the JavaScript type null and undefined.

## Null vs Undefined in JavaScript

Null and undefined are very similar in JavaScript and are both primitive types.

A variable has the type of `null` if it intentionally contains the value of `null`. In contrast, a variable has the type of `undefined` when you declare it without initiating a value.

```js
// This is null
let firstName = null;

// This is undefined
let lastName;
```

Undefined works well because when you check the type using the `typeof()` method, it will return `undefined`:

```js
let lastName;

console.log(typeof(lastName)); // undefined
```

Let’s now see the two major ways you can check for `null` and how it relates to `undefined`.

## How to Check for Null in JavaScript with Equality Operators

The equality operators provide the best way to check for `null`. You can either use the loose/double equality operator (`==`) or the strict/triple equality operator (`===`).

### How to use the loose equality operator to check for null

You can use the loose equality operator to check for `null` values:

```js
let firstName = null;

console.log(firstName == null); // true
```

But, this can be tricky because if the variable is undefined, it will also return `true` because both `null` and `undefined` are loosely equal.

```js
let firstName = null;
let lastName;

console.log(firstName == null); // true
console.log(lastName == null); // true
console.log(firstName == undefined); // true
console.log(lastName == undefined); // true
console.log(firstName == lastName); // true
console.log(null == undefined); // true
```

**Note:** This can be useful when you want to check if a variable has no value because when a variable has no value, it can either be `null` or `undefined`.

But suppose you only want to check for `null` – then you can use the strict equality operator.

### How to use the strict equality operator to check for null

The strict equality operator, compared to the loose equality operator, will only return `true` when you have exactly a `null` value. Otherwise, it will return `false` (this includes `undefined`).

```js
let firstName = null;
let lastName;

console.log(firstName === null); // true
console.log(lastName === null); // false
console.log(firstName === undefined); // false
console.log(lastName === undefined); // true
console.log(firstName === lastName); // false
console.log(null === undefined); // false
```

As you can see, it only returns `true` when a null variable is compared with `null`, and an undefined variable is compared with `undefined`.

## How to Check for Null in JavaScript with the `Object.is()` Method

`Object.is()` is an ES6 method that determines whether two values are the same. This works like the strict equality operator.

```js
// Syntax
Object.is(value1, value2)
```

Let’s make use of the previous example to see if it works like the strict equality operator:

```js
let firstName = null;
let lastName;

console.log(Object.is(firstName, null)); // true
console.log(Object.is(lastName, null)); // false
console.log(Object.is(firstName, undefined)); // false
console.log(Object.is(lastName, undefined)); // true
console.log(Object.is(firstName, lastName)); // false
console.log(Object.is(null, undefined)); // false
```

This happens because it only returns `true` when both values are the same. This means that it will only return `true` when a variable set to `null` is compared with `null`, and an undefined variable is compared with `undefined`.

## Conclusion

Now you know how to check for null with confidence. You can also check whether a variable is set to `null` or `undefined`, and you know the difference between the loose and strict equality operators.

I hope this was helpful. Have fun coding!

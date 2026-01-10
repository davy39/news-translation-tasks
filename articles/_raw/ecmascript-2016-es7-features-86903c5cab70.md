---
title: Introducing the new features that ECMAScript 2016 (ES7) adds to JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-14T16:10:59.000Z'
originalURL: https://freecodecamp.org/news/ecmascript-2016-es7-features-86903c5cab70
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UdGS7qrmIMueYfILnJJ6QA.png
tags:
- name: ES6
  slug: es6
- name: es7
  slug: es7
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sanket Meghani

  Since ECMAScript 2015 (also known as ES6) was released, it has introduced a huge
  set of new features. They include arrow functions, sets, maps, classes and destructuring,
  and much more. In many ways, ES2015 is almost like learning a...'
---

By Sanket Meghani

Since ECMAScript 2015 (also known as ES6) was released, it has introduced a huge set of new features. They include arrow functions, sets, maps, classes and destructuring, and much more. In many ways, ES2015 is almost like learning a new version of JavaScript.

Ecma Technical Committee 39 governs the ECMA specification. They decided to release a new version of ECMAScript every year starting in 2015. A yearly update means no more big releases like ES6.

ECMAScript 2016 introduced only two new features:

* Array.prototype.includes()
    
* Exponentiation operator
    

### Array.prototype.includes()

`Array.prototype.includes()` checks the array for the `value` passed as an `argument`. It returns `true` if the array contains the `value`, otherwise, it returns `false`.

Before, we needed to use `Array.prototype.indexOf()` to check if the given array contains an element or not.

```javascript
let numbers = [1, 2, 3, 4];

if(numbers.indexOf(2) !== -1) {
  console.log('Array contains value');
}
```

With ECMA2016, we can write:

```javascript
if (numbers.includes(2)) {
  console.log('Array contains value');
}
```

`Array.prototype.includes()` handles `NaN` better than `Array.prototype.indexOf()`. If the array contains `NaN`, then `indexOf()` does not return a correct index while searching for `NaN`.

`Array.prototype.includes()` returns the correct value when searching for `NaN`.

`NaN` is a property of the JavaScript global object and represents a value that is Not-a-Number. There are known quirks when [comparing `NaN` to another value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN). These are addressed in `Array.prototype.includes()`, but not in `Array.protoype.indexOf`.

```javascript
let numbers = [1, 2, 3, 4, NaN];

console.log(numbers.indexOf(NaN)); //Prints -1
console.log(numbers.includes(NaN)); //Prints true
```

### Exponentiation Operator

JavaScript already supports many arithmetic operators like `+, -, *` and more.

ECMAScript 2016 introduced the exponentiation operator, `**`.

It has the same purpose as `Math.pow()`. It returns the first argument raised to the power of the second argument.

```javascript
let base = 3;
let exponent = 4;
let result = base**exponent;

console.log(result); //81
```

### Conclusion

New features introduced by ECMA2016 provide convenient alternatives to existing functionalities.

Looking ahead, ECMA2017 was finalized in June of this year. New features include `async/await`, `SharedArrayBuffer` and some useful methods to `Object.prototype`.

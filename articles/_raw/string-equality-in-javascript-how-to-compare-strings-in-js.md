---
title: String Equality in JavaScript – How to Compare Strings in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-12-22T18:57:16.000Z'
originalURL: https://freecodecamp.org/news/string-equality-in-javascript-how-to-compare-strings-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-template--3-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When writing code or building a solution, you might need to compare two
  strings to see if they are the same before proceeding with an operation.

  For example, when a user signs in, you''ll want to compare the username the provide
  to the one in your dat...'
---

When writing code or building a solution, you might need to compare two strings to see if they are the same before proceeding with an operation.

For example, when a user signs in, you'll want to compare the username the provide to the one in your database to see if they match.

In JavaScript, you can compare strings based on their value, length, character case, and lots more. In this article, you will learn how to compare strings in JavaScript.

## How to Compare Strings in JavaScript With the Strict Equality Operator

Strict equality, or three equality (`===`) as its symbol implies, is a more detailed comparison than loose equality (`==`). It does not only check if the values are the same, but it also checks the operands:

```js
let a = 12;
let b = '12';

// Loose Equality
console.log(a == b); // true
// Strict Equality
console.log(a === b); // false
```

The strict operator is best used to compare strings in JavaScript because it checks to be sure both operands and values are the same and then returns a boolean result.

```js
let string1 = "freeCodeCamp";
let string2 = "codeCamp";

console.log(string1 === string2); // false
```

You can also directly compare a string to a variable and a string to a string if you wish:

```js
let string1 = "freeCodeCamp";

console.log(string1 === "codeCamp"); // false
console.log(string1 === "freeCodeCamp"); // true
console.log("codeCamp" === "freeCodeCamp"); // false
```

### How to Perform Case Insensitive Comparison

When comparing with the strict equality operator, it is essential to know that this comparison is case sensitive. This means that `freeCodeCamp` is not equal to `FreeCodeCamp` because the first letter f is lowercase for one and uppercase for the other.

```js
console.log("freeCodeCamp" === "FreeCodeCamp"); // false
```

To avoid situations like this, you can perform case-insensitive comparisons. This means you convert the strings you are comparing to the same case:

```js
let string1 = "freeCodeCamp";
let string2 = "FreeCodeCamp";

console.log(string1.toLowerCase() == string2.toLowerCase()); // true
console.log(string1.toUpperCase() == string2.toUpperCase()); // true
```

## How to Compare Strings in JavaScript with the `.length` Property

In JavaScript, when you attach the `.length` property to a variable, it returns the string length:

```js
let string1 = "freeCodeCamp";

console.log(string1.length); // 12
```

This means you can use the length property to compare alongside either the equality (loose or strict), greater than (&gt;), or less than (operator) to check if both lengths are the same or if one is more than the other.

```js
let string1 = "freeCodeCamp";
let string2 = "codeCamp";

console.log(string1.length > string2.length); // true
console.log(string1.length < string2.length); // false
console.log(string1.length == string2.length); // false
console.log(string1.length === string2.length); // false
```

## How to Compare Strings in JavaScript With the `localeCompare()` Method

The `localeCompare()` method can compare strings based on the current locale on the browser’s settings.

This method can be quite tricky, but it’s important to know that this method compares each character of both strings and returns a number which can be “-1”, “1”, or “0”.

* \-1: The left side string alphabetically comes before the right side string.
    
* 1: The left side string alphabetically comes after the right side string.
    
* 0: This means that both strings are equal.
    

```js
let string1 = "freeCodeCamp";
let string2 = "codeCamp";

console.log(string1.localeCompare(string2)); // 1
```

This returns “1” because “f” comes after “c” in the first character comparison.

```js
let string1 = "freeCodeCamp";
let string2 = "codeCamp";

console.log(string2.localeCompare(string1)); // -1
```

This now returns “-1” because “c” which is the first character of `string2` on the left side comes before “f”. When both strings are equal, it returns “0” irrespective of their positions:

```js
let string1 = "freeCodeCamp";
let string2 = "freeCodeCamp";

console.log(string2.localeCompare(string1)); // 0
```

### How to Perform Case Insensitive Comparison

It is also important to highlight that when you use the `localeCompare()` method, it is case sensitive. This means that it will return either “1” or “-1” depending on the position, even if both strings are the same but with a different case:

```js
let string1 = "freeCodeCamp";
let string2 = "FreeCodeCamp";

console.log(string2.localeCompare(string1)); // 1
```

You can fix this by introducing options and locale to the `localeCompare()` method. This method allows you to set a locale and also options that you can use to convert both strings to similar cases, so you perform a case-insensitive comparison.

```js
let string1 = "freeCodeCamp";
let string2 = "FreeCodeCamp";

console.log(string2.localeCompare(string1, "en", { sensitivity: "base" })); // 0
```

You can read more about the [localeCompare()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare) method in the MDN documentation.

## Wrapping Up

In this article, you have learned how to compare strings in JavaScript using the equality operators and the `localeCompare()` method.

Feel free to use your preferred methods, but you should mostly use `localeCompare()` when the comparison involves locale and some specific comparison that involves locale.

Have fun coding!

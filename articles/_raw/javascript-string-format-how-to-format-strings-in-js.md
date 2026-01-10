---
title: JavaScript String Format – Formatting Strings in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-11T18:38:41.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-format-how-to-format-strings-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/js-string-format.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  JavaScript has many string methods you can use to format strings. In this article,
  I''ll show you some of the most commonly used methods.

  How to Use the toLowerCase() String Method

  As the name implies, you use the toLowerCase() strin...'
---

By Dillion Megida

JavaScript has many string methods you can use to format strings. In this article, I'll show you some of the most commonly used methods.

## How to Use the `toLowerCase()` String Method

As the name implies, you use the `toLowerCase()` string method to convert strings to their lowercase version. 

This method does not affect the original string. It takes the original string and returns a new string, which is the lowercased version. 

Here is an example:

```js
const string = "HeLLo woRld"

const lowercased = string.toLowerCase()

console.log(string)
// HeLLo woRld

console.log(lowercased)
// hello world
```

As you can see, the new string has all its letters lowercased.

## How to Use the `toUpperCase()` String Method

Similar to the first method, `toUpperCase` is a string method you use to convert strings to their uppercase version. 

It also doesn't affect the original string. 

Here is an example:

```js
const string = "HeLLo woRld"

const uppercased = string.toUpperCase()

console.log(string)
// HeLLo woRld

console.log(uppercased)
// HELLO WORLD
```

Using the original string, it returns a new string, which is the uppercase version.

## How to Use the `replace()` String Method

You use the `replace` string method to replace a section of a string with a substring. This way, you will format the string so you can modify it. 

Here's an example of how the `replace` method works:

```js
const string = "Hello world"

const modified = string.replace("world", "developers")

console.log(string)
// Hello world

console.log(modified)
// Hello developers
```

The `replace` method, as seen above, replaces the "world" substring with "developers". It also doesn't affect the original string.

You can also use a regex in place of a string as a replacer:

```js
const string = "Hello world"

const modified = string.replace(/o/g, "--")

console.log(string)
// Hello world

console.log(modified)
// Hell-- w--rld
```

Using a regex pattern to match the "o" character globally, you can see the modified string containing double hyphens in place of the "o" in the string.

## How to Use the `trim()` String Method

The `trim` method modifies strings by removing whitespaces from the beginning and end of a string. 

It doesn't modify the original string. Instead it returns a new string with the whitespaces stripped out. 

Here is an example:

```js
const string = "  H ell  o world  "

const modified = string.trim()

console.log(string)
//   H ell  o world 

console.log(modified)
// H ell  o world
```

You can see that only the spaces at the start and end are stripped off, and not the spaces between letters.

Whitespaces include spaces, tabs, break lines, and so on.

## Wrapping Up

There are a couple of more ways you can format or modify strings in JavaScript. In this article, I've shared four of the most common methods you can use: `toUpperCase`, `toLowerCase`, `replace` and `trim`. 

These methods do not affect the original string but return a new string formatted in a specific way.

You can learn more about [Useful String Methods in JavaScript here](https://dillionmegida.com/p/10-useful-string-methods-in-javascript/).



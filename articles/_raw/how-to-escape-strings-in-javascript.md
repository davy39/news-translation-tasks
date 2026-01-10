---
title: How to Escape a String in JavaScript – JS Escaping Example
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-02T19:05:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-escape-strings-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, a string is a data type representing a sequence of characters
  that may consist of letters, numbers, symbols, words, or sentences.

  Strings are used to represent text-based data and are mostly defined using either
  single quotes ('') or do...'
---

In JavaScript, a string is a data type representing a sequence of characters that may consist of letters, numbers, symbols, words, or sentences.

Strings are used to represent text-based data and are mostly defined using either single quotes (`'`) or double quotes (`"`).

```js
let name1 = 'John Doe';
let name2 = "John Doe";
```

Due to the fact that these quotation marks are used to denote strings, you need to be careful when using apostrophes and quotes in strings.

When you attempt to use them within a string, in an actual sense it will end the string, and JavaScript will attempt to parse the rest of the intended string as code. This will throw an error.

```js
let quote = "He said, "I learned from freeCodeCamp!"";
```

This will throw an error, as seen below:

```js
Uncaught SyntaxError: Unexpected identifier 'I'
```

In JavaScript, if you need to include quotes or apostrophes within a string, there are three major ways to fix the error. These methods are:

* By using the opposite string syntax
    
* Using an escape character
    
* Using template literals
    

## How to use Opposite String Syntax to Escape a String in JavaScript

In JavaScript, you can use the opposite string syntax `'` or `"` to escape a string. To do so, you must wrap the string in the opposite syntax of what you are escaping.

```js
let quote = 'He said, "I learned from freeCodeCamp!"';
console.log(quote); // He said, "I learned from freeCodeCamp!"

let apostrophe = "It's a beautiful day";
console.log(apostrophe); // It's a beautiful day
```

This means if you use double quotes to wrap your string, you can use an apostrophe within the string. Also if you wrap your string in single quotes, then you can use double quotes within the string.

But there are limitations to this because what if you have to use a quote and an apostrophe within the same string? Then you can use an escape character (`\`).

## How to Use the Escape Character (`\`) to Escape a String in JavaScript

In JavaScript, you can escape a string by using the `\` (backslash) character. The backslash indicates that the next character should be treated as a literal character rather than as a special character or string delimiter.

Here is an example of escaping a string in JavaScript:

```js
let quote = "He said, \"I learned from freeCodeCamp!\"";
console.log(quote); // He said, "I learned from freeCodeCamp!"

let apostrophe = 'It\'s a beautiful day';
console.log(apostrophe); // It's a beautiful day
```

## How to Use Template Literals to Escape a String in JavaScript

In JavaScript, you can also use Template Literals (also known as Template Strings) to escape a string.

Template Literals are string literals that allow you to embed expressions inside a string, using the syntax `${expression}`.

```js
let quote = `He said, "I learned from freeCodeCamp!"`;
console.log(quote); // He said, "I learned from freeCodeCamp!"
```

With Template Literals, you don't need to use backslashes to escape characters. Instead, you simply wrap the string in backticks ( )

## Wrapping Up!

In this article, you have learned how to escape a string in JavaScript. This will help you avoid using Unicode characters to add quotes and apostrophes within strings.

You can access over 180 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.

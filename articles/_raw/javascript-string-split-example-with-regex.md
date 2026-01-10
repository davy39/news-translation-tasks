---
title: JavaScript String.Split() Example with RegEx
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-26T18:31:08.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-split-example-with-regex
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/string-split-with-regex.png
tags:
- name: JavaScript
  slug: javascript
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'By Dillion Megida

  In JavaScript, you use RegEx to match patterns in characters. Combining this with
  the .split() string method gives you more splitting powers.

  The string constructor has many useful methods, one of which is the split() method.
  You us...'
---

By Dillion Megida

In JavaScript, you use RegEx to match patterns in characters. Combining this with the `.split()` string method gives you more splitting powers.

The string constructor has [many useful methods](https://dillionmegida.com/p/10-useful-string-methods-in-javascript/), one of which is the `split()` method. You use this method to split a string into an array of substrings using a breakpoint. 

Here is how it is often used:

```js
const string = "How is everything going?"

const breakpoint = " "

const splitted = string.split(breakpoint);

// [ 'How', 'is', 'everything', 'going?' ]
```

Using a space (" ") as the breakpoint, the `split` method splits the string at those breakpoints.

The breakpoint here is a fixed character. What if you want to split based on a pattern? Like a number-character or symbol-space? Then you can use the `split` method with regex to achieve this.

## How to Use RegEx with .split in JavaScript

The `split` method accepts one argument – a breakpoint. This breakpoint determines the points at which the splitting should occur. This breakpoint can be a string or a regex pattern.

Here is an example using a regex pattern:

```js
const string = "How is $everything g$oing?"

const breakpoint = /\$e|\$o/

const splitted = string.split(breakpoint)

// [ 'How is ', 'verything g', 'ing?' ]
```

The regex pattern matches the dollar sign followed by the letter "e" (`$e`) or the dollar sign followed by the letter o (`$o`). 

The split method uses characters that match this pattern as a breakpoint, and as you can see, the "$e" in "$everything" and the "$o" in "g$oing" served as a breakpoint to split the string into substrings.

You do not need to apply the global flag `g` in the regex, as the split method already looks for all occurrences of the regex pattern as the breakpoint.

## Wrapping Up

You do not only have to use literal strings for splitting strings into an array with the `split` method. You can use regex as breakpoints that match more characters for splitting a string.

The `replace` method in strings also supports regex patterns. Check it out in this article: [JavaScript String.Replace() Example with RegEx](https://www.freecodecamp.org/news/javascript-string-replace-example-with-regex/)



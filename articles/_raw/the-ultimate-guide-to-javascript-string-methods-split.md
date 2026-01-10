---
title: The Ultimate Guide to JavaScript String Methods - Split
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-10T18:06:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-javascript-string-methods-split
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f74740569d1a4ca42ac.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'The split() method separates an original string into an array of substrings,
  based on a separator string that you pass as input. The original string is not altered
  by split().

  Syntax

  const splitStr = str.split(separator, limit);



  separator - a strin...'
---

The `split()` method separates an original string into an array of substrings, based on a `separator` string that you pass as input. The original string is not altered by `split()`.

## Syntax

```js
const splitStr = str.split(separator, limit);
```

* `separator` - a string indicating where each split should occur
* `limit` - a number for the amount of splits to be found

## Examples:

```js
const str = "Hello. I am a string. You can separate me.";
const splitStr = str.split("."); // Will separate str on each period character

console.log(splitStr); // [ "Hello", " I am a string", " You can separate me", "" ]
console.log(str); // "Hello. I am a string. You can separate me."
```

Since we used the period (`.`) as the `separator` string, the strings in the output array do not contain the period in them – the output separated strings do not include the input `separator` itself.

You can operate on strings directly, without storing them as variables:

```js
"Hello... I am another string... keep on learning!".split("..."); // [ "Hello", " I am another string", " keep on learning!" ]
```

Also, string separator does not have to be a single character, it can be any combination of characters:

```js
const names = "Kratos- Atreus- Freya- Hela- Thor- Odin";
const namesArr = names.split("- "); // Notice that the separator is a dash and a space
const firstThreeNames = names.split("- ", 3);

console.log(namesArr) // [ "Kratos", "Atreus", "Freya", "Hela", "Thor", "Odin" ]
console.log(firstThreeNames); // [ "Kratos", "Atreus", "Freya" ]
```

## Common Uses of `split`

The `split()` method is very useful once you grasp the basics. Here are a few common use cases for `split()`:

### Create an array of words from a sentence:

```js
const sentence = "Ladies and gentlemen we are floating in space.";
const words = sentence.split(" "); // Split the sentence on each space between words

console.log(words); // [ "Ladies", "and", "gentlemen", "we", "are", "floating", "in", "space." ]
```

### Create an array of letters in a word:

```js
const word = "space";
const letters = word.split("");

console.log(letters); // [ "s", "p", "a", "c", "e" ]
```

### Reversing the letters in a word:

Because the `split()` method returns an array, it can be combined with array methods like `reverse()` and `join()`:

```js
const word = "float";
const reversedWord = word.split("").reverse().join("");

console.log(reversedWord); // "taolf"
```

That's all you need to know to `split()` strings with the best of 'em!


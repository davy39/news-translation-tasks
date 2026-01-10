---
title: JavaScript String.Replace() Example with RegEx
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-20T20:31:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-replace-example-with-regex
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c982a740569d1a4ca1884.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Regex
  slug: regex
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dillion Megida

  Regular Expressions (also called RegEx or RegExp) are a powerful way to analyze
  text. With RegEx, you can match strings at points that match specific characters
  (for example, JavaScript) or patterns (for example, NumberStringSymbol ...'
---

By Dillion Megida

Regular Expressions (also called RegEx or RegExp) are a powerful way to analyze text. With RegEx, you can match strings at points that match specific characters (for example, JavaScript) or patterns (for example, NumberStringSymbol - 3a&).

The `.replace` method is used on strings in JavaScript to replace parts of string with characters. It is often used like so:

```js
const str = 'JavaScript';
const newStr = str.replace("ava", "-");
console.log(newStr);
// J-Script
```

As you can see above, the replace method accepts two arguments: the string to be replaced, and what the string would be replaced with.

Here is where **Regex** comes in.

The use of `.replace` above is limited: the characters to be replaced are known - "ava". What if we're concerned with a pattern instead? Maybe, a number, two letters, and the word "foo" or three symbols used together?

The `.replace` method used with `RegEx` can achieve this. `RegEx` can be effectively used to recreate patterns. So combining this with `.replace` means we can replace patterns and not just exact characters.

## How to use `RegEx` with `.replace` in JavaScript

To use RegEx, the first argument of `replace` will be replaced with regex syntax, for example `/regex/`. This syntax serves as a pattern where any parts of the string that match it will be replaced with the new substring.

Here's an example:

```js
// matches a number, some characters and another number
const reg = /\d.*\d/
const str = "Java3foobar4Script"
const newStr = str.replace(reg, "-");
console.log(newStr);
// "Java-Script"
```

The string `3foobar4` matches the regex `/\d.*\d/`, so it is replaced.

What if we wanted to perform replacements at multiple places?

`Regex` already offers that with the `g` (global) flag, and the same can be used with `replace`. Here's how:

```js
const reg = /\d{3}/g
const str = "Java323Scr995ip4894545t";
const newStr = str.replace(reg, "");
console.log(newStr);
// JavaScrip5t
// 5 didn't pass the test :(
```

The regex matches parts of the string that are exactly 3 consecutive numbers. `323` matches it, `995` matches it, `489` matches it, and `454` matches it. But the last `5` does not match the pattern. 

The result is that `JavaScrip5t` shows how the patterns are correctly matched and replaces with the new substring (an empty string).

The case flag - `i` can also be used. This means you can replace case-insensitive patterns. Here's how it is used:

```js
const reg1 = /\dA/
const reg2 = /\dA/i
const str = "Jav5ascript"
const newStr1 = str.replace(reg1, "--");
const newStr2 = str.replace(reg2, "--");
console.log(newStr1) // Jav5ascript
console.log(newStr2) // Jav--script
```

`..5a..` does not match the first syntax because RegEx is by default case-sensitive. But with the usage of the `i` flag, as seen in the second syntax, the string is as expected - replaced.

## How to use Split with Regular Expressions

`split` also uses `RegEx`. Which means you can split a string not just at substrings that match exact characters, but also patterns.

Here's a quick look:

```js
const regex = /\d{2}a/;
const str = "Hello54 How 64aare you";
console.log(str.split(regex))
// ["Hello54 How ", "are you"]
```

The string was `split` at `64a` because that substring matches the regex specified.

**Note that** the global flag - `g` - in `split` is irrelevant, unlike the `i` flag and other flags. This is because `split` splits the string at the several points the regex matches.

## Wrapping up

`RegEx` makes `replace`ing strings in JavaScript more effective, powerful, and fun. 

You're not only restricted to exact characters but patterns and multiple replacements at once. In this article, we've seen how they work together using a few examples.

Cheers to RegEx ?



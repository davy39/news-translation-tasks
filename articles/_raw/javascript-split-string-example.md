---
title: JavaScript Split String Example – How to Split a String into an Array in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-03T00:04:13.000Z'
originalURL: https://freecodecamp.org/news/javascript-split-string-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/jon-flobrant-rB7-LCa_diU-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By David\nA string is a data structure that represents a sequence of characters,\
  \ and an array is a data structure that contains multiple values. \nAnd did you\
  \ know – a string can be broken apart into an array of multiple strings using the\
  \ split method...."
---

By David

A string is a data structure that represents a sequence of characters, and an array is a data structure that contains multiple values. 

And did you know – a string can be broken apart into an array of multiple strings using the `split` method. Let's see how that works with some examples.

## TL;DR

If you just want the code, here you go:

```javascript
const publisher = 'free code camp'
publisher.split(' ') // [ 'free', 'code', 'camp' ]

```

## Syntax

According to the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split), the syntax you'll need to split the string is `str.split([separator[, limit]])`. If we apply this to the above example:

* `str` is `publisher`
* `separator` is `' '`
* there is no `limit`

## When do you need to split a string?

### Example 1: getting part of a string

Here is a common example which involves getting the token from an auth header that is part of a Token-based Authentication System. 

If this doesn't mean anything to you that's ok. All you need to know for the following example is that there is a string with the value `bearer token`, but only `token` is needed (as this is the part that identifies the user):

```javascript
const authHeader = 'bearer token'
const split = authHeader.split(' ') // (1) [ 'bearer', 'token' ]
const token = split[1] // (2) token
```

Here's what's happening in the above code:

1. The string is split with `' '` as the separator
2. The second entry in the array is accessed

### Example 2: apply array methods to a string

Often the input you are given is a string, but you want to apply array methods to it (eg. `map`, `filter`, or `reduce`). 

For example, let's say you are given a string of morse code and you want to see what it reads in English:

```javascript
const morse = '-.-. --- -.. .'
// (1)
const morseToChar = {
  '-.-.': 'c',
  '-..': 'd',
  '.': 'e',
  '---': 'o',
}

const morseArray = morse.split(' ') // (2) [ '-.-.', '---', '-..', '.' ]
const textArray = morseArray.map((char) => morseToChar[char]) // (3) [ 'c', 'o', 'd', 'e' ]
const text = textArray.join(") // (4)

```

Here's what's happening in the above code:

1. An object literal is created to map morse chars to the English alphabet
2. The morse code is split into an array with a `' '` as the separator. (Without `' '` as an argument you would end up with an array that has separate entries for each `.` and `-`.)
3. The morse code array is mapped/transformed to a text array
4. A string is created from the array with `''` as the separator. (Without `''` as an argument the output would be `c,o,d,e`.)

## How to add a limit to split

According to the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split), it is also possible to pass a `limit` as an argument to `split`. I have never needed to do this, but here is how you could apply it:

```javascript
const publisher = 'free code camp'
publisher.split(' ', 1) // [ 'free' ]

```

In the above example, the array is limited to one entry. Without it the value of the array would be `[ 'free', 'code', 'camp' ]`.

## Before you go…

Thank you for reading this far! I write about my professional and educational experiences as a self-taught software developer, so feel free to check out [my website](https://learnitmyway.com/) or subscribe to [my newsletter](https://learnitmyway.com/newsletter) for more content.

You might also like:

* [Learn JavaScript with these resources](https://learnitmyway.com/learn-javascript-with-these-resources/)
* [Learning material - software development](https://www.learnitmyway.com/2016/11/11/learning-material-software-development/) (starting with Intro to CS)


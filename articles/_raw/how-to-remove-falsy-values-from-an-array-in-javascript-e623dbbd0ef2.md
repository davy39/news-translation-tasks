---
title: How to remove falsy values from an array in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-12T17:43:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-falsy-values-from-an-array-in-javascript-e623dbbd0ef2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ArHOj9iu7kJxxEhRukDKJw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dylan Attal

  There are a lot of ways to remove elements from an array in JavaScript, but what’s
  the easiest way to remove all falsy values from an array? In order to answer that
  question we’ll take a close look at truthy versus falsy values and typ...'
---

By Dylan Attal

There are a lot of ways to remove elements from an array in JavaScript, but what’s the easiest way to remove all falsy values from an array? In order to answer that question we’ll take a close look at truthy versus falsy values and type coercion within the context of an algorithm scripting challenge.

#### Algorithm instructions

> Remove all falsy values from an array.

> Falsy values in JavaScript are `false`, `null`, `0`, `""`, `undefined`, and `NaN`.

> Hint: Try converting each value to a Boolean.

#### Provided Test Cases

* `bouncer([7, "ate", "", false, 9])`should return `[7, "ate", 9]`.
* `bouncer(["a", "b", "c"])`should return `["a", "b", "c"]`.
* `bouncer([false, null, 0, NaN, undefined, ""])`should return `[]`.
* `bouncer([1, null, NaN, 2, undefined])`should return `[1, 2]`.

### Solution #1: .filter( ) and Boolean( )

#### PEDAC

**Understanding the Problem**: We have one input, an array. Our goal is to remove all the falsy values from the array then return the array.

The good people at freeCodeCamp have told us that falsy values in JavaScript are `false`, `null`, `0`, `_""_`, `undefined`, and `NaN`.

They have also dropped a major hint for us! They suggest converting each value of the array into a boolean in order to accomplish this challenge. I think that’s a great hint!

**Examples/Test Cases**: Our provided test cases show us that if the input array only contains falsy values, then we should just return an empty array. That’s pretty straightforward.

**Data Structure**: We are going to stick with arrays here.

Let’s talk about `[.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)`:

`.filter()` creates a new array with all elements that pass the test implemented by the provided function.

In other words, `.filter()` goes through each element in an array and preserves all the elements that pass a certain test. All the elements in the array that fail that test are filtered out — they’re removed.

For example, if we had an array of numbers and we only wanted the numbers greater than 100, we could use `.filter()` to accomplish that:

```
let numbers = [4, 56, 78, 99, 101, 150, 299, 300]numbers.filter(number => number > 100)// returns [ 101, 150, 299, 300 ]
```

Let’s talk about the hint of converting each element to a boolean. This is a good hint because we can use `.filter()` to return the array with only the truthy values.

We’re going to accomplish that through [JavaScript type conversion](https://www.w3schools.com/js/js_type_conversion.asp).

JavaScript gives us useful functions to convert one data type to another. `String()` converts to a string, `Number()` converts to a number, and `Boolean()` converts to a boolean.

For example:

```
String(1234)// returns "1234"
```

```
Number("47")// returns 47
```

```
Boolean("meow")// returns true
```

`Boolean()` is the function we’ll be implementing with this challenge. If the argument provided to `Boolean()` is truthy, then `Boolean()` will return `true.` If the argument provided to `Boolean()` is falsy, then `Boolean()` will return `false`.

This is useful to us because we know from the instructions that only `false`, `null`, `0`, `_""_`, `undefined`, and `NaN` are falsy in JavaScript. Every other value is truthy. Knowing that, if we convert each value in the input array to a boolean, we can remove all elements that evaluate to `false`, and that will satisfy the requirements for this challenge.

**Algorithm**:

1. Determine which values in `arr` are falsy.
2. Remove all falsy values.
3. Return the new array that contains only truthy values.

**Code**: See below!

Without comments and removing the local variable:

If you have other solutions and/or suggestions, please share in the comments!

#### This article is a part of the series [freeCodeCamp Algorithm Scripting](https://medium.com/@DylanAttal/freecodecamp-algorithm-scripting-b96227b7f837).

#### This article references [freeCodeCamp Basic Algorithm Scripting: Falsy Bouncer](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/falsy-bouncer).

You can follow me on [Medium](https://medium.com/@DylanAttal), [LinkedIn](https://www.linkedin.com/in/dylanattal/), and [GitHub](https://github.com/DylanAttal)!


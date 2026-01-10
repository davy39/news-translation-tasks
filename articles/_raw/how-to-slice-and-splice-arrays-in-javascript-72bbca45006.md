---
title: How to slice and splice arrays in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T21:17:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-slice-and-splice-arrays-in-javascript-72bbca45006
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XLAL5nDPpacrVdZ4MhJH2Q.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Dylan Attal

  .slice() and .splice() are similar methods in JavaScript. They look similar, they
  sound similar, and they do similar things. For those reasons, it’s important to
  know the differences between them. Also, they’re used very often, so unde...'
---

By Dylan Attal

`.slice()` and `.splice()` are similar methods in JavaScript. They look similar, they sound similar, and they do similar things. For those reasons, it’s important to know the differences between them. Also, they’re used very often, so understanding their usage is good to learn early on for any software developer.

In this article we’ll look at how to use them with a specific algorithm scripting challenge. We’ll be inserting elements from one array into another and returning the combined array without mutating the original arrays.

#### Algorithm instructions

> You are given two arrays and an index.

> Use the array methods `slice` and `splice` to copy each element of the first array into the second array, in order.

> Begin inserting elements at index `n` of the second array.

> Return the resulting array. The input arrays should remain the same after the function runs.

```js
function frankenSplice(arr1, arr2, n) {
  return arr2;
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

#### Provided Test Cases

* `frankenSplice([1, 2, 3], [4, 5], 1)`should return `[4, 1, 2, 3, 5]`.
* `frankenSplice([1, 2], ["a", "b"], 1)`should return `["a", 1, 2, "b"]`.
* `frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2)`should return `["head", "shoulders", "claw", "tentacle", "knees", "toes"]`.
* All elements from the first array should be added to the second array in their original order.
* The first array should remain the same after the function runs.
* The second array should remain the same after the function runs.

### Solution #1: .slice( ), .splice( ), and spread operator

#### PEDAC

**Understanding the Problem**: We have one input, a string. Our output is also a string. Ultimately, we want to return the input string with the first letter — and only the first letter — of each word capitalized.

**Examples/Test Cases**: Our provided test cases show that we should have a capitalized letter only at the beginning of each word. We need to lower case the rest. The provided test cases also show that we aren’t being thrown any curve balls in terms of weird compound words separated by symbols instead of whitespace. That’s good news for us!

**Data Structure**: We are going to have to transform our input string into an array in order to manipulate each word separately.

Let’s have a little chat about `.slice()` and `.splice()`:

First let’s address `[.slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)`:

`.slice()` extracts a section of a string and returns it as a new string. If you call `.slice()` on a string without passing it any additional information, it will return the whole string.

```js
"Bastian".slice()
// returns "Bastian"
```

This will be useful to us in this algorithm scripting challenge because the instructions tell us that we should not directly modify the input arrays. So we’re going to need to make a copy of one of them.

Now let’s look at `[.splice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)`:

`.splice()` changes the contents of an array by removing or replacing existing elements and/or adding new elements.

We can pass `.splice()` several arguments that determine where the deletion begins, how much is deleted, and what is inserted. `start` is a number that tells `.splice()` at which index to begin deleting elements. `deleteCount` tells `.splice()` how many elements to delete.

Wait a second! What if you don’t want to delete anything? What if you just want to insert elements? That’s fine. Just set `deleteCount` to zero. Now we can start adding items. Just separate each element with a comma, like so `item1, item2, item3, item4`.

```
.splice(start, deleteCount, item1, item2, item3, etc.)
```

Another concept to keep in mind for this algorithm scripting challenge is the [spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax). ES6 gifted us with the spread operator which looks like ellipses — just three dots in a row.

The spread operator is most commonly used when you want to use the elements of an array as arguments to a function. That’s exactly what we’re going to do with it in this challenge. We don’t want to insert the entire array `arr1` into `arr2`. We want to insert each element of `arr1` into `arr2`.

**Algorithm**:

1. Create a copy of `arr2`.
2. Insert all the elements of `arr1` into `arr2` starting at the index in `arr2` specified by `n`.
3. Return the combined arrays.

**Code**: See below!

```js
function frankenSplice(arr1, arr2, n) {
  // Create a copy of arr2.
  let combinedArrays = arr2.slice()
  //                   [4, 5, 6]

  // Insert all the elements of arr1 into arr2 beginning
  // at the index specified by n. We're using the spread
  // operator "..." to insert each individual element of 
  // arr1 instead of the whole array.
  combinedArrays.splice(n, 0, ...arr1)
  //                   (1, 0, ...[1, 2, 3])
  //                   [4, 1, 2, 3, 5, 6]

  // Return the combined arrays.
  return combinedArrays
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

Without comments:

```js
function frankenSplice(arr1, arr2, n) {
  let combinedArrays = arr2.slice()
  combinedArrays.splice(n, 0, ...arr1)
  return combinedArrays
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

### Solution #2: .slice( ), .splice( ), and for loop

#### PEDAC

**Understanding the Problem**: We have one input, a string. Our output is also a string. Ultimately, we want to return the input string with the first letter — and only the first letter — of each word capitalized.

**Examples/Test Cases**: Our provided test cases show that we should have a capitalized letter only at the beginning of each word. We need to lower case the rest. The provided test cases also show that we aren’t being thrown any curve balls in terms of weird compound words separated by symbols instead of whitespace. That’s good news for us!

**Data Structure**: We are going to have to transform our input string into an array in order to manipulate each word separately.

Let’s have a little chat about `.slice()` and `.splice()`:

First let’s address `[.slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)`:

`.slice()` extracts a section of a string and returns it as a new string. If you call `.slice()` on a string without passing it any additional information, it will return the whole string.

```js
"Bastian".slice()
// returns "Bastian"
```

This will be useful to us in this algorithm scripting challenge because the instructions tell us that we should not directly modify the input arrays. So we’re going to need to make a copy of one of them.

Now let’s look at `[.splice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)`:

`.splice()` changes the contents of an array by removing or replacing existing elements and/or adding new elements.

We can pass `.splice()` several arguments that determine where the deletion begins, how much is deleted, and what is inserted. `start` is a number that tells `.splice()` at which index to begin deleting elements. `deleteCount` tells `.splice()` how many elements to delete. Wait a second! What if you don’t want to delete anything? What if you just want to insert elements? That’s fine. Just set `deleteCount` to zero. Now we can start adding items. Just separate each element with a comma, like so `item1, item2, item3, item4`.

```
.splice(start, deleteCount, item1, item2, item3, etc.)
```

Unlike in the previous solution, we won’t be using the spread operator here. We’ll be using a for loop instead to pluck each element one at a time from `arr1` and insert them into `arr2`.

The trick here is to increment `n` by 1 each time the loop runs or else the elements of `arr1` will not end up in the right order when inserted into `arr2`.

**Algorithm**:

1. Create a copy of `arr2`.
2. Using a for loop, insert each element of `arr1` into `arr2` starting at index `n`.
3. Increment `n` by 1 each time the loop runs.
4. Return the combined arrays.

**Code**: See below!

```js
function frankenSplice(arr1, arr2, n) {
  // Create a copy of arr2.
  let combinedArrays = arr2.slice()
  // Using a for loop, insert each element of arr1
  // into combinedArrays starting at index n.
  for (let i = 0; i < arr1.length; i++) {
      combinedArrays.splice(n, 0, arr1[i])
  //       [4, 5, 6].splice(1, 0, 1)
  //    [4, 1, 5, 6].splice(2, 0, 2)
  // [4, 1, 2, 5, 6].splice(3, 0, 3)
  // [4, 1, 2, 3, 5, 6]

  //  increment n by 1 each time the loop runs
      n++
  }
  // Return the combined arrays.
  return combinedArrays
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

Without comments:

```js
function frankenSplice(arr1, arr2, n) {
  let combinedArrays = arr2.slice()
  for (let i = 0; i < arr1.length; i++) {
    combinedArrays.splice(n, 0, arr1[i])
    n++
  }
  return combinedArrays
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

If you have other solutions and/or suggestions, please share in the comments!

#### This article is a part of the series [freeCodeCamp Algorithm Scripting](https://medium.com/@DylanAttal/freecodecamp-algorithm-scripting-b96227b7f837).

#### This article references [freeCodeCamp Basic Algorithm Scripting: Slice and Splice](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/slice-and-splice)

You can follow me on [Medium](https://medium.com/@DylanAttal), [LinkedIn](https://www.linkedin.com/in/dylanattal/), and [GitHub](https://github.com/DylanAttal)!


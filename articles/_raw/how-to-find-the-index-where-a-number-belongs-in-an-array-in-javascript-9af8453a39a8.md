---
title: How to find the index where a number belongs in an array in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-13T20:07:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-the-index-where-a-number-belongs-in-an-array-in-javascript-9af8453a39a8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XdBvGuY3oLB3E3Iv0CD-SA.jpeg
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

  Sorting is a very important concept when writing algorithms. There are all kinds
  of sorts: bubble sort, shell sort, block sort, comb sort, cocktail sort, gnome sort
  — I’m not making these up!

  This challenge gives us a glimpse into the ...'
---

By Dylan Attal

Sorting is a very important concept when writing algorithms. There are all kinds of sorts: bubble sort, shell sort, block sort, comb sort, cocktail sort, gnome sort — [I’m not making these up](https://en.wikipedia.org/wiki/Sorting_algorithm)!

This challenge gives us a glimpse into the wonderful world of sorts. We have to sort an array of numbers from least to greatest and find out where a given number would belong in that array.

#### Algorithm instructions

> Return the lowest index at which a value (second argument) should be inserted into an array (first argument) once it has been sorted. The returned value should be a number.

> For example, `_getIndexToIns([1,2,3,4], 1.5)_` should return `_1_`because it is greater than `_1_` (index 0), but less than `_2_` (index 1).

> Likewise, `_getIndexToIns([20,3,5], 19)_` should return `_2_`because once the array has been sorted it will look like `_[3,5,20]_` and `_19_` is less than `_20_` (index 2) and greater than `_5_` (index 1).

```js
function getIndexToIns(arr, num) {
  return num;
}

getIndexToIns([40, 60], 50);
```

#### Provided Test Cases

* `getIndexToIns([10, 20, 30, 40, 50], 35)` should return `3`.
* `getIndexToIns([10, 20, 30, 40, 50], 35)` should return a number.
* `getIndexToIns([10, 20, 30, 40, 50], 30)` should return `2`.
* `getIndexToIns([10, 20, 30, 40, 50], 30)` should return a number.
* `getIndexToIns([40, 60], 50)` should return `1`.
* `getIndexToIns([40, 60], 50)` should return a number.
* `getIndexToIns([3, 10, 5], 3)` should return `0`.
* `getIndexToIns([3, 10, 5], 3)` should return a number.
* `getIndexToIns([5, 3, 20, 3], 5)` should return `2`.
* `getIndexToIns([5, 3, 20, 3], 5)` should return a number.
* `getIndexToIns([2, 20, 10], 19)` should return `2`.
* `getIndexToIns([2, 20, 10], 19)` should return a number.
* `getIndexToIns([2, 5, 10], 15)` should return `3`.
* `getIndexToIns([2, 5, 10], 15)` should return a number.
* `getIndexToIns([], 1)` should return `0`.
* `getIndexToIns([], 1)` should return a number.

### Solution #1: .sort( ), .indexOf( )

#### PEDAC

**Understanding the Problem**: We have two inputs, an array, and a number. Our goal is to return the index of our input number after it is sorted into the input array.

**Examples/Test Cases**: The good people at freeCodeCamp don’t tell us in which way the input array should be sorted, but the provided test cases make it clear that the input array should be sorted from least to greatest.

Notice that there is an edge case on the last two provided test cases where the input array is an empty array.

**Data Structure**: Since we’re ultimately returning an index, sticking with arrays is going to work for us.

We’re going to utilize a nifty method named `[.indexOf()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)`:

`.indexOf()` returns the first index at which an element is present in an array, or a `-1` if the element is not present at all. For example:

```
let food = ['pizza', 'ice cream', 'chips', 'hot dog', 'cake']
```

```
food.indexOf('chips')// returns 2food.indexOf('spaghetti')// returns -1
```

We’re also going to be using `[.concat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)` here instead of `[.push()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)`. Why? Because when you add an element to an array using `.push()`, it returns the length of the new array. When you add an element to an array using `.concat()`, it returns the new array itself. For example:

```
let array = [4, 10, 20, 37, 45]
```

```
array.push(98)// returns 6array.concat(98)// returns [4, 10, 20, 37, 45, 98]
```

**Algorithm**:

1. Insert `num` into `arr`.
2. Sort `arr` from least to greatest.
3. Return the index of `num`.

**Code**: See below!

```js
function getIndexToIns(arr, num) {
  // Insert num into arr, creating a new array.
     let newArray = arr.concat(num)
  //             [40, 60].concat(50)
  //             [40, 60, 50]

  // Sort the new array from least to greatest.
     newArray.sort((a, b) => a - b)
  // [40, 60, 50].sort((a, b) => a - b)
  // [40, 50, 60]

  // Return the index of num which is now
  // in the correct place in the new array.
     return newArray.indexOf(num);
  // return [40, 50, 60].indexOf(50)
  // 1
}

getIndexToIns([40, 60], 50);
```

Without local variables and comments:

```js
function getIndexToIns(arr, num) {
  return arr.concat(num).sort((a, b) => a - b).indexOf(num);
}

getIndexToIns([40, 60], 50);
```

### Solution #2: .sort( ), .findIndex( )

#### PEDAC

**Understanding the Problem**: We have two inputs, an array, and a number. Our goal is to return the index of our input number after it is sorted into the input array.

**Examples/Test Cases**: The good people at freeCodeCamp don’t tell us in which way the input array should be sorted, but the provided test cases make it clear that the input array should be sorted from least to greatest.

There are two edge cases to take into account with this solution:

1. If the input array is empty then we need to return `0` because `num` would be the _only_ element in that array, therefore at index `0`.
2. If `num` would belong at the very end of `arr` sorted from least to greatest, then we need to return the length of `arr`.

**Data Structure**: Since we’re ultimately returning an index, sticking with arrays is going to work for us.

Let’s checkout `[.findIndex()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)` to see how it’s going to help solve this challenge:

`.findIndex()` returns the index of the first element in the array that satisfies the provided testing function. Otherwise, it returns -1, indicating no element passed the test. For example:

```js
let numbers = [3, 17, 94, 15, 20]
numbers.findIndex((currentNum) => currentNum % 2 == 0)
// returns 2
numbers.findIndex((currentNum) => currentNum > 100)
// returns -1
```

This is useful for us because we can use `.findIndex()` to compare our input `num` to every number in our input `arr` and figure out where it would fit in order from least to greatest.

**Algorithm**:

1. If `arr` is an empty array, return `0`.
2. If `num` belongs at the end of the sorted array, return the length of `arr`.
3. Otherwise, return the index `num` would be if `arr` was sorted from least to greatest.

**Code**: See below!

```js
function getIndexToIns(arr, num) {
  // Sort arr from least to greatest.
    let sortedArray = arr.sort((a, b) => a - b)
  //                  [40, 60].sort((a, b) => a - b)
  //                  [40, 60]

  // Compare num to each number in sortedArray
  // and find the index where num is less than or equal to 
  // a number in sortedArray.
    let index = sortedArray.findIndex((currentNum) => num <= currentNum)
  //            [40, 60].findIndex(40 => 50 <= 40) --> falsy
  //            [40, 60].findIndex(60 => 50 <= 60) --> truthy
  //            returns 1 because num would fit like so [40, 50, 60]

  // Return the correct index of num.
  // If num belongs at the end of sortedArray or if arr is empty 
  // return the length of arr.
    return index === -1 ? arr.length : index
}

getIndexToIns([40, 60], 50);
```

Without local variables and comments:

```js
function getIndexToIns(arr, num) {
  let index = arr.sort((a, b) => a - b).findIndex((currentNum) => num <= currentNum)
  return index === -1 ? arr.length : index
}

getIndexToIns([40, 60], 50);
```

If you have other solutions and/or suggestions, please share in the comments!

#### This article is a part of the series [freeCodeCamp Algorithm Scripting](https://medium.com/@DylanAttal/freecodecamp-algorithm-scripting-b96227b7f837).

#### This article references [freeCodeCamp Basic Algorithm Scripting: Where do I Belong](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/where-do-i-belong).

You can follow me on [Medium](https://medium.com/@DylanAttal), [LinkedIn](https://www.linkedin.com/in/dylanattal/), and [GitHub](https://github.com/DylanAttal)!


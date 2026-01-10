---
title: How to Merge Arrays in JavaScript – Array Concatenation in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-28T15:37:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-merge-arrays-in-javascript-array-concatenation-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/7.-merge-arrays.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  There are multiple ways to merge arrays in JavaScript. You can use long or short
  approaches. I''ll be showing 3 of them in this article.

  When working with arrays in JavaScript, there are cases where you want to combine
  multiple array...'
---

By Dillion Megida

There are multiple ways to merge arrays in JavaScript. You can use long or short approaches. I'll be showing 3 of them in this article.

When working with arrays in JavaScript, there are cases where you want to combine multiple arrays together. For example, arrays with related data coming from different sources can be merged into one single array.

You can merge arrays in different ways. Let's look at some of them, from my favorite to my least favorite.

Here's a [video version](https://youtu.be/YcPHJLc8ZDY) of this article if you'd like to use it to supplement your learning.

## 1. How to Use the Spread Operator in JavaScript

The spread operator allows you to spread an iterable collection (object or array) into another collection. Using this operator on arrays, you can merge the contents of arrays together.

Here's an example:

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]

const merged = [...array1, ...array2]
// [1, 2, 3, 4, 5, 6]
```

For the `merged` variable, we create a new array and then spread the values of `array1` followed by `array2` in it. Now you can see the `merged` array containing the values from these arrays.

You can use this operator for multiple arrays:

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]
const array3 = [7, 8, 9]

const merged = [...array2, ...array3, ...array1]
// [4, 5, 6, 7, 8, 9, 1, 2, 3]
```

In the `merged` array here, we first spread `array2`, then `array3`, and lastly, `array1`.

You can learn more about this operator in this article: [Spread Operator Simplified](https://dillionmegida.com/p/spread-operator-simplified/).

## 2. How to Use `Array.concat` in JavaScript

You use the `concat` method of arrays to combine the contents of an array with new values to form a new array.

These new values can be numbers, strings, booleans, objects, or even, arrays.

The method accepts a list of values as arguments:

```js
array.concat(value1, value2, ..., valueN)
```

By specifying an array as an argument, you can merge an existing array with the specified array to form a new array. Here's an example:

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]

const merged = array1.concat(array2)
// [1, 2, 3, 4, 5, 6]
```

As you can see, the contents of `array1` are concatenated with the contents of `array2` to form a new array assigned to `merged`.

You can pass multiple arrays for merging also:

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]
const array3 = [7, 8, 9]

const merged = array2.concat(array3, array1)
// [4, 5, 6, 7, 8, 9, 1, 2, 3]
```

In this example, we use the `concat` method on `array2` which means the contents of `array2` are first in the merged array. 

For the arguments, we pass `array3` first, which means the contents of `array3` are next in the merged array, then followed by the contents of `array1`.

You can learn more about `concat` in this article: [Array concat simplified](https://dillionmegida.com/p/array-concat/).

## 3. How to Use `Array.push` in JavaScript

The `push` method of arrays allows you to "push" (add) new values to the end of an array.

```js
array.push(value1, value2, ...valueN)
```

Using this method, you can push a new array to an existing array to create a merge process. Unlike the previous approaches I mentioned, the `push` approach modifies the array it is used on.

Here's an example:

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]

for(let i = 0; i < array2.length; i++) {
  array1.push(array2[i])
}

console.log(array1)
// [1, 2, 3, 4, 5, 6]
```

Here, we use a `for` loop to loop through the values of `array2`, and on each loop, we push the value at the index to `array1`.

At the end of the loop, you see `array1` modified, containing the values from `array2`.

Instead of a `for` loop, you can also use the `spread` operator with the `push` method. Since the `push` method accepts a list or arguments separated by a comma, you can spread another array in this method, and they will all be pushed to the array the method is applied to:

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]

array1.push(...array2)

console.log(array1)
// [1, 2, 3, 4, 5, 6]
```

You can do this for multiple arrays:

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]
const array3 = [7, 8, 9]

array3.push(...array2, ...array1)

console.log(array3)
// [7, 8, 9, 4, 5, 6, 1, 2, 3]
```

Here, we call `push` on `array3`, then spread the values of `array2` followed by `array1` as arguments to be pushed into `array3`.

## Wrapping Up

In this article, we've seen three approaches for merging arrays in JavaScript. I especially love the `spread` operator as it's easier and simpler to use.

When using `push`, beware, as I mentioned, that it modifies the array it is used on (unlike `concat` that returns a new array instead). This can cause unexpected results if you do not use it intentionally and carefully.



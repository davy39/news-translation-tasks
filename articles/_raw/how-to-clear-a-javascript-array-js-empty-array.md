---
title: How to Clear a JavaScript Array – JS Empty Array
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-27T15:53:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-clear-a-javascript-array-js-empty-array
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/clear-an-array.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  There are multiple ways to empty an existing array in JavaScript. Emptying an array
  means removing all values from it.

  In this article, I''ll show and explain two ways to clear an array.

  1. How to Clear an Array by Modifying the Leng...'
---

By Dillion Megida

There are multiple ways to empty an existing array in JavaScript. Emptying an array means removing all values from it.

In this article, I'll show and explain two ways to clear an array.

## 1. How to Clear an Array by Modifying the Length Property

The length property of an array is **readable** and **writeable**. 

When you read the property (`array.length`), it returns the length of the array, which is the number of values in it. When you write the property (that is, modify the array, like `array.length = 10`), it changes the length of the array and the number of values in it.

If the modified length is smaller than the original length, excess values will be removed. Here is what I mean:

```js
const array = [1, 2, 3]
array.length = 2

console.log(array)
// [1, 2]
```

Because the new length is smaller than the original, the excess value (**3**, in this case) is removed.

However, if the new length is larger than the original length, the array will be filled with `undefined` values to make up for the new length:

```js
const array = [1, 2, 3]
array.length = 4

console.log(array)
// [1, 2, 3, undefined]
```

Now that you understand how you can use the `length` property to modify an array, here's how to empty an array:

```js
const array = [1, 2, 3]
array.length = 0

console.log(array)
// []
```

With a length of 0, every value in the array gets removed, and the array becomes empty.


## 2. How to Empty an Array by Reassigning Values

You can reassign a new value (an empty array) to a variable that initially has a non-empty array assigned to it.

If you declare a variable with `const`, you cannot reassign it:

```js
const array = [1, 2, 3]
array = []

console.log(array)
```

The above code will throw a **TypeError: Assignment to constant variable** error. But if you declared this variable with `let`, then you can reassign it with an empty array value:

```js
let array = [1, 2, 3]
array = []

console.log(array)
// []
```

Now, you have the empty array.

Thank you for reading, and happy coding!



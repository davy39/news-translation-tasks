---
title: How to Reverse an Array in JavaScript – JS .reverse() Function
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-29T20:12:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-reverse-an-array-in-javascript-js-reverse-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/8.-reverse-array.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  In this article, I''ll show you two ways to reverse arrays in JavaScript.

  The reverse method of arrays reverses an array by making the last item the first,
  and making the first item the last. The other items in between also get rever...'
---

By Dillion Megida

In this article, I'll show you two ways to reverse arrays in JavaScript.

The `reverse` method of arrays reverses an array by making the last item the first, and making the first item the last. The other items in between also get reversed, respectively.

Before showing you examples of the `reverse` method, let me show you how to reverse an array without using it.

I have a [video version](https://youtu.be/HXeUEwWT1F4) of this article you can check out as well.

## 1. How to Reverse an Array Using a `for` Loop

Using a `for` loop (or any other type of loop), we can loop through an array from the last time to the first item, and push those values to a new array which becomes the reversed version. Here's how:

```js
const array = [1, 2, 3, 4]

const reversedArray = []

for(let i = array.length - 1; i >= 0; i--) {
  const valueAtIndex = array[i]
  
  reversedArray.push(valueAtIndex)
}

console.log(reversedArray)
// [4, 3, 2, 1]
```

By using a `for` loop, we start looping from the index of the last value (`array.length - 1`) to the index of the first value (`0`). Then we push the values accordingly to `reversedArray`.

But there's an easier way to reverse an array, which is using the `reverse` method.

## 2. How to Use `Array.reverse` to Reverse an Array

You can use the `reverse` method, which is an easier-to-read/write approach to the `for` loop, to reverse an array. This method reverses the array in place, which means that the array it is used on is modified.

Let's see an example:

```js
const array = [1, 2, 3, 4]

array.reverse()

console.log(array)
// [ 4, 3, 2, 1 ]
```

As you can see in this example, the `array` is modified when the `reverse` method is applied to it.

If you do not want the `array` to be modified, you can clone it before applying the `reverse`. The `reverse` method also returns the reversed array, so you can assign that array to a variable.

Here's how to duplicate and reverse an array:

```js
const array = [1, 2, 3, 4]

const reversed = [...array].reverse()

console.log(reversed)
// [ 4, 3, 2, 1 ]

console.log(array)
// [ 1, 2, 3, 4 ]
```

Using the [spread operator](https://dillionmegida.com/p/spread-operator-simplified/) here, we first clone the `array`, then apply the `reverse` method on the clone. The returned reverse array is then returned to the `reverse` variable.

As you can see, by logging `array`, it is not affected because we cloned it first.

## Thanks for reading!

So if you ever need to reverse an array, I hope this article has taught you something.



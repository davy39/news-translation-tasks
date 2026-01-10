---
title: How to Use the flat() and flatMap() Methods to Flatten Arrays in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-26T16:47:22.000Z'
originalURL: https://freecodecamp.org/news/flat-and-flatmap-javascript-array-methods
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/js-map-2.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Kenechukwu Nwobodo

  In this article I''m going to explain how to use the new array methods introduced
  in ES2019 (EcmaScript 2019) – flat() and flatMap(). You use these methods to flatten
  arrays.

  The methods are very useful and easy to use. It will r...'
---

By Kenechukwu Nwobodo

In this article I'm going to explain how to use the new array methods introduced in ES2019 (EcmaScript 2019) – `flat()` and `flatMap()`. You use these methods to flatten arrays.

The methods are very useful and easy to use. It will really be cool to use these methods in your next project. Grab a coffee and let's dive into it.

## Prerequisites

You should be familiar with the concept of arrays in JavaScript to follow along with this tutorial.

## What is an Array?

The array object is a data structure used in different programming languages for storing different collections of data.

### Example of an array in JavaScript 

```javascript
const array = [1, 2, 3, true, null, undefined];

console.log(array);

// expected output
1, 2, 3, true, null, undefined
```

In the code above, we assigned a variable named **`arr`** and stored different elements/data of different data types in it.

The first element which is 1 is at index 0. The last element, undefined, is at index 5.

Don't forget that array objects are zero indexed, which means that the first element starts at an index of zero.

## Characteristics of JavaScript Arrays

* **Arrays are zero indexed:** This simply means that the first element in an array is at index 0. Index here means position. In JavaScript and likewise in other programming languages, the right word to use is index and not position.
* **JavaScript arrays can contain different data types:** This means that JavaScript arrays can contain a mix of numbers, strings, booleans, null values, and so on.
* **JavaScript creates shallow copies**: This means that the original array and the copy point to the same reference  – modifying the copy can alter the original array.

## New JavaScript Array Methods

Arrays are one of the most popular data structures in JavaScript used for storing data.

There are different array methods you can use to simplify operations and make your life easier. A few of those methods include `reduce()`, `filter()`, `map()`, `flat()`, `flatMap()`, and many more.

But in this article we won't discuss all the array methods used in JavaScript. Rather here, we'll discuss the new `flat()` and `flatMap()` methods you can use to convert an original array into a new array.

## How to Use the `flat` Array Method in JavaScript

You use the `flat` method to convert an original array into a new array. It does this by collecting and concatenating the sub-arrays in an array into a single array.

An important note about this array method is that you can compute the original into another array based on the depth of the array. This method is really useful because it makes computing the operations of an array much easier.

## Examples of `flat()` array method

### How to set the depth paramater‌

```js
array.flat(depth);
```

The depth value is 1 by default and you can leave it empty. The depth value takes a number as its data type.

#### `flat()` array method example 1

`array.flat(1)` is equal to `array.flat()`.

`array.flat(2);`

The depth above is **2**.

```javascript
const arr = ["mon", "tues", ["wed", "thurs", ["fri", "sat"]], "sun"] ;

console.log(arr.flat());

// expected output 
["mon", "tues", "wed", "thurs", Array ["fri", "sat"], "sun"];
```

So what's happening in this code?

First, the array contains two sub-arrays which are `["wed", "thurs", ["fri", "sat"]]`.

We use the **flat()** method on the array named **`arr`** to concatenate the first sub array because we did not specify any depth value inside the **flat()** method. Recall that the default depth value is **1**.

So you can guess what the array object would be if the the depth value was 2, right?‌

#### `flat()` array method example 2

```javascript
const arr = [1, 2, [3, 4, 5], 6, 7];

console.log(arr.flat());

// expected output 
[1, 2, 3, 4, 5, 6, 7]
```

In the code above, the array contains a sub-array which is `[3, 4, 5]`.

We use the **flat()** method on the array named **`arr`** to concatenate the two arrays together into a single array.

#### `flat()` array method example 3

```javascript
//depth 2 example 
const arr2 = [[[1, 2], 3, 4, 5]] ;

console.log(arr2.flat(2));

// expected output 
[1, 2, 3, 4, 5]
```

In the above code, the array named **`arr2`** contains two sub-arrays.

We use the **flat()** method on `arr2` to concatenate the two arrays into a single array because of the depth value 2 used inside the flat(2) method. Take a quick look above to see what the depth value does.‌

The array method is a nice way of concatenating elements in an array recursively.

## How to Use the `flatMap` Array Method in JavaScript

The `flatMap()` method uses a combination of the `map()` and `flat()` methods to perform operations.

The `flatMap()` loops through the elements of an array and concatenates the elements into one level. `flatMap()` takes in a callback function which takes in the current element of the original array as a parameter.

### `flatMap()` array method example

```javascript
const arr3 = [1, 2, [4, 5], 6, 7, [8]] ;

console.log(arr3.flatMap((element) => element)); 

// expected output 
[1, 2, 4, 5, 6, 7, 8]
```

In the above code, the array named **`arr3`** contains two distinct sub-arrays.

We used the **flatMap()** method on the array by passing in a call-back function, **(element) => element** which loops through the array and then concatenates the arrays into a single array.

Sometimes you'll have a situation where you have more than one depth of an array and you decide to change the new array into a one base level. Then you will have to use the `flat()` method immediately after the `flatMap()` method.

### Here's an example:

```javascript
const arr4 = [1, 2, [3, [4, 5, [6, 7]]]] ;

console.log(arr4.flatMap((element) => element).flat(2)) ;

// expected output 
[1, 2, 3, 4, 5, 6, 7]

```

In the above code, the array named **`arr4`** contains three sub-arrays.

We used the **flatMap()** method on the array by passing in a call-back function, **(element) => element** which loops through the array and then concatenates the arrays.

We used the **flat(2)** method to further concatenate the array into a single array by passing in a depth of **2**.

Make sure to practice the above example without passing the flat(2) method and see the difference.

This is all you need to get started with these two new array methods.

## Summary

In this article, I briefly discussed what arrays are and how useful they are in JavaScript. Then we learned about the two new important array methods which were introduced in ECMAScript 2019 that let you change an original array into a new array.

These new array methods are the `flat()` and `flatMap()` methods.

You use the `flat()` method for concatenating sub-arrays recursively into a single array. The `flat()` method takes a depth value as its parameter which is optional depending on the depth of the array you wish to flatten (concatenate). The `flat()` method takes in 1 as a depth by default.

On the other hand, `flatMap()` works basically the same expect that it is a combination of the `map()` and `flat()` methods together. `flatMap()` loops through the elements in the array and concatenates the elements.

Both new methods are useful when you're changing an original array into a new array. They're worth trying out in your next big or small project.

### Other helpful resources:

* [MDN reference on flatMap()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
* [MDN reference on flat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)()


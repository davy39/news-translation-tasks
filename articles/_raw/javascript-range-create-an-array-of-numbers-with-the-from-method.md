---
title: JavaScript Range – How to Create an Array of Numbers with .from() in JS ES6
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-12-14T21:15:06.000Z'
originalURL: https://freecodecamp.org/news/javascript-range-create-an-array-of-numbers-with-the-from-method
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-template--1-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'The .from() method is a static method of the Array object in JavaScript
  ES6. It creates a new, shallow-copied Array instance from an array-like or iterable
  object like map and set.

  This method returns an array from any object with a length property. ...'
---

The `.from()` method is a static method of the `Array` object in JavaScript ES6. It creates a new, shallow-copied Array instance from an array-like or iterable object like `map` and `set`.

This method returns an array from any object with a length property. You can use it to create an Array of numbers within a specified range.

In this article, you will learn what the `.from()` static method is all about, how it works, and how you can create a range of numbers in JavaScript.

In case you are in a rush, here is a method to help you get the range:

```js
const arrayRange = (start, stop, step) =>
    Array.from(
    { length: (stop - start) / step + 1 },
    (value, index) => start + index * step
    );

console.log(arrayRange(1, 5, 1)); // [1,2,3,4,5]
```

You can continue reading this short article to understand how it works.

## How the `.from()` Method Works in JavaScript

The `Array.from()` method returns an array from any array-like or iterable object. The method takes in one compulsory parameter and two other optional parameters:

```js
// Syntax
Array.from(arraylike, mapFunc, thisArg)
```

* `arraylike` - An Array-like or iterable object to convert to an array.
    
* `mapFunc` - This is an optional parameter. The Map function is called on each element.
    
* `thisArg` - This value is used when executing `mapFunc` as `this`. It is also optional.
    

To see how this works, let’s create an array from a string using the `Array.from()` method:

```js
let newArray = Array.from("freeCodeCamp");

console.log(newArray); // ["f","r","e","e","C","o","d","e","C","a","m","p"]
```

In the example above, the `Array.from()` method returned an array of the string. You can also use the method to return an array from any object with a length property that specifies the number of elements in the object.

```js
let arrayLike = {0: 1, 1: 2, 2: 3, length: 3};
let newArray = Array.from(arrayLike);

console.log(newArray); // [1,2,3]
```

You can also introduce the map function that gets called for each element. For example, if you want to manipulate each array item by maybe multiplying each with a specific number:

```js
let arrayLike = {0: 1, 1: 2, 2: 3, length: 3};
let newArray = Array.from(arrayLike, x => x * 2);

console.log(newArray); // [2,4,6]
```

**Note:** `.from()` is a static method, which is why it uses the `Array` class name. You can only use it as `Array.from()` and not `myArray.from()`, where `myArray` is an array. It will return undefined.

## How to Create a Sequence of Numbers with the `.from()` Method

The `Array.from()` method makes it possible for you to create a sequence of numbers using the map function:

```js
let newArray = Array.from({ length: 7 }, (value, index) => index);

console.log(newArray); // [0,1,2,3,4,5,6]
```

The above method creates an array of 7 elements which are by default initialized with `undefined`. But using the map function, the index value is now used instead of its actual value of undefined.

If you use its actual value, you will get an array of 7 elements (based on the length) with the value of undefined:

```js
let newArray = Array.from({ length: 7 }, (value, index) => value);

console.log(newArray); 
// returns [undefined,undefined,undefined,undefined,undefined,undefined,undefined]
```

## How to Create a Range of Numbers with the `.from` Method

You now know how to create an array with a sequence of numbers. But when you create a range, you want these numbers to start from a specified value and end at a specified value. For example, numbers within the range of 4 and 8 would be 4, 5, 6, 7, 8.

You can also specify if you want an array of odd or even numbers within a specified range. All these can be achieved with the `Array.from()` method.

```js
const arrayRange = (start, stop, step) =>
    Array.from(
    { length: (stop - start) / step + 1 },
    (value, index) => start + index * step
    );
```

In the above code, the length of the array-like object is defined by subtracting the last number from the first number in the range and dividing by the step plus one. This will give the exact number of elements in the array.

In the map function, the start number is added to the index of each element (remember, the value is always undefined) and multiplied by the step value. This map function runs for each element and helps calculate the value of each element.

Let’s try the method with a few examples:

```js
// Generate numbers between range 2 and 7
let range = arrayRange(2, 7, 1);
console.log(range); // [2,3,4,5,6,7]

// Generate even numbers between range 2 and 7
let evenRange = arrayRange(2, 7, 2);
console.log(evenRange); // [2,4,6]

// Generate odd numbers between range 1 and 5
let oddRange = arrayRange(1, 5, 2);
console.log(oddRange); // [1,3,5]
```

## Wrapping Up

In this article, you have learned how to create an array of numbers with the `Array.from()` method. You have also learned how the `Array.from()` method works.

Keep in mind that there are other options to create a range of numbers in JavaScript – we just focused on `.from()` in this tutorial.

Have fun coding!

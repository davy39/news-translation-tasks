---
title: JavaScript Array Length Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-12T17:56:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-length
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9df3740569d1a4ca3a91.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'length is a property of arrays in JavaScript that returns or sets the number
  of elements in a given array.

  The length property of an array can be returned like so.

  let desserts = ["Cake", "Pie", "Brownies"];

  console.log(desserts.length); // 3


  The as...'
---

`length` is a property of arrays in JavaScript that returns or sets the number of elements in a given array.

The `length` property of an array can be returned like so.

```js
let desserts = ["Cake", "Pie", "Brownies"];
console.log(desserts.length); // 3
```

The assignment operator, in conjunction with the `length` property, can be used to set the number of elements in an array like so.

```js
let cars = ["Saab", "BMW", "Volvo"];
cars.length = 2;
console.log(cars.length); // 2
```

## More info about arrays:

### isArray() method

The `Array.isArray()` method returns `true` if an object is an array, `false` if it is not.

**Syntax:**

```text
Array.isArray(obj)
```

**Parameters:**

**obj** The object to be checked.

[MDN link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray) | [MSDN link](https://msdn.microsoft.com/en-us/LIBRary/ff848265%28v=vs.94%29.aspx)

**Examples:**

```text
// all following calls return true
Array.isArray([]);
Array.isArray([1]);
Array.isArray(new Array());
// Little known fact: Array.prototype itself is an array:
Array.isArray(Array.prototype); 

// all following calls return false
Array.isArray();
Array.isArray({});
Array.isArray(null);
Array.isArray(undefined);
Array.isArray(17);
Array.isArray('Array');
Array.isArray(true);
Array.isArray(false);
Array.isArray({ __proto__: Array.prototype });
```

### Array.prototype.forEach

The ‘forEach’ array method is used to iterate through each item in an array. The method is called on the array Object and is passed a function that is called on each item in the array.

```javascript
var arr = [1, 2, 3, 4, 5];

arr.forEach(number => console.log(number * 2));

// 2
// 4
// 6
// 8
// 10
```

The callback function can also take a second parameter of an index in case you need to reference the index of the current item in the array.

```javascript
var arr = [1, 2, 3, 4, 5];

arr.forEach((number, i) => console.log(`${number} is at index ${i}`));

// '1 is at index 0'
// '2 is at index 1'
// '3 is at index 2'
// '4 is at index 3'
// '5 is at index 4'
```

## Further reading about arrays:

[array.prototype.filter](https://guide.freecodecamp.org/javascript/standard-objects/array/array-prototype-filter/)

[array.prototype.reduce](https://guide.freecodecamp.org/javascript/standard-objects/array/array-prototype-reduce/)


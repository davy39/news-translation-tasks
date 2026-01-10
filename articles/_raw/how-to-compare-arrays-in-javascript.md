---
title: Comparing Arrays in JavaScript – How to Compare 2 Arrays in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-16T00:15:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-compare-arrays-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When handling logic with JavaScript, you might need to compare two arrays
  to see if they are equal or not.

  Really, this shouldn''t be difficult, as you''d think we could easily use either
  the loose equality (double equals - ==) or the strict equality (...'
---

When handling logic with JavaScript, you might need to compare two arrays to see if they are equal or not.

Really, this shouldn't be difficult, as you'd think we could easily use either the loose equality (double equals - `==`) or the strict equality (triple equals - `===`). But unfortunately, you cannot use them in this case.

```js
let array1 = [11, 22, 33];
let array2 = [11, 22, 33];

console.log(array1 == array2); //false
console.log(array1 === array2); //false
```

This happens because JavaScript arrays have a type of Object:

```js
let arrayType = typeof(array1);
console.log(arrayType); //"Object"
```

Objects are not compared based on their values but based on the references of the variables:

```js
console.log(array1[0] == array1[0]); //true
console.log(array1[1] === array1[1]); //true
```

But this is not what you want. Instead, you want to be able to compare both arrays directly and return just one boolean value without having to check each element one by one.

In this article, you will learn the various ways you can compare two arrays in JavaScript to see if they are similar or not.

## How to Compare Two Arrays by Converting to Strings

A common and quite straightforward approach you can use to compare two arrays is first to convert these arrays to string form.

There are two different methods that you can use: you can decide to convert your array to JSON text using the `JSON.stringify()` method, or you can use the `.toString()` method to return your array as a string.

**Note:** Both methods are different, as you can see below:

```js
let array = [11, 22, 33];
console.log(JSON.stringify(array)); //"[11,22,33]"
console.log(array.toString()); //"11,22,33"
```

### Method 1: How to use `JSON.stringify()`

This method allows you to serialize each array by converting the array to a JSON string. You can then compare the two JSON strings.

```js
let array1 = [11, 22, 33];
let array2 = [11, 22, 33];

console.log(JSON.stringify(array1) === JSON.stringify(array2)); //true
```

We can also decide to create a reusable function that helps us compare any two arrays we pass into it:

```js
const compareArrays = (a, b) => {
  return JSON.stringify(a) === JSON.stringify(b);
};

let array1 = [11, 22, 33];
let array2 = [21, 22, 23];
let array3 = [11, 22, 33];

console.log(compareArrays(array1, array2)); //false
console.log(compareArrays(array1, array3)); //true
```

### Method 2: How to use `.toString()`

Similar to `JSON.stringify()`, this method converts any data type to a string and can similarly convert an object to a string.

```js
let array1 = [11, 22, 33];
let array2 = [11, 22, 33];

console.log(array1.toString() === array2.toString()); //true
```

You can also decide to create a reusable function that helps you compare any two arrays you pass into it:

```js
const compareArrays = (a, b) => {
  return a.toString() === b.toString();
};

let array1 = [11, 22, 33];
let array2 = [21, 22, 23];
let array3 = [11, 22, 33];

console.log(compareArrays(array1, array2)); //false
console.log(compareArrays(array1, array3)); //true
```

**Note:** You should use the `JSON.stringify()` method, as it only serializes your JavaScript array. The array still takes the shape of an array, but it’s only parsed to become the string version of the array.

## How to Compare Two Arrays by Lopping Through Their Values

The methods above fall short in some scenarios. For example, when one array has a value of `null` and another has a value of `undefined`, when we use the strict comparison, we get `false` by default – which is correct:

```js
console.log(null === undefined); //false
```

But when we use the `JSON.Strigify()` or `.toString()` methods you get `true`, which shouldn't be the case:

```js
let array1 = [11, null, 33];
let array2 = [11, undefined, 33];

console.log(JSON.stringify(array1) === JSON.stringify(array2)); //true
console.log(array1.toString() === array2.toString()); //true
```

A better approach would be to compare the array’s length and then loop through and compare each element of the array.

### Method 1: using `every()`

The `every()` method helps you execute a function for each element of your array. This function is referred to as the call back function. It has access to some basic parameters like the element, index, and lots more, which we can use within the function:

```js
// Syntax
array.every((currentValue, index, arr)=> { ... })
```

In this method, we'll first test if the lengths of the two arrays are comparable. Then we'll loop through one array and using its index to compare its elements to those in the second array:

```js
const compareArrays = (a, b) =>
  a.length === b.length &&
  a.every((element, index) => element === b[index]);

let array1 = [11, 22, 33];
let array2 = [21, 22, 23];
let array3 = [11, 22, 33];

console.log(compareArrays(array1, array2)); //false
console.log(compareArrays(array1, array3)); //true
```

And when we have null and undefined as part of our Array elements, it will be able to detect that they are not the same:

```js
const compareArrays = (a, b) =>
  a.length === b.length && a.every((element, index) => element === b[index]);

let array1 = [11, null, 33];
let array2 = [21, 22, 23];
let array3 = [11, undefined, 33];

console.log(compareArrays(array1, array2)); //false
console.log(compareArrays(array1, array3)); //false
```

### Method 2: using a for loop

The every() method has a better syntax. Still, another way we can implement the method is to use other iteration methods like the `for` loop, `forEach()` or `map()` alongside `if` statements. These can be easier for a newbie to grasp.

```js
const compareArrays = (a, b) => {
  if (a.length !== b.length) return false;
  else {
    // Comparing each element of your array
    for (var i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) {
        return false;
      }
    }
    return true;
  }
};

let array1 = [21, null, 33];
let array2 = [21, 22, 23];
let array3 = [21, undefined, 33];
let array4 = [21, 22, 23];

console.log(compareArrays(array1, array2)); //false
console.log(compareArrays(array1, array3)); //false
console.log(compareArrays(array2, array4)); //true
```

In both methods above, you will first check for the length, because if the length is not equal, it automatically means both arrays are not equal and then returns `false`.

If the length is equal, then we begin to check each element. It returns `false` as soon as two elements on the same `index` in both arrays are different.

## Wrapping Up

This article taught you how to compare two arrays in JavaScript using two major approaches.

These approaches are to convert the array to a string before comparing them, or you can loop through to check if their values are similar to each other for a more detailed comparison.

**Note:** The double equals checks if both values are equal, while the triple equals checks if both values and their data types are equal. You can read more about [both types of equality here](https://www.freecodecamp.org/news/javascript-triple-equals-sign-vs-double-equals-sign-comparison-operators-explained-with-examples/).

Have fun coding!

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.

---
title: How to Swap Two Array Elements in JavaScript – Switch Elements in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-29T20:15:18.000Z'
originalURL: https://freecodecamp.org/news/swap-two-array-elements-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--11-.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When you''re working with arrays, there are times when you need to swap
  two elements in an array in JavaScript.

  Maybe you''re working on an algorithm question such as the bubble sort algorithm
  where you need to compare two values and then swap them if ...'
---

When you're working with arrays, there are times when you need to swap two elements in an array in JavaScript.

Maybe you're working on an algorithm question such as the bubble sort algorithm where you need to compare two values and then swap them if your condition is true.

Aside from that, many other situations may require you to swap array elements.

In case you don’t already understand what I mean by "swapping", here is an example. Suppose you have an array of numbers and you want to swap the element at index `1` which is **\-2** with the element at index `0` which is **12**, as seen in the image below:

![](https://paper-attachments.dropbox.com/s_B08002E277AA9EEDFC6B2A9D153D5485AA9F9B4567270177E695FBE6032A1880_1664460747763_Untitled.drawio+14.png align="left")

Implementing this in JavaScript can get confusing if you are not already familiar with how JS does these types of things. You may also be searching for better ways to handle this.

This article will teach you three approaches: using a temporary variable, destructuring, and the using the `splice()` array method.

## How to Swap Two Array Elements With a Temporary Variable

To swap elements, you can use a temporary variable and go through three steps.

The first step is to create a temporary variable to hold the first element's value. The second step is to set the value of the first element to the value of the second element. The third step is to set the value of the second element to the value in the temporary variable.

```js
let myArray = [12, -2, 55, 68, 80];

const temp = myArray[0];
myArray[0] = myArray[1];
myArray[1] = temp;

console.log(myArray); // [-2,12,55,68,80]
```

You can also create a reusable function to handle this whereby you specify the array and the two indexes you wish to swap.

```js
const swapElements = (array, index1, index2) => {
    let temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
};

let myArray = [12, -2, 55, 68, 80];
swapElements(myArray, 0, 1);
console.log(myArray); // [-2,12,55,68,80]
```

## How to Swap Two Array Elements by Destructuring

A far better method you can use to swap array elements is destructuring, as it does the job in only one line of code.

You just create a new array containing both elements in a particular order, then assign it to a new array that contains both elements in the reversed order.

```js
let myArray = [12, -2, 55, 68, 80];

[myArray[0], myArray[1]] = [myArray[1], myArray[0]];

console.log(myArray); // [-2,12,55,68,80]
```

You can also create a reusable function to handle this whereby you specify the array and the two indexes you wish to swap.

```js
const swapElements = (array, index1, index2) => {
    [myArray[index1], myArray[index2]] = [myArray[index2], myArray[index1]];
};

let myArray = [12, -2, 55, 68, 80];
swapElements(myArray, 0, 1);
console.log(myArray); // [-2,12,55,68,80]
```

## How to Swap Two Array Elements With the `Splice()` Method

Finally, you can use the `splice()` array method. You can use this method to remove one or more element(s) from an array and replace the element(s) with any specified element.

```js
// Syntax
array.splice(index, howmany, element1, ....., elementX)
```

For example, if you have an array and want to remove a particular element, you will specify its id and the number of elements you want to remove. In our case, it’s just one.

```js
let myArray = [12, -2, 55, 68, 80];

myArray.splice(1, 1);
console.log(myArray); // 12,55,68,80]
```

Also, if you want to replace the removed element with another, your code will look like this:

```js
let myArray = [12, -2, 55, 68, 80];

myArray.splice(1, 1, 32);
console.log(myArray); // [12,32,55,68,80]
```

But if you want to swap two elements, you will have something like this:

```js
let myArray = [12, -2, 55, 68, 80];

myArray[0] = myArray.splice(1, 1, myArray[0])[0];

console.log(myArray); // [-2,12,55,68,80]
```

You can also create a reusable function to handle this whereby you specify the array and the two indexes you wish to swap:

```js
const swapElements = (array, index1, index2) => {
    array[index1] = array.splice(index2, 1, array[index1])[0];
};

let myArray = [12, -2, 55, 68, 80];
swapElements(myArray, 0, 1);
console.log(myArray); // [-2,12,55,68,80]
```

## Wrapping Up

In this article, you have learned three methods to swap an array's elements in JavaScript.

You can use any method, but it's best to use the ES6 destructuring method as it is far easier for everyone to understand and use.

Have fun coding!

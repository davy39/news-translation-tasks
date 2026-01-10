---
title: JavaScript Reverse Array – Tutorial With Example JS Code
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-01-18T18:02:07.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-reverse-tutorial-with-example-js-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/js-reverse.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Reversing an array with certain restrictions is one of the most common\
  \ challenges you will find in job interviews and coding quizzes. \nThis tutorial\
  \ will show you five ways to reverse an array in JavaScript with and without the\
  \ reverse method, along ..."
---

Reversing an array with certain restrictions is one of the most common challenges you will find in job interviews and coding quizzes. 

This tutorial will show you **five** ways to reverse an array in JavaScript with and without the `reverse` method, along with code snippets that you can use.

## How to Reverse an Array in JavaScript with the Reverse Method

When you need to reverse an array in JavaScript, you can use the `reverse` method, which will put the last element first and the first element last:

```js
let numbers = [1, 2, 3, 4, 5];
let reversedNumbers = numbers.reverse();

console.log(reversedNumbers);
// [5, 4, 3, 2, 1]
```

But keep in mind that the `reverse` method will also modify the original array:

```js
let numbers = [1, 2, 3, 4, 5];
let reversedNumbers = numbers.reverse();

console.log(reversedNumbers);
// [5, 4, 3, 2, 1]

console.log(numbers);
// [5, 4, 3, 2, 1]
```

Some coding challenges may want you to preserve the original array, so let's look at how you can reverse an array without changing the original.

## How to Reverse an Array in JavaScript with the Spread Operator

You can use a combination of the [spread operator](https://sebhastian.com/javascript-spread-operator/) and the `reverse` method to reverse an array without changing the original. 

First, you put the elements returned from the spread operator into a new array by enclosing the spread syntax with square brackets `[]`:

```js
[...numbers]
```

Then, you call the `reverse` method on the array. This way, the `reverse` method will be executed on the new array instead of the original:

```js
let numbers = [1, 2, 3, 4, 5];
let reversedNumbers = [...numbers].reverse();

console.log(reversedNumbers);
// [5, 4, 3, 2, 1]

console.log(numbers);
// [1, 2, 3, 4, 5]
```

Note: the `spread` method is ES6 syntax. When you need to support older browsers or you want to use ES5 syntax, you can combine the `slice` and `reverse` methods. Let's look at that now.

## How to Reverse an Array in JavaScript with the Slice and Reverse Methods 

[The `slice` method](https://sebhastian.com/javascript-array-slice/) is used to return the selected elements as a new array. When you call the method without any argument, it will return a new array that's identical to the original (from the first element to the last).

Next, you call the `reverse` method on the newly returned array. This is why the original array is not reversed:

```js
let numbers = [1, 2, 3, 4, 5];
let reversedNumbers = numbers.slice().reverse();

console.log(reversedNumbers);
// [5, 4, 3, 2, 1]

console.log(numbers);
// [1, 2, 3, 4, 5]
```

## How to Reverse an Array in JavaScript Without the Reverse Method

Sometimes a job interview will challenge you to reverse an array without the `reverse` method. No problem! You can use the combination of [a `for` loop](https://sebhastian.com/javascript-for-loop/) and an array `push` method like in the example below:

```js
let numbers = [1, 2, 3, 4, 5];
let reversedNumbers = [];

for(let i = numbers.length -1; i >= 0; i--) {
  reversedNumbers.push(numbers[i]);
}

console.log(reversedNumbers);
```

## How to Write your Own Reverse Function in JS

Finally, let's say you're tasked with writing your own reverse function that needs to reverse an array without creating a copy. This might seem complicated at first, but don't worry because it's actually quite easy.

What you need to do here is to swap the first and last elements of the array, then the second and second-to-last elements, and so on until you've swapped all the elements.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/js-array-reverse-function-1.png)
_A function to reverse an array_

Let's write a function to do just that.

Write the function `customReverse` and store both the first index at `0` and the last index using `array.length - 1` as variables. 

```js
function customReverse(originalArray) {

  let leftIndex = 0;
  let rightIndex = originalArray.length - 1;
}
```

Next, create [a `while` loop](https://sebhastian.com/javascript-while-loop/) that runs as long as the `leftIndex` is smaller than the `rightIndex`. 

Inside this loop, swap the value of the `leftIndex` and the `rightIndex`. You can temporary store one of the values in a temporary variable:

```js
while (leftIndex < rightIndex) {

  // Swap the elements
  let temp = originalArray[leftIndex];
  originalArray[leftIndex] = originalArray[rightIndex];
  originalArray[rightIndex] = temp;
}
```

Finally, move the `leftIndex` up and the `rightIndex` down. When the `while` loop repeats, it will swap the second and second-to-last elements, and so on:

```js
  function customReverse(originalArray) {

  let leftIndex = 0;
  let rightIndex = originalArray.length - 1;

  while (leftIndex < rightIndex) {

    // Swap the elements with temp variable
    let temp = originalArray[leftIndex];
    originalArray[leftIndex] = originalArray[rightIndex];
    originalArray[rightIndex] = temp;

    // Move indices to the middle
    leftIndex++;
    rightIndex--;
  }
}
```

The loop will stop right when there are no more elements to reverse. For odd-sized arrays, the value of `leftIndex` and `rightIndex` will be equal, so no more swapping. For even-sized, the `leftIndex` will be greater than the `rightIndex`.

You can test the function to see if it works properly like this:

```js
let myArray = [1, 2, 3, 4, 5];

customReverse(myArray);

console.log(myArray);

// output is [5, 4, 3, 2, 1]
```

## Conclusion

Congratulations! You've learned not only how to reverse an array in JavaScript, but also how to write your own reverse function.

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!


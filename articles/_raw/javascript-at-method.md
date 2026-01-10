---
title: How to Use the JavaScript at() Array Method
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2023-08-21T14:41:05.000Z'
originalURL: https://freecodecamp.org/news/javascript-at-method
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Grey-Minimalist-Tips-Blog-Banner.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'One of JavaScript''s most exciting new features is the at() method. The
  at() method is a new addition to the Array prototype in JavaScript. You can use
  this method to access elements in an array using a numeric index.

  The at() method takes an integer ...'
---

One of JavaScript's most exciting new features is the `at()` method. The `at()` method is a new addition to the `Array` prototype in JavaScript. You can use this method to access elements in an array using a numeric index.

The `at()` method takes an integer value and returns the item at that index. The value can be either a positive or negative integer. Negative integers count back from the last item in the array.

## Syntax of the `at()` Method

Here's the syntax – it's pretty simple:

```javascript
arr.at(index)

```

## How JavaScript's `at()` Method Works

How does this method work, you might ask? The `at()` method takes a single parameter, which is the index of the element to be accessed.

The index should be a positive or negative integer value. Negative integers will count backward from the last item in the array, and positive integers will count forward from the start of the array.

 For example, given the following array:

```javascript
const rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple'];

```

To access the first element in the array (remember that arrays in JS are zero-indexed), you can do this:

```javascript
const color = rainbow.at(0); // red

```

To access the last element in the array, you'd do this:

```javascript
const lastColor = rainbow.at(-1); // purple

```

In the example above, the `-1` index is treated as an index relative to the end of the array, and will point to the last element in the array.

### What is relative indexing?

Relative indexing is a technique used to index elements or values by their position in relation to a reference point or another element. 

Rather than relying on fixed numerical indices that assign specific positions to elements, relative indexing enables you to indicate positions based on the relationship with other elements, adapting dynamically. Relative indexing has become a much easier solution with `at()`.

### Example Use Case

Arrays are used to store collections of data. Developers often need to retrieve specific elements from an array to use their values to display information. When processing data, you might want to modify, transform, or perform calculations on specific data points in an array.

Let's consider a real-world example where the `at()` method could be useful. Imagine you are building a weather app that displays the forecast for the upcoming week. You have an array containing the weekly temperatures:

```javascript
const temperatureForecast = [70, 71, 75, 80, 77, 88, 90];

```

The first item in the array is the temperature for today and it's followed by the next 6 days. You want to display the upcoming temperature for tomorrow. To access the temperature for tomorrow, you'd want to get the value at an index of 1.

Here's how you can use `at()` to access the temperature:

```javascript
const temperatureForecast = [70, 71, 75, 80, 77, 88, 90];

const tomorrowsTemperature = temperatureForecast.at(1);

console.log(`The high for tomorrow is ${tomorrowsTemperature}°F.`); 
// The high for tomorrow is 71°F.
```

When presenting data to users, there are many scenarios where you want to display the most recent or latest item from an array. This is common in news feeds, chat applications, or activity logs.

### Try it out:

I encourage you to play around with this method to learn by doing. I've created a CodePen playground. Change the values in the array and the values passed into `at()` , try to see if you can guess the result:

%[https://codepen.io/nataliepina/pen/RwedQNj?editors=1010]

## Problems the `at()` Method Solves

Prior to its introduction, to access array elements by their index, you had to perform manual calculations.

It has been a common practice to use an array's `length` property to calculate the number of items in the array, and then to subtract from the length to target an index. For example, to access the last element of an array, you can use `array[array.length - 1]`.

### `slice()` vs the `length` property vs `at()`

Let's look at a comparison between three different methods that let us access items in an array. Notice the amount of code required for each, the readability of the code, and the complexity between the methods.

```javascript
const animals = ["panda", "zebra", "penguin"];

// with slice()
const animal = animals.slice(-2, -1); // 'zebra'

// with the length property
const animal = animals[animals.length - 2]; // 'zebra'

// with at()
const animal = animals.at(-2); // 'zebra'
```

Using the `at()` method, accessing the last element of an array is as simple as `array.at(-1)` . This method provides a far more readable and intuitive solution.

Readability is enhanced with `at()` method's syntax, because it's intention is well described with the word "at". For example, `array.at(0)` can be read as "the array **at** the index of zero". 

In contrast, an alternative like `array.slice(0, 1)` lacks the same clarity. Improved readability reduces cognitive load and makes code easier to understand at a glance.

Additionally, adopting the `at()` method aligns well with other array methods like `map()` and `filter()`, fostering a cohesive and functional programming-oriented coding style throughout your code.

The `at()` method mitigates risk by providing a straightforward way to access elements. With `at()`, it is less likely to make indexing mistakes or off-by-one errors that commonly arise when working with numerical indices. The method's clear syntax reduces the likelihood of introducing bugs related to index manipulation.

The `at()` method performs bounds checking automatically, meaning it ensures that the index is within the valid range for the array. The `length` method does not offer any bounds checking. With bounds checking if an out-of-range index is provided, the method will return `undefined` without throwing an error.

Performing manual checks with `length` tend to be error-prone, and more difficult to debug. While manual indexing allows you to access elements, it requires a longer code sequence to do so. 

The need to calculate indices, perform subtraction, and handle edge cases adds extra characters and complexity to your code. This approach can introduce subtle errors can be challenging to identify and fix.

For accessing a single element, using `.slice()` introduces unnecessary complexity. The method requires specifying both the start and end indices, which is inconvenient when you only need one element. 

The use of `array.slice()` is best for scenarios where you want to retrieve a range of elements. If you only need a single element, using array indexing directly is more efficient.

While `slice()` and `length` have their uses, the `at()` method provides a compelling solution for array element access.

## Browser Support for `at()`

Because this method is new, it is not supported by all browsers just yet. Currently, it is supported by all major browsers like Chrome, FireFox, and Safari. It is not yet supported by Edge, or Internet Explorer (r.i.p).

Keep in mind, you can use a [polyfill](https://developer.mozilla.org/en-US/docs/Glossary/Polyfill) to handle browsers without this capability. Due to the support from major browsers already, it shouldn't be long until full support is available. 

## Summary

The addition of `at()` is a valuable asset to JavaScript's set of Array methods. It allows for a simple and straightforward way to access array elements using an index value. 

With `at()`, you can provide a positive or negative integer value to retrieve an element in an array, counting forward or backward respectively. It is supported by all major browsers such as Chrome, Firefox, and Safari.

Give this new method a whirl and share your thoughts. Happy coding! 



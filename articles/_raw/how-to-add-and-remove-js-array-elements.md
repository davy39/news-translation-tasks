---
title: How to Add and Remove Elements from Arrays in JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2024-03-13T12:34:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-and-remove-js-array-elements
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/mohammad-rahmani-unwXUc_Pqi4-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Arrays are common data structures in JavaScript, and it is important to
  know how to work with them. Common operations on arrays include adding or removing
  elements from the beginning, end or at a specific index.

  In this article, you will learn how to...'
---

Arrays are common data structures in JavaScript, and it is important to know how to work with them. Common operations on arrays include adding or removing elements from the beginning, end or at a specific index.

In this article, you will learn how to work with the built in JavaScript methods: `pop`, `push`, `shift` and `unshift`. You will also learn how to work with the `splice` method which allows you to mutate the original array and add/remove elements at a specific index.

## What is an Array in JavaScript?

Before we start looking at these different array methods, it is important to understand what an array is in JavaScript.

An array is a type of data structure in JavaScript that is used to store a collection of elements that can be of different types. These data types can include strings, numbers, booleans(`true` or `false`), other arrays and objects(`{}`).

Here is an example of an array of names:

```js
const names = ["Jessica", "Jacob", "Zach", "Michelle"];
```

To access an element from an array, you reference the array name, followed by a pair of square brackets containing the index of the element you want to access.

Arrays are zero-indexed, which means the first element in the array has an index of 0, the second element has an index of 1, and so on.

Here is an example of accessing the second element in the `names` array:

```js
names[1]; // "Jacob"
```

If you want to access the last element in an array, you can use the length of the array minus 1.

```js
names[names.length - 1]; // "Michelle"
```

## How to Remove an Element at the End of the Array

If you want to remove an element at the end of an array, you can use the `pop` method. The `pop` method removes the last element from an array and returns that element.

Here is an example of using the `pop` method on the `names` array:

```js
const names = ["Jessica", "Jacob", "Zach", "Michelle"];
const removedName = names.pop();

console.log(removedName); // "Michelle"
```

If you try to use the `pop` method on an empty array, it will return `undefined`.

```js
const emptyArray = [];
const removedElement = emptyArray.pop();

console.log(removedElement); // undefined
```

If you log out the `names` array, then you will see the remaining elements.

```js
console.log(names); // ["Jessica", "Jacob", "Zach"]
```

## How to Remove an Element at the Beginning of the Array

If you want to remove an element at the beginning of an array, you can use the `shift` method. The `shift` method removes the first element from an array and returns that element.

Here is an example of using the `shift` method on the `names` array:

```js
const names = ["Jessica", "Jacob", "Zach", "Michelle"];
const removedName = names.shift();

console.log(removedName); // "Jessica"
```

Just like the `pop` method, if you try to use the `shift` method on an empty array, it will return `undefined`.

```js
const emptyArray = [];
const removedElement = emptyArray.shift();

console.log(removedElement); // undefined
```

## How to Add an Element at the End of the Array

If you need to add an element to the end of an array, you can use the `push` method. The `push` method adds one or more elements to the end of an array and returns the new length of the array.

Here is an example of an array of programming languages:

```js
const programmingLanguages = ["JavaScript", "Python", "Ruby"];
```

If you want to add the languages of `Go` and `Rust` to the end of the `programmingLanguages` array, you would use the `push` method.

```js
const programmingLanguages = ["JavaScript", "Python", "Ruby"];
const originalLength = programmingLanguages.length; // 3

const newLength = programmingLanguages.push("Go", "Rust");

console.log(newLength); // 5
console.log(programmingLanguages); // ["JavaScript", "Python", "Ruby", "Go", "Rust"]
```

A cool thing you can do with the `push` method is to add an array to the end of another array.

In this example we have an array of `programmingLanguages` and an array of `newLanguages`. We can use the `push` method and [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) to add the `newLanguages` array to the end of the `programmingLanguages` array.

```js
const programmingLanguages = ["JavaScript", "Python", "Ruby"];
const newLanguages = ["Go", "Rust"];

const newLength = programmingLanguages.push(...newLanguages);

console.log(newLength); // 5
console.log(programmingLanguages); // ["JavaScript", "Python", "Ruby", "Go", "Rust"]
```

## How to Add an Element at the Beginning of the Array

If you want to add an element to the beginning of an array, you can use the `unshift` method. The `unshift` method adds one or more elements to the beginning of an array and returns the new length of the array.

Here is an example of using the `unshift` method to add three new programming languages to the beginning of the `programmingLanguages` array.

```js
const programmingLanguages = ["JavaScript", "Python", "Ruby"];
const originalLength = programmingLanguages.length; // 3

const newLength = programmingLanguages.unshift("Go", "Rust", "C#");

console.log(newLength); // 6
console.log(programmingLanguages); // ["Go", "Rust", "C#", "JavaScript", "Python", "Ruby"]
```

## How to Add and Remove Elements at a Specific Index

An index is the position of an element in the array. The first element in the array has an index of 0, the second element has an index of 1, and so on.

To add elements at a specific index, you can use the `splice` method. The `splice` method allows you to add and remove elements from a specific index in an array.

In this example, we have a list of American cities.

```js
const cities = ["New York", "Los Angeles", "Chicago", "Houston"];
```

If we want to add the city of `San Francisco` to the second index of the `cities` array, we would use the `splice` method.

```js
const cities = ["New York", "Los Angeles", "Chicago", "Houston"];

cities.splice(1, 0, "San Francisco");

console.log(cities); // ["New York", "San Francisco", "Los Angeles", "Chicago", "Houston"]
```

The first argument of the `splice` method is the index where you want to add or remove elements. In this case, we want to add our city at index 1.

The second argument is the number of elements to remove. In this case, we are not looking to remove any elements, so we pass in 0.

The third argument is the element(s) you want to add. This is where we pass in the city of `San Francisco`.

```js
cities.splice(1, 0, "San Francisco");
```

If we want to remove elements at a specific index, we can use the `splice` method as well.

In this example, we want to remove the city of `Los Angeles` from the `cities` array. We can use the `indexOf` method to find the index of `Los Angeles` and then use the `splice` method to remove it.

The `indexOf` method returns the first index at which a given element can be found in the array, or -1 if it is not present.

```js
const cities = ["New York", "Los Angeles", "Chicago", "Houston"];

const index = cities.indexOf("Los Angeles");

if (index !== -1) {
  cities.splice(index, 1);
}

console.log(cities); // ["New York", "Chicago", "Houston"]
```

The first argument of `index` is the index where we want to remove the element. The second argument of 1 is the number of elements we want to remove.

```js
cities.splice(index, 1);
```

We are wrapping this inside an `if` statement to check if the index of `Los Angeles` is not equal to -1. -1 represents that the element is not present in the array.

If the city is present in the array, then we can use the `splice` method to remove it.

```js
if (index !== -1) {
  cities.splice(index, 1);
}
```

## Conclusion

In this article you learned how to work with the built in JavaScript methods of `pop`, `push`, `shift` and `unshift`. These methods are useful when you want to add or remove elements from the beginning or end of an array.

You also learned how to work with the `splice` method which allows you to mutate the original array and add/remove elements at a specific index.

All of the methods we covered in this article mutate the original array. This means that the original array is changed after using these methods.

I hope you found this article helpful and happy coding!




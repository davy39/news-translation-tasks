---
title: How to Access Properties from an Array of Objects in JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2024-02-29T00:59:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-access-properties-from-an-array-of-objects-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/david-rangel-4m7gmLNr3M0-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When you''re working with JavaScript applications, it''s common to work
  with arrays, nested arrays, and an array of objects. But a lot of beginners sometimes
  struggle with knowing how to access properties from these different data structures.

  In this a...'
---

When you're working with JavaScript applications, it's common to work with arrays, nested arrays, and an array of objects. But a lot of beginners sometimes struggle with knowing how to access properties from these different data structures.

In this article, we will discuss how to access properties from a variety of arrays and look at a few code examples.

## What is an Array in JavaScript?

An array is a type of data structure in JavaScript that is used to store a collection of elements that can be of different types.

You can have an array of strings, like this:

```js
const fruits = ["apple", "banana", "mango", "orange"];
```

You can have an array of numbers:

```js
const numbers = [1, 2, 3, 4, 5];
```

You can have a nested array of arrays like this:

```js
const nestedArray = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
```

You can also have an array of mixed data types:

```js
const mixedArray = ["apple", 1, "banana", 2, "mango", 3];
```

## How to Access Elements from an Array in JavaScript

To access an element from an array, you reference the array name, followed by a pair of square brackets containing the index of the element you want to access.

Here is an example of accessing the first element from the `fruits` array:

```js
const fruits = ["apple", "banana", "mango", "orange"];
console.log(fruits[0]); // apple
```

Arrays are zero-indexed, which means the first element in the array has an index of 0, the second element has an index of 1, and so on.

If you want to access the last element in an array, you can use the length of the array minus 1.

```js
const fruits = ["apple", "banana", "mango", "orange"];
console.log(fruits[fruits.length - 1]); // orange
```

Sometimes it can get confusing when you are dealing with a nested array of arrays. But the syntax remains the same when you want to access an element from a nested array.

Here is an example of accessing the first element from the first array in the `nestedArray`:

```js
const nestedNumberArray = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
console.log(nestedNumberArray[0][0]); // 1
```

`nestedNumberArray[0]` points to this array here:

```js
[1, 2, 3];
```

To access the first element from this array, you use another pair of square brackets with the index of the element you want to access.

```js
nestedNumberArray[0][0];
```

## How to Access Properties from an Array of Objects in JavaScript

Often times you will encounter an array of objects in JavaScript.

Here is an example with an array of developers. Each developer has a name, age, and an array of programming languages they know.

```js
const developers = [
  { name: "John", age: 25, languages: ["JavaScript", "Python"] },
  { name: "Kelly", age: 37, languages: ["Ruby", "Python", "C", "C++"] },
  { name: "Zack", age: 45, languages: ["Go", "C#"] },
];
```

If you wanted to access the name of the first developer, you can use the following syntax:

```js
console.log(developers[0].name); // John
```

Here we are using a combination of dot and bracket notation to access the name property of the first developer object in the `developers` array.

`developers[0]` is the first developer object

```js
{ name: "John", age: 25, languages: ["JavaScript", "Python"] }
```

Then we use dot notation (`developers[0].name`) to access the `name` property of this object.

## How to Find a Specific Value from an Array of Objects in JavaScript

If we are looking for a specific object from an array of objects, we can use the `find` method. The `find` method returns the first element in the array that satisfies the provided testing function. If no elements pass the test, `undefined` is returned.

Here is an example of using the `find` method for an array of numbers:

```js
const numbers = [1, 2, 3, 4, 5];

const foundNumber = numbers.find((number) => number > 3); // 4
```

The following example looks through the numbers array and returns the first number that is greater than 3. In this case, the `find` method returns the number 4.

We can apply the same concept to find a specific object from an array of objects.

In the following example, we are looking for the developer object with the name "Kelly".

```js
const developers = [
  { name: "John", age: 25, languages: ["JavaScript", "Python"] },
  { name: "Kelly", age: 37, languages: ["Ruby", "Python", "C", "C++"] },
  { name: "Zack", age: 45, languages: ["Go", "C#"] },
];

developers.find((developer) => developer.name === "Kelly");
```

In this example, `developer` represents each object in the array. The `find` method will go through the `developers` array and return the first developer object that has the name "Kelly".

```js
{ name: "Kelly", age: 37, languages: ["Ruby", "Python", "C", "C++"] }
```

## Conclusion

I hope you found this article helpful when learning about arrays and how to access properties from them.

We looked at a few examples of arrays as well as how to access elements from nested arrays and an array of objects.

We also learned about the `find` method and how to use it to find a specific object from an array of objects.

Now you should have a better understanding of how to work with arrays and objects in JavaScript.

Happy coding! 🚀



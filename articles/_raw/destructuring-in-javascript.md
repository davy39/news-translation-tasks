---
title: How Destructuring Works in JavaScript – Explained with Code Examples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-07T19:31:01.000Z'
originalURL: https://freecodecamp.org/news/destructuring-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-5--1-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Destructuring is a powerful JavaScript feature introduced in ES6 (ECMAScript\
  \ 2015). It makes it easier to extract values from arrays or properties from objects\
  \ and assign them to variables in a readable way. \nLet's delve into how destructuring\
  \ works ..."
---

Destructuring is a powerful JavaScript feature introduced in ES6 (ECMAScript 2015). It makes it easier to extract values from arrays or properties from objects and assign them to variables in a readable way. 

Let's delve into how destructuring works and explore various use cases with examples.

You can get the source code from [here](https://github.com/dotslashbit/fcc-article-resources/blob/main/js-destruturing/index.js).

## Table of Contents

* [What is Destructuring](#heading-what-is-destructuring)?
* [Array Destructuring](#heading-array-destructuring)
* [Object Destructuring](#heading-object-destructuring)
* [Conclusion](#heading-conclusion)

## What is Destructuring?

Destructuring is a technique that allows you to unpack values from arrays or objects into separate variables. 

This process involves breaking down complex data structures into simpler parts, making it easier to work with them.

## Array Destructuring

Let's start with array destructuring. We'll use the following example.

Without destructuring, extracting values from an array can be verbose:

```javascript
const hobbies = ["Reading", "Coding", "Hiking"];
const firstHobby = hobbies[0];
const secondHobby = hobbies[1];
const thirdHobby = hobbies[2];
console.log(firstHobby); // Output: Reading
console.log(secondHobby); // Output: Coding
console.log(thirdHobby); // Output: Hiking

```

Here, you're accessing each element of the `hobbies` array using index notation and assigning them to individual variables.

Destructuring simplifies this process into a single line of code, like this:

```javascript
const hobbies = ["Reading", "Coding", "Hiking"];
const [firstHobby, secondHobby, thirdHobby] = hobbies;
console.log(firstHobby); // Output: Reading
console.log(secondHobby); // Output: Coding
console.log(thirdHobby); // Output: Hiking

```

In this example, you're extracting the values from the `hobbies` array and assigning them to variables `firstHobby`, `secondHobby`, and `thirdHobby`, respectively.

### Skipping Elements from the Array

You can choose to ignore certain elements by omitting them from the destructuring pattern:

```js
const hobbies = ["Reading", "Coding", "Hiking"];
const [firstHobby, , thirdHobby] = hobbies;
console.log(firstHobby); // Output: Reading
console.log(thirdHobby); // Output: Hiking


```

In this example, you're destructuring the `hobbies` array but only assigning values to the `firstHobby` and `thirdHobby` variables. You're skipping the second element in the array by placing a comma without a variable name between `firstHobby` and `thirdHobby`. This allows you to extract specific elements from the array while ignoring others, providing more flexibility and control in your destructuring patterns.

### Nested Array Destructuring

Array destructuring can also be nested. Here's an example:

```javascript
const nestedArray = [1, [2, 3], 4];
const [firstValue, [secondValue, thirdValue], fourthValue] = nestedArray;
console.log(firstValue); // Output: 1
console.log(secondValue); // Output: 2
console.log(thirdValue); // Output: 3
console.log(fourthValue); // Output: 4

```

In this code, we have a nested array `nestedArray`. Using nested array destructuring, you're extracting values from both the outer and inner arrays and assigning them to variables `firstValue`, `secondValue`, `thirdValue`, and `fourthValue`.

## Object Destructuring

Moving on to object destructuring, consider the following object:

```javascript
const person = {
  name: "John Doe",
  age: 30,
  city: "New York",
  occupation: "Software Engineer",
  hobbies: ["Reading", "Coding", "Hiking"]
};

```

### Regular Destructuring

Object destructuring allows you to extract properties from objects:

```javascript
const { name, age, city } = person;
console.log(name); // Output: John Doe
console.log(age); // Output: 30
console.log(city); // Output: New York

```

In this example, `{ name, age, city }` is the destructuring syntax. It means you're extracting the `name`, `age`, and `city` properties from the `person` object and assigning them to variables of the same name. So `name` will have the value `"John Doe"`, `age` will have `30`, and `city` will have `"New York"`.

### Destructuring with Different Names

You can assign extracted properties to variables with different names:

```javascript
const { name: personName, age: personAge, city: personCity } = person;
console.log(personName); // Output: John Doe
console.log(personAge); // Output: 30
console.log(personCity); // Output: New York

```

In this example, you're using a syntax like `{ name: personName, age: personAge, city: personCity }` which allows you to assign extracted properties to variables with different names. Here, `name` from the `person` object is assigned to `personName`, `age` is assigned to `personAge`, and `city` is assigned to `personCity`.

### Having Default Values while Destructuring

You can also provide default values for object properties:

```javascript
const { name, age, gender = "Unknown" } = person;
console.log(gender); // Output: Unknown

```

Here, you're providing a default value `"Unknown"` for the `gender` property in case it's not present in the `person` object. If `gender` is not defined in `person`, the variable `gender` will default to `"Unknown"`.

### Nested Objects

Object destructuring supports nested objects:

```javascript
const { name, address: { city, country } } = person;
console.log(city); // Output: New York
console.log(country); // Output: undefined (assuming address does not have a country property)

```

In this example, `{ name, address: { city, country } }` is the destructuring syntax. You're extracting the `name` property directly from the `person` object. Then within the `address` object, you're extracting the `city` and `country` properties. So `city` will have the value `"New York"`, and `country` will default to `undefined` assuming `address` does not have a `country` property.

## Conclusion

That's it! You should now have a good understanding of how JavaScript destructuring works for arrays and objects. 

Feel free to experiment with the code examples to further solidify your understanding. If you have any feedback or questions, please contact me on [Twitter](https://twitter.com/introvertedbot) or [Linkedin](https://www.linkedin.com/in/sahil-mahapatra/). Happy learning!


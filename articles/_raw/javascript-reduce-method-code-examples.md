---
title: How JavaScript's Reduce Method Works – Explained with Code Examples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-19T18:00:44.000Z'
originalURL: https://freecodecamp.org/news/javascript-reduce-method-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-10-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Introduced alongside other array methods in ECMAScript 5, reduce() offers\
  \ a unique and powerful way to transform arrays into single values. \nIn this article,\
  \ you'll learn about the reduce() method by understanding what it is, its syntax,\
  \ and finally ..."
---

Introduced alongside other array methods in ECMAScript 5, `reduce()` offers a unique and powerful way to transform arrays into single values. 

In this article, you'll learn about the `reduce()` method by understanding what it is, its syntax, and finally you'll see some use cases where you can use it effectively.

You can get all the source code from [here](https://github.com/dotslashbit/fcc-article-resources/blob/main/js-reduce-method/index.js).

## Table of Contents

* [Understanding the Fundamentals of `reduce()`](#understanding-the-fundamentals)
* [Think of it Like Sculpting Clay](#heading-think-of-it-like-sculpting-clay)
* [Use Cases of `reduce()`](#use-cases)
* [Conclusion](#heading-conclusion)

## Understanding the Fundamentals of `reduce()`

At its heart, `reduce()` iterates through each element of an array, applying a user-defined function (aptly named the "reducer") to both the current element and an accumulator value.

This accumulator starts with an initial value you provide (or defaults to the first array element) and gets updated with the return value of the reducer in each iteration. 

Ultimately, the final state of the accumulator becomes the single value returned by `reduce()`.

### Think of it Like Sculpting Clay

Imagine shaping a piece of clay. You start with a lump and repeatedly apply pressure and direction, transforming it into the desired form. 

Similarly, `reduce()` takes an initial value (the clay) and, through your custom reducer function (your sculpting hands), molds it into the final result.

## Use Cases of `reduce()`

Now, let's delve into some scenarios where `reduce()` shines:

### Calculating Totals

**Scenario:** You have an array of objects representing products, and you want to calculate the total price of all products.

#### Traditional approach with a loop:

```javascript
const products = [
  { name: "Shirt", price: 20 },
  { name: "Shoes", price: 50 },
  { name: "Hat", price: 15 }
];

// Initialize totalPrice to 0
let totalPrice = 0;

// Loop through each product and add its price to totalPrice
for (const product of products) {
  totalPrice += product.price;
}

console.log("Total price (loop):", totalPrice); // Output: Total price (loop): 85

```

The traditional approach initializes a variable `totalPrice` to 0, then iterates through each product in the `products` array using a `for...of` loop. 

Inside the loop, it adds the `price` property of the current product to the `totalPrice`. 

After iterating through all products, the final `totalPrice` (85) is printed to the console.

#### Using `reduce()`:

```javascript
const products = [
  { name: "Shirt", price: 20 },
  { name: "Shoes", price: 50 },
  { name: "Hat", price: 15 }
];

// Use reduce() with an initial value of 0 for totalPrice
const totalPriceReduce = products.reduce((sum, product) => sum + product.price, 0);

console.log("Total price (reduce):", totalPriceReduce); // Output: Total price (reduce): 85

```

The `reduce()` method takes a callback function and an optional initial value (0 in this case). The callback function receives two arguments: `sum`, the accumulator, initially set to the initial value (0), and `product`, the current product object. 

Inside the callback function, the `price` property of the current `product` is added to the `sum`. The return value of the callback function becomes the new `sum` for the next iteration. 

After iterating through all products, the final `sum` (85) is returned and stored in `totalPriceReduce`.

**Comparison:** Both approaches achieve the same result, but `reduce()` offers a more concise and functional way to calculate the total price. It avoids the need for an explicit loop and directly expresses the logic of adding prices within the callback function.

### Finding Minimum or Maximum Values

**Scenario:** You have an array of temperatures and want to find the highest and lowest temperatures.

#### Traditional approach with loops:

```javascript
const temperatures = [25, 18, 32, 20, 15];

// Initialize maxTemp and minTemp to unrealistic values
let maxTemp = -Infinity;
let minTemp = Infinity;

// Loop through each temperature and update maxTemp and minTemp
for (const temp of temperatures) {
  maxTemp = Math.max(maxTemp, temp);
  minTemp = Math.min(minTemp, temp);
}

console.log("Max temp (loop):", maxTemp); // Output: Max temp (loop): 32
console.log("Min temp (loop):", minTemp); // Output: Min temp (loop): 15

```

The traditional approach initializes `maxTemp` to negative infinity and `minTemp` to positive infinity to ensure they are updated with the first encountered temperature.

It then iterates through each temperature in the `temperatures` array using a `for...of` loop. Inside the loop, it uses `Math.max()` to compare the current `maxTemp` with the current temperature and updates `maxTemp` if necessary.

Similarly, it uses `Math.min()` to compare the current `minTemp` and update it if needed. After iterating through all temperatures, the final `maxTemp` (32) and `minTemp` (15) are printed to the console.

#### Using `reduce()`:

```javascript
const temperatures = [25, 18, 32, 20, 15];

// Use reduce() with initial values of -Infinity and Infinity
const maxTempReduce = temperatures.reduce((max, temp) => Math.max(max, temp), -Infinity);
const minTempReduce = temperatures.reduce((min, temp) => Math.min(min, temp), Infinity);

console.log("Max temp (reduce):", maxTempReduce); // Output: Max temp (reduce): 32
console.log("Min temp (reduce):", minTempReduce); // Output: Min temp (reduce): 15

```

The `reduce()` method takes a callback function and an initial value (negative and positive infinity in this case). The callback function receives two arguments: `max` or `min`, the accumulator, starting as the initial values, and `temp`, the current temperature. 

Inside the callback function, `Math.max()` or `Math.min()` is used to compare the current temperature with the accumulator and update it accordingly. 

After iterating through all temperatures, the final maximum and minimum temperatures are returned.

**Comparison:** Both approaches achieve the same result, but `reduce()` offers a more concise and functional way to find the maximum and minimum values. It leverages the accumulator concept to directly compare and update the values within the callback function.

### Building Complex Objects:

**Scenario:** You have an array of students and want to group them by their subjects into a single object.

#### Traditional approach with loops:

```javascript
const students = [
  { name: "Alice", age: 25, subject: "Math" },
  { name: "Bob", age: 30, subject: "Science" },
  { name: "Charlie", age: 28, subject: "History" },
];

// Initialize an empty object to store subject groups
const subjectMap = {};

// Loop through each student and add them to their respective subject group
for (const student of students) {
  const subject = student.subject;
  if (!subjectMap

[subject]) {
    subjectMap[subject] = [];
  }
  subjectMap[subject].push(student);
}

console.log("Subject map (loop):", subjectMap); // Output: { Math: [...], Science: [...], History: [...] }

```

This approach initializes an empty object `subjectMap` to store the grouped students. It then iterates through each student in the `students` array using a `for...of` loop. 

Inside the loop, it retrieves the student's `subject`. If the `subject` doesn't exist as a key in `subjectMap`, a new array is created for that subject. The current student object is then pushed into the corresponding subject array within `subjectMap`.

After iterating through all students, the final `subjectMap` object contains groups of students based on their subjects.

#### Using `reduce()`:

```javascript
const students = [
  { name: "Alice", age: 25, subject: "Math" },
  { name: "Bob", age: 30, subject: "Science" },
  { name: "Charlie", age: 28, subject: "History" },
];

// Use reduce() to build the subject map object
const subjectMapReduce = students.reduce((map, student) => {
  const subject = student.subject;
  map[subject] = map[subject] || [];
  map[subject].push(student);
  return map;
}, {});

console.log("Subject map (reduce):", subjectMapReduce); // Output: { Math: [...], Science: [...], History: [...] }

```

The `reduce()` method takes a callback function and an initial value (an empty object in this case). The callback function receives two arguments: `map`, the accumulator, starting as the initial empty object, and `student`, the current student object. 

Inside the callback function, the `subject` property of the current student is retrieved. If the `subject` doesn't exist in `map`, an empty array is created for it. The current student object is pushed into the corresponding subject array within `map`.

The updated `map` object is returned as the new accumulator for the next iteration. After iterating through all students, the final `map` object contains the grouped students.

**Comparison:** Both approaches achieve the same result, but `reduce()` offers a more concise and functional way to build the object. It leverages the accumulator concept to directly build the `subjectMap` within the callback function.

### Flattening Multidimensional Arrays:

**Scenario:** You have a nested array structure and want to create a single-level array.

#### Traditional approach with loops:

```javascript
const multiArray = [[1, 2], [3, 4], [5]];

// Initialize an empty array to store flattened elements
const flatArray = [];

// Loop through each sub-array and push its elements into flatArray
for (const subArray of multiArray) {
  for (const element of subArray) {
    flatArray.push(element);
  }
}

console.log("Flat array (loop):", flatArray); // Output: [1, 2, 3, 4, 5]

```

This approach initializes an empty array `flatArray` to store the flattened elements. It then iterates through each sub-array in the `multiArray` using a nested `for...of` loop. 

Inside the inner loop, each element of the current sub-array is pushed into `flatArray`. After iterating through all sub-arrays, the final `flatArray` contains all elements in a single level.

#### Using `reduce()`:

```javascript
const multiArray = [[1, 2], [3, 4], [5]];

// Use reduce() to flatten the multidimensional array
const flatArrayReduce = multiArray.reduce((accumulator, currentArray) => {
  return accumulator.concat(currentArray);
}, []);

console.log("Flat array (reduce):", flatArrayReduce); // Output: [1, 2, 3, 4, 5]

```

The `reduce()` method takes a callback function and an initial value (an empty array `[]` in this case). The callback function receives two arguments: `accumulator`, the accumulator, starting as the initial empty array, and `currentArray`, the current sub-array being processed. 

Inside the callback function, the `concat()` method is used to concatenate the `currentArray` with the `accumulator`, effectively flattening the array. The result of `concat()` becomes the new accumulator for the next iteration. 

After iterating through all sub-arrays, the final `accumulator` contains all elements of the multidimensional array flattened into a single level.

**Comparison:** Both approaches achieve the same result of flattening the array, but `reduce()` provides a more elegant and concise solution. It leverages the accumulator concept to gradually build the flattened array, avoiding the need for nested loops and manual pushing of elements.

## Conclusion

In summary, the `reduce()` method in JavaScript provides a concise and powerful way to transform arrays into single values or complex data structures. 

By offering flexibility through a customizable reducer function and an optional initial value, `reduce()` simplifies common tasks such as calculating totals, finding extremes, grouping objects, and flattening arrays. 

Understanding `reduce()` empowers developers to write cleaner, more efficient code and opens up new possibilities for data manipulation in JavaScript projects.

If you have any feedback, then DM me on [Twitter](https://twitter.com/introvertedbot) or [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).


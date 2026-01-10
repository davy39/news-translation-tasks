---
title: How to Declare an Array in JavaScript – Creating an Array in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-14T21:38:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-declare-an-array-in-javascript-creating-an-array-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover-template--2-.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, an array is one of the most commonly used data types. It
  stores multiple values and elements in one variable.

  These values can be of any data type — meaning you can store a string, number, boolean,
  and other data types in one variable....'
---

In JavaScript, an array is one of the most commonly used data types. It stores multiple values and elements in **one** variable.

These values can be of any data type — meaning you can store a string, number, boolean, and other data types in one variable.

There are two standard ways to declare an array in JavaScript. These are either via the array constructor or the literal notation.

In case you are in a rush, here is what an array looks like declared both ways:

```js
// Using array constructor
let array = new array("John Doe", 24, true);

// Using the literal notation
let array = ["John Doe", 24, true];
```

You can continue reading this article to properly understand these methods alongside some other interesting options they possess.

## How to Declare an Array with Literal Notation

This is the most popular and easiest way to create an array. It is a shorter and cleaner way of declaring an array.

To declare an array with literal notation you just define a new array using empty brackets. It looks like this:

```js
let myArray = [];
```

You will place all elements within the square brackets and separate each item or element with a comma.

```js
let myArray = ["John Doe", 24, true];
```

Arrays are zero-indexed, meaning you can access each element starting from zero or output the entire array.

```js
console.log(myArray[0]); // 'John Doe'
console.log(myArray[2]); // true
console.log(myArray); // ['John Doe', 24, true]
```

## How to Declare an Array with the Array Constructor

You can also use the array constructor to create or declare an array. There are a lot of technicalities to declaring an array with the `Array()` constructor.

Just as you can store multiple values with diverse data types in one variable with the array literal notation, you can do the same with the array constructor.

```js
let myArray = new Array();
console.log(myArray); // []
```

The above will create a new empty array. You can add values to the new array by placing them in between the brackets, separated by a comma.

```js
let myArray = new Array("John Doe", 24, true);
```

Just like you learned earlier, you can access each value using its index number, which starts from zero (0).

```js
console.log(myArray[0]); // 'John Doe'
console.log(myArray[2]); // true
console.log(myArray); // ['John Doe', 24, true]
```

When declaring arrays with the array constructor method, it is important to bear the following in mind.

* When you pass a single digit into an array constructor, it will fill the array with the number of empty values you entered.
    

```js
let myArray = new Array(4);
console.log(myArray); // [,,,]
```

But when you pass a single string or any other data type, it works well.

```js
let myArray = new Array(true);
console.log(myArray); // [true]
```

* It is not compulsory to add `new`, as both `Array()` and `new Array()` perform the same task.
    

```js
let myArray = Array("John Doe", 24, true);
```

## Wrapping up!

In this article, you have learned how to declare an array in JavaScript. It is important to know that the array constructor is not really used, as it’s way more complicated than using the array literal notation.

You can learn more in this article on [JavaScript Arrays - How to Create an Array in JavaScript](https://www.freecodecamp.org/news/how-to-create-an-array-in-javascript/) by [Jessica Wilkins](https://www.freecodecamp.org/news/author/jessica-wilkins/)

Have fun coding!

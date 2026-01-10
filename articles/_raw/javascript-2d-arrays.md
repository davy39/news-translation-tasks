---
title: JavaScript 2D Array – Two Dimensional Arrays in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-01-17T16:47:25.000Z'
originalURL: https://freecodecamp.org/news/javascript-2d-arrays
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/cover-template--9-.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript programming, we are all used to creating and working with
  one-dimensional arrays. These are arrays that contain elements (elements of similar
  data types or multiple data types).

  But it’s also good to know that two-dimensional arrays (2D...'
---

In JavaScript programming, we are all used to creating and working with one-dimensional arrays. These are arrays that contain elements (elements of similar data types or multiple data types).

But it’s also good to know that two-dimensional arrays (2D arrays) exist in JS.

In this article, you will learn what two-dimensional arrays are and how they work in JavaScript. It is quite different from other programming languages because, technically, there is no two-dimensional array in JavaScript.

## What is a Two-Dimensional Array?

A two-dimensional array, also known as a 2D array, is a collection of data elements arranged in a grid-like structure with rows and columns. Each element in the array is referred to as a cell and can be accessed by its row and column indices/indexes.

```js
[ a1, a2, a3, ..., an,
  b1, b2, b3, ..., bn,
  c1, c2, c3, ..., cn,
  .
  .
  .
  z1, z2, z3, ..., zn ]
```

In JavaScript, there is no direct syntax for creating 2D arrays as with other commonly used programming languages like C, C++, and Java.

You can create two-dimensional arrays in JavaScript through jagged arrays — an array of arrays. For example, below is what a jagged array looks like:

```js
let twoDimensionalArr = [ [ a1, a2, a3, ..., an ],
[ b1, b2, b3, ..., bn ],
[ c1, c2, c3, ..., cn ],
.
.
.
[ z1, z2, z3, ..., zn ] ];
```

But there is a limitation. It is important to note that two-dimensional arrays have a fixed size. This means that once they are created, the number of rows and columns should be fixed. Also, each row should have a similar number of elements (columns).

For example, the array below has three rows and four elements:

```js
let myArray = [
[0, 1, 2, 3], 
[4, 5, 6, 7],
[8, 9, 0, 0]
];
```

The limitation is that with jagged arrays, you don't get to specify a fixed row and column. This means that a jagged array could have m rows, each having different numbers of elements.

```js
let myArray = [
[0, 1, 2, 3], 
[4, 5, 6, 7],
[8, 9]
];
```

## Why Use a 2D Array in JavaScript?

At this point, you may ask yourself about the importance of a 2D array, especially if this is your first time reading about 2D arrays.

In JavaScript, we use two-dimensional arrays, also known as matrices, to store and manipulate data in a structured and organized manner.

* They allow for the efficient storage and manipulation of large amounts of data, such as in image or video processing, scientific simulations, and spreadsheet applications.
    
* Two-dimensional arrays also enable the use of matrix operations, such as matrix multiplication and transposition, which can simplify complex calculations and make code more readable.
    
* Two-dimensional arrays can represent mathematical matrices in linear algebra and a wide range of data, such as graphs, maps, and tables.
    
* Two-dimensional arrays are commonly used in applications that involve data tables, image processing, and game development.
    

## How to Access Elements in a JavaScript 2D Array

Before you learn how to create 2D arrays in JavaScript, let’s first learn how to access elements in 2D arrays.

You can access the elements of a two-dimensional array using two indices, one for the row and one for the column. Suppose you have the following two-dimensional array:

```js
let MathScore = [
    ['John Doe', 20, 60, 'A'],
    ['Jane Doe', 10, 52, 'B'],
    ['Petr Chess', 5, 24, 'F'],
    ['Ling Jess', 28, 43, 'A'],
    ['Ben Liard', 16, 51, 'B']
];
```

The above is a jagged array in which each element holds the student's name, test score, exam score, and grade. You can access specific elements using the row and column index as seen in the syntax below:

```js
arrayName[rowIndex][columnIndex]
```

To better understand this, let’s convert the two-dimensional array above to a table using `console.table(arrayName)`.

> **Note:** make sure that you replace `arrayName` with the name of your 2D array. In my case, it is `MathScore`.

You will get an output like this, showing the row and column index. Remember that arrays are zero-indexed, meaning items are referenced from 0, not 1.

![](https://paper-attachments.dropboxusercontent.com/s_357699FE5D3810E96F0B6815928F66401CBB5DFE39FAA8BDA7338BEC543A022F_1673843651418_Untitled.drawio+3.png align="left")

Please note that the `(index)` column and row are for the illustration that indicates the indices/indexes of the inner array.

You use two square brackets to access an element of the two-dimensional or multi-dimensional array. The first accesses the rows, while the second accesses the element in the specified row.

```js
console.log(MathScore[4][0]); // returns 'Ben Liard'
console.log(MathScore[2][1]); // returns 5
console.log(MathScore[1][3]); // returns 'B'
console.log(MathScore[2][2]); // returns 24
```

### How to access the first and last elements of a 2D array

Sometimes you might need to find the first and last elements of a two-dimensional array. You can do this using the first and last index of both the rows and columns.

The first element will always have the row and column index of 0, meaning you will use `arrayName[0][0],`.

The index of the last element can be tricky, however. For example, in the example above, the first element is ‘John Doe’ while the last is ‘B’:

```js
console.log(MathScore[0][0]); // returns 'John Doe'
console.log(MathScore[MathScore.length-1][(MathScore[MathScore.length -1]).length - 1]); // returns 'B'
```

### How to add all elements of a 2D array

In some situations, all the elements of your 2D array can be numbers, so you may need to add them together and arrive at just one digit. You can do this using a nested loop. You will first loop through the rows, then, for each row, you loop through its elements.

```js
let numberArr = [
  [10, 20, 60],
  [8, 10, 52],
  [15, 5, 24],
  [26, 28, 43],
  [12, 16, 51]
];

var sum = 0;
numberArr.forEach((row) => {
  row.forEach((element) => {
    sum += element;
  });
});
console.log("The sum of all elements in the array is:" + sum); // returns "The sum of all elements in the array is: 380"
```

## How to Manipulate 2D Arrays in JavaScript

You can manipulate 2D arrays just like one-dimensional arrays using general array methods like pop, push, splice and lots more.

Let’s start by learning how to add/insert a new row and element to the 2D array.

### How to insert an element into a 2D array

You can add an element or many elements to a 2D array with the push() and unshift() methods.

The push() method adds elements(s) to the end of the 2D array, while the unshift() method adds element(s) to the beginning of the 2D array.

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.push(["Tom Right", 30, 32, "B"]);

MathScore.unshift(["Alice George", 28, 62, "A"]);
```

When you `console.log()` or `console.table()` the array, you will see that the new rows have been added:

```js
[
  ["Alice George", 28, 62, "A"],
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"],
  ["Tom Right", 30, 32, "B"]
]
```

You can also add elements to the inner array, but it’s wrong to push to just one inner array without affecting all the array elements. This is because two-dimensional arrays are meant to have the same number of elements in each element array.

```js
MathScore[0].push("B");
```

Instead of affecting one array element, you can add elements to all element arrays at once:

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.forEach((score) => {
  let totalScore = score[1] + score[2];
  score.push(totalScore);
});

console.log(MathScore);
```

This will return:

```js
[
  ["John Doe", 20, 60, "A", 80],
  ["Jane Doe", 10, 52, "B", 62],
  ["Petr Chess", 5, 24, "F", 29],
  ["Ling Jess", 28, 43, "A", 71],
  ["Ben Liard", 16, 51, "B", 67]
]
```

You can also use the `unshift()` method to insert the element at the beginning and the `splice()` method to insert at the middle of the array:

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.splice(2, 0, ["Alice George", 28, 62, "A"]);
```

In the above, `1` is the position where you want the new array to be inserted (remember it is zero-indexed), `0` is used so it removes no element, and then the third parameter is the array to be added.

This is the output:

```js
[
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Alice George", 28, 62, "A"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
]
```

### How to remove an element from a 2D array

You can also remove element(s) from the beginning and end of a 2D array with the `pop()` and `shift()` methods. This is similar to how the `push()` and `unshift()` methods work, but you do not add any parameters to the methods this time.

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.pop();

MathScore.shift();
```

When you `console.log()` or `console.table()` the array, you will see that the first and last array elements have been removed:

```js
[
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
]
```

You can also remove elements from each array element:

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.forEach((score) => {
  score.pop();
});

console.log(MathScore);
```

This will return:

```js
[
  ["John Doe", 20, 60],
  ["Jane Doe", 10, 52],
  ["Petr Chess", 5, 24],
  ["Ling Jess", 28, 43],
  ["Ben Liard", 16, 51]
]
```

You can also use the `shift()` method to remove the element at the beginning and the `splice()` method to remove array elements from specific positions:

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.splice(2, 1);
```

In the code above, you remove one item from position index `2` of the `MathScore` 2D array. This will output:

```js
[
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
]
```

**Note:** All JavaScript array methods will operate on a 2D array because it is an array of arrays. You only have to be mindful when adjusting individual elements in the elements array. You make a similar change on all elements by looping through, even though 2D arrays in JavaScript are not strict.

## How to Create 2D Arrays in JavaScript

There are two options for creating a multi-dimensional array. You can create the array manually with the array literal notation, which uses square brackets `[]` to wrap a list of elements separated by commas. You can also use a nested loop.

### How to create a 2D array using an array literal

This is just like the examples we have been considering using the following syntax:

```js
let arrayName = [
[ elements ],
[ elements ],
[ elements ], ... ];
```

For example, below is a 2D array that holds information about each student’s math score and grade:

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];
```

### How to create a 2D array using a nested for loop

There are many approaches to doing this. But generally, you create a nested loop where the first loop will loop through the rows while the second loop will loop through the elements in the inner array (columns):

```js
let arr = [];
let rows = 4;
let columns = 3;

// creating two-dimensional array
for (let i = 0; i < rows; i++) {
  arr[i] = [];
  for (let j = 0; j < columns; j++) {
    arr[i][j] = j;
  }
}

console.log(arr);
```

In the code above, you will first loop through the rows. For each row, it will create an empty array within the original array declared and stored in variable `arr`. You will then create a nested loop to loop through the columns and add individual elements.

In this example, the index for `j` is used and will output:

```js
[
  [0, 1, 2],
  [0, 1, 2],
  [0, 1, 2],
  [0, 1, 2]
]
```

You can decide to create a number, initialize with 0, and then increase as you loop through so you don’t have the same number for all elements:

```js
let arr = [];
let rows = 4;
let columns = 3;

let value = 0;
// creating two-dimensional array
for (let i = 0; i < rows; i++) {
  arr[i] = [];
  for (let j = 0; j < columns; j++) {
    arr[i][j] = value++;
  }
}

console.log(arr);
```

This will return:

```js
[
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [9, 10, 11]
]
```

You can also decide to create a function that accepts these values as arguments:

```js
const create2Darr = (rows, columns) => {
  let arr = [];
  let value = 0;

  // creating two-dimensional array
  for (let i = 0; i < rows; i++) {
    arr[i] = [];
    for (let j = 0; j < columns; j++) {
      arr[i][j] = value++;
    }
  }
  console.log(arr);
};

let rows = 4;
let columns = 3;
create2Darr(rows, columns);
```

## How to Update Elements in 2D Arrays in JavaScript

This is very similar to how you do it with one-dimensional arrays, where you can update an array’s value by using the index to assign another value.

```js
let array = [1, 2, 3];
array[1] = 5;

console.log(array); // returns [1, 5, 3]
```

You can use the same approach to change an entire row or even individual elements:

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore[1] = ["Alice George", 28, 62, "A"];
console.log(MathScore);
```

This will replace the value of index `1` with this new array:

```js
[
  ["John Doe", 20, 60, "A"],
  ["Alice George", 28, 62, "A"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
]
```

You can update individual elements by tracking the row and column indices and updating their values:

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore[2][0] = "Jack Jim";
console.log(MathScore);
```

This will change the name on the row with index `2` to “Jack Jim”, as seen below:

```js
[
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Jack Jim", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
]
```

## Wrapping Up

In this article, you have learned what two-dimensional arrays are and how they work in JavaScript.

It’s important to know that 2D arrays in JavaScript still work very much like one-dimensional arrays, so feel free to tweak and manipulate them with [JavaScript methods](https://www.freecodecamp.org/news/the-javascript-array-handbook/).

Have fun coding!

You can access over 150 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.

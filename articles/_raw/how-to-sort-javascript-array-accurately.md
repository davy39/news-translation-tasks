---
title: JavaScript Sort Array - How to Sort an Array Accurately
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-14T15:14:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-javascript-array-accurately
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--5-.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In programming, situations that need you to sort data will always arise.
  When you sort data, you will always want accurate results because failure to get
  an accurate result can result in malfunctions or bugs within your code.

  In this article, you wil...'
---

In programming, situations that need you to sort data will always arise. When you sort data, you will always want accurate results because failure to get an accurate result can result in malfunctions or bugs within your code.

In this article, you will learn how to sort an array in JavaScript, some shortcomings associated with the `sort()` method, and how to get more accurate results.

If you are in a rush, the best way to sort an array accurately is to use the comparison function. You need to pass a comparison function into the `sort()` method. This would be explained better in this article, but here is an example:

```js
const numbersArr = [3, 10, 4, 21, 5, 9, 2, 6, 5, 3, 5];

// Ascending Order
numbersArr.sort((a, b) => a - b);
console.log(numbersArr); // Output: [2,3,3,4,5,5,5,6,9,10,21]

// Descending Order
numbersArr.sort((a, b) => b - a);
console.log(numbersArr); // Output: [21,10,9,6,5,5,5,4,3,3,2]
```

If you are not in a rush, let’s understand what causes this malfunction with the `sort()` method and the various ways to fix the issue.

## How the JavaScript Array `sort()` Method Works

The `sort()` method can be used to sort elements of an array in ascending order based on Unicode character code values by default.

Before we explore how it sorts based on Unicode character code values, let’s see some examples.

```js
let numArray = [3, 4, 1, 7, 2];
let sortedArr = numArray.sort();
console.log(sortedArr); // Output: [1,2,3,4,7]
```

It is also important for you to know that when you apply the `sort()` method to an array, it will change the position of the elements in the original array. This means you do not need to assign a new variable to the sorted array:

```js
let numArray = [3, 4, 1, 7, 2];
numArray.sort();
console.log(numArray); // Output: [1,2,3,4,7]
```

You can also apply the method to the array itself:

```js
let numArray = [3, 4, 1, 7, 2].sort();
console.log(numArray); // Output: [1,2,3,4,7]
```

But this is far from what this article is all about. The `sort()` method compares the elements of the array by converting them into strings and then comparing their Unicode code points. This means that in some situations, the sorting could go wrong in reality:

```js
let numArray = [3, 10, 4, 21, 5, 9, 2, 6, 5, 3, 5].sort();
console.log(numArray); // Output: [10,2,21,3,3,4,5,5,5,6,9]
```

You will notice that **10** is coming first before **2**, **21** before **3** and so on.

## JavaScript sort() Method Shortcomings And How To Sort Accurately

Let’s now go over some shortcomings of the `sort()` method and how to solve them. Understanding these shortcomings and how to solve them will give you an edge and help you avoid some bugs.

### How To Sort Numbers Accurately in JavaScript

The `sort()` method of JavaScript compares the elements of the array by converting them into strings and then comparing their Unicode code points.

This can lead to unexpected results when sorting arrays of numbers, as seen in the example where 10, 5, and 80 are sorted as 10, 5, 80 instead of 5, 10, 80.

```js
let numArr = [10, 5, 80].sort();
console.log(numArr); // Output: [10, 5, 80]
```

To solve this shortcoming, you can provide a comparison function that defines the desired sorting order.

For sorting an array of numbers, the comparison function should subtract the second number from the first number.

This will result in a negative number if the first number is smaller than the second number, a positive number if the first number is larger than the second number, and 0 if the two numbers are equal.

Here's an example:

```js
let numArr = [10, 5, 80];

numArr.sort((a, b) => a - b);
console.log(numArr); // Output: [5, 10, 80]
```

By providing a comparison function that defines the correct sorting order, we can ensure that the array is sorted accurately.

You can also sort your array elements in descending order by subtracting the first number from the second number:

```js
let numArr = [10, 5, 80];

numArr.sort((a, b) => b - a);
console.log(numArr); // Output: [80, 10, 5]
```

### How To Sort Strings Accurately

The `sort()` method can also be used to sort an array of strings, but the sorting order may not be accurate in all cases.

For example, the strings "a", "A", and "b" would be sorted as "A", "a", "b" instead of "a", "A", "b", because the uppercase "A" has a lower Unicode code point than the lowercase "a".

```js
let stringsArr = ["a", "A", "b"].sort();
console.log(stringsArr); // Output: ["A","a","b"]
```

To solve this shortcoming, you can provide a comparison function that defines the desired sorting order.

For sorting an array of strings in a case-insensitive alphabetical order, the comparison function should convert both strings to lowercase using the `toLowerCase()` method and then compare them using the `<` and `>` operators.

Here's an example:

```js
let stringsArr = ["a", "A", "b"];

stringsArr.sort((a, b) => a.toLowerCase() < b.toLowerCase() ? -1 : 1);
console.log(stringsArr); // Output: ["a", "A", "b"]
```

By providing a comparison function that defines the correct sorting order, we can ensure that the array of strings is sorted accurately.

You can sort in the opposite order by alternating the values of `-1` and `1`:

```js
let stringsArr = ["a", "A", "b"];

stringsArr.sort((a, b) => a.toLowerCase() < b.toLowerCase() ? 1 : -1);
console.log(stringsArr); // Output: ["b", "A", "a"]
```

### How to Avoid Modifying the Original Array When Sorting

One of the shortcomings of the `sort()` method is that it sorts the elements in place, which means it modifies the original array.

This can be problematic if you need to preserve the original order of the elements or if you need to sort a large array multiple times.

To avoid modifying the original array, you can make a copy of the array using the `slice()` method before sorting it.

Here's an example:

```js
let originalArray = [2, 1, 3];
let sortedArray = originalArray.slice().sort((a, b) => a - b);

console.log(originalArray); // Output: [2, 1, 3]
console.log(sortedArray); // Output: [1, 2, 3]
```

## Wrapping Up 🎉

In this article, you have learned how to sort an array in JavaScript, the various shortcomings of the `sort()` method and how to fix them.

There is more to the sort method and what it can do, but understanding that the comparison function exists will help you handle many difficulties.

Have fun coding!

You can access over 195 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.

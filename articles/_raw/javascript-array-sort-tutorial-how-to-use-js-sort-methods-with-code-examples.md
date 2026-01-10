---
title: JavaScript Array Sort – How to Use JS Sort Methods (With Code Examples)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-24T19:34:05.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-sort-tutorial-how-to-use-js-sort-methods-with-code-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ad9740569d1a4ca2820.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Cem Eygi\nIn JavaScript, we can sort the elements of an array easily\
  \ with a built-in method called the sort( ) function. \nHowever, data types (string,\
  \ number, and so on) can differ from one array to another. This means that using\
  \ the sort( ) method..."
---

By Cem Eygi

In JavaScript, we can sort the elements of an array easily with a built-in method called the sort( ) function. 

However, data types (string, number, and so on) can differ from one array to another. This means that using the sort( ) method alone is not always an appropriate solution. 

In this post, you will learn how to sort an array in JavaScript by using the sort( ) method for strings and numbers.

## Array of Strings

Let's start with strings:

```javascript
const teams = ['Real Madrid', 'Manchester Utd', 'Bayern Munich', 'Juventus'];
```

When we use the sort( ) method, elements will be sorted in ascending order (A to Z) by default:

```javascript
teams.sort(); 

// ['Bayern Munich', 'Juventus', 'Manchester Utd', 'Real Madrid']
```

If you prefer to sort the array in descending order, you need to use the reverse( ) method instead:

```javascript
teams.reverse();

// ['Real Madrid', 'Manchester Utd', 'Juventus', 'Bayern Munich']
```

## Array of Numbers

Sorting numbers is unfortunately not that simple. If we apply the sort method directly to a numbers array, we will see an unexpected result:

```javascript
const numbers = [3, 23, 12];

numbers.sort(); // --> 12, 23, 3
```

### Why the sort( ) method isn't working for numbers

Actually it is working, but this problem happens because JavaScript sorts numbers alphabetically. Let me explain this in detail.

Let's think of A=1, B=2, and C=3.

```javascript
const myArray = ['C', 'BC', 'AB'];

myArray.sort(); // [AB, BC, C]
```

As an example, if we have three strings as C (3), BC (23) and AB(12), JavaScript will sort them as AB, BC, and C in an ascending order, which is alphabetically correct.

However, JavaScript will sort the numbers (alphabetically again) as 12, 23, and 3, which is incorrect.

### Solution: The Compare Function

Luckily, we can support the sort( ) method with a basic comparison function which will do the trick:

```javascript
function(a, b) {return a - b}
```

The sort method, fortunately, can sort negative, zero, and positive values in the correct order. When the sort( ) method compares two values, it sends the values to our compare function and sorts the values according to the returned value.

* If the result is negative, a is sorted before b.
* If the result is positive, b is sorted before a.
* If the result is 0, nothing changes.

All we need to is using the compare function inside the sort( ) method:

```javascript
const numbers = [3, 23, 12];

numbers.sort(function(a, b){return a - b}); // --> 3, 12, 23
```

If we want to sort the numbers in descending order, this time we need to subtract the second parameter (b) from the first one (a):

```javascript
const numbers = [3, 23, 12];

numbers.sort(function(a, b){return b - a}); // --> 23, 12, 3
```

## Wrap Up

So as we can see, sorting the elements of an array can be done easily in JavaScript with the sort( ) method, if we know how to use it correctly. I hope my post helps you to understand how to use the sort( ) method in JavaScript in the right way.

**If you want to learn more about Web Development, feel free to visit my [Youtube channel](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q?view_as=subscriber).**

Thank you for reading!


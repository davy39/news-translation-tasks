---
title: JavaScript Map, Reduce, and Filter - JS Array Functions Explained with Code
  Examples
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-10T17:53:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-map-reduce-and-filter-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f75740569d1a4ca42b1.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: Map, reduce, and filter are all array methods in JavaScript. Each one will
  iterate over an array and perform a transformation or computation. Each will return
  a new array based on the result of the function. In this article, you will learn
  why and ho...
---

Map, reduce, and filter are all array methods in JavaScript. Each one will iterate over an array and perform a transformation or computation. Each will return a new array based on the result of the function. In this article, you will learn why and how to use each one.

Here is a fun summary by Steven Luscher:

%[https://twitter.com/steveluscher/status/741089564329054208]

## Map

The `map()` method is used for creating a new array from an existing one, applying a function to each one of the elements of the first array.

### Syntax

```javascript
var new_array = arr.map(function callback(element, index, array) {
    // Return value for new_array
}[, thisArg])
```

In the callback, only the array `element` is required. Usually some action is performed on the value and then a new value is returned.

### Example 

In the following example, each number in an array is doubled.

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(item => item * 2);
console.log(doubled); // [2, 4, 6, 8]
```

## Filter

The `filter()` method takes each element in an array and it applies a conditional statement against it. If this conditional returns true, the element gets pushed to the output array. If the condition returns false, the element does not get pushed to the output array. 

### Syntax

```javascript
var new_array = arr.filter(function callback(element, index, array) {
    // Return true or false
}[, thisArg])
```

The syntax for `filter` is similar to `map`, except the callback function should return `true` to keep the element, or `false` otherwise. In the callback, only the `element` is required. 

### Examples

In the following example, odd numbers are "filtered" out, leaving only even numbers.

```javascript
const numbers = [1, 2, 3, 4];
const evens = numbers.filter(item => item % 2 === 0);
console.log(evens); // [2, 4]
```

In the next example, `filter()` is used to get all the students whose grades are greater than or equal to 90.

```javascript
const students = [
  { name: 'Quincy', grade: 96 },
  { name: 'Jason', grade: 84 },
  { name: 'Alexis', grade: 100 },
  { name: 'Sam', grade: 65 },
  { name: 'Katie', grade: 90 }
];

const studentGrades = students.filter(student => student.grade >= 90);
return studentGrades; // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]
```

## Reduce

The `reduce()` method reduces an array of values down to just one value. To get the output value, it runs a reducer function on each element of the array.

### **Syntax**

```javascript
arr.reduce(callback[, initialValue])
```

The `callback` argument is a function that will be called once for every item in the array. This function takes four arguments, but often only the first two are used.

* _accumulator_ - the returned value of the previous iteration
* _currentValue_ - the current item in the array
* _index_ - the index of the current item
* _array_ - the original array on which reduce was called
* The `initialValue` argument is optional. If provided, it will be used as the initial accumulator value in the first call to the callback function.

### Examples

The following example adds every number together in an array of numbers.

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce(function (result, item) {
  return result + item;
}, 0);
console.log(sum); // 10
```

In the next example, `reduce()` is used to transform an array of strings into a single object that shows how many times each string appears in the array. Notice this call to reduce passes an empty object `{}` as the `initialValue` parameter. This will be used as the initial value of the accumulator (the first argument) passed to the callback function.

```javascript
var pets = ['dog', 'chicken', 'cat', 'dog', 'chicken', 'chicken', 'rabbit'];

var petCounts = pets.reduce(function(obj, pet){
    if (!obj[pet]) {
        obj[pet] = 1;
    } else {
        obj[pet]++;
    }
    return obj;
}, {});

console.log(petCounts); 

/*
Output:
 { 
    dog: 2, 
    chicken: 3, 
    cat: 1, 
    rabbit: 1 
 }
 */
```

## Video Explanation

Check out the video below from the freeCodeCamp.org YouTube channel. It covers the array methods discussed, plus a few more.

%[https://www.youtube.com/watch?v=Urwzk6ILvPQ]



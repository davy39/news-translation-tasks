---
title: The Ultimate Guide to JavaScript Array Methods - Reduce
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-23T18:07:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-javascript-array-methods-reduce
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f19740569d1a4ca40cf.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'The reduce() method reduces an array of values down to just one value.
  The single value that is returned can be of any type.

  reduce() is like the Swiss Army knife of array methods. While others like map()
  and filter() provide specific functionality, ...'
---

The `reduce()` method reduces an array of values down to just one value. The single value that is returned can be of any type.

`reduce()` is like the Swiss Army knife of array methods. While others like `map()` and `filter()` provide specific functionality, `reduce()` can be used to transform an input array into any output you desire, all while preserving the original array.

## Syntax

```js
const newValue = arr.reduce(function(accumulator, currentValue, index, array) {
  // Do stuff with accumulator and currentValue (index, array, and initialValue are optional)
}, initialValue);
```

* `newValue` - the new number, array, string, or object that is returned
* `arr` - the array being operated on
* `accumulator` - the returned value of the previous iteration
* `currentValue` - the current item in the array
* `index` - the index of the current item
* `array` - the original array on which `reduce()` was called
* `initialValue` - a number, array, string, or object that serves as an initial value for the eventual output

## Examples

### ES5

```js
var numbers = [1, 2, 3]; 

var sum = numbers.reduce(function(total, current) {
  return total + current;
}, 0);

console.log(numbers); // [1, 2, 3]
console.log(sum); // 6
```

### ES6

```js
const numbers = [1, 2, 3];

const sum = numbers.reduce((total, current) => {
  return total + current;
}, 0);

const sumOneLiner = numbers.reduce((total, current) => total + current, 0);

console.log(numbers); // [1, 2, 3]
console.log(sum); // 6
console.log(sumOneLiner); // 6
```

## All About `initialValue`

### `initialValue` Provided

The `initialValue` argument is optional. If provided, it will be used as the initial accumulator value (`total`) in the first call to the callback function:

```js
const numbers = [2, 3, 4];
const product = numbers.reduce((total, current) => {
  return total * current;
}, 1);

console.log(product); // 24
```

Since the `initialValue` of 1 is provided after the callback function, the `reduce()` starts at the beginning of the array and sets the first element (2) as the current value (`current`). It then iterates through the rest of the array, updating the accumulator value and current value along the way.

### `initialValue` Omitted

If `initialValue` is not provided, the iteration will start at the second element in the array (at index 1), with `accumulator` equal to the first element in the array and `currentValue` equal to the second element:

```js
const numbers = [2, 3, 4];
const product = numbers.reduce((total, current) => {
  return total * current;
});

console.log(product);
```

In this example, no `initialValue` is provided, so `reduce()` sets the first element of the array as the accumulator value (`total` is equal to 2), and sets the second element of the array as the current value (`currentValue` is equal to 3). It then iterates through the rest of the array.

When reducing an array of strings:

```js
const strings = ['one', 'two', 'three'];
const numberString = strings.reduce((acc, curr) => {
  return acc + ', ' + curr;
});

console.log(numberString); // "one, two, three"
```

While it's easy to omit the `initialValue` argument if your `reduce()` method will return a number or a simple string, you should include one if it will return an array or object.

## Returning an Object

Transforming an array of strings into a single object that shows how many times each string appears in the array is simple. Just pass an empty object (`{}`) as the `initialValue`:

```js
const pets = ["dog", "chicken", "cat", "dog", "chicken", "chicken", "rabbit"];

const petCounts = pets.reduce(function(obj, pet) {
  if (!obj[pet]) {
    // if the pet doesn't yet exist as a property of the accumulator object,
    //   add it as a property and set its count to 1
    obj[pet] = 1;
  } else {
    // pet exists, so increment its count
    obj[pet]++;
  }
  
  return obj; // return the modified object to be used as accumulator in the next iteration
}, {}); // initialize the accumulator as an empty object

console.log(petCounts);
/*
{
  dog: 2, 
  chicken: 3, 
  cat: 1, 
  rabbit: 1 
}
*/
```

## Returning and Array

Generally, if you plan to return an array, `map()` is often a better option. It tells the compiler (and others reading your code) that every element in the original array will be transformed and returned as a new array of equal length.

On the other hand, `reduce()` indicates that all elements of the original array will get transformed into a new value. That new value could be an array, the length of which might be different than the original.

Say you have a shopping list as an array of strings, but you want to remove all of the foods that you don't like from the list. You could use `filter()` to filter out everything you don't like and `map()` to return a new array of strings, or you could just use `reduce()`:

```js
const shoppingList = ['apples', 'mangoes', 'onions', 'cereal', 'carrots', 'eggplants'];
const foodsIDontLike = ['onions', 'eggplants'];
const newShoppingList = shoppingList.reduce((arr, curr) => {
  if (!foodsIDontLike.includes(curr)) {
    arr.push(curr);
  }
  
  return arr;
}, []);

console.log(newShoppingList); // ["apples", "mangoes", "cereal", "carrots"]
```

That's all you need to know about the `reduce()` method. Like a Swiss Army knife, it's not always the best tool for the job. But you'll be glad to have it in your back pocket when you really need it.


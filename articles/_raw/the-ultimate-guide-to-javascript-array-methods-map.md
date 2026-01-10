---
title: The Ultimate Guide to JavaScript Array Methods - Map
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-21T18:05:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-javascript-array-methods-map
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f23740569d1a4ca40fc.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "The map() method applies a function to each element in an array and returns\
  \ a copy of the original array with modified values (if any).\nSyntax:\nconst newArr\
  \ = oldArr.map(function(currentValue, index, array) {\n  // Do stuff with currentValue\
  \ (index an..."
---

The `map()` method applies a function to each element in an array and returns a copy of the original array with modified values (if any).

## Syntax:

```js
const newArr = oldArr.map(function(currentValue, index, array) {
  // Do stuff with currentValue (index and array are optional)
});
```

* `newArr` - the new array that is returned
* `oldArr` - the old array being operated on. This array will not be changed
* `currentValue` - the current value being processed
* `index` - the current index of the value being processed
* `array` - the original array

## Examples:

### ES5

```js
var arr = [1, 2, 3, 4];

var newArray = arr.map(function(element) {
  return element * 2
});

console.log(arr); // [1, 2, 3, 4]
console.log(newArray); // [2, 4, 6, 8]
```

### ES6

```js
const arr = [1, 2, 3, 4];

const newArray = arr.map(element => {
  return element * 2;
});

const newArrayOneLiner = arr.map(element => element * 2);

console.log(arr); // [1, 2, 3, 4]
console.log(newArray); // [2, 4, 6, 8]
console.log(newArrayOneLiner); // [2, 4, 6, 8]
```

## `map` vs `forEach`

On the surface, the `map()` and `forEach()` methods are very similar. Both methods iterate through an array and apply a function to each element. The main difference is that `map()` returns a new array, while `forEach()` doesn't return anything.

So which method should you use? Generally, it's better to use `forEach()` if you don't need to change the values in the original array. `forEach()` is a good choice if all you need to do is log each element of an array to the console, or save them to a database:

```js
const letters = ['a', 'b', 'c', 'd'];

letters.forEach(letter => {
  console.log(letter);
});
```

`map()` is a better choice if you need to update the values in the original array. It's especially useful if you want to store the updated array as a variable and keep the original as a reference.

## How to Use `map` with Other Array Methods

Since `map()` returns an array, you can use it with other array methods to make your code much more succinct and readable.

### Using `map` with `filter`

One thing to remember while using `map()` is that it applies a function to _every_ element of the original array, and returns a new array the same length as the old one. In other words, it's not possible to skip over elements of the array that you don't want to modify:

```js
const nums = [5, 10, 15, 20];
const doublesOverTen = nums.map(num => {
  if (num > 10) {
    return num * 2;
  }
});

console.log(doublesOverTen); // [undefined, undefined, 30, 40]
```

That's where the `filter()` method comes in. `filter()` returns a new array of filtered elements that meet a certain condition, which you can then chain `map()` to:

```js
const nums = [5, 10, 15, 20];
const doublesOverTen = nums.filter(num => {
  return num > 10;
}).map(num => {
  return num * 2;
});

console.log(doublesOverTen); // [30, 40]
```

This code can be simplified even further:

```js
const nums = [5, 10, 15, 20];
const doublesOverTen = nums.filter(num => num > 10).map(num => num * 2);

console.log(doublesOverTen); // [30, 40]
```

### Using `map` with `reverse`

There may be times when you need to reverse an array while mapping through it. The `reverse()` method makes this easy, but it's important to remember that, while `map()` is immutable, `reverse()` isn't. In other words, the `reverse()` method will change the original array:

```js
const nums = [1, 2, 3, 4, 5];
const reversedDoubles = nums.reverse().map(num => num * 2);

console.log(nums); // [5, 4, 3, 2, 1]
console.log(reversedDoubles); // [10, 8, 6, 4, 2]
```

One of the main advantages of `map()` is that it doesn't alter the original array, and using `reverse()` like this defeats the purpose. However, this is a simple fix – just remember to use `map()` first, then `reverse()` the new array it returns:

```js
const nums = [1, 2, 3, 4, 5];
const reversedDoubles = nums.map(num => num * 2).reverse();

console.log(nums); // [1, 2, 3, 4, 5]
console.log(reversedDoubles); // [10, 8, 6, 4, 2]
```

### Using `map` on an Object

While `map()` is meant for operating on arrays, with just a little extra work you can also iterate through objects. `Object.keys()`, `Object.values()`, and `Object.entries()` all return an array, meaning that `map()` can easily be chained to each method:

```js
const obj = { 
  a: 1, 
  b: 2, 
  c: 3 
}
const doubles = Object.values(obj).map(num => num * 2);

console.log(doubles); // [2, 4, 6]
```

Now go forth and `map()` all the things!



---
title: How to Count Objects in an Array
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:18:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-count-objects-in-an-array
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a9a740569d1a4ca2696.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: object
  slug: object
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Knowing how to quickly iterate through an array and count objects is deceptively
  simple. The length() method will tell you the total number of values in the array,
  but what if you only want to count those values based on certain conditions?

  For examp...'
---

Knowing how to quickly iterate through an array and count objects is deceptively simple. The `length()` method will tell you the total number of values in the array, but what if you only want to count those values based on certain conditions?

For example, imagine you have an array like this:

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];
```

And you only want to count the number of objects with `status` set to `'0'`.

Like with just about everything in programming, there are a number of ways to do this. We'll go through a few of the common methods below.

## Use a `for` loop

Probably the easiest way would be to declare a `counter` variable, loop through the array, and iterate `counter` only if `status` is equal to `'0'`:

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

let counter = 0;
for (let i = 0; i < storage.length; i++) {
  if (storage[i].status === '0') counter++;
}

console.log(counter); // 6
```

You could simplify this a bit by using a `for...of` loop:

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

let counter = 0;
for (const obj of storage) {
  if (obj.status === '0') counter++;
}

console.log(counter); // 6
```

Also, you could create a function to do the same thing if you have other arrays of objects to count conditionally:

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

function statusCounter(inputs) {
  let counter = 0;
  for (const input of inputs) {
    if (input.status === '0') counter += 1;
  }
  return counter;
}

statusCounter(storage); // 6
```

## Use array methods

JavaScript includes a bunch of [helpful methods](https://www.freecodecamp.org/news/javascript-standard-objects-arrays/) when working with arrays. Each one can be chained to an array and passed different parameters to work with while iterating through the elements in the array.

The two we'll look at are `filter()` and `reduce()`.

### `filter()`

The filter method does just that – it iterates through each element in the array and filters out all elements that don't meet the condition(s) you provide. It then returns a new array with all the elements that returned true based on your condition(s).

For example:

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.filter(function(item){
  if (item.status === 0) {
    return true;
  } else {
    return false;
  }
});

/*
[
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' }
] 
*/
```

Now that you've filtered out the object with `status: '1'`, just call the `length()` method on the new array to get the total count of objects with `status: '1'`:

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.filter(function(item){
  if (item.status === 0) {
    return true;
  } else {
    return false;
  }
}).length; // 6
```

But this can be shortened a lot with ES6 syntax:

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.filter(item => item.status === '0').length; // 6
```

### `reduce()`

Think of the `reduce()` method like a Swiss army knife – it's extremely flexible, and lets you take an array as input and transform it into just about anything. Even better, like `filter()`, this method returns a new array, leaving the original unchanged.

You can read more about `reduce()` in [this article](https://www.freecodecamp.org/news/the-ultimate-guide-to-javascript-array-methods-reduce/).

For our purposes, we want to take an array, examine its contents, and produce a number. Here's a simple way to do that:

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.reduce((counter, obj) => {
  if (obj.status === '0') counter += 1
  return counter;
}, 0); // 6
```

You could simplify further by using ES6 syntax and a ternary operator:

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.reduce((counter, obj) => obj.status === '0' ? counter += 1 : counter, 0); // 6
```

And even a bit more by using [object destructuring](https://www.freecodecamp.org/news/array-and-object-destructuring-in-javascript/): 

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.reduce((counter, { status }) => status === '0' ? counter += 1 : counter, 0); // 6
```

So those are a few ways to go through the elements of an array and count them conditionally. Now get out there and count with confidence!


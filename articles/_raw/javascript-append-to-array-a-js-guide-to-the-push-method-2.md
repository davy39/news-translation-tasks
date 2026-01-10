---
title: 'JavaScript Append to Array: a JS Guide to the Push Method'
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-04-19T13:57:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-append-to-array-a-js-guide-to-the-push-method-2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/604b89aba7946308b768767f.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Sometimes you need to append one or more new values at the end of an array.
  In this situation the push() method is what you need.

  The push() method will add one or more arguments at the end of an array in JavaScript:

  let arr = [0, 1, 2, 3];

  arr.push(...'
---

Sometimes you need to append one or more new values at the end of an array. In this situation the `push()` method is what you need.

The `push()` method will add one or more arguments at the end of an array in JavaScript:

```javascript
let arr = [0, 1, 2, 3];
arr.push(4);
console.log(arr); // [0, 1, 2, 3, 4]
```

This method accepts an unlimited number of arguments, and you can add as many elements as you want at the end of the array.

```
let arr = [0, 1, 2, 3];
arr.push(4, 5, 6, 7, 8, 9);
console.log(arr); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The `push()` method also returns the new length of the array.

```
let arr = [0, 1, 2, 3];
let newLength = arr.push(4);
console.log(newLength); // 5
```

## Examples of `push` in JavaScript and common errors

### How to reassign the array

 Reassigning the array with the output from `push` is a common error.

```javascript
let arr = [0, 1, 2, 3];
arr = arr.push(4);
console.log(arr); // 5
```

To avoid this error you need to remember that `push`  changes the array, and returns the new length. If you reassign the variable with the return value from `push()` you are overwriting the array value.

### How to add the contents of one array to the end of another

If you want to add the content of an array to the end of another, `push` is a possible method to use. `push` will add as new elements whatever you use as an argument. This is the same also for another array, so the array has to be unpacked with the spread operator:

```javascript
let arr1 = [0, 1, 2, 3];
let arr2 = [4, 5, 6, 7];
arr1.push(...arr2);
console.log(arr1); // [0, 1, 2, 3, 4, 5, 6, 7]
```

### How to use `push` on an array-like object

There are objects that are similar to arrays (like the `arguments` object – the object that allows access to all arguments of a function), but that do not have all methods that arrays have. 

To be able to use `push` or other array methods on these, first they have to be converted to arrays.

```
function myFunc() {
   let args = [...arguments];
   args.push(4);
   returns args;
}

console.log(myFunc(0, 1, 2, 3)); // [0, 1, 2, 3, 4]
```

If you don't first change the array-like `arguments` object to an array, the code would stop with a `TypeError: arguments.push is not a function`.

## Conclusion

If you work with arrays, don't miss out on `push`. It adds one or more elements at the end of an array and returns the new length of the array.


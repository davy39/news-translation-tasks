---
title: Nesting For Loops in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/nesting-for-loops-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a97740569d1a4ca2681.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
- name: toothbrush
  slug: toothbrush
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'If you''re having trouble understanding freeCodeCamp''s Nesting For Loops
  challenge, don''t worry. We got your back.

  In this problem you have to complete the multiplyAll() function, and takes a multi-dimensional
  array as an argument. Remember that a mul...'
---

If you're having trouble understanding freeCodeCamp's [Nesting For Loops](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/nesting-for-loops) challenge, don't worry. We got your back.

In this problem you have to complete the `multiplyAll()` function, and takes a multi-dimensional array as an argument. Remember that a multi-dimensional array, sometimes called a 2D array, is just an array of arrays, for example, `[[1,2], [3,4], [5,6]]`.

In the editor on the right, `multiplyAll()` is defined as follows:

```js
function multiplyAll(arr) {
  var product = 1;
  // Only change code below this line

  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

You need to complete the function so it multiplies the `product` variable by each number in the sub-arrays of the parameter `arr`, which is a multi-dimensional array.

There are a lot of different ways to solve this problem, but we'll focus on the simplest method using `for` loops.

## Set up your `for` loops

Because `arr` is a multi-dimensional array, you'll need two `for` loops: one to loop through each of the sub-arrays arrays, and another to loop through the elements in each sub-array.

### Loop through the inner arrays

To do this, set up a `for` loop like you've done in previous challenges:

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

Note that we're using `let` instead of `var` for the loop and to declare `product`. In this challenge you won't notice a difference between the two, but generally it's good practice to use ES6's `const` and `let` whenever you can. You can read more about why [in this article](https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/).

Now log each of the sub-arrays to the console:

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

Because you're calling `multiplyAll()` with `[[1,2],[3,4],[5,6,7]]` at the bottom, you should see the following:

```
[ 1, 2 ]
[ 3, 4 ]
[ 5, 6, 7 ]
```

### Loop through the elements in each sub-array

Now you need to loop through each number in the sub-arrays you just logged to the console.

Remove `console.log(arr[i]);` and create another `for` loop inside of the one you just wrote:

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

Remember that, for the inner loop, we need to check the `.length` of `arr[i]` since `arr[i]` is one of the sub-arrays we looked at earlier.

Now log `arr[i][j]` to the console to see each of the individual elements:

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      console.log(arr[i][j]);
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

```
1
2
3
4
5
6
7
```

Finally, multiply `product` by every element in each of the sub-arrays:

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      product *= arr[i][j];
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);
```

If you log `product` to the console, you'll see the correct answer for each test case:

```
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      product *= arr[i][j];
    }
  }
  // Only change code above this line
  console.log(product);
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);
```

```
6  // [[1], [2], [3]]
5040  // [[1, 2], [3, 4], [5, 6, 7]]
54  // [[5, 1], [0.2, 4, 0.5], [3, 9]]
```

## A closer look

If you're still not sure why the code above works, don't worry – you're not alone. Working with nested loops is complicated, and even experienced developers can get confused.

In cases like this, it can be helpful to log something more detailed to the console. Go back to your code and log ``Sub-array ${i}: ${arr[i]}`` to the console just before the inner `for` loop:

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    console.log(`Sub-array ${i}: ${arr[i]}`);
    for (let j = 0; j < arr[i].length; j++) {
      product *= arr[i][j];
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);
```

In the outer `for` loop, each iteration goes through the sub-arrays in `arr`. You should see this in the console:

```
Sub-array 0: 1,2
Sub-array 1: 3,4
Sub-array 2: 5,6,7
```

Note that we're using [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) above. ``Sub-array ${i}: ${arr[i]}`` is the same as `'Sub-array ' + i + ': ' + arr[i]`, just much easier to write.

Now in the inner `for` loop, log ``Element ${j}: ${arr[i][j]}`` to the console:

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    console.log(`Sub-array ${i}: ${arr[i]}`);
    for (let j = 0; j < arr[i].length; j++) {
      console.log(`Element ${j}: ${arr[i][j]}`);
      product *= arr[i][j];
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);
```

The inner `for` loop goes through each element in each sub-array (`arr[i]`), so you should see this in the console:

```
Sub-array 0: 1,2
Element 0: 1
Element 1: 2
Sub-array 1: 3,4
Element 0: 3
Element 1: 4
Sub-array 2: 5,6,7
Element 0: 5
Element 1: 6
Element 2: 7
```

The first iteration of `i` grabs the first sub-array, `[1, 2]`. Then the first iteration of `j` goes through each element in that sub-array:

```
// i is 0
arr[0] // [1, 2];

// j is 0
arr[0][0] // 1
// j is 1
arr[0][1] // 2

-----

// i is 1
arr[1] // [3, 4]

// j is 0
arr[1][0] // 3
// j is 1
arr[1][1] // 4

...
```

This example is pretty simple, but `arr[i][j]` can still be difficult to understand without logging multiple things to the console.

One quick improvement we can make is declaring a `subArray` variable in the outer `for` loop and setting it equal to `arr[i]`:

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    const subArray = arr[i];
    for (let j = 0; j < arr[i].length; j++) {
      product *= arr[i][j];
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

Then just make a few tweaks to the code to use the new `subArray` variable instead of `arr[i]`:

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    const subArray = arr[i];
    for (let j = 0; j < subArray.length; j++) {
      product *= subArray[j];
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

That should be everything you need to know about multi-dimensional arrays and nested `for` loops. Now get out there and iterate with the best of 'em!


---
title: 'JavaScript Loops Explained: For Loop, While Loop, Do...while Loop, and More'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-15T21:53:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-loops-explained-for-loop-for
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c92740569d1a4ca32f7.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Loops are used in JavaScript to perform repeated tasks based on a condition.
  Conditions typically return true or false. A loop will continue running until the
  defined condition returns false.

  for Loop

  Syntax

  for (initialization; condition; finalExpre...'
---

Loops are used in JavaScript to perform repeated tasks based on a condition. Conditions typically return `true` or `false`. A loop will continue running until the defined condition returns `false`.

## `for` Loop

### **Syntax**

```js
for (initialization; condition; finalExpression) {
  // code
}

```

The `for` loop consists of three optional expressions, followed by a code block:

* `initialization` - This expression runs before the execution of the first loop, and is usually used to create a counter.
* `condition` - This expression is checked each time before the loop runs. If it evaluates to `true`, the `statement` or code in the loop is executed. If it evaluates to `false`, the loop stops. And if this expression is omitted, it automatically evaluates to `true`.
* `finalExpression` - This expression is executed after each iteration of the loop. This is usually used to increment a counter, but can be used to decrement a counter instead.

Any of these three expressions or the the code in the code block can be omitted.

`for` loops are commonly used to run code a set number of times. Also, you can use `break` to exit the loop early, before the `condition` expression evaluates to `false`.

### **Examples**

1. Iterate through integers from 0-8:

```js
for (let i = 0; i < 9; i++) {
  console.log(i);
}

// Output:
// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
```

2. Use `break` to exit out of a `for` loop before `condition` is `false`:

```js
for (let i = 1; i < 10; i += 2) {
  if (i === 7) {
    break;
  }
  console.log('Total elephants: ' + i);
}

// Output:
// Total elephants: 1
// Total elephants: 3
// Total elephants: 5
```

### Common Pitfall: **Exceeding the** B**ounds of an** A**rray**

When iterating over an array, it's easy to accidentally exceed the bounds of the array.

For example, your loop may try to reference the 4th element of an array with only 3 elements:

```js
const arr = [ 1, 2, 3 ];

for (let i = 0; i <= arr.length; i++) {
  console.log(arr[i]);
}

// Output:
// 1
// 2
// 3
// undefined
```

There are two ways to fix this code: set `condition` to either `i < arr.length` or `i <= arr.length - 1`.

## `for...in` Loop

### Syntax

```js
for (property in object) {
  // code
}
```

The `for...in` loop iterates over the properties of an object. For each property, the code in the code block is executed.

### Examples

1. Iterate over the properties of an object and log its name and value to the console:

```js
const capitals = {
  a: "Athens",
  b: "Belgrade",
  c: "Cairo"
};

for (let key in capitals) {
  console.log(key + ": " + capitals[key]);
}

// Output:
// a: Athens
// b: Belgrade
// c: Cairo

```

### Common Pitfall: **Unexpected Behavior When Iterating Over an Array**

Though you can use a `for...in` loop to iterate over an array, it's recommended to use a regular `for` or `for...of` loop instead.

The `for...in` loop can iterate over arrays and array-like objects, but it may not always access array indexes in order.

Also, the `for...in` loop returns all properties and inherited properties for an array or array-like object, which can lead to unexpected behavior.

For example, this simple loop works as expected:

```js
const array = [1, 2, 3];

for (const i in array) {
  console.log(i);
}

// 0
// 1
// 2

```

But if something like a JS library you're using modifies the `Array` prototype directly, a `for...in` loop will iterate over that, too:

```js
const array = [1, 2, 3];

Array.prototype.someMethod = true;

for (const i in array) {
  console.log(i);
}

// 0
// 1
// 2
// someMethod

```

Though modifying read-only prototypes like `Array` or `Object` directly goes against best practices, it could be an issue with some libraries or codebases.

Also, since the `for...in` is meant for objects, it's much slower with arrays than other loops.

In short, just remember to only use `for...in` loops to iterate over objects, not arrays.

## `for...of` Loop

### Syntax

```js
for (variable of object) {
  // code
}

```

The `for...of` loop iterates over the values of many types of iterables, including arrays, and special collection types like `Set` and `Map`. For each value in the iterable object, the code in the code block is executed.

### Examples

1. Iterate over an array:

```js
const arr = [ "Fred", "Tom", "Bob" ];

for (let i of arr) {
  console.log(i);
}

// Output:
// Fred
// Tom
// Bob

```

2. Iterate over a `Map`:

```js
const m = new Map();
m.set(1, "black");
m.set(2, "red");

for (let n of m) {
  console.log(n);
}

// Output:
// [1, black]
// [2, red]

```

3. Iterate over a `Set`:

```js
const s = new Set();
s.add(1);
s.add("red");

for (let n of s) {
  console.log(n);
}

// Output:
// 1
// red

```

## `while` Loop

### Syntax

```js
while (condition) {
  // statement
}

```

The `while` loop starts by evaluating `condition`. If `condition` evaluates to `true`, the code in the code block gets executed. If `condition` evaluates to `false`, the code in the code block is not executed and the loop ends.

### Examples:

1. While a variable is less than 10, log it to the console and increment it by 1:

```js
let i = 1;

while (i < 10) {
  console.log(i);
  i++;
}

// Output:
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9

```

## `do...while` loop

### Syntax:

```js
do {
  // statement
} while (condition);

```

The `do...while` loop is closely related to `while` loop. In a `do...while` loop, `condition` is checked at the end of each iteration of the loop, rather than at the beginning before the loop runs.

This means that code in a `do...while` loop is guaranteed to run at least once, even if the `condition` expression already evaluates to `true`.

### Example:

1. While a variable is less than 10, log it to the console and increment it by 1:

```js
let i = 1;

do {
  console.log(i);
  i++;
} while (i < 10);

// Output:
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9

```

2. Push to an array, even if `condition` evaluates to `true`:

```js
const myArray = [];
let i = 10;

do {
  myArray.push(i);
  i++;
} while (i < 10);

console.log(myArray);

// Output:
// [10]
```


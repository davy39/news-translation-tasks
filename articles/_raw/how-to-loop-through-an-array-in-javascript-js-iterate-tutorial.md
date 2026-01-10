---
title: How to Loop Through an Array in JavaScript – JS Iterate Tutorial
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-23T19:55:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-loop-through-an-array-in-javascript-js-iterate-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template--3-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: null
seo_desc: 'An array is a single variable used to store elements of different datatypes
  so that they can be accessed through a single variable.

  It is an ordered list of values, and each value is referred to as an element, which
  is specified by an index.

  Knowing ...'
---

An array is a single variable used to store elements of different datatypes so that they can be accessed through a single variable.

It is an ordered list of values, and each value is referred to as an element, which is specified by an index.

Knowing that these single variables contain a list of elements, you might want to create a list of these elements so that you can perform individual functions with them and much more. This is where the loop comes into play.

### Here's an interactive scrim about how to loop through an array in JavaScript:

<iframe src="https://scrimba.com/scrim/co0844e78b1b48c6e5bc87da1?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="480"></iframe>

## What are Loops in JavaScript?

A loop is a type of computer program that allows us to repeat a specific operation a predetermined number of times without having to write that operation individually.

For example, if we have an array and want to output each element in the array, rather than using the index number to do so one by one, we can simply loop through and perform this operation once.

There are numerous methods for looping through an array in JavaScript. In this article, we will go over the most commonly used so you can learn different approaches and understand how they work.

We will use the following array for this article:

```js
const scores = [22, 54, 76, 92, 43, 33];
```

## How to Loop Through an Array with a While Loop in JavaScript

You can use a `while` loop to evaluate a condition that is enclosed in parenthesis `()`. If the condition is `true`, the code inside the `while` loop is executed. If it is `false`, the loop is terminated.

If we want to loop through an array, we can use the `length` property to specify that the loop should continue until we reach the last element of our array.

Let's now use the while loop method to loop through the array:

```js
let i = 0;

while (i < scores.length) {
    console.log(scores[i]);
    i++;
}
```

This will return each element in our array one after the other:

```bash
22
54
76
92
43
33
```

In the loop above, we first initialized the index number so that it begins with `0`. Then the number will continue to increase and output each element until the condition we set returns false, indicating that we have reached the end of the array. When `i = 6`, the condition will no longer be executed because the array's last index is `5`.

## How to Loop Through an Array with a `do…while` Loop in JavaScript

The `do...while` loop is nearly identical to the while loop, except that it executes the body first before evaluating the condition for subsequent executions. This means that the loop's body is always executed at least once.

Let’s perform the same loop with the `do…while` loop to see how it works:

```bash
let i = 0;

do {
    console.log(scores[i]);
    i++;
} while (i < scores.length);
```

This will return each element in our array:

```bash
22
54
76
92
43
33
```

As previously stated, this will always run once before evaluating any condition set. For example, if we set the index `i` to `6` and it is no longer less than `scores.length`, the body of the loop will run first before checking the condition:

```js
let i = 6;

do {
    console.log(scores[i]);
    i++;
} while (i < scores.length);
```

This will return a single `undefined` because we do not have an element in the array of index `6` but as you can see it ran once before stopping.

## How to Loop Through an Array with a for Loop in JavaScript

The `for` loop is an iterative statement that checks for certain conditions and then executes a block of code repeatedly as long as those conditions are met.

We don't need to initialize the index first when using the `for` loop method because the initialization, condition, and iteration are all handled in the bracket, as shown below:

```js
for (let i = 0; i < scores.length; i++) {
    console.log(scores[i]);
}
```

This will return all the elements as other methods have done:

```bash
22
54
76
92
43
33
```

## How to Loop Through an Array with a `for…in` Loop in JavaScript

The `for…in` loop is an easier way to loop through arrays as it gives us the key which we can now use to get the values from our array this way:

```js
for (i in scores) {
    console.log(scores[i]);
}
```

This will output all the elements in our array:

```bash
22
54
76
92
43
33
```

## How to Loop Through an Array with a `for…of` Loop in JavaScript

The `for...of` Loop iterates over iterable objects such as arrays, sets, maps, strings, and so on. It has the same syntax as the `for...in` loop, but instead of getting the `key`, it gets the element itself.

This is one of the easiest methods for looping through an array and was introduced in later versions of JavaScript ES6.

```bash
for (score of scores) {
    console.log(score);
}
```

This gets each element of our array and we no longer need to make use of the index to get each element of our array:

```bash
22
54
76
92
43
33
```

## How to Loop Through an Array with a `forEach` Loop in JavaScript

The array method `forEach()` loop's through any array, executing a provided function once for each array element in ascending index order. This function is known as a callback function.

This is a more advanced method that can do much more than simply loop through each element, but you can also use it to loop through this way:

```js
scores.forEach((score) => {
    console.log(score);
});
```

You can write this in one line this way:

```js
scores.forEach((score) => console.log(score));
```

And this will give us the same output as all previous methods:

```bash
22
54
76
92
43
33
```

## Wrapping Up

In this article, we looked at six different/standard methods for looping through an array.

It is critical that you understand all of these methods and then determine which method is preferable for you, cleaner to use, and easier to read.

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.

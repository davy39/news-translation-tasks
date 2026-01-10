---
title: JavaScript Random Number – How to Generate a Random Number in JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-08-03T19:29:55.000Z'
originalURL: https://freecodecamp.org/news/javascript-random-number-how-to-generate-a-random-number-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-josh-sorenson-1714208.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When working with a JavaScript program, there may be times when you will
  need to generate a random number.

  For example, you may want to generate a random number when developing a JavaScript
  game, such as a number guessing game.

  JavaScript has many bu...'
---

When working with a JavaScript program, there may be times when you will need to generate a random number.

For example, you may want to generate a random number when developing a JavaScript game, such as a number guessing game.

JavaScript has many built-in methods for working with numbers and performing mathematical calculations. One of those methods is the `Math.random()` method.

In this article, you will learn how to use the `Math.random()` method to retrieve random numbers.

Here is what we will cover:

1. [Introduction to the `Math` object](#intro)
2. [`Math.random()` syntax breakdown](#syntax)
    1. [How to generate a random decimal with a specified `max`](#max)
    2. [How to generate a random decimal with a specified `min` and `max` range](#range)
    3. [How to generate a random integer with a specified `max`](#integer-max)
    4. [How to generate a Random integer with a specified `max` inclusive](#max-inclusive)
    5. [How to generate a random integer with a specified `min` and `max` inclusive range](#range-inclusive)

## How To Use Math in JavaScript - An Introduction to the `Math` Object <a name="intro"></a>

JavaScript has the `Math` built-in static object, which allows you to perform mathematical calculations and operations.

The `Math` object has a few built-in methods that make performing those operations much more accurate.

The general syntax for the `Math` object methods is the following:

```
Math.methodName(number);
```

Some of the most popular methods are:

- `Math.round()`
- `Math.ceil()`
- `Math.floor()`
- `Math.random()`

Let's go over some examples of how to implement those methods.

If you want to want to round a number to its nearest integer, use the `Math.round()` method:

```js
console.log(Math.round(6.2)); // 6

console.log(Math.round(6.3)); // 6

console.log(Math.round(6.5)); // 7

console.log(Math.round(6.8)); // 7
```

If you want to round a number **up** to its nearest integer, use the `Math.ceil()` method:

```js
console.log(Math.ceil(6.2));  // 7

console.log(Math.ceil(6.3));  // 7

console.log(Math.ceil(6.5));  // 7

console.log(Math.ceil(6.8));  // 7
```

If you want to round a number **down** to its nearest integer, use the `Math.floor()` method:

```js
console.log(Math.floor(6.2));  // 6

console.log(Math.floor(6.3));  // 6

console.log(Math.floor(6.5));  // 6

console.log(Math.floor(6.8)); // 6
```

If you want to generate a **random** number, use the `Math.random()` method:

```js
console.log(Math.random());

// You will not get the same output

//first time running the program:
// 0.4928793139100267 

//second time running the program:
// 0.5420802533292215

// third time running the program:
// 0.5479835477696466
```

## What Is The `Math.random()` Method in JavaScript? - A Syntax Breakdown <a name="syntax"></a>

The syntax for the `Math.random()` method is the following:

```js
Math.random();
```

The method does not take any parameters.

By default, the method returns a value that is a **random decimal (or floating point)** number between `0` and `1`. 

Something to note about this is that `0` is inclusive, whereas `1` is *not* inclusive. 

So, it will return a value greater than or equal to `0` and always less than and never equal to `1`.

### How To Generate A Random Decimal With A Specified `max` Limit Using `Math.random()` in JavaScript <a name="max"></a>

As you have seen so far, by default, the numbers `Math.random()` generates are small. 

What if you want to generate a random decimal number that starts from, and includes, `0` and is also *greater* than `1`? For this, you  specify a **max** number.

Specifically, you will need to multiply this `max` number with the random number from `Math.random()`.

For example, if you want to generate a random number between `0` and `10` you would do the following:

```js
console.log(Math.random() * 10);

// You won't get the same output
//9.495628210218175
```

In the example above, I multiplied the `max` number (`10`), which will act as a limit, with the resulting number from `Math.random()`.

Keep in mind that in this case, the random number will be between `0` and `10` - this means greater than or equal to `0` and less than and never equal to `10`.

### How To Generate A Random Decimal With A Specified `min` and `max` Range Using `Math.random()` in JavaScript <a name="range"></a>

What if you want to generate a random decimal number between a range of numbers that you specify? 

You saw in the previous section how to specify a `max`, but what if you *don't* want the range to start from `0` (which is the default starting range)? To do this, you can also specify a `min`.

The general syntax for generating a decimal between two values (or range) looks something similar to this:

```
Math.random() * (max - min) + min;
```

Le'ts take the following example:

```js
// specify a minimum - where the range will start
let min = 20.4;

// specify a maximum - where the range will end
let max = 29.8;
```

I created two variables, `min` and `max` - where `min` will be the smallest number and `max` the biggest number in the range.

Next, I generate a random number within that range using the syntax you saw earlier on:

```js
let min = 20.4;
let max = 29.8;

let randomNum = Math.random() * (max - min) + min;

console.log(randomNum);

// You won't get the same output
// 23.309418058783486
```

Something to note here is that `min` is inclusive, so the random number will be greater than or equal to `20.4`, whereas `max` is *not* inlcusive, so the result will always be a number that is less than and never equal to `29.8`.

### How To Generate A Random Integer With A Specified `max` Limit Using `Math.random()` in JavaScript <a name="integer-max"></a>

So far, you have seen how to generate random *decimal* numbers. 

That said, there is a way to generate random *whole* numbers using `Math.random()`. 

You will need to pass the result of the `Math.random()` calculation to the `Math.floor()` method you saw earlier.

The general syntax for this is the following:

```
Math.floor(Math.random());
```

The `Math.floor()` method will round down the random decimal number to the nearest whole number (or integer).

On top of that, you can specify a `max` number. 

So, for example, if you wanted to generate a random number between `0` and `10`, you would do the following:

```js
console.log(Math.floor(Math.random() * 10));

// You won't get the same output
// 0
```

In this example, I multiplied the `max` number (which is `10` in this case) with the result from `Math.random()` and passed the result of this calculation to `Math.floor()`.

Something to note here is that the random number will be between `0` inclusive and `10` exclusive. So, the numbers can be greater than or equal to `0` and less than and never equal to `10`.

### How To Generate A Random Integer With A Specified `max` Inclusive Limit Using `Math.random()` in JavaScript <a name="max-inclusive"></a>

In the example from the previous section, I generated a random number between the numbers `0` (inclusive) and `10` (exclusive).

So far, you have seen that you cannot generate a random number equal to the specified `max`.

What if you want to generate a random number that includes the specified max?

The solution to this is to add `1` during the calculation.

So, let's revisit the code from the previous section:

```js
console.log(Math.floor(Math.random() * 10));
```

You would now re-write the code like so:

```js
console.log(Math.floor(Math.random() * 10) + 1);

// You will not get the same output
// 10
```

Something to note here is that this code will generate a random integer between `1`(not `0`) and `10` - including `10`.

### How To Generate A Random Integer With A Specified `min` and `max` Inclusive Range Using `Math.random()` in JavaScript <a name="range-inclusive"></a>

So far, you have seen how to generate a random integer with an inclusive `max` you specify.

As you saw in the example above, the code to make the `max` number inclusive used the number `1` as the starting number and not `0`.

That said, there is a way for you to specify an inclusive range of numbers. For this, you need to specify a `min` and `max`.

In a previous section, you saw how to generate a random number between a specified range, and the code is similar. The only change is that you pass the result to the `Math.floor()` method to round down the decimal to the nearest integer.

So, the general code is the following:

```
Math.floor(Math.random() * (max - min) + min);
```

To make that range *inclusive*, you would do the following:

```
console.log(Math.floor(Math.random() * (max - min + 1)) + min);
```

So, to generate a random number between the numbers `0` (inclusive) *and* `10` (inclusive), you would write the following:

```js
let min = 0;
let max = 10;

console.log(Math.floor(Math.random() * (max - min + 1)) + min);

//You will not get the same output
// 0
```

## Conclusion

And there you have it! You now know how the `Math.random()` method works and some ways you can use it.

To learn more about JavaScript, head to freeCodeCamp's [JavaScript Algorithms and Data Structures Certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/).

It's a free, well-thought-out, and structured curriculum where you will learn interactively. In the end, you will also build 5 projects to claim your certification and solidify your knowledge.

Thanks for reading!



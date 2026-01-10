---
title: Destructuring in JavaScript – How to Destructure Arrays and Objects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-20T18:27:28.000Z'
originalURL: https://freecodecamp.org/news/destructuring-patterns-javascript-arrays-and-objects
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/destructuring-arrays-and-objects-image.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Alvin Okoro

  Working with JavaScript arrays and objects can be more fun if you destructure them.
  This helps when you''re fetching stored data.

  In this article, you will learn how you can take destructuring to the next level
  in JavaScript arrays and ...'
---

By Alvin Okoro

Working with JavaScript arrays and objects can be more fun if you destructure them. This helps when you're fetching stored data.

In this article, you will learn how you can take destructuring to the next level in JavaScript arrays and objects.

### Table of contents:

* What is an array?
* What is an object?
* What it means to destructure in JavaScript
* Destructuring in Arrays
* Destructuring in Objects

## What is an Array in JavaScript?

In JavaScript, an array is a single variable that stores multiple elements. It is a collection of data. We can declare an array in two different ways, which are:

```js
// Method 1
const firstArray = ["JavaScript", "Python", "Go"];

// Method 2
const secondArray = new Array(3);
secondArray[0] = "JavaScript";
secondArray[1] = "Python";
secondArray[2] = "Go";

```

In method 1, you can initialize while declaring your array. In method 2, you declare your array with the number of elements to be stored before initializing.

## What is an Object in JavaScript? 

In JavaScript, an object is a collection of properties, and a property is an association between a name (or _key_) and a value. 

Writing an object in JavaScript looks somehow similar to an array, but instead we use curly braces or moustaches to create them. Let's look at the code below showing a car object with its properties:

```js
const car = {
  name: "Toyota",
  color: "Black",
  year: 2022,
  engineType: "Automatic",
};

```

Notice that what makes up an object is a key followed by its value.

Now that you know the basics of what JavaScript arrays and objects look like, let's talk more about destructuring.

## What is Destructuring in JavaScript?

Imagine you want to pick out some shoes from your collection, and you want your favorite blue ones. The very first thing you have to do is to search through your collection and unpack whatever you have there.

Now destructuring is just like that approach you took when looking for your shoes. Destructuring is the act of unpacking elements in an array or object. 

Destructuring not only allow us to unpack elements, it also gives you the power to manipulate and switch elements you unpacked depending on the type of operation you want to perform.

Let's see how destructuring works in arrays and objects now.

## Destructuring in Arrays

To destructure an array in JavaScript, we use the square brackets [] to store the variable name which will be assigned to the name of the array storing the element.

```js
const [var1, var2, ...] = arrayName;

```

The ellipses right after the `var2` declared above simply means that we can create more variables depending on how many items we want to remove from the array.

### How to Assign Variables With Destructuring

Now, let's say we have an array of 6 colors but we want to get just the first 2 colors in the array. We can use destructuring to get what we want.

Let's take a look at it now:

```js
const colorArr = ["red", "yellow", "blue", "green", "white", "black"];

const [first, second] = colorArr;
console.log(first, second);

// red, yellow

```

![Image](https://www.freecodecamp.org/news/content/images/2022/01/first.png)

When we run the above code, we should have red and yellow logged to the console. Awesome!

### How to Swap Variables with Destructuring

Now that you know how to assign variables with destructuring, let's look at how you can use destructuring to quickly swap variable values.

Say we have an array of two elements, `"food"` and `"fruits"`, and we use destructuring to assign those values to the variables `positionOne` and `positionTwo`:

```js
const edibles = ["food", "fruits"];

let [positionOne, positionTwo] = edibles;
console.log(positionOne, positionTwo);

// food, fruits

```

If we later want to swap the values of `positionOne` and `positionTwo` without destructuring, we would need to use another variable to temporarily hold the value of one of the current variables, then perform the swap.

For example:

```js
const edibles = ["food", "fruits"];

let [positionOne, positionTwo] = edibles;
const temp = positionOne;

positionOne = positionTwo;
positionTwo = temp;
console.log(positionOne, positionTwo);

// fruits, food

```

But with destructuring, we could swap the values of `positionOne` and `positionTwo` really easily, without having to use a temporary variable:

```js
const edibles = ["food", "fruits"];

let [positionOne, positionTwo] = edibles;
[positionOne, positionTwo] = [positionTwo, positionOne];
console.log(positionOne, positionTwo);

// fruits, food

```

![Image](https://www.freecodecamp.org/news/content/images/2022/01/second.png)

Note that this method of swapping variables doesn't mutate the original array. If you log `edibles` to the console, you'll see that its value is still `["food", "fruits"]`.

### How to Mutate Arrays with Destructuring

Mutating means changing the form or value of an element. A value is said to be mutable if it can be changed. With the help of destructing in arrays, we can mutate arrays themselves.

Say we have the same `edibles` array, and that we want to mutate the array by swapping the order of `"food"` and `"fruits"`.

We can do that with destructuring, similar to the way we swapped the values of two variables before:

```js
const edibles = ["food", "fruits"];

[edibles[0], edibles[1]] = [edibles[1], edibles[0]];
console.log(edibles);

// ["fruits", "food"]

```

### Destructuring in Objects

When destructuring objects, we use curly braces with the exact name of what we have in the object. Unlike in arrays where we can use any variable name to unpack the element, objects allow just the use of the name of the stored data.

Interestingly, we can manipulate and assign a variable name to the data we want to get from the object. Let's see all of that now in code.

```js
const freeCodeCamp = {
  frontend: "React",
  backend: "Node",
  database: "MongoDB",
};

const { frontend, backend } = freeCodeCamp;
console.log(frontend, backend);

// React, Node

```

![Image](https://www.freecodecamp.org/news/content/images/2022/01/3-4.png)

Logging what we have to the console shows the value of frontend and backend. Let's now see how to assign a variable name to the object we want to unpack.

```js
const freeCodeCamp = {
  frontend: "React",
  backend: "Node",
  database: "MongoDB",
};

const { frontend: courseOne, backend: courseTwo } = freeCodeCamp;
console.log(courseOne, courseTwo);

// React, Node

```

![Image](https://www.freecodecamp.org/news/content/images/2022/01/4-2.png)

As you can see, we have `courseOne` and `courseTwo` as the names of the data we want to unpack. 

Assigning a variable name will always help us keep our code clean, especially when it comes to working with external data when we want to unpack and reuse it across our code.

## Wrapping Up

You've now learned how to work with destructing in arrays and objects. You've also learned how to switch the positions of elements in arrays.

So what next? Try practicing and take your destructuring abilities to next level.


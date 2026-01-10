---
title: Higher Order Functions in JavaScript – Reach New Heights in Your JS Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-12T21:44:55.000Z'
originalURL: https://freecodecamp.org/news/higher-order-functions-in-javascript-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/spacex-uj3hvdfQujI-unsplash.jpg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dave Gray

  What is a Higher Order Function?

  Let''s look at the name, and consider how we talk about things.

  We dig down into the details, but sometimes we want a high level view of things.

  This high level view indicates more abstraction. We go down ...'
---

By Dave Gray

## What is a Higher Order Function?

Let's look at the name, and consider how we talk about things.

We dig _down_ into the details, but sometimes we want a _high_ level view of things.

This high level view indicates more abstraction. We go down into details, but we elevate into a more abstract viewpoint.

Higher Order Functions are exactly that: A higher level of abstraction than your typical functions.

### So how can we define a Higher Order Function?

Higher Orders Functions are functions that perform operations on other functions.

In this definition, _operations_ can mean taking one or more functions as an argument OR returning a function as the result. It doesn't have to do both. Doing one or the other qualifies a function as a higher order function.

## Let's look at an example of a higher order function

Without a higher order function, if I want to add one to each number in an array and display it in the console, I can do the following:

```
const numbers = [1, 2, 3, 4, 5];

function addOne(array) {
  for (let i = 0; i < array.length; i++) {
    console.log(array[i] + 1);
  }
}

addOne(numbers);

```

The function `addOne()` accepts an array, adds one to each number in the array, and displays it in the console. The original values remain unchanged in the array, but the function is doing something for each value.

However, using what may be the most common higher order function, `forEach()`, we can simplify this process:

```
const numbers = [1, 2, 3, 4, 5];

numbers.forEach((number) => console.log(number + 1));

```

**Whoa.**

We've abstracted the function definition and call in the original code above to just one line!

We apply `forEach()` to the array named "numbers." There is an anonymous function at the beginning of `forEach()` that accepts each element of the array - one at a time. 

With the array named numbers, it makes sense to name each element of the array "number" although we could have named it "element" or "el" or even "whatever".

The anonymous arrow function logs the value of the number + 1 to the console.

The higher order function `forEach()` applies a function to each element of an array.

## Another higher order function example

Without a higher order function, if I wanted to create a new array that only has the odd numbers from the numbers array, I could do the following:

```
const numbers = [1, 2, 3, 4, 5];

function isOdd(array, oddArr = []) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] % 2 !== 0) {
      oddArr.push(array[i]);
    }
  }
  return oddArr;
}

const oddArray = isOdd(numbers);
console.log(oddArray);

```

The function `isOdd()` accepts an array and has a second optional parameter for an array. If not provided, the array has a default value of an empty array. 

The function checks each number in the array to see if it is an odd number. If the number is odd, it adds it to the array from the second parameter. After all numbers are checked, the array from the second parameter is returned.

So yeah, that's a lot to keep track of.

If we use the higher order function, `filter()`, we can abstract so much:

```
const numbers = [1, 2, 3, 4, 5];

const oddArray = numbers.filter((number) => number % 2 !== 0);
console.log(oddArray);

```

**YES!**

Pardon me for getting excited, but that is a big improvement.

We start by defining the new array `oddArray` because applying `filter()` will create a new array. The higher order function will return each element that meets the condition set within the anonymous function it receives. The anonymous function is once again applied to each element in the numbers array.

## Since We're On A Roll – Another Higher Order Function Example

We've come this far, and I think you're starting to see why higher order functions are so good!

Let's look at another example...

Back in our `forEach()` example, we added one to each number in the array and logged each value to the console. But what about creating a new array with those new values instead? Without a higher order function, I could do the following:

```
const numbers = [1, 2, 3, 4, 5];

function addOneMore(array, newArr = []) {
  for (let i = 0; i < array.length; i++) {
    newArr.push(array[i] + 1);
  }
  return newArr;
}

const newArray = addOneMore(numbers);
console.log(newArray);

```

The function `addOneMore()` once again accepts an array and has an array as a second parameter which has a default value of empty. One is added to each element of the existing numbers array and the result is pushed to the new array which is returned.

We abstract this away with the higher order function, `map()`:

```
const numbers = [1, 2, 3, 4, 5];

const newArray = numbers.map((number) => number + 1);
console.log(numbers);

```

We start by defining the newArray because `map()` creates a new array. Like `forEach()`, `map()` applies an anonymous function to each element of the numbers array. However, `map()` creates a new array in the process.

## Just One More Example

What if we wanted to find the total of all values in the numbers array?

Without a higher order function, I could do this:

```
const numbers = [1, 2, 3, 4, 5];

function getTotalValue(array) {
  let total = 0;
  for (let i = 0; i < array.length; i++) {
    total += array[i];
  }
  return total;
}

const totalValue = getTotalValue(numbers);
console.log(totalValue);

```

The function `getTotalValue()` accepts an array, defines the total variable as equal to zero, and loops through the array while adding each element to the total variable. Finally, it returns the total.

With the higher order function `reduce()`, this process can yet again be abstracted away:

```
const numbers = [1, 2, 3, 4, 5];

const totalValue = numbers.reduce((sum, number) => sum + number);
console.log(totalValue);

```

The higher order function `reduce()` expects two parameters in the anonymous function within. 

The first parameter is an accumulator and the second parameter is an element from the numbers array. 

The accumulator parameter (sum in the example above) keeps track of the total as `reduce()` applies the anonymous function to each element of the array.

## Conclusion

Higher Order Functions provide a higher level of abstraction for functions.

They have the potential to take your JavaScript code to new heights!

I'll leave you with a tutorial from my YouTube channel that applies Higher Order Functions to JSON data.

%[https://youtu.be/7BeT6lsudL4]





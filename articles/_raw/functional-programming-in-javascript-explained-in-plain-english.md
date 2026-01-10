---
title: Functional Programming in JavaScript Explained in Plain English
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-05T16:45:41.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-in-javascript-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/blog1.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Joel P. Mugalu

  One of the hardest things you have to do in programming is control complexity. Without
  careful consideration, a program''s size and complexity can grow to the point where
  it confuses even the creator of the program.

  In fact, as one a...'
---

By Joel P. Mugalu

One of the hardest things you have to do in programming is control complexity. Without careful consideration, a program's size and complexity can grow to the point where it confuses even the creator of the program.

In fact, as one author put it:

> "The art of programming is the skill of controlling complexity" - Marijn Haverbeke

In this article we will break down a major programming concept. This programming concept can help you keep complexity under control and write better programs.

By the end of this article, you will know what functional programming is, the types of functions there are, the principles of functional programming, and have a deeper understanding of Higher Order functions.

I assume that you already have pre-existing knowledge of the basics of functions. The fundamental concepts of functions will not be covered in this article.

If you want a quick review of functions in JavaScript, then I've written a detailed article [here](https://dev.to/codingknite/javascript-functions-broken-down-4fgh).

## What is Functional Programming?

Functional programming is a programming paradigm or style of programming that relies heavily on the use of pure and isolated functions.

Just as you might have guessed from the name, the use of functions is the main component of functional programming. But, merely using functions doesn't translate to functional programming.

In functional programming, we use pure functions, which are functions that don't have side effects. I will explain what all of this means.

Before diving deeper into the article, let us understand some of the terminology and types of functions there are.

## Types of Functions

There are four main types of functions.

### First Class Functions

In JavaScript all functions are first class functions. That means they can be treated like any other variable.

First class functions are functions that can be assigned as values to variables, returned from other functions, and passed as arguments to other functions.

Consider this example of a function passed to a variable:

```javascript
const helloWorld = () => {
	console.log("Hello, World"); // Hello, World
};
helloWorld();

```

### Callback Functions

Callback functions are functions that are passed into other functions as arguments and are called by the function in which they are passed.

Simply, callback functions are functions that we write as arguments in other functions. We can't invoke callback functions. They are invoked when the main function in which they were passed as arguments is called.

Let's look at an example:

```javascript
const testValue = (value, test) => {
    if (test(value)) {
        return `${value} passed the test`;
    } else 
        return `${value} did not pass the test`;
};
const checkString = testValue('Twitter',  string  =>  typeof  string === 'string');
checkString; // Twitter passed the test

```

`testValue` is a function that accepts a  value and a callback function `test`  which returns "value passed the test" if the value returns true when passed into the callback function.

In this case, the callback function is the second argument we passed into the `testValue` function. It is invoked when the `testValue` function is called.

### Higher Order Functions

Higher order functions are functions that receive other functions as arguments or return a function.

In this article, am going to further elaborate on higher order functions and why they are such a powerful provision. For now, all you need to know is that these types of functions receive other functions as arguments or return functions.

### Asynchronous Functions

Asynchronous functions are functions that don't have a name and cannot be reused. These functions are normally written when we need to carry out something once and in only one place.

A perfect example of an asynchronous function is what we wrote earlier in the article.

```javascript
const checkString = testValue('Twitter',  value  =>  typeof  value === 'string');
checkString;

// Refer to previous code snippet
```

`checkString` is a variable whose value is a function. We pass two arguments into this function. 

`'Twitter'` is the first argument and the second is an asynchronous function. This function has no one name and has only one task: to check whether the given value is a string.

![Principles Meme](https://memegenerator.net/img/instances/81322055.jpg)

## Principles of Functional Programming

Earlier in the article I alluded to the fact that merely using functions does not translate to functional programming.

There are some principles we need to understand if our programs are to qualify for the functional programming standard. Let's look at those.

### Avoid Mutations and Side effects.

The first principle of functional programming is to avoid changing things. A function should not change anything such as a global variable.

This is very important because changes often lead to bugs. If a function changes a global variable, for example, it might lead to unexpected behavior in all the places where that variable is used.

The second principle is that a function must be pure, meaning it has no side effects. In functional programming, changes that are made are called mutations, and the outcomes are called side effects.

A pure function does neither of the two. A pure function will always have the same output for the same input.

If a function depends on a global variable, that variable should be passed to the function as an argument. This allows us to obtain the same output for the same input.

Here is an example:

```javascript
const legalAgeInTheUS = 21;
const checkLegalStatus = (age, legalAge) => {
    return age >= legalAge ? 'Of legal age.' : 'Not of legal age.';
};
const johnStatus = checkLegalStatus(18, legalAgeInTheUS);
johnStatus; // Not of legal age
legalAgeInTheUS; // 21

```

### Abstraction

Abstractions hide details and allow us to talk about problems at a higher level without describing all the implementation details of the problem.

We use abstractions in all almost all aspects of our lives, especially in speech.

For example, instead of saying _"I'm going to exchange money for a machine that once plugged in displays moving images accompanied with sound"_, you are most likely to say _"I'm going to buy a television"_.

In this case **buy** and **television** are abstractions. These forms of abstractions make speech a lot more easier and reduce the chances of saying the wrong thing.

But you'll agree with me that before using abstract terms like **buy** you need to first understand the meaning of the term and the problem it abstracts.

Functions allow us to achieve something similar. We can create functions for tasks that we are most likely to repeat again and again. Functions allows us to create our own abstractions.

On top of creating our own abstractions, some functions have already been created for us to abstract tasks that we are most likely to do time and again.

So we are going to look at some of these higher order functions that already exist to abstract repetitive tasks.

### Filtering Arrays

When working with data structures like arrays, we are most likely to find ourselves in a situation where we are only interested in certain items in the array.

To obtain these items we can easily create a function to do the task:

```javascript
function filterArray(array, test) {
    const filteredArray = [];
    for (let item of array) {
        if (test(item)) {
            filteredArray.push(item);
        }
    }
    return filteredArray;
};
const mixedArray = [1, true, null, "Hello", undefined, "World", false];
const onlyStrings = filterArray(mixedArray, item => typeof item === 'string');
onlyStrings; // ['Hello', 'World']

```

`filterArray` is a function that accepts an array and a callback function. It loops through the array and adds the items that pass the test in the callback function into an array called `filteredArray`.

Using this function we are able to filter an array and return items that we're interested in, such as in the case of `mixedArray`.

Imagine if we had 10 different programs and in each program we needed to filter an array. Sooner or later it would become extremely tiresome to rewrite the same function over and over again.

Luckily someone already thought about this. Arrays have a standard `filter` method. It returns a new array with the items in the array it receives that pass the test that we provide.

```javascript
const mixedArray = [1, true, null, "Hello", undefined, "World", false];
const stringArray = mixedArray.filter(item => typeof item === 'string')
stringArray; // ['Hello', 'World']

```

Using the standard filter method we were able to achieve the same results we did when we defined our own function in the previous example. So, the filter method is an abstraction of the first function we wrote.

### Transforming Array Items With Map

Imagine another scenario where we have an array of items but we would like to perform a certain operation on all the items. We can write a function to do this for us:

```javascript
function transformArray(array, test) {
    const transformedArray = [];
    for (let item of array) {
        transformedArray.push(test(item));
    }
    return transformedArray;
};
const ages = [12, 15, 21, 19, 32];
const doubleAges = transformArray(ages, age => age * 2);
doubleAges; // [24, 30, 42, 38, 64];

```

Just like that we  have created a function that loops through any given array and transforms all the items in the array based on the callback function the we provide.

But again this would grow tedious if we had to rewrite the function in 20 different programs.

Again, someone thought about this for us, and luckily arrays have a standard method called `map` which does the same exact thing. It applies the callback function on all the items in the given array and then it returns a new array.

```javascript
const ages = [12, 15, 21, 19, 32];
const doubleAges = ages.map(age => age * 2);
doubleAges; // [24, 30, 42, 38, 64];

```

### Reducing Arrays with Reduce

Here's another scenario: You have an array of numbers, but you would like to compute the sum of all these numbers and return it. Of course you can write a function to do this for you.

```javascript
function reduceArray(array, test, start) {
    let sum = start;
    for (let item of array) {
        sum = test(sum, item)
    }
    return sum;
}
let numbers = [5, 10, 20];
let doubleNumbers = reduceArray(numbers, (a, b) => a + b, 0);
doubleNumbers; // 35

```

Similar to the previous examples we just looked at, arrays have a standard `reduce` method that has the same logic as the function we just wrote above.

The reduce method is used to reduce an array to a single value based on the callback function that we provide. It also takes an optional second argument which specifies where we want the operation in the callback to start from.

The callback function we provide in the reduce function has two parameters. The first parameter is the first item in the array by default. Otherwise it is the second argument we provide into the reduce method. The second parameter is the current item in the array.

```javascript
let numbers = [5, 10, 20];
let doubleNumbers = numbers.reduce((a, b) => a + b, 10);
doubleNumbers;  // 45

//The above example uses the reduce method to add all the items in the array starting from 10.
```

## Other Useful Array Methods

### Array.some()

All arrays have the `some` method which accepts a callback function. It returns `true` if **any** element in the array passes the test given in the callback  function. Otherwise it returns `false`:

```javascript
const numbers = [12, 34, 75, 23, 16, 63]
console.log(numbers.some(item => item < 100)) // true
```

### Array.every()

The every method is the opposite of the some method. It also accepts a callback function and returns `true` if **all** the items in the array pass the test given in the callback  function. Otherwise it returns `false`:

```javascript
const numbers = [12, 34, 75, 23, 16, 63]
console.log(numbers.every(item => item < 100)) // true
```

### Array.concat()

The `concat` method, short for concatenate, is a standard array method that concatenates or joins two arrays and returns a new array:

```javascript
const array1 = ['one', 'two', 'three'];
const array2 = ['four', 'five', 'six'];
const array3 = array1.concat(array2);
array3; // [ 'one', 'two', 'three', 'four', 'five', 'six' ]
```

### Array.slice()

The `slice` method is an array method which copies the items of an array from a given index and returns a new array with the copied items. The `slice` method accepts two arguments.

The first argument receives the index from which to begin copying. The second argument receives the index from which to stop copying. It returns a new array with the copied items from the starting index (exclusive) to the final index (inclusive).

Note however that the slice method does not use zero indexing. So the index of the first array item is 1 not 0:

```javascript
const numbers = [1,2,3,4,5,7,8];
console.log(theArray.slice(1, 4)); // [ 2, 3, 4 ]

```

## Conclusion

I hope you enjoyed reading this article and learned something new at the same time. 

There are lots of array and string methods that I didn't mention in the article. If you wish, take some time to do some research on those methods.

_If you would like to connect with me or to just say hi? feel free to do so via  [Twitter](http://twitter.com/joeepm) . I also share interesting tips and resources  for developers._ ?


---
title: 'Intro to JavaScript APIs: The Reduce Function'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-19T12:18:14.000Z'
originalURL: https://freecodecamp.org/news/applications-of-the-reduce-function-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dbc740569d1a4ca395f.jpg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Samuel Omole

  As the year begins, I have decided to make a series of articles that explain the
  various APIs (Application Programming Interfaces) in the JavaScript language. In
  each article we will break down a commonly used function in JavaScript a...'
---

By Samuel Omole

As the year begins, I have decided to make a series of articles that explain the various APIs (Application Programming Interfaces) in the JavaScript language. In each article we will break down a commonly used function in JavaScript and try to go through its various applications.

The first function we will be going through is the '**Reduce**' higher-order function. This is mainly because, out of all the JS array methods, it took me a bit of time to understand how the Reduce function works.

This article assumes that the reader understands other array methods like **Map** and **Filter** because it will help in understanding how **Reduce** works. 

In order to fully grasp the idea behind Reduce**,** we will look at a few examples of simple solutions using **for** loops and then implement those same solutions using the Reduce function. Then we will look at some more advanced use cases for the Reduce function.

## Example 1

The first example we will look at is a common one: calculating the sum of items in an array. This requires a simple solution, and using a **for** loop should look like this:

```javascript
const arrayItems = [1,2,3,4,5,6];
let sum = 0;

for (let i = 0; i < arrayItems.length; i++) {
	sum = sum + arrayItems[i];
}
// sum = 21
```

The solution above is pretty straightforward, where we add each item in the array and store the result in the `sum` variable. So the next step is to implement the same solution using **Reduce**, which should look like the code below:

```javascript
const arrayItems = [1,2,3,4,5,6];

const sum = arrayItems.reduce(function(accumulator, currentItemInArray){
	accumulator = accumulator + currentItemInArray;
    return accumulator;
}, 0);

// sum = 21
```

Looking at the two examples above it's pretty obvious that the **for** loop example seems simpler, and this has been the cause of some arguments in the ecosystem. But this example is overkill, and we are only using it make it easy to understand how the Reduce function works, so let's work through the example.

We need to, first of all, understand what the Reduce function is. It is a method that exists for every JavaScript Array. It enables us to loop through each item in the array and perform a function on each of those items. 

This is pretty similar to the behavior of the **Map** function, but it has a twist–it allows us to return any value from our function in a particular iteration, which will then exist as a parameter (argument) in that function in the next iteration (that value is commonly known as the **accumulator**).

To explain further, the Reduce function takes 2 arguments:

* Callback function: This is a function that contains 4 parameters typically. But right now we are only concerned with the first, the accumulator, and the second which is the current item in the array during that iteration.
* Initial value: This is the initial value of the accumulator when the iteration starts. In the example above the value is 0, which means the initial value of the accumulator will be 0.

Back to our example:

```javascript
const arrayItems = [1,2,3,4,5,6];

const sum = arrayItems.reduce(function(accumulator, currentItemInArray){
	accumulator = accumulator + currentItemInArray;
    return accumulator;
}, 0);

// sum = 21
```

It can be further broken out into the callback function and the initial value:

```javascript
const arrayItems = [1,2,3,4,5,6];

function callbackFunction(accumulator, currentItemInArray){
    accumulator = accumulator + currentItemInArray;
    return accumulator;
}

const initialValue = 0;

const sum = arrayItems.reduce(callbackFunction, initialValue);

// sum = 21
```

The tricky part for me was understanding how the accumulator works. To explain it we will go through each iteration in the loop.

### Iteration 1

In the first iteration, since our initial value is 0, our accumulator will have a value of 0. So our function will look like this:

```javascript
const arrayItems = [1,2,3,4,5,6];
// 1 is the current item in the array

function callbackFunction(accumulator = 0, currentItemInArray = 1){
    accumulator = 0 + 1;
    return accumulator // which is 1;
}
```

`callbackFunction` will return a value of 1. This will automatically be used as the next value for the accumulator in the second iteration.

### Iteration 2

```javascript
const arrayItems = [1,2,3,4,5,6];
// 2 is the current item in the array

function callbackFunction(accumulator = 1, currentItemInArray = 2){
    accumulator = 1 + 2;
    return accumulator // which is 3;
}
```

In this iteration, our accumulator will have a value of 1 which was returned in our first iteration. The `callbackFunction` will return a value of 3 in this iteration. This means that our accumulator will have a value of 3 in our third iteration.

### Iteration 3

```js
const arrayItems = [1,2,3,4,5,6];
// 3 is the current item in the array

function callbackFunction(accumulator = 3, currentItemInArray = 3){
    accumulator = 3 + 3;
    return accumulator // which is 6;
}
```

In the third iteration, our accumulator will have a value of 3 which was returned by the `callbackFunction` in iteration 2. The  `callbackFunction` will return a value of 6, which will be used as the value of accumulator in iteration 4. These steps will repeat themselves until we get to the last item in the array which is 6.

As I mentioned before, the example above can be an overkill, so let's look at a problem where using Reduce is more common. (However, this doesn't mean that a **for** loop cannot be used to implement a working solution). 

## Example 2

The second example will involve counting the number of occurrences of each element in an array, for example:

```js
//Given an input
const fruits = ['apples', 'apples', 'bananas', 'oranges', 'apples', 'oranges', 'bananas', 'grapes'];

// should give an output of
const count = { 'apples': 3,'oranges': 2,'bananas': 2, 'grapes': 1 };
```

Let's implement the solution, then go through each iteration and see what is happening:

```js
const fruits = ['apples', 'apples', 'bananas', 'oranges', 'apples', 'oranges', 'bananas', 'grapes'];

function countOccurrence(accumulator, currentFruit){
	const currentFruitCount = accumulator[currentFruit];
    // if the fruit exists as a key in the  object, increment its value, else add the fruit as a key to the object with a value of 1
    
    if(currentFruitCount) {
    	accumulator[currentFruit] = currentFruitCount + 1;
    } else {
    	accumulator[currentFruit] = 1
    }
    
    return accumulator;
}

const initialValue = {};

const count = fruits.reduce(countOccurrence, initialValue);
```

The solution is written to be as verbose a possible so we can understand what is going on in the code. As we did before, let's go through the first few iterations.

### Iteration 1

In the first iteration, since we made our initial value an empty object, the value of `accumulator` will be an empty object. This means that the `countOcurrence` function will look like the code below when it is called:

```js
const fruits = ['apples', 'apples', 'bananas', 'oranges', 'apples', 'oranges', 'bananas', 'grapes'];

// current element is 'apples'

function countOccurrence(accumulator = {}, currentFruit = 'apples'){
    // since currentFruit = 'apples' then accumulator[currentFruit] = accumulator['apples']
    
	const currentFruitCount = accumulator[currentFruit];
    // currentFruitCount will be null since accumulator is an empty object
    
    if(currentFruitCount) {
    	accumulator[currentFruit] = currentFruitCount + 1;
    } else {
        // this block will run since accumulator is empty
        // currentFruit = 'apples'
    	accumulator['apples'] = 1
        // accumulator should look like this: { 'apples': 1 }
    }
    
    return accumulator // which is { 'apples': 1 };
}
```

Since `accumulator` is an empty object, `currentFruitCount` will be `null`. This means that the `else` block will run where a new key (apples) with the value of 1 will be added to the `accumulator`. This will be returned from the function which will be passed as the value of the accumulator in the second iteration.

### Iteration 2

In the second iteration, our `accumulator` will have the value of `{ 'apples': 1 }`, which was returned by the `countOccurrence` function in the first iteration. Then the `countOccurrence` function will look like the code below:

```js
const fruits = ['apples', 'apples', 'bananas', 'oranges', 'apples', 'oranges', 'bananas', 'grapes'];

// current element is 'apples'

function countOccurrence(accumulator = { 'apples': 1 }, currentFruit = 'apples'){
    // since currentFruit = 'apples' then accumulator[currentFruit] = accumulator['apples']
    
	const currentFruitCount = accumulator[currentFruit];
    // currentFruitCount will be 1 
    
    if(currentFruitCount) {
        // this block will run since currentFruitCount is 1
        // currentFruit = 'apples'
    	accumulator['apples'] = 1 + 1;
        // accumulator should look like this: { 'apples': 2 }
    } else {
    	accumulator[currentFruit] = 1
    }
    
    return accumulator // which is { 'apples': 2 };
}
```

Since the `accumulator` contains a key ('apple') with the value of 1, `currentFruit` will be 1, which means the `if` block will be run. In that block the value of the `apple` key will be incremented by 1 making it 2, and this new value will be updated in the accumulator object to make it `{ 'apples' : 2 }` . This value will be returned by the `countOccurrence` function and passed as the value for the accumulator in the third iteration.

### Iteration 3

For our third iteration, `accumulator` has the value of `{ apples: 2 }` which was returned by `countOccurence` during the second iteration. The `countOccurence` function will look like the code below:

```js
const fruits = ['apples', 'apples', 'bananas', 'oranges', 'apples', 'oranges', 'bananas', 'grapes'];

// current element is 'bananas'

function countOccurrence(accumulator = { 'apples': 2 }, currentFruit = 'bananas'){
    // since currentFruit = 'bananas' then accumulator[currentFruit] = accumulator['bananas']
    
	const currentFruitCount = accumulator[currentFruit];
        // currentFruitCount will be null since accumulator doesn't contain 'bananas'
    
    if(currentFruitCount) {
        accumulator[currentFruit] = currentFruitCount + 1;
    } else {
        // this block will run since currentFruitCount is null
        // currentFruit = 'bananas'
    	accumulator['bananas'] = 1
    }
    
    return accumulator // which is { 'apples': 2, 'bananas': 1  };
}
```

This iteration is similar to the first one–since `bananas` doesn't exist in `accumulator` it will be added to the object and given a value of `1` , making `accumulator` look like this: `{ 'apples': 2, 'bananas': 1 }`. This will then become the value of `accumulator` for the fourth iteration.

The process will repeat itself until the Reduce function has iterated through each element in the array.

## Wrapping up

I really hope these examples were clear enough to create a mental model of how the **Reduce** function works. 

If you are reading this and you would like to see more advanced examples (like implementing the `pipe` function) feel free to tweet at me and I'll respond as soon as I can. Also, if you have other examples I would love to see them. Thanks!!!


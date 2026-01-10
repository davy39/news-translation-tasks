---
title: JS For Loop Tutorial – How to Iterate Over an Array in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-01T19:32:45.000Z'
originalURL: https://freecodecamp.org/news/javascript-loop-tutorial-how-to-iterate-over-an-array-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b53740569d1a4ca2b1a.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: null
seo_desc: "By Marty Jacobs\nThis article will provide you with a solid understanding\
  \ of exactly how to iterate over an Array data structure in JavaScript. \nWhether\
  \ you are just beginning to learn JavaScript or are here for a refresher, there\
  \ will be value for yo..."
---

By Marty Jacobs

  
This article will provide you with a solid understanding of exactly how to iterate over an Array data structure in JavaScript. 

Whether you are just beginning to learn JavaScript or are here for a refresher, there will be value for you either way. This article will walk you through one of the most widely used JavaScript concepts.

### What is an array?

```js
let cars = ["Tesla", "Ferrari", "Lamborghini", "Audi"];
```

Above is a JavaScript array used to store multiple values. This is one of the simplest forms of an array. It contains 4 “elements” inside the array, all strings. And as you can see each element is separated by a comma. 

This example array holds different makes of cars, and can be referred to with the `cars` variable.

There are a number of ways we can iterate over this array. JavaScript is incredibly feature-rich, so we have the luxury to choose the best way to solve our problem.

Here’s how we will tackle iterating over arrays in JavaScript:  


1. Highlight 5 common methods to iterate over an array
2. Show some insights into each iterative method
3. Provide some code you can use to test it out, too!

## Traditional For Loop

### What is a For Loop? 

Here's a simple definition of a [For Loop](https://en.wikipedia.org/wiki/For_loop):

> “In computer science, a **for-loop** (or simply **for loop**) is a [control flow](https://en.wikipedia.org/wiki/Control_flow) [statement](https://en.wikipedia.org/wiki/Statement_(programming)) for specifying [iteration](https://en.wikipedia.org/wiki/Iteration), **which allows code to be** [**executed**](https://en.wikipedia.org/wiki/Execution_(computers)) **repeatedly.”**

A for loop is a way to execute code repeatedly. Instead of typing out `console.log(“hi”)` five times, you could wrap it inside a for loop.  
  
In this first example, we will learn how to iterate over the cars array you have seen above, and print out every element. The iterator, or counter, will start at the first index “Tesla” and finish at the last “Audi”. It moves through the array and prints one element at a time.

```js
let cars = ["Tesla", "Ferrari", "Lamborghini", "Audi"];

for(let i = 0; i < cars.length; i++) {
  console.log(cars[i]);
}
```

**Output:**

```
Tesla
Ferrari
Lamborghini
Audi
```

Diving into the code, we pass three options to the for loop

* the iterator variable - `let i = 0;`
* where the iterator should stop - `i < card.length`
* how much to increment the iterator each loop - `i++`

This loop starts us at `0`, increases the variable by one each loop, and stops when we hit the last element in the array.

_The key benefit of the traditional for loop is that you have more control._   
  
It’s possible to access different elements within the array, or iterate through the array in a sophisticated way to solve a complex problem. For example, skipping every other element in the array can be done quite easily with the traditional for loop.

## The forEach method

### What is the forEach method? 

The `forEach` method is used to execute a function for each element of your array. This method is a great choice if the length of the array is “unknown”, or guaranteed to change. This method can be only used with Arrays, Sets, and Maps. 

```js
const amounts = [65, 44, 12, 4];
let doubledAmounts = [];

amounts.forEach(item => {
  doubledAmounts.push(item * 2);
})

console.log(doubledAmounts);
```

The greatest benefit of a `forEach` loop is being able to access each item, even if your array is likely to grow in size. It is a scalable solution for many use-cases and is easier to read and understand than a traditional for loop because we know we will iterate over each element exactly once.

## While loop

### What is a While Loop? 

Here's a simple definition of a While Loop:

> “A **while loop** is a control flow statement that allows code to be executed repeatedly based on a given [Boolean](https://en.wikipedia.org/wiki/Boolean_datatype) condition. The _while_ loop can be thought of as a repeating if statement.**”**

A `while` loop is a way to execute code repeatedly to check if a condition is true or false. So, instead of using a for loop, with a nested if statement, we can use a while loop. Or, if we're not able to find the length of the array, while loops are an excellent choice.

The while loop is often controlled by a counter. In the example below we show a basic while loop iterating through an array. The key is to have control over the while loop you are creating. 

**While Loop Example (Good):**

```js
let i = 0 

while (i < 5) { 
  console.log(i); 
  i++; 
}
```

**Output**: 

```
0
1
2
3
4
```

The while loop's if statement is `i < 5`, or spoken aloud, "i is less than 5". The variable `i` is incremented every time the loop runs.

In simple terms, this means that 1 is added to the variable `i` every time the loop performs a full iteration. On the first iteration, `i` is equal to 0, and we print “0” to the console. 

_The greatest risk of using a while loop is writing a condition which is never met._ 

This occurs frequently in real-world scenarios, where someone writes a while loop but forgets to test their loop, and it introduces an [infinite loop](https://en.wikipedia.org/wiki/Infinite_loop) into the code-base. 

An infinite loop occurs when the condition is never met, and the loop keeps running forever. This often results in breaking changes, which then causes the entire software application to break and stop working. 

**Warning: Do not run this code.**   
  
**Infinite Loop Example (Bad):** 

```js
let i = 0 

while (i < 5) { 
  console.log(i); 
}
```

**Output:**   
  
Results may vary. 

## The Do While Loop

### What is a do while loop? 

Here is a simple definition of a Do-While loop:

> “a **do while loop** is a control flow statement that executes a block of code **at least once**, and then repeatedly executes the block, or not, depending on a given boolean condition at the end of the block.”

A do-while loop is almost identical to a while loop, however there is one key difference. The do-while loop will guarantee to always execute the block of code at least once before the if statement is checked. 

I often think of it as a reverse while loop, and almost never use them. However, they do come in handy in some very specific scenarios. 

**Do-Loop Example (Good):**

```js
let i = 0; 

do { 
  console.log(i); 
  i++; 
} while (i < 5);
```

**Output**:

```
0
1
2
3
4
```

_The greatest risk of using a do-loop is writing a condition which is never met. (Same as with a While Loop.)_

**Warning: Do not run this code.**   
  
**Infinite Loop Example (Bad):** 

```js
let i = 0; 

do { 
  console.log(i); 
} while (i < 5);
```

**Output**:   
  
Results may vary.

Want to take your JavaScript knowledge to the next level? Learn about `map`, which is the same as `forEach`, but with a bonus!! ?

## BONUS Example (Iteration with map)

### What is map? 

Here's a simple definition of a map: 

> “In many [programming languages](https://en.wikipedia.org/wiki/Programming_language), **map** is the name of a [higher-order function](https://en.wikipedia.org/wiki/Higher-order_function) that applies a [given function](https://en.wikipedia.org/wiki/Procedural_parameter) to each element of a [functor](https://en.wikipedia.org/wiki/Functor_(disambiguation)), e.g. a [list](https://en.wikipedia.org/wiki/List_(computing)), returning a list of results in the same order. It is often called _apply-to-all_ when considered in [functional form](https://en.wikipedia.org/wiki/Functional_form).”

How does it work? The `map` function in JavaScript applies a function to _every element_ inside the array_._ Please take a moment to re-read that sentence. 

Afterwards, the `map` function returns a new array with the results of applying a function to every element in the array. 

**Map example:**

```js
const array = [1, 1, 1, 1];

// pass a function to map
const results = array.map(x => x * 2);

console.log(results);
```

**Output**: 

```
[2,2,2,2]
```

We have applied the `map` function to the array containing four 1's. The `map` function then multiplied each element by 2, i.e., `x * 2`, and returned a new array. The new array was then stored in the `results` variable.

By viewing our output, we can see this worked successfully. Every element in the array has been multiplied by 2. This method can be used as a replacement to a loop in some cases, and is incredibly powerful. 

## Conclusion 

Well done! You have learned five different ways to iterate over an array in JavaScript. These are the fundamental building blocks that will set you up for success in your JavaScript programming journey. 

You have also been exposed to an advanced concept, `map`, which is used often in large-scale software applications. 

So, I’ll leave you with this: how are you going to use arrays in your projects? And which iteration method did you find most exciting?   

**_Thanks for reading!_** 

If you liked my article, please follow me and/or send me a message!  

**[Twitter](https://twitter.com/MartyJacobsDev) • [Medium](https://medium.com/@majikarpp) • [Github](https://github.com/majikarp)**


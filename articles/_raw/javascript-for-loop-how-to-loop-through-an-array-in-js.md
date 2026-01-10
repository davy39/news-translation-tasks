---
title: JavaScript For Loop – How to Loop Through an Array in JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-03T19:53:47.000Z'
originalURL: https://freecodecamp.org/news/javascript-for-loop-how-to-loop-through-an-array-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/srinivas-jd-PtpB2jiakOE-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'There are various types of loops in JavaScript, and all of them essentially
  do the same thing: they repeat an action again and again.

  Loops come in handy if you want to repeat the same block of code for a certain number
  of times. Basically, they are ...'
---

There are various types of loops in JavaScript, and all of them essentially do the same thing: they repeat an action again and again.

Loops come in handy if you want to repeat the same block of code for a certain number of times. Basically, they are a fast and effective way to repeat something.

This article focuses on the `for` loop in the JavaScript programming language and goes over its basic syntax.

In addition, I'll explain how to loop through an array using a `for` loop, which is a fundamental programming concept.

## What is a for loop? A basic syntax breakdown

A `for` loop repeats an action while a specific condition is `true`. It stops repeating the action when the condition finally evaluates to `false`.

A `for` loop in JavaScript looks very similar to a `for` loop in C and Java.

There are many different types of `for` loops in JavaScript, but the most basic ones look like this:

```
for( initialization of expression; condition; action for initialized expression ) {
  instruction statement to be executed;
}
```

This type of loop starts with the `for` keyword, followed by a set of parentheses. Inside them, there are three *optional* expression statements separated by a semicolon,`;`. Lastly, there is a set of curly braces, `{}`, that enclose the code block statement to be executed.

Here's an example:

```Javascript
for (let i = 0; i < 10; i++) {
  console.log('Counting numbers');
  // runs and prints "Counting numbers" 10 times
  // values of i range from 0 to 9 
  }
```

In more detail, when a `for` loop is executed:

- If there is any initial expression, it is run first and executed only one time before any code in the block is run and before the loop starts. In this step there is an initialization of one or more counters and declaration of one or more variables used in the loop, like `let i =0`. If there is more than one variable, they are separated by commas. 
- Next is the definition of the condition expression that has to be met in order for the loop to run, `i < 10`. As mentioned earlier, the instruction statements in the code block will run only when this condition evaluates to  `true`. If the value is `false` the loop stops running. If there is no condition it is always `true` which creates an *infinite loop*.
- Then, the instruction statement inside the block with the curly braces, `{..}`, is executed. There can be more than one, on multiple lines.
- After each time the code block has been executed, there can be an action for the initialized expression that takes place at the end, like an increment statement (` i++`) that updates the initial expression.
- After that, the condition is checked again and if it evaluates to true the process is repeated.

## What is an array?

An array is a data structure.

It is an ordered collection of multiple items, called elements, under the same name stored together in a list. This then allows them to be easily sorted or searched through.

Arrays in JavaScript can contain elements with values of different data types. An array can contain numbers, strings, another array, boolean values, and more – at the same time.

Indexing always starts at `0`. This means that the first item in an array is referenced with a zero index, the second item has a one index, and the last item is the `array length - 1`.

The easiest and most preferable way to create an array is with *array literal notation*, which you can do with square brackets with a comma separated list of elements, like the below array of strings:

```Javascript
let programmingLanguages = ["JavaScript","Java","Python","Ruby"];
```

To access the first item we use the index number:

```JavaScript
console.log(programmingLanguages[0]);
// prints JavaScript
```

## How to Iterate Over an Array with a for loop

Each time the `for` loop runs, it has a different value – and this is the case with arrays.

A for loop examines and iterates over every element the array contains in a fast, effective, and more controllable way.

A basic example of looping through an array is:

```JavaScript

const  myNumbersArray = [ 1,2,3,4,5];

for(let i = 0; i < myNumbersArray.length; i++) {
    console.log(myNumbersArray[i]);
}
```

Output:
```
1
2
3
4
5
```

This is much more effective than printing each value individually:

```javascript
console.log(myNumbersArray[0]);
console.log(myNumbersArray[1]);
console.log(myNumbersArray[2]);
console.log(myNumbersArray[3]);
console.log(myNumbersArray[4]);
```

Let's break it down:

The iterator variable `i` is initialized to 0. `i` in this case refers to accessing the index of the array. This means that the loop will access the first array value when it runs for the first time.

The condition`i < myNumbersArray.length` tells the loop when to stop, and the increment statement `i++` tells how much to increment the iterator variable for each loop.
 
In other words, the loop starts at `0 index`, checks the length of the array, prints out the value to the screen, and then increases the variable by 1. The loop prints out the contents of the array one at a time and when it reaches its length, it stops.
 
## Conclusion

This article covered the basics on how to get started with `for` loops in JavaScript. We learned how to loop through arrays using that method which is one of the most common ones you'll use when you're starting to learn the language.

If you want to learn about other JavaScript array methods, you can [read all about them here](https://www.freecodecamp.org/news/complete-introduction-to-the-most-useful-javascript-array-methods/).

Thanks for reading and happy coding!





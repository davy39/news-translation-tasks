---
title: JavaScript For loop – How to Loop Through an Array in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-26T23:14:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-loop-through-an-array-with-for-loop-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/1_9H5rmyp3MgrcA8i1emsJPg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: null
seo_desc: 'By Dennis Temoye Charity

  A loop is an instruction in computer programming that allows an application to repeat
  a process until a specific condition is met.

  For example, say you want to run through a list of names and output each name on
  your screen. ...'
---

By Dennis Temoye Charity

A loop is an instruction in computer programming that allows an application to repeat a process until a specific condition is met.

For example, say you want to run through a list of names and output each name on your screen. If you didn't use a loop, you'd end up repeating code to output each name. But with a loop, you're able to output each name individually without repeating any code.

This article will walk you through the process of how you can loop through an array using the five most common loops in JavaScript.

## **What Is an Array in JavaScript?**

An array in JavaScript is a variable that you can use to store multiple elements. It is usually in the form of square brackets that contain different elements, strings, and integers (or both strings and integers).

## **What Is a Loop in JavaScript?**

A loop is a conditional statement used to run a sequence of instructions until a specified condition is met. It is given a statement that repeats the execution of a block of code and ends the execution once the stated condition is met.

Let's loop through this array – `let name = ['Dennis', 'Precious', 'Evelyn']`, – using one of the most commonly used loops in JavaScript.

## **How to Loop Through an Array with a For Loop in JavaScript**

A `for` loop is a statement that repeats the execution of a block of code when the condition has not been met and terminates the execution when the condition has been met.

Let's now loop through an array using the `for` loop method.

I advise that you go through this article carefully to not miss vital details along the way. But in case you are in a hurry to loop through an array using the `for` loop statement, you can check out the syntax below.

### **Quick for loop explanation:**

This is the fast route to looping through an array using the `for` loop statement with an example.

Syntax:

```js
let name = ['Dennis', 'Precious', 'Evelyn'];
for (let i = 0; i < name.length; i++)
 {    
     console.log(name[i]);
}
```

And here's the output:

```js
Dennis
Precious
Evelyn
```

### **How for loops work – in more detail**

Here we will get to understand what a `for` loop is and how to use this statement to loop through an array with an example.

To run a `for` loop statement, you must know that it always needs to have three primary expressions that are always separated by a semicolon.

Syntax:

```js
for (expression1; expression2; expression3)
 {  
  //code to be executed
}
```

* expression1: This is the `initialization` expression, which you use to declare a `for` loop counter variable with either the `var` or `let` keywords, such as `var i = 0` or `let i = 0`.
* expression2: This is the `condition` expression, which either returns true or false. It determines whether the `for` loop should continue the execution or end the execution.

Remember that a `for` loop statement continues executing a block of code when the condition has not been met, it only terminates the loop when the condition has been met.

* expression3: This is the `update` expression, which is usually used to increment (`++i`) or decrement (`--i`) the `for` loop counter variable whenever the `for` loop condition has been met.

Now that we understand the `for` loop statement expressions, let's work with an example.

Syntax:

```js
const arrayName = ['Dennis', 'Precious', 'Evelyn']
for (let i = 0; i < arrayName.length; i++) {
	console.log(arrayName[i]);
}
```

This syntax above loops through the `name` array and `console.log ()` the strings in the array as long as the condition has not been met.

From the syntax above:

* We first initialized the counter variable, `let i = 0;`.
* Then we gave the loop a condition to terminate the loop once the value of the counter variable (`i`) is less than (`<`) the length of the name (`name.length;`).
* You use the keyword `length` to check the length of a string.

Here's the output:

```js
Dennis
Precious
Evelyn
```

## **Conclusion**

In this tutorial, we discussed the fundamentals of a for loop in JavaScript as well as the definition of an array. We also learned how to use the JavaScript 'for' loop statement to loop through an array.

Thanks for reading.


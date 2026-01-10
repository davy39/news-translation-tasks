---
title: JavaScript For Loop – Explained with Examples
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-05-27T16:32:36.000Z'
originalURL: https://freecodecamp.org/news/javascript-for-loops
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/for-loops.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: null
seo_desc: 'Loops are a programming concept that we constantly encounter and implement
  as JavaScript developers.

  And many developers are familiar with loops, but not everyone understands how they
  work and why or when they should use a specific type of loop.

  In t...'
---

Loops are a programming concept that we constantly encounter and implement as JavaScript developers.

And many developers are familiar with loops, but not everyone understands how they work and why or when they should use a specific type of loop.

In this article, we will learn what for loops are, how they work, and why we use them. We'll also keep in mind that there are several types of loops, each of which performs a specific function even though they can almost all perform the same common function.

## What are Loops?

Loops are computer programs that execute a set of instructions or a block of code a certain number of times without having to write it again until a certain condition is met. In other words, loops let your code execute one or more statements as many times as desired.

Again, there are many types of loops, but we will only look at the for loop in this article.

Almost every high-level programming language, including JavaScript, has a for loop. We're only going to look at JavaScript in this article, and we'll look at its syntax and some examples.

### For Loops in JavaScript

The for loop is an iterative statement which you use to check for certain conditions and then repeatedly execute a block of code as long as those conditions are met.

![Image](https://paper-attachments.dropbox.com/s_3315FAFA14C012362B87C753E4A1C2D25C00228882CEE2A5B63A9FDA99BA4B77_1653509464069_for+loop+flowchart+1.jpg align="left")

*Flowchart for the for loop*

### Syntax of a for loop

```javascript
for (initialExpression; condition; updateExpression) {
    // for loop body: statement
}
```

The code block above is the standard syntax used by for loop. Let's look at each parameter to see what it means and what it does:

* `initialExpression`: This is used to set the value of a counter variable, and it is only evaluated once, before the loop starts. Depending on the scope, these counter variables are usually declared with the `var` or `let` keywords.
    
* `condition`: This is a constant-evaluation expression that determines whether the loop should be executed. In simple terms, if this condition returns true, the for loop's block of code is executed. If it returns false, the for loop is terminated.
    
* `updateExpression`: This is commonly used to update or increment the `initialExpression` counter variable. In other words, when the condition is true, it updates the value of the `initialExpression`.
    

In summary, the for loop causes the `initialExpression` variable, which is set to a starting value, to increase or decrease in response to the `updateExpression` as long as the condition is met. Finally, the statement, will always be executed if the condition evaluates to true.

## For Loop Examples in JavaScript

At this point, we now understand what loops are, so let’s take a look at some examples and see how we can use loops.

### How to Display Text Multiple Times

Let’s start by displaying some text several times until our condition is met.

```javascript
for (var i = 0; i < 3; i++) {
  let name = "John Doe";
  console.log("Hi, my name is " + name);
}
```

**Output:**

```bash
"Hi, my name is John Doe"
"Hi, my name is John Doe"
"Hi, my name is John Doe"
```

Here is how the program processed this loop:

| Iteration | Variable | Condition: i &lt; 3 | Action & variable update |
| --- | --- | --- | --- |
| 1st | i = 0 | true | Hi, my name is John Doe is printed. |
| 2nd | i = 1 | true | Hi, my name is John Doe is printed. |
| 3rd | i = 2 | true | Hi, my name is John Doe is printed. |
| 4th | i=3 | false | The loop is terminated. |

**Note:** The loop is terminated because 3 is not less than 3, so it returned `false`.

### How to Display a Sequence of Numbers with a For Loop

This time around, let’s display a sequence of numbers by displaying the iteration value.

```javascript
for (let i = 2; i <= 5; i++) {
    console.log(i);  // printing the value of i
}
```

**Output:**

```bash
2
3
4
5
```

Here is how the program processed this loop:

| Iteration | Variable | Condition: i &lt;= 5 | Action& variable update |
| --- | --- | --- | --- |
| 1st | i = 2 | true | 2 is printed. |
| 2nd | i = 3 | true | 3 is printed. |
| 3rd | i = 4 | true | 4 is printed. |
| 5th | i = 5 | true | 5 is printed. |
| 6th | i = 6 | false | The loop is terminated. |

**Note:** The loop is terminated because 6 is not less than or equal to 5, so the condition returns false.

### How to Display a Sequence of Even Numbers

Let’s now display a sequence of even numbers only by displaying the iteration value:

```javascript
for (let i = 2; i <= 10; i+=2) {
    console.log(i);  // printing the value of i
}
```

**Output:**

```bash
2
4
6
8
10
```

Here is how the program processed this loop:

| Iteration | Variable | Condition: i &lt;= 10 | Action & variable update |
| --- | --- | --- | --- |
| 1st | i = 2 | true | 2 is printed. |
| 2nd | i = 4 | true | 4 is printed. |
| 3rd | i = 6 | true | 6 is printed. |
| 5th | i = 8 | true | 8 is printed. |
| 6th | i = 10 | true | 10 is printed. |
| 7th | i = 12 | false | The loop is terminated. |

Suppose we want to obtain the odd numbers. All we have to do is change the `initialExpression` to equal `1` or any odd number we wish to start from as seen below

```javascript
for (let i = 1; i <= 10; i+=2) {
    console.log(i);  // printing the value of i
}
```

### How to Break a For Loop Operation

So far, we have seen how to create a for loop, but it’s also important to mention that we can break out of a loop using `break`. The break statement is used to terminate the loop immediately when it is encountered.

```javascript
for (let i = 1; i <= 10; i++) {    
    if (i == 5) {
        break;
    }
    console.log(i);
}
```

**Output:**

```bash
1
2
3
4
```

### How to Display the Sum of Natural Numbers

Let’s now loop from 1-10 and then add these numbers together as the iteration is increased:

```javascript
let sum = 0;

for (let i = 1; i <= 10; i++) {
    sum += i;  // This is same as: sum = sum + i
}

console.log('The sum of 1 to 10 is: ', sum); // "The sum of 1 to 10 is:  55"
```

**Note:** We are adding `console.log(…)` outside the loop, so it only gives us the final output when the loop is terminated.

We can also decide to use variables to set the max number of our condition this way:

```javascript
let sum = 0;
let n = 10;

for (let i = 1; i <= n; i++) {
    sum += i;  // this is same as: sum = sum + i
}

console.log('The sum of 1 to 10 is: ', sum); // "The sum of 1 to 10 is:  55"
```

### How to Perform Infinite Loops with a For Loop

This can hang your system, because it continues to run until the memory is full, since the condition always evaluates as true.

```javascript
for(let i = 1; i > 0; i++) {
    // block of code
}
```

### How to Loop Through an Array to Check for Odd and Even Numbers

Most times you will be working with arrays, so let’s see how we can loop through an array of numbers to output all odd and even numbers:

```javascript
var numbers = [1, 4, 44, 64, 55, 24, 32, 55, 19, 17, 74, 22, 23];
var evenNumbers = [];
var oddNumbers = [];

for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 != 1) {
        evenNumbers.push(numbers[i]);
    } else {
        oddNumbers.push(numbers[i]);
    }
}

console.log("The even numbers are: " + evenNumbers); // "The even numbers are: 4,44,64,24,32,74,22"
console.log("The odd numbers are: " + oddNumbers); // "The odd numbers are: 1,55,55,19,17,23"
```

### How to Loop Through an Array of Numbers to Get the Maximum and Minimum Number

Finally, before we round up this article, let’s see how to get the maximum and minimum number from an array with for loop:

**Maximum:**

```javascript
var numbers = [1, 4, 44, 64, 55, 24, 32, 55, 19, 17, 74, 22, 23];
var max = 0;

for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
        max = numbers[i];
    }
}

console.log(max); // 74
```

**Minimum:**

```javascript
var numbers = [4, 44, 64, 55, 24, 32, 55, 19, 17, 74, 22, 23];
var min = numbers[0];

for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] < min) {
        min = numbers[i];
    }
}

console.log(min); // 4
```

## Conclusion

In this article, we learned what a JavaScript loop is and looked at some examples.

It is important to understand that there are many other types of loops, including the while loop, which is best used when you don't know the number of iterations. Otherwise, always use the for loop when you do know the number of iterations.

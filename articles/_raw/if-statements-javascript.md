---
title: How to Use If Statements in JavaScript – a Beginner's Guide
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-11-20T21:45:44.000Z'
originalURL: https://freecodecamp.org/news/if-statements-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Pink-Elegant-Group-Project-Education-Presentation.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "JavaScript is a powerful and versatile programming language that is widely\
  \ used for creating dynamic and interactive web pages. \nOne of the fundamental\
  \ building blocks of JavaScript programming is the if statement. if statements allow\
  \ developers to c..."
---

JavaScript is a powerful and versatile programming language that is widely used for creating dynamic and interactive web pages. 

One of the fundamental building blocks of JavaScript programming is the `if` statement. `if` statements allow developers to control the flow of their programs by making decisions based on certain conditions. 

In this article, we will explore the basics of `if` statements in JavaScript, understand their syntax, and see how they can be used to create more responsive and intelligent code.

## What is an `if` Statement?

An `if` statement is a conditional statement that allows you to execute a block of code only if a specified condition is true. In other words, it provides a way to make decisions in your code. 

For example, you might want to display a message to the user if they have entered the correct password, or you might want to perform a certain action only if a variable has a specific value.

Here's a simple example to illustrate the basic structure of an `if` statement:

```javascript
let temperature = 25;

if (temperature > 20) {
  console.log("It's a warm day!");
}

```

In this example, the `if` statement checks whether the value of the `temperature` variable is greater than 20. If the condition is true, the code inside the curly braces (`{}`) is executed, and the message "It's a warm day!" is logged to the console.

## Syntax of `if` Statements

The syntax of an `if` statement in JavaScript is straightforward. It consists of the `if` keyword followed by a set of parentheses containing a condition. If the condition evaluates to `true`, the code inside the curly braces is executed. Here is the basic syntax:

```javascript
if (condition) {
  // Code to be executed if the condition is true
}

```

Let's break down the components of the `if` statement:

* **`if` keyword:** This is the keyword that starts the `if` statement and is followed by a set of parentheses.
* **Condition:** Inside the parentheses, you provide the condition that you want to evaluate. This condition should result in a boolean value (`true` or `false`).
* **Code block:** The code block is enclosed in curly braces `{}`. If the condition is true, the code inside the block is executed.

It's important to note that the curly braces are essential, even if the block contains only one statement. Including the braces makes your code more readable and helps prevent bugs that can occur when adding more statements to the block later.

## Simple `if` Statements

Let's dive deeper into simple `if` statements by exploring some examples. Simple `if` statements consist of a single condition and a block of code that executes when the condition is true.

### Example 1: Checking a Number

```javascript
let number = 7;

if (number > 0) {
  console.log("The number is positive.");
}

```

In this example, the `if` statement checks whether the value of the `number` variable is greater than 0. If the condition is true, the message "The number is positive." is logged to the console.

### Example 2: Verifying User Input

```javascript
let userInput = prompt("Enter your age:");

if (userInput >= 18) {
  console.log("You are eligible to vote.");
}

```

This example uses the `prompt` function to get the user's age as input. The `if` statement then checks whether the entered age is greater than or equal to 18. If true, the message "You are eligible to vote." is logged to the console.

### Example 3: Checking Equality

```javascript
let password = "secure123";

if (password === "secure123") {
  console.log("Access granted.");
}

```

In this example, the `if` statement checks whether the value of the `password` variable is exactly equal to the string "secure123". If the condition is true, the message "Access granted." is logged to the console.

## If-Else Statements

While simple `if` statements are useful, often you'll want to provide an alternative action when the condition is false. This is where the `if-else` statement comes in handy. The `else` block contains code that executes when the `if` condition is false.

### Example: If-Else Statement

```javascript
let hour = 14;

if (hour < 12) {
  console.log("Good morning!");
} else {
  console.log("Good afternoon!");
}

```

In this example, the `if` statement checks whether the value of the `hour` variable is less than 12. If true, it logs "Good morning!" to the console. Otherwise, it logs "Good afternoon!".

## If-Else If Statements

Sometimes, you may have multiple conditions to check. In such cases, you can use `else if` statements to add additional conditions. The code inside the first true condition block encountered will be executed, and subsequent conditions will be ignored.

### Example: If-Else If Statement

```javascript
let grade = 85;

if (grade >= 90) {
  console.log("A");
} else if (grade >= 80) {
  console.log("B");
} else if (grade >= 70) {
  console.log("C");
} else {
  console.log("D");
}

```

In this example, the code determines a student's grade based on their score. It first checks if the grade is greater than or equal to 90, and if true, it logs "A". If not, it moves to the next condition and checks if the grade is greater than or equal to 80, and so on. If none of the conditions are true, it logs "D".

## Nested `if` Statements

You can also nest `if` statements inside other `if` statements to create more complex decision structures. Each `if` statement within the nested structure adds an additional layer of conditions.

### Example: Nested `if` Statement

```javascript
let temperature = 25;
let isSummer = true;

if (isSummer) {
  if (temperature > 30) {
    console.log("It's a hot summer day!");
  } else {
    console.log("It's a warm summer day.");
  }
} else {
  console.log("It's not summer.");
}

```

In this example, the outer `if` statement checks if it's summer. If true, it enters the nested structure and checks the temperature. Depending on the temperature, it logs different messages. If it's not summer, it logs "It's not summer."

## Logical Operators in `if` Statements

JavaScript provides logical operators (`&&`, `||`, `!`) that allow you to combine multiple conditions in a single `if` statement.

### Example: Logical Operators

```javascript
let age = 25;
let hasLicense = true;

if (age >= 18 && hasLicense) {
  console.log("You are eligible to drive.");
} else {
  console.log("You are not eligible to drive.");
}

```

In this example, the `&&` (logical AND) operator combines two conditions: the person's age being 18 or older and having a valid license. If both conditions are true, it logs "You are eligible to drive." Otherwise, it logs "You are not eligible to drive."

## Switch Statements

In situations where you have multiple possible conditions to check against a single value, a `switch` statement can be more concise than a series of `if-else if` statements.

### Example: Switch Statement

```javascript
let dayOfWeek = "Wednesday";

switch (dayOfWeek) {
  case "Monday":
    console.log("It's the start of the week.");
    break;
  case "Wednesday":
    console.log("It's the middle of the week.");
    break;
  case "Friday":
    console.log("It's almost the weekend.");
    break;
  default:
    console.log("It's an ordinary day.");
}

```

In this example, the `switch` statement checks the value of `dayOfWeek` and executes the corresponding block of code. If none of the cases match, the `default` block is executed.

## Common Mistakes with `if` Statements

While using `if` statements, beginners often make some common mistakes. Let's address a few of them:

### Mistake 1: Forgetting the Equality Operator

```javascript
let x = 5;

// Incorrect
if (x = 10) {
  console.log("x is 10.");
}

```

The above code is incorrect because it uses the assignment operator `=` instead of the equality operator `===` inside the `if` condition. The correct code should be `if (x === 10)`.

### Mistake 2: Misplacing Curly Braces

```javascript
let y = 15;

// Incorrect
if (y > 10)
  console.log("y is greater than 10");
  console.log("This statement is not in the if block");

```

In this example, only the first `console.log` statement is part of the `if` block because the curly braces are missing. To include both statements in the `if` block, use curly braces:

```javascript
if (y > 10) {
  console.log("y is greater than 10");
  console.log("This statement is in the if block");
}

```

### Mistake 3: Confusing `=` and `==`

```javascript
let z = "5";

// Incorrect
if (z = 5) {
  console.log("z is 5.");
}

```

The above code is incorrect because it uses the assignment operator `=` instead of the equality operator `==` inside the `if` condition. The correct code should be `if (z == 5)`.

## Conclusion

Understanding and mastering `if` statements is essential for any JavaScript developer. These conditional statements provide the logic that enables your programs to make decisions and respond dynamically to different situations. 

Whether you're validating user input, controlling the flow of your application, or handling different cases, `if` statements are a fundamental tool in your programming arsenal.

As you continue your journey in JavaScript development, practice using `if` statements in various scenarios. Experiment with different conditions, nesting structures, and logical operators to become comfortable and proficient in utilizing these powerful tools. 

With a solid understanding of `if` statements, you'll be well-equipped to build more dynamic and responsive web applications.


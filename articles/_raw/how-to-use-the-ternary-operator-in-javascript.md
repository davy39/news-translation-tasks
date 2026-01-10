---
title: How to Use the Ternary Operator in JavaScript – JS Conditional Example
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-02-27T18:40:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-ternary-operator-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-ken-tomita-389818.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'The ternary operator is a helpful feature in JavaScript that allows you
  to write concise and readable expressions that perform conditional operations on
  only one line.

  In this article, you will learn why you may want to use the ternary operator, and
  ...'
---

The ternary operator is a helpful feature in JavaScript that allows you to write concise and readable expressions that perform conditional operations on only one line.
 
In this article, you will learn why you may want to use the ternary operator, and you will see an example of how to use it. You will also learn some of the best practices to keep in mind when you do use it.

Let's get into it!

## What Is The Ternary Operator in JavaScript?

The ternary operator (`?:`), also known as the conditional operator, is a shorthand way of writing conditional statements in JavaScript – you can use a ternary operator instead of an `if..else` statement.

A ternary operator evaluates a given condition, also known as a Boolean expression, and returns a result that depends on whether that condition evaluates to `true` or `false`. 

### Why Use the Ternary Operator in JavaScript?

You may want to use the ternary operator for a few reasons:

- **Your code will be more concise**: The ternary operator has minimal syntax. You will write short conditional statements and fewer lines of code, which makes your code easier to read and understand.
- **Your code will be more readable**: When writing simple conditions, the ternary operator makes your code easier to understand in comparison to an `if..else` statement.
- **Your code will be more organized**: The ternary operator will make your code more organized and easier to maintain. This comes in handy when writing multiple conditional statements. The ternary operator will reduce the amount of nesting that occurs when using `if..else` statements.
- **It provides flexibility**: The ternary operator has many use cases, some of which include: assigning a value to a variable, rendering dynamic content on a web page, handling function arguments, validating data and handling errors, and creating complex expressions.
- **It enhances performance**: In some cases, the ternary operator can perform better than an `if..else` statement because the ternary operator gets evaluated in a single step.
- **It always returns a value**: The ternary operator always has to return something.

## How to Use the Ternary Operator in JavaScript – a Syntax Overview

The operator is called "ternary" because it is composed of three parts: one condition and two expressions.

The general syntax for the ternary operator looks something similar to the following:

```
condition ? ifTrueExperssion : ifFalseExpression;
```

Let's break it down:

- `condition` is the Boolean expression you want to evaluate and determine whether it is `true` or `false`. The condition is followed by a question mark, `?`.
- `ifTrueExpression` is executed if the condition evaluates to `true`.
- `ifFalseExpression` is executed if the condition evaluates to `false`.
- The two expressions are separated by a colon, `.`.

The ternary operator always returns a value that you assign to a variable: 

```
const returnValue = condition ? ifTrueExperssion : ifFalseExpression;
```

Next, let's look at an example of how the ternary operator works.

## How to Use the Ternary Operator in JavaScript

Say that you want to check whether a user is an adult:

```javascript
// get user input
const age = prompt("What is your age?");

// check condition
const message = (age >= 18) ? "You are an adult" : "You are not an adult yet";

console.log(message); 
```

In this example, I used the ternary operator to determine whether a user's age is greater than or equal to `18`.

Firstly,  I used the `prompt()` built-in JavaScript function.

This function opens a dialog box with the message `What is your age?` and the user can enter a value.

I store the user's input in the `age` variable.

Next, the condition (`age >= 18`) gets evaluated.

If the condition is `true`, the first expression, `You are an adult`, gets executed. 

Say the user enters the value `18`. 

The condition `age >= 18` evaluates to `true`:

```
What is your age? 18

// output
You are an adult
```

If the condition is `false`, the second expression, `You are not an adult yet`, gets executed.

Say the user enters the value `17`. 

The condition `age >= 18` now evaluates to `false`:

```
What is your age? 17

// output
You are not an adult yet
```

As mentioned earlier, you can use the ternary operator instead of an `if..else` statement.

Here is how you would write the same code used in the example above using an `if..else` statement:

```javascript
// get user input
const age = prompt("What is your age?");

// check the condition

if (age >= 18) {
  console.log("Your are an adult");
} else {
  console.log("You are not an adult yet");
}
```

## Ternary Operator Best Practices in JavaScript

Something to keep in mind when using the ternary operator is to keep it simple and don't overcomplicate it.

The main goal is for your code to be readable and easily understandable for the rest of the developers on your team.

So, consider using the ternary operator for simple statements and as a concise alternative to `if..else` statements that can be written in one line.

If you do too much, it can quickly become unreadable.

For example, in some cases, using nested ternary operators can make your code hard to read:


```javascript
// get user input
const age = prompt("What is your age?");

// check condition
const message = (age >= 18) ? (age == 18 ? "You are exactly 18" : "You are over 18") : "You are under 18";

console.log(message); 
```

If you find yourself nesting too many ternary operators, consider using `if...else` statements instead.

## Wrapping Up

Overall, the ternary operator is a useful feature in JavaScript as it helps make your code more readable and concise. 

Use it when a conditional statement can be written on only one line and keep code readability in mind.

Thanks for reading, and happy coding! :)



---
title: JavaScript Ternary Operator – Syntax and Example Use Case
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-06T23:30:48.000Z'
originalURL: https://freecodecamp.org/news/the-ternary-operator-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/13.-ternary-operator.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  There are many operators in JavaScript, one of which is the ternary operator. In
  this article, I''ll explain what this operator is, and how it can be useful when
  building applications.

  I have a video version of this topic you can che...'
---

By Dillion Megida

There are many operators in JavaScript, one of which is the ternary operator. In this article, I'll explain what this operator is, and how it can be useful when building applications.

I have a [video version of this topic](https://youtu.be/MmwtZ0AwN9A) you can check out as well to supplement your learning.

## What is the Ternary Operator?

The ternary operator is a conditional operator which evaluates either of two expressions – a true expression and a false expression – based on a conditional expression that you provide.

Here's the syntax:

```js
condition ? trueExpression : falseExpression
```

You have the **condition** which returns a truthy or falsy value. Truthy values here include `true`, and non-falsy values. Falsy values here include `false`, `null`, `0`, and so on.

After the condition, you have the question mark (which you can think of as "questioning the condition"), followed by the **trueExpression**. This expression is executed if the condition expression evaluates to `true`.

After the true expression, you have a colon, followed by the **falseExpression**. This expression is executed if the condition expression evaluates to `false`.

The ternary operator returns a value that you can assign to a variable. You cannot use the operator without assigning the returned value to a variable:

```js
const result = condition
  ? trueExpression
  : falseExpression
```

The returned value depends on the evaluation of the condition expression. If the condition is `true`, the returned value returned from **trueExpression** is assigned to the variable. Else, the returned value from **falseExpression** will be assigned to the variable.

## How to Use the Ternary Operator in Place of `if` Statements

The ternary operator can be a good replacement for `if` statements in some cases. It allows you to write concise, cleaner, and easier-to-read lines of code if used well.

Let's see an example:

```js
const score = 80
let scoreRating

if (score > 70) {
  scoreRating = "Excellent"
} else {
  scoreRating = "Do better"
}

console.log(scoreRating)
// "Excellent"
```

In this example, we have a `score` variable with **80** and a `scoreRating` variable. Then we have an `if` statement that checks `score > 70`. If this condition evaluates to `true`, the `scoreRating` variable is assigned **"Excellent"**, else, it is assigned **"Do better"**.

We can improve this code with the ternary operator. Here's how.

Remember the syntax: you have the condition, a question mark, the true expression, a colon, and finally a false expression. Let's look at this in code:

```js
const score = 80

const scoreRating =
  score > 70 ? "Excellent" : "Do better"

console.log(scoreRating)
// Excellent
```

This is how we use the ternary operator. The true and false expressions here are strings that will be returned to the `scoreRating` variable depending on our condition `score > 70`.

The true and false expressions can be any kind of expression from function executions to arithmetic operations and so on. Here's an example with a function execution:

```js
function printPoor() {
  console.log("Poor result")
  return "poor"
}

function printSuccess() {
  console.log("Nice result")
  return "success"
}


const pass = false;

const result = pass ? printSuccess() : printPoor()
// Poor result (console.log executed)

console.log(result)
// poor
```

Here, you see that as the condition returns `false`, the false expression, `printPoor()` is executed which prints "Poor result" to the console. And as the false expression returns "poor", you can see that value assigned to the `result` variable.

For the rest of this article, I'll be using string true and false expressions for simplicity.

## How to Use Nested Ternary Operators

What if you wanted to achieve an `if...else if...else` statement with a ternary operator? Then you can use nested ternary operators. You should be careful how you use this, however, as it can make your code harder to read.

Let's see an example:

```js
const score = 60
let scoreRating

if (score > 70) {
  scoreRating = "Excellent"
} else if (score > 50) {
  scoreRating = "Average"
} else {
  scoreRating = "Do better"
}

console.log(scoreRating)
// "Average"
```

We have an `if-else-if-else` statement here where we first check if `score > 70`. If this returns `true`, we assign "Excellent" to the `scoreRating` variable. If this returns `false`, we check if `score > 50`. If this second condition returns `true`, we assign "Average" to the variable but if this also returns false, we finally (`else`) assign "Do better" to the variable.

Let's see how to do this with the ternary operator:

```js
const score = 60

const scoreRating =
  score > 70
    ? "Excellent"
    : score > 50
    ? "Average"
    : "Do better"

console.log(scoreRating)
// "Average"
```

Here, you see we have two question marks and two colons. In the first ternary operator, we have the conditional expression `score > 70`. After the first question mark, we have the true expression which is **"Excellent"**. After the first colon, the next expression is supposed to be the false expression. For the false expression, we declare another conditional expression using the ternary operator.

The second condition here is `score > 70`. After the second question mark, we have the true expression which is **"Average"**. After the second colon, we now have another false expression, which is **"Do better"**.

With this, if the first condition is true, "Excellent" is returned to `scoreRating`. If the first condition is false, then we have another condition check. If this second condition is true, "Average" is returned to the variable. If this second condition is also false, then we have the final false expression, "Do better", which will be assigned to the variable.

## Multiple Ternary Operators Can Make Your Code Unreadable

In the previous examples, we've seen how we can improve our code while maintaining readability. But you have to be careful when using multiple ternary operators.

Imagine we had an extra ternary operator in our previous example:

```js
const score = 45

const scoreRating =
  score > 70
    ? "Excellent"
    : score > 50
    ? "Average"
    : score > 40
    ? "Fair"
    : "Do better"

console.log(scoreRating)
// "Fair"
```

Here we have three ternary operators, and you can see that things are becoming harder to read. 

In cases like this where you need multiple conditions, using an `if` or `switch` statement, though requiring longer lines of code, makes you write more readable code.

## Wrapping Up

The ternary operator allows you to evaluate conditional expressions and can substitute for `if` statements in some cases. It allows you to write shorter and cleaner code (even on one line).

In this article, I've shown you how it works, using some `if` examples and the ternary operator version. I also emphasized that you should be careful when using nested ternary operators as that can then make your code unreadable.

If you enjoyed this piece, please share!




---
title: Ternary Operator JavaScript If Statement Tutorial
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-01-25T14:56:28.000Z'
originalURL: https://freecodecamp.org/news/ternary-operator-javascript-if-statement-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/js-ternary.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'This tutorial will help you learn how to replace an if/else statement with
  a more concise shorthand syntax called the ternary operator.

  The conditional operator – also known as the ternary operator – is an alternative
  form of the if/else statement th...'
---

This tutorial will help you learn how to replace an `if/else` statement with a more concise shorthand syntax called the ternary operator.

The conditional operator – also known as the ternary operator – is an alternative form of the `if/else` statement that helps you to write conditional code blocks in a more concise way.

The syntax for the conditional operator looks like this:

```js
conditional ? expression_when_true : expression_when_false;
```

First, you need to write a _conditional expression_ that evaluates into either `true` or `false`. If the expression returns true, JavaScript will execute the code you write on the left side of the colon operator (`:`) when it returns false, the code on the right side of the colon operator is executed.

To understand how it works, let's compare it with a regular `if/else` statement. Let's say you have a small program that assigns different exam grades depending on your exam score:

* When you have a score higher than 80, you assign "A" as the grade.
* Else, you assign "B" as the grade.

Here's one way to write the program: 

```js
let score = 85;
let grade;
if(score >= 80){
    grade = "A";
} else {
    grade = "B";
}

console.log(`Your exam grade is ${grade}`);
```

Alternatively, you can write the above code using the ternary operator as follows:

```js
let score = 85;
let grade = score >= 80 ? "A" : "B";

console.log(`Your exam grade is ${grade}`);
```

And there you go. The ternary operator shorthand looks way more concise and shorter than a regular `if/else` statement.

But what if your code requires multiple `if/else` statements? What if you add "C" and "D" grades into the evaluation?

```js
let score = 85;
let grade;
if(score >= 80){
    grade = "A";
} else if (score >= 70) {
    grade = "B";
} else if (score >= 60) {
    grade = "C";
} else {
    grade = "D";
}

console.log(`Your exam grade is ${grade}`);
```

No worries! You can write multiple ternary operators to replace the code above like this:

```js
let score = 85;
let grade = score >= 80 ? "A" 
  : score >= 70 ? "B" 
  : score >= 60 ? "C" 
  : "D";

console.log(`Your exam grade is ${grade}`);
```

However, it's not recommended to replace multiple `if/else` statements with multiple ternary operators because it makes the code harder to read in the future. It's best to stick with either `if/else` or `switch` statements for such cases.

## Thanks for reading this tutorial

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!


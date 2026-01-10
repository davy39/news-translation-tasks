---
title: JavaScript Switch Statement – With JS Switch Case Example Code
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-04-09T18:27:57.000Z'
originalURL: https://freecodecamp.org/news/javascript-switch-statement-with-js-switch-case-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/js-switch-statement.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Creating conditionals to decide what action to perform is one of the most\
  \ fundamental parts of programming in JavaScript. This tutorial will help you learn\
  \ how to create multiple conditionals using the switch keyword. \nHow switch statements\
  \ work in J..."
---

Creating conditionals to decide what action to perform is one of the most fundamental parts of programming in JavaScript. This tutorial will help you learn how to create multiple conditionals using the `switch` keyword. 

## How switch statements work in JavaScript

The JavaScript `switch` keyword is used to create multiple conditional statements, allowing you to execute different code blocks based on different conditions.

The code below shows you a `switch` statement in action:

```js
var score = 20;

switch(age){
    case 10:
        console.log("Score value is 10");
        break;
    case 20:
        console.log("Score value is 20");
        break;
    default:
        console.log("Score value is neither 10 or 20");
}
```

The code above will print `"Score value is 20"` to the console. The switch statement works by comparing an `expression` given to it with the expressions in each `case` clause.

First, you need to pass an `expression` into the `switch` statement, which is then enclosed in a pair of round brackets `()`. You can pass a variable or a literal value as shown below:

```js
var age = 29;

switch(age){}
// or
switch(true){}
switch("A string"){}
switch(5+5){}
```

The `expression` will be evaluated once, and then compared with the expressions that you define in each `case` clause, from top to bottom.

In the following example, the `switch` statement will evaluate the value of the variable `flower` and then compare it with each `case` clause to see if it returns `true`:

* The first `case` will compare if `flower === "rose"`
* The second `case` will compare if `flower === "violet"`
* The third `case` will compare if `flower === "sunflower"`
* When all three `case` clauses return `false` , the `default` case will be executed

```js
var flower = "tulip";

switch (flower){
    case "rose":
        console.log("Roses are red");
        break;
    case "violet":
        console.log("Violets are blue");
        break;
    case "sunflower":
        console.log("Sunflowers are yellow");
        break;
    default:
        console.log("Please select another flower");
}
```

The `default` case is optional, meaning you can simply run through the `switch` statement without generating any output. But it's always better to include one `default` case so that you know the `switch` statement is properly executed by JavaScript.

You can only include one `default` case in a `switch` statement, or JavaScript will throw an error.

Finally, you need to include the `break` keyword in each `case` clause's body to stop the `switch` statement's execution once a matching case is found. If you omit the `break` keyword, JavaScript will continue to evaluate the expression until the last `case` clause.

The following code will print both `"Roses are red"` and `"Please select another flower"` because the `break` keyword is omitted from the `case` clauses, causing JavaScript to continue the expression comparison down to the last case, which is the `default` case:

```js
var flower = "rose";

switch (flower){
    case "rose":
        console.log("Roses are red");
    case "violet":
        console.log("Violets are blue");
    case "sunflower":
        console.log("Sunflowers are yellow");
    default:
        console.log("Please select another flower");
}
```

Even when the expression `"rose"` already found a match in the first `case` clause, JavaScript still continue running the `switch` statement because there is no `break` keyword.

_Note: there's no need for the `break` keyword in the last case, because the `switch` statement will be executed completely by then._

To summarize, here's how a `switch` statement works:

* First, you need an `expression` that you want to compare with some conditionals. 
* Then, you write all the conditionals to compare with the `expression` in each `case` clause, including a `default` case when there is no matching `case`
* Finally, write the code that you want to execute inside each `case`, followed by the `break` keyword to stop JavaScript from further comparing the `expression` with the `case` clauses.

Now that you know how the `switch` statement works, let's learn when you should use `switch` statement instead of an `if..else` statement.

## When to use the switch statement

Both the `switch` statement and `if..else` statement are used to create conditionals. The rule of thumb is that the `switch` statement is only used when you have a **precise value** for the conditionals.

This is because an `if..else` statement can be used to compare an `expression` with an **imprecise value** such as larger than or smaller than:

```js
var score = 70;

if(score > 50){
  console.log("Score is higher than 50");
} else {
  console.log("Score is 50 or lower");
}
```

But you can't use `score > 50` as a condition for a `case` clause. The following example will print the `default` case even though `score > 50`:

```js
var score = 70;

switch(score){
    case score > 50:
        console.log("Score is higher than 50");
        break;
    default:
        console.log("Score is 50 or lower");
}
```

If you want to evaluate an imprecise value using the `switch` statement, you need to create a workaround by evaluating a `true` expression as in the code below:

```js
var score = 70;

switch(true){
    case score > 50:
        console.log("Score is higher than 50");
        break;
    default:
        console.log("Score is 50 or lower");
}
```

While the code above will work, it's better to use an `if..else` statement because it's more readable.

## **Thanks for reading this tutorial**

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!


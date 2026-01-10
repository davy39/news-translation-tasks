---
title: JavaScript If-Else and If-Then – JS Conditional Statements
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-08-09T23:21:21.000Z'
originalURL: https://freecodecamp.org/news/javascript-if-else-and-if-then-js-conditional-statements
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/walling-e_MdMMKrgdY-unsplash.jpg
tags:
- name: Conditionals
  slug: conditionals
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "There will be times where you will want to write commands that handle different\
  \ decisions in your code. \nFor example, if you are coding a bot, you can have it\
  \ respond with different messages based on a set of commands it receives. \nIn this\
  \ article, I..."
---

There will be times where you will want to write commands that handle different decisions in your code. 

For example, if you are coding a bot, you can have it respond with different messages based on a set of commands it receives. 

In this article, I will explain what an `if...else` statement is and provide code examples. We will also look at the conditional (ternary) operator which you can use as a shorthand for the `if...else` statement. 

## What is an if...else statement in JavaScript?

The `if...else` is a type of conditional statement that will execute a block of code when the condition in the `if` statement is `truthy`. If the condition is `falsy`, then the `else` block will be executed. 

`Truthy` and `falsy` values are converted to `true` or `false` in  `if` statements.

```js
if (condition is true) {
   // code is executed
} else {
   // code is executed
}
```

Any value that is not defined as `falsy` would be considered `truthy` in JavaScript. 

Here is a list of  `falsy` values:

* false
* 0 (zero)
* -0 (negative zero)
* 0n (BigInt zero)
* `""`, `''`, ```` (empty string)
* null
* undefined
* NaN (not a number)

## Examples of if...else statements in JavaScript

In this example, the condition for the `if` statement is `true` so the message printed to the console would be "Nick is an adult."

```js
const age = 18;

if (age >= 18) {
  console.log("Nick is an adult.");
} else {
  console.log("Nick is a child.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-3.18.12-AM.png)

But if I change the `age` variable to be less than 18, then the condition would be `false` and the code would execute the `else` block instead. 

```js
const age = 12;

if (age >= 18) {
  console.log("Nick is an adult.");
} else {
  console.log("Nick is a child.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-3.17.07-AM.png)

## Examples of multiple conditions (if...else if...else statements) in JavaScript

There will be times where you want to test multiple conditions. That is where the `else if` block comes in. 

```js
if (condition 1 is true) {
   // code is executed
} else if (condition 2 is true) {
  // code is executed
} else {
   // code is executed
}
```

When the `if` statement is `false`, the computer will move onto the `else if` statement. If that is also `false`, then it will move onto the `else` block. 

In this example, the `else if` block would be executed because Alice is between the ages of 18 and 21. 

```js
const age = 18;

if (age < 18) {
  console.log("Alice is under 18 years old.");
} else if (age >= 18 && age <= 21) {
  console.log("Alice is between the ages of 18 and 21.");
} else {
  console.log("Alice is over 21 years old.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-3.33.33-AM.png)

## When to use switch statements over if...else statements? 

There are times in JavaScript where you [might consider using a `switch` statement](https://www.freecodecamp.org/news/javascript-switch-case-js-switch-statement-example/) instead of an `if else` statement.

`switch` statements can have a cleaner syntax over complicated `if else` statements.

Take a look at the example below – instead of using this long `if else` statement, you might choose to go with an easier to read `switch` statement.

```js
const pet = "dog";

if (pet === "lizard") {
  console.log("I own a lizard");
} else if (pet === "dog") {
  console.log("I own a dog");
} else if (pet === "cat") {
  console.log("I own a cat");
} else if (pet === "snake") {
  console.log("I own a snake");
} else if (pet === "parrot") {
  console.log("I own a parrot");
} else {
  console.log("I don't own a pet");
}
```

```js
const pet = "dog";
 
switch (pet) {
  case "lizard":
    console.log("I own a lizard");
    break;
  case "dog":
    console.log("I own a dog");
    break;
  case "cat":
    console.log("I own a cat");
    break;
  case "snake":
    console.log("I own a snake");
    break;
  case "parrot":
    console.log("I own a parrot");
    break;
  default:
    console.log("I don't own a pet");
    break;
}
```

`switch` statements will not be appropriate to use in all situations. But if you feel like the `if else` statements are long and complicated, then a `switch` statement could be an alternative option. 

## The logical AND (&&) operator and if...else statements in JavaScript

In the logical AND (`&&`) operator, if both conditions are `true`, then the `if` block will be executed. If one or both of the conditions are `false`, then the `else` block will be executed. 

In this example, since age is greater than 16 and the `ownsCar` variable is `true`, the `if` block will run. The message printed to the console will be "Jerry is old enough to drive and has his own car."

```js
const age = 17;
const ownsCar = true;

if (age >= 16 && ownsCar) {
  console.log("Jerry is old enough to drive and has his own car.");
} else {
  console.log("Jerry does not drive.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-4.22.49-AM.png)

If I change the `age` variable to be less than 16, then both conditions are no longer `true` and the `else` block would be executed instead. 

```js
const age = 13;
const ownsCar = true;

if (age >= 16 && ownsCar) {
  console.log("Jerry is old enough to drive and has his own car.");
} else {
  console.log("Jerry does not drive.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-4.20.19-AM.png)

## The logical OR (||) operator and if...else statements in JavaScript

In the logical OR (`||`) operator, if one or both of the conditions are `true`, then the code inside the `if` statement will execute. 

In this example, even though the `isSale` variable is set to `false`, the code inside the `if` block will still execute because the `boyfriendIsPaying` variable is set to `true`. 

```js
const boyfriendIsPaying = true;
const isSale = false;

if (boyfriendIsPaying || isSale) {
  console.log("Jesse will go shopping.");
} else {
  console.log("Jesse will not go shopping.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-4.40.36-AM.png)

If I were to change the value of the `boyfriendIsPaying` variable to `false`, then the `else` block would execute because both conditions are `false`. 

```js
const boyfriendIsPaying = false;
const isSale = false;

if (boyfriendIsPaying || isSale) {
  console.log("Jesse will go shopping.");
} else {
  console.log("Jesse will not go shopping.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-4.42.12-AM.png)

## The logical NOT (!) operator and if...else statements in JavaScript

The logical NOT (`!`) operator will take something that is `true` and make it `false`. It will also take something that is `false` and make it `true`.

We can modify the example from earlier to use the `!` operator to make the `boyfriendIsPaying` variable  `false`. Since both conditions are `false`, the `else` block would be executed. 

```js
const boyfriendIsPaying = true;
const isSale = false;

if (!boyfriendIsPaying || isSale) {
  console.log("Jesse will go shopping.");
} else {
  console.log("Jesse will not go shopping.");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-5.02.04-AM.png)

## Conditional (ternary) operator in JavaScript

If you have a short `if else` statement, then you might choose to go with the ternary operator.  The word ternary means something composed of three parts.

This is the basic syntax for a ternary operator:

```js
condition ? if condition is true : if condition is false

```

The condition goes before the `?` mark and if it is `true`, then the code between the `?` mark and `:` would execute. If the condition is `false`, then the code after the  `:` would execute. 

In this example, since age is greater than 18, then the message to the console would be "Can vote". 

```js
const age = 32;
const citizen = age >= 18 ? "Can vote" : "Cannot vote";
console.log(citizen);

```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-09-at-5.25.14-AM.png)

This is what the code would look like using an `if else` statement:

```js
const age = 32;
let citizen;

if (age >= 18) {
  citizen = "Can vote";
} else {
  citizen = "Cannot vote";
}

console.log(citizen);
```

## Conclusion

`if else` statements will execute a block of code when the condition in the `if` statement is `truthy`. If the condition is `falsy`, then the `else` block will be executed. 

There will be times where you want to test multiple conditions and you can use an `if...else if...else` statement. 

If you feel like the `if else` statement is long and complicated, then a `switch` statement could be an alternative option. 

Using logical operators to test multiple conditions can replace nested `if else` statements. 

The ternary operator can be used to write shorter code for a simple `if else` statement. 



---
title: Unary, Binary, and Ternary Operators in JavaScript – Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-17T16:58:24.000Z'
originalURL: https://freecodecamp.org/news/unary-binary-ternary-operators-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/16.-unary-binary-ternary.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Dillion Megida\nThere are many operators in JavaScript that let you\
  \ carry out different operations. \nThese operators can be categorized based on\
  \ the number of operands they require, and I'll be using examples to explain these\
  \ categories in this tut..."
---

By Dillion Megida

There are many operators in JavaScript that let you carry out different operations. 

These operators can be categorized based on the number of operands they require, and I'll be using examples to explain these categories in this tutorial.

The three categories of operators based on the number of operands they require are:

* Unary operators: which require one operand (Un)
* Binary operators: which require two operands (Bi)
* Ternary operators: which require three operands (Ter)

Note that these categories do not only apply to JavaScript. They apply to programming in general.

In the rest of this article, I will share some examples of operators that fall under each category.

I have a [video version of this topic](https://youtu.be/dwP0WuzbFA0) you can watch if you're interested.

## What is an Operand?

First, let's understand what an operand is. In an operation, an **operand** is the data that is being **operated on**. The operand combined with the operator makes an operation.

Look at this example:

```js
20 + 30
```

Here we have a sum operation (which we will learn more about later). This operation involves the plus operator `+`, and there are two operands here: `20` and `30`.

Now that we understand operands, let's see examples of operators and the categories they fall under.

## What is a Unary Operator?

These operators require one operand for operation. Providing two or more can result in a syntax error. Here are some examples of operators that fall under this category.

### the `typeof` operator

The `typeof` operator returns the data type of a value. It requires only one operand. Here's an example:

```js
typeof "hello"
// string
```

If you pass two operands to it, you'd get an error:

```js
typeof "hello" 50
// Uncaught SyntaxError: Unexpected number
```

### The `delete` operator

You can use the `delete` operator to delete an item in an array or delete a property in an object. It's a unary operator that requires only one operand. Here's an example with an array:

```js
const array = [2,3,4]
delete array[2]

console.log(array)
// [ 2, 3, <empty> ]
```

Note that deleting items from an array with the `delete` operator is not the right way to do this. I explained why [in this article here](https://dillionmegida.com/p/deleting-items-from-array-with-delete-keyword/)

And here's an example with an object:

```js
const object = {
  name: "deeecode",
  age: 50
}
delete object.age

console.log(object)
// { name: 'deeecode' }
```

### The Unary plus `+` operator

This operator is not to be confused with the arithmetic plus operator which I will explain later in this article. The unary plus operator attempts to convert a non-number value to a number. It returns `NaN` where impossible. Here's an example:

```js
+"200"
// 20 - number

+false
// 0 - number representation

+"hello"
// NaN
```

As you can see here again, only one operand is required, which comes after the operator.

I'll stop with these three examples. But know that there are more unary operators such as the increment `++`, decrement `++`, and Logical NOT `!` operators, to name a few.

## What is a Binary Operator?

These operators require two operands for operation. If one or more than two operands are provided, such operators result in a syntax error. 

Let's look at some operators that fall under this category

### Arithmetic Operators

All arithmetic operators are binary operators. You have the first operand on the left of the operator, and the second operand on the right of the operator. Here are some examples:

```js
10 + 20
// 30

20 - 5
// 15

30 / 6
// 5
```

If you don't provide two operands, you will get a syntax error. For example:

```js
10 +
// SyntaxError: Unexpected end of input
```

### Comparison Operators

All comparison operators also require two operands. Here are some examples:

```js
80 < 20
// false

10 < 40
// true

2 >= 2
// true
```

### Assignment Operator `=`

The assignment operator is also a binary operator as it requires two operands. For example:

```js
const number = 20
```

On the left, you have the first operand, the variable (`const number`), and on the right, you have the second operand, the value (`20`).

You're probably asking: "isn't `const number` two operands?". Well, `const` and `number` makes up one operand. The reason for this is `const` defines the behavior of `number`. The assignment operator `=` does not need `const`. So you can actually use the operator like this:

```js
number = 20
```

But it's good practice to always use a variable keyword.

So like I said, think of `const number` as one operand, and the value on the right as the second operand.

## What is a Ternary Operator?

These operators require three operands. In JavaScript, there is **one operator** that falls under this category – the conditional operator. In other languages, perhaps, there could be more examples.

### The Conditional Operator `? ... :`

The conditional operator requires three operands:
* the **conditional expression**
* the **truthy expression** which gets evaluated if the condition is `true`
* the **falsy expression** which gets evaluated if the condition is `false`.

You can learn more about the [Conditional Operator here](https://www.freecodecamp.org/news/the-ternary-operator-in-javascript/)

Here's an example of how it works:

```js
const score = 80
const scoreRating = score > 50 ? "Good" : "Poor"

// "Good"
```

The first operand – the conditional expression – is `score > 50`.

The second operand – the truthy expression – is "Good", which will be returned to the variable `scoreRating` if the condition is `true`.

The third operand – the falsy expression – is "Poor", which will be returned to the variable `scoreRating` if the condition is `false`.

I've written an article related to this operator that you can check out [here](https://www.freecodecamp.org/news/why-a-ternary-operator-is-not-a-conditional-operator-in-js/). It's about why a ternary operator is not a conditional operator in JavaScript.

## Wrap Up

Operations in JavaScript involve one or more operands and an operator. And operators can be categorized based on the number of operands they require.

In this article, we've looked at the three categories of operators: **unary**, **binary**, and **ternary**. We also looked at the examples of operators in JavaScript that fall under each category.

Please share this article if you find it helpful.


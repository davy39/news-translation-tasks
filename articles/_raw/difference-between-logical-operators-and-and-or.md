---
title: Difference between logical operators AND and OR
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-27T08:15:17.000Z'
originalURL: https://freecodecamp.org/news/difference-between-logical-operators-and-and-or
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/31-and-or.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  AND && and OR || are logical operators in JavaScript which you can use for performing
  different logical expressions. In this article, I''ll explain the difference between
  them.

  The goal of this article is for you to understand how th...'
---

By Dillion Megida

AND `&&` and OR `||` are logical operators in JavaScript which you can use for performing different logical expressions. In this article, I'll explain the difference between them.

The goal of this article is for you to understand how these operators work and how they are different.

To understand these operators, it's important to understand the concept of **truthy** and **falsy** values in JavaScript.

## Truthy and Falsy values

In JavaScript, many values can be represented by their boolean equivalents. A value that is represented by `false` is a falsy value and a value that is represented by `true` is a truthy value. Let's see some examples:

```js
0
false
undefined
null
"" // empty string
```

The values `0`, `false`, `undefined`, `null`, and empty string `""` are falsy values because their boolean representations are `false`.

As for truthy values, any value that is not `falsy` is `truthy`. This means truthy values include `true`, `1`, `[3. 4]`, `{}`, `"hello"`.

Now that we have that out of the way, let's see how these tie into the `AND` and `OR` operators.

I have a [video version of this topic](https://youtu.be/HZ-X6JVqfhQ) if you're interested in that.

## The `AND` operator

The logical `AND` operator is used between two operands in an expression like this:

```js
operand1 && operand2
```

The operator returns the second operand **if the first operand is a truthy value**. If the first operand is a falsy value, the operator would return the first operand instead. As we have seen, a truthy value is a value that evaluates to `true`.

Let's see an example:

```js
const exp1 = 5
const exp2 = "Dillion"

const result = exp1 && exp2

console.log(result)
// "Dillion"
```

In this example, we have `exp1` with a value of **5** and `exp2` with a value of **"Dillion"**. Then we have the `result` variable which holds the returned value from using the `&&` operator between `exp1` and `exp2`.

What happens here is that the operator, from the left, checks if `exp1` is a **truthy value**. **5** is a truthy value, so the operator returns the value on the right. That's why `result` holds the value of **"Dillion"**.

Let's see another example where we use the `AND` operator multiple times:

```js
function returnFalsy() {
  return ""
}

const exp1 = [1, 2]
const exp2 = returnFalsy()
const exp3 = { name: "Dillion" }

const result = exp1 && exp2 && exp3

console.log(result)
// ""
```

As we can see in this example, we have:

- `exp1` with an array
- `exp1` with the returned value of calling `returnFalsy()` (which is an empty string--a **falsy value**)
- `exp3` with an object

Lastly, we have the `result` variable which holds the returned value from using the `&&` operator between `exp1` and `exp2` and between `exp2` and `exp3`.

What we have here is `exp1 && exp2` as operand 1 and operand 2. Then the result of this expression will become operand 1 for the next expression: `result && exp3`. `exp3` here is the second operand in the second expression.

What happens here is that the operator, from the left, checks if `exp1` is a **truthy value**. In this case, we have an array, which is a truthy value, which means the second operand `exp2` will be returned. `exp2` becomes the first operand, and `exp3` becomes the second operand for the second expression.

The second `&&` operator checks if `exp2` is a truthy value. In this case, the empty string **""** is a falsy value, so the operator returns `exp2`. It doesn't bother checking `exp3` because the fact that `exp2` is falsy, means the operator would stop checking from left to right.

What happens here is **short-circuiting** which you can learn more about in my [article on short-circuit operators](https://dillionmegida.com/p/short-circuit-in-programming-simplified/)

## The `OR` operator

The logical `OR` operator is used between two operands in an expression like this:

```js
operand1 || operand2
```

The operator returns the first operand **if the first operand is a truthy value**. If the first operand is a falsy value, the operator would return the second operand instead.

Let's see an example:

```js
const exp1 = 5
const exp2 = "Dillion"

const result = exp1 || exp2

console.log(result)
// 5
```

In this example, we have `exp1` with a value of **5** and `exp2` with a value of **"Dillion"**. Then we have the `result` variable which holds the returned value from using the `||` operator between `exp1` and `exp2`.

What happens here is that the operator, from the left, checks if `exp1` is a **truthy value**. **5** is a truthy value, so the operator returns it. That's why `result` holds the value of **5**.

The `OR` operator doesn't bother checking `exp2` because it already found a truthy value. This is the opposite of the `AND` operator. `AND` keeps going from left to right as long as `true`. But `OR` stops (again, [short-circuiting](https://dillionmegida.com/p/short-circuit-in-programming-simplified/) once it sees a `true`--it only keeps going from left to right as long as `false`

Let's see another example where we use the `OR` operator multiple times:

```js
function returnFalsy() {
  return ""
}

const exp1 = null
const exp2 = returnFalsy()
const exp3 = { name: "Dillion" }

const result = exp1 || exp2 || exp3

console.log(result)
// { name: "Dillion" }
```

As we can see in this example, we have:

- `exp1` with a value of `null` (a **falsy value**)
- `exp1` with the returned value of calling `returnFalsy()` (which is an empty string--a **falsy value**)
- `exp3` with an object

Lastly, we have the `result` variable which holds the returned value from using the `||` operator between `exp1` and `exp2` and between `exp2` and `exp3`.

What we have here is `exp1 || exp2` as operand 1 and operand 2. Then the result of this expression will become operand 1 for the next expression: `result || exp3`. `exp3` here is the second operand in the second expression.

What happens here is that the operator, from the left, checks if `exp1` is a **truthy value**. In this case, we have `null`, which is a falsy value, which means the second operand `exp2` will be returned. `exp2` becomes the first operand, and `exp3` becomes the second operand for the second expression.

The second `||` operator checks if `exp2` is a truthy value. In this case, the empty string **""** is a falsy value, so the operator returns `exp3`. As you notice here, the `OR` operator keeps going as long as it comes across false values. It only stops once it finds a truthy value or when it comes to the end of the expressions.

## Using `AND` and `OR` in `if` statements

`if` statements allow you to create conditional statements where you determine what would be executed based on a condition.

<!-- You can learn more about [if statements in this article](). -->

Let's see an example where we use `AND` in an `if` statement:

```js
const isLoggedIn = true
const cart = []

if (isLoggedIn && cart.length) {
  console.log("Cart not empty")
} else {
  console.log("Cart is empty")
}
```

Can you guess the result of executing this code? The result is:

```js
// Cart is empty
```

Here's why. The condition for the `if` statement is `isLoggedIn && cart.length`. The left operand is `isLoggedIn` which evaluates to `true`. Remember that the `&&` operator returns the right operand if the left operand is `true`. It only returns the left operand if the left operand is `false`. In this case, the operator would return `cart.length`, which evaluates to 0 since the `cart` array is empty.

Which means the `if` block is executed as `if(0)`.

The `if` statement would coerce `0` to a boolean value. As we saw earlier, `0` is a **falsy value**. So the `if` statement seeing that the condition expression `0` is `false`, would execute the `else` block: `console.log("Cart is empty")`. You can learn more about [type coercion in this article](https://www.freecodecamp.org/news/coercion-and-type-conversion-in-javascript/).

Let's say `OR` was used instead:

```js
const isLoggedIn = true
const cart = []

if (isLoggedIn || cart.length) {
  console.log("Cart not empty")
} else {
  console.log("Cart is empty")
}
```

Can you guess the result of this? Here it is:

```js
// Cart not empty
```

Here's why. The condition for the `if` statement here is `isLoggedIn || cart.length`. The left operand is `isLoggedIn` which evaluates to `true`. Remember that the `||` operator returns the left operand if it is `true`. It only returns the right operand if the left operand is `false`. In this case, the operator would return `isLoggedIn` which evaluates to `true`.

Which means the `if` block is executed as `if(true)`.

In this case, coercion doesn't happen as `true` is already a boolean value. So the `if` statement seeing that the condition expression `true` is `true`, would execute the `if` block: `console.log("Cart not empty")`.

## Wrap Up

Here's a summary of the difference between `AND` and `OR`:

- `AND` returns the right expression if the left expression is `true`
- `AND` returns the left expression if the left expression is `false`
- `OR` returns the right expression if the left expression is `false`
- `OR` returns the left expression if the left expression is `true`

You notice that the `OR` is the inverse of `AND`? While `AND` keeps going to the right as long as the left is `true`, `LEFT` keeps going to the right as long as the left is `false` 

If you enjoyed this article, please share it with others.




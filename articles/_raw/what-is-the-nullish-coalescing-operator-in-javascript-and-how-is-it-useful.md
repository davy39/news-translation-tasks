---
title: What is the Nullish Coalescing Operator in JavaScript, and how is it useful
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-05T06:55:34.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-nullish-coalescing-operator-in-javascript-and-how-is-it-useful
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/28-nullish-coalescing-operator.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  The Nullish Coalescing Operator is a new logical operator in JavaScript introduced
  in ES 2020. In this article, we''ll understand how this operator works.

  There are over four logical operators in JavaScript: the AND &&, OR ||, NOT !,...'
---

By Dillion Megida

The Nullish Coalescing Operator is a new logical operator in JavaScript introduced in ES 2020. In this article, we'll understand how this operator works.

There are over four logical operators in JavaScript: the AND `&&`, OR `||`, NOT `!`, and the Nullish Coalescing Operator `??`.

Sometimes called the **Nullish Operator**, this operator is used between two operands:

```js
operand1 ?? operand2
```

To understand this operator, we'll have to understand what "nullish", "coalescing" and **short-circuiting** mean.

I have a [video on this topic](https://youtu.be/CX3VWymirxw) that you can check out also.

## What are "nullish" values?

Nullish values in JavaScript are `null` and `undefined`. These values fall under **falsy values** but are more specifically referred to as **null values**. All nullish values are falsy, but not all falsy values (for example, `0`) are nullish.

So, the nullish operator is related to `null` and `undefined` values while other logical operators are related to `truthy` and `falsy` values in general.

## What does "coalescing" mean?
Coalescing, according to the dictionary means "coming together to form one whole". How does this apply to programming? It means you bring multiple values together, to make one value out of it.

Coalescing in programming does not specifically mean "joining the values together", but more about "deciding what value is made out of the provided values".

We'll see how this works with examples later in this article.


## Short-Circuiting

The concept of short-circuiting applies to many programming languages. It occurs when interpreters execute a boolean-related expression and skips the irrelevant part of the expression.

For example, a boolean expression like "I am 40 years old, and I am in tech". This expression would only be `true` if I am 40 years old, and not just that, I am in tech.

After the interpreter executes "I am 40 years old", it cannot yet conclude that the whole expression is true, because in the case that "I am **NOT** in tech", the expression will be false. The second part of the expression is relevant because it can change the result.

But, in the case that "I am **NOT** 40 years old", short-circuiting will happen. Since the first part of the expression returns `false`, the interpreter knows that there is no point evaluating the second expression. The second part is irrelevant, as the value from this expression does not change the result. So the interpreter skips the second part (thereby saving resources--time, power).

This also applies to the nullish operator.

You can learn more about short-circuiting [in this article](https://dillionmegida.com/p/short-circuit-in-programming-simplified/)

## The Nullish Coalescing Operator

Now that we've looked at the fundamentals of this operator, let's understand what this operator does.

When used in an expression, the Nullish Operator checks the first operand (on the left) to see if its value is `null` or `undefined`. If it isn't, the operator returns it from the expression. But if the first operand is any of those values, the operator returns the second operand from the expression.

Let's see a quick example:

```js
function expression1() {
  return null
}

const expression2 = 4 * 5

const result = expression1() ?? expression2

console.log(result)
// 20
```

Here, we have a function called `expression1` which when called returns `null`. And we also have `expression2` which holds the value from the expression **4 * 5**.

For the `result` variable, we use the nullish operator and pass `expression1()` and `expression2` as the operands.

The first operand (the function call expression) returns `null`. The operator confirms that the first operand is `null`, so it returns the value from the second expression: `expression2`.

Let's see another example:

```js
function expression1() {
  console.log("expression1")
  return false
}

function expression2() {
  console.log("expression2")
  return "Dillion"
}

const result = expression1() ?? expression2()

console.log(result)
// expression1
// false
```

Here, we have `expression1`, a function which when called executes `console.log("expression1")`, then returns `false`. And we have `expression2`, which is a function that when called, executes `console.log("expression2")`, and returns "Dillion".

Using the nullish operator, we have the first operand as `expression1()`, and the second operand as `expression2()` and assign the value from the expression to `result`.

When we run this code, you see that we have "expression1" logged, which calls from the execution of `expression1`. And you see that `result` is logged as `false`. This means, `expression1()` is the returned expression from the nullish operator.

The operator checks if the first expression returns `null` or `undefined`, for which it would return the second expression. But in this case, the first expression returns `false`, therefore, the operator would return the first expression.

Another thing you notice is that "expression2" is not logged. This means that `expression2()` is not executed at all. **Short-circuiting** happens here.

Since the operator has already confirmed that the first operand is NOT `null` or `undefined`, it doesn't bother about the second expression, because the value of the second expression does not change what the operator would return.

## Nullish vs OR Operator

The Nullish and OR operators have some similarities, but they work a bit differently.

The OR operator **checks if the first operand is a truthy value**. If the first operand is one, it returns it, else, it returns the second operand.

But, the Nullish operator **checks if the first operand is a nullish value**. If the first operand isn't one, it returns it, else, it returns the second operand

Here's an OR example:

```js
const expression1 = ""
const expression2 = "Dillion"

const result = expression1 || expression2

console.log(result)
// "Dillion"
```

Since the first operand, `expression1`, is a falsy value (empty string), the operator returns the second operand. If `expression1` was 20, for example (which is a truthy value), it would have been returned, and short-circuiting would have happened.

Here's a Nullish example:

```js
const expression1 = undefined
const expression2 = "Dillion"

const result = expression1 ?? expression2

console.log(result)
// "Dillion"
```

Using the nullish operator here, the first operand is `undefined`, a nullish value, so the operator returns the second operand. If `expression1` was `false`, 20, or some other non-nullish value, it would have been returned, and short-circuiting would have happened.

## Using the nullish operator directly with AND/OR

You can directly mix the AND and OR operators in expressions but you cannot do that for the nullish operator. Here's what I mean:

```js
exp1 && exp2 || exp3 && exp4
```

Here, we combine AND and OR. The order in this expression is:
1. "exp1 AND exp2"
2. "the result of that OR exp3"
3. "the result of that AND exp4"

> Don't forget that due to short-circuiting, step 2 or step 3 may never be reached.

But you cannot do these combinations directly with the nullish operator. For example:

```js
exp1 && exp2 ?? exp3 || exp4
```

We're mixing AND, Nullish, and OR here: this will throw a syntax error. Let's see an actual example:

```js
function expression1() {
  return null
}

const expression2 = 20 < 10

const expression3 ="Dillion"

const result = expression1() ?? expression2 || expression3
// SyntaxError: Unexpected token '||'
```

We have `expression1` a function which when called returns `null`, `expression2` which holds the returned value from **20 < 10**, and `expression3` which holds the string value "Dillion".

Use the nullish and OR operators with these three expressions, what I would expect is that:

1. `expression1()` returns `null`, so the nullish operator returns the right side of the expression which is `expression2 || expression3`
2. on the right side, the OR operator is used, which checks if the left side, `expression2` is truthy; since it is a falsy value, the operator returns the right side

But, by executing this, we get an error: **SyntaxError: Unexpected token '||'**. This means you cannot use these operators directly. The only way to combine them is to add parenthesis like this:

```js
const result = (expression1() ?? expression2) || expression3

console.log(result)
// Dillion
```

By surrounding **expression1() ?? expression2** with parentheses, we can then use the returned result as the first operand for the OR operator, and add `expression3` as the second operand.

## Wrap up

The nullish operator is very useful in declaring default values for potential `null` or `undefined` values. Say, you're expecting an object from an API. If that object does not contain an expected property, that property may either hold `null` or be `undefined` like this:

```js
const obj = {}

console.log(obj.type)
// undefined
```

Using the nullish operator, we can provide a default value:

```js
const obj = {}

console.log(obj.type ?? "default")
// "default"
```

There are many other ways you can use this operator for default values or safe checks.

If you enjoyed this article, please share :)



---
title: Coercion and Type Conversion in JavaScript – Explained with Code Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-07T17:03:46.000Z'
originalURL: https://freecodecamp.org/news/coercion-and-type-conversion-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/4.-coercion.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  Coercion is an automatic type conversion that occurs in JavaScript when you want
  to perform certain operations. I''ll explain what coercion is in this article.

  What is Type Conversion?

  As the name implies, type conversion is the proc...'
---

By Dillion Megida

Coercion is an automatic type conversion that occurs in JavaScript when you want to perform certain operations. I'll explain what coercion is in this article.

## What is Type Conversion?

As the name implies, type conversion is the process of converting a value from one type to another. 

Values in JavaScript can be of different types. You could have a number, string, object, boolean – you name it. Sometimes, you may want to convert data from one type to another to fit a certain operation.

Type conversion can either be implicit (automatically done during code execution) or explicit (done by you the developer).

Implicit Type Conversion is also known (and more commonly referred to) as **Coercion** while Explicit Type Conversion is also known as **Type Casting**. Let's look at these two conversions in detail.

I also have a [video version](https://youtu.be/00vjwv2BJqE) of this tutorial if you would prefer that.

## What is Implicit Type Conversion (Coercion)?

There are some operations that you might try to execute in JavaScript which are literally not possible. For example, look at the following code:

```js
const sum = 35 + "hello"
```

Here, you're trying to add a number and a string. This is, practically speaking, not possible. You can only add numbers (**sum**) together or add strings (**concatenate**) together.

So what happens here if you try to run the code?

Well, JavaScript is a weakly typed language. Instead of JavaScript throwing an error, it coerces the type of one value to fit the type of the other value so that the operation can be carried out.

In this case, using the **+** sign with a number and a string, the number is coerced to a string, then the **+** sign is used for a concatenation operation.

```js
const sum = 35 + "hello"

console.log(sum)
// 35hello

console.log(typeof sum)
// string
```

This is an example of coercion where the type of one value is coerced to fit the other so that the operation can continue.

With the plus sign, it is more ideal for the number to be converted to a string (instead of the string converted to a number). This is because a number equivalent to a string is `NaN` but a string equivalent for a number, say `15`, is `"15"` – so it makes more sense to **concatenate** two strings than to **sum** a number and `NaN`.

Look at another example below:

```js
const times = 35 * "hello"

console.log(times)
// NaN
```

Here, we use times **\*** for a number and a string. There's no operation with strings that involves multiplication, so here, the ideal coercion is from string to number (as numbers have compatible operations with multiplication). 

But since a string (in this case, `"hello"`) is converted to a number (which is `NaN`) and that number is multiplied by `35`, the final result is `NaN`.

Coercion is usually caused by different operators used between different data types:

```js
const string = ""
const number = 40
const boolean = true

console.log(!string)
// true - string is coerced to boolean `false`, then the NOT operator negates it

console.log(boolean + string)
// "true" - boolean is coerced to string "true", and concatenated with the empty string

console.log(40 + true)
// 41 - boolean is coerced to number 1, and summed with 40
```

One very common operator that causes coercion is the **loose equality operator** (**==**, or double equals).

## Double Equality and Coercion

In JavaScript, there's both the double equality operator (**==** which is called the **loose equality operator**) and the triple equality operator (**===** which is called the **strict equality operator**). You use both operators to compare values' equality.

### How the Loose Equality Operator Works

The **loose equality operator** does a loose check. It checks if values are equal. The types are not a focus for this operator – only the values are the major factor.

What I mean here is **20**, a value of a `number` type, and **"20"**, a value of the `string` type, are equal when you use double equality:

```js
const variable1 = 20
const variable2 = "20"

console.log(variable1 == variable2)
// true
```

Though the types are not equal, the operator returns `true` because the values are equal. What happens here is **coercion**.

When you use the **loose equality operator** with values of different types, what happens first is coercion. Again, this is where one value is converted to the type that fits the other, before the comparison occurs. 

In this case, the **string "20"** is converted to a number type (which is `20`) and then compared with the other value, and they are both equal.

Another example:

```js
const variable1 = false
const variable2 = ""

console.log(variable1 == variable2)
// true
```

Here, `variable1` is the value **false** (boolean type) and `variable2` is the value **""** (an empty string, of the string type). Comparing both variables with the double equality returns `true`. That's because the empty string is coerced to a boolean type (which is **false**).

### How the Strict Equality Operator Works

This operator does a strict check – that is, it strictly checks the values compared, as well as the types. Type coercion does not occur here, so there are no unexpected answers. Here are the examples from above:

```js
const variable1 = 20
const variable2 = "20"

console.log(variable1 === variable2)
// false

const variable3 = false
const variable4 = ""

console.log(variable3 === variable4)
// false
```

In the case of `variable1` and `variable2`, they have the same values, but the types are not the same. So the triple equality returns `false`.

In the case of `variable3` and `variable4`, they have the same values (if one is converted to the type of the other) but the types are not the same, so the triple equality returns `false` this time, too.

## What is Explicit Type Conversion (Type Casting)?

Here, you explicitly convert a value from one type to another. This can also be for you to execute a certain operation successfully.

To explicitly convert types, you use the type `Constructors`. For example, to convert a number to a string:

```js
const number = 30

const numberConvert = String(number)

console.log(numberConvert)
// "30"

console.log(typeof numberConvert)
// string
```

Another example is to convert a number to a boolean:

```js
const number = 30

const numberConvert = Boolean(number)

console.log(numberConvert)
// true

console.log(typeof numberConvert)
// boolean
```

And one more example, to convert a boolean to a string:

```js
const boolean = false

const booleanConvert = String(boolean)

console.log(booleanConvert)
// "false"

console.log(typeof booleanConvert)
// string
```

In these examples, we explicitly convert a value from one type to another. What are cases where you need to do this?

This is useful when you don't know what type you're expecting for a value. For example, data coming from an API. Let's say an API is configured to return a string, maybe "50" and you want to compare it to a number using strict equality like this:

```js
const apiData = {
  rate: "50"
}

console.log(apiData.rate === 50)
// false
```

In such a case, you want to first ensure that the value is a number type explicitly (instead of relying on the double equality to trigger coercion) before doing the check:

```js
const apiData = {
  rate: "50"
}

const rate = Number(apiData.rate)

console.log(rate === 50)
// true
```

## Wrapping Up

Because JavaScript is a weakly typed language, sometimes you can have unexpected type conversions. This happens implicitly when you try to use some operators between values of different types. Then instead of getting an error, JavaScript tries to "help" you. JavaScript be like...

"Oh, I think they wanted to type a string but they typed a number instead. Let's help them convert it to a string before we carry out the operation. They would appreciate that 😇"

Well not actually like this 😂 but I hope you get the idea.

In this article, we've seen how type conversion works in JavaScript – both implicitly and explicitly – with examples.

While coercion can be helpful sometimes, it can cause unexpected errors, especially when comparing values with the **loose equality operator**. That's why it is recommended to always use the **strict equality operator** for comparing values.

Also, [using TypeScript](https://www.freecodecamp.org/news/an-introduction-to-typescript/) can help you avoid unpredicted errors as you can ensure that variables are the data types that you want them to be.




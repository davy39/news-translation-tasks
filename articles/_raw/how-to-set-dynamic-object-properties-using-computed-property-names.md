---
title: How to Set Dynamic Object Properties using Computed Property Names
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-17T16:53:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-dynamic-object-properties-using-computed-property-names
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/20.-dynamic-object-properties-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Dillion Megida\nWhen declaring objects before ES6, you had to use static\
  \ keys for properties. But since the release of ES6, you can use dynamic keys. \n\
  I'll show you how they work in this article.\nWhat are Static and Dynamic Keys?\n\
  What do I mean by ..."
---

By Dillion Megida

When declaring objects before ES6, you had to use static keys for properties. But since the release of ES6, you can use dynamic keys. 

I'll show you how they work in this article.

## What are Static and Dynamic Keys?

What do I mean by static keys? Take a look at this object:

```js
const obj = {
  name: "dillion",
  age: 1000,
}
```

You can see that `name` and `age` are static keys. They do not come from anywhere – they are not computed (calculated). These keys are directly added to the object.

What if you wanted to add a dynamic key? A dynamic key here refers to the result of an expression. For example, a dynamic key can be a variable or a computed value.

I'll show you how to do that in this article.

I have a [video version](https://youtu.be/iP02oY4rt6A) of this topic you can also check out.

## The Computed Property Names Feature

The Computed Property Names feature in ES6 allows you to set property names dynamically – that is, property names will be expressions that evaluate to a value.

This feature is useful for property names that you do not know ahead of time. For a property name like "name", you already know this, so you can create your object like this:

```js
const object = {
  name: value
}  
```

But what about a property name that comes from an expression executed during runtime? Such an expression can be a concatenation, function call, or a conditional expression, to name a few. 

In such cases, you do not know the property name ahead of time. And this is where you use the computed property names feature.

To use computed values for property names, you use square brackets and pass the expression.

Here's the syntax:

```js
const object = {
  [expression]: value
}
```

### How to Set Variables as Property Names

Let's look at a variable example:

```js
const key1 = "language"
const key2 = "isStudent"

const obj = {
  name: "dillion",
  age: 1000,
  [key1]: "javascript",
  [key2]: true
}

console.log(obj)
// {
//   name: "dillion",
//   age: 1000,
//   language: "javascript",
//   isStudent: true
// }
```

As you can see in this example, `name` and `age` are added directly, as static keys. But, `language` and `isStudent` are not added as static keys. They are added dynamically, as variable expressions: `[key1]` and `[key2]`. The returned values of the expressions then represent the keys that will be added to the object.

This is just one example showing a variable expression. Like I said, you can use different forms of expressions that returns a value.

Let's see another expression example.

### How to Set Conditional Expressions as Property Names

Conditional expressions, created with the [conditional operator](https://www.freecodecamp.org/news/the-ternary-operator-in-javascript/), allows you to define conditions. A certain value will be returned if the condition is true, and another value will be returned if false.

Let's see an example using a conditional expression as a property name:

```js
const age = 10

const key1 = "ageIsMoreThan5"
const key2 = "ageIsMoreThan10"

const obj = {
  name: "dillion",
  [age > 10 ? key2 : key1]: true
}

console.log(obj)
// {
//   name: "dillion",
//   ageIsMoreThan5: true
// }
```

Here, we have an `age` variable which holds a number value of **10**. 

In the object `obj`, we have a conditional expression: `age > 10 ? key2 : key1`. This expression states that if the value of the `age` variable is greater than 10, `key2` is returned, else `key1` is returned. 

Because **10** (value of `age`) is not greater than 10, `key2` is returned. The value of the `key2` variable is `ageIsMoreThan5`.

And if `age` is **20**, a different property key is added to `obj`:

```js
const age = 20

const key1 = "ageIsMoreThan5"
const key2 = "ageIsMoreThan10"

const obj = {
  name: "dillion",
  [age > 10 ? key2 : key1]: true
}

console.log(obj)
// {
//   name: "dillion",
//   ageIsMoreThan10: true
// }
```

As you can see here, the conditional expression is evaluated to `key2` as `age > 10` returns `true`. The value of `key2` is "ageIsMoreThan10", so that is the property added to the object.

## Wrapping Up

In this article, I've shown you how the Computed Property Names support in JavaScript works to add dynamic keys when declaring objects.

You can think of any expression that returns a value. Such expressions can be used in brackets, to serve as a property key in an object.

You can also use this feature for accessing/modifying an existing property or adding a new property. You can learn more about this in my article on [Dot Notation and Bracket Notation for Object Properties](https://freecodecamp.org/news/dot-notation-vs-square-brackets-javascript/).

If you found this piece helpful, please share 🙏🏾



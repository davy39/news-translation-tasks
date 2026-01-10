---
title: Why a Ternary Operator is not a Conditional Operator in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-17T17:17:44.000Z'
originalURL: https://freecodecamp.org/news/why-a-ternary-operator-is-not-a-conditional-operator-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/17.-ternary-not-conditional.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Dillion Megida\nUntil recently, I called a ternary operator a conditional\
  \ operator in JavaScript. But I just learned that this isn't correct. \nIn this\
  \ tutorial, I will explain how I learned this, and hopefully it teaches you something\
  \ new.\nI have a..."
---

By Dillion Megida

Until recently, I called a ternary operator a conditional operator in JavaScript. But I just learned that this isn't correct. 

In this tutorial, I will explain how I learned this, and hopefully it teaches you something new.

I have a [video version on this topic](https://youtu.be/vcNlFKzZTq4) you can watch as well to supplement your learning.

## How I Learned About the Ternary Operator

I recently wrote an article on [the Ternary operator in JavaScript](https://www.freecodecamp.org/news/the-ternary-operator-in-javascript/). In that article, I defined the ternary operator starting like this:

> "The ternary operator is a conditional operator..."

Here's a screenshot of that sentence:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-80.png)

**Note:** I'm going to make some updates to that article when I'm done with this, so don't be surprised if you do not see some of the text I mention here.

After publishing that article, [someone shared it on Twitter](https://twitter.com/OnlineMDdavid/status/1612935576373673985?s=20&t=87LZfssH26pOK0bJwMBzXw), saying "Thanks", and then [someone else made a comment under the tweet](https://twitter.com/jonrandy/status/1613541257728626691?s=20&t=87LZfssH26pOK0bJwMBzXw) explaining that "A ternary operator is a conditional operator" is a wrong statement:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-83.png)

These comments made me take a step back, and after reading it a few times, it made total sense. Thanks, Jon!

I then went online to research ternary operators, and the categories of operators in general (which also include **unary** and **binary**) operators.

My learnings from those comments and my research led me to write my recent article on [Unary, Binary and Ternary Operators in JavaScript](https://www.freecodecamp.org/news/unary-binary-ternary-operators-javascript/), where I explained these categories, and showed some examples of operators that fall under each category. It's worth checking out.

## It's True – a Ternary Operator is not a Conditional Operator

In my article on Unary, Binary, and Ternary Operators, I explained that:
* Unary operators require one operand
* Binary operators require two operands
* Ternary operators require three operands

I also mentioned that these categories do not apply to only JavaScript, but to programming languages in general.

An example of a unary operator is `typeof`, which requires only one operand.

For binary operators, an example is the arithmetic plus `+` operator which requires two operands (one before, and the other after the operand) to perform the sum operation.

While unary and binary operators have a couple of examples under them, **there is ONLY ONE operator which classifies as a ternary operator: the conditional operator**. This is where the confusion comes from.

The conditional operator requires three operands:

```js
condition ? truthyExpression : falsyExpression
```

`condition` is the first operand, `truthyExpression` is the second, and `falsyExpression` is the third.

The reason why many people (including myself, until recently) call the ternary operator a conditional operator, is because the conditional operator is the only ternary operator in JavaScript (and some other languages as well).

But one thing to note here is that in some other programming languages (that currently exist or will in the future), there could be more examples of the ternary operator. 

So the point is that "a ternary operator **is not** a conditional operator". The better statement is: "A conditional operator is a ternary operator". A conditional operator requires three operands, which means it falls under the ternary category.

## Wrapping Up

The purpose of this article isn't to say "don't ever say a ternary operator is a conditional operator". You can still stay that and every developer will likely understand what you're saying.

The purpose of this article is to show you that "literally", that statement is not correct, even though it is widely used.

The better statement (which I will learn to start saying henceforth) is "a conditional operator is a ternary operator in JavaScript"

If you learned something from this article, please share it with others :)



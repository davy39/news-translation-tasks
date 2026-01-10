---
title: How the Question Mark (?) Operator Works in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-03T17:13:24.000Z'
originalURL: https://freecodecamp.org/news/how-the-question-mark-works-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--5--1.png
tags:
- name: JavaScript
  slug: javascript
- name: js
  slug: js
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nishant Kumar

  The conditional or question mark operator, represented by a ?, is one of the most
  powerful features in JavaScript. The ? operator is used in conditional statements,
  and when paired with a :, can function as a compact alternative to i...'
---

By Nishant Kumar

The conditional or question mark operator, represented by a `?`, is one of the most powerful features in JavaScript. The `?` operator is used in conditional statements, and when paired with a `:`, can function as a compact alternative to `if...else` statements.

But there is more to it than meets the eye. There are three main uses for the `?` operator, two of which you might not used or even heard of. Let's learn about them all in detail.

## Three Main Uses for the Question Mark (`?`) in JavaScript:

1. Ternary Operator
2. Optional Chaining
3. Nullish Coalescing

We'll look at each of these in detail, starting with the most common way you'll see the `?` operator being used – as a ternary operator.

## 1. Ternary Operator

The term ternary means composed of three items or parts. The `?` operator is also called the ternary operator because, unlike other operators such as strict equal (`===`) or remainder (`%`), it's the only one that takes three operands.

Starting with `?`, we add a condition on the left side and a value on the right side to return when the condition is true. Then we add a colon (`:`) followed by a value to return if the condition is false.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--1-.png)

The ternary operator is basically a shortcut for a traditional `if...else` statement.

Let's compare a ternary operator with a longer `if...else` statement:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--22-.png)

Here, the ternary operator occupies only one line of code, whereas the `if...else` takes seven lines.

Using a ternary operator is much more effective, right?

## 2. Optional Chaining

In 2020, an awesome new feature known as Optional Chaining was introduced.

To understand how it works, imagine this scenario.

Let's say you have code that calls on an object property that doesn't exist, which triggers an error at run time. This may be because of a missing or undefined value in your database or from an API:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--23--2.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-01-25-00-56-06.png)
_A common error – `TypeError: Cannot read property ‘salary’ of undefined`_

Thanks to Optional Chaining, you can just insert a `?` between the property name and the period between the next property. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--24-.png)

With that, it will just return `undefined` instead of throwing an ugly error.

Optional Chaining is truly a life-changing feature for JavaScript developers. 

## 3. Nullish Coalescing

In some cases, you have to set a default value for a missing property name or value. 

For example, let's say we are creating a Weather App in which we are fetching the temperature, humidity, wind speed, pressure, time of sunrise and sunset, and the picture of the city. We inputted a place, let's say _Bangalore_, but for some reason, its image is not there in the database.

When the app fetches and displays the data, the picture will be blank, which can look ugly. What we can do, in that case, is set a default picture for those cities which don't have an image, Bangalore in our case. 

This way, when the app displays the data, the default picture will be there for the cities without images.

You can do this using the `||` operator, known as the logical OR operator:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--4-.png)

But if you use `||` to provide a default value, you may encounter unexpected behaviors if you consider some values as usable (for example, `''` or `0`).

Consider a scenario where a variable has the value of 0 or an empty string. If we use (`||`), it will be considered as undefined or NULL and return some default value that we have fixed.

Instead of the logical OR (`||`) operator, you can use double question marks (`??`), or Nullish Coalescing. 

Let's learn with an example.

```javascript
const value1 = 0 || 'default string';
console.log(value1);


const value2 = '' || 1000;
console.log(value2);
```

Here, we have '0' and 'default string' in variable value1. If we log its value in the console, we will get 'default string', which is weird. Instead of the default string, we should be getting 0, as zero is not undefined or null. So, '`||`' fails to do the job here.

Similarly, it's the same with value2.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--25-.png)
_Output for '`||`'_

```javascript
const value1 = 0 ?? 'default string';
console.log(value1);


const value2 = '' ?? 1000;
console.log(value2);
```

But if we replace '`||`' with '`??`', we will get 0 and an empty string, which makes it so cool.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--26-.png)
_Output for '`??`'_

Nullish Coalescing works exactly like the logical OR operator, except you will get the right side value when the left side value is `undefined` or `null`.

In other words, `??` only allows `undefined` and `null` values, not empty strings (`''`) or `0`s.

## Conclusion

Now hopefully you understand how the `?` operator works in JavaScript. It looks simple, but it's one of the most powerful characters in the language. It provides syntactic sugar in three awesome but different ways. 

Try them them out and let me know how it goes.

Happy learning!


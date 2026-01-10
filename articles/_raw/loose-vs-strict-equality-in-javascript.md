---
title: How is == Different from === in JavaScript? Strict vs Loose Equality Explained
subtitle: ''
author: Sobit Prasad
co_authors: []
series: null
date: '2023-02-14T18:09:26.000Z'
originalURL: https://freecodecamp.org/news/loose-vs-strict-equality-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/shapes--1--1.png
tags:
- name: Equality
  slug: equality
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'If you are reading this blog, you''re probably learning JavaScript – and
  that''s awesome.

  Double equals (==) and triple equals (===) in JavaScript often make beginners scratch
  their heads. This doesn''t mean that you should fear JavaScript, in fact jarg...'
---

If you are reading this blog, you're probably learning JavaScript – and that's awesome.

Double equals (==) and triple equals (===) in JavaScript often make beginners scratch their heads. This doesn't mean that you should fear JavaScript, in fact jargon like this makes JavaScript even more beautiful once you know how it works.

## What are `==` and `===` in JavaScript?

Now, one thing we need to remember is that both `==` and `===` are used for comparisons and to find the degree of sameness or equality between the things we are comparing.

Both `==` and `===` returns **true** if they find equality and **false** otherwise. But there is a catch: `==` and `===` use different criteria to measure the degree of equality.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/shapes--2-.png align="left")

With that said, let's understand how `==` (double equals) is different from `===` (triple equals) using different examples.

## How Double Equals (==) Works – with Examples

Double equals (==) is often referred to as 'loose equality' because it performs type coercion before making any comparison.

This means that if the datatypes of the operands we are comparing are different, then the JavaScript Engine automatically converts one of the operands to be the same as the other one in order to make the comparison possible.

Let's understand with the help of an example.

```js
const a = 100;
const b = '100';

console.log(a == b) // true
```

In the above example, we have two variables `a` and `b`. The type of variable `a` is `number` and the type of variable `b` is `string`.

Now, when we compare the two variables using double equals (`==`) we get `true` as our output.

This is because the type of the variable `a` is converted to a `string` before making the comparison.

After the comparison, the value is checked in both the variables. If it's the same, we will get `true`, and we'll get `false` otherwise. In our case, it's `true`.

**It is important to note that the actual values remains unchanged. It only implicitly gets converted while comparing.**

### Rules for Type Coercion

The above example is quite easy, isn't it? So, let's test it again with an another example. And after that, we will explore the rules for type coercion.

```js
const a = true;
const b = 'true';

console.log(a == b)
```

Now, what do you think will be the output? If your answer was `true`, unfortunately that's not correct. But if you figured out that it was `false`, then congrats.

If your answer was wrong, don't worry because we are going to learn some rules that will help you understand it even better.

So, here are the rules for type coercion in JavaScript:

* If either operand is a `string`, the other operand will be converted to a `string`.
    
* If either operand is a `number`, the other operand will be converted to a `number`.
    
* If either operand is a `boolean`, it will be converted to a `number` (`true` becomes `1` and `false` becomes `0`).
    
* If one operand is an `object` and the other is a primitive value, the object will be converted to a primitive value before the comparison is made.
    
* If one of the operands is `null` or `undefined`, the other must also be `null` or `undefined` to return `true`. Otherwise it will return `false`.
    

Now, from point three, you know why our answer was `false` in the above example.

It is because the value of the variable `a` (`true`) gets converted to a number before the comparison. So after comparison – where we're now comparing 1 and `'true'` – we get `false` because the variables contain different values.

## How Triple Equals (===) Works – with Examples

Triple equals (===), also referred to as "strict equality", works similarly to how double equals (==) works, with one important difference: it does not convert the types of the operands before comparing.

While comparing the variables, it first checks if the types differ. If they do, it returns `false`. If the types match, then it checks for the value. If the values are same and are not numbers, it returns `true`.

Finally, if both the operands are numbers and are not `NaN`, and they have the same value, then it returns `true`. Otherwise, `false`.

Let's understand this with the help of examples:

```js
const a = 100;
const b = '100';

console.log(a === b);
```

We have taken the same example as above, but instead of comparing with double (==) equals we are comparing with triple equals (===).

So, you may have guessed the answer already. Yeah, it's `false`, Why? Because the type of variable `a` is number and type of variable `b` is string.

While comparing, triple equals checks for the types of the operands first – and those types differ in this example. So, it returns `false`.

Let's look at another example:

```js
const a = true;
const b = 1;

console.log(a === b);
```

In the above example, we have two variables `a` and `b`. The type of variable `a` is boolean and the type of variable `b` is number.

So, if we're comparing using triple equals (===), it will return `false` – because again, the variables have different types.

## Conclusion

The `==` and `===` operators in JavaScript are comparison operators that we use to determine if two values are equal or not.

The `==` operator performs a loose equality comparison that performs type coercion if necessary to make the comparison possible.

The `===` operator, on the other hand, performs a strict equality comparison that does not perform type coercion and requires the operands to have the same type (as well as the same value).

Type coercion in JavaScript can sometimes lead to unexpected results, so it's mostly recommended to use the strict equality operator `===` instead of the loose equality operator `==`.

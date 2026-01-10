---
title: JavaScript Triple Equals Sign VS Double Equals Sign – Comparison Operators
  Explained with Examples
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-03-12T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-triple-equals-sign-vs-double-equals-sign-comparison-operators-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c2d740569d1a4ca306d.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'You may have seen double and triple equals signs in JavaScript. But what
  do they mean?

  Well in short: == inherently converts type and === does not convert type.

  Double Equals (==) checks for value equality only. It inherently does type coercion.
  This...'
---

You may have seen double and triple equals signs in JavaScript. But what do they mean?

Well in short: `==` inherently converts type and `===` does not convert type.

Double Equals (`==`) checks for value equality only. It inherently does type coercion. This means that before checking the values, it converts the types of the variables to match each other.

On the other hand, Triple Equals (`===`) does not perform type coercion. It will verify whether the variables being compared have both the same value **AND** the same type.

OK - so let's help you better understand the difference through a few examples. For each of these, consider what the output of these statements will be.

### Example 1:

```js
const foo = "test" 
const bar = "test"  

console.log(foo == bar) //true
console.log(foo === bar) //true                            
```

The value and the type of both `foo` and `bar` is same. Therefore the result is `true` for both.

### Example 2:‌

```js
const number = 1234 
const stringNumber = '1234'  

console.log(number == stringNumber) //true
console.log(number === stringNumber)  //false                                   

```

The value of `number` and `stringNumber` looks similar here. However, the type of `number` is `Number` and type of `stringNumber` is `string`. Even though the values are same, the type is not the same. Hence a `==` check returns `true`, but when checked for value **and** type, the value is `false`. 

### Example 3:

```js
console.log(0 == false) //true
console.log(0 === false) //false                  
```

Reason: same value, different type. Type coercion 

This is an interesting case. The value of `0` when checked with `false` is same. It is so because `0` and `false` have the same value for JavaScript, but when checked for type **and** value, the value is false because `0` is a `number` and `false` is `boolean`. 

### Example 4: 

```
const str = ""

console.log(str == false) //true
console.log(str === false) //false
```

The value of empty string and `false` is same in JavaScript. Hence, `==` returns true. However, the type is different and hence `===` returns false. 

## When should you use `==` and when should you use `===`?

When in doubt, use `===`. This will save you from a ton of potential bugs.

If you are supporting a use case where you can be a little lenient about the type of incoming data, then use `==`. For example, if an API accepts both `"true"` and `true` from the client, use `==`. In short, do not use `==` unless you have a strong use case for it. 

Here's a handy JavaScript truth table for your reference, and to show you just how complicated equality is in JavaScript:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-6.png)
_Source: [https://dorey.github.io/JavaScript-Equality-Table/](https://dorey.github.io/JavaScript-Equality-Table/)_

If you enjoyed this article, be sure to follow me on twitter for updates.

%[https://twitter.com/shrutikapoor08/status/1180173695643348992?s=20]


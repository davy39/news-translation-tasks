---
title: JavaScript Comparison Operators – How to Compare Objects for Equality in JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-01-25T18:47:40.000Z'
originalURL: https://freecodecamp.org/news/javascript-comparison-operators-how-to-compare-objects-for-equality-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-christina-morillo-1181675.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'While coding in JavaScript, there may be times when you need to compare
  objects for equality. The thing is, comparing objects in JavaScript is not that
  straightforward.

  In this article, you learn three ways to compare objects for equality in JavaScri...'
---

While coding in JavaScript, there may be times when you need to compare objects for equality. The thing is, comparing objects in JavaScript is not that straightforward.

In this article, you learn three ways to compare objects for equality in JavaScript.

Let's get into it!

## What's the Difference Between Comparing Primitive Data Types VS Non-Primitive Data Types in JavaScript?

Data types in JavaScript fall into one of two categories:

- Primitive (such as Number, String, Boolean, Undefined, Null, Symbol)
- Non-primitive (such as Object)

Primitive data types refer to a single value, and comparing primitive values is relatively straightforward – you only need to use any of the comparison operators.

In the following example, I use the strict equality operator, `===`, which checks if the two operands are equal and returns a Boolean as a result:

```javascript
let a = 1;
let b = 1;

console.log(a === b); // true
```

You can also assign the value of the variable `a` to another variable, `a1`, and compare them:

```javascript
let a = 1;
let b = 1;

let a1 = a;

console.log(a === a1); // true
```

In the example above, both variables point to the same value, so the result is `true`.

When it comes to objects, however, comparing them isn't that straightforward.

```javascript
let a = { name: 'Dionysia', age: 29};
let b = {name: 'Dionysia', age:29};

console.log(a === b); // false
```

Even though both objects have the same key and value pairs, the result of the comparison is `false`. Why is that?

Is it because I used the strict equality operator, `===`? What happens if I use the loose quality operator, `==`?

```javascript
let a = { name: 'Dionysia', age: 29};
let b = {name: 'Dionysia', age:29};

console.log(a == b); // false
```

I get the same result! 

Both `a` and `b` are seemingly the same, yet the objects are not equal when I use `===` or `==`.

You would think that two objects with the same properties and properties with the same values would be considered equal.

The reason for this result has to do with how JavaScript approaches testing for equality when it comes to comparing primitive and non-primitive data types.

The difference between primitive and non-primitive data types is that:

- primitive data types are compared by *value*.
- non-primitive data types are compared by *reference*.

In the following sections, you will see some ways to compare objects for equality.

## How to Compare Objects by Reference in JavaScript

As you saw from the example in the section above, using `==` and `===` returns `false` when you try to compare objects by value:

```javascript
let a = { name: 'Dionysia', age: 29};
let b = {name: 'Dionysia', age:29};

console.log(a === b); // false
```

Both objects have identical keys and values, but the result was `false` because they are different instances. 

To compare objects by reference, you have to test whether both point to the same location in memory. 

When referring to an object, you refer to an address in memory.

Let's see an example:

```javascript
let a = { name: 'Dionysia', age: 29};

let b = a;


console.log(a === b); // true
```

In the example above, thanks to the line `let b = a;`, both variables have the same reference and point to the same object instance, so the result is `true`.

When I assign the variable `a` to the `b`, the address of `a` gets copied to `b`. This results in both having the same address – not the same value.

With that said, most of the time, you will want to compare objects by value and not by instance.

And as you saw, you can't just use `==` or `===` to compare objects by value – it requires a bit more work.

## How to Compare Objects Using The `JSON.stringify()` Function in JavaScript

One way you can compare two objects by value is by using the `JSON.stringify` function.

The `JSON.stringify()` function converts objects into equivalent JSON strings. You can then use any of the comparison operators to compare the strings.
 
```javascript
let a = { name: 'Dionysia', age: 29};
let b = { name: 'Dionysia', age: 29};

console.log(JSON.stringify(a) === JSON.stringify(b)); // true
```

The `JSON.stringify()` function converted both objects into JSON strings, and since both `a` and `b` have the same properties and values, the result is `true`.

But `JSON.stringify()` isn't always the best solution for comparing objects by value since it has limitations.

First of all, when using `JSON.stringify()`, the order of the keys matters.

Look at what happens when the keys are in a different order:

```javascript
let a = { age: 29, name: 'Dionysia'};
let b = { name: 'Dionysia', age: 29};

console.log(JSON.stringify(a) === JSON.stringify(b)); //false
```

In this example, you would expect the result to be `true` since the values are the same – only the order of the keys got reversed. 

`JSON.stringify()` stringifies the object as it is, so the order of the keys is important. If they are not in the same order, the result will be `false`.

So, `JSON.stringify()` is not the best choice for comparing objects since you can't always be certain of the order of the keys.

There is also an additional limitation: JSON doesn't represent all types. 

Look at what happens when the value of one key is undefined:

```javascript
let a = { name: 'Dionysia'};
let b = { name: 'Dionysia', age: undefined};

console.log(JSON.stringify(a) === JSON.stringify(b)); //true
```

In the example above, the result is unexpected. The result should have been `false` but returned as `true` because JSON ignores keys whose values are undefined.

## How to Compare Objects Using the Lodash `_.isEqual()` Method in JavaScript

An elegant and sophisticated solution for comparing objects by their value is to use the well-tested JavaScript library [Lodash](https://lodash.com/) and its `_.isEqual()` method.

Let's take the example from the previous section, where the keys have the same value but are in a different order, and use the `_.isEqual()` method:

```javascript
let a = { age: 29, name: 'Dionysia'};
let b = { name: 'Dionysia', age: 29};

console.log(_.isEqual(a, b)); // true
```

In the previous section, the result when using `JSON.stringify` was `false`.

The Lodash library offers a variety of edge cases and performs a deep comparison between two values to check if the two objects are deeply equal.

## Conclusion

In this article, you learned how to compare objects for equality in JavaScript.

You saw three different ways and the pros and cons of each. When in doubt, the most effective way to compare objects is by using the Lodash library.

Thank you for reading, and happy coding!




---
title: Why Are Two Similar Objects Not Equal in JavaScript?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-18T18:53:47.000Z'
originalURL: https://freecodecamp.org/news/why-are-two-similar-objects-not-equal-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/32-objects-not-equal-1.png
tags: []
seo_title: null
seo_desc: "By Dillion Megida\nIn JavaScript, two objects may not be equal even though\
  \ they appear to be similar. Why is that the case? \U0001F914 Let's understand why.\n\
  For example:\nconst obj1 = {\n  name: \"Dillion\"\n}\nconst obj2 = {\n  name: \"\
  Dillion\"\n}\n\nconsole.log(obj1 =..."
---

By Dillion Megida

In JavaScript, two objects may not be equal even though they appear to be similar. Why is that the case? 🤔 Let's understand why.

For example:

```js
const obj1 = {
  name: "Dillion"
}
const obj2 = {
  name: "Dillion"
}

console.log(obj1 === obj2)
// false
```

As you can see here, `obj1` and `obj2` look similar. They both have the property of `name` with a value of "Dillion". But comparing them--`obj1 === obj2`--returns `false`. 🤔

The same thing applies to arrays:

```js
let arr1 = [1, 2, 3]
let arr2 = [1, 2, 3]

console.log(arr1 === arr2)
// false
```

To understand why this is the case, you have to understand what **primitive** and **reference** values are in JavaScript.

## Primitive and Reference Values

Think of a primitive value as **one value** (static, fixed) and a reference value as **a group of multiple values** or (dynamic) value.

Primitive values are of the types `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, and `BigInt`. These values are fixed and stored on the **stack**, for example:

```js
let name = "Dillion"
let age = 60
let isRaining = true
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-71.png)

Reference values are of the `object` types which includes objects, arrays and functions. These values  are dynamic (can contain multiple values, properties, and can be modified over time) and are stored on the **heap**, with a reference value in the stack, for example:

```js
let array = [1, 2, 3]
let obj = { name: "Dillion" }
function print() {
  console.log('hello')
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-72.png)

The reference value is an address that points to the location of the data in the memory.

Here's an article where I explained the difference in more detail: [Primitive and Reference Values Simplified](https://deeecode.com/p/primitive-vs-reference-values/)

## Comparing Primitive and Reference Values

When you compare primitive values, you are comparing **static** values, which have a fixed size on the stack:

```js
let name = "Dillion"
let name2 = "Dillion"

console.log(name === name2)
// true
```

Here, we compare `name` and `name2` if they are equal. What happens here is that JavaScript checks for the `name` and `name2` variables in the stack, and then it sees that they have equal values, so it's true--they are equal.

In the case of objects, you are comparing the **references** (the **addresses**) and not the exact values. Here's what I mean.

If you have two arrays like this:

```js
let array = [1, 2, 3]
let array2 = [1, 2, 3]
```

Here's what it would look like on the stack and heap:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-73.png)

As you can see here, for `array`, `[1, 2, 3]` is not stored on the stack. It is stored on the heap, and the memory location of that data is stored on the stack as a reference.

The same thing for `array2`; `[1, 2, 3]` is not stored on the stack. It is stored on the heap, in a different memory location and the reference is stored on the stack.

When you compare both arrays like `array === array2`, you're not exactly comparing `[1, 2, 3] === [1, 2, 3]` but you're actually comparing `refForArray === refForArray2` (ref is short for reference).

As we saw in the heap illustration, `array` and `array2` have different memory locations, which means they have different references, which then means the variable `array` is not equal to the variable `array2`.

The only way `array` and `array2` can be equal, is if you have something like:

```js
let array = [1, 2, 3]
let array2 = array

console.log(array === array2)
// true
```

By assigning `array` to `array2`, you are assigning the reference that `array` holds in the stack, to `array2`:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-74.png)

Therefore, `array` and `array2` now have the same value--the same **reference**.

## How to compare objects

We've seen that in our attempt to compare two object values, we are actually comparing the reference and not the object data. So how do we correctly compare the object data?

There are a couple of ways you can do this but I will share two of them.

### Compare objects using `_.isEqual` from Lodash

You can write a function that does an equality check between two objects, but it could become complicated when you have to compare deeply nested objects which can have different values, including objects.

A faster approach is using the [isEqual method from Lodash](https://lodash.com/docs/4.17.15#isEqual) which is an effective solution that handles deep comparison between two values:

```js
const _ = require('lodash'); 

const array = [1, 2, 3]
const object = { name: "Dillion" }

const array2 = [1, 2, 3]
const object2 = { name: "Dillion" }

console.log(_.isEqual(array, array2))
// true

console.log(_.isEqual(object, object2))
/ true
```

### Compare objects using `JSON.stringify()`

Say you don't want to use Lodash, you can use `JSON.stringify` which recursively stringifies an object or array to a string:

```js
const array = [1, 2, 3]
const object = { name: "Dillion" }

const array2 = [1, 2, 3]
const object2 = { name: "Dillion" }

console.log(
  JSON.stringify(array)
  ===
  JSON.stringify(array2)
)
// true

console.log(
  JSON.stringify(object)
  ===
  JSON.stringify(object2)
)
// true
```

Since the stringified version is a primitive type (static), the data of both values can be compared. But here is a limitation with `JSON.stringify()`.

`JSON.stringify` can return different results if the order or properties in an object are different. For example:

```js
const object = {
  name: "Dillion",
  age: 50
}

const object2 = {
  age: 50,
  name: "Dillion"
}

console.log(
  JSON.stringify(object)
  ===
  JSON.stringify(object2)
)
// false
```

In `object`, we have `name` coming before `age`, but in `object2`, we have `age` coming before `name`. This means their stringified representations would be different and as a result, their data are not equal.

## Wrap up

Primitive and Reference values are fundamental concepts to understand when working with data in JavaScript. And as we have seen in this article, comparing primitive values is easier, but comparing reference values can be trickier because when you think you are comparing the **data**, you may not realize that you are actually comparing the **reference**.

I hope this article answers the question of "Why are two similar objects not equal in JavaScript?". If it does, please give this article a share 🙏🏾



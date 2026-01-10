---
title: Boolean Definition
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-19T06:43:00.000Z'
originalURL: https://freecodecamp.org/news/boolean-definition
coverImage: https://cdn-media-2.freecodecamp.org/w1280/605d74a79618b008528a7978.jpg
tags:
- name: Boolean
  slug: boolean
- name: Tech Terms
  slug: tech-terms
seo_title: null
seo_desc: 'In computer science, a boolean refers to a value that is either true or
  false.

  Boolean gets its name from the English mathematician, George Boole.

  Boole created a new branch of algebra, now known as Boolean Algebra, where the value
  of true is 1 and t...'
---

In computer science, a boolean refers to a value that is either true or false.

Boolean gets its name from the English mathematician, George Boole.

Boole created a new branch of algebra, now known as Boolean Algebra, where the value of true is 1 and the value of false is 0. In Boolean Algebra, there are three main logical operations: **AND**, **OR**, and **NOT**.

Boolean Algebra laid the foundation for the information age and computer science. All computers function using the basic principles of Boolean Algebra, where 1, or true, is on, and 0, or false, is off.

Because of this, many programming languages include boolean data types and operators.

For example, in JavaScript, it's common to see the boolean data types `true` and `false`:

```js
const isCat = true;

```

JavaScript also has logical operators for **AND**:

```js
const isCat = true;
const isCute = true;

if (isCat && isCute) { // isCat AND isCute are both true
  console.log("There's a cute cat :D"); // logs "There's a cute cat :D" to the console
}

```

**OR**:

```js
const isCat = true;
const isFluffy = false;

if (isCat || isFluffy) { // either isCat OR isFluffy are true
  console.log("There's an animal that might be a cat, fluffly, or both"); // logs "There's an animal that might be a cat, fluffly, or both" to the console
}

```

And **NOT**:

```js
const isCat = true;
const isFluffy = false;

if (!isFluffy) { // isFluffy is false, or NOT true
  console.log("Whatever this animal is, it's not fluffy"); // logs "Whatever this animal is, it's not fluffy" to the console
}

```

Also, like many other programming languages, JavaScript has other operators that return a boolean value:

```js
const catName = 'Boomer';

if (catName === 'Boomer') { // evaluates to true
  console.log('BOOMER LIVES!'); // logs 'BOOMER LIVES!' to the console
}

```

## Related Tech Terms:

* [Binary Definition](https://www.freecodecamp.org/news/binary-definition/)
* [Bit Definition](https://www.freecodecamp.org/news/bit-definition/)


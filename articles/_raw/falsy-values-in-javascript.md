---
title: Falsy Values in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-14T00:09:00.000Z'
originalURL: https://freecodecamp.org/news/falsy-values-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb6740569d1a4ca3ea5.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Description

  A falsy value is something which evaluates to FALSE, for instance when checking
  a variable. There are only six falsey values in JavaScript: undefined, null, NaN,
  0, "" (empty string), and false of course.

  Checking for falsy values on vari...'
---

## **Description**

A falsy value is something which evaluates to FALSE, for instance when checking a variable. There are only six falsey values in JavaScript: `undefined`, `null`, `NaN`, `0`, `""` (empty string), and `false` of course.

## **Checking for falsy values on variables**

It is possible to check for a falsy value in a variable with a simple conditional:

```javascript
if (!variable) {
  // When the variable has a falsy value the condition is true.
}
```

## **General Examples**

```javascript
var string = ""; // <-- falsy

var filledString = "some string in here"; // <-- truthy

var zero = 0; // <-- falsy

var numberGreaterThanZero // <-- truthy

var emptyArray = []; // <-- truthy, we'll explore more about this next

var emptyObject = {}; // <-- truthy
```

## **Fun With Arrays**

```javascript
if ([] == false) // <-- truthy, will run code in if-block

if ([]) // <-- truthy, will also run code in if-block

if ([] == true) // <-- falsy, will NOT run code in if-block

if (![]) // <-- falsy, will also NOT run code in if-block
```

## **Caveat**

Be aware of the data type when evaluating a value in a Boolean context. If the data type of the value is meant to be a _number_, the truthy/falsy evalution can result in an unexpected outcome:

```javascript
const match = { teamA: 0, teamB: 1 }
if (match.teamA)
  // The following won't run due to the falsy evaluation
  console.log('Team A: ' + match.teamA);
}
```

An alternative to the use case above is to evaluate the value using `typeof`:

```javascript
const match = { teamA: 0, teamB: 1 }
if (typeof match.teamA === 'number')
  console.log('Team A: ' + match.teamA);
}
```

## **More Information**

* [**truthy**](http://james.padolsey.com/javascript/truthy-falsey/) | Blog Post - Truthy & Falsey
* [Falsy | Glossary | MDN](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
* [Truthy and Falsy: When All is Not Equal in JavaScript](https://www.sitepoint.com/javascript-truthy-falsy/)


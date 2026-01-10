---
title: A Brief Introduction to Array Destructuring in ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-01T01:39:22.000Z'
originalURL: https://freecodecamp.org/news/array-destructuring-in-es6-30e398f21d10
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5TN-55RU-eTfNlcDL2RR1g.png
tags:
- name: arrays
  slug: arrays
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kevwe Ochuko

  Destructuring in JavaScript is a simplified method of extracting multiple properties
  from an array by taking the structure and deconstructing it down into its own constituent
  parts through assignments by using a syntax that looks simi...'
---

By Kevwe Ochuko

**Destructuring** in JavaScript is a simplified method of extracting multiple properties from an array by taking the structure and deconstructing it down into its own constituent parts through assignments by using a syntax that looks similar to array literals.

It creates a pattern that describes the kind of value you are expecting and makes the assignment. Array destructuring uses position.

See the below code snippet.

```js
const [first, second, third] = ["Laide", "Gabriel", "Jets"];

```

_The Syntax with Destructuring._

```js
const first = "Laide",
      second = "Gabriel",
      third = "Jets";

```

_The Syntax Without Destructuring._

> _You cannot use Numbers for destructuring. Numbers will throw an error because numbers cannot be variable names._

```js
const [1, 2, 3] = ["Laide", "Gabriel", "Jets"];

```

_This syntax throws an error._

**Destructuring** has made extracting data from an array very simple and readable. Imagine trying to extract data from a nested array with 5 or 6 levels. That would be very tedious. You use an array literal on the left-hand side of the assignment.

```js
const householdItems = ["Table", "Chair", "Fan"];
const [a, b, c] = householdItems;

```

It takes each variable on the array literal on the left-hand side and maps it to the same element at the same index in the array.

```js
console.log(a); // Output: Table
console.log(b); // Output: Chair
console.log(c); // Output: Fan

```

Declaration and assignment can be done separately in destructuring.

```js
let first, second;
[first, second] = ["Male", "Female"];

```

If the number of variables passed to the destructuring array literals are more than the elements in the array, then the variables which aren’t mapped to any element in the array return `undefined`_._

```js
const householdItems = ["Table", "Chair", "Fan", "Rug"];
const [a, b, c, d, e] = householdItems;

console.log(c); // Output: Fan
console.log(d); // Output: Rug
console.log(e); // Output: undefined

```

If the number of variables passed to the destructuring array literals are lesser than the elements in the array, the elements without variables to be mapped to are just left. There are no errors whatsoever.

```js
const householdItems = ["Table", "Chair", "Fan", "Rug"];
const [a, b, c] = householdItems;
console.log(c); // Output: Fan
```

### **Destructuring Returned Arrays**

Destructuring makes working with a function that returns an array as a value more precise. It works for all iterables.

```js
function runners() {
  return ["Sandra", "Ola", "Chi"];
}

const [a, b, c] = runners();

console.log(a); // Output: Sandra
console.log(b); // Output: Ola
console.log(c); // Output: Chi

```

### **Default Value**

Destructuring allows a default value to be assigned to a variable if no value or `_undefined_` is passed. It is like providing a fallback when nothing is found.

```js
let a, b;
[a = 40, b = 4] = [];
console.log(a); // Output: 40
console.log(b); // Output: 4

[a = 40, b = 4] = [1, 23];
console.log(a); // Output: 1
console.log(b); // Output: 23
```

Default values can also refer to other variables including the one in the same array literal.

```js
const [first = "Cotlin", second = first] = [];
console.log(first); // Output: Cotlin
console.log(second); // Output: Cotlin

```

```js
const [first = "Cotlin", second = first] = ["Koku"];
console.log(first); // Output: Koku
console.log(second); // Output: Koku

```

```js
const [first = "Cotlin", second = first] = ["Koku", "Lydia"];
console.log(first); // Output: Koku
console.log(second); // Output: Lydia

```

### Ignoring Some Values

Destructuring lets you map a variable to the elements you are interested in. You can ignore or skip the other elements in the array by using trailing commas.

```js
let a, b;
[a, , b] = ["Lordy", "Crown", "Roses"];

console.log(a); // Output: Lordy
console.log(b); // Output: Roses

```

### **The Rest Parameter And Spread Syntax**

The new _(…)_ _operator_ that was added in ES6 can be used in destructuring. If the _(…) operator_ appear on the left-hand side in destructuring then it is a [**REST PARAMETER**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)**.** A Rest parameter is used to map all the remaining elements in the array that have not been mapped to the rest variable itself. It is like gathering what is left behind**.** The Rest variable must always be the last otherwise a `SyntaxError` is thrown.

```js
const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
const [first, , third, ...others] = planets;

console.log(first); // Output: Mercury
console.log(third); // Output: Earth
console.log(others); // Output: ["Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

```

If the (…) operator appears on the right-hand in destructuring then it is a [**SPREAD SYNTAX**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)**.** It takes all the other elements in the array which have no variable mapped to them and then maps it to the rest variable.

```js
const otherPlanets = ["Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
const [first, second, ...rest] = ["Mercury", "Venus", ...otherPlanets];

console.log(first); // Output: Mercury
console.log(second); // Output: Venus
console.log(rest); // Output: ["Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
```

When you have more variables on the left-hand side, it maps the single elements in the array equally to the variables.

```js
const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

const [first, second, ...rest] = ["Sun", ...planets];

console.log(first); // Output: Sun
console.log(second); // Output: Mercury
console.log(rest); // Output: ["Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

```

### **Interchanging Or Swapping Variables**

One destructuring expression can be used in swapping the values of two variables.

```js
let a, b;
[a, b] = ["Male", "Female"];
[a, b] = [b, a];

console.log(a); // Output: Female
console.log(b); // Output: Male

```

### **Nested Array Destructuring**

You can also do nested destructuring with arrays. The corresponding item must be an array in order to use a nested destructuring array literal to assign items in it to local variables.

```js
const numbers = [8, [1, 2, 3], 10, 12];
const [a, [d, e, f]] = numbers;

console.log(a); // Output: 8
console.log(d); // Output: 1
console.log(e); // Output: 2

```

### Multiple Array Destructuring

You can destructure an array more than once in the same code snippet.

```js
const places = ["first", "second", "third", "fourth"];
const [a, b, , d] = [f, ...rest] = places;

console.log(a); // Output: first
console.log(d); // Output: fourth
console.log(f); // Output: first
console.log(rest); // Output: ["second", "third", "fourth"]

```

### **Conclusion**

You can copy and paste the code on [Babel’s website](https://babeljs.io/en/repl.html#?babili=false&browsers=&build=&builtIns=false&spec=false&loose=false&code_lz=Q&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=es2015%2Ces2016%2Creact%2Cstage-2&prettier=false&targets=&version=6.26.0&envVersion=) to see what the code would look like if destructuring did not exist. You would have written more lines of code, but destructuring simplifies it all.


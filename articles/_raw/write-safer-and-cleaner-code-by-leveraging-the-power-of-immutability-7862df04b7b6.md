---
title: Write safer and cleaner code by leveraging the power of “Immutability”
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-17T17:51:34.000Z'
originalURL: https://freecodecamp.org/news/write-safer-and-cleaner-code-by-leveraging-the-power-of-immutability-7862df04b7b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eO8-0-GT5ht8CR7TdK9knA.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Guido Schmitz

  Immutability is one of the building blocks of functional programming. It allows
  you to write safer and cleaner code. I’ll show you how you can achieve immutability
  through some JavaScript examples.

  According to Wikipedia (source):


  A...'
---

By Guido Schmitz

Immutability is one of the building blocks of functional programming. It allows you to write safer and cleaner code. I’ll show you how you can achieve immutability through some JavaScript examples.

**According to Wikipedia ([source](https://en.wikipedia.org/wiki/Immutable_object)):**

> An immutable object (unchangeable object) is an object whose state cannot be modified after it is created. This is in contrast to a mutable object (changeable object), which can be modified after it is created. In some cases, an object is considered immutable even if some internally used attributes change but the object’s state appears to be unchanging from an external point of view.

### Immutable Arrays

Arrays are a good starting point to get a grasp of how immutability actually works. Lets take a look.

```
const arrayA = [1, 2, 3];arrayA.push(4); const arrayB = arrayA;arrayB.push(5); console.log(arrayA); // [1, 2, 3, 4, 5]console.log(arrayB); // [1, 2, 3, 4, 5]
```

This example assigns **arrayB** to a reference of **arrayA**, so the push method adds the value 5 into both variables. Our code mutates other values indirectly, which is not what we want to do. This violates the principle of immutability.

We can improve our example to be immutable by using the [slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) function, and the behavior of the code is different.

```
const arrayA = [1, 2, 3];arrayA.push(4); const arrayB = arrayA.slice(0);arrayB.push(5); console.log(arrayA); // [1, 2, 3, 4]console.log(arrayB); // [1, 2, 3, 4, 5]
```

This is exactly what we want. The code doesn’t mutate the other values.

Remember: When using [push](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push) to add a value to an array, you are **mutating** the array. You want to avoid mutating variables because it can cause side effects in your code. The [slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) function returns a copy of the array.

### Functions

Now you know how to avoid mutating other values. How would you write functions to be “pure”? Pure is another word to call a function that doesn’t have any side effects and will not change state.

Let’s look at a function that leverages the same principle from the arrays example. First we create a function that mutates another value, then we improve the function to be “pure”.

```
const add = (arrayInput, value) => {  arrayInput.push(value);   return arrayInput;};
```

```
const array = [1, 2, 3]; console.log(add(array, 4)); // [1, 2, 3, 4]console.log(add(array, 5)); // [1, 2, 3, 4, 5]
```

So again, we are **mutating** our input which creates an unpredictable function. In the functional programming world, there is a golden rule around functions: **a function with the same input should always return the same result**.

The function above violates the golden rule. Every time our **add** function is called, it mutates the **array** variable and the result is different.

Let’s see how we can change the implementation of our **add** function so it’s immutable.

```
const add = (arrayInput, value) => {  const copiedArray = arrayInput.slice(0);  copiedArray.push(value);   return copiedArray;}; const array = [1, 2, 3];
```

```
const resultA = add(array, 4);console.log(resultA); // [1, 2, 3, 4]
```

```
const resultB = add(array, 5);console.log(resultB); // [1, 2, 3, 5]
```

Now we can call our function multiple times, and expect the output to be the same, based on the input. This is because we are no longer mutating the **array** variable. We can call this function a “pure function”.

> **Note:** You can also use **concat**, instead of **slice** and **push**.  
> So: arrayInput.concat(value);

We can use the [spread syntax](https://developer.mozilla.org/nl/docs/Web/JavaScript/Reference/Operators/Spread_operator), available in ES6, to shorten this function.

```
const add = (arrayInput, value) => […arrayInput, value];
```

### Concurrency

NodeJS applications use a concept called concurrency. A concurrent operation means that two computations can both make progress regardless of the other. If there are two threads, the second computation doesn’t need to wait for the completion of the first one in order to advance.

![Image](https://cdn-media-1.freecodecamp.org/images/ajQNacOo6-0-aOa4K4a5wH-1SoCEfKAEftij)
_Visualization of a concurrent operation_

NodeJS makes concurrency possible with the event-loop. The event-loop repeatedly takes an event and fires any event handlers listening to that event one at a time. This model allows a NodeJS application to process a huge amount of requests. If you want to learn more, read [this article about the event-loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick).

What does immutability have to do with concurrency? Since multiple operations can change a value outside of the function’s scope in a concurrent way, this creates unreliable output and causes unexpected results. Be aware of a function that mutates variables outside of its scope, as this can be really dangerous.

### Next steps

Immutability is an important concept to understand on your journey to learn functional programming. You might want to take a look at [ImmutableJS](https://facebook.github.io/immutable-js), written by developers at Facebook. The library provides certain immutable data structures like **Map**, **Set**, and **List**.

[**Immutable.js, persistent data structures and structural sharing**](https://medium.com/@dtinth/immutable-js-persistent-data-structures-and-structural-sharing-6d163fbd73d2)  
[_Why use Immutable.js instead of normal JavaScript object?_medium.com](https://medium.com/@dtinth/immutable-js-persistent-data-structures-and-structural-sharing-6d163fbd73d2)[**Higher Order Functions: Using Filter, Map and Reduce for More Maintainable Code**](https://medium.freecodecamp.org/higher-order-functions-in-javascript-d9101f9cf528)  
[_Higher order functions can help you to step up your JavaScript game by making your code more declarative. That is…_medium.freecodecamp.org](https://medium.freecodecamp.org/higher-order-functions-in-javascript-d9101f9cf528)

_Click the ? below so other people will see this article here on Medium. Thanks for reading._

![Image](https://cdn-media-1.freecodecamp.org/images/0pF5DeetY83EjRZztJ7vbRQek2p9bcgiWnrV)


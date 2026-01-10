---
title: JavaScript forEach() – JS Array For Each Loop Example
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-16T14:52:20.000Z'
originalURL: https://freecodecamp.org/news/javascript-foreach-js-array-for-each-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template.png
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: null
seo_desc: 'When working with arrays, there will be times when you need to loop or
  iterate through the array''s values in order to either output or manipulate them.

  These arrays can hold any datatype, including objects, numbers, strings, and many
  others.

  In this ...'
---

When working with arrays, there will be times when you need to loop or iterate through the array's values in order to either output or manipulate them.

These arrays can hold any datatype, including objects, numbers, strings, and many others.

In this article, we'll look at how you can use the JavaScript `forEach()` array method to loop through all types of arrays, as well as how it differs from the for loop method.

There are many iteration methods in JavaScript, including the `forEach()` method, and they almost all perform the same function with minor differences. It is entirely up to you whether or not to use a specific loop method, but it is important that we understand each of them and how they work.

## JavaScript forEach()

The `forEach()` array method loops through any array, executing a provided function once for each array element in ascending index order. This function is referred to as a callback function.

> **Note:** Arrays are collections of elements that can be of any datatype.

### Syntax and Parameters of a forEach() Loop

Here are the standard ways of writing the forEach Loop:

```js
array.forEach(callbackFunction);
array.forEach(callbackFunction, thisValue);
```

The callback function can accept up to three different arguments, though not all of them are required. Here are some examples of `forEach()` loops that use both the normal function and the ES6 method to declare the callback function:

```js
// Using only Current Element
array.forEach((currentElement) => { /* ... */ })
array.forEach(function(currentElement) { /* ... */ })

// Using only Current Element and Index
array.forEach((currentElement, index) => { /* ... */ })
array.forEach(function(currentElement, index) { /* ... */ })

// Using only Current Element, Index and array
array.forEach((currentElement, index, array) => { /* ... */ })
array.forEach(function(currentElement, index, array){ /* ... */ })

// Using all parameters with thisValue (value of this in the callback) 
array.forEach((currentElement, index, array) => { /* ... */ }, thisValue)
array.forEach(function(currentElement, index, array) { /* ... */ }, thisValue)
```

The syntax above may appear confusing, but it is the general syntax for writing a forEach loop depending on the value you want to use. Let's go over all of the parameters that we used:

* `callbackFunction`: The callback function is a function that is executed only once for each element and can accept the following arguments to be used within the callback function:
    

1. `currentElement`: The current element, as the name implies, is the element in the array that is being processed at the time the loop occurs. It is the only necessary argument.
    
2. `index`: index is an optional argument that carries the index of the `currentElement`.
    
3. `array`: The array is an optional argument that returns the array that was passed to the `forEach()` method.
    

* `thisValue`: This is an optional parameter that specifies the value that will be used in the callback function.
    

In summary, the `forEach()` array iteration method accepts a callback function that holds arguments that can be used within the callback function for each array item, such as the array item, the `index` of the item, and the entire array.

## forEach() Examples in JavaScript

Before we look at other possible examples, let's look at all of the arguments we passed into the callback function and what they could be used for.

### How to use the `currentElement` Argument

Assume we have an array of employee details that includes their names, age, salary amount, and currency:

```js
const staffsDetails = [
  { name: "Jam Josh", age: 44, salary: 4000, currency: "USD" },
  { name: "Justina Kap", age: 34, salary: 3000, currency: "USD" },
  { name: "Chris Colt", age: 37, salary: 3700, currency: "USD" },
  { name: "Jane Doe", age: 24, salary: 4200, currency: "USD" }
];
```

If we want to display all of the names individually with some words around them, we can use the `forEach()` method as follows:

```js
staffsDetails.forEach((staffDetail) => {
  let sentence = `I am ${staffDetail.name} a staff of Royal Suites.`;
  console.log(sentence);
});
```

Output:

```bash
"I am Jam Josh a staff of Royal Suites."
"I am Justina Kap a staff of Royal Suites."
"I am Chris Colt a staff of Royal Suites."
"I am Jane Doe a staff of Royal Suites."
```

**Note:** We could also destructure the `currentElement` value in case it’s an object that contains key/value pairs this way:

```js
staffsDetails.forEach(({ name }, index) => {
  let sentence = `I am ${name} a staff of Royal Suites.`;
  console.log(sentence);
});
```

### How to use the `index` Argument

We could also get the `index` of each array item by just making use of the unbuilt index argument this way:

```js
staffsDetails.forEach((staffDetail, index) => {
  let sentence = `index ${index} : I am ${staffDetail.name} a staff of Royal Suites.`;
  console.log(sentence);
});
```

Output:

```bash
"index 0 : I am Jam Josh a staff of Royal Suites."
"index 1 : I am Justina Kap a staff of Royal Suites."
"index 2 : I am Chris Colt a staff of Royal Suites."
"index 3 : I am Jane Doe a staff of Royal Suites."
```

### How to use the `array` Argument

The `array` argument is the third argument which holds the original array that is being iterated over. For example, we could try displaying the value in our console this way:

```js
staffsDetails.forEach((staffDetail, index, array) => {
  console.log(array);
});
```

This would output the entire array 4 times since we have 4 items and the iteration runs 4 times. Let’s do it for an array with a few values so I can add the output here:

```js
let scores = [12, 55, 70];

scores.forEach((score, index, array) => {
  console.log(array);
});
```

Output:

```bash
[12,55,70]
[12,55,70]
[12,55,70]
```

So far, we've used every argument of the callback function. Let's look at some other examples to fully understand how it works before doing a quick comparison with the for loop method.

### How to Add All Values in An Array of Numbers with `forEach()`

Suppose we have an array of `scores`. We could use the `forEach()` array method to loop through and help add up these numbers:

```js
const scores = [12, 55, 70, 47];

let total = 0;
scores.forEach((score) => {
  total += score;
});

console.log(total);
```

Recall that earlier on, we were making use of an array of staff details. Now let’s try adding all the staff member's salaries together to see how it works with objects:

```bash
let totalSalary = 0;
staffsDetails.forEach(({salary}) => {
  totalSalary += salary;
});

console.log(totalSalary + " USD"); // "14900 USD"
```

**Note:** We destructed the `currentElement`’s Object.

### How to Use Conditionals in a `forEach()` Callback Function

When looping through arrays, we may want to check for specific conditions, as is commonly done with the for loop method. We can pass these conditions into our callback function or any other operation we want to run on each array item.

For example, if we only want to show the names of people whose salaries are greater than or equal to `4000` from the array of staff details we declared earlier, we can do the following:

```js
staffsDetails.forEach(({name, salary}) => {
  if(salary >= 4000){
    console.log(name);
  }
});
```

Output:

```bash
"Jam Josh"
"Jane Doe"
```

## Comparing forEach() with a for Loop

The for loop is very similar to the forEach method, but each possess some features that are unique to them such as:

### Break out and continue in a Loop

When looping through an array, we may want to either break out or continue the loop when a certain condition is met (meaning we skip). This is possible with the `break` and `continue` instruction, but it does not work with the `forEach()` method, as shown below:

```js
const scores = [12, 55, 70, 47];

scores.forEach((score) => {
  console.log(score);

  if (score === 70) 
    break;
});
```

This will throw a syntax error of `Illegal break statement`. This applies also to the continue instruction which would also throw an `Illegal continue statement: no surrounding iteration statement`.

```js
const scores = [12, 55, 70, 47];

scores.forEach((score) => {
  if (score === 70) 
    continue;
  
  console.log(score);
});
```

But fortunately this works with the for loop method perfectly:

```js
const scores = [12, 55, 70, 47];

for (i = 0; i < scores.length; i++) {
  console.log(scores[i]);

  if (scores[i] === 70) 
    break;
}
```

Output:

```bash
12
55
70
```

And the same with the `continue` instruction:

```js
const scores = [12, 55, 70, 47];

for (i = 0; i < scores.length; i++) {
  if (scores[i] === 70) 
    continue;
  
  console.log(scores[i]);
}
```

Output:

```bash
12
55
47
```

### Array with Missing elements

Another important comparison to make is in a situation whereby the array we are iterating over has some missing values/array items as seen below:

```js
const studentsScores = [70, , 12, 55, , 70, 47];
```

This could be due to a developer error or something else, but these two methods take two different approaches to looping through these types of arrays. The for loop returns undefined where there are missing values, whereas the `forEach()` method skips them.

**For Loop**

```js
const studentsScores = [70, , 12, 55, , 70, 47];

for (i = 0; i < studentsScores.length; i++) {
  console.log(studentsScores[i]);
}
```

Output:

```bash
70
undefined
12
55
undefined
70
47
```

**forEach()**

```js
const studentsScores = [70, , 12, 55, , 70, 47];

studentsScores.forEach((stundentScore) => {
  console.log(stundentScore);
});
```

Output:

```bash
70
12
55
70
47
```

**Note:** Async/Await does not work with the `forEach()` array method but works with the for loop method.

## Conclusion

In this article, we learned how to use the `forEach()` array method, which allows us to loop through an array of any type of item. It also allows us to write cleaner, more readable code than the for loop.

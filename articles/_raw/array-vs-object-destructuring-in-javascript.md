---
title: Array vs Object Destructuring in JavaScript – What’s the Difference?
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2021-11-10T16:24:16.000Z'
originalURL: https://freecodecamp.org/news/array-vs-object-destructuring-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/extract-777603_1920-Image-by-Oscar-Castillo-from-Pixabay.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'The destructuring assignment in JavaScript provides a neat and DRY way
  to extract values from your arrays and objects.

  This article aims to show you exactly how array and object destructuring assignments
  work in JavaScript.

  So, without any further ad...'
---

The destructuring assignment in JavaScript provides a neat and DRY way to extract values from your arrays and objects.

This article aims to show you exactly how array and object destructuring assignments work in JavaScript.

So, without any further ado, let’s get started with array destructuring.

## What Is Array Destructuring?

**Array destructuring** is a unique technique that allows you to neatly extract an array’s value into new variables.

For instance, without using the array destructuring assignment technique, you would copy an array’s value into a new variable like so:

```js
const profile = ["Oluwatobi", "Sofela", "codesweetly.com"];

const firstName = profile[0];
const lastName = profile[1];
const website = profile[2];

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-mrqjsu?file=script.js)

Notice that the snippet above has a lot of repeated code which is not a DRY (**D**on’t **R**epeat **Y**ourself) way of coding.

Let’s now see how array destructuring makes things neater and DRYer.

```js
const profile = ["Oluwatobi", "Sofela", "codesweetly.com"];

const [firstName, lastName, website] = profile;

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-uxrjek?file=script.js)

You see, like magic, we’ve cleaned up our code by placing the three new variables (that is, `firstName`, `lastName`, and `website`) into an array object (`[...]`). Then, we assigned them the `profile` array's values.

In other words, we instructed the computer to extract the `profile` array’s values into the variables on the left-hand side of the [assignment operator](https://www.codesweetly.com/javascript-expression#types-of-expressions-in-javascript).

Therefore, JavaScript will parse the `profile` array and copy its first value (`"Oluwatobi"`) into the destructuring array’s first variable (`firstName`).

Likewise, the computer will extract the `profile` array’s second value (`"Sofela"`) into the destructuring array’s second variable (`lastName`).

Lastly, JavaScript will copy the `profile` array’s third value (`"codesweetly.com"`) into the destructuring array’s third variable (`website`).

Notice that the snippet above destructured the `profile` array by referencing it. However, you can also do direct destructuring of an array. Let’s see how.

### How to Do Direct Array Destructuring

JavaScript lets you destructure an array directly like so:

```js
const [firstName, lastName, website] = [
  "Oluwatobi", 
  "Sofela", 
  "codesweetly.com"
];

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-rndtx5?file=script.js)

Suppose you prefer to separate your variable declarations from their assignments. In that case, JavaScript has you covered. Let’s see how.

### How to Use Array Destructuring While Separating Variable Declarations from Their Assignments

Whenever you use array destructuring, JavaScript allows you to separate your variable declarations from their assignments.

**Here’s an example:**

```js
let firstName, lastName, website;

[firstName, lastName, website] = ["Oluwatobi", "Sofela", "codesweetly.com"];

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-nm1ng3?file=script.js)

What if you want `"Oluwatobi"` assigned to the `firstName` variable—and the rest of the array items to another variable? How you do that? Let’s find out below.

### How to Use Array Destructuring to Assign the Rest of an Array Literal to a Variable

JavaScript allows you to use the [rest operator](https://www.codesweetly.com/javascript-rest-operator) within a destructuring array to assign the rest of a regular array to a variable.

**Here’s an example:**

```js
const [firstName, ...otherInfo] = ["Oluwatobi", "Sofela", "codesweetly.com"];

console.log(firstName); // "Oluwatobi"
console.log(otherInfo); // ["Sofela", "codesweetly.com"]
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-w15axc?file=script.js)

**Note:** Always use the rest operator as the last item of your destructuring array to avoid getting a `SyntaxError`.

Now, what if you only want to extract `"codesweetly.com"`? Let's discuss the technique you can use below.

### How to Use Array Destructuring to Extract Values at Any Index

Here’s how you can use array destructuring to extract values at any index position of a regular array:

```js
const [, , website] = ["Oluwatobi", "Sofela", "codesweetly.com"];

console.log(website); // "codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-311nkt?file=script.js)

In the snippet above, we used commas to skip variables at the destructuring array's first and second index positions.

By so doing, we were able to link the `website` variable to the third index value of the regular array on the right side of the assignment operator (that is, `"codesweetly.com"`).

At times, however, the value you wish to extract from an array is `undefined`. In that case, JavaScript provides a way to set default values in the destructuring array. Let’s learn more about this below.

### How Default Values Work in an Array Destructuring Assignment

Setting a default value can be handy when the value you wish to extract from an array does not exist (or is set to `undefined`).

Here’s how you can set one inside a destructuring array:

```js
const [firstName = "Tobi", website = "CodeSweetly"] = ["Oluwatobi"];

console.log(firstName); // "Oluwatobi"
console.log(website); // "CodeSweetly"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-r38k67?file=script.js)

In the snippet above, we set `"Tobi"` and `"CodeSweetly"` as the default values of the `firstName` and `website` variables.

Therefore, in our attempt to extract the first index value from the right-hand side array, the computer defaulted to `"CodeSweetly"`—because only a zeroth index value exists in `["Oluwatobi"]`.

So, what if you need to swap `firstName`’s value with that of `website`? Again, you can use array destructuring to get the job done. Let’s see how.

### How to Use Array Destructuring to Swap Variables’ Values

You can use the array destructuring assignment to swap the values of two or more different variables.

**Here's an example:**

```js
let firstName = "Oluwatobi";
let website = "CodeSweetly";

[firstName, website] = [website, firstName];

console.log(firstName); // "CodeSweetly"
console.log(website); // "Oluwatobi"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-fu7phn?file=script.js)

In the snippet above, we used direct array destructuring to reassign the `firstName` and `website` variables with the values of the array literal on the right-hand side of the assignment operator.

As such, `firstName`’s value will change from `"Oluwatobi"` to `"CodeSweetly"`. While `website`’s content will change from `"CodeSweetly"` to `"Oluwatobi"`.

Keep in mind that you can also use array destructuring to extract values from a regular array to a function’s parameters. Let’s talk more about this below.

### How to Use Array Destructuring to Extract Values from an Array to a Function’s Parameters

Here’s how you can use array destructuring to extract an array’s value to a function’s parameter:

```js
// Define an array with two items:
const profile = ["Oluwatobi", "Sofela"];

// Define a function with one destructuring array containing two parameters:
function getUserBio([firstName, lastName]) {
  return `My name is ${firstName} ${lastName}.`;
}

// Invoke getUserBio while passing the profile array as an argument:
getUserBio(profile);

// The invocation above will return:
"My name is Oluwatobi Sofela."
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-ckdkjb?file=script.js)

In the snippet above, we used an array destructuring parameter to extract the `profile` array’s values into the `getUserBio`’s `firstName` and `lastName` parameters.

**Note:** An array destructuring parameter is typically called a _destructuring parameter_.

**Here’s another example:**

```js
// Define an array with two string values and one nested array:
const profile = ["codesweetly.com", "Male", ["Oluwatobi", "Sofela"]];

// Define a function with two destructuring arrays containing a parameter each:
function getUserBio([website, , [userName]]) {
  return `${userName} runs ${website}`;
}

// Invoke getUserBio while passing the profile array as an argument:
getUserBio(profile);

// The invocation above will return:
"Oluwatobi runs codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-gvzqak?file=script.js)

In the snippet above, we used two array destructuring parameters to extract the `profile` array’s values into the `getUserBio`’s `website` and `userName` parameters.

There are times you may need to invoke a function containing a destructuring parameter without passing any argument to it. In that case, you will need to use a technique that prevents the browser from throwing a `TypeError`.

Let’s learn about the technique below.

### How to Invoke a Function Containing Array Destructuring Parameters Without Supplying Any Argument

Consider the function below:

```js
function getUserBio([firstName]) {
  console.log(
    "Do something else that does not need the destructuring parameter."
  );
  return `My name is ${firstName}.`;
}
```

Now, let’s invoke the `getUserBio` function without passing any argument to its destructuring parameter:

```js
getUserBio();
```

[**Try it on CodeSandBox**](https://codesandbox.io/s/wrong-way-to-invoke-a-function-containing-an-array-destructuring-parameter-vtdrl)

After invoking the `getUserBio` function above, the browser will throw an error similar to `TypeError: undefined is not iterable`.

The `TypeError` message happens because functions containing a destructuring parameter expect you to supply at least one argument.

So, you can avoid such error messages by assigning a default argument to the destructuring parameter.

**Here’s an example:**

```js
function getUserBio([firstName] = []) {
  console.log(
    "Do something else that does not need the destructuring parameter."
  );
  return `My name is ${firstName}.`;
}
```

Notice in the snippet above that we assigned an empty array as the destructuring parameter’s default argument.

So, let’s now invoke the `getUserBio` function without passing any argument to its destructuring parameter:

```js
getUserBio();
```

The function will output:

```js
"Do something else that does not need the destructuring parameter."
"My name is undefined."
```

[**Try it on CodeSandBox**](https://codesandbox.io/s/the-correct-way-to-invoke-a-function-containing-an-array-destructuring-parameter-voo50?file=/src/index.js)

Keep in mind that you do not have to use an empty array as the destructuring parameter’s default argument. You can use any other value that is not `null` or `undefined`.

So, now that we know how array destructuring works, let's discuss object destructuring so we can see the differences.

## What Is Object Destructuring in JavaScript?

**Object destructuring** is a unique technique that allows you to neatly extract an object’s value into new variables.

For instance, without using the object destructuring assignment technique, we would extract an object’s value into a new variable like so:

```js
const profile = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
};

const firstName = profile.firstName;
const lastName = profile.lastName;
const website = profile.website;

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-3tyjgy?file=script.js)

Notice that the snippet above has a lot of repeated code which is not a DRY (**D**on’t **R**epeat **Y**ourself) way of coding.

Let’s now see how the object destructuring assignment makes things neater and DRY.

```js
const profile = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
};

const { firstName: firstName, lastName: lastName, website: website } = profile;

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-begth4?file=script.js)

You see, like magic, we’ve cleaned up our code by placing the three new variables into a properties object (`{...}`) and assigning them the `profile` object’s values.

In other words, we instructed the computer to extract the `profile` object’s values into the variables on the left-hand side of the [assignment operator](https://www.codesweetly.com/javascript-expression#types-of-expressions-in-javascript).

Therefore, JavaScript will parse the `profile` object and copy its first value (`"Oluwatobi"`) into the destructuring object’s first variable (`firstName`).

Likewise, the computer will extract the `profile` object’s second value (`"Sofela"`) into the destructuring object’s second variable (`lastName`).

Lastly, JavaScript will copy the `profile` object’s third value (`"codesweetly.com"`) into the destructuring object’s third variable (`website`).

Keep in mind that in `{ firstName: firstName, lastName: lastName, website: website }`, the keys are references to the `profile` object’s properties – while the keys’ values represent the new variables.

![Anatomy of a JavaScript object destructuring assignment](https://www.freecodecamp.org/news/content/images/2021/11/destructuring-object-anatomy-codesweetly.png)
_The anatomy of a JavaScript object destructuring assignment_

Alternatively, you can use shorthand syntax to make your code easier to read.

**Here’s an example:**

```js
const profile = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
};

const { firstName, lastName, website } = profile;

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-4nhtlt?file=script.js)

In the snippet above, we shortened `{ firstName: firstName, age: age, gender: gender }` to `{ firstName, age, gender }`. You can learn more about the shorthand technique [here](https://alligator.io/js/object-property-shorthand-es6/).

Observe that the snippets above illustrated how to assign an object’s value to a variable when both the object’s property and the variable have the same name.

However, you can also assign a property’s value to a variable of a different name. Let’s see how.

### How to Use Object Destructuring When the Property’s Name Differs from That of the Variable

JavaScript permits you to use object destructuring to extract a property’s value into a variable even if both the property and the variable’s names are different.

**Here’s an example:**

```js
const profile = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
};

const { firstName: forename, lastName: surname, website: onlineSite } = profile;

console.log(forename); // "Oluwatobi"
console.log(surname); // "Sofela"
console.log(onlineSite); // "codesweetly.com"
console.log(website); // "ReferenceError: website is not defined"
```

**[Try it on CodeSandBox](https://codesandbox.io/s/how-to-use-object-destructuring-when-the-propertys-name-differs-from-that-of-the-variable-ppohh?file=/src/index.js)**

In the snippet above, the computer successfully extracted the `profile` object’s values into the variables named `forename`, `surname`, and `onlineSite`—even though the properties and variables are of different names.

**Note:** `const { firstName: forename } = profile` is equivalent to `const forename = profile.firstName`.

**Here’s another example:**

```js
const profile = {
  lastName: { familyName: "Sofela" }
};

const { lastName: { familyName: surname } } = profile;

console.log(surname); // "Sofela"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-nbnqcl?file=script.js)

In the snippet above, the computer successfully extracted the `profile` object’s value into the `surname` variable—even though the property and variable are of different names.

**Note:** `const { lastName: { familyName: surname } } = profile` is equivalent to `const surname = profile.lastName.familyName`.

Notice that so far, we’ve destructured the `profile` object by referencing it. However, you can also do direct destructuring of an object. Let’s see how.

### How to Do Direct Object Destructuring

JavaScript permits direct destructuring of a properties object like so:

```js
const { firstName, lastName, website } = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
};

console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-vspaeg?file=script.js)

Suppose you prefer to separate your variable declarations from their assignments. In that case, JavaScript has you covered. Let see how.

### How to Use Object Destructuring While Separating Variable Declarations from Their Assignments

Whenever you use object destructuring, JavaScript allows you to separate your variable declarations from their assignments.

**Here’s an example:**

```js
// Declare three variables:
let firstName, lastName, website;

// Extract values to the three variables above:
({ firstName, lastName, website } = {
  firstName: "Oluwatobi", 
  lastName: "Sofela", 
  website: "codesweetly.com"
});

// Invoke the three variables:
console.log(firstName); // "Oluwatobi"
console.log(lastName); // "Sofela"
console.log(website); // "codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-3fmanq?file=script.js)

**Note:**

* Make sure that you encase the object destructuring assignment in parentheses. By so doing, the computer will know that the object destructuring is an object literal, not a block.
* Place a semicolon (`;`) after the parentheses of an object destructuring assignment. By doing so, you will prevent the computer from interpreting the parentheses as an invocator of a function that may be on the previous line.

What if you want `"Oluwatobi"` assigned to the `firstName` variable—and the rest of the object’s values to another variable? How can you do this? Let’s find out below.

### How to Use Object Destructuring to Assign the Rest of an Object to a Variable

JavaScript allows you to use the [rest operator](https://www.codesweetly.com/javascript-rest-operator/) within a destructuring object to assign the rest of an object literal to a variable.

**Here’s an example:**

```js
const { firstName, ...otherInfo } = {
  firstName: "Oluwatobi",
  lastName: "Sofela",
  website: "codesweetly.com"
};

console.log(firstName); // "Oluwatobi"
console.log(otherInfo); // {lastName: "Sofela", website: "codesweetly.com"}
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-hksus5?file=script.js)

**Note:** Always use the rest operator as the last item of your destructuring object to avoid getting a `SyntaxError`.

At times, the value you wish to extract from a properties object is `undefined`. In that case, JavaScript provides a way to set default values in the destructuring object. Let’s learn more about this below.

### How Default Values Work in an Object Destructuring Assignment

Setting a default value can be handy when the value you wish to extract from an object does not exist (or is set to `undefined`).

Here’s how you can set one inside a destructuring properties object:

```js
const { firstName = "Tobi", website = "CodeSweetly" } = {
  firstName: "Oluwatobi"
};

console.log(firstName); // "Oluwatobi"
console.log(website); // "CodeSweetly"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-pnjh9a?file=script.js)

In the snippet above, we set `"Tobi"` and `"CodeSweetly"` as the default values of the `firstName` and `website` variables.

Therefore, in our attempt to extract the second property’s value from the right-hand side object, the computer defaulted to `"CodeSweetly"`—because only a single property exists in `{firstName: "Oluwatobi"}`.

So, what if you need to swap `firstName`’s value with that of `website`? Again, you can use object destructuring to get the job done. Let’s see how below.

### How to Use Object Destructuring to Swap Values

You can use the object destructuring assignment to swap the values of two or more different variables.

**Here’s an example:**

```js
let firstName = "Oluwatobi";
let website = "CodeSweetly";

({ firstName, website } = {firstName: website, website: firstName});

console.log(firstName); // "CodeSweetly"
console.log(website); // "Oluwatobi"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-fmyerw?file=script.js)

The snippet above used direct object destructuring to reassign the `firstName` and `website` variables with the values of the object literal on the right-hand side of the assignment operator.

As such, `firstName`’s value will change from `"Oluwatobi"` to `"CodeSweetly"`. While `website`’s content will change from `"CodeSweetly"` to `"Oluwatobi"`.

Keep in mind that you can also use object destructuring to extract values from properties to a function’s parameters. Let’s talk more about this below.

### How to Use Object Destructuring to Extract Values from Properties to a Function’s Parameters

Here’s how you can use object destructuring to copy a property’s value to a function’s parameter:

```js
// Define an object with two properties:
const profile = {
  firstName: "Oluwatobi",
  lastName: "Sofela",
};

// Define a function with one destructuring object containing two parameters:
function getUserBio({ firstName, lastName }) {
  return `My name is ${firstName} ${lastName}.`;
}

// Invoke getUserBio while passing the profile object as an argument:
getUserBio(profile);

// The invocation above will return:
"My name is Oluwatobi Sofela."
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-aucght?file=script.js)

In the snippet above, we used an object destructuring parameter to copy the `profile` object’s values into `getUserBio`’s `firstName` and `lastName` parameters.

**Note:** An object destructuring parameter is typically called a _destructuring parameter_.

**Here’s another example:**

```js
// Define an object with three-parent properties:
const profile = {
  website: "codesweetly.com",
  gender: "Male",
  fullName: {
    firstName: "Oluwatobi",
    lastName: "Sofela"
  }
};

// Define a function with two destructuring objects containing a parameter each:
function getUserBio({ website, fullName: { firstName: userName } }) {
  return `${userName} runs ${website}`;
}

// Invoke getUserBio while passing the profile object as an argument:
getUserBio(profile);

// The invocation above will return:
"Oluwatobi runs codesweetly.com"
```

[**Try it on StackBlitz**](https://stackblitz.com/edit/web-platform-g2n2a6?file=script.js)

In the snippet above, we used two destructuring parameters to copy the `profile` object’s values into `getUserBio`’s `website` and `userName` parameters.

**Note:** If you are unclear about the destructuring parameter above, you may grasp it better by reviewing [this section](#heading-how-to-use-object-destructuring-when-the-propertys-name-differs-from-that-of-the-variable).

There are times you may need to invoke a function containing a destructuring parameter without passing any argument to it. In that case, you will need to use a technique that prevents the browser from throwing a `TypeError`.

Let’s learn about the technique below.

### How to Invoke a Function Containing Destructured Parameters Without Supplying Any Argument

Consider the function below:

```js
function getUserBio({ firstName }) {
  console.log(
    "Do something else that does not need the destructuring parameter."
  );
  return `My name is ${firstName}.`;
}
```

Now, let’s invoke the `getUserBio` function without passing any argument to its destructuring parameter:

```js
getUserBio();
```

[**Try it on CodeSandBox**](https://codesandbox.io/s/wrong-way-to-invoke-a-function-containing-an-object-destructuring-parameter-c1hdx?file=/src/index.js)

After invoking the `getUserBio` function above, the browser will throw an error similar to `TypeError: (destructured parameter) is undefined`.

The `TypeError` message happens because functions containing a destructuring parameter expect you to supply at least one argument.

So, you can avoid such error messages by assigning a default argument to the destructuring parameter.

**Here’s an example:**

```js
function getUserBio({ firstName } = {}) {
  console.log(
    "Do something else that does not need the destructuring parameter."
  );
  return `My name is ${firstName}.`;
}
```

Notice that in the snippet above, we assigned an empty object as the destructuring parameter’s default argument.

So, let’s now invoke the `getUserBio` function without passing any argument to its destructuring parameter:

```js
getUserBio();
```

The function will output:

```js
"Do something else that does not need the destructuring parameter."
"My name is undefined."
```

**[Try it on CodeSandBox](https://codesandbox.io/s/the-correct-way-to-invoke-a-function-containing-an-object-destructuring-parameter-7kvum?file=/src/index.js)**

Keep in mind that you do not have to use an empty object as the destructuring parameter’s default argument. You can use any other value that is not `null` or `undefined`.

## Wrapping It Up

Array and object destructuring work similarly. The main difference between the two destructuring assignments is this:

* Array destructuring extracts values from an array. But object destructuring extracts values from a JavaScript object.

## Overview

This article discussed how array and object destructuring works in JavaScript. We also looked at the main difference between the two destructuring assignments.

Thanks for reading!

### And here's a useful ReactJS resource:

I wrote a book about React! 

* It's beginner’s friendly ✔
* It has live code snippets ✔
* It contains scalable projects ✔
* It has plenty of easy-to-grasp examples ✔

The [React Explained Clearly](https://amzn.to/30iVPIG) book is all you need to understand ReactJS.

[Click Here to Get Your Copy](https://amzn.to/30iVPIG)

[![React Explained Clearly Book Now Available at Amazon](https://www.freecodecamp.org/news/content/images/2021/11/Twitter-React_Explained_Clearly-CodeSweetly-Oluwatobi_Sofela-1.jpg)](https://amzn.to/30iVPIG)



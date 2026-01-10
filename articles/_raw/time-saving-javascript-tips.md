---
title: 5 JavaScript Tips That'll Help You Save Time
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2020-11-19T16:54:42.000Z'
originalURL: https://freecodecamp.org/news/time-saving-javascript-tips
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/time-saving-javascript-tips.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: tips
  slug: tips
seo_title: null
seo_desc: 'I''ve always wanted to create videos around my programming hobby. But I''m
  not a native English speaker, and I was scared to try.

  But a few weeks ago, while I was preparing some JavaScript tips to start my YouTube
  journey, I wrote this list of time-sav...'
---

I've always wanted to create videos around my programming hobby. But I'm not a native English speaker, and I was scared to try.

But a few weeks ago, while I was preparing some JavaScript tips to start my YouTube journey, I wrote this list of time-saving tips. I hope they help you as they've helped me.

In this article, I'm going to share with you 5 useful JavaScript tips (are you ready to dive in? 😀).

And now, guess what? Some of these tips are on [my YouTube channel](https://www.youtube.com/channel/UCSRuzHhjUaAnBb6_rmlr10g)📹! (here is [the playlist](https://www.youtube.com/playlist?list=PL-P9AMQZdy2aj3uLhjHagEsfTOrVqF7AR). 


## Object Destructuring

Destructuring is a feature that was introduced in ES6. It's one of the features you will use daily once you know how.

It helps you deal with three main issues:

- **Repetition.** Every time you want to extract one object property and create a new variable, you create a new line.

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

// Wow... should we display
// John's password like that?

const firstName = user.firstName;
const lastName = user.lastName;
const password = user.password;
```

- **Accessibility.** Each time you want to access an object property, you should write the path to it. (**example:** `user.firstName`, `user.family.sister`, and so on).
- **Usage.** As an example, when you create a new function, and you are only working with one property of an object.

Now that you've seen what these three issues with objects are, how do you think you can solve them?

### How to Solve the Repetition Issue

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

const { firstName, lastName, password } = user;

console.log(firstName, lastName, password);
// Output: 'John', 'Doe', '123'
```

Destructuring is the process of extracting a property from an object by its key. By taking an existing key in your object, then placing it between two brackets (`{ firstName }`) you tell JavaScript:

"Hey JavaScript, I want to create a variable with the same name as my property. I want to create a variable `firstName` for the `firstName` property of my object."

> **Note:** If you want to destructure an object, you should always use an existing key. Otherwise, it will not work.

### How to Solve the Accessibility Issue

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
  family: {
    sister: {
      firstName: "Maria",
    },
  },
};

// We access to the nested object `sister`
// and we extract the `firstName` property
const { firstName } = user.family.sister;

console.log(firstName);
// Output: 'Maria'
```

When you work with nested objects, it can become quite repetitive and wastes a lot of time accessing the same property many times.

Using destructuring, in one line only, you can reduce the property path to one variable.

### How to Solve the Usage Issue

Now that you know how to destructure an object, let me show you how to extract properties directly in your function parameter definition.

If you know React, you're probably already familiar with it.

```javascript
function getUserFirstName({ firstName }) {
  return firstName;
}

const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

console.log(getUserFirstName(user));
// Output: 'John'
```

In the above example, we have a `getUserFirstName` function, and we know that it will only use one property of our object, `firstName`.

Rather than passing the whole object or creating a new variable, we can destructure the object's function parameters.

## How to Merge Objects in ES6

In programming, you often have to tackle issues with data structures. Thanks to [the spread operator](https://herewecode.io/blog/spread-operator-in-javascript/) introduced in ES6, object and array manipulations are more straightforward.

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

const userJob = {
  jobName: "Developer",
  jobCountry: "France",
  jobTimePerWeekInHour: "35",
};
```

Let's imagine that we have two objects:

- **User.** An object defining general information about the user.
- **UserJob.** An object defining job information of the user.

We want to create one object that only contains the properties of these two objects.

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

const userJob = {
  jobName: "Developer",
  jobCountry: "France",
  jobTimePerWeekInHour: "35",
};

const myNewUserObject = {
  ...user,
  ...userJob,
};

console.log(myNewUserObject);
// Output:
//{
//  firstName: 'John',
//  lastName: 'Doe',
//  password: '123',
//  jobName: 'Developer',
//  jobCountry: 'France',
//  jobTimePerWeekInHour: '35'
//}
```

Using the spread operator (`...`), we can extract all the properties of one object to another.

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

const myNewUserObject = {
  ...user,
  // We extract:
  // - firstName
  // - lastName
  // - password
  // and send them to
  // a new object `{}`
};
```

### How to Merge Arrays

```javascript
const girlNames = ["Jessica", "Emma", "Amandine"];
const boyNames = ["John", "Terry", "Alexandre"];

const namesWithSpreadSyntax = [...girlNames, ...boyNames];

console.log(namesWithSpreadSyntax);
// Output: ['Jessica', 'Emma', 'Amandine', 'John', 'Terry', 'Alexandre']
```

Like objects, the spread operator (`...`) extracts all the elements from one array to another.

```javascript
const girlNames = ["Jessica", "Emma", "Amandine"];

const newNewArray = [
  ...girlNames,
  // We extract:
  // - 'Jessica'
  // - 'Emma'
  // - 'Amandine'
  // and send them to
  // a new array `[]`
];
```

### How to Remove Array Duplicates

Because arrays are lists, you can have many items of the same value. If you want to remove duplicates in your array, you can follow one of the examples below.

One of them will be only one line thanks to ES6, but I let the "old" example  in there so you can compare.

#### How to remove array duplicates "the old way"

```javascript
const animals = ["owl", "frog", "canary", "duck", "duck", "goose", "owl"];

const uniqueAnimalsWithFilter = animals.filter(
  // Parameters example: 'owl', 0, ['owl', 'frog', 'canary', 'duck', 'duck', 'goose', 'owl']
  (animal, index, array) => array.indexOf(animal) == index
);

console.log(uniqueAnimalsWithSet);
// Output: ['owl', 'frog', 'canary', 'duck', 'goose']
```

In the above example, we want to clean the `animals` array by removing all duplicates.

We can do that by using the function `filter` with `indexOf` inside it.

The `filter` function takes all elements of the `animals` array (`animals.filter`). Then for each occurrence it provides:

- the current value (**example:** `duck`)
- the index (**example:** 0)
- the initial array (**example:** the `animals` array => `['owl', 'frog', 'canary', 'duck', 'duck', 'goose', 'owl']`)

We will apply `indexOf` on the original array for each occurrence and give as a parameter the `animal` variable (the current value).

`indexOf` will return the first index of the current value (**example:** for 'owl' the index is 0).

Then inside of the filter, we compare the value of `indexOf` to the current index. If it's the same, we return `true` otherwise `false`.

`filter` will create a new array with only the elements where the returned value was `true`.

So, in our case: `['owl', 'frog', 'canary', 'duck', 'goose']`.


### How to remove array duplicates "the new way"

Well, the "old way" is interesting to understand, but it's long and a bit hard. So let's check out the new way now: 

```javascript
const animals = ["owl", "frog", "canary", "duck", "duck", "goose", "owl"];

const uniqueAnimalsWithSet = [...new Set(animals)];

console.log(uniqueAnimalsWithSet);
// Output: ['owl', 'frog', 'canary', 'duck', 'goose']
```

Let's separate out the different steps:

```javascript
// 1
const animals = ["owl", "frog", "canary", "duck", "duck", "goose", "owl"];

// 2
const animalsSet = new Set(animals);

console.log(animalsSet);
// Output: Set { 'owl', 'frog', 'canary', 'duck', 'goose' }

// 3
const uniqueAnimalsWithSet = [...animalsSet];

console.log(uniqueAnimalsWithSet);
// Output: ['owl', 'frog', 'canary', 'duck', 'goose']
```

We have an `animals` array, and we convert it into a `Set`, which is a special type of object in ES6.

The thing that's different about it is that it lets you create a collection of unique values.

> **Note:** `Set` is a collection of unique values, but it's not an `Array`.

Once we have our `Set` object with unique values, we need to convert it back to an array.

To do that, we use the spread operators to destructure it and send all the properties to a new `Array`.

Because the `Set` object has unique properties, our new array will also have unique values only.

## How to Use Ternary Operators

Have you already heard about a way to write small conditions in only one line?

If not, it's time to remove a lot of your `if` and `else` blocks and convert them to small ternary operations.

Let's look at an example with `console.log` to start. The idea is to check the value of a variable and conditionally display an output.

```javascript
const colour = "blue";

if (colour === "blue") {
  console.log(`It's blue!`);
} else {
  console.log(`It's not blue!`);
}
```

This example is a typical case where you can use [the ternary operator](https://herewecode.io/blog/ternary-operator-in-javascript/) to reduce these 5 `if` and `else` lines to only one!

**One line to rule them all!**

```javascript
const colour = "blue";

colour === "blue" ? console.log(`It's blue!`) : console.log(`It's not blue!`);
// [condition] ? [if] : [else]
```

Ternary operators replace `if` and `else` for small conditions.

> **Note:** It's not recommended to create complex conditions with ternary operators because it can reduce readability.

Below is another example that uses ternary operators, but this time in the `return` of a function.

```javascript
function sayHelloToAnne(name) {
  return name === "Anne" ? "Hello, Anne!" : "It's not Anne!";
}

console.log(sayHelloToAnne("Anne"));
// Output: 'Hello, Anne!'

console.log(sayHelloToAnne("Gael"));
// Output: "It's not Anne!"
```

## Want to Contribute? Here's How.

You are welcome to contribute to this GitHub repository. Any contribution is appreciated, and it will help each of us improve our JavaScript skills.
[GitHub: JavaScript Awesome Tips](https://github.com/gael-thomas/javascript-awesome-tips)

## Conclusion

I hope you learned some new things about JavaScript while reading this post.

If you want more content like this, you can [follow me on Twitter](https://twitter.com/gaelgthomas/) where I tweet about web development, self-improvement, and my journey as a full stack developer!




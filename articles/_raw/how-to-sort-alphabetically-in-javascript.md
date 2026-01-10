---
title: Sort Alphabetically in JavaScript – How to Order by Name in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-29T19:59:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-alphabetically-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--4-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Sometimes you might have an array of words where you want to sort each
  word alphabetically (from a-z). Or you might have an array of objects containing
  user information including names, for example, where you want to sort the users
  by their names.

  We...'
---

Sometimes you might have an array of words where you want to sort each word alphabetically (from a-z). Or you might have an array of objects containing user information including names, for example, where you want to sort the users by their names.

We can do this in JavaScript by using the `sort()` method directly or with the compare function.

In case you are in a rush, here are the two ways:

```js
// order an array of names
names.sort();

// order an array of objects with name
users.sort(function (a, b) {
  if (a.name < b.name) {
    return -1;
  }
  if (a.name > b.name) {
    return 1;
  }
  return 0;
});
```

Let's now learn how we came to both solutions.

## How to Sort an Array of Names Alphabetically

Suppose we have an array of names:

```js
let names  = ["John Doe", "Alex Doe", "Peter Doe", "Elon Doe"];
```

We can sort these names alphabetically using the `sort()` method:

```js
let sortedNames = names.sort();
console.log(sortedNames);
```

This will return an array of alphabetically sorted names:

```bash
["Alex Doe","Elon Doe","John Doe","Peter Doe"]
```

**Note:** In a situation when some names start with uppercase while others start with lowercase, then the output will be incorrect because the `sort()` method places uppercase letters before lowercase:

```js
let names = ["John Doe", "alex Doe", "peter Doe", "Elon Doe"];
let sortedNames = names.sort();

console.log(sortedNames); // ["Elon Doe","John Doe","alex Doe","peter Doe"]
```

So you'll need to make sure that the words are all in the same case, else it won't return the names alphabetically as we desire.

## How to Order by Name Alphabetically in JavaScript

In a real-world scenario, we might have an array of users with each user's information in an object. This information could be anything alongside the name of the user. For example:

```js
let users = [
  {
    name: "John Doe",
    age: 17
  },
  {
    name: "Elon Doe",
    age: 27
  },
  {
    name: "Alex Doe",
    age: 14
  }
];
```

Looking at the object above, the previous method in which we just applied the `sort()` method on the array directly will not work. Instead, it will throw the same array but the items won't be in the order we want.

We will use the `sort()` method alongside the compare function to order this array of users by name.

We will use the compare function to define an alternative sort order. It returns a negative, zero, or positive value, depending on the arguments:

Syntax:

```js
function(a, b){return a - b}
```

When we pass this comparison function into the `sort()` method, it compares each value based on the condition we set and then sorts each name according to the returned value (negative, zero, positive).

* If the result is negative, `a` is sorted before `b`.
    
* If the result is positive, `b` is sorted before \`a'.
    
* If the result is `0`, no changes are made to the sort order of the two values.
    

Using the example above, we can now use the `sort()` method alongside the compare function this way:

```js
users.sort(function (a, b) {
  if (a.name < b.name) {
    return -1;
  }
  if (a.name > b.name) {
    return 1;
  }
  return 0;
});

console.log(users);
```

The above code compares each name. If it's greater, it returns 1. If it's less, it returns -1. Otherwise, it returns 0. The returned value is used to order our array's values alphabetically:

```bash
[
  {
    name: "Alex Doe",
    age: 14
  },
  {
    name: "Elon Doe",
    age: 27
  },
  {
    name: "John Doe",
    age: 17
  }
]
```

**Note:** Just like we saw previously, this always works according to letter case and will order uppercase letters before lowercase:

```js
let users = [
  {
    name: "alex Doe",
    age: 14
  },
  {
    name: "Elon Doe",
    age: 27
  },
  {
    name: "John Doe",
    age: 17
  }
];
    
users.sort(function (a, b) {
  if (a.name < b.name) {
    return -1;
  }
  if (a.name > b.name) {
    return 1;
  }
  return 0;
});

console.log(users);
```

Output:

```bash
[
  {
    name: "Elon Doe",
    age: 27
  },
  {
    name: "John Doe",
    age: 17
  },
  {
    name: "alex Doe",
    age: 14
  }
]
```

## Wrapping Up

In this article, you have learned how to order an array alphabetically using the `sort()` method in two possible situations.

In a situation when the names have different letter cases, it is best to first convert them to a specific letter case before using the `sort()` method.

Happy coding!

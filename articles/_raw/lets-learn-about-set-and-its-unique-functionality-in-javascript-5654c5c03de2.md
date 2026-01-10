---
title: Let's learn about Set and its unique functionality in JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-17T16:29:45.000Z'
originalURL: https://freecodecamp.org/news/lets-learn-about-set-and-its-unique-functionality-in-javascript-5654c5c03de2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WHhLDFPAo2DnMjPoSXV3sw.png
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Asif Norzai

  SET ?

  ES2015/ES6 gave us a lot of useful tools and features, but one that stands out the
  most for me is Set. It’s not used to its full potential. I hope to convince you
  of its worth with this article, so that you can reap the full bene...'
---

By Asif Norzai

### SET ?

ES2015/ES6 gave us a lot of useful tools and features, but one that stands out the most for me is Set. It’s not used to its full potential. I hope to convince you of its worth with this article, so that you can reap the full benefits of this beautiful utility.

#### So what is Set, you ask?

> “The `**Set**` object lets you store unique values of any type, whether [primitive values](https://developer.mozilla.org/en-US/docs/Glossary/Primitive) or object references.”, [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set).

Set removes duplicate entries.

#### **Basic Functionality** ?

Whenever you want to use `Set`, you have to initialize it using the `new` keyword and pass in an initial [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterable_protocol) data, leave it blank or `null`.

```js
// All valid ways to initialize a set
const newSet1 = new Set();
const newSet2 = new Set(null);
const newSet3 = new Set([1, 2, 3, 4, 5]);
```

### **Set utilities/methods** ?

`**add**`**,** like its name suggests, adds new entries to the newly initialized Set const. If at any time a duplicate value gets added to the set, it will be discarded using `strict equality`.

```js
const newSet = new Set();

newSet.add("C");
newSet.add(1);
newSet.add("C");

// chain add functionality
newSet.add("H").add("C");

newSet.forEach(el => {
  console.log(el);
  // expected output: C
  // expected output: 1
  // expected output: H
});
```

`**has**` checks to see if the value that you pass in exists in the `newSet` const. If the value does exist, it will return the Boolean `true`, and it’ll return `false` if it doesn’t

```js
const newSet = new Set(["A", 2, "B", 4, "C"]);

console.log(newSet.has("A"));
// expected output: true

console.log(newSet.has(4));
// expected output: true

console.log(newSet.has(5));
// expected output: false
```

`**clear**` & `**delete**` are two of the most important functionalities of `Set` if you want to either remove all entries or delete a specific value.

```js
const newSet = new Set(["A", 2, "B", 4, "C"]);

newSet.delete("C");
// expected output: true

newSet.delete("C");
// expected output: false

newSet.size
// expected output: 4

newSet.clear();
// expected output: undefined

newSet.size
// expected output: 0
```

`**keys**` and `values` both have the same functionality, which is weird if you think about how they behave with JS objects. They both return an `iterator` object. This means you can access the `.next()` method on it to get its value.

```js
const newSet = new Set(null);

newSet.add("Apples");
newSet.add(12);

let iterator = newSet.keys();  // same as newSet.values();

console.log(iterator.next().value);
// expected output: Apples

console.log(iterator.next().value);
// expected output: 12

console.log(iterator.next().value);
// expected output: undefined
```

### **Bring it all together**

Let’s create a simple function for a hacker party. The function adds users to the list only if they have the approval of an admin. So you have to have an admin’s name with your entry, which is secret (not in this article, though). At the end of the program, it will say who is invited.

```js
// The Admins
const allowedAdminUsers = new Set(["Naimat", "Ismat", "Azad"]);

// An empty Set, stored in memory
const finalList = new Set();

// A function to add users to permission list
const addUsers = ({user, admin}) => {
  
   // Check to see if the admin is the admin 
  // list and that the user isn't already in the set
  if(allowedAdminUsers.has(admin) && !finalList.has(user)) {
    
    // Return the users list at the end
   return finalList.add(user);
    
  }
  // Console.log this message if the if the condition doesn't pass
  console.log(`user ${user} is already in the list or isn't allowed`); 
};

// Add some entries
addUsers({user: "Asep", admin: "Naimat"});
addUsers({user: "John", admin: "Ismat"});

// Lets add John again and this time that inner function console error will be shown
addUsers({user: "John", admin: "Azad"});

const inviationList = [...finalList].map(user => 
 `${user} is invited`);

console.log(inviationList);
// Expected output:  ["Asep is invited", "John is invited"]
```

That’s enough functionality for us to use Set today in our projects. ?

![Image](https://cdn-media-1.freecodecamp.org/images/9HUfTsuNCDKzpF6NJsItRYlX-68khdXAb9hk)

**Before you go**: if you liked this post, follow me on here and also on [Twitter](https://twitter.com/asepnorzai), where I post and retweet web-related content.


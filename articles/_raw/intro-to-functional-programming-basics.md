---
title: Intro to Functional Programming Basics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-17T23:52:00.000Z'
originalURL: https://freecodecamp.org/news/intro-to-functional-programming-basics
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c89740569d1a4ca32c7.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Functional Programming

  Functional programming is the process of building software by composing pure functions,
  avoiding shared state, mutable data, and side-effects. Functional programming is
  declarative (telling the computer what you want to do) rat...'
---

## **Functional Programming**

Functional programming is the process of building software by composing **pure functions**, avoiding **shared state**, **mutable data**, and **side-effects**. Functional programming is **declarative** (telling the computer what you want to do) rather than **imperative** (telling the computer exactly how to do that), and application state flows through pure functions. Contrast it with object-oriented programming, where application state is usually shared and co-located with methods in objects.

### **Why Functional Programming?**

* It’s generally more concise
* It’s generally more predictable
* It’s easier to test than object-oriented code

### **Adoption by Programing Languages**

Many programming languages support functional programming like Haskell, F#, Common Lisp, Clojure, Erlang, OCaml. JavaScript also has the properties of an untyped functional language.

### **Uses**

Functional programming has long been popular in academia, but with few industrial applications. However, recently several prominent functional programming languages have been used in commercial or industrial systems. For example, the Erlang programming language, which was developed by the Swedish company Ericsson in the late 1980s, is used for building a range of applications at companies such as T-Mobile, Nortel, Facebook, Électricité de France and WhatsApp.

### **Higher-Order Functions**

Higher-order functions are a big part of functional programming. A higher-order function is a function that either takes a function(s) as a parameter or returns a function.

### **Map**

`map` is a higher-order function that calls a function to each element of a list, and returns the results as a _new_ list.

Here is an example of `map`:

```javascript
const myList = [6, 3, 5, 29];

let squares = myList.map(num => num * num); // [36, 9, 25, 841]
```

### **More Information on Functional Programming:**

* [Learn functional programming in Java - full course (video)](https://www.freecodecamp.org/news/functional-programming-in-java-course/)
* [How learning functional programming can make you a better developer](https://www.freecodecamp.org/news/learn-the-fundamentals-of-functional-programming/)
* [How to use functional programming in Modern JavaScript](https://www.freecodecamp.org/news/how-and-why-to-use-functional-programming-in-modern-javascript-fda2df86ad1b/)



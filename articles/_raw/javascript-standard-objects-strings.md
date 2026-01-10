---
title: 'JavaScript Standard Objects: Strings'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-standard-objects-strings
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d18740569d1a4ca35df.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Surely you''ve heard that, in JavaScript, everything is an object. Strings,
  numbers, functions, arrays, and, well, objects, are considered objects.

  In this tutorial we''ll take a deep dive into the String "global" or "standard built-in"
  object, along w...'
---

Surely you've heard that, in JavaScript, everything is an object. Strings, numbers, functions, arrays, and, well, objects, are considered objects.

In this tutorial we'll take a deep dive into the **String** "global" or "standard built-in" object, along with the methods associated with it.

## String.prototype.toUpperCase()

The JavaScript method `String.toUpperCase()` returns the same string it was called on, but in all uppercase characters.

### Syntax

```text
str.toUpperCase()
```

### Examples

```text
console.log("hello world".toUpperCase()); // "HELLO WORLD"
```

## String.prototype.fromCharCode()

The `String.fromCharCode()` method returns a string created by using the specified sequence of Unicode values.

### Syntax

```text
String.fromCharCode(num1, num2...)
```

### **Parameters**

A sequence of numbers that represent Unicode values.

### Examples

```text
String.fromCharCode(65, 66, 67);  // "ABC"

var test = String.fromCharCode(112, 108, 97, 105, 110);
document.write(test);

// Output: plain
```


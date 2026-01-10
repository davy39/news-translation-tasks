---
title: A taste of what’s new in ES10
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-11T17:06:20.000Z'
originalURL: https://freecodecamp.org/news/a-taste-of-whats-new-in-es10-68d28ba22f92
coverImage: https://cdn-media-1.freecodecamp.org/images/0*DiulTq2UG0G7_Jrf
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ashay Mandwarya ?️??

  Every year, a new version of ECMAScript is released with the proposals which are
  officially ready for distribution to devs and users alike. This article will be
  discussing the latest iteration of the language, and what new fea...'
---

By Ashay Mandwarya ?️??

Every year, a new version of ECMAScript is released with the proposals which are officially ready for distribution to devs and users alike. This article will be discussing the latest iteration of the language, and what new features it brings to the table.

**ES10/ES2019** has made great improvements in this update. It introduces functions and methods which will enable developers to write less code, and do more productive work.

**Let’s jump right into it.**

### flat()

flat() is a method which is used to flatten an array. There are certain situations in which the elements of an array are an array. These types of arrays are called nested arrays.

Normally to un-nest (flatten) them, we had to use recursion. Now with the introduction of flat(), it can be done in a single line. F.Y.I — a flattened array is an array of depth 0. flat() takes an argument, a number which represents the depth. Depth is the amount of nesting inside an array. Let's see an example of explaining nesting and depth.

![Image](https://cdn-media-1.freecodecamp.org/images/QUDBVgv-56mkzLWlS5yz04WXxldztqBFW5Ob)
_An array of depth 3_

The above is an array of depth 3. It is an array inside of an array, inside of an array, inside of an array ???. Generally, in JavaScript an array can have a depth of infinity or until you run out of memory. Suppose if an array has nesting depth of 3 and we flatten only till depth 2, then there still will be one nested array inside the main array.

#### **Syntax**

![Image](https://cdn-media-1.freecodecamp.org/images/7PGK5m4DnlCd5ba8m8ScN8PI1omeKLB91OS5)

#### **Returns**

It returns a flattened array.

#### Example

![Image](https://cdn-media-1.freecodecamp.org/images/ATwKx7nwYwfJ3Pr1bntIsdYSk7QKsg-dMmTr)

The nested array of depth 3 is flattened using flat for a depth of 3.

If we put the depth as 2, we get this:

![Image](https://cdn-media-1.freecodecamp.org/images/Q6EA0RBJSfec7TcQ7oIZks09NOudcEQ6J86w)

We can see we still have an un-flattened array, in the output.

### **flatMap()**

flatMap() is used to flatten a nested array and to change the values according to a function like a map() function. This function works on an array and takes a callback as an argument. The callback dictates how the array has to be flattened. It works just like a map, but in addition, it also flattens it. If you want to know more about maps, check out [this](https://hackernoon.com/map-filter-reduce-ebbed4be4201) article.

flatMap() can be used to flatten an array of depth of 1 only, as internally it calls a map function followed by flat function with a depth of 1.

#### **Syntax**

![Image](https://cdn-media-1.freecodecamp.org/images/-JLMPV4UYEggPQoN6iU6LnN2unU0SlrparOw)

#### **Returns**

A flattened array with manipulated values courtesy of the callback function which is provided to it. Just like a map.

**map()**+**flat()**=&**gt;flatma**p()

#### Example

![Image](https://cdn-media-1.freecodecamp.org/images/CCBG2KFQbF63sdLnICx4jf7A8iAOA30QHvpJ)

In this example, map and flatMap are shown one by one to show the difference between the two functions. map() returns an array of arrays that contained the values, while the output of flatMap() was same as map, in addition to the flattening of the array.

### Object.fromEntries()

Another very useful function. Object.fromEntries is used to form objects from a provided key value pair. It takes in a list of key-value pairs and returns an object whose properties are given by the entries. It functions as reverse of **Object.entries()**.

#### **Parameters**

It takes in any iterable, i.e. an array.

#### **Returns**

It returns an object with the given key-value pairs.

#### **Example**

![Image](https://cdn-media-1.freecodecamp.org/images/OL255RjE690hCSdMN9hq567NXpI6zR4GXioW)

We can see that when we supplied a map (which stores values in pairs) to the fromEntries() function, we get an object with respective key-value pairs as just in the map.

### trimStart()

The trimStart() method removes whitespace from the beginning of a string. trimLeft() is an alias of this method.

#### **Syntax**

![Image](https://cdn-media-1.freecodecamp.org/images/xyYdL1RkMnebTKlvSkqFuSfcom7TyS7OsI1i)

#### **Returns**

It returns a string with the white spaces from the front removed.

#### **Example**

![Image](https://cdn-media-1.freecodecamp.org/images/8syOWHSR0HNlxxwrpzB53SyUcoZcyDdu88Kt)

We can clearly see the removed white spaces from the output.

### trimEnd()

The trimEnd() method removes white space from the end of a string. trimRight() is an alias of this method.

#### **Syntax**

![Image](https://cdn-media-1.freecodecamp.org/images/H15TWnL1dwUbOWTyiNWvy7NrohUHI9rah1PL)

#### **Returns**

It returns a string with all spaces trimmed from the end.

#### **Example**

![Image](https://cdn-media-1.freecodecamp.org/images/D-VXK9s3JgxhALJPet71YfkS-iLfMsb2Tomh)

We can clearly see the spaces from the end are trimmed.

### **Changes to catch binding**

Until ES10, we were forced by the syntax to bind an exception variable for the catch clause, whether it was necessary or not. Many time it can be noticed that the catch block is just redundant. ES10 proposal enables us to simply omit the variable altogether, giving us one less thing to care about.

#### **Example**

![Image](https://cdn-media-1.freecodecamp.org/images/8Ljl779UXBNH5uwn2GdtB0xzbQlrSyCjppkZ)

In the above example, we can see that no variable is to be provided to catch to run.

### Symbol Description

When we create a Symbol in JS, it is possible to specify a description which can be used for debugging later. The process of getting back this description is a bit tedious. We have to re-construct the Symbol again and with the help of the toString() method to access the description.

ES10 adds a new read-only property known as description, which returns the description of the Symbol.

#### **Example**

![Image](https://cdn-media-1.freecodecamp.org/images/Tb8bH2d2Bpv0UiowLyz1JS06GJ6HwXPCHqbh)

We can see that we directly get the description using .description property of the Symbol.

### Wrap up

These were some of the features that are going to be introduced in the current ES10 standard. I hope you enjoyed the article! Thanks for reading.

![Image](https://cdn-media-1.freecodecamp.org/images/pZsQZzx0nRyznNDnWEa2-9xpJ0d93RF5mExF)
_Google_


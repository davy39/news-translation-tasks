---
title: How to use destructuring in JavaScript to write cleaner, more powerful code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-08T18:00:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-destructuring-in-javascript-to-write-cleaner-more-powerful-code-9d1b38794050
coverImage: https://cdn-media-1.freecodecamp.org/images/0*xJuGwNdtkReGucN_
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ashay Mandwarya ?️??


  Sometimes you have to destroy to build something new.

  -Mistborn: The Hero of Ages


  ES6 introduced us to one of the most awaited JavaScript features: destructuring.
  As a concept, Destructuring is not new or groundbreaking and ...'
---

By Ashay Mandwarya ?️??

> Sometimes you have to destroy to build something new.

> -Mistborn: The Hero of Ages

ES6 introduced us to one of the most awaited JavaScript features: destructuring. As a concept, Destructuring is not new or groundbreaking and some languages already had Destructuring(??) long before. But it was a much needed and requested feature in JavaScript .

Destructuring is the process of breaking a structure. In the context of programming, the structures are the data structures, and destructuring these data structures means unpacking individual values from the data structure. In JavaScript, destructuring can be applied to an Object or an Array.

**Destructuring makes, breaks whatever…. what use do we have for it??**

Before answering that question, let’s have a formal definition for Destructuring. _MDN to the rescue!_

> The **destructuring assignment** syntax is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables. -MDN

Let’s look at some examples to have a better understanding of the basics of destructuring.

#### Arrays

Sample 1:

![Image](https://cdn-media-1.freecodecamp.org/images/vctLJdok3mwgR0m8Fsg3rQnc1Zt-0IdW1BY6)

When I saw this simple piece of code the first time, I was baffled. I did’t get what happened. If you are like I was, let me try and explain.

In line 1, we define 2 variables `a` and `b` . In the next line both the variables are inside an array in the left hand side which in turn is equated to an actual array in the ride hand side. In the subsequent lines we print the values of `a` & `b` and we get 7 and 8 respectively which were the elements in the RHS array. The magic happening in line 2 is called destructuring.

The LHS destructures the RHS and the values gained from unpacking the elements are assigned to the variables in order.

**But why is the LHS inside an array???**

The destructuring assignment uses similar syntax, on the LHS compared to the RHS to define what values to unpack from the sourced variable.

Sample 2:

![Image](https://cdn-media-1.freecodecamp.org/images/XLVhZxEiMUW3ZcImmob74XfJ35XNICjLHOrK)

Here we have introduced another variable `leftout` in the code now. We have 2 different types of uses of `leftout` in the code.

* `[a,b,leftout]-&`gt; This assigns the third element in the array `to left`out as expected.
* `[a,b,…leftout]-&`gt; This gives the first 2 values `t`o a a`n`d b respectively and the rest of the array is assigned to t`he lefto`ut variable.

The solution lies in the `…` operator. This operator collapses all remaining arguments (**_rest_**) into one array. In the latter point, the first 2 array elements are assigned to `a` & `b` respectively, and the rest of the arguments are collapsed into an array (restructuring maybe??) and assigned to the `leftout` variable. We can verify the same by looking at the output.

#### Objects

Sample 1:

![Image](https://cdn-media-1.freecodecamp.org/images/0IP9fC5h8SaQgOfRupMy3VrAprZD8Y7Ruuis)

Destructuring works the same for object and arrays alike. The object in the LHS has properties `a` & `b` which are assigned respectively to the properties `a` & `b` of the RHS object. We get 1 & 2 respectively by printing them.

One thing to notice (_if you have_) is that there is a slight change in syntax (_now you have_).

![Image](https://cdn-media-1.freecodecamp.org/images/wysq-sQxfF1KgL4u4RzGzyLeJJh2Xm6ayZIi)

> _In Object destructuring, the whole LHS & RHS are wrapped inside `(`_`)`

![Image](https://cdn-media-1.freecodecamp.org/images/AEvjPd-JS4LSFQKNPgft2P1HoBu6CsnZ6EXD)

We can see the error we get when we do not wrap it inside `().` **It says declaration of statement expected.**

What is actually happening is that enclosing something in curly brackets `{}` confuses JavaScript so that it considers it a block and not an Object. Due to that, it is looking for a declaration for the block (_function declaration_), so we enclose the code within `()`. This makes it an expression rather than a block, and we get our results.

Sample 2:

![Image](https://cdn-media-1.freecodecamp.org/images/3VZxBELTjXt0s9TT4XPe9QgKblm-U2wLmocM)

Again the `rest` operator. Works just like in arrays, except this time the rest values are collapsed inside an object because the structure to be used is defined by the LHS.

### What is destructuring used for?

As seen from above examples, we now know the importance of destructuring. There are a lot of uses and different cases of how destructuring can be used for both Objects and Arrays. We will try some of them. (**P.S. —** _the examples are valid for both objects and arrays unless otherwise mentioned._)

#### Variable assignment

We already saw how variables are assigned in the above examples, so let’s have a look at another one.

![Image](https://cdn-media-1.freecodecamp.org/images/qucTgfx8ChDUFSt5e23j9ZC-H-ytxvsm9df1)

In this example an already created array is directly assigned for destructuring. Values are assigned to the variables nonetheless.

The same goes for the Object.

#### Default values

Sometimes it can happen that we define `n` number of variables to get values from destructuring, but the array/object might only have `n-x` elements. In this case `x` variables will be assigned `undefined`.

![Image](https://cdn-media-1.freecodecamp.org/images/bKDR20pG1uWtpsmLS1HBudY4Gqa7aMhWqb97)

We can see that `b` is undefined because the array simply does not have that many elements to destructure and assign every variable.

![Image](https://cdn-media-1.freecodecamp.org/images/cwlRrrmE9KClkUQTlv-QZy9yLLnnhUU1ok8K)

The solution to that is to give default values to the variables, so if there are not enough elements the variables take default values rather than go undefined.

#### Swapping

Swapping is the process of interchanging values between 2 or more variables. A standard way of performing swapping is either using a temporary variable or using XOR. In JavaScript the same can be done using destructuring.

![Image](https://cdn-media-1.freecodecamp.org/images/tLDijuHCNuduNyMosckz9Duuw6-kx90Qg5wc)
_Using temporary variable_

![Image](https://cdn-media-1.freecodecamp.org/images/ODUhWbdggQIzMq8eFQMwQaDrQU6JeUJetUs6)
_Using destructuring_

Swap using a variable temp. The code is self explanatory.

Using destructuring we just swap the position of elements and Voilà! Swap done.

#### Ignoring values

We can capture and use only the values which are required and reject or ignore the unnecessary values.

![Image](https://cdn-media-1.freecodecamp.org/images/zIJpQ2bE1p6MFfkierxlodGv1zvAGjxSmFEa)

Here we can see that we ignored the middle value by not assigning it to any variable thus saving us the hassle.

#### Indirect assignment of a function return

![Image](https://cdn-media-1.freecodecamp.org/images/vw5YPLogWb2GhazAyBcLhlqEmpVQq7pN8pL0)

Here we can see that the function x returns an array. On line 4 where we destructure, we provide the function call which returns the array and not the array directly. It makes the code tidy and easy to read and understand.

#### Assignment to new variables

Properties can be unpacked from an object and assigned to a variable with a different name than the object property.<Applicable to objects only>

![Image](https://cdn-media-1.freecodecamp.org/images/mdhZkJwQQ8sUBjGxMGB0-q1mRY40hNHuRN90)

We can see that the values for properties are also variables to whom values are assigned via destructuring.

#### Nested object and array destructuring

![Image](https://cdn-media-1.freecodecamp.org/images/EDN-Rs05z2noXItyxqtnPY9fIo9G3fYZ5p5J)

As we can see, that data is an object which has a property called location which in turn contains an array whose elements are objects.

With destructuring we have to get the values of all the properties present inside the object inside the location array.

So we created an object called obj which contains the same structure as the data object, and the values we want to unpack are provided as variables (mylatitude,mylongitude,mycity). These in turn are equated to the data array (same as the destructuring syntax before). When the variables are printed we get the respective values.

#### Destructuring with for-of loop

![Image](https://cdn-media-1.freecodecamp.org/images/ZMbT6bd6j3NX79H9wD5MwfUR4dpfw-TcKZ5S)

In the above code snippet, we have a people array of objects whose properties in turn contain an object (people > object >family). Now we want to unpack some of the values from the object using for..of loop.

In the loop we have assigned an object variable, with the same structure as in the people array, ignoring the values we don’t need. We have assigned variables n & m respectively to the name and mother properties, because these are the values we want to unpack. Inside the loop we print the variables and we get the needed values.

### The Big picture.

![Image](https://cdn-media-1.freecodecamp.org/images/1qA678ILbFdyrsQbPU23KMUDk6KCS5g30XFC)
_Photo by [Unsplash](https://unsplash.com/@jeremybishop?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Jeremy Bishop</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

You have to use destructuring in your code or practice it to actually get a hang of it. It seems simple in the examples because the examples are just to make you understand the basics. With complex/multiple operations (reduce()!), desctructuring might get confusing quickly, which we don’t want!

Moreover you might also think destructuring is just sugar syntax for performing a set of tasks (like we can give variables the value of each element from an array using a for loop). To an extent we can say it is sugar, but when we look at the broader image ‘The Big Picture’ we will get why destructuring has more value than just a code minimizer.

JavaScript has many operations for both extracting as well as constructing data, but all of them work on one element at a time.

**For constructing**

![Image](https://cdn-media-1.freecodecamp.org/images/QZXe1vAOI2Ej9qAbqIh6Wy-jGFquOKRXRQoP)

**For extracting** (still one at a time)

![Image](https://cdn-media-1.freecodecamp.org/images/u4ESs-rTstc3LGGnOC-pZMNU0Coi1vq-wlxD)

Although there is a syntax for constructing multiple properties at a time, but it can only be used at the time of assignment — it cannot be used for altering an existing object.

![Image](https://cdn-media-1.freecodecamp.org/images/g07Cm8JHppxOkVc7xSyb08lJtJWIgGCjWc7L)

Before ES6 was introduced, there was no mechanism for extracting all data at once. That’s where destructuring has really come to shine. It lets you extract multiple properties from an object. We have seen this in the above examples.

#### Pitfalls

There is only one I can think of and we discussed it:

* A statement should not start with a curly bracket `{`

### Conclusion

I tried to simplify destructuring by demonstrating as many destructuring use cases as possible. I hope it made this concept clear to you. Now you can use destructuring to write powerful and clean code.

![Image](https://cdn-media-1.freecodecamp.org/images/sUivtdGf22RnNFYooZCq1j0mWzsiOTnKt0yk)
_Google_


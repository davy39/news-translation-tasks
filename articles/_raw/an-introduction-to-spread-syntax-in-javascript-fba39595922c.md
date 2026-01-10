---
title: An introduction to Spread syntax in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-03T21:16:09.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-spread-syntax-in-javascript-fba39595922c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*wYWeW6thQtSGbuS5
tags:
- name: coding
  slug: coding
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

  What is it and why do we need it?


  _Photo by [Unsplash](https://unsplash.com/@thesollers?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Anton Darius | @theSollers on <a href="https://unsplash.co...'
---

By Ashay Mandwarya ?️??

#### What is it and why do we need it?

![Image](https://cdn-media-1.freecodecamp.org/images/kpPvb3XGdd7Dt04-ad26LV1wNB-YWlD5Uljn)
_Photo by [Unsplash](https://unsplash.com/@thesollers?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Anton Darius | @theSollers</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

The spread syntax was introduced in the ES6 specification of JavaScript. It since has proved to be a valuable piece of code making the code clean and easy to understand.

MDN defines **…** as:

> **Spread syntax** allows an iterable such as an array expression or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected, or an object expression to be expanded in places where zero or more key-value pairs (for object literals) are expected.

Let’s all agree that the above definition is a handful and none of us caught a word it is trying to say. So let’s start with the most basic things about the spread syntax.

* The spread operator is just 3 dots `...`
* It can be used on iterables like an array or a string.
* It expands an iterable to its individual elements
* It can provide a function call with an array (or any other iterable) where 0 or more arguments were expected.

**Example**

The below snippet contains a function called sum which expects 3 arguments x, y, and z. We have an array with 3 elements, and we want to pass the elements in the array as the arguments for the function.

![Image](https://cdn-media-1.freecodecamp.org/images/3hR85inZDEf6pPSrvHNxh6nBWCtiyzMLDTCu)

Before the spread operator was introduced, this was done via the apply function.

After the introduction of the spread operator, it could be done very simply:

![Image](https://cdn-media-1.freecodecamp.org/images/GOyLsS18ND0S5WdIYUueFVTr5w5n7chDfOg4)

As can be seen from the above snippet with the spread operator, we do not have to use the apply function. This saves us from writing more code.

The above example gives a very rough and brief idea about the spread operator. First, let’s get into more details regarding the same, and then we will see more examples.

### Syntax

The spread operator can be used in many ways and scenarios such as

* **Inside function calls**

![Image](https://cdn-media-1.freecodecamp.org/images/GBky3Srjrr4UtzdstTzJLa1jYs95mZhfZMCT)

When used in the above scenario the `…` is called the rest parameter. We will see examples related to this in the examples section.

* **Creating/Extending an array/iterable:**

![Image](https://cdn-media-1.freecodecamp.org/images/plbemKpJR4jYL1RxOpQykp6DLOwKRgU0zAIK)

### Examples

* **As rest**

… is used as an argument for a variadic function. A variadic function is a function which can have a variable number of parameters.

![Image](https://cdn-media-1.freecodecamp.org/images/E65KbaqcTyzOKHExPf06s1PxCeNN5ecEg9qQ)

Here when we return args, we see that we get back our array which we passed as separate values in the call. This shows that the rest operator actually works exactly opposite of the spread syntax. One expands and one condenses the value.

One more thing to point out is that there is no specific number of parameters mentioned in the function definition. This means using … the function can have n number of arguments. We do not need to specify the parameters beforehand.

This is particularly a very flexible way of receiving arguments for a function for which the specific numbers of arguments aren’t determined like the Math.max and Math.min function. They are variadic functions as the numbers of inputs can be infinite for them.

Back to the example, to get the sum of all the arguments

![Image](https://cdn-media-1.freecodecamp.org/images/GGxZLLfTPqmxmoz4UWDs9QC0gcPwfTY79mRb)

We have to iterate the array and add all the individual elements to produce the result.

* **Push elements in an array**

push() function is used to push elements into an array. The limitation with push is that we have to push elements one by one (push(1,2,3)). If there is an array whose elements are to be inserted in the array using push we will get a multidimensional array, which we did not ask for.

![Image](https://cdn-media-1.freecodecamp.org/images/jDIOeXcE5FWI28Pd3ZvA2glor-bky4ULBLRn)

Again apply to the rescue

![Image](https://cdn-media-1.freecodecamp.org/images/A8ehvgpbQXdo5QjrEV01luli6oiXLS2RGv12)

As we can see that using apply does not look very elegant and we need a simple and small syntax to do that. Let us use spread …

![Image](https://cdn-media-1.freecodecamp.org/images/7mVMylAGnatsCSTGdBWyn5Fo2oZ70UWUNwLW)

Elegant!

* **Copying an array**

![Image](https://cdn-media-1.freecodecamp.org/images/PjvE5dPbLmi1dK0UDrBH95ads1-wlP-ADGMN)

Simple!

The same result can be produced using an object

![Image](https://cdn-media-1.freecodecamp.org/images/YYlEmAxXhv2fZ0C0ROiBC74mbRP1mWesgHI5)

* **Concatenating 2 arrays**

Concatenation is done using the concat function

![Image](https://cdn-media-1.freecodecamp.org/images/WlYNJfs0jB6Hw4Y3VttUHTn8lI6S5FDiiidQ)

Same can be achieved using the … operator

![Image](https://cdn-media-1.freecodecamp.org/images/eSN8Hm-y7BbaBtEXHU9k5SfMHbeK8IyPO3hQ)

* **Converting a string to an array**

This can be done using both the split function and the … operator

![Image](https://cdn-media-1.freecodecamp.org/images/vHzSvkmtOb1eLW8XuoLhVOtsEYP4-ZuVFa1-)

![Image](https://cdn-media-1.freecodecamp.org/images/0hJH3tYjZ96gDMlAVioIG9hoK4p1Zo-RVCEv)

* **Use in max and min functions**

The below snippet tends to find the maximum element in the array, so we pass the whole array in the function but we get the result as NaN

![Image](https://cdn-media-1.freecodecamp.org/images/rGe20ar6559QFEyd1NzdUF8S-2Z2VqR6S13p)

We can use apply, but as seen from the previous examples I hate using it

![Image](https://cdn-media-1.freecodecamp.org/images/4318SrchWxeR0K2k9GTS45C0DH1i0I5ZqUBy)

Same for min

![Image](https://cdn-media-1.freecodecamp.org/images/SnMeVaTIwhsxcJYIzHn34touLSHHJaODLhJO)

### Conclusion

We saw many situations where the spread operator comes in handy and reduces our code and also makes it super easy to understand.

If you like it Clap? and Follow? for more.

![Image](https://cdn-media-1.freecodecamp.org/images/QM0OaPVNzU78PsxECtJR-DrVQBUFaXN15dT7)
_Google_


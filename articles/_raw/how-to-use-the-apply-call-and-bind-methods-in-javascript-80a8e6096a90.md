---
title: How to use the apply(?), call(?), and bind(➰) methods in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T18:06:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-apply-call-and-bind-methods-in-javascript-80a8e6096a90
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FzzV3ThEeCwqNKNL
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ashay Mandwarya ?️??

  In this article, we’ll talk about the apply, call, and bind methods of the function
  prototype chain. They are some of the most important and often-used concepts in
  JavaScript and are very closely related to the this keyword.

  S...'
---

By Ashay Mandwarya ?️??

In this article, we’ll talk about the apply, call, and bind methods of the function prototype chain. They are some of the most important and often-used concepts in JavaScript and are very closely related to the _this_ keyword.

So, to get a grasp of the information in this article, first you have to be familiar with the concept and use of the _this_ keyword. If you are already familiar with it then you can proceed — else, you can refer this article [here](https://medium.freecodecamp.org/a-guide-to-this-in-javascript-e3b9daef4df1) and then come back here.

To learn about **apply|call|bind** we need to know about functions in JavaScript too, assuming you are familiar with _this_.

### Functions

![Image](https://cdn-media-1.freecodecamp.org/images/EIxaDY6mTA74uZjnPlWuLJAIzhhTuxGEiVC9)
_Photo by [Unsplash](https://unsplash.com/@the_roaming_platypus?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">The Roaming Platypus</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

The Function constructor creates a new Function object. Calling the constructor directly can create functions dynamically, which can be executed in the global scope.

As functions are objects in JavaScript, their invocation is controlled by the **apply, call, and bind** methods.

To check if a function is a Function object, we can use the code in the following snippet, which returns true.

![Image](https://cdn-media-1.freecodecamp.org/images/qOSEplK6rs2hhpbJBDkiBwASvpaAnd9XW3EX)

> The global Function object has no methods or properties of its own. However, since it is a function itself, it does inherit some methods and properties through the prototype chain from Function.prototype. — MDN

The following are the methods in the function prototype chain:

* **Function.prototype.apply()**
* **Function.prototype.bind()**
* **Function.prototype.call()**
* Function.prototype.isGenerator()
* Function.prototype.toSource()
* Object.prototype.toSource
* Function.prototype.toString()
* Object.prototype.toString

We are concerned with the first three, so let’s begin.

### Apply ?

![Image](https://cdn-media-1.freecodecamp.org/images/2iPUdLujyCPb7mglSPBbmJNDoAUbrFmLcGlw)
_Photo by [Unsplash](https://unsplash.com/@anckor?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Julian O'hayon</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

> The **apply()** method is an important method of the function prototype and is used to call other functions with a provided _this_ keyword value and arguments provided in the form of array or an array like object.

Array-like objects may refer to NodeList or the arguments object inside a function.

This means that we can call any function and explicitly specify what _this_ should reference in the calling function.

#### Syntax

![Image](https://cdn-media-1.freecodecamp.org/images/F6MxVYBXV6R5cwxInuapX0vlxhhG8Hr5aRp6)

#### Return

It returns the result of the function which is invoked by _this._

#### Description

The **apply** method is used for allowing a function/object belonging to an object x to be called and assigned to an object y.

#### Examples

#### 1.

![Image](https://cdn-media-1.freecodecamp.org/images/BwwKE0rDKIyFmfJbiLfV-6h-sYIXXrdeD3vL)

As seen in the given snippet, we see that when we push an array inside another, the whole array is treated as one element and pushed inside the array variable.

But what if we want the elements to be pushed individually instead as an array? Sure there are literally n number of ways to do so, but as we are learning apply, let’s use it:

![Image](https://cdn-media-1.freecodecamp.org/images/NuH14RCGXQv2R0jiw7U34bJ2FeTonBfE3Yl8)

In the given example we can see the use of **apply** in joining two given arrays. The arguments array is the elements array and the _this_ argument points to the array variable. The elements of the elements array are pushed to the Object(_array_) to which the _this_ is pointing_._ We get the result as the second array’s individual elements pushed to the array to which the _this_ is pointed.

#### 2.

![Image](https://cdn-media-1.freecodecamp.org/images/87MhVt1p1yejr-WnUHXElvuWx8qLgUFi4g4s)

The max function in JS is used to find the element with the maximum value from a given pool of elements. But as we can see from the snippet, if the values are in the form of an array, we get the result as NaN. Surely we are talking about JavaScript so again, there are n number of ways doing this, but let’s use apply.

![Image](https://cdn-media-1.freecodecamp.org/images/yDD0VibWncT0LGNE09uj6V0JgkEHrDRNxvY8)

Now when we use apply and use the Math.max() function, we get the result. As we know, the apply will take all the values inside the array as individual arguments and then the max function will be applied to them. This will give us the maximum value in the array.

An interesting thing to point out here is that in place of _this_ we have used null. As the argument provided is the number array, even if _this_ is introduced it will point to the same array and we will get the same result. Therefore, in such cases, we can use null in place of _this._ This shows us that the _this_ argument in the apply function is an optional argument.

### Call

![Image](https://cdn-media-1.freecodecamp.org/images/6qS5RGWz35jfeQxoKPXtxee5EYrUX0HDqrMd)
_Photo by [Unsplash](https://unsplash.com/@ericmuhr?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Eric Muhr</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

> The **call()** method is used to call a function with a given _this_ and arguments provided to it individually.

This means that we can call any function, explicitly specifying the reference that _this_ should reference in the calling function.

This is very similar to **apply,** the only difference being that **apply** takes arguments in the form of an array or array-like objects, and here the arguments are provided individually.

#### Syntax

![Image](https://cdn-media-1.freecodecamp.org/images/huZ9MJlBZBLQHOCJqKBJN0PxhY1DtvFV0Tqg)

#### Return

The result of calling the function with the specified `**this**` value and arguments.

#### Description

The **call** method is used for allowing a function/object belonging to an object x to be called and assigned to an object y.

#### Examples

#### 1.

![Image](https://cdn-media-1.freecodecamp.org/images/rMsi0io-O7iX5t5YqfljgTgYEC5mWTEJHXcz)

This is an example of constructor chaining. As we can see, in every function the constructor of the Product is called, and using **call** the properties of the Product object are chained with the Pizza and Toy objects, respectively.

When new instances are created of the Pizza and Toy objects, parameters are provided as name, price and category. Category is applied in the definition only, but the name and price are applied using the chained constructor of the Product object, as they are defined and applied in the Product object. With a little more tweaking we can achieve inheritance.

#### 2.

![Image](https://cdn-media-1.freecodecamp.org/images/iVxMTwdWkE5H9tfzv-8xCm84IDJOruqEmGXS)

In the snippet above, we defined a function called sleep. It consists of an array reply which consists of elements which address properties using the _this_ keyword. They are defined in a separate object outside the function.

The function sleep is called with the object _obj_ as an argument. As we can see, the properties of the _obj_ are set in the _this.animal_ and _this.sleepDuration,_ respectively, and we get the full sentence as output.

### Bind➰

![Image](https://cdn-media-1.freecodecamp.org/images/DITA8UeL2muluoiEjqmiYAnHO9mWDYqIEr0G)
_Photo by [Unsplash](https://unsplash.com/@michaelheld?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Michael Held</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

> The **bind()** method creates a new function that, when called, has its `this` keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called. — MDN

#### Syntax

![Image](https://cdn-media-1.freecodecamp.org/images/CEVBSady5dOht7k7f-qex5gsTijBcqVQXobA)

#### Return

**Bind** returns a copy of the function with the supplied _this_ and the arguments.

#### Description

The **bind** function is much like the **call** function, with the main difference being that bind returns a new function whereas call does not.

According to ECMAScript 5 specifications, the function returned by **bind** is a special type of exotic function object (as they call it) called the **Bound function** **(BF)**. The BF wraps the original function object. Calling a BF runs the wrapped function in it.

#### Examples

#### 1.

![Image](https://cdn-media-1.freecodecamp.org/images/wxd-80Uzp6j4LGZ7nOnzt6jBrJJD2-g6MpFq)
_Example taken from MDN_

In the above snippet, we have defined a variable x and an object called module. It also contains a property called _x_ and another property whose corresponding value is a function which returns the value of _x_.

When the function _getX_ is called it returns the values of _x_ which is defined inside the object and not the _x_ in the global scope.

Another variable is declared in the global scope which calls the _getX_ function from the _module_ object. But as the variable is in the global scope, the _this_ in the _getX_ points to the global _x_ and hence 9 is returned.

Another variable is defined which calls the previous function but this time binds the said function with the _module_ object. This binding returns the value of _x_ inside the object. Due to the binding, the _this_ in the function points to the value of _x_ in the object and not the global _x_. Hence we get 81 as the output

### Conclusion

Now that we have learned the basics about the methods, you might still be a little bit confused about why there are 3 different functions doing almost the same thing. To clarify this concept, you have to practice with different situations and scenarios so you can learn more thoroughly where and how they can be used. They will for sure make your code cleaner and more powerful.

If you liked this article, please clap? and follow? for more.

![Image](https://cdn-media-1.freecodecamp.org/images/ueu4IJwqszzZov80yvEMaZi9e4RPClhf6sjx)
_Google_


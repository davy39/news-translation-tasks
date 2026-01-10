---
title: How array.prototype.map() works
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-27T23:12:55.000Z'
originalURL: https://freecodecamp.org/news/how-array-prototype-map-works-b6b69379c3af
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sxqOoI2RvGq8n7MYwoWX-w.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Pradeep Pothineni

  JavaScript is an ubiquitous language now. Once confined to client side usage, now
  you can find it on servers in many flavors. As JavaScript grew, so did its arsenal
  of functions that users can use. Most times you are content usin...'
---

By Pradeep Pothineni

JavaScript is an ubiquitous language now. Once confined to client side usage, now you can find it on servers in many flavors. As JavaScript grew, so did its arsenal of functions that users can use. Most times you are content using these methods and only rarely will you want to take that extra step to understand what is really going on under the hood.

On that note, let’s take that extra step today and explore a very popular function: `**Array.prototype.map()**`_._

![Image](https://cdn-media-1.freecodecamp.org/images/1*sxqOoI2RvGq8n7MYwoWX-w.jpeg)

_Disclaimer_: I won’t be explaining how to use `**map()**` **—** the below example illustrates it, or you can find numerous examples when you google. Instead, let’s dwell into how map actually gets implemented behind the scenes.

The `**map()**` method creates a new array with the result of calling a provided function on every element in the calling array.

Example:

```js
var array1 = [1, 4, 9, 16];
// pass a function to map
const map1 = array1.map(x => x * 2);

console.log(map1);
// expected output: Array [2, 8, 18, 32]
```

#### **Implementation**

Let’s pick the implementation right from the horse’s mouth and try dissecting it. Below is the MDN polyfill. Spend some time understanding the code and copy it and run it on your machine. If you are a beginner/intermediate JavaScript developer, you will surely run into at least couple of questions.

```js
/*Array.prototype.map implementation*/
Array.prototype.map = function (callback/*, thisArg*/) {
    var T, A, k;
    if (this == null) {
        throw new TypeError('this is null or not defined');
    }
    var O = Object(this);
    var len = O.length >>> 0;
    if (typeof callback !== 'function') {
        throw new TypeError(callback + ' is not a function');
    }
    if (arguments.length > 1) { 
        T = arguments[1];
    }
    A = new Array(len);
    k = 0;
    while (k < len) {
        var kValue, mappedValue;
        if (k in O) {
            kValue = O[k];
            mappedValue = callback.call(T, kValue, k, O);            
            A[k] = mappedValue;
        }
        k++;
    }
    return A;
};
```

I have highlighted few common questions that might arise in the code comments below.

```js
/*Array.prototype.map implementation*/
Array.prototype.map = function (callback/*, thisArg*/) {
    var T, A, k;
    if (this == null) {
        throw new TypeError('this is null or not defined');
    }
    var O = Object(this);
    var len = O.length >>> 0;// QUESTION 1 : What is the need for this line of code?
    if (typeof callback !== 'function') {
        throw new TypeError(callback + ' is not a function');
    }
    if (arguments.length > 1) { 
        T = arguments[1];
    }
    //  QUESTION 2 :What is the need for the if condition and why are we assiging T=arguments[1]?
    A = new Array(len);
    k = 0;
    while (k < len) {
        var kValue, mappedValue;
        if (k in O) {
            kValue = O[k];
            mappedValue = callback.call(T, kValue, k, O); 
            // QUESTION 3: why do we pass T,k and O when all you need is kvalue?
            A[k] = mappedValue;
        }
        k++;
    }
    return A;
};
```

Let’s address each of them starting from the bottom

**QUESTION 3: Why do we pass T,k and O when all you need is kValue?**

```js
mappedValue = callback.call(T, kValue, k, O);
```

This is the simplest of the three questions so I have picked this to start with. In most cases, passing the **kValue** to the **callback** would be sufficient but:

* What if you have a use case where you need to perform an operation only on every other element? Well, you need an index which is **(k)**.
* Similarly there could be other use cases where you need the array **(O)** itself to be available in the callback.
* Why **T**? For now just know that **T** is being passed around to maintain context. You will understand this better once you are done with question 2.

**QUESTION 2 :What is the need for the if condition and why are we assigning T=arguments[1]?**

```js
if (arguments.length > 1) {   T = arguments[1];    }
```

The map function in the above implementation has two arguments: the **callback** and the optional **thisArg**_. Callback is a mandatory argument whereas **thisArg** is optional._

One can pass what should be the **“this”** value inside the **callback** by providing the second optional argument. This is why the code checks if there is more than one argument and assigns the second optional argument to a variable that can be passed on to the callback.

To illustrate better, let’s say you have a mock requirement where you need to return the _number/2_ if it is divisible by 2, and if it is not divisible by 2, you need to return the username of the calling person. The below code illustrates how you can make this happen:

```js
const myObj = { user: "John Smith" }
var x = [10, 7];
let output = x.map(function (n) {
  if (n % 2 == 0) {
    return n / 2;
  } else {
    return this.user
  }
}, myObj) // myObj is the second optional argument arguments[1]

console.log(output); // [5,'John Smith']
//if you run the program without supplying myObj it would be //undefined as it cannot access myObj values
console.log(output); // [ 5, undefined ]
```

**QUESTION 1: What is the need for this line of code?**

```js
var len = O.length >>> 0
```

This one took some time for me to figure out. There is a lot going on in this line of code. In JavaScript, you have the ability to redefine the **“this”** within a function by invoking the method using **call_._** You can do this using **bind** or **apply** as well, but for this discussion lets stick with **call.**

```js
const anotherObject={length:{}} 
const myObj = { user: "John Smith" }
var x = [10, 7];
let output = x.map.call(anotherObject,function (n) {
  if (n % 2 == 0) {return n / 2;}
  else 
  {return this.user}
}, myObj)
```

When you invoke using **call,** the first parameter would be the context in which the map function executes. By sending the parameter, you are overwriting the **“this”** inside the map with the **“this”** of anotherObject.

If you observe, the **length** property of the anotherObject is an empty object and not an integer. If you just use **O.length instead of O.length>**>>0 it would result in an undefined value. By zero shifting, you are actually converting any fractions and non integers to an integer. In this case the result would be coerced to 0.

Most use cases won’t need this check, but there might be an edge case where this kind of scenario needs to be handled. The good programmers who designed the specification really did think it through! Talking about the specification, you can actually find the specification on how each function has to be implemented in Ecmascript here:

[**ECMAScript Language Specification - ECMA-262 Edition 5.1**](https://www.ecma-international.org/ecma-262/5.1/#sec-15.4.4.19)  
[_This document and possible translations of it may be copied and furnished to others, and derivative works that comment…_](https://www.ecma-international.org/ecma-262/5.1/#sec-15.4.4.19)  
[www.ecma-international.org](https://www.ecma-international.org/ecma-262/5.1/#sec-15.4.4.19)

The spec (**step 3**) clearly says that the length has to be a 32 bit unsigned integer. This is the reason we are zero fill shifting to ensure that length is an integer, as map itself does not require that the **this** value be an Array object.

That’s it!

I would like to thank couple of people, i never met them but they were kind enough to take time (in internet forums) and help me understand few nuances.

[Salathiel Genese](https://github.com/SalathielGenese), [Jordan Harband](https://twitter.com/ljharb) — thank you!

Note: If you are stuck on a different line of code, feel free to put that in the comments and I will do my best to clarify.

Thank you for your time and happy coding!


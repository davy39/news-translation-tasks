---
title: Hacks for Creating JavaScript Arrays
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T22:59:31.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-gladchinda-hacks-for-creating-javascript-arrays-a1b80cb372b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ikt9LNJUhCX7QxbjnwKstA.png
tags:
- name: ES6
  slug: es6
- name: hacks
  slug: hacks
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Glad Chinda

  Insightful tips for creating and cloning arrays in JavaScript.


  _Original Photo by [Unsplash](https://unsplash.com/photos/FXFz-sW0uwo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" ti...'
---

By Glad Chinda

#### Insightful tips for creating and cloning arrays in JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/IH842JnVoctZM6QoKOfXQe8luuYHXHjMuNxf)
_Original Photo by [Unsplash](https://unsplash.com/photos/FXFz-sW0uwo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Markus Spiske</a> on <a href="https://unsplash.com/search/photos/code?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

A very important aspect of every programming language is the data types and structures available in the language. Most programming languages provide data types for representing and working with complex data. If you have worked with languages like Python or Ruby, you should have seen data types like **lists**, **sets**, **tuples**, **hashes**, **dicts**, and so on.

In JavaScript, there are not so many complex data types — you simply have **arrays** and **objects**. However, in ES6, a couple of data types and structures were added to the language, such as **symbols**, **sets**, and **maps**.

> _Arrays in JavaScript are high-level list-like objects with_ a length property and _integer properties as indexes._

In this article, I share a couple of hacks for creating new JavaScript arrays or cloning already existing ones.

### Creating Arrays: The Array Constructor

The most popular method for creating arrays is using the **array literal** syntax, which is very straightforward. However, when you want to dynamically create arrays, the array literal syntax may not always be the best method. An alternative method is using the `Array` constructor.

Here is a simple code snippet showing the use of the `Array` constructor.

<script src="https://gist.github.com/gladchinda/fe7eee22be4cd4722d3e0099fadd3919.js"></script>

From the previous snippet, we can see that the `Array` constructor creates arrays differently depending on the arguments it receives.

### New Arrays: With Defined Length

Let’s look more closely at what happens when creating a new `Array` of a given length. The constructor just sets the `length` property of the array to the given length, without setting the keys.

![Image](https://cdn-media-1.freecodecamp.org/images/HuAR3m0WmxP390Ezk4Ufyam-9vlyDzwNvEzi)

From the above snippet, you may be tempted to think that each key in the array was set to a value of `undefined`. But the reality is that those keys were never set (they don’t exist).

The following illustration makes it clearer:

![Image](https://cdn-media-1.freecodecamp.org/images/wtfHBQo1MBofKp-EVs-IB6qqq07cfM18rK8I)

This makes it useless to attempt to use any of the array iteration methods such as `map()`, `filter()` or `reduce()` to manipulate the array. Let’s say we want to fill each index in the array with the number `5` as a value. We will attempt the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1OHTGXHuG93TuWcOpzRVtUNjoB-BFP3Pykq5)

We can see that `map()` didn’t work here, because the index properties don’t exist on the array — only the `length` property exists.

Let’s see different ways we can fix this issue.

#### 1. Using Array.prototype.fill()

The `**fill()**` method fills all the elements of an array from a start index to an end index with a static value. The end index is not included. You can learn more about `fill()` [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill).

**Note that `fill()` will only work in browsers with ES6 support.**

Here is a simple illustration:

![Image](https://cdn-media-1.freecodecamp.org/images/w3CWlvnWqG5VEy6qupnAYvTqECGhPdj3P9Wu)

Here, we have been able to fill all the elements of our created array with `5`. You can set any static value for different indexes of the array using the `fill()` method.

#### 2. Using Array.from()

The `**Array.from()**` method creates a new, shallow-copied `Array` instance from an array-like or iterable object. You can learn more about `Array.from()` [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from).

**Note that `Array.from()` will only work in browsers with ES6 support.**

Here is a simple illustration:

![Image](https://cdn-media-1.freecodecamp.org/images/XfZGhDWQWU1VwxliMKIjYgHuwYvkfvPSBkVT)

Here, we now have true `undefined` values set for each element of the array using `Array.from()`. This means we can now go ahead and use methods like `.map()` and `.filter()` on the array, since the index properties now exist.

One more thing worth noting about `Array.from()` is that it can take a second argument, which is a **map function.** It will be called on every element of the array. This makes it redundant calling `.map()` after `Array.from()`.

Here is a simple example:

![Image](https://cdn-media-1.freecodecamp.org/images/UgaAHFIo4xzuw4cc4bI1iaxaPzGHKkTCbjYK)

#### 3. Using the Spread Operator

The **spread operator** (`...`), added in ES6, can be used to spread the elements of the array, setting the missing elements to a value of `undefined`. This will produce the same result as simply calling `Array.from()` with just the array as the only argument.

Here is a simple illustration of using the spread operator:

![Image](https://cdn-media-1.freecodecamp.org/images/gZrwaPsFq15WkPf2BnuAb2wA54JdIEXx7VNv)

You can go ahead and use methods like `.map()` and `.filter()` on the array, since the index properties now exist.

### Using Array.of()

Just like we saw with creating new arrays using the `Array` constructor or function, `**Array.of()**` behaves in a very similar fashion. In fact, the only difference between `Array.of()` and `Array` is in how they handle a single integer argument passed to them.

While `**Array.of(5)**` creates a new array with a single element, `5`, and a length property of `1`, `**Array(5)**` creates a new empty array with 5 empty slots and a length property of `5`.

```js
var array1 = Array.of(5); // [5]
var array2 = Array(5); // Array(5) {length: 5}
```

Besides this major difference, `Array.of()` behaves just like the `Array` constructor. You can learn more about `Array.of()` [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of).

**Note that `Array.of()` will only work in browsers with ES6 support.**

### Converting to Arrays: Array-likes and Iterables

If you have been writing JavaScript functions long enough, you should already know about the `arguments` object — which is an **array-like** object available in every function to hold the list of arguments the function received. Although the `arguments` object looks much like an array, it does not have access to the `Array.prototype` methods.

Prior to ES6, you would usually see a code snippet like the following when trying to convert the `arguments` object to an array:

![Image](https://cdn-media-1.freecodecamp.org/images/NaMaYAla-PzcPacVZGr3E03twovKgKTuRVwm)

With `Array.from()` or the spread operator, you can conveniently convert any array-like object into an array. Hence, instead of doing this:

```
var args = Array.prototype.slice.call(arguments);
```

you can do either of these:

```js
// Using Array.from()
var args = Array.from(arguments);

// Using the Spread operator
var args = [...arguments];
```

These also apply to **iterables** as shown in the following illustration:

![Image](https://cdn-media-1.freecodecamp.org/images/87TEnXS9-qV7Lak1XBBcEYiQVvh96FqXDJXc)

### Case Study: Range Function

As a case study before we proceed, we will create a simple `**range()**` function to implement the new **array hack** we just learned. The function has the following signature:

```js
range(start: number, end: number, step: number) => Array<number>
```

Here is the code snippet:

<script src="https://gist.github.com/gladchinda/439981b34aa8f23c661e9663edf762f0.js"></script>

In this code snippet, we used `Array.from()` to create the new range array of dynamic length and then populate it sequentially incremented numbers by providing a mapping function.

**Note that the above code snippet will not work for browsers without ES6 support except if you use polyfills.**

Here are some results from calling the `**range()**` function defined in the above code snippet:

![Image](https://cdn-media-1.freecodecamp.org/images/zFBQwh8KfkoDDWXcZDl8YnDe7e9jBEsocdCa)

You can get a live code demo by running the following pen on **Codepen**:

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="QxeXzm" src="//codepen.io/gladchinda/embed/QxeXzm/?height=265&theme-id=0&default-tab=js,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/gladchinda/pen/QxeXzm/'>QxeXzm</a> by Glad Chinda
  (<a href='https://codepen.io/gladchinda'>@gladchinda</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

### Cloning Arrays: The Challenge

In JavaScript, arrays and objects are reference types. This means that when a variable is assigned an array or object, what gets assigned to the variable is a reference to the location in memory where the array or object was stored.

Arrays, just like every other object in JavaScript, are reference types. **This means that arrays are copied by reference and not by value.**

Storing reference types this way has the following consequences:

#### **1. Similar arrays are not equal.**

![Image](https://cdn-media-1.freecodecamp.org/images/brYlg3Dp3gVRqGqHGkMBR2XR7eLvWQK8xymc)

Here, we see that although `array1` and `array2` contain seemingly the same array specifications, they are not equal. This is because the reference to each of the arrays points to a different location in memory.

#### **2. Arrays are copied by reference and not by value.**

![Image](https://cdn-media-1.freecodecamp.org/images/PZF-lU5f4C-OWkNLeF-q4g9T2anP6k88PPr1)

Here, we attempt to copy `array1` to `array2`, but what we are basically doing is pointing `array2` to the same location in memory that `array1` points to. Hence, both `array1` and `array2` point to the same location in memory and are equal.

The implication of this is that when we make a change to `array2` by removing the last item, the last item of `array1` also gets removed. This is because the change was actually made to the array stored in memory, whereas `array1` and `array2` are just pointers to that same location in memory where the array is stored.

### Cloning Arrays: The Hacks

#### **1. Using Array.prototype.slice()**

The `**slice()**` method creates a shallow copy of a portion of an array without modifying the array. You can learn more about `slice()` [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice).

The trick is to call `slice()` either with`0` as the only argument or without any arguments at all:

```js
// with O as only argument
array.slice(0);

// without argument
array.slice();
```

Here is a simple illustration of cloning an array with `slice()`:

![Image](https://cdn-media-1.freecodecamp.org/images/-XUoysUS92IrVW9lYY6EkJHXv8vKw0yahdaW)

Here, you can see that `array2` is a clone of `array1` with the same items and length. However, they point to different locations in memory, and as a result are not equal. You also notice that when we make a change to `array2` by removing the last item, `array1` remains unchanged.

#### **2. Using Array.prototype.concat()**

The `**concat()**` method is used to merge two or more arrays, resulting in a new array, while the original arrays are left unchanged. You can learn more about `concat()` [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat).

The trick is to call `concat()` either with an empty array(`[]`) as argument or without any arguments at all:

```js
// with an empty array
array.concat([]);

// without argument
array.concat();
```

Cloning an array with `concat()` is quite similar to using `slice()`. Here is a simple illustration of cloning an array with `concat()`:

![Image](https://cdn-media-1.freecodecamp.org/images/OXjY30kwODk5622BQraHtZfHxN5d5gewTeZj)

#### 3. Using Array.from()

Like we saw earlier, `**Array.from()**` can be used to create a new array which is a shallow-copy of the original array. Here is a simple illustration:

![Image](https://cdn-media-1.freecodecamp.org/images/kS-1uaQbt9K6zFk4PZWfmnLXHADDnHaVqELf)

#### 4. Using Array Destructuring

With ES6, we have some more powerful tools in our toolbox such as **destructuring**, **spread** **operator**, **arrow functions**, and so on. Destructuring is a very powerful tool for extracting data from complex types like arrays and objects.

The trick is to use a technique called **rest parameters,** which involves a combination of array destructuring and the spread operator as shown in the following snippet:

```js
let [...arrayClone] = originalArray;
```

The above snippet creates a variable named `arrayClone` which is a clone of the `originalArray`. Here is a simple illustration of cloning an array using array destructuring:

![Image](https://cdn-media-1.freecodecamp.org/images/aohdaDoLpdH1XJ8Thk5U4JE7u0g89qsaTUcI)

# Cloning: Shallow versus Deep

All the array cloning techniques we’ve explored so far produce a **_shallow copy_** of the array. This won’t be an issue if the array contains only primitive values. However, if the array contains nested object references, those references will remain intact even when the array is cloned.

Here is a very simple demonstration of this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image.png)

Notice that modifying the nested array in `array1` also modified the nested array in `array2` and vice-versa.

The solution to this problem is to create a **_deep copy_** of the array and there are a couple of ways to do this.

## 1. The JSON technique

The easiest way to create a deep copy of an array is by using a combination of `[**JSON.stringify()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)` and `[**JSON.parse()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)`.

`JSON.stringify()` converts a JavaScript value to a valid JSON string, while `JSON.parse()` converts a JSON string to a corresponding JavaScript value or object.

Here is a simple example:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-1.png)

> The JSON technique has some flaws especially when values other than strings, numbers and booleans are involved.

These flaws in the JSON technique can be majorly attributed to the manner in which the `JSON.stringify()` method converts values to JSON string.

Here is a simple demonstration of this flaw in trying to `**JSON.stringify()**` a value containing nested function.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-2.png)

## 2. Deep Copy Helper

A viable alternative to the JSON technique will be to implement your own **_deep copy helper function_** for cloning reference types whether they be arrays or objects.

Here is a very simple and minimalistic deep copy function called `**deepClone**`:

<script src="https://gist.github.com/gladchinda/75355e7f7992e800b5350c8c992df9b0.js"></script>

Now this is not the best of deep copy functions out there, like you will soon see with some JavaScript libraries — however, it performs deep copying to a pretty good extent.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-3.png)

## 3. Using JavaScript Libraries

The deep copy helper function we just defined is not robust enough in cloning all the kinds of JavaScript data that may be nested within complex objects or arrays.

JavaScript libraries like [**Lodash**](https://lodash.com/) and [**jQuery**](https://jquery.com/) provide more robust deep copy utility functions with support for different kinds of JavaScript data.

Here is an example that uses `**_.cloneDeep()**` from the Lodash library:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-4.png)

Here is the same example but using `**$.extend()**` from the jQuery library:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-5.png)

### Conclusion

In this article, we have been able to explore several techniques for dynamically creating new arrays and cloning already existing ones, including converting array-like objects and iterables to arrays.

We have also seen how some of the new features and enhancements introduced in ES6 can enable us to effectively perform certain manipulations on arrays.

We used features like destructuring and the spread operator for cloning and spreading arrays. You can learn more about destructuring from [this article](https://codeburst.io/es6-destructuring-the-complete-guide-7f842d08b98f).

#### Clap & Follow

If you found this article insightful, you are free to give some rounds of applause if you don’t mind.

You can also follow me on Medium ([Glad Chinda](https://www.freecodecamp.org/news/https-medium-com-gladchinda-hacks-for-creating-javascript-arrays-a1b80cb372b/undefined)) for more insightful articles you may find helpful. You can also follow me on Twitter ([@gladchinda](https://twitter.com/@gladchinda)).

**_Happy hacking…_**


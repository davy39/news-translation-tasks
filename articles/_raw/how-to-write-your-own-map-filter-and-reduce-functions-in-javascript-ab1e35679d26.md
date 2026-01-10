---
title: How to write your own map, filter and reduce functions in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-21T00:05:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-your-own-map-filter-and-reduce-functions-in-javascript-ab1e35679d26
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5PyeGXp9J3PpUTHCv9drnQ.jpeg
tags:
- name: ES6
  slug: es6
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Hemand Nair

  A sneak peek into functional programming and higher order functions in Javascript.


  _Photo by [Unsplash](https://unsplash.com/photos/pgSkeh0yl8o?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target=...'
---

By Hemand Nair

#### A sneak peek into functional programming and higher order functions in Javascript.

![Image](https://cdn-media-1.freecodecamp.org/images/8rPml1LfKKppm-gvbSSoKziPC-RHoF0CsVKg)
_Photo by [Unsplash](https://unsplash.com/photos/pgSkeh0yl8o?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Christopher Robin Ebbinghaus</a> on <a href="https://unsplash.com/search/photos/javascript?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Whenever I hear about functional programming, the first thing that comes into my mind is higher order functions. To the folks who don’t know about higher order functions, here’s what Wikipedia says:

A [**higher-order function**](https://en.wikipedia.org/wiki/Higher-order_function) is a function that does at least one of the following:

* Takes one or more functions as arguments,
* Returns a function as its result.

Higher order functions can be best described by the map, filter and reduce functions. Javascript by default has its own implementation of these functions. Today, we will be writing our own map, filter and reduce functions.

**Note: Keep in mind that these implementations of the map, filter and reduce methods might not reflect the native implementations of their Javascript counterparts.**

#### Map

From [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map):

> The `**map()**` method creates a new array with the results of calling a provided function on every element in the calling array.

Seems pretty straightforward. Now let’s see the Javascript `map()` in action!

```
let arr = [1, 2, 3, 4, 5];
```

```
// pass a function to mapconst squareArr = arr.map(num => num ** 2);
```

```
console.log(squareArr); // prints [1, 4, 9, 16, 25]
```

So what just happened? We wrote a function that returns the square of a number and passed that function as an argument to our `map()`. Let’s see step by step instructions on how to create our own map function.

1. Create an empty array `mapArr`.
2. Loop through array elements.
3. Call function `mapFunc` with the current element as the argument.
4. Push the result of the `mapFunc` function to the `mapArr` array.
5. Return the `mapArr` array after going through all the elements.

Now let’s write our implementation of the `map()`

```
// map takes an array and function as argumentfunction map(arr, mapFunc) {    const mapArr = []; // empty array        // loop though array    for(let i=0;i<arr.length;i++) {        const result = mapFunc(arr[i], i, arr);        mapArr.push(result);    }    return mapArr;}
```

Now if you call the new `map()` in the previous example code,

```
const squareArr2 = map(arr, num => num ** 2);
```

```
console.log(squareArr2); // prints [1, 4, 9, 16, 25]
```

Pretty cool huh? Let’s jump into `filter()` next.

#### **Filter**

From [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter):

> The `**filter()**` method creates a new array with all elements that pass the test implemented by the provided function.

Let’s see an example:

```
let arr = [1, 2, 3, 4, 5];
```

```
// pass a function to filterconst oddArr = arr.filter(num => num % 2 === 0);
```

```
console.log(oddArr); // prints [2, 4]
```

The filter function took a function which will return `true` if a number is even. The `filter()` “filters” the input array based on whether the element is true or false. Let’s go through step by step on how the `filter()` works.

1. Create an empty array `filterArr`.
2. Loop through the array elements.
3. Called the `filterFunc` function with the current element as the argument.
4. If the result is true, push the element to the `filterArr` array.
5. Return `filterArr` array after going through all the elements.

Time to write our own `filter()`

```
// filter takes an array and function as argumentfunction filter(arr, filterFunc) {    const filterArr = []; // empty array        // loop though array    for(let i=0;i<arr.length;i++) {        const result = filterFunc(arr[i], i, arr);        // push the current element if result is true        if(result)             filterArr.push(arr[i]);     }    return filterArr;}
```

Let’s see if our new `filter()` works out with the previous example:

```
const oddArr2 = filter(arr, num => num % 2 === 0);
```

```
console.log(oddArr2); //prints [2, 4]
```

Neat! I have saved the best and hardest one for the last. Let’s go to `reduce()` next.

#### **Reduce**

From [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce):

> The `**reduce()**` method executes a **reducer** function (that you provide) on each member of the array resulting in a single output value.

Makes sense? No? Here’s an example to wrap your head around:

```
let arr = [1, 2, 3, 4];const sumReducer = (accumulator, currentValue) => accumulator + currentValue;
```

```
// 1 + 2 + 3 + 4const sum = arr.reduce(sumReducer);console.log(sum);// prints 10
```

```
// 5 + 1 + 2 + 3 + 4const sum2 = arr.reduce(sumReducer);console.log(sum2);// prints 15
```

Starting to get a picture? Let’s make it clear. Before digging too deep into the `reduce()` method, you might need to get acquainted with the reducer function.

If you have used [**redux**](https://redux.js.org) in the past, you might have some idea about what a reducer function is. In the example above, the reducer function is written as the sum between the accumulator and current value. When you pass the reducer function to the `reduce()` method, it will loop through each number in the array and adds it to the accumulator ( 0 at the beginning), which itself becomes the new accumulator for the next iteration. This continues till the end of the array and returns the accumulator as a result.

If I had to output the value of the accumulator in each step for the above example, it would be like this:

* Before the start of the iteration, `accumulator = 0`
* 1st iteration, `accumulator += 1; // accumulator = 1`
* 2nd iteration, `accumulator += 2; // accumulator = 3`
* 3rd iteration, `accumulator += 3; // accumulator = 6`
* 4th iteration, `accumulator += 4; // accumulator = 10`

Your **reducer** function’s returned value is assigned to the accumulator, whose value is remembered across each iteration throughout the array. It ultimately becomes the final, single resulting value.

If you are still stuck at some point, try writing some operations with the inbuilt `reduce()` method. Whenever you feel you are ready, go through the next steps on how to implement your custom `reduce()`:

1. Initialize `accumulator` variable with 0 or `initalValue` argument from the `reduce()`.
2. Loop through the array elements.
3. Call the `reducer` function with the `accumulator` and current element as the arguments.
4. Return `accumulator` after going through all the elements.

Alright, time to code.

```
// reducer takes an array, reducer() and initialValue as argumentfunction reduce(arr, reducer, initialValue) {    let accumulator = initialValue === undefined ? 0 : initialValue        // loop though array    for(let i=0;i<arr.length;i++)        accumulator = reducer(accumulator, arr[i], i, arr);    return accumulator;}
```

Well, that was easier than expected. Let’s see if it’s working.

```
const sum = reduce(arr, sumReducer);
```

```
console.log(sum); // prints 10
```

```
const sum2 = reduce(arr, sumReducer, 5);
```

```
console.log(sum2);// prints 15
```

Works like a charm!

**That’s it :)**

Comment down below if you have any questions.


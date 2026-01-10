---
title: How the JavaScript reduce and reduceRight Methods Work
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2022-05-13T16:10:35.000Z'
originalURL: https://freecodecamp.org/news/how-reduce-reduceright-works-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/reduce-cover-with-title-3.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "reduce and reduceRight are two built-in JavaScript array methods that have\
  \ a bit of a steep learning curve. \nBut the very essence of these methods are as\
  \ simple as the following arithmetic computations.\nSuppose we have an array of\
  \ numbers:\n[1, 2, 3, ..."
---

`reduce` and `reduceRight` are two built-in JavaScript array methods that have a bit of a steep learning curve. 

But the very essence of these methods are as simple as the following arithmetic computations.

Suppose we have an array of numbers:

```js
[1, 2, 3, 4]
```

And we want to get the sum of them.

The `reduce` way to get the sum is similar to:

<p style="text-align: center; font-size: 1.2em">((((1) + 2) + 3) + 4)</p>

Whereas the `reduceRight` way to get the sum is similar to:

<p style="text-align: center; font-size: 1.2em">((((4) + 3) + 2) + 1)</p>

With `reduce` and `reduceRight`, you can define your own +. Array elements can be anything too. Sounds exciting, right?

Think of `reduce` and `reduceRight` as nothing but a generalization of the above arithmetic patterns. In this article we will cover all the important details.

This article takes an easy-to-digest algorithmic approach to show you how reducing works in JavaScript. 

I've also created a video to show you how these methods work. Check it out if want to learn the concepts from a more visual angle:

%[https://youtu.be/o43livPsWn4]

## Table of Contents

<ul
  style="
    padding-left: 0px;
    padding-block: 0.5rem;
    list-style-type: none;
    margin: 0px;
  "
>
  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >1</span
    ><a href="#what-is-reduced-to-what">What is reduced to what? </a>
  </li>

  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >2</span
    ><a href="#parameters-of-reduce-reduceright"
      >Parameters of <code>reduce</code>/<code>reduceRight</code>
    </a>
  </li>

  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >3</span
    ><a href="#understanding-reduce-reduceright-with-a-diagram"
      >Understanding <code>reduce</code>/<code>reduceRight</code> with a diagram
    </a>
  </li>

  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >4</span
    ><a href="#the-algorithm-of-reduce-reduceright"
      >The algorithm of <code>reduce</code>/<code>reduceRight</code>
    </a>
  </li>

  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >5</span
    ><a href="#excercises">Excercises </a>

    <ul style="padding-left: 1.3em; list-style-type: none">
      <li>
        <span
          style="
            margin-right: 0.6rem;
            color: rgb(102, 166, 46);
            font-weight: bold;
          "
          >5.1</span
        ><a href="#flat-nested-array">Flat nested array </a>
      </li>

      <li>
        <span
          style="
            margin-right: 0.6rem;
            color: rgb(102, 166, 46);
            font-weight: bold;
          "
          >5.2</span
        ><a href="#remove-duplicate-items-from-an-array"
          >Remove duplicate items from an array
        </a>
      </li>

      <li>
        <span
          style="
            margin-right: 0.6rem;
            color: rgb(102, 166, 46);
            font-weight: bold;
          "
          >5.3</span
        ><a href="#reverse-an-array-without-mutating-it"
          >Reverse an array without mutating it
        </a>
      </li>
    </ul>
  </li>

  <li>
    <span
      style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold"
      >6</span
    ><a href="#conclusion">Conclusion </a>
  </li>
</ul>


<h2 id="what-is-reduced-to-what"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1</span>What is reduced to what?
<a href="#what-is-reduced-to-what" aria-label="Anchor link for: &quot;What is reduced to what?
&quot;" style="text-decoration: none;">§</a></h2>

You might be wondering, "What kind of reduction happens when using `reduce` or `reduceRight`?"

Here, reduction reflects a particular way of transforming (which we will see in detail) the elements in an array to a single value similar to the arithmetic computations we have seen above. 

But note that the output value can be anything. So it can be a value that looks bigger than the original array on which the method is called.

In _functional programming_ languages, the idea of reducing has many [other names](https://en.wikipedia.org/wiki/Fold_(higher-order_function)) such as **fold**, **accumulate**, **aggregate**, **compress** and even **inject**.

<h2 id="parameters-of-reduce-reduceright"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2</span>Parameters of <code>reduce</code>/<code>reduceRight</code>
<a href="#parameters-of-reduce-reduceright" aria-label="Anchor link for: &quot;Parameters of reduce/reduceRight
&quot;" style="text-decoration: none;">§</a></h2>

These methods both have the same rules for calling them. So it's easy to learn them together. Let's see how they can be called:

```js
let myArray      = [/* an array */];
let callbackfn   = /* A function value */ ;
let initialvalue = /* any value */ ;

myArray.reduce(callbackfn)
myArray.reduce(callbackfn, initialValue)

myArray.reduceRight(callbackfn)
myArray.reduceRight(callbackfn, initialValue)

```

Here the usage of the parameters of `reduce`/`reduceRight` is explained through the `callbackfn` and `initialValue` variables:

**`callbackfn`**: It must be a function. While iterating over the array, for each element, `reduce`/`reduceRight` calls `callbackfn` with 4 arguments. Let's assume the variables `previousValue`, `currentElement`, `index` and `array` hold the values of those arguments, respectively. So the internal call to `callbackfn` looks like this:

```js
callbackfn(previousValue, currentElement, index, array)

```

Now let's see the meaning of those values:

1. `previousValue`: This is also known as the _accumulator_. Long story short, this value represents the "work in progress" of the return value of the method. What this value is made up of will become completely clear when you study the algorithm presented later in this article.
2. `currentElement`: The current element.
3. `index`: The index of the current element.
4. `array`: `myArray`.

**Return value of `callbackfn`**: For the last call to `callbackfn`, its return value becomes the return value of `reduce`/`reduceRight`. Otherwise, its return value will be given as `previousValue` for the next call to `callbackfn`.

And finally, **`initialValue`**: This is an optional initial value for `previousValue` (the accumulator). If it's given, and `myArray` has some elements in it, the first call to `callbackfn` will receive this value as its `previousValue`.

**Note**: The `callbackfn` is usually called a **reducer function**(or just **reducer** for short).

<h2 id="understanding-reduce-reduceright-with-a-diagram"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">3</span>Understanding <code>reduce</code>/<code>reduceRight</code> with a diagram
<a href="#understanding-reduce-reduceright-with-a-diagram" aria-label="Anchor link for: &quot;Understanding reduce/reduceRight with a diagram
&quot;" style="text-decoration: none;">§</a></h2>

The only difference between `reduce` and `reduceRight` is the direction of the iteration. `reduce` iterates over the array elements left to right. And `reduceRight` iterates over the elements right to left.

Let's see how you can use `reduce`/`reduceRight` to join an array of strings. Note how the final output is reached by joining the array elements step by step in both directions:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/reduce-diagram1-1.png)
_A diagram showing the differences between `reduce` and `reduceRight`_

Here note that:

* `acc` is used to access `previousValue` .
* `curVal` is used to access `currentElement`.
* The circular shaped input to _**`r`**_ represents `curVal`.
* The rectangular shaped input to _**`r`**_ represents `acc` or the accumulator.
* Initial values are in rectangular shapes, because they are received by `**_r_**` as `acc`s.

<h2 id="the-algorithm-of-reduce-reduceright"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">4</span>The algorithm of <code>reduce</code>/<code>reduceRight</code>
<a href="#the-algorithm-of-reduce-reduceright" aria-label="Anchor link for: &quot;The algorithm of reduce/reduceRight
&quot;" style="text-decoration: none;">§</a></h2>

The 29 line algorithm below might look intimidating at first glance. But you'll likely find it much easier to understand it than digesting globs of long sentences explaining the intricate details of these methods.

**Note**: The algorithm described here has the context of the "[Parameters of reduce/reduceRight](https://www.freecodecamp.org/news/how-reduce-reduceright-works-javascript/#parameters-of-reduce-reduceright)" section. (That is, the variables `myArray`, `callbackfn` and `initialValue` come from that section.)

So relax, enjoy the steps, and don't forget to experiment in the console:

<div style="position: relative; margin-left: 40px; margin-bottom: 20px;"><ul style="padding: 0px; margin-block: 0px;"><div style="border-left: 1px solid lightgray; position: absolute; height: 100%;"></div><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">1</div>If <code>initialValue</code> is present,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">2</div>If <code>myArray</code> has no elements, <ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">3</div>Return <code>initialValue</code>.</li></ul></li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">4</div>Else <ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">5</div>Let <code>accumulator</code> be <code>initialValue</code>.</li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">6</div>If the method is <code>reduce</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">7</div>Let <code>startIndex</code> be the index of the leftmost element of <code>myArray</code>.</li></ul></li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">8</div>If the method is <code>reduceRight</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">9</div>Let <code>startIndex</code> be the index of the rightmost element of <code>myArray</code>.</li></ul></li></ul></li></ul></li><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">10</div>Else<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">11</div>If <code>myArray</code> has no elements, <ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">12</div>Throw <code>TypeError</code>.</li></ul></li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">13</div>Else if <code>myArray</code> has just only one element, <ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">14</div>Return that element.</li></ul></li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">15</div>Else<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">16</div>If the method is <code>reduce</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">17</div>Let <code>accumulator</code> be the leftmost element of <code>myArray</code>.</li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">18</div>Let <code>startIndex</code> be the index of the element that comes right after the leftmost element of <code>myArray</code>.</li></ul></li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">19</div>If the method is <code>reduceRight</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">20</div>Let <code>accumulator</code> be the rightmost element of <code>myArray</code>.</li><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">21</div>Let <code>startIndex</code> be the index of the element that comes right before the rightmost element of <code>myArray</code>.</li></ul></li></ul></li></ul></li><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">22</div>&nbsp;</li><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">23</div>If the method is <code>reduce</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">24</div>In left to right order, for each element of <code>myArray</code> such that it's index <code>i</code> ≥ <code>startingIndex</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">25</div>Set <code>accumulator</code> to <code>callbackfn(accumulator, myArray[i], i, myArray)</code>. </li></ul></li></ul></li><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">26</div>If the method is <code>reduceRight</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">27</div>In right to left order, for each element of <code>myArray</code> such that it's index <code>i</code> ≤ <code>startingIndex</code>,<ul style="border-left: 1px dashed blue; margin-left: 5px; margin-block: 0px; padding-left: 20px;"><li style="list-style-type: none; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">28</div>Set <code>accumulator</code> to <code>callbackfn(accumulator, myArray[i], i, myArray)</code>. </li></ul></li></ul></li><li style="list-style-type: none; padding-left: 10px; margin-block: 0px;"><div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div><div style="font-style: italic; font-weight: bold; position: absolute; left: -36px; width: 30px; text-align: right; user-select: none;">29</div>Return <code>accumulator</code>.<div style="border-top: 1px solid lightgray; position: absolute; left: -36px; width: calc(100% + 40px);"></div></li></ul></div>

**Note**: An array can have a length greater than `0` but no elements. Such empty places in the array are usually called _holes_ in the array. For example:

```js
let arr = [,,,,];
console.log(arr.length);
// 4

// note that trailing comma doesn't increase the length.
// This feature enables us to add a new element quickly.

```

These methods only call `callbackfn` for elements of `myArray` which actually exist. For example if you have an array like `[1,,3,,5]`, they will not consider the non-existing elements at indices `1` and `3`. Try to guess what will be logged after running the following:

```js
[,,,3,,,4].reduce((_, cv, i) => {
  console.log(i);
});
```

If you said `6`, you are right!

⚠️ **Warning**: It is not recommended to modify `myArray` inside of `callbackfn` because it complicates the logic of your code and thus increases the possibility of bugs.

If you've read and understood this far, congratulations! Now you should have a solid understanding of how `reduce`/`reduceRight` works. 

It's a great time to solve some problems to get used to `reduce`/`reduceRight`. Before seeing the solutions, solve them yourself or at least spend some time thinking about it.

<h2 id="excercises"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">5</span>Excercises
<a href="#excercises" aria-label="Anchor link for: &quot;Excercises
&quot;" style="text-decoration: none;">§</a></h2>

<h3 id="flat-nested-array"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">5.1</span>Flat nested array
<a href="#flat-nested-array" aria-label="Anchor link for: &quot;Flat nested array
&quot;" style="text-decoration: none;">§</a></h3>

Write a function `flatten` that can flat a nested array.

```js
let arr = [1, [2, [3], [[4], 5], 6]];
console.log(flatten(arr));
// [1, 2, 3, 4, 5, 6]

```

<details  style="align-self: flex-start; margin: 0 0 1.5em; width: 100%;">
  <summary>
    <b>Solution</b>
  </summary>
  <pre style="min-width: 0;" class="language-js">
    <code class=" language-js">
const flatten = (arr) => 
  arr.reduce((acc, curVal) =>
    acc.concat(Array.isArray(curVal) ? flatten(curVal) : curVal), []);
    </code>
  </pre>
</details>


<h3 id="remove-duplicate-items-from-an-array"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">5.2</span>Remove duplicate items from an array
<a href="#remove-duplicate-items-from-an-array" aria-label="Anchor link for: &quot;Remove duplicate items from an array
&quot;" style="text-decoration: none;">§</a></h3>

Write a function `rmDuplicates` that removes the duplicate items like below:

```js
console.log(rmDuplicates([1, 2, 2, 3, 4, 4, 4]));
// [1, 2, 3, 4]
```

<details style="align-self: flex-start; margin: 0 0 1.5em; width: 100%;">
  <summary>
    <b>Solution</b>
  </summary>
  <pre style="min-width: 0;" class="language-js">
    <code class=" language-js">
const rmDuplicates = arr => 
  arr.reduce((p, c) => p.includes(c) ? p : p.concat(c), []);
    </code>
  </pre>
</details>


<h3 id="reverse-an-array-without-mutating-it"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">5.3</span>Reverse an array without mutating it
<a href="#reverse-an-array-without-mutating-it" aria-label="Anchor link for: &quot;Reverse an array without mutating it
&quot;" style="text-decoration: none;">§</a></h3>

There is a built-in `reverse` array method to reverse arrays. But it mutates the original array. Use `reduceRight` to reverse an array without mutating it.

<details style="align-self: flex-start; margin: 0 0 1.5em; width: 100%;">
  <summary>
    <b>Solution</b>
  </summary>
  <pre style="min-width: 0;" class="language-js">
    <code class=" language-js">
let arr = [1, 2, 3];

let reversedArr = arr.reduceRight((acc, curVal) => [...acc, curVal], []);

console.log(arr);
// [1, 2, 3]

console.log(reversedArr);
// [3, 2, 1]
    </code>
  </pre>
  <p>
    Note that by reversing array this way you will lose all the holes in the
    array.
  </p>
</details>


<h2 id="conclusion"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">6</span>Conclusion
<a href="#conclusion" aria-label="Anchor link for: &quot;Conclusion
&quot;" style="text-decoration: none;">§</a></h2>

When `reduce`/`reduceRight` calls `callbackfn` internally we can call those patterns of calling it "normal behaviors" and we can treat other scenarios as edge cases. These can be summarized in the table below:

Initial value | Number of elements | Output
--- | --- | --- 
Present | 0 | **Edge case**: Initial value
Present | Greater than 0 | **Normal behavior** 
Absent | 0 | **Edge case**: TypeError
Absent | 1 | **Edge case**: That element
Absent | Greater than 1 | **Normal behavior** 

Learning `reduce`/`reduceRight` is a little bit more involved than other higher order array methods. But it's worth your time to learn it well. 

Thank you for reading! I hope this article was helpful. If you want you can checkout my [website](https://www.ashutoshbiswas.dev/) and follow me on [Twitter](https://twitter.com/ashutoshbw) and [LinkedIn](https://www.linkedin.com/in/ashutosh-biswas/).

Happy reducing 😃


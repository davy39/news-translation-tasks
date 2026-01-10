---
title: JavaScript Array Methods – How to Use every() and some() in JS
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2022-08-10T15:23:43.000Z'
originalURL: https://freecodecamp.org/news/learn-the-every-and-some-array-methods-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-1.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, every and some help you test if something is true for every
  element or some elements of an array.

  In this article, I''ll show you how to use these helpful array methods.


  Table of Contents1How every() and some() Work – an Overview2Param...'
---

In JavaScript, `every` and `some` help you test if something is true for every element or some elements of an array.

In this article, I'll show you how to use these helpful array methods.

<!--
Generator: https://ashutoshbw.github.io/ftg/

## How `every()` and `some()` Work – an Overview
## Parameters of `every` and `some`
### `predicate`
### Optional `thisArg`
## Edge cases for `every` and `some`
### What happens when `every` and `some` is called on an empty array?
### Non-existing elements are ignored
### Mutating the array in the predicate
## A challenge for you
-->
<div style="margin-bottom: 20px; font-size: 19px; font-family: Lato, sans-serif;"><h2 style="margin-bottom: 0px; margin-top: 20px; font-weight: normal; line-height: 50px;">Table of Contents</h2><ul style="padding-left: 10px; padding-block: 8px; list-style-type: none; margin: 0px; border-block: 1px solid gray;"><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">1</span><a href="#how-every-and-some-work-–-an-overview">How <code>every()</code> and <code>some()</code> Work – an Overview</a></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2</span><a href="#parameters-of-every-and-some">Parameters of <code>every</code> and <code>some</code></a><ul style="list-style-type: none; margin: 0px; padding-left: 19.0243px;"><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2.1</span><a href="#predicate"><code>predicate</code></a></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2.2</span><a href="#optional-thisarg">Optional <code>thisArg</code></a></li></ul></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3</span><a href="#edge-cases-for-every-and-some">Edge cases for <code>every</code> and <code>some</code></a><ul style="list-style-type: none; margin: 0px; padding-left: 19.0243px;"><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.1</span><a href="#what-happens-when-every-and-some-is-called-on-an-empty-array">What happens when <code>every</code> and <code>some</code> is called on an empty array?</a></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.2</span><a href="#non-existing-elements-are-ignored">Non-existing elements are ignored</a></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.3</span><a href="#mutating-the-array-in-the-predicate">Mutating the array in the predicate</a></li></ul></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">4</span><a href="#a-challenge-for-you">A challenge for you</a></li></ul><span style="font-size: 9px; float: right; line-height: 12px;"><a href="https://ashutoshbw.github.io/ftg/" target="_blank">Made with FTG</a></span></div>



<h2 id="how-every-and-some-work-–-an-overview"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">1</span>How <code>every()</code> and <code>some()</code> Work – an Overview<a href="#how-every-and-some-work-–-an-overview" aria-label="Anchor link for: &quot;How every() and some() Work – an Overview&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h2>

First we need some data to test. For simplicity let's consider an array of numbers:

```js
const nums = [34, 2, 48, 91, 12, 32];
```

Now let's say we want to test if every number in the array is less than `100`. Using `every` we can easily test it like below:

```js
nums.every(n => n < 100);
// true
```

Short and sweet! You can think about what happens here like this:

- `every` loops over the array elements left to right.
  - For each iteration, it calls the given function with the current array element as its 1st argument. 
  - The loop continues until the function returns a **[falsy value](https://www.ashutoshbiswas.dev/blog/truthy-and-falsy/)**. And in that case `every` returns `false` – otherwise it returns `true`.


`some` also works very similarly to `every`:
- `some` loops over the array elements left to right.
  - For each iteration, it calls the given function with the current array element as its 1st argument. 
  - The loop continues until the function returns a **[truthy value](https://www.ashutoshbiswas.dev/blog/truthy-and-falsy/)**. And in that case `some` returns `true` – otherwise it returns `false`.

Now let's use `some` to test if some number in the array is odd:

```js
nums.some(n => n % 2 == 1);
// true
```

That's really true! `91` is odd.

But this is not the end of the story. These methods have some more depth. Let's dig in.

<h2 id="parameters-of-every-and-some"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2</span>Parameters of <code>every</code> and <code>some</code><a href="#parameters-of-every-and-some" aria-label="Anchor link for: &quot;Parameters of every and some&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h2>

The way to use `every` and `some` array methods is exactly the same. They have the same set of parameters and those parameters also mean identical things. So it's very easy to learn them at once.  

We have already worked with first parameter of these methods which is a function. We call this function _predicate_.

> In computer science, a **[predicate](https://www.baeldung.com/cs/predicates)** is a function of a set of parameters that returns a boolean as an answer. JavaScript treats the function we give to `every`/`some` as a _predicate_. We can return any type of value we wish, but those are treated as a Boolean, so it's common to call this function a predicate.

They also have an optional 2nd parameter to control `this` inside of non-arrow predicates. We call it `thisArg`.

So you can call these methods in the following ways:

```javascript
arr.every(predicate)
arr.every(predicate, thisArg)

arr.some(predicate)
arr.some(predicate, thisArg)
```

Let's see the `predicate` and the optional `thisArg` in detail below. 

<h3 id="predicate"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2.1</span><code>predicate</code><a href="#predicate" aria-label="Anchor link for: &quot;predicate&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h3>

Through the `predicate`, `every`/`some` not only gives us access to the current array element but also its index and the original array through its parameters like below:

* **1st parameter**: The current array element.
* **2nd parameter**: The index of the current element.
* **3rd parameter**: The array itself on which `every`/`some` is called.

We have only seen the first parameter in action in earlier examples. Let's catch the index and the array by defining two more parameters. This time, let's say we have some T-Shirt data to test if all of them have `freeCodeCampe` logo:

```js
let tshirts = [
  { size: "S", color: "black", logo: "freeCodeCamp" },
  { size: "S", color: "white", logo: "freeCodeCamp" },
  { size: "S", color: "teal",  logo: "freeCodeCamp" },
  { size: "M", color: "black", logo: "freeCodeCamp" },
  { size: "M", color: "white", logo: "freeCodeCamp" },
  { size: "M", color: "teal",  logo: "freeCodeCamp" },
  { size: "L", color: "black", logo: "freeCodeCamp" },
  { size: "L", color: "white", logo: "freeCodeCamp" },
  { size: "L", color: "teal",  logo: "freeCodeCamp" },
];

tshirts.every((item, i, arr) => {
  console.log(i);
  console.log(arr);
  return item.logo == "freeCodeCamp";
})
```

Try this out in your console to see the output. And don't forget to play around with `some` too.

<h3 id="optional-thisarg"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2.2</span>Optional <code>thisArg</code><a href="#optional-thisarg" aria-label="Anchor link for: &quot;Optional thisArg&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h3>

If in any case you need to have a particular `this` value inside your predicate, you can set that with `thisArg`. Note that is only applicable for non-arrow predicates because arrow functions have no `this` bindings.

If you omit this argument, `this` inside the predicate (non-arrow function) works as usual, that is:

* In strict mode `this` is `undefined`.
* In sloppy mode `this` is the **global object** which is `window` in browser and `global` in Node.

I can't think of any good use case of `thisArg`. But I think it's good that it exists because now you have control over `this` inside your predicate. So even if someday there is a need for it you will know that there is a way.

 If you have any good ideas for uses of `thisArg`, please let me know on Twitter :)

<h2 id="edge-cases-for-every-and-some"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3</span>Edge cases for <code>every</code> and <code>some</code><a href="#edge-cases-for-every-and-some" aria-label="Anchor link for: &quot;Edge cases for every and some&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h2>

<h3 id="what-happens-when-every-and-some-is-called-on-an-empty-array"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.1</span>What happens when <code>every</code> and <code>some</code> is called on an empty array?<a href="#what-happens-when-every-and-some-is-called-on-an-empty-array" aria-label="Anchor link for: &quot;What happens when every and some is called on an empty array?&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h3>

Sometimes the array you want to test might be empty. For example, you fetched an array from an API and it can have an arbitrary number of elements at different times including zero.

For the case of `every` a `true` return value can mean two things:

* If the array has more than zero elements, then all elements of the array satisfies the predicate.
* The array has no elements.

So if we want we can do crazy things inside the predicate like below:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/wth-what-the-hell-is-going-on.gif)

```js
const myCatsBankAccounts = [];
myCatsBankAccounts.every(account => account.balance > elonMusk.totalWealth)

```

And still get `true` as the return value!

If the array is empty, JavaScript directly returns `true` without any calls to the predicate.

It's because in logic, you can say anything about the elements of an empty set and that is regarded as true or more precisely [vacuously true](https://en.wikipedia.org/wiki/Vacuous_truth). Such logic might seem nonsense in everyday usage but it's how logic works. Read the wiki page linked above to know more about it.

So if you get `true` as the the return value of `every` you should be aware that the array could be empty.

`some` on the other hand, directly returns `false` on empty arrays without any calls to `predicate` and without any weirdness.

<h3 id="non-existing-elements-are-ignored"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.2</span>Non-existing elements are ignored<a href="#non-existing-elements-are-ignored" aria-label="Anchor link for: &quot;Non-existing elements are ignored&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h3>

If your array has holes in it like below, they are ignored by `every`/`some`:

```js
const myUntiddyArry = [1,,,3,,42];
```

<h3 id="mutating-the-array-in-the-predicate"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.3</span>Mutating the array in the predicate<a href="#mutating-the-array-in-the-predicate" aria-label="Anchor link for: &quot;Mutating the array in the predicate&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h3>

I will not discuss this case here, because mutating the original array in most cases just complicates things and makes more room for bugs. 

If you really need to or are interested, please read the note in the [spec](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array.prototype.every) for details.

<h2 id="a-challenge-for-you"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">4</span>A challenge for you<a href="#a-challenge-for-you" aria-label="Anchor link for: &quot;A challenge for you&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h2>

Express `every` with `some` and `some` with `every` in JavaScript.

I hope you will also feel the immense joy and wonder that I got when I discovered this relationship!

<details style="align-self: flex-start; margin: 1.5em 0 1.5em; width: 100%;">
  <summary>Solution</summary>
<p>Let's do it step by step. First let's try to express <code>every</code> with <code>some</code>:</p>
<ul>
<li>For every element of the array, the predicate is true.</li>
<li>It's not true that for some elements of the array the predicate is not true.</li>
</ul>
<p>We can translate that into JavaScript like below:</p>
<pre style="min-width:0">const myEvery = (arr, predicate) =&gt; !arr.some(e =&gt; !predicate(e));
</pre>
<p>Now let's express <code>some</code> with <code>every</code>. It's almost the same as before. Just <code>some</code> is replaced by <code>every</code>. Try to understand what is going on:</p>
<ul>
<li>For some elements of the array, the predicate is true.</li>
<li>It's not true that for every element of the array the predicate is not true.</li>
</ul>
<p>In JavaScript:</p>
<pre style="min-width:0">const mySome = (arr, predicate) =&gt; !arr.every(e =&gt; !predicate(e));
</pre>
<p>Note that the above implementations also work when <code>arr</code> is empty. And for simplicity, I've excluded other parameters of the <code>predicate</code> and <code>thisArg</code>. Try to add these details yourself, if you are interested. In this process, you might learn one or a few things!</p>
</details>

Thanks for reading! I hope this article was helpful. Check out my other articles [here](https://www.freecodecamp.org/news/author/ashutoshbw/). Let's connect on [Twitter](https://twitter.com/ashutoshbw).


---
title: What’s new in JavaScript ES2019
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T17:20:45.000Z'
originalURL: https://freecodecamp.org/news/whats-new-in-javascript-es2019-8af4390d8494
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eK0RbuEJK9WzmA272g41Qg.png
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
seo_desc: 'By Vali Shah

  Many of us know that there is a standard procedure for Javascript’s latest releases
  and a committee behind that. In this post, I will explain about who makes the final
  call on any new specification, what is the procedure for it, and what...'
---

By Vali Shah

Many of us know that there is a standard procedure for Javascript’s latest releases and a committee behind that. In this post, I will explain about who makes the final call on any new specification, what is the procedure for it, and what's new in **ES2019.**

The language specification that drives JavaScript is called **ECMAScript.** There is a team behind that called Technical Committee 39 **[TC39]** that reviews every specification before adopting**.**

Every change goes through a process with stages of maturity.

* **Stage 0:** Ideas/Strawman
* **Stage 1:** Proposals
* **Stage 2:** Drafts
* **Stage 3:** Candidates
* **Stage 4:** Finished/Approved

A feature which reaches **Stage 4** will most likely be part of the language specification.

Let's dive into the things which are added newly into the specification under ES2019.

#### Array.prototype.{flat,flatMap}

`Array.prototype.flat()` proposed to flatten arrays recursively up to the specified `depth` and returns a new array.

**Syntax**: `Array.prototype.flat(depth)`   
**depth —** Default value **1**, Use `Infinity` to flatten all nested arrays.

```js
const numbers = [1, 2, [3, 4, [5, 6]]];
// Considers default depth of 1
numbers.flat(); 
> [1, 2, 3, 4, [5, 6]]
// With depth of 2
numbers.flat(2); 
> [1, 2, 3, 4, 5, 6]
// Executes two flat operations
numbers.flat().flat(); 
> [1, 2, 3, 4, 5, 6]
// Flattens recursively until the array contains no nested arrays
numbers.flat(Infinity)
> [1, 2, 3, 4, 5, 6]
```

`Array.prototype.flatMap()` maps each element using a mapping function and flattens the result into a new array. It’s identical to the map operation followed by a `flat` of `depth` **1.**

**Syntax:** `Array.prototype.flatMap(callback)`   
**callback:** `function` that produces an element of the new Array.

```js
const numbers = [1, 2, 3];
numbers.map(x => [x * 2]);
> [[2], [4], [6]]
numbers.flatMap(x => [x * 2]);
> [2, 4, 6]
```

#### Object.fromEntries

`Object.fromEntries` performs the reverse of `Object.entries` . It transforms a list of key-value pairs into an object.

**Syntax:** `Object.fromEntries(iterable)`   
**iterable:** An iterable like `Array` or `Map` or objects implementing the [iterable protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterable_protocol)

```js
const records = [['name','Mathew'], ['age', 32]];
const obj = Object.fromEntries(records);
> { name: 'Mathew', age: 32}
Object.entries(obj);
> [['name','Mathew'], ['age', 32]];
```

#### String.prototype.{trimStart, trimEnd}

`trimStart()` removes whitespace from the beginning of a string and `trimEnd()` removes whitespace from the end of a string.

```js
const greeting = ` Hello Javascript! `;
greeting.length;
> 19
greeting = greeting.trimStart();
> 'Hello Javascript! '
greeting.length;
> 18
greeting = 'Hello World!   ';
greeting.length;
> 15
greeting = greeting.trimEnd();
> 'Hello World!'
greeting.length;
> 12
```

#### Optional Catch Binding

Prior to the new specification, it was required to have an exception variable bind to a `catch` clause. ES2019 made it optional.

```js
// Before
try {
   ...
} catch(error) {
   ...
}
// After
try {
   ...
} catch {
   ...
}
```

This feature is useful when you want to completely ignore the error. **Best practice is to consider handling an error.**

There are cases where you know the possible error that could trigger on operations. You can ignore the catch block handling.

#### JSON ⊂ ECMAScript

The line separator (U+2028) and paragraph separator (U+2029) symbols are now allowed in string literals. Previously, these were treated as line terminators and resulted in `SyntaxError` exceptions.

```js
// Produces invalid string before ES2019
eval('"\u2028"');
// Valid in ES2019
eval('"\u2028"');
```

#### Well-formed JSON.stringify

Instead of unpaired surrogate code points resulting in single **UTF-16** code units, ES10 represents them with JSON escape sequences.

```js
JSON.stringify('\uD800');
> '"�"'
JSON.stringify('\uD800');
> '"\\ud800"'
```

#### Function.prototype.toString

`.toString()` now returns exact slices of source code text, including whitespaces and comments.

```js
function /* a comment */ foo () {}
// Previously:
foo.toString();
> 'function foo() {}'
             ^ no comment
                ^ no space
// Now:
foo.toString();
> 'function /* comment */ foo () {}'
```

#### Symbol.prototype.description

Read-only property that returns the optional description of a `Symbol` Object:

```js
Symbol('desc').toString();
> "Symbol(desc)"
Symbol('desc').description;  
> "desc"
Symbol('').description;      
> ""
Symbol().description;
> undefined
```

### Conclusion

**TC39** keeps all the upcoming specifications which are in stage >1 of the proce[ss h](https://github.com/tc39/proposals)ere. As [a develo](https://www.microverse.org/)per, It's important to keep tabs on what's happening around. There are many more exciting things coming up li**ke static & private methods and fields in classes, Legacy RegE**x, etc. Find out all the new things which are in the proposal sta[ge h](https://github.com/tc39/proposals)ere.

`**code** = **co**ffee + **de**veloper`

Here are a few more interesting topics:

* [**A quick overview of JavaScript Symbols**](https://medium.freecodecamp.org/how-did-i-miss-javascript-symbols-c1f1c0e1874a)
* [**How to adopt a git branching strategy**](https://medium.freecodecamp.org/adopt-a-git-branching-strategy-ac729ff4f838)
* [**An Introduction to Git Merge and Git Rebase: What They Do and When to Use Them**](https://medium.freecodecamp.org/an-introduction-to-git-merge-and-rebase-what-they-are-and-how-to-use-them-131b863785f)


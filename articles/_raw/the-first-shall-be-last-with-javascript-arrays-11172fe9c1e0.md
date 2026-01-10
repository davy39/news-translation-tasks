---
title: The first shall be last with JavaScript arrays
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-28T15:44:06.000Z'
originalURL: https://freecodecamp.org/news/the-first-shall-be-last-with-javascript-arrays-11172fe9c1e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qpeU4geKupip-i6jxgxF9Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Thomas Barrasso


  So the last shall be [0], and the first [length — 1].

  – Adapted from Matthew 20:16


  I’ll skip the Malthusian Catastrophe and get to it: arrays are one of the simplest
  and most important data structures. While terminal elements (fi...'
---

By Thomas Barrasso

> So the last shall be `[0]`, and the first [length — 1].

> – Adapted from [Matthew 20:16](https://www.biblegateway.com/passage/?search=Matthew+20%3A16&version=KJV)

I’ll skip the Malthusian Catastrophe and get to it: arrays are one of the simplest and most important data structures. While terminal elements (first and last) are frequently accessed, Javascript provides no convenient property or method for doing so and using indices can be redundant and prone to side effects and [off-by-one errors](https://en.wikipedia.org/wiki/Off-by-one_error).

A lesser-known, [recent JavaScript TC39 Proposal](https://github.com/keithamus/proposal-array-last) offers solace in the form of two “new” properties: `Array.lastItem` & `Array.lastIndex`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*76m-CxmcYIqWbOpln0Za8g.png)
_[Jeff Atwood @codinghorror](https://twitter.com/codinghorror/status/506010907021828096?lang=en" rel="noopener" target="_blank" title=")_

### **Javascript Arrays**

In many programming languages including Javascript, arrays are zero-indexed. The terminal elements–first and last– are accessed via the `[0]` and `[length — 1]` indices, respectively. We owe this pleasure to a [precedent set by C](https://medium.com/@albertkoz/why-does-array-start-with-index-0-65ffc07cbce8), where an index represents an offset from the head of an array. That makes zero the first index because it _is_ the array head. Also Dijkstra proclaimed “[zero as a most natural number.](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html)” So let it be written. So let it be done.

I suspect if you averaged access by index you would find that terminal elements are referenced most often. After all, arrays are commonly used to store a sorted collection and doing so places superlative elements (highest, lowest, oldest, newest, etc.) at the ends.

Unlike other scripting languages (say [PHP](https://secure.php.net/manual/en/function.end.php) or [Elixir](https://hexdocs.pm/elixir/List.html#last/1)), Javascript does not provide convenient access to terminal array elements. Consider a trivial example of swapping the last elements in two arrays:

```
let faces = ["?", "?", "?", "?", "?"];let animals = ["?", "?", "?", "?", "?"];  
```

```
let lastAnimal = animals[animals.length - 1];animals[animals.length - 1] = faces[faces.length - 1];faces[faces.length - 1] = lastAnimal;
```

The swapping logic requires 2 arrays referenced 8 times in 3 lines! In real-world code, this can quickly become very repetitive and difficult for a human to parse (though it is perfectly readable for a machine).

What’s more, solely using indices, you cannot define an array and get the last element in the same expression. That might not seem important, but consider another example where the function, `getLogins()`, makes an asynchronous API call and returns a sorted array. Assuming we want the most recent login event at the end of the array:

```
let lastLogin = async () => {  let logins = await getLogins();  return logins[logins.length - 1];};
```

Unless the length is fixed and known in advance, we _have_ to assign the array to a local variable to access the last element. One common way to address this in languages like [Python](http://knowledgehills.com/python/negative-indexing-slicing-stepping-comparing-lists.htm) and [Ruby](http://rubyquicktips.com/post/996814716/use-negative-array-indices) is to use negative indices. Then `[length - 1]` can be shortened to `[-1]`, removing the need for local reference.

I find `-1` only marginally more readable than `length — 1`, and while it is possible to approximate [negative array indices in Javascript](https://h3manth.com/new/blog/2013/negative-array-index-in-javascript/) with [ES6 Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) or `Array.slice(-1)[0]`, both come with [significant performance implications](https://jsperf.com/last-array-element2/14) for what should otherwise constitute simple random access.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tv90DqFJ1xOyUhbtmm4UXw.png)

#### **Underscore & Lodash**

One of the most well-known principles in software development is Don’t Repeat Yourself (DRY). Since accessing terminal elements is so common, why not write a helper function to do it? Fortunately, many libraries like [Underscore](https://underscorejs.org/) and [Lodash](https://lodash.com/) already provide utilities for `_.first` & `_.last`.

This offers a big improvement in the `lastLogin()` example above:

```
let lastLogin = async () => _.last(await getLogins());
```

But when it comes to the example of swapping last elements, the improvement is less significant:

```
let faces = ["?", "?", "?", "?", "?"];let animals = ["?", "?", "?", "?", "?"];  
```

```
let lastAnimal = _.last(animals);animals[animals.length - 1] = _.last(faces);faces[faces.length - 1] = lastAnimal;
```

These utility functions removed 2 of the 8 references, only now we introduced an external dependency that, oddly enough, does not include a function for _setting_ terminal elements.

Most likely such a function is deliberately excluded because its API would be confusing and hard to readable. Early versions of Lodash provided a method `[_.last(array, n)](https://github.com/lodash/lodash/issues/946)` where _n_ was the number of items from the end but it was ultimately removed in favor of `[_.take](https://lodash.com/docs#take)(array, n)`.

Assuming `nums` is an array of numbers, what would be the expected behavior of `_.last(nums, n)`? It could return the last two elements like `_.take`, or it could set the value of the last element equal to _n_.

If we were to write a function for setting the last element in an array, there are only a few approaches to consider using pure functions, method chaining, or using prototype:

```
let nums = ['d', 'e', 'v', 'e', 'l']; // set first = last
```

```
_.first(faces, _.last(faces));        // Lodash style
```

```
$(faces).first($(faces).last());      // jQuery style
```

```
faces.first(faces.last());            // prototype
```

I do not find any of these approaches to be much of an improvement. In fact, something important is lost here. Each performs an assignment, but none use the assignment operator (`=`).This could be made more apparent with naming conventions like `getLast` and `setFirst`, but that quickly becomes overly verbose. Not to mention the [fifth circle of hell](https://blog.toggl.com/seven-levels-developer-hell/) is full of programmers forced to navigate “self-documenting” legacy code where the only way to access or modify data is through getters and setters.

Somehow, it looks like we are stuck with `[0]` & `[length — 1]`…

Or are we? ?

#### **The Proposal**

As mentioned, an ECMAScript Technical Candidate (TC39) proposal attempts to address this problem by defining two new properties on the `Array` object: `lastItem` & `lastIndex`. This proposal is [already supported](https://kangax.github.io/compat-table/esnext/) in [core-js 3](https://github.com/zloirock/core-js) and usable today in Babel 7 & TypeScript. Even if you are not using a transpiler, this proposal includes a [polyfill](https://github.com/keithamus/proposal-array-last#polyfill).

Personally, I do not find much value in `lastIndex` and prefer Ruby’s shorter naming for `[first](https://stackoverflow.com/questions/18212240/ruby-convention-for-accessing-first-last-element-in-array)` [and `last`](https://stackoverflow.com/questions/18212240/ruby-convention-for-accessing-first-last-element-in-array), although this was ruled out because of [potential web compatibility issues](https://github.com/keithamus/proposal-array-last/issues/4). I am also surprised that this proposal does not suggest a `firstItem` property for consistency and symmetry.

In the interim, I can offer a no-dependency, Ruby-esque approach in ES6:

#### **First & Last**

We now have two new Array properties–`first` & `last`–and a solution that:

✓ Uses the assignment operator

✓ Does not clone the array

✓ Can define an array and get a terminal element in one expression

✓ Is human-readable

✓ Provides one interface for getting & setting

We can rewrite `lastLogin()` again in a single line:

```
let lastLogin = async () => (await getLogins()).last;
```

But the real win comes when we swap the last elements in two arrays with half the number of references:

```
let faces = ["?", "?", "?", "?", "?"];let animals = ["?", "?", "?", "?", "?"];  
```

```
let lastAnimal = animals.last;animals.last = faces.last;faces.last = lastAnimal;
```

Everything is perfect and we have solved one of CS’ most difficult problems. There are no evil covenants hiding in this approach…

#### **Prototype Paranoia**

> Surely there is no one [programmer] on earth so righteous as to do good without ever sinning.– Adapted from [Ecclesiastes 7:20](https://www.biblegateway.com/passage/?search=Ecclesiastes+7%3A20&version=NRSVA)

Many consider [extending a native Object’s prototype an anti-pattern](https://we-are.bookmyshow.com/prototype-pattern-in-js-5c1f44440081) and a crime punishable by 100 years of programming in Java. Prior to the introduction of the `[enumerable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Enumerability_and_ownership_of_properties)` property, [extending `Object.prototype`](https://javascriptweblog.wordpress.com/2011/12/05/extending-javascript-natives/) could change the behavior of `for in` loops. It could also lead to conflict between various libraries, frameworks, and third-party dependencies.

Perhaps the most insidious issue is that, without compile-time tools, a simple spelling mistake could [inadvertently create an associative array](https://nemisj.com/why-getterssetters-is-a-bad-idea-in-javascript/).

```
let faces = ["?", "?", "?", "?", "?"];let ln = faces.length  
```

```
faces.lst = "?"; // (5) ["?", "?", "?", "?", "?", lst: "?"]  
```

```
faces.lst("?");  // Uncaught TypeError: faces.lst is not a function 
```

```
faces[ln] = "?"; // (6) ["?", "?", "?", "?", "?", "?"]  
```

This concern is not unique to our approach, it applies to all native Object prototypes (including arrays). Yet this offers safety in a different form. Arrays in Javascript are not fixed in length and consequently, there are no `IndexOutOfBoundsExceptions`. Using `Array.last` ensures we do not accidentally try to access `[length]` and unintentionally enter `undefined` territory.

No matter which approach you take, there are pitfalls. Once again, software proves to be an [art of making tradeoffs](https://pragprog.com/articles/the-art-of-tradeoffs).

Continuing with the extraneous biblical reference, assuming we do not believe extending `Array.prototype` is an eternal sin, or we’re willing to take a bite of the forbidden fruit, we can use this concise and readable syntax today!

### **Last Words**

> Programs must be written for people to read, and only incidentally for machines to execute. – [Harold Abelson](https://www.goodreads.com/book/show/43713.Structure_and_Interpretation_of_Computer_Programs?from_choice=false&from_home_module=false)

In scripting languages like Javascript, I prefer code that is functional, concise, and readable. When it comes to accessing terminal array elements, I find the `Array.last` property to be the most elegant. In a production front-end application, I might favor Lodash to minimize conflict and cross-browser concerns. But in Node back-end services where I control the environment, I prefer these custom properties.

I am certainly [not the first](https://esdiscuss.org/topic/array-prototype-last), nor will I be the last, to appreciate the value (or caution about the implications) of properties like `Array.lastItem`, which is hopefully coming soon to a version of ECMAScript near you.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z63EqxzV68XKUa3b81d8wg.png)

Follow me on [LinkedIn](https://www.linkedin.com/in/tombarrasso) · [GitHub](https://github.com/Tombarr) · [Medium](https://medium.com/@tbarrasso)


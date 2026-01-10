---
title: Stability in Sorting Algorithms — A Treatment of Equality
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-28T23:16:19.000Z'
originalURL: https://freecodecamp.org/news/stability-in-sorting-algorithms-a-treatment-of-equality-fa3140a5a539
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ghZAH4YaFgcBXL84TuMLXw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Onel Harrison

  Algorithms are at the heart of computer science. Algorithms used for sorting are
  some of the most fundamental, useful, and consequently, ubiquitous.


  Algorithm — a finite set of unambiguous steps for solving a specific problem.


  We c...'
---

By Onel Harrison

Algorithms are at the heart of computer science. Algorithms used for sorting are some of the most fundamental, useful, and consequently, ubiquitous.

> Algorithm — a finite set of unambiguous steps for solving a specific problem.

We constantly and often unconsciously sort and rely on the order of grouped objects. For instance, we rank tasks on a list according to priority. We stack books on shelves by their height. We sort rows in a spreadsheet or database, or rely on the alphabetical order of words in a dictionary. Sometimes, we even perceive a certain kind of beauty in ordered arrangements.

![Image](https://cdn-media-1.freecodecamp.org/images/bi4NZvtpx6kQ5I1PXNoNLOsusrYSVCQDbVhP)
_Photo by [Unsplash](https://unsplash.com/photos/6GjHwABuci4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Mikael Kristenson</a> on <a href="https://unsplash.com/search/photos/order-placement?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

As programmers, knowing **how** we sort is important because it affects what a sorted arrangement might look like. Not all sorts order objects in the same way! Because of this, the results of sorting operations differ based on the algorithms used. If this goes unacknowledged, we might surprise ourselves or the people who use our software.

The stability of sorting algorithms is one of the distinguishing properties among them. It deals with how the algorithm treats comparable items with equal sort keys.

> Sort key — A key used to determine the ordering of items in a collection, e.g. age, height, position in the alphabet, etc.

**A stable sorting algorithm** maintains the relative order of the items with equal sort keys. An unstable sorting algorithm does not. In other words, when a collection is sorted with a stable sorting algorithm, items with the same sort keys preserve their order after the collection is sorted.

### An Example, Code, and a Demo

![Image](https://cdn-media-1.freecodecamp.org/images/cLIBZqqktMgD1zb37j0Ic-RpIXSLOBQtNYdx)
_Image showing the effect of stable sorting_

The image above illustrates the effect of a stable sort. On the left, the data was sorted alphabetically by Name. After sorting the data by Grade, you can see that the alphabetical order of the names was maintained for each row with the same Grade.

![Image](https://cdn-media-1.freecodecamp.org/images/qFs0bAIY74R0sBaXe-PmAjqOA00fbhU5tR4p)
_Image showing the effect of unstable sorting_

With an unstable sort, there is no guarantee the alphabetical ordering is maintained as shown in the image above.

#### You don’t always need a stable sort

Knowing whether or not the sort you use is stable is particularly important. Especially in situations when your data already has some order to it that you would like to maintain when you sort it by another sort key. For example, you have rows in a spreadsheet containing student data that is, by default, sorted by name. You would like also to sort it by grades while maintaining the sorted order of the names.

On the other hand, the stability of the sort doesn’t matter when the sort keys of the objects in a collection are the objects themselves — an array of integers or strings, for example — because we can’t tell the difference among the duplicated keys.

```
// JavaScript
```

```
// $5 bucks if you can correctly tell which 4 in the sorted// array was the first 4 when the array was unsorted.
```

```
var numbers = [5, 4, 3, 4, 9];numbers.sort(); // [3, 4, 4, 5, 9]
```

```
// A one second trip around the world, courtesy of the Flash, to// whomever correctly tells me which 'harry' in the sorted array was// the second 'harry' in the unsorted array.
```

```
var names = ['harry', 'barry', 'harry', 'cisco'];names.sort(); // ['barry', 'cisco', 'harry', 'harry']
```

#### Sorts are everywhere — know your sorts

It’s quite easy to find out if the default sort in your programming language or library is stable. The documentation should include this information. For instance, [default sorting is stable in Python](https://wiki.python.org/moin/HowTo/Sorting), [unstable in Ruby](https://ruby-doc.org/core-2.0.0/Enumerable.html#method-i-sort), and [undefined](http://www.ecma-international.org/ecma-262/7.0/index.html#sec-array.prototype.sort)? [in JavaScript](http://www.ecma-international.org/ecma-262/7.0/index.html#sec-array.prototype.sort) (it depends on the browser’s implementation).

Here are a few common sorting algorithms and their stability:

* Insertion Sort — Stable
* Selection Sort — Unstable
* Bubble Sort — Stable
* Merge Sort — Stable
* Shell Sort — Unstable
* Timsort — Stable

See [Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability) for a more exhaustive list.

#### It’s demo time ?‍?

[This demo](https://onelharrison.com/sort-stability-demo/) shows the effect of using a stable (insertion sort) and unstable sorting (selection sort) algorithm to sort a small table of data. I had a bit of fun and practically reverse engineered React while building this. Have a look at the [source](https://github.com/onelharrison/sort-stability-demo).

### What’s next?

If you are thirsty for more knowledge about the stability of other sorting algorithms, [Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability) has a good comparison table and additional information on well known sorting algorithms.

Until next time, peace.

#### Learned something new or enjoyed reading this article? Clap it up ?, share it so that others can read too, and follow along for more. Feel free to leave a comment too.


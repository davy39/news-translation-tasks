---
title: A Step Towards Computing as a Science
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T21:02:36.000Z'
originalURL: https://freecodecamp.org/news/a-step-towards-computing-as-a-science-algorithms-data-structures-4c0e2d6ae79a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*494Zt3R4wuX6jGEE93bGyg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Yung L. Leung

  Simple Algorithms & Data Structures in JS


  _Photo by J. Craig on [Un-splash](https://unsplash.com/photos/HH4WBGNyltc" rel="noopener"
  target="blank" title=")

  An algorithm is the steps taken to solve a problem. A data structure is data...'
---

By Yung L. Leung

#### Simple Algorithms & Data Structures in JS

![Image](https://cdn-media-1.freecodecamp.org/images/SzQAdm6hPSs6JDis5HmlTUsfRMeAn3gR3Q6z)
_Photo by J. Craig on [Un-splash](https://unsplash.com/photos/HH4WBGNyltc" rel="noopener" target="_blank" title=")_

An **algorithm** is the steps taken to solve a problem. A **data structure** is data organized for efficient access. You can use an algorithm to solve all kinds of problems (i.e., searching for a piece of data or sorting a collection of data) for a given data structure.

So with regards to computers, an **algorithm** is the method of what you are doing (i.e., linear search, binary search, bubble sort, selection sort, insertion sort, etc.), whereas a **data structure** is the thing that you are doing it to (i.e., array, key-value paired objects, etc.). So you can methodically search through, sort, or create an organized dataset.

### A Simple Data Structure

#### Array

An **array** is like numbered boxes (**index**) ordered from lowest (0) to its highest (2) label. Each box is fixed in place and remains ordered by its label.

![Image](https://cdn-media-1.freecodecamp.org/images/1b9YMqQJlydsZT6RkSa6w0EhBWycwnEwBvxe)

You can jump to any labeled box to look at its contents (arrayName[2]), to add content, or replace its content (arrayName[2] = “Sherlock Holmes”). You can **push** newly boxed content to the end of your collection (arrayName.push(“The Memoirs of Sherlock Holmes”)).

![Image](https://cdn-media-1.freecodecamp.org/images/GBmaTMT21U4XkgINEpi6zbABzdSTUL3HOgQP)

This gives the incoming box the next label in the sequence (3). To return to your original boxed collection, you can **pop** off the end (arrayName.pop()).

You can also **shift** off your first box (arrayName.shift()), but this will require relabelling all your other boxes.

![Image](https://cdn-media-1.freecodecamp.org/images/SaNd1RwP9IGtFhZ8JlUXmUoYgSZbTSw2-ApI)

Your Sherlock Holmes collection is now in the box labeled 1. If you **unshift** your box collection, you can add to the start of your collection a new box of content (arrayName.shift(“Dr. Strange”)).

![Image](https://cdn-media-1.freecodecamp.org/images/MNkPBN3GvJN-TxmukjSFaN7s6iDVRJwC0o0j)

This gives us our Dr. Strange & Sherlock Holmes collection at boxes labeled 0 & 2.

### Searching a Data Structure

#### Linear Search

A **linear search** is like walking along an array of boxes (i.e., 0 — 16) and opening each cover to see if its contents are what you are looking for (i.e., 37).

![Image](https://cdn-media-1.freecodecamp.org/images/pxaLBaOpULERV7f1iJJeRG14Rm5ROMx62Sq5)
_[source](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif" rel="noopener" target="_blank" title=")_

So, for an index ranging from the start of a collection (let us say 0) to its end (its length less one), we can search for our desired content in a box and move on to the next. We can increment from one box to the next until we find a match.

#### Binary Search

A **binary search** is like searching through an array of boxes, whose contents are ordered (i.e., numerical or alphabetical), by jumping halfway to a middle box and checking its contents for your desired item. If you overstepped, you **jump backward**, halfway between your current position and the starting point. Otherwise, you **leap forward**, halfway between your current position and the endpoint.

![Image](https://cdn-media-1.freecodecamp.org/images/NnKWfGNACsLaYbS0WvBCI4Ipx0k7Ojmoa4DP)
_[source](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif" rel="noopener" target="_blank" title=")_

So, what you can do is keep track of your low (initially **0**), mid (**8**) & high (initially **16**) index positions. The mid position is always half the sum of low & high indexes. You check the mid box for a match (i.e., **37**). If its less than what you expected (< 37), then you leap forward. You reset your low index to be passed your current mid position by one (8 + 1 = 9). Then, recalculate a new mid position ((9 + 16) / 2 **≈** 12).

**In other words, you can leap forward in your search by resetting your low index & recalculating a new mid index. Conversely, if you overstepped, you can jump backward by resetting your high index & recalculating a new mid index_._**

Unlike linear search, this type is binary. You are always guessing whether your item is located on the 1st or 2nd half of your boxed collection.

### Sorting a Data Structure

#### Bubble Sort

A **bubble sort** is sorting a collection by continuously swapping a higher value with an adjacent lesser, resulting in the effect of the highest value bubbling up to the top.

![Image](https://cdn-media-1.freecodecamp.org/images/HawSOQIini2SfP9RayRvllpjAXrMxQMJi3yV)
_[source](https://upload.wikimedia.org/wikipedia/commons/5/54/Sorting_bubblesort_anim.gif" rel="noopener" target="_blank" title=")_

So, for the length of your collection, starting at index 0, you swap the contents of a current index (i) with the contents of a later index (i + 1), if the earlier is greater in value. Then, you move on to the next set of indexes (i + 1 vs. i + 2), and so forth.

At some point in time, you will have arrived at a box with the highest value in your collection. And so, it will be the content that keeps being swapped forward. Hence it bubbles upward. You repeat this process until your collection is sorted, from low to high in value.

Since the last box of each iteration will end with the highest value, you repeat the process by excluding the last boxes.

#### Selection Sort

A **selection sort** is sorting a collection by continuously _selecting_ for the lowest value and swapping it to one end.

![Image](https://cdn-media-1.freecodecamp.org/images/bbeO5vQWD0Q6Dl6tRXVsHMoXjwtFF109Z99H)
_[source](https://codepumpkin.com/selection-sort-algorithms/" rel="noopener" target="_blank" title=")_

So, here you scan through your entire collection to find the lowest value. Once it is found, you swap its content with the box labeled with the lowest index (initially index 0). You repeat this process starting with the next lowest index (index 1) since your lowest value is in its correct position. With every iteration, the range of length for your scan decreases by 1, until your entire collection is sorted from lowest to the highest value.

#### Insertion Sort

An **insertion sort** is sorting a collection by _inserting_ each encountered value into its correct position.

![Image](https://cdn-media-1.freecodecamp.org/images/q27NtXV17832eN--MmZuUaCUiY4r1QExDI-R)
_[source](https://gfycat.com/densebaggyibis" rel="noopener" target="_blank" title=")_

So here, rather than scanning an entire collection per iteration (i.e., Bubble & Selection Sorts), you start at index 0 & 1 to compare their values. If the later value is lower, if index 1’s contents are lower in value than index 0, you swap their contents. You move to the next box at index 2 and compare to your previously sorted boxes (index 1, then index 0).

Every time you encounter a higher value, you swap its contents over to the right. When you have found the correct position, you insert the contents (previously at index 2) into the correct box. So, it is as if you “pulling out” the contents of a later box and walking over to an earlier box.

If the earlier box has a higher value than what you are holding, you move its contents over to the later box. You keep doing this until you find the correct spot to insert what you are holding.

### Another Simple Data Structure

#### Key — Value Paired Objects

A **key — value paired object** is like an unlabelled set of deposit boxes. Each unique key opens up to a specific piece of data. Unlike an array, it is unordered data that is accessible by unique keys.

![Image](https://cdn-media-1.freecodecamp.org/images/exHs5jS2Faf9ymhaXL2954GoGeaPAFp78oP2)
_[source](https://cdn.shopify.com/s/files/1/1147/6518/products/safeandvaultstore-sdbx9-safe-deposit-boxes_large.jpg?v=1495593363" rel="noopener" target="_blank" title=")_

So, you access a deposit box by using its key (objectName[‘s’]), change its content or create a key that opens up to a specified content (objectName[‘s’] = “Sherlock Holmes”). You can access all keys made for or all content stored in all your deposit boxes (Object.keys(objectName) or Object.values(objectName)).

### Conclusion

Basic **algorithms** (linear & binary searches; bubble, selection & insertion sorts) & **data structures** (array & key-value objects) lead to questions of time & space regarding data management. Considerations of the **time** taken to search, sort or access data and the memory **space** required for these processes can elevate a software developer from computer programming to computer science. It takes you from thinking of programming for efficacy to programming for efficiency.


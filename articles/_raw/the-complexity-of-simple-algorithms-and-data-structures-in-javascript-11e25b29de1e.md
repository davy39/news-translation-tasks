---
title: The complexity of simple algorithms and data structures in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:02:28.000Z'
originalURL: https://freecodecamp.org/news/the-complexity-of-simple-algorithms-and-data-structures-in-javascript-11e25b29de1e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1bB3zrN0WrNC6ErArRF6cQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Yung L. Leung

  In the previous article “A Step Towards Computing as a Science: Simple Algorithms
  & Data Structures in JS,” we discussed simple algorithms (linear & binary searches;
  bubble, selection & insertion sorts) & data structures (array & key...'
---

By Yung L. Leung

In the previous article “[A Step Towards Computing as a Science: Simple Algorithms & Data Structures in JS](https://medium.com/@yunglleung1/a-step-towards-computing-as-a-science-algorithms-data-structures-4c0e2d6ae79a),” we discussed simple algorithms (linear & binary searches; bubble, selection & insertion sorts) & data structures (array & key-value paired objects). Here, I continue with the concept of complexity and its application to these algorithms & data structures.

### **Complexity**

**Complexity** is a factor involved in a complex process. Regarding algorithms & data structures, this can be the **time** or **space** (meaning computing memory) required to perform a specific task (search, sort or access data) on a given data structure. The efficiency of performing a task is dependent on the number of operations required to complete a task.

**Taking out the trash** may require 3 steps (tying up a garbage bag, bringing it outside & dropping it into a dumpster). **Taking out the trash** may be simple, but if you are taking out the trash after a long week of renovation, you may find yourself unable to complete the task due to a **lack of space** in the dumpster.

**Vacuuming a room** can require many repetitive steps (turning it on, repeatedly sweeping the vacuum head across a floor & turning it off). The larger a room, the more times you will have to sweep a vacuum head across its floor. Thus, the **longer the time** it will take to vacuum the room.

![Image](https://cdn-media-1.freecodecamp.org/images/L12QMT1j9D8t1gr3hUD5nE72YpEsgo3DPowC)

So, there is a direct causal relationship between the number of operations performed and the number of elements that are performed on. Having a lot of trash (elements) requires taking it out many times. This can lead to a problem of **space complexity**. Having a lot of square footage (elements) requires sweeping a vacuum head across a floor many times over. This can lead to a problem of **time complexity**.

Whether you are **taking out the trash** or **vacuuming a room**, you might say that the **operation count (**O**)** increases exactly with the **number of elements (**n**)**. If I have 1 trash bag, I have to take out the trash once. If I had 2 trash bags, I have to perform the same task twice, assuming you physically cannot lift more than one bag at a time. So, the Big-O of these chores is O = n or O = function(n) or **O(n)**. This is a linear complexity (a straight line with a 1 operation: 1 element correspondence). So, 30 operations are performed on 30 elements (yellow line on graph).

This is similar to what happens when considering algorithms & data structures.

### Searches

#### Linear Search

![Image](https://cdn-media-1.freecodecamp.org/images/CMLgOmQiGx-An2R8TeY3yghPSmQzfHc4KCsa)
_[source](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif" rel="noopener" target="_blank" title=")_

The **best case** for searching an item in an ordered list, one after another, is a constant **O(1)**, assuming it is the 1st item in your list. So, if the item you are searching for is always listed first, regardless of your list size, you will find your item in an instant. The complexity of your search is constant with the list size. The **average to the worst case** of this kind of search is a linear complexity or **O(n).** In other words, for n items, I have to look n times, before I find my item, hence linear search.

#### Binary Search

![Image](https://cdn-media-1.freecodecamp.org/images/BdVrmbkpWAEROeZzJh-WwglcO3ZvE92aE7Co)
_[source](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif" rel="noopener" target="_blank" title=")_

For a binary search, the **best case** is O(1), meaning the item of your search is located at the midpoint. The **worst & average case** is log base 2 of n or:

![Image](https://cdn-media-1.freecodecamp.org/images/O4yQ5gMCaNxd9A8fGyTmZRoJlZmUvw2aPxmi)

Logarithm or log is a way of expressing an exponent for a given base. So, if there were 16 elements (n = 16), then it would take, at worse case, 4 steps to find the number 15 (exponent = 4).

![Image](https://cdn-media-1.freecodecamp.org/images/DSYpZXtP0NNN0Poj2wNYEE-n6wQhuekHm8KY)

Or simply: **O(log n)**

![Image](https://cdn-media-1.freecodecamp.org/images/xWIc5wqomKmecGODTG4drhWSHdirPt9D9lSE)

### Sorts

#### Bubble

![Image](https://cdn-media-1.freecodecamp.org/images/0aAaHJbR5Nb4u4NCSWXn2pomchbOh9ThVPUm)
_[source](https://upload.wikimedia.org/wikipedia/commons/5/54/Sorting_bubblesort_anim.gif" rel="noopener" target="_blank" title=")_

In bubble sort, every item is compared to the rest of the collection to determine the highest value to bubble up. For this reason, on **average to worst case**, its complexity is **O(n²)**. Think a loop nested within another loop.

![Image](https://cdn-media-1.freecodecamp.org/images/02WXe7k1k0y-OFHvIwKyyUh0vNZNs0FUVp-G)

So, for each item, you are comparing it to the rest of your collection. This amounts to 16 comparisons (or operations) for 4 elements (4² = 16). The **best case** is if your collection is almost sorted, except for a single item. This would amount to a single round of comparisons. That is, four comparisons are required to bubble up a member of a four-item collection, which is a complexity of **O(n)**.

#### Selection

![Image](https://cdn-media-1.freecodecamp.org/images/3HuokiI2FYWnn70N50fhDf-9LrLBLu3Xdcfk)
_[source](https://codepumpkin.com/selection-sort-algorithms/" rel="noopener" target="_blank" title=")_

Unlike **bubble sort**, instead of bubbling up the highest value, **selection sort** selects the lowest value to swap it to the earliest positions. But, because it requires comparing each item to the rest of the collection, it also has a complexity of **O(n²)**.

#### Insertion

![Image](https://cdn-media-1.freecodecamp.org/images/3tfg-fQ3pfT9czmGkS8p41nLAavr2XlPuxVK)
_[source](https://gfycat.com/densebaggyibis" rel="noopener" target="_blank" title=")_

Unlike the **bubble** & **selection sorts**, **insertion sort** inserts the item into its correct position. But, like the previous sorts, this also requires comparing each item to the rest of the collection, therefore, it has an **average to worst case** complexity of **O(n²)**. Like the **bubble sort**, if there is only one item left to sort, it only requires a single round of comparisons to insert the item into its correct position. That is, it has the **best case** complexity of **O(n)**.

### Data Structures

#### Arrays

![Image](https://cdn-media-1.freecodecamp.org/images/5UN4-lEeiZ5sR3wLv3S0t5RU0bKU4ixbPTB7)

Because it takes a single step to access an item of an array via its index, or add/remove an item at the end of an array, the complexity for **accessing**, **pushing** or **popping** a value in an array is **O(1)**. Whereas, **linearly searching** through an array via its index, as seen before, has a complexity of **O(n)**.

Also, because a **shift** or **unshift** of a value to or from the front of an array requires **reindexing** each element that follows it (i.e. removing an element at index 0 requires relabelling element at index 1 as index 0, and so forth), they have a complexity of **O(n)**. The relabelling is carried through from the start to the end of the array.

#### Key — Value Paired Objects

![Image](https://cdn-media-1.freecodecamp.org/images/uSM26U11UIi7pAVC9TOM0Ku20YXoAE7C2UCD)
_[source](https://cdn.shopify.com/s/files/1/1147/6518/products/safeandvaultstore-sdbx9-safe-deposit-boxes_large.jpg?v=1495593363" rel="noopener" target="_blank" title=")_

**Accessing**, **inserting** or **removing** a value by using a key is instantaneous, and so, they have a complexity of **O(1)**. Searching through each “deposit box” for a specific item by using every available key is essentially a **linear search**. And so, it has a complexity of **O(n)**.

### Conclusion

**Complexity** is more than just a topic for discussing established algorithms & data structures. If used wisely, it can be a useful tool for gauging the efficiency of the work you do and the code you create to solve your problems.

### **Reference:**

[https://www.udemy.com/js-algorithms-and-data-structures-masterclass/](https://www.udemy.com/js-algorithms-and-data-structures-masterclass/)


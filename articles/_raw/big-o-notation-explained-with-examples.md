---
title: Big O Notation Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/big-o-notation-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cf0740569d1a4ca3502.jpg
tags:
- name: algorithms
  slug: algorithms
- name: '#big o notation'
  slug: big-o-notation
- name: data structures
  slug: data-structures
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Big O notation is a way to describe the speed or complexity of a given
  algorithm. If your current project demands a predefined algorithm, it''s important
  to understand how fast or slow it is compared to other options.

  What is Big O notation and how do...'
---

Big O notation is a way to describe the speed or complexity of a given algorithm. If your current project demands a predefined algorithm, it's important to understand how fast or slow it is compared to other options.

## What is Big O notation and how does it work?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31781171-74c6b48a-b500-11e7-9626-f715b37b10f0.png)

Simply put, Big O notation tells you the number of operations an algorithm will make. It gets its name from the literal "Big O" in front of the estimated number of operations.

What Big O notation doesn't tell you is the speed of the algorithm in seconds. There are way too many factors that influence the time an algorithm takes to run. Instead, you'll use Big O notation to compare different algorithms by the number of operations they make.

### Big O establishes a worst-case run time

Imagine that you're a teacher with a student named Jane. You want to find her records, so you use a simple search algorithm to go through your school district's database.

You know that simple search takes O(n) times to run. This means that, in the worst case, you'll have to search through every single record (represented by n) to find Jane's. 

But when you run the simple search, you find that Jane's records are the very first entry in the database. You don't have to look at every entry – you found it on your first try.

_Did this algorithm take O(n) time? Or did it take O(1) time because you found Jane's records on the first try?_

In this case, 0(1) is the best-case scenario – you were lucky that Jane's records were at the top. But Big O notation focuses on the worst-case scenario, which is 0(n) for simple search. It’s a reassurance that simple search will never be slower than O(n) time.

### Algorithm running times grow at different rates

Assume that it takes 1 millisecond to check each element in the school district's database.

With simple search, if you have to check 10 entries, it will take 10 ms to run. But with the _binary search algorithm_, you only have to check 3 elements, which takes 3 ms to run.

In most cases, the list or database you need to search will have hundreds or thousands of elements.

If there are 1 billion elements, using simple search will take up to 1 billion ms, or 11 days. On the other hand, using binary search will take just 32 ms in the worst-case scenario: 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31781165-723a053c-b500-11e7-937c-7b33db281efe.png)

Clearly the run times for simple search and binary search don't grow at nearly the same rate. As the list of entries gets larger, binary search takes just a little more time to run. Simple search's run time grows exponentially as the list of entries increases. 

This is why knowing how the running time increases in relation to a list size is so important. And this is exactly where Big O notation is so useful.

### Big O notation shows the number of operations

As mentioned above, Big O notation doesn't show the _time_ an algorithm will run. Instead, it shows the number of operations it will perform. It tells you how fast an algorithm grows and lets you compare it with others.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31781175-768c208e-b500-11e7-9718-e632d1391e2d.png)

Here are some common algorithms and their run times in Big O notation:

| Big O notation | Example algorithm |
| :---: | :---: |
| O(log n) | Binary search |
| O(n) | Simple search |
| O(n * log n)  | Quicksort |
| O(n2) | Selection sort |
| O(n!) | Traveling salesperson |

Now you know enough to be dangerous with Big O notation. Get out there and start comparing algorithms.


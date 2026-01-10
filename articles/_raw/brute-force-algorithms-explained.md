---
title: Brute Force Algorithms Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T18:38:00.000Z'
originalURL: https://freecodecamp.org/news/brute-force-algorithms-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e20740569d1a4ca3b74.jpg
tags:
- name: algorithms
  slug: algorithms
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Brute Force Algorithms are exactly what they sound like – straightforward
  methods of solving a problem that rely on sheer computing power and trying every
  possibility rather than advanced techniques to improve efficiency.

  For example, imagine you hav...'
---

Brute Force Algorithms are exactly what they sound like – straightforward methods of solving a problem that rely on sheer computing power and trying every possibility rather than advanced techniques to improve efficiency.

For example, imagine you have a small padlock with 4 digits, each from 0-9. You forgot your combination, but you don't want to buy another padlock. Since you can't remember any of the digits, you have to use a brute force method to open the lock.

So you set all the numbers back to 0 and try them one by one: 0001, 0002, 0003, and so on until it opens. In the worst case scenario, it would take 10<sup>4</sup>, or 10,000 tries to find your combination.

A classic example in computer science is the traveling salesman problem (TSP). Suppose a salesman needs to visit 10 cities across the country. How does one determine the order in which those cities should be visited such that the total distance traveled is minimized? 

The brute force solution is simply to calculate the total distance for every possible route and then select the shortest one. This is not particularly efficient because it is possible to eliminate many possible routes through clever algorithms.

The time complexity of brute force is **O(m**n**)**, which is sometimes written as **O(n*m)** . So, if we were to search for a string of "n" characters in a string of "m" characters using brute force, it would take us n * m tries.

## More information about algorithms

In computer science, an algorithm is simply a set of step by step procedure to solve a given problem. Algorithms can be designed to perform calculations, process data, or perform automated reasoning tasks.

Here's how the dictionary defines [algorithms](https://www.merriam-webster.com/dictionary/algorithm) in simple terms:

> a step-by-step procedure for solving a problem or accomplishing some end.

There are certain requirements that an algorithm must abide by:

1. Definiteness: Each step in the process is precisely stated.
2. Effective Computability: Each step in the process can be carried out by a computer.
3. Finiteness: The program will eventually successfully terminate.

Some common types of algorithms include:

* sorting algorithms
* search algorithms 
* compression algorithms. 

Classes of algorithms include 

* Graph
* Dynamic Programming 
* Sorting
* Searching
* Strings
* Math
* Computational Geometry
* Optimization
* Miscellaneous.

Although technically not a class of algorithms, Data Structures are often grouped with them.

### **Efficiency**

Algorithms are most commonly judged by their efficiency and the amount of computing resources they require to complete their task. 

A common way to evaluate an algorithm is to look at its time complexity. This shows how the running time of the algorithm grows as the input size grows. Since the algorithms today have to operate on large data inputs, it is essential for our algorithms to have a reasonably fast running time.

### **Sorting Algorithms**

Sorting algorithms come in various flavors depending on your necessity. Some, very common and widely used are:

#### **Quicksort**

There is no sorting discussion which can finish without quick sort. Here is the basic concept: [Quick Sort](http://me.dt.in.th/page/Quicksort/)

#### **Mergesort**

A sorting algorithm which relies on the concept how to sorted arrays are merged to give one sorted arrays. Read more about it here: [Mergesort](https://www.geeksforgeeks.org/merge-sort/)

freeCodeCamp’s curriculum heavily emphasizes creating algorithms. This is because learning algorithms is a good way to practice programming skills. Interviewers most commonly test candidates on algorithms during developer job interviews.

## Books about algorithms in JavaScript:

_Data Structures in JavaScript_

* Free book which covers Data Structures in JavaScript
* [GitBook](https://www.gitbook.com/book/pmary/data-structure-in-javascript/details)

_Learning JavaScript Data Structures and Algorithms - Second Edition_

* Covers object oriented programming, prototypal inheritance, sorting & searching algorithms, quicksort, mergesort, binary search trees and advanced algorithm concepts
* [Amazon](https://www.amazon.com/Learning-JavaScript-Data-Structures-Algorithms/dp/1785285491)
* ISBN-13: 978-1785285493

_Data Structures and Algorithms with JavaScript: Bringing classic computing approaches to the Web_

* Covers recursion, sorting and searching algorithms, linked lists and binary search trees.
* [Amazon](https://www.amazon.com/Data-Structures-Algorithms-JavaScript-approaches/dp/1449364934)
* ISBN-13: 978-1449364939



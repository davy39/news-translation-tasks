---
title: Everything you need to know about Insertion Sort algorithm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-07T13:32:38.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-about-insertion-sort-algorithm
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/image-44-1.png
tags:
- name: algorithms
  slug: algorithms
- name: Backend Development
  slug: backend-development
- name: coding
  slug: coding
- name: creative coding
  slug: creative-coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sanjula Madurapperuma

  Introduction

  Hi! I am Sanjula, and in this guide I hope to teach you a little bit about the Insertion
  Sort algorithm including:


  What is Insertion sort?

  Why is insertion sort important?

  Performance of Insertion Sort

  How does ...'
---

By Sanjula Madurapperuma

### **Introduction**

Hi! I am [Sanjula](https://www.linkedin.com/in/sanjula-madurapperuma/), and in this guide I hope to teach you a little bit about the Insertion Sort algorithm including:

* What is Insertion sort?
* Why is insertion sort important?
* Performance of Insertion Sort
* How does Insertion sort work?
* Java Implementation of Insertion sort

Let’s get started!

### **What is Insertion sort?**

It is a simple sorting algorithm that sorts an array one item at a time.

### **Why is insertion sort important?**

Insertion sort has several advantages including:

* The pure simplicity of the algorithm.
* The relative order of items with equal keys does not change.
* The ability to sort a list as it is being received.
* Efficient for small data sets, especially in practice than other quadratic algorithms — i.e. O(n²).
* It only requires a constant amount of additional memory space — O(1).

### **Performance of Insertion Sort**

* Worst-case performance of insertion sort is O(n²) comparisons and swaps.
* Best-case performance is O(n) comparisons and O(1) swaps.
* Average-case performance is O(n²) comparisons and swaps.

### **How does Insertion sort work?**

In each iteration, insertion sort compares the current element with the next element and determines whether the current element is greater than the one it was compared to.

If this is _true_, then it leaves the element in its place and moves on to the next element. If it is _false_, then it finds its correct position in the sorted array and moves it to that position by shifting all the elements which are larger in the sorted array to one position ahead.

### **Java Implementation of Insertion sort**

P.S. — Try to implement it on your own first!

<script src="https://gist.github.com/sanjulamadurapperuma/25677635f216b9fa858d8051140e47f2.js"></script>

---

**Congratulations!!!** You have now absorbed the basic but essential knowledge about how Insertion Sort works.

For reference or reporting issues regarding the code above, use the following public GitHub Gist [link](https://gist.github.com/sanjulamadurapperuma/25677635f216b9fa858d8051140e47f2).

---

Hope this was helpful. Thanks for reading! :)


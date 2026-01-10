---
title: Insertion Sort Algorithm - Most Asked Questions About Insertion Sort
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-31T19:26:33.000Z'
originalURL: https://freecodecamp.org/news/most-asked-questions-about-insertion-sort-algorithm
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--3-.png
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Sorting algorithms are an essential part of computer science. There are
  many sorting algorithms used to sort data.

  The insertion sort algorithm is one of the most basic and simple sorting algorithms.
  It is an efficient algorithm for small input sizes...'
---

Sorting algorithms are an essential part of computer science. There are many sorting algorithms used to sort data.

The insertion sort algorithm is one of the most basic and simple sorting algorithms. It is an efficient algorithm for small input sizes or for partially sorted data. The algorithm works by sorting elements one at a time, starting with the first element in the list.

In this article, you'll learn about the insertion sort algorithm and how it works. You'll also learn how to implement the algorithm in JavaScript. This article will also answer some common questions about the insertion sort algorithm.

## What is Insertion Sort?

Insertion sort is a sorting algorithm that sorts an array by inserting each element in its correct position in a sorted sub-list. It is called an in-place comparison sorting algorithm because it sorts the input list in place without requiring any extra memory.

It works by comparing each element with the previous elements and then moving the element to its correct position by shifting the larger elements to the right.

## Implementation of Insertion Sort With JavaScript

Here's an implementation of the Insertion Sort algorithm in JavaScript:

```js
const insertionSort = (arr) => {
  for (let i = 1; i < arr.length; i++) {
    let currentValue = arr[i];
    let j = i - 1;
    while (j >= 0 && arr[j] > currentValue) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = currentValue;
  }
  return arr;
};
```

The function takes an array as input and performs the insertion sort algorithm. It loops through the array starting from the second element and compares it with the elements before it.

If an element is greater than the current value, it shifts the element to the right until it finds its proper position.

Once the element is placed properly, the loop moves on to the next element until the array is completely sorted. The function returns the sorted array.

You can call the function with an array as follows:

```js
let myArray = [3, 7, 4, 10, 12];
console.log(insertionSort(myArray)); // returns [3, 4, 7, 10, 12]
```

This is just one way to implement the insertion sort algorithm in JavaScript. There are many other ways to write it, but this should give you an idea of how it works.

## Is Insertion Sort Stable?

Yes, insertion sort is a stable sorting algorithm.

A stable sorting algorithm is one that maintains the relative order of equal elements in the sorted output.

In other words, if two elements have the same value, their relative order in the input array should be preserved in the sorted array.

## What Kind of Algorithm is Insertion Sort?

Insertion sort is a comparison-based algorithm.

It compares the current and previous elements to determine their correct position in the sorted list. It is a simple and efficient algorithm that is easy to implement.

## Is Insertion Sort a Greedy Algorithm?

No, insertion sort is not a greedy algorithm.

A greedy algorithm is an algorithm that makes a locally optimal choice at each step with the hope of finding a global optimum.

Insertion sort does not make any locally optimal choice but instead inserts each element in its correct position to achieve the global optimum.

## Time Complexity of Insertion Sort Algorithm

The time complexity of the insertion sort algorithm is O(n^2) in the worst case and O(n) in the best case.

### Best Case Running Time of an Insertion Sort Algorithm

The best-case running time of an insertion sort algorithm is O(n). This occurs when the input array is sorted, and no elements must be moved.

This results in n-1 comparisons, which is approximately equal to n. Therefore, the time complexity is O(n).

### Best Case Time Efficiency of Insertion Sort

The best-case time efficiency of an insertion sort algorithm is Ω(n), which is the lower bound of the running time. This occurs when the input array is sorted and no elements need to be moved.

### Worst Time Complexity of Insertion Sort

The worst-case time complexity of an insertion sort algorithm is O(n^2).

This occurs when the input array is in reverse order, and each element must be moved to its correct position by shifting all the larger elements to the right.

The input array is in reverse order. Every element has to be compared and swapped with every other element in the array. This results in n\*(n-1)/2 comparisons and swaps, approximately equal to n^2/2. Therefore, the time complexity is O(n^2).

### Average Case Running Time of an Insertion Sort Algorithm

The average case running time of an insertion sort algorithm is O(n^2).

This occurs when the input array is randomly ordered, and each element must be moved to its correct position by shifting all the larger elements to the right.

### Typical Runtime for Insertion Sort for Singly Linked Lists

Insertion sort can also be used to sort singly-linked lists.

The typical runtime for insertion sort for singly linked lists is also O(n^2), the same for arrays. However, the space complexity may differ due to the data structure difference.

## Does Insertion Sort Use Divide and Conquer?

No, insertion sort does not use the Divide and Conquer approach.

Divide and Conquer is an algorithmic paradigm that involves breaking a problem into sub-problems, solving them independently, and then combining their solutions to solve the original problem.

Insertion sort works by sorting the elements individually without breaking the problem into sub-problems.

## Why is Insertion Sort Slow?

Insertion sort is slow because it has a time complexity of O(n^2) in the worst case.

This means that as the input size increases, the algorithm's running time also increases rapidly. Insertion sort is not the best choice for large input sizes, but it can be very efficient for small input sizes or for partially sorted data.

## Wrapping Up

Insertion sort is a simple and efficient algorithm for small input sizes or partially sorted data. It has a time complexity of O(n^2) in the worst case and O(n) in the best case.

It is a stable sorting algorithm that maintains the relative order of equal elements. Although it may be slow for large input sizes, it can be very efficient for small input sizes or for partially sorted data.

Have fun coding!

You can access over 200 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.

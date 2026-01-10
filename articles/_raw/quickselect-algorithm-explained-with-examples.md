---
title: 'QuickSelect: The Quick Select Algorithm Explained With Code Examples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-03T18:44:00.000Z'
originalURL: https://freecodecamp.org/news/quickselect-algorithm-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ee2740569d1a4ca3fb0.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: null
seo_desc: 'What is QuickSelect?

  QuickSelect is a selection algorithm to find the K-th smallest element in an unsorted
  list.

  The Algorithm Explained

  After finding the pivot (a position that partitions the list into two parts: every
  element on the left is less th...'
---

## What is QuickSelect?

QuickSelect is a selection algorithm to find the K-th smallest element in an unsorted list.

### The Algorithm Explained

After finding the pivot (a position that partitions the list into two parts: every element on the left is less than the pivot and every element on the right is more than the pivot) the algorithm recurs only for the part that contains the k-th smallest element. 

If the index of the partitioned element (pivot) is more than k, then the algorithm recurs for the left part. If the index (pivot) is same as k, then we have found the k-th smallest element and it is returned. If index is less than k, then the algorithm recurs for the right part.

#### Selection Psudocode

```
Input : List, left is first position of list, right is last position of list and k is k-th smallest element.
Output : A new list is partitioned.

quickSelect(list, left, right, k)

   if left = right
      return list[left]

   // Select a pivotIndex between left and right

   pivotIndex := partition(list, left, right, 
                                  pivotIndex)
   if k = pivotIndex
      return list[k]
   else if k < pivotIndex
      right := pivotIndex - 1
   else
      left := pivotIndex + 1

```

### Partition

Partition is to find the pivot as mentioned above. (Every element on the left is less than the pivot and every element on the right is more than pivot) There are two algorithm for finding the pivot of partition.

* Lomuto Partition
* Hoare Partition

#### Lomuto Partition

This partition chooses a pivot that is typically the last element in the array. The algorithm maintains index i as it scans the array using another index j such that the elements lo through i (inclusive) are less than or equal to the pivot, and the elements i+1 through j-1 (inclusive) are greater than the pivot.

This scheme degrades to `O(n^2)` when the array is already in order.

```
algorithm Lomuto(A, lo, hi) is
    pivot := A[hi]
    i := lo    
    for j := lo to hi - 1 do
        if A[j] < pivot then
            if i != j then
                swap A[i] with A[j]
            i := i + 1
    swap A[i] with A[hi]
    return i

```

#### Hoare Partition

Hoare uses two indices that start at the ends of the array being partitioned, then move toward each other until they detect an inversion: a pair of elements, one greater than or equal to the pivot, one less than or equal to the pivot, that are in the wrong order relative to each other. 

The inverted elements are then swapped. When the indices meet, the algorithm stops and returns the final index. There are many variants of this algorithm.

```
algorithm Hoare(A, lo, hi) is
    pivot := A[lo]
    i := lo - 1
    j := hi + 1
    loop forever
        do
            i := i + 1
        while A[i] < pivot

        do
            j := j - 1
        while A[j] > pivot

        if i >= j then
            return j

        swap A[i] with A[j]

```


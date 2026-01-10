---
title: How To Write Quick Sort Algorithm With JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-15T09:27:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-quick-sort-algorithm-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--6-.png
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Quick sort is a widely used sorting algorithm that efficiently sorts an
  array of elements by dividing it into smaller subarrays based on a chosen pivot
  element.

  In this article, we will walk through how to write a quick sort algorithm using
  JavaScrip...'
---

Quick sort is a widely used sorting algorithm that efficiently sorts an array of elements by dividing it into smaller subarrays based on a chosen pivot element.

In this article, we will walk through how to write a quick sort algorithm using JavaScript and explore the key concepts behind the algorithm.

## What Is the Quick Sort Algorithm?

Sorting is a common task in computer programming, and there are many sorting algorithms available that can be used in different ways. One of the most popular and efficient sorting algorithms is quick sort.

Quick sort is a divide-and-conquer algorithm that sorts an array by choosing a pivot element and partitioning the array into two subarrays, one containing elements smaller than the pivot, and the other containing elements larger than the pivot. The two subarrays are then recursively sorted until the entire array is sorted.

**Note:** In quick sort algorithm, the pivot is a selected element from the array that is used as a reference point for partitioning the array into two smaller sub-arrays.

The pivot is usually selected as the first or last element of the array, although there are other methods for selecting the pivot.

## Implementing Quick Sort Algorithm With Javascript

Before we start implementing the quick sort algorithm, let's first understand its basic concepts. As we mentioned earlier, quick sort is a divide-and-conquer algorithm. The algorithm can be broken down into three main steps:

1. Choose a pivot element from the array.
    
2. Partition the array into two subarrays, one containing elements smaller than the pivot, and the other containing elements larger than the pivot.
    
3. Recursively apply the quick sort algorithm to the two subarrays until the entire array is sorted.
    

With this understanding, let's move on to implementing the algorithm in JavaScript.

```js
const quickSort = (arr) => {
  if (arr.length <= 1) {
    return arr;
  }

  let pivot = arr[0];
  let leftArr = [];
  let rightArr = [];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) {
      leftArr.push(arr[i]);
    } else {
      rightArr.push(arr[i]);
    }
  }

  return [...quickSort(leftArr), pivot, ...quickSort(rightArr)];
};
```

Let's walk through this implementation step by step. First, we create a function to handle the quick sort operation and hold the algorithm.

### Step 1: Choose a Pivot Element

We start by choosing a pivot element from the array. In this implementation, we will use the first element of the array as the pivot.

```js
const pivot = arr[0];
```

### Step 2: Partition the Array

After choosing the pivot element, the next step is to partition the array into two subarrays — one containing elements smaller than the pivot, and the other containing elements larger than the pivot.

We can achieve this by iterating through the array, comparing each element to the pivot and pushing it into the appropriate subarray.

```js
let leftArr = [];
let rightArr = [];

for (let i = 1; i < arr.length; i++) {
  if (arr[i] < pivot) {
    leftArr.push(arr[i]);
  } else {
    rightArr.push(arr[i]);
  }
}
```

### Step 3: Recursively Sort the Subarrays

Next, we recursively apply the quick sort algorithm to the two subarrays until the entire array is sorted. We then use the spread operator to concatenate the sorted left subarray, pivot, and sorted right subarray.

```js
return [...quickSort(leftArr), pivot, ...quickSort(rightArr)];
```

But for this not to continue over and over, there has to be a base case to stop the [recursion](https://joelolawanle.com/posts/recursion-in-javascript-explained-for-beginners).

### Step 4: Define a Base Case

The final step is to define a base case for the recursive function. This is used when the array has a length of 0 or 1, as an array with one element is already sorted.

```js
if (arr.length <= 1) {
  return arr;
}
```

## Testing the Quick Sort Algorithm

To test the quick sort algorithm, we can create an array of random numbers and pass it to the `quickSort()` function.

Here's an example:

```js
let myArray = [3, 7, 2, 5, 1, 4, 6, 8];
console.log(quicksort(myArray)); // Output: [1,2,3,4,5,6,7,8]
```

## Wrapping Up ✨

In this article, you have learned what the quick sort algorithm means and how you can create the algorithm.

You can use any value as your pivot number by tweaking the code a little.

Have fun coding!

You can access over 195 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.

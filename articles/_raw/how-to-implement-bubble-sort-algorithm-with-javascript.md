---
title: How To Implement Bubble Sort Algorithm With JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-30T15:34:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-bubble-sort-algorithm-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--2-.png
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Sorting is an essential task in programming, and the bubble sort algorithm
  is one of the simplest and most commonly used methods.

  As a beginner in solving algorithm questions or preparing for an interview, you
  might wonder how to implement this algor...'
---

Sorting is an essential task in programming, and the bubble sort algorithm is one of the simplest and most commonly used methods.

As a beginner in solving algorithm questions or preparing for an interview, you might wonder how to implement this algorithm effectively.

Don't worry; in this article, I will guide you step by step on how to implement the bubble sort algorithm with JavaScript. By the end of this tutorial, you will have a solid understanding of how this algorithm works and be able to apply it to your own projects.

## What is Bubble Sort Algorithm?

Bubble sort algorithm is a simple sorting technique that compares two adjacent elements in an array and swaps them if they are in the wrong order. It keeps repeating this process until the array is sorted.

For example, the diagram below illustrates the different swaps/bubble that happens when the element on the left is greater than the element on the right.

Also, at the end of the array iteration, it checks to see if any swaps occurred; if so, the process is repeated; otherwise, the array is sorted.

![](https://paper-attachments.dropboxusercontent.com/s_AA89D639F731C302D3BEA2FB06F0908D85A1AFFFF9C777BBB48943CB5F4958DF_1680155344777_Untitled.drawio.png align="left")

Imagine bubbles in a glass of soda where the bubbles rise to the top one by one. That's similar to how this algorithm works.

Bubble sort is easy to understand and implement but can be slow for large data sets.

## How to Implement Bubble Sort Algorithm With Javascript

With the illustration in the previous section, you should have an idea of how the bubble sort algorithm is supposed to work. But how can you write this algorithm with JavaScript?

Here are 5 steps to make the process easy for you:

1. Create a boolean variable to track the swapping of elements in the current iteration.
    
2. Create a "do-while" loop that iterates through the array until it is sorted.
    
3. At the start of each iteration, set the boolean variable to false.
    
4. Use a "for" loop to compare adjacent elements. Swap them if they are not in the correct order, and set the boolean variable to true if any element is swapped.
    
5. Repeat the loop until there are no more elements to swap in the current iteration.
    

Using the steps above, let's implement the algorithm in JavaScript.

```js
const bubbleSort = (arr) => {
  let swapped;

  do {
    swapped = false;
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        swapped = true;
      }
    }
  } while (swapped);

  return arr;
};
```

Let's walk through this implementation step by step. First, we create a function to handle the bubble sort operation and hold the algorithm.

### Step 1: Create a boolean variable

You will need to track whether any swap has been made in the current iteration of the array. To do this, create a boolean variable named "swapped" for this purpose.

```js
let swapped;
```

### Step 2: Create a "do-while" loop to iterate until the array is sorted

Let’s use the "do-while" loop to iterate through the array until it is sorted. The loop executes at least once, even if the array is already sorted — which is why it’s best used for this.

You will also use the "swapped" variable to check whether any swap has been made in the current iteration.

```js
do {
  // code to be executed
} while (swapped);
```

### Step 3: Set the boolean variable to false at the start of each iteration

At the beginning of each iteration, you need to set the "swapped" variable to false. This is because you have not made any swap yet in the current iteration.

```js
do {
  swapped = false;
  // code to be executed
} while (swapped);
```

### Step 4: Use a "for" loop to compare adjacent elements

Within the "do-while" loop, we use a "for" loop to compare each array element with the element next to it. If the current element is greater than the next element, they are swapped.

We also set the "swapped" variable to true if a swap is made, indicating that the array is not yet sorted.

```js
for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      let temp = arr[i];
      arr[i] = arr[i + 1];
      arr[i + 1] = temp;
      swapped = true;
    }
  }
} while (swapped);
```

### Step 5: Repeat the loop until no more swaps are made

If no swap is made in the current iteration, the "swapped" variable remains false. This means the array is sorted, and we can exit the loop.

If elements have been swapped, the "swapped" variable is set to true, and the loop continues to iterate until the array is sorted.

## Testing the Bubble Sort Algorithm

To test the bubble sort algorithm, you can create an array of random numbers and pass it to the `bubbleSort()` function.

Here's an example:

```js
let myArray = [12, 10, 3, 7, 4];
console.log(bubbleSort(myArray)); // Output: [3, 4, 7, 10, 12]
```

## Worst Case Time Complexity of Bubble Sort Algorithm

The worst-case time complexity of an algorithm refers to the maximum amount of time the algorithm can take to complete, given the worst possible input.

For bubble sort, the worst-case time complexity occurs when the array is in reverse order. This means that every element needs to be swapped with every other element.

In this case, the algorithm's time complexity is O(n^2), where n is the number of elements in the array.

This makes bubble sort inefficient for large arrays, as the time required to sort the array grows quadratically with the size of the array.

However, bubble sort can be useful for small arrays or in cases where the array is nearly sorted, as it has a simple implementation and requires only constant space.

## Wrapping Up

In this article, you have learned what the bubble sort algorithm means and how you can create the algorithm.

Finally, let’s tweak the algorithm to arrive at a shorter one by swapping each element by destructuring:

```js
const bubbleSort = (arr) => {
  let swapped;

  do {
    swapped = false;
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        [myArray[i], myArray[i + 1]] = [myArray[i + 1], myArray[i]];
        swapped = true;
      }
    }
  } while (swapped);

  return arr;
};

let myArray = [12, 10, 3, 7, 4];
console.log(bubbleSort(myArray)); // returns [3, 4, 7, 10, 12]
```

You can read more on [how to swap two array elements in JavaScript](https://www.freecodecamp.org/news/swap-two-array-elements-in-javascript/).

Have fun coding!

You can access over 200 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.

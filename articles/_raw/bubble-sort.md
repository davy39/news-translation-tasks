---
title: Bubble Sort Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-25T17:24:00.000Z'
originalURL: https://freecodecamp.org/news/bubble-sort
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d8f740569d1a4ca3864.jpg
tags:
- name: algorithms
  slug: algorithms
- name: bubble
  slug: bubble
seo_title: null
seo_desc: Just like the way bubbles rise from the bottom of a glass, bubble sort is
  a simple algorithm that sorts a list, allowing either lower or higher values to
  bubble up to the top. The algorithm traverses a list and compares adjacent values,
  swapping them...
---

Just like the way bubbles rise from the bottom of a glass, **bubble sort** is a simple algorithm that sorts a list, allowing either lower or higher values to bubble up to the top. The algorithm traverses a list and compares adjacent values, swapping them if they are not in the correct order.

With a worst-case complexity of O(n^2), bubble sort is very slow compared to other sorting algorithms like quicksort. The upside is that it is one of the easiest sorting algorithms to understand and code from scratch. 

### **Example:**

```js
let arr = [4, 2, 6, 3, 9];
let sorted = false

while(!sorted) {
  sorted = true
  for(var i = 0; i < arr.length; i++) {
    if(arr[i] < arr[i - 1]) {
      let temp = arr[i];
      arr[i] = arr[i - 1];
      arr[i - 1] = temp;
      sorted = false;
    }
  }
}
```

### First pass through the list:

* Starting with `[4, 2, 6, 3, 9]`, the algorithm compares the first two elements in the array, 4 and 2. It swaps them because 2 < 4: `[2, 4, 6, 3, 9]`
* It compares the next two values, 4 and 6. As 4 < 6, these are already in order, and the algorithm moves on: `[2, 4, 6, 3, 9]`
* The next two values are also swapped because 3 < 6: `[2, 4, 3, 6, 9]`
* The last two values, 6 and 9, are already in order, so the algorithm does not swap them.

### Second pass through the list:

* 2 < 4, so there is no need to swap positions: `[2, 4, 3, 6, 9]`
* The algorithm swaps the next two values because 3 < 4: `[2, 3, 4, 6, 9]`
* No swap as 4 < 6: `[2, 3, 4, 6, 9]`
* Again, 6 < 9, so no swap occurs: `[2, 3, 4, 6, 9]`

The list is already sorted, but the bubble sort algorithm doesn't realize this. Rather, it needs to complete an entire pass through the list without swapping any values to know the list is sorted.

#### **Third pass through the list:**

* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`
* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`
* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`
* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`

Clearly bubble sort is far from the most efficient sorting algorithm. Still, it's simple to wrap your head around and implement yourself. 

Now go pour yourself a cold, bubbly beverage – you deserve it.


---
title: Bubble Sort Visualized
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-20T01:04:00.000Z'
originalURL: https://freecodecamp.org/news/cjn-bubble-sort-visualized
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/7632653238_c9436bb80d_b-1.jpg
tags:
- name: algorithms
  slug: algorithms
- name: learning to code
  slug: learning-to-code
seo_title: null
seo_desc: 'By Clark Jason Ngo

  What you need:

  1) Unsorted array

  2) for loop i - number of loop is based on the number of elements in the array.
  Each loop of i would reset loop of j to index zero.

  3) for loop j - number of loop is based on number of loop i minus ...'
---

By Clark Jason Ngo

**What you need:**

1) Unsorted array

2) for loop **i** - number of loop is based on the number of elements in the array. Each loop of **i** would reset loop of **j** to index zero.

3) for loop **j** - number of loop is based on number of loop **i** minus - 1 for every loop of **j**. Why? we are already sure that the last element of each loop is sorted and doesn't needed to be compared in the next loop (hence -1).

4) a variable to switch number. you don't need this in Python.

**Visualization:**

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-56.png)

If you are wondering how i made this, i used **Numbers** App in my MacBook.

### Python program for implementation of Bubble Sort

```py
def bubbleSort(arr):
  n = len(arr)

  # Traverse through all array elements 
  for i in range(n): 

	  # Last i elements are already in place 
	  for j in range(0, n-i-1): 
  
  		  # traverse the array from 0 to n-i-1 
		  # Swap if the element found is greater 
		  # than the next element 
		  if arr[j] > arr[j+1] : 
			  arr[j], arr[j+1] = arr[j+1], arr[j] 

```

### Driver code to test above

```py
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print ("Sorted array is:")

for i in range(len(arr)):
    print ("%d" %arr[i]),
```

Source for code: [https://www.geeksforgeeks.org/bubble-sort/](https://www.geeksforgeeks.org/bubble-sort/)


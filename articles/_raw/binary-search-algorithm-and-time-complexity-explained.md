---
title: Binary Search – Algorithm and Time Complexity Explained
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2023-07-12T14:26:58.000Z'
originalURL: https://freecodecamp.org/news/binary-search-algorithm-and-time-complexity-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/cover-img-search.png
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: Python
  slug: python
seo_title: null
seo_desc: 'When working with arrays, you’ll often have to search through them to check
  if they contain a target element.

  You can always run a sequential search—scanning the array from the beginning to
  the end—on the array. But if the array is sorted, running th...'
---

When working with arrays, you’ll often have to search through them to check if they contain a target element.

You can always run a sequential search—scanning the array from the beginning to the end—on the array. But if the array is sorted, running the binary search algorithm is much more efficient.

Let's learn how binary search works, its time complexity, and code a simple implementation in Python.

## How Does Linear Search Work?

We'll start our discussion with **linear** or **sequential search**.

Suppose we have an unsorted sequence of numbers `nums`. Given this nums array, you should check if the `target` is present in `nums`. You don’t have information about whether `nums` is sorted.

So the only way you can do this is to scan the array in a linear fashion, starting at the first element—until you find a match.

You can loop through the entire array to check if the element at index `i` matches the `target`. Once you find a match, you can break out of the loop.

Notice that in the worst case, you’ll have to scan the entire array and be lucky enough to find a match at the last index. Or you’ll have exhausted the array—without finding a match—indicating that the element is not present in the array. 

Suppose the array has `n` elements. Because you have to scan the entire array—in the worst case—the linear search algorithm has a time complexity of O(n).

Here's an example:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-66.png)
_Linear Search Example | Image by the author_

But when you do not know anything about the sequence, this is the best you can do. _So linear or sequential search is the best you can do when searching through unsorted sequences._

### How Linear Search Works in Python

The function `linear_search` takes in an array `nums` and a `target` to search for. It then loops through the array sequentially to check if `target` is present in `nums`:

```python
def linear_search(nums,target):
  for num in nums:
    if num == target:
      return True
  return False
```

Here are a couple of sample outputs:

```python
nums = [14,21,27,30,36,2,5,7,11]
target = 27

print(linear_search(nums,target))
# Output: True

target = 100
print(linear_search(nums,target))
# Output: False
```

## How Does Binary Search Work?

Now consider the `nums` sequence with `n` elements sorted in ascending order. For any valid index `k`, the following holds `True` for the element `a_k` at index `k`:

> The elements at indices 0, 1, 2, …, (k-1) are all less than or equal to `a_k`. And all elements at indices (k+1) to (n-1) are greater than or equal to `a_k`.

With this information, you no longer need to run a linear scan. You can do it much faster with binary search. 

We’re given a sorted array `nums` and a `target`. Let mid denote the middle-most index of the array and `nums[mid]` denote the element at the middle index. Here’s how the binary search algorithm works:

* Check if `nums[mid]` is equal to the `target`. If so, we’ve already found a match—in the very first step—and the search terminates.
* If `nums[mid]` > `target`, you _only_ need to search the _left half_ of the array. Even when you search through the left subarray you can use the same binary search algorithm.
* If `nums[mid]` < `target`, you can ignore all the elements up to the middle element and _only_ consider the _right half_ of the array.

Notice that we have a recurrence relation here. First, we start by running the binary search algorithm on the array with n elements. If we don't find the target in the very first step, we run binary search on the subarray of size at most n/2 elements.

If we end up with an empty array or an array with one element that is _not_ the `target`, we conclude that the target does not exist in the `nums` array.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-65.png)
_Binary Search Example | Image by the author_

### How to Implement Binary Search in Python

Here's a recursive implementation of binary search in Python:

```python
def binary_search(nums,target,low,high):
  if low > high:
    return False
  else:
    mid = (low + high)//2
    if nums[mid] == target:
      return True
    elif nums[mid] < target:
      return binary_search(nums,target,mid+1,high)
    else:
      return binary_search(nums,target,low,mid-1)
```

With a few sample runs of the `binary_search` function:

```python
nums = [2,5,7,11,14,21,27,30,36]
target = 27

print(binary_search(nums,target,0,len(nums)-1))
# Output: True

target = 38
print(binary_search(nums,target,0,len(nums)-1))
# Output: False
```

## What Is the Time Complexity of Binary Search?

In binary search, we know that the _search space is reduced by half_ at each step and this guides us in computing the time complexity. 

For an array with `n` elements, we check if the middle-most element matches the `target`. If so, we return `True` and terminate the search.

But if the middle element does not match the `target`, we perform binary search on a subarray of size at most `n/2`. In the next step, we have to search through an array of size at most `n/4`. And we continue this recursively until we can make a decision in a constant time (when the subarray is empty). 

At step `k`, we need to search through an array of size at most `n/(2^k)`. And we need to find the smallest such `k` for which we have no subarray to search through.

Mathematically:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-68.png)

The time complexity of binary search is, therefore, **O(logn)**. This is much more efficient than the linear time O(n), especially for large values of n.

For example, if the array has 1000 elements. 2^(10) = 1024. While the binary search algorithm will terminate in around 10 steps, linear search will take a thousand steps in the worst case.

## Wrapping Up

And that's a wrap. I hope you found this introduction to binary search helpful! You’ll often run into questions involving binary search in coding interviews. 

If you’re preparing for coding interviews, check out [10 Common Coding Interview Questions [Solved]](https://youtu.be/Peq4GCPNC5c) on freeCodeCamp’s YouTube channel.  


  


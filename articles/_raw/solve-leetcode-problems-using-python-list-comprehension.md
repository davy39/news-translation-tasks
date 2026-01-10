---
title: How to Solve Leetcode Problems With Python One-Liners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-02T15:13:35.000Z'
originalURL: https://freecodecamp.org/news/solve-leetcode-problems-using-python-list-comprehension
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60640fde9618b008528aa027.jpg
tags:
- name: leetcode
  slug: leetcode
- name: Problem Solving
  slug: problem-solving
- name: Python
  slug: python
seo_title: null
seo_desc: "By Ganesh Kumar Marimuthu\nPython is one of the most powerful programming\
  \ languages. It gives us various unique features and functionalities that make it\
  \ easy for us to write code. \nIn this article we'll solve Leetcode array problems\
  \ in one line using..."
---

By Ganesh Kumar Marimuthu

Python is one of the most powerful programming languages. It gives us various unique features and functionalities that make it easy for us to write code. 

In this article we'll solve Leetcode array problems in one line using one of Python's most interesting features – **List Comprehension**.

## What is List Comprehension?

Before going into the problems, let's make sure we understand what list comprehension is all about.

> A list comprehension is a syntactic construct available in some programming languages for creating a list based on existing lists  
> - Wikipedia

Let's see how list comprehension works with an example.

Consider an array of numbers. Our task is to add 1 to the numbers at odd indices and to add 2 to the number at even indices.

Now we'll see how to solve the above problem using both a for-loop and list comprehension.

### How to solve the problem with a for-loop

```python
def addOneAndTwo(nums, n):
    for i in range(n):
        if i % 2 == 1:
            nums[i] += 1 
        else:
            nums[i] += 2 
    return nums
```

### How to solve it with list comprehension

```python
def addOneAndTwo(nums, n):
    return [nums[i] + 1 if i % 2 == 1 else nums[i] + 2 for i in range(n)]
```

You can see how the solution using list comprehension is simplified from 6 lines to 1 line. This is the power of list comprehension.

## How to Solve Leetcode Problems with List Comprehension

Now let us solve the below Leetcode problems in 1 line using list comprehension.

### 1. [Shuffle The Array](https://leetcode.com/problems/shuffle-the-array/)

Here's the problem from Leetcode:

Given the array `nums` consisting of `2n` elements in the form `[x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub>,y<sub>1</sub>,y<sub>2</sub>,...,y<sub>n</sub>]`. _Return the array in the form_ `[x<sub>1</sub>,y<sub>1</sub>,x<sub>2</sub>,y<sub>2</sub>,...,x<sub>n</sub>,y<sub>n</sub>]`.

#### Example

Input: nums = [2,5,1,3,4,7], n = 3   
Output: [2,3,5,4,1,7] 

Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

#### Solution

```python
def shuffle(self, nums, n):
    return reduce(lambda a, b: a + b, [[nums[i], nums[j]] for i, j in zip(range(0, n), range(n, 2 * n))])
```

### 2. [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)

Given an array of integers `nums`. A pair `(i,j)` is called _good_ if `nums[i]` == `nums[j]` and `i` < `j`.Return the number of _good_ pairs.

#### Example

Input: nums = [1,2,3,1,1,3]   
Output: 4 

Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

#### Solution

```python
def numIdenticalPairs(self, nums):
    return sum([int(i != j and nums[i] == nums[j]) for i in range(0, len(nums)) for j in range(i + 1, len(nums))])
```

### 3. [Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

Given the array `candies` and the integer `extraCandies`, where `candies[i]` represents the number of candies that the **_ith_** kid has.

For each kid check if there is a way to distribute `extraCandies` among the kids such that they can have the **greatest** number of candies among them. Notice that multiple kids can have the **greatest** number of candies.

#### Example

Input: candies = [2,3,5,1,3], extraCandies = 3   
Output: [true,true,true,false,true]

Explanation: Kid 1 has 2 candies, and if they receive all extra candies (3) they will have 5 candies – the greatest number of candies among the kids. 

Kid 2 has 3 candies, and if they receive at least 2 extra candies then they will have the greatest number of candies among the kids. 

Kid 3 has 5 candies, and this is already the greatest number of candies among the kids. 

Kid 4 has 1 candy, and even if they receive all extra candies they will only have 4 candies. 

Kid 5 has 3 candies, and if they receive at least 2 extra candies then they will have the greatest number of candies among the kids.

#### Solution

```python
def kidsWithCandies(self, candies, extraCandies):
    return [candy + extraCandies >= max(candies) for candy in candies]
```

### 4. [Decompress Run-Length Encoded List](https://leetcode.com/problems/decompress-run-length-encoded-list/)

We are given a list `nums` of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements `[freq, val] = [nums[2*i], nums[2*i+1]]` (with `i >= 0`).  For each such pair, there are `freq` elements with value `val` concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

#### Example

Input: nums = [1,2,3,4]   
Output: [2,4,4,4] 

Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2]. 

The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4]. At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

#### Solution

```python
def decompressRLElist(self, nums):
    return reduce(lambda a, b: a + b, [[nums[i + 1]] * nums[i] for i in range(0, len(nums), 2)])
```

### 5. [Richest Customer's Wealth](https://leetcode.com/problems/richest-customer-wealth/)

You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the `i​​​​​<sup>​​​​​​th</sup>​​​​` customer has in the `j​​​​​<sup>​​​​​​th</sup>`​​​​ bank. Return _the **wealth** that the richest customer has._

A customer's **wealth** is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum **wealth**.

#### Example

Input: accounts = [[1,2,3],[3,2,1]]   
Output: 6 

Explanation: `1st customer has wealth = 1 + 2 + 3 = 6 2nd customer has wealth = 3 + 2 + 1 = 6`  Both customers are considered the richest with a wealth of 6 each, so return 6.

#### Solution

```python
def maximumWealth(self, accounts):
    return max([sum(row) for row in accounts])
```

## Conclusion

I hope the above solutions were useful. You can combine [**list comprehension**](https://data-flair.training/blogs/python-list-comprehension/) with other functions like [**map**, **filter** and **reduce**](https://www.freecodecamp.org/news/15-useful-javascript-examples-of-map-reduce-and-filter-74cbbb5e0a1f/) to make the solutions more simple and effective.

## Thank You 🤘

[Linkedin](https://www.linkedin.com/in/ganeshkumarm1) | [Github](https://github.com/ganeshkumarm1)


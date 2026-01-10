---
title: Big Theta and Asymptotic Notation Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T22:16:00.000Z'
originalURL: https://freecodecamp.org/news/big-theta-and-asymptotic-notation-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e1b740569d1a4ca3b63.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: null
seo_desc: "Big Omega tells us the lower bound of the runtime of a function, and Big\
  \ O tells us the upper bound. \nOften times, they are different and we can’t put\
  \ a guarantee on the runtime - it will vary between the two bounds and the inputs.\
  \ But what happens w..."
---

Big Omega tells us the lower bound of the runtime of a function, and Big O tells us the upper bound. 

Often times, they are different and we can’t put a guarantee on the runtime - it will vary between the two bounds and the inputs. But what happens when they’re the same? Then we can give a **theta** (Θ) bound - our function will run in that time, no matter what input we give it. 

In general, we always want to give a theta bound if possible because it is the most accurate and tightest bound. If we can’t give a theta bound, the next best thing is the tightest O bound possible.

Take, for example, a function that searches an array for the value 0:

```python
def containsZero(arr): #assume normal array of length n with no edge cases
  for num x in arr:
    if x == 0:
       return true
  return false
```

1. What’s the best case? Well, if the array we give it has 0 as the first value, it will take constant time: Ω (1)
2. What’s the worst case? If the array doesn’t contain 0, we will have iterated through the whole array: O(n)

We’ve given it an omega and O bound, so what about theta? We can’t give it one! Depending on the array we give it, the runtime will be somewhere in between constant and linear.

Let’s change our code a bit.

```python
def printNums(arr): #assume normal array of length n with no edge cases
  for num x in arr:
    print(x)
```

Can you think of a best case and worst case?? I can’t! No matter what array we give it, we have to iterate through every value in the array. So the function will take AT LEAST n time (Ω(n)), but we also know it won’t take any longer than n time (O(n)). What does this mean? Our function will take **exactly** n time: Θ(n).

If the bounds are confusing, think about it like this. We have 2 numbers, x and y. We are given that x <= y and that y <= x. If x is less than or equal to y, and y is less than or equal to x, then x has to equal y!

If you’re familiar with linked lists, test yourself and think about the runtimes for each of these functions!

1. get
2. remove
3. add

Things get even more interesting when you consider a doubly linked list!

## **Asymptotic Notation**

How do we measure the performance value of algorithms?

Consider how time is one of our most valuable resources. In computing, we can measure performance with the amount of time a process takes to complete. If the data processed by two algorithms is the same, we can decide on the best implementation to solve a problem.

We do this by defining the mathematical limits of an algorithm. These are the big-O, big-omega, and big-theta, or the asymptotic notations of an algorithm. On a graph the big-O would be the longest an algorithm could take for any given data set, or the “upper bound”. Big-omega is like the opposite of big-O, the “lower bound”. That’s where the algorithm reaches its top-speed for any data set. Big theta is either the exact performance value of the algorithm, or a useful range between narrow upper and lower bounds.

Some examples:

* “The delivery will be there within your lifetime.” (big-O, upper-bound)
* “I can pay you at least one dollar.” (big-omega, lower bound)
* “The high today will be 25ºC and the low will be 19ºC.” (big-theta, narrow)
* “It’s a kilometer walk to the beach.” (big-theta, exact)

#### **More Information:**

[https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-big-theta-notation](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-big-theta-notation) [https://stackoverflow.com/questions/10376740/what-exactly-does-big-%D3%A8-notation-represent](https://stackoverflow.com/questions/10376740/what-exactly-does-big-%D3%A8-notation-represent) [https://www.geeksforgeeks.org/analysis-of-algorithms-set-3asymptotic-notations/](https://www.geeksforgeeks.org/analysis-of-algorithms-set-3asymptotic-notations/)


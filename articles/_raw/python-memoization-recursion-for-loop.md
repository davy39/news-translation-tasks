---
title: Memoisation, Recursion, and For Loops in Python Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-11T17:48:27.000Z'
originalURL: https://freecodecamp.org/news/python-memoization-recursion-for-loop
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/martin-shreder-5Xwaj9gaR0g-unsplash.jpg
tags:
- name: Python
  slug: python
- name: Recursion
  slug: recursion
seo_title: null
seo_desc: 'By Diva Dugar


  There''s more than one way to do things. There''s always different points of views
  and styles of pitching. ~Tim Hudson


  In this article, we will use three different techniques in Python to code a basic
  Fibonacci program which will give t...'
---

By Diva Dugar

> _There's more than one way to do things. There's always different points of views and styles of pitching. ~_**_Tim Hudson_**

In this article, we will use three different techniques in Python to code a basic Fibonacci program which will give the sum of the sequence as a result. The Fibonacci sequence is 0,1,1,2,3,5,8...

As you may have noticed, we add the first and second numbers, 0 and 1, to get the third number in the sequence (1) -> 0+1=1. Then we add the second and third numbers, 1+1=2, to get the 4th number in the sequence...and so on.

You can implement this code in Jupyter, Colab or any IDE or text editor you feel comfortable with.

## How to Code the Fibonacci Sequence Using a For Loop in Python

Here, I have written a basic Fibonacci program using a for loop in Python. The logic behind this is simple and we already discussed it above.

The time complexity is O(N) and space complexity is O(1) or constant. But, it is actually more complicated than this complexity implies. 

> "If your number is less than _N < 94_, and you use a 64 bit integer, then the algorithm acts as a linear complexity. However, for _N > 94_ it starts to behave like a quadratic complexity algorithm." ~ [Michael Veksler](https://qr.ae/pNxAka)

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_foR_1.png)
_Printing a Fibonacci result using a For Loop_

I am going to run this with Python's `%timeit` module. This avoids a number of common traps for measuring execution times. You can see more uses [here](https://docs.python.org/3/library/timeit.html).

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_foR_R_1.png)
_It took 675 nanoSec per loop for 10_

## How to Code the Fibonacci Sequence with Recursion in Python

Here, we will implement the sequence using recursion. Recursive functions tend to call themselves on repeat until they reach the base case. So, recursion creates a tree structure. 

If we take a Fibonacci series of 5, this is the tree which will be created by recursion. 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_foR_R2_1.png)

The Space Complexity is O(N) and the Time complexity is O(2^N) because the root node has 2 children and 4 grandchildren. And, as you can see, every node has 2 children. 

Now the depth is N, which means that we have to do this N times. Also, you may have noticed that the right sub-tree is smaller than the left sub-tree, so the true runtime is roughly O(1.6^_N_).

The base case: _Fibonacci(2)_ = _Fib(1)_ + _Fib(0)_  = _1 + 0 = 1_

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_Recur_op_2.png)
_Printing Fibonacci result using Recursion_

The Recursive Fibonacci example is definitely faster than the for loop.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_Recur_R_2.png)

## How to Code the Fibonacci Sequence Using Memoisation in Python

Memoisation is a technique which can significantly improve a recursive function's performance by reducing the computational liability. 

It [stores the results of expensive function calls in an array](https://en.wikipedia.org/wiki/Memoization) or dictionary and returns the cached results when the same input is called. 

You can see the above tree for reference, and how certain inputs keep getting recomputed on each call to them. 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_Memo_op_3.png)
_Printing Fibonacci result using Memoisation_

The time complexity is O(nlogn). 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/serverCode_Memo_R_3.png)

## Which is better, recursion, for-loops, or memoisation?

Now, these techniques aren't supposed to be better than one another. You simply need to know when you need to use which one. Which of course depends on your requirements. 

Iteration will be faster than recursion because recursion has to deal with the recursive call stack frame. But, if recursion is written in a language which optimises the tail call, then it eliminates the overhead and is almost on par with for loops. 

Lastly, memoisation is better whenever the state space is sparse, that is not all smaller sub-problems need to be solved, but only a few of them.

_Thanks for reading! If you liked this article, you can **[read my other articles here](https://medium.com/@divadugar).** You can **show your appreciation for this article** by sharing it. Also you can **[connect with me on LinkedIn](https://www.linkedin.com/in/divadugar).**_


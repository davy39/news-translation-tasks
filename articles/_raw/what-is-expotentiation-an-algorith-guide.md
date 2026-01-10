---
title: What is Expotentiation? An Algorithm Guide with Code Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-28T18:36:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-expotentiation-an-algorith-guide
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ef8740569d1a4ca4020.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: null
seo_desc: "Given two integers a and n, write a function to compute a^n.\nCode\nAlgorithmic\
  \ Paradigm: Divide and conquer.\nint power(int x, unsigned int y) { \n    if (y\
  \ == 0) \n        return 1; \n    else if (y%2 == 0) \n        return power(x, y/2)*power(x,\
  \ y/2); \n ..."
---

Given two integers a and n, write a function to compute a^n.

#### Code

Algorithmic Paradigm: Divide and conquer.

```
int power(int x, unsigned int y) { 
    if (y == 0) 
        return 1; 
    else if (y%2 == 0) 
        return power(x, y/2)*power(x, y/2); 
    else
        return x*power(x, y/2)*power(x, y/2); 
} 

```

Time Complexity: `O(n)` | Space Complexity: `O(1)`

#### Optimized Solution: O(logn)

```
int power(int x, unsigned int y) { 
    int temp; 
    if( y == 0) 
        return 1; 
    temp = power(x, y/2); 
    if (y%2 == 0) 
        return temp*temp; 
    else
        return x*temp*temp; 
} 

```

Why is this faster?

Suppose we have x = 5, y = 4, we know that our answer is going to be (5 * 5 * 5 * 5).

If we break this down, we notice that we can write (5 * 5 * 5 * 5) as (5 * 5) * 2 and further, we can write (5 * 5) as 5 * 2.

Through this observation, we can optimize our function to O(log n) by calculating power(x, y/2) only once and storing it.

## Modular Exponentiation

Given three numbers x, y, and p, compute (x^y) % p

```
int power(int x, unsigned int y, int p) { 
    int res = 1;  
    x = x % p; 
    while (y > 0) {  
        if (y & 1) 
            res = (res*x) % p; 
  
        // y must be even now 
        y = y >> 1; 
        x = (x*x) % p;   
    } 
    return res; 
} 

```

Time Complexity: `O(Log y)`.


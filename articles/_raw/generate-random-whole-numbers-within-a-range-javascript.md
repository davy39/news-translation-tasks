---
title: How to Generate Random Whole Numbers within a Range using JavaScript Math.floor
  - Solved
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2019-11-28T18:02:00.000Z'
originalURL: https://freecodecamp.org/news/generate-random-whole-numbers-within-a-range-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ef9740569d1a4ca4026.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
seo_title: null
seo_desc: "Quick Solution\nfunction randomRange(myMin, myMax) {\n  return Math.floor(Math.random()\
  \ * (myMax - myMin + 1) + myMin);\n}\n\nCode Explanation\n\nMath.random() generates\
  \ our random number between 0 and ≈ 0.9.\nBefore multiplying it, it resolves the\
  \ part betw..."
---

## Quick Solution

```javascript
function randomRange(myMin, myMax) {
  return Math.floor(Math.random() * (myMax - myMin + 1) + myMin);
}

```

## Code Explanation

* `Math.random()` generates our random number between 0 and ≈ 0.9.
* Before multiplying it, it resolves the part between parenthesis `(myMax - myMin + 1)` because of the grouping operator `(   )`.
* The result of that multiplication is followed by adding `myMin` and then "rounded" to the largest integer less than or equal to it (eg: 9.9 would result in 9)

If the values were `myMin = 1, myMax= 10`, one result could be the following:

1. `Math.random() = 0.8244326990411024`
2. `(myMax - myMin + 1) = 10 - 1 + 1 -> 10`
3. `a * b =  8.244326990411024`
4. `c + myMin = 9.244326990411024`
5. `Math.floor(9.244326990411024) = 9`

`randomRange` should use both `myMax` and `myMin`, and return a random number in your range.

You cannot pass the test if you are only re-using the function `ourRandomRange` inside your `randomRange` formula. You need to write your own formula that uses the variables `myMax` and `myMin`. It will do the same job as using `ourRandomRange`, but ensures that you have understood the principles of the `Math.floor()` and `Math.random()` functions.


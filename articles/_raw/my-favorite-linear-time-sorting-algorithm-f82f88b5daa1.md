---
title: My Favorite Linear-time Sorting Algorithm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T22:15:56.000Z'
originalURL: https://freecodecamp.org/news/my-favorite-linear-time-sorting-algorithm-f82f88b5daa1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ub3PKyJ0IANMyfahqVk6EA.png
tags:
- name: algorithms
  slug: algorithms
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Franziska Hinkelmann

  Counting sort with a twist

  The problem: Given an unsorted array of numbers, find the maximum difference between
  the successive elements in its sorted form. The numbers can be negative or decimals.


  Given [21, 41, 17, 45, 9, 28...'
---

By Franziska Hinkelmann

#### Counting sort with a twist

**The problem:** Given an unsorted array of numbers, find the maximum difference between the successive elements in its sorted form. The numbers can be negative or decimals.

![Image](https://cdn-media-1.freecodecamp.org/images/mtqxI3ioTnLVE0O1wyHpGz6cOPCqbqfaLgNQ)
_Given [21, 41, 17, 45, 9, 28], the maximum difference is 13._

### Straightforward Algorithm

```
const maxGap = input =>  input    .sort((a, b) => a — b)    .reduce((acc, cur, idx…
```


---
title: Mon algorithme de tri linéaire préféré
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
seo_title: Mon algorithme de tri linéaire préféré
seo_desc: 'By Franziska Hinkelmann

  Counting sort with a twist

  The problem: Given an unsorted array of numbers, find the maximum difference between
  the successive elements in its sorted form. The numbers can be negative or decimals.


  Given [21, 41, 17, 45, 9, 28...'
---

Par Franziska Hinkelmann

#### Tri par comptage avec une touche spéciale

**Le problème :** Étant donné un tableau non trié de nombres, trouver la différence maximale entre les éléments successifs dans sa forme triée. Les nombres peuvent être négatifs ou décimaux.

![Image](https://cdn-media-1.freecodecamp.org/images/mtqxI3ioTnLVE0O1wyHpGz6cOPCqbqfaLgNQ)
_Étant donné [21, 41, 17, 45, 9, 28], la différence maximale est 13._

### Algorithme direct

```
const maxGap = input =>  input    .sort((a, b) => a — b)    .reduce((acc, cur, idx…
```
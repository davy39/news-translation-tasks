---
title: Euler's Method Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T18:49:00.000Z'
originalURL: https://freecodecamp.org/news/eulers-method-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d81740569d1a4ca3821.jpg
tags:
- name: Math
  slug: math
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'What is Euler’s Method?

  The Euler’s method is a first-order numerical procedure for solving ordinary differential
  equations (ODE) with a given initial value.

  The General Initial Value Problem


  Methodology

  Euler’s method uses the simple formula,


  to c...'
---

# **What is Euler’s Method?**

The Euler’s method is a first-order numerical procedure for solving ordinary differential equations (ODE) with a given initial value.

## **The General Initial Value Problem**

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn006.png)

## **Methodology**

Euler’s method uses the simple formula,

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn3.png)

to construct the tangent at the point `x` and obtain the value of `y(x+h)`, whose slope is,

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn008.png)

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/Euler.png)

In Euler’s method, you can approximate the curve of the solution by the tangent in each interval (that is, by a sequence of short line segments), at steps of `h`.

_In general_, if you use small step size, the accuracy of approximation increases.

## **General Formula**

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn7.png)

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn_new_2.png)

## **Functional value at any point `b`, given by `y(b)`**

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn6.png)

where,

* **n** = number of steps
* **h** = interval width (size of each step)

### **Pseudocode**

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn_new_1.png)

## **Example**

Find `y(1)`, given

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn007.png)

Solving analytically, the solution is _**y = e<sup>x</sup>**_ and `y(1)`= `2.71828`. (Note: This analytic solution is just for comparing the accuracy.)

Using Euler’s method, considering `h` = `0.2`, `0.1`, `0.01`, you can see the results in the diagram below.

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/comparison.png)

When `h` = `0.2`, `y(1)` = `2.48832` (error = 8.46 %)

When `h` = `0.1`, `y(1)` = `2.59374` (error = 4.58 %)

When `h` = `0.01`, `y(1)` = `2.70481` (error = 0.50 %)

You can notice, how accuracy improves when steps are small.


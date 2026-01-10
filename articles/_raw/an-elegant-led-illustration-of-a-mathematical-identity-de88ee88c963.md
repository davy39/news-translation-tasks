---
title: An elegant LED illustration of a mathematical identity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T19:10:21.000Z'
originalURL: https://freecodecamp.org/news/an-elegant-led-illustration-of-a-mathematical-identity-de88ee88c963
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jtP8OiDRsdDAdwBjyN5DGA.jpeg
tags:
- name: arduino
  slug: arduino
- name: coding
  slug: coding
- name: Electronics
  slug: electronics
- name: Mathematics
  slug: mathematics
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Chris Lam

  I am a big fan of science toys. I have been looking for one that combines the elegance
  of math and programming for a while. However, there was not much success in the
  search. So, I decided to make one myself.

  Here is a demo. The flashing...'
---

By Chris Lam

I am a big fan of science toys. I have been looking for one that combines the elegance of math and programming for a while. However, there was not much success in the search. So, I decided to make one myself.

Here is a demo. The flashing LEDs are used to illustrate a mathematical identity visually.

### Math

The mathematical identity is the following. The left side of the equation is an arithmetic sum from 1 to _n-1_ and the right side of the equation is “[n choose 2](https://en.wikipedia.org/wiki/Combination)”, the number of unique ways to choose 2 items from _n_ items.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XZUYnypW2Qb9XLxW7VIC7g.png)
_Mathematical identity_

It is not the identity itself that is elegant, but the visual proof itself. Let’s look at the diagram below. There are _n=4_ green dots in the illustration.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jtP8OiDRsdDAdwBjyN5DGA.jpeg)
_LED illustration_

For every two green dots on the bottom row, there is always a unique red dot in the triangle above that corresponds to them. That red dot is the tip of an equilateral triangle with the base specified by the green dots.

Therefore, the number of ways to choose 2 green dots out of _n_ green dots is equal to the sum of the red dots, 1 +2 + 3 + … + (_n_-1).

In this case, it is 1 + 2 + (4 –1) = 6.

This observation was originally made by Loren C. Larson in [this article](https://www.tandfonline.com/doi/abs/10.1080/07468342.1985.11972910?journalCode=ucmj20&).

### Programming

While it is easy to trace the red dot from the green dots visually, it is more fun and challenging to specify the relationship in code.

Let us assume that we know the indices of the green dots (say, i and j). The programming challenge is to specify the corresponding index of the red dot that forms the equilateral triangle with the green dots.

It looks difficult at first glance.

But the problem can be simplified a lot when we tweak the way that we label the red dots. We can label the red dots from bottom-up instead of top-down.

With that indexing scheme, we can then specify the index of the red dots by the following formula.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cNwsj8hBqeC6HF1pz1dotg.jpeg)
_An illustration of how to index the red dots using the indices of the green dots._

Here is the complete code used to flash the LEDs using Arduino.

### Electronics

I solder the LEDs on a board and connect the LEDs to Arduino output pins through 1k resistors. It is very important to use the resistors because they protect the LEDs.

The connection is as follows.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AGo0vjfM8z5LmZmtOXMiJQ.jpeg)
_Schematics_

And when you put them together and load the software to Arduino, it will start flashing like below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xggk2l3AY4vi5ZtN-KZYgw.jpeg)
_Final result_

Hope you enjoy this gadget!


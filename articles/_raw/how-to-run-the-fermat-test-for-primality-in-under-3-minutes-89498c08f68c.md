---
title: How to run the Fermat test for primality in under 3 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-22T15:24:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-the-fermat-test-for-primality-in-under-3-minutes-89498c08f68c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZILryLJXlIQxX1i-nKRPtw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Functional Programming
  slug: functional-programming
- name: Mathematics
  slug: mathematics
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Devesh Shetty

  The Fermat test is based on a result from number theory known as Fermat’s little
  theorem.

  According to Fermat’s little theorem, if n is a prime number and d is any positive
  integer less than n, then d raised to the nth power is congr...'
---

By Devesh Shetty

The Fermat test is based on a result from number theory known as Fermat’s little theorem.

According to Fermat’s little theorem, if _n_ is a prime number and _d_ is any positive integer less than _n_, then _d_ raised to the _nth_ power is congruent to _d_ modulo _n_.

If two numbers have the same remainder when divided by _n_ then they are said to be _congruent modulo n_. _d_ _modulo n_ is simply the remainder of a number _d_ when divided by _n_.

For example, 34 is congruent to 16 (modulo 3) as   
34 modulo 3 = 1 and 16 modulo 3 = 1.

#### Fermat test for primality

1. For a given number _n_, pick a random positive number _d_ such that _d <_; n.
2. Calculate _(d^n) modulo n_.
3. _d modulo n_ is always going to be _d_ as we always pick _d_ that satisfies the condition _d <_; n.
4. If the result of _(d^n) modulo n_ is not equal to _d_, then _d_ is certainly not prime.
5. If the result of _(d^n) modulo n_ is equal to _d_, then the chances are good that _n_ is prime.
6. Pick another random _d_ that satisfies the condition _d <_ n and repeat the above steps.

**Note**: The examples in this post use [Swift 4.1](https://swift.org/blog/swift-4-1-released/)

We need a function to calculate the exponential of a number modulo another number.

![Image](https://cdn-media-1.freecodecamp.org/images/xo3yNSnDQAS1sAk0KnD7kTLNpwDQtiqnDJlp)
_Calculate (d^n) modulo n_

We use [modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation) to compute values when the exponent is greater than 1 as this lets us perform computation while only dealing with numbers less than _n_ (_modulo_ in the above function).

![Image](https://cdn-media-1.freecodecamp.org/images/orqRbwqC3uRbSiX15dGgDg7GmZAxYPRRS43l)
_The Fermat test_

The Fermat test chooses at random a number _d_ between 1 and _n-1_ (_number — 1_ in the above function) inclusive. The aim is to check whether the remainder modulo n of the nth power of d is equal to d.

![Image](https://cdn-media-1.freecodecamp.org/images/jNeeRWHFVv2TIeNPZORAqFJHH5IXXyv70sTS)
_Run the Fermat test for the specified count_

The Fermat test is run for the specified count. If a number fails the Fermat test, we are assured that it is not prime. If a number passes the Fermat test, it is not guaranteed to be prime. We try to reduce the probability of error in our primality test by running the test enough times.

By trying more and more values of _d_ (a random positive number between 1 and n-1), we can increase our confidence in the result.


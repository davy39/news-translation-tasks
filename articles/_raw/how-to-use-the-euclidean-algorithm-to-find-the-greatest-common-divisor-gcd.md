---
title: How to Use the Euclidean Algorithm to find the Greatest Common Divisor (GCD)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T22:39:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-euclidean-algorithm-to-find-the-greatest-common-divisor-gcd
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e4c740569d1a4ca3c63.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: null
seo_desc: 'For this topic you must know about the Greatest Common Divisor (GCD) and
  the MOD operation first.

  Greatest Common Divisor (GCD)

  The GCD of two or more integers is the largest integer that divides each of the
  integers such that their remainder is zero...'
---

For this topic you must know about the Greatest Common Divisor (GCD) and the MOD operation first.

### Greatest Common Divisor (GCD)

The GCD of two or more integers is the largest integer that divides each of the integers such that their remainder is zero.

Here's an example:

GCD of 20, 30 = 10 (10 is the largest number which divides 20 and 30 with remainder of 0)  
GCD of 42, 120, 285 = 3 (3 is the largest number which divides 42, 120 and 285 with remainder of 0)

### “mod” Operation

The mod operation gives you the remainder when two positive integers are divided. We write it as follows:  
`A mod B = R`

This means, dividing A by B gives you the remainder R. This is different than your division operation which gives you the quotient.

Here's an example:

7 mod 2 = 1 _(Dividing 7 by 2 gives the remainder 1)_  
42 mod 7 = 0 _(Dividing 42 by 7 gives the remainder 0)_

If you understand the above two concepts you will easily understand the Euclidean Algorithm.

## Euclidean Algorithm for Greatest Common Divisor (GCD)

The Euclidean Algorithm finds the GCD of 2 numbers.

You will better understand this Algorithm by seeing it in action. Assuming you want to calculate the GCD of 1220 and 516, let's apply the Euclidean Algorithm.

Pseudo Code of the Algorithm:

Step 1: **Let `a, b` be the two numbers**  
Step 2: **`a mod b = R`**  
Step 3: **Let `a = b` and `b = R`**  
Step 4: **Repeat Steps 2 and 3 until `a mod b` is greater than 0**  
Step 5: **GCD = b**  
Step 6: Finish

Here's the Javascript Code to Perform GCD:

```javascript
function gcd(a, b) {
  var R;
  while ((a % b) > 0)  {
    R = a % b;
    a = b;
    b = R;
  }
  return b;
}
```

Here's the Javascript Code to Perform GCD using Recursion:

```javascript
function gcd(a, b) {
  if (b == 0)
    return a;
  else
    return gcd(b, (a % b));
}
```

You can also use the Euclidean Algorithm to find GCD of more than two numbers. Since GCD is associative, the following operation is valid:  `GCD(a,b,c) == GCD(GCD(a,b), c)`

Calculate the GCD of the first two numbers, then find GCD of the result and the next number. Example: `GCD(203,91,77) == GCD(GCD(203,91),77) == GCD(7, 77) == 7`

You can find GCD of `n` numbers in the same way.


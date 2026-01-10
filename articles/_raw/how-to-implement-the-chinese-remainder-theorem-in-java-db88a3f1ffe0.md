---
title: How to implement the Chinese Remainder Theorem in Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T22:06:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-the-chinese-remainder-theorem-in-java-db88a3f1ffe0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*wyjesOXusRqfQ_BG
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: cybersecurity
  slug: cybersecurity
- name: Java
  slug: java
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Anuj Pahade

  This post assumes that you know what Chinese Remainder Theorem (CRT) is and focuses
  on its implementation in Java. If you don’t, I’d recommend you read about it here.

  You can find the link to the complete code at the end of this post. ...'
---

By Anuj Pahade

This post assumes that you know what Chinese Remainder Theorem (CRT) is and focuses on its implementation in Java. If you don’t, I’d recommend you read about it [here](https://en.wikipedia.org/wiki/Chinese_remainder_theorem).

You can find the link to the complete code at the end of this post. So let’s get started.

#### What do we need to find?

We need to find X. ?

The statement goes as follows:

There exists a _minimum positive number_ X such that:

```
X % number[0]    =  remainder[0], X % number[1]    =  remainder[1], ...............X % number[k-1]  =  remainder[k-1]
```

So, here we have two arrays.

1. **The array of numbers:** All the numbers in this array are pairwise relatively prime. Which means, pick any two numbers from the array, you’ll find that their greatest common divisor is 1.
2. **The array of remainders:** As you can see in the expressions above, when X is divided by a number _n_ from the _number_ array it leaves a respective remainder from the _remainder_ array.

### Steps to implement the CRT

These are the steps, or as we engineers say, the ‘algorithm’, to implement CRT.

#### Step 1: Find the product of all the numbers in the first array.

```
for(int i=0; i<number.length; i++ ){   product *= number[i];}
```

#### Step 2: Find the partial product of each number.

Partial product of _n_= product/_n_

```
for(int i=0; i<num.length; i++){   partialProduct[i] = product/number[i];}
```

#### 3. Find the modular multiplicative inverse of number[i] modulo partialProduct[i].

Here we find the inverse using the [extended Euclidean algorithm](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/). So, we call _computeInverse(partialProduct[i],num[i])_

```
public static int computeInverse(int a, int b){         int m = b, t, q;         int x = 0, y = 1;               if (b == 1)             return 0;               // Apply extended Euclid Algorithm         while (a > 1)         {             // q is quotient             q = a / b;             t = b;                   // now proceed same as Euclid's algorithm             b = a % b;a = t;             t = x;             x = y - q * x;             y = t;         }               // Make x1 positive         if (y < 0)          y += m;               return y;     }
```

#### Step 4: Final Sum

```
sum += partialProduct[i] * inverse[i] * rem[i];
```

#### Step 5: Return the smallest X

In order to find the smallest of all solutions, we divide the sum from step 4 by the product from step 2.

```
return sum % product;
```

Thus, we have found our X. I’d recommend you to try to implement the code on your own before looking at the code in the link below.

Thanks for reading the post. I hope it helped you. Leave suggestions in the comments below or reach out to me with a better version of [this code](https://github.com/anujpahade/CRT) or queries on anujp5678[at]gmail[dot]com or connect with [me on LinkedIn](https://www.linkedin.com/in/anuj-pahade/).

Please clap. ? Claps motivate.

Have fun and happy coding! :)


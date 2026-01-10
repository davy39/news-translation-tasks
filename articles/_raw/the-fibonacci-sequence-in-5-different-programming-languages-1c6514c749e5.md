---
title: The Fibonacci Sequence –  Explained in Python, JavaScript, C++, Java, and Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-01T15:38:00.000Z'
originalURL: https://freecodecamp.org/news/the-fibonacci-sequence-in-5-different-programming-languages-1c6514c749e5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*74G0BbEUwrCaw8iQ.
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Pau Pavón

  The Fibonacci sequence is, by definition, the integer sequence in which every number
  after the first two is the sum of the two preceding numbers. To simplify:

  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

  It has many applications in ma...'
---

By Pau Pavón

The Fibonacci sequence is, by definition, the integer sequence in which every number after the first two is the sum of the two preceding numbers. To simplify:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

It has many applications in mathematics and even trading (yes, you read that right: trading), but that’s not the point of this article. My goal today is to show you how you can compute any term of this series of numbers in five different programming languages using recursive functions.

Recursive functions are those functions which, basically, call themselves.

I want to note that this isn’t the best method to do it — in fact, it could be considered the most basic method for this purpose. This is because the computing power required to calculate larger terms of the series is immense. The number of times the function is called causes a stack overflow in most languages.

All the same, for the purposes of this tutorial, let’s begin.

First of all, let’s think about what the code is going to look like. It’ll include:

· A recursive function F (F for Fibonacci): to compute the value of the next term.

· Nothing else: I warned you it was quite basic.

Our function will take _n_ as an input, which will refer to the _n_th term of the sequence that we want to be computed. So, F(4) should return the fourth term of the sequence.

Let’s plan it. The code should, regardless the language, look something like this:

[`function F(n)  if n = 0`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return 0  if n = 1`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return 1  else`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return F(n-1) + F(n-2)`](https://unsplash.com?utm_source=medium&utm_medium=referral)

Note: the term 0 of the sequence will be considered to be 0, so the first term will be 1; the second, 1; the third, 2; and so on. You get it.

Let’s analyze the function for a moment. If it gets 0 as an input, it returns 0. If it gets 1, it returns 1. If it gets 2… Well, in that case it falls into the else statement, which will call the function again for terms 2–1 (1) and 2–2 (0). That will return 1 and 0, and the two results will be added, returning 1. Perfect.

Now you can see why recursive functions are a problem in some cases. Imagine you wanted the 100th term of the sequence. The function would call itself for the 99th and the 98th, which would themselves call the function again for the 98th and 97th, and 97th and 96th terms…and so on. It would be **really** slow.

But the good news is that it actually works!

So let’s start with the different languages. I won’t give too much detail (actually, no detail at all) to make your reading experience better. There isn’t too much to detail anyways.

Let’s jump into it:

### Python

[`def F(n):  if n == 0:`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return 0  if n == 1:`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return 1  else:`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
    [`return F(n-1) + F(n-2)`](https://unsplash.com?utm_source=medium&utm_medium=referral)

### Swift

[`func F(_ n: Int) -> Int {  if n == 0 {    return 0`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  if n == 1 {    return 1`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  else {    return F(n-1) + F(n-2)`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}}`](https://unsplash.com?utm_source=medium&utm_medium=referral)

### JavaScript

[`function F(n) {  if(n == 0) {    return 0;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  if(n == 1) {    return 1;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  else {    return F(n-1) + F(n-2);`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}}`](https://unsplash.com?utm_source=medium&utm_medium=referral)

### Java

[`public static int F(int n) {  if(n == 0) {    return 0;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  if(n == 1) {    return 1;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  else {    return F(n-1) + F(n-2);`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}}`](https://unsplash.com?utm_source=medium&utm_medium=referral)

### C++

[`int F(int n) {  if(n == 0) {    return 0;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  if(n == 1) {    return 1;`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}  else {    return F(n-1) + F(n-2);`](https://unsplash.com?utm_source=medium&utm_medium=referral)  
  [`}}`](https://unsplash.com?utm_source=medium&utm_medium=referral)

And that’s it. I chose these languages just based on popularity — or at least because these 5 are the most common ones that I use They’re in no particular order. They could be classified by syntax difficulty, in my opinion, from Python (easiest) to C++ (hardest). But that depends on your personal opinion and your experience with each language.

I hope you liked this article and, if you have any questions/recommendations or just want to say hi, comment below!


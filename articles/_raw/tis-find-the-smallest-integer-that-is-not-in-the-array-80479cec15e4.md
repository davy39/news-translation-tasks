---
title: 'Today I Spaced: how to find the smallest number that is not in the array'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-06T11:01:02.000Z'
originalURL: https://freecodecamp.org/news/tis-find-the-smallest-integer-that-is-not-in-the-array-80479cec15e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uGGUGY-TAtzH7-XYMdzzvQ.jpeg
tags:
- name: Today I Spaced
  slug: today-i-spaced
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Marin Abernethy

  TIS in my first technical interview. Here’s what I learned.


  ID 48395285 © Ojogabonitoo | Dreamstime.com

  Today I Spaced in my first technical interview, and could barely rememberhow to
  console.log()let alone find an optimal solutio...'
---

By Marin Abernethy

#### TIS in my first technical interview. Here’s what I learned.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uGGUGY-TAtzH7-XYMdzzvQ.jpeg)
_ID 48395285 © Ojogabonitoo | Dreamstime.com_

Today I Spaced in my first technical interview, and could barely remember  
how to `console.log()`let alone find an optimal solution.

First, a one sentence summary of my software journey: for a couple of years after my BA, I worked for a small software consultancy as a full stack developer before getting my Masters in Software Engineering, which I finished this year.

Woah, ok. Maybe that should have been two sentences. Point is, I used to feel confident in my engineering capabilities, but the pressure of interviews has caused that confidence to wane slightly.

I spaced in my first technical phone interview today while live coding, but I  
hope my Today I Spaced (TIS) moment will turn into a Today I Learned (TIL) after a walkthrough of my interview. Here goes nothing…

### The problem

The interviewer framed the question in the context of the product the company builds, but it boils down to this: Given an array of integers, write a function that finds the lowest integer that is **not** in the array.

For example, given the array, `[5, 2, 1, 4, 0, 2]` , the function should return `3`.

Simple, right? Let the spacing commence.

### **Where I went wrong**

Hmm where do I start? As soon as the interviewer finished explaining the question, internal panic ensued. I couldn’t think.

**Inner monologue:** _THINK Marin, THINK. Why aren’t you even trying to think about the problem? Aha! Google always knows. Yo Google, tell me what to do… Oh, wait I am supposed to talk. All of the advice online says I should talk through my thought process. Ahhh ok ok ok. I can't read and talk at the same time. Fine, bye Google._

**Outer monologue**: “Ummm, ah, well… let's see. Hmmm. Yeah so, hm.”

After a few minutes of hemming and hawing, plus a minute or two of  
silence, I came up with this solution (in JavaScript):

Remember how I said I couldn’t even recall how to `console.log()`? Well, after completing my first attempt, I was confused when [Coderpad](https://coderpad.io/) ran my function and nothing appeared on the screen. The interviewer had to remind me that it was, indeed, compiling properly, I just needed to `console.log()` if I wanted to see the output in the console. Doh. Cue face to palm.

So I updated it: `console.log(count)`. And it returned the correct answer! Wahooo! …Can I go home now?

“Alright, now what is the time complexity of this algorithm?” the interviewer asked. I had printed out a list of different complexities to help me if it came up. Turns out I can’t read when I am nervous.

_THINK, Marin. THINK._ Well, my solution is just a single loop, right? `Loop === Constant` was scribbled on my printout. So I said “Constant, O(n) time”, without giving it much more thought.

_WRONG_. Yes, I did write one `while` loop. However, I failed to recognize the JavaScript `includes()` function as anything other than magic. When pushed on this point by the interviewer, I realized that `includes()` is also iterating through the array each time. So really, its O(n²) time complexity. Cue face to palm round two.

For one brief moment, the wheels started turning. What data structures have I been reading about? Linked List? Doesn’t seem helpful. Stack? Nah. HashTable? Aha!

### Towards a Solution

Attempt number two:

So I figured I could map each integer in the array to their frequency. Upon review of this solution post-interview, I realized it is unnecessary to keep track of how many times an integer appeared in the array. We just need to know whether it appeared at all, so the boolean `true` would have sufficed. Either way, this is O(n) time complexity.

Due to the limited remaining time, the interviewer asked me how I would solve this with only arrays. _Ding!_ I said, “you could sort the array, and then iterate through it until there is a missing number”. Here is what I meant by that:

Looking back, I see that not only could I have given a clearer explanation, but I should also have discussed the tradeoffs between this and my hashmap solution. That is, because this solution is done [in-place](https://www.geeksforgeeks.org/in-place-algorithm/), the space complexity is O(1) which is superior to the hashmap solution with O(n). However, it is safe to assume the sorting algorithm is O(n log n) time complexity, which is less efficient than the previous solution.

_Sigh_. More practice! More Interviews! Stay tuned.

### **TL;DR**

My brain, given the choice of fight or flight, when faced with an intimidating technical interview, chose flight. Maybe with a little more practice, it will choose to fight next time.

Note to self:

* Talk through a solution before coding it up. This may help you discover a more efficient solution sooner (e.g. the interviewer can be more than a sounding board, they sometimes give hints)
* Yes, talking through your answer is important, but not to the detriment of your final solution. Take a beat to think, if necessary.
* Internal JavaScript functions aren’t magic! They have time and space complexity too.


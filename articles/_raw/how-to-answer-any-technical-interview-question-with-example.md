---
title: How to Answer Any Technical Interview Question – Example Included
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-17T17:48:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-answer-any-technical-interview-question-with-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99a9740569d1a4ca2106.jpg
tags:
- name: coding interview
  slug: coding-interview
- name: interview questions
  slug: interview-questions
- name: Interview tips
  slug: interview-tips
- name: Job Interview
  slug: job-interview
seo_title: null
seo_desc: "By Sameer Khoja\nTechnical interviews can be extremely daunting. From the\
  \ beginning of each question to the end, it's important to know what to expect,\
  \ and to be aware of the areas you might be asked about. \nFortunately, there's\
  \ a way to prepare for a..."
---

By Sameer Khoja

Technical interviews can be extremely daunting. From the beginning of each question to the end, it's important to know what to expect, and to be aware of the areas you might be asked about. 

Fortunately, there's a way to prepare for any question that may come your way. It involves four parts:

1. **Understand the question**
2. **Discuss tradeoffs of solutions**
3. **Write the code**
4. **Test the code**

Let's try this technique with sample problem involving LinkedLists.

## The Problem

**Question:** Given two singly LinkedListNodes, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. If the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, they are intersecting.

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F13a33ada-6399-4679-a631-0e43be042886_1076x292.png)

## Step 1: Understand the question.

It's really important to know exactly what this question is asking. Some questions we could ask the interviewer are:

1. What exactly do we want to return? _(A: The intersecting node)._
2. Does that mean we can assume the linked lists always intersect? _(A: Yes)_

It's always important to gain a sense of the question before thinking about the approach to solving.

## Step 2: Discuss the tradeoffs of different solutions.

One immediate solution is to traverse both linked lists at the same time until you reach an intersection. For this example, we would make a **pointer** at nodes 2 and 7, and **traverse** each of them one-by-one until we reach a common node.

However, as you may have noticed, this will not work as the lengths of the two LinkedLists may differ. What we want to do essentially is “chop off” the beginning part of the longer LinkedListNode, and then iterate repeatedly.

This would be the kind of conversation to have with your interviewer.

## Step 3: Write the code.

Below is the method to achieve this.

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa761d963-8a59-4c0a-bd90-489931e6c5e2_1330x660.png)

We make use of **helper methods** here. We use `getKthNode()` to get the kth node of the given linked list. This is helpful when traversing the longer linked list to “chop off” extra nodes. 

We also use `getTailAndSize()` which captures both the length and the last node of the given list. This is helpful because we definitely need the size to compare lengths of the lists. We also need the tails because if the tails of the two lists are unequal, then they don’t intersect at all. 

Note that when we say “unequal”, we mean that the two nodes do not reference the same **object**. Even though they may have the same value and look identical, they must reference the same LinkedListNode to count as equal. (You can find more information on this [here](http://shortn/_xLxPLI0JXV).) 

Going back to the question, if we come across the case where the tails are unequal, we return a failed value (null).

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa50b3b05-93d6-4f2b-bd40-1b2127c18490_1072x966.png)

## Step 4: Test the code.

Below are some good test cases we can add. A helpful rule of thumb for test cases is the following:

* Empty/null case
* Considering options in the middle/beginning/end
* Sizes equal or different

This strategy doesn't only apply to LinkedList questions – this would work for arrays, Strings, and essentially any other data structure. 

For this question, our LinkedList tests would be the following:

* Two linked lists which intersect at the beginning/middle/end
* Both/one linked list is null (should return null)
* Linked lists are the same/different size

We’re done!

![Coding GIF by memecandy](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8cae3ba9-33c1-4c92-a8ea-fb0119929389_300x300.gif)

**More Questions:**

* [Circular Linked List](https://leetcode.com/problems/linked-list-cycle/)
* [Reversing a Linked List](https://leetcode.com/problems/reverse-linked-list/)
* [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

_Interested in breaking into Computer Science? Eager to expand your knowledge base and learn new things? Enjoy problem solving?_ 

_If so, [SWEPrep](http://sweprep.com) may be the newsletter for you. Subscribe to get fully explained interview prompts commonly given in engineering interviews, from Arrays to Dynamic Programming. Questions come out weekly and are also categorized by subject and difficulty. The above post is a Guest Post from the author, Sameer Khoja._

  
_[Subscribe](http://sweprep.com) to get full access to the newsletter. Never miss an update._


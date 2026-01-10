---
title: 'Linear Data Structures: Linked Lists, Stacks, and Queues in JS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T14:09:52.000Z'
originalURL: https://freecodecamp.org/news/linear-data-structures-linked-lists-stacks-and-queues-in-javascript-a13c7591ad87
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AlfSJzw3bKoEHHaO9oiMqQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Yung L. Leung

  Building from Simple Algorithms & Data Structures in JS, here we’ll look at data
  structures beyond arrays and key-value objects, beyond “labelled & deposit” boxes.
  Like a road along a path, linked lists, stacks & queues are direct wa...'
---

By Yung L. Leung

Building from [Simple Algorithms & Data Structures in JS](https://medium.freecodecamp.org/a-step-towards-computing-as-a-science-algorithms-data-structures-4c0e2d6ae79a?source=friends_link&sk=1291dffce9f32b30f36339d59a66e12c), here we’ll look at data structures beyond arrays and key-value objects, beyond “labelled & deposit” boxes. Like a road along a path, **linked lists**, **stacks** & **queues** are direct ways to move from one unit of data to the next.

### Linked Lists

A **linked list** is like a set of boxes chained together and stored in a dark room. To get to any one box requires starting at one end (head or tail) and following the links, from one box to the next. Upon arriving at any one box, you are pointed towards the direction of the next box. **There is no index** to act as a guide for leaping to any one box.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kaShgNb9EtR7ps6odxP3QA.png)
_[source](https://www.blackline.com/blog/rpa/blockchain-finance-6-things/" rel="noopener" target="_blank" title=")_

You can easily **unshift** or **push** “boxes” to the head or tail of the linked list. You can also easily **shift** or **pop** off “boxes” from the head or tail. The head or tail are easily accessible. But, to **insert** or **remove** “boxes” along the body of this linked list, to **set** items into a “box” that is beyond the head or tail, is more difficult. It requires starting at the head (or tail) and moving from a current “box” to the next one, before you can **get** to your desired “box.”

A **singly linked list** is a one-way linked list. This means that you can only move forward from the head to the tail. The complexity to **unshift** & **shift** is a constant (**O(1)**). This is because adding a “box” to or removing it from the beginning requires only accessing the head of the list. The complexity to **push** a “box” to the end is also **O(1)** for a similar reason, the tail is immediately accessible.

But, to **pop** off the tail requires reassigning a new tail, which is reachable only by moving forward starting from the head, hence a linear complexity (**O(n)**). An **n** number of “boxes” requires **n** number of steps (operations) to reach the second to last “box” & reassign it as the new tail. Similarly, to **insert/remove** a “box,” or to **get/set** items in any “box” along the body of a list requires traveling from the head, and so their complexities are in general **O(n)**.

A **doubly linked list** is a two-way linked list. This means you can move forward from the head or the tail. An advantage is that both the head & tail are easily accessible to add “boxes” to or remove “boxes” from. The complexity to **unshift**, **shift**, **push** or **pop** is **O(1)**. The new tail required for popping a tail off is reachable from the current tail.

Another advantage of being able to travel from two different end points (head or tail) is that to **insert/remove** any “box” or to **get/set** “items” in a “box” along the body of a list takes half the time of a singly linked list. That is, their complexities are **half of O(n)**. If the “box” or “item” is located at the 2nd half of the list, traveling from the tail will not require traveling through the 1st half of the list. The opposite is also true. Although, an **O(1/2 n)** tends to be simplified as **O(n)**.

### Stacks

A **stack** is a pile of items neatly arranged atop each other. A new item can be **pushed** onto the top of a stack, one at a time, building to the height of the stack. Reversely, each item can be **popped** off, one at a time, from the top of the stack. The last item in is always the first item out (**LIFO**).

![Image](https://cdn-media-1.freecodecamp.org/images/1*H0FjbIyvwvDMrw0OCqyCwQ.jpeg)
_Annie Spratt from [UnSplash](https://unsplash.com/photos/thI_CZAB0MY" rel="noopener" target="_blank" title=")_

Since a stack operates by a LIFO process, the complexity to **push** an item to the top of the stack or to **pop** it off is a constant of **O(1)**. The top of the stack is easily accessible.

### Queues

A **queue** is a line of items, neatly arranged next to each other. A new item can be **enqueued** to the end of the line, one at a time, elongating the line. Reversely, each item can be **dequeued** from the front of the line, one at a time. The first item in is always the first item out (**FIFO**).

![Image](https://cdn-media-1.freecodecamp.org/images/1*hRd8rEZW87TbU1_uc6xCQw.jpeg)
_[source](http://www.communityvoiceks.com/news/wichita_news/sedgwick-county-treasurer-launches-new-virtual-waiting-line-process/article_e1fce0c2-f05f-11e5-979b-93e21092f3d5.html" rel="noopener" target="_blank" title=")_

Since both the front & end of the line is easily accessible, a queue’s **enqueue** & **dequeue** have a complexity of **O(1)**.

Thanks for reading!

### Reference:

[https://www.udemy.com/js-algorithms-and-data-structures-masterclass/](https://www.udemy.com/js-algorithms-and-data-structures-masterclass/)


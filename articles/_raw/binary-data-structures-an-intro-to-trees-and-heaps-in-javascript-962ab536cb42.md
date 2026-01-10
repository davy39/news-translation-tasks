---
title: 'Binary data structures: an intro to trees and heaps in JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-20T21:24:05.000Z'
originalURL: https://freecodecamp.org/news/binary-data-structures-an-intro-to-trees-and-heaps-in-javascript-962ab536cb42
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zrltwsvmiJBwYBZ2g6uiOg.jpeg
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

  Linear data structures are simple in direction. A linked list is a list of nodes
  (each containing their own data) that are linked from one node to the next (and
  to the previous, for a doubly linked list). A stack builds upward like a...'
---

By Yung L. Leung

[**Linear data structures**](https://medium.freecodecamp.org/linear-data-structures-linked-lists-stacks-queues-a13c7591ad87) are simple in direction. A **linked list** is a list of nodes (each containing their own data) that are linked from one node to the next (and to the previous, for a doubly linked list). A **stack** builds upward like a tower of data. Each node stacking atop another, and shortens in a **last in first out (**LIFO**)** manner. A **queue** is a line of nodes that elongate from the end of the line and shortens in a **first in first out (**FIFO**)** mechanism.

**Binary data structures** are like a fork in a road of data. The nodes build like the branches of a **tree** or a **heap** of rocks.

### Trees

![Image](https://cdn-media-1.freecodecamp.org/images/pt4Jg1dZ90bHVIsMWmfT0O5bI3FPflW53AGf)
_[source](https://www.rosettacode.org/mw/images/a/a3/Fractal_tree_bbc.gif" rel="noopener" target="_blank" title=")_

A **binary search tree** is made up of nodes that branch off to no more than two nodes (binary). A parent node can have left and right child nodes. By convention, left child nodes contain values less than the parent. Whereas right child nodes contain greater values (**left is less, right is greater**). All trees begin with a single root node.

![Image](https://cdn-media-1.freecodecamp.org/images/msMkP14InEQYWfg8eWglyjdXhZ5SrojngUPm)
_A root branches off into two parents of leaves. Leaves (green) are nodes without children._

To **insert** a value requires creating a **new node**, comparing its value to the **root** & its **descendant** values, while deciding to search further leftward (insertion of lesser value) or rightward (insertion of greater value). Once an available position is found, the node is inserted in place.

![Image](https://cdn-media-1.freecodecamp.org/images/ZSfQBHy1ZvdXm5A304q1jFMOZpAamWG1F4Ae)
_**Insertion of the node with a value of 6**_

To **find** a value is similar to the insertion of a value. You are performing the search for a stored value and returning the node containing it.

![Image](https://cdn-media-1.freecodecamp.org/images/dSrg3P7BVUiquGDvZYHwvCfVW9AgK4HeuaMC)
_**Finding the node with a value of 6**_

To make a **breadth-first search** of values requires storing a root value. Then proceeding with the left child, then the right child and so forth.

![Image](https://cdn-media-1.freecodecamp.org/images/MgGzdIJ78U3kLa-qh-AezTkzNYDsCOo4MB6j)
_**Breadth First Search returns [3, 1, 5, 0, 2, 4, 6]**_

To make a **depth-first search (**pre-order**)** of values requires storing a root value. Then proceeding with all leftward descendants, before the rightward descendants.

![Image](https://cdn-media-1.freecodecamp.org/images/VhYpkEBTORBiFDgRHEJAHOpSO5dVTH6h0IBe)
_**Depth First Search Pre — Order returns [3, 1, 0, 2, 5, 4, 6]**_

Since **inserting** & **finding** a node of some value are relatively similar processes (insertion inserts a node whereas finding returns a node), it is of no surprise that their complexity is the same, **O(log n)**.

![Image](https://cdn-media-1.freecodecamp.org/images/3WWlcSbWBhhv7P-lPxF-hbaQ8Kq7vyoqvcKw)
_**n = 3**_

For a 3 node **binary search tree**, to **find** **5** requires two steps:

* Is **5** greater than or less than 3? Proceed rightward.
* Is **5** equal to the value being searched? Return node.

Similarly to **insert** a node with value 6 requires two steps:

* Is **6** greater than or less than 3? Proceed rightward.
* Is **6** greater than or less than 5? Insert the right side.

### Heaps

![Image](https://cdn-media-1.freecodecamp.org/images/d1JWsgkTF-HSMsfHQw-QJt6OcGDfQBOk8OGe)
_Photo by Nick Tong on [Unsplash](https://unsplash.com/photos/zjy2yMUGzRU" rel="noopener" target="_blank" title=")_

A **binary heap** is a pyramidal structure of nodes whose nodes can stack upward with rows of decreasing values toward a minimum (**minimum binary heap**) or with rows of increasing values toward a maximum (**maximum binary heap**). Like the tree, each parent node can extend up to two child nodes. Unlike the tree, each parent can contain a lesser value than its children (**minimum binary heap**) or a greater value (**maximum binary heap**).

![Image](https://cdn-media-1.freecodecamp.org/images/HE8SQ3qiyd19h6kZOCpp8griQB2cOIXcV4L6)
_Max Binary Heap_

For a **max binary heap**, to **insert** a value at the base of the pyramid requires comparing it to parent nodes and **bubbling up** the larger value.

![Image](https://cdn-media-1.freecodecamp.org/images/v7W4gtqZZ4vknoz9-Qj28CuXtviStsYYXAS8)
_**Insertion of a node with a value of 6 &amp; bubbling it upward.**_

To **extract a max** value requires removing the apex value and **sinking down** a value from the pyramid’s base. This involves finding the higher of the two children nodes.

![Image](https://cdn-media-1.freecodecamp.org/images/C-UotKFPhKz02WrcwHlP-qf6zyjI9OlPpe64)
_**Extraction of the max node with the value of 6 &amp; sinking down node with the value of 3.**_

For a **max binary heap**, **insertion** of a node & **extraction** of a node with the max value both has a complexity of **O(log n)**.

For a 3 node **max binary heap**, insertion of a node with value 6 requires two steps.

![Image](https://cdn-media-1.freecodecamp.org/images/YHk4cDUnf9vpmrx1IwSnmOqXJ6t0QAsbq7cs)
_**Bubbling up of the new node with value 6**_

* Upon attaching node of value 6 to a new row (below 4), is **6** greater than or less than 4? Swap.
* Is **6** greater than or less than 5? Swap.

Similarly, after the removal of a node with a max value & replacing it with a node of value **1**, two steps remain.

![Image](https://cdn-media-1.freecodecamp.org/images/37yXpaPzOVAquuqkOYNPPqch6OtMbmf8EW4W)
_**Sinking down of node with value 1**_

* Is **1** greater than or less than 5? Swap.
* Is **1** greater than or less than 4? Swap.

Thank you for reading!

### Reference:

[https://www.udemy.com/js-algorithms-and-data-structures-masterclass/](https://www.udemy.com/js-algorithms-and-data-structures-masterclass/)


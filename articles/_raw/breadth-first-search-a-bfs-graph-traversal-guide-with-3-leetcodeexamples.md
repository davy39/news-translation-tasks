---
title: Breadth-First Search - A BFS Graph Traversal Guide with 3 Leetcode Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-26T21:16:31.000Z'
originalURL: https://freecodecamp.org/news/breadth-first-search-a-bfs-graph-traversal-guide-with-3-leetcodeexamples
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/graph_theory_design_web_forms_08.png
tags:
- name: algorithms
  slug: algorithms
seo_title: null
seo_desc: 'By Anamika Ahmed

  Breadth First Search (BFS) is one of the most popular algorithms for searching or
  traversing a tree or graph data structure. In this tutorial, we will learn briefly
  how BFS works and explore a basic pattern that can be used to solve ...'
---

By Anamika Ahmed

Breadth First Search (BFS) is one of the most popular algorithms for searching or traversing a tree or graph data structure. In this tutorial, we will learn briefly how BFS works and explore a basic pattern that can be used to solve some medium and easy problems in Leetcode.

Let's get started, shall we?

## What is Breadth First Search?

So, we all know that a graph is a set of vertices and edges: G={V,E}. Traversing a graph means to visit every vertex and every edge _exactly once_ in an orderly manner. 

In BFS, we are required to traverse the graph breadth-wise or level-wise. This means that we would first move horizontally and visit all the nodes of the current layer before moving on to the next layer. 

Therefore, whenever we are asked to do some **level order traversal,** we can use the BFS technique.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-154.png)

In BFS, we would start traversing from 1 (the root node) and visit its child nodes 8, 5, and 2. We would store them in the order in which they were visited. This would allow us to visit the child nodes of 8 first (i.e. 6, 4 and 3), then of 5 (i.e. null), and then of 2 (i.e. 9) and so on.

## Implementation

In order to implement BFS, a **queue** data structure is used. The queue stores the node and marks it as 'visited' until all its adjacent vertices are marked. 

The queue follows the First In First Out (FIFO) method. This means that the neighbors of the node will be visited in the order in which they were inserted.

**BFS magic spell:**

1. Add a node to the queue 
2. Remove node 
3. Retrieve unvisited neighbors of the removed node, add them to queue
4. Repeat steps 1, 2, and 3 as long as the queue is not empty.

Now let's look at some Leetcode problems and apply what we've learned.

### [102. Binary Tree Level Order Traversal (Difficulty: Medium)](https://leetcode.com/problems/binary-tree-level-order-traversal/) 

The question asks us to traverse through the graph and print the nodes at each level in a linked list. To solve this one, all we need to do is apply our magic spell!

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-157.png)

Make sure you understand the code well, since this is the **basic template** we'll use to solve multiple problems. So let's go through it.

In the code above, we have at first inserted the root node in the queue. While the queue is not empty, we have removed this node from queue and inserted its left and right child in the queue. 

But before that, we checked whether each of its children is null or not. If null, we would have gotten a Null Pointer Exception.

The process is repeated again with the next elements that remains in the queue. The **for loop** is maintained to give us the list of nodes at each level in separate linked lists.

### [637. Average of Levels in a Binary Tree (Difficulty: Easy)](https://leetcode.com/problems/average-of-levels-in-binary-tree/)

This question tells us to find the average value of nodes at each level of a binary tree in an array. This follows the same procedure as our previous problem with a bit of a tweak. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-159.png)

As you can see, all we did was copy and paste the template code. Then we simply put a sum variable within the for loop that can give us the sum of the node values at each level. This is what we will use to calculate our desired average. 

### [429. N-ary Tree Level Order Traversal (Difficulty: Medium)](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

A tree in which each node has **no more than** N number of children is called a N-ary tree. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-173.png)

This follows the exact same procedure as the traversal of a binary tree, except for the fact that in here, we insert all the children of a node in the queue. Remember that while solving problems related to binary tree, we have only inserted the left and right children of any given node in the queue.

That's all! I hope this has helped you understand BFS better and that you have enjoyed the tutorial. Please recommend this post if you think it may be useful for someone else!


---
title: How to Learn Tree Data Structures the Codeless Way
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-09T23:16:20.000Z'
originalURL: https://freecodecamp.org/news/the-codeless-guide-to-tree-data-structures
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c36740569d1a4ca30b5.jpg
tags:
- name: data structures
  slug: data-structures
- name: Trees
  slug: trees
seo_title: null
seo_desc: 'By Armstrong Subero

  The tree data structure can form some of the most useful and complex data structures
  in all of programming. In fact the tree is so powerful that I can make the bold
  claim:

  Once you understand trees you''ll be able to understand man...'
---

By Armstrong Subero

The tree data structure can form some of the most useful and complex data structures in all of programming. In fact the tree is so powerful that I can make the bold claim:

**Once you understand trees you'll be able to understand many other data structures and algorithms with ease.**

There is one caveat. There are so many types of trees it may be impossible to know where to start! There are B-trees, Red Black Trees, Binary Trees, AVL Trees and many others. There are abundant choices and each seems valuable to learn.

This presents a problem. As someone learning about trees you may find yourself asking, which tree data structure do I learn about first? Which tree is most important for me? There are so many, where do I start?

Learning about trees is like learning about the numerous marvels in our current world. We have a lot of choices, in fact we may even have too much choice. 

Psychologists call it **Overchoice** or "**choice overload**", that is when faced with many options, people have a difficult choice deciding on what to do. I call it a beginning coder's worst nightmare. 

However there is no need to panic. From my knowledge of using the tree data structure, as with most things in life, the Pareto principle (what we call the 80/20 rule) applies. 

What this means is that as a programmer, 80% of cases where you will need to use trees will be covered by approximately 20% of the types of trees that you will attempt to learn.

For this reason we will focus only on these 20% which I think are the most important trees you need to understand. Don't get me wrong here, I'm not saying don't learn other types of trees. I'm saying learn these first, then focus on the others to really get that edge. 

Even when you do figure out which tree data structure you want to learn, you are faced with another problem.

There are a lot of resources out there that teach you about trees, however they all present you with some code in a particular language be it JavaScript, Java, Python or others as part of the explanation. 

**In this post I break that status quo and teach you about the essential tree data structures, and all without having you write a single line of code.**

Join me on a journey into the world of trees, regardless of which programming language you are using, you will be able to learn all the basics you need to know about the tree data structure.

## Getting to the Root of Trees

Let's get to the root of our discussion (pun intended). The way I like to explain trees is by relating it to something we are all familiar with, that of the biological tree. In case you are not familiar, let's look at one right now:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/photography-of-tree-1067333.jpg)
_A Biological Tree_

Look at our tree, isn't it beautiful!? We see that a tree is a giant plant with a trunk, a branch and leaves. There are also roots hidden beneath the ground that also form part of the organism. 

A tree in computer science isn't so different. Let's look at one here:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-23.png)
_A Computer Science Tree_

A computer science tree is very similar to a regular tree – it resembles an upside down biological tree a little doesn't it? It not only looks similar, but it also has parts that are named similar to our good ol' tangible tree. 

Before we learn about the types of trees though, there are a few facts about trees you must know.

### Here are 5 facts you need to know about trees:

 1. Each of the circles in the tree is called a node and each line is called an edge.

 2. The root node is the part of the tree that all the other parts are built upon. 

 3. There are parent nodes connected to other nodes in the direction of the root, and         child nodes connected in the direction away from the root.

 4. The last nodes of the trees are called leaves

 5. The process of navigating a tree is called traversal. 

If you like to see things visually, here is a diagram of the tree we looked at earlier identifying the parts:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-25.png)
_Our Labelled Tree_

You should also know that when a tree is the child of a node, it is called a subtree. Look at the diagram above, the node labelled "Parent" along with its two child nodes can be classified as a subtree. 

Great, now you have an idea about basic trees. So let's dive into some of the most useful type of trees you will encounter.

## The General Tree

The first type of tree we need to know about is the general tree. The general tree is what we call a superset. This is because all other types of trees are derived from the general tree. 

Trees are hierarchical in the way they store data. Whereas simpler data structures may store data in a linear manner (think an array), trees are non-linear. 

The general tree is the embodiment of a hierarchical tree structure as it has no restrictions on how many children each node can have, and has no restraint imposed on the hierarchy of the tree.  

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-29.png)
_Example of A General Tree_

## The Binary Tree

It is impossible to talk about trees without talking about the binary tree (okay not totally impossible, but you know what I mean).

Simply put, a binary tree is a type of tree that has a restriction. In the binary tree, each parent can only be linked to two child nodes within the tree. 

There is one binary tree type that illustrates this best: the binary search tree. Trees you see aren't just empty circles connected by lines. Each of the node in the tree has a value associated with it and the entirety of the tree is a key-value structure. 

Binary search trees keep their keys sorted. They sort it like this: all the nodes are greater that the nodes in their left subtree, but are smaller than the nodes in their right subtree. Confused? Maybe a picture will help:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-26.png)
_A Binary Search Tree_

Look closely at this tree and you will learn a little secret. In the binary tree the smallest node is located at the leftmost subtree stemming from the root node. Wanna guess where we can find the largest node?

## Red-Black Tree

Let's look at a variant of the binary search tree that people tend to over-complicate. I'm talking about the Red-Black Tree. 

There are many cases of trees where data may be inserted and deleted. So variations of the binary search tree have been created which makes this constant insertion and deletion more efficient.

The Red-Black tree is one such configuration of the binary search tree that makes the insertion and deletion process more efficient. 

The tree does this by having a bit that adds an attribute to the node. This attribute that is added on the node is color, and this color can be interpreted as red or black. Hence the name Red-Black tree. 

Let's look at how a Red-Black tree many be arranged:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-28.png)
_A Red-Black Tree_

In the Red-Black tree, the root node is usually black and each red node has children that are black. 

If you made it this far, then congratulations! You already understand enough to make a foray into the world of tree data structures. 

## Where Are Trees Used?

At this point you may be wondering what trees are used for. That's a good question! Trees are used in many facets of development including use in:

1. Databases
2. Compilers
3. Networking
4. Heaps
5. Machine Learning Algorithms

There are countless uses for trees and the only limit in their use is the imagination of the designer.

## Wrapping Up

In this post we began our journey into the world of the tree. Even though we covered some ground, we merely scrapped the surface of this vast and intricate data structure. 

We whet our appetite for tree data structures by covering what trees are and looked at their structure. We then discussed three common types of trees including general trees, binary trees and red-black trees. Finally we looked at some places where trees may be used.

By the end of this post you should have a solid foundation to venture into the world of trees!

## Where to Go Next?

Want to learn about trees and other data structures without writing a single line of code? The pick up the book "Codeless Data Structures and Algorithms", where you'll learn all you need to know about data structures and algorithms without writing a single line of code!

We will not only greatly expand on what we learned, but we'll cover juicy topics not covered here like tree balancing, AVL trees, B-Trees, Heaps and a ton of topics in the realm of data structures and algorithms!

You can read the book here:

%[https://www.apress.com/gp/book/9781484257241]



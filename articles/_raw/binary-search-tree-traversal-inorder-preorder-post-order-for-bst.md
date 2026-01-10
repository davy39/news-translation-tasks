---
title: Binary Search Tree Traversal – Inorder, Preorder, Post Order for BST
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-01-26T20:01:40.000Z'
originalURL: https://freecodecamp.org/news/binary-search-tree-traversal-inorder-preorder-post-order-for-bst
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/binary-search-tree-traversal.png
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
seo_title: null
seo_desc: "In this tutorial, you will learn what a binary search tree is, what parts\
  \ make up a tree, and some of the common terms we use when describing parts of a\
  \ tree. \nWe will also see how to traverse a tree using some of the common algorithms\
  \ – all illustra..."
---

In this tutorial, you will learn what a binary search tree is, what parts make up a tree, and some of the common terms we use when describing parts of a tree. 

We will also see how to traverse a tree using some of the common algorithms – all illustrated with clear examples.

## What Is a Binary Search Tree?

A binary search tree is a binary tree made up of nodes. Each node has a key signifying its value. 

The value of the nodes on the left subtree are smaller than the value of the root node. And the value of the nodes on the right subtree are larger than the value of the root node. 

The root node is the parent node of both subtrees.

The diagram below shows the main parts of a binary tree:

![Image](https://www.freecodecamp.org/news/content/images/2022/01/binary-tree.png)
_Diagram of a binary search tree_

Let's us look at the relationship between the nodes. 

* `**A**` is the root node. 
* The left subtree begins at **`B`** while the right subtree begins at **`C`**.
* Node **`A`** has two child nodes – **`B`** and **`C`**.
* Node **`C`** is the parent node to **`F`** and **`G`**. **`F`** and **`G`** are siblings.
* Node **`F`** and **`G`** are know as **leaf** nodes because they do not have children.
* Node **`B`** is the parent node to **`D`** and **`E`**.
* Node **`D`** is the parent node to **`H`** and **`I`**.
* **`D`** and **`E`** are siblings as well as **`H`** and **`I`**.
* Node **`E`**  is a leaf node.

So here are some important terms that we just used to describe the tree above:

**Root:** The topmost node in the tree.

**Parent:** A node with a child or children.

**Child:** A node extended from another node (parent node).

**Leaf:** A node without a child.

## What Is a Binary Search Tree Used For?

Binary search trees help us speed up our binary search as we are able to find items faster. 

We can use the binary search tree for the addition and deletion of items in a tree. 

We can also represent data in a ranked order using a binary tree. And in some cases, it can be used as a chart to represent a collection of information.

Next, we'll look at some techniques used in traversing a binary tree.

## What is Tree Traversal?

Traversing a tree means visiting and outputting the value of each node in a particular order. In this tutorial, we will use the Inorder, Preorder, and Post order tree traversal methods.

The major importance of tree traversal is that there are multiple ways of carrying out traversal operations unlike linear data structures like arrays, bitmaps, matrices where traversal is done in a linear order.

Each of these methods of traversing a tree have a particular order they follow:

* For **Inorder**, you traverse from the **left** subtree to the **root** then to the **right** subtree.
* For **Preorder**, you traverse from the **root** to the **left** subtree then to the **right** subtree.
* For **Post order**, you traverse from the **left** subtree to the **right** subtree then to the **root**.

Here is another way of representing the information above:

Inorder => Left, Root, Right.

Preorder => Root, Left, Right.

Post order => Left, Right, Root.

### How to Traverse a Tree Using Inorder Traversal

We are going to create a tree similar to the one in the last section, but this time the node keys will be numbers instead of letters. 

Remember that the values of the nodes on the left subtree are always smaller than the value of the root node. Also, the values of the nodes on the right subtree are larger than the value of the root node. 

Here is the diagram we will be working with:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ex-binary-search-tree.png)

Recall that the order for inorder traversal is Left, Root, Right.

This is the result we get after using inorder traversal:

**D, B, E, A, F, C, G**

If that seems a bit complex for you to understand, then follow the order of the colors in the picture below

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ex-inorder-traversal.png)
_Inorder traversal_

### How to Traverse a Tree Using Preorder Traversal

The order here is Root, Left, Right.

Using the same diagram above, we have:

**A, B, D, E, C, F, G**

Here is the same diagram with different colors used as a guide:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ex-preorder-traversal.png)
_Preorder traversal_

### How to Traverse a Tree Using Postorder Traversal

The order for post order traversal is Left, Right, Root.

Here is the output:

**D, E, B, F, G, C, A**

If you can't figure out how we arrived at that result, then use the colors in the picture below as a guide:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ex-post-order-traversal.png)
_Postorder traversal_

## Conclusion

In this tutorial, we learned the basics of what a binary search tree is, what the various parts of a binary tree are, and the common terms associated with a tree. We also saw some of the algorithms we can use to traverse a tree.

Thank you for reading!


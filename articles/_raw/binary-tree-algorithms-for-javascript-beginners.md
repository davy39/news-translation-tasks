---
title: Binary Search Tree Algorithms for JavaScript Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-11T23:50:28.000Z'
originalURL: https://freecodecamp.org/news/binary-tree-algorithms-for-javascript-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/binarytree.png
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'I recently had the chance to teach high school students how to code. There
  are not that many beginner-friendly tutorials on algorithms coded in JavaScript
  which is the language they were learning. So I decided to make one.

  In this article, I will try...'
---

I recently had the chance to teach high school students how to code. There are not that many beginner-friendly tutorials on algorithms coded in JavaScript which is the language they were learning. So I decided to make one.

In this article, I will try my best to explain some core algorithms you should learn before a coding interview.

If you are not familiar with the concept of a binary tree, I encourage you to check out the [wikipedia](https://en.wikipedia.org/wiki/Binary_tree) page. If you fully master those basic algorithms, you will have an easier time solving more complex problems.

## What is a Binary Search Tree (BST)?

Commonly found in coding interviews, BST is a tree-like data structure with a single root at the very top. They are a great way to store numeric values as their ordered nature allows for fast search and lookups. 

Compared to a normal tree, BST has the following properties:

* every left child has a smaller value than its parent
* every right child has a larger value than its parent
* every node can contain from 0 to 2 children.

The following diagram should clarify things a bit more. 

## Definition of a Binary Tree Node

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Untitled_Artwork-25.png)
_A binary search tree_

We usually define a Binary Tree Node with the following function in Javascript:

```js
 function TreeNode(val, left, right) {
     this.val = val
     this.left = left
     this.right = right
 }
```

## Binary Tree Basic Traversals (Inorder, Postorder, Preorder)

The first thing to know is how to loop through each node of the BST. This allows us to perform a function on all nodes of our BST. For example, if we want to find a value `x` in our BST, we'd need the nodes. 

There are three main ways of doing this. Luckily, they share common themes.

### Inorder traversal

A recursive algorithm is the easiest way to get started with binary tree inorder traversal. The idea is as follows:

* If the node is null, do nothing – else, recursively call the function on the node's left child.
* Then, do some operation on the node after traversing though all left children. Our current node is guaranteed to be the leftest node.
* Finally, call the function on node.right.

The Inorder algorithm traverses the tree nodes from left, to mid, to right. 

```js
/**
* @param {TreeNode} root
*/
const inorder = (root) => {
    const nodes = []
    if (root) {
        inorder(root.left)
        nodes.push(root.val)
        inorder(root.right)
    }
    return nodes
}
// for our example tree, this returns [1,2,3,4,5,6]
```

### Postorder traversal

A recursive algorithm is the easiest way to get started with the postorder traversal.

* If the node is null, do nothing – else, recursively call the function on the node's left child.
* When there are no more left children, call the function on node.right.
* Finally, do some operation on the node.

Postorder traversal visits the tree nodes from left, to right, to mid. 

```js
/**
* @param {TreeNode} root
*/
const postorder = (root) => {
    const nodes = []
    if (root) {
        postorder(root.left)
        postorder(root.right)
        nodes.push(root.val)
    }
    return nodes
}
// for our example tree, this returns [1,3,2,6,5,4]
```

### Preorder traversal

A recursive algorithm is the easiest way to get started with the preorder traversal.

* If the node is null, do nothing – else, do some operation on the node.
* Traverse to the left child of the node and repeat.
* Traverse to the right child of node and repeat.

Postorder traversal visits the tree nodes from mid, to left, to right. 

```js
/**
* @param {TreeNode} root
*/
const preorder = (root) => {
    const nodes = []
    if (root) {
        nodes.push(root.val)
        preorder(root.left)
        preorder(root.right)
    }
    return nodes
}
// for our example tree, this returns [4,2,1,3,5,6]
```

## What is a Valid Binary Search Tree?

A valid binary search tree (BST) has ALL left children with values less than the parent node, and ALL right children with values greater than the parent node.

To verify if a tree is a valid binary search tree:

* Define the min and max value the current node can have
* If a node's value is not within those bounds, return false
* Recursively validate the node's left children, with the max bound set to the node's value
* Recursively validate the node's right children, with the min bound set to the node's value

```js
/**
* @param {TreeNode} root
*/
const isValidBST = (root) => {
    const helper = (node, min, max) => {
        if (!node) return true
        if (node.val <= min || node.val >= max) return false
        return helper(node.left, min, node.val) && helper(node.right, node.val, max)
    }
    return helper(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER)
}
```

## How to Find Binary Tree Max Depth

Here, the algorithm is attempting to find the height/depth of our BST. In other words, we are looking at how many 'levels' a BST contains.

* If the node is null, we return 0 as it does not add any depth
* Else we add + 1 to our current depth (we traversed one level)
* Recursively calculate the depth of node's children and return the maximum sum between node.left and node.right

```js
/**
* @param {TreeNode} root
*/
const maxDepth = function(root) {
    const calc = (node) => {
        if (!node) return 0
        return Math.max(1 + calc(node.left), 1 + calc(node.right))
    }
    return calc(root)
};
```

## How to Find the Lowest Common Ancestor Between Two Tree Nodes

Let's bump up the difficulty. How do we find the common ancestor between two tree nodes in our binary tree? Let's look at some examples.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Untitled_Artwork-25.png)
_A binary search tree_

In this tree, the lowest common ancestor of 3 and 1 is 2. The LCA of 3 and 2 is 2. The LCA of 6 and 1 and 6 is 4. 

See the pattern here? The LCA between two tree nodes is either one of the nodes itself (the case of 3 and 2), or a parent node where the first child is found somewhere in its left subtree, and the second child somewhere in its right subtree.

The algorithm to find the lowest common ancestor (LCA) between two tree nodes p and q is as follows:

* Verify if p or q is found in the left subtree or right subtree
* Then, verify if the current node is p or q
* If one of p or q is found in the left or right subtree, and one of p or q is the node itself, we have found the LCA
* If both p and q are found in the the left or right subtree, we have found the LCA

```js
/**
* @param {TreeNode} root
* @param {TreeNode} p
* @param {TreeNode} q
*/
const lowestCommonAncestor = function(root, p, q) {
    let lca = null
    const isCommonPath = (node) => {
        if (!node) return false
        var isLeft = isCommonPath(node.left)
        var isRight = isCommonPath(node.right)
        var isMid = node == p || node == q
        if (isMid && isLeft || isMid && isRight || isLeft && isRight) {
            lca = node
        }
        return isLeft || isRight || isMid
    }
    isCommonPath(root)
    return lca
};
```

## Wrapping Up

In summary, we have learned how to traverse, verify, and calculate the depth of a BST. 

These algorithms are often asked about in coding interviews. It is important to understand them before practicing more advanced BST applications, like finding the LCA of two nodes.


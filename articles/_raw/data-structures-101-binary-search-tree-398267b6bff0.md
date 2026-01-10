---
title: 'Data Structures 101: Binary Search Tree'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-10T16:31:48.000Z'
originalURL: https://freecodecamp.org/news/data-structures-101-binary-search-tree-398267b6bff0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*gYtXwdbgInK7hI-u
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Turney

  How to combine the efficiency of insertion of a Linked List and the quick search
  of an ordered array.


  _“leafless tree on the hill” by [Unsplash](https://unsplash.com/@fabulu75?utm_source=medium&utm_medium=referral"
  rel="noopener" tar...'
---

By Kevin Turney

#### How to combine the efficiency of insertion of a Linked List and the quick search of an ordered array.

![Image](https://cdn-media-1.freecodecamp.org/images/4k66O-44Ze-2G1D19GB4by1CUYiTnQbEzmpo)
_“leafless tree on the hill” by [Unsplash](https://unsplash.com/@fabulu75?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Fabrice Villard</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### **What is a Binary Search Tree?**

Let’s start with basic terminology so we may share the same language and investigate related concepts. First, what are the principles that define a Binary Search Tree?

* From here on out I will use “BST” for brevity

A BST is considered a data structure made up of **nodes**, like [**Linked Lists**](https://medium.freecodecamp.org/data-structures-101-linked-lists-254c82cf5883)**_._** These nodes are either null or have references (links) to other nodes. These ‘other’ nodes are child nodes, called a left node and right node. Nodes have **values**. These values determine where they are placed within the BST.

Similarly to a linked list, each node is referenced by **only** one other node, its parent (except for the root node). So we can say that each node in a BST is in itself a BST. Because further down the tree, we reach another node and that node has a left and a right. Then depending on which way we go, that node has a left and a right and so on.

1. The left node is always smaller than its parent.

2. The right node is always greater than its parent.

3. A BST is considered balanced if every level of the tree is fully filled with the exception of the last level. On the last level, the tree is filled left to right.

4. A Perfect BST is one in which it is both full and complete (all child nodes are on the same level and each node has a left and a right child node).

![Image](https://cdn-media-1.freecodecamp.org/images/2rTqYlcrnWtICedt131tDft0CmkzZaViExJX)

### Why would we use this?

What are some real-world examples of BST’s? Trees are often used in search, game logic, autocomplete tasks, and graphics.

Speed. As mentioned earlier, the BST is an ordered data structure. Upon insertion, the nodes are placed in an orderly fashion. This inherent order makes searching fast. Similar to binary search (with an array that is sorted), we cut the amount of data to sort through by half on each pass. For example, suppose we are looking for a small node value. On each pass, we keep moving along the leftmost node. This eliminates half the greater values automatically!

Also, unlike an array, the data is stored by reference. As we add to the data structure, we create a new chunk in memory and link to it. This is faster than creating a new array with more space and then inserting the data from the smaller array to the new, larger one.

In short, inserting, deleting and searching are the all-stars for a BST

Now that we understand the principles, the benefits, and the basic components of a BST, let’s implement one in javascript.

The API for a BST consists of the following: **Insert, Contains, Get Min, Get Max, Remove Node, Check if Full, Is Balanced**, and the types of Search — **Depth First (preOrder, inOrder, postOrder), Breadth First Search**, and lastly **Get Height**. That’s a big API, just take it one section at a time.

### **Implementation**

**The constructor**

The BST is made up of nodes, and each node has a value.

```
function Node(value){  this.value = value;  this.left = null;  this.right = null;}
```

The BST constructor is made up of a root node.

```
function BinarySearchTree() { this.root = null;}
```

```
let bst = new BST();let node = new Node();
```

```
console.log(node, bst); // Node { value: undefined, left: null, right: null } BST { root: null }
```

… so far so good.

### Insertion

```
BinarySearchTree.prototype.insert = function(value){ let node = new Node(value); if(!this.root) this.root = node; else{    let current = this.root;    while(!!current){       if(node.value < current.value){       if(!current.left){           current.left = node;           break;         }         current = current.left;         }        else if(node.value > current.value){         if(!current.right){            current.right = node;            break;           }          current = current.right;          }         else {          break;           }         }        }    return this; };
```

```
let bst = new BST();bst.insert(25); // BST { root: Node { value: 25, left: null, right: null } }
```

Let’s add some more values.

```
bst.insert(40).insert(20).insert(9).insert(32).insert(15).insert(8).insert(27);
```

```
BST { root:  Node { value: 25, left: Node { value: 20, left: [Object], right: null }, right: Node { value: 40, left: [Object], right: null } } }
```

For a cool visualization [Go Here](http://btv.melezinek.cz/binary-search-tree.html)!!

Let’s unpack this.

1. First, we pass a value and create a new node
2. Check if there is a root, if not, set this newly created node to the root node
3. If there is a root node, we create a variable declared “current”, and set its value to the root node
4. If the newly created node.value is smaller than the root node, we will move left
5. We keep comparing this node.value to left nodes.
6. If the value is small enough and we reach a point where there are no more left nodes, we place this item here.
7. If the node.value is greater we repeat the same steps as above except we move along the right.
8. We need the break statements because there is no count step to terminate the while loop.

### Contains

This is a pretty straightforward approach.

```
BinarySearchTree.prototype.contains = function(value){ let current = this.root; while(current){ if(value === current.value) return true; if(value < current.value) current = current.left; if(value > current.value) current = current.right; } return false;};
```

### Get Min and Get Max.

Keep traversing left to the smallest value or right for the largest.

```
BinarySearchTree.prototype.getMin = function(node){ if(!node) node = this.root; while(node.left) { node = node.left; } return node.value};
```

```
BinarySearchTree.prototype.getMax = function(node){ if(!node) node = this.root; while(node.right) { node = node.right; } return node.value;};
```

### Removal

Removing a node is the trickiest operation, because nodes have to be reordered to maintain the properties of a BST. There is a case if a node has only one child and a case if there is both a left and a right node. We use the larger helper function to do the heavy lifting.

```
BinarySearchTree.prototype.removeNode = function(node, value){ if(!node){   return null; } if(value === node.value){ // no children if(!node.left && !node.right) return null; // one child and it’s the right if(!node.left) node.right;// one child and it’s the left if(!node.right) node.left;  // two kids const temp = this.getMin(node.right); node.value = temp; node.right = this.removeNode(node.right, temp); return node; } else if(value < node.value) {     node.left = this.removeNode(node.left, value);     return node; } else  {     node.right = this.removeNode(node.right, value);     return node;   }};
```

```
BinarySearchTree.prototype.remove = function(value){ this.root = this.removeNode(this.root, value);};
```

It works like this…

Unlike deleteMin and deleteMax, where we can just traverse all the way left or all the way right and pick off the last value, we have to take out a node and then replace it with something. This solution was developed in 1962 by T. Hibbard. We account for the case where we can delete a node with only one child or none, that’s minor. If no children, no problem. If a child is present, that child just moves up one.

But with a node scheduled to be removed that has two children, which child takes its place? Certainly, we can’t move a larger node down. So what we do is replace it with its successor, the next kingpin. We have to find the smallest right child on the right that is larger than the left child.

1. Create a temp value and store the smallest node on its right. What this does is satisfy the property that values to the left are still smaller and values to the right are still greater.
2. Reset the node’s value to this temp variable
3. Remove the right node.
4. Then we compare values on the left and the right and determine the assigned value.

This is best explained with a picture:

![Image](https://cdn-media-1.freecodecamp.org/images/cEcyXZpZvRln6p7jzJq08lOJsORH6yA7Rd0T)

### Searching

There are two types of search, Depth First and Breadth First. Breadth First is simply stopping at each level on the way down. It looks like this: we start at the root, then the left child, then the right child. Move to the next level, left child then right child. Think of this as moving horizontally. We employ, I should say simulate, a queue to help order the process. We pass a function, because many times we want to operate on a value.

```
BinarySearchTree.prototype.traverseBreadthFirst = function(fn) { let queue = []; queue.push(this.root); while(!!queue.length) {   let node = queue.shift();   fn(node);   node.left && queue.push(node.left);   node.right && queue.push(node.right);  }}
```

Depth First Search involves moving down the BST in a specified manner, either, preOrder, inOrder, or postOrder. I’ll explain the differences shortly.

In the spirit of concise code, we have a basic traverseDepthFirst function and we pass a function and a method. Again the function implies that we want to do something to the values along the way, while the method is the type of search we wish to perform. In the traverseDFS, we have a fallback: preOrder search in place.

Now, how is each one different? First, let’s dispatch inOrder. It should be self-explanatory but it isn’t. Do we mean in order of insertion, in order of highest to lowest or lowest to highest? I just wanted you to consider these things beforehand. In this case, yes, it does mean lowest to highest.

**preOrder** can be thought of as **Parent, Left Child, then Right child_._**

**postOrder** as **Left Child, Right Child, Parent_._**

```
BinarySearchTree.prototype.traverseDFS = function(fn, method){ let current = this.root; if(!!method) this[method](current, fn); else this._preOrder(current, fn);};
```

```
BinarySearchTree.prototype._inOrder = function(node, fn){ if(!!node){ this._inOrder(node.left, fn); if(!!fn) fn(node); this._inOrder(node.right, fn); }};
```

```
BinarySearchTree.prototype._preOrder = function(node, fn){ if(node){ if(fn) fn(node); this._preOrder(node.left, fn); this._preOrder(node.right, fn); }};
```

```
BinarySearchTree.prototype._postOrder = function(node, fn){ if(!!node){ this._postOrder(node.left, fn); this._postOrder(node.right, fn); if(!!fn) fn(node); }};
```

### **Check if the BST is full**

Remember from earlier, a BST is full if every node has Zero or Two children.

```
// a BST is full if every node has zero two children (no nodes have one child)
```

```
BinarySearchTree.prototype.checkIfFull = function(fn){ let result = true; this.traverseBFS = (node) => {   if(!node.left && !node.right) result = false;   else if(node.left && !node.right) result = false;  } return result;};
```

### Get Height of BST

What does it mean to get the height of a tree? Why is this important? This is where **Time Complexity** (aka Big O) comes into play. Basic operations are proportional to the height of a tree. So as we alluded to earlier, if we search for a particular value, the number of operations we have to do is halved on each step.

That means if we have a loaf of bread and cut it in half, then cut that half in half, and keep doing that till we get the exact piece of bread we want.

In computer science, this is called O(log n). We start with an input size of some sort, and over time that size gets smaller (kind of flattening out). A straight linear search is denoted as O(n), as the input size increases so does the time it takes to run operations. O(n) conceptually is a 45-degree line starting at origin zero on a chart and moving right. The horizontal scale represents the size of an input and the vertical scale represents the time it takes to complete.

Constant time is O(1). No matter how large or small the input size is, the operation takes place in the same amount of time. For example, push() and pop() off of an array are constant time. Looking up a value in a HashTable is constant time.

I will explain more about this in a future article, but I wanted to arm you with this knowledge for now.

**Back to height.**

We have a recursive function, and our base case is: **‘if we have no node then we start at this.root’_._** This implies that we can start at values lower in the tree and get tree sub-heights.

So if we pass in this.root to start, we recursively move down the tree and add the function calls to the execution stack (other articles here). When we get to the bottom, the stack is filled. Then the calls get executed and we compare the heights of the left and the heights of the right and increment by one.

```
BinarySearchTree.prototype._getHeights = function(node){ if(!node) return -1; let left = this._getHeights(node.left); let right = this._getHeights(node.right); return Math.max(left, right) + 1;};
```

```
BinarySearchTree.prototype.getHeight = function(node){ if(!node) node = this.root; return this._getHeights(node);};
```

### Lastly, Is Balanced

What we are doing is checking if the tree is filled at every level, and on the last level, if it is filled left to right.

```
BinarySearchTree.prototype._isBalanced = function(node){ if(!node) return true; let heightLeft = this._getHeights(node.left); let heightRight = this._getHeights(node.right); let diff = Math.abs(heightLeft — heightRight); if(diff > 1) return false; else return this._isBalanced(node.left) &&    this._isBalanced(node.right);};
```

```
BinarySearchTree.prototype.isBalanced = function(node){ if(!node) node = this.root; return this._isBalanced(node);};
```

### Print

Use this to visualize all the methods you see, especially depth first and breadth first traversals.

```
BinarySearchTree.prototype.print = function() { if(!this.root) {   return console.log(‘No root node found’); } let newline = new Node(‘|’); let queue = [this.root, newline]; let string = ‘’; while(queue.length) {   let node = queue.shift();   string += node.value.toString() + ‘ ‘;   if(node === newline && queue.length) queue.push(newline);    if(node.left) queue.push(node.left);   if(node.right) queue.push(node.right);  } console.log(string.slice(0, -2).trim());};
```

**Our Friend Console.log!! Play around and experiment.**

```
const binarySearchTree = new BinarySearchTree();binarySearchTree.insert(5);binarySearchTree.insert(3);
```

```
binarySearchTree.insert(7);binarySearchTree.insert(2);binarySearchTree.insert(4);binarySearchTree.insert(4);binarySearchTree.insert(6);binarySearchTree.insert(8);binarySearchTree.print(); // => 5 | 3 7 | 2 4 6 8
```

```
binarySearchTree.contains(4);
```

```
//binarySearchTree.printByLevel(); // => 5 \n 3 7 \n 2 4 6 8console.log('--- DFS inOrder');
```

```
binarySearchTree.traverseDFS(function(node) { console.log(node.value); }, '_inOrder'); // => 2 3 4 5 6 7 8
```

```
console.log('--- DFS preOrder');
```

```
binarySearchTree.traverseDFS(function(node) { console.log(node.value); }, '_preOrder'); // => 5 3 2 4 7 6 8
```

```
console.log('--- DFS postOrder');
```

```
binarySearchTree.traverseDFS(function(node) { console.log(node.value); }, '_postOrder'); // => 2 4 3 6 8 7 5
```

```
console.log('--- BFS');
```

```
binarySearchTree.traverseBFS(function(node) { console.log(node.value); }); // => 5 3 7 2 4 6 8
```

```
console.log('min is 2:', binarySearchTree.getMin()); // => 2
```

```
console.log('max is 8:', binarySearchTree.getMax()); // => 8
```

```
console.log('tree contains 3 is true:', binarySearchTree.contains(3)); // => true
```

```
console.log('tree contains 9 is false:', binarySearchTree.contains(9)); // => false
```

```
// console.log('tree height is 2:', binarySearchTree.getHeight()); // => 2
```

```
console.log('tree is balanced is true:', binarySearchTree.isBalanced(),'line 220'); // => true
```

```
binarySearchTree. remove(11); // remove non existing node
```

```
binarySearchTree.print(); // => 5 | 3 7 | 2 4 6 8
```

```
binarySearchTree.remove(5); // remove 5, 6 goes up
```

```
binarySearchTree.print(); // => 6 | 3 7 | 2 4 8
```

```
console.log(binarySearchTree.checkIfFull(), 'should be true');
```

```
var fullBSTree = new BinarySearchTree(10);
```

```
fullBSTree.insert(5).insert(20).insert(15).insert(21).insert(16).insert(13);
```

```
console.log(fullBSTree.checkIfFull(), 'should be true');
```

```
binarySearchTree.remove(7); // remove 7, 8 goes up
```

```
binarySearchTree.print(); // => 6 | 3 8 | 2 4
```

```
binarySearchTree.remove(8); // remove 8, the tree becomes unbalanced
```

```
binarySearchTree.print(); // => 6 | 3 | 2 4
```

```
console.log('tree is balanced is false:', binarySearchTree.isBalanced()); // => true
```

```
console.log(binarySearchTree.getHeight(),'height is 2')
```

```
binarySearchTree.remove(4);
```

```
binarySearchTree.remove(2);
```

```
binarySearchTree.remove(3);
```

```
binarySearchTree.remove(6);
```

```
binarySearchTree.print(); // => 'No root node found'
```

```
//binarySearchTree.printByLevel(); // => 'No root node found'
```

```
console.log('tree height is -1:', binarySearchTree.getHeight()); // => -1
```

```
console.log('tree is balanced is true:', binarySearchTree.isBalanced()); // => true
```

```
console.log('---');
```

```
binarySearchTree.insert(10);
```

```
console.log('tree height is 0:', binarySearchTree.getHeight()); // => 0
```

```
console.log('tree is balanced is true:', binarySearchTree.isBalanced()); // => true
```

```
binarySearchTree.insert(6);
```

```
binarySearchTree.insert(14);
```

```
binarySearchTree.insert(4);
```

```
binarySearchTree.insert(8);
```

```
binarySearchTree.insert(12);
```

```
binarySearchTree.insert(16);
```

```
binarySearchTree.insert(3);
```

```
binarySearchTree.insert(5);
```

```
binarySearchTree.insert(7);
```

```
binarySearchTree.insert(9);
```

```
binarySearchTree.insert(11);
```

```
binarySearchTree.insert(13);
```

```
binarySearchTree.insert(15);
```

```
binarySearchTree.insert(17);
```

```
binarySearchTree.print(); // => 10 | 6 14 | 4 8 12 16 | 3 5 7 9 11 13 15 17
```

```
binarySearchTree.remove(10); // remove 10, 11 goes up
```

```
binarySearchTree.print(); // => 11 | 6 14 | 4 8 12 16 | 3 5 7 9 x 13 15 17
```

```
binarySearchTree.remove(12); // remove 12; 13 goes up
```

```
binarySearchTree.print(); // => 11 | 6 14 | 4 8 13 16 | 3 5 7 9 x x 15 17
```

```
console.log('tree is balanced is true:', binarySearchTree.isBalanced()); // => true
```

```
//console.log('tree is balanced optimized is true:', binarySearchTree.isBalancedOptimized()); // => true
```

```
binarySearchTree.remove(13); // remove 13, 13 has no children so nothing changes
```

```
binarySearchTree.print(); // => 11 | 6 14 | 4 8 x 16 | 3 5 7 9 x x 15 17
```

```
console.log('tree is balanced is false:', binarySearchTree.isBalanced()); // => false
```

```
// yields ...5 | 3 7 | 2 4 6 8--- DFS inOrder2345678--- DFS preOrder5324768--- DFS postOrder2436875--- BFS5372468min is 2: 2max is 8: 8tree contains 3 is true: truetree contains 9 is false: falsetree is balanced is true: true line 2205 | 3 7 | 2 4 6 86 | 3 7 | 2 4 8true 'should be true'true 'should be true'6 | 3 8 | 2 46 | 3 | 2 4tree is balanced is false: false2 'height is 2'No root node foundtree height is -1: -1tree is balanced is true: true---tree height is 0: 0tree is balanced is true: true10 | 6 14 | 4 8 12 16 | 3 5 7 9 11 13 15 1711 | 6 14 | 4 8 12 16 | 3 5 7 9 13 15 1711 | 6 14 | 4 8 13 16 | 3 5 7 9 15 17tree is balanced is true: true11 | 6 14 | 4 8 16 | 3 5 7 9 15 17tree is balanced is false: false
```

### Time Complexity

1. Insertion O(log n)  
2. Removal O(log n)  
3. Search O(log n)

Wow, that is indeed a lot of information. I hope the explanations were as clear and as introductory as possible. Again, writing helps me solidify concepts and as Richard Feynman said, “When one person teaches, two learn.”

### Resources

Probably the best resource for visualizing, definitely use it:

[**Data Structure Visualization**](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)  
[_David Galles Computer Science University of San Francisco_www.cs.usfca.edu](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)[**BinaryTreeVisualiser - Binary Search Tree**](http://btv.melezinek.cz/binary-search-tree.html)  
[_Site description here_btv.melezinek.cz](http://btv.melezinek.cz/binary-search-tree.html)[**VisuAlgo - Binary Search Tree, AVL Tree**](https://visualgo.net/en/bst?slide=1)  
[_A Binary Search Tree (BST) is a binary tree in which each vertex has only up to 2 children that satisfies BST property…_visualgo.net](https://visualgo.net/en/bst?slide=1)[**Big-O Algorithm Complexity Cheat Sheet (Know Thy Complexities!) @ericdrowell**](http://www.bigocheatsheet.com/)  
[_Hi there! This webpage covers the space and time Big-O complexities of common algorithms used in Computer Science. When…_www.bigocheatsheet.com](http://www.bigocheatsheet.com/)[**Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne**](https://algs4.cs.princeton.edu/home/)  
[_The textbook Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne surveys the most important algorithms and data…_algs4.cs.princeton.edu](https://algs4.cs.princeton.edu/home/)[**Binary search tree - Wikipedia**](https://en.wikipedia.org/wiki/Binary_search_tree)  
[_In computer science, binary search trees ( BST), sometimes called ordered or sorted binary trees, are a particular type…_en.wikipedia.org](https://en.wikipedia.org/wiki/Binary_search_tree)


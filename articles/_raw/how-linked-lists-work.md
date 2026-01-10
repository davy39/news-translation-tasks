---
title: How Does a Linked List Work? A Beginner's Guide to Linked Lists
subtitle: ''
author: Palistha Singh
co_authors: []
series: null
date: '2023-05-12T17:45:27.000Z'
originalURL: https://freecodecamp.org/news/how-linked-lists-work
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-joey-kyber-119562.jpg
tags:
- name: data structures
  slug: data-structures
- name: Java
  slug: java
seo_title: null
seo_desc: 'A Linked List is a linear data structure used for storing a collection
  of elements. Unlike arrays, linked lists use nodes to store elements which are not
  stored in contiguous memory locations.

  In this article, you will learn what linked lists are, ho...'
---

A Linked List is a linear data structure used for storing a collection of elements. Unlike arrays, linked lists use nodes to store elements which are not stored in contiguous memory locations.

In this article, you will learn what linked lists are, how they work, and how to build one.

While the concepts discussed are not specific to any particular programming language, this article will use Java to demonstrate how to create a linked list programmatically.

## What is a Linked List?

A linked list is a collection of nodes where each node contains data as well as the memory address of the next node in the list.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/7.png align="left")

*Illustration of a linked list with three nodes*

Here, you can see that the addresses of the nodes are not necessarily immediately sequential. The first node has an address of **200** and the second node has an address of **801**, instead of **201** as you might expect.

Then how are the nodes stored linearly?

Even though the nodes are not in a contiguous memory, the nodes are stored linearly through links. Every node has the address of its succeeding node. That is how each node can access its succeeding node.

## Nodes in a Linked List

Nodes are the building block of the linked list. After all, a linked list is a collection of nodes.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/8.png align="left")

*Example node*

A node in a linked list consists of two parts:

* `data` which denotes the value of the node.
    
* `next` which is a reference to the succeeding node.
    

## Head and Tail in a Linked List

As mentioned earlier, a linked list is a collection of nodes.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/9.png align="left")

*Illustration of a linked list showing the head and tail*

The first node of the linked list is called the `head` node. It is the starting point of a linked list.

The last node is called the `tail` node. As there is no node after the last node, the last node always points to the `null`.

A `null` pointer does not point to any memory location.

## How to Create a Linked List Programmatically

At this point, you should have basic knowledge of how a linked list works and its structure. Let’s create a linked list with the following steps:

* Create node.
    
* Connect nodes.
    
* Append nodes.
    
* Insert nodes.
    
* Delete nodes.
    

## How to Create a Node in a Linked List

As you know, a node consists of two parts: the data and the address to the next node.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/10.png align="left")

*Illustration of a single node*

Here's how you can create a class called `Node`:

```java
class Node {
    int data;
    Node next;
 
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}
```

The `Node` class represents a node in a linked list, with two instance variables: data (holds the data stored in the node), and next (holds a reference to the next node in the list).

The constructor takes an `int` argument data to initialize the data variable and sets the next variable to null by default.

Now, you can simply create nodes and add data to them by creating new instances of the `Node` class:

```java
// create nodes
Node node1 = new Node(11);
Node node2 = new Node(18);
Node node3 = new Node(24);
```

In the code above, we created three nodes:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/11.png align="left")

*Showing the three nodes we created with the above code*

## How to Link the Nodes in a Linked List

After creating the nodes, you must connect them to form a linked list.

To do this you first need to create a linked list with a `head` node.

```bash
class LinkedList {

    Node head;

        LinkedList() {
        this.head = null;
    }

}
```

Initially the `head` node is set to `null` because there are no nodes in the linked list yet.

Now to connect the nodes together in a Linked List, you can start by setting the `head` node to the first node in the list, in this case `node1`.

```bash
head = node1;
```

Then make the next of `node1` point to `node2`, and the next of `node2` point to `node3`. That is:

```java
node1.next = node2;
node2.next = node3;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/19-1.png align="left")

*Illustration showing the linking of nodes*

You have successfully created a linked list and connected the nodes.

## How to Append a Node to Linked List

Appending a node means adding a node to the end of a linked list. There are two cases to consider when appending a node:

* Appending to an empty linked list.
    
* Appending to a non-empty linked list.
    

### How to Append a Node to an Empty Linked List

If there are no nodes in a linked list, it is an empty linked list. To append a node to an empty linked list, you must first make sure the linked list is empty. You can do this by checking if the `head` node is `null`.

If the `head` node is `null` then you can simply set `head` to the new node:

```java
if (head == null) {
    head = newNode;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/13.png align="left")

*Head node is null*

### How to Append a Node to Non-Empty Linked List

If there are one or more nodes in a linked list, it is a non-empty linked list.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/19-2.png align="left")

*Illustration of a non-empty linked list*

To append a node to a non-empty linked list, make the last node link to the new node.

Unlike arrays, we cannot access any elements in a linked list directly. We must traverse from the `head` node to the `last` node.

To do that, create a temporary pointer (you can call the pointer `current`) that points to the head node.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/17-2.png align="left")

*Illustration showing temporary pointer (current) pointing to head node*

Next, make `current` point to its `next` node, till the `next` of the current node points to `null`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/18-1.png align="left")

*Illustration showing temporary pointer (current) pointing its next node*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/16-2.png align="left")

*Illustration showing temporary pointer (current) pointing its next node*

When the `next` node of `current` is `null`, you can then make the `next` of the `current` node point to the new node. That is:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/15-1.png align="left")

*Illustration showing temporary pointer (current) pointing to new node*

```java
while (current.next != null) {
    current = current.next;
}
current.next = newNode;
```

## How to Insert a Node in a Linked List

Inserting a node means adding a node to a given index. There are two cases to consider when inserting a node:

* Inserting a node at the first index.
    
* Inserting a node at a given index.
    

### How to Insert a node at the First Index

To insert a node at the first index:

* make `next` of the new node point to the `head` node
    
* set the `head` to the new node
    

![Image](https://www.freecodecamp.org/news/content/images/2023/05/13-1.png align="left")

*Illustration showing new node pointing to head node*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/14-1.png align="left")

*Illustration showing head node pointing to the new node*

```java
if (index == 0) {
    newNode.next = head;
    head = newNode;
}
```

### How to Insert a Node at Any Position

![Image](https://www.freecodecamp.org/news/content/images/2023/05/4-1.png align="left")

*Linked List with index*

Let’s suppose you want to add a node at index 2 in the linked list above.

To insert a node at index 2, you must traverse the node that comes before index 2.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/5-1.png align="left")

*Illustration showing temporary pointer (current) pointing to head node*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/10-1.png align="left")

*Illustration showing temporary pointer (current) pointing its next node*

Next, create a new node and make the `next` of the new node point to the `next` of the `current` node.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/9-1.png align="left")

*Illustration showing new node pointing next node of current*

Make the `next` of `current` point to the new node.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/8-2.png align="left")

*Illustration showing current pointing new node*

Here's the code to do all this:

```java
for (int i = 0; i < index - 1 && current != null; i++) {
    current = current.next;
}
if (current != null) {
    newNode.next = current.next;
    current.next = newNode;
}
```

## How to Delete a Node in a Linked List

There are two ways to delete nodes in a linked list:

* Deleting the head node.
    
* Deleting a node at a given position.
    

### How to Delete the Head Node

Deleting the `head` node of a linked list is simple. You can store the data of the `head` node in a temporary variable if it needs to be accessed later. Then set the `head` pointer to point to the `next` node after the `head` node.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/7-1.png align="left")

*Illustration showing temporary pointer (current) pointing to head node*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/6.png align="left")

*Illustration showing temporary pointer (current) pointing its next node*

```java
if (index == 0) {
    deletedValue = head.data;
    head = head.next;
}
```

### How to Delete a Node at a Given Position

Suppose you want to delete the node at index 2 in the diagram below:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/4-2.png align="left")

*Linked List with index*

You can delete the node at index 2 by making the node at index 1 point to the node at index 3.

To delete a node you must access the node you want to delete and the node before it. Take two temporary pointers (you can call the pointers `previous` and `current`). Let `previous` point to `null` and `current` point to the `head` node.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/data--3-.png align="left")

*Illustration showing temporary pointer (current) pointing to head node*

Now, move `current` one step forward and move `previous` to `current` till you reach index 2.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/2-2.png align="left")

*Illustration showing temporary pointer (previous) pointing to head node*

![Image](https://www.freecodecamp.org/news/content/images/2023/05/3-1.png align="left")

*Illustration showing temporary pointer pointing to its succeeding nodes*

Make the `next` of `previous` point to the `next` of the `current` node.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/1.png align="left")

*Illustration showing previous pointing to node next to current*

Then store the data of `current` in a variable for future use.

After removing the link to the node at index 2, it is no longer accessible through any reference in the linked list.

It's important to note that when removing a node from a linked list, you don't need to explicitly delete the node itself at the given index. This is because the removed node will be automatically handled by the garbage collector when it is no longer reachable through any references.

However, in languages like C or C++, which do not have automatic garbage collection, you need to manually delete the node when it is no longer needed to avoid memory leaks and wasted memory resources.

```java
for (int i = 0; i < index && current != null; i++) {
    previous = current;
    current = current.next;
}

if (current != null) {
    deletedValue = current.data;
    previous.next = current.next;
}
```

## Complete Linked List Code

The code below shows a complete linked list. You can create, append, insert, delete, and display the nodes in the linked list:

```java
class Node {

	int data;
	Node next;

	Node(int data) {
		this.data = data;
		this.next = null;
	}
}

class LinkedList {

	Node head;

	LinkedList() {
		this.head = null;
	}

	public void createLinkedList() {

		Node node1 = new Node(11);
		this.head = node1;

		Node node2 = new Node(18);
		node1.next = node2;

		Node node3 = new Node(24);
		node2.next = node3;
	}

	public void append(Node newNode) {

		Node current = this.head;

		if (current == null) {
			this.head = newNode;
		} else {
			while (current.next != null) {
				current = current.next;
			}
			current.next = newNode;
		}

	}

	public void insert(Node newNode, int index) {

		Node current = this.head;
		if (index == 0) {
			newNode.next = current;
			this.head = newNode;
		} else {

			for (int i = 0; i < index - 1 && current != null; i++) {
				current = current.next;
			}
			if (current != null) {
				newNode.next = current.next;
				current.next = newNode;
			}

		}

	}

	public int delete(int index) {

		Node current = this.head;
		Node previous = null;
		int deletedValue = -1;

		if (index == 0) {
			deletedValue = this.head.data;
			this.head = this.head.next;
			return deletedValue;
		}

		else {
			for (int i = 0; i < index && current != null; i++) {
				previous = current;
				current = current.next;

			}
			if (current != null) {

				deletedValue = current.data;
				previous.next = current.next;
			}
			return deletedValue;
		}
	}
	
	public void displayLinkedList() {

		Node current = this.head;
		while (current != null) {
			System.out.println(current.data);
			current = current.next;

		}
	}

}

class Main {
	public static void main(String[] args) {
		LinkedList l1 = new LinkedList();
		Node newNode1 = new Node(22);
		Node newNode2 = new Node(43);
		Node newNode3 = new Node(5);
		l1.createLinkedList();

		l1.append(newNode1);
		l1.insert(newNode2, 0);
		l1.insert(newNode3, 2);
		l1.delete(2);
		l1.displayLinkedList();
	}
}
```

## Wrapping Up

The linked list data structure can be used in various applications, such as web browsers and music players.

For example, in a web browser, the browser history can be stored as a linked list. Each page visited can be represented by a node, with the link pointing to the next page visited. This allows for easy navigation through the history, by simply traversing the linked list.

Similarly, in a music player, the playlist can be represented as a linked list. Each song can be represented by a node, with the link pointing to the next song in the playlist. This allows for easy navigation through the playlist, by simply traversing the linked list.

It is not very likely that you will create a linked list for your applications, as almost every programming language has a built-in linked list.

However, creating one and understanding its implementation can deepen your knowledge of the data structure. This knowledge can help you determine when to use a linked list over other data structures in real-life applications.

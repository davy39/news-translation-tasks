---
title: 'Python interview question guide: how to code a linked list'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T21:50:34.000Z'
originalURL: https://freecodecamp.org/news/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y2zqUEPWCjkWCWVnxmy3GQ.jpeg
tags:
- name: interview
  slug: interview
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Anthony Sistilli

  I always understood the core concept of Linked Lists, but I never put it into practice.

  It wasn’t until my very first Amazon interview years ago when I realized that I
  had no idea how the concept of Linked Lists translated into co...'
---

By Anthony Sistilli

I always understood the core concept of Linked Lists, but I never put it into practice.

It wasn’t until my very first Amazon interview years ago when I realized that I had no idea how the concept of Linked Lists translated into code.

![Image](https://cdn-media-1.freecodecamp.org/images/hTliWmiFIsrEJqgzgpkHffXflO3tkNIUa5-E)
_*My face during my first ever Amazon interview*_

And that’s why I’m writing this guide!

My goal is to help **you** get a job as a Software Engineer.

I want to cover a lot of Linked Lists interview questions, and this article is the first step in that process. So let’s dive in.

### What is a Linked List?

A Linked List is a data structure that consists of many mini-data structures called ‘Nodes.’ The Nodes link together to form a list.

![Image](https://cdn-media-1.freecodecamp.org/images/QUIARoltvUdLReB8VIoNcGFPkaAvGwDWOl8d)
_An entire Linked List, made up of 3 Nodes linked together._

#### Each node contains 2 attributes

1. Its value. This can be anything: integers, characters, strings, objects, and so on.
2. A pointer to the next node in the sequence.

#### Some definitions

**The ‘Head Node’:** The head node is simply the first node in the linked list. As we can see from the example above, the node containing ‘5’ is the first node, and therefore the head.

**The ‘Tail Node’:** The tail node is the last node in the sequence. Since it’s the last node, it points to null, because there is no next node in the sequence. In the example above, the node containing ‘3’ would be the tail node.

### Singly Linked vs Doubly Linked

When it comes to Linked Lists, there are two main kinds.

Those that are ‘singly’ linked, and those that are ‘doubly’ linked.

**Singly linked** means that each node only points to at most 1 other node, the node in front of it. This is exhibited in the example above.

![Image](https://cdn-media-1.freecodecamp.org/images/Yii0EYpRWc8SQO4mOq0Lejev6T8uTe4unJfv)
_An example of a singly linked list._

**Doubly linked** means that each node can point to 2 other nodes, the node in front of it **and the node behind it.** As we can see from the example below, since there is no node preceding the head node (which is 5), one of its pointers points to null.

![Image](https://cdn-media-1.freecodecamp.org/images/ucPAE2WqQmZiN1dIkbtr4LpONEZW-UPPnPyI)
_An example of a doubly linked list._

### Okay, I understand all of that. But how does the code work?

Coding Linked Lists can be a **4 line problem or a 400 line problem.** It depends on how you want to approach it.

On the simplest level, like we discussed, a linked list is just a **bunch of connected nodes.**

Thus, all we really need to create this structure is a node object.

```
class linkedListNode:    def __init__(self, value, nextNode=None):        self.value = value        self.nextNode = nextNode
```

Here we can see we’ve simply created a class that has a value and nextNode attribute.

To create a node, we simply pass in a value.

```
node1 = linkedListNode("3") # "3"node2 = linkedListNode("7") # "7"node3 = linkedListNode("10") # "10"
```

Here, we’ve created 3 individual nodes.

The next step is simply to connect them together.

```
node1.nextNode = node2 node2.nextNode = node3 
```

The first line above makes node1 point to node2:

“3” →“7”

The second line above makes node2 point to node3:

“7”→”10"

All together, we’re left with a Linked List that looks like this:

“3”→”7"→”10"→Null

**Note: “10” points to null, because there was no nextNode assigned to node3, and the default nextNode is Null.**

Like I mentioned earlier, there are a lot of different ways to do this. This is just the simplest.

If you are trying to make an entire LinkedList class, [this video](https://www.youtube.com/watch?v=6sBsF13n5ig) goes in depth on how to do that.

### Traversing A Linked List

If you’re doing a programming interview, and you get asked a Linked List question, you’re not going to be given all the nodes.

All you’ll get is the head node.

![Image](https://cdn-media-1.freecodecamp.org/images/05jgbOs3qG84t7qmpEd-Ubhl9QyQgYWUiiV-)
_All that’s being passed in here is the head node._

From that head node, you have to get the rest of the list.

First let’s understand how to get the value and nextNode from a node in Python.

Let’s say we have a node simply named ‘node’.

Getting the value of the node:

```
node.value
```

Getting the nextNode of the node:

```
node.nextNode
```

#### **Traversal**

This first thing we want to do is create a variable called “currentNode” that keeps track of the node we’re at. We want to assign this to our head node at first.

```
currentNode = head
```

Now all we have to do is simply check whether or not our current node is Null. If it’s not, we make our ‘currentNode’ equal to the ‘nextNode’ of the ‘currentNode’.

```
currentNode = node1while currentNode is not None:    currentNode = currentNode.nextNode
```

Let’s say we have the following Linked List: “3”→”7"→”10".

Our head and first ‘currentNode’ is “3”.

When we do

```
currentNode = currentNode.nextNode
```

We are reassigning ‘currentNode’ to our current node’s neighbor, which in this case is “7”.

This continues until the currentNode is pointed to None, in which case the loop stops.

And that is the basic way to traverse through a Linked List in Python.

[Link to the code on Github.](https://github.com/AtotheY/YoutubeTutorials/blob/master/Introductions/linkedListOnlyNodes.py)

### Inserting elements

When you insert an element into a linked list, you insert it into the back unless specified otherwise.

Let’s use the following example:

“3”→”7"→”10"→Null

Let’s say we want to insert a “4”.

We would simply find the tail node, in this case “10”, and set its nextNode to our “4” node.

“3”→”7"→”10"→“4”→Null

```
node4 = linkedListNode("4")node3.nextNode = node4
```

Now let’s say we were in an interview, and all we had was the head node.

We simply traverse through the LinkedList to find the tail. Once we have the tail, we simply set its nextNode to our new node that we create.

```
def insertNode(head, valuetoInsert):    currentNode = head    while currentNode is not None:        if currentNode.nextNode is None:            currentNode.nextNode = linkedListNode(valuetoInsert)            return head        currentNode = currentNode.nextNode
```

### Deleting elements

Deleting can get a bit tricky.

Let’s take the same example.

“3”→”7"→”10"→Null

If we wanted to delete the “7”, all we need to do is point the “3” to the “10” so that the “7” is never referenced.

“3”→”10"→Null

To do this, we would have to traverse the list while not only keeping track of the currentNode, but also keeping track of the **previousNode.**

We would also have to account for the head node being the node we want to delete.

In the code below, we simply delete the first instance of the value we want to delete.

Note that there are many ways to accomplish this, and the solution below might not be the cleanest code you’ll see in your life. However, in the heat of an interview, the interviewer probably won’t expect textbook perfect code.

```
def deleteNode(head, valueToDelete):    currentNode = head    previousNode = None    while currentNode is not None:        if currentNode.value == valueToDelete:            if previousNode is None:                 newHead = currentNode.nextNode                currentNode.nextNode = None                return newHead # Deleted the head            previousNode.nextNode = currentNode.nextNode            return head        previousNode = currentNode        currentNode = currentNode.nextNode    return head # Value to delete was not found.
```

In the code above, once we find the node we want to delete, we set the previous node’s “nextNode” to the deleted node’s “nextNode” to completely cut it out of the list.

### Big O Time Complexity Analysis

****NOTE** These are the time complexities for the node structure above, which is most likely to appear on an interview. In practical cases, you can store attributes in a LinkedList class to lower these complexities.**

‘n’ = the amount of elements inside the Linked List.

**Inserting to the back of the Linked List—** We go through all n elements to find the tail and insert our new node. **O(n)**

**Inserting to the front of the Linked List —** We simply create the new node and set its nextNode to the head. No need to traverse the list. **O(1)**

**Traversing —** We go through all n elements once. **O(n)**

**Deleting —** Worst case scenario, the node we’re deleting is the last node, causing us to traverse through the entire list. **O(n)**

### You can now tackle Linked List interview questions!

You now have the fundamental knowledge you need to start tackling Linked List interview questions!

They can start off easy, and get tough really quick.

In the next article, I’m going to go over a couple of common questions and techniques you can use to solve them.

**If you’re a student looking to land your dream internship or full-time job within the next 2 years, start practicing now!**

I’ve started a community ([www.theforge.ca](http://www.theforge.ca)) where we connect students with mentors and industry experts that help them navigate their way to their dream job.

Thanks for reading, and good luck!


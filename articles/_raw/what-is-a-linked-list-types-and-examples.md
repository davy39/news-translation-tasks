---
title: What is a Linked list? Types of Linked List with Code Examples
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2024-03-18T15:25:17.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-linked-list-types-and-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/john-petter-fagerhaug-nlT3NvhGKt8-unsplash.jpg
tags:
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: PHP
  slug: php
seo_title: null
seo_desc: "A linked list is a linear data structure consisting of a sequence of nodes.\
  \ Unlike arrays, linked lists do not require contiguous memory allocation. Instead,\
  \ each node is dynamically allocated its own memory space. \nNodes are connected\
  \ through refere..."
---

A linked list is a linear data structure consisting of a sequence of nodes. Unlike arrays, linked lists do not require contiguous memory allocation. Instead, each node is dynamically allocated its own memory space. 

Nodes are connected through references, forming the linked structure. One advantage of linked lists is that insertion and deletion of elements at the beginning of the list can be done in constant time, denoted as O(1). 

This efficiency stems from the ability to directly manipulate references without needing to shift elements as required in arrays. Data types in a linked list can be any of the available data types supported by a programming language.

In this tutorial, you'll learn the following:

<ul>
  <li><a href="#understanding-linked-list">Understanding Linked list</a></li>
  <li><a href="#types-of-linked-list">Types of Linked List</a></li>
    <li><a href="#summary-of-operations">Summary of operations with their respective time and space complexities in tabular format.</a></li>
  <li><a href="#differentiate-between-array-and-linked-list">Differences Between Array and Linked list.</a></li>
  <li><a href="#how-to-solve-the-remove-duplicates-from-sorted-list-problem">Algorithm: Solve the Remove Duplicates from Sorted list in PHP and JavaScript.</a></li>
</ul>

<h2 id="understanding-linked-list"> Understanding Linked list </h2>

![Untitled-2024-01-31-1554](https://www.freecodecamp.org/news/content/images/2024/02/Untitled-2024-01-31-1554.png)

head => Points to the first box in the list  
tail => Points to the last box in the list

To access the data in the first box

head.data => 6

To access the data in the second box, we first need to set the pointer (arrow) to point to the box. Hence we need the (next)  
head.next => This points to the next item on the list  
head.next.data => 4

To access the data in the third box, we first need to set the pointer (arrow) to point to the box. Hence we need the (next.next)  
head.next.next => This points to the next > next item on the list  
head.next.next.data => 5

### What is a node ?

![node](https://www.freecodecamp.org/news/content/images/2024/02/node.png)

A node in a linked list is an example of a self-referential structure in programming. This structure is comprised of elements called nodes, where each node contains both data and a reference to another node of the same type. This reference, often termed a 'pointer,' facilitates the creation of a chain-like structure, where nodes are interconnected, forming the linked list.

The self-referential nature of nodes allows for efficient traversal and manipulation of data within the linked list. The structure can be implemented using classes or arrays

### How to Implement a Linked List Using classes

```php
class Node {
    public function __construct(
        public $data,
        public ?Node $next = null
    ) {}
}

// Creating nodes

$node1 = new Node(10);
$node2 = new Node(20);
$node3 = new Node(30);

// Linking nodes

$node1->next = $node2;
$node2->next = $node3;

// Traversing linked list

$current = $node1;
while ($current != null) {
    echo $current->data . " ";
    $current = $current->next;
}
```

### How to Implement a Linked List Using Using arrays

```php
// creating nodes as an associative array

$node1 = ['data' => 10, 'next' => null];
$node2 = ['data' => 20, 'next' => null];
$node3 = ['data' => 30, 'next' => null];

// linking nodes

$node1['next'] = &$node2;
$node2['next'] = &$node3;

// Traversing linked list

$current = $node1;
while ($current != null) {
  echo $current["data"] . " ";
  $current = &$current["next"];
}
```

In both cases, we create a structure where each element (node) contains data and a reference (next) to another element of the same type. This creates a self-referential structure. We then link these elements together to form a data structure like a linked list. Finally, we traverse the structure to access and manipulate its elements.

Unlike an array, a linked list doesn't provide constant time access to a particular index within the list. This means that if you'd like to find the nth element in the list, you'll need to traverse through to the nth element. 

Traversing a linked list means iterating through each node of the list until the end node is reached.

<h2 id="types-of-linked-list"> Types of Linked list</h2>

We'll discuss the types under the Traversal, Memory and Complexity categories.

## Singly Linked List

Each node has data and a reference to the next node. 

![singly linked list](https://www.freecodecamp.org/news/content/images/2024/02/singly-2.png)

### Non-code explanation

Imagine taking a journey by train, where each train represents a part of your trip, and each station represents a point where you need to make a change.

* Train A represents the first part of your journey, taking you from Station A to Station B. When you arrive at Station B, there's a sign directing you to switch trains to continue your journey.
* Train B represents the second part of your journey, taking you from Station B to Station C. Again, when you arrive at Station C, there's no sign for another train because you've reached your final destination.

In this analogy:

* Each train segment (Train A, Train B, and Train C) represent a node in the singly linked list.
* The task of each train is analogous to the data stored in each node, representing a segment of your journey.
* The transition between trains at each station is analogous to the "next" pointer in a linked list, indicating the next segment of your journey.
* At the final destination (Station C), there's no need for a pointer or sign to another train because it's the end of your journey.

In simpler terms, a singly linked list is like a train journey with different segments, where each train (node) has the task of taking you from one station to the next until you reach your final destination. The transitions between trains are like pointers, guiding you through each segment of your journey.

### Performance Characteristics of Singly Linked List

1. **Traversal:** Traversal is allowed only in one direction (that is, forward only). You can move forward through the list, but you cannot easily move backward. 
2. **Memory Efficiency:** Singly linked list is generally more memory-efficient because it requires only one reference per node. 
3. **Complexity:** Insertion and Deletion operation is easier as you only need to update references in one direction.

### Time and Space Complexity

I wrote about constant and linear time complexity [here](https://www.freecodecamp.org/news/what-is-a-hash-map/), and we'll be using that to discuss the general time and space complexities for some common operations:

#### Traversal

Time complexity O(n), where n is the number of nodes in the list. Space complexity O(1), it doesn't require additional space proportional to the input size.

#### Insertion at the Beginning

Time complexity O(1), it involves updating references at the head. Space complexity O(1), it doesn't require additional space proportional to the input size.

#### Insertion at the End

Time complexity O(n), it may require traversing the entire list to reach the end. Space complexity O(1), it doesn't require additional space proportional to the input size.

#### Deletion at the Beginning

Time complexity O(1), it involves updating references at the head. Space complexity O(1), constant.

#### Deletion at the End

Time complexity O(n), it may require traversing the entire list to reach the end. Space complexity O(1), constant.

## Doubly Linked List

In a doubly linked list, the `head` node typically does not have a `prev` reference because it is the first node and therefore has no previous node. 

However, the `head` node does have a `next` reference pointing to the next node in the list. Each node has data and references to both the next and previous nodes.

![doubly-1inked-list](https://www.freecodecamp.org/news/content/images/2024/02/doubly-1.png)

### Non-code explanation 

Imagine that you have a book where each page represents a task you need to complete, just like items on your to-do list.

Each page does not only contain information about the task written on it but also has connections to the pages before and after it in the book.

* Page 1 (Task A) represents the first task in the book. It contains information about Task A and has an arrow pointing forward to Page 2 (Task B), indicating that Task B comes after Task A in the book. However, Page 1 does not have a backward arrow because it is the first page of the book and doesn't have a previous page.
* Page 2 (Task B) contains information about Task B and has arrows pointing both forward to Page 3 (Task C) and backward to Page 1 (Task A), indicating that Task C comes after Task B and Task A comes before Task B in the book.
* Page 3 (Task C) represents the last task in the book. It contains information about Task C and has an arrow pointing backward to Page 2 (Task B), indicating that Task B comes before Task C in the book.

With this in mind, you can think of a doubly linked list as a book where each page not only contains information about a task but also provides easy navigation to the tasks before and after it. The first page, similar to the head of a doubly linked list, does not have a previous reference, while the last page, similar to the tail of a doubly linked list, does not have a next reference

### Performance Characteristics of Doubly Linked Lists

1. **Traversal:** Doubly linked lists allow traversal in both directions — forward and backward. This bidirectional traversal enables more flexible navigation through the list, allowing operations such as iterating in reverse order.
2. **Memory Efficiency**: Doubly linked lists typically require more memory compared to singly linked lists because each node contains two references (pointers) — one for the next node and one for the previous node. This additional memory overhead per node can impact the overall memory efficiency, especially for large lists.
3. **Complexity**: Doubly linked lists offer bidirectional traversal and flexibility. Insertion and deletion operations may require updating references in both directions (forward and backward), which can increase the complexity and potentially impact performance.

### Time and Space Complexity

#### Traversal

The time and space complexity for this operation is the same with the singly linked list.

#### Insertion at the Beginning

The time and space complexity for this operation is the same with the singly linked list.

#### Insertion at the End

Time complexity for this operation takes O(1) time. This is because you have direct access to the tail node, so you can update the references without needing to traverse the entire list. Space complexity O(1), it doesn't require additional space proportional to the input size.

#### Deletion at the Beginning

The time and space complexity for this operation is the same with the singly linked list.

#### Deletion at the End

Time complexity for this operation takes O(1) time. This is because you have direct access to the tail node, so you can update the references without needing to traverse the entire list. Space complexity O(1), it doesn't require additional space proportional to the input size.

## Circular Linked List

A circular linked list is a type of linked list where the last node of the list points back to the first node, forming a circle or loop. This characteristic distinguishes it from a traditional linked list, where the last node typically points to null, indicating the end of the list. In a circular linked list, there is no null pointer at the end; instead, the last node points back to the first node, creating a loop structure. This looping behavior allows for continuous traversal through the list. The below image shows how a singly circular linked list works.

![circular-linked-list-1](https://www.freecodecamp.org/news/content/images/2024/02/circular-linked-list-1.png)


### Non-code explanation

Imagine a train line that forms a loop, with passengers boarding and exiting at various stations along the way. This loop represents a circular linked list, where each station is a node and the train continuously travels around the loop, picking up and dropping off passengers. 

Just like in a circular linked list, the loop ensures continuous traversal without an end point, and passengers (data) can be added or removed at any station (node).  
  
The circular linked list offers advantages in certain applications but requires careful handling of pointers and memory management to maintain its circular structure and prevent issues such as infinite loops.

### Performance Characteristics of Circular Linked Lists

1. **Traversal:** Circular linked lists enable traversal in a loop, allowing seamless navigation from one node to another regardless of the direction. This circular structure facilitates efficient traversal without needing to iterate back to the beginning when reaching the end, enhancing traversal performance.
2. **Memory Efficiency**: Singly circular linked lists typically offer similar memory efficiency to singly linked lists, as they require only one pointer per node to connect to the next node in the sequence. This single-pointer structure results in lower memory overhead per node compared to doubly linked lists, potentially improving memory efficiency for large lists.
3. **Complexity:** In singly circular linked lists, insertion and deletion operations require updating references to maintain the circular structure, introducing moderate complexity compared to linear linked lists.

### Time and Space Complexity

#### Traversal

Time Complexity: O(n) – Since you have to traverse through all the nodes in the list to reach the end. 

Space Complexity: O(1) – Only a constant amount of extra space is required for a temporary variable to traverse the list.

#### Insertion at the Beginning

Time Complexity: O(1) – Insertion at the beginning simply involves updating the references at the head. 

Space Complexity: O(1) – No additional space is required.

#### Insertion at the End

Time Complexity: O(n) – It may require traversing the entire list to reach the end where insertion needs to take place.

Space Complexity: O(1) – No additional space is required.

#### Deletion at the Beginning

Time complexity O(1), it involves updating references at the head. 

Space complexity O(1), constant.

#### Deletion at the End

Time complexity O(n), it may require traversing the entire list to reach the end.

Space complexity O(1), constant.

<h2 id="summary-of-operations"> Summary of Operations for the Time Complexity </h2>

<table>
<thead>
<tr>
<th>Operation</th>
<th>Singly Linked List</th>
<th>Doubly Linked List</th>
<th>Circular Linked List</th>
</tr>
</thead>
<tbody>
<tr>
<td>Traversal</td>
<td>O(n)</td>
<td>O(n)</td>
<td>O(n)</td>
</tr>
<tr>
<td>Insertion at Beginning</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Insertion at End</td>
<td>O(n)</td>
<td>O(1)</td>
<td>O(n)</td>
</tr>
<tr>
<td>Deletion at Beginning</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Deletion at End</td>
<td>O(n)</td>
<td>O(1)</td>
<td>O(n)</td>
</tr>
</tbody>
</table>


<h2 id="summary-of-operations"> Summary of Operations for the Space Complexity </h2>

<table>
<thead>
<tr>
<th>Operation</th>
<th>Singly Linked List</th>
<th>Doubly Linked List</th>
<th>Circular Linked List</th>
</tr>
</thead>
<tbody>
<tr>
<td>Traversal</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Insertion at Beginning</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Insertion at End</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Deletion at Beginning</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Deletion at End</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
</tbody>
</table>

<h2 id="differentiate-between-array-and-linked-list"> Differences Between Array and Linked list </h2>

A linked list is a dynamic way to represent a list, where adding and removing items from the beginning of the list typically involves changing only a few pointers. This operation can be performed in constant time, denoted as O(1), regardless of the list's size.

On the other hand, arrays are a sequential representation of a list. Adding or removing items from the beginning of the list requires shifting all subsequent elements to accommodate the change. This operation has a time complexity of O(n), where n is the number of elements in the array. Therefore, for large arrays, adding or removing items from the beginning can be relatively slow compared to linked lists.

<h2 id="how-to-solve-the-remove-duplicates-from-sorted-list-problem"> How to Solve the Remove Duplicates from Sorted List Problem </h2>

Explanation of the problem: Given the `head` of a sorted linked list, _delete all duplicates such that each element appears only once_. Return _the linked list **sorted**_ as well.

![algo-sample-3](https://www.freecodecamp.org/news/content/images/2024/02/algo-sample-3.png)


### Solution in PHP

```php
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */


class Solution {

    /**
     * @param ListNode $head
     * @return ListNode
     */
    function deleteDuplicates($head) {
        $node = $head;

        while($node !== null && $node->next !== null) {
         
            if ($node->val == $node->next->val) {
                $node->next = $node->next->next;
            }else {
                $node = $node->next;
            }   
        }

        return $head;
    }
}

```

### Solution in JavaScript

```javascript
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */


var deleteDuplicates = function(head) {
    let node = head;

    while(node?.next) {

        if (node.val === node.next.val) {
            node.next = node.next.next
        } else {
            node = node.next
        }
    }

    return head
};

```

**Code explanation**

Given the `deleteDuplicates` method:

* `node` is initialized to the head of the linked list.
* A while loop iterates through the linked list until the end or until the current node's `next` property is `null`.
* Inside the loop, it checks if the current node's value is equal to the next node's value. If they are equal, it skips the next node by setting the current node's `next` property to the next node's `next` property.
* If the values are not equal, it moves to the next node by updating the value of `node` to `node->next`.
* Finally, the method returns the head of the modified linked list.

The null safe operator (`?.`) used in the JS code solution is also available from PHP 8.0. 

This code efficiently removes duplicates from a singly-linked list by adjusting pointers and has a time complexity of `_O_(_n_)` and a space complexity of `_O_(1)`, where _`n`_ is the number of nodes in the linked list.

## Reference

* [How does a linked list work](https://www.freecodecamp.org/news/how-linked-lists-work/)

## Conclusion

In this article, you learned about linked list, types of linked list and a real world problem that involves solving the removal of duplicates from sorted list.

Keep learning, and Happy Coding!

You can find me on [LinkedIn](https://www.linkedin.com/in/suleolanrewaju/) and [Twitter](https://twitter.com/bigdevlarry).


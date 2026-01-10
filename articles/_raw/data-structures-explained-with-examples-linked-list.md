---
title: Data Structures Explained with Examples - Linked List
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/data-structures-explained-with-examples-linked-list
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cfb740569d1a4ca353d.jpg
tags:
- name: data structures
  slug: data-structures
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Just like a garland is made with flowers, a linked list is made up of nodes.
  We call every flower on this particular garland to be a node. And each of the node
  points to the next node in this list as well as it has data (here it is type of
  flower).

  T...'
---

Just like a garland is made with flowers, a linked list is made up of nodes. We call every flower on this particular garland to be a node. And each of the node points to the next node in this list as well as it has data (here it is type of flower).

## **Types**

### Singly Linked List

Singly linked lists contain nodes which have a `data` field as well as a `next` field, which points to the next node in the sequence. Operations that can be performed on singly linked lists are insertion, deletion and traversal.

```text
   head
    |
    |
  +-----+--+      +-----+--+      +-----+------+
  |  1  |o----->  |  2  |o----->  |  3  | NULL |
  +-----+--+      +-----+--+      +-----+------+
```

Internal implementation of CPython, the frames and evaluated variables are kept on a stack.

For this we need to iterate only forward aur get the head, therefore singly linked-list is used.

### Doubly Linked List

Doubly linked lists contain node which have `data` field, `next` field and another link field `prev` pointing to the previous node in the sequence.

```text
          head
           |
           |
  +------+-----+--+    +--+-----+--+       +-----+------+
  |      |     |o------>  |     |o------>  |     |      |
  | NULL |  1  |          |  2  |          |  3  | NULL |
  |      |     |  <------o|     |  <------o|     |      |
  +------+-----+--+    +--+-----+--+       +-----+------+
```

The browser cache which allows you to hit the BACK and FORWARD button. Here we need to maintain a doubly linked list, with `URLs` as data field, to allow access in both direction. To go to previous URL we will use `prev` field and to go to next page we will use `next` field.

### Circular Linked List

Circular linked lists is a singly linked list in which last node, `next` field points to first node in the sequence.

```text
     head
      |
      |
    +-----+--+      +-----+--+      +-----+--+
    —> | 1 |o-----> | 2 |o----->    | 3 |o----| 
    +-----+--+      +-----+--+      +-----+--+
```

Timesharing problem solved by the operating system.

In a timesharing environment, the operating system must maintain a list of present users and must alternately allow each user to use a small portion of CPU time, one user at a time. The operating system will pick a user, let him/her use a small amount of CPU time and then move on to the next user.

For this application, there should be no NULL pointers unless there is absolutely no one requesting CPU time, i.e list is empty.

## **Basic Operations**

### Insertion

To add a new element to the list.

Insertion at the beginning:

* Create a new node with given data.
* Point new node’s `next` to old `head`.
* Point `head` to this new node.

Insertion in the middle/end.

Insertion after node X.

* Create a new node with given data.
* Point new node’s `next` to old X’s `next`.
* Point X’s `next` to this new node.

**Time Complexity: O(1)**

### Deletion

To delete existing element from the list.

Deletion at the beginning

* Get the node pointed by `head` as Temp.
* Point `head` to Temp’s `next`.
* Free memory used by Temp node.

Deletion in the middle/end.

Deletion after node X.

* Get the node pointed by `X` as Temp.
* Point X’s `next` to Temp’s `next`.
* Free memory used by Temp node.

**Time Complexity: O(1)**

### Traversing

To travel across the list.

Traversal

* Get the node pointed by `head` as Current.
* Check if Current is not null and display it.
* Point Current to Current’s `next` and move to above step.

**Time Complexity: O(n) // Here n is size of link-list**

## **Implementation**

### **C++ implementation of singly linked list**

```text
// Header files
#include <iostream>

struct node
{
    int data;
    struct node *next;
};

// Head pointer always points to first element of the linked list
struct node *head = NULL;
```

#### **Printing data in each node**

```text
// Display the list
void printList()
{
    struct node *ptr = head;

    // Start from the beginning
while(ptr != NULL)
{
    std::cout << ptr->data << " ";
    ptr = ptr->next;
}

std::cout << std::endl;
}
```

#### **Insertion at the beginning**

```text
// Insert link at the beginning
void insertFirst(int data)
{
    // Create a new node
    struct node *new_node = new struct node;

    new_node->data = data;

// Point it to old head
new_node->next = head;

// Point head to new node
head = new_node;

std::cout << "Inserted successfully" << std::endl;
}
```

#### **Deletion at the beginning**

```text
// Delete first item
void deleteFirst()
{
    // Save reference to head
    struct node *temp = head;

    // Point head to head's next
head = head->next;

// Free memory used by temp
temp = NULL:
delete temp;

std::cout << "Deleted successfully" << std::endl;
}
```

#### **Size**

```text
// Find no. of nodes in link list
void size()
{
    int length = 0;
    struct node *current;

    for(current = head; current != NULL; current = current->next)
{
    length++;
}

std::cout << "Size of Linked List is " << length << std::endl;
}
```

#### **Searching**

```text
// Find node with given data
void find(int data){

    // Start from the head
struct node* current = head;

// If list is empty
if(head == NULL)
{
    std::cout << "List is empty" << std::endl;
    return;
}

// Traverse through list
while(current->data != data){

    // If it is last node
    if(current->next == NULL){
        std::cout << "Not Found" << std::endl;
        return;
    }
    else{
        // Go to next node
        current = current->next;
    }
}

// If data found
std::cout << "Found" << std::endl;
}
```

#### **Deletion after a node**

```text
// Delete a node with given data
void del(int data){

    // Start from the first node
struct node* current = head;
struct node* previous = NULL;

// If list is empty
if(head == NULL){
    std::cout << "List is empty" << std::endl;
    return ;
}

// Navigate through list
while(current->data != data){

    // If it is last node
    if(current->next == NULL){
        std::cout << "Element not found" << std::endl;
        return ;
    }
    else {
        // Store reference to current node
        previous = current;
        // Move to next node
        current = current->next;
    }

}

// Found a match, update the node
if(current == head) {
    // Change head to point to next node
    head = head->next;
}
else {
    // Skip the current node
    previous->next = current->next;
}

// Free space used by deleted node
current = NULL;
delete current;
std::cout << "Deleted succesfully" << std::endl;
}
```

### **Python Implementation of Singly Linked List**

```text
class Node(object):
    # Constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # Function to get data
def get_data(self):
    return self.data

# Function to get next node
def get_next(self):
    return self.next

# Function to set next field
def set_next(self, new_next):
    self.next = new_next
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
```

#### **Insertion**

```text
    # Function to insert data
def insert(self, data):
    # new_node is a object of class Node
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node
    print("Node with data " + str(data) + " is created succesfully")
```

#### **Size**

```text
    # Function to get size
def size(self):
    current = self.head
    count = 0
    while current:
        count += 1
        current = current.get_next()
    print("Size of link list is " + str(count))
```

#### **Searching**

```text
    # Function to search a data
def search(self, data):
    current = self.head
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            current = current.get_next()
    if current is None:
        print("Node with data " + str(data) + " is not present")
    else:
        print("Node with data " + str(data) + " is found")
```

#### **Deletion after a node**

```text
    # Function to delete a node with data
def delete(self, data):
    current = self.head
    previous = None
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            previous = current
            current = current.get_next()
    if current is None:
        print("Node with data " + str(data) + " is not in list")
    elif previous is None:
        self.head = current.get_next()
        print("Node with data " + str(data) + " is deleted successfully")
    else:
        previous.set_next(current.get_next())
        print("Node with data " + str(data) + " is deleted successfully")
```

**Advantages**

1. Linked lists are a dynamic data structure, which can grow and shrink, allocating and deallocating memory while the program is running.
2. Insertion and deletion of node are easily implemented in a linked list at any position.

**Disadvantages**

1. They use more memory than arrays because of the memory used by their pointers (`next` and `prev`).
2. Random access is not possible in linked list. We have to access nodes sequentially.
3. It’s more complex than array. If a language supports array bound check automatically, Arrays would serve you better.

#### **Note**

We have to use free() in C and delete in C++ to free the space used by deleted node, whereas, in Python and Java free space is collected automatically by garbage collector.


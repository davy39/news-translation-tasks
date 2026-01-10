---
title: 'Real world data structures: tables and graphs in JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-22T16:20:55.000Z'
originalURL: https://freecodecamp.org/news/real-world-data-structures-tables-and-graphs-in-javascript-bcb70c929495
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l60KCqKpGbwvSTqO301VZg.jpeg
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

  An aerial view of boxes with addresses, each containing people & various items,
  shows neighborhoods connected by their roads. Viewed up close, you may say that
  we have a hash table. But, when viewed from afar, you might see a graph. ...'
---

By Yung L. Leung

An aerial view of boxes with addresses, each containing people & various items, shows neighborhoods connected by their roads. Viewed up close, you may say that we have a **hash table.** But, when viewed from afar, you might see a **graph**. Advancing from [**linear**](https://medium.com/@yunglleung1/linear-data-structures-linked-lists-stacks-queues-a13c7591ad87) **(**linked lists, stacks & queues**)** and [**binary**](https://medium.com/@yunglleung1/binary-data-structures-trees-heaps-962ab536cb42) **(**binary search trees, binary heaps**) data structures**, **hash tables,** and **graphs** are steps towards a greater diversity of real-world applications.

### Tables

A **hash table** represents data (key-value pairs) tabulated by indexes.

![Image](https://cdn-media-1.freecodecamp.org/images/ZUvaqYuUfuop4ImFdmh8ETIYuIOzpdTKRA4l)
_[source](https://www.geeksforgeeks.org/implementing-our-own-hash-table-with-separate-chaining-in-java/" rel="noopener" target="_blank" title=")_

Each unique key is used to generate an index (hash function). A hash function can generate the same index for several unique keys (**collision**). A solution to this problem is to store the data sets under the same index (**chaining**).

So, you can imagine a **hash table** being a system for shelving similar items together. Simply enter the item name into a **hash function** and all the greenish type items will be assigned a shelf space, i.e. 4.

![Image](https://cdn-media-1.freecodecamp.org/images/ZUHz2n8mBe59eDg2pYEh5lKSwqoH8tx25K3p)
_[source](http://verticalcarousel.com.au/wp-content/uploads/2015/05/003.gif" rel="noopener" target="_blank" title=")_

In general, a key-value pair **insert** requires generating an **index** (shelf number), checking whether that shelf exists, and placing the item (**data**) on the shelf. Suppose I had bananas and apples on the bottom shelf (**index 0**) and red wine on my top shelf (**index 2**).

![Image](https://cdn-media-1.freecodecamp.org/images/LGr1DoJ-ff7xBfWKUNsvjzAhBRyvyfbu2at-)
_**Stock items of 10 bananas, 20 apples &amp; 3 bottles of red wine**_

If my index generator (**hash function**) returned an **index 2** for my 2 “rotisserie chickens,” to insert that data requires checking for and creating shelf space.

![Image](https://cdn-media-1.freecodecamp.org/images/kuBoqej6nIc86-NkYK3dn4dSacva67PQ-Cg9)
_Added stock items of 2 rotisserie chickens_

To get a **value** (item) requires inputting its name (**key**) to generate its index (shelf number) and retrieving all items on that shelf. Then searching for the exact item (its name or key) and retrieving it (return value). So, to find how many apples are in stock (**20**) requires iterating through my shelf of fruits.

To get a list of all **keys** or **values** requires searching through each existing shelf, logging it into your manifest (push into an array), and submitting the documents (return keys or values array).

![Image](https://cdn-media-1.freecodecamp.org/images/2dzLy-laxGEJeh-82AriZNVRZrFNR3nc8DSX)
_Keys (items) &amp; Values (quantity) of Hash Table (shelves of stock items)_

The complexity to **insert** a key-value pair or **access** a value is, in general, a constant time (**O(1)**). A good hash function evenly distributes all items to all available shelves. So, **insertion or access** does not require looping through all existing “shelves” for storage or retrieval of data.

Because cataloging (**keys or values**) requires going through all shelves, it has a complexity **O(n)**. For **n** different data sets (for 4 different items), requires **n steps** to perform a catalog (requires looking through all 4 items to document its name or its quantity).

### Graphs

A **graph** is nodes (**vertices**) of data related by their connections (**edges**). A road map of cities connected by their roads is a graph. A graph of connected users from a social media app is another example.

![Image](https://cdn-media-1.freecodecamp.org/images/tigLuAgDy-UgPVLMxl1J8cY4Ad0ibhgHXkQG)
_[source](http://allthingsgraphed.com/2014/11/02/twitter-friends-network/" rel="noopener" target="_blank" title=")_

To **add a vertex** and an **edge** requires storing them as key-value pairs in an **adjacency list**. So a vertex (New York) can be connected to other vertices (New Jersey & Pennsylvania) by making “New York” a key to an array containing “New Jersey,” “Pennsylvania.”

![Image](https://cdn-media-1.freecodecamp.org/images/TIVezWjeMZplRJMlfSouOvwh0aLT2JjOlllu)
_**List of All States Adjacent to New York**_

The reverse must also be implemented, i.e.: “New Jersey” pointing to an array of “New York,” “Pennsylvania,” and so forth. So the result is an adjacency list of keys (“New York,” “New Jersey,” “Pennsylvania”), each pointing to arrays of their corresponding connections.

![Image](https://cdn-media-1.freecodecamp.org/images/WxoaIC-fYN31u0y7wUSLzoYyyPI2MMKrWEQk)
_**Complete Adjacency List from Google Maps**_

To **remove edge** requires removing vertex1’s connection to vertex2 and the reverse. So, to remove New York’s connection to New Jersey requires, also, removing New Jersey’s connection to New York.

![Image](https://cdn-media-1.freecodecamp.org/images/s5U41Kuzl32KdTufMakqs46-ae2bXCTEtJ-y)
_**Updated Adjacency List from Google Maps**_

To **remove a vertex** requires iterating through its connections. Removing its edges, before finally deleting the vertex from the adjacency list. So, to remove New York requires disconnecting it from its neighbors before deleting from the list.

![Image](https://cdn-media-1.freecodecamp.org/images/LSlDfdqy6hctdAAbQo81-oFpT1P1ZFrhaZNU)
_**Adjacency List without New York from Google Maps**_

Relative to a starting point, a **depth-first** traversal involves visiting a neighbor and its neighbors, before proceeding with the next immediate neighbor. A **breadth-first** traversal involves visiting all immediate neighbors before distant neighbors.

So for a graph with New York, New Jersey, Pennsylvania & Virginia as vertices, a **depth-first** traversal starting from New Jersey would be [“New Jersey”, “Pennsylvania”, “Virginia”, “New York”].

![Image](https://cdn-media-1.freecodecamp.org/images/bZWSlshOSxdFmeauaEAbiqYDVDVrfqn3FKdv)
_**Graph of New York, New Jersey, Pennsylvania &amp; Virginia from Google Maps**_

A **breadth-first** from New Jersey would be [“New Jersey”, “New York”, “Pennsylvania”, “Virginia”].

Since a **graph** is a set of nodes connected, [**linear**](https://medium.com/@yunglleung1/linear-data-structures-linked-lists-stacks-queues-a13c7591ad87) & [**binary**](https://medium.com/@yunglleung1/binary-data-structures-trees-heaps-962ab536cb42) **data structures** can, in a sense, be viewed as simple graphs. Because graphs can take many different forms & shapes, the **complexity of traversal** through a graph depends on the algorithm(s) used for the traveling, a discussion best saved for another time.

### References:

[https://www.udemy.com/js-algorithms-and-data-structures-masterclass/](https://www.udemy.com/js-algorithms-and-data-structures-masterclass/)


---
title: Find the Shortest Path Between Two Points on a Graph with Dijkstra's Algorithm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T21:29:00.000Z'
originalURL: https://freecodecamp.org/news/find-the-shortest-path-between-two-points-on-a-graph-with-dijkstras-algorithm
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9df6740569d1a4ca3aa2.jpg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
seo_title: null
seo_desc: "Finding the shortest path between two points on a graph is a common problem\
  \ in data structures, especially when dealing with optimization. \nA graph is a\
  \ series of nodes connected by edges. Graphs can be weighted (edges carry values)\
  \ and directional (..."
---

Finding the shortest path between two points on a graph is a common problem in data structures, especially when dealing with optimization. 

A graph is a series of nodes connected by edges. Graphs can be weighted (edges carry values) and directional (edges have direction).

Some applications of this are flight path optimization or [6 degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon).

## **Dijkstra’s Algorithm**

The most common solution for this problem is Dijkstra’s algorithm which updates the shortest path between the current node and all of its neighbors. 

After updating the distance of all of the neighbors it moves to the node with the lowest distance and repeats the process with all unvisited neighbors. This process continues until the entire graph has been visited.

![Image of Levels of Code](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

### Step 0:

Our graph needs to be setup so that we can record the required values. On any edge we have the distance between the two nodes it connects. On any node we have its shortest distance from the starting node. 

Let's set the value on every node to positive infinity, and set the value on the starting node to zero.

### Step 1:

Look at all nodes directly adjacent to the starting node. The values carried by the edges connecting the start and these adjacent nodes are the shortest distances to each respective node. 

Record these distances on the node - overwriting infinity - and also cross off the nodes, meaning that their shortest path has been found.

### Step 2:

Select one of the nodes which has had its shortest path calculated, we’ll call this our pivot. Look at the nodes adjacent to it (we’ll call these our destination nodes) and the distances separating them. 

For every destination node: 

* If the value in the pivot plus the edge value connecting it totals less than the destination node’s value, then update its value, as a new shorter path has been found. 
* If all routes to this destination node have been explored, it can be crossed off.

### Step 3:

Repeat step 2 until all nodes have been crossed off. We now have a graph where the values held in any node will be the shortest distance to it from the start node.

#### **More Information:**

[More On Dijkstra’s algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[Other Shortest path algorithms](https://en.wikipedia.org/wiki/Shortest_path_problem#Algorithms)


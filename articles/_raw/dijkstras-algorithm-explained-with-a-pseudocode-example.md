---
title: Dijkstra's Algorithm – Explained with a Pseudocode Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-12-01T20:57:53.000Z'
originalURL: https://freecodecamp.org/news/dijkstras-algorithm-explained-with-a-pseudocode-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/michael-dziedzic-vLmo8kAVVt4-unsplash--2-.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: null
seo_desc: 'You can use algorithms in programming to solve specific problems through
  a set of precise instructions or procedures.

  Dijkstra''s algorithm is one of many graph algorithms you''ll come across. It is
  used to find the shortest path from a fixed node to a...'
---

You can use algorithms in programming to solve specific problems through a set of precise instructions or procedures.

Dijkstra's algorithm is one of many graph algorithms you'll come across. It is used to find the shortest path from a fixed node to all other nodes in a graph.

There are different representations of Dijkstra's algorithm. You can either find the shortest path between two nodes, or the shortest path from a fixed node to the rest of the nodes in a graph. 

In this article, you'll learn how Dijkstra's algorithm works with the help of visual guides.

## How Does Dijkstra’s Algorithm Work?

Before we dive into more detailed visual examples, you need to understand how Dijkstra's algorithm works. 

Although the theoretical explanation may seem a bit abstract, it'll help you understand the practical aspect better.

In a given graph containing different nodes, we are required to get the shortest path from a given node to the rest of the nodes. 

These nodes can represent any object like the names of cities, letters, and so on.

Between each node is a number denoting the distance between two nodes, as you can see in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/nodes-1.png)

We usually work with two arrays – one for visited nodes, and another for unvisited nodes. You'll learn more about the arrays in the next section. 

When a node is visited, the algorithm calculates how long it took to get to the node and stores the distance. If a shorter path to a node is found, the initial value assigned for the distance is updated.

Note that a node cannot be visited twice. 

The algorithm runs recursively until all the nodes have been visited. 

## Dijkstra's Algorithm Example

In this section, we'll take a look at a practical example that shows how Dijkstra's algorithm works. 

Here's the graph we'll be working with:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/nodes.png)

We'll use the table below to put down the visited nodes and their distance from the fixed node:

| Node   |Shortest distance from fixed node|
|----------|:-------------:|
| A |  ∞ |
| B |    ∞   |
| C | ∞ |
| D |  ∞ |
| E |    ∞   |

Visited nodes = []  
Unvisited nodes = [A,B,C,D,E]

Above, we have a table showing each node and the shortest distance from the that node to the fixed node. We are yet to choose the fixed node. 

Note that the distance for each node in the table is currently denoted as infinity (∞). This is because we don't know the shortest distance yet.

We also have two arrays – visited and unvisited. Whenever a node is visited, it is added to the visited nodes array. 

Let's get started!

To simplify things, I'll break the process down into iterations. You'll see what happens in each step with the aid of diagrams. 

### Iteration #1

The first iteration might seem confusing, but that's totally fine. Once we start repeating the process in each iteration, you'll have a clearer picture of how the algorithm works.

##### **Step #1 - Pick an unvisited node**

We'll choose **A** as the fixed node. So we'll find the shortest distance from **A** to every other node in the graph. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node1-1.png)

We're going to give **A** a distance of 0 because it is the initial node. So the table would look like this:

| Node   |Shortest distance from fixed node|
|----------|:-------------:|
| A |  0 |
| B |    ∞   |
| C | ∞ |
| D |  ∞ |
| E |    ∞   |

##### **Step #2 - Find the distance from current node**

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node1a-3.png)

The next thing to do after choosing a node is to find the distance from it to the unvisited nodes around it. 

The two unvisited nodes directly linked to **A** are **B** and **C**.

To get the distance from **A** to **B**: 

0 + 4 = 4

0 being the value of the current node (**A**), and 4 being the distance between **A** and **B** in the graph. 

To get the distance from **A** to **C**: 

0 + 2 = 2

##### **Step #3 - Update table with known distances**

In the last step, we got 4 and 2 as the values of **B** and **C** respectively. So we'll update the table with those values:

| Node   |Shortest distance from fixed node|
|----------|:-------------:|
| A |  0 |
| B |    4   |
| C | 2 |
| D |  ∞ |
| E |    ∞   |

##### **Step #4 - Update arrays**

At this point, the first iteration is complete. We'll move node **A** to the visited nodes array:

Visited nodes = [A]  
Unvisited nodes = [B,C,D,E]

Before we proceed to the next iteration, you should know the following:

* Once a node has been visited, it cannot be linked to the current node. Refer to step #2 in the iteration above and step #2 in the next iteration. 
* A node cannot be visited twice. 
* You can only update the shortest known distance if you get a value smaller than the recorded distance. 

### Iteration #2

##### **Step #1 - Pick an unvisited node**

We have four unvisited nodes — [B,C,D,E]. So how do you know which node to pick for the next iteration?

Well, we pick the node with the smallest known distance recorded in the table. Here's the table:

| Node   |Shortest distance from fixed node|
|----------|:-------------:|
| A |  0 |
| B |    4   |
| C | 2 |
| D |  ∞ |
| E |    ∞   |

So we're going with node **C**.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node2-2.png)

##### **Step #2 - Find the distance from current node**

To find the distance from the current node to the fixed node, we have to consider the nodes linked to the current node. 

The nodes linked to the current node are **A** and **B**.

But **A** has been visited in the previous iteration so it will not be linked to the current node. That is:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node2a-1.png)

From the diagram above,

* The green color denotes the current node.
* The blue color denotes the visited nodes. We cannot link to them or visit them again.
* The red color shows the link from the unvisited nodes to the current node. 

To find the distance from **C** to **B**:

2 + 1 = 3

2 above is recorded distance for node **C** while 1 is the distance between **C** and **B** in the graph. 

##### **Step #3 - Update table with known distances**

In the last step, we got the value of **B** to be 3. In the first iteration, it was 4. 

We're going to update the distance in the table to 3. 

| Node   |Shortest distance from fixed node|
|----------|:-------------:|
| A |  0 |
| B |    3   |
| C | 2 |
| D |  ∞ |
| E |    ∞   |

So, **A** --> **B** = 4 (First iteration).

**A** --> **C** --> **B** = 3 (Second iteration).

The algorithm has helped us find the shortest path to **B** from **A**.

##### **Step #4 - Update arrays**

We're done with the last visited node. Let's add it to the visited nodes array:

Visited nodes = [A,C]  
Unvisited nodes = [B,D,E]

### Iteration #3

##### **Step #1 - Pick an unvisited node**

We're down to three unvisited nodes — [B,D,E]. From the array, **B** has the shortest known distance. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node3-2.png)

To restate what is going on in the diagram above:

* The green color denotes the current node.
* The blue color denotes the visited nodes. We cannot link to them or visit them again.
* The red color shows the link from the unvisited nodes to the current node. 

##### **Step #2 - Find the distance from current node**

The nodes linked to the current node are **D** and **E**.

**B** (the current node) has a value of 3. Therefore,

For node **D**, 3 + 3 = 6.

For node **E**, 3 + 2 = 5.

##### **Step #3 - Update table with known distances**

| Node   |Shortest distance from fixed node|
|----------|:-------------:|
| A |  0 |
| B |    3   |
| C | 2 |
| D |  6 |
| E |    5   |

##### **Step #4 - Update arrays**

Visited nodes = [A,C,B]  
Unvisited nodes = [D,E]

### Iteration #4

##### **Step #1 - Pick an unvisited node**

Like other iterations, we'll go with the unvisited node with the shortest known distance. That is **E**.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node4-1.png)

##### **Step #2 - Find the distance from current node**

According to our table, **E** has a value of 5. 

For **D** in the current iteration, 

5 + 5 = 10. 

The value gotten for **D** here is 10, which is greater than the recorded value of 6 in the previous iteration. For this reason, we'll not update the table. 

##### **Step #3 - Update table with known distances**

Our table remains the same:

| Node   |Shortest distance from fixed node|
|----------|:-------------:|
| A |  0 |
| B |    3   |
| C | 2 |
| D |  6 |
| E |    5   |

##### **Step #4 - Update arrays**

Visited nodes = [A,C,B,E]  
Unvisited nodes = [D]

### Iteration #5

##### **Step #1 - Pick an unvisited node**

We're currently left with one node in the unvisited array — **D**.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/node5-1.png)

##### **Step #2 - Find the distance from current node**

The algorithm has gotten to the last iteration. This is because all nodes linked to the current node have been visited already so we can't link to them. 

##### **Step #3 - Update table with known distances**

Our table remains the same:

| Node   |Shortest distance from fixed node|
|----------|:-------------:|
| A |  0 |
| B |    3   |
| C | 2 |
| D |  6 |
| E |    5   |

At this point, we have updated the table with the shortest distance from the fixed node to every other node in the graph. 

##### **Step #4 - Update arrays**

Visited nodes = [A,C,B,E,D]  
Unvisited nodes = []

As can be seen above, we have no nodes left to visit. Using Dijkstra's algorithm, we've found the shortest distance from the fixed node to others nodes in the graph.

## Dijkstra's Algorithm Pseudocode Example

The pseudocode example in this section was gotten from [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). Here it is:

```txt
 1  function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
```

## Applications of Dijkstra's Algorithm

Here are some of the common applications of Dijkstra's algorithm:

* In maps to get the shortest distance between locations. An example is Google Maps. 
* In telecommunications to determine transmission rate.
* In robotic design to determine shortest path for automated robots. 

## Summary

In this article, we talked about Dijkstra's algorithm. It is used to find the shortest distance from a fixed node to all other nodes in a graph. 

We started by giving a brief summary of how the algorithm works. 

We then had a look at an example that further explained Dijkstra's algorithm in steps using visual guides. 

We concluded with a pseudocode example and some of the applications of Dijkstra's algorithm. 

Happy coding!



---
title: Coding Interview Graph Traversal Crash Course – The Only One You'll Ever Need
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-09-09T17:24:25.000Z'
originalURL: https://freecodecamp.org/news/coding-interview-graph-traversal-crash-course-the-only-one-youll-ever-need
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Coding-Interview-Series-1-.png
tags:
- name: algorithms
  slug: algorithms
- name: coding interview
  slug: coding-interview
seo_title: null
seo_desc: 'Are you preparing for coding interviews? I designed a crash course series
  to help you out.

  I''m Lynn, a software engineer and a recent graduate from the University of Chicago.
  This is the third course in my Coding Interview Crash Course Series. Feel f...'
---

Are you preparing for coding interviews? I designed a crash course series to help you out.

I'm Lynn, a software engineer and a recent graduate from the University of Chicago. This is the third course in my Coding Interview Crash Course Series. Feel free to check out [my YouTube channel, Lynn's DevLab](https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw), to stay updated on this series.

This crash course is about **Graph Traversal.** If you just want to dive right in, you can find the course here (and linked at the bottom of this article). If you want a little more info, read on. 😎

%[https://youtu.be/d31vGF-Z69c] 

## Introduction

We will cover two common graph traversal techniques: **Depth-First Search (DFS)** and **Breadth-First Search (BFS).**

We will first learn about how they work and how to implement them in code. Then we will see the algorithms in action by solving a LeetCode problem as well as looking at how I applied Graph Traversal when implementing an algorithm for my game, [**Clicky Galaxy**](https://github.com/RuolinZheng08/unity-clicky-galaxy) (also my first game in Unity when I was learning Unity 😉).

![Image](https://www.freecodecamp.org/news/content/images/2021/08/clicky.gif align="left")

*Clicky Galaxy, a game I made when learning Unity*

## Course Outline

[This course video](https://youtu.be/d31vGF-Z69c) runs for 1 hour and features:

* A high-level description of Graphs, DFS, and BFS
    
* DFS implementation
    
* BFS implementation
    
* How to find a path between a source and a destination node
    
* LeetCode Demo: 785. Is Graph Bipartite?
    
* Clicky Galaxy Demo and Graph Traversal in Unity C# 🚀
    

Graphs are a favorite interview subject among top tech companies like Google, Microsoft, and Facebook. More importantly, it's also fun and useful in practical software engineering like Game Development. Let's crunch this topic together in my course!

## Definition of a Graph

We will use the following graph to show the traversal path for the two traversal algorithms.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-21-at-08.41.06.png align="left")

We may represent the graph by mapping each node to its list of neighbors, as shown in this Python snippet:

```python
graph = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}
```

## How to Use Depth-First Search

As its name suggests, DFS prioritizes depth in its search.

For a given node (say 1), after visiting one of its neighbors (say 0), instead of visiting the rest of the neighbors (nodes 2, 3, and 4) immediately, it caches those neighbors and immediately resumes its visit on 0's neighbors. Only when it has exhausted the depth will it return to those cached neighbors.

### Iterative Implementation

```python
def dfs(graph, start):
  visited, stack = set(), [start]
  while stack:
    node = stack.pop()
    if not node in visited:
        # perform some operations on the node
        # for example, we print out the node
        print('Now visiting', node)
    visited.add(node)
    for neighbor in graph[node]:
      if not neighbor in visited:
        stack.append(neighbor)
  return visited
```

In this template, the commented lines are where we can perform some operations on the node: for example, printing out its value, checking for equality, and so on.

We keep track of a set named **visited** to avoid visiting the same node multiple times where there is a cycle in the graph, like in our example graph above.

Running this code on the graph we defined above results in the output below:

```python
Now visiting 0
Now visiting 4
Now visiting 3
Now visiting 2
Now visiting 1
```

## How to Use Breadth-First Search

BFS prioritizes breadth in its search. For a given node, it visits all of its immediate neighbors before moving onto the neighbors' neighbors.

### Iterative Implementation

```python
def bfs(graph, start):
  visited, queue = set(), deque([start])
  while queue:
    node = queue.popleft()
    if not node in visited:
        # perform some operations on the node
        print('Now visiting', node)
    visited.add(node)
    for neighbor in graph[node]:
      if not neighbor in visited:
          queue.append(neighbor)
  return visited
```

Running this code on the graph we defined above results in the output below:

```python
Now visiting 0
Now visiting 1
Now visiting 4
Now visiting 2
Now visiting 3
```

## How to Find a Path Between a Source and a Destination

Now that we've seen how to use DFS and BFS to traverse the entire graph and print out the whole traversal history, we can make some small changes to the templates to find a **path** between any two nodes in the graph (if such path exists).

On a graph where each edge has the same weight, BFS is equivalent to **Dijkstra's Shortest Path Algorithm**. It finds the shortest path (path with the fewest number of nodes) between a source node and a destination node. This is a nice property that a path search with DFS doesn't have.

Here's how we adapt the DFS template to return a path given a **src** and a **dst** node:

```python
def dfs_path(graph, src, dst):
  stack = [(src, [src])]
  visited = set()
  while stack:
    node, path = stack.pop()
    if node in visited:
      continue
    if node == dst:
      return path
    visited.add(node)
    for neighbor in graph[node]:
      stack.append((neighbor, path + [neighbor]))
  return None
```

Similarly for BFS:

```python
def bfs_path(graph, src, dst):
  visited, queue = set(), deque([[src]])
  while queue:
    path = queue.popleft()
    node = path[-1]
    if node in visited:
      continue
    if node == dst:
      return path
    for neighbor in graph[node]:
      queue.append(path + [neighbor])
  return None
```

## Let's Solve a LeetCode Problem!

Let's now apply what we learned about Graph Traversal to solve a problem on [LeetCode, 785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)

According to [this article](https://www.geeksforgeeks.org/bipartite-graph/), a modified BFS algorithm is all we need:

> Following is a simple algorithm to find out whether a given graph is Bipartite or not using Breadth First Search (BFS).
> 
> 1. Assign RED color to the source vertex (putting into set U).
>     
> 2. Color all the neighbors with BLUE color (putting into set V).
>     
> 3. Color all neighbor’s neighbor with RED color (putting into set U).
>     
> 4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2.
>     
> 5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot be colored with 2 vertices (or graph is not Bipartite)
>     

Plugging our template, the solution is as simple as follows. Check out [my video](https://youtu.be/d31vGF-Z69c) for a line-by-line explanation.

```python
RED = 0
BLUE = 1
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return False
        queue, visited = deque([]), set()
        for v in range(len(graph)):
            if v in visited:
                continue
            queue.append(v)
            node_colors = {v: RED}
            while queue:
                node = queue.popleft()
                visited.add(node)
                my_color = node_colors[node]
                for neighbor in graph[node]:
                    if neighbor in node_colors and node_colors[neighbor] == my_color:
                        return False
                    if not neighbor in visited:
                        queue.append(neighbor)
                    node_colors[neighbor] = RED if my_color == BLUE else BLUE

        return True
```

## Graph Traversal in Action: Clicky Galaxy, A Game by Me

One more fun demo about Graph Traversal: Clicky Galaxy 🚀, a casual match-three game I built when I was learning Unity.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/clicky.png align="left")

In the game, you move a planet to an empty cell and score when there are three or more identical planets aligned horizontally or vertically. A planet can only move horizontally or vertically, and its movement path cannot be obstructed by other planets.

I applied Graph Traversal to check for a valid path between the planet the player clicked on and the destination cell to determine if the planet can move to that cell.

Each cell in the grid is a node and has four immediate neighbors: up, down, left, and right. As I want to find a short path between the source and the destination (if there exists one), **BFS pathfinding** is ideal for my use case.

Here is how my code looks like in C#. I used a helper named **GetNeighbors** to get the four immediate neighbors, ignoring out-of-bound ones.

```csharp
List<Vector2Int> BreadthFirstSearch(Vector2Int srcIndices, Vector2Int dstIndices) {
    // identify a path from srcIndices to dstIndices, could be null
    // the path include src and dst
    HashSet<Vector2Int> visited = new HashSet<Vector2Int>();
    Queue<List<Vector2Int>> pathQueue = new Queue<List<Vector2Int>>();

    List<Vector2Int> startPath = new List<Vector2Int>();
    startPath.Add(srcIndices);
    pathQueue.Enqueue(startPath);

    while (pathQueue.Count > 0) {
        List<Vector2Int> path = pathQueue.Dequeue();
        Vector2Int node = path[path.Count - 1];
        if (visited.Contains(node)) {
            continue;
        }
        if (node == dstIndices) { // done
            return path;
        }
        visited.Add(node);
        List<Vector2Int> neighbors = GetNeighbors(node);
        foreach (Vector2Int neighbor in neighbors) {
            Sprite sprite = GetSpriteAtIndices(neighbor.x, neighbor.y);
            if (sprite == null) { // can visit this next
                List<Vector2Int> newPath = new List<Vector2Int>(path);
                newPath.Add(neighbor);
                pathQueue.Enqueue(newPath);
            }
        }
    }

    return null;
}

List<Vector2Int> GetNeighbors(Vector2Int indices) {
    // return the four immediate neighbors, left, right, up, down
    List<Vector2Int> neighbors = new List<Vector2Int>();
    if (indices.x >= 0 && indices.x < gridDimension && indices.y >= 0 && indices.y < gridDimension) {
        if (indices.y >= 1) {
            neighbors.Add(new Vector2Int(indices.x, indices.y - 1));
        }
        if (indices.y < gridDimension - 1) {
            neighbors.Add(new Vector2Int(indices.x, indices.y + 1));
        }
        if (indices.x >= 1) {
            neighbors.Add(new Vector2Int(indices.x - 1, indices.y));
        }
        if (indices.x < gridDimension - 1) {
            neighbors.Add(new Vector2Int(indices.x + 1, indices.y));
        }
    }
    return neighbors;
}
```

And my game came together really well with this algorithm!

![Image](https://www.freecodecamp.org/news/content/images/2021/08/clicky-1.gif align="left")

## Final Thoughts

In this crash course, we learned about the two Graph Traversal algorithms, DFS and BFS. We saw them in implementation first and then in action in a LeetCode problem as well as in my game.

If you enjoyed Graphs, think about how they relate to Trees. Spoiler alert! Pre-order traversal in trees is essentially DFS in graphs and level-order traversal in trees is essentially BFS in graphs. 🤫

Try figuring this out on your own or watch [my crash course on Tree Traversal](https://youtu.be/uaeCfsCcYWo) for a refresher. Trust me, algorithms can be fun! 😃

## Resources

Watch the course here:

%[https://youtu.be/d31vGF-Z69c] 

Access the code template on my GitHub:

%[https://gist.github.com/RuolinZheng08/a86a3940a23d653bae4d5c399c06639e] 

Check out Clicky Galaxy on my GitHub:

%[https://github.com/RuolinZheng08/unity-clicky-galaxy] 

Stay up-to-date with the whole crash course series:

%[https://youtube.com/playlist?list=PLKcjA7XxXuvSsE-_heuBxIvzWcx4IKfXD] 

And lastly, feel free to subscribe to my YouTube channel for more content like this :)

%[https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw]

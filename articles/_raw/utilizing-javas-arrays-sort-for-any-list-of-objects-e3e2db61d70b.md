---
title: Using Java’s Arrays.sort() for any List of Objects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-07T16:39:21.000Z'
originalURL: https://freecodecamp.org/news/utilizing-javas-arrays-sort-for-any-list-of-objects-e3e2db61d70b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Aap5LkZQvXhukGZicn8_vA.jpeg
tags:
- name: Java
  slug: java
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ethan Arrowood

  Sorting can be tricky, especially when your list is not of a primitive Java numeric
  type (Byte, Integer, Short, Long, Double, Float). Now, all situations will vary
  so this method might not be the best case. However, I’ve found it in...'
---

By Ethan Arrowood

Sorting can be tricky, especially when your list is not of a primitive Java numeric type (Byte, Integer, Short, Long, Double, Float). Now, all situations will vary so this method might not be the best case. However, I’ve found it incredibly useful for simple coding challenges and university lab assignments.

To start, pick your list. For this example I’ll be using a list of `Edges` from a simple `Graph` data structure:

```
// Very simple Edge classpublic class Edge {    public Vertex src;    public Vertex dst;    public double cost;        // creates an edge between two vertices    Edge(Vertex s, Vertex d, double c) {        src = s;        dst = d;        cost = c;    }}
```

```
// List of edgesEdge[] edges = graph.getEdges();
```

Next, define the implementation of the `java.util.Comparator` interface:

```
class SortByCost implements Comparator<Edge> {    public int compare(Edge a, Edge b) {        if ( a.cost < b.cost ) return -1;        else if ( a.cost == b.cost ) return 0;        else return 1;    }}
```

In this example, we will be sorting the `edges` by their cost, or distance from the `src` (source) vertex to the `dst` (destination) vertex.

Finally use the standard `java.util.Arrays.sort()` method:

```
Arrays.sort(edges, new SortByCost())
```

And just like that, the list of `Edges` is now sorted in ascending (least to greatest) order.

If you have any questions feel free to reach out on [Twitter](https://twitter.com/ArrowoodTech)

You can also find me on [GitHub](https://github.com/ethan-arrowood) or my personal [website](https://ethanarrowood.com)

~ Happy Coding

— Ethan Arrowood


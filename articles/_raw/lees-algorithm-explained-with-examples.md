---
title: Lee's Algorithm Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-28T19:35:00.000Z'
originalURL: https://freecodecamp.org/news/lees-algorithm-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e6c740569d1a4ca3d00.jpg
tags:
- name: algorithms
  slug: algorithms
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'The Lee algorithm is one possible solution for maze routing problems. It
  always gives an optimal solution, if one exists, but is slow and requires large
  memory for dense layout.

  Understanding how it works

  The algorithm is a breadth-first based algori...'
---

The Lee algorithm is one possible solution for maze routing problems. It always gives an optimal solution, if one exists, but is slow and requires large memory for dense layout.

### **Understanding how it works**

The algorithm is a `breadth-first` based algorithm that uses `queues` to store the steps. It usually uses the following steps:

1. Choose a starting point and add it to the queue.
2. Add the valid neighboring cells to the queue.
3. Remove the position you are on from the queue and continue to the next element.
4. Repeat steps 2 and 3 until the queue is empty.

One key concept to understand is that `breadth-first` searches go wide, while `depth-first` searches go deep.

Using the example of a maze solving algorithm, a `depth-first` approach will try every possible path one by one until it either reaches a dead end or the finish and returns the result. However the path it returns might not be the most efficient, but simply the first complete path to the finish that the algorithm was able to find.

A `breadth-first` search will instead go out to each open space adjacent to the starting point, then look for other possible open spaces. It will keep doing this, going out layer by layer and trying each possible path in tandem, until it finds the finish point. Since you're trying each path at the same time, you can be sure that the first complete path from start to finish is also the shortest. 

### **Implementation**

C++ has the queue already implemented in the `<queue>` library, but if you are using something else you are welcome to implement your own version of queue.

C++ code:

```cpp
int dl[] = {-1, 0, 1, 0}; // these arrays will help you travel in the 4 directions more easily
int dc[] = {0, 1, 0, -1};

queue<int> X, Y; // the queues used to get the positions in the matrix

X.push(start_x); //initialize the queues with the start position
Y.push(start_y);

void lee()
{
  int x, y, xx, yy;
  while(!X.empty()) // while there are still positions in the queue
  {
    x = X.front(); // set the current position
    y = Y.front();
    for(int i = 0; i < 4; i++)
    {
      xx = x + dl[i]; // travel in an adiacent cell from the current position
      yy = y + dc[i];
      if('position is valid') //here you should insert whatever conditions should apply for your position (xx, yy)
      {
          X.push(xx); // add the position to the queue
          Y.push(yy);
          mat[xx][yy] = -1; // you usually mark that you have been to this position in the matrix
      }
      
    }
    
    X.pop(); // eliminate the first position, as you have no more use for it
    Y.pop();
    
  }


}
```


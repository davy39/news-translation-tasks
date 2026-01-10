---
title: 'Backtracking Algorithms: Recursive and Search Explained with Examples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-27T18:32:00.000Z'
originalURL: https://freecodecamp.org/news/backtracking-algorithms-recursive-search
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eff740569d1a4ca4042.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: null
seo_desc: 'Examples where backtracking can be used to solve puzzles or problems include:


  Puzzles such as eight queens puzzle, crosswords, verbal arithmetic, Sudoku [nb 1],
  and Peg Solitaire.

  Combinatorial optimization problems such as parsing and the knapsack ...'
---

Examples where backtracking can be used to solve puzzles or problems include:

1. Puzzles such as eight queens puzzle, crosswords, verbal arithmetic, Sudoku [nb 1], and Peg Solitaire.
2. Combinatorial optimization problems such as parsing and the knapsack problem.
3. Logic programming languages such as Icon, Planner and Prolog, which use backtracking internally to generate answers.

### Example Problem (The Knight’s tour problem)

_The knight is placed on the first block of an empty board and, moving according to the rules of chess, must visit each square exactly once._

### Path followed by Knight to cover all the cells

Following is chessboard with 8 x 8 cells. Numbers in cells indicate move number of Knight.

![The knight's tour solution - by Euler](https://upload.wikimedia.org/wikipedia/commons/d/df/Knights_tour_%28Euler%29.png)

### Naive Algorithm for Knight’s tour

The Naive Algorithm is to generate all tours one by one and check if the generated tour satisfies the constraints.

```
while there are untried tours
{ 
   generate the next tour 
   if this tour covers all squares 
   { 
      print this path;
   }
}

```

### Backtracking Algorithm for Knight’s tour

Following is the Backtracking algorithm for Knight’s tour problem.

```
If all squares are visited 
    print the solution
Else
   a) Add one of the next moves to solution vector and recursively 
   check if this move leads to a solution. (A Knight can make maximum 
   eight moves. We choose one of the 8 moves in this step).
   b) If the move chosen in the above step doesn't lead to a solution
   then remove this move from the solution vector and try other 
   alternative moves.
   c) If none of the alternatives work then return false (Returning false 
   will remove the previously added item in recursion and if false is 
   returned by the initial call of recursion then "no solution exists" )

```

### And here's a video explanation for you

%[https://www.youtube.com/watch?v=gBC_Fd8EE8A]



---
title: A step-by-step guide to building a simple chess AI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-30T19:26:08.000Z'
originalURL: https://freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eP0V-xfRWfW3QHJhALJ5RA.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chess
  slug: chess
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Lauri Hartikka

  Let’s explore some basic concepts that will help us create a simple chess AI:


  move-generation

  board evaluation

  minimax

  and alpha beta pruning.


  At each step, we’ll improve our algorithm with one of these time-tested chess-programmi...'
---

By Lauri Hartikka

Let’s explore some basic concepts that will help us create a simple chess AI:

* move-generation
* board evaluation
* minimax
* and alpha beta pruning.

At each step, we’ll improve our algorithm with one of these time-tested chess-programming techniques. I’ll demonstrate how each affects the algorithm’s playing style.

You can view the final AI algorithm here on [GitHub](https://github.com/lhartikk/simple-chess-ai).

### Step 1: Move generation and board visualization

We’ll use the [chess.js](https://github.com/jhlywa/chess.js) library for move generation, and [chessboard.js](https://github.com/oakmac/chessboardjs/) for visualizing the board. The move generation library basically implements all the rules of chess. Based on this, we can calculate all legal moves for a given board state.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_Z_qtrm9ayf_UhycYudE3g.png)
_A visualization of the move generation function. The starting position is used as input and the output is all the possible moves from that position._

Using these libraries will help us focus only on the most interesting task: creating the algorithm that finds the best move.

We’ll start by creating a function that just returns a random move from all of the possible moves:

Although this algorithm isn’t a very solid chess player, it’s a good starting point, as we can actually play against it:

![Image](https://cdn-media-1.freecodecamp.org/images/1*GzOiJRh6Z3FOC3xmPEmKrQ.gif)
_Black plays random moves. Playable on [https://jsfiddle.net/lhartikk/m14epfwb/](https://jsfiddle.net/lhartikk/m14epfwb/" rel="noopener" target="_blank" title=")4_

### Step 2 : Position evaluation

Now let’s try to understand which side is stronger in a certain position. The simplest way to achieve this is to count the relative strength of the pieces on the board using the following table:

![Image](https://cdn-media-1.freecodecamp.org/images/1*e4p9BrCzJUdlqx7KVGW9aA.png)

With the evaluation function, we’re able to create an algorithm that chooses the move that gives the highest evaluation:

The only tangible improvement is that our algorithm will now capture a piece if it can.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fTWDdJ2m3L72X6rqce9_tQ.gif)
_Black plays with the aid of the simple evaluation function. Playable on [https://jsfiddle.net/lhartikk/m5q6fgtb/1/](https://jsfiddle.net/lhartikk/m5q6fgtb/1/" rel="noopener" target="_blank" title=")_

### Step 3: Search tree using Minimax

Next we’re going to create a search tree from which the algorithm can chose the best move. This is done by using the [Minimax](https://en.wikipedia.org/wiki/Minimax) algorithm.

In this algorithm, the recursive tree of all possible moves is explored to a given depth, and the position is evaluated at the ending “leaves” of the tree.

After that, we return either the smallest or the largest value of the child to the parent node, depending on whether it’s a white or black to move. (That is, we try to either minimize or maximize the outcome at each level.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UA5VlNs7s4gl80VknA099w.jpeg)
_A visualization of the minimax algorithm in an artificial position. The best move for white is **b2-c3**, because we can guarantee that we can get to a position where the evaluation is **-50**_

With minimax in place, our algorithm is starting to understand some basic tactics of chess:

![Image](https://cdn-media-1.freecodecamp.org/images/1*xRfitY19MvJW3ynGKWhQ5A.gif)
_Minimax with depth level 2. Playable on: [https://jsfiddle.net/k96eoq0q/1/](https://jsfiddle.net/k96eoq0q/1/" rel="noopener" target="_blank" title=")_

The effectiveness of the minimax algorithm is heavily based on the search depth we can achieve. This is something we’ll improve in the following step.

### Step 4: Alpha-beta pruning

[Alpha-beta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) pruning is an optimization method to the minimax algorithm that allows us to disregard some branches in the search tree. This helps us evaluate the minimax search tree much deeper, while using the same resources.

The alpha-beta pruning is based on the situation where we can stop evaluating a part of the search tree if we find a move that leads to a worse situation than a previously discovered move.

The alpha-beta pruning does not influence the outcome of the minimax algorithm — it only makes it faster.

The alpha-beta algorithm also is more efficient if we happen to visit **first** those paths that lead to good moves.

![Image](https://cdn-media-1.freecodecamp.org/images/1*96QEzhnsOkNqz7swB0qx8w.jpeg)
_The positions we do not need to explore if alpha-beta pruning isused and the tree is visited in the described order._

With alpha-beta, we get a significant boost to the minimax algorithm, as is shown in the following example:

![Image](https://cdn-media-1.freecodecamp.org/images/1*k3DrkWLNq33ei_t-094qpg.png)
_The number of positions that are required to evaluate if we want to perform a search with depth of 4 and the “root” position is the one that is shown._

Follow [this link](https://jsfiddle.net/Laa0p1mh/3/) to try the alpha-beta improved version of the chess AI.

### Step 5: Improved evaluation function

The initial evaluation function is quite naive as we only count the material that is found on the board. To improve this, we add to the evaluation a factor that takes in account the position of the pieces. For example, a knight on the center of the board is better (because it has more options and is thus more active) than a knight on the edge of the board.

We’ll use a slightly adjusted version of piece-square tables that are originally described in the [chess-programming-wiki](https://chessprogramming.wikispaces.com/Simplified+evaluation+function).

![Image](https://cdn-media-1.freecodecamp.org/images/1*iG6FUYZpU0_RKlqHnC8XxA.png)
_The visualized piece-square tables visualized. We can decrease or increase the evaluation, depending on the location of the piece._

With the following improvement, we start to get an algorithm that plays some “decent” chess, at least from the viewpoint of a casual player:

![Image](https://cdn-media-1.freecodecamp.org/images/1*sX_XwfPrOQ6c62iuVZ75fw.gif)
_Improved evaluation and alpha-beta pruning with search depth of 3. Playable on [https://jsfiddle.net/q76uzxwe/1/](https://jsfiddle.net/q76uzxwe/1/" rel="noopener" target="_blank" title=")_

### Conclusions

The strength of even a simple chess-playing algorithm is that it doesn’t make stupid mistakes. This said, it still lacks strategic understanding.

With the methods I introduced here, we’ve been able to program a chess-playing-algorithm that can play basic chess. The “AI-part” (move-generation excluded) of the final algorithm is just 200 lines of code, meaning the basic concepts are quite simple to implement. You can check out the final version is on [GitHub](https://github.com/lhartikk/simple-chess-ai).

Some further improvements we could make to the algorithm would be for instance:

* [move-ordering](https://chessprogramming.wikispaces.com/Move+Ordering)
* faster [move generation](https://chessprogramming.wikispaces.com/Move+Generation)
* and [end-game](https://chessprogramming.wikispaces.com/Endgame) specific evaluation.

If you want to learn more, check out the [chess programming wiki](https://chessprogramming.wikispaces.com/). It’s a helpful resource for exploring beyond these basic concepts I introduced here.

Thanks for reading!


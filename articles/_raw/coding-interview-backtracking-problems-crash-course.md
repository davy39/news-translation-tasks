---
title: Coding Interview Backtracking Problems Crash Course – The Only One You'll Ever
  Need
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-06-29T20:00:32.000Z'
originalURL: https://freecodecamp.org/news/coding-interview-backtracking-problems-crash-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/1080P-Thumbnails-1-.png
tags:
- name: coding interview
  slug: coding-interview
- name: interview questions
  slug: interview-questions
- name: Interview tips
  slug: interview-tips
- name: Job Interview
  slug: job-interview
- name: leetcode
  slug: leetcode
seo_title: null
seo_desc: 'Whether you are new to coding interviews or are already familiar with the
  concept of backtracking algorithms, this is the crash course for you.

  In it, we will learn about an all-purpose coding template for solving backtracking
  problems and apply it t...'
---

Whether you are new to coding interviews or are already familiar with the concept of **backtracking** algorithms, this is the crash course for you.

In it, we will learn about **an all-purpose coding template** for solving backtracking problems and apply it to **two LeetCode hard problems**. Ready to crunch your next coding interview? Let's go!

If you just want to dive right in, [you can find the course here](https://www.youtube.com/watch?v=H2gnD7Ixeao) (and linked at the bottom of this article). If you want a little more info, read on. :)

## Who is the Course for and What is the Backtracking Algorithm?

This course is suitable for anyone who is preparing for coding interviews, especially those who are looking to hone their skills in solving **backtracking** problems.

Backtracking is a common category for questions in coding interviews. The algorithm for solving those problems usually involves **recursion** and **building incrementally on previous states** to arrive at the ultimate valid solution.

Backtracking is a favorite topic among top tech companies like Google, Microsoft, and Facebook, precisely because it requires robust reasoning and coding competence to nail those questions.

However, because of its recursive nature and complex problem definition, backtracking problems are usually a major source of confusion among devs who are preparing for coding interviews.

To address this confusion, this crash course aims to arm with you a concise, 20-line template that you can apply to the majority of backtracking problems.

## Course Outline

This course runs for a total of 40 minutes and the structure is as follows:

* An 8-minute introduction to [the template](https://gist.github.com/RuolinZheng08/cdd880ee748e27ed28e0be3916f56fa6)
    
* A 15-minute hands-on code-along session for [LeetCode Question 51. N-Queens](https://leetcode.com/problems/n-queens/)
    
* A 15-minute hands-on code-along session for [LeetCode Question 37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
    

## The All-Purpose Template

For your convenience, I've copied the template over. This is exactly the same template that I use for my coding interviews, or when I'm developing algorithms for my indie games. I even used it once in my research on a non-convex optimization problem.

```python
def is_valid_state(state):
    # check if it is a valid solution
    return True

def get_candidates(state):
    return []

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)

def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions
```

The first three are all helper functions, and the last and most important one, `solve`, is essentially the one that a LeetCode problem is asking you to write.

## Solving LeetCode Problems Hands-On

We will next apply this template to solving two LeetCode hard problems: [LeetCode Question 51. N-Queens](https://leetcode.com/problems/n-queens/) and [LeetCode Question 37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/).

To illustrate the flexibility of the template, see below for how we solve the N-Queens problem by doing nothing fancy other than adapting the four functions (renaming `solve` to `solveNQueens`). The complete code for either problem is available [in my GitHub gist](https://gist.github.com/RuolinZheng08/cdd880ee748e27ed28e0be3916f56fa6).

Watch [the video course](https://youtu.be/H2gnD7Ixeao) to follow along my analysis and adaptation of the template.

```python
class Solution:
    # solveNQueens is essentially the solve function
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
        
    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        
        # find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))
        # prune down candidates that place the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if it's occupied by a queen
            candidates.discard(col)
            dist = position - row
            # discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
```

Check out the video course here:

%[https://youtu.be/H2gnD7Ixeao] 

You can access the template as well as the solutions to the two LeetCode problems (**N-Queens** and **Sudoku Solver**) in my GitHub gist:

%[https://gist.github.com/RuolinZheng08/cdd880ee748e27ed28e0be3916f56fa6] 

## Final Thoughts

Remember that practice makes perfect, so do try applying this template to [more backtracking problems on LeetCode.](https://leetcode.com/tag/backtracking/) Best of luck crunching your next coding interview!

For more content like this, check out my YouTube channel:

%[https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw]

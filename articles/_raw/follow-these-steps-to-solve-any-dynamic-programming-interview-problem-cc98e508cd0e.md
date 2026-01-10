---
title: Follow these steps to solve any Dynamic Programming interview problem
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-06T19:32:36.000Z'
originalURL: https://freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*DpsbrfUM89M_LHKY.jpg
tags:
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: jobs
  slug: jobs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nikola Otasevic

  Despite having significant experience building software products, many engineers
  feel jittery at the thought of going through a coding interview that focuses on
  algorithms. I’ve interviewed hundreds of engineers at Refdash, Google,...'
---

By Nikola Otasevic

Despite having significant experience building software products, many engineers feel jittery at the thought of going through a coding interview that focuses on algorithms. I’ve interviewed hundreds of engineers at [Refdash](https://refdash.com/?utm_source=dp_blog_f), Google, and at startups I’ve been a part of, and some of the most common questions that make engineers uneasy are the ones that involve Dynamic Programming (DP).

Many tech companies like to ask DP questions in their interviews. While we can debate whether they’re effective in evaluating someone’s ability to perform in an engineering role, DP continues to be an area that trips engineers up on their way to finding a job that they love.

### Dynamic Programming — Predictable and Preparable

One of the reasons why I personally believe that DP questions might not be the best way to test engineering ability is that they’re predictable and easy to pattern match. They allow us to filter much more for preparedness as opposed to engineering ability.

These questions typically seem pretty complex on the outside, and might give you an impression that a person who solves them is very good at algorithms. Similarly, people who may not be able to get over some mind-twisting concepts of DP might seem pretty weak in their knowledge of algorithms.

The reality is different, and the biggest factor in their performance is preparedness. So let’s make sure everyone is prepared for it. Once and for all.

### 7 Steps to solve a Dynamic Programming problem

In the rest of this post, I will go over a recipe that you can follow to figure out if a problem is a “DP problem”, as well as to figure out a solution to such a problem. Specifically, I will go through the following steps:

1. How to recognize a DP problem
2. Identify problem variables
3. Clearly express the recurrence relation
4. Identify the base cases
5. Decide if you want to implement it iteratively or recursively
6. Add memoization
7. Determine time complexity

### Sample DP Problem

For the purpose of having an example for abstractions that I am going to make, let me introduce a sample problem. In each of the sections, I will refer to the problem, but you could also read the sections independently of the problem.

#### Problem statement:

![Image](https://cdn-media-1.freecodecamp.org/images/YIelQx3b0OSZIaNWVkJEmirqOZRZWXm2fbBk)

_In this problem, we’re on a crazy jumping ball, trying to stop, while avoiding spikes along the way._

#### Here are the rules:

1) You’re given a flat runway with a bunch of spikes in it. The runway is represented by a boolean array which indicates if a particular (discrete) spot is clear of spikes. It is True for clear and False for not clear.

Example array representation:

![Image](https://cdn-media-1.freecodecamp.org/images/c5h0NAmIsaNYEjJfcIZa3uPCiTxO28ew9gPV)

2) You’re given a starting speed S. S is a non-negative integer at any given point, and it indicates how much you will move forward with the next jump.

3) Every time you land on a spot, you can adjust your speed by up to 1 unit before the next jump.

![Image](https://cdn-media-1.freecodecamp.org/images/bCnFU8w6zxjnUpypi0ArUOyON6L20E0EPl0p)

4) You want to safely stop anywhere along the runway (does not need to be at the end of the array). You stop when your speed becomes 0. However, if you land on a spike at any point, your crazy bouncing ball bursts and it’s game over.

**The output of your function should be a boolean indicating whether we can safely stop anywhere along the runway.**

#### Step 1: How to recognize a Dynamic Programming problem

First, let’s make it clear that DP is essentially just an optimization technique. DP is a method for solving problems by breaking them down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions. The next time the same subproblem occurs, instead of recomputing its solution, you simply look up the previously computed solution. This saves computation time at the expense of a (hopefully) modest expenditure in storage space.

Recognizing that a problem can be solved using DP is the first and often the most difficult step in solving it. What you want to ask yourself is whether your problem solution can be expressed as a function of solutions to similar smaller problems.

In the case of our example problem, given a point on the runway, a speed, and the runway ahead, we could determine the spots where we could potentially jump next. Furthermore, it seems that whether we can stop from the current point with the current speed depends only on whether we could stop from the point we choose to go to next.

That is a great thing, because by moving forward, we shorten the runway ahead and make our problem smaller. We should be able to repeat this process all the way until we get to a point where it is obvious whether we can stop.

> Recognizing a Dynamic Programming problem is often the most difficult step in solving it. Can the problem solution be expressed as a function of solutions to similar smaller problems?

#### Step 2: Identify problem variables

Now we have established that there is some recursive structure between our subproblems. Next, we need to express the problem in terms of the function parameters and see which of those parameters are changing.

Typically in interviews, you will have one or two changing parameters, but technically this could be any number. A classic example of a one-changing-parameter problem is “determine an n-th Fibonacci number”. Such an example for a two-changing-parameters problem is “Compute edit distance between strings”. If you’re not familiar with these problems, don’t worry about it.

A way to determine the number of changing parameters is to list examples of several subproblems and compare the parameters. Counting the number of changing parameters is valuable to determine the number of subproblems we have to solve. It’s also important in its own right in helping us strengthen the understanding of the recurrence relation from step 1.

In our example, the two parameters that could change for every subproblem are:

1. **Array position (P)**
2. **Speed (S)**

One could say that the runway ahead is changing as well, but that would be redundant considering that the entire non-changing runway and the position (P) carry that information already.

Now, with these 2 changing parameters and other static parameters, we have the complete description of our sub-problems.

> Identify the changing parameters and determine the number of subproblems.

#### Step 3: Clearly express the recurrence relation

This is an important step that many rush through in order to get into coding. Expressing the recurrence relation as clearly as possible will strengthen your problem understanding and make everything else significantly easier.

Once you figure out that the recurrence relation exists and you specify the problems in terms of parameters, this should come as a natural step. How do problems relate to each other? In other words, let’s assume that you have computed the subproblems. How would you compute the main problem?

Here is how we think about it in our sample problem:

Because you can adjust your speed by up to 1 before jumping to the next position, there are only 3 possible speeds, and therefore 3 spots in which we could be next.

More formally, if our speed is S, position P, we could go from (S, P) to:

1. **(S, P + S)**; # if we do not change the speed
2. **(S — 1, P + S — 1)**; # if we change the speed by -1
3. **(S + 1, P + S + 1)**; # if we change the speed by +1

If we can find a way to stop in any of the subproblems above, then we can also stop from (S, P). This is because we can transition from (S, P) to any of the above three options.

This is typically a fine level of understanding of the problem (plain English explanation), but you sometimes might want to express the relation mathematically as well. Let’s call a function that we’re trying to compute canStop. Then:

**canStop(S, P) = canStop(S, P + S) || canStop(S — 1, P + S — 1) || canStop(S + 1, P + S + 1)**

Woohoo, it seems like we have our recurrence relation!

> Recurrence relation: Assuming you have computed the subproblems, how would you compute the main problem?

#### Step 4: Identify the base cases

A base case is a subproblem that doesn’t depend on any other subproblem. In order to find such subproblems, you typically want to try a few examples, see how your problem simplifies into smaller subproblems, and identify at what point it cannot be simplified further.

The reason a problem cannot be simplified further is that one of the parameters would become a value that is not possible given the **constraints** of the problem.

In our example problem, we have two changing parameters, S and P. Let’s think about what possible values of S and P might not be legal:

1. **P should be within the bounds of the given runway**
2. **P cannot be such that runway[P] is false because that would mean that we’re standing on a spike**
3. **S cannot be negative, and a S==0 indicates that we’re done**

Sometimes it can be a little challenging to convert assertions that we make about parameters into programmable base cases. This is because, in addition to listing the assertions if you want to make your code look concise and not check for unnecessary conditions, you also need to think about which of these conditions are even possible.

In our example:

1. **P < 0 || P >= length of** runway seems like the right thing to do. An alternative could be to consider m_aking_ **P == end of** runway a base case. However, it is possible that a problem splits into a subproblem which goes beyond the end of the runway, so we really need to check for inequality.
2. This seems pretty obvious. We can simply check **if runway[P] is false_._**
3. Similar to #1, we could simply check for S < 0 and S == 0. However, here we can reason that it is impossible for S to be < 0 because S decreases by at most 1, so it would have to go through S == 0 case beforehand. Ther**efore** S == 0 is a sufficient base case for the S parameter.

#### Step 5: Decide if you want to implement it iteratively or recursively

The way we talked about the steps so far might lead you to think that we should implement the problem recursively. However, everything that we’ve talked about so far is completely agnostic to whether you decide to implement the problem recursively or iteratively. In both approaches, you would have to determine the recurrence relation and the base cases.

**To decide whether to go iteratively or recursively, you want to carefully think about the trade-offs**.

![Image](https://cdn-media-1.freecodecamp.org/images/E-2qbrD5g7UtOJIN7ULrdwAdgiL0jAU7uGFH)

**Stack overflow issues are typically a deal breaker** and a reason why you would not want to have recursion in a (backend) production system. However, for the purposes of the interview, as long as you mention the trade-offs, you should typically be fine with either of the implementations. You should feel comfortable implementing both.

**In our particular problem, I implemented both versions. Here is python code for that:**  
 A recursive solution: (original code snippets can be found [here](http://blog.refdash.com/dynamic-programming-tutorial-example/))

![Image](https://cdn-media-1.freecodecamp.org/images/MmSzAzTeUbtfjiYFSjilQlCBaXRAsOOIesKL)

An iterative solution: (original code snippets can be found [here](http://blog.refdash.com/dynamic-programming-tutorial-example/))

![Image](https://cdn-media-1.freecodecamp.org/images/aZgiyRIJ3SAD0Mx6lywCaohZt1BUJ0ZW-1Hm)

#### Step 6: Add memoization

**Memoization** is a technique that is closely associated with DP. It is used for storing the results of expensive function calls and returning the cached result when the same inputs occur again.

Why are we adding memoization to our recursion? We encounter the same subproblems which, without memoization, are computed repeatedly. Those repetitions very often lead to exponential time complexities.

In recursive solutions, adding memoization should feel straightforward. Let’s see why. Remember that memoization is just a cache of the function results. There are times when you want to deviate from this definition in order to squeeze out some minor optimizations, but treating memoization as a function result cache is the most intuitive way to implement it.

This means that you should:

1. Store your function result into your memory before every _return_ _statement_
2. Look up the memory for the function result before you start doing any other computation

Here is the code from above with added memoization (added lines are highlighted): (original code snippets can be found [here](http://blog.refdash.com/dynamic-programming-tutorial-example/))

![Image](https://cdn-media-1.freecodecamp.org/images/aAgK5alenVTE0zyCTsknv32r-RTjiFOJmMu6)

In order to illustrate the effectiveness of memoization and different approaches, let’s do some quick tests. I will stress test all three methods that we have seen so far. Here is the set up:

1. I created a runway of length 1000 with spikes in random places (I chose to have a probability of a spike being in any given spot to be 20%)
2. initSpeed = 30
3. I ran all functions 10 times and measured the average time of execution

Here are the results (in seconds):

![Image](https://cdn-media-1.freecodecamp.org/images/bOxJ2uGkAzVHEakgeFnPJMMe44oFIhLAqGh5)

You can see that the pure recursive approach takes about 500x more time than the iterative approach and about 1300x more time than the recursive approach with memoization. Note that this discrepancy would grow rapidly with the length of the runway. I encourage you to try running it yourself.

#### Step 7: Determine Time complexity

There are some simple rules that can make computing time complexity of a dynamic programming problem much easier. Here are two steps that you need to do:

1. Count the number of states — this will depend on the number of changing parameters in your problem
2. Think about the work done per each state. In other words, if everything else but one state has been computed, how much work do you have to do to compute that last state?

In our example problem, the number of states is **|P| * |S|,** where

* P is the set of all positions (|P| indicates the number of elements in P)
* S is the set of all speeds

The work done per each state is O(1) in this problem because, given all other states, we simply have to look at 3 subproblems to determine the resulting state.

As we noted in the code before, |S| is limited by length of the runway (|P|), so we could say that the number of states is |P|² and because work done per each state is O(1), then the total time complexity is O(|P|²).

However, it seems that |S| can be further limited, because if it were really |P|, it is very clear that stopping would not be possible because you would have to jump the length of the entire runway on the first move.

So let’s see how we can put a tighter bound on |S|. Let’s call maximum speed S. Assume that we’re starting from position 0. How quickly could we stop if we were trying to stop as soon as possible and if we ignore potential spikes?

![Image](https://cdn-media-1.freecodecamp.org/images/tnzdVcGH4Npix6BcaJu1vGVlOkcvJo89NYgv)

In the first iteration, we would have to come at least to the point (S-1), by adjusting our speed at zero by -1. From there we would at a minimum go by (S-2) steps forward, and so on.

For a runway of **length L**, the following has to hold:

**=> (S-1) + (S-2) + (S-3) + ….+ 1** < L

**=> S*(S-1) / 2** < L

**=> S² — S — 2L** < 0

If you find roots of the above function, they will be:

**r1 = 1/2 + sqrt(1/4 + 2L) and r2 = 1/2 — sqrt(1/4 + 2L)**

We can write our inequality as:

**(S — r1) * (S — r2) <**; 0

Considering that S — r2 > 0 for any S > 0 and L > 0, we need the following:

**S — 1/2 — sqrt(1/4 + 2L) <**; 0

**=> S < 1/2 + sqrt(1/4** + 2L)

That is the maximum speed that we could possibly have on a runway of a length L. If we had a speed higher than that, we could not stop even theoretically, irrespective of the position of the spikes.

That means that the total time complexity depends only on the length of the runway L in the following form:

O(L * sqrt(L)) which is better than O(L²)

> _O(L * sqrt(L)) is the upper bound on the time complexity_

Awesome, you made it through! :)

The 7 steps that we went through should give you a framework for systematically solving any dynamic programming problem. I highly recommend practicing this approach on a few more problems to perfect your approach.

### **Here are some next steps that you can take**

1. Extend the sample problem by trying to find a path to a stopping point. We solved a problem that tells you whether you can stop, but what if you wanted to also know the steps to take in order to stop eventually along the runway? How would you modify the existing implementation to do that?
2. If you want to solidify your understanding of memoization, and understand that it is just a function result cache, you should read about decorators in Python or similar concepts in other languages. Think about how they would allow you to implement memoization in general for any function that you want to memoize.
3. Work on more DP problems by following the steps we went through. You can always find a bunch of them online (ex. [LeetCode](https://leetcode.com/tag/dynamic-programming/) or [GeeksForGeeks](http://www.geeksforgeeks.org/dynamic-programming/)). As you practice, keep in mind one thing: learn ideas, don’t learn problems. The number of ideas is significantly smaller and it’s an easier space to conquer which will also serve you much better.

When you feel like you’ve conquered these ideas, check out [**Refdash**](https://refdash.com/?utm_source=dp_blog) where you are interviewed by a senior engineer and get a detailed feedback on your coding, algorithms, and system design.

_Originally published at [Refdash blog](http://blog.refdash.com/dynamic-programming-tutorial-example/). Refdash is an interviewing platform that helps engineers interview anonymously with experienced engineers from top companies such as Google, Facebook, or Palantir and get a detailed feedback. [Refdash](https://refdash.com/) also helps engineers discover amazing job opportunities based on their skills and interests._


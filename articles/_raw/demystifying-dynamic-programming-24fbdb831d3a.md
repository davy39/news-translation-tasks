---
title: Demystifying Dynamic Programming
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T00:28:32.000Z'
originalURL: https://freecodecamp.org/news/demystifying-dynamic-programming-24fbdb831d3a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Tyqzs42Dpy2qPZHpcm2HoQ.png
tags:
- name: algorithms
  slug: algorithms
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Prajwal M

  There are many quality articles on how to become a software developer. They teach
  you to program, develop, and use libraries. But little has been done to educate
  in Algorithms and DataStructures. No matter how good you are at development...'
---

By Prajwal M

There are many quality articles on how to become a software developer. They teach you to program, develop, and use libraries. But little has been done to educate in **Algorithms** and **DataStructures**_._ No matter how good you are at development, without knowledge of **Algorithms** and **Data Structures**_,_ you can’t get hired_._

Learning popular algorithms like **Matrix Chain Multiplication, Knapsack or Travelling Salesman** **Algorithms** is not sufficient. Interviewers ask problems like the ones you find on competitive programming sites. To solve such problems, you need to have a good and firm understanding of the concepts.

#### **What is Dynamic Programming?**

According to [Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming), dynamic programming is simplifying a complicated problem by breaking it down into simpler sub-problems in a [recursive](https://en.wikipedia.org/wiki/Recursion) manner. This article will teach you to:

```
-> Identify subproblems
-> Learn how to solve subproblems
-> Identify that subproblems are repetitive 
-> Identify that subproblems have optimal substructure property
-> Learn to cache/store results of sub problems
-> Develop a recursive relation to solve the problem
-> Use top-down and bottom-up approach to solve the problem
```

#### **Which language will I use?**

I know that most people are proficient or have experience coding in JavaScript. Also, once you learn in JavaScript, it is very easy to transform it into Java code. The same can be said of Python or C++. The trick is to understand the problems in the language you like the most. Hence I have chosen to use JavaScript.

**This post is about algorithms and more specifically about dynamic programming. It is generally perceived as a tough topic. If you make it to the end of the post, I am sure you can tackle many dynamic programming problems on your own** ?.

### **Problem Statement**

```
Problem: Given an integer n, find the minimum number of steps to reach integer 1.

At each step, you can:

Subtract 1,

Divide by 2, if it is divisible by 2

Divide by 3, if it is divisible by 3
```

All Dynamic programming problems have a **start state. Y**ou have to reach the **goal** by **transitioning** through a **number of intermediate states**. In a typical textbook, you will often hear the term **subproblem**. It is the same as a **state**. The terms can be used interchangeably. In this article, I will use the term state instead of the term subproblem.

**What is a subproblem or state ?** A subproblem/state is a smaller instance of the original problem. The methods used to solve the original problem and the subproblem are the same.

> _Some problems will give you the rules that specify the state transitions. This is one such problem. This problem says you can move to n-1, n/2 or n/3 starting from n. On the flip side, there are problems that will not specify the state transitions. You will have to figure them out by yourself. I will talk about these types of problems in another post._

Here,

```
Start state -> n
Goal -> 1
Intermediate states -> any integer number between 1 and n
```

Given a state (either start or intermediate), **you can always move to a fixed number of states.**

```
from n you can move to :

n -> n-1 

if n % 2 == 0:
   n -> n/2
   
if n % 3 == 0:
   n -> n/3
   
example:

from 3 you can move to,
3 -> 3-1 = 2
3 -> 3/3 = 1

from 4 you can move to,
4 -> 4-1 = 3
4 -> 4/2 = 2
```

In a dynamic programming optimization problem_,_ you have to determine **moving though which states from start to goal will give you an optimal solution.**

```
For n = 4:

approach one:
4 -> 3 -> 2 -> 1

approach two:
4 -> 2 -> 1 

approach three:
4 -> 3 -> 1
```

Here, of the three approaches, approaches two and three are optimal, as they require smallest amount of moves/transitions. Approach one is the worst, as it requires more moves.

#### **Textbook terminologies explained**

```
Repetitive subproblems : You will end up solving the same problem more than once.

for n = 5
example:
5 -> 4 -> 3 -> 1
5 -> 4 -> 2 -> 1
5 -> 4 -> 3 -> 2 -> 1

observe here that 2 -> 1 occurs two times. 
also observe that 5 -> 4 occurs three times.

Optimal Substructure : Optimal solutions to subproblems give optimal solution to the entire problem

example:
2 -> 1 is optimal 
3 -> 1 is optimal 

when I am at 4,
4 -> 3 -> 2 -> 1 and 4 -> 3 -> 1 is possible
but the optimal solution of 4 is 4 -> 3 -> 1. The optimal solution of four comes from optimal solution of three (3 -> 1).

similarly,
4 -> 3 -> 2 -> 1 and 4 -> 2 -> 1 is possible
but the optimal solution of 4 is 4 -> 2 -> 1. The optimal solution of four comes from optimal solution of two (2 -> 1).

now 5,
The optimal solution of 5 depends on optimal solution to 4.
5 -> 4 -> 2 -> 1 and 5 -> 4 -> 3 -> 1 are optimal.
```

**How should you use Repetitive subproblems and Optimal Substructure to our advantage ?**

> _We will solve the subproblems only once and solve each subproblem optimally._

```
we will solve the subproblems 3 -> 1 and 2 -> 1 only once and optimally.

Now for 4 we will solve only once by 4 -> 3 -> 1 and optimally. You can also solve as 4 -> 2 -> 1 but that is left to you. 

Finally for 5 we will solve only once by 5 - > 4 -> 3 -> 1 and optimally.
```

In practice you will use an array to store the optimal result of a subproblem. This way when you have to solve the subproblem again, you can get the value from the array rather than solving it again. Essentially you are now solving a subproblem only once.

#### **How to measure Optimality**

By using something called **cost**. There is always a cost associated with moving from one state to another state. Cost may be zero or a finite number. The set of moves/transitions that give the optimal cost is the optimal solution.

```
In 5 -> 4 -> 3 -> 1 
for 5 -> 4 cost is 1 
for 4 -> 3 cost is 1
for 3 -> 1 cost is 1

The total cost of 5 -> 4 -> 3 -> 1 is the total sum of 3.

In In 5 -> 4 -> 3 -> 2 -> 1
for 5 -> 4 cost is 1
for 4 -> 3 cost is 1 
for 3 -> 2 cost is 1
for 2 -> 1 cost is 1
The total cost of 5 -> 3 -> 2 -> 1 is the total sum of 4.

The optimal solution of 5 -> 4 -> 3 -> 1 has a cost of three which is the minimum. Hence we can see that optimal solutions have optimal costs
```

**Recursive Relation:** All dynamic programming problems have recursive relations. **Once you define a recursive relation, the solution is merely translating it into code.**

```
For the above problem, let us define minOne as the function that we will use to solve the problem and the cost of moving from one state to another as 1.

if n = 5,
solution to 5 is cost + solution to 4
recursive formulae/relation is 
minOne(5) = 1 + minOne(4) 

Similarly,
if n = 6,
recursive formulae/relation is
minOne(6) = min(             
              1 + minOne(5),
              1 + minOne(3),
              1 + minOne(2) )
```

### **Code**

Dynamic programming problems can be solved by a **top down** approach or a **bottom up** approach.

```
Top Down : Solve problems recursively. 
for n = 5, you will solve/start from 5, that is from the top of the problem.
It is a relatively easy approach provided you have a firm grasp on recursion. I say that this approach is easy as this method is as simple as transforming your recursive relation into code.

Bottom Up : Solve problems iteratively.
for n = 5, you will solve/start from 1, that is from the bottom of the problem.
This approach uses a for loop. It does not lead to stack overflow as in recursion. This approach is also slightly more optimal.
```

#### **Which approach is better?**

It is up to your comfort. Both give the same solutions. In very large problems, bottom up is beneficial as it does not lead to stack overflow. If you choose a input of 10000, the top-down approach will give maximum call stack size exceeded, but a bottom-up approach will give you the solution.

But do remember that you cannot eliminate recursive thinking completely. You will always have to define a recursive relation irrespective of the approach you use.

#### **Bottom-Up approach**

```js
/*
Problem: Given an integer n, find the minimum number of steps to reach integer 1.
At each step, you can:
Subtract 1,
Divide by 2, if it is divisible by 2 
Divide by 3, if it is divisible by 2 
*/


// bottom-up
function minOneBottomUp(n) {

    const cache = [];
    // base condition
    cache[1] = 0;

    for (i = 2; i <= n; i++) {

        // initialize a , b and c to some very large numbers
        let a = 1000, b = 1000, c = 1000;

        // one step from i -> i-1
        a = 1 + cache[i - 1];

        // one step from i -> i/2 if i is divisible by 2
        if (i % 2 === 0) {
            b = 1 + cache[i / 2];
        }

        // one step from i -> i/3 if i is divisible by 3
        if (i % 3 === 0) {
            c = 1 + cache[i / 3];
        }

        // Store the minimum number of steps to reach i
        cache[i] = Math.min(a, b, c);
    }

    // return the number minimum number of steps to reach n
    return cache[n];
}

console.log(minOneBottomUp(1000));
```

```
Line 11 : The function that will solve the problem is named as minOneBottomUp. It takes n as the input.

Line 13 : The array that will be used to store results of every solved state so that there is no repeated computation is named cache. Some people like to call the array dp instead of cache. In general, cache[i] is interpreted as the minimum number of steps to reach 1 starting from i.

Line 15 : cache[1] = 0 This is the base condition. It says that minimum number of steps to reach 1 starting from 1 is 0.

Line 17 - 37 : For loop to fill up the cache with all states from 1 to n inclusive.

Line 20 : Initialize variables a, b and c to some large number. Here a represents minimum number of steps. If I did the operation n-1, b represents the minimum number of steps. If I did the operation n/2, c represents the minimum number of steps. If I did the operation n/3. The initial values of a, b and c depends upon the size of the problem.

Line 23 : a = 1 + cache[i-1]. This follows from the recursive relation we defined earlier.

Line 26 - 28: if(i % 2 == 0){
                  b = 1 + cache[i/2];
              }
              
This follows from the recursive relation we defined earlier.

Line 31 - 33: if(i % 3== 0){
                  c= 1 + cache[i/3];
              }
This follows from the recursive relation we defined earlier.

Line 36 : This the most important step.
cache[i] = Math.min(a, b, c). This essentially determines and stores which of a, b and c gave the minimum number of steps.

Line 40 : All the computations are completed. Minimum steps for all states from 1 to n is calculated. I return cache[n](minimum number of steps to reach 1 starting from n) which is the answer we wanted.

Line 43 : Testing code. It returns a value of 9
```

#### **Top-Down approach**

```js
/*
Problem: Given an integer n, find the minimum number of steps to reach integer 1.
At each step, you can:
Subtract 1,
Divide by 2, if it is divisible by 2 
Divide by 3, if it is divisible by 2 
*/


// top-down
function minOne(n, cache) {

    // if the array value at n is not undefined, return the value at that index
    // This is the heart of dynamic programming 
    if (typeof (cache[n]) !== 'undefined') {
        return cache[n];
    }

    // if n has reached 1 return 0
    // terminating/base condition
    if (n <= 1) {
        return 0;
    }

    // initialize a , b and c to some very large numbers
    let a = 1000, b = 1000, c = 1000;

    // one step from n -> n-1
    a = 1 + minOne(n - 1, cache);

    // one step from n -> n/2 if n is divisible by 2
    if (n % 2 === 0) {
        b = 1 + minOne(n / 2, cache);
    }

    // one step from n -> n/3 if n is divisible by 3
    if (n % 3 === 0) {
        c = 1 + minOne(n / 3, cache);
    }

    // Store the minimum number of steps to reach n 
    return cache[n] = Math.min(a, b, c);

}



const cache = [];
console.log(minOne(1000, cache));
```

```
Line 11 : The function that will solve the problem is named as minOne. It takes n and cache as the inputs.

Line 15 - 16 : It checks if for a particular state the solution has been computed or not. If it is computed it returns the previously computed value. This is the top-down way of not doing repeated computation.

Line 21 - 23 : It is the base condition. It says that if n is 1 , the minimum number of steps is 0.

Line 26 :  Initialize variables a, b and c to some large number. Here a represents minimum number of steps if I did the operation n-1, b represents the minimum number of steps if I did the operation n/2 and c represents the minimum number of steps if I did the operation n/3. The initial values of a, b and c depends upon the size of the problem.

Line 29 : a = 1 + minOne(n-1, cache). This follows from the recursive relation we defined earlier.

Line 32 - 34 : if(n % 2 == 0){
                  b = 1 + minOne(n/2, cache);
              }
This follows from the recursive relation we defined earlier.

Line 37 - 39 : if(n % 3== 0){
                  c = 1 + minOne(n/3, cache);
              }
This follows from the recursive relation we defined earlier.

Line 42 : return cache[n] = Math.min(a, b, c) . This essentially determines and stores which of a, b and c gave the minimum number of steps.

Line 48 - 49 : Testing code. It returns a value of 9
```

#### **Time Complexity**

In Dynamic programming problems, Time Complexity is **the number of unique states/subproblems * time taken per state**.

In this problem, for a given n, there are **n** unique states/subproblems. For convenience, each state is said to be solved in a constant time. Hence the time complexity is **O(n * 1).**

This can be easily cross verified by the for loop we used in the bottom-up approach. We see that we use only one for loop to solve the problem. Hence the time complexity is **O(n ) or linear.**

This is the power of dynamic programming. It allows such complex problems to be solved efficiently.

#### **Space Complexity**

We use one array called cache to store the results of n states. Hence the size of the array is n. Therefore the space complexity is **O(n)**.

#### **DP as Space-Time tradeoff**

Dynamic programming makes use of space to solve a problem faster. In this problem, we are using **O(n)** space to solve the problem in **O(n)** time. Hence we trade space for speed/time. Therefore it’s aptly called the **Space-Time tradeoff.**

### Wrapping up

I hope this post demystifies dynamic programming. I understand that reading through the entire post might’ve been painful and tough, but dynamic programming is a tough topic. Mastering it requires a lot of practice.

I will publish more articles on demystifying different types of dynamic programming problems. I will also publish a article on how to transform a backtracking solution into a dynamic programming solution.

If you like this post, please support by clapping ?(you could go up to 50) and follow me here on Medium ✌️. You can connect with me on [LinkedIn](https://www.linkedin.com/in/prajwalm/) . You can also follow me on [Github](https://github.com/PrajwalM2212).


---
title: Developer Interview Prep – How to Use a Collaborative Approach to Problem-Solving
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-19T21:14:37.000Z'
originalURL: https://freecodecamp.org/news/collaborative-problem-solving-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/michal-czyz-ALM7RNZuDH8-unsplash.jpg
tags:
- name: Collaboration
  slug: collaboration
- name: interview questions
  slug: interview-questions
- name: Interview tips
  slug: interview-tips
- name: Python
  slug: python
seo_title: null
seo_desc: "By Alberto Gonzalez Rosales\nNo matter how experienced of a developer you\
  \ are, being interviewed for a new job is always stressful. This is certainly true\
  \ from my own experience. \nIn my case, I have been working professionally as a\
  \ Software Developer ..."
---

By Alberto Gonzalez Rosales

No matter how experienced of a developer you are, being interviewed for a new job is always stressful. This is certainly true from my own experience. 

In my case, I have been working professionally as a Software Developer for two and a half years, and I've had to face developer interviews five times already.

I have seen people focus too much on learning specific algorithmic problems, or training in online platforms specialized in interview challenges. But there is another side to interviews which I think is as important – and people pay less attention to it.

So, if you want to know how I think you should focus your training for interviews, grab a cup of coffee and get comfortable.

It's going to be a bit of a ride ride (but don't worry – Python examples included!).

## Here's what we'll cover:

1. [Do algorithms and data structures matter for interviews?](#heading-do-algorithms-and-data-structures-matter-for-interviews)
2. [Focus on a collaborative approach](#heading-focus-on-a-collaborative-approach)
3. [Try doing a mock interview](#heading-try-doing-a-mock-interview)  
– [The initial example interview problem](#heading-the-initial-example-interview-problem)  
– [The second example interview problem](#heading-the-second-example-interview-problem)  
– [The hardest example interview problem](#heading-the-hardest-example-interview-problem)
4. [Final words](#heading-final-words)

Let's dive in.

## **Do Algorithms and Data Structures Matter for Interviews?**

The short answer is **Yes**.

Knowing about Data Structures and Algorithms will often help you get a job. Also, the benefits of having a solid algorithmic background include the capacity to make better decisions when faced with a challenging problem.

In real life, algorithmic problems won't appear like the statements in the academic exercises you might study. Still, the more trained you are the most likely you are to be able to recognize an application of a Balanced Binary Tree or a Shortest Path algorithm in disguise.

With this in mind, I would recommend not training Data Structures and Algorithms solely for the interviews that you want to excel at. The design of algorithms and how to use the right data structures are topics beautiful enough to be studied just for the pleasure of knowing.

The scope of an interview is very limited. Instead, focus on the problem-solving part of the issue. Try to understand how to use an algorithm (or variations of it) for similar tasks. Study all the variants, and learn to recognize them in different situations. This will help you face new tasks with an open mind.

Also, don't memorize solutions. It won't take you anywhere. It is very easy for an experienced developer to ask the right questions that will put you on display if you only train for very specific topics.

Take a problem and try to solve it using different methods. Try to solve harder problems every time. Get out of your comfort zone.

It will pay off.

## **Focus on a Collaborative Approach**

Most people train for their interviews on websites like [Leetcode](https://leetcode.com/). There is no problem with that. These websites are good for training your problem-solving skills.

I have been participating in Competitive Programming contests for the last eight years at least, and I have always benefited from these online resources.

But there is one thing that's hard to understand for most software engineers wanting to perform well in an interview. They don't train for the most important aspect of software development: **Collaboration**.

Usually, when you are faced with a problem in an online platform, it comes with some constraints on the maximum values for some input. It also might have some time and memory limits that require you to adjust your solutions to be more or less efficient. But this is not how it will be in real life.

It is not obvious how to map these constraints to real-life scenarios. They usually come in the form of very specific requests from a client, or very specific characteristics of the team.

In a real project, the team will **collaborate** to determine what these constraints will be. You have to analyze your use cases, the time you have for the task, who is the final user, how many people will be working on it, and so on...

After a series of discussions, you will reach a consensus and finally start implementing a solution that suits your needs. And this solution doesn't even have to be the more efficient in some cases, but the fastest to implement, for example.

This is what interviewers want to see from candidates during the interviews as well.

You don't jump straight to implementing the best solution you know for the problem you are facing. Instead, you should use your interviewers as a valuable resource, treat them as if they were your teammates (in the end, you want them to be). Ask questions about how the team prefers the solution for the problem to be implemented.

This will lead to a very fruitful discussion where you can showcase your coding abilities and your collaborative skills. You could start proposing simple solutions and walk your interviewers through the process of how the solution can be improved using the best Aces up your sleeve.

As a final note on online training, I would recommend doing individual and team training. Use websites such as [Codeforces](https://codeforces.com/) or [AtCoder](https://atcoder.jp/), which have a huge set of interesting (and challenging) problems, and try to compete against yourself every day.

Don't focus on your rating. I have done that before, and it only holds you back.

## **Try Doing a Mock Interview**

If you reached this point in the article, I would like to propose a little exercise. Let's have a mock interview where I will act as the interviewer. I will tell you how I think the candidate (you) should answer every question and perform each task.

Of course, we will focus only on the programming challenge part. Other aspects of interviews, such as talking about previous experiences, are also important, but we will try to cover that in another article.

So, if you feel ready enough, let's go!

### The Initial Example Interview Problem

Let's start with the task that you will be solving. Keep in mind that if you and I are ever in this situation, I won't be using this same example, but of course, I will be using the same methodology 😉.

The statement of the problem is the following:

> "Given an integer number `X`, find out if it is a prime number."

You might be tempted to go for the best solution you know to solve this problem. I think that this approach, as I explained before, isn't always correct.

Instead, what I would like to know are the different approaches to solving this problem. Also, I would like you to ask about the requirements for this task. Something like:

* Should we aim for performance or to solve it faster?
* Should we make a solution that is easy to understand for other developers?

Usually, some aspects to consider when creating the first solution for a problem are:

* Easy vs Hard: Should we make an easy-to-implement solution even if it is not perfect, or should we go for a more robust solution that will be difficult to implement?
* Naïve vs Efficient: Should we deliver a working, naïve solution first and then a more efficient one, or should we go straight to efficient?

Evaluate what your team wants to optimize for. Reach a consensus, and implement the agreed solution.

In my case, I would be glad if you proposed the easiest, fastest-to-implement, correct solution that you can think of and then guide me through the process of how to improve that solution. 

An example of a very good initial solution to this problem is something like the following:

```python
# naive.py

def is_prime(x: int) -> bool:
    if x in [0, 1]:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

```

As you can see, this function is correct. Since a prime number is an integer only divisible by the number `1` and itself, it makes sense to iterate from `2` to `x - 1` looking for a divisor of `x`. If we find one, we can immediately return `False`. Otherwise, we return `True`. As edge cases, the numbers `0` and `1` are not prime by definition.

This is a good starting point!

Now, before diving into optimizing this method, you can discuss the style of the code. Is it Pythonic enough? Do we care about it? Is it readable?

All these questions might not seem important at first but, since we work as a team, they do matter. Having a coding style is important because it makes it easier for every team member to understand each other's code, and it will speed up reviews and refactoring. Also, the code is more often read than written, so readability counts!

You might be tempted to show off your Python skills and rewrite the previous function as follows:

```python
# pythonic_naive.py

def is_prime(x: int) -> bool:
    return False if x in {0, 1} else all(x % i != 0 for i in range(2, x))

```

I think this is a good, pythonic way to write this function. But, since the team is the most important thing here, this change should be discussed.

It might be the case that some team members are not so skilled in Python. Maybe, in this case, we should optimize for readability instead and keep the function as we first wrote it.

A more interesting addition, before getting into performance, would be adding docstrings to the function. As I said before, this code is most likely to be read by your team members in the future. It is important, then, to make it easier for them (and your future self) to understand what this function is doing.

Maybe changing the function to something like the following will add more value:

```python
# naive.py

def is_prime(x: int) -> bool:
    """This function takes an integer `x` as
    argument and checks whether is prime or not.

    Args:
        x (int): The integer number to test for primality.

    Returns:
        bool: True if the number `x` is prime, False otherwise.
    """
    if x in [0, 1]:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

```

#### First Optimization

Until this point, we have an initial solution that works. We have discussed important topics such as code styling, readability, and documentation for developers. These are all important things to consider when working as a team.

But we still haven't talked about the performance of the solution! So, it's probably time for that.

At this moment, you should probably bring up that this function can be implemented so it runs much faster. And now is when you showcase all that algorithmic knowledge inside you.

The previous solution has a time complexity of `O(x)`, where `x` is the input integer the function takes as an argument. This can be optimized to `O(sqrt(x))` with the following code:

```python
# sqrt.py

import math

def is_prime(x: int) -> bool:
    if x in [0, 1]:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

```

Or even like this, without importing the `math` library:

```python
# sqrt.py

def is_prime(x: int) -> bool:
    if x in [0, 1]:
        return False
    i = 2
    while i**2 <= x:
        if x % i == 0:
            return False
        i += 1
    return True

```

I would be ok with either alternative.

I omitted the docstrings in the previous implementation for the sake of making the actual code changes clearer. But, it would be great to include the time complexity of the function in the documentation for developers. The more information you can give about your code, the better it will be for your team members and yourself.

You are doing great so far. Let's continue!

### The Second Example Interview Problem

So far, I have been able to evaluate that you have the necessary collaborative skills to take on easy tasks with the team. Now it's time to complicate things a little.

This is the statement of the second problem I would propose:

> "Given two integer numbers `L` and `R`, count how many prime integers are in the interval `[L, R]`."

Once again, I would recommend discussing what priorities the team has set regarding this task. Start simple and walk through the process of improving an initial solution. Emphasize that premature optimization is not a good practice.

Also, discuss the possibility of using the solution that you implemented for the previous task to solve this one. It makes sense that if we have a function that tells whether an integer is a prime number or not we can use it for every number in a range.

And this is something that you will have to do in real life. Usually, when a new task shows up, the team should look into the maintained projects to see what can be reused to speed up the implementation process. If you don't do this, you might end up coding duplicated functionalities.

That being said, a good initial solution for this task could be something like this:

```python
# range_primes.py

from sqrt import is_prime

def count_primes(l: int, r: int) -> int:
    primes = 0
    for i in range(l, r + 1):
        if is_prime(i):
            primes += 1
    return primes

```

This is perfectly fine, and you have shown that you can reuse previous functionality to build new ones. As in the first example, you might be tempted to show off your Python skills and write this function like this:

```python
# range_primes.py

from sqrt import is_prime

def count_primes(l: int, r: int) -> int:
    return sum(bool(is_prime(i)) for i in range(l, r + 1))

```

I recommend not going for this Pythonic implementation as your first option. Leave it for discussion, evaluate the readability of the code, and maybe analyze the differences in performance. Don't forget the docstrings!

The next section is when things get interesting. Keep reading. We are on the final step...

### The Hardest Example Interview Problem

Remember when I said previously that the constraints present in competitive programming websites are hard to map to real-life requirements?

Here is how I would present a difficult challenge for you to determine those constraints and implement the best solution that you can:

> "Suppose a client wants us to provide the functionality of calculating prime numbers in a range as a service. They want the focus to be on performance because they plan to use this service very often. How would you implement it?"

If you have been practicing your algorithmic skills for interviews, you have probably solved problems similar to this one a few times. The main difference here is the change in context.

Instead of giving you precise instructions, numeric constraints, and input or output formats, I gave you a broader description of the task. And my goal here is the same as before: get you to interact with me as if we were teammates figuring out how to solve this problem from the little information we know.

Hopefully, after exchanging a few questions and answers, we can translate the previous, more ambiguous statement into something much more familiar:

> "Given a set of queries of the form `[L, R]`, answer, for each query, how many integer numbers inside that range are prime."

And this makes sense because the client wanted to use this service very often, as stated in the description.

We want to focus on performance. That should be our main concern when implementing the solution. But still, the best way to get to an optimal solution is to start with a simple one, analyze if we meet our performance requirements, and keep improving gradually. Let's see the entire example.

We could start by using the solution we implemented in the previous step. Is it good enough?

Let's assume that the maximum range of numbers we will have as an argument to our function is `[1, 10^6]`. Also, realistically, let's assume that the number of queries our service will answer per minute is around `10^5`.

Our previous solution has a time complexity of `O(sqrt(n))` to determine if a number is a prime. If we were to do that for every number in the range, the complexity goes up to `O(n * sqrt(n))`. On top of that, if we do that for every query, we will end up with an even higher time complexity of `O(q * n * sqrt(n))`.

Substitute the previous variables with the highest possible values they can have, and you will get that this solution will take around `10^14` operations to answer all the queries. Assuming that a computer can perform around `10^8` elementary operations per second, it will take approximately `10^6` seconds to complete all of them.

> Note: Convert 10^6 seconds to days. You will be amazed 🤯.

This solution is unfeasible if the goal is to prioritize the performance of our solution. Let's see how we can improve it.

At this point, what I would expect is for you to take out the best of the training that you've had on all those online platforms, and show me an impressive solution. This is the time to showcase all your analytical and algorithmic skills.

But only now, because I know that you are a team player.

#### The Final Solution

Since this is a mock interview, I am very interested in knowing your approach to solving this last problem efficiently. Let me know how you would implement the solution or share your code on GitHub – don't be shy.

I guarantee you one thing: if you can make it to this point in real interviews, probably it won't matter too much if you don't know the optimal solution to this problem. It doesn't mean that you shouldn't try your best to solve it, but rest assured that you have done a very good job already.

That's it! Now I want to see your code.

## **Final Words**

In this article, I tried to summarize some of the aspects I consider to be the most important in coding interviews. I placed special emphasis on the collaborative part because I think most people underestimate how important this skill is. It is a must, especially if you want to work on a team with other developers.

I tried to guide you through a mock interview where I explained the thought process I would follow when faced with a standard coding task in an interview. I hope this exercise was useful and that it can help you in your next interview (as a candidate or as an interviewer).

Share your thoughts on this mock interview, and let's start a fruitful discussion.

See you soon! 👋

## **Sources**

* Code examples used in the article can be found [here](https://github.com/albexl/a-problem-solving-oriented-approach).
* Hint for the last problem: implementation of the [Sieve of Eratosthenes](https://github.com/albexl/data-structures-for-teaching/blob/dev/algorithms/number_theory/eratosthenes_sieve.py) algorithm.

👋 Hello, I'm Alberto, Software Developer at [doWhile](https://dowhile.se/), Competitive Programmer, Teacher, and Fitness Enthusiast.

🧡 If you liked this article, consider sharing it.

🔗 [All links](https://bio.link/albexl) | [Twitter](https://twitter.com/albe_xl) | [LinkedIn](https://www.linkedin.com/in/albexl/)


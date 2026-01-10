---
title: Common Logic Puzzles – The Knights and Knaves, Monty Hall, and Dining Philosophers
  Problems Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/common-logic-puzzles-the-knights-and-knaves-monty-hall-and-dining-philosophers-problems-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d11740569d1a4ca35b6.jpg
tags:
- name: logic
  slug: logic
- name: puzzles
  slug: puzzles
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'While not strictly related to programming, logic puzzles are a good warm
  up to your next coding session. You may encounter a logic puzzle in your next technical
  interview as a way to judge your problem solving skills, so it''s worth being prepared.

  In...'
---

While not strictly related to programming, logic puzzles are a good warm up to your next coding session. You may encounter a logic puzzle in your next technical interview as a way to judge your problem solving skills, so it's worth being prepared.

In this article, we've collected a few famous logic puzzles and their solutions. Can you solve them without peeking at the answer?

## Knights and Knaves

For this logic puzzle, imagine there are two types of people, knights and knaves. Knights only tell the truth, while Knaves only tell lies.

There are many variations of this puzzle, but most involve asking a question to figure out who is the knight and who is the knave.

### Red and Blue

There are two people standing in front of you, Red and Blue. Blue says, "We are both knaves." Who is really the knight and who is the knave?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/photo-1556549957-f41c6fcc4210-4.jpeg)

**Solution**  
It's impossible for Blue to be the knight. If Blue was a knight, the statement, "We are both knaves," would actually be a lie. Therefore, Blue is a knave as his statement is a lie, and Red must be a knight.

### Two Paths

You arrive at a fork in the road and need to choose the correct path that leads to your destination. There are two people standing at the fork, and you know that one must be a knight and the other must be a knave. 

What single question could you ask to one of the people to determine the correct path, A or B?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/photo-1519401706-5cf17f6e70de.jpeg)

**Solution**  
The question you can ask either person is, "What path would the other person tell me is the correct one?" The answer will always be the wrong path to take, and you can safely take the other path.  
  
Imagine the correct path is A.   
  
If you ask directly, "Which is the correct path?" the knave will say B is correct while the knight will say A.  
  
However, when asked which path the _other_ person would say is correct, the knave will lie and say that the knight would tell you path B is correct. Meanwhile, the knight will tell the truth about the knave's answer, and say that the knave will tell you that path B is the correct one.  
  
In both cases  you know that then answer, path B, is actually a lie, so you should take the other path.

## The Monty Hall Problem

The Monty Hall Problem is a riddle on probability named after the host of the 70’s game show it’s based on, _Let’s Make a Deal_. This particular problem is a [veridical paradox](https://en.wikipedia.org/wiki/Paradox), which means that there is a solution that seems counter-intuitive, yet proven to be true.

Imagine you are on a game show and there are 3 doors, each with a different prize behind them. Behind one of the three doors is a car. Behind the other two doors there are goats. 

You must choose one of the 3 doors to select as your prize. 

Say you decide to open Door 1. The host, who knows where the car is, opens a different door, Door 2, which reveals a goat. He then asks if you would like to open Door 3 instead.

Should you choose Door 3 over your original choice? Does it even matter?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/zachary-anderson-ceYJ1HKt9Rk-unsplash.jpg)

**Solution**  
It turns out that your choice really does matter, and it is actually to your benefit to choose Door 3 instead of Door 1. Here's why.

When you chose Door 1 from the 3 closed doors, you had a 1 out of 3 chance that you picked the right one. Both Door 2 and Door 3 also have a 1 out of the 3 chance of having a car behind it. 

Another way to think about it is that Doors 2 and 3 have a 2 out of 3 chance of having a car behind it _combined_.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/8EsVvZk-1.png)

But when the host opens Door 2 and reveals the goat, you suddenly have more information about the problem.

Remember that Doors 2 and 3 have a combined probability hiding the car 2/3rds of the time. When Door 2 was opened you know that there was no car behind it.

But this reveal does not change the combined probability of the two doors. That’s the key takeaway here!

![Image](https://www.freecodecamp.org/news/content/images/2020/04/V2JzAka-1.png)

Since you know that Door 2 has a 0/3 chance of hiding the car, you can now say that there's a 2/3 chance that the car is behind Door 3. Door 1 remains unchanged – there's only a 1/3 the car is behind it.

So if you decide to switch, you go from roughly a 33.33% chance to a 66.67% chance of finding the car. In other words, you are doubling your chances of success by opening Door 3 instead!

Yes, it is possible that Door 1 was hiding all along and host tricked you. That doesn’t matter. You are gambling by taking the deal, but you’re gambling smart. You should make the best decision with the information you’re given and let the dice roll. 

In the long run, you'd perform better by switching than a contestant who decides to go with their first choice. Though it's not immediately obvious, the host is actually doing you a favor by offering you a better deal.

## **The Dining Philosophers Problem**

The dining philosophers problem is a classic example in computer science to illustrate issues with synchronization. It was originally created by Edsger Dijkstra in 1965, who presented it to his students as a handful of computers competing for access to shared tape drives.

Imagine five silent philosophers sitting around a table, each with a bowl of spaghetti. There are forks on the table between each pair of adjacent philosophers.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/at_the_table.png)
_Image courtesy of [adit.io](http://adit.io/posts/2013-05-11-The-Dining-Philosophers-Problem-With-Ron-Swanson.html)._

Each philosopher can only do one thing at a time: think and eat. However, a philosopher can only eat spaghetti when they have both the left and right forks. A fork can only be held by one philosopher at a time.

After a philosopher finishes eating, they need to put down both the left and right forks so they're available to the others. A philosopher can take a fork as soon as it's available, but can only start eating once they have both forks.

The philosophers are famous for their appetites – they can all eat endlessly and never get full. On top of that, the bowls of spaghetti magically replenish no matter how much is eaten.

The problem is, how can can you ensure that no philosopher will starve, and that they can continue eating and thinking forever?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mae-mu-Pvclb-iHHYY-unsplash.jpg)

### Synchronization and Deadlock

In simple terms, the dining philosophers problem is an illustration of how synchronized access to a shared resource can result in creation of a deadlock situation.

**Synchronization** is used to control concurrent access to a shared resource. This is necessary in any situation where multiple independent actors may be competing for the use of one resource like the forks. Since there is only one resource available, we use synchronization to prevent confusion and chaos.

A **Deadlock** is a system state where no progress is possible. This situation can occur when synchronization is enforced, and many processes end up waiting for a shared resource which is being held by some other process. Like with the philosophers who are either stuck eating or thinking, the processes just keep waiting and execute no further.

### Solutions

At first glance it appears like it would not be possible for a deadlock where all philosophers are stuck either eating or thinking. For example, pattern for each philosopher to follow might be:

> 1: think until the left fork is available; when it is, pick it up;  
>   
> 2: think until the right fork is available; when it is, pick it up;  
>   
> 3: when both forks are held, eat for a fixed amount of time;  
>   
> 4: then, put the right fork down;  
>   
> 5: then, put the left fork down;  
>   
> 6: repeat from the beginning.  
>   
> Source: [Wikipedia](https://en.wikipedia.org/wiki/Dining_philosophers_problem)

There are many solutions possible to prevent deadlock. If we look closely, one problem in the algorithm above is that all philosophers have equal chance (have the same priority) of acquiring one fork. This prevents anyone from acquiring two forks and the whole system grinds to a halt.

Here are some possible solutions:

1. **Priority**: Some philosophers are assigned higher priority, so that the chance of acquiring both forks is increased.
2. **Preemption** (Politeness): Philosophers relinquish the acquired fork without eating, in case the other fork is not available.
3. **Arbitration**: A mediator allocates forks ensuring that two forks are given to one person, instead of one to many.

Now that you know how to solve these logic puzzles, treat yourself to an endless bowl of spaghetti. You earned it.


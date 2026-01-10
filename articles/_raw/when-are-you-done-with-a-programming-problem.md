---
title: How to Know When You've Learned Everything You Can From a Programming Problem
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-22T20:30:26.000Z'
originalURL: https://freecodecamp.org/news/when-are-you-done-with-a-programming-problem
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/ashkan-forouzani-m0l9NBCivuk-unsplash-1.jpg
tags:
- name: productivy
  slug: productivy
- name: learn to code
  slug: learn-to-code
- name: learning
  slug: learning
- name: Problem Solving
  slug: problem-solving
- name: General Programming
  slug: programming
seo_title: null
seo_desc: "By Amy Haddad\nThe answer may seem obvious: you’re done with a problem\
  \ once you’ve solved it. \nThat’s how I approached problem-solving when I began\
  \ learning to code. I was on a problem-solving treadmill: solving as many problems\
  \ as quickly as possible..."
---

By Amy Haddad

The answer may seem obvious: you’re done with a problem once you’ve solved it. 

That’s how I approached problem-solving when I began learning to code. I was on a problem-solving treadmill: solving as many [problems](https://www.freecodecamp.org/news/do-you-solve-programming-problems-or-complete-exercises-the-difference-matters/) as quickly as possible.

And why not? There’s no shortage of problems to solve. Besides, don’t you get better by solving more problems? More to the point: what else can you do once you have the answer? As it turns out, quite a bit. The fallacy of my approach soon surfaced. 

Although I solved the problem, I didn’t learn much from it. That’s because a few days or weeks later when I tried to re-solve the problem or when I came across a related one, I got really [stuck](https://www.freecodecamp.org/news/how-to-get-unstuck/). Mistakes were made. Concepts were confused. Progress was stalled. 

I now realize that getting the solution is only part of the problem-solving process. Then, in the words of a mathematician named George Pólya, it’s time to “look back.”

## Looking Back

Pólya writes about the problem-solving process in his book, _How to Solve It_, through the lens of mathematical problem-solving. But his ideas are applicable to programming. What’s particularly interesting to me is his fourth phase: looking back.

“By looking back at the completed solution, by reconsidering and reexamining the result and the path that led to it, [students] could consolidate their knowledge and develop their ability to solve problems,” Pólya writes.

In some ways, solving a problem is like creating a piece of art. There’s always something more we could do. “We could improve any solution, and, in any case, we can always improve our understanding of the solution,” explains Pólya.

For me, “looking back” is a practice of self-improvement and [learning](https://amymhaddad.com/four-ways-to-learn-programming-topics). The aim is to:

* Learn from my successes: understand what you wrote and why.
* Solidify my learning of new concepts.
* See patterns and understand the context for using a particular data structure or algorithm. 

Consider a basketball player who takes 1,000 shots each day. That sounds admirable. But as he rushes to get the 1,000 shots in, his form gets sloppy. He uses the wrong technique. 

He’d benefit more from taking a few hundred shots, then evaluating his performance: watching a video recording of his form, seeing the flaws, and correcting them. Then, he'd hit the court again. 

Now he’ll be more informed, since he looked back and evaluated his performance. He’ll practice better.

The same is true with solving problems. The idea isn’t to check a box so you can claim you solved “x” number of problems. Instead it’s doing your best work each time and learning as much as possible along the way. 

There are three reasons why looking back matters.

### Reason #1: See the Patterns and Understand the Context

You’ll see similar patterns over and over again in the problems you solve. 

Understand how to use a particular algorithm, like binary search. Train your eye so you know _when_ and _how_ to apply it. So when you encounter a related problem in the future, you’ll be ready. Doing so will save time (and frustration) in the long run.

### Reason #2: Solidify Your Learning

Say you used something that’s new to you to solve a problem, like a stack or queue. 

Do you really know how to use it again? Do you feel comfortable using a stack in a related problem? Take the time to understand anything new you used so you can use it again in the future.

### Reason #3: Learn from Your Successes

Mathematician Richard Hamming gets to the heart of the matter with this quote from his book, _The Art of Doing Science and Engineering._

“I regard the study of successes as being basically more important than the study of failures...there are so many ways of being wrong and so few of being right, studying successes is more efficient.”

As programmers, we deal with our fair share of errors. And then (many tries later) we run the program and it works. Now is a great time to put Hamming’s words to practice and study your success. 

Do you understand _how_ your program works? Do you understand _what_ you wrote and _why_ you wrote it? 

By looking back⁠—when the information is still fresh in your mind⁠—you’re preparing your future self. It’ll help you bridge your understanding and solidify your mental models. It’ll help you improve and prevent repeating the same mistakes over again. In short, it’ll help you get better.

## Four Ways to Look Back

There are a few ways that I “look back” at problems. Give them a try.

### Teach Yourself

A fantastic way to help solidify your mental models is to teach yourself. After you complete a program or problem, go through your code and explain it line by line. It’s one of the best ways of “looking back” when you’re learning something new.

I’ve found this process invaluable while learning web development. After I complete a project, I copy my code into a Google Doc. Starting at the top, I make comments throughout to teach myself about important concepts.

Here’s an example of some code and some of the comments I wrote.

```JS
export default function ManageTeamMembersPage(props) {
 
    const [teammate, setTeammate] = useState({
       name:"",
       email: "",
       role: "",
   })
   
   ...
   
```

* Use props to access data passed down from the parent component.
* Add state hook. The hook takes a default, which is an object that contains everything I need for the form: name, email, role.

This method of “looking back” is about understanding. In this example, I was learning about state, props, and forms in React. 

Writing out comments to explain your code will help you solidify concepts in your mind. If you can’t type a short explanation of it on the spot, then revisit the topic. 

This method is equally useful for future problems and projects. I regularly pull up old problems and programs I’ve notated. I use them as a reference when writing related programs or solving related problems. Doing so reinforces key ideas, and to Hamming’s point, it helps me remember my successes: what to keep doing.

### Study Solutions of Great Programmers

It’s not only useful to study your own code, but also the code of others who have solved the same problem. There are a lot of [great programmers](https://amymhaddad.com/2-traits-of-great-programmers) out there and we can learn from them.

After I solve a problem, I apply [a learning technique that Ben Franklin used](https://amymhaddad.com/how-ben-franklin-can-help-you-become-a-better-programmer.mdx) to become a better writer. His process involved trying to reproduce an article from a publication he admired after he’d forgotten the details of it. 

I follow a similar process to become a better programmer.

Here’s how it works:

* **Solve a problem**.
* **Find a programmer who’s better than you and who’s solved the same problem.**
* **Study their solution**: read each line of code and type a comment in your editor to explain it.
* **Re-solve the program** after some time has passed. Use the comments you typed out as hints to guide you along the way.
* **Compare your program** to the one you studied.

To be clear, this practice isn’t about memorizing or copying someone else’s code—far from it. Rather, it’s about learning: get practice [reading](https://amymhaddad.com/why-reading-code-matters) code; see another way to solve the same problem; experiment with new parts of a language; and get practice teaching yourself. It’s also about applying what you’ve learned by putting it into your own style.

### Add a Constraint

See how different techniques apply to the same problem when you add a constraint. For example, you solved the problem using a hash table. Now try solving it using an array.

The idea is to gain another perspective, and adding a constraint can do just that. It’ll get you out of your comfort zone, forcing you to think creatively. 

As a result, you may find a slicker approach and cut the length of your program in half. Or may realize what data structure _not_ to use, which is equally important. 

Here’s the point: you’ll have another approach at your ready when you’re faced with a related problem in the future.

### Solve a Related Problem

The programming website LeetCode is great for many reasons. One is providing similar questions for problems that you solve.

In one problem on LeetCode you are given an array of integers and a target number. The aim is to find two numbers that add up to the target and return their indices. 

You solve the problem. 

Now solve a related one, which LeetCode provides. This time you’re given an array of integers that’s sorted in ascending order, along with a few additional constraints to differentiate this problem from the previous one.

Solving a related problem is a great way to get practice using a similar technique, data structure, or algorithm in a different context.

Looking back focuses on the _process_, instead of the end result. And revisiting the process matters. It’s getting out of your comfort zone, trying something new whether that’s a data structure or algorithm. It’s realizing there are different ways to solve the same problem. It’s understanding how to write better code. It’s about learning.  

Yes, it takes some time to look back. But it’s time well spent: it’s how we get better.

_I write about the programming skills you need to master and the concepts you need to learn, and the best ways to learn them (_[amymhaddad.com](https://amymhaddad.com/)).


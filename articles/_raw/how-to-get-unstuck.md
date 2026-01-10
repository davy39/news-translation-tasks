---
title: How to Get Unstuck When You Hit a Programming Wall
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-14T15:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-unstuck
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/get_unstuck-1.jpg
tags:
- name: Problem Solving
  slug: problem-solving
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Amy Haddad

  Getting stuck is part of being a programmer, no matter the level. The so-called
  “easy” problem is actually pretty hard. You’re not exactly sure how to move forward.
  What you thought would work doesn’t.

  The other part of being a programm...'
---

By Amy Haddad

Getting stuck is part of being a programmer, no matter the level. The so-called “easy” problem is actually pretty hard. You’re not exactly sure how to move forward. What you thought would work doesn’t.

The other part of being a programmer is getting yourself unstuck. 

I’ve been getting stuck a lot recently, so finding ways to get _unstuck_ has been ever-present on my mind. Here are a few tactics I’ve been using. Maybe they can help you, too.

## Make the problem concrete 

Create a diagram, make a quick sketch, or use actual objects to give yourself a visual. It’ll make the problem a lot easier to think about.

One problem I faced asked me to find the absolute difference between the sums of a square matrix’s diagonals. That’s a mouthful and a lot to keep in my head. So I drew it out: I created a square matrix of numbers and circled the diagonals.  

![Image](https://www.freecodecamp.org/news/content/images/2020/01/2020-01-15-12.58.06.jpeg)

A simple sketch literally made the steps jump out at me: sum one diagonal (which is 15), then the other (which is 17), and then find the absolute difference between them (which is 2).

This approach applies to other problems, too. When I was learning about for loops, I iterated through a pile of almonds. When I’m working on a recursive problem, I’ll make a diagram to see what’s happening on the call stack until I hit my base case. 

The commonality is this: make the abstract concrete.

## Write out exactly what you’re trying to do

Write down the specific step you’re working on when you feel the all-too-familiar “spinning your wheels” cycle come upon you.  

The five or ten seconds it takes to jot down a few words on a piece of paper will help you solidify your thought process and redirect your attention.

Here are some examples:

* Store the course names as keys in the object
* Pass the argument to the callback function
* Reset the “maxValue” variable to 0

Resetting the “maxValue” variable, for example, didn’t solve the problem. But it was an important step in the process. Writing this short phrase got me back on track: it was a reminder of what I’d set out to do. It also ensured I was focused on one thing, not many.

So the next time you find yourself trying the same approach over and over again and getting the same result, stop yourself and ask: “What exactly am I trying to do here?” 

Then, write—yes, write—your answer down on a piece of paper.

It’s not enough to think of your response. If I casually “think” to myself, I’ll rush the process and not much (if anything) is gained. I’ve got to write it down. 

## Simplify your given input

It’s far less intimidating to work with a few things than many. That's why it's helpful to simplify your given input.

One problem gave me a list of three dictionaries. It was _only_ three dictionaries, but that was still two too many. 

```
names = [
    {'first':'John', 'last':'Smith', 'email':'johns@example.com'},
    {'first':'Mary', 'last':'McDonald', 'email':'marym@example.com'},
    {'first':'Sam', 'last':'Davey', 'email':'samd@example.com'}
]
 ```


My job was to sort each dictionary by last name, then by first name (ie, Davey, Sam: samd@example.com). However, the problem was easier to think about when I made the list of three dictionaries a list of one.  

``` 
name = [
    {'first':'John', 'last':'Smith', 'email':'johns@example.com'}
]
```

I solved the problem using a single dictionary. Then, I applied the same logic to the larger problem at hand. 

When you simplify your given input, you make the problem much more manageable.

## Solve a smaller problem

Spot patterns more easily and understand what you're _really_ asked to do when you solve a smaller version of the problem.

Here’s an example problem from Reuven Lerner’s book, _Python Workout_:

“Use a list comprehension to reverse the word order of lines in a text file. That is, if the first line is abc def and the second line is ghi jkl, then you should return the list ['def abc', 'jkl ghi'].”

When solving a smaller version of a problem, I find it helpful to remove layers of complexity and use my ideal data structure. In this example, that meant ignoring the text file and list comprehension (layers of complexity) and using a list (my ideal data structure).

Then I solved the problem. I opened up my editor and typed out my ideal data structure.

```
letters = ['abc def', 'ghi jkl']
```

I reversed the order and got the expected result using a for loop.

```
reversed_letters = []
for letter in letters:
   letter_list = letter.split(" ")
   letter_list.reverse()
   reversed_letters.append(" ".join(letter_list))
```

Once I got that working, I added the layers of complexity back in one at a time until I solved the problem as the problem statement asked.

Solving a smaller version of the problem helps get you to the heart of what you need to do. It's also another way to make the complex simple.

## Take a break 

Your brain doesn’t stop thinking just because your fingers stop typing. 

Has an idea ever “popped” into your head while you were doing something other than programming? Have you ever returned to a problem after a workout and the solution is staring you in the face? It’s happened to me.

It’s no coincidence that you arrived at your idea or solution when you were doing something else—when you weren’t deliberately working. “Epiphanies may seem to come out of nowhere,” explains [Scientific American](https://www.scientificamerican.com/article/mental-downtime/), “but they are often the product of unconscious mental activity during downtime.” 

If you feel like you’re running up against a brick wall, you very well could be. It may be best to take a break. Give your mind some time to digest what you’re working on and return to the problem renewed.

## Pair with another programmer

Working with someone else can be a great way to generate ideas and see a problem from another perspective. But I highly recommend you do everything in your power to get yourself unstuck first.

There will always be roadblocks. Learning how to troubleshoot your own problems is a critical skill to learn. It’s easy to say “I don’t get it. Let me ask this senior engineer.” Then, have the senior engineer solve the problem for you. It’s harder to figure it out yourself, but you need to at least try.

If you’ve sincerely put your best foot forward, then reach out to a programmer with a specific question. This shows respect for the other programmer’s time and it’ll make your pairing session more effective. 

Then, ask for a hint—don’t have the programmer solve the problem for you. You’ll undoubtedly encounter a similar situation down the road, so use the pairing session as a learning opportunity. It’ll help you in the long run.

## Wrapping up

Getting stuck is frustrating, to be sure. You may try just one of the above tactics and have a “light bulb” moment, or you may need to try a combination and find yourself simply inching along during the process. 

But there are two things I’ve learned from embracing the struggle: I’m learning a lot and the breakthrough is coming. Keep at it.

_I write about learning to program, and the best ways to go about it_ ([amymhaddad.com](https://amymhaddad.com/)).



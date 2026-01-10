---
title: How to Solve Einstein's Five House Riddle
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-09-08T15:36:22.000Z'
originalURL: https://freecodecamp.org/news/einsteins-riddle
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Capture.JPG
tags:
- name: logic
  slug: logic
- name: puzzles
  slug: puzzles
seo_title: null
seo_desc: 'I recently learned about a logic puzzle online that apparently only 2%
  of people can solve.

  There are a few different incarnations of it – some have slightly different wording,
  different names, or change the items in the riddle slightly. But they are...'
---

I recently learned about a logic puzzle online that apparently only 2% of people can solve.

There are a few different incarnations of it – some have slightly different wording, different names, or change the items in the riddle slightly. But they are all the exact same core problem.

The riddle itself is used as a benchmark in the evaluation of [constraint satisfaction problems](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem) for computer algorithms.

## What is the Einstein Riddle?

Even the origin of it the riddle is a little unclear. It's famously known as the **Einstein Riddle** because it was supposedly created by Einstein as a young man for fun. Others say it was used by Einstein to only select the smartest PhD students he would supervise. 

But there are some claims online that it actually was invented by the author of _Alice's Adventures in Wonderland_, [Lewis Carrol](https://en.wikipedia.org/wiki/Lewis_Carroll).

It's highly unlikely that it was written by Einstein, but that doesn't really matter. What's important is that, with a basic understanding of truth tables (and a bit of patience), you can solve it, too.

## How to Solve Einstein's Riddle

I'm now going to give you a list of clues, and then you will need to answer a question at the end of the clues.

Just to be absolutely clear, all the clues are enough for you to solve it. You don't need any extra hints, and there aren't any assumptions I expect you to know.

> There are 5 houses painted five different colors.  
> In each house lives a person with a different nationality.  
> These five owners drink a certain type of beverage, smoke a certain brand of cigar, and keep a certain pet.  
> No owners have the same pet, smoke the same brand of cigar, or drink the same beverage.

* The Brit lives in the red house
* The Swede keeps dogs as pets
* The Dane drinks tea
* The green house is on the left of the white house
* The person who smokes Pall Malls rears birds
* The owner of the yellow house smokes Dunhill
* The green house’s owner drinks coffee
* The man living in the center house drinks milk
* The Norwegian lives in the first (leftmost) house
* The man who smokes Blends lives next to the one who keeps cats
* The man who keeps horses lives next to the man who smokes Dunhill
* The owner who smokes BlueMaster drinks beer
* The German smokes Princes
* The Norwegian lives next to the blue house
* The man who smokes Blends has a neighbor who drinks water

Now to solve, **tell me who owns the fish**?

I solved it, but it did take me a couple attempts and a bit of scribbling on paper.

## How I Approached the Problem

To solve the problem, the first thing I did was to try and group together the clues. There are two references to the green house in the clues, so I tried to "solve" and consider those two clues together when I was able to.  
  
I then also filled out the center house's beverage as one clue immediately tells you, and I was also able to immediately fill out the leftmost house's nationality.

I essentially drew a really basic grid and eliminated and filled in possibilities based initially just on the clues. Then as I filled in more, I was able to fill in more details on other houses.  
  
I don't want to keep going with the hints if you want to solve this for yourself, but that's a starting point.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-29.png)
_A screenshot of part of a 5x5 table with every different possibility of Nationality, Color, Beverage, Pet and Smoking Cigar that can be removed on click._

To try and make it easier for anyone who wants to solve it or check their answer, I have made a basic site you can find here: [http://einsteins-riddle.com/](http://einsteins-riddle.com/) – the screenshot from above is a part of the grid on the site.

On that site, you'll find a table with all the options laid out as clickable buttons. The grid is initially filled out with all the possibilities, and as you learn more you can remove possibilities until eventually there is only one option left. 

At the bottom is a "Check Answer" button that will evaluate what you have left on your grid.

Try and solve it and see how you get on! If you prefer to do it via paper please do so.

I wish you luck 😊

If it stumps you, and you want to know how to solve it, you can find the solution [here](https://udel.edu/~os/riddle-solution.html).

## Why are Truth Tables Helpful?

I enjoy trying to work through these truth table problems, as it helps improve my clarity of thought. 

Sometimes when I'm coding and need to carefully consider some complex Boolean states in my code (not **this**, and not **that OR this** and **that** (and not **those**)) I think that these puzzles help me reason more clearly to simplify my code.

They also help me technically plan out my approach to a problem, from the very beginning to the eventual solution. 

I start from a basic set of requirements and no idea how all they fit together. But as I move along, I can go through a process of fact finding, checking edge cases, verifying/testing my logic against the requirements and finally submitting my work. All of these steps translate exactly to software development.  
  
Whenever you have a complicated set of states you are confused by, draw a basic truth table. Or however you want to represent the problem. Breaking it down into smaller and smaller problems will allow you to solve almost anything.

## **Conclusion**

I hope this has been an enjoyable brain teaser, and that you solved as much or as little as was fun for you.

I share my writing on [Twitter](https://twitter.com/kealanparr) if you enjoyed this article and want to see more.


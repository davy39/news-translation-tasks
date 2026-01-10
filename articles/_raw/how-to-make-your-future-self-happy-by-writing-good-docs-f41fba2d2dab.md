---
title: How to make your future self happy by writing good docs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-18T17:04:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-future-self-happy-by-writing-good-docs-f41fba2d2dab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bJKzkdJMBUhmDAnhwmpNsQ.jpeg
tags:
- name: docs
  slug: docs
- name: engineering
  slug: engineering
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Gabriele Cimato

  Or how to be less miserable when dusting off an old code base


  This is a little overview of common problems faced when working on a new or old
  project. Sometimes making a little effort up front can save you time and energy
  down the...'
---

By Gabriele Cimato

#### Or how to be less miserable when dusting off an old code base

![Image](https://cdn-media-1.freecodecamp.org/images/RH-mg3pmhVjtkFBzYfiWrfexlQZjf5KnUshr)

This is a little overview of common problems faced when working on a new or old project. Sometimes making a little effort up front can save you time and energy down the line. Writing good docs is like getting ready for your future self to high-five you ✋! We’ll see a silly example and a few recommended practices to get started with a good `README.md`.

### The Struggle

I’m almost certain that in your career, or in your everyday life, you faced a situation before that makes you think:

> “This problem looks familiar, I’m pretty sure I solved it before. If only I could remember how I did it!”

Especially coming from an engineering perspective this happens quite a lot. Repeated patterns, functions or bugs we’ve met before that require us to go through the exact same past effort to overcome an issue. Sometimes we are willing to do it again, so we go ahead and figure it out once more. Some other times though…

### An example

I lead the R&D department at Hutch and we often have to dig deep into new and unseen technologies, frameworks or languages. You try and experiment a lot and can’t expect to remember everything you interact with. You work on something for a couple months then, once you’re done, switch to something very different. Or maybe you just work on the next step in a pipeline.

Then, when you least expect it, it happens. You have to go back to that framework you used 3 months before to make a change. You give it a look, a puzzled one ?.

> “Oh, actually I remember this. To make it behave this other way I go here…change this…and voilà!”

At that moment you feel pretty good about it. You were able to recollect how things worked. You’re even proud of yourself for leaving simple docs on many of the functions you wrote many moons before. Then with a light touch of your mouse, you run the project and…

⛔ **ERROR! The main frame has some cowbells directed towards Mars, this is not allowed.**

? Yikes! This looks very cryptic. You take a look at the code you changed and, well…you try to run it again. Maybe something will automatically change. Maybe looking at it again had some quantum effect of some sort. Nope.

⛔ **ERROR! The main frame has some cowbells directed towards Mars, this is not allowed.**

You then read through the comments or the docs. Nothing mentions this error, nothing points you in the right direction. This error is so distinctive that you’re sure you saw it before, and also solved it before. As daunting as it feels, you have to figure it out…again!

You start googling the problem and notice some previously visited links.

> “Great! This link is probably the one that helped me with the error…phew. Crisis averted!”

You then scroll the page and, oh no! More…many more visited links. So now you have no idea which one led to a solution if any. And so the search continues until eventually, you figure it out — minutes, hours or even days later.

### Good documentation covers more than just happy paths ?

I learned this the hard way. Multiple times. It’s often easy, although admirable, to add docs to your functions/methods/classes with the assumption that everything will work well.

I always try to make life easier for whoever will dig into my code. That includes future me! So I diligently add docs to almost all of my functions but the trivial ones. As many have said for decades:

> Your comments should explain the **why** more than the **what**.

Your code should be “_self-documenting”_ so that any added comment addressing the “what” would result redundant.

In all fairness, I tend to add comments even for the “what”, only when I know a function is either long or somehow intricate. Adding a few lines of comments would allow me to skip examining every line of code. This has been helpful countless times and I absolutely recommend it!

But documentation is not just lines of comments on a function. Good documentation is a well written `README.md`. In some scenarios even a full-fledged dedicated website for bigger projects (see [React](https://reactjs.org/docs/getting-started.html), [Redux](https://redux.js.org/introduction/getting-started), [Vue](https://vuejs.org/v2/guide/), [Slate](https://docs.slatejs.org/), …).

The projects mentioned are all open source. Teams are basically compelled to go in greater detail to help people start using their framework or library (and have been doing a great job in that regard!). But what about smaller private projects? What about those projects that will only live within the company (no matter what the size of the team is)? And what about all those issues that are not purely code related?

More often than not we tend to skip the `README.md` file or dismiss it with a few lines only. I’ve been following a simple yet powerful practice to make this task less intimidating and help go beyond the happy paths.

### A basic approach to creating a good README

When mentioning “happy paths” I refer to the practice of assuming everything will run smoothly. This means we are only addressing each step of a process as if it will always succeed.

Unfortunately, that is not always the case so, how can we make our lives better? How do we make sure that even the not-so-happy paths are covered?

Here are a few suggestions:

* Start by writing down a few lines about what the project is about and **what problem you are trying to solve.** This helps you, and whoever goes through it, understanding the intent of the project.
* As you go about setting everything up, make sure you add each step to the `README.md`. It doesn’t have to be well formatted and phrased, it just needs to be there for now. This usually comes in the form of installation instructions.
* If at any time you face an error of any sort, add a section at the bottom. You can call it **Common Errors.** There you add some details about the error you faced and how you solved it. One crucial thing I like to do here is add links to the source of the solution (or anything that helped me get there).
* When I reach a stable point in the project I try to install it on a new machine (if it’s a possibility). The goal here is to **ensure that the set-up steps we listed before are correct** and work as expected.
* Most importantly, you need to have a section answering the question: **how do I use/run this project?** This should be as clear as possible, so put some effort into it! Sometimes, though, you can’t answer this question until later on. You can wait until you are in a working/running state to update the `README.md` .
* Put aside some time to **review and clean** up your `README.md` file. Most of the time you’ll probably need to **update it**.

This is often enough for small size projects. For mid to large-sized ones it can be a starting point to develop some good practices. Talk about it with the rest of the team and agree on a common approach that will make everyone happy. Keep in mind that **maintaining the docs up to date is crucial!** Hold each other accountable for it and after the initial effort, it’ll become natural, just like a simple refactoring!

### Conclusion

Writing good docs involves maintaining a good `README.md` and documenting the **whys** in your code more than the **what**.

If you make a small effort and incrementally build up a good `README.md` it will feel less intimidating. Not only will it make your life better in the future, but it will help anyone else contributing.

Don’t cover only the happy paths expecting everything will work, also cover eventual errors that you face or any issue a newcomer might face. Keep a dedicated section for this.

**Bonus:** when estimating your work with a PM, take into account the effort required to write/update the docs. Don’t underestimate the fact that good docs require a good amount of time. But that time is very well spent!

? Hi, I’m Gabri! I love innovation and lead R&D at Hutch. I also love React, Javascript and Machine Learning (among a million other things). You can follow me on twitter @[**G**abriOnTheRocks](https://twitter.com/GabriOnTheRocks) and on GitHub @[Gabri3l](https://github.com/Gabri3l) . Leave a comment if you have any other recommendation that you’d like to share, or send a DM on Twitter if you have any question!


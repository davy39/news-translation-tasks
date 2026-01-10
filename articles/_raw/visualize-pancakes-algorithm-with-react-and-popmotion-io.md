---
title: How to Visualize the Pancakes Algorithm with React and Popmotion.io
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2019-09-03T12:39:43.000Z'
originalURL: https://freecodecamp.org/news/visualize-pancakes-algorithm-with-react-and-popmotion-io
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/pancakes-algorithm-1.png
tags:
- name: algorithms
  slug: algorithms
- name: Job Interview
  slug: job-interview
- name: React
  slug: react
seo_title: null
seo_desc: What you are going to see below was supposed to be part of my solution to
  an exercise given in a coding challenge. It was several months ago, and I had signed
  in for it. Due to unforeseen factors, I hadn't finished it. Now, after that time
  and the ch...
---

![Image](https://www.freecodecamp.org/news/content/images/2019/09/pancakes-algorithm.png align="left")

What you are going to see below was supposed to be part of my solution to an exercise given in a coding challenge. It was several months ago, and I had signed in for it. Due to unforeseen factors, I hadn't finished it. Now, after that time and the challenge is finished, I can share it here.

This is not going to be a step-by-step tutorial. Rather, it'll be a quick review of how can we use frameworks like React and Popmotion.io along with an algorithm. And then create a nice visualization of that very same algorithm. Somehow it feels nice! ?

The so called [*Pancakes Sorting Algorithm*](https://en.wikipedia.org/wiki/Pancake_sorting) is a famous (or not?) sorting algorithm that you can read more about on the internet, if you're interested. Its nature is out of the scope of this article. Here we only see it in action with nice animations, thanks to Popmotion.io.

Here is the [*live demo*](https://pancakes-algorithm.herokuapp.com/) you can play with. There are two text inputs and two buttons. In the first input you enter the time interval which will be used for each animation round, that is how fast each pancake will be sorted. It's in milliseconds, which means if you enter the value 1000, the animation will execute for roughly 1 second.

The second input is used to define how many pancakes you want to see sorting. The value there must be between 2 and 50. The buttons are self-explanatory enough. One is for starting the sorting animation, the other one is for resetting it.

And [*here*](https://gitlab.com/mihailgaberov/pancake-algorithm-visualizer) is where you can find the source code for the demo app. Feel free to check it out and take a closer look. You might try to amend the animations I did. I would be more than interested to see your versions. :)

That was all. Nice and short, perfect for the summer! ☀️ ?

? Thanks for reading! ?

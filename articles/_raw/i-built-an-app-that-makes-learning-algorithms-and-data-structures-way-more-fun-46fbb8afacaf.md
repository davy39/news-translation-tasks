---
title: I built an app that makes learning algorithms and data structures way more
  fun
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-20T17:15:35.000Z'
originalURL: https://freecodecamp.org/news/i-built-an-app-that-makes-learning-algorithms-and-data-structures-way-more-fun-46fbb8afacaf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8NEXTT3SN0DQ9Di99WK_CA.png
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By peterWeinberg

  I’m a self-taught programmer. This means I’m constantly dealing with impostor syndrome.
  It’s not uncommon for me to feel like I’m inadequate, and at a disadvantage for
  grasping complex Computer Science concepts.

  I’ve never been any g...'
---

By peterWeinberg

[I’m a self-taught programmer](https://medium.freecodecamp.org/the-freecodecamp-alumni-network-a-homegrown-mentorship-network-for-fcc-alumni-529e4531c34f). This means I’m constantly dealing with [impostor syndrome](https://guide.freecodecamp.org/working-in-tech/imposter-syndrome). It’s not uncommon for me to feel like I’m inadequate, and at a disadvantage for grasping complex Computer Science concepts.

I’ve never been any good at math. And I’ve always tied strong math skills to one’s natural ability to excel at programming. I feel like I have to work harder than others (who have innate skills in math) to learn the same concepts. With this idea rooted deep in my brain, I was pretty sure I’d never be able to learn things like traversing binary search trees, and how to mentally parse recursive nightmares like Mergesort.

Though with a little effort, I managed to surprise myself. So I wanted to share a bit about how, and the tangible results of my efforts. As always, with the hope that there might be some contributors out there willing to pitch in!

Enter [CS-Playground-React](http://cs-playground-react.surge.sh/), a simple in-browser JavaScript sandbox for learning and practicing algorithms and data structures.

This no-sign-up interview prep app saves your progress automatically, offers solutions for when you get stuck, and comes chock-full of [links to helpful articles, tutorials, and other resources](https://github.com/no-stack-dub-sack/cs-playground-react/blob/master/RESOURCES.md) to help make your journey a lot less painful than mine was!

Let me acknowledge outright that this app is nothing groundbreaking. (I know you were thinking it!) There are a ton of apps out there that teach similar skills and give you the ability to write and run code right in your browser.

But CS Playground React intends to be extremely minimalistic, and hones in on a very specific set of topics. Plus, this _is not_ meant to be the next big thing. Building this app was just my way of making learning this stuff fun. If it ends up being a valuable resource for even one other person along the way, all the better.

The app is still a work in progress, and there’s plenty of ground left to cover when it comes to subject matter and potential features. So if you know a cool challenge or data structure I haven’t covered, or see something you think you can improve, don’t hesitate to [open an issue](https://github.com/no-stack-dub-sack/cs-playground-react/issues/new) or submit a pull request. ?

If you just want to check out the app, read no more — it’s live [here](http://cs-playground-react.surge.sh) (also available over https, will register service worker for offline caching).

If you’re interested in the code, [look no further](https://github.com/no-stack-dub-sack/cs-playground-react).

The rest is all the boring stuff about the why and the how :-)

### Why I built this

My motivations for building this app were simple: I wanted to learn, and I wanted to make learning easier and more fun. More important, is why I wanted to learn these specific skills.

Over the past 18 months or so, I can confidently say I’ve learned how to code. Though I still hesitate to call myself a programmer. And this is not because I don’t code for a living (I don’t), but more or less because of the [impostor syndrome](https://en.wikipedia.org/wiki/Impostor_syndrome) phenomenon I referenced earlier. I know how to build stuff, sure. But up until very recently, I knew very little about formal Computer Science.

By learning CS fundamentals, I hoped to not only feel more confident in thinking of myself as a programmer, but to help others see me that way too.

Self-taught programmers are a pill that the tech industry has found easier to swallow in recent years. Especially in areas like Silicon Valley, where coding bootcamps have sprung up on every street corner.

Yet, there’s still a major hurdle to overcome for most programmers hoping to enter the industry without a formal Computer Science education.

So to help lessen the blow of holding a Bachelors of Arts rather than a Bachelors of Science, I set out to teach myself some of the concepts that a first or second year CS student might learn. I thought that this would complement some of my more practical development skills, and help others to take me more seriously as a programmer.

I used a set of topics known to be common to programming interviews as the baseline that I wanted to cover.

Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, Stacks, Queues, Linked Lists, Hash Tables, and Binary Search Trees. Phwewf…

I was super intimidated by this line-up of problems, and had been putting off tackling them for quite some time.

Unwilling to accept defeat, I finally began to dig in. Tracking down tutorials, reading every article I could find, and running circles of confusion around myself day after day.

In time, though, some of the concepts were beginning to sink in. But there were a couple of problems:

1. **I was getting kind of bored.** I love problem solving, but let’s face it, solving `reverseLevelOrder` traversal of a binary search tree is a lot less fun than solving a real-world problem for your latest app.
2. **This was _very_ time consuming.** I work full-time (NOT writing code all day) and my free time to code is extremely valuable. I knew I’d be spending months on this, and I became concerned that I would lose touch with my more marketable skills.

All this CS stuff is great to have under your belt, but let’s face it, most often we web devs get hired to build stuff. And there aren’t too many practical uses for most of these concepts in every day web development.

For me, learning these concepts were a point of pride, and I wasn’t going to give up. But my number one priority was still to be proficient in practical web development.

So I decided to bring the two ideas together. The answer was to build a simple app that would help me achieve my goals _and_ keep me well-practiced in my core skills.

To me, the best way to learn something (especially something dry), is to relate it to something you love. So as I was building this app, and having a blast doing it, I was also developing content for it.

Now, learning algos and data structures was a necessary part of my latest project. Because, of course, what’s the point of building an interview prep app unless you’re going to fill it with problems!

Every few days, I was learning a new algorithm or data structure. Once I almost had it down, I would compile the learning resources and add it to the app. Now, I could practice it over and over again in a super simple workspace that I built myself. How cool is that!?

![Image](https://cdn-media-1.freecodecamp.org/images/1*LMKb4tY_71Nr3NuuPrlwQg.gif)
_A really cool site I found which visualizes how sorting algos and data structures work. This is Quicksort doing its thing on a 100 item array. You can find the full list of visualizations [here](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html" rel="noopener" target="_blank" title="). Thanks USF, this is awesome!_

The main point is, I took something I had been putting off for a long time, and found a way to make it fun. And sure enough, I had greater success in achieving my goals because of it.

I built this app for me, but I wanted to share it with you all for a reason. If even one other person finds CS-Playground-React useful, I’ll feel like I’ve done my part (or at least part of it) to give back to this community.

There are so many programmers out there who freely share their knowledge and experiences, and ask for little or nothing in return. Without such an open minded community, learning to code on your own would hardly be possible.

Ten years ago, there were far fewer options when it came to self-guided learning. So I’m grateful every day for living in an information age where so much knowledge is so readily accessible.

It made this journey possible for me, and I hope someone else out there will stumble upon this article and discover that their own journey has gotten just a little bit easier.

#### Tech Stack & Hacks

In case you’re interested, I built this app with React & React-Redux (although the [first version](https://github.com/no-stack-dub-sack/algos-and-data-structures) was vanilla JS, CSS, and HTML). It also uses [CodeMirror](https://codemirror.net/) and [React-Codemirror2](https://github.com/scniro/react-codemirror2) to embed an editor into the browser (NOTE: the original React-CodeMirror is no longer maintained and doesn’t play well with newer versions of React, so go give [Scniro](https://github.com/scniro)’s repo a star on GitHub for picking up the slack!).

#### Mock console

A little hack allows me to fire a redux action every time a user calls `console.log` in their code. In this way, I can capture the logged messages and in turn mock out a console in the browser to show the code’s output — which I thought was kind of cool! You can run `clearConsole()` any time you want to clear the mock console’s messages.

#### Persisting Code

I wanted to make this app super easy to use. So instead of implementing a database and asking users to login, I chose a simpler approach for saving progress. Redux manages the application’s state during each session, and I use `localStorage` for persisting code across sessions. The app retrieves this saved state on your next visit, and rehydrates the Redux store with it. This way you can pick up right where you left off.

If for some reason you want to erase all your progress, you can run `resetState()` at any time in the editor. If you do not want to commit your code to local storage, leave a `// DO NOT SAVE` comment in your code before navigating away. This will prevent saving any code, not only for that file.

As a side note, it turns out that there’s a package that does this for you, called Redux-Persist (which I found out after the fact). But for a simple use-case, if you can do something with a few lines of code, or install an NPM package to do the same thing? I’ll choose the former every time. Chances are, you’re saving hundreds of lines of code and a whole new set of dependencies. It’s always a give and take, and you have to decide when the highly optimized (but heavier weight) solution is better than your simplistic one.

#### Resizable Panes

The last trick I had up my sleeve was making the workspace flexible and easy to use. I wanted to give users the ability to resize both the editor and the console, so I used a little script I found called `[simpleDrag.js](https://github.com/lingtalfi/simpledrag)`, React `refs`, and the magic of flexbox to make this possible.

Thanks for reading, and happy hacking!


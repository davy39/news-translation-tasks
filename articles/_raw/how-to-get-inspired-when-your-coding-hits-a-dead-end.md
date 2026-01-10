---
title: How to Get Inspired When Your Coding Hits a Dead End
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-25T17:23:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-inspired-when-your-coding-hits-a-dead-end
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/codinginspiration-2.png
tags:
- name: Inspiration
  slug: inspiration
- name: motivation
  slug: motivation
- name: 'self-improvement '
  slug: self-improvement
seo_title: null
seo_desc: "By Ryan Dawson\nHitting a dead-end is common when you're programming. It’s\
  \ common with any type of problem-solving. \nWe get stuck on a particular way of\
  \ seeing the problem and it can be difficult to achieve a new perspective. \nI recently\
  \ came across a..."
---

By Ryan Dawson

Hitting a dead-end is common when you're programming. It’s common with any type of problem-solving. 

We get stuck on a particular way of seeing the problem and it can be difficult to achieve a new perspective. 

I recently came across a tool from the creative arts and realised it could be adapted to work for programming.

The tool that inspired me is Oblique Strategy Cards. They are prompts to break a cycle of thinking and inspire us to think differently. Cards include ‘Remove specifics and convert to ambiguities’ and ‘Use an old idea’. 

One of their most famous uses was on the David Bowie album _Heroes_. On the track ‘Sense of Doubt’, for example, Bowie and Brian Eno took turns doing overdubs based on Oblique Strategy Cards [without revealing to the other what their card had said](https://dangerousminds.net/comments/brian_eno_and_peter_schmidts_oblique_strategies_the_original_handwritt).

I think coding dead ends need something more direct. In moments of being stuck on a problem we both need inspiration and reassurance. 

## The Solution? The Coding Inspiration Machine

So I’ve collected quotes on the process of coding from experts – people who have created programming languages and operating systems. And I’ve put these wise words into a [design by Gordana Minovska](https://github.com/gminovska/RandomQuoteMachine) that gives the quotes centre stage.

![Image](https://lh5.googleusercontent.com/vFx4xkI63PkxfNy1UQGuiGvKYBeVl_-83ScRc68smMQSa1AgRRGi9mPtHnet_XHDYk-hZono_wHUz_F7fXY1dbYhsJ0nq24ynFU52md65YZfqmdMRd_LQR-4zYID4ZK0Vg7l0NVD)
_[https://ryandawsonuk.github.io/CodingInspirationMachine/](https://ryandawsonuk.github.io/CodingInspirationMachine/)_

The aim is to have a tool to help get from “I can’t see any solution” to “maybe this approach will go somewhere” to “aha”. 

We often get stuck in a perspective that doesn’t allow us to see the ‘maybe’ approaches. In those moments we could use some wise words from a master problem-solver to give us a jolt. 

For example, these words from Robert C. Martin:

> When you are working on a problem, you sometimes get so close to it that you can’t see all the options. You miss elegant solutions because the creative part of your mind is suppressed by the intensity of your focus.

The idea is to either bookmark [the url](https://ryandawsonuk.github.io/CodingInspirationMachine/) or fork the repo and configure GitHub Pages to host your own version. 

With a fork you can change the quotes to whatever you find most helpful. Then you can return to the Coding Inspiration Machine when you get stuck.

Of course this is just one inspiration tool. It won’t replace others like brainstorming and mind-maps. 

David Bowie used many tools for inspiration and his music probably owes more to inspiration from [newspaper clippings](http://www.openculture.com/2019/05/how-david-bowie-used-william-s-burroughs-cut-up-method-to-write-his-unforgettable-lyrics.html) than Oblique Strategy Cards. 

But the point with the Coding Inspiration Machine is to have an easy, go-to tool to remind us that it’s ok to get stuck, that it’s meant to be hard, and that there will be ways forward.

## Real world applications for the Coding Inspiration Machine

Here are a few situations I’ve hit recently that got me thinking about this technique.

### Getting creative

There was an authorization problem with a system I work on. The authorization code that was working with several authorization providers didn’t work for a particular Active Directory setup. 

We didn’t know initially if it was a config problem on the provider side, config on the app side, a connectivity problem, or a problem in our code. We even [built a custom test tool](https://github.com/ryandawsonuk/oauth2-test-tool) to narrow the problem down. 

It eventually turned out that we needed an extra resource_uri parameter to be included in one of our http calls.

### Finding a solution

For this same system we wanted to show metrics over long periods. This led to trying to make Prometheus queries over data ranges that are too big for Prometheus queries. 

There’s a range of ways to handle this, from changing what we query for, to using different/more tools, to restructuring the data. We chose what amounts to [restructuring the data](https://github.com/SeldonIO/seldon-core/pull/2484).

### Seeing the less obvious answer

My father-in-law showed me that his smart TV was not working with Netflix. 

After navigating several confusing menus and trying various wireless networks, we found it to be a signal strength problem with the network that the TV was preferring (it worked fine with a network that the TV thought was lower strength).

## Wrapping up

These problems are all different but they share common features. 

Each required research and experimentation and eliminating possibilities. Each of them was initially surprising and it took time to adjust expectations and realise why the problem was there. It was necessary to explore multiple paths and each time that a path was unsuccessful it was disheartening. 

It is easy to get stuck in these situations and find that we can’t see any paths anymore. The words of others who have been there before can help us see these situations with fresh eyes.

Have a look at the [Coding Inspiration Machine](https://ryandawsonuk.github.io/CodingInspirationMachine/) and feel free to submit suggestions to the [github repo](https://github.com/ryandawsonuk/CodingInspirationMachine) or [contact me on twitter](https://twitter.com/ryandawsongb).  


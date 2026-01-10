---
title: How to choose the best code conventions for you and your team
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T21:30:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-the-best-code-conventions-for-you-and-your-team-992cc2cc7b83
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OcAtcYPz7bzbXr40
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ofer Vugman

  Put an end to the never-ending debate


  _Photo by [Unsplash](https://unsplash.com/@johnjac?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">John Jackson on <a href="https://unsplash.com?utm_source=medium&ut...'
---

By Ofer Vugman

#### **Put an end to the never-ending debate**

![Image](https://cdn-media-1.freecodecamp.org/images/1n2grhWszDdGlSdNlQCg75q4JI6fUIk9Uu6t)
_Photo by [Unsplash](https://unsplash.com/@johnjac?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">John Jackson</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

_- “Listen, those private variables should go after the public ones!”_  
_- “No way! Public variables go before private!”_  
_- “Let’s ask Deb, and let her decide”_  
_- “Wait, why aren’t these constants camel-cased?”_

?‍♂ ?‍♀

Raise your hand if you’ve found yourself in this kind of discussion before. Ok, don’t really raise it, but something tells me some of you may have taken part in this scenario once or twice.

As a developer for the past decade, I’ve found myself in quite a few, some might say too many, discussions about code conventions. These discussions, as useful as they are, sometimes deteriorate to never-ending philosophical rambles. And then they start to shift into topics ranging from indentation to folder structure.

It can be painful.

So, how do you truly decide what the best convention is, and better yet, do best conventions even exist? I’ll lay it out here, so you can put those philosophical rambles to rest, once and for all.

### So why do we even need conventions?

In order to determine what the best convention is and whether they even exist, we first need to understand _why_ we even need conventions.

There are more than a few reasons, but I’ll focus on the most important one: **readability**.

What if I decided to switch to writing in caps only. LIKE THIS, WHICH MAY SEEM STRANGE. You immediately notice it, and your brain starts to process what’s different.

Take this simple example, and think about variable naming or indentation. If every time you returned to the code and it was written differently, it would be as if you were starting from square one. But when coding with conventions, your code is easier to understand, and hence readable, even if it was written months ago.

This becomes even more crucial when working on a team of developers, where each writes their own code with their preferred convention. The amount of time spent to understand and review each other’s code will take… well… you get the point.

**In order to collaborate with other developers efficiently and qualitatively, you must have a common convention.**

> “Programs must be written for people to read, and only incidentally for machines to execute.” — Hal Abelson

### How to choose the best code convention

Whether you just started coding, or you’re part of a kickass dev team, or if you’ve just become a CTO, how do you go about choosing your code conventions?

Here’s my guide to choosing the best code convention:

1. **Get inspiration from dev teams you admire:** Nothing beats experience, and some of the biggest and smartest companies publish their coding guidelines. For example, Airbnb published their [javascript](https://github.com/airbnb/javascript) and [ruby](https://github.com/airbnb/ruby) style guides, and Google published their own [Java](https://google.github.io/styleguide/javaguide.html) and [Python](https://google.github.io/styleguide/pyguide.html) style guides. Whether you like these companies or not, if you sum up the years of experience each of their developers have, it adds up to gazillion. Try to apply some of these companies’ style guides to your own team.
2. **Crowdsource knowledge from your peers:** We’re lucky to be part of such a dynamic community. In fact, one of the biggest advantages of being a developer today is our community. Whether on [Slack](http://slack.com), [Spectrum](https://spectrum.chat/), [Discord](https://discordapp.com/), or any collab platform, you can always find knowledgeable groups to post a question about code conventions and get answers from devs around the world, instantly.
3. **Ignore code samples.** Yup, just ignore them. Every now and then I stumble upon code that was copy/pasted from an answer on [Stackoverflow](https://stackoverflow.com/), or something similar. What people sometimes forget is that the code samples they just copied were probably written as an answer to a technical question, or as an explanation for some library. In most cases, the writer didn’t mean to, nor had time to deal with, code conventions.

These tips should help you get started, and can lay the groundwork for introducing code conventions for your dev team.

And now for some philosophy.

### Do ‘best’ conventions even exist?

That depends on what ‘best’ means. If Airbnb or Google use a certain convention, or if 10 different CTOs told you their convention is the best — does that mean it’s the best convention for you?

Moreover, conventions are subject to change. Can something that changes over time ever be named the ‘best’?

When I started at [Lemonade](https://www.lemonade.com/) as the only front-end developer, I found it hard to read the code the previous dev wrote. It might have been the best convention for him, but it wasn’t for me. So I rewrote every piece of code I worked on using my conventions. Over time, more developers joined the team and our conventions evolved.

Each dev came from a diverse background, with different standards and conventions. To formalize our conventions, we used Airbnb’s javascript style guide as a starting point. We reviewed the conventions in that guide and changed or removed the ones we didn’t agree with, and adopted the ones we liked. We even adopted conventions devs brought from their own experience, and integrated them into our master convention.

The process of evaluating each convention and deciding whether we should adopt it, not only improved our code readability but also improved our teamwork. (More on that in a future post!)

Here’s the hard truth: **there is no universal definition for best conventions, because they simply don’t exist.**

![Image](https://cdn-media-1.freecodecamp.org/images/TMEHrum5-VFAoJBR5yPJgrZpevkRgXRtCvc3)

In contrast to what you were taught in school, there isn’t always one right answer to each question. In this case, there can be a lot of them.

Developers have different ways to implement different or even the same things. Some of us prefer all class members names begin with an ‘m_’ prefix. Some of us like to use two space indents, some prefer tabs, some might say that using the word `Utils` in a class name is wrong. Geez, this is an endless discussion, but all these preferences come with good reasoning.

At the end of the day, it all comes down to which convention improves the readability of your code. Which one allows your team to communicate better, move forward faster, and with better efficiency.

Remember, code conventions are merely suggestions. Yes, once you decide on a convention to use, you should follow through. But remember: they’re not carved in stone and are subject to change. Allow yourself to experiment with different conventions until you find the best one that suits you and your team.

So what are the best code conventions? Easy - yours!


---
title: How to properly give a code review
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-02-13T18:12:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-properly-give-a-code-review-c2fcc49e345f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*MQGtEWPkQYWeOatk
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: teamwork
  slug: teamwork
- name: technology
  slug: technology
seo_title: null
seo_desc: You're sitting at your desk, minding your own business, when one of your
  colleagues comes over and asks if you could give them a code review. Not wanting
  to seem rude (and remembering that they have bestowed this favor upon you not so
  long ago), you ...
---

You're sitting at your desk, minding your own business, when one of your colleagues comes over and asks if you could give them a code review. Not wanting to seem rude (and remembering that they have bestowed this favor upon you not so long ago), you agree to walk along to their desk to examine what they have been working on.

At this point in time, you have no idea what your colleague has been working on. It could be a simple bug fix, a small feature or a major refactor. Regardless of the size and scale of the task, you should always go in prepared when you are giving a code review. To find out how, read below.

#### The basics: what is a code review?

According to [Wikipedia](https://en.wikipedia.org/wiki/Code_review), a code review is:

> A software quality assurance activity in which one or several humans check a program mainly by viewing and reading parts of its source code, and they do so after implementation or as an interruption of implementation. At least one of the humans must not be the code’s author.

And in simple words, it means that to improve the quality of your company’s product, it is necessary for different people to evaluate the code.

Up to this point, I’m assuming I haven’t added anything new to your perception of a code review. But in all fairness, there are still a lot of ambiguities:

* How should a code review start?
* How do you tell if a code review is good or bad?
* How long should a code review be?

These are just some examples to questions I am sure you are asking. While there isn’t a simple answer for each of them, there are guidelines you can follow to help you along.

![Image](https://cdn-media-1.freecodecamp.org/images/nCL-jGPPlOdY1JaYcT4PXYDTN56J1mPHEDN5)
_Photo by [Unsplash](https://unsplash.com/@heftiba?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Toa Heftiba</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Preparation Is Key

Before you go into the code review itself, ask these two questions:

1. Are you aware of what your co-worker has been working on?
2. Are you familiar with the area of the code they have been working on?

If you answered no to either of these questions, then you need to do some homework. This is so you can come to the code review as prepared as you can be.

One way of bridging the gap is by looking at the ticket/issue associated with the feature. There you should find enough information to let you know the scope and reasoning behind the developer’s task. Furthermore, if it is customary in your work place, you can look over the comments in the ticket. You want to see if there have been any changes to the ticket that do not match the original intention. And if all else fails, before you begin the code review, ask your team member to explain what they have been working on and why.

What I always tend to do, even if I am well aware of what the task is all about, is to ask the developer to explain the scope of the task in their own words. That way I can minimize the risk of not being aware of something in the task. When the developer gets to reiterate what they have been doing, they can better explain to themselves what they have done.

![Image](https://cdn-media-1.freecodecamp.org/images/Z52U2ZJOF56lA-XRETqnNYA3MwSU4LgKSQV3)
_Photo by [Unsplash](https://unsplash.com/@roller1?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">kyle smith</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Listen, then Ask

Every conversation is a two-way street: while one side does the talking, the other side listens. The same logic applies to a code review. Try not to interrupt the other developer so as not to disrupt the flow they have prepared in their minds. Take mental notes or write down things that seem important to you in order to remind yourself what to ask when you get your turn.

A code review can become long and tedious and it is important to stay focused and ask crucial questions. If there is something you don’t understand, ask the developer to elaborate on it. There is no shame in not being perfectly knowledgeable in every section of your code base.

By asking questions, not only are **_you_** getting more familiar with the code, but the developer is also experiencing having to explain to someone else what they have done. In doing so, more often than not, the developer might identify a scenario they haven’t thought about. Or you might see a certain flow which may cause a bug.

I know that some of you might be saying, **“but how can I ask questions if I have less/more experience than the other developer? Won’t it be rude?”**

The answer is **NO**.

When there is no asking, there is no learning. The whole point of a code review is not just to apply an approval stamp to what the other developer has done. You are there to go over the logic of the code but are also in part responsible for the overall structure of the code.

![Image](https://cdn-media-1.freecodecamp.org/images/ayTOonqiasKzPynMEhepqu4Xx0wxSkuEanTI)
_Photo by [Unsplash](https://unsplash.com/@h4x0r3?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Thao Le Hoang</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Be empathetic but honest

Developers take pride in their work. Like most human beings, they do not like to hear someone else tell them what they are doing wrong. Be that as it may, it is important to let your voice be heard as the reviewer.

Similar to how each person will have a different flavor of ice cream, each developer has a different opinion on how code should be written and maintained. Nevertheless, there are certain common truths each developer must adhere to. So in order to keep things calm, be sure to phrase your statements in a constructive manner. That way, no one should get offended.

Sure, you will have disagreements. In certain situations it will be important to stress the drawbacks of the code that needs to be re-written. If you reach a dead end, try to bring it up with another developer or a team leader. Never forget that on the other side, there is another developer with their own point of view.

#### Good Things To Keep In Mind

While the subjects discussed above form the tripod of a code review (if you will), there are also other things to pay attention to:

* If relevant, ask if unit tests have been added and if so, go over them
* [Documentation](https://medium.freecodecamp.org/why-documentation-matters-and-why-you-should-include-it-in-your-code-41ef62dd5c2f) is part of the code review (and if there is none, discuss the point of adding it)
* Before the code review starts, ask the developer how long they think it should take (this will help you plan your day accordingly)
* If there are many changes following the code review, make sure to schedule another one so the next iteration doesn’t go unnoticed
* Be courteous and try to give the other developer compliments on what they have done

No two code reviews are alike, and similar to most activities, practice makes perfect. Trust your instincts and trust your co-workers. Everything else will follow through.


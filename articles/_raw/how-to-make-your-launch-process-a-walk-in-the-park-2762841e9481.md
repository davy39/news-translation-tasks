---
title: How to make your launch process a walk in the park
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-19T20:10:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-launch-process-a-walk-in-the-park-2762841e9481
coverImage: https://cdn-media-1.freecodecamp.org/images/1*B3eOiQjaBkMbn7AzF8Erhg.jpeg
tags:
- name: business
  slug: business
- name: Productivity
  slug: productivity
- name: project management
  slug: project-management
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By David Yu

  It was 2AM. My phone was still buzzing with developer conversations about how to
  handle 404 pages. It was only the beginning…

  T minus three days until launch. We were running around like a chicken with its
  head cut off. ?

  I had to think o...'
---

By David Yu

It was 2AM. My phone was still buzzing with developer conversations about how to handle 404 pages. It was only the beginning…

T minus three days until launch. We were running around like a chicken with its head cut off. ?

I had to think of how we would avoid the feeling of apocalypse when we approach the official launch date.

As Murphy’s Law states:

> Anything that can go wrong will go wrong.

How do we launch a product and ensure that something DOES NOT go wrong (as much as we’re able)?

Below is the beta version of my strategy for the next launch.

### Have content for the first week

When you tell a client that the launch date is a month away, the list of data and assets required for launch are buried in their Inbox and pop out just a week before launch. ?

In the end, we’re scrambling for stuff because of the sudden changes to images and text — the “little things”.

> Oh wait, the image size ratio is not right, let’s double check with the client if there is another image…

Valuable time is lost during this back and forth communication.

![Image](https://cdn-media-1.freecodecamp.org/images/exFn60wYTY3iP0eLWC1CNil4lBRWCn8DyPew)
_“A group of people brainstorming over a laptop and sheets of paper” by [Unsplash](https://unsplash.com/@cikstefan?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Štefan Štefančík</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### How to urge the client to provide the information you need without being rude

* Explain how the content is the soul of the product. Without it, the product is only a skeleton of fancy logic.
* Be more proactive in understanding what their obstacles are in acquiring those assets.
* Write down detailed specifications for image and copy: image size ratio, preferred file type, word length, preferred font family, etc.
* Identify the single person who is responsible for the task. Offer help and assistance. Adjustments are easier to do in the early stages.

#### What if the client says, “Chill…bro, we’re on it.” And there’s no clear action you see being taken?

You could explain why you’re in a hurry, so they get the context behind what all you need to do.

It’s like building a brick house. When we only have one or two bricks laid on the ground, we can easily say, **“Meh, I don’t like brick. Let’s use bamboo.”**

But, it will take a miracle to swap bricks with bamboo when the brick house is near completion. We will build a flimsy house (product) at best if that’s the case, or our launch date will be delayed.

### Be firm on feature freeze

Feature freeze is a handy concept that is easier said than done.

> In software engineering, a **freeze** is a point in time in the development process after which the rules for making changes to the source code or related resources become more strict, or the period during which those rules are applied - [Wikipedia](https://en.wikipedia.org/wiki/Freeze_(software_engineering))

In addition to setting a feature freeze a week prior to the launch date, we also need to be clear about what a **feature** is.

> A discrete piece of functionality desired by stakeholders - [Oliver Dolan](https://www.quora.com/profile/Oliver-Dolan-1)

If you have a website with an interactive map in it, would it be a new feature to build a “back-up” map with another map provider?

Our thought process may have been that since we’re in China, there is no guarantee that our first choice of map provider wouldn’t be blocked.

So we may cram it into our schedule as a feature.

![Image](https://cdn-media-1.freecodecamp.org/images/4cUvVvqpUznMVlXLdn1PSBSHXxCH2GgeL-GO)
_Photo by [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

But, how do we decide if this feature is worth our time?

#### Here are the questions to ask your team and client for every feature that you plan on implementing

1. What happens if we don’t implement this?
2. What’s the priority level of this?
3. Do we have the capacity to take on this work without delaying the launch date?

### Be more assertive with your opinions

[Imposter syndrome](https://en.wikipedia.org/wiki/Impostor_syndrome) affects us at all stages of our career. When a senior developer with 20 years experience says let’s do it this way, and you’re not 100% sure about a counter argument, you whisper under your breath, “Oh… ok.”

This is what I do when I can’t come up with a better solution on the spot.

#### So, how do we prepare for situations like this?

* Understand exactly how we arrived at the conclusion first
* Phrase your solution as a question
* Write down what bothers you and think of a better way to do it later
* Improve your [communication skills](https://medium.freecodecamp.org/how-to-cultivate-great-communication-skills-as-a-dev-and-kick-bad-habits-to-the-curb-d62a075700f5)

> If at first, the idea is not absurd, then there is no hope for it. **- Albert Einstein**

### Take care of [DevOps](https://en.wikipedia.org/wiki/DevOps) first

We complicated our initial setup for development, staging, and production. We spent an enormous amount of time on working on a problem and coming up with a solution.

Waiting twenty minutes to see my changes come online because of fancy code pipelines and connection issues almost made me hate coding. ?

#### So, how could we have done it differently?

* The Dev environment should be able to change **fast.**
* If automation is not saving time, it’s not automation.
* Use a cloud provider that meets your needs
* Make sure the deployment process is smooth from week one

### Have a checklist for testing

To prevent time lost while fixing the same thing, here are a few things to keep in mind when writing the list.

And I’m not talking about writing code to test your code. How often do we fix something and something else breaks?

![Image](https://cdn-media-1.freecodecamp.org/images/2PICSsmZDVBuww5WTJrrBoJOq1CSw40fh6N6)
_“A person making a checklist in a notebook” by [Unsplash](https://unsplash.com/@glenncarstenspeters?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Glenn Carstens-Peters</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

To avoid having to fix the same thing over and over again, here are a few things to keep in mind when writing the list.

* Write the checklist from the user’s perspective
* Grow the list with the feedback from each iteration
* Have a fresh set of eyes run through the list
* Help other developers on the team check the list

### Practice empathy

No matter what position you’re in. A little empathy goes a long way.

For example: if you built an API that’s utilized by a web app and you’re about to make some data key naming changes.

You understand the particular data key names may have been included everywhere by another developer in a web app. Proactively notify other developers before things start to go wrong.

![Image](https://cdn-media-1.freecodecamp.org/images/LnfuxLIiDjt3m5qLBVUKQiFcshcSGAiWJoWY)
_Photo by [Unsplash](https://unsplash.com/@nesabymakers?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">NESA by Makers</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

By notifying all teams that may be affected by a change, we can reduce the likelihood of hiccups during the live demo or even production.

Every role in a team faces its own hurdles. The ability to put yourself in different shoes will change you from just a developer who writes code into a leader that dishes out high quality stable code.

#### Thanks for reading

If you enjoyed this piece, you can clap ? it up so more people can benefit from it.


---
title: Learn CSS Variables in this FREE and interactive course
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-23T08:21:53.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-css-variables-heres-my-free-8-part-course-f2ff452e5140
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m4MKxjoyY-RXYRWBGEjkOw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Per Harald Borgen

  CSS Variables is an exciting new technology for modern browsers. It brings the power
  of variables to CSS, which results in less repetition, better readability, and more
  flexibility.

  To help you get started, I’ve created a free co...'
---

By Per Harald Borgen

CSS Variables is an exciting new technology for modern browsers. It brings the power of variables to CSS, which results in less repetition, better readability, and more flexibility.

To help you get started, I’ve [created a free course on CSS Variables at Scrimba.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article)

This is a continuation of our series of free CSS courses. Previously, we’ve launched courses on [CSS Grid](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article) and [Flexbox](https://scrimba.com/g/gflexbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article). Combined, they’ve gotten well over 20K enrollments.

### The course structure

The course contains 8 interactive screencasts. They’re all between 3–6 minutes long, as my goal is to teach you CSS Variables as quickly as possible. At the end of some of them, I’ll give you a challenge, and encourage you to play with the code interactively. This can be done directly in the browser, as Scrimba screencasts make this possible.

Throughout the course, we’ll be working with a very simple portfolio website, as it gives us the ability to highlight the most important use cases for CSS Variables.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Eu0wU_hiyqOqrhyxNamvsg.png)

Now let’s have a look at each of the lessons.

#### Lesson #1: Why learn CSS Variables

In the very first screencast, I’ll talk about why you should learn CSS Variables. I’ll discuss the general benefits as well as its advantages over SASS and LESS variables.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MxS9trU9nmVDttW_IqQTyA.png)

#### Lesson #2: Your first CSS Variable

Then we’ll jump directly into the code. I’ll first show you how you create a CSS Variable, and then ask you to do the same. It’s important that you actually code, and not just watch the screencasts, as it makes the knowledge stick better.

:root {  
--red: #ff6f69;  
}

body {  
color: var(--red);  
}

#### Lesson #3: Overriding variables

We’ll continue with overriding, a cool concept that’s possible since CSS Variables have access to the DOM and are inherited down the hierarchy. This separates them clearly from SASS and LESS variables, who work more like _constants_ than _variables_ when they hit the browser, and have no knowledge of the DOM.

#### Lesson #4: Local variables

Local variables are variables that only are available in a certain scope, for example inside the header or sidebar section of your app. If you try to access it from another scope, it won’t be defined.

#### Lesson #5: Theming with CSS Variables

Themes is one of the biggest benefits about CSS Variables. By themes, I’m not only talking about full website themes, but also component specific themes, which are a more normal use case (e.g. visually changing an item to _featured_ so that it stands out from the crowd).

![Here we’re using themes to make one of our items in the grid stand out from the others.](https://cdn-media-1.freecodecamp.org/images/1*oRy5JEdUGibetP7OSQ7upQ.png)

  
Here we’re using themes to make one of our items in the grid stand out from the others.

#### Lesson #6: Changing variables with JavaScript

You can also change CSS Variables with JavaScript, which is very useful. This opens up the possibility to allow your users to change your variables. Again something which aren’t possible with LESS and SASS variables. A very relevant example of this is allowing users to adjust the overall font size on your site. This will make it more accessible for people with bad vision.

#### Lesson #7: Responsiveness with CSS Variables

Given that CSS Variables have access to the DOM, they can also be changed based upon to screen size. This is actually just an example on overriding, but I think it deserves a whole new screencast, as responsiveness is pretty core these days. Everything that makes responsiveness easier ought to be used by front-end developers.

#### Lesson #8: CSS Variables and inheritance

Even though I talk about inheritance throughout the course, we’ll end the course with a few extra notes on it, as there are a couple of use cases which you might imagine works, but which don’t.

And that’s it. Going through these quick screencasts, you’ll have a solid understanding of CSS Variables. Watching them will take you less than 30 minutes, and you can also adjust the replay speed to make it even faster.

In other words: this course is probably the fastest way to learn CSS Variables properly.

The challenges might, of course, make it take a little bit more time, but they are voluntary. You choose how interactive you want this course to be.

### The Scrimba format

The course is built using Scrimba, an interactive coding screencast tool of which I’m a co-founder, together with [Magnus](https://medium.com/u/1a7998d688dd) and [Sindre](https://medium.com/u/c825b7f99be3).

As I’ve mentioned before, the unique thing with Scrimba is that the screencasts are fully interactive, meaning you can edit the code inside the casts.

Here’s a gif which explains the concept:

![Pause the screencast → Edit the code → Run it! → See your changes](https://cdn-media-1.freecodecamp.org/images/1*4PWxbgV--7ZHlB-YVqavJg.gif)

  
Pause the screencast → Edit the code → Run it! → See your changes

This is great for when you feel you need to experiment with the code in order to properly understand it, or when you simply want to copy a piece of the code.

Also, Scrimba screencasts weigh 1% of videos in file size, meaning that it’s much easier to watch even when your internet connection is slow.

So check out [the course today](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article), and happy coding :)

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gcssvariables_launch_article)_



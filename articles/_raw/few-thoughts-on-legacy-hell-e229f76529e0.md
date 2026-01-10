---
title: Stuck in legacy code hell? Here are some few thoughts to help you manage the
  situation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-04T11:57:40.000Z'
originalURL: https://freecodecamp.org/news/few-thoughts-on-legacy-hell-e229f76529e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DST6EDWapMJFwawjNykejA.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Felipe Lopes

  I’m gonna tell you a little story about how I ended up in a legacy code project
  and how our team managed to get the best from that.

  First, a little bit of context

  I’ve been working for almost a year on a project, that is quite complex...'
---

By Felipe Lopes

I’m gonna tell you a little story about how I ended up in a legacy code project and how our team managed to get the best from that.

### First, a little bit of context

I’ve been working for almost a year on a project, that is quite complex, to say the least.

While I pass the time reading here at Medium about all the awesome things people are doing around the world in software engineering (creating big infrastructures, putting together several cutting-edge systems to respond to thousands of requests per second ), part of my daily life as a software engineer has not been-so-glamorous. Which is to keep an old extension, for an old platform, up and running properly.

To put it in plain English, I suffer with legacy code.

First, let me tell you about the bright stack. This extension is meant to run in one of the most important e-commerce platforms, [Magento](https://magento.com/). But Magento released a new version of the platform (2.0), with lots of improvements, implementing most of the good practices, backend developers were hoping to see.

For me, it would be great if the extension was made for the latest Magento version, but the extension was developed for the previous version (1.9). An archaic one, lots of times unnecessarily complex, cumbersome and full of intricate xml files. But it does the job. Oh, boy, it does!

Besides that, the extension, as you may be expecting, is written in PHP, the language everyone loves to hate.

Although PHP has gained lots of improvements with the latest 7.x version, Magento 1.9 does not support it and I’m forced into working with old PHP versions. Thus, I’m unable to play with all the new stuff. To finish explaining the scenario, there is not a single piece of test. Neither I, nor anyone in the team, was part of the original extension design and development. In the beginning we were kind of lost, most of the time.

### Running in circles and screaming is not an option

When you start working in a project like this, you feel like those guys playing the last song in the Titanic. Everything is falling apart, but you keep doing your job.

The clients keep opening tickets, the problems never seem to be solved at all. Your boss ask for new features. You start blaming the platform, the code base (someone you don’t even know wrote and you start hating them for that). At this point you are deep down in the legacy hell.

There are actually two things you can do here. The first one is to update your Linkedin profile, put a nice photo, tell a nice story about how good you are and start sending resumés. Looking for a new job, a job without legacy code (spoiler alert, this place does **not** exist) or you can stop, breath and make a plan to deal with that thing.

### Start doing something about it

![Image](https://cdn-media-1.freecodecamp.org/images/jxhrSA2A9s8felRM-frky-yPewds0lZFA3R7)
_Photo by [Unsplash](https://unsplash.com/photos/qAShc5SV83M?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Yung Chang</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

If you are in a scenario like this, you should start acting fast. If your code base is not under a source code version system (git, please) and your team does not use a tool to manage the tasks, maybe you should think about that Linkedin stuff. But if you have the minimum, start with the basic, remove the [cruft](https://www.techopedia.com/definition/15410/cruft).

I’m pretty sure that there is deprecated code, code that is not reached at all, and code that was left behind. Just taking space and making things look like a lot worse than it actually is. Give that code a good look, tinker with it, fill it with break points and start getting rid of what is not being used. Make sure you are not doing anything stupid here and don’t exaggerate. Remember, there is no test yet, so only get rid of those methods you are **completely** sure are useless.

Doing that, you’ll be more comfortable with your code base and you will probably feel more confident. After that, you will still have unnecessary code, but almost everything you have there has meaning, or is useful.

The next step is to think about tests. There are several ways to test software. You can do unitary tests, integration tests, system tests, stress tests, and plenty more. They are great and should be used in the right time. But remember, you are in a critical moment here and you should start with what is really important. Functional tests.

I’m not the most skilled tester. Far from that. I still have a lot to learn and study. But as far as I know, functional tests (for web projects, at least) are the least invasive ones. You don’t have to create mocks, stubs, fakes, dummies. Your tests are going to interact with the browser and simulate the human interaction.

At this point you have a code base with only the code that is needed and few tests to help you stop adding new bugs with every new feature. It is a win-win situation. Now you can stop, breath and think more calmly.

### What next?

![Image](https://cdn-media-1.freecodecamp.org/images/6R3e-PyHQpIrCFWPlPpxLYGtp3X3Za7Xv5pn)
_Photo by [Unsplash](https://unsplash.com/photos/4pPzKfd6BEg?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Patryk Grądys</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

With more time, less bugs and sanity in place, you can start tackling other problems. Have you thought about continuous integration? How is your team development workflow? If you are using git (which I hope), you could start planning your branches. Create a master branch, a develop branch, add new features through feature branches, hot fix branches, and so on.

How is your continuous delivery? How are your versions created? If you have to do more than “pushing a button”, maybe it is time to think about that process. How could you make it more reliable, less error prone? Does your application generate enough logs? Could you improve that? Now it is time to create a better software, now it is up to you.

### That’s it

We are still working on our legacy, trying to make it better. Although we haven’t reached the ideal scenario yet, several things have changed. Now we have only the necessary code. The workflow for that particular extension is well defined. We have functional tests in place and the deployment process is getting better.

After changing that scenario and surviving the legacy hell, our team got the task to develop a new extension to the same old Magento 1.9. Any sane person would be angry about that, but I’m thinking it is the perfect moment to do the right thing. This is the chance to make all the complaints become best practices and create a piece of software with maintainability in mind. but this is a subject for another article.


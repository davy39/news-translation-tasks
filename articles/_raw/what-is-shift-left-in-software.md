---
title: What Does "Shift Left" Mean in Software Development?
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2024-04-15T22:25:08.000Z'
originalURL: https://freecodecamp.org/news/what-is-shift-left-in-software
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Shift-Left-.png
tags:
- name: software development
  slug: software-development
seo_title: null
seo_desc: "I once had a manager who, in a discussion about our project, mentioned\
  \ that we needed to try and shift our work left as much as we could. \nA few months\
  \ later in an interview, the interviewer asked me if I knew what \"shift left\"\
  \ meant.\nUnless there's ..."
---

I once had a manager who, in a discussion about our project, mentioned that we needed to try and **shift our work left** as much as we could. 

A few months later in an interview, the interviewer asked me if I knew what "**shift left**" meant.

Unless there's a secret software-dance someone didn't tell me about, I'm now here to tell you what **shift left** means.

## What Does it Mean to Shift Left in Software?

To shift left is a technical term meaning to try and identify problems as early as you can in your software project lifecycle. 

The 'left' means the beginning of the project, and it's a phrase that just means "let's try and catch as many of our issues, blockers, and problems as early as we can."

## The Software Development Lifecycle

Let's say you're starting a new job as a software engineer at a bank.

Your software development lifecycle may look something like this:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-110.png)
_Example Software Development Lifecycle_

1. First, requirements are provided by your Product Managers.
2. Then the analysis to complete this work is completed by your Business Analysts. 
3. Designs get created for the way the UI needs to look.
4. The devs do their own planning now.
5. Then the devs begin the work!
6. Piece by piece the feature gets built and the testers can test.
7. The project goes through the environments on its way to production. It passes dev. It passes test. It reaches pre-production, and is released to production.
8. The project enters a maintenance period. You check for any issues in your logs, you fix any bugs that arise.

A few examples of **shifting our work left** in this cycle, would be the following:

* Checking the requirements by the technical team to make sure everything asked for can be completed, in the timeframe expected.
* The architects get involved early in the planning stage and try to make tech documents and spot any edge cases or problems the developers might face.
* Maybe the designers make a basic prototype from the designs, to illustrate exactly what is expected.
* When the devs plan, they are given enough time to do a thorough review. It's not a short 15 minute meeting. They are expected to produce class diagrams, code architectural improvements, accurate estimates, they plan for their unit test suite, and they ensure relevant documentation gets updated.
* Testers do manual testing, as well as automated testing. They use the software like a real user would!

### When do we commonly find issues?

Let's think about the times we could commonly catch a bug in a project. Try and think when you would prefer to catch an issue.

* At the end of the project, when all the code has been written, and it's already been released to production for 2 weeks
* As you release it into the pre-production environment
* By the tester on the _testing_ environment
* As the devs are in the middle of coding
* As the devs are doing their planning
* When the designs are being created
* When the architects are making their architectural diagrams
* As the product managers are specifying requirements

The place in this timeline that you can most easily respond to the issue, lose minimal time, and quickly rectify it is **right at the start**. And you can help your team get there by shifting your work left.

## There Are Many Ways to Catch Errors

**Shift left** is a phrase, but it's based on a whole methodology that helps us try and catch issues early for fast iteration cycles to deliver software.

So what are some more steps we could try that would help us **shift our work left**?

Beyond just planning things better, what else can we do?

* You can lint your codebase and catch typos, common errors, and bad design.
* You can introduce type checking into parts of your codebase you think would benefit from it.
* You can increase your unit test coverage.
* You can increase your integration test coverage.
* You can introduce code QA's in your team.
* You can introduce logging and metric alarms for deploys.

Just remember, the later in the flow of your project you go, the more difficult it can be to recover from an error. Catch problems as far left as you can! 😉

Because if your team doesn't find the bug, you can always bet a user will.

## **Conclusion**

I hope this has been useful, and has explained what "shift left" means. Try to incorporate this way of thinking into your development lifecycle and see what happens.

I tweet my articles [here](https://twitter.com/kealanparr) if you would like to read more.


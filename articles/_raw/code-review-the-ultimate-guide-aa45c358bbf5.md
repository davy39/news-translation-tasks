---
title: Code Review — The Ultimate Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T16:05:16.000Z'
originalURL: https://freecodecamp.org/news/code-review-the-ultimate-guide-aa45c358bbf5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c8t6OXt7tMEUpeki-HEobg.jpeg
tags:
- name: code review
  slug: code-review
- name: project management
  slug: project-management
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Assaf Elovic

  The ultimate guide for building your team’s code review process


  After conducting hundreds of code reviews, leading R&D teams and pushing several
  unintentional bugs myself, I’ve decided to share my conclusions for building the
  ultimat...'
---

By Assaf Elovic

#### The ultimate guide for building your team’s code review process

![Image](https://cdn-media-1.freecodecamp.org/images/1*c8t6OXt7tMEUpeki-HEobg.jpeg)

After conducting hundreds of code reviews, leading R&D teams and pushing several unintentional bugs myself, I’ve decided to share my conclusions for building the ultimate code review process for your team.

This article assumes you know what a code review is. So if you don’t, [click here](https://en.wikipedia.org/wiki/Code_review) for a great intro.

Let’s quickly state some straightforward reasons as to why you should do code reviews:

1. Can help reduce bugs in code.
2. Validate that all coding requirements have been filled.
3. An effective way to learn from peers and get familiar with the code base.
4. Helps maintain code styling across the team.
5. Team cohesion — encourage developers to talk to each other on best practices and coding standards.
6. Improves overall code quality due to peer pressure.

However, code reviews can be one of the most **difficult and time-consuming parts** of the software development process.

We’ve all been there. You might have waited days until your code was reviewed. Once it was reviewed you started a ping pong with the reviewer of resubmitting your pull request. All the sudden you’re spending weeks going back and forth. You are context switching between new features and old commits that still need polishing.

> If the code review process is not planned right, it could have more cost than value.

This is why it’s extremely important to structure and build a well-defined process for code reviews within your engineering team.

In general, you’ll need to have in place well-defined guidelines for both the reviewer and reviewee, prior to creating a pull request and while it’s being reviewed. More specifically:

#### Define perquisites for creating pull requests.

I’ve found that the following greatly reduces friction:

1. Make sure code compiles successfully.
2. Read and annotate your code.
3. Build and run tests that validate the scope of your code.
4. All code in codebase should be tested.
5. Link relevant tickets/items in your task management tool (JIRA for example) to your pull request.
6. Do not assign a reviewer until you’ve finalized the above.

#### Define reviewee responsibilities

While the reviewer is last in the chain of merging your PR, the better it’s handed over by the reviewee, the fewer risks you’ll run into in the long term. Here are some guidelines that can greatly help:

1. **Communicate with your reviewer** — Give your reviewers background about your task. Since most of us pull request authors have likely been reviewers already, simply put yourself in the shoes of the reviewer and ask, “How could this be easier for me?”
2. **Make smaller pull requests** — Making smaller pull requests is the best way to speed up your review time. Keep your pull requests small so that you can iterate more quickly and accurately. In general, smaller code changes are also easier to test and verify as stable. When a pull request is small, it’s easier for the reviewers to understand the context and reason with the logic.
3. **Avoid changes during the code review** — Major changes in the middle of code review basically resets the entire review process. If you need to make major changes after submitting a review, you may want to ship your existing review and follow-up with additional changes. If you need to make major changes after starting the code review process, make sure to communicate this to the reviewer as early in the process as possible.
4. **Respond to all actionable code review feedback** — Even if you don’t implement their feedback, respond to it and explain your reasoning. If there’s something you don’t understand, ask questions inside or outside the code review.
5. **Code reviews are discussions, not dictation** — You can think of most code review feedback as a suggestion more than an order. It’s fine to disagree with a reviewer’s feedback but you need to explain why and give them an opportunity to respond.

#### Define reviewer responsibilities

Since the reviewer is last in the chain before merging the code, a great part of the responsibility is on him for reducing errors. The reviewer should:

1. Be aware to the task description and requirements.
2. Make sure to completely understand the code.
3. Evaluate all the architecture tradeoffs.
4. Divide your comments into 3 categories: Critical, Optional and Positive. The first are comments that the developer must accept to change, and the latter being comments that let the developer know your appreciation for nice pieces of code.

Also, avoid many comments and use Github review instead (see example below).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dk9zXJdZRlzpapQ_ERyKwA.png)

When you have several comments, you should use the review option in Github, instead of comment each of them separately, and notify the developer (PR owner) when you’re done.

Finally, I’ve found that asking the following questions is a great tool for an overall better and easier reviewing process:

* Am I having difficulty in understanding this code?
* Is there any complexity in the code which could be reduced by refactoring?
* Is the code well organized in a package structure which makes sense?
* Are the class names intuitive and is it obvious what they do?
* Are there any classes which are notably large?
* Are there any particularly long methods?
* Do all the method names seem clear and intuitive?
* Is the code well documented?
* Is the code well tested?
* Are there ways in which this code could be made more efficient?
* Does the code meet our teams styling standards?

There are various effective and different code review practices that vary based on team’s needs. So assume this is my personal opinion and that there are other ways that might work for your team. In the end, building such a sensitive process should be subjective to your companies goals, team’s culture and overall R&D structure.

If you have any questions or feedback for improving these guidelines, please feel free to add a comment below!


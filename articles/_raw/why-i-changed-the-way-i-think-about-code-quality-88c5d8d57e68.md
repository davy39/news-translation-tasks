---
title: Why I changed the way I think about Code Quality
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-19T23:18:01.000Z'
originalURL: https://freecodecamp.org/news/why-i-changed-the-way-i-think-about-code-quality-88c5d8d57e68
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mxwl0_gdFfhnpXeh8RozCA.jpeg
tags:
- name: Code Quality
  slug: code-quality
- name: code review
  slug: code-review
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By John Cobb

  What do you think about when you think about code quality?

  Is it consistency? Enforcing a set of standards and best practices on your code
  through linter rules and formatters? How about ensuring your code has tests that
  run automatically...'
---

By John Cobb

What do you think about when you think about code quality?

Is it consistency? Enforcing a set of standards and best practices on your code through linter rules and formatters? How about ensuring your code has tests that run automatically during your build process? What about pull requests and code reviews — protecting your master branch from direct commits and having peers review your code?

They’re some of the things that come to mind for me. Automated processes and manual checks. Smart and efficient. Yet, while they’re all useful, they really only address half of the problem.

### We can’t automate everything

Automation is crucial for maintaining code quality. Static analysis of your syntax with a linter and automated testing should be mandatory. But I can write code that passes all the automated processes without any guarantee to its actual quality.

Does the code follow established patterns? Does it use existing modules, or does it duplicate code? Is everything named sensibly? Is the code in the right place in the codebase? Will this change have wider, unintended, implications? Does this code actually address/solve what it intends to? Does it even _work_?

Automated processes can’t answer those questions for you (yet). If you (or another human being) aren’t asking these questions of your code, then you’re probably not shipping _quality_ code. That’s why we have code reviews.

#### A good code review should be about more than the code

Of course a code review should be about the code (it’s right there in the name after all). But it should also be about the broader questions posed above, and also about the end product.

I’ve noticed a tendency for developers to treat code reviews as perfunctory. A rudimentary check of the modified code. A comment on any obvious mistakes (or just picking a nit or two to look busy).

Five minutes, job done. _Looks good to me_.

But, code that doesn’t address the requirements of the task is not quality code. Code that produces console errors or visual bugs in the device/browser is not quality code. Neither of those things can be picked up in a perfunctory code review. You can’t adequately review code unless you _actually run it_.

I propose that a good code review _should_ involve at minimum:

* Pulling down the branch to a local environment.
* Building the project (and checking that the linter and tests all pass).
* Checking that the code runs error free in the target browsers/devices.
* Checking that the completed work matches the requirements of the task.

If there are any issues with any of those steps the pull request should be rejected. Do not pass Go. Do not collect $200. Do not merge to master.

Reviewers should also use the code review as an opportunity to ask questions. If you don’t understand the code, then you shouldn’t approve the pull request. Don’t assume that the author knows more than you do — if it doesn’t make sense to you, ask for clarification.

The reviewer has equal responsibility with the author for the quality of the code. This is a mindset that is essential for maintaining code quality.

Comprehensive code reviews go a long way to helping ensure code quality. But there are steps you can take before you even open a pull request. Small things you can do that will help enhance the quality of your code, and reduce the effort required to review it.

### Double check your own work for completeness

I have an annoying habit. When I finish writing the last lines of code for a task, I mentally check the task off as _complete_.

If I were to listen to that impatient voice in my head, I’d submit my pull request right then. But that code would likely contain many, or all, of the following:

* Missed requirements.
* Missing test cases.
* Superfluous, unused or draft code.
* Not enough code comments.
* Visual bugs in some browsers/devices.

If any of those things are true about your code, then your code is not complete. If any of those things end up in the master branch, then you have degraded the quality of the codebase.

The main point here is this: code quality _starts_ with the code author. You shouldn’t rely on automated tasks, a code review, quality assurance or user acceptance testing to catch your mistakes.

Double checking work for completeness is an essential first step toward code quality. It’s the easiest step to take, but also the easiest one to ignore.

You should only open up a pull request when you are certain your code is complete.

### Perform a self review of your branch

I’m always surprised at how many issues — or opportunities to refine a solution — I can find in my own code. Issues and opportunities that only become visible to me when I step back and view my changes in isolation.

You can review your work and apply your own feedback before assigning a team member to review your work. You can also use this opportunity to leave comments on the pull request to clarify anything for the reviewer.

Taking time to ensure your work is complete, to correct obvious mistakes, or assess your solution, will enhance the quality of your code. It also reduces the effort required to review it.

It might also save you some embarrassment. I know it has for me.

### Ensuring code quality should be an inherent requirement of every development task

You may be thinking that this approach adds time to the length of a task. And you’re right, it does. But that isn’t a bad thing.

Efficiency is important, but laziness and apathy is harmful. Apathy leads to a bloated, inconsistent code base. Laziness creates a growing backlog of bad technical debt. We can’t be passive and maintain code quality. It requires time and effort.

Changing the culture around code quality can be hard. Project managers and product owners generally aren’t concerned about code quality — they have their own concerns. Requesting extra time for code quality processes can sometime fall on deaf ears. However, maintaining code quality shouldn’t be thought of as something _extra —_ it should be an inherent requirement of every task.

As developers, if we don’t change the way _we_ think about code quality, we can’t expect anyone else to.

Nothing I’ve talked about here is particularly groundbreaking, nor is it prescriptive. Not every team, workplace, or project is the same, and some of the above may not be applicable to you.

I do believe there is often a gap between the way developers think about code quality, and the actual actions taken to address it. If you’ve found that too, then hopefully there is something you can take away from this article — or perhaps you’ve already taken a different approach to addressing it. I’d love to hear your suggestions in the comments.

Thanks for reading!


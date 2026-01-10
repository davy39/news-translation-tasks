---
title: Create a sane office environment with these effective code review guidelines
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-10T19:49:05.000Z'
originalURL: https://freecodecamp.org/news/create-a-sane-office-environment-with-these-effective-code-review-guidelines-1d99ae2bdd47
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tmWNK9yElTaVKFqq_5C6qQ.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sandor Dargo

  In my new team, we are working on several guidelines, rules and process improvements.
  Why do we think these are so important? If things are well-documented, it’s easier
  for a newcomer to start delivering value. It reduces the possibil...'
---

By Sandor Dargo

In my new team, we are working on several guidelines, rules and process improvements. Why do we think these are so important? If things are well-documented, it’s easier for a newcomer to start delivering value. It reduces the possibilities of errors for everyone. It removes lots of possibilities for arguments. And we all know that [one cannot win an argument](http://lesswrong.com/lw/j6o/according_to_dale_carnegie_you_cant_win_an), so we should avoid them at all costs.

For a more detail vision about the importance of guidelines, please check out [this article](https://medium.com/@SandorDargo/zuckerbergs-gray-t-shirt-and-coding-guidelines-caef9079ba7e). I’ll revisit it soon, by the way.

This time, I’m going to focus on code reviews and on the corresponding guidelines.

### The aim of the code review

Reviewing a pull request is an important and sensitive task. In my opinion, it is at least as important as writing the code. Besides, reviewing someone else’s code is a not just a technical task, it’s also a human one. That gives most of its delicateness.

So let me start with the most important rule that you should always have in mind whenever you start to review a pull request or whenever you open up a review you received:

**No comment should be personal. No comment should be made about the author or the reviewer. A review must always be about the code!**

The aim of a code review is to make the code better, to detect bugs before merging and delivering, and to improve maintainability of a given code base.

![Image](https://cdn-media-1.freecodecamp.org/images/iwBJmQjVw5bLuAarwiexTTHpdZWktPyW-WEx)
_Code must be rigorously checked_

### Items to be checked in a code review

Reviewing code is difficult , and it’s a very broad task. According to my bosses, I’m considered a good code reviewer. But still, I think my effectiveness could be improved a lot. I think that following checklists, in most cases, can be a huge help.

Now, obviously, some of those checklists and/or tasks will be language-specific. However, reviews are helped by the same concepts existing in multiple code languages.

These lists are mostly here to give you some ideas, as they are far from complete. Feel free to use them, update them, personalize them, or just let them inspire you to come up with completely new ones.

I think that one reviewer shouldn’t use them all, but maybe just a few. But if you have separate checklists, it’s easy to share the tasks.

Not all the checklists are there to be used for all code reviews. If the pull request is a really small bugfix, just correcting an off-by-one in a condition, it will not require checking the design of the whole domain.

### Types of checklists

#### Full process checklist

This one focuses on some foundational characteristics of a pull request. Make sure that the new commits don’t break the compilation or the tests. Your Continuous Integration pipeline should take care of this, but in case not — don’t forget about it. Otherwise, check these:

* Are new unit/regression tests added?
* Are there new compiler warnings?
* Does the change functionally make sense?
* Are there a lot of dependencies?
* Are the commit messages clean?

#### SOLID (object-oriented design) principles checklist

In order to verify the sanity of the design, it’s worth going through the SOLID principles. It’s useful to expand these items into sublists, which helps to verify each principle:

* Single responsibility principles
* Open/closed principle
* Liskov substitution principle
* Interface segregation principle
* Dependency inversion principle

#### Security checklist

Your application might or might not be security-critical. As soon as it’s hacked once or it fails because of some messy input, it will become one. This checklist should be heavily language dependent (I’m giving you one for C++). The list is extracted mainly from this [talk on secure programming practices at the NDC Security Conference at 2018](https://www.youtube.com/watch?v=Jh0G_A7iRac)

* Is external input handled properly?
* Are C-style interfaces used?
* Is the `new` operator superfluously used instead of stack allocation?
* Are there lots of (error-prone) size calculations?
* Are pointers used a lot?
* Are shared_ptrs used a lot?
* Are there any threads?

#### Testing best practices checklist

I hope we all agree that testing is part of a developer’s job. If we had a discussion on testing, it would be about the different ways of doing it, not whether we should do it or not.

The bad news is that there is no one way fits for all. Still, I’d advise you to follow the cycle of Test Driven Development. The good news is that, on a project, there is at least a common understanding about what should be done.

If there is none, step in and advocate for testing, gather articles and studies, and convince the team. You’ll be much more respected.

Here a few points to clarify in regards to the testing part:

* Are there enough unit tests?
* Are there enough non-regression tests?
* Do tests test one thing?
* Do they have assertions? (A test might have multiple assertions, still logically they assert one thing)
* Are they readable?
* How are dates used? (Fixed vs. generated)

#### Code readability checklist

We — developers — are all authors. If we do an impeccable job, [our code will read like a prose](https://www.goodreads.com/quotes/7029841-clean-code-is-simple-and-direct-clean-code-reads-like). I’m not saying that you should always reach this goal for the whole codebase, but you should aim for that.

The code reviewer has a huge responsibility here. If you are reading a pull request, please think about the following questions:

* Are names meaningful?
* Are classes/functions small enough?
* Does the code “read like a prose”?
* Is the code well-formatted?
* Is there duplicated code?

#### Resource handling checklist, a.k.a. [RAII](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization)

This last one is rather language-specific. It’s not only for C++, but mostly. If you are a C++ developer and you’ve ever fought against dangling pointers, memory leaks, and nasty core dumps, then you know what I mean.

It can be really difficult for a non-expert to spot these issues. But following a helpful checklist can help you both in pointing out the problematic lines and in developing the RAII expertise.

* Is object ownership clarified?
* Are objects properly destroyed/ is the memory correctly deallocated?
* Are new fields properly handled?
* Are Fields correctly initialized in the constructors?
* Are comparison operators updated?

![Image](https://cdn-media-1.freecodecamp.org/images/g5hd9nbvxcs2wVXZN-AmvzcLiYZeqQ9xUq2Q)
_The review is for improving quality and educating each other_

### The code of conduct for code reviewers

As stated before, commenting on someone else’s code is also a human task, so be nice to your fellow developers. Here are some pieces of advice. Following them will markedly decrease the chance that developers will cry or throw chairs at each other in the office. (But I have never seen the latter — so far…)

#### Don’ts

* Don’t refer to personal traits and don’t judge (for instance, refrain from saying you/your code is stupid…)
* Don’t make demands (at least put a please in there and explain why you’re asking for a change)
* Don’t be sarcastic, even if you are buddies. Other reviewers/readers might find some comments inappropriate
* Never say never, nor always. There will always be exceptions. So treat this rule with care…
* Avoid selective ownership of the code (that is, don’t use “mine,” “not mine,” “yours”…)

#### Dos

* Ask questions.
* Ask for clarification.
* Be explicit. Remember people don’t always understand your intentions online.
* Seek to understand the author’s perspective.
* If discussions turn too philosophical or academic, move the discussion offline
* Identify ways to simplify the code while still solving the problem.
* Communicate which ideas you feel strongly about and which you don’t. If you just express your preference, say that it’s only your preference.
* Educate. If you suggest something, share proofs for why it’s better (like articles, studies, books, and so on).

![Image](https://cdn-media-1.freecodecamp.org/images/f1wn8KRB4zrj1SyBz3iMmvkGrv66l7hjr3Bb)
_We developers are all authors_

### Rules for the authors

* Be humble and honest about the submitted code. Mistakes happen every day, and the process is there to support you.
* Remember that you shouldn’t take it personally. The review is of the code, not of you.
* Explain why the code exists.
* Follow guidelines.
* Seek to understand the reviewer’s perspective.
* Be grateful for alternative suggestions and keep the discussion technical. Try to learn from different perspectives.

### Call to action

* Make thorough code reviews. You will learn a lot, just like your fellow developers.
* Emphasize the importance of proper code reviews in your teams, and if necessary, educate your colleagues how to review code.
* Check out and star [this repository](https://github.com/sandordargo/code-review-guidelines) where I’ve collected some checklists and ideas. Feel free to contribute, and add what you have found important!

_This article has been originally published on [my blog](http://sandordargo.com/blog/2018/03/28/codereview-guidelines)._


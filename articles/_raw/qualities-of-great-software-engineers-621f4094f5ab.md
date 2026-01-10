---
title: The qualities that make a great software engineer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-23T20:25:27.000Z'
originalURL: https://freecodecamp.org/news/qualities-of-great-software-engineers-621f4094f5ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Xv37PaIjTqZzoWQUk-4arw.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Caleb Taylor

  Over the years, I’ve noticed some common traits of people that were incredibly valuable
  to a company. These engineers were smart, but that’s not why they were great. They
  tended to consistently do certain things that many other engine...'
---

By Caleb Taylor

Over the years, I’ve noticed some common traits of people that were incredibly valuable to a company. These engineers were smart, but that’s not why they were great. They tended to consistently do certain things that many other engineers did not. I’ve captured some of these qualities and boiled them down into concepts that any engineer could use.

> **_Disclaimer:_** _These are not always easy things to do. I have personally fallen short of each quality at some point in my career. I consider these “guiding principles” for anyone who is looking to be a great engineer, but it’s not a comprehensive list. Your definition of a “great” engineer may differ from mine._

### Train To Be A Firefighter

When I was a young, fresh-faced engineer, I got my first valuable lesson from my manager. He said,

> “If you want to be valuable to your company, be the person that runs toward fires.”

He wasn’t encouraging me to go throw myself in a fire (although I’m sure I deserved that at times), but rather to be the engineer who was willing — and capable — to tackle the big problems.

The “fires” can be anything from a nasty production bug, to a daunting refactor of a major service. Not everyone can put out these fires. A willingness to tackle hard issues is the first step, but it’s not enough. You have to actually be capable of putting out the fire.

Preparing for these big moments isn’t always easy. You must dedicate yourself to understanding your system’s architecture and design. The more complicated a system, the more time it will take.

There are a couple of ways I’ve found that help prepare me to fight fires:

* Creating an HLD ([High-level design](https://en.wikipedia.org/wiki/High-level_design)) for your app/service
* Documenting complicated pieces of your code
* Debugging common flows through your code line-by-line
* Taking time to dig into any code you run across that you don’t understand
* Research technologies that your team uses and become an expert

When you work on individual tasks, be on the lookout for anything you don’t understand. **Don’t accept things that _“just work”_**_._ Every time you touch your code, you have a chance to build your understanding. That’s why training to be a “fireman” is so hard. It can be a tedious, daily effort to be ready for fires.

Great engineers are the people that consistently do these sort of things. They are willing to jump on issues they don’t know how to solve. They tend to dig deeper than the average engineer because they want to truly understand things. This has nothing to do with intelligence. It’s a mindset.

**Takeaway:** Dedicate yourself to acquiring a deep understanding of your application. When tough issues arise, be willing to dive in and put out the fire.

### Recognize Bottlenecks

How many times have you experienced a situation like this?

> Developer A: “I’m going to deploy the latest change, okay? Once I manually update each of the static files and remove the local configuration settings, I can upload it”.

> New Developer: “Wait, you manually edit these files each time you deploy?”

> Developer A: “Yeah, it’s a pain. We’ve also broken production a few times when we make a mistake. It’s pretty annoying.”

> New Developer: “That seems like a bad way to do deploys..”

> Developer A: “Yeah, we really should fix that.

This is unfortunately a pretty common problem for software teams. Important or common pieces of your team’s workflow are manual, fragile, and slow. Occasionally, the team will recognize that it’s a problem and fix it. At the very least, they might make a card in the backlog.

> The real problem is when nobody recognizes a bottleneck

So where do you begin looking? A good starting point is to think about automating everything. Start with the most critical tasks you perform manually. Does your team have tests that everybody manually runs for each pull request to make sure they pass? Why not hook that up to a CI server like [Jenkins](https://jenkins.io/) or [Travis CI](https://travis-ci.org/) and display the results directly in the pull request with web hooks?

Do members of your team spend time reviewing code style and formatting? Why not automatically lint your code using a Git hook on each commit with a tool like [Husky](https://github.com/typicode/husky) and [lint-staged](https://github.com/okonet/lint-staged)?

These sort of optimizations can be easy to miss. Teams accept these pain points as “the way things are”, rather than as candidates for optimization. Great engineers tend to think about these issues. They take the time to fix them, and the resulting changes are big wins for the entire team.

> _I’ve recently read [Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations-ebook/dp/B07B9F83WM)_ and found it to be a great resource. It gives insight into best engineering practices, and how they affect team performance and happiness. It can also be useful to help justify working on your team’s bottlenecks to your company’s leadership and product teams with data from many other companies.

**Takeaway:** Look for bottlenecks in your team’s development process or deploy pipeline. Make an effort to prioritize and fix the most important issues to improve your team’s quality of life.

### Don’t Blindly Follow Existing Patterns

Engineers love patterns. Thousands of books exist on the best programming patterns and how to use them. Unfortunately, not all code patterns should be reused.

Occasionally, I’ve reviewed a pull request and found an odd or poorly-written section of code. When I ask why it was written this way, the answer is usually the same: “That’s how it was done before. I just copied it from somewhere else”.

> Breaking old patterns is the first step of establishing new ones

The tendency for developers to copy existing code is one of the biggest reasons for tech debt. It’s easy to allow these changes through because it looks like other code in production.

Great engineers are very careful about reusing existing code. This applies to both writing and reviewing code. They tend to ask the questions:

* Is the copied code the best way to solve the problem?
* If it’s similar to an existing piece of code, can we combine into a single module to reduce duplication?
* Are there any logic bugs due to subtle differences between the new and existing code?
* Does this code fit with my team’s latest standards and design discussions?

These principles also apply to making updates to older pieces of code. It’s very easy to sneak in a code change to a outdated or poorly-written section of code without fixing anything, but **great engineers rarely do this**. They tend to embrace the concept of [continuous refactoring](https://martinfowler.com/bliki/OpportunisticRefactoring.html).

This doesn’t mean that each code update results in a massive refactor. The improvements can be (and usually are) a variety of simple things:

* Improving variable or function names
* Breaking out a large, complex function into smaller ones
* Abstracting out logic copied in several places into a shared component

Great engineers are constantly thinking about ways to improve code, and almost always leave the code in a better state than they found it.

> _I’ve recently read the book [Refactoring: Improving the Design of Existing Code](https://martinfowler.com/books/refactoring.html)_ by Martin Fowler, and found it to be a great resource on refactoring.

**Takeaway**: Constantly re-evaluate code structures, patterns, and design. Copying and pasting code is the root of all evil. Always leave code in a better state than when you found it.

### Conclusion

Any software engineer can apply these qualities to their work. It can be difficult to do consistently. Some characteristics require a willingness to go the extra mile in the many facets of your job. If you are willing to work at these qualities, you will become a better software engineer.

This short list is based upon my own experiences, but I’d love to hear what others think. What qualities do great engineers tend to have in your experience? Please let me know!


---
title: How to avoid code review pitfalls that slow your productivity down
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-06T18:36:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-code-review-pitfalls-that-slow-your-productivity-down-b7a8536c4d3b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*_9ClYv6zGLGlJJpg
tags:
- name: code review
  slug: code-review
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Michaela Greiler

  Code reviewing is an engineering practice used by many high performing teams. And
  even though this software practice has many advantages, teams doing code reviews
  also encounter quite a few code review pitfalls.

  In this article, I...'
---

By Michaela Greiler

Code reviewing is an engineering practice used by many high performing teams. And even though this software practice has many advantages, teams doing code reviews also encounter quite a few code review pitfalls.

In this article, I explain the main code review pitfalls you should be aware of to ensure code reviewing does not slow your team down. Knowing which pitfalls and problems arise can help you to ensure a productive and effective code review experience. Those findings are based on a [survey we conducted at Microsoft with over 900 participants](https://www.michaelagreiler.com/wp-content/uploads/2019/03/Code-Reviewing-in-the-Trenches-Understanding-Challenges-Best-Practices-and-Tool-Needs.pdf).

### A typical code review process

A typical tool-based code review process looks roughly like this: Once the developer has finished a piece of code, they prepare the code for being submitted for review. Then, they select reviewers who are notified about the review. The reviewers then review the code and give comments. The author of the code works on those comments and improves and changes the code accordingly. Once everybody is satisfied, or an agreement is reached, the code can be checked into the code base.

In another post, I described how [a typical code review process looks like at Microsoft.](https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/)

### Code reviewing isn’t always a smooth process

These steps read like a smooth process. But, like everything, in practice, things tend to be more complicated than anticipated. During the code review process there a quite a few pitfalls that can reduce the positive experience with code reviews for the whole team. If not done correctly, code reviewing can also take its tolls on the whole team’s productivity. So, let’s have a look at the difficulties and pitfalls of code reviews.

The two main types of code review pitfalls are about the time spent on code reviews, and the value code reviews provide.

[Be aware of code review pitfalls. Otherwise, code reviews can slow your team down. Click To Tweet](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=Be%20aware%20of%20code%20review%20pitfalls.%20Otherwise%2C%20code%20reviews%20can%20slow%20your%20team%20down.%20&via=mgreiler&related=mgreiler)

### Waiting for code review feedback is a pain

One of the main pitfalls code authors face is to receive feedback in a timely manner. Waiting for the comments to come in and not being able to work on the code in the meanwhile can be a huge problem. Even though developers can pick up other tasks to work on, if the code review takes too long, it impacts the developer’s productivity and also the developer’s satisfaction.

But, why does the code review feedback take so long?

### Developers have to juggle several responsibilities

Well, code reviewing is not the only task the code reviewer has to perform. On the contrary, code reviewing — even though it can take a significant amount of time of a developer’s day-to-day work — is only one part of the responsibilities and tasks of a developer. So, it is very likely that the code reviewer is engaged in other activities and has to stop or finish those first before looking at the code review.

If the timing is not ideal, and especially if the code reviewer hasn’t anticipated this change coming along, chances are, it takes a while before they look at the review. Remote teams also have to be aware of time differences. Otherwise, code reviews might even take longer.

### Developers face problems if code reviews are not counted as actual work

Time constraints are real, and they affect both, the code reviewer and the author of the code. Doing a proper code review takes time. If teams want developers to do code reviews but do not value or count the time developers spend on code reviews, this becomes a real problem.

![Image](https://cdn-media-1.freecodecamp.org/images/iO9crhcrMsfcZYZnlcTayHSfN647zOBnmRQs)
_You have to value and plan for the time spent doing code reviews.<br>Photo by [Unsplash](https://unsplash.com/photos/vcPtHBqHnKk?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">freestocks.org</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

[You can’t expect quality code reviews if you don’t value the time a developer spends on them. Click To Tweet](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=You%20can%27t%20expect%20quality%20code%20reviews%2C%20if%20you%20don%27t%20value%20the%20time%20a%20developer%20spends%20on%20them.&via=mgreiler&related=mgreiler)

### Not rewarding code reviewing efforts and performance

It does not help to claim to value code reviews if you do not reward the effort developers spend on this task. Many companies focus on rewarding developers for the amount of code they write or the features they develop. This decreases the motivation and the ability of developers to do a good job helping each other (which includes code reviewing). Code review effort and performance should be a cornerstone for performance evaluation or promotion decisions.

[If you want your team to do code reviews well, reward them for their work. Click To Tweet](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=If%20you%20want%20your%20team%20to%20do%20code%20reviews%20well%2C%20reward%20them%20for%20their%20work.%20&via=mgreiler&related=mgreiler)

### Social factors and team dynamics

But waiting on a code review had not always to do with the lack of time or missing reward system. Due to its social character, delayed reviews can be due to insecurities or team dynamics. Especially if the code review is overwhelming, or if the reviewer is new to the code, doing a code review can be overwhelming:

> _I’m expected to participate, but I’m not quite sure how. I’ll wait until someone else starts. — study participant_

### Large reviews are hard to review

Another significant code review pitfall is large reviews. Imagine you are the reviewer, and you just got this review. You think, well, I am quickly going to look at that, but once you open the review, you see this large code change. Several files have been changed, and all changes tangle throughout the code base. What’s your first reaction?

Probably: holy cow!

That’s right. That is exactly what we saw when analyzing thousands of code reviews. Not only does review time increase with the size of the code change, but also feedback quality decreases. Well, that’s probably understandable.

> _10 lines of code = 10 issues._

> _500 lines of code = “looks fine.”_

> _Code reviews._

> _— I Am Devloper (@iamdevloper) [November 5, 2013](https://twitter.com/iamdevloper/status/397664295875805184?ref_src=twsrc%5Etfw)_

Large code changes are just incredibly difficult to review. If, in addition, the code reviewer is not that familiar with the part of the code base the change took place in, reviewing can quickly become a nightmare.

[Large code reviews are hard to review. The quality of the review decreases with the size of the change, thus limiting the value teams get out of from code reviews. Click To Tweet](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=Large%20code%20reviews%20are%20hard%20to%20review.%20The%20quality%20of%20the%20review%20decreases%20with%20the%20size%20of%20the%20change%2C%20thus%20limiting%20the%20value%20teams%20get%20out%20of%20from%20code%20reviews.%20&via=mgreiler&related=mgreiler)

### Understanding code changes needs some guidance

Understanding code changes, and especially the motivation for a code change, is another code review pitfall many reviewers face. If there is no description explaining the purpose of the change, code reviewing becomes much harder. We saw in the study that if the code reviewer does not understand the code change, or if she is overwhelmed by the amount of change, she cannot give insightful feedback.

> _It’s just this big incomprehensible mess. Then you can’t add any value because they are just going to explain it to you and you’re going to parrot back what they say._

> _— interviewed developer13_

### Not getting valuable feedback decreases the developers’ benefit from and motivation for code reviews

Without doubt, spending the time on code reviews and not getting useful feedback back is a problem. Even though the team might still benefit from the knowledge transfer, the developer’s motivation to do code reviews and the benefits from code reviews decrease when they do not get valuable feedback.

There are several reasons why reviewers do not or can’t give insightful feedback. It can be that the code reviewer did not have the right expertise. Another common reason is that the reviewer did not have enough time to look thoroughly through the change.

Maybe the code reviewer does not understand the code. It can also be that the code reviewer does not know what issues to look for. [Understanding what makes for valuable code review feedback](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/boosting-code-reviews-useful-comments) and implementing best practices mitigates this pitfall.

### Once the main discussion is about styling, you need to act

Another problem that can happen during a code review is called bikeshedding. Bikeshedding means that developers focus on smaller issues and start disputing minor issues and overlook the serious ones.

The reasons for that are manifold. Common behind the scenes challenges that lead to bikeshedding is that developers do not understand the code change or that they do not have enough time for the code reviews. Sometimes bikeshedding can be a sign that there are issues with the team dynamics.

[If people dispute about minor issues during code reviews, you have to take a look at the underlying issue. Time pressure, too large reviews, rivalry? Click To Tweet](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-review-pitfalls-slow-down/&text=If%20people%20dispute%20about%20minor%20issues%20during%20code%20reviews%2C%20you%20have%20to%20take%20a%20look%20at%20the%20underlying%20issue.%20Time%20pressure%2C%20too%20large%20reviews%2C%20rivalry%3F%20&via=mgreiler&related=mgreiler)

### Reaching consensus might need a face-to-face discussion

Sometimes it can happen that it is hard to reach a consensus. This can occur between code reviewer and code author, or also between several code reviewers directly. Such situations must be handled carefully as team dynamics are closely connected to these happenings. Communication via tools and in written form can aggravate this problem. If there seems to be any tension, or contentious issues to discuss, switching to face-to-face (either in person or via a video call) might be a good idea.

### The benefits of code review outweigh the effort

I hope this list of code review pitfalls did not change your mind about code reviews. Because, the good news is that if you are aware of the code review pitfalls and counteract them, code reviews are a very beneficial engineering technique. And, there are even more proven ways to work effectively with code reviews.

### Code review best practices

In the next blog post in [this code review series](https://www.michaelagreiler.com/code-review-blog-post-series/), I show best practices to help to minimize the code review pitfalls and challenges and ensure your team gets the best out of the code review practice. So keep on reading. To be notified when I publish the next post, follow me on [twitter](https://twitter.com/mgreiler).

I prepared an exclusive Code Review e-Book for my newsletter subscribers. So make sure [you subscribe to my email list](https://www.michaelagreiler.com/code-review-e-book/) and secure your Code Review e-Book including a handy cheat sheet of code review best practices.

_Originally published at [https://www.michaelagreiler.com](https://www.michaelagreiler.com/code-review-pitfalls-slow-down/) on April 6, 2019._


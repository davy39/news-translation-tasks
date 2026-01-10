---
title: How Google Does Code Reviews – Quality Assurance Tips from Google's Documentation
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-01-14T18:09:46.000Z'
originalURL: https://freecodecamp.org/news/what-google-taught-me-about-code-reviews
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Google.png
tags:
- name: code review
  slug: code-review
- name: Google
  slug: google
- name: QA
  slug: qa
- name: Quality Assurance
  slug: quality-assurance
seo_title: null
seo_desc: "A code review, sometimes called code Quality Assurance, is the practice\
  \ of having other people check your code after you write it. \nCode reviews bring\
  \ many benefits to the process of writing and delivering software:\n\nEnsures consistency\
  \ through your ..."
---

A code review, sometimes called code Quality Assurance, is the practice of having other people check your code after you write it. 

Code reviews bring many benefits to the process of writing and delivering software:

* Ensures consistency through your codebase.
* Teaches all members of the review (helps knowledge transfer).
* Builds contextual awareness regarding what might affect other parts of the team
* Helps avoid breaking builds
* Casts fresh eyes over a code change to search for optimisations and simplifications in the change.
* Promotes quality and helps make sure no one forgot or missed anything.

Google has 1,918 repositories on [their GitHub](https://github.com/google) across multiple languages, and even more that aren't open source.

One of their codebases is shared by over 25,000 Googlers, and typically has [40,000 commits](https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext) daily (16,000 human changes, and 24,000 by automated systems). Each day it has to serve around 800,000 queries per second during peak times.

Google has published their engineering practices, so let's see how they review code at their scale, with so many commits a day.

Google refers to changes in their codebases as **CLs** standing for change lists. It's just a unit of work / piece of code going through review. 

# How to Prepare for Code Reviews

Firstly, before you even think about the code review process, try and focus on **who** will do the review. Try to pick a subject matter expert. Pick someone who is familiar with this codebase or area of the codebase. 

Sometimes this may even mean having different people review different parts of the code. But less [than 25% of code review's at Google have more than one reviewer.](https://sback.it/publications/icse2018seip.pdf)

Getting someone to respond in a timely manner is also important. To avoid bottle necks and overloading individuals, just CC reviewers onto the change to review it at their convenience if they want to.

# How to Run Fast Code Reviews

Code reviews should be completed quickly. The **maximum** length of time for a review should be one business day.

Why the urgency? I've personally had QA's sometimes take weeks or longer.

* **It becomes a blocker.** Although the author of the code moves onto new work, new changes start to form a back log, and the delays can build up to weeks or months.
* **Developers feel frustrated.** If the reviewer asks for major changes but only responds every 3 days, it is frustrating for the developer working on that change. But with quick responses, whenever you require explanation of exactly what you need to do, the frustration fades away.
* **Code quality can degrade.** If your reviews are always slow, developers are less likely to do code clean ups, refactoring work or general code improvement ("If my reviewer won't reply for 4 days what's even the point?"), and the code quality submitted in the reviews is more likely to go down.

The main reason code reviews can be fast is because they're small. Rather than sending a 1,000 line CL, they're separated into multiple CL's – pushing 10 smaller changes of 100 lines for example.

Google also has emergencies where code changes have to be made quickly to resolve major problems in production. In these cases, code quality is relaxed. This review should immediately become the reviewers first priority. There are some examples of emergencies Google has faced [here](https://www.freecodecamp.org/news/what-is-a-software-post-mortem/) if you're curious.

## Google's Code Review Standards

The key rule Google emphasizes is:

**Reviewers should generally approve a change once it definitely improves the overall code health, even if it isn't perfect.**

The key point Google seem to be making is that perfect code doesn't exist. If it makes it **better**, that is enough. 

It's definitely a balancing act between something being better, and **how** much better it could be. If you could add more feedback to make significant improvements, there may need to be more work done on the code.

## What Googlers Look for in Code Reviews

When doing code reviews, Google focuses on these elements according to their [engineering practices documentation](https://google.github.io/eng-practices/review/reviewer/looking-for.html):

> **Design**: Is the code well-designed and appropriate for your system? Does this change belong in your codebase, or in a library? Does it integrate well with the rest of your system?  
>   
> **Functionality**: Does the code behave as the author likely intended? Is the way the code behaves good for its users? Mostly, we expect developers to test CLs well-enough that they work correctly by the time they get to code review.   
>   
> **Complexity**: Could the code be made simpler? Would another developer be able to easily understand and use this code when they come across it in the future? Is it over-engineered for its current use case?  
>   
> **Tests**: Does the code have correct and well-designed automated tests? Will the tests actually fail when the code is broken? Will they start producing false positives? Does each test make simple and useful assertions?  
>   
> **Naming**: Did the developer choose clear names for variables, classes, methods, etc.?  
>   
> **Comments**: Are the comments clear and useful? Ensure where sensible comments explain **why** something is being done, rather than how.  
>   
> **Style & Consistency**: Does the code follow our [style guides](http://google.github.io/styleguide/)?  
>   
> **Documentation**: Did the developer also update relevant documentation?

Google has style guides for multiple languages like [C++](https://google.github.io/styleguide/cppguide.html), [Swift](https://google.github.io/swift/), [HTML/CSS](https://google.github.io/styleguide/htmlcssguide.html), [Lisp](https://google.github.io/styleguide/lispguide.xml), [JavaScript](https://google.github.io/styleguide/jsguide.html) and [more.](https://google.github.io/styleguide/)

Having a document that everyone can refer to helps standardise the code. It also helps clarify what the expectations are in the review process.

## How Googlers Review Code

There is a three-stage process for code review in Google's engineering practices. Here's a list of things you'd need to cover if you were to review:

1. Get a high level overview of the change
2. Examine the main parts of the change
3. Look through the rest of the code, in a sensible order

Let's go over each step in more detail.

## 1. Get a High Level Overview of the Code Change

Look at the code change's description/summary. Does it all make sense? For example, if someone is changing a codebase that is being deleted next week, push back on the change _courteously,_ and explain why the change doesn't look needed anymore. 

It's inefficient if people are spending time on work that isn't actually needed, so have a look at your development life cycle and see why this might be happening. The earlier you can catch these issues the better.

In order to get a high level overview of the code, you may want to briefly scan the code components to see how it all works together. 

If you see a serious architectural problem or something majorly wrong, you should share your observations immediately at this stage. Even if you don't have time to review every single other element of the review. Reviewing the rest may well even end up being a waste of time if the architectural problems are severe enough. 

Aside from this, there are 2 major reasons why you should send your review comments immediately: 

* Googlers will often email a change, and then immediately start new work based on that change. If the change in review need serious adjustments, they may be building on something that needs to be significantly changed.
* Big changes to the CL may take a while to finish. Developers all have deadlines and it's courteous to try and help them meet them by letting them start rework as soon as possible.

## 2. Examine the Main Parts of the Code Change

Once you have had an overview, review the "main" parts of the change.

Find the file or files that are central to the CL. Often, there is one file that has the largest number of changes, and it’s the major piece of the CL.

Spend most of your focus reviewing these pieces. This provides context to all the smaller pieces, and generally makes it faster to review. 

If the CL is too large for you to get a good overview and understand the flow, it's a good sign the developer should be splitting up their CL into smaller changes.

## 3. Look Through the Rest of the Code, in a Sensible Order

Once you have a good overview of the change, it's time to drill down into the details and go file by file. 

Each reviewer generally does this differently. Some go in the order that the version control presents to them and some pick a particular order. Choose what makes sense to you. It's important to just review **everything**, and miss nothing.

### Review Every Line of Code

Don't miss or skim important details. Sometimes there might be config files, or generated code you can scan briefly looking for irregularities. But your job here is to be very thorough and carefully scrutinise the code. 

Make sure you think about bugs, race conditions, alternate approaches, conciseness, readability, and so on.

If you can't understand the code, it's highly likely other developers won't be able to either, and should ask the developer to clarify it.

### Understand the Context

Often times the version control software will only show the changed lines. But it's important to read the lines before and after, or the whole file, to ensure you understand exactly what the change is doing.  

You may only see someone adding 2 more `if` blocks in a change. But if you look at the context you might see that the `if` `else` block now has 15 different `if`'s inside it. Then you can reject the code change and properly improve the code quality in this area, rather than making it worse.

Remember code degradation happens slowly, with every change that goes in. Our main aim is to ensure the quality trends consistently up, and we never go backwards.

## **How Googlers Write Code Feedback** 

Google has some specific sections covering how to do [code reviews courteously, and respectfully](https://chromium.googlesource.com/chromium/src/+/master/docs/cr_respect.md). This isn't in opposition to being clear and as helpful as you can to the developer. The golden rule here is to make comments about the _code_ and not the developer. 

## What to Do:

#### 

> **Ask for the why:** If it is unclear why the author is doing things a certain way, feel free to ask why they made a particular change. Not knowing is OK, and asking “Why” leaves a written record that will help answer this question in the future. (And sometimes, “I'm curious, why did you decide to do it that way?” can help the author to rethink their decision.)  
>   
> **Find an end:** If you like things neat, it’s tempting to go over a code review over and over until it’s perfect, dragging it out for longer than necessary. It’s soul-deadening for the recipient, though. Keep in mind that “LGTM” does not mean “I vouch my immortal soul this will never fail”, but “looks good to me”. If it looks good, move on. (That doesn’t mean you shouldn’t be thorough. It’s a judgment call.) And if there are bigger refactorings to be done, move them to a new CL. ([Source](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/cr_respect.md))

## What Not to Do

> **Don't use extreme or very negative language:** Please don't say things like “no sane person would ever do this” or “this algorithm is terrible”, whether it’s about the change you're reviewing or about the surrounding code. While it might intimidate the reviewee into doing what you want, it’s not helpful in the long run - they will feel incapable, and there is not much info in there to help them improve. “This is a good start, but it could use some work” or “This needs some cleanup” are nicer ways of saying it. Discuss the code, not the person.  
>   
> **Don't bikeshed:** Always ask yourself if this decision _really_ matters in the long run, or if you're enforcing a subjective preference. It feels good to be right, but only one of the two participants can win that game. If it’s not important, agree to disagree, and move on. ([Source](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/cr_respect.md))

Remember code reviews can sometimes trend towards finding issues or discussions with code and not praise.

If your reviewer has addressed your comments, or they have done some optimisation or smart code you like, thank them. Say you like the approach / how they have solved an issue. 

Conversely, thank the reviewer if they thoroughly explain what they want and promptly answer your questions.

I have had some reviews where reviewers have put huge comments explaining something I misunderstood and I can still remember who it was and what they said.

## How to Handle Pushback in Code Reviews

Sometimes the developer who is receiving the review might disagree with the changes that you're proposing. Here's how to handle that.

### Consider That They Might Be Right

Sometimes the developer is closer to the code and how it works, and they may be right. If they are, move on from that discussion point and leave that code as it is.

But if they're not, or they've misunderstood something, you should insist on the change. Respond to what the developer initially challenged you on, and explain your reasoning courteously. 

Code quality improvements tend to happen in small incremental steps, and review is one way it happens. Insist on the code improvement, even if it means extra work for the developer.

### Try to Avoid "I'll fix this later..."

One of the most common issues in reviews is not that people disagree whether the code change is necessary, but rather that they want to do it under a different ticket or do it later. So if you pass this review, they assure you that they will follow up later and fix the issues.

Generally speaking, _following up later_ rarely happens. This doesn't mean there's something wrong with the developer or their work ethic. But it's easy to forget, have priorities change, or even just get lost in their queue of work. 

Insist that the work gets done now. There is no real fantastic gain to merging changes in the codebase you have to immediately fix. You are just adding technical debt that _might_ be followed up on later, or might be forgotten_._ Fixing lots of tickets later is an easy way for quality to drop.

The only exception to this is [emergencies](https://google.github.io/eng-practices/review/emergencies.html), which involve the highest priority bugs Google deals with where there is something seriously wrong. This could be services going down, or errors crashing people's pages in production.

There is naturally an eagerness to merge changes ASAP, and the review might accept slightly lower quality, with a follow up fix immediately being written. The main point is that the first change removes the emergency, and the second change fixes it _properly._

# **Conclusion**

I hope this has explained some helpful concepts Google makes use of in their code review process. I wrote this to better cement it into my own mind, and was curious about how other companies handle the QA process. 

I found that there are quite a few points that I can take away and apply to the reviews I conduct.

The document I referred to throughout this article can be found [here](https://google.github.io/eng-practices/review/reviewer/).

I share my writing on [Twitter](https://twitter.com/kealanparr) if you enjoyed this article and want to see more.


---
title: When writing code is a waste of time.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T10:37:34.000Z'
originalURL: https://freecodecamp.org/news/when-writing-code-is-a-waste-of-time-6602af8cb759
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EX0zEmU2JgcNjGoIeHEnIQ.jpeg
tags:
- name: open source
  slug: open-source
- name: Product Management
  slug: product-management
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jonathan Solórzano-Hamilton

  Knowing what not to build is the most crucial part of modern software development.

  One of the most prominent mistakes made by development teams is doing too much work.

  Last time you were in crunch mode on a project, did...'
---

By Jonathan Solórzano-Hamilton

#### Knowing what not to build is the most crucial part of modern software development.

One of the most prominent mistakes made by development teams is doing too much work.

Last time you were in crunch mode on a project, did you think “this is going great”? Crunch time is the penance we pay for the poor decisions we made earlier in the project. In particular, the decision to do too much work.

I have spent many years architecting and developing enterprise software. I cut my teeth with an internship at HP and [survived a harrowing stint at an imploding start-up](https://blog.usejournal.com/the-4-red-flags-i-missed-as-the-startup-imploded-around-me-be120dc390cb) before moving on to a more stable career track. I spent several years working at Stanford University and have since become the Assistant Director of Architecture at UCLA Research Information Systems.

In this role I lead enterprise software development efforts, particularly the implementation of micro-services, to support research administration processes. I have learned a lot, through the school of hard knocks, about what does **not** work in a collaborative software development process.

#### Avoiding work saved my bacon

Years ago I found myself [leading a 6-month rewrite of a 5-year project](https://medium.freecodecamp.org/we-fired-our-top-talent-best-decision-we-ever-made-4c0a99728fde). At the end of the six months, we would either have a successful release or the chance to iterate on our resumes.

We had two options: work ten times as fast as the previous team — which had already been putting in 70+ hour weeks — or avoid most of the work. We avoided most of the work.

![Image](https://cdn-media-1.freecodecamp.org/images/YhEt22lS0VPShY5fmOskxkyeR5FQZKuj4gG8)
_Bacon. (Photo by [Unsplash](https://unsplash.com/photos/It0bkN5ClD8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Andrew Ridley</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

We achieved this by aggressively limiting the scope. The customer, though, would only tolerate so much feature reduction. They had been waiting for five years and weren’t going to accept a skeleton of a product.

The rest of the scope restriction came from within. The team re-structured the product architecture to reuse third-party packages wherever we could. Out went the bespoke logger. Gone was the custom expression-trees framework. Goodbye, home-brew object-relational mapper. Hello, free open-source software.

I did not have to update my resume.

#### Blazing the trail ensures you will find all the pitfalls

First let’s hit the most severe problem with a complete do-it-yourself approach to application development: security. The literal definition of a pitfall is a pit which is covered to entrap the unwary.

The road to secure applications is lousy with pitfalls.

![Image](https://cdn-media-1.freecodecamp.org/images/TMsBjMFpOfXnbIjKvHZ4mE9VBMOBQ-J8rAh5)
_Here be dragons. (Photo by [Unsplash](https://unsplash.com/photos/7FLh300YONc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Orlova Maria</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

Hackers have been playing a game of cat-and-mouse with application developers since the dawn of the discipline. They have gotten very, very good at cracking security safeguards. They have built up an entire arsenal of methods, techniques, and vulnerabilities to exploit. Do you want to fight them starting from scratch?

It is **possible** that you will anticipate every single exploit an attacker could levy against your application. It is **possible** that you will keep up with the latest developments and ensure that your custom front-end security is up to par. It is **far likelier** that one day you will miss one hole and your boss shows up to set an empty cardboard box on your desk.

#### You will waste time

Setting aside application security concerns, you also do not want to waste time. Rebuilding commonplace features that are already supported by popular public packages is a complete waste. If you cannot extend these packages, you should at least fork them.

But wait, you may think. It will be a useful exercise for me to learn how to build this feature. Learning is not a waste of time!

This is only partly true. Yes, learning on the job is not a waste of **your** time. Subjecting the broader team to your half-baked, sub-par “learning implementation” of a common feature is a massive waste of **your colleagues’ time**.

It is worthwhile to invest in your own learning. Spend time at [freeCodeCamp](https://www.freecodecamp.org/) building your skills in a low-risk environment. Other online schools and [university extensions](https://bootcamp.uclaextension.edu/coding/) offer coding curriculum as well

Perhaps you only have time to learn on the job. You may feel that you must use your contributions to the team as an independent learning exercise. If so, at least abstract your attempt behind an [interface](https://guide.freecodecamp.org/java/interfaces) to make it easy to rip out and replace later.

#### Other benefits to conspicuous consumption

Consuming a free (or otherwise third-party) package offers many immediate benefits. It also pays off in the long term.

![Image](https://cdn-media-1.freecodecamp.org/images/cK6XUH9wRLhG5D1vkUQw-Rula7yuVCgrHtwx)
_Free packages. (Photo by [Unsplash](https://unsplash.com/photos/PGrp_5aJLC0?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">NeONBRAND</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

First, you will get access to more features quickly. A package that solves your immediate problem will also likely address some common, related issues. The maintainers probably ran into similar issues and expanded the package features. You can even look to these “extra” features for ideas about where to take your product.

Second, you are signing up for automatic improvements and new features as they are released. Public packages rarely stand still: their developers encounter additional needs, their community grows, their consumers have to upgrade base frameworks. These all drive the implementation of new features. They also motivate the release of updates that ensure the code stays compatible with the latest version of the underlying language or framework.

Third, if it is an open-source package, you have the opportunity to give back to the community. Become one of the maintainers. You will have a say in the direction of the package. Other maintainers may adopt your extensions as core features into the code base. As a bonus, you will gain personal exposure as a developer, and you will also have the opportunity to improve your skills by learning from your peers.

You will also incur much less [technical debt](https://guide.freecodecamp.org/agile/technical-debt/). Even the best code incurs some maintenance overhead, which will chip away at your team’s future productivity. Reducing the amount of code you write today will increase the number of features you can release tomorrow.

#### So when do you build it yourself?

Given the already-enumerated benefits, and the mitigated risks, it may seem that coding is always a waste of time. Many application features are already available in third-party packages. So what’s left for the developer to do? Wire them together?

You assuredly can create a minimum-viable product by assembling pre-built packages. It still needs at least one feature of differentiation to be viable. If that one element is compelling enough, it will pave the way for you to iterate to greatness.

![Image](https://cdn-media-1.freecodecamp.org/images/zbwe98TiVWFnA2nIy6318Ntc3xyP4G4DVKpo)
_Just guessing, but this guy probably didn’t fabricate all of that rebar. (Photo by [Unsplash](https://unsplash.com/photos/4zwozQxDbD4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Guilherme Cunha</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

I have already [written about Tesla](https://medium.freecodecamp.org/how-to-run-a-successful-development-process-even-if-youre-not-technical-185d0558c89a) in my article about sustainable development, but it’s a good analogy. The first Tesla vehicle was a completely pre-built electric car. Tesla only provided their disruptive new lithium-ion battery. The second iteration merged the electric drivetrain and bespoke Tesla battery from this car into a respected production sports car.

Now Tesla has iterated into five-door SUVs and mass-market consumer vehicles. They differentiate their current products via gull-wing doors and self-driving capability.

With each product iteration, Tesla expanded the scope of their differentiation. They identified what their customers wanted next and scaled out their development to maintain their edge.

Find your essential differentiation and build it. Craft it with the most love and care you can. The rest of the product can recycle what’s already out there until you have grown enough to broaden your value proposition.

#### Perusing packages

You have identified the product you intend to build. You have outlined its features and defined the minimum viable scope. You have identified the differentiators, so the rest is up to packages.

How do you find and identify which packages to use?

First, you will need a source. [GitHub](https://github.com/) is a popular destination for free open-source software. [Stack Overflow](https://stackoverflow.com/) has many suggestion threads, and you can ask the community for advice. These are also valuable communities to join, because they will build your public profile as a developer.

Language-specific package repositories exist as well, including [NPM](https://www.npmjs.com/) for JavaScript, [RubyGems.org](https://rubygems.org/) for Ruby and Rails, and [NuGet.org](https://www.nuget.org/) for .NET development.

Browsing the source, you will need to identify which packages will be viable for your product. The first indicator I examine is ongoing freshness. When was the last update? How many people help maintain the repository? How many of them are active?

![Image](https://cdn-media-1.freecodecamp.org/images/USnWkVVtN-bdgL2B3k12B7iCW1REEwUg7JpE)
_Mmmm. Fresh packages. (Photo by [Unsplash](https://unsplash.com/photos/vnNFWKY7Tj4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jakub Kapusnak</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

Next, you need to make sure that the license is compatible with your product. Some licenses may impose additional obligations on you as a user of the package. The MIT License and Apache License 2.0 are usually safe choices. They impose few commitments on you (but you still have to comply with the license, however minimal).

There are other considerations to selecting the right package. Is it officially supported by a company, especially a major company? These have a lower risk of falling out of maintenance. [Bootstrap](https://getbootstrap.com/) (by Twitter) and [React](https://reactjs.org/) (by Facebook) are good examples.

Is it the right size for your project? Some packages are big and unwieldy. It may take longer to learn and implement the package than to build a small custom solution.

How many users have downloaded it overall, and how many recently? These metrics provide clues to which packages the community supports, and which may be on the way out.

Is your language or platform of choice in the middle of a major release roll-out? Check and see how the repository is performing. Have the maintainers already started integration to the new version? Have they run into any roadblocks? How does support for the next version vs. the current version look?

Picking the right package is an exercise in risk analysis. You need to perform due diligence to ensure that the package will be capable of supporting your product long enough.

#### So what does this mean for you?

Be humble. Keep your team humble, too. You are not the best developers ever born. You do not have time to remake the entire world in your image and remain competitive. Even if you did, you are squandering competitive edge unless you are re-inventing with purpose.

Use packages that are already out there. Give back to the community if you can by becoming a maintainer.

Focus your efforts on the change you want to bring to your market. Create something truly novel. It will always be worth your time.

I recently had a [conversation about this topic](http://www.developingup.com/28) with Michael Miles on his excellent podcast, Developing Up. Click the link to listen!

Please ? if you enjoyed this article!


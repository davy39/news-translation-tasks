---
title: Why you should not use (long-lived) feature branches
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-30T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-not-use-feature-branches-a86950126124
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iBt55gRsIwnNX3D_9uJVTA.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: Git
  slug: git
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jean-Paul Delimat

  Isn’t the git history in the picture above nice to work with? There are probably
  many problems in that repository, but one of them is most definitely the use of
  feature branches. Let’s see how such a bad thing became such a commo...'
---

By Jean-Paul Delimat

Isn’t the git history in the picture above nice to work with? There are probably many problems in that repository, but one of them is most definitely the use of feature branches. Let’s see how such a bad thing became such a common practice.

When git came to replace SVN it brought a ridiculously easy way to create branches.

> _The idea behind git is to ease your pain as a developer working on many features at a time. Not to push branches around and tie them to the whole development process of your team._

When JIRA and others came along, companies like Atlassian started to promote the “git workflow” and feature branches heavily. The “Create branch” button appeared in your JIRA tasks and boom, feature branches were born! Atlassian tells you all about it in [this interesting article](https://www.atlassian.com/agile/software-development/branching). I like Atlassian’s products very much. Keep in mind though that their core business is tasks management for development teams. The more tangled it gets with branches and code, the better.

Ten years later, feature branching is a standard in most teams, when in fact it doesn’t bring any benefits to your bottom line: release quality software to production. Not only do feature branches provide zero benefits, they actually slow you down!

For the sake of clarity: this article assumes a feature branch will carry the whole feature you are developing and is a so-called ‘long-lived’ feature branch that will last 1 week or more. It’s not a “no branches at all” mantra.

> “The feature is ready. I just need to merge it!”

I’ve heard this way too many times. This falls in the same category as statements like “It compiles so it works”.

In practice, the merging leads to the “unpredictable release syndrome”. It can be quick or evince a major incompatibility, which needs fixing in a rush. You are either lucky or … your timeline shifts and code quality drops.

> _The real problem with feature branches is the reason they are so popular: they pump a developer’s pride and make you feel good about your work._

Your feature branch is your own perfect garden and you can keep it clean and shiny. But it is separated from the other gardens of your team. The more you work apart, the harder it is to reconcile.

I am a big fan of the management book “The goal”. It shows how over time people tend to use metrics that highlight local optimums of a process because it is more comfortable. They just lose focus on their global bottom line. The book is about a production plant, but the analogy stands. Your feature branch is a local optimum with high-quality code. It may also be so far off the main branch that it is of no use for the upcoming release.

### Trunk based development to the rescue

As the name suggests, in trunk based development the whole team pushes continuously to the main branch or use very short-lived (1 or 2 days max) branches.

Here is a [detailed description](https://trunkbaseddevelopment.com/) of the idea. I have no affiliation with the linked website. It is just a great overview of the concept.

When you push your work to the main branch on every push, the amount of code to merge is way smaller and it becomes trivial. There is a far greater benefit though: you and your team can spot problems before they become painful. It might be that your refactoring clashes with another feature. Or you are drifting off from the project conventions or architecture patterns. This is the real value of the process. As I preach in any place I find myself in:

> _It is teamwork that makes or breaks software projects._

Working days on code that will never get to the release on time is the biggest failure there is for a team.

Another upside of pushing to the main branch is that your changes will run live in some environment. It is always good to deploy and battle test your code, even in progress, in some real deploy.

#### Objection 1: “WIP” in the main branch!?!

If you read so far you are probably thinking “This is crazy, how can I push my half done work to the main branch when it will probably get deployed to production very soon!?!”.

Here are the common objections one might have and a tentative solution.

#### Objection 2: I can’t expose unfinished work!

Use feature toggles. They can be environment variables or whatever suits you best to turn on and off your work in progress. Make it defensive of course so your half-finished code does not get active in production by mistake.

Your whole team will love this: you can activate the code on any environment at any time to see how it looks or performs. Testers can prepare to test early on. Product owners can comment on your work along the way. It is all live and easy to access for everyone! If your work is just started, this provides little value. But evil lies in the details. It usually takes half the time to get to 90% completion and another half to finish the remaining 10%. Sharing your work in this state of 90% completion is always a good idea ;)

Another thing that comes for free: you can turn the feature off in production if a problem arises after deployment. After a few days or weeks, once the feature runs smoothly, just remove the toggle from the code.

#### Objection 3: What if I break the main branch for everyone?

It is 2019. If you don’t have a continuous integration setup that builds and runs tests automatically … then set it up yesterday. If you break anything you’ll be notified before it becomes a problem for the whole team.

In pure Trunk Based Development the feedback will come after the merge and has to be fixed right away. If you are using short-lived branches the merge should be blocked by your CI tool. A short-lived branch is something that should last 1 or 2 days max and carry a consistent piece of code that contributes to the feature you are building.

#### Objection 4: There must be a code review before we merge!

That’s a valid point. Code reviews do not need feature branches though. If the code review culture is strong in your team then it can very well be done on the commit to the main branch. The reviewer would stop by the author of the commit and discuss what needs to be fixed. The fix would come in another commit. Even better, have the code review together before pushing the commit in the first place.

If it is not acceptable to your team to have post-merge code reviews (because let’s face it it is less handy as tools do not really support that), use short-lived branches and apply your code review process there.

#### Objection 5: **I want to see the code that is related to a task**

If you have a given branch per feature then it is easy to track code back to your agile board. You can navigate from a task to the branch that implements it.

It sounds cool, while in reality, this is useless! How many people can you have on an agile team? Up to 5? Up to 10? How hard is it to ask the person running a task or story what commits you need to look at to deep dive into the implementation?

After some time, once tasks are completed for a long time, linking tasks to code does not make sense anymore. Developers rely on git blame to know the who, on code content to know the how, and hopefully on comments to know the why.

### The cherry on the cake: opt-in on new features

It became common to see major UI features or updates released using an “opt-in” approach. Github, Bitbucket, Gmail, … to name a few.

The concept is that major changes are introduced using a banner “Hey we have this new feature / improved dashboard / whatever. Click here to try it out”. You can opt-in, and usually opt out as easily if you don’t like the change. This is a very good adoption testing strategy as it involves the end users in the decision process. If people opt-in and stay there it means you are improving the experience. If they opt in and out … you know you’ve changed things for the worse.

If you are using feature toggles from the start, exposing these on a per-user basis at run time becomes very easy.

### Conclusion

If you never thought of trunk based development as an alternative to the feature branch mantra, I hope this article gave you some perspective and that you will to try it out.

The best thing is that to get there you’ll need to setup or improve every other aspect of your process (CI, automated tests, code reviews). This is a good path to take. We obviously recommend Fire CI as a [continuous integration tool](https://fire.ci/).

Remember that your bottom line is to put quality software in front of your users. The closer your code is from the production environment at all times, the better.

Now, although the article is very much “trunk based development” oriented, note that it might not be a valid approach for your team.

If your team is highly distributed, in different time zones, has a lot of junior developers who need to learn the project conventions and architecture, using longer-lived feature branches might work better.

The main idea in this article is:

**The faster you integrate the different pieces together and check that things are working, the safer you are to have a working product at the end.**

A good common ground is to use short-lived branches that last 1 or 2 days max and merge them to the main branch. This way you can humanly control what gets in and still integrate code fast.

**Thanks for reading! If you find the article useful please hit the clap button below. It would mean a lot to me and it helps other people see the story!**

_Originally published at [fire.ci](https://fire.ci/blog/why-you-should-not-use-feature-branches/) on March 30, 2019._


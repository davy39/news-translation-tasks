---
title: The real difference between Continuous Integration and Continuous Deployment
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-01T21:37:46.000Z'
originalURL: https://freecodecamp.org/news/the-real-difference-between-ci-and-cd
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/continuous-integration-and-delivery.png
tags:
- name: continuous delivery
  slug: continuous-delivery
- name: continuous deployment
  slug: continuous-deployment
- name: Continuous Integration
  slug: continuous-integration
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
seo_title: null
seo_desc: "By Jean-Paul Delimat\nThere is plenty of content out there describing what\
  \ Continuous Integration, Continuous Delivery, and Continuous Deployment are. But\
  \ what purposes do these processes serve in the first place? \nIt is crucial to\
  \ understand the prob..."
---

By Jean-Paul Delimat

There is plenty of content out there describing what Continuous Integration, Continuous Delivery, and Continuous Deployment are. But what purposes do these processes serve in the first place? 

It is crucial to understand the problems CI and CD solve to use them properly. This will allow your team to improve your process and avoid putting effort into chasing fancy metrics that do not bring any value to your process.

## Continuous Integration is a team problem

If you work in a team, chances are there are several developers working on the same repository. There is a main branch in the repository carrying the latest version of the code. Developers work on different things on different branches. Once someone is done with their change, they'll push or merge it to the main branch. Eventually the whole team will pull this change.

The scenario we want to avoid is that a faulty commit makes it to the main branch. Faulty means the code does not compile or the app won't start or is unusable. Why? Not because the app is broken or because all tests must always be green. That is not a problem–you can decide not to deploy that version and wait for a fix. 

The problem is that your entire team is stuck. All the developers who pulled the faulty commit will spend 5 minutes wondering why it doesn't work. Several will probably try to find the faulty commit. Some will try to fix the issue by themselves in parallel of the faulty code author.

This is a waste of time for your team. The worst part is that repeated incidents fuel a mistrust of the main branch and encourage developers to work apart.

> Continuous Integration is all about preventing the main branch from breaking so your team is not stuck. That's it. It is **not** about having all your tests green all the time and the main branch deployable to production at every commit.

The process of Continuous Integration is independent of any tool. You could manually verify that the merge of your branch and the main branch works locally, and then only actually push the merge to the repository. But that would be very inefficient. That's why Continuous Integration is implemented using automated checks.

The checks ensure that, at the bare minimum:

* The app should build and start
* Most critical features should be functional at all times (user signup/login journey and  key business features)
* Common layers of the application that all the developers rely on should be stable. This means unit tests on those parts.

In practice, this means you need to pull any unit test framework that works for you and secure the common layers of the application. Sometimes it is not that much code and can be done fairly quickly. Also you need to add a "smoke test" verifying that the code compiles and that the application starts. This is especially important in technologies with crazy dependency injections like Java Spring or .NET core. In large projects it is so easy to miswire your dependencies that verifying that the app always starts is a must.

> If you have hundreds or thousands of tests you don't need to run them all for each merge. It will take a lot of time and most tests probably verify "non team blocker" features.

We'll see in the next sections how the process of Continuous Delivery will make good use of these many tests.

### It's not about tools

Tools and automated checks are all fine. But if your developers only merge giant branches they work on for weeks, they won't help you. The team will spend a good amount of time merging the branches and fixing the code incompatibilities that will arise eventually. It is as much a waste of time as being blocked by a faulty commit.

> Continuous Integration is not about tools. It is about working in small chunks and integrating your new code to the main branch and pulling frequently. 

Frequently means at least daily. Split the task you are working on into smaller tasks. Merge your code very often and pull very often. This way nobody works apart for more than a day or two and problems do not have time to become snowballs.

A large task does not need to be all in one branch. It should never be. Techniques to merge work in progress to the main branch are called "branching by abstraction" and "feature toggles". See the blog post [How to get started with Continuous Integration](https://fire.ci/blog/how-to-get-started-with-continuous-integration/)  for more details.

### Key points for a good CI build

It's very simple. **Keep it short. 3-7 minutes should be the max.** It's not about CPU and resources. It is about developers' productivity. The first rule of productivity is focus. Do one thing, finish it, then move to the next thing. 

Context switching is costly. Studies show it takes ~23 minutes to deeply refocus on something when you get disturbed. 

Imagine you push your branch to merge it. You start another task. You spend 15-20 minutes getting into it. The minute after you are in the zone you receive a "build failed" notification from your 20 minutes long CI build for the previous task. You get back to fix it. You push it again. You easily lost more than 20 minutes moving back and forth.

> Multiply 20 minutes once or twice a day by the number of developers in your team... That's a lot of precious time wasted.

Now imagine if the feedback came within 3 minutes. You probably wouldn't have started the new task at all. You would have proof read your code one more time or reviewed a PR while waiting. The failed notification would come and you would fix it. Then you could move on to the next task. That is the kind of focus your process should enable.

Keeping your CI build short makes it a trade off. Tests that run longer or provide little value in the context of CI should be moved to the CD step. And yes, failures there also need to be fixed. But since they are not preventing anybody from doing their thing, you can take the fixes as a "next task" when you finish what you are doing. Just turn off the notifications while working and check every now and then. Keep the context switching to a minimum.

## Continuous Delivery and Deployment are engineering problems

Let’s settle on the definitions to get that out of the way.

**Continuous Delivery** is about being able to deploy any version of your code at all times. In practice it means the last or pre-last version of your code. You don’t deploy automatically, usually because you don’t have to or are limited by your project lifecycle. But as soon as someone feels like it, a deployment can be done in a minimal amount of time. That someone can be the test/QA team that wants to test things out on a staging or pre-production environment. Or it can actually be time to roll out the code to production.

The idea of Continuous Delivery is to prepare artifacts as close as possible from what you want to run in your environment. These can be .jar or .war files if you are working with Java, or executables if you are working with .NET. These can also be folders of transpiled JS code or even Docker containers, whatever makes deployment shorter (i.e. you have pre-built as much as you can in advance).

By preparing artifacts, I don't mean turning code into artifacts. This is usually a few scripts and minutes of execution. Preparing means:

> Run all the tests you can to ensure that, once deployed, the code will actually work. Run unit tests, integration tests, end to end tests, and even performance tests if you can automate that. 

This way you can filter which versions of your main branch are actually production ready and which are not. The ideal test suite:

* Ensures that the application's key functionalities work. Ideally all functionalities
* Ensures that no performance deal breaker has been introduced so when your new version hits your many users, it has a chance to last
* Dry run any database updates your code needs to avoid surprises

It does not need to be very fast. 30 minutes or 1 hour is acceptable.

**Continuous Deployment** is the next step. You deploy the most up to date and production ready version of your code to some environment. Ideally production if you trust your CD test suite enough. 

Note that, depending on the context, this is not always possible or worth the effort. Continuous Delivery is often enough to be productive, especially if you are working in a close network and have limited environments you can deploy to. It can also be that the release cycle of your software prevents unplanned deploys.

Continuous Delivery and Continuous Deployment (let’s call them CD from now on) are not team problems. They are about finding the right balance between execution time, maintenance efforts and relevance of your tests suite to be able to say "This version works as it should." 

And it is a balance. If your tests last 30 hours that is a problem. See [this epic post](https://news.ycombinator.com/item?id=18442941) about what the Oracle database test suite looks like. But if you spend so much time keeping your tests up to date with the latest code that it impedes the team's progress, that is not good either. Also if your test suite ensures pretty much nothing... it is basically useless.

In an ideal world we want one set of deployable artifacts per commit to the main branch. You can see we have a vertical scalability problem: the faster we move from code to artifacts, the more ready we are to deploy the newest version of the code.

## What’s the big difference?

Continuous Integration is a horizontal scalability problem. You want developers to merge their code often so the checks must be fast. Ideally within minutes to avoid developers switching context all the time with highly async feedback from the CI builds. 

The more developers you have, the more computing power you need to run simple checks (build and test) on all the active branches.

> **A good CI build:**

> Ensures no code that breaks basic stuff and prevents other team members to work is introduced to the main branch, and

> Is fast enough to provide feedback to developers within minutes to prevent context switching between tasks.

Continuous Delivery and Deployment are vertical scalability problems. You have one rather complex operation to perform.

> **A good CD build:**

> Ensures that as many features as possible are working properly.

> The faster the better, but it is not a matter of speed. A 30-60 minutes build is OK.

A common misconception is to see CD as a horizontal scalability problem like CI: the faster you can move from code to artifacts, the more commits you can actually process, and the closer to the ideal scenario you can be. 

But we don't need that. Producing artifacts for every commit and as fast as possible is usually overkill. You can very well approach CD on a best effort basis: have a single CD build that will just pick the latest commit to verify once a given build is finished.

Make no mistake about CD. It is really hard. Getting to sufficient test confidence to say your software is ready to be deployed automatically usually works on low surface applications like APIs or simple UIs. It is very difficult to achieve on a complex UI or a large monolith system.

## Conclusion

Tools and principles used to execute CI and CD are often very similar. The goals are very different though. 

Continuous Integration is a trade off between speed of feedback loop to developers and relevance of the checks your perform (build and test). No code that would impede the team progress should make it to the main branch. 

Continuous Delivery of Deployment is about running as thorough checks as you can to catch issues on your code. Completeness of the checks is the most important factor. It is usually measured in terms code coverage or functional coverage of your tests. Catching errors early on prevents broken code to get deployed to any environment and saves the precious time of your test team.

Craft your CI and CD builds to achieve these goals and keep your team productive. No workflow is perfect. Problems will arise every now and then. Use them as lessons learned to strengthen your workflow every time they do.

Published on 27 Nov 2019 on the [Fire CI Blog](https://fire.ci/blog/).


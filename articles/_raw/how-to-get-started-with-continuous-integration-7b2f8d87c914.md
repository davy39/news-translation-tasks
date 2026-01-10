---
title: How to get started with Continuous Integration
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-continuous-integration-7b2f8d87c914
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yOJI5juQCdKyFFk9YWKDWw.jpeg
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

  Everything you need to know to get started with continuous integration: branching
  strategies, tests automation, tools and best practices.

  The goal: Deliver working code quickly and safely

  The goal of Continuous Integration is to ...'
---

By Jean-Paul Delimat

Everything you need to know to get started with continuous integration: branching strategies, tests automation, tools and best practices.

### The goal: Deliver working code quickly and safely

The goal of Continuous Integration is to deliver code to the main branch of your repository:

* Quickly: from pushing new code to the repository to merging it to the main branch when it works should be done within minutes
* Safely: how do we know the new code works? Continuous Integration is about setting up the right checks to merge code automatically in full confidence

Continuous Integration is a bit about tools and a lot about mindset and culture in the team. You want your development process to facilitate fast integration of new code while keeping a working main branch at all times. This working main branch will enable Continuous Delivery or Continuous Deployment in the future. But these are for another post. Let’s focus on Continuous Integration first.

There are 2 pillars to achieve Continuous Integration:

#### Work in small chunks

Imagine a team of 5 working on a SaaS product. Each of them develops a separate new feature. The workload on each feature is about 1 or 2 weeks. There are 2 ways to go here.

* The team could go with feature branches. Each developer will work on their part on a “feature branch”. The branches will be merged to the main branch once everyone is happy with their work
* The team could go with branches (still) but integrate their work to the main branch on every push. Even if things are still a work in progress! The work in progress would remain invisible to any end user or tester of the main branch

Which approach do you think will work best?

The first approach will ultimately lead to the “unpredictable release syndrome”. Long lived feature branches create a false sense of safety and comfort for each developer **individually**. As the branches drift apart for a long period of time, there is no way to measure how hard it will be to merge it all. At best some minor code conflicts will arise, at worst fundamental design assumptions will be challenged and things will have to be reworked … the hard way.

> _Rework will be done under time pressure, leading to a drop in quality and accumulation of technical debt. This is a vicious circle._

See the post about [Why you should not use feature branches](https://fire.ci/blog/why-you-should-not-use-feature-branches/) for the dirty details.

The second approach is what we need to enable continuous integration. Each developer does work on their own branch. Difference is:

> _Changes are merged to the main branch on every push, and each developer syncs their branch with latest main branch version a few times a day._

This way the team can fix conflicts and align design assumptions faster and easier. 5 small problems discovered early on are way better that 1 big problem discovered just before release day. Check out the “Feature Toggles” section below to see how you should integrate “work in progress” to the main branch.

#### Safety comes with automated checks

Ancient software development process was based on a build cycle followed by a test cycle. And this would probably still fit the “feature branches” approach described above. If we integrate and merge code tens of times a day, manual testing does not make sense. It would take too long. We need automated checks to verify that the code works properly. We need a CI tool that will take each developers’ push and run build and tests automatically.

The test’s type and content should be:

* fast enough to provide feedback to the developer within minutes
* thorough enough to merge the code to the main branch in full confidence

Unfortunately there is no one size fit all test type and content. The right balance is specific to your project. Do not run large and time consuming test suites during your CI phase. Such tests provide better safety but they come at the cost of a delayed feedback to the developers. This leads to context switching which is a pure waste of time.

### Optimize developers’ time and reduce context switching

Long CI checks, and by long I mean over 3 minutes, introduce a compound waste of time for each developer in your team. Let’s compare a “good” and a “bad” worklow.

The “good” workflow:

* You commit and push your code
* The CI build and tests run for 1 to 3 minutes
* During the 1 to 3 minutes you review the task at hand, bump the status in some management tool, or review your code once again
* Within 3 minutes you get a successful status: you can move on to the next part of your task. If you get a failed build: you can fix the issue right away

The “bad” workflow:

* You commit and push your code
* The CI build and tests run for 15 minutes
* What do you do during these 15 minutes?
* You could grab a cup of coffee with the team. Fair enough, but how many of these can you have per day?
* You would probably get your head on the next task in your pipeline
* 15 minutes later you get a failed build notification. You need to switch back to the previous task, try to fix the issue … and go for another 15 minutes loop …
* At that point you are wondering: should I get back to this next task again or just wait the 15 minutes and achieve peace of mind that I am actually really done with my current task …

The bad workflow is not only a waste of time. It is also frustrating for developers. And productive developers are happy developers.

> _You need to align your tools and workflows to keep your developers happy._

### Tools

#### Branching

Continuous Integration is about integrating code from different developers’ branches to a common branch in your configuration management system. Chances are you are using git. In git the default main branch in a repository is called “master”. Some teams create a branch called “develop” as the main branch for continuous integration. They use “master” to track deliveries and deployments (develop being merged to master).

You probably already have a main branch your team pushes or merges code to. Stick with it.

Each developer should work on their own branch. One can use multiple branches if working on many different topics at once. Although this would be a sign of “unfocused” work at best. As soon as a consistent part of your code is ready, push your repository. The CI checks will kick in and merge your code to the main branch if they are successful. If the checks fail, you are still on your own branch and can fix whatever needs to be fixed and push again.

The important word in the process above is **consistent part of your code**. How do you know it is consistent? Simple.

> _If you can easily come up with a good commit message, it’s consistent._

On the other hand if your commit message needs 3 bullets and many adjectives and adverbs, it’s probably not good. Split your work in multiple, consistent commits. And then push the code. Consistent commits help code reviews and make the repository history easier to follow.

Don’t just push whatever because it’s the end of the day!

#### Pull requests

What is a pull request? A pull request is a concept in which you ask the team to merge your branch to the main branch. The acceptance of your request should go through a status provided by your CI tool and potentially a code review. Ultimately the manual acceptance of a human being in charge of merging the pull requests.

Pull requests were born in open source projects. Maintainers needed a structured way to evaluate contributions before merging them in. Pull requests are not part of Git. They are supported by any Git provider, though (GitHub, BitBucket, GitLab, …).

Note that pull requests are not mandatory for Continuous Integration. Their main benefit is to support a code review process, which cannot be automated by design.

If you are using pull requests, the same principles of “work in small chunks” and “optimize developers time” apply:

* keep each pull request small and with one clear purpose (it will make code review way easier)
* keep your CI checks fast

#### Automated checks

The heart of your Continuous Process are automated checks. They ensure that the main branch code is working properly after your code is merged. If they fail, your code does not get merged. As a minimum the code should compile or transpile or whatever your tech stack is doing to make it ready for runtime.

On top of compilation you should run automated tests to ensure the software works properly. The better the test coverage, the better confidence you can have in the new code being merged to the main branch. Careful though! Better coverage means more tests and longer execution time. You need to find the right tradeoff.

_Where do you start when you have no tests at all or need to cut down on some long running tests? Focus on what is critical for your project or product._

If you are building a SaaS application, you should check that users can sign up or login, and perform the most basic operations your SaaS provides. Unless you are developing a Salesforce competitor, you should be able to run your tests within minutes if not seconds. If you are building a heavy data processing backend: use limited data sets to exercise the different building blocks. Keep long running runs on large data sets out of Continuous Integration. Long running tests can be triggered after code is merged.

### Pro Tips

#### Feature toggles

The key concept of Continuous Integration is to put your code in the main branch as soon as possible. Even work in progress. Even features that do not fully work or that you don’t want exposed to testers or end users. The way to achieve that is to use feature toggles. Have your new feature under an enabled/disabled toggle. The toggle can be a compile time boolean flag, an environment variable or a runtime thing. The right approach depends on what you want to achieve.

The first major benefits of feature toggles is that you can take them up to production and enable/disable the new feature upon need. You could restart a server with a changed environment variable, or toggle on/off a new UI dashboard layout. This way you have full flexibility to roll out the feature. Or disable it if causes unexpected issues in production. Or allow end users to opt in or out of the feature (in case of the UI toggles).

The second major benefit of feature toggles is that they force you to think of the boundary between what you are doing and the existing code. This is a good exercise and this is what you should start with anyway every time you make an addition to an existing system. The feature toggle step makes this step of the process more visible.

The only drawback on feature toggles is that you need to clean them up periodically from the environment and from the code. Once a feature is battle tested and adopted by users, it should be the default. The code for the toggle and the old version of things (if any) should be cleaned up. Don’t fall into the trap of a “configuration as toggles” system. The pitfall is that you will never be able to maintain and test all combination of the toggles and will have a fragile architecture in the end.

#### Keep CI build time under 3 minutes

Remember the “good” and the “bad” workflow in the first part of the article. We want to avoid context switching for developers. Pick your phone and set a 3 minutes timer on. See how long it is when you are just waiting for something! 3 minutes should be an absolute maximum for you to focus and move safely and efficiently from one task to the other.

A build under 3 minutes might seem crazy to some teams, but it is definitely achievable. It has more to do with how you organize your work than the tools you use. Ways to optimize your build are:

* Use more build capacity: if you don’t have enough concurrent builds on your CI tool and builds get queued, developers lose time
* Leverage caching: most tech stacks require you to install and configure dependencies when running a fresh build. Your CI tool should be able to cache these steps when dependencies do not change to optimize build time
* Review your tests: check that your tests are optimized for time. Remove timeouts and “safely long” waiting steps. If you have heavy tests suites to run, consider moving them on a separate build that is run after the merge to the main branch. They would not be part of the Continuous Integration safeguard anymore, but heavy tests should not be anyway
* Split your code base: do you have to have everything in one repository? Do you have to build and run tests on everything even when some small part changes? There might be wins here.
* Run tests conditionally: run your tests only if some directories have changed. If your codebase is well organized, this can be a huge win

> _The great thing about forcing a short time limit on your CI checks is that it requires you to fundamentally improve your whole development process._

As [Jim Rohn](https://www.jimrohn.com/) said:

> “Become a millionaire not for the million dollars, but for what it will make of you to achieve it”.

#### The virtual merge: your code alone does not really matter

Most Continuous Integration tools run the CI build on your branch to say if it can be merged or not. But that is not what is of interest here. If you know what you’re doing there is a pretty good chance that the code you have just pushed is working already! What your CI tool is supposed to verify is that your branch merged with the main branch works properly.

Your CI tool should perform a local merge of your branch to the main branch and run the build and tests against that. Your branch can then be automatically merged if the main branch does not change in the meantime. If it does change, the CI checks should be run again until your code can be safely merged. If your CI tools does not support this kind of workflow, change your tool.

#### The evil task manager

There is a misbelief that it is cool to be able to trace the code related to a task in your Agile board or bug tracker like JIRA or similar. While it is a nice concept on paper, the impact on the development process is for sure not worth the effort. The task manager provides a “features and bugs” view of the world. The code is structured and layered in a very different way. Trying to reconciling an item in the task manager and a set of commits is pointless. If you want to know why a piece of code has been written, you should be able to get the information from the code context and comments.

### Final Thoughts

Tools are only tools. Setting up the tools is probably a 1 hour thing. If you use them wrong though, you won’t get the expected results.

Keep in mind the goals we set for ourselves for Continuous Integration:

* Deliver working code quickly and safely
* Optimize developers’ time and reduce context switching

The real deal is about shifting your mindset to “continuously deliver value” to your project or product.

> _Think of your software development process as a hardware production facility. Developers’ code represents the moving parts. The main branch is the assembled product._

The faster you integrate the different pieces together and check that things are working, the closer you are to have a working product at the end.

A few practical examples:

* You are working on a new feature and have to change a low level component others will most likely use. Make a dedicated commit for that common component part and have it merge already. Then continue working on the rest of your feature. Other developers will be able to base their work on your change right away.
* You are working on a large feature that will require a lot of time and code? Use a feature toggle. Don’t work in isolation. Ever!
* You are waiting for a code review but no one is available to do it. If your code is passing the CI checks then just merge it and make the code review happen afterwards. If it sounds like breaking the process, remember that “done is better than perfect”. If it is working, it provides more value in the main branch than parked on the side for days.

**Thanks for reading! If you find the article useful please hit the clap button below. It would mean a lot to me and it helps other people see the story!**

_Article originally published at [fire.ci](https://fire.ci/blog) on April 9, 2019._


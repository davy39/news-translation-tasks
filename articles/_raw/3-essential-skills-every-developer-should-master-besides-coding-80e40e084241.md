---
title: Essential skills every developer should master (besides coding)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-21T21:34:05.000Z'
originalURL: https://freecodecamp.org/news/3-essential-skills-every-developer-should-master-besides-coding-80e40e084241
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GP9tKFzB_XqNkHSWuiuk1A.jpeg
tags:
- name: careers
  slug: careers
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jean-Paul Delimat

  Whether you are learning to code, looking for a new job, or just want to improve
  your skills as a developer, you need to master the essential tools of team collaboration.
  These are as important as knowing how to code.

  It is teamw...'
---

By Jean-Paul Delimat

Whether you are learning to code, looking for a new job, or just want to improve your skills as a developer, you need to master the essential tools of team collaboration. These are as important as knowing how to code.

**It is teamwork that makes or breaks software projects.**

Your code will work eventually. If you want it to work “on time” and be of good quality, you and your team need to be organized.

* Everyone needs to know what they have to do and when
* People’s work should not overlap or clash
* Common rules need to be followed through by everyone

You can achieve this using the right processes and tools. You want your team to focus on coding 90% of the time (the remaining 10% are for coffee breaks and Windows Updates).

Here are three essential things you need to master.

### Git and Pull Requests

[Configuration management](https://en.wikipedia.org/wiki/Configuration_management) is the foundation of team collaboration in software. Many tools exist for it, but luckily one has become the absolute and ultimate reference: [Git](https://git-scm.com/).

Documentation on the key aspects is well described in the [Git Book](https://git-scm.com/book/en/v2).

There are plenty of turnkey services to get started: [GitHub](https://github.com/) is probably the most popular, but also [BitBucket](https://bitbucket.org/) or [GitLab](https://about.gitlab.com/).

A great graphical tool to work with is [SourceTree](https://www.sourcetreeapp.com/). I recommend you master the command line before reaching for UI tools, though.

Below are the questions you should know how to answer:

* How do I merge or rebase my branch, and what is the difference?
* How do I resolve conflicts? For example, mine versus theirs versus manual merge
* What is a [feature branch](https://bocoup.com/blog/git-workflow-walkthrough-feature-branches)?
* What is a [pull request](https://yangsu.github.io/pull-request-tutorial/)?
* What are the different [collaboration workflows](https://www.atlassian.com/git/tutorials/comparing-workflows) in Git?

That’s it, and this is pretty straightforward. After reading the theory and with some practice, you will become a Git master in a jiffy.

### The Agile board

The first thing a team needs to do when starting a project or a larger task is to split the job. Over the last 10 years, the “Agile” methodology replaced the traditional waterfall planning. The Agile manifesto is [here](http://agilemanifesto.org/).

Practically speaking it says “let’s not plan too much ahead, because inputs and assumptions we have today about the project will change”. This is almost always true, and nowadays there is hardly any team under the sun that is not (sometimes self-proclaimed) “Agile”.

Here are the practical things you need to know:

* The most popular Agile way of working is [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)). Divide your project into “sprints” of two weeks and put “tasks” in the content of the sprint. All the rest is for the future and is called the “[backlog](https://www.scrum.org/resources/what-is-a-product-backlog?gclid=EAIaIQobChMIrYurlr7o2AIVEhoYCh0dwQVdEAAYASAAEgIXtPD_BwE)”. This is useful to track progress, adjust planning going forward, and improve [team velocity](https://www.mountaingoatsoftware.com/blog/know-exactly-what-velocity-means-to-your-scrum-team) over time.
* Another Agile approach is [Kanban](https://en.wikipedia.org/wiki/Kanban). The idea is to limit the number of tasks that are “in progress”. This way, you are sure to close one item fully before moving to the next. There are no sprints or time frames like in Scrum. You just go through tasks one after the other until you’re done.

In Agile, a software project will be split into tens or hundreds of tasks. You need a tool to manage them. The reference tool is [JIRA](https://www.atlassian.com/software/jira).

Other tools [exist](https://blog.capterra.com/5-outstanding-atlassian-jira-alternatives-for-your-growing-tech-team/) of course, but you will probably have to work with JIRA at some point. So if you are new to these all the tools, just go for JIRA. There is a [free 7 day trial](https://www.atlassian.com/software/jira/pricing?tab=cloud). It is more than enough to get an overview of how things work. Again, this is fairly straightforward, and very well-documented.

### Testing and Continuous Integration

Git and agile tools allow teams to go fast. With speed inevitably come errors and bugs. Consider a team of five developers working on rather independent pieces of code. Each of them will make a pull request to the repository. Two problems can arise:

* Once the code of the “first developer” gets to the Git repository, the code of the others is no longer valid or working because some things have changed. This is not a mistake from “the first developer”, it is just life and it will happen.
* Once all the developers pushed their code to the Git repository, chances that everything work as expected out of the box are rather low. Again, this is not a reflection of poor teamwork. It will just happen.

Therefore, you need to test your software. Even after each developer has pushed their code? It would be great, but a waste of time.

When other developers push their code, we’ll need to repeat this task. Should you test once everyone has pushed their code? Also great, but you’ll find bugs late in the process, which can delay the whole project. So how can you solve this?

Automated tests and [Continuous Integration](https://www.martinfowler.com/articles/continuousIntegration.html) are there to the rescue.

Automated testing is a topic one could write many books about. Each language and framework has its own set of tools. Listing them all would not make sense here. Just keep in mind that testing is time consuming and not always planned for.

Regardless, you should know how to write unit tests for your code and be proactive about writing them. If you don’t have time to actually do it, you should at least be aware that it’s wrong.

Continuous Integration is a process in which every push to your repository triggers a build and runs your tests automatically. A red flag is raised as soon as a faulty commit goes in. Pull requests should also be tested automatically before merging to avoid bugs that impact the whole team.

Continuous Delivery is the extension of Continuous Integration. If the tests pass properly, the tested version is pushed to the production environment automatically.

As an example: at [Quora](https://www.quora.com/), they track the time between a push to the repository and deployment of that code to production servers. The last benchmark I read about was 15 minutes … for around 100 developers. This is the most powerful setup a team could hope for.

Popular continuous integration servers are [Jenkins](https://jenkins.io/), [Travis](https://travis-ci.org/), [CircleCI](https://circleci.com), and a few more. You do not need to know how to set the server up and everything, but you should know such tools exist, and a red alert should trigger in your head if your team do not use any.

### Conclusion

The core of a developer’s job is coding. Once you move from solo/hobbyist to member of a performing team, proper use of the key collaboration tools is as important as writing clean code. Hopefully this article gave you an overview of what these tools are and how to dig further to be the best at what you do!

**Thanks for reading! If you find the article useful please hit the clap button below. It would mean a lot to me and it helps other people see the story!**


---
title: How to use GitHub native features to help manage a mid-size distributed team
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T22:02:43.000Z'
originalURL: https://freecodecamp.org/news/using-github-native-features-for-a-mid-size-distributed-team-3acdfd0f027c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3_KSG37XnfbQIaHf-_-b-A.jpeg
tags:
- name: communication
  slug: communication
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: project management
  slug: project-management
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Alex Ewerlöf

  My team created a wiki page in our private Github repo about how we work on a common
  code base. I want to share it with you.

  We’re a team of 15 people with 10 developers, a project manager (PM), a tech lead
  (TL), an engineering manage...'
---

By Alex Ewerlöf

My team created a wiki page in our private Github repo about how we work on a common code base. I want to share it with you.

We’re a team of 15 people with 10 developers, a project manager (**PM**), a tech lead (**TL**), an engineering manager, a UXer and DevOps spread across three European countries. The product is an internal web based SaaS that’s used by other teams inside the company.

### Communication

We primarily communicate via Slack, but have a biweekly retro on video conference (VC). We don’t have a daily standup, but instead have a weekly reminder for the week’s tasks where everyone can write an update in a thread. The idea is to turn the standup questions around from being about people to being about the tasks. We got the idea from the “Flow” workshop by _Marcus Hammarberg_:

### Why?

As the project and team grows, we can work more efficiently by keeping track of the issues and PRs in a smart way.

GitHub has many project management features built in. Besides, it is easier for developers to have their code and tasks in one place. Features like [closing issues with comments](https://help.github.com/articles/closing-issues-using-keywords/), [contribution guide](https://help.github.com/articles/setting-guidelines-for-repository-contributors/), and [issue templates](https://help.github.com/articles/manually-creating-a-single-issue-template-for-your-repository/), [code owners](https://help.github.com/articles/about-codeowners/) and its [integrations with other services](https://github.com/marketplace) make it a quite useful tool.

The idea is to define a loose way of handling work without putting too much load on the PM/TL while still getting their input when needed.

### What?

We use a few native GitHub features to organize the issues and have a clearer picture on what is going on in the project at any time.

### How?

We use GitHub issues, labels, and milestones. We currently don’t use GitHub projects (but instead use [Zenhub](https://www.zenhub.com/) as our Kanban board).

### When?

We use weekly milestones. At the beginning of every week, we have a planning meeting (also on VC) where together with the PM/TL we define the weekly milestone which is the focus of the team for that week.

We use GitHub milestones that that have names like W22, with a description of what is supposed to be achieved by the end of the week. It also clearly mentions the acceptance criteria.

At the end of the week, we have the weekly demo (also on VC) where we show the result and give kudos to anyone who has done an outstanding job.

### Atomic issues & pull requests

* Each issue should address one thing. If the discussion regarding an issue expands out of scope, create another issue.
* Always start from an issue rather than a PR. Always discuss the problem (in an issue) before submitting a solution (in a PR).
* Squash the PRs when merging to keep the history of the `master` branch clean and reasonable.
* It’s good practice to add background info to a PR, but if you’re writing too much it probably means that you need to comment on the issue instead.
* Keep the discussions in the issues and let the priorities be assigned before starting to code.

### 1:1 mapping between issues and PRs

* In the rare case that you make a PR without a relevant issue, make an issue and refer to it in the PR description.
* There must be at least one issue for every PR.
* It is recommended that each PR closes one issue.
* Write a brief description of the solution in the PR and refer to the relevant issue(s).

### No direct commit to master

* All changes to master should come from PRs.
* The idea is to always have a working `master` branch.

### Who?

In our team, we use a lean way of taking on tasks. Once they are prioritized by the PM, anyone can go and pick a task and work on it. To signal that the issue is in progress, you simply assign it to yourself.

We use mob programming for larger tasks, and in that case, all people involved in the task are assigned. They are also pinged in the PR description so they’ll get an update for comments on the PR.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MGMLp6oH0kjAnAjTg6ySCg.jpeg)

### Labels

When creating an issue, we assign the relevant labels to it for easier filtering. For example, we can filter all `test` related issues or `prio-hi` issues with one click or even bookmark the query.

There are many labels, but they basically fall into the following categories:

#### Prioritization

When a new issue comes in, it waits until it is prioritized by the PM and gets one of these labels:

* `prio-high`: high priority tasks that should be done ASAP
* `prio-mid`: mid priority tasks that can be done when there’s no high priority tasks
* `prio-low`: low priority tasks that can wait
* `on-hold`: the tasks that we will not do until further notice

If an issue doesn’t have any of these labels, it shouldn’t be worked on. The PM can change the priority of an issue based on the changes in stakeholder needs.

When an issue has a milestone, it is ready to be developed. All other issues that are not in a milestone are in the “backlog”. Issues may be assigned to the weekly milestone of an upcoming week. If you can’t contribute to this week’s milestone, maybe you can prepare for next week by doing some of that work.

Anyone can create an issue. In fact a question can be an issue, if you feel it’s the best way to get answers. An issue will not automatically convert to task until it has been prioritized (got a `prio-*` label) and added to a milestone.

#### Size

* `EPIC`: is an issue that can lead to several PRs and should be broken down into `atomic` issues before it gets implemented.
* `atomic`: is an issue that can be implemented on its own and will lead to a PR.

#### Grouping

We also use labels to group similar issues together or flag different aspects of an issue or PR. An issue can have any number of these flags:

* `tooling` the issues that touch on the build system, linting, test tooling...
* `test` the issues about testing and QA
* `ux` the issues that require some UX work, improve UX, or affect UX in some way
* `config` the issues related to configuration changes
* `doc` the issues about documentation (in-code comments or published documentation like wiki)
* `perf`: suggestions for monitoring and improving performance
* `dx`: stuff that improves developer experience like logging and so on.
* `security`: security issues or security improvements.
* `discussion`: we haven't reached a consensus there, maybe you can contribute?
* `help needed`: the issue needs some help from external teams (if you're waiting on an internal volunteer, you can just go ahead and ping them). These issues are typically a good candidate for PM/TL to facilitate cross-team communication.
* `feature`: for introducing new features
* `bug`: for bug reports
* more labels can be added if we have enough issues that fit a certain lavel.

### Things GitHub can’t do

Unfortunately, the current Github tooling falls short for at least two important things:

1. There’s no easy way to group issues together under (Epics). We used labels for a while, but it was suboptimal.
2. Apart from using labels, there’s no way to prioritize the issues. We need a tool where the order of the issues can show their importance.

Both of these issues are solved by [Zenhub](https://www.zenhub.com/), which is a Chrome/Firefox extension that enriches the native GitHub interface. It also has a hosted service for those who don’t use Chrome/Firefox.

The only area that Zenhub still falls short is defining a limit on work in progress ([WIP limit](https://github.com/ZenHubIO/support/issues/272)).


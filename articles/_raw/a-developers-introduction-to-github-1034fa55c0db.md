---
title: A developer’s introduction to GitHub
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-02-28T17:44:48.000Z'
originalURL: https://freecodecamp.org/news/a-developers-introduction-to-github-1034fa55c0db
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1xi2ApL_xJQp2oevpEfQqw.png
tags:
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  GitHub is a website that hosts billions of lines of code, and it’s where millions
  of developers gather every day to collaborate on and report issues with open source
  software.

  In shor...'
---

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

GitHub is a website that hosts billions of lines of code, and it’s where millions of developers gather every day to collaborate on and report issues with open source software.

In short, it’s a platform for software developers, and it’s built around Git.

_TIP: If you don’t know about Git yet, [checkout my Git guide](https://flaviocopes.com/git-guide)._

As a developer, **you can’t avoid using GitHub or another Git-based tool on a daily basis** as part of your work. It’s used to either host your code or to collaborate on other people’s code. This article explains some key concepts of GitHub, and how to use some of its features to improve your workflow.

### Why GitHub?

Now that you know what GitHub is, you might ask why you should use it.

GitHub, after all, is managed by a private company, which profits from hosting people’s code. So why should you use that instead of similar platforms such as BitBucket or GitLab?

Beside personal preferences, and technical reasons, there is one big reason: everyone uses GitHub, so the network effect is huge.

Major codebases have migrated over time from other version control systems to Git because of its convenience, and GitHub has been historically well positioned and put in a lot of effort to serve the needs of the Open Source community.

So today, any time you look up some library, you will 99% of the time find it on GitHub.

Apart from Open Source code, many developers also host private repositories on GitHub because of the convenience of the platform.

Now lets get started on the important Git specific concepts that a developer needs to know.

### GitHub Issues

GitHub issues are one of the most popular bug trackers in the world.

They provide the owners of a repository the ability to organize, tag, and associate issues to milestones.

If you open an issue on a project managed by someone else, it will stay open until either you close it (for example if you figure out the problem you had) or the repo owner closes it.

Sometimes you’ll get a definitive answer, and at other times the issue will be left open and tagged with some information that categorizes it. Then the developer can get back to it to fix the problem or improve the codebase with your feedback.

Most developers are not paid to support their code released on GitHub, so you can’t expect prompt replies. But some open source repositories are published by companies that provide services around that code, have commercial offerings for versions with more features, or utilize a plugin-based architecture. And so they have paid developers working on the open source project.

### Social coding

![Image](https://cdn-media-1.freecodecamp.org/images/zeKPlxHOUmeK4gjz37spBu8yaOyHFfn0SPn6)
_Image credit: [https://octodex.github.com](https://octodex.github.com" rel="noopener" target="_blank" title=")_

A few years ago, the GitHub logo included the “social coding” tagline.

What did this mean, and is that still relevant? It certainly is.

#### Follow

With GitHub you can follow a developer or a repository by going to the user’s profile and clicking “follow,” or by clicking the “watch” button on a repo.

In both cases, the activity will show up in your dashboard. Following a user or repository is unlike Twitter, where you see what people **say** — instead you see what people **do**.

#### Stars

One big feature of GitHub is the ability to **star a repository**. This action will include it in your “starred repositories” list, which allows you to keep track of projects you find interesting and discover similar projects.

It’s also one of the most important rating mechanisms, as the more stars a repo has, the more popular and important it generally is. This results in it showing up more prominently in search results.

Major projects can have tens of thousands of stars.

GitHub also has a [trending page](https://github.com/trending) where it features the repositories that get the most stars in a determined period of time (for example, today or this week or this month).

Getting into those trending lists can cause other network effects like being featured on other sites, just because you have more visibility.

#### Fork

The last important network indicator of a project is the number of forks.

This is key to how GitHub works, as a fork is the base of a Pull Request (PR), which is a change proposal. A person may fork your repository, make some changes, and then create a pull request to ask you to merge those changes.

Sometimes the person that forks a repository may never ask you to merge anything. They may fork your repository just because they liked your code and decided to add something on top of it which they don’t want to merge back into the original repository. A user may also fix a bug they were experiencing which was specific to them.

#### Popular = better

All in all, those are all key indicators of the popularity of a project. Apart from the above indicators, the date of the latest commit and the involvement of the author in the issues tracker are useful indications of whether or not you should rely on a library or software.

### Pull requests

In the previous section I introduced what a Pull Request (PR) is. To reiterate, a person may fork your repository, makes some changes, and then create a pull request to ask you to merge those changes.

A project might have hundreds of PRs, and it’s generally the case that the more popular a project, the more PRs it has, like the React project:

![Image](https://cdn-media-1.freecodecamp.org/images/Z3cdqa5H6YpVbiRanpK5KrI7R7ylKFnErRho)

Once a person submits a pull request, it needs to be reviewed by the core maintainers of the project.

Depending on the **scope** of your pull request (the number of changes, the number of things affected by your change, or the complexity of the code touched) the maintainer might need more or less time to make sure your changes are compatible with the project.

A project might have a clear timeline of changes they want to introduce. The maintainer might like to keep things simple while you are introducing a complex architecture in a pull request.

This is to say that **a pull request does not always get accepted** quickly, and **there is no guarantee that the pull request will ever get accepted**.

In the example I posted above, there is a pull request in the repo that dates back to 1.5 years ago. And this happens in **all** projects — it’s quite normal and may be due to the reasons I mentioned above.

### Project management

Along with issues, which are the places where developers get feedback from users, the GitHub interface offers other features aimed at providing a few project management features.

One of those is **Projects**. It’s very new in the ecosystem and very rarely used, but it’s a **Kanban board** that helps organize issues and work that needs to be done.

The **Wiki** is intended to be used as a documentation for users. One of the most impressive uses of the Wiki I’ve seen up to now is the [Go Programming Language GitHub Wiki](https://github.com/golang/go/wiki).

Another popular project management aid is **milestones**. It’s part of the issues page, and you can assign issues to specific milestones, which could be release targets.

Speaking of releases, GitHub enhanced the **Git tag** functionality by introducing **releases**.

A Git tag is a pointer to a specific commit, and if done consistently, it helps you roll back to previous version of your code without referencing specific commits.

A GitHub release builds on top of Git tags and represents a complete release of your code, along with Zip files, release notes, and binary assets that might represent a fully working version of your code’s end product.

While a Git tag can be created programmatically (for example, using the command line `git` program), creating a GitHub release is a manual process that happens through the GitHub UI. You basically tell GitHub to create a new release and tell them which tag you want to apply that release to.

### Comparing commits

GitHub offers many tools to work with your code.

One of the most important things you might want to do is compare one branch to another one. Or you might want to compare the latest commit with the version you are currently using to see which changes were made over time.

GitHub allows you to do this with the **compare view**: just add `/compare` to the end of the repo name.

For example, [https://github.com/facebook/react/compare](https://github.com/facebook/react/compare)

![Image](https://cdn-media-1.freecodecamp.org/images/GBDt2fNQIOZS17JBdVo2ILLTQdu1wcF9FYxq)

In the figure below, I compare the latest **React v15.x** to the latest **v16.0.0-rc** version available at the time of this writing to see what’s changed.

![Image](https://cdn-media-1.freecodecamp.org/images/NVNSfcKh3bIYmlM0wgG4qgJNLp9wwFcg8mqB)

This view shows you **the commits made** between two releases (or tags or commits references) that were changed, and **the actual diff**, **if the number of changes is lower than a reasonable amount**.

### Webhooks and Services

GitHub offers many features that help the developer workflow, such as webhooks and services.

#### Webhooks

Webhooks allow external services to be pinged when certain events happen in the repository, for example when code is pushed, a fork is made, or a tag was created or deleted.

When an event happens, GitHub sends a POST request to the URL we tell it to use.

A common usage of this feature is to ping a remote server to fetch the latest code from GitHub when we push an update from our local computer.

We push to GitHub, GitHub tells the server we pushed, and the server pulls from GitHub.

#### Services

GitHub services, and the new GitHub apps, are 3rd party integrations that improve the developer experience or provide a service to you.

For example, you can setup a test runner to run the tests automatically every time you push some new commits, using [TravisCI](https://travis-ci.org/).

You can setup Continuous Integration using [CircleCI](https://circleci.com/).

You might create a [Codeclimate](https://codeclimate.com/) integration that analyzes the code and provides a report of “Technical Debt” and test coverage.

### Final words

GitHub is an amazing tool and service to take advantage of, a real gem in today’s developer toolset. This tutorial will help you get started, but the real experience of working on GitHub open source (or closed source) projects is something not to be missed.

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)


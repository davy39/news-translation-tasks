---
title: How to pull from a Git remote repository
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-09-03T23:37:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-pull-from-a-git-remote-repository-b9fabb6b3c9d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*3MKmgO4C_GLI_of0.png
tags:
- name: Git
  slug: git
- name: learning
  slug: learning
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'Note: This the fourth video in the Git for beginners series. Watch the
  first video here.

  When you make a change to a local repository, you can push a change to a Git remote
  repository. Likewise, when the remote gets changed, you can pull the changes ...'
---

Note: This the fourth video in the Git for beginners series. [Watch the first video here](https://zellwk.com/blog/setting-up-git).

When you make a change to a local repository, you can push a change to a Git remote repository. Likewise, when the remote gets changed, you can pull the changes back to your local repository.

Today, you’ll learn how to do the pull from the remote back to your repository.

### Making a change to the remote

Usually, another person working on the same project makes a change to the remote. They change the code on their computer, and they push it to the remote repository.

Once the remote repository changes, you can pull it back to your local repository to get the updated version.

That’s the standard workflow.

But, since I’m working on the project alone, I’m going to show you how to change the remote repository directly on GitHub. Once we’re done, we’ll pull from there.

### Changing the GitHub repository directly

Let’s say we want to change the `README.md` text.

To do so, you can click on the pencil icon beside the Readme file. This brings you to an editor where you can change the text.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3MKmgO4C_GLI_of0.png)

Once you’re done, scroll down to the bottom and write a commit message. You can click on the green button to commit the changes directly on GitHub.

![Image](https://cdn-media-1.freecodecamp.org/images/0*M48tNNP5FvJvRUcE.png)

The project will be updated.

### Fetching changes

Fork and other Git clients can show you the changes to a remote repository. They do it through a command called Git Fetch.

You can do a Fetch yourself by clicking on the empty arrow that points downwards. It’s the leftmost arrow button on the top left-hand corner

![Image](https://cdn-media-1.freecodecamp.org/images/0*b7PHmWflcH2u27tT.png)

Fetch checks the remote repository for any changes. It’s like an email client that says you have three emails to read.

Once the Fetch finishes, you can see in the Git history that `origin/master` is on the `update README.md` commit. The `update README.md` commit is one commit ahead of our local master branch.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ewPdamyyxzHQqcl8.png)

On the sidebar, you can see the number 1 beside our master branch, and an arrow that points downwards. This tells us our branch is one commit behind the remote.

### Pulling changes

To update your local branch, you can click on the pull button. The pull button is the filled downwards arrow at the top left-hand corner. It’s the one between Fetch and Push.

![Image](https://cdn-media-1.freecodecamp.org/images/0*d3YLHKVBJVh3OwQp.png)

When you click on Pull, you’ll be able to select the branch you want to pull. Since we have tracked it previously, you can pull the master branch directly by clicking pull again.

When you pull the branch from the remote to your local repository, you’ll see that `master` moves up to the same commit as `origin/master`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*O463L1K2aqiZ685A.png)

### Wrapping up

Fetch checks if there are any changes in the remote repository.

Pull brings the changes from the remote repository to your local repository.

Thanks for reading. Did this article help you in any way? If you did, [I hope you consider sharing it](http://twitter.com/share?text=Pulling%20from%20a%20Git%20remote%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/pulling-from-a-git-remote/&hashtags=). You might help someone out. Thank you!

This article was originally posted at [my blog](https://zellwk.com/blog/pulling-from-a-git-remote/). Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better front-end developer.


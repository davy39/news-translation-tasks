---
title: How to Use Git Rebase – Tutorial for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-17T22:17:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-rebase
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-15-at-10.58.48-PM.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'By Nick Abbene

  The software engineering landscape is constantly changing. Staying up to date on
  new technologies is absolutely critical.

  But as developers, sometimes we forget how important it is to dig a bit deeper into
  the tried and true technologi...'
---

By Nick Abbene

The software engineering landscape is constantly changing. Staying up to date on new technologies is absolutely critical.

But as developers, sometimes we forget how important it is to dig a bit deeper into the tried and true technologies that are the backbone of software development – such as version control systems like Git.  

In this article, we’ll take a look at an alternative to the widely used git merge command.  That alternative is git rebase.

## Understanding Git Rebase

Git rebase is a powerful feature of Git that has the ability to rewrite and reorganize your commit history. Git rebase allows you to change the base of your branch.

Unlike merging, which creates a new merge commit and combines the history of both branches, rebasing replays the commits of one branch onto another. This results in a linear commit history, making it easier to read and understand.

### Setting the stage with Git Merge

Not grokking the difference between git merge and git rebase? Let’s consider an example. You’re working on a new change, so you create a new branch with `git checkout -b`.  You then commit some changes to your new branch.  


![Image](https://lh4.googleusercontent.com/KzlG4wOQ_D3M6THap-VPhIQaRsYs2_PjXrbwwzru4fiYmAorZZJLMUl0SqH6MeTCLDXE5rHtpzpLztENpFBRXMcM0EFbUS-mb3cnOuC7kSgsiMdK5NWo138AcbTVNF_ePqLsMRMbnx-7HuH4SFjL5_E)
_Basic commit illustration_

In the meantime, someone else working on a separate part of the system merges in their own Pull Request! The git history now looks a bit like this, as they don’t have any context or knowledge of your changes.  


![Image](https://lh3.googleusercontent.com/qLOwHczX8I02UWtZ5ymTVSvaaXB9760kv0UhDDx-e3eOPtjM93jNhsxTHePfyWL0OBrAxEgR8X9mRgUg_U-q0AHtSnZDad5HJyZeEMQMkb7CXBY18xRBhzgP6pXhW-uuhUX0LsHJCdxf81XCex5FIR8)
_Illustration of git, your teammate pushed some new commits._

You finish up your changes with one last final commit. But what do you do next to get it back into the main branch?  


![Image](https://lh4.googleusercontent.com/1mzTfQy7U1z6hMtin6JHIpJofRSoeElpHJcflmFIE2niq16PP-GlqWn6ebw1O0TKTmivUVJPOh3oaCc6sVOB751x3TDJNDVgXiVgmVMb2zu3kw9bDHXffG15bLA6uaWb7nqKwRMQ9nIqdhHgaqT64EU)
_Illustration of git, with an additional commit on your branch_

Well, you have two options. First up is a command that you're likely familiar with if you've used Git before: git merge. The end result looks a bit like this.

![Image](https://lh5.googleusercontent.com/S4eILyjWjxrmlBThz1q2wKQgSddVJ0QGkGTUiDP2y_f3TX1NoMNRfVkmklgmLDICBeRyBPVUOdeD7HbGs6HzSszEv01pXl8TWxhLSEKq44MVsVqWIYcJSec85gkfO53B9sUCRc9MA3I9mgOfetVHYu4)
_Illustration of git, with an additional merge commit_

As you can see, we have an additional commit just for the merge.  The history carries on from here, and this is fine! Many coders get on just fine using merge commits. But what if you have a longer-lived branch that you need to keep up to date? 

In this case, we’re working on a branch named `foo`. Our commits are the ones with the comments, `some other thing`, `adding test`, and `addressing comments.` Take a look at what the history looks like.

![Image](https://lh3.googleusercontent.com/RVMAGg4oPs1DSX6gFjo1CClg4Vtl6uLmc_-sWsb9dkw-5bxPRTWkSVPVR7C-vCLobok6kpWU942RtRJPwq8xP_p5HuA0mJSdrH7dxLJwhlj2oZjhx29RTvrTswKf0eSqOUF3jz2HFqu8vSQkPkQchDI)
_Git History with Merging_

Those `Merge branch ‘main’ into foo` commits don’t seem very helpful - they’re simply logistical, and they don’t actually describe changes that you’re making on your branch. It’s also a bit hard to reason about the consecutive changes you made on your current branch when looking at your Git history.

### How to perform the rebase

Let’s explore the alternative with git rebase. Taking the same example above, let’s start with our final commit right before we’re ready to merge back into `main`.

![Image](https://lh4.googleusercontent.com/1mzTfQy7U1z6hMtin6JHIpJofRSoeElpHJcflmFIE2niq16PP-GlqWn6ebw1O0TKTmivUVJPOh3oaCc6sVOB751x3TDJNDVgXiVgmVMb2zu3kw9bDHXffG15bLA6uaWb7nqKwRMQ9nIqdhHgaqT64EU)
_The base case_

This time, we’re going to do a git rebase. This will actually replay your commits **on top** of the new commits (known as the HEAD) of `main`, preventing merge commits.

![Image](https://lh5.googleusercontent.com/0sbSYMp0Xhbod-lkHDr-24wrB4NWov857B7C_vnpkQlM7bTq1qFbGMcWqfYrDHWDs1lHlxm9ZyLJaRfRr0pmcqVf7nfe_siDLv0dWdq2ZtoCUboChjR_9SzAAtMOVapYaK3kF40E3CY_qrbEveA6_jk)
_Rebasing illustration_

So how do we accomplish this? While on your side branch (in our case, `foo`), you’ll want to do the following.

1. Switch to your `main` branch with `git checkout main`
2. Update your local `main` branch with `git pull`. This is so we have the latest HEAD of `main` available for the rebase.
3. Switch back to your branch `foo` with `git checkout foo`
4. Use `git rebase main`, this will complete the rebase, replaying your commits on top of the HEAD of `main`.

In comparison to the earlier example, what does this look like with the same commits “some other thing”, “adding test”, and “addressing comments”?

![Image](https://lh5.googleusercontent.com/aS-mY0pqWfzcT-uIvvILDMouHOys4MEtiORn_jpVk479QVopePBM-2h4YwiW4Do5k7127Gkb_dbYfWuGyr508Te2ISmsWQgEgSRK3qxY82pNnb6b9mjIc7yxQJS7gNuypru_-zjPBdNFD9uBhxpUMvg)
_Cleaner commit history with git rebase_

Very nice! It’s cleaner, and looking at my branch history, it’s pretty straightforward to reason about the changes on my branch. I only need to know where I started (commit hash `2a2db46`).

## Rebase Best Practices

While git rebase undoubtedly keeps your commit history cleaner, there are a few things to be mindful of:

* Use rebase **only** for local branches. **Do not rebase branches others are working on.**  Rebase _changes_ the commit history, and others will not know about it.
* Regularly fetch and rebase your local branches to stay up-to-date with the main branch. Conflicts become messy! Rebase early and often.

## Conclusion

While it's easy to get caught up in new and exploding technologies such as [artificial intelligence tooling](https://nickabbene.com/best-ai-productivity-tools) and [edge computing](https://www.forbes.com/sites/forbestechcouncil/2023/03/17/top-six-edge-computing-trends-to-know-about-in-2023/?sh=4b239b886754), it's also important for us as developers to take a step back and make sure we are using tried and true tools such as Git to their maximum potential.  

In this article, we took a look at `git rebase`, and gave an example of why rebasing could be a good tool in your toolbox.

Happy rebasing!


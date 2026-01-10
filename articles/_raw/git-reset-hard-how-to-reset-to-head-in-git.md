---
title: Git Reset Hard – How to Reset to Head in Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-10T12:09:39.000Z'
originalURL: https://freecodecamp.org/news/git-reset-hard-how-to-reset-to-head-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/resetToHead.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Git is a powerful version control system for tracking and managing changes
  and files in your source codes and other digital assets. One of the core functionalities
  of Git is "commits".

  Commits let you create a snapshot of your code. In other words, i...'
---

Git is a powerful version control system for tracking and managing changes and files in your source codes and other digital assets. One of the core functionalities of Git is "commits".

Commits let you create a snapshot of your code. In other words, it’s like saving your work, but with some added advantages and differences. When you create a commit, that’s one version of your code.

While working with Git, there might be some situations you want to reset to a particular commit or reset to the most recent commit in the current branch.

In this article, I’ll show you how to reset to `HEAD` in Git. But what is `HEAD` in Git? That’s what we are looking at next!


## What We’ll Cover
- [What is `HEAD` in Git?](#heading-what-is-head-in-git)
- [Why Reset to `HEAD` or Any Other Commit in Git?](#heading-why-reset-to-head-or-any-other-commit-in-git)
- [How to Reset to `HEAD` in Git](#heading-how-to-reset-to-head-in-git)
- [How to Reset to a Particular Commit with the Git Reset Command](#heading-how-to-reset-to-a-particular-commit-with-the-git-reset-command)
- [Conclusion](#heading-conclusion)


## What is `HEAD` in Git?
In Git, `HEAD` points to the tip of the current branch, which is the commit where you last updated the current branch. So, `HEAD` is a reference to the most recent commit in the current branch.

When you create a new commit, Git automatically updates `HEAD` to point to the new commit. You can use the `git log --oneline` command to view the commit history of the current branch, and the commit at the top of the list is the one that `HEAD` is currently pointing to.

For example, in the sample code I’m using to show you how to reset to `HEAD` in Git, the current `HEAD` is the commit hash `d8cd0ee`, with the commit message `Linked JavaScript file`:

![Screenshot-2023-04-10-at-10.39.42](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-10.39.42.png)

`HEAD` can also be used to refer to the current working directory state. For example, if you make changes to files in your working directory but have not committed them, you can use the command `git diff HEAD` to see the differences between the working directory and the last commit:

![Screenshot-2023-04-10-at-10.43.29](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-10.43.29.png)

So, when we are talking about resetting to `HEAD`, it means resetting the current branch to the most recent commit. Apart from the `HEAD`, you can also reset to other commits with the `git reset --hard <commit-hash>` command.

You can even use some numbers with `HEAD` itself to go back to a particular commit. For instance, `HEAD{0}` means the `HEAD` itself, `HEAD{1}` means the commit before the `HEAD`, `HEAD{2}` means two commits before the `HEAD`, and so on.


## Why Reset to `HEAD` or Any Other Commit in Git?
Some of the situations that might warrant you reset to `HEAD` in Git include the following:
- undoing unwanted changes: if you have some uncommitted changes that confuse you and you want to get rid of them
- unstaging changes: if you have added changes to the staging area and you don’t want them anymore
- fixing a bad commit: if you have a commit already and you discovered there are issues with it that confuse you
- splitting a commit: if the commit you or a team member make involves too many changes that are different in scope


## How to Reset to `HEAD` in Git
For clarity, run `git log --oneline` to show your commit history:

![Screenshot-2023-04-10-at-10.39.42-1](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-10.39.42-1.png)

If it’s a large codebase and you want to see more details, you can run `git log --oneline --graph`:

![Screenshot-2023-04-10-at-11.04.56](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-11.04.56.png)

The `git log --oneline --graph` command includes a graphical representation of the commit history. This can be particularly useful in visualizing complex branching and merging scenarios.

In the two screenshots above, the `HEAD` is the commit hash `d8cd0ee`, with the commit message `Linked JavaScript file`. It is the previous commit I made.

To reset the codebase to that commit, I would run `git reset --hard HEAD`:

![Screenshot-2023-04-10-at-11.10.45](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-11.10.45.png)

You can see I got the response ` HEAD is now at d8cd0ee Linked JavaScript file`, – as you can see in the screenshot, too.

The `git reset --hard HEAD` command would discard all uncommitted changes even if you’ve added them to the staging area.


## How to Reset to a Particular Commit with the Git Reset Command
Apart from resetting to the `HEAD` itself, you can also reset to a particular commit.

First, run `git reflog` to see how each commit is associated with the `HEAD`:

![Screenshot-2023-04-10-at-11.17.37](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-11.17.37.png)

You can now run `git reset --hard HEAD@{n}` to go back to a particular commit. For example, I want to go back to the commit message `Linked CSS file`. So, I’ll run `git reset --hard HEAD@{5}` to go back to that commit:

![Screenshot-2023-04-10-at-11.25.13](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-11.25.13.png)

You can see that the `HEAD` has moved to another commit. I would run `git log --oneline` again to see the `HEAD` and other commits:

![Screenshot-2023-04-10-at-11.26.46](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-10-at-11.26.46.png)


## Conclusion
This article showed you how to reset your codebase to HEAD and to a particular commit using the `git reset --hard HEAD` and `git reset –hard HEAD@{n}` commands.

Be aware that the `git reset –hard HEAD` or `git reset –hard HEAD@{n}` command would remove your uncommitted changes, even if you staged them. If you don’t want your unstaged changes to be removed, you can use the `--soft` flag instead of the `--hard` flag.

Thank you for reading.



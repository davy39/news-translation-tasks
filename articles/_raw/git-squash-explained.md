---
title: Git Squash Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T18:07:00.000Z'
originalURL: https://freecodecamp.org/news/git-squash-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d82740569d1a4ca3827.jpg
tags:
- name: Git
  slug: git
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'What is Git Squash?

  One of the things that developers hear quite often regarding their pull requests
  is something like “That looks good to me, please squash and merge”. The fun part
  is that there is no such command like git squash (unless you create ...'
---

## **What is Git Squash?**

One of the things that developers hear quite often regarding their pull requests is something like “That looks good to me, please squash and merge”. The fun part is that there is no such command like `git squash` (unless you create an [alias](https://guide.freecodecamp.org/git/git-rebase) to it). 

To `squash` pull request means commonly to compact all the commits in this request into one (rarely to other number) to make it more concise, readable and not to pollute main branch’s history. To achieve this, a developer needs to use **interactive mode** of [Git Rebase](https://guide.freecodecamp.org/git/git-rebase) command.

Quite often when you develop some new feature you end up with several intermittent commits in your history - you develop incrementally after all. That might be just some typos or steps to final solution. Most of the time there is no use in having all these commits in the final public version of your code, so it’s more beneficial to have all of them compacted into one, single and final version.

So let’s assume you have following commit log in the branch you’d like to merge as part of pull request:

```shell
$ git log --pretty=oneline --abbrev-commit
30374054 Add Jupyter Notebook stub to Data Science Tools
8490f5fc Minor formatting and Punctuation changes
3233cb21 Prototype for Notebook page
```

Clearly we would prefer to have only one commit here, since there is no benefit in knowing what we started on writing and which typos we fixed there later. Only the final result is important.

So what we do is start an interactive rebase session from the current **HEAD** (commit **30374054**) to commit **3233cb21**, with the intention to combine the **3** latest commits into one:

```shell
$ git rebase -i HEAD~3
```

That will open an editor with something like the following:

```shell
pick 3233cb21 Prototype for Notebook page
pick 8490f5fc Minor formatting and Punctuation changes
pick 30374054 Add Jupyter Notebook to Data Science Tools
# Rebase
#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
```

As always, Git gives us a very nice help message where you can see the `squash` option we are looking for.

Currently the instructions for interactive rebase say to `pick` every specified commit **and** preserve the corresponding commit message. That is - don’t change anything. But we want to have only one commit in the end. 

So you can simply edit the text in you editor replacing `pick` with `squash` (or just `s`) next yo every commit we want to get rid of and save/exit the editor. That might look like this:

```shell
s 3233cb21 Prototype for Notebook page
s 8490f5fc Minor formatting and Punctuation changes
pick 30374054 Add Jupyter Notebook to Data Science Tools
```

When you close your editor after saving this change it will be reopened right away and will suggest that you choose and reword those commit messages. Something like this:

```shell
# This is a combination of 3 commits.
# The first commit's message is:
Prototype for Notebook page

# This is the 2nd commit message:

Minor formatting and Punctuation changes

# This is the 3rd commit message:

Add Jupyter Notebook to Data Science Tools

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
```

At this point you can delete all the messages you don’t want to be included in the final commit version. You can also reword them or just write commit message from scratch. 

Just remember that the new version will include all the lines that don't start with the `#` character. Once again, save and exit your editor.

Your terminal now should show a success message including `Successfully rebased and updated <branch name>` and the git log should show a nice and compacted history with only one commit. All intermediary commits are gone and we are ready to merge!

### **Warning about local and remote commit history mismatch**

This operation is slightly dangerous if you have your branch already published in a remote repository - you are modifying commit history after all. So it’s best to do the squash operation on a local branch before you do **push**. 

Sometimes, it will be already pushed - how would you create a pull request after all? In this case you’ll have to **force** the changes on the remote branch after doing the squashing, since your local history and branch history in the remote repository are different:

```shell
$ git push origin +my-branch-name
```

Do your best to make sure you are the only one using this remote branch at this point, or you’ll make the other developer's life harder when they have a history mismatch. But since **squashing** is usually done as the final operation on a branch before getting rid of it, it’s usually not so big of a concern.


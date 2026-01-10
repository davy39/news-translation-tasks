---
title: How to Use the Git Stash Command
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-11T15:05:10.000Z'
originalURL: https://freecodecamp.org/news/git-stash-commands
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/stahs-1.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'By Preethi⚡

  Let''s say you''re working on a serious feature of a branch in Git – like revamping
  the hero section of your marketing page. You''ll want to start doing experiments
  in your Revamp/Marketing-page-hero-section branch without screwing up master...'
---

By Preethi⚡

Let's say you're working on a serious feature of a branch in Git – like revamping the hero section of your marketing page. You'll want to start doing experiments in your `Revamp/Marketing-page-hero-section` branch without screwing up `master` or `main` branch.

Then suddenly you get call from your coworker to fix some bugs on the `login-page` branch. It's a serious issue. So, you try to switch to the `login-page` branch using `git switch login-page` or `git checkout login-page`. 

If you're switching branches with staged and unstaged changes, you might encounter any of the following scenarios:

First, while switching to the `login-page` branch, the staged and unstaged changes of the `Revamp/Marketing-page-hero-section` branch will come with you to the `login-page` branch. 

The `Revamp/Marketing-page-hero-section` branch contains some staged and unstaged changes on `index.html`.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/stash-1.png)

If we switch to the `login-page` branch, the staged and unstaged changes on `Revamp/Marketing-page-hero-section` branch come to `login-page` also.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/stash-1-1.png)

This muddies the `login-page` branch.

Next, sometimes Git doesn't allow you to switch branches without committing those changes. This is because you might lose the changes you made in your current branch or they may conflict with the destination branch (`login-page`). Whatever the reason, we can't switch the branch without committing or stashing the changes.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/error.png)

At the same time, you can't commit the half-done feature branch.

To help with this, you can use **Git stashing**. Stash means to store (changes) safely in a hidden place (the stash stack).

Stashing the current working directory's staged or unstaged changes or untracked files and then storing them in the stash stack reverts the current working directory to the last commit.

This is great to hear, right? Let's get our hands dirty with stash commands.

## **Table of Contents**

* [How to stash your changes 🤐](#heading-how-to-stash-your-changes)
* [How to stash untracked files❗](#heading-how-to-stash-untracked-files)
* [How to list stashes 📃](#heading-how-to-list-stashes)
* [Understanding the format of stash](#heading-understanding-the-format-of-stash)
* [How to show the latest stash 📺](#heading-how-to-show-the-latest-stash)
* [How to show an individual stash 📺](#heading-how-to-show-an-individual-stash)
* [How to apply the stash 🖊️](#heading-how-to-apply-the-stash)
* [How to delete a stash ☠️](#heading-how-to-delete-a-stash)
* [How to create a branch from stash](#heading-how-to-create-a-branch-from-stash)

## How to stash your changes 🤐

You can use any one of the below commands to **stash your staged and unstaged changes in the stash stack**. It undoes things to the latest commit and doesn't delete the changes, which are stored in the stash stack.

```
git stash
```

or

```
git stash save
```

## How to stash untracked files❗

Want to stash your untracked files in the stash stack? Just use the `--include-untracked` flag at the end of the command.

```
git stash --include-untracked
```

or use `-u` at the end of the command:

```
git stash -u
```

## How to list stashes 📃

Use the below command to list out all the stashes stored in the stash stack:

```
git stash list
```

Listing the stashes like below,

![Image](https://www.freecodecamp.org/news/content/images/2022/04/list-1.png)

* The latest stashes (stash@{0}) will be at the top of the stack.
*  The older stashes (stash@{1}) will be at the bottom of the stack.

## Understanding the format of stash

 The stash command lists the stashes in the below format:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/stash-list.jpg)
_A single stash format_

If you're not exactly clear on what this is saying 😅, it's completely fine. Let's explore some of the terms on the stash listing:

* **`Stash@{0}`** – this is just a stash reference. It refers to the particular stash. By default, `Stash@{0}` is always the latest stash.

_Note: Higher numbered stashes like stash@{3} are older stashes. The latest stashes always have the lowest number._

* **`WIP On fake` –** _fake_ is just a branch name like any other branch and WIP stands for Work In Progress. "_WIP on fake"_ means that `stash@{0}` was created on the branch "fake".
* **`fc99b30 add head line`** – _fc99b30_ is a Commit hash and _add head line_ is a commit message. At that time of stash creation, _fc99b30 add head line_ is the latest commit.

## How to show the latest stash 📺

Maybe you have multiple stashes in your stash stack and you're not able to tell which stash reference holds which changes. 

So, before you apply stashes on the current working branch, you can confirm and show the changes recorded in the stash with the below command:

```
git stash show
```

By default `git stash show` shows the changes recorded in the **latest** stash (stash@{0}) in the `--stat` format.

The `--stat` format shows only how many lines you've added and deleted on each of the modified files.

```
readme.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

If you want to show the recorded changes of the latest stash on **patch view**, use the `-p` flag at the end of the command, like this:

```
git stash show -p
```

If you also want to show **untracked files**, use the `-u` flag.

```
git stash show -u

```

or you can use the `--include-untracked` flag like this:

```
git stash show --include-untracked
```

You can show untracked files with the **patch format**:

```
git stash show -p -u
```

You can also show **only** untracked files with the patch format like this:

```
git stash show -p --only-untracked
```

Wow, you've already learned 10+ stash commands 🎉🎉

Let's look at some more so you can get the most out of stash.

## How to show an individual stash 📺

You can show the recorded changes of an individual stash by using **stash reference**.

```
git stash show stash@{1}

```

For the patch format, you guessed it right 👏🏻👏🏻 – use the `-p` flag.

```
git stash show stash@{1} -p

```

Want to show a stash with untracked files? Use this command:

```
git stash show stash@{1} -u

```

or this one:

```
git stash show stash@{1} --include-untracked

```

Whereas you can do this to show untracked files only:

```
git stash show stash@{1} --only-untracked
```

## How to apply the stash 🖊️

To apply the recorded changes of your latest stash on the current working branch as well as remove that stash from the stash stack, run this command:

```
git stash pop

```

_Note: We can apply stashes on any branch. It's not specific to the branch where the stash was created._

You can also apply the latest stash without removing the stash from the stash stack like this:

```
git stash apply

```

You can apply an earlier stash by using the stash reference:

```
git stash apply stash@{3}
```

## How to delete a stash ☠️

Want to clear all the stashes from stash stack? Use this command:

```
git stash clear

```

Want to delete a particular stash? Yes! you are right – you use the stash reference:

```
git stash drop stash@{2}
```

## How to create a branch from stash

![Image](https://www.freecodecamp.org/news/content/images/2022/03/branch-stash.png)

Yes, you can create a new branch from your latest stash. Just use this command:

```
git stash branch <branch_name>

```

For instance,

```
git stash branch demo

```

If you want to create a branch from an earlier stash, that's also possible by using stash reference:

```
git stash branch <branch_name> stash@{revision}
```

For instance,

```
git stash branch purple stash@{3}
```

## Wrapping Up

Such a long journey – but there was a lot to cover. If you can't remember each command, that's ok. The more often you use these commands, the more easily you'll remember them. You can refer to my [**git stash command cheat sheet**](https://gist.github.com/Preethi-Dev/fa8ae46a75761356dc1fa711376c8345) for a quick reference.

I hope today you grasped many new things about git stash. It's time to relax and have a coffee or tea 🍵. Let me know if you have any questions!


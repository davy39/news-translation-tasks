---
title: Renaming a Git Branch – How to Rename the Current Branch in Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-07T18:22:39.000Z'
originalURL: https://freecodecamp.org/news/renaming-a-git-branch-how-to-rename-the-current-branch-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/git-branches.png
tags:
- name: beginner
  slug: beginner
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'If you are using Git for version control, it’s likely you’ve created branches
  for various reasons.

  Since you have those branches in place, you might want to rename any of them if
  you find a typo, for example, or change the code''s purpose.

  In this art...'
---

If you are using Git for version control, it’s likely you’ve created branches for various reasons.

Since you have those branches in place, you might want to rename any of them if you find a typo, for example, or change the code's purpose.

In this article, I will show you how to rename the branch you’re working with without switching to another branch.

## How to Rename a Branch in Git
To rename a branch you are not currently working in, you usually run the command `git branch -m old-name new-name`.

For example, I’m currently on the main branch and I was able to rename `kolade-works` to `kolade-codes`.

![ss1-1](https://www.freecodecamp.org/news/content/images/2022/09/ss1-1.png) 

Proceed to the next section of this article to see how you can rename the current branch in Git.

## How to Rename the Current Branch in Git
The first thing you need to do is to run `git branch` so you can see the branches you have in place:

![ss2-1](https://www.freecodecamp.org/news/content/images/2022/09/ss2-1.png) 

Next, make sure you are in the branch you want to change the name of. You can do that by running `git checkout branch-name`. 

In this case, I want to change the `fix-bug` branch to `bug-fixes`. So I’ll run `git checkout fix-bug`:

![ss3-1](https://www.freecodecamp.org/news/content/images/2022/09/ss3-1.png) 

You can see that git bash shows me the branch I’m currently in now, which is `fix bug`.

To rename the branch, you need to run the command `git branch -m new-name`.

Remember I pointed out that I want to rename the `fix bug` branch to `bug-fixes`, so I’ll run `git branch -m bug-fixes`.

![ss4-1](https://www.freecodecamp.org/news/content/images/2022/09/ss4-1.png) 

`-m` in this situation is a flag that stands for `move`.

You can see the name of the branch has been successfully changed to `bug fixes`. 

To confirm that, you can run `git branch` again:

![ss5-1](https://www.freecodecamp.org/news/content/images/2022/09/ss5-1.png) 

## Wrapping Up
This article showed you how you can rename a local Git branch, especially if it’s the current branch. Even if it’s not the current branch, you’ve also learned about the command to use in that case.

If you want to learn about how to rename a remote branch too, I wrote [an article](https://www.freecodecamp.org/news/how-to-rename-a-local-or-remote-branch-in-git/) on it as well.

Thank you for reading.



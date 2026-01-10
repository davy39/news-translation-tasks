---
title: How to Rename a Local or Remote Branch in Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-10T19:03:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-rename-a-local-or-remote-branch-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/git.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: "Git is a version control system that software developers use to keep track\
  \ of changes in their applications and collaborate with others. \nOne helpful feature\
  \ of Git is branches. Different people working on a software project can work in\
  \ different bra..."
---

Git is a version control system that software developers use to keep track of changes in their applications and collaborate with others. 

One helpful feature of Git is branches. Different people working on a software project can work in different branches before merging their changes with the original code.

You can also add new features and fix bugs on a different branch without affecting the original code.

Sometimes, you might want to change the name of a branch because of typos or other errors, and that’s what I’m going to show you how to do in this guide.

## How to Rename a Local Git Branch
**Step 1**: To see the branches you have, run `git branch --list` or `git branch -a`
![ss-1-2](https://www.freecodecamp.org/news/content/images/2022/03/ss-1-2.png)

**Step 2**: Switch to the branch you want to rename by running `git checkout branch-name`. 

In this case, I’m going to switch to the `mistake-fixes` branch so I can rename it `bug-fixes`. 

To switch to a branch, run `git switch branch-name` or `git checkout branch-name`. 

**Step 3**: To rename the branch, run `git branch -m new-name`
![ss-2-2](https://www.freecodecamp.org/news/content/images/2022/03/ss-2-2.png)

You can see that the branch has been renamed from `mistake-fixes` to `bug-fixes`

If you are on another branch, for example, main and you want to rename the branch from there, run `git branch -m old-name new-name`

**N.B.**: Make sure you verify that the branch has been renamed by running `git branch -a` to see all branches.

## How to Rename a Remote Git Branch
Renaming a remote branch is not as straightforward as renaming a local branch. 

To be precise, renaming a remote branch is not direct – you have to delete the old remote branch name and then push a new branch name to the repo.

**Follow the steps below to rename a remote git branch**:

**Step 1**: Delete the old name by running `git push origin --delete old-branch-name`

In the example I’ve been using, this would be `git push origin --delete mistake-fixes`
![ss-3-1](https://www.freecodecamp.org/news/content/images/2022/03/ss-3-1.png)

**Step 2**: Reset the upstream branch to the name of your new local branch by running `git push origin -u new-branch-name`. 

So, for the example, this would be `git push origin -u bug-fixes`
![ss-4-1](https://www.freecodecamp.org/news/content/images/2022/03/ss-4-1.png)

To confirm that you successfully renamed the remote repo, log into your client's website and check the repo.

In the case of this tutorial, I’m using Github as the client and the renaming was successful:
![ss-5-1](https://www.freecodecamp.org/news/content/images/2022/03/ss-5-1.png)

## Conclusion

Branches are an awesome feature of Git that make your hosted software project safer.

Oftentimes, renaming branches locally and remotely might be inevitable, so that’s why I wrote this article to help you rename your branches without costly errors.

If you find this article helpful, don’t hesitate to share it with your friends and family.

Thank you for reading.



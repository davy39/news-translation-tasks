---
title: Git Reset to Remote Head – How to Reset a Remote Branch to Origin
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2021-03-08T20:14:39.000Z'
originalURL: https://freecodecamp.org/news/git-reset-to-remote-head-how-to-reset-a-remote-branch-to-origin
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/article-banner--1-.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Branching is a core concept in Git. It can help you set up a distributed
  workflow for team collaboration and makes your development process more efficient.

  When you''re using version control and you''re distributing features across branches,
  there''s a ...'
---

Branching is a core concept in Git. It can help you set up a distributed workflow for team collaboration and makes your development process more efficient.

When you're using version control and you're distributing features across branches, there's a lot of communication between your local computer and your online repository on GitHub. During this process, you might need to reset back to the project's original copy.

If resetting a branch scares you, then don't worry – this article will introduce you to remote branches, remote head, and how you can easily reset a remote branch to remote head.

## **Prerequisites**

* Basic knowledge of how to use the terminal.
    
* Git installed (Learn [how to install Git here](https://www.freecodecamp.org/news/git-clone-branch-how-to-clone-a-specific-branch/#how-to-install-git-on-windows) if you haven't already).
    
* Basic knowledge of GitHub and repositories.
    
* A grin on your face. 😉
    

## What is a Branch in Git?

A branch is a core concept in Git and GitHub that you'll use all the time. Branches help you manage different versions of one project.

The `main` branch is always the default branch in a repository and is considered "production and deployable code". You can create new branches like `prod-staging` or `prod-current` from the `main` branch.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-27-at-7.19.26-PM.png align="left")

*All branches in https://github.com/freeCodeCamp/freeCodeCamp*

### What is a Remote Branch in Git?

A **remote branch** is a reference to the state of the branches in a remote repository (a version of your project hosted on the internet or on a network like GitHub).

When you clone a repository, you pull data from a repository on the internet or an internal server known as the **remote** (it looks something like `(remote)/(branch)`).

## What is Origin (or Remote Head) in Git?

The word origin is an alias that Git created to replace the remote URL of a remote repository. It represents the default branch on a remote and is a local ref representing a local copy of the HEAD in the remote repository.

In summary, origin/HEAD represents the default branch on the remote, which is defined automatically when you clone a repository from the internet.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-08-at-8.23.47-AM.png align="left")

## How to Reset a Remote Branch to Origin in Git

Now that you have background knowledge of how remotes and branches work, let's solve our problem and reset a remote branch to origin using the `git reset --hard` command.

Before you do this (if this your first time), make sure that you back up your branch before you reset it in case something goes wrong. You can back it up like so:

```bash
git commit -a -m "Branch backup"
git branch branch-backup
```

Now run the command below to reset your remote branch to origin. If you have a different remote and default branch name (not `origin` or `main`, respectively), just replace them with the appropriate name.

```bash
git fetch origin
git reset --hard origin/main
```

If you have created some new files or directories, they may still remain after resetting. You can use the command below to clean up the working tree by recursively removing files from the previous branch that are not under version control.

```python
git clean -xdf
```

* The `-x` flag removes all untracked files, including ignored build directories.
    
* The `-d` flag allows Git to recurse into untracked directories when no path is specified.
    
* The `-f` flag overwrites the default Git clean configuration and starts cleaning untracked files and directories.
    

## Conclusion

If your remote repository’s name is not “origin” and the branch named is not “main” ​in the remote repository, don't forget to update the commands above with the appropriate names. You can always run `git remote show origin` to check this.

I hope this article has made you more comfortable with working with and resetting branches. You should also join the new [freeCodeCamp chat server](https://www.freecodecamp.org/news/introducing-freecodecamp-chat) to network with other learners and ask questions. Thanks for reading! 💙

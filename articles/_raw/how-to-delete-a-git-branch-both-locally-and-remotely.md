---
title: How to Delete a Git Branch Both Locally and Remotely
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T19:13:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e53740569d1a4ca3c89.jpg
tags:
- name: Git
  slug: git
seo_title: null
seo_desc: 'In most cases, it is simple to delete a Git branch. You''ll learn how to
  delete a Git brach locally and remotely in this article.

  TL;DR version

  // delete branch locally

  git branch -d localBranchName


  // delete branch remotely

  git push origin --delete ...'
---

In most cases, it is simple to delete a Git branch. You'll learn how to delete a Git brach locally and remotely in this article.

### TL;DR version

```bash
// delete branch locally
git branch -d localBranchName

// delete branch remotely
git push origin --delete remoteBranchName

```

## When to Delete branches

It is common for a Git repo to have different branches. They are a great way to work on different features and fixes while isolating the new code from the main codebase. 

Repos often have a `main` branch for the main codebase and developers create other branches to work on different features.

Once work is completed on a feature, it is often recommended to delete the branch.

## Deleting a branch LOCALLY

Git will not let you delete the branch you are currently on so you must make sure to checkout a branch that you are NOT deleting. For example: `git checkout main`

Delete a branch with `git branch -d <branch>`.

For example: `git branch -d fix/authentication`

The `-d` option will delete the branch only if it has already been pushed and merged with the remote branch. Use `-D` instead if you want to force the branch to be deleted, even if it hasn't been pushed or merged yet.

The branch is now deleted locally.

## Deleting a branch REMOTELY

Here's the command to delete a branch remotely: `git push <remote> --delete <branch>`.

For example: `git push origin --delete fix/authentication`

The branch is now deleted remotely.

You can also use this shorter command to delete a branch remotely: `git push <remote> :<branch>`

For example: `git push origin :fix/authentication`

If you get the error below, it may mean that someone else has already deleted the branch.

```bash
error: unable to push to unqualified destination: remoteBranchName The destination refspec neither matches an existing ref on the remote nor begins with refs/, and we are unable to guess a prefix based on the source ref. error: failed to push some refs to 'git@repository_name'

```

 Try to synchronize your branch list using:

```
git fetch -p

```

The `-p` flag means "prune". After fetching, branches which no longer exist on the remote will be deleted.

If you found this tutorial helpful, our nonprofit has more than 11,000 no-nonsense tutorials like this one. All free. Tell your friends. 😉


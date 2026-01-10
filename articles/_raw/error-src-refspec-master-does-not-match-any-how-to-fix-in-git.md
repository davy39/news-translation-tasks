---
title: 'Error: src refspec master does not match any – How to Fix in Git'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-01T13:58:44.000Z'
originalURL: https://freecodecamp.org/news/error-src-refspec-master-does-not-match-any-how-to-fix-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/refspec-master-error.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: "By Dillion Megida\nWhen working with Git, you may come across an error\
  \ that says \"src refspace master does not match any\". \nHere's what the error\
  \ means and how you can solve it.\nWhat Does src refspec master does not match any\
  \ Mean in Git?\nYou may get ..."
---

By Dillion Megida

When working with Git, you may come across an error that says "src refspace master does not match any". 

Here's what the error means and how you can solve it.

## What Does `src refspec master does not match any` Mean in Git?

You may get this error when you try to trigger a push from a local repository to a master repository like this:

```bash
git push origin master
```

This error can occur for different reasons.

The most likely reason this error will occur is that the `master` branch does not exist.

Perhaps you cloned a new repository and the default branch is `main`, so there's no master branch when you try to push for it.

You can display the remote branches connected to a local repository using the `git branch -b` command like this:

```bash
git branch -b

# results
#  origin/main
#  origin/feat/authentication
#  origin/other branches ...
```

With the above results, you can see that there is no `master` repository (`origin/master`). So when you try to push to that repository, you will get the "respec error".

This result also applies to any other branch that does not exist. Let's say, for example, I make changes and push to a remote `hello` branch that does not exist:

```bash
git add .
git commit -m "new changes"
git push origin hello
```

This command will produce the following error:

```bash
error: src refspec hello does not match any
```

## How to Fix the "src refspec master does not match any" Error

Now you are aware that the `master` branch does not exist. The solution to this error is to either create a local and remote `master` branch that you can push the commit to or to push the commit to an existing branch – maybe `main`.

You can create a remote `master` branch on a Git managed website (like GitHub) or you can do that directly from your terminal like this:

```bash
git checkout -b master

# add commit

git push origin master
```

These commands will create a `master` branch locally. And by pushing to `origin master`, the `master` branch will also be created remotely.

But if you do not want to create a `master` branch, you can use the existing default branch (which may be `main`) instead.

## Wrapping up

So if you get the `Error: src refspec master does not match any` error when you try to push to master, the most viable reason is that the `master` branch does not exist.




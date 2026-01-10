---
title: How to Sync Your Fork with the Original Git Repository
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-11T18:30:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-sync-your-fork-with-the-original-git-repository
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b23740569d1a4ca29ed.jpg
tags:
- name: Git
  slug: git
seo_title: null
seo_desc: 'By Johan Rin

  You''re contributing to an open-source project, and you noticed that your fork is
  out of sync with the original repository. How can you correct that?

  TL;DR version

  # Add a new remote upstream repository

  git remote add upstream https://git...'
---

By Johan Rin

You're contributing to an open-source project, and you noticed that your fork is out of sync with the original repository. How can you correct that?

## TL;DR version

```bash
# Add a new remote upstream repository
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git

# Sync your fork
git fetch upstream
git checkout master
git merge upstream/master
```

## Add a new remote upstream repository

You cloned your fork on your laptop and started to work on your issue. 

Did you know that your fork is an orphan? If you list the configured remote repository you will only see your fork as origin:

```bash
git remote -v
origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
```

There are no signs of parents! Where is the original repository?

We need to configure this information to restore the family relationship by adding a new remote upstream repository:

```shell
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

You saved the family! You can now see both the original repository and the fork:

```bash
git remote -v
origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
```

## Sync your fork

Everything is now set up. You can sync your fork with only 2 commands.

Be sure you're in the root of your project and also in the master branch. Otherwise, you can check out to the master branch:

```bash
git checkout master
Switched to branch 'master'
```

Now, you have to fetch the changes from the original repository:

```bash
git fetch upstream
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 7 (delta 5), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (7/7), 1.72 Kio | 160.00 Kio/s, done.
From https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY
   909ef5a..0b228a8  master     -> upstream/master
```

And merge the changes in your master branch:

```bash
git merge upstream/master
Updating 909ef5a..0b228a8
Fast-forward
 node.js/WorkingWithItems/batch-get.js               | 51 ++++++++++++++++++++++++++------------------------
 node.js/WorkingWithItems/batch-write.js             | 95 +++++++++++++++++++++++++++++++++++++++++++++++----------------------------------------------
 node.js/WorkingWithItems/delete-item.js             | 37 ++++++++++++++++++------------------
 node.js/WorkingWithItems/get-item.js                | 31 +++++++++++++++++--------------
 node.js/WorkingWithItems/put-item-conditional.js    | 51 +++++++++++++++++++++++++-------------------------
 node.js/WorkingWithItems/put-item.js                | 49 ++++++++++++++++++++++++------------------------
 node.js/WorkingWithItems/transact-get.js            | 51 ++++++++++++++++++++++++++------------------------
 node.js/WorkingWithItems/transact-write.js          | 79 ++++++++++++++++++++++++++++++++++++++++-------------------------------------
 node.js/WorkingWithItems/update-item-conditional.js | 51 ++++++++++++++++++++++++++------------------------
 node.js/WorkingWithItems/update-item.js             | 47 ++++++++++++++++++++++++----------------------
 10 files changed, 282 insertions(+), 260 deletions(-)
```

That's it! Your fork is now up to date.

Any questions? Feel free to contact me on [Twitter](https://twitter.com/johanrin)!


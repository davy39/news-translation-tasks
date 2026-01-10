---
title: 7 Git Hacks You Just Can’t Ignore
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-11T22:17:28.000Z'
originalURL: https://freecodecamp.org/news/7-git-hacks-you-just-can-t-ignore-41aea137727a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_RzIXapqnP4ZZ9twx5_KSg.jpeg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ritesh Shrivastav

  Git has probably saved more developers’ jobs than any other technology. As long
  as you frequently save your work with Git, you will always be able to roll back
  to how your code was in the past, thus reversing those late night mis...'
---

By Ritesh Shrivastav

Git has probably saved more developers’ jobs than any other technology. As long as you frequently save your work with Git, you will always be able to roll back to how your code was in the past, thus reversing those late night mistakes.

This said, Git’s command line interface is notoriously difficult to master. Let’s explore 7 tips for getting the most out of Git.

![Image](https://cdn-media-1.freecodecamp.org/images/0*n2QYqEj3coS_yKNl.png)
_photo credit: [xkcd](http://xkcd.com/" rel="noopener" target="_blank" title=")_

Usually 70% of using Git is only _add_, _commit_, _branch_ and _push / pull_. Most people are familiar with the flow that always moves in one direction. Ever wondered how to go back or undo steps if you added wrong files to the _repo_ or made a _commit_ with wrong message to a wrong _branch_?

If you are one of those who follows what is shown in the comic above, then this list of Git hacks is for you.

#### **1. Edit an incorrect commit message**

The commit message is going to live for a very long time in your code base, so you definitely want it to be something which correctly defines the changes.

This command will let you edit the most recent commit message. You need to make sure that there are no working copy changes or they too may get committed.

```
$ git commit --amend -m ”YOUR-NEW-COMMIT-MESSAGE”
```

In case you’ve already _pushed_ your _commit_ to the remote branch then you need to force push the commit with this command:

```
$ git push <remote> <branch> --force
```

You can follow this [Stack Overflow answer](http://stackoverflow.com/questions/179123/edit-an-incorrect-commit-message-in-git/179147#179147) for additional information.

#### **2. Undo ‘git add’ before committing**

What if you added some wrong files to your staging area, but did not make a commit? You can undo this by a simple command. If there’s only one file that needs to be removed then:

```
$ git reset <filename>
```

or if you want to unstage all your uncommitted changes:

```
$ git reset
```

You can follow this [Stack Overflow answer](http://stackoverflow.com/questions/348170/undo-git-add-before-commit/348234#348234) for additional information.

#### **3. Undo your most recent commit**

Sometimes you accidentally committed the wrong files or missed something in the first place. Here’s a three-step process to cover you in such cases.

```
$ git reset --soft HEAD~1# make changes to your working files as necessary$ git add -A .$ git commit -c ORIG_HEAD
```

When you execute the first command, Git will move your HEAD pointer back to the commit you made before making this one, so that you can move files or make changes as necessary.

Then you add all your changes, and when you finally execute the last command, Git will pop open your default text editor with the same commit message. You may edit this message if you want, or you can override this step altogether by using ‘-C’ instead of ‘-c’ in the final command.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eiuAyfDRLIr6ZKutQWbJZQ.gif)
_Git + spaghetti = spagitty_

#### **4. Revert your g_it repo_ to a previous commit**

‘Reverting’ can make a lot of senses in a many cases — especially if you’ve completely messed up a piece of code. The most common case is when you want a go back in time and explore a previous state of your codebase, then return back to your present state. This can be done by:

```
$ git checkout <SHA>
```

‘_<S_HA>‘ is the first 8–10 characters of the Hash Code of the commit where you want to go.

It will detach the HEAD, and let you fool around with no branch checked out. Don’t worry — detaching your head is not as scary as it sounds. If you want to make commits while you’re here, you can do so by creating a new branch here:

```
$ git checkout -b <SHA>
```

To go back to the present state, just checkout to the branch you were on previously.

You can follow this [Stack Overflow answer](http://stackoverflow.com/questions/4114095/revert-git-repo-to-a-previous-commit/4114122#4114122) for additional information.

#### **5. Undo a Git Merge**

You might have to do a _Hard Reset_ to the previous commit in order to undo a merge. What ‘merge’ basically does is it resets the index and updates the files in the working tree that are different between _<comm_it>_; an_d HEAD, but keeps those which are different between the index and working tree (i.e. which has changes that have not been added).

```
$ git checkout -b <SHA>
```

But there are always alternate ways of doing things in Git, and you can explore them [here](http://stackoverflow.com/questions/2389361/undo-a-git-merge?rq=1).

#### **6. Remove local (untracked) files from current Git branch**

Let’s say you happen to have a lot of files which are untracked (because they are not required), and you don’t want them to show up every time you use _git status_ . Here are a few ways to get around this problem:

```
$ git clean -f -n         # 1
```

```
$ git clean -f            # 2
```

```
$ git clean -fd           # 3
```

```
$ git clean -fX           # 4
```

```
$ git clean -fx           # 5
```

(1): _-n_ option will let you know what files will be removed if you run (2).

(2): This will remove all files as reported by command-(1).

(3): _-d_ if you also want to remove directories.

(4): _-X_ if you just want to remove ignored files.

(5): _-x_ if you want to remove both ignored and non-ignored files

Note the case difference of _X_ in last two commands.

For more information, you may explore [official git-clean documentation](http://git-scm.com/docs/git-clean).

![Image](https://cdn-media-1.freecodecamp.org/images/1*bLtPTIsKUeAQHPo2eGrKpw.png)
_Photo credit: [xkcd](http://xkcd.com/" rel="noopener" target="_blank" title=")_

#### **7. Delete a Git branch both locally and remotely**

To delete a local branch:

```
$ git branch --delete --force <branchName>
```

```
# OR use -D as a short-hand:
```

```
$ git branch -D
```

To delete a remote branch:

```
$ git push origin --delete <branchName>
```

#### Get Good with Git

Checkout [the official GitHub training documentation](https://training.github.com/kit/downloads/github-git-cheat-sheet) for a quick reference, and the [official Git documentation](https://git-scm.com/docs) to learn more about Git.

If you have a favorite Git hack, post it in the comments and tell us how you use it.

_Originally published at [blog.projectshrv.com](http://blog.projectshrv.com/7-git-hacks-you-cant-ignore/) on November 11, 2015._


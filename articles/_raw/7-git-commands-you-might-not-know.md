---
title: 'Git Secrets: 7 Commands You Might Not Know'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-21T17:56:21.000Z'
originalURL: https://freecodecamp.org/news/7-git-commands-you-might-not-know
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/header-image@1000x420.sketch.png
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: version control
  slug: version-control
seo_title: null
seo_desc: "By Tobias Günther\nOver the last couple years, Git has become a default\
  \ part of almost every developer's knowledge stack. But even though Git is so well-known,\
  \ there are many Git commands that are not. \nIn this short post, I'd like to show\
  \ you seven l..."
---

By Tobias Günther

Over the last couple years, Git has become a default part of almost every developer's knowledge stack. But even though Git is so well-known, there are many Git _commands_ that are not. 

In this short post, I'd like to show you seven little commands that can help you become more productive and well-versed with Git. Let's dive in.

## Finding Out What Has Changed in a File

Staying on top of things can be hard – especially if many people work on the same code base. 

To help you understand exactly _how_ (as well as _when_ and _by whom_) a file was changed, you can use the good old `git log` command – but with a little spice:

```cli
$ git log --since="3 weeks" -p index.html

```

Using "-p" makes sure you see the actual changes as diffs (and not only the commit's metadata). And the "--since" option helps you zero in on a recent time frame.

## Undoing Your Last Commit in Style

Sometimes we think a bunch of changes are ready for committing – but directly after making the commit, we notice that we were too quick. 

Changes could be missing, we could have hit the wrong branch, or a multitude of other problems could have happened... 

The only thing that's certain: we'd like to undo this last commit and get our changes back into our Working Copy!

We can use the `git reset` command with a special set of options:

```cli
$ git reset --mixed HEAD~1

```

The "--mixed" option makes sure that the changes contained in the commits being reset are NOT discarded. Instead, they are preserved as local changes in the Working Copy. 

Using the "HEAD~1" notation is a great shortcut to specify "the commit before the latest one" – which is exactly what we want in order to undo the very last commit.

Feel free to read more about this topic in [how to undo the last commit](https://www.git-tower.com/learn/git/faq/undo-last-commit?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=7-little-know-git-commands).

## Finding Out How a File is Different in Another Branch

After making some changes to a file in a feature branch, you might want to compare it to how it looks on another branch. To make a concrete example, let's say...

* you are currently on the "feature/login" branch and...
* want to understand how the file "myFile.txt" here...
* is different from its version on the "develop" branch.

The `git diff` command can do this if you provide the following parameters:

```cli
$ git diff develop -- myFile.txt

```

You'll then see a nice, clear diff that shows how exactly your file differs from its version on the other branch.

## Using "switch" Instead of "checkout"

The `git checkout` command has a multitude of different jobs and meanings. That's why, pretty recently, the Git community decided to publish a new command: `git switch`. As the name implies, it was made specifically for the task of switching branches:

```cli
$ git switch develop

```

As you can see, its usage is very straightforward and similar to "git checkout". But the huge advantage over the "checkout" command is that "switch" does NOT have a million other meanings and capabilities.

As it is quite a new member of the Git command family, you should check if your Git installation already includes it.

## Switch Back and Forth Between Two Branches

In some scenarios, it might be necessary for you to switch back and forth between two branches repeatedly. Instead of always writing out the branch names in full, you can simply use the following shortcut:

```cli
$ git switch -

```

Using the dash character as its only parameter, the "git switch" command will check out the _previously_ active branch. As said, this can come in very handy if you have to go back and forth between two branches a bunch of times.

## Using "git restore" to Undo Local Changes

Until recently, you had to use some form of `git checkout` or `git reset` when you wanted to undo local changes. 

But with the (relatively new) `git restore` command, we now have a command that was made exactly for this purpose. This sets it apart from "checkout" and "reset", because those commands have plenty of other use cases.

Here's a quick overview of the most important things you can do with "git restore":

```cli
# Unstaging a file, but leaving its actual changes untouched
$ git restore --staged myFile.txt

# Discarding your local changes in a certain file
$ git restore myFile.txt

# Undoing all of the local changes in the working copy (be careful)
$ git restore .

```

## Restoring a Historic Version of a File

The `git restore` command offers another very helpful option named "--source". With this option's help, you can easily restore any previous version of a specific file:

```cli
$ git restore --source 6bcf266b index.html

```

You simply mention the revision hash of the version you want to restore (and the name of the file, of course).

If you need some help _finding_ the right revision, you can use a [desktop Git client like Tower](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=7-little-know-git-commands): with a feature like its "File History", you can easily inspect only the changes that happened in a certain file – and then select a revision to restore.

## Discover the Power of Git

Although Git is so well-known these days, much of its power is still unknown to the public. It's true that you can "survive" with just a handful commands like commit, push, and pull. But this is like driving a Ferrari in first gear only!

If you're willing to dive a bit deeper, you will discover some of the more powerful features of Git. And these have the potential to not only make you more productive, but also – ultimately – a better developer!

If you want to learn more about Git, I recommend you take a look at the following _free_ resources:

* [The First Aid Kit for Git](https://www.git-tower.com/learn/git/first-aid-kit/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=7-little-know-git-commands): Learn how to undo and recover from mistakes in Git with a series of very short and simple videos.
* [The Git Cheat Sheet](https://www.git-tower.com/learn/cheat-sheets/git/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=7-little-know-git-commands): A popular cheat sheet to always have the most important commands at hand.

## About the Author

[Tobias Günther](https://twitter.com/gntr) is the CEO of [Tower](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=7-little-know-git-commands), the popular Git desktop client that helps more than 100,000 developers around the world to be more productive with Git.


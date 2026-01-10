---
title: The Ultimate Guide to Git Reset and Git Revert
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-11T17:10:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-git-reset-and-git-revert
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ffc740569d1a4ca45e7.jpg
tags:
- name: Git
  slug: git
seo_title: null
seo_desc: 'Welcome to our ultimate guide to the git reset and git revert commands.
  This tutorial will teach you everything you need to know about fixing common mistakes
  and undoing bad commits while using Git.

  Understand the Three Sections of a Git Project

  A Gi...'
---

Welcome to our ultimate guide to the `git reset` and `git revert` commands. This tutorial will teach you everything you need to know about fixing common mistakes and undoing bad commits while using Git.

## Understand the Three Sections of a Git Project

A Git project has the following three main sections:

1. Git directory
2. Working directory (or working tree)
3. Staging area

The **Git directory** (located in `YOUR-PROJECT-PATH/.git/`) is where Git stores everything it needs to accurately track the project. This includes metadata and an object database which includes compressed versions of the project files.

The **working directory** is where a user makes local changes to a project. The working directory pulls the project's files from the Git directory's object database and places them on the user's local machine.

Note: **Directory** is also known as **Repository** or short form repo. The repo on the user's local machine is called "Local repo" while the repo on git server is called "Remote repo".

The **staging area** is a file (also called the "index", "stage", or "cache") that stores information about what will go into your next commit. A commit is when you tell Git to save these staged changes. Git takes a snapshot of the files as they are and permanently stores that snapshot in the Git directory.

With three sections, there are three main states that a file can be in at any given time: modified, committed, or staged. You _modify_ a file any time you make changes to it in your working directory. Next, it's _staged_ when you move it to the staging area. Finally, it's _committed_ after a commit.

## Git Reset

The `git reset` command allows you to RESET your current head to a specified state. You can reset the state of specific files as well as an entire branch. This is useful if you haven't pushed your commit up to GitHub or another remote repository yet.

### Reset a file or set of files

The following command lets you selectively choose chunks of content and revert or unstage it.

```shell
git reset (--patch | -p) [tree-ish] [--] [paths]
```

### Unstage a file

If you moved a file into the staging area with `git add`, but no longer want it to be part of a commit, you can use `git reset` to unstage that file:

```shell
git reset HEAD FILE-TO-UNSTAGE
```

The changes you made will still be in the file, this command just removes that file from your staging area.

### Reset a branch to a prior commit

The following command resets your current branch's HEAD to the given `COMMIT` and updates the index. It basically rewinds the state of your branch, then all commits you make going forward write over anything that came after the reset point. If you omit the `MODE`, it defaults to `--mixed`:

```shell
git reset MODE COMMIT
```

The options for `MODE` are:

* `--soft`: does not reset the index file or working tree, but resets HEAD to `commit`. Changes all files to "Changes to be commited"
* `--mixed`: resets the index but not the working tree and reports what has not been updated
* `--hard`: resets the index and working tree. Any changes to tracked files in the working tree since `commit` are discarded
* `--merge`: resets the index and updates the files in the working tree that are different between `commit`and HEAD, but keeps those which are different between the index and working tree
* `--keep`: resets index entries and updates files in the working tree that are different between `commit`and HEAD. If a file that is different between `commit` and HEAD has local changes, the reset is aborted

### Important Note About Hard Resets

Be very careful when using the `--hard` option with `git reset` since it resets your commit, staging area and your working directory. If this option is not used properly then one can end up losing the code that is written.

## Git Revert

Both the `git revert` and `git reset` commands undo previous commits. But if you've already pushed your commit to a remote repository, it is recommended that you do not use `git reset` since it rewrites the history of commits. This can make working on a repository with other developers and maintaining a consistent history of commits very difficult.

Instead, it is better to use `git revert`, which undoes the changes made by a previous commit by creating an entirely new commit, all without altering the history of commits.

### Revert a commit or set of commits

The following command lets you revert changes from a previous commit or commits and create a new commit.

```shell
git revert [--[no-]edit] [-n] [-m parent-number] [-s] [-S[<keyid>]] <commit>…
git revert --continue
git revert --quit
git revert --abort
```

### Common options:

```shell
  -e
  --edit
```

* This is the default option and doesn't need to be explicitly set. It opens your system's default text editor and lets you edit the new commit message before commit the revert.
* This option does the opposite of `-e`, and `git revert` will not open the text editor.
* This option prevents `git revert` from undoing a previous commit and creating a new one. Rather than creating a new commit, `-n` will undo the changes from the previous commit and add them to the Staging Index and Working Directory.

```shell
  --no-edit
```

```shell
-n
-no-commit
```

### Example.

Let's imagine the following situation: 1.) You are working on a file and you add and commit your changes. 2.) You then work on a few other things, and make some more commits. 3.) Now you realize, three or four commits ago, you did something that you would like to undo - how can you do this?

You might be thinking, just use `git reset`, but this will remove all of the commits after the one you would like to change - `git revert` to the rescue! Let's walk through this example:

```shell
mkdir learn_revert # Create a folder called `learn_revert`
cd learn_revert # `cd` into the folder `learn_revert`
git init # Initialize a git repository

touch first.txt # Create a file called `first.txt`
echo Start >> first.txt # Add the text "Start" to `first.txt`

git add . # Add the `first.txt` file
git commit -m "adding first" # Commit with the message "Adding first.txt"

echo WRONG > wrong.txt # Add the text "WRONG" to `wrong.txt`
git add . # Add the `wrong.txt` file
git commit -m "adding WRONG to wrong.txt" # Commit with the message "Adding WRONG to wrong.txt"

echo More >> first.txt # Add the text "More" to `first.txt`
git add . # Add the `first.txt` file
git commit -m "adding More to first.txt" # Commit with the message "Adding More to first.txt"

echo Even More >> first.txt # Add the text "Even More" to `first.txt`
git add . # Add the `first.txt` file
git commit -m "adding Even More to First.txt" # Commit with the message "Adding More to first.txt"

# OH NO! We want to undo the commit with the text "WRONG" - let's revert! Since this commit was 2 from where we are not we can use git revert HEAD~2 (or we can use git log and find the SHA of that commit)

git revert HEAD~2 # this will put us in a text editor where we can modify the commit message.

ls # wrong.txt is not there any more!
git log --oneline # note that the commit history hasn't been altered, we've just added a new commit reflecting the removal of the `wrong.txt`
```

And with that you're one step closer to getting your black belt in Git.


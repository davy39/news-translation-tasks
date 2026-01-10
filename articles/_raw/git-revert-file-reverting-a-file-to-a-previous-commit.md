---
title: Git Revert File – Reverting a File to a Previous Commit
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-08-18T15:39:20.000Z'
originalURL: https://freecodecamp.org/news/git-revert-file-reverting-a-file-to-a-previous-commit
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/pexels-tatiana-fet-1105766.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Git is a version control system that helps teams and individuals track
  and record changes made to a file or an entire project.

  When working with Git, you often commit your changes and then push them to a remote
  repository.

  Suppose you have made a lot...'
---

Git is a version control system that helps teams and individuals track and record changes made to a file or an entire project.

When working with Git, you often commit your changes and then push them to a remote repository.

Suppose you have made a lot of commits and later realize that your current version of changes is wrong. Or you discover a situation that requires you to revert to a previous commit, like a strange bug.

Manually changing each line of code in your file to its original state or a specific commit state and doing a new commit can lead to a messy commit history. Reverting the file is a much cleaner way to handle it.

There are many possible approaches, but in this article, you will learn the best approach, the `git checkout` method.

If you are in a rush, here is the command:

```bash
$ git checkout SHA-HASH -- file/file-path
```

But suppose you are not in a rush. Let’s start by first learning how to locate all previous commits and their SHA hash. Then we'll see how to revert a file to a previous commit.

## How to Find the Commit SHA/ID

There are many ways to get each commit's SHA and details. The best method is to use the command below in your terminal:

```bash
$ git log
```

This command will show a list of all commits you have made in your projects to all files and their hash codes:

![](https://paper-attachments.dropbox.com/s_E7BE213D0AE03E619B0ABFE8B0450BCDCD832D2BDB3CB303964F1820DADBA52A_1660857327507_image.png align="left")

But a more straightforward command to use is the command below, where you attach the `oneline` option:

```bash
$ git log --oneline
```

**Note:** The `oneline` option displays the output as one commit per line.

```bash
198d425 (HEAD -> main) initial
c368a1c new removal
bcbef35 updated readme 2
da9cc5f (origin/main) updated Readme
a5150af first commit
```

Using this command alone would return all commits made on that project. If you want to revert a particular file to a previous commit, you must first see all commits made to that file.

To do this, add the file name to the command:

```bash
$ git log --oneline README.md
```

In a situation where the file is located in another folder, you can either navigate your terminal to the folder or use the file path in the command as seen below:

```bash
$ git log --oneline src/App.js
```

This will return only commits for the specified file and the commit SHA hash followed by the commit message. You will use the SHA hash to revert your file:

```bash
198d425 (HEAD -> main) initial
c368a1c new removal
bcbef35 updated readme 2
da9cc5f (origin/main) updated Readme
a5150af first commit
```

## How to Revert a File to a Previous Commit

So now that you know how to get the SHA code, you can use the `git checkout` command to revert your file to any commit you want by also passing the file name or file path:

```bash
$ git checkout da9cc5f -- README.md

Or

$ git checkout 55a1dff -- src/App.js
```

Just make sure you want to revert a file before doing so, because you will discard your current local changes to the file. Git will replace the file with the specified committed version. Use this only if you are sure and don’t want those unsaved local changes.

## Wrapping Up

In this article, you have learned how to revert a file to a previous commit with the `git checkout` command.

It is essential to know that when you revert, you'll need to commit the changes again (the reverted changes). You can do this with the standard commit command:

```bash
$ Git commit -m 'commit message'
```

Then you can push that commit to the remote repository as you wish.

You can learn more about Git in this [video](https://www.freecodecamp.org/news/git-for-professionals/) or [article](https://www.freecodecamp.org/news/learn-git-and-version-control-in-an-hour/).

Have fun coding!

---
title: Git Undo Merge – How to Revert the Last Merge Commit in Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-30T17:40:00.000Z'
originalURL: https://freecodecamp.org/news/git-undo-merge-how-to-revert-the-last-merge-commit-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/puppy-g3ddb72a98_1920.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Branching is an integral part of Git because it lets you work without tampering
  with code that''s already in production.

  When you finish working with a branch other than main, you''ll want to merge it
  with the main so the feature or bug fix you just in...'
---

Branching is an integral part of Git because it lets you work without tampering with code that's already in production.

When you finish working with a branch other than `main`, you'll want to merge it with the main so the feature or bug fix you just integrated will be reflected.

But what if you finish merging and realize you forgot to do one more thing? Or what if you accidentally merge when you are not ready to?

You can undo almost anything in Git. So, in this article, I will show you how to undo a merge in Git so you can revert to the last commit you made.

## How to Undo a Merge Commit in Git

You can use the Git reset command to undo a merge. 

Firstly, you need to check for the commit hash (or id) so you can use it to go back to the previous commit. 

To check for the hash, run `git log` or `git reflog`. `git reflog` is a better option because things are more readable with it.
![ss1-2](https://www.freecodecamp.org/news/content/images/2022/03/ss1-2.png)

When you get the hash of the commit you want to get back to, run `git reset --hard commit-before-the-merge`:
![ss-2-5](https://www.freecodecamp.org/news/content/images/2022/03/ss-2-5.png)

You should see some things get removed from your code editor when you run the command.

If you are not sure of the hash of the last commit, you can run `git reset --hard HEAD~1` to go back to the commit before the merge:
![ss-3-3](https://www.freecodecamp.org/news/content/images/2022/03/ss-3-3.png)

Note that when you use the `--hard` flag to undo a merge, any uncommitted change will be reverted.

## A Better Way to Undo a Merge in Git

Since the methods discussed above will revert uncommitted changes, Git provides a safer flag which is `--merge`. 

To undo a merge with the `--merge` flag, run `git reflog` to see the hashes of commits, then run `git reset --merge previous-commit`:
![ss4-1](https://www.freecodecamp.org/news/content/images/2022/03/ss4-1.png)

You can also use the HEAD keyword with the `--merge` flag by running `git reset --merge HEAD~1`:
![ss5](https://www.freecodecamp.org/news/content/images/2022/03/ss5.png)

**N.B.**: If you don’t get a response from this command when you use the `--merge` flag, don’t worry, it works.

## Conclusion
In this article, you learned how to undo a merge in Git, so you can undo a mistaken or unwanted merge and work more efficiently with Git.

Here is the take-away with the `--hard` and `--merge` flags while using them to undo a merge: the `--hard` flag removes uncommitted changes, while the `--merge` flag keeps uncommitted changes.

Thank you for reading!



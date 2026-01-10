---
title: The Ultimate Guide to Git Merge and Git Rebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-26T18:08:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-git-merge-and-git-rebase
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f05740569d1a4ca4068.jpg
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Welcome to our ultimate guide to the git merge and git rebase commands.
  This tutorial will teach you everything you need to know about combining multiple
  branches with Git.

  Git Merge

  The git merge command will merge any changes that were made to the ...'
---

Welcome to our ultimate guide to the `git merge` and `git rebase` commands. This tutorial will teach you everything you need to know about combining multiple branches with Git.

## Git Merge

The `git merge` command will merge any changes that were made to the code base on a separate branch to your current branch as a new commit.

The command syntax is as follows:

```shell
git merge BRANCH-NAME
```

For example, if you are currently working in a branch named `dev` and would like to merge any new changes that were made in a branch named `new-features`, you would issue the following command:

```shell
git merge new-features
```

**Note:** If there are any uncommitted changes on your current branch, Git will not allow you to merge until all changes in your current branch have been committed. To handle those changes, you can either:

Create a new branch and commit the changes

```shell
git checkout -b new-branch-name
git add .
git commit -m "<your commit message>"
```

Stash them

```shell
git stash               # add them to the stash
git merge new-features  # do your merge
git stash pop           # get the changes back into your working tree
```

Abandon all of the changes

```shell
git reset --hard        # removes all pending changes
```

## Git Rebase

Rebasing a branch in Git is a way to move the entirety of a branch to another point in the tree. The simplest example is moving a branch further up in the tree. Say we have a branch that diverged from the master branch at point A:

```text
        /o-----o---o--o-----o--------- branch
--o-o--A--o---o---o---o----o--o-o-o--- master
```

When you rebase you can move it like this:

```text
                                   /o-----o---o--o-----o------ branch
--o-o--A--o---o---o---o----o--o-o-o master
```

To rebase, make sure you have all the commits you want in the rebase in your master branch. Check out the branch you want to rebase and type `git rebase master` (where master is the branch you want to rebase on).

It is also possible to rebase on a different branch, so that for example a branch that was based on another branch (let's call it feature) is rebased on master:

```text
                            /---o-o branch
           /---o-o-o-o---o--o------ feature
----o--o-o-A----o---o--o-o-o--o--o- master
```

After `git rebase master branch` or `git rebase master` when you have checked out the branch, you'll get:

```text
           /---o-o-o-o---o--o------ feature
----o--o-o-A----o---o--o-o-o--o--o- master
                                  \---o-o branch
```

### Git rebase interactive in the console

To use `git rebase` in the console with a list of commits you can choose, edit or drop in the rebase:

* Enter `git rebase -i HEAD~5` with the last number being any number of commits from the most recent backwards you want to review.
* In vim, press `esc`, then `i` to start editing the test.
* On the left hand side you can overwrite the `pick` with one of the commands below. If you want to squash a commit into a previous one and discard the commit message, enter `f` in the place of the `pick` of the commit.
* Save and quit your text editor.
* When rebase is stopped, make the necessary adjustments, then use `git rebase --continue` until rebase is successful.
* If it rebases successfully then you need to force push your changes with `git push -f` to add the rebased version to your remote repository.
* If there is a merge conflict, there are a number of ways to fix this. One way is to open the files in a text editor and delete the parts of the code you do not want. Then use `git add <file name>` followed by `git rebase --continue`. You can skip over the conflicted commit by entering `git rebase --skip`, stop rebasing by running `git rebase --abort` in your console.

```text
pick 452b159 <message for this commit>
pick 7fd4192 <message for this commit>
pick c1af3e5 <message for this commit>
pick 5f5e8d3 <message for this commit>
pick 5186a9f <message for this commit>

# Rebase 0617e63..5186a9f onto 0617e63 (30 commands)
#
# Commands:
# p, pick = use commit
# r, reword = use commit, but stop to edit the commit message.
# e, edit = use commit, but stop to amend or add commit.
# s, squash = use commit, meld into previous commit and stop to edit the commit message.
# f, fixup = like "squash", but discard this commit's log message thus doesn't stop.
# x, exec = run command (the rest of the line) using shell
# d, drop = remove commit
#
# These lines can be re-ordered; they are executed from top to bottom. 
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
```

## Merge Conflicts

A merge conflict is when you make commits on separate branches that alter the same line in conflicting ways. If this happens, Git will not know which version of the file to keep in an error message similar to the following:

```shell
CONFLICT (content): Merge conflict in resumé.txt Automatic merge failed; fix conflicts and then commit the result.
```

If you look at the `resumé.txt` file in your code editor, you can see where the conflict took place:

```shell
<<<<<<< HEAD
Address: 808 South Street
=======
Address: 505 North Street
>>>>>>> updated_address
```

Git added some additional lines to the file:

* `<<<<<<< HEAD`
* `=======`
* `>>>>>>> updated_address`

Think of  `=======` as the dividing line of the conflict. Everything between `<<<<<<< HEAD` and `=======` is the content of the current branch that the HEAD ref is pointing to. On the other hand, everything between  `=======` and `>>>>>>> updated_address` is the content in the branch being merged, `updated_address`.

## Git Merge vs Git Rebase

Both `git merge` and `git rebase` are very useful commands, and one is not better than the other. However, there are some very important differences between the two commands that you and your team should take into consideration.

Whenever `git merge` is run, an extra merge commit is created. Whenever you are working in your local repository, having too many merge commits can make the commit history look confusing. One way to avoid the merge commit is to use `git rebase` instead.

`git rebase` is a very powerful feature. That being said, it is **risky** as well if it is not used in the right way. `git rebase` alters the commit history, so use it with care. If rebasing is done in the remote repository, then it can create a lot of issues when other developers try to pull the latest code changes from the remote repository. Remember to only run `git rebase` in a local repository.

That's all you need to know to merge and rebase with the best of 'em.


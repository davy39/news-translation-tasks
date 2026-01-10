---
title: Git Delete Branch – How to Remove a Local or Remote Branch
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-26T17:00:36.000Z'
originalURL: https://freecodecamp.org/news/git-delete-branch-how-to-remove-a-local-or-remote-branch
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/elaine-alex-OFMEk4ar9RA-unsplash--1-.jpg
tags:
- name: clean code
  slug: clean-code
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Git is a popular version control system and an essential tool in a web
  developer''s toolkit.

  Branches are a powerful and integral part of working with Git.

  In this article, you will learn the basics about how to remove local and remote
  branches in Git...'
---

Git is a popular version control system and an essential tool in a web developer's toolkit.

Branches are a powerful and integral part of working with Git.

In this article, you will learn the basics about how to remove local and remote branches in Git.

## What are Branches in Git?

A branch is a pointer to a commit.

Git branches are a snapshot of a project and its changes, from a specific point in time.

When working on a big project, there is the main repository with all the code, often called `main` or `master`.

Branching allows you to create new, independent versions of the original main working project. You might create a branch to edit it to make changes, to add a new feature, or to write a test when you're trying to fix a bug. And a new branch lets you do this without affecting the main code in any way.

So to sum up – branches let you make changes to the codebase without affecting the core code until you're absolutely ready to implement those changes. 

This helps you keep the codebase clean and organized.

## Why Remove Branches in Git?

So you've created a branch to hold the code for a change you wanted to make in your project.

You then incorporated that change or new feature into the original version of the project.

That means you no longer need to keep and use that branch, so it is a common best practice to delete it so it doesn't clutter up your code.


## How to Delete a Local Branch in Git

Local branches are branches on your local machine and do not affect any remote branches.

The command to delete a local branch in Git is:

```
git branch -d  local_branch_name
```

- `git branch` is the command to delete a branch locally.
- `-d` is a flag, an option to the command, and it's an alias for `--delete`. It denotes that you want to delete something, as the name suggests.  - `local_branch_name` is the name of the branch you want to delete.

Let's look into this in a bit more detail with an example.

To list out all the local branches, you use the following command:

```
git branch
```

I have two, branches, `master` and `test2`. I am currently on the `test2` branch as the `(*)` shows:

![Screenshot-2021-08-25-at-4.13.14-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-4.13.14-PM.png)

I want to delete the `test2` branch, but it is not possible to delete a branch you are currently in and viewing.

If you try to do so, you'll get an error that will look something like this:

![Screenshot-2021-08-25-at-4.17.50-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-4.17.50-PM.png)

So before deleting a local branch, make sure to switch to another branch  that you do NOT want to delete, with the `git checkout` command:

```
git checkout branch_name

#where branch_name is the name of the branch you want to move to
#in my case the other branch I have is master, so I'd do:
#git checkout master
```

Here's the output:

![Screenshot-2021-08-25-at-4.20.40-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-4.20.40-PM.png)

Now I can delete the branch:

![Screenshot-2021-08-25-at-5.10.13-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-5.10.13-PM.png)

The command for deleting a local branch that we just used doesn't work in all cases.

If the branch contains unmerged changes and unpushed commits, the `-d` flag will not allow the local branch to be deleted.

This is because the commits are not seen by any other branches and Git is protecting you from accidentaly losing any commit data.

If you try to do this, Git will show you an error:

![Screenshot-2021-08-25-at-5.23.46-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-5.23.46-PM.png)

As the error suggests, you'll need to use the `-D` flag instead:

```
git branch -D local_branch_name
```

The `-D` flag, with a capital D (which is an alias for `-- delete --force`), forcefully deletes the local branch, regradless of its merged status.

But note that **you should use this command should with caution**, as there is no prompt asking you to confirm your actions. 

Use it only when you are absolutely sure you want to delete a local branch.

If you didn't merge it into another local branch or push it to a remote branch in the codebase, you will risk losing any changes you've made.

![Screenshot-2021-08-25-at-5.33.41-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-5.33.41-PM.png)


## How to Delete a Remote Branch in Git

Remote branches are separate from local branches.

They are repositories hosted on a remote server that can be accessed there. This is in comparison to local branches, which are repositories on your local system.

The command to delete a remote branch is:

```
git push remote_name -d remote_branch_name
```

- Instead of using the `git branch` command that you use for local branches, you can delete a remote branch with the `git push` command.
- Then you specify the name of the remote, which in most cases is `origin`.
- `-d` is the flag for deleting, an alias for `--delete`.
- `remote_branch_name` is the remote branch you want to delete.

Now, let's see an example of how to go about deleting a remote branch.

To view any remote branches, you use this command:

```
git branch -a
```

The `-a` flag (an alias for `--all`) shows all branches – both local and remote.

![Screenshot-2021-08-25-at-7.35.31-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-7.35.31-PM.png)

I have two local branches called `master` and `test` and two remote branches `origin/master` and `origin/test`.

The `-r`, an alias for `--remotes`, shows *only* the remote repositories.

![Screenshot-2021-08-25-at-7.37.12-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-7.37.12-PM.png)

I want to delete the remote `origin/test` branch, so I use the command:

```
git push origin -d test
```

Output:

![Screenshot-2021-08-25-at-7.39.34-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-7.39.34-PM.png)

This deleted the `test` branch in the remote repository named `origin`.

The `origin/test` remote repository is no longer there:

![Screenshot-2021-08-25-at-7.42.01-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-7.42.01-PM.png)

## Conclusion

You now know how to delete local and remote branches in Git.

If you want to learn more about Git, you can watch the following courses on freeCodeCamp's YouTube channel:

- To learn how to get set up with Git, and for an overview of important Git commands and the typical git workflow – [Git and GitHub for beginners - Crash course](https://www.youtube.com/watch?v=RGOj5yH7evk).
- To go more in depth on branches and learn how they work – [Git Branches Tutorial](https://www.youtube.com/watch?v=e2IbNHi4uCI&t=6s).

Thanks for reading and happy learning!







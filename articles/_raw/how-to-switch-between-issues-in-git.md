---
title: How to Switch Between Issues in Your Local Git Repository
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2020-06-08T17:59:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-switch-between-issues-in-git
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a74740569d1a4ca25b6.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'On my journey to open source I ran into a simple (yet tricky) situation
  that can trip you up if you do it wrong. And that''s what we''ll discuss in this
  article.

  Participating in the open source community means you''re contributing to the development
  of...'
---

On my journey to open source I ran into a simple (yet tricky) situation that can trip you up if you do it wrong. And that's what we'll discuss in this article.

Participating in the open source community means you're contributing to the development of free or open source software. There are many organizations that are always welcoming contributors to their codebases.

To get started with open source, you need to have a basic understanding of version control tools such as [Git](https://git-scm.com/). Contributors use Git to track changes in project files and it also helps people coordinate their work on those files.

## Prerequisites

1. Have [Git](https://git-scm.com/downloads) installed
2. Have a basic understanding of Git

## Why issues? 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/issue-scrrenshot-1.PNG)

Issues in a repository can be used to keep track of tasks, ideas, bugs, or enhancements for the project you are working on. Basically, they provide you with a description of what the task entails. 

To take up an issue the project administrators need to assign that particular issue to you. This way other team members will know that someone is working on the issue.

## Working on an issue 

To start working on an issue, you need to make a clone or copy of the target repository using the Git clone command on your local machine. 

```git
git clone <url of repository>
```

Create an upstream allowing you to keep track of latest upstream (i.e original repository) changes. This way Git keeps you informed when there are changes so you can update the cloned repository.

```git
git remote add upstream <url of the original repository>

```

To preview the list of available remote and tasks that can be performed (fetch and push) type:

```git
git remote -v
```

To stay updated with the latest changes, you always need to try to fetch from the upstream. This way you get all the commits from every team member who also worked on various features.

```git
git fetch <upstream>/<master>
```

Moving forward, you'll need to merge the commits of other contributors to the local repository. 

```git
git merge <upstream>/<master>


```

The goal of Git merge is to make the local copy of the master branch match exactly the same as the upstream copy of the master branch.

Next, create a branch for the issue you were assigned. Why do you have to create a branch? And what is a branch used for? Let's investigate further.

### Git branch 

A branch gives you a snapshot of the changes that have been made. When a commit is made, Git stores the information from the commit. This provides a pointer that can later be used to reference or track the changes that were made. This is why it's helpful to create a branch when working on new task, bug fix, or any other feature. 

When we get started, Git provides us with a master branch. The master branch contains working code. To avoid mixing your changes with production code, you need to create a new branch.

To create a branch you need to enter the following Git command:

```git
git checkout -b <descriptive-branch-name>
```

This command creates a new branch based on the current branch, although you can also specify the branch where you want your new branch created.

```git
git checkout -b <descriptive-branch-name> <target-branch-name>

```

To list all available branches in your repository, type:

```git
git branch
```

When the task you're working on has been completed, push changes on the local repository for review. After that, create a pull request to notify project administrators on the current state of the assigned task.

```git
git push -u origin <descriptive-branch-name>

```

## Now how do I switch to work on the next issue?  

Create a different branch with a descriptive name, like this:

```git
git checkout -b <descriptive-branch-name> <target-branch-name>

```

Once we have our branch we'll use a utility command from [hub](https://hub.github.com/). The command will help us fetch code from upstream, and it'll also run the merge (if you install the [hub utility)](https://github.com/github/hub#installation). 

```git
hub sync
```

The command retrieves the upstream changes and merges them with the newly created branch. You can always check for changes with your branch and upstream using the Git status command:

```git
git status
```

Now you can proceed and work on the new branch. Just remember to commit your changes and push to the remote branch as we did above. 

### Mistakes you might make.

You might make a mistake while working on multiple issues - which can lead to to deleting commits from a branch. 

Here's a sample walk-through of what can be done to erase unwanted commits from a branch:

**Step 1:** Switch into the branch where you would like to remove unwanted commits:

```git
git checkout <descriptive-branch-name>

```

**Step 2:** Run the records of commits made to the branch. This will help you decide which commits you would like to retain based on the unique **Commit Hash** (SHA1 40 character checksum of the commits contents) usually in this form: **da034f6ff3e856b5ba155bc01def0847a1c4ed7e**.

```git
git log
```

It's also worth noting that if you are looking to retain the most recent commit (say the last on) you can simply do this:

```git
git log -n 1
```

**Step 3:** Since you want to discard all the other commits on that branch, simply apply that one single commit to the branch. Discard and apply are two steps:

First, discard all commits on the branch with:

```git
git reset --hard <upstream>/<master>


```

In simple terms, the above command tells Git to throw away all staged and un-staged changes. It'll forget everything on the current local branch and make it exactly the same as the `upstream/master`.

Second, apply that one single commit to the branch with the command:

```git
git cherry-pick Hash

//where Hash is a commit hash from other branch
```

This command picks a single reference (i.e commit) by default from a branch and applies it to another. 

**Step 4:** When you run `git status` it will report that your branch `<origin>/<descriptive-branch-name>` diverged. Since that's expected we need to force the remote to only contain those changes we have cherry-picked. 

To get this done, we need to use a command to help erase the remote history and replace it with a different history:

```git
git push --force origin
```

This command will discard the extra commits on the remote, just as we discarded the extra commits on the local copy. This is dangerous because it is one of the very few git commands that will discard something - so be careful when using it.

Now when you run `git status` it reports that the branch is up to date with `<origin>/<descriptive-branch-name>`. This shows you that the operation was carried out successfully.

Thank you for reading ?! Big shout out to [Mark Waite](https://github.com/markewaite)?  

Follow me on [twitter](https://twitter.com/devlarri).


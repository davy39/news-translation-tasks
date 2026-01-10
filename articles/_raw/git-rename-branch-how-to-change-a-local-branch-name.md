---
title: Git Rename Branch – How to Change a Local Branch Name
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-11-03T15:42:12.000Z'
originalURL: https://freecodecamp.org/news/git-rename-branch-how-to-change-a-local-branch-name
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/mila-tovar-NTiW908Uc1A-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: Git
  slug: git
- name: how-to
  slug: how-to
- name: version control
  slug: version-control
seo_title: null
seo_desc: "As you are building out a project, there might be times where you need\
  \ to rename a local branch. But how do you do that in Git?\nIn this article, I will\
  \ provide you with two methods for renaming  local branches in Git. \nHow to Rename\
  \ a Branch in Git –..."
---

As you are building out a project, there might be times where you need to rename a local branch. But how do you do that in Git?

In this article, I will provide you with two methods for renaming  local branches in Git. 

## How to Rename a Branch in Git – Method #1

### Step 1: Make sure you are in the root directory for your project

You will first need to open up your terminal and then `cd` (change directory) to the root of your project.

For example, this is what the command would look like if you were in the home directory and wanted to `cd` into the project which is located on the Desktop. 

```
cd Desktop/project-name
```

This is an example of changing directories to a project named `Happy_Messages_Bot`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-10.30.01-PM.png)

### Step 2: Go to the branch you want to rename

We can use the `git checkout` command to switch to another branch. 

```
git checkout branch-name
```

In this example, I want to switch over to the `test-branch` I created.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-10.39.57-PM.png)

### Step 3: Use the `-m` flag to change the name of the branch

This is what the command would look like to change the name of the branch:

```
git branch -m new-branch-name
```

In this example, I want to change my branch name from `test-branch` to `test-branch2`.

```
git branch -m test-branch2
```

You can use `git status` to see your new branch name.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-10.52.02-PM.png)

## How to Rename a Branch in Git – Method #2

We can rename the local branch in just one command without having to use `git checkout`.

### Step 1: Make sure you are in the master/main branch

To check if you are in the master/main branch, run `git status`:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-11.02.20-PM.png)

If you are not in the master/main branch, then you will need to run `git checkout master` or `git checkout main`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-11.05.28-PM.png)

### Step 2: Use the `-m` flag to rename the branch

You can use this syntax to rename the old branch to something new.

```
git branch -m old-branch new-branch
```

This is what it would look like to rename the `test-branch` to `test-branch2`. 

```
git branch -m test-branch test-branch2
```

To see your new branch name, you can run `git branch` which will list all of your branches. 

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-02-at-11.15.52-PM.png)

Those are two methods for renaming local branches in Git.



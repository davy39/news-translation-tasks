---
title: How to Rename a Local and Remote Branch in Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-05T17:19:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-rename-local-and-remote-git-branch
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Rename-Git-Branch.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'By Chaitanya Prabuddha

  Have you ever needed to rename a Git branch? If so, this article will assist you
  in resolving the problem.

  Git makes it simple to rename a git branch both locally and remotely. Let''s take
  a look at the solution.

  Why would you n...'
---

By Chaitanya Prabuddha

Have you ever needed to rename a Git branch? If so, this article will assist you in resolving the problem.

Git makes it simple to rename a git branch both locally and remotely. Let's take a look at the solution.

## Why would you need to rename a branch in Git?

Git branches are distinct stages in the development of your project. They give you a way to work alongside your master branch while keeping it free of clutter and unfinished code.

In a hurry, you might name a branch that doesn't accurately describe the code, or you might want to rename it. Most people want to change their branch names in these situations.

## How to rename a local git branch

You can use this command if you are already in the local branch you want to rename.

```
git branch -m <new_name>
```

If you're on a different branch and want to rename it, use the command below:

```
git branch -m <old_name> <new_name>
```

Use the command below to determine your current branch name:

```
git status 
```

## How to rename a remote git branch

If you want to rename a branch that has already been pushed to a remote repository, use the command below:

```
git push origin -u <new_name>
```

And now you will need to delete the old name. To do this, use this command:

```
git push origin --delete <old_name>
```

To check the changes you just did, login into your client portal, and check the repository you just changed.

**That's a wrap! Isn’t it so simple? 🥳**

I also write regularly on my newsletter. You can signup directly here. **👇👇**

<iframe src="https://thelearners.substack.com/embed" height="100"></iframe>



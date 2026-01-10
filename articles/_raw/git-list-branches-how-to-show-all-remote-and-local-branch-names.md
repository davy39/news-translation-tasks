---
title: Git List Branches – How to Show All Remote and Local Branch Names
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-29T17:55:45.000Z'
originalURL: https://freecodecamp.org/news/git-list-branches-how-to-show-all-remote-and-local-branch-names
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/magnolia-trees-gffa46356f_1920.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: "Git is a version control system used by software developers to track changes\
  \ in applications and collaborate on projects. \nOne feature that makes Git more\
  \ dynamic is branches. Developers working on a project can work in different branches\
  \ before merg..."
---

Git is a version control system used by software developers to track changes in applications and collaborate on projects. 

One feature that makes Git more dynamic is branches. Developers working on a project can work in different branches before merging their changes with the original code or the main branch.

Sometimes, you might want to see the branches you and other collaborators have created. And that’s what I’m going to show you how to do in this article.

## How to Show All Remote and Local Branch Names

To see local branch names, open your terminal and run `git branch`:
![ss-1-4](https://www.freecodecamp.org/news/content/images/2022/03/ss-1-4.png)

**N.B** the current local branch will be marked with an asterisk. In addition, if you’re using Git bash or WSL’s Ubuntu as your terminal, the current local branch will be highlighted in green.

To see all remote branch names, run `git branch -r`:
![ss-2-4](https://www.freecodecamp.org/news/content/images/2022/03/ss-2-4.png)

To see all local and remote branches, run `git branch -a`:
![ss3](https://www.freecodecamp.org/news/content/images/2022/03/ss3.png)

You can see detailed information such as the local or remote branches in use, commit ids, and commit messages by running `git branch -vv` or `git branch -vva`:
![ss4](https://www.freecodecamp.org/news/content/images/2022/03/ss4.png)

## Conclusion

This article showed you how to list branches while working with Git.

Being able to list the Git branches of a project can help you learn more about the project and get to know what your team members are working on.

If you find this article helpful, don’t hesitate to share it with others who might need it.

Thank you for reading.



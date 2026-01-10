---
title: Git Push Local Branch to Remote – How to Publish a New Branch in Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-09T20:36:25.000Z'
originalURL: https://freecodecamp.org/news/git-push-local-branch-to-remote-how-to-publish-a-new-branch-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/code-5290465_1920.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: null
seo_desc: "Git branches let you add new features without tampering with the live version\
  \ of your projects. And if you work in a team, different developers might have unique\
  \ branches they work on. \nIn the long run, you'll have to push those independent\
  \ branches ..."
---

Git branches let you add new features without tampering with the live version of your projects. And if you work in a team, different developers might have unique branches they work on. 

In the long run, you'll have to push those independent branches to a remote server. For example, GitHub, GitLab, and others.

In this article, I’ll show you how to push a local git branch to a remote server. It doesn’t matter whether you are yet to push at all. You might even have pushed your main branch and want to push another branch. I’m going to show you everything from scratch.

## How to Push the Main Branch to Remote
If you want to push the main branch to remote, it’s possible you’re pushing for the first time. Before you attempt to push to remote, make sure you’ve executed these commands:
- `git init` for initializing a local repository
- `git add .` to add all your files that the local repository
- `git commit -m ‘commit message’` to save the changes you made to those files

![ss1-2](https://www.freecodecamp.org/news/content/images/2022/09/ss1-2.png)

To push the main repo, you first have to add the remote server to Git by running `git remote add <url>`.

To confirm the remote has been added, run `git remote -v`:

![ss2-2](https://www.freecodecamp.org/news/content/images/2022/09/ss2-2.png) 

To finally push the repo, run `git push -u origin <branch-name>`
(“main” is the name of that branch for me). It could be master or Main for you. Initially, it was “master”, so I ran `git branch -M main` to change it. 

If you have not configured Git to use a credential helper, you will be asked for your GitHub username and PAT (personal access token):

![ss3-2](https://www.freecodecamp.org/news/content/images/2022/09/ss3-2.png) 

That’s how you push the main branch for the first time.

## How to Push a New Branch to Remote
If you have another branch you’ve worked at that you want to push to remote, you’ll still use the `git push` command, but in a slightly different way.

As a reminder, to create a new branch, you run `git branch branch-name`. And to switch to that branch so you can work there, you have to run `git switch branch name` or `git checkout branch-name`.

To push the branch to the remote server, run `git push –u origin <branch name>`. In my case, the name of that branch is `bug-fixes`. So, I have to run `git push -u origin bug-fixes`:

![ss4-2](https://www.freecodecamp.org/news/content/images/2022/09/ss4-2.png) 

To confirm that the branch has been pushed, head over to GitHub and click the branches drop-down. You should see the branch there:

![ss5-2](https://www.freecodecamp.org/news/content/images/2022/09/ss5-2.png)

## Conclusion
This article showed you how to push a new branch to remote. Apart from that, we also looked at how you would push to a remote server the first time.

If you want to learn more about git, check out other [freeCodeCamp articles on Git and GitHub](https://www.freecodecamp.org/news/tag/git/).




---
title: How to make your first Git commit
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-08-18T16:23:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-first-git-commit-a0581cb774f7
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9caaf4740569d1a4ca8e54.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'Note: This is the second video in my Git for beginners series. Watch the
  first video here.

  Today we’re going to talk about how to make your first Git commit.

  If you open up Fork from where we left off before, you’ll see the project screen.
  If you cli...'
---

Note: This is the second video in my Git for beginners series. [Watch the first video here](https://zellwk.com/blog/setting-up-git).

Today we’re going to talk about how to make your first Git commit.

If you open up Fork from [where we left off before](https://medium.freecodecamp.org/how-to-set-up-a-git-client-in-just-a-few-minutes-3d78b8d2264f), you’ll see the project screen. If you click on changes, the screen will split into two parts.

On the left of the screen, you’ll see a section that says unstaged files. Below this section, you’ll see another section that says staged files.

To the right, you’ll see a placeholder that shows Fork’s icon. At the bottom, you’ll see a few fields:

1. A commit message field
2. A description field
3. An amended checkbox
4. A commit button

This is called the **staging area**. This is where you decide what files you want to save into Git.

![Image](https://cdn-media-1.freecodecamp.org/images/0*z0qu2lqJZwZ87_WP.png)

### Staging a file

Before you save anything, you need to make a change in the Git repository.

Open up your Git project in a text editor like VS Code. Create a file called `index.html` and give it some HTML to start with.

Once you save this file, you’ll see this file in the staging area. It should appear in the unstaged files section of the staging area.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_5EDE_vPmD2X9uaY.png)

**An unstaged file is a file that has been changed since you last committed into the Git repository.**

If you want to commit a file (in this case, the `index.html` file), you can click on the file and click on stage. This file will be moved from the unstaged files section into the staged files section.

![Image](https://cdn-media-1.freecodecamp.org/images/0*m6JbL6aElj11k9yl.png)

**When you have a file in the staged file section**, what you’re saying is **you want to save that file when you make a commit**.

If you click on the file, you’ll see the lines of code (in green) that will be saved into the repository.

### Creating a commit

To create a commit, you write your commit message at the bottom right corner, then click the “create commit” button.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ZtPjvgZI42RK1Rwr.png)

Once you click on the commit button, the staged files will disappear from the staging area. This is because the files are saved — there are no more new changes for the file in the repository.

### Committing more than one file

You can commit many files at the same time. To do so, you need to change many files.

In this example, I added a CSS file and a JavaScript file to the repository. I also added code to the `index.html` file to point to the CSS and JavaScript files.

If you go back into Fork now, you should see the folders and files that are changed.

![Image](https://cdn-media-1.freecodecamp.org/images/0*o7IRLjIX4NW2xLZg.png)

To commit all three files at once, you select the files and click the stage button. Then, you write your commit message and commit the files.

![Image](https://cdn-media-1.freecodecamp.org/images/0*fLy8BmEjCBv0gsh8.png)

### Checking the Git History

If you click on All Commits in the sidebar, you’ll see the commits you have made so far. In some Git clients, this is called Git History.

### Exercise

Try to make a few commits into your Git repository with Fork. In the next video, I’ll show you how to push to a git remote and how to pull from a git remote.

Thanks for reading. Did this article help you in any way? If I did, [I hope you consider sharing it](http://twitter.com/share?text=Your%20first%20Git%20commit%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/your-first-git-commit/&hashtags=). You might just help someone who felt the same way you did before reading the article. Thank you.

This article was originally posted at [my blog](https://zellwk.com/blog/your-first-git-commit)_._

Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer.


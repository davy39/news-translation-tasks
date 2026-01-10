---
title: What not to save into a Git repository
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-14T22:18:40.000Z'
originalURL: https://freecodecamp.org/news/what-not-to-save-into-a-git-repository-29779ee94b96
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca75a740569d1a4ca769d.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: tips
  slug: tips
seo_title: null
seo_desc: 'You should not commit these four types of files into your Git repository.


  Files that don’t belong to the project

  Files that are automatically generated

  Libraries (depends on the situation)

  Credentials


  Files that don’t belong to the project

  Files li...'
---

You should not commit these four types of files into your Git repository.

1. Files that don’t belong to the project
2. Files that are automatically generated
3. Libraries (depends on the situation)
4. Credentials

### Files that don’t belong to the project

Files like `.DS_Store` (for Mac OS), `Thumds.db` (for Windows), `.vscode` (for code editors) have nothing to do with your project.

They should not be checked in.

### Files that are automatically generated

This includes files from preprocessors (like Sass to CSS). You don’t check in the CSS. You check in the Sass files.

If you use JavaScript compilers like Webpack or Rollup, you don’t check in the generated JavaScript file. You check in the code you write.

### Libraries

If you don’t use a package manager, you should check in your libraries. This is because if you want to download the library, you have to:

1. Google for the library
2. Get to the website
3. Find the link
4. Download the library
5. Put into your project

This process is tedious. If your code needs the library to work, you should check in the library.

On the other hand, if you use a package manager, you shouldn’t check in a library because you can install the library with a single command like `npm install`.

### Credentials

You shouldn’t store credentials like usernames, passwords, API keys and API secrets.

If someone else steals your credentials, they can do nasty things with it. I almost lost $40,00 to $60,000 because a friend accidentally exposed my amazon credentials. Luckily, the amount was waived.

If you don’t want to get into sticky situations like I did, then don’t store your credentials in a Git repository.

Thanks for reading. Did this article help you in any way? If you did, [I hope you consider sharing it](http://twitter.com/share?text=What%20not%20to%20save%20into%20a%20Git%20repository%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/what-not-to-save-into-a-git-repo/&hashtags=). You might help someone out. Thank you!

This article was originally posted at [my blog](https://zellwk.com/blog/what-not-to-save-into-a-git-repo).  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer.


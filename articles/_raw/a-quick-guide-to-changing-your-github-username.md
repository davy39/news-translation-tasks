---
title: A quick guide to changing your GitHub username
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-07-31T14:45:37.000Z'
originalURL: https://freecodecamp.org/news/a-quick-guide-to-changing-your-github-username
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/barcat.png
tags:
- name: GitHub
  slug: github
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'Some additional steps to consider after making a change to your username
  on GitHub.

  This being the 2,38947234th and probably last time I’ll change my username, (marriage
  is permanent, right?) I thought I’d better write a quick post on how this transi...'
---

## Some additional steps to consider after making a change to your username on GitHub.



This being the 2,38947234th and probably last time I’ll change my username, (marriage is permanent, right?) I thought I’d better write a quick post on how this transition can be achieved as smoothly as possible. You can read [official instructions on how to change your GitHub username](https://help.github.com/en/articles/changing-your-github-username?source=post_page---------------------------) here, and they will tell you how to do it and what happens. The following is a quick guide to some things to consider _afterwards._

# Where to make changes

1. Change username in [GitHub account settings.](https://github.com/settings/admin?source=post_page---------------------------)
2. If using GitHub Pages, change name of your “username.github.io” repository.
3. If using other services that point to your “username.github.io” repository address, update them.
4. If using Netlify, you _may_ want to sign in and reconnect your repositories. (Mine still worked, but due to a possibly unrelated issue, I’m not positive.)
5. Sign in to Travis CI and other integrations (find them in your repository Settings tab -> Integrations & services). This will update your username there.
6. Update your local files and repository links with _very carefully executed_`find` and `sed` commands, and push back changes to GitHub.
7. Redeploy any websites you may have with your updated GitHub link.
8. Fix any links around the web to your profile, your repositories, or Gists you may have shared.

# Local file updates

Here are some suggestions for strings to search and replace your username in.

* `github.com/username` (References to your GitHub page in READMEs or in website copy)
* `username.github.io` (Links to your GitHub Page)
* `git@github.com:username` (Git config remote ssh URLs)
* `travis-ci.com/username` (Travis badges in READMEs)
* `shields.io/github/.../username` (Shields badges in READMEs, types include `contributors`, `stars`, `tags`, and more)

You can quickly identify where the above strings are located using this command for each string:

`grep -rnw -e 'foobar'`

This will recursively (`r`) search all files for strings matching the whole (`w`) pattern (`e`) provided and prefix results with the line numbers (`n`) so you can easily find them.

Using `find` and `sed` can make these changes much faster. See [this article on search and replace](https://victoria.dev/verbose/how-to-replace-a-string-in-a-dozen-old-blog-posts-with-one-sed-terminal-command/?source=post_page---------------------------).

Enjoy your new handle! (I hope it sticks.)


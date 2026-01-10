---
title: How to Push an Empty Commit in Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-10T21:04:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-push-an-empty-commit-with-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Push.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'By Chaitanya Prabuddha

  In this article, we will discuss how to push a commit in Git without making any
  changes.

  Git makes this process of pushing an empty commit super simple. It''s like pushing
  a regular commit, except that you add the --allow-empty ...'
---

By Chaitanya Prabuddha

In this article, we will discuss how to push a commit in Git without making any changes.

Git makes this process of pushing an empty commit super simple. It's like pushing a regular commit, except that you add the `--allow-empty` flag.

```
git commit --allow-empty -m "Empty-Commit"
```

You will now need to push this to the main directory. To do this, you can use this command:

```
git push origin main
```

You can see that the commit has been pushed to your branch without any changes after running the above commands.

### Why would you need push an empty commit?

It's possible that you'll need to start a build without making any changes to your project. Or you may not be able to manually initiate the build. The only method to start the build is to use Git. You can start your build without making any modifications to the project by pushing an empty commit.

**That's a wrap! Isn’t it so simple? 🥳**

I also write regularly on my newsletter. You can signup directly here. **👇👇**

<iframe src="https://thelearners.substack.com/embed" height="100"></iframe>



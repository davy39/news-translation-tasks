---
title: How to use Git stash as temporary storage
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-10-22T20:38:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-stash-as-temporary-storage-84a0a1e37a43
coverImage: https://cdn-media-1.freecodecamp.org/images/0*5QOUGLobId0ruTih.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Let’s say you’re coding on your development branch. And you get a notice
  that there’s a bug in the production branch.

  You want to check for the bug, but you don’t want to lose the work you’ve created
  on the development branch. You also don’t want to ...'
---

Let’s say you’re coding on your development branch. And you get a notice that there’s a bug in the production branch.

You want to check for the bug, but you don’t want to lose the work you’ve created on the development branch. You also don’t want to commit what you’ve written because it’s not done yet.

What do you do? You can’t commit and you can’t switch branches. If you switch branches, things that aren’t committed will flow over to the branch you switched to.

What you want to do is save the changes somewhere temporary while you switch over to another branch. **A Git stash is that temporary storage.**

### Using a Stash with Git Fork

To use a stash, you need to start with some uncommitted code. For this lesson, we’re going to use the following piece of code as the uncommitted changes:

```
<!-- Some uncommitted code in index.html -->
```

```
<main>  <p> A new paragraph</p></main>
```

To stash this code, you can click on the stash button.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5QOUGLobId0ruTih.png)

Once you click on the stash button, Fork will ask you to leave a message. This message indicates what the stash is about.

Since stashes are temporary, you can use whatever name you want. We’re going to call it “Temp storage”.

![Image](https://cdn-media-1.freecodecamp.org/images/0*iPtWYwszjCoDgTMx.png)

Once you create a new stash, you’ll find it in the Stashes section on the sidebar.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dbSJ_kDKSTlCKbSt.png)

Note: You won’t be able to see the changes in this stash, but that’s not a problem because you won’t have to. What you want to do is switch your branch, finish what you need to do and switch back.

In this case, we’re going to check out to the `master` branch. When you do so, notice you don’t see the uncommitted code we wrote above in both the `master` and `develop` branches.

### Applying stashed changes

You can go back to the branch you were at, then right-click on your stash and select Apply stash.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Iajs_VZW2LF43WnM.png)

Fork will ask you whether to delete the stash when you do so. I usually delete the stash because I don’t want to keep more than one stash at one time.

![Image](https://cdn-media-1.freecodecamp.org/images/0*xBHNRhlClGgyIUiu.png)

Once you apply the stash, you’ll be able to see the changes you made.

```
<!-- You'll see your uncommitted code again! -->
```

```
<main>  <p> A new paragraph</p></main>
```

### Wrapping up

Stashes are temporary storage spaces where you can store your code. When you’ve stored your code, you can move to other branches to do something else.

When you’re done, you can put your code back from the stash.

With Git Stash, you won’t have to worry about losing any uncommitted changes!

Thanks for reading. Did this article help you in any way? If you did, [I hope you consider sharing it](http://twitter.com/share?text=How%20to%20use%20Git%20stashes%20as%20a%20temporary%20storage%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/git-stash/&hashtags=). You might help someone out. Thank you!

This article was originally posted at [zellwk.com](https://zellwk.com/blog/git-stash).  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better front-end developer.


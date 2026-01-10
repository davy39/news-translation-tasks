---
title: How to undo changes in Git
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-12-07T16:47:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-undo-changes-in-git-e1da7930afdb
coverImage: https://cdn-media-1.freecodecamp.org/images/0*6JjR02sGP4FgM6zj.png
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: videos
  slug: videos
seo_title: null
seo_desc: 'You may already know that Git is like a save point system. What you generally
  learn with Git initially is to learn to save your changes and commit them to a remote
  repository. But how do you undo a change, and go back to a previous state?

  That’s what...'
---

You may already know that Git is like a save point system. What you generally learn with Git initially is to learn to save your changes and commit them to a remote repository. But how do you undo a change, and go back to a previous state?

That’s what we’re going to cover within this article.

I’ve covered the contents in this article in a video if you like learning by watching instead of reading.

### Local vs Remote

It’s more complicated to undo something that’s already on the remote. This is why you want to keep things on your local until they’re kind of confirmed.

### Four common scenarios

We’ll be covering the following four common scenarios

1. Discarding local changes
2. Amending the previous commit
3. Rolling back to a previous commit
4. Reverting a commit that has been pushed to the remote

Note: In the screen shots below, I’ve used the [Fork for Mac OS](https://git-fork.com/) Git Client. You can do the same in other similar Git clients.

#### Scenario 1: Discarding local changes

The first scenario is when you’ve created some changes. They’re not committed yet. And you want to delete these changes.

Let’s say we want to create a new feature. We’re going to add some HTML and CSS into the project:

```html
<!--In index.html-->
<div class="feature"></div>
```

```css
/* In CSS file */
.feature {
  font-size: 2em; 
  /* Other styles */
}
```

To discard these changes:

1. Go to the staging area
2. Select the files where you want to discard changes
3. Right click on the files
4. Select discard changes

![Image](https://cdn-media-1.freecodecamp.org/images/0*6JjR02sGP4FgM6zj.png)

#### Scenario 2: Amending the previous commit

When you have created a commit and you missed out some changes and you want to add these changes in the previous commit message.

1. Go to the staging area
2. Stage the files to commit
3. Click on the amend checkbox
4. Edit your commit message
5. Commit

![Image](https://cdn-media-1.freecodecamp.org/images/0*1wkCc2i9X8JWsBz4.png)

#### Scenario 3: Rolling back to a previous commit

You already have a few commits in your local repository. You decide that you don’t want these commits anymore and you want to “load” your files from a previous state.

1. Go into the Git History
2. Right click the commit you want to roll back to
3. Select reset `branch` to here

![Image](https://cdn-media-1.freecodecamp.org/images/0*IwWQ9XZNRmCaVvb8.png)

> Note: You can only reset to a commit that hasn’t been pushed into the remote.

#### Scenario 4: Reverting a commit that has been pushed to the remote

If you have a commit that has been pushed into the remote branch, you need to revert it.

> Reverting means undoing the changes by creating a new commit. If you added a line, this revert commit will remove the line. If you removed a line, this revert commit will add the line back.

To revert, you can:

1. Go to the Git history
2. Right click on the commit you want to revert
3. Select revert commit
4. Make sure `commit the changes` is checked.
5. Click revert

![Image](https://cdn-media-1.freecodecamp.org/images/0*29rgArX4rXn3aH6x.png)

![Image](https://cdn-media-1.freecodecamp.org/images/0*fUD5rUESrzaMnbXu.png)

### Other scenarios

GitHub has a useful article that shows you how to undo almost everything with Git. It will be helpful if you face other scenarios. Read it [here](https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/).

Thanks for reading. Did this article help you in any way? If it did, [I hope you consider sharing it](http://twitter.com/share?text=Undoing%20changes%20in%20Git%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/git-undo/&hashtags=). You might help someone out. Thank you!

This article was originally posted at [my blo](https://zellwk.com/blog/git-undo)g.  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer.


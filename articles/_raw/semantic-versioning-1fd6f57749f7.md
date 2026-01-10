---
title: 'A quick intro to Semantic Versioning: what it is, and why we use it'
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-10-03T04:58:47.000Z'
originalURL: https://freecodecamp.org/news/semantic-versioning-1fd6f57749f7
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FQw6EFwILTQfFjY3.png
tags:
- name: Git
  slug: git
- name: semantics
  slug: semantics
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'We create numbers like 1.0.0 and 1.0.1 for releases and hotfixes when we
  work on Git Flow. What do these numbers represent, and why do we use them?

  These numbers represent the version number of the product we put out in the world.
  We use them because...'
---

We create numbers like `1.0.0` and `1.0.1` for releases and hotfixes when we work on Git Flow. What do these numbers represent, and why do we use them?

These numbers represent the version number of the product we put out in the world. We use them because we’re following a best practice called Semantic Versioning.

**When we use Semantic Versioning, developers will know whether a change will break their code.** The numbers give a clue to the kind of changes that have occurred.

Many popular projects use Semantic Versioning. Examples are React and Vue.

### Understanding Semantic Versioning

**A semantic version has three numbers.** The rightmost number is a patch version.

#### Patch Versions

**Patch versions are used for bugfixes.** There are no functionality changes. (That’s why we use a patch version when we released a hotfix in the [previous lesson](https://zellwk.com/blog/git-flow)).

When you increase a new patch, **you increase the rightmost number by 1.** From 1, you increase it to 2, then to 3, and so on.

**If your patch number is 9** when you increase the patch version again, **you increase it to 10,** then 11, then 12, and so on. (There are no limits to the numbers.)

![Image](https://cdn-media-1.freecodecamp.org/images/0*FQw6EFwILTQfFjY3.png)

#### Minor versions

The second number is called the minor version number. It is **used when you release new functionality** in your project.

When you increase the minor version, you also increase it by one. **But** **when you increase the minor version, you must reset the patch version to zero.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*ljytd-KnDUHIcPP_.png)

#### Major versions

The leftmost number is a major version. When you increase the major version, you tell people that there are **backward-incompatible changes**. People may experience breakage if they use the next version.

**When you increase the major version number, you reset both patch version and minor versions.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*HDxRFW5vBUnkN1pN.png)

#### Pre-releases

If you want to create a pre-release (like an alpha or beta version), you can add a `-`, followed by the words `alpha` or `beta`.

There are **no hard and fast rules for pre-releases**, so you can name them anything you want. Usually, we use alpha or beta, followed by a number, like `alpha1`.

### Starting a project

Most people start projects with `0.1.0`. When you’re ready to release the project to the public, you increase the version to `1.0.0`.

Thanks for reading. Did this article help you in any way? If you did, [I hope you consider sharing it](http://twitter.com/share?text=Semantic%20Versioning%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/semantic-versioning/&hashtags=). You might help someone out. Thank you!

This article was originally posted on [_my blog_](https://zellwk.com/blog/semantic-versioning)_._   
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer.


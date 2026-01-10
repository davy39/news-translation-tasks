---
title: How to host on GitHub Pages with Git Submodules
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T17:25:51.000Z'
originalURL: https://freecodecamp.org/news/hosting-on-github-pages-with-git-submodules-36815856c3f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NNm6FdS2dbSlstMML1yduw.png
tags:
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Felix Wu

  Git Submodules is one of the most terrific but exhausting features in Git.I mean,
  we all love Git, right? But have you ever tried using Git Submodules?

  Actually, standalone Git Submodules aren’t hard to understand. Initializing is easily
  ...'
---

By Felix Wu

Git Submodules is one of the most terrific but exhausting features in Git.   
I mean, we all **love** Git, right? But have you ever tried using Git Submodules?

Actually, standalone Git Submodules aren’t hard to understand. Initializing is easily done by typing:

```
git submodule add <link-to-remote-repo>
```

However, I recently wanted to use submodules for hosting my reveal.js presentations based on a subpath, and this got quite complicated as I didn’t had any tutorial to refer to.

I basically wanted to have a repository called “presentations,” so that GH-Pages would host this repository on the respective subpath ([http://presentations.flxwu.com/](http://presentations.flxwu.com/)) in which I could include my actual reveal repositories.

Thus, I could have **separate standalone repos for my presentations which would be automatically updated in the “presentations” repository.** This would cause my “firebase-101” repository to be hosted on [http://flxwu.com/presentations/firebase-101](http://flxwu.com/presentations/firebase-101).

You can also host on a custom subdomain — I have my presentations at [**presentations.flxwu.com/[repo name]**](http://presentations.flxwu.com/[repo name]). Therefore you can still have your other non-presentations repositories under [username.github.io/[repo name]](http://username.github.io/[repo name])

### Setting up the local repository

First off, we initialize a new repository and add respective submodules to it.

```
mkdir parentrepo && cd parentrepo/git initgit submodule add https://github.com/flxwu/firebase-101
```

You may replace my repository link with your respective repository which you want to host on your [username.github.io/parentrepo/[repository name]](http://username.github.io/parentrepo/[repository name]) subpath. **Just make sure that the link uses HTTPS and the repository is public**.

Now commit everything and go through the usual procedure of creating the GitHub repository, adding the remote GitHub repository locally and pushing to it:

```
git commit -a -m "Initial Commit"git remote add origin [your github repository .git link]git push origin master
```

Your GitHub repository should now look like this (except with only one hooked folder in case you only added one submodule)

![Image](https://cdn-media-1.freecodecamp.org/images/o9f8sM3ccAkSpITYVAAPUoy6D3iMkg49OPOP)

Now go into the settings and publish the “master” branch on GitHub Pages. You should now see this below, replacing [flxwu.com] with your own user GitHub pages domain (username.github.io if you didn’t set a custom one).

![Image](https://cdn-media-1.freecodecamp.org/images/4wrrjCiLFksvG2UmDIwqFYTUoFJUu-oEGDqM)

You can now also set a custom subdomain:

![Image](https://cdn-media-1.freecodecamp.org/images/4y3gU4qaLbvZeoO-sXUdeOWLiK5YZWcwlWCL)
_This is how I configured GitHub Pages_

Now, your respective submodule `**firebase-101**` (if you didn’t add your own repo instead of mine) is hosted at **subdomain.domain.com/firebase-101**.

#### Success!

If this article helped you, follow me on twitter [@flxwu](http://twitter.com/flxwu)

### Bonus: How to Remove a Submodule

* Delete the section referring to the submodule from the `.gitmodules` file
* Stage the changes via `git add .gitmodules`
* Delete the relevant section of the submodule from `.git/config`.
* Run `git rm --cached path_to_submodule` (no trailing slash)
* Run `rm -rf .git/modules/path_to_submodule`
* Commit the changes with `git commit -m “Removed submodule ”
* Delete the now untracked submodule files `rm -rf path_to_submodule`


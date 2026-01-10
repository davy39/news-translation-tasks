---
title: Pushing to Github - made simple enough for Poets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-08T16:00:00.000Z'
originalURL: https://freecodecamp.org/news/pushing-to-github-made-simple-enough-for-poets
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca19c740569d1a4ca4f9d.jpg
tags:
- name: Git
  slug: git
- name: Inspiration
  slug: inspiration
- name: learning to code
  slug: learning-to-code
seo_title: null
seo_desc: 'By Usheninte Dangana

  When I started actively pushing content to Github, I did not push Open Source contributions,
  Components or anything of the like - I pushed poetry. I did this, because it is
  what I love the most, after coding. I remain ever gratef...'
---

By Usheninte Dangana

When I started actively pushing content to Github, I did not push Open Source contributions, Components or anything of the like - I pushed poetry. I did this, because it is what I love the most, after coding. I remain ever grateful that I took the initiative to make my first `git commit`.

Now, I want to breakdown the process for new coders (and poets - hopefully ), so that they can become comfortable with working with Github too. I will be breaking down several ways to push content to Github. For the purpose of this article, I will assume that readers are familiar with Terminal usage (GitBash or otherwise).

---

### Pushing to a new repository with a README file

There are just a few essential steps to this:

* Click the green Clone or download button on the repository page.  
![Git Clone](http://res.cloudinary.com/poetrique/image/upload/v1535965331/allbuy-i-ng/gallery/git-clone.png)

* Use the Clone with HTTPS option, and copy the link provided.
![Git Clone 2](http://res.cloudinary.com/poetrique/image/upload/v1535965671/allbuy-i-ng/gallery/git-clone2.png)

* Run `git clone https://github.com/UserProfile/repository.git` in the terminal. Here, **_UserProfile_** and **_repository_** will be replaced by the values provided in the copied link.
* Run `git init` in the terminal. This will initialize the folder/repository that you have on your local computer system.
* Run `git add .` in the terminal. This will track any changes made to the folder on your system, since the last commit. If this is the first time you are committing the contents of the folder, it will add everything.
* Run `git commit -m"insert Message here"`. This will prepare the added/tracked changes to the folder on your system for pushing to Github. Here, **_insert Message here_** can be replaced with any relevant commit message of your choice.
* Run `git push origin master`. Note that the last word in the command **_master_**, is not a fixed entry when running `git push`. It can be replaced with any relevant “branch_name”.

---

### How to push Existing Code to a new Github repository

> _"Coding is a beautiful thing. Anyone can learn to code!"_ 

What you need to do:

* Copy the `HTTPS` link provided.  
![Example Empty Repo](http://res.cloudinary.com/poetrique/image/upload/c_scale,w_700/v1536217259/allbuy-i-ng/gallery/github-example.png)

* Run `git init` in the terminal. This will initialize the folder/repository that you have on your local computer system.
* Run `git add .` in the terminal. This will track any changes made to the folder on your system, since the last commit. As this is the first time you are committing the contents of the folder, it will add everything.
* Run `git commit -m"insert Message here"`. This will prepare the added/tracked changes to the folder on your system for pushing to Github. Here, **_insert Message here_** can be replaced with any relevant commit message of your choice.
* Run `git remote add origin https://github.com/Usheninte/example.git` in the terminal. Here, **_Usheninte_** and **_example_** will be replaced by the values provided in the copied link. This will push the existing folder on you local computer system, to the **newly created** Github repository.
* Run `git remote -v`. This does some **_git pull_** and **_git push_** magic, to ensure that the contents of your new Github repository, and the folder on you local system are the same.
* Run `git push origin master`. Note that the last word in the command **_master_**, is not a fixed entry when running `git push`. It can be replaced with any relevant “branch_name”.

---

So, that's it! I honestly believe anyone can learn to code. I have spent the past year, tutoring undergraduate students in Nigeria, on Software Development. Soon, I will be starting off my journey as an [Entrepreneur-in-Training](https://meltwater.org/training-program/) at the **Meltwater Entrepreneurial School of Technology.**

> Start coding today!


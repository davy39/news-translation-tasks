---
title: How to use Git efficiently
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-29T16:34:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-efficiently-54320a236369
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Nv1sgovc6sNy89N_
tags:
- name: Git
  slug: git
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: workflow
  slug: workflow
seo_title: null
seo_desc: 'By Aditya Sridhar


  The code was working yesterday but today it is not

  The code got deleted

  A weird bug has been introduced suddenly and no-one knows how


  If you have been in any of the above situations then this post is for you.

  Apart from knowing gi...'
---

By Aditya Sridhar

> _The code was working yesterday but today it is not_

> The code got deleted

> _A weird bug has been introduced suddenly and no-one knows how_

If you have been in any of the above situations then **this post is for you**.

Apart from knowing `git add`, `git commit` , and `git push` , there are a bunch of other important techniques in Git. Knowing these will help a lot in the long run. Here I will be covering some of the things which will enable you to make the **best use of Git.**

### Git workflows

Whenever multiple developers are involved in a project it is necessary to use the right workflow for Git. Here I will be covering one workflow which is very effective in big projects with multiple developers.

![Image](https://cdn-media-1.freecodecamp.org/images/LBct-BJctnUEC2R7MIznkdoVQ5Lh6BfhykHC)
_Hopefully this workflow chart I created will help you visualize the process :)_

#### Scenario

All of a sudden you have become the tech lead for a project in which you are planning to build the next Facebook. The team has three developers:

1. **Alice**: has one year of experience and knows programming
2. **Bob**: has one year of experience and knows programming
3. **John**: has 3 years of experience and knows programming well
4. **You:** assigned as tech lead for this project

### Development process in Git

#### Master branch

1. The Master Branch should always have a copy of the existing code in Production.
2. No-one — **including** the tech lead — should be coding directly in the master branch since it is a copy of production code.
3. The actual code is written in other branches.

#### Release branch

1. When the project begins the first thing to do is to create a **release branch** for the project. The release branch is created from the **master branch**.
2. All code pertaining to this project will be in the **release branch.** The release branch is just a normal branch with the prefix **release/**.
3. Let’s call the release branch for this example **release/fb.**
4. It’s possible that there are multiple projects running on the same code base. So, for each project, a separate release branch is created. Let’s say there is one more project running in parallel. Then that project can have a separate release branch like **release/messenger**
5. The reason to have a release branch is that the same code base can have multiple projects running in parallel — there should be no conflict between the projects.

#### Feature branch

1. For every feature that is built in the application a separate **feature branch** is created. This ensures that the features can be built independently
2. Feature branch is just like any other branch but with the prefix **feature/**
3. Now you, being the tech lead, have asked **Alice** to build a login screen for Facebook. So she creates a new feature branch for this. Lets call the feature branch **feature/login.** Alice would write the entire login code only in this feature branch.
4. The feature branch is generally created from the **release branch**
5. Bob has been tasked with building the “Friend” request page. So Bob creates a feature branch called **feature/friendrequest**
6. John’s task is to build the news feed. So John creates a feature branch called **feature/newsfeed**
7. All of the developers code in their individual feature branches. So far so good.
8. Now, let’s say that Alice finished her task and the login code is ready. She needs to send her code to the release branch **release/fb** from her feature branch **feature/login.** This is done through a **pull request.**

#### Pull request

First and foremost, a pull request is not to be confused with `git pull` .

The developer cannot push the code directly into the release branch. The tech lead needs to review the **feature** code before it goes into the **release** branch. This is done through a pull request.

Alice can raise the pull request as follows in GitHub — these steps are specifically for GitHub.

![Image](https://cdn-media-1.freecodecamp.org/images/hITedlsOLA34aFDhyVV1BEISNTkaIzgrtIbE)

Right next to the branch name there is an option called “New pull request”. Clicking on this opens a new screen shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/qkFVwIlr3U1dIk5z86x9-Nko77ew6FGdic3I)

Here:

* the **compare** branch should be Alice’s feature branch **feature/login**
* the **base** branch should be the release branch **release/fb.**

Once this is done, Alice needs to enter a title and description for the pull request, and finally click on “Create Pull Request”. Alice also needs to assign a reviewer for this pull request. She enters **your name** as the reviewer since you are the tech lead.

The tech lead then reviews the code in the pull request, and merges the code from the **feature** branch into the **release** branch

So now you have merged the code from the **feature/login** branch to the **release/fb** branch and Alice is pretty happy that her code has been merged.

#### Code Conflicts.

1. Bob has completed his code as well, and has raised a pull request from **feature/friendrequest** to **release/fb**.
2. Since the release branch already has the login code, **code conflicts** occur. It is the responsibility of the reviewer to resolve these code conflicts and merge the code. In this case, you as the tech lead need to resolve these code conflicts and merge the code.
3. Now John has also completed his code and wants to add his code to the release branch. But John is pretty good at handling code conflicts. John takes the Latest code from **release/fb** branch into his own feature branch **feature/newsfeed** ( either through `git pull` or `git merge` ). John resolves all the conflicts that are present. Now the **feature/newsfeed** branch has all the code present in **release/fb** as well.
4. Finally, John raises a pull request. This time there are no code conflicts in the pull request since John has already resolved them.

So there are **two ways** to resolve code conflicts:

* First method: the reviewer of the pull request needs to resolve the code conflicts.
* Second method: the developer ensures that latest code from the release branch is merged into the feature branch and resolves the conflicts themselves.

#### Master branch again

Once the project is completed, the code from the **release** branch is merged back into the **master** branch. The code is then deployed to production. Thus, the code in production and the code in the master branch are always in sync. This also ensures that, for any future project, the up-to-date code is available in **master**.

### References

More information about pull requests is [here](https://help.github.com/articles/creating-a-pull-request/).

### Congrats ?

You now know how to make the best use of Git. Git has some other concepts like amending commits, and rebasing which are also useful. But **Git workflow** is pretty important for big projects to be successful.

### About the author

I love technology and follow the advancements in technology. I also like helping others with any knowledge I have in the technology space.

Feel free to connect with me on my LinkdIn account [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

You can also follow me on twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

My Website: [https://adityasridhar.com/](https://adityasridhar.com/)

### Other Posts by Me

[Best Practises while using Git](https://adityasridhar.com/posts/how-you-can-go-wrong-with-git)

[Here is my introduction to Git](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61).


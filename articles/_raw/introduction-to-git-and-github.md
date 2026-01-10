---
title: How to Use Git and GitHub – Introduction for Beginners
subtitle: ''
author: Segun Ajibola
co_authors: []
series: null
date: '2022-09-26T05:23:00.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-git-and-github
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Untitled-design--6-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Git and GitHub are common tools used in programming. They help you manage
  different versions of your code and collaborate with other developers.

  Building projects is one of the core parts of being a developer. And Git and GitHub
  are essential tools y...'
---

Git and GitHub are common tools used in programming. They help you manage different versions of your code and collaborate with other developers.

Building projects is one of the core parts of being a developer. And Git and GitHub are essential tools you'll use when building projects with others.

But they can look complicated if you haven't used them before. So I wrote this article to simplify how Git and GitHub work.

## Table of Contents

* [What are Git and GitHub](#heading-what-are-git-and-github)?
* [Why should you learn Git and GitHub](#heading-why-should-you-learn-git-and-github)?
* [Differences between Git and GitHub](#heading-differences-between-git-and-github)
* [How to start using Git and GitHub](#heading-how-to-start-using-git-and-github)
* [Resources to learn Git and GitHub](#resouces-to-learn-git-and-github)

## What are Git and GitHub?

Git was developed in 2005 by Linus Torvalds as _open source software_ for tracking changes in a _distributed version control system_.

Git is open source because its source code is made freely available for anyone to modify and use, aside from its creator. Open-source projects are built and maintained collectively by different developers in different locations.

Git track changes via a distributed version control system. This means that Git can track the state of different versions of your projects while you're developing them. It is distributed because you can access your code files from another computer – and so can other developers.

When you're building an open source project, you'll need a way to document or track your code. This helps make your work organized, and lets you keep track of the changes you've made. This is what Git lets you do.

But you also need a place to host your code – which makes controlling each version of your project easier and faster. This is where GitHub comes in.

GitHub is a "hub" (a place or platform) where Git users build software together. GitHub is also an hosting provider and version control platform you can use to collaborate on open source projects and share files. When you're using GitHub, you're working with Git beneath the hood.

## Why Should You Learn Git and GitHub?

According to Techmonitor.ai, over 73 million developers use GitHub as of November 2021. And the GitHub community is set to hit 100 million users by 2025.

As you can see, millions of people all over the world use these tools, and the numbers just keep going up.

Because of this, more companies are requiring new hires to know how to use Git and GitHub. So if you're looking for a developer job, these are essential skills to have.

If you're not using Git and GitHub, it's clear – you should be!

## Differences between Git and GitHub

Git is a version control system that manages and keeps track of your code. GitHub, on the other hand, is a service that let you host, share, and manage your code files on the internet.

GitHub uses Git underneath, and lets you manage your Git repositories or folders easily on its platform.

So Git is the actual version control system and GitHub is the platform where you host your code.

If you want to learn more about the differences between these two tools, you can [read this tutorial](https://www.freecodecamp.org/news/git-and-github-overview/).

## How to Start Using Git and GitHub

### Step 1 – Install Git

Git comes preinstalled in some Macs and Linux-based systems, but you can always check if you have Git installed in your machine by typing `git version` in your terminal. You can use the Command Prompt to do this.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/checkGItInstalled-1.png)

As you can see above, I have Git version 2.31.1 installed on my Windows computer. If you don't have Git installed in your computer, you won't get a version.

You can download Git [here](https://git-scm.com/download) and then select your operating system to download.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/gitDownload-1.png)

Follow the necessary installer guide until installation is complete. Open the command prompt and type `git version` to verify that Git was successfully installed.

### Step 2 – Create a GitHub Account.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/githubDownload-1.png)

To create an account on GitHub, you will be asked for some personal information like name, confirm your email, set a username and password, and your account should be set up in minutes.

Create an account on [GitHub.com here](https://github.com/).

### Step 3 – Connect your GitHub account to your Git account.

You'll do this from your terminal.

To set your Git username, type this in your terminal:

```shell
git config --global user.name "Segun Ajibola"
```

To confirm that you have set your Git username correctly, type this:

```shell
git config --global user.name
```

You should have "Segun Ajibola" as the output. 

To set your Git email, type this in your terminal:

```shell
git config --global user.email "youremail@gmail.com"
```

To confirm that you have set your Git email correctly, type this:

```shell
git config --global user.email
```

You should have "youremail@gmail.com" as the output. 

You will be asked to authenticate your GitHub account, so just sign in with the same email to confirm.

### Step 4 – Create and edit your code files locally

![Image](https://www.freecodecamp.org/news/content/images/2022/09/codeFIles-1.png)

### Step 5 – Create a repository on GitHub

Click the + sign at the top right corner to create a new repository. Repositories are like your code folders online.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/newRepo-1.png)

You will be prompted to this page:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/newRepo2-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/09/newRepo3-1.png)

Name your repository and give it a description (this is optional).

Click the "Create repository" button to create the repository. You will be prompted to this page:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/newRepoGitHub-1.png)

### Step 6 – Push your local code to GitHub

You can use the code editor built-in terminal to use Git to push your code to GitHub. Click `ctrl` + `shift` + `'` to open the terminal in VSCode.

Input the commands below one after the other in your terminal. Press the `Enter` key to proceed after every input.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/pushCode-1.png)

‌`echo "# sample-code" >> README.md` 

`git init`

`git add .`

`git commit -m "first commit"`

`git branch -M main`

`git remote add origin https://github.com/segunajibola/sample-code.git`

`git push -u origin main` 

Note that we have `git add README.md`  in the repository on GitHub. But here we have `git add .`, which is to let Git add all our code files instead of the `README.md` file which will be created by `echo "# sample-code" >> README.md`. So if you have created other files in your local folder, you need to use `git add .` to add all files.

Take note that `git remote add origin [https://github.com/segunajibola/sample-code.git](https://github.com/segunajibola/sample-code.git)` will contain the link to your own repository and it will have have the name of your GitHub account.

## Common Git Commands to Know

They are many Git commands you can use in the terminal, and that can get overwhelming. So I'd suggest focusing on some of the most popular ones first. 

Here they are:

`git init` lets you initialize Git in your folder.

`git add [Readme.md](https://readme.md/)` lets you add the Readme file, while `git add .` lets you add all files in the present folder.

`git commit` stores the added files. Use `-m` for message followed by the actual message.

`git branch` creates a new branch which is a new version of the repository as it appears when added, and `-M` to move the name to `main`.

`git remote add origin` finally connects the local folder to the repository on GitHub. It is followed by the repository's link.

`git push -u origin main` pushes the code to GitHub. The `-u` flag creates a tracking reference for the branch, and `origin main` puts the code in the `main` branch.

Those are some of the main commands you'll use all the time. This is a beginner and non-technical guide to help you get started using Git and GitHub, so we won't go into too much more detail here.

The more you continue using GitHub, the more comfortable you'll get using these commands. The key is to start small and maintain your momentum.

It will eventually get easier as you build small projects and host them on GitHub using Git.

If you find it hard to use the terminal to navigate between folders, spend some time to practice with it. Again, it gets easier with time and use.

## How to Customize Your GitHub Profile

Customizing your GitHub profile README helps you stand out from random GitHub users.

The README.md file helps you describe your GitHub profile, and you can use it to show what you're currently learning along with your skills and contributions.

The GitHub README.md uses markdown to format its content. It has an easy-to-learn syntax.

[Here](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/) is a simple guide to create and customize your GitHub account.

Here is my GitHub profile's README.md file.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/GithubReadme1-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/09/GithubReadme2-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/09/GithubReadme3-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/09/GithubReadme4-1.png)

You can check out some other GitHub README.md personalized profiles [here](https://github.com/abhisheknaiidu/awesome-github-profile-readme).

## Resources to learn Git and GitHub

Here are some helpful courses and articles you can go through if you want to learn Git and GitHub in more detail:

1. [Git and GitHub Tutorial – Version Control for Beginners](https://www.freecodecamp.org/news/git-and-github-for-beginners/)
2. [Basic Git Commands – How to Use Git in a Real Project](https://www.freecodecamp.org/news/how-to-use-basic-git-and-github-commands/)
3. [Git and GitHub for Beginners - Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk)
4. [An introduction to Git: what it is, and how to use it](https://www.freecodecamp.org/news/what-is-git-and-how-to-use-it-c341b049ae61/)
5. [About GitHub](https://github.com/about)

## Conclusion

If you have finished reading this, you might be feeling overwhelmed about Git and GitHub. Yes it's another big thing you need to learn in tech, but do not fret.

Remember that whenever you start learning something new, at first it can seem like you won't get the hang of it. But after some time and hard work, you'll become more comfortable.

It's the same with Git and GitHub too – if you use it a lot for a while, you will get comfortable with it.

Thanks for reading this article. If you enjoyed it, consider sharing it to help other developers.

You can reach me on [Twitter](https://twitter.com/iamsegunajibola), [LinkedIn](https://www.linkedin.com/in/segunajibola/) and [GitHub](https://github.com/segunajibola).

Happy Learning.


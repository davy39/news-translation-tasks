---
title: How you can learn Git and GitHub while you’re learning to code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-31T18:53:36.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-learn-git-and-github-while-youre-learning-to-code-7a592ea287ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zGKyRHC3yvnYyCDzHgtL9A.jpeg
tags:
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Iago Rodrigues

  In this article, I’ll give you some hints about how to become a Git/GitHub ninja.
  Also, as a bonus, I’ll show you how to use the Terminal (shell) while coding. So
  if you are a beginner, this post should help you understand this tech...'
---

By Iago Rodrigues

In this article, I’ll give you some hints about how to become a Git/GitHub ninja. Also, as a bonus, I’ll show you how to use the **Terminal** (shell) while coding. So if you are a beginner, this post should help you understand this tech. And if you already are a ninja, have a look through to help you remember things that you might have forgotten.

### A brief intro

Git and GitHub are extremely important tools to our routine as a software developers. But, how can we learn them as we have so much on our plates when we are learning code?

I’m Iago Rodrigues, a Brazilian. I’m a Systems Information student, a software developer intern, and a freelancer. I’m at the beginning of my career, and I wanted to share some knowledge that I’ve acquired with you. So, get your coffee and let’s hack!

If you are a Portuguese reader, please go [here](https://medium.com/trainingcenter/plano-para-estudar-git-e-github-enquanto-aprende-programa%C3%A7%C3%A3o-f5d5f986f459).

You can use this plan to study any programming language like JavaScript, Python, Node, and also HTML and CSS. It doesn’t matter what tech you are learning — versioning your work with Git is the default way to program.

### Preparing the environment

Before we start, we need to set up the environment to save our code and examples of what we are learning.

To do this, we must complete some requirements:

* install Git on our machine
* create a GitHub account
* create a workspace on our machine

If you’ve already done this, you can go straight to the **GitHub’s workflow and the Terminal** section.

#### Installing Git on your machine

Git installation is different on each operation system. Check out [Git’s](https://git-scm.com/downloads) official site to see which way is right for you.

But if you are using Windows (and speak Portuguese), I recommend [this](https://woliveiras.com.br/posts/instalando-o-git-windows/) article.

Once Git is installed, we need to create a GitHub account and configure it on our machine.

#### Creating an account on GitHub

To create an account, go to the [GitHub](https://github.com/) web site and fill out the main form.

![Image](https://cdn-media-1.freecodecamp.org/images/5cNW40jBqX4VdNrWJoCP8HAXPagXVfLvPus8)
_This form is the first thing that appears if you enter the website without being logged in_

I recommend that you choose a real and nice user name here so you can use the account on résumés or your [LinkedIn](https://www.linkedin.com/in/iago-rodrigues/) account.

You need to inform GitHub which plan you want to use. Choose the **free** option. The only difference is that you can setup private repositories with the paid plan.

![Image](https://cdn-media-1.freecodecamp.org/images/dayAModQsbAZ5Evh5-DuMKdNx9sQwJpoHBmA)
_Choosing your GitHub account’s plan._

GitHub will ask a few things before finishing your account setup. You can answer them now, or just jump to the next screen.

With everything completed, we can start our project.

![Image](https://cdn-media-1.freecodecamp.org/images/p5NkEAEk33Tp8PgRbJRc8e63VNKA8D0IovjJ)
_Confirmation screen._

Before we create our repository, though, let’s setup our GitHub email and user name in our machine.

#### Setting up our system with our GitHub data

Open up your Terminal. In Windows, you have to open the **start menu** and type **cmd.** Then click enter.

![Image](https://cdn-media-1.freecodecamp.org/images/nCvpCO1j10nA46u-DvtqvP6tSLKqTSPRMKP4)
_Acessing the CMD via start menu on Windows_

Or, you can install [cmder](http://cmder.net/) (which is a good option) to use it instead of **cmd**, which is the default Windows Terminal.

With that, we have to execute the following shell command in the cmder:

```
git config --global user.name "our_GitHub_user_name"
```

Now put in your GitHub email address:

```
git config --global user.email "our_GitHub_user_email"
```

#### Setting up your GitHub access key

Whenever you access a repository via shell, you need to have access permission. This is granted when you sign into your GitHub account. But, every time you send something to your repository (repo), you must pass your credentials.

To avoid this, use an SSH key. This is an access key which GitHub exchanges with the one configured on our machine.

To create this key, follow the process outlined in the GitHub [documentation](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

With all everything all configured, you are good to go!

![Image](https://cdn-media-1.freecodecamp.org/images/D9WuDGk4mfRzuxpwkWdP1OdKxphqAZwRa2-2)

### GitHub’s workflow and the Terminal

Let’s set up a **rule** here:

Every time you create a project to study something, such as making an HTML page or a command line game with Node.js or anything, you’ll create a repository, clone it in your machine, work on it using branches, and make small commits to send to GitHub_._

Deal?!

This will guarantee that you get some experience which you’ll need to master these tools.

So let’s get started.

#### **Create a new project**

Let’s get back to your GitHub page and click on the plus icon (+) at the top of the page.

![Image](https://cdn-media-1.freecodecamp.org/images/aRgF6kizz2QH8XyBmXpMpJxf73SgS5Ryn6kH)
_Creating a new repo._

Click on **New repository**.

Let’s say you are creating a project to study HTML, so name your repository **learning-html**. It could be the name of a page that is being created or any project, such as: **curriculum-in-html**, **little-snake**, **tic-tac-toe**_,_ or anything else_,_ ok?

The description of the project is optional. But I think it’s important to enter some helpful text there, as it will identify the scope of your project. If other people want to help you, they can understand your project briefly through the description. In your case, you can enter something like **HTML language study repository**.

![Image](https://cdn-media-1.freecodecamp.org/images/ZHd1WW2mltowVKBEVXCAxfbLgjXVlzmeaCi3)
_Creating a repository._

You should make a README file as well, and define the type of license that you will use in the project. Take a look at these good [examples](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) of READMEs, as well as the [license](https://choosealicense.com/) to use on the project.

The README file is a more complete description of your project, so it’s a good idea to put some helpful information in there. Follow the examples in the link.

Although the license is optional, it’s good practice to define it. The license will say what other people can do with your code. The MIT license is one of the most popular, and allows you (and others) to do many things with the project. Take some time to search for others types of licenses if you wish.

#### **Create your workspace**

Once you’ve created the repository, you can clone it on your machine. But before that, you need to create a folder where you will clone all future repositories you work on.

Use the terminal to create a folder that will be your **workspace**. You do this to maintain an organized system, otherwise you’ll end up scattering your projects around (and you might lose them just like you lost those kittens gifs that you saved on your computer…).

Assuming that you’ve already installed cmder, we can now open it (if you didn’t, [now](http://cmder.net/) is a good time) and we will be at `C:/Users/your_computer_name` .

If you aren’t on this path, use the command:

```
cd %home%
```

Run the command `mkdir folder_name` to create the workspace. For example:

```
mkdir workspace
```

That’s it! Now you have the default folder for your projects, and you can clone your repositories in there.

#### **Clone your repositories**

Cloning a repository means that you’ll copy all of the files and directories on the GitHub server onto your machine so you can work with them.

Now you need to clone the project that you created on GitHub to your **workspace.** To do this, go to the folder that you just created. On cmder, type:

```
cd workspace\
```

**Tip**: if you created the folder or want to access one which already exists, you can start typing its name and hit TAB, and cmder will autocomplete the name for you.

With that, go to your project page on GitHub and get the link that you need to clone the repository.

The link is in that green button named **Clone or Download**:

![Image](https://cdn-media-1.freecodecamp.org/images/fvqwCR6gUSaY2P6mo1FAATPOjnt68Ug-aple)
_Getting the link to clone our repo._

Change from HTTPS to SSH, because you already configured your access key in your account.

![Image](https://cdn-media-1.freecodecamp.org/images/rizYyKsRhGxI7Jo5V85wbufiqLJpqDFa5pjP)
_Changing https to ssh link._

Now you can run the `git clone` command and pass the link that you get. Just like that:

```
git clone git@github.com:our-username/learning-html.git
```

And your repository will be cloned, like in the following picture:

![Image](https://cdn-media-1.freecodecamp.org/images/y3Ek5z6w63gFwCq-gUjcxhexVyZYtp5HKKnu)
_Clone confirmation message._

You can access the repository folder which was created in your workspace when you cloned it.

Type the command: `cd learning-html/`

**Attention**: I’m assuming that you are inside the`workspace` diretory now. If you aren’t, the above command will not work. Use `cd %home%\workspace\` and then the above command.

#### **Create a branch**

Every time you change something in a project versioned with Git, you should create a **branch** with the name of the task which you’re working on. This prevents you from messing up the “main” code located on the **master** branch. For this, you can use the following command:

```
git checkout -b task_name
```

A **branch** is like a tree branch. It’s part of the trunk of the tree. So you can make changes in parallel with the main part of the project without affecting it.

For example:

![Image](https://cdn-media-1.freecodecamp.org/images/h4qa8Fx5PUOOjlvN5AAyy2xqMHcHkSWSG9Hi)
_Changing branch._

Once you’ve done this, you can change automatically to the newly created branch and can code like crazy now.

![Image](https://cdn-media-1.freecodecamp.org/images/owmN8324SP6p7hQt1wayIX1oYkVWy22hF-Ch)
_A kitty coding._

#### **Commit the changes**

Once you finish a change to your project, you should **commit** the change to your remote repository (the one on GitHub’s servers).

To **commit** something is to tell Git that you are putting your changes in the queue to be pushed (sent) to your remote repository.

Imagine that you just created an HTML page and added some titles and text to it. You have the first version of this document now, so you should commit it.

To do this, run some commands so that Git understands that we want to send our changes do the remote repo. Run `git add file_name` to tell Git to stage the file.

Alternatively, you can run `git add --all` to send all the files that you made some changes to. With the `git status` command, you can see which changed files you will commit to the server.

![Image](https://cdn-media-1.freecodecamp.org/images/PFTyey85HGhG36f1xJsc-VvOI-Xt17GvDS53)
_Example of the first version of a file._

In the above example, the **index.html** file was created and the **git status** command was run to see what was changed. Then the file was added with **git add** and **git status** was run again to see which file was added to the Git workspace.

With that you can now **commit** the changes. Just run the **git commit** command, just like `git commit -m "commit_message"` . Remember to include a descriptive message of what was added to the commit.

#### **Merging the changes**

After you’ve committed the changes, you now have a branch with modifications ahead of the ones in the **master** branch. That means that you have a different version of the project, and you need to merge those changes with the main version of the project. Before doing that, verify what the differences are between the branches. On your branch, perform the command:

```
git diff master
```

The output will be something like:

![Image](https://cdn-media-1.freecodecamp.org/images/9dKretvO8Ne5fHSUs2lofy0SqXXvZyynxCvV)
_Git diff output._

Git shows you the newest commit made, which files were added or changed, and what was changed as well.

Since you know that you have differences between your branch and the master, you need to **merge** them to **join** the new commits, which you made in your branch, with the code in the master. To do this, you need to go to the master branch, on cmder, and run the command `git merge` .

To get back to the master, run `git checkout master` . To merge the commits, run `git merge our_branch_name` .

![Image](https://cdn-media-1.freecodecamp.org/images/TOoDL2f60zFngTvP-TUexS3p2pknLqNWR3xV)
_Merging example._

Git will show you an output confirming what was added.

#### **Sending it to GitHub**

After you’ve made and merged all the changes, you can now send them to your remote repository on GitHub.

You will use `git push origin master` to do this.

![Image](https://cdn-media-1.freecodecamp.org/images/2XbKSpQhgJi8d0teKw11WeBt2J7Q0814etT4)
_Push our changes to the remote repo._

You can also just use `git push` . It’ll have the same result. But when you push changes for the first time on your workspace, you need to do `git push origin master` so that Git will know that your workspace is the origin of the push.

Now your commit will appear on your GitHub repository’s page:

![Image](https://cdn-media-1.freecodecamp.org/images/B3ytaUMnmfBhj4fGouLbEiixHnVgDZqbxN0E)
_The last commit which we just did is showed on the project’s page on github._

### Conclusion

In this tutorial, you learned how to create a project on GitHub so that you can track your progress every time you study something new. This will help you get to know the command line (Terminal), Git commands, and GitHub. Besides that, it’ll help you create a nice portfolio that you can show in job interviews.

Practicing like this will also help you better understand how to use **Git with remote repositories** (the repositories hosted on some platform like **GitHub**). You’ll also level up your knowledge and skills on the Terminal.

Don’t forget the ground rules that you set:

* always create a new project of study
* work on branches
* commit the changes until it’s time to push them to GitHub

Ok? :)

Come back here and follow this step-by-step guide every time you forget something!

My name is Iago Rodrigues. I am an intern in Brazil, in the city of Belem.

You can follow me on social media. Always a pleasure to help with what I can.

[**Iago Rodrigues (@iagokv) | Twitter**](https://twitter.com/iagokv)  
[_The latest Tweets from Iago Rodrigues (@iagokv). Front-End Developer | Vue.js padawan | Noob on life. Belém, Brasil_twitter.com](https://twitter.com/iagokv)

Yeah! I know. My twitter photo is something …


---
title: The Best Git Tutorials
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-21T17:35:00.000Z'
originalURL: https://freecodecamp.org/news/best-git-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f26740569d1a4ca4107.jpg
tags:
- name: Git
  slug: git
seo_title: null
seo_desc: 'Git is an open source distributed version control system created in 2005
  by Linus Torvalds and others from the Linux development community. Git can work
  with many types of projects, but it’s most commonly used for software source code.

  Version contro...'
---

Git is an open source distributed version control system created in 2005 by Linus Torvalds and others from the Linux development community. Git can work with many types of projects, but it’s most commonly used for software source code.

Version control is a system that keeps track of changes to a file or group of files over time. When you have a history of these changes, it lets you find specific versions later, compare changes between versions, recover files you may have deleted, or revert files to previous versions.

A _distributed_ version control system means that different users maintain their own repositories of a project, instead of working from one central repository. Users automatically have full file tracking abilities and the project’s complete version history without needing access to a central server or network.

When Git is initialized in a project directory, it begins tracking file changes and stores them as “change sets” or “patches.” Users working together on a project submit their change sets which are then included (or rejected) in the project.

freeCodeCamp has a [YouTube playlist with lots of practical Git and GitHub tips here](https://www.youtube.com/watch?v=vR-y_2zWrIE&list=PLWKjhJtqVAbkFiqHnNaxpOPhh9tSWMXIF).

![Image](https://img.youtube.com/vi/vR-y_2zWrIE/maxresdefault.jpg)

### Other tutorials:

* The [Pro Git](https://github.com/progit/progit2) book, written by Scott Chacon and Ben Straub and published by Apress. The book is displayed in full in the [Git documentation](https://git-scm.com/book/en/v2).
* For downloads, documentation, and a browser-based tutorial: [Git official website](https://git-scm.com/)
* Most useful commands when you’re in bad GIT situation: [Oh s***, git!](http://ohshitgit.com/)

### **Understand the Three Sections of a Git Project**

A Git project will have the following three main sections:

1. Git directory
2. Working directory (or working tree)
3. Staging area

The **Git directory** (located in `YOUR-PROJECT-PATH/.git/`) is where Git stores everything it needs to accurately track the project. This includes metadata and an object database which includes compressed versions of the project files.

The **working directory** is where a user makes local changes to a project. The working directory pulls the project’s files from the Git directory’s object database and places them on the user’s local machine.

The **staging area** is a file (also called the “index”, “stage”, or “cache”) that stores information about what will go into your next commit. A commit is when you tell Git to save these staged changes. Git takes a snapshot of the files as they are and permanently stores that snapshot in the Git directory.

With three sections, there are three main states that a file can be in at any given time: committed, modified, or staged. You _modify_ a file any time you make changes to it in your working directory. Next, it’s _staged_ when you move it to the staging area. Finally, it’s _committed_ after a commit.

### **Install Git**

* Ubuntu: `sudo apt-get install git`
* Windows: [Download](https://git-scm.com/download/win)
* Mac: [Download](https://git-scm.com/download/mac)

### **Configure the Git Environment**

Git has a `git config` tool that allows you to customize your Git environment. You can change the way Git looks and functions by setting certain configuration variables. Run these commands from a command line interface on your machine (Terminal in Mac, Command Prompt or Powershell in Windows).

There are three levels of where these configuration variables are stored:

1. System: located in `/etc/gitconfig`, applies default settings to every user of the computer. To make changes to this file, use the `--system` option with the `git config` command.
2. User: located in `~/.gitconfig` or `~/.config/git/config`, applies settings to a single user. To make changes to this file, use the `--global` option with the `git config` command.
3. Project: located in `YOUR-PROJECT-PATH/.git/config`, applies settings to the project only. To make changes to this file, use the `git config` command.

If there are settings that conflict with each other, the project-level configurations will override the user-level ones, and the user-level configurations will override the system-level ones.

Note for Windows users: Git looks for the user-level configuration file (`.gitconfig`) in your `$HOME`directory (`C:\Users\$USER`). Git also looks for `/etc/gitconfig`, although it’s relative to the MSys root, which is wherever you decide to install Git on your Windows system when you run the installer. If you are using version 2.x or later of Git for Windows, there is also a system-level config file at `C:\Documents and Settings\All Users\Application Data\Git\config` on Windows XP, and in `C:\ProgramData\Git\config` on Windows Vista and newer. This config file can only be changed by `git config -f FILE` as an admin.

#### **Add Your Name and Email**

Git includes the user name and email as part of the information in a commit. You’ll want to set this up under your user-level configuration file with these commands:

```shell
git config --global user.name "My Name"
git config --global user.email "myemail@example.com"
```

#### **Change Your Text Editor**

Git automatically uses your default text editor, but you can change this. Here’s an example to use the Atom editor instead (the `--wait` option tells the shell to wait for the text editor so you can do your work in it before the program moves on):

```shell
git config --global core.editor "atom --wait"
```

#### **Add Color to Git Output**

You can configure your shell to add color to Git output with this command:

```shell
git config --global color.ui true
```

To see all your configuration settings, use the command `git config --list`.

### **Initialize Git in a Project**

Once Git is installed and configured on your computer, you need to initialize it in your project to start using its version control powers. In the command line, use the `cd` command to navigate to the top-level (or root) folder for your project. Next, run the command `git init`. This installs a Git directory folder with all the files and objects Git needs to track your project.

It’s important that the Git directory is installed in the project root folder. Git can track files in subfolders, but it won’t track files located in a parent folder relative to the Git directory.

### **Get Help in Git**

If you forget how any command works in Git, you can access Git help from the command line several ways:

```shell
git help COMMAND
git COMMAND --help
man git-COMMAND
```

This displays the manual page for the command in your shell window. To navigate, scroll with the up and down arrow keys or use the following keyboard shortcuts:

* `f` or `spacebar` to page forward
* `b` to page back
* `q` to quit

## **Difference between Git and GitHub**

Git and Github are two different things. [Git](https://git-scm.com/) is the [version control system](https://en.wikipedia.org/wiki/Version_control), while [GitHub](https://github.com/) is a service for hosting Git repos that helps people collaborate on writing software. However, they are often confounded because of their similar name, because of the fact that GitHub builds on top of Git, and because many websites and articles don’t make the difference between them clear enough.

![Git is not GitHub](https://i.imgur.com/EkjwJdr.png)

### **Git**

Git is the distributed version control system. Git is responsible for keeping track of changes to content – usually source code files.

For more info, there is a [complete article about Git itself](https://guide.freecodecamp.org/git).

### **GitHub**

GitHub is a service that provides Git repository hosting. That means that they provide a turnkey solution to host Git repositories on their servers. That can be useful to keep a backup of your repository (Git only tracks the changes made to your files over time; the repo still needs to be backed up), and to have a centralized place to keep and share your code with others.

More than just a Git repository hosting service, GitHub is a [software forge](https://en.wikipedia.org/wiki/Forge_(software)). That means it also provides an [issue tracker](https://en.wikipedia.org/wiki/Issue_tracking_system), tools for [code review](https://en.wikipedia.org/wiki/Code_review), and other tools for collaborating with other people and creating software.

GitHub isn’t the only one to provide this kind of service. One of its major competitors is [GitLab](https://gitlab.com/). For more on this, look at the [section about Git hosting](https://www.freecodecamp.org/news/the-beginners-guide-to-git-github/#git-repositories).

# **How to authenticate with GitHub using SSH**

Check that there are no `rsa` files here before continuing, use:

```shell
ls -al ~/.ssh
```

If there is nothing to list (i.e. `: No such file or directory`) then use:

```shell
mkdir $HOME/.ssh
```

If there’s nothing there then generate a new keygen with:

```shell
ssh-keygen -t rsa -b 4096 -C your@email.com
```

Now using `ls -al ~/.ssh` will show our `id_rsa.pub` file.

Add the SSH key to the SSH agent:

```shell
eval "$(ssh-agent -s)" # for mac and Linux from bash
```

```shell
eval `ssh-agent -s`
ssh-agent -s # for Windows
```

Add RSA key to SHH with:

```shell
ssh-add ~/.ssh/id_rsa
```

Copy your key to clipboard

```shell
clip < ~/.ssh/id_rsa.pub # Windows
```

```shell
cat ~/.ssh/id_rsa.pub # Linux
```

Go to your GitHub [settings](https://github.com/settings/keys) page and click the ‘New SSH key’ button paste in your generated key.

Then authenticate with:

```shell
ssh -T git@github.com
```


---
title: How to Set Up Git for the First Time on macOS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-08-08T20:07:30.000Z'
originalURL: https://freecodecamp.org/news/setup-git-on-mac
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-template-1.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: macOS
  slug: macos
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'If you''re setting up Git for the first time on a MacBook, you don''t have
  to struggle to get it done.

  Maybe you just got a new laptop, or you''re getting into tech for the first time
  with a MacBook. Either way, I''ve got you covered.

  This short article ...'
---

If you're setting up Git for the first time on a MacBook, you don't have to struggle to get it done.

Maybe you just got a new laptop, or you're getting into tech for the first time with a MacBook. Either way, I've got you covered.

This short article will help you understand how to set up Git on macOS so you can get back to work immediately.

I assume you already know what Git is and what it does before reading this article. But if you don't and need an introduction to Git and version control, you can check out [this article on What is Git? A Beginner's Guide to Git Version Control.](https://www.freecodecamp.org/news/what-is-git-learn-git-version-control/)

*Let's now get started.*

## How to Install Git on a Mac

There are so many methods available to install Git on a Mac computer, but the easiest is by using Homebrew. You can find [other methods and how to make them work in this documentation](https://git-scm.com/download/mac) or [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

### How to Install Git with Homebrew

[Homebrew](https://brew.sh/) is a free and open-source software package management system that simplifies software installation on Apple's operating system (macOS). You can use it to install all types of packages you will need in the future, not just Git. This makes it really useful.

You don't need to install an application or anything to install Homebrew. You only need to open the terminal and install [Homebrew](https://brew.sh/) by running the following command:

```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Note:** Once you enter the command, it will request your password.

Once that is successful, you can proceed to install Git via the command below in your terminal:

```bash
$ brew install git
```

At this point, if it's successful, you've installed Git on your Mac. You can now verify by running the command below in your terminal:

```bash
$ Git --version
```

## How to Configure Git in macOS

So far, you have learned how to install Git – but installing Git alone doesn't just let you push, pull, and commit code and perform other Git operations from your Git Version Control.

To work with Git, you must set up your Git environment using the `git config` command. This will give you access to configuration variables that control how Git works on your system.

Two significant git config variables you need are the identity variables. These let you set your username and email. This is the username and email you used when setting up your version control system with GitHub, GitLab, and so on.

```bash
$ git config --global user.name "olawanlejoel"
$ git config --global user.email "mymail@gmail.com"
```

**Note:** Replace the name and email with yours. You should also know that the `--global` option ensures that these values are used throughout your system.

Once you've done this, there are a couple of other configurations you can do, which are to setup the default text editor and colors for your Git console:

```bash
$ git config --global core.editor emacs
$ git config --global color.ui true
```

You can choose whatever editor you regularly use. I've chosen EMACS.

Now Git is ready for you to use. You can check your Git configurations to be sure they are correct using this command:

```bash
$ git config --list
```

This will show the following (with your own information):

```bash
user.name=olawanlejoel
user.email=mymail@gmail.com
color.ui=true
```

Suppose there is an error, and you wish to change any of the configurations. Feel free to rerun the config command particular to the error.

For example, if there is an error with my email, I can rerun the email configuration to correct it:

```bash
$ git config --global user.email "mynewmail@gmail.com"
```

Now, when you rerun the `--list` command, you will get the updated value:

```bash
user.name=olawanlejoel
user.email=mynewmail@gmail.com
color.ui=true
```

## Wrapping Up

In this article, you have learned how to set up Git on a Mac computer for the first time.

If you also want to check out how to do it on other systems like Windows and Linux, [check out this comprehensive guide](https://www.freecodecamp.org/news/git-first-time-setup/).

Also, if you are also interested in learning some basic Git commands, here is a [detailed cheat sheet](https://www.freecodecamp.org/news/git-cheat-sheet/).

Have fun coding!

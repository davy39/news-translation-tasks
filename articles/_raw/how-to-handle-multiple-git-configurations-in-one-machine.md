---
title: How to Use Multiple Git Configs on One Computer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-13T01:15:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-multiple-git-configurations-in-one-machine
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/cover-1.jpg
tags:
- name: configuration
  slug: configuration
- name: Git
  slug: git
- name: GitHub
  slug: github
seo_title: null
seo_desc: 'By Dhruv Barochiya

  You might have a hard time managing many cats, but when it comes to Git profiles
  there is something you can do.

  Let''s get straight to the solution – The answer lies in the .gitconfig file. This
  is starter point for Git to identify ...'
---

By Dhruv Barochiya

You might have a hard time managing many cats, but when it comes to Git profiles there is something you can do.

Let's get straight to the solution – The answer lies in the `.gitconfig` file. This is starter point for Git to identify what configurations need to be used. 

The idea is to segregate the repos on your machine into multiple directories by separating the profiles you want, and then define a `.gitconfig` file per profile.

## Step 1 → create separate directories for repos

Organize the projects that you are working on into separate folders by the profiles you want to work with.

For example let's say there are two Git profiles you are working with. This is a common use case for most of us:

* `WORK` → for work related projects
* `PERSONAL` → for open source and side projects

## Step 2 → create a global Git configuration

Create the global `.gitconfig` file in your home directory if it doesn't already exist. Then add all the profile directories as an entry like in the example below.

The way this works is very intuitive – if the directory path where you created the Git directory matches one of the paths in `includeIF`, then Git uses that particular profile configuration file. Otherwise, it uses the default configuration.

```
[includeIf "gitdir:~/personal/"]
  path = ~/.gitconfig-personal
[includeIf "gitdir:~/work/"]
  path = ~/.gitconfig-work


```

## Step 3 → create individual Git configurations for profiles

If you haven't noticed by now, we just mentioned the `.gitconfig-personal` and  `.gitconfig-work` files in the global `.gitconfig` file, but we didn't create them yet. These individual files can contain all the customization that you need, from user name and email to commit hooks.

```bash
[user]
 name = work_user
 email = work_email

```

```bash
[user]
 name = personal_user
 email = personal_email

```

## Let's verify

We're all set!  Now you will have three Git files in your home directory.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-03-at-3.36.24-PM.png)

Now we will create and initiate a new Git repo in the work and personal directories and check the configurations.

```bash
$ cd ~/work
$ mkdir work-test-repo
$ cd work-test-repo
$ git init
		*Initialized empty Git repository in /Users/dbarochiya/work/work-test-repo/.git/*
$ git config -l   
		*credential.helper=osxkeychain
		includeif.gitdir:~/personal/.path=~/.gitconfig-personal
		includeif.gitdir:~/work/.path=~/.gitconfig-work
		**user.name=working_me
		user.email = work@work.com**
		core.repositoryformatversion=0
		core.filemode=true
		core.bare=false
		core.logallrefupdates=true
		core.ignorecase=true
		core.precomposeunicode=true*                                                                                                                   1 

```

```bash
$ cd ~/personal
$ mkdir personal-test-repo
$ git init
	*Initialized empty Git repository in /Users/dbarochiya/personal/.git/*
$ git config -l
	*credential.helper=osxkeychain
	includeif.gitdir:~/personal/.path=~/.gitconfig-personal
	**user.name=me_personal
	user.email=personal@personal.com**
	includeif.gitdir:~/work/.path=~/.gitconfig-work
	core.repositoryformatversion=0
	core.filemode=true
	core.bare=false
	core.logallrefupdates=true
	core.ignorecase=true
	core.precomposeunicode=true*

```

Voilà – as you can see, the email and user name are different in both cases. Depending on the path of the Git repo, it is able to use the custom `.gitconfig` files.


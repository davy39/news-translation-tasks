---
title: The Essential Git Handbook – Learn Git for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T17:16:29.000Z'
originalURL: https://freecodecamp.org/news/the-essential-git-handbook-a1cf77ed11b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AhGSZ1spetb37qk_bZd9XA.png
tags:
- name: coding
  slug: coding
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sanjula Madurapperuma

  Introduction

  Hi! I am Sanjula, and in this guide I hope to teach you a little bit about Git including:


  What Git is

  Why learn Git

  Setting configuration variables

  Introduction to the help command in Git

  How to convert an exist...'
---

By Sanjula Madurapperuma

### Introduction

Hi! I am [Sanjula](https://www.linkedin.com/in/sanjula-madurapperuma/), and in this guide I hope to teach you a little bit about Git including:

* What Git is
* Why learn Git
* Setting configuration variables
* Introduction to the help command in Git
* How to convert an existing project into a local Git repository
* Things to do before the first commit
* How to add files to the staging area
* How to remove files from the staging area
* Making your first commit
* How to clone a remote repository
* View information about the remote repository
* How to push your changes to the remote repository
* How to create a branch for a specific feature or issue
* Push the branch to the remote repository after committing
* How to merge a branch
* How to delete a branch

Let’s get started!

### What is Git?

In straightforward terms, Git is an **open-source distributed version control system**.

Version control systems help any software team to manage changes to source code of a product or service over time. It keeps track of all the modifications to the source code in a database. If a critical mistake has been made to the source code, then the developers on a software team can rewind the source code to a version before the erroneous change was made. As a result, version control systems protects source code from disasters, human errors and unintended consequences (when a bug fix breaks another part of the application, for example).

### So why learn Git?

Git is the most widely used version control system in the world today. It is a mature and actively maintained open source project originally developed by Linus Torvalds.

An astounding amount of software projects rely on Git for version control, including both commercial and open-source projects, especially using the git repository hosting service, GitHub, which is now owned by Microsoft. Hence, the importance of learning Git.

### Prerequisite for this guide

Download and install git [**here**](http://www.git-scm.com/downloads)

### Check version of git

```
git --version
```

![Image](https://cdn-media-1.freecodecamp.org/images/G81z00SqImj30aOmL1mnhLIa6tW08Xyws1z6)
_Figure-2: Git version_

If the version number is returned, then it means that git is successfully installed on your computer.

### Setting config values

Now we need to set the global configuration variables, which are very important, especially if you are working with other developers. The main advantage of this being it is easier to find out who has committed a certain code block, for example.

```
git config --global user.name “Sanjula Madurapperuma”
```

```
git config --global user.email “sanjula@mail.com”
```

```
git config --list
```

### Help Command

As you may notice, _config_ is a verb that has been used frequently so far in this handbook and verbs can also be used as either a prefix or suffix with the help command. We can use the same example (the verb _config_) from above to explain these commands.

```
git help config
```

```
git config --help
```

![Image](https://cdn-media-1.freecodecamp.org/images/TpOqdmWxNM11sihKZDfCBkvpqrPyO0QVMkhj)
_Figure-3: Help Command_

Both of the above commands perform the same action. Show the manual page for the verb specified. This will be useful to identify more advanced capabilities of git.

### How to initialize a repository from existing code

If you have a local repository that you want to convert into a git project to start tracking it, then we can start by running the command below within the project directory.

```
git init
```

![Image](https://cdn-media-1.freecodecamp.org/images/X5ju5iD8xMwFsvQ5xomZtkvkGbo2GCAWLYVQ)
_Figure-4: Git init_

Done! Just like that you have converted your project into a local git repository. If you open up the project folder you will see that a new directory called .git has been created.

### What to do before the first commit

Enter the following command to view untracked files:

```
git status
```

![Image](https://cdn-media-1.freecodecamp.org/images/A1cKNf7PUeDJ-SI2zyrkuH-g3NvF5YfHy-T7)
_Figure-5: Git status_

If there are files that you don’t want other people to see in the repository, such as files containing personal preferences or those of the IDE, then do the following:

```
touch .gitignore
```

![Image](https://cdn-media-1.freecodecamp.org/images/AkaWuuihvkq5cE5P1r8E0QHOF6cgDzrQlJsy)
_Figure-6: Create .gitignore file_

To specify which files are not to be added to the git repository, open up a text editor and view the .gitignore file, which can be edited like a normal text file. Now we can enter the following into the file, for example:

```
.project
```

```
*.java
```

Wildcard characters can also be used. In this case, it has been used to specify not to add all files ending with the .java extension to the repository.

![Image](https://cdn-media-1.freecodecamp.org/images/Q3wRtlkpWsPt02lPztKmqDDVfWuKovzkZGL5)
_Figure-7: Editing in text editor_

Now run git status again

![Image](https://cdn-media-1.freecodecamp.org/images/V5AwN6ykf9r1dBZ87ViMbvschLJI2iTfBJ4t)
_Figure-8: After updating .gitignore_

Now you can see that the files we excluded in the .gitignore file are no longer shown in the list of untracked files. The .gitignore file should be committed to the repository in order to maintain the same exclusions in all other places.

### Adding files to the staging area

All this time we were in the working directory. The staging area is where we organize all the files that are tracked and have to be committed before pushing to the git repository. It is a file that stores what has to be included in the next commit.

If you want to add all the files that are currently untracked and you’ve changed to the staging area, then use the following command:

```
git add -A
```

If you want to add files individually, then we can give the file name after git add. For example,

```
git add .gitignore
```

Now if you type in git status, you will see that the .gitignore file is now in the staging area.

![Image](https://cdn-media-1.freecodecamp.org/images/HaV5Fai1lvx-xPkdMRsRdCM8Gp8D8Ns6M5fX)
_Figure-9: Staging area_

### Removing files from the staging area

To remove files individually from the staging area, type in the following (for example):

```
git reset simple.py
```

This will remove the file simple.py from the staging area. To see this change, type in git status again.

![Image](https://cdn-media-1.freecodecamp.org/images/hbseWQzJKSluv5zAwHbsj7gi6DBAWt6YBWwM)
_Figure-10: Removing file from staging area_

If you want to remove all the files from the staging area, then run the following:

```
git reset
```

Now if we type in git status, we will see that all the files have been changed to untracked files.

![Image](https://cdn-media-1.freecodecamp.org/images/aUpZJl-E8YA74eLlnf6en0ojS1ohWSil09wY)
_Figure-11: Reset all files_

### Making the first commit

Now run the following to add all the files to the staging area to be committed.

```
git add -A
```

If you want, you can run git status to see all the files that will be committed.

To commit, type in the following.

```
git commit -m “Initial Commit”
```

“-m” specifies a message to be passed describing the commit. Since this is our first commit, we will say Initial Commit.

![Image](https://cdn-media-1.freecodecamp.org/images/lAHfY5GgwQEjkE8HBcuXiDGM9yDFdqxS0AvX)
_Figure-12: Initial Commit_

As you can see, the files have been committed successfully.

If you run git status now, you will see that it says the working directory is clean because we have committed the files and haven’t modified any file since.

![Image](https://cdn-media-1.freecodecamp.org/images/UscWoVk2VszFJowNHo8kawe9dPqmanjl717h)
_Figure-13: Working Tree after commit_

If we run the following command:

```
git log
```

then we can see the commit that we just made, including the hash number of the commit.

![Image](https://cdn-media-1.freecodecamp.org/images/cjCho8GR69IU5ACe0ghU7TsDOKFKuP4Flbjt)
_Figure-14: Commit hash number_

We are now successfully tracking the local project with git!

### Cloning a remote repository

If we want to track an existing remote project with git, then we have to type in a command in the following format:

```
git clone <url> <where to clone>
```

For an example, I will be using the git repository at [this link](https://github.com/sanjulamadurapperuma/GitDemoMedium.git).

I will first move into the directory that I want to clone the project in, though you can specify this as shown above as well.

Go to the repository link given above and click on the “Clone or Download” button, then copy the link given there.

Then enter:

```
git clone https://github.com/sanjulamadurapperuma/GitDemoMedium.git
```

![Image](https://cdn-media-1.freecodecamp.org/images/lHzsIA1k-D5qeBSOciWt443gD3YClS8q8e9y)
_Figure-15: Cloning remote repository_

Now we have cloned the repository successfully.

If we enter the following command, we will see all the files that are in the local directory now.

```
ls -la
```

![Image](https://cdn-media-1.freecodecamp.org/images/2OMMDj4xttnnVsgamdc36jy5B2oopjLcSLsB)
_Figure-16: List all files in directory_

### Viewing information about the remote repository

If you type in the following command:

```
git remote -v
```

![Image](https://cdn-media-1.freecodecamp.org/images/qkYzprJKHXHwd4KHfzDQwF3Sjj2Nh1niZIZU)
_Figure-17: Git remote -v_

This command will list the locations where the local repository would fetch external commits from and push your commits to the remote repository.

If you were to type the command

```
git branch -a
```

![Image](https://cdn-media-1.freecodecamp.org/images/ig6sDj8Y1Gzqm2UMsvRvbwZlxnVrtKy6MBBl)
_Figure-18: List all git branches_

This will list all the branches which are in the repository, both locally and remotely.

In order to demonstrate updating the remote repository, we will make some changes to the files in the repository we cloned.

![Image](https://cdn-media-1.freecodecamp.org/images/n7tWT09vfQnKeaxoN0XyCY1r9Ql4pbwUozXw)
_Figure-19: Make changes to simple.py_

Now that we’ve made a change to our code, the next action we have to make is to push these changes to the remote repository

### Pushing changes to the remote repository

The following command will show all the changes that have been made to the files.

```
git diff
```

![Image](https://cdn-media-1.freecodecamp.org/images/UiWSb3gZiGs5A7fBksCDIDHkt99puF551amJ)
_Figure-20: View changes to file_

If we enter git status again, we can see that changes have been tracked and that simple.py has been modified.

![Image](https://cdn-media-1.freecodecamp.org/images/n9A8DdvhDyKjllzgS2ExFYrM4FsofyoUA0gR)
_Figure-21: View modified files_

Now add them to the staging area

```
git add -A
```

Run git status again

![Image](https://cdn-media-1.freecodecamp.org/images/7jaUjBjc3Y2870zUbEllhi8rWvQ1Hshgcyqx)
_Figure-22: Add files to staging area_

Now we can see that simple.py is ready to be committed.

Then enter the commit command with a message

```
git commit -m “Updated hello function”
```

![Image](https://cdn-media-1.freecodecamp.org/images/XU3eet4u0GXZ7QHQNz98n2nN5fEVlswPV1s2)
_Figure-23: Commit message_

Now we have to push the committed changes to the remote repository so other people have access to them.

Since the common case is that there are several developers working on a single project, we have to first pull any changes that have been done in the remote repository before pushing our changes to it to avoid conflicts.

Run the following command:

```
git pull origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/5TkIfVHFN2pS9akhGmgjHVxHRoR6SrgwJEYc)
_Figure-24: Pull changes from remote repository_

Since we are already up-to-date, we can now push our changes to the remote repository.

Now run the following:

```
git push origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/t7wVKea6PcQGihQzTeoz3WdS66L8IGjPdpqE)
_Figure-25: Push changes to remote repository_

We have successfully pushed our changes to the master branch of the remote repository!

### Creating a branch for a feature or issue

So far we have been working on our master branch, but this is not how you should be working in git as a developer because the master branch should be a stable release of the project that you are working on. So for every feature or issue, it is usually the norm to create your own branch and then work off that branch.

The command to create a new branch called simple-greeting is as follows:

```
git branch simple-greeting
```

Now if you run

```
git branch
```

then you will see all the branches in the repository, and the current branch that you are in is highlighted with an asterisk on the left side.

![Image](https://cdn-media-1.freecodecamp.org/images/XlYSPXjn7qFPNQiLTIywhgNdYKjxD9MFzip4)
_Figure-26: git branch_

If you want to switch to the branch that you just created, then type the following:

```
git checkout simple-greeting
```

Now if you type git branch you will see that you are now on the simple-greeting branch.

Now we have to make the changes in the project. We’ll switch to the project and define the greeting function.

![Image](https://cdn-media-1.freecodecamp.org/images/VLWULRA1hRT85jSYBs1d4JH90JBUQP2kDrrc)
_Figure-27: Define the greeting function_

Now we will repeat the process of committing these changes:

```
git status
```

![Image](https://cdn-media-1.freecodecamp.org/images/lFNjI8aQZ7CZFUUnNMieYovVJ218kg9MO3Lf)
_Figure-28: See changes that are not staged_

```
git add -A
```

```
git commit -m “Greeting Function”
```

![Image](https://cdn-media-1.freecodecamp.org/images/vsigz7NjuUVcgaaPetiERCN1La5W8F5BoOFd)
_Figure-29: Commit message for Greeting function_

This commit will only change the files in the local branch simple-greeting and it has had no effect on the local master branch or remote repository yet.

### Pushing branch to remote repository after committing

Enter the following command:

```
git push -u origin simple-greeting
```

where origin is the name of the repository and simple-greeting is the branch that we want to push to.

![Image](https://cdn-media-1.freecodecamp.org/images/M3mB0GiO80v-Jk56yKQKuIgnUVaXQvDfGnM-)
_Figure-30: Push branch to remote repository_

Now we have pushed the simple-greeting branch to the remote repository. If you type:

```
git branch -a
```

![Image](https://cdn-media-1.freecodecamp.org/images/GrUXJqmZJmFgb3jHf8B3PlxT7yxVwOCncuIB)
_Figure-31: simple-greeting Branch in remote repository_

We can see that, in our remote repository we now have the simple-greeting branch. Why do we need to push the branch to the remote repository? Because in some companies that’s where they run their unit testing and various others to make sure the code runs well before it’s merged with the master branch.

Given that all the testing has come out well (we won’t go into detail here), we can now merge the branch simple-greeting with master branch.

### Merging a branch

First, we have to checkout into the local master branch

```
git checkout master
```

![Image](https://cdn-media-1.freecodecamp.org/images/OvI0f0CpYa3xrFvKv-HQ5LB20HxbgOEHxT9I)
_Figure-32: Checkout to master branch_

Pull all the changes in the remote master branch:

```
git pull origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/S1bz0eJjDY1avLSy4Gl7Et33gwDw2uGVeih3)
_Figure-33: Pull changes from remote repository_

We’ll now see the branches we have merged in so far:

```
git branch —-merged
```

![Image](https://cdn-media-1.freecodecamp.org/images/v9PBL7dVbIsb3aIz61PRypR6qorrAcw6nahW)
_Figure-34: Display merged branches_

simple-greeting branch will not appear here because we haven’t merged it yet.

To merge simple-greeting with master, enter:

```
git merge simple-greeting
```

(Keep note that we are in the master branch right now)

![Image](https://cdn-media-1.freecodecamp.org/images/4G84bB5YgbwdfH8XkDHUxUZwGfi8mMw0ZHKa)
_Figure-35: Merge simple-greeting branch_

Now that it’s been merged, we can push the changes to the remote repository master branch.

```
git push origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/bQjuJUw584OprdvxUzmNs1yxOh8Ijd3WLQwK)
_Figure-36: Push to remote master branch_

Now the changes have been pushed to the master branch in the remote repository.

### Deleting a branch

Since the feature has now been deployed, we can delete the simple-greeting branch. To double check the merge done in the previous section, we can run:

```
git branch --merged
```

![Image](https://cdn-media-1.freecodecamp.org/images/C-XMNUIumKsfPaPVDD5BFyvDBzo8rrJCTTEl)
_Figure-37: Display merged branches_

If simple-greeting shows up here, then that means that we have merged all the changes and that the branch can now be discarded.

```
git branch -d simple-greeting
```

![Image](https://cdn-media-1.freecodecamp.org/images/hd10e8Mc246riKYeTEvv0hL1xz7k7b7njSHf)
_Figure-38: Delete local branch simple-greeting_

Now the branch has been deleted locally.

But since we pushed the branch to the remote repository it is still there in the remote repository. This can be seen by running:

```
git branch -a
```

![Image](https://cdn-media-1.freecodecamp.org/images/gHdlHkbjv1QhmID0PkoWM35qMagnJ9B-qIkx)
_Figure-39: Display all branches_

To remove the branch from the remote repository, enter:

```
git push origin --delete simple-greeting
```

![Image](https://cdn-media-1.freecodecamp.org/images/5-equM6f4mL9prXhxNiet0JC4lqhn4uzn84v)
_Figure-40: Delete remote branch simple-greeting_

If we re-run

```
git branch -a
```

![Image](https://cdn-media-1.freecodecamp.org/images/33hTj4HTBLKO5Eg345weOEBa4yNE2uXglp5Z)
_Figure-41: Display all branches_

we can see that the branch has now been deleted from the remote repository as well.

Congratulations!!! You are now a master in basic but critical Git commands!

For reference or use of this tutorial, here is the public GitHub Repository [Link](https://github.com/sanjulamadurapperuma/GitDemoMedium)

**In the meantime, give as many claps as you like to this article if you liked it, comment down below for any concerns. Also please checkout my profile at [LinkedIn](https://www.linkedin.com/in/sanjula-madurapperuma/) and follow me on Twitter!**


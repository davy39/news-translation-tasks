---
title: Git Revert – How to Reset a File or Commit
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-28T00:21:11.000Z'
originalURL: https://freecodecamp.org/news/git-revert-how-to-reset-a-file-or-commit
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/roman-synkevych-wX2L8L-fGeA-unsplash--1-.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: "When working on a project with a team or by yourself, it's important to\
  \ track changes in the code base through version control. \nGit provides you with\
  \ different commands for tracking file changes. These commands will enable you to\
  \ collaborate with ot..."
---

When working on a project with a team or by yourself, it's important to track changes in the code base through version control. 

Git provides you with different commands for tracking file changes. These commands will enable you to collaborate with other developers, access file history, manage code, and more. 

In this article, you'll learn how to revert and reset a file or commit to a previous commit. 

We'll use some simple HTML code to demonstrate how you can revert and reset to a previous commit using Git. 

Let's get started!

## How to Reset a File or Commit

In this section, you'll learn how to revert/reset a file or commit using the following commands: 

* `git revert`.
* `git reset`.

### How To Revert a File or Commit Using the `git revert` Command

Here's what the syntax for the `git revert` command looks like:

```txt
git revert [commit ID]
```

Here's the code we'll be working with:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>

```

Let's assume that the file above is the current state of the code base for every developer working on the project. 

We'll make some changes to the file then add, commit, and push the changes. That is: 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World!</h1>

    <ul>
        <li>Red</li>
        <li>Yellow</li>
        <li>Orange</li>
    </ul>
    
  </body>
</html>

```

We've added a list of colors to the code. Let's push the changes using the command below:

```bash
git add .
git commit -m "added colors to the HTML file"
git push -u origin main
```

At this point, the new changes have been updated for everyone working on that particular branch of the code. 

But what if the colors added are part of features that are supposed to be released for users in the future? You've made a mistake by releasing this feature before time. 

To revert to a previous commit, you'd need the ID of that particular commit. To get the commit ID, run the command below:

```bash
git log
```

The command shows you the commit ID, author, and date of every commit. It should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/02/git-log.PNG)
_git log_

In our own case, the commit ID is 785dd5a6dd0f1ebd9e06045df787d8d28fd38285.

So to reset the file, you use `git revert [commit ID]`. That is:

```bash
git revert 785dd5a6dd0f1ebd9e06045df787d8d28fd38285
```

The command above will reset all the changes made to the file before that particular commit was made. Here's what the HTML file will look like now:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>
```

Now you can push this new state. 

Note that the  `git revert` command doesn't remove the reverted commit from the remote repository. Instead, it creates a new commit for the reverted changes. 

This means that you'll have the history of the commit that was reverted and a new commit for the file containing the reverted changes. 

### How To Reset a File or Commit Using the `git reset` Command

The `git reset` command can also be used to revert changes. Consider the commit history below:

![Image](https://www.freecodecamp.org/news/content/images/2023/02/git-log-1.PNG)

The image above shows all the commit history — from the first commit to the reverted commit in the last section. 

If we use `git reset [commit ID]` to revert back to a particular commit, every other commit after that will be removed from the commit history. 

Here's an example:

```bash
git reset c1e4962a9b355f023c250609cfa9303a67b3063e
```

Using the commit ID of the first commit, we're reverting back to the state of the first commit. 

Running the `git log` command, you'd have a commit history like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/02/git-log-2.PNG)

While you've successfully reverted back to the first commit, the history for other commits in the code has been erased. This can have a very negative effect when collaborating with other developers. 

## Summary

In this article, we talked about two important Git commands for undoing changes in a Git repository – `git revert` and `git reset`. 

Both commands takes you back to a specified previous state in the code base but with different after effects. 

The `git revert` command reverts to a specified commit but keeps the history of every other commit made to the code base, and creates a new commit for the reverted changes. This is a more efficient way of undoing changes when collaborating with others. 

Alternatively, the `git reset` command will revert back to a specified commit, then delete every commit that comes after the specified commit. 

To be on the safe side, use `git revert` when undoing changes in a repo that has other developers working on it. 

You can use `git reset` in cases where you want to completely get rid of commits after undoing changes.

Happy coding!


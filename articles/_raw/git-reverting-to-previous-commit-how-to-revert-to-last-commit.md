---
title: Git Reverting to Previous Commit – How to Revert to Last Commit
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-10-19T22:55:44.000Z'
originalURL: https://freecodecamp.org/news/git-reverting-to-previous-commit-how-to-revert-to-last-commit
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/roman-synkevych-wX2L8L-fGeA-unsplash.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Git is a great tool for version control. It also makes collaborating with
  others more efficient.

  In this article, you''ll learn how to revert to previous commits when tracking your
  project with Git.

  The two commands we''ll discuss in this article are g...'
---

[Git](https://www.freecodecamp.org/news/git-and-github-for-beginners/) is a great tool for version control. It also makes collaborating with others more efficient.

In this article, you'll learn how to revert to previous commits when tracking your project with Git.

The two commands we'll discuss in this article are `git reset` and `git revert`. These commands can help you undo your commits and go back to a previous commit. 

They are not exactly the same, though, so we'll make this article a bit more practical by demonstrating how each command works in a project.

Anyone can follow along with this tutorial because it's not going to be language specific — we'll make use of a text (txt) file. 

## How to Revert to a Previous Commit Using the `git reset` Command

In this section, we'll go through the process of creating a new file and making three commits. You'll then see how you can revert to either the last commit or any other commit using the commit ID.

To get started, I've created a file called `tasks.txt`. The file has this in it:

```txt
1. code.
2. Practice.
3. Build. 
```

Next, we're going to initialize, add, and commit this file: 

```bash
git init
git add tasks.txt
git commit -m "first commit"
```

We have made the first commit. 

We'll repeat the process above two more times but we'll add an extra line of text to the file before each commit. That is:

```txt
1. code.
2. Practice.
3. Build. 
4. Research. 
```

```bash
git add tasks.txt
git commit -m "second commit"
```

Lastly, for the third commit:

```txt
1. code.
2. Practice.
3. Build. 
4. Research. 
5. Write.
```

```bash
git add tasks.txt
git commit -m "third commit"
```

Now we have three commits. To revert to a previous commit, you must first get the commit ID. To do that, run the command below:

```bash
git log --oneline
```

In my terminal, I have this:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/git-commit.PNG)
_git log --oneline_

As you can see above, this command lists all your commits along with their IDs. 

To go back to the second commit, you run the `git reset` command followed by the commit ID. That is:

```bash
git reset 5914db0
```

If you've followed up to this point, you'll not notice any difference in the file (you'll see how to undo both the commit and any changes made to the file later). 

The file still looks this way:

```txt
1. code.
2. Practice.
3. Build. 
4. Research. 
5. Write.
```

But when we run the `git log --oneline` command, the third commit wont't be in the log of commits:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/second-commit.PNG)
_git log --oneline_

We've successfully gone back to a previous commit.

If you want to undo a commit and the all the changes made after that commit, you attach the `--hard` flag to your `git reset` command. 

Let's test this out by reverting back to the first commit:

```bash
git reset 89f6c3d --hard
```

This is what the text file looks like now:

```txt
1. code.
2. Practice.
3. Build. 
```

We're back to the initial state of the file at the point of the specified commit. All changes that were made to the file after that commit were deleted. When we check the commit log, we'll have just the first commit. 

While this seems like something cool to do, you should be careful when using this command. Especially when you're working with a team.

If you undo a commit and delete every file change that came after it, you might lose important changes made to your code by you and other teammates. This will also change the commit history of your project.

Luckily for us, there is way to recover the state of a deleted commit. You can learn more about that [here](https://www.freecodecamp.org/news/how-to-recover-a-deleted-file-in-git/). 

## How to Revert to a Previous Commit Using the `git revert` Command

I have already initialized the project and made three commits like we did in the last section. Here's what the commit log looks like:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/commit-log.PNG)
_git log --oneline_

To revert to the to the previous commit, run the `git revert` command along with the commit ID of the current commit. 

In our case, we'll be using the ID of the third commit:

```bash
git revert 882ad02
```

The command above will undo the current commit and revert the file to the state of the previous commit. When you check the commit logs, you'll have something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/revert-log.PNG)
_git log --oneline_

Unlike the `git reset` command, the `git revert` command creates a new commit for the reverted changes. The commit where we reverted from will not be deleted. 

So as you can see, `git reset` and `git revert` are not the same. 

`git reset` will undo changes up to the state of the specified commit ID. For example, reverting to the second commit ID will undo changes and leave the state of the file as the state of the second commit.

`git revert` will undo changes up to the state before the specified commit ID. For example, reverting to the second commit ID will undo changes and leave the state of the file as the state of the commit that comes before the second commit – the first commit.

The explanations above may seem confusing. The best way to understand it is to try it out yourself.

## When to Use `git reset` and `git revert`

You should use `git reset` when working on a local repository with changes yet to be pushed remotely. This is because running this command after pulling changes from the remote repo will alter the commit history of the project, leading to merge conflicts for everyone working on the project.

`git reset` is a good option when you realize that the changes being made to a particular local branch should be somewhere else. You can reset and move to the desired branch without losing your file changes.

`git revert` is a good option for reverting changes pushed to a remote repository. Since this command creates a new commit, you can safely get rid of your mistakes without rearranging the commit history for everyone else.

## Summary

In this article, we talked about reverting to previous commits in Git. 

We talked about two main commands that showed how to undo Git changes – the `git reset` and `git revert` commands.

We also saw how both commands work using practical examples.

Happy coding!


---
title: 5 Git Commands You Should Know, with Code Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-09T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/5-git-commands-you-should-know-with-code-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a67740569d1a4ca2575.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: Git
  slug: git
- name: Software Engineering
  slug: software-engineering
seo_title: null
seo_desc: 'By Sarah Chima Atuonwu

  I''ve used Git for some years now, and I still find myself googling how to do some
  basic tasks. So this article is my attempt to learn how to do some of these things
  by writing about them. And even if I still forget, at least I''...'
---

By Sarah Chima Atuonwu

I've used Git for some years now, and I still find myself googling how to do some basic tasks. So this article is my attempt to learn how to do some of these things by writing about them. And even if I still forget, at least I'll have a reference where I can easily find these commands – and you will, too.

Before we move on to learn these things, something a colleague of mine once said has stuck with me. He told me that everything is possible with Git and that nothing is lost in Git. 

I don't know if the former part of his statement is entirely true but I keep it in mind every time I try to do something with Git. I believe that I'm going to find a command that will help me do what I need to do. I just have to google with the right words. If you are new to Git, I want you to believe that, too.

In this article, we'll learn how to do the following:

1. Add remote repositories
2. Change remote repositories
3. Delete a branch
4. Merge a file from one branch to another
5. Undo a commit locally and remotely

Though this article is intended for people with a basic knowledge of Git, I'll do my best to explain terms as much as possible.

## 1. Add Remote Repositories

Remote repositories are versions of your projects that are stored on the internet or elsewhere. Adding a remote repository is a way of telling Git where your code is stored. 

We can do this using the URL of the repository. This could be the URL of your repository, another user's fork, or even a completely different server.

When you clone a repository, Git implicitly adds that repository as the `origin` remote for you. To add a new Git repository, you use this command:

```text
git remote add <shortname> <url>
```

where `shortname` is a unique remote name and `url` is the url of the repository you want to add.

For example, if I want to add a repository with the shortname `upstream`, I can do this:

```text
git remote add upstream https://github.com/sarahchima/personal-website.git
```

Remember that your `shortname` can be anything, it just has to be unique, that is different from what the names of the remote repositories you already have. It should also be something you can easily remember for your sanity.

To view the list of remote URLs you have added, run the following command:

```text
git remote -v
```

You'll see a list of the remote names and the URLs you have added.

But what if you want to change these remote URLs? Let's move to the next Git command.

## 2. Change remote repositories

There are several reasons why you may want to change a remote URL. For example, I recently had to move from using `https` URLs to `SSH` URLs for a project I worked on.

To do this, you use the following command:

```text
git remote set-url <an-existing-remote-name> <url>
```

For this command to work, the remote name has to be an existing remote name. That means it won't work if you've not added that remote name before.

Using the example above, if I want to change the remote URL, I'll do this:

```text
git remote set-url upstream git@github.com:sarahchima/personal-website.git
```

Remember to run `git remote -v` to verify that your change worked.

Enough about remote repositories. Let's move on to something different.

## 3. Delete a branch both locally and remotely

A branch is a version of the repository that is different from the main working project. You may want to read up on Git branches and how to add a branch if you are not familiar with that process.

### How to delete a local branch

To delete a branch locally, make sure you are not on the branch you want to delete. So you have to checkout to a different branch and use the following command:

```text
git branch -d <name-of-branch>
```

So if I want to delete a branch named `fix/homepage-changes`, I'll do the following:

```text
git branch -d fix/homepage-changes
```

You can run `git branch` on your terminal to confirm that the branch has been successfully removed.

Sometimes you may have to delete a branch you've already pushed to a remote repository. How can you do this?

### How to delete a remote branch

To delete a branch remotely, you use the following command:

```text
git push <remote-name> --delete <name-of-branch>
```

where `remote-name` is the name of the remote repository you want to delete the branch from.

If I want to delete the branch `fix/homepage-changes` from `origin`, I'll do this:

```text
git push origin --delete fix/homepage-changes
```

The branch will be deleted remotely now.

## 4. Merge a file from one branch to another

Sometimes, you may want to merge the content of a specific file in one branch into another. For example, you want to merge the content of a file `index.html` in the `master` branch of a project into the `development` branch. How can you do that?

First, checkout to the right branch (the branch you want to merge the file) if you've not already done so. In our case, it's the `development` branch.

```text
git checkout development
```

Then merge the file using the checkout --patch command.

```text
git checkout --patch master index.html
```

If you want to completely overwrite the `index.html` file on the `development` branch with the one on the `master` branch, you leave out the `--patch` flag.

```text
git checkout master index.html
```

Also, leave out the `--patch` flag if the `index.html` file does not exist on the `development` branch.

## 5. Undo a commit

There are times when you've committed your changes incorrectly and you want to undo this commit. Sometimes, you may have even pushed the changes to a remote branch. How do you undo or delete this commit? Let's start with undoing a local commit.

### How to undo a local commit

One way you can undo a commit locally is by using `git reset`. For example, if you want to undo the last commit made, you can run this command:

```text
git reset --soft HEAD~1
```

The `--soft` flag preserves the changes you've made to the files you committed, only the commit is reverted. However, if you don't want to keep the changes made to the files, you can use the `--hard` flag instead like this:

```text
git reset --hard HEAD~1
```

Note that you should use the `--hard` flag only when you are sure that you don't need the changes.

Also, note that `HEAD~1` points to the last commit. If you want to undo a commit before that, you can use `git reflog` to get a log of all previous commits. Then use the `git reset` command with the commit hash (the number you get at the beginning of each line of history). For example, if my commit hash is `9157b6910`, I'll do this

```text
git reset --soft 9157b6910 
```

### How to undo a remote commit

There are times you want to undo a commit you have pushed to a remote repository. You can use `git revert` to undo it locally and push this change to the remote branch.

First, get the commit hash using git reflog.

```text
git reflog
```

Then revert it. Assuming my commit hash is 9157b6910, I'll do the following:

```text
git revert 9157b6910 
```

Finally, push this change to the remote branch.

## Summary

In this article, we discussed commands to do the following in Git:

1. Add Remote Repositories
2. Change remote repositories
3. Delete a branch
4. Merge a file from one branch to another
5. Undo a commit locally and remotely

Maybe someday, I'll write about more things you can do with Git.

I hope you enjoyed the article. Thanks for reading.

_Want to get notified when I publish a new article? [Click here](https://mailchi.mp/69ea601a3f64/join-sarahs-mailing-list)._


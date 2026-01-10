---
title: Force Pull in GitHub – How to Overwrite on Local Changes with Git
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-02-16T17:32:02.000Z'
originalURL: https://freecodecamp.org/news/force-pull-in-github-how-to-overwrite-on-local-changes-with-git
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/jannis-brandt-4mHaSX8zvJI-unsplash.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'While working on a project as part of a team, you may get an error message
  telling you that you can''t execute git pull on your repository because you have
  local changes.

  Why does this happen?

  This error usually occurs when several people are introduc...'
---

While working on a project as part of a team, you may get an error message telling you that you can't execute `git pull` on your repository because you have local changes.

Why does this happen?

This error usually occurs when several people are introducing updates to the same file. Essentially, there are identical files with different content.

You may want to force `git pull` and overwrite your local changes with the ones in the remote repository.

By default, Git will not overwrite the changes. Instead, for safety reasons, it lets you know that you have local changes that will get overwritten by the new changes introduced and committed to the Git repository. 

In this article, you will learn how to overwrite local changes with the latest ones from the remote repository.

Let's get into it!

## How To Force `git pull` To Overwrite Local Changes in Git

Keep in mind that when you execute the commands in the following sections, you will lose your uncommitted local changes on your system. All changes will get replaced by the ones on the repository.

### Fetch All Remote Changes

Firstly, fetch all of the most recent changes from the remote repository.

To do this, you need to run the `git fetch` command like so:

```bash
git fetch --all
```

The command above will download the latest updates from the remote and sync your local repository to the remote. 

### Reset Your Local Branch

Next, execute the `git reset --hard` command.

The general syntax for this command looks something like the following:

```bash
git reset --hard remote/remote-branch-name
```

So, if the `remote-branch-name` is called `main`, you write the following:

```bash
git reset --hard origin/main
```

This command will discard and overwrite all of your uncommitted local changes and set the state of the branch to the state of the remote you just fetched. 

The `--hard` option performs a hard reset on the `origin/main` branch.

You will lose any uncommitted local changes tracked by Git. Local files and directories not tracked by Git are not affected.

### Remove Untracked Files and Folders

To remove any files and directories not tracked by Git from your working directory, you can  use the `git clean` command:

```bash
clean -fd
```

Keep in mind that this operation is irreversible!

### Pull

Finally, execute the `git pull` command:

```bash
git pull
```

## How to Force `git pull` and Save Local Changes in Git

If you want to be safe, you may want to save uncommitted local changes, as you will lose them after executing the `git reset --hard` command.

You can use the `git stash` command to save uncommitted local changes for later use:

```bash
git stash
```

This command will save local changes in a stash, and you will be able to apply them in the future if you need to after the `fetch`, `reset`, and `clean` steps mentioned in the previous section.

To reapply the stashed changes at a later date, use the `git stash pop` command:

```bash
git stash pop
```

## Conclusion

In this article, you learned how to force `git pull` to overwrite local changes in Git and how to save local changes in a stash if needed.

Thank you for reading, and happy coding!




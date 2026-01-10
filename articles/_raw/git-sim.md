---
title: How to Visualize Confusing Git Commands with Git-Sim
subtitle: ''
author: Jacob Stopak
co_authors: []
series: null
date: '2023-01-23T14:57:06.000Z'
originalURL: https://freecodecamp.org/news/git-sim
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/git-sim-merge_01-05-23_09-44-46-1.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Git is an essential tool for developers to learn in order to effectively
  collaborate on source code. But certain Git concepts and commands are notoriously
  difficult for devs to learn.

  Not only that, but Git commands often have nuances that lead to va...'
---

Git is an essential tool for developers to learn in order to effectively collaborate on source code. But certain Git concepts and commands are notoriously difficult for devs to learn.

Not only that, but Git commands often have nuances that lead to varying results on the state of your local repository. In addition, even once you learn a specific Git command, you might not use that command for a significant amount of time before needing it again.

This leads devs to repeatedly search Google or Stackoverflow for specific situational Git commands over and over again, praying that parallel results will occur when executing the command locally.

This commonly occurs with notoriously confusing Git commands such as `git reset`, `git merge`, and `git rebase`.

In this article, we'll provide an overview of these 3 commands using a command-line tool called [Git-Sim to visually simulate Git operations in your local repo](https://initialcommit.com/blog/git-sim). This tool will enable us to easily create handy diagrams and animations illustrating how each Git command will affect the state of your own Git repo.

## `git reset` – How to Reset Git HEAD while Managing Changes

The [git reset command](https://initialcommit.com/blog/git-reset) is one that I constantly find myself Googling before I need to use it.

This is partly because there are several commands that you can use to [undo changes in Git](https://initialcommit.com/blog/undoing-changes-in-git), and I want to make sure I'm choosing the right one.

Also, any command that could accidentally lead to "losing work", like `git reset --hard` is worth taking a few seconds beforehand to make sure you're confident in what you're about to do.

### What does `git reset` do?

In a nutshell, git reset simply moves the tip of the current branch back to a previous commit. In that sense it can be used to "undo" the changes applied by commits between the current commit and the commit you want to reset back to.

Technically speaking, a Git branch is just a name (or label) that points to the newest commit in a chain of commits. This gets moved forward each time you make a new commit on a branch, and therefore always identifies what is known as the **branch head** commit.

The `git reset` command moves this branch label back to a previous commit, which becomes the new branch head – effectively undoing all the changes in between.

Let's consider a simple example. Assume we have a repository which only tracks 1 file called `cheese.txt`. The repo has 5 commits, each changing the text content within the file to a different cheese name.

We can illustrate this visually using Git-Sim by running the `$ git-sim log` command to visually simulate the output of the `$ git log` command:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-log_01-05-23_09-33-17.jpg align="left")

*Note: we actually simulated this* `git log` output using the git-sim command `$ git-sim log`, which draws 5 commits in the output image by default.

As you can see, we have a `main` branch pointing to the commit with ID `14c121...` with commit message `Cheddar`.

Now let's say we want to undo the commits changing the content of `cheese.txt` to "cheddar" and "Swiss". We can do this using the `git reset` command to reset the `main` branch back 2 commits, to "Gouda":

```sh
$ git reset HEAD~2
```

But if we are ever unsure about the impact this command will have, we can simulate it first using Git-Sim:

```sh
$ git-sim reset HEAD~2
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-reset_01-05-23_09-34-16.jpg align="left")

Or if you prefer, the simulation can be rendered as a dynamic video animation using Git-Sim's `--animate` flag as follows:

```sh
$ git-sim --animate reset HEAD~2
```

%[https://youtu.be/mJHdM6nTjb4] 

As you can see, the Git-Sim simulated output above shows that the `main` branch and `HEAD` pointer are reset backward 2 commits to the "Gouda" commit.

In addition, we can see that Git-Sim created a table with 3 columns:

* **Changes deleted from**
    
* **Working directory modifications**
    
* **Staging area**
    

By default, the `git reset` command applies the `--mixed` flag behavior, which moves any changes in reset commits into the working directory.

Git-Sim reflects this in the simulated output above by adding the file `cheese.txt` into the **Working directory modifications** column.

Now that you've simulated the `git reset` command using Git-Sim and can clearly see the expected result in the image output above, you can run the actual Git command `$ git reset HEAD~2` with confidence.

In addition to `--mixed`, Git-Sim understands `--soft` and `--hard` resets. The command `$ git-sim reset --soft HEAD~2` would keep the undone changes in the **Staging area** column, while the command `$ git-sim reset --hard HEAD~2` would place the undone changes in the **Changes deleted from** column since a hard reset discards changes to committed files.

Note that `git reset` doesn't ever delete any commits (even when using the `--hard` option), which means you don't lose any work at the time of executing it. But keep in mind that commits can become *orphaned*, meaning that certain commits become unreachable by any branch head. Git will eventually remove these via garbage collection, but they are retrievable for a while if you need them!

## `git merge` – How to Merge Changes from Multiple Branches

The [git merge command](https://initialcommit.com/blog/git-merge) is another tricky one for beginner and intermediate Git users to wrap their heads around. There are several different types of merges that Git performs depending on the circumstances.

To provide a foundation, this sequence of two commands highlights how the merge syntax works:

```sh
$ git checkout <merge-into>
$ git merge <merge-from>
```

The first command shows that the `<merge-into>` branch is the active branch that you currently have checked out in your working directory. Then when you execute the merge, you specify `<merge-from>` as the branch that you want to merge changes from, into the active branch.

So for example, the following commands would merge changes from the `dev` branch into `main`:

```sh
$ git checkout main
$ git merge dev
```

### Git three-way merge

The most common merge case occurs when the history of two branches has diverged and the developer wishes to recombine the changes. In this scenario, Git performs something known as a **three-way merge**.

It is called a three-way merge because Git uses three commits to determine how to combine changes in your diverged branches:

* The commit at the tip of branch A
    
* The commit at the tip of branch B
    
* The merge-base of the two branches
    

We can use Git-Sim to simulate a three-way merge which merges the changes in two new commits on the `dev` branch into `main`:

```sh
$ git checkout main
$ git-sim merge dev
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-merge_01-05-23_09-44-46.jpg align="left")

*Three-way merge output in Git-Sim*

In the example above, the tip of the `main` branch before the merge is commit `14c121` ("Cheddar"), and the tip of the `dev` branch is `f42fee` ("Asiago"). The third commit used in Git's three-way merge algorithm is commit `640bb5` which is the **merge base** of the two branches. You can identify this by tracing back both branches until you find the first common ancestor.

Using the content in these 3 commits, Git creates a new **merge commit** (labelled `abcdef` in the Git-Sim diagram above) which combines the changes from both branches.

Unlike regular commits, a merge commit has two parents instead of one, corresponding to the tips of the two branches that were merged together. These two parent relationships are denoted by the two dotted lines in the image above.

### Git fast-forward merge

A **fast-forward merge** in Git occurs when the branch you are merging from is just further along the same line of development as the active branch. Consider the example below:

```sh
$ git-sim log
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-log_01-05-23_09-49-08.jpg align="left")

In this case, the `dev` and `main` branches have not actually diverged – they both lie along the same line of development. As a result, if you check out the `dev` branch and try to merge in `main`, Git doesn't even need to actually need to merge the content from the two branches.

Instead, Git can simply repoint the `dev` branch ref to the same commit as `main` points to, which is `14c121`. (Remember a branch in Git is just a label pointing to a particular commit).

Git-Sim knows how to simulate this type of merge as well:

```sh
$ git checkout dev
$ git-sim merge main
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-merge_01-05-23_09-49-49.jpg align="left")

*Fast-foward merge*

Note that after checking out the `dev` branch and merging `main` into it, the `dev` branch label was simply *fast-forwarded* to the same commit as `main`, and no new merge commit was created.

However, in some cases you may want to **force** Git to create a merge commit even when doing a fast-forward merge.

This might be useful if you want to preserve the history of all merges so that your team knows when a merge was performed. You can do this using the `--no-ff` flag, which is also supported by Git-Sim:

```sh
$ git checkout dev
$ git-sim merge --no-ff main
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-merge_01-05-23_09-50-14.jpg align="left")

*Forced merge commit*

In the simulated output image above, Git created a new merge commit `abcdef` which the `dev` branch label now points to, even though it was possible to simply fast-forward to the commit pointed to by `main`.

Keep in mind that even when forcing a merge commit in this way, no divergence of branch history has taken place. Both branches still fall along a single line of development.

## `git rebase` – How to Move the Current Commit onto a New Base Commit

Lastly, we'll briefly cover one specific scenario of the standard [git rebase](https://initialcommit.com/blog/git-rebase) command. Instead of merging the contents of two branches, `git rebase <new-base>` reapplies the commits reachable by the current branch onto a new base commit, specified by `<new-base>`.

By default, `git rebase` runs in **standard mode**, which is what we'll be discussing here. The `-i` flag allows rebase to run in **interactive mode**, but that is out of the scope of this article.

Using our previous example repo, let's note the 2 new commits added to the `dev` branch `ead5cc` ("Fontina") and `f42fee` ("Asiago"):

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-log_01-05-23_09-53-00.jpg align="left")

Then we want to move these 2 new commits to the tip of the `main` branch using the `git rebase` command. This can be simulated using the commands:

```sh
$ git checkout dev
$ git-sim rebase main
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-rebase_01-05-23_09-53-34.jpg align="left")

In the simulated output above, the dotted lines show how the 2 new commits on the `dev` branch are rebased onto the tip of `main`.

In a standard rebase, Git identifies the number of commits to rebase by walking back from the tip of the active branch until a common ancestor commit is found between the two branches.

Of course, this common ancestor already exists on the destination branch, so the rebase does not need to include it, and can end at that point.

In this case, the two commits on the `dev` branch that don't yet exist on `main` are `ead5cc` ("Fontina") and `f42fee` ("Asiago"). These get rebased onto `main` as shown by the dotted lines above. Since commit `640bb5` ("Gouda") already exists on `main`, it is not included in the rebase.

Note that rebasing in Git actually rewrites commit history, since each commit ID depends on that commit's content *and* the history that comes before it.

Even if the content in the two rebased commits in the example above applies cleanly to the `main` branch, new commit ID's must be calculated since their history now differs from when they were applied to the `dev` branch.

For this reason, a good rule of thumb is to **only rebase commits locally that haven't yet been pushed to a remote repository**. This will ensure that you and your team maintain a consistent repository state for your project over time.

## Summary

In this article, we use the [Git-Sim tool](https://initialcommit.com/tools/git-sim) to provide an overview of 3 notoriously confusing Git commands – `git reset`, `git merge`, and `git rebase`.

We illustrated how to reset Git's HEAD pointer to a previous commit while managing committed files, staged files, and working directory files as desired using the `--soft`, `--mixed`, or `--hard` flags.

Then we outlined the basic merge types in Git, including the 3-way merge and the fast-forward-merge.

Finally, we discussed rebasing branches, which means moving a set of commits onto a new base commit.

For each of these commands, we showed how the Git-Sim command-line tool can be leveraged to create unique, customized simulations of your Git command's effects before running the actual Git command itself.

## Next Steps

If you're a visual learner and Git user, I encourage you to try out [Git-Sim](https://initialcommit.com/tools/git-sim) to simulate Git commands in your own local repos before running the actual commands.

This will give you the confidence to execute the actual Git commands, and even provide you with visual content to aid in documentation, content-sharing, and teaching others to use Git.

Git-Sim is a free and open-source tool written in Python, so if you're interested in contributing or if you find any bugs, feel free to check out the [Git-Sim project on GitHub](https://github.com/initialcommit-com/git-sim) and/or contact me at [jacob@initialcommit.io](mailto:jacob@initialcommit.io)!

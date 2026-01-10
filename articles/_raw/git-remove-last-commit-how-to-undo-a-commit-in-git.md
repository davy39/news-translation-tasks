---
title: Git Remove Last Commit – How to Undo a Commit in Git
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-09-21T17:42:10.000Z'
originalURL: https://freecodecamp.org/news/git-remove-last-commit-how-to-undo-a-commit-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-andrew-neel-2312369.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'Git is a powerful tool and the most popular version control system. It
  is how developers and technical teams collaborate and work together on projects.

  But what happens when you accidentally commit a file and realize that you shouldn''t
  have done that...'
---

Git is a powerful tool and the most popular version control system. It is how developers and technical teams collaborate and work together on projects.

But what happens when you accidentally commit a file and realize that you shouldn't have done that because that file contains an error?

There is no need to fret because Git allows you to undo your mistakes and go back to an earlier version of your project.

One of the most helpful features of Git is the ability to undo the changes you make to a project over time.

In this article, you will learn how to undo changes in Git depending on the state of your Git repository.

Here is what we will cover:

1. [How to undo local unstaged changes](#unstaged)
2. [How to undo local staged changes](#staged)
3. [How to undo local committed changes](#local-committed)
4. [How to undo public committed changes](#public-committed)

## How to Undo Local Unstaged Changes in Git <a name="unstaged"></a>

Say you are working on your local machine.  You made and saved some changes to a file locally, but you would like to discard them.

When you have yet to stage those changes, you haven't used the `git add` command.

In this case, you need to use the `git restore` command.

Specifically, the `git restore` command will look something like this:

```git
git restore filename
```

So, say you have a `README.md` file and you accidentally wrote and saved some text you want to discard.

You can first use the `git status` command to view the state of your Git repository.

This command will confirm that the file is unstaged (meaning you haven't used `git add` yet), and will let you view the files you may want to undo:

```git
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

Here is how you would undo the changes in the `README.md` file:

```git
git restore README.md
```

You can then use `git status` again to check the state of the repository:

```git
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Now, you have successfully discarded your most recent changes and reverted to the last committed version of your project.

## How to Undo Local Staged Changes in Git <a name="staged"></a>

A file is staged when you have used the `git add` command.

So, say you made some changes to the `README.md` file locally, you used the `git add` command which staged the changes, and then you realized that the text contains some mistakes.

First, run `git status` to make sure you have staged the file (meaning you used `git add`) :

```git
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md
```

As you can tell by the output of `git status`, you can use the following command to undo your changes:

```git
git restore --staged filename
```

This command will unstage the staged file, but will keep your changes.

Let's run `git status` again:

```git
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

Now, to discard the changes you made and restore the file to its original contents, use:

```git
git restore README.md 
```

And let's run `git status` one last time:

```git
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Now, the changes you made have gone and the file is reverted to the current committed version.

## How to Undo Local Committed Changes in Git <a name="local-committed"></a>

Say you made changes to a file, you staged the file with the `git add` command, and you committed the file with the `git commit` command.

This means that the commit exists only locally and has not been pushed to a remote repository yet.

First, use `git status` to check that you committed the file:

```git
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

Next, if you want to undo your last local commit, use the `git log` command:

The latest commit will have a commit hash (a long series of numbers and characters) and a `(HEAD -> main)` at the end – this is the commit you are looking to undo. 

The second to last commit has a commit hash and a `(origin/main)` at the end – this is the commit you want to keep and the commit you pushed to the remote repository.

After that, use the following command to undo the commit:

```git
git reset --soft HEAD~
```

Now, let's use `git log` again.

You should see the commit hash, and a `(HEAD -> main, origin/main)` at the end.

The last commit you made is no longer part of the repository's history and has been removed. 

The command above restored everything to the version of the file prior to that accidental or mistaken commit and has gone back one commit.

Let's check `git status` again

```git
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md
```


Keep in mind that although the `git reset --soft HEAD~` command undid your latest commit, it kept the changes you made.

## How to Undo Public Committed Changes in Git <a name="public-committed"></a>

What if you made changes to a file, you staged the file `git add`, committed it with `git command`, and pushed it to a remote repository with `git push` – but then realized you shouldn't have committed that file in the first place?

What do you do then?

First, use `git status` to check the state of the git repository:

```git
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

In the section above, you saw that each commit has a commit hash, which is a long series of numbers and characters.

To see the short version of the commit hash, use the following command:

```git
git log --oneline
```

With the `git log` command, you can also check which commit you want to undo. 

Say that your latest commit has a commit hash of `cc3bbf7`, which is followed by `(HEAD -> main, origin/main)`, and a commit message such as  "commit README.md file" .

To undo that specific commit, use the following command:

```git
git revert cc3bbf7 --no-edit
```

The command above will undo the changes by creating a new commit and reverting that file to its previous state, as if it never changed.

Lastly, use `git push` to push the change to the remote branch.

Once you do that, you will see that the commit message will be the same as the previous one but with the word `revert` preceding it, such as 
'Revert "commit README.md file"'.

Keep in mind that the commit history will show both commits separately:

```git
Revert "commit README.md file"
@john-doe
john-doe committed 9 minutes ago

commit README.md file
@john-doe
john-doe committed 16 minutes ago 
```

## Conclusion

And there you have it – you now know how to undo changes in Git.

To learn more about Git, check out the following free resources:

- [Git and GitHub for Beginners - Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk)
- [Git for Professionals Tutorial - Tools & Concepts for Mastering Version Control with Git](https://www.youtube.com/watch?v=Uszj_k0DGsg)
- [Advanced Git Tutorial - Interactive Rebase, Cherry-Picking, Reflog, Submodules and more](https://www.youtube.com/watch?v=qsTthZi23VE)


Thank you for reading and happy coding :) 



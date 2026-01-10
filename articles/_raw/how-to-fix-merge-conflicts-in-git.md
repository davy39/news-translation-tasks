---
title: How to Fix Merge Conflicts in Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-28T20:25:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-merge-conflicts-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/fixConflicts.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'If you’ve ever worked on a team that''s working on a large codebase, you’ve
  likely experienced merge conflicts while creating a pull request or merging two
  branches.

  Even if you’ve never worked with a team or on a large codebase, it is still possible
  ...'
---

If you’ve ever worked on a team that's working on a large codebase, you’ve likely experienced merge conflicts while creating a pull request or merging two branches.

Even if you’ve never worked with a team or on a large codebase, it is still possible to have merge conflicts as long as you have more than one branch. In the process of merging one branch with another, a merge conflict may occur.

In this article, you’ll learn about merge conflicts in Git and the types of merge conflicts you might encounter. Most importantly, you will learn how to resolve merge conflicts on GitHub and with VS Code’s 3-way merge editor.

## What We’ll Cover
- [What is a Merge Conflict in Git?](#heading-what-is-a-merge-conflict-in-git)
- [What to Do When Merge Conflicts Occur](#heading-what-to-do-when-merge-conflicts-occur)
- [What are the Types of Merge Conflicts in Git?](#heading-what-are-the-types-of-merge-conflicts-in-git)
  - [Content Merge Conflict](#heading-content-merge-conflict)
  - [Structural Merge Conflict ](#heading-structural-merge-conflict)
- [How to Resolve Merge Conflicts in Git](#heading-how-to-resolve-merge-conflicts-in-git)
   - [How to Resolve Merge Conflicts in Git with the GitHub interface](#heading-how-to-resolve-merge-conflicts-in-git-with-the-github-interface)
   - [How to Resolve Merge Conflicts in Git with VS Code](#heading-how-to-resolve-merge-conflicts-in-git-with-vs-code)
   - [How to Resolve Merge Conflicts in Git with VS Code 3-way Merge Editor](#heading-how-to-resolve-merge-conflicts-in-git-with-vs-code-3-way-merge-editor)
- [Wrapping Up](#heading-wrapping-up)


## What is a Merge Conflict in Git?
In Git, a merge conflict occurs when you or any of your team members make conflicting changes to the same file from two different branches.

Merge conflicts can also occur even if you’re not working with team members. If you’ve made changes to the same file from different branches and the changes are conflicting, there will be a merge conflict.

On many occasions, Git automatically handles merging for you. But if there are conflicting changes you make to the same file, you have to resolve them manually.

A sample scenario of a merge conflict could look like this:
- you work in branch `main` and you make changes to line 1 of a mytext.txt file, say `Hi world`.
- you switch to branch `new-feature` and you make a change to the same line two of `mytext.txt`, say `Hello earth`.

If you attempt to merge the branch `new-feature` to `main`, Git won’t be able to automatically decide which one to accept between `Hi world` and `Hello earth`. So, Git will raise a merge conflict error and tell you to manually resolve the conflict.


## What to Do When Merge Conflicts Occur
It’s not the end of the world if merge conflicts occur while you're working. Git is just telling you "I want to do this merging for you, but there’s something you have to do for me first".

When these conflicts occur and you attempt to resolve them, Git will automatically annotate the conflicting lines for you with the lesser than symbol (`<`), equals sign (`=`), and greater than symbol (`>`) like this:

```
<<<<<<< 
=======
>>>>>>> 
```

![Screenshot-2023-03-28-at-16.36.58](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-16.36.58.png)

Everything between the lesser than (`<`) and equals signs (`=`) is the change in the current branch (the branch you're merging into). Everything between the equals (`=`) and greater than (`>`) signs is the incoming change from the branch you want to merge to another branch.

It is left up to you to remove those annotations and decide how you want the conflicting lines to be – you can accept one of the changes or both of them.

So, instead of looking at merge conflicts as a stumbling block, you can just see them as some annotations you need to remove and things you need to accept or reject.

Keep reading this article so you can see how to resolve a merge conflict. But before that, let’s look at the types of merge conflicts.


## What are the Types of Merge Conflicts in Git?
There are two types of merge conflicts. They are *content conflict* and *structural conflict*.

### Content Merge Conflict
Content conflict occurs when the changes you make in two different branches affect the same lines of code in a file. This results in conflicting changes that cannot be automatically merged by Git.

For example, you make the change `display: flex` to line 2 in one branch and another change `text-align: center` to the same line 2 in the same file in another branch.

When this *content conflict* happens, Git will stop the merging process and prompt you to make adjustments to the code before moving forward.

### Structural Merge Conflict
Structural conflict occurs when the changes you make in two different branches affect the same file but do not conflict with each other line-by-line. Instead, the changes affect the structure or organization of the file, such as renaming a variable, or function, or moving a block of code.

If this structural conflict happens, Git won’t be able to determine which of the changes to accept and will prompt you to decide which changes you want.


## How to Resolve Merge Conflicts in Git
To show you how to resolve merge conflicts, I have initialized Git in a working directory (folder) by running `git init`. I have also created a new branch I call `new-feature` by running `git checkout -b new-feature`.

Running `git branch` shows that I have branches `main` and `new-feature`:

![Screenshot-2023-03-28-at-11.51.38](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-11.51.38.png)

I have also pushed both branches to GitHub, so I can show you how to resolve merge conflicts on GitHub:

![Screenshot-2023-03-28-at-11.52.10](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-11.52.10.png)

I have added some code to the HTML and JavaScript files in the directory. I triggered some conflicts in the two files and made some commits:

![Screenshot-2023-03-28-at-11.53.19](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-11.53.19.png)


## How to Resolve Merge Conflicts in Git with the GitHub Interface
Since I have pushed the `new-feature` branch to GitHub, GitHub will ask that I create a pull request so the `new-feature` branch will be merged to `main`:

![Screenshot-2023-03-28-at-12.00.23](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-12.00.23.png)

In this case, immediately you click on “Compare and Pull”, you will see that there can’t be an automatic merging because there’s a conflict:

![Screenshot-2023-03-28-at-13.10.15](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.10.15.png)

This means there’s a conflict you need to resolve. Create the pull request and scroll down to see where you can resolve the conflict, then click the “Resolve conflicts” button:

![Screenshot-2023-03-28-at-13.12.39](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.12.39.png) 

When you click on “Resolve conflicts”, you will get an editor, and to the right, you will see the list of files that have the conflicts:

![Screenshot-2023-03-28-at-13.15.12](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.15.12.png)

In the editor, you will see the lines where the conflicts have occurred:

![Screenshot-2023-03-28-at-13.16.24](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.16.24.png)

You can see that the changes in the incoming branch are between the lesser than (`<`) and equals (`=`) signs, while the changes in the branch you want to merge into are surrounded by greater than (`>`) and equals (`=`) signs.

Choose the line you want, remove the annotations, and click “Mark as resolved” in the top right corner:

![Screenshot-2023-03-28-at-13.20.10](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.20.10.png)

Repeat the same process for any other file that have some conflict(s) too.

If you want, you can keep both lines. Just make sure you remove the annotations.

After doing that, click on “Commit merge” in the top right corner:

![Screenshot-2023-03-28-at-13.23.46](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.23.46.png)

Now, there should not be a merge conflict any more:

![Screenshot-2023-03-28-at-13.24.30](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.24.30.png) 


## How to Resolve Merge Conflicts in Git with VS Code
Many popular code editors have interfaces for resolving a merge conflict when you try to merge locally.

When you switch to the branch you want to merge into and run `git merge branch-to-merge`, you will be prompted to resolve some conflicts (if any). If there are conflicts to resolve, the interface looks like this in VS Code:

![Screenshot-2023-03-28-at-12.21.03](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-12.21.03.png)

At this stage, if you’re not ready to resolve the conflicts, you can abort the merging by running `git merge --abort`.

But if you want to resolve the conflicts, you can either accept the incoming change(s), accept the current change, or accept both changes.

If you select any of the three, the merge conflict(s) will be resolved. After that, add the file and commit it the usual way you would do it:

```
git add .
git commit -m "<commit message>"
```


## How to Resolve Merge Conflicts in Git with VS Code 3-way Merge Editor
You can also rebase a conflict with the VS Code 3-way merge editor. 

After running `git merge <branch-to-merge>`, click on the “Resolve in Merge Editor” button

You will see you now have 3 views. You will see the changes in the incoming branch on the right, the changes in the branch you want to merge into on the right (the current branch), and the preview below the two:

![Screenshot-2023-03-28-at-14.32.49-copy](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-14.32.49-copy.png)

Now start resolving the conflicts by selecting any of the available options: 
- Accept Incoming
- Accept Combination (Incoming First)
- Accept Current
- Accept Combination (Current First)

Incoming is the change in the branch you want to merge into a target branch, and current is the change already in the branch you want to merge into.

Switch to each file, click on the “Resolve in Merge Editor” button, and select any of the options there.

![Screenshot-2023-03-28-at-14.31.34](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-14.31.34.png)

You can also resolve the conflicts by entering the right code in each of the files.

When you are satisfied, click on “Complete Merge” in each merge editor:

![Screenshot-2023-03-28-at-14.32.49](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-14.32.49.png)

You have to add the files again and commit them:

```
git add .
git commit -m "<commit-message>"
```

That’s it! If you want the 3-way merge editor to open automatically when you want to merge conflicts, click “Settings” and search for “merge editor”, then checkmark “open the merge editor for files that are currently under conflicts”.

![Screenshot-2023-03-28-at-15.01.54](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-15.01.54.png)


## Wrapping Up
As you’ve seen, having a Git conflict is not as scary as it seems, and resolving it is not an impossible task. You can typically resolve it right on GitHub or in your text editor. The VS Code 3-way merge editor is also a convenient way to resolve a merge conflict.

If you’ve created a PR for a large codebase and you have a merge conflict, another way you can resolve it might be rebasing with main by running `git pull --rebase upstream main` (as the case may be). After that, you will be presented with an interface to resolve the conflicts and the files containing the conflicts. When you are done, run `git add .`, `git rebase --continue`, and then force push to your branch.



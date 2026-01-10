---
title: Git Delete Remote Branch – How to Remove a Remote Branch in Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-16T17:20:10.000Z'
originalURL: https://freecodecamp.org/news/git-delete-remote-branch
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-nidhi-tokas-dahiya-867677.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'When you''re working with Git, you might want to delete remote branches
  pushed to a platform like GitHub for various reasons.

  In this article, I will show you how to delete a remote branch in Git. But firstly,
  let’s look at how to delete a local branc...'
---

When you're working with Git, you might want to delete remote branches pushed to a platform like GitHub for various reasons.

In this article, I will show you how to delete a remote branch in Git. But firstly, let’s look at how to delete a local branch.

I’ll use Git bash in this article because it makes working with Git easier than any other terminal. But it's okay if you use another terminal. The commands are still the same.

## How to Delete a Local branch in Git
Run `git branch` or `git branch -a` to see the branches you’ve created for your project.
![ss1-3](https://www.freecodecamp.org/news/content/images/2022/08/ss1-3.png) 

If you run `git branch -a` in particular, it will make the remote branches distinct. This is a feature I've seen only in Git bash.
![ss2-3](https://www.freecodecamp.org/news/content/images/2022/08/ss2-3.png)

In this situation, `test-branch2` is a branch I’m yet to push, so it’s a local branch.

To delete a local branch, run `git branch -d branch-name`.

If you type in the command correctly, you will get a response that the branch has been deleted.
![ss3-3](https://www.freecodecamp.org/news/content/images/2022/08/ss3-3.png)

## How to Delete a Remote Branch in Git

If you try to delete a remote branch with the same command used for deleting a local branch, you will get a message that the branch has been deleted. But if you run `git branch -a`, the branch will still be listed.
![ss4-4](https://www.freecodecamp.org/news/content/images/2022/08/ss4-4.png)

And if you check GitHub, the branch will still be there:
![ss5-4](https://www.freecodecamp.org/news/content/images/2022/08/ss5-4.png) 

To completely remove a remote branch, you need to use the `git push origin` command with a `-d` flag, then specify the name of the remote branch.

So the syntax representing the command for removing a remote branch looks like this: `git push origin -d branch-name`.

For instance, to remove the `test-branch1` branch, I will run `git push origin –d test-branch1`:
![ss6-3](https://www.freecodecamp.org/news/content/images/2022/08/ss6-3.png) 

To verify that the remote branch has been deleted, run `git branch -a` again.
![ss7-2](https://www.freecodecamp.org/news/content/images/2022/08/ss7-2.png) 

You can see the remote branch, `test-branch1`, is not listed anymore.

If you check GitHub again, it won’t be there:
![ss8-2](https://www.freecodecamp.org/news/content/images/2022/08/ss8-2.png) 

## Wrapping Up

Bear in mind that to completely remove a Git branch from your project, you need to use the `git push origin` command.

That’s because you’ve pushed the branch already. So, running the `git branch -d` command would only remove the branch locally. 

And if you have issues working with Git, I suggest you switch your terminal to Git bash. That's because it has syntax highlighting for everything – making it easier to work with Git.

Thank you for reading. 



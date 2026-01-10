---
title: How to Create a Local Branch in Git
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-13T16:41:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-local-git-branch
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'When you''re making changes to a Git repository, it''s a best practice
  to push to a different branch first. This lets you compare changes before submitting
  a pull request and finally merging it.

  This is especially crucial when working with other develo...'
---

When you're making changes to a Git repository, it's a best practice to push to a different branch first. This lets you compare changes before submitting a pull request and finally merging it.

This is especially crucial when working with other developers.

Your repository's `main` branch, which is regarded as the authoritative branch, is the only branch present by default. Now let's quickly go over how to create branches in Git.

## How to Create Branches in Git

In essence, there are two methods in Git for creating branches.

You can use a single command to create the branch and switch to it. Or you can create the branch first using one command and then switch to it later using another command when you wish to work with it.

Here's the TL;DR quick version of the code:

```bash
// create a branch and switch to the branch
$ git checkout -b <branch-name>

// create a branch only
$ git branch <branch-name>
```

### How to Create a Git Branch and Switch to a New Branch

We can create a new branch and switch to it using the `git checkout` command with the `-b` option and `<branch-name>`. It looks like this:

```bash
$ git checkout -b <branch-name>
```

Assume we want to create a new Git branch named "pagination" from the main branch. To accomplish this, we will use the "git checkout" command with the "-b" option and the branch name "pagination".

![](https://paper-attachments.dropbox.com/s_E7E3F14C4905C4CE20AE3FDC33EFE78C3CAFED59288B605B89A9E40497700515_1657112003074_branch.gif align="left")

As you can see, we created a new branch, and the checkout command caused our branch to automatically switch from "main” to “pagination”.

Let's now look at how to create a Git branch without switching to it.

### How to Create a Git Branch Without Switching to the New Branch

This is the standard method for creating a branch using the `git branch` command and specifying the name of the Git branch you want to create.

```bash
$ git branch <branch-name>
```

For example, as we did earlier, we can create a branch for “pagination” by replacing “” with “pagination”. Here's what that would look like:

![](https://paper-attachments.dropbox.com/s_E7E3F14C4905C4CE20AE3FDC33EFE78C3CAFED59288B605B89A9E40497700515_1657114781462_switch.gif align="left")

As we can see the branch did not change, but the new branch was created. To see a list of all available branches, you can use this command:

```bash
$ git branch
```

Finally, suppose we later wish to switch to our new Git branch or any other branch we previously created. In that case, we can make use of the `git checkout` command.

```bash
$ git checkout <branch-name>
```

## Conclusion

In this article, we learned how to use Git commands in our terminal to create a branch locally.

If we want to add this branch remotely, all we have to do is push it to our Git provider such as GitHub using the command below:

```bash
$ git push -u origin <branch-name>
```

Learn how to [clone a specific branch with Git via this article](https://joelolawanle.com/posts/how-to-clone-a-specific-branch-with-git).

Happy coding!

You can access over 200 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.

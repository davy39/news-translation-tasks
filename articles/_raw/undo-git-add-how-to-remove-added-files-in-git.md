---
title: Undo Git Add – How to Remove Added Files in Git
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-23T18:27:08.000Z'
originalURL: https://freecodecamp.org/news/undo-git-add-how-to-remove-added-files-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template.png
tags:
- name: Git
  slug: git
seo_title: null
seo_desc: 'Git is a powerful version control and collaboration tool. It allows developers
  to work together seamlessly on projects.

  But even the most experienced developers can make mistakes while using Git, such
  as accidentally adding files that were not meant ...'
---

Git is a powerful version control and collaboration tool. It allows developers to work together seamlessly on projects.

But even the most experienced developers can make mistakes while using Git, such as accidentally adding files that were not meant to be committed. This can be a problem, especially if the added files contain sensitive or confidential information.

In this article, you will learn how to undo the “Git add” command, which means removing files from the staging area and preventing them from being committed.

## How to Add Files in Git and Confirm

You probably know how to add files to the staging area using the `git add` command. When you want to add all files, you use the dot(.), but when you want to add specific file(s), you attach the file names/path:

```bash
// stage all files in current directory
git add .

// stage single file
git add <file>

// stage multiple files
git add <file1> <file2> <file3> ...
```

When you stage files, you can confirm using the `git status` commands, which shows a list of all staged files:

![](https://paper-attachments.dropboxusercontent.com/s_4E8AA27FDBD6E92188ADA8CF7AE76BB35CFED775D18B77141314D06FC8C13ADB_1679558784394_image.png align="left")

## How to Remove Added Files in Git

There are two major commands that you can use to undo “git add” or remove added files in Git. In other words, you can use two major commands to remove staged files from the staging area.

These are the `git reset` and `git rm --cached` commands. But these commands are quite different from each other.

### How to Remove Added Files in Git with `git reset`

`git reset` is used to unstage changes that have been added to the staging area. This means it will remove the files from the staging area but keep the changes in your “working directory”.

To remove **a single file** from the staging area, you can use the following command:

```bash
git reset <file>
```

To remove **all files** from the staging area, you can use the following command:

```bash
git reset
```

So you are not confused, let me explain what the working directory means. The working directory is where you make changes to your code, while the staging area is an intermediate step where you prepare changes for committing to your repository.

When you use `git reset` to unstage changes from the staging area, Git will remove them but keep them in your working directory. This means that the changes you made to the files will still be visible in your local files, and you can continue to make further changes if needed.

### How to Remove Added Files in Git with `git rm --cached`

On the other hand, `git rm` is used to remove a file from the staging area and the working directory. This means that it will permanently delete the file from your repository.

To remove a file from the repository, you can use the following command:

```bash
git rm <file>
```

But you only want to “unstage” your files (that is, undo the `git add` command) and not “remove” them from your working repository. This is where you use the `--cached` flag. The cached option specifies that the removal should happen only on the staging index. Working directory files will be left alone.

```bash
git rm --cached <file>
```

It's important to note that using `git rm --cached` is not a complete solution for keeping files in the repository. The file can still be deleted from the working directory accidentally or intentionally.

Because of this, it's recommended to use this command with caution and to make sure you are intentionally removing files you no longer need to track in Git.

## Conclusion

One advantage of having multiple Git commands that can achieve similar results, such as `git rm` and `git reset`, is that they provide users with flexibility and choice. Different users may have different preferences or workflows, and having multiple options allows you to choose the best method.

However, having too many similar commands can also lead to confusion and mistakes, especially for new users who may not understand their subtle differences. This can result in the accidental deletion of files or other unintended consequences.

So just make sure you understand the Git commands and their differences carefully so you can deliberately use them. It's also helpful to consult the documentation or seek assistance from more experienced users if you are unsure how to use a particular command.

Have fun coding!

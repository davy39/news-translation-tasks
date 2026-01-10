---
title: How to Remove a Directory in Linux – Delete a Folder Command
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-08T17:11:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-directory-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/delete-folders-command.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'By Dillion Megida

  If you''re using a user interface, you can right-click on a directory and select
  "Delete" or "Move to Bin". But how do you do this on the terminal? I''ll explain
  that in this article.

  How to Remove a Directory in Linux

  There are two w...'
---

By Dillion Megida

If you're using a user interface, you can right-click on a directory and select "Delete" or "Move to Bin". But how do you do this on the terminal? I'll explain that in this article.

## How to Remove a Directory in Linux

There are two ways to remove directories in Linux: the **rm** and **rmdir** commands.

The TL;DR of both commands is that **rm** deletes directories that may contain content such as files and subdirectories, while **rmdir** ONLY deletes empty directories. 

Also, both commands delete directories permanently (rather than moving them to the trash), so be careful when using them.

Let's look at both commands in more detail.

## How to Use the Linux `rm` command

You use the `rm` command to delete files and directories in Linux. For directories, this command can be used to delete a directory entirely – that is, it deletes a directory and all files and subdirectories within the directory.

Here's the syntax of this command:

```bash
rm [options] [files and/or directories]
```

To remove a file, say `test.txt`, you can use the command without options like this:

```bash
rm test.txt
```

For directories, you have to provide some flag options.

### How to delete a folder with contents

For a directory with contents, you have to provide the `-r` flag. Without using this flag like this:

```bash
rm test
```

You will get this error: **rm: test: is a directory**

The `-r` flag informs the `rm` command to recursively delete the contents of a directory (whether it's files or subdirectories). So, you can delete a directory like this:

```bash
rm -r test
```

### How to delete an empty folder

For an empty folder, you can still provide the `-r` flag, but the dedicated `-d` flag applies to this case. Without this flag, you will get the same error **rm: [folder]: is a directory**.

To delete an empty directory, you can use this command:

```bash
rm -d test
```

It is recommended to use the `-d` flag for empty directory cases instead of the `-r` flag because the `-d` flag ensures that a directory is empty. 

If it is not empty, you will get the error **rm: test: Directory not empty**. So, to be sure you are performing the proper empty directory operation, use the `-d` flag.


## How to Use the Linux `rmdir` Command

The `rmdir` command is specifically used to delete empty directories. The syntax is:

```bash
rmdir [folders]
```

It is the equivalent of the `rm` command with the `-d` flag: `rm -d`.

When you use `rmdir` on a non-empty directory, you get this error: **rmdir: [folder]: Directory not empty**.

To delete an empty directory, use this command without options:

```bash
rmdir test
```

The `rmdir` command also has the `-p` flag, which allows you to delete a directory along with its parent in the tree. For example, if you have this file structure:

```bash
> Test
---> Test22
```

In this case, **Test** is a directory that has the **Test2** subdirectory. If you delete the **Test2** directory, **Test** becomes an empty directory. So instead of doing:

```bash
rmdir Test/Test2 Test
# deleting Test2 and then Test
```

You can use the `-p` flag like this:

```bash
rmdir -p Test/Test2
```

This command will delete **Test2** and afterward delete **Test**, the parent in the tree. But this command will throw an error if either directory is not empty.

## How to Delete Directories that Match a Pattern in Linux

You can also use **rm** and **rmdir** with glob patterns. [Globbing is similar to Regex](https://dillionmegida.com/p/regex-vs-glob-patterns/), but the former is used for matching file names in the terminal.

For example, if you want to delete the directories **test1**, **test2**, and **test3**, instead of running:

```bash
rm -r test1 test2 test3

# or if they are empty

rmdir test1 test2 test3
```

You can use a wildcard glob pattern like this:

```bash
rm -r test*

# or if they are empty

rmdir test*
```

The **asterisk \*** matches any mixture of characters after the "test" word. You can also apply other glob patterns. Learn more in the [globbing documentation](https://linux.die.net/man/7/glob)

## Wrap Up
Now you know how to delete directories in Linux from the command line. You learned about the `rm` and `rmdir` commands and when to use each.

Happy coding!



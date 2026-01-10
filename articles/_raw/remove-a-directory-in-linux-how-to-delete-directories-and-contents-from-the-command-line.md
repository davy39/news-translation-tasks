---
title: Remove a Directory in Linux – How to Delete Directories and Contents From the
  Command Line
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-30T21:35:33.000Z'
originalURL: https://freecodecamp.org/news/remove-a-directory-in-linux-how-to-delete-directories-and-contents-from-the-command-line
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-any-lane-5945735.jpg
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'Linux is a popular open source operating system, and its features are often
  available in your development environment. If you can learn its basic commands,
  it''ll make your life as a developer much easier.

  In this guide you will learn how to delete di...'
---

Linux is a popular open source operating system, and its features are often available in your development environment. If you can learn its basic commands, it'll make your life as a developer much easier.

In this guide you will learn how to delete directories and files from the Linux command line.

# The Linux `rm` Command

The `rm` (short for remove) command is pretty useful. Let's learn its syntax and look at a few examples to see it in action.

## `rm` Command Syntax

The syntax is shown below, with `args` being any number of arguments (folders or files).

```
rm [options] args
```

Without `options` you can use it to delete files. But to delete directories you need to use the `options` for this command.

The options are as follows:

* `-r`, "recursive" – this option allows you to delete folders and recursively remove their content first
* `-i`, "interactive" – with this option, it will ask for confirmation each time before you delete something
* `-f`, "force" – it ignores non-existent files and overrides any confirmation prompt (essentially, it's the opposite of `-i`). It will not remove files from a directory if the directory is write-protected.
* `-v`, "verbose" – it prints what the command is doing on the terminal
* `-d`, "directory" – which allows you to delete a directory. It works only if the directory is empty.

## Linux `rm` Command Example

Let's take a `project_folder` directory as an example. It has these files and folders inside:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-94.png)



Let's use this directory to show how the various options work.

You can add the option `-v` to all commands so that it will write down step by step what's going on.

So, let's start with the first option, `-r`. You just learned that this removes files and folders recursively. You can use it like this `rm -r project_folder` or also `rm -rv project_folder` as the verbose option.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-98.png)

It has deleted the `project_folder` directory and everything inside it, in the order shown.

Let's recreate the folder and try again.

What happens if you don't use the `-r` option and you try to delete the directory anyway? It will not allow it and will instead show an error:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-99.png)

To delete directories you can use the `-d` option, but if you try to use it in this case it will give an error as the folder is not empty.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-106.png)

The `-i` option make so that it asks about each action individually.

And you need to press `y` or `n` and then `Enter` after each query.

If you select `y` for all queries it will delete everything:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-107.png)

If instead you decide to not delete some files or folders, with `n` it will keep those files and continue with the rest:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-109.png)

The last option we haven't seen so far is `-f`, which will suppress errors. 

For example writing as below you would be trying to delete two non existing files – there is not a `rat.png` file, and `dog.pmg` has a typo and it gives two errors. With the `-f` option, you will not see the errors.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-108.png)

# Conclusion

The Linux command line is pretty useful if you're a developer. In this article, you have seen one of its possible commands, `rm`, that you can use to delete directories and files. 

Enjoy this new tool in your arsenal!





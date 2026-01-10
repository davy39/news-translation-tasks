---
title: The Cat Command in Linux – How to Create a Text File with Cat or Touch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-11T00:57:51.000Z'
originalURL: https://freecodecamp.org/news/the-cat-command-in-linux-how-to-create-a-text-file-with-cat-or-touch
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a5d740569d1a4ca2531.jpg
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'By Hughie Coles

  The cat command is a very popular and versatile command in the ''nix ecosystem.  There
  are 4 common usages of the cat command. It can display a file, concatenate (combine)
  multiple files, echo text, and it can be used to create a new f...'
---

By Hughie Coles

The `cat` command is a very popular and versatile command in the 'nix ecosystem.  There are 4 common usages of the `cat` command. It can display a file, concatenate (combine) multiple files, echo text, and it can be used to create a new file.

## Displaying a file

The most common use of the cat command is to output the contents of a file. The following is an example that you can try.

```sh
echo "Dance, Dance" > cat_create #create a file
cat cat_create
```

In this simple example, we're using a combination of `echo` and a redirect to create a file containing "Dance, Dance". We then use the `cat` command to display the contents.

The output is as follows:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-11.png)
_The output of the example commands_

## (Con)cat

The previous example is actually a specific case of the cat command's main function, which is to concatenate files for display.  If we use the command the same way, but give it two or more files, then it outputs the concatenation for the files.

If we run the following commands:

```sh
echo "This is how we do it" > test1 #create 1st file
echo "*This is how we do it*" > test2 #create 2nd file
cat test1 test2

```

The output is the contents of the 1st file, followed by the contents of the 2nd file. You can give cat many files and it will concatenate (combine) all of them. Notice however, that the cat command automatically inserts a line break between outputs.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-12.png)
_The output of two files concatenated_

`cat` also provides some switches to to do things such as show non-print characters (-v), or number your lines (-n). A complete breakdown can be found [in the man pages](https://man7.org/linux/man-pages/man1/cat.1.html).

## Echoing

This is a less common usage of `cat` , but is the basis for the next section. If you run the `cat` command with no commands, `cat` will run in interactive mode and echo anything you type until you exit the command.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-13.png)
_Running cat in interactive mode_

In the example here, I've typed a single word per line. Each time I hit enter, the line was echoed.

You can also pipe text to `cat`, in which case that text is echoed. For example:

```sh
echo "Piping fun" | cat

```

This will result in the following output:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-14.png)
_Piping text into cat_

## Creating a File

In the previous examples, we've been using the `echo` command redirected to a file to create new files. Cat can be used in a similar way. In fact, we can use `cat`'s concat and echo functionality to create files.

We can create a file containing the concatenation of multiple files like this:

```sh
echo "File 1 Contents" > file1
echo "File 2 Contents" > file2
echo "File 3 Contents" > file3
cat file1 file2 file3 > combined_file
cat combined_file
```

In the above example, we're creating 3 files using `echo`, combining the 3 files into one using `cat`, and then displaying the new combined file using `cat`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-15.png)
_The result of the above commands. We've created 3 files, then combined them into a single file using cat_

We can also use `cat`'s interactive mode to create a file with the text that we type into the terminal.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-16.png)

Each time you hit enter, it commits the text to the file. If you have uncommitted text and exit, it won't be captured in the file.

This is a fantastic way to create a file quickly with the ability to enter the content of the file.

## Using Touch to create a file instead

Sometimes you just need a file to exist. As an alternative to using `cat` to create a file, you can use the `touch` command.

The `touch` command was designed to update the modified timestamp of a file, but is commonly used as a quick way to create an empty file. Here is an example of that usage:

```sh
touch new_file_name
```

The touch command can create multiple files, update the modification and/or creation timestamps, and a bunch of other useful things. [The full man pages can be found here.](https://www.man7.org/linux/man-pages/man1/touch.1.html)

Touch is commonly used to ensure that a file exists, and is a great command if you need an empty file quickly.

## Summary

Cat is a very useful command.  You can use it to create, display, and combine text files very quickly and easily.  

If you only need a file to exist, but don't mind (or require) it being empty, using `touch` is a great alternative.

Hughie Coles is a lead developer at Index Exchange. He writes about software architecture, scaling, leadership, and culture.  For more of his writing, check out his blog on medium.



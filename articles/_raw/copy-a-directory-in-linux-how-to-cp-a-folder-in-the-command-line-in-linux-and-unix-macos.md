---
title: Copy a Directory in Linux – How to cp a Folder in the Command Line in Linux
  and Unix (MacOS)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-04T15:33:12.000Z'
originalURL: https://freecodecamp.org/news/copy-a-directory-in-linux-how-to-cp-a-folder-in-the-command-line-in-linux-and-unix-macos
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/copy-directory-linux-article.jpg
tags:
- name: Linux
  slug: linux
- name: macOS
  slug: macos
- name: unix
  slug: unix
seo_title: null
seo_desc: 'By John Mosesman

  To copy files or directories in Unix-based operating systems (Linux and MacOS),
  you use the cp command.

  The cp command is a relatively simple command, but its behavior changes slightly
  depending on the inputs (files vs directories) a...'
---

By John Mosesman

To copy files or directories in Unix-based operating systems (Linux and MacOS), you use the `cp` command.

The `cp` command is a relatively simple command, but its behavior changes slightly depending on the inputs (files vs directories) and the options you pass to it.

To view the documentation or manual for the `cp` command, run `man cp` at your terminal:

```
$ man cp

NAME
     cp -- copy files

SYNOPSIS
     cp [OPTIONS] source_file target_file
     cp [OPTIONS] source_file ... target_directory

...

```

The basic form of this command takes an input source (or sources) that you want to copy (files or directories) and a destination to copy the files or directories to:

```
cp [OPTIONS] source_file target_file
```

## How to copy a file to the current directory

To copy a file, pass the file you want to copy and the path of where you want to copy the file to.

If you have a file named `a.txt`, and you want a copy of that file named `b.txt`:

```
$ ls
a.txt

$ cp a.txt b.txt

$ ls
a.txt   b.txt
```

> If you're not familiar with the `ls` command, `ls` "lists" all the contents of a directory.

By default the `cp` command uses _your_ _current directory_ as the path.

### How to copy a file to another directory

To copy a file to a directory that is _different_ from your current directory, you just need to pass the path of the other directory as the destination:

```
$ ls ../directory-1/

$ cp a.txt ../directory-1/

$ ls ../directory-1/
a.txt

```

After the `cp`  command, the previously empty `directory-1` now contains the file `a.txt`.

By default the copied file receives the name of the original file, but you can also optionally pass a file name as well:

```
$ cp a.txt ../directory-1/b.txt

$ ls ../directory-1/
b.txt
```

## How to copy multiple files to a directory

To copy more than one file at a time you can pass multiple input sources and a directory as destination:

```
$ ls ../directory-1/

$ cp first.txt second.txt ../directory-1/

$ ls ../directory-1/
first.txt       second.txt

```

Here the two input sources (`first.txt` and `second.txt`) were both copied to the directory `directory-1`.

> **Note:** when passing multiple sources the last argument must be a directory.

## How to copy a directory to another directory

If you try to pass a directory as the input source, you get this error:

```
$ cp directory-1 directory-2
cp: directory-1 is a directory (not copied).
```

To copy a directory, you need to add the `-r` (or `-R`) flag—which is shorthand for `--recursive`:

```
$ ls directory-1
a.txt

$ cp -r directory-1 directory-2

$ ls
directory-1          directory-2

$ ls directory-2
a.txt
```

Here `directory-1` containing the file `a.txt` is copied to a new directory called `directory-2`—which now also contains the file `a.txt`.

### How to copy the entire directory vs the contents of the directory

There is an interesting edge case when you copy a directory: if the destination directory already exists, you can choose whether to copy **the contents of the directory** or the **entire directory** by adding or removing a trailing `/` from your input.

Here's the description from the `-R` option of the `man` page:

> If source_file designates a directory, cp copies the directory and the entire subtree connected at that point. If the source_file ends in a /, the contents of the directory are copied rather than the directory itself.

If you want to copy _just the contents_ of the directory into another directory, add a trailing `/` to your input.

If you want to copy the contents of the directory _and the directory folder itself_ into another directory, don't add a trailing `/`:

```
$ ls
directory-1          directory-2

$ ls directory-2

$ cp -r directory-1 directory-2

$ ls directory-2
directory-1

$ ls directory-2/directory-1
a.txt
```

Here you can see that because `directory-2` already exists—and the input source didn't have a trailing `/`—both the contents of `directory-1` _and_ the directory itself was copied into the destination.

## How to prevent overwriting files with `cp`

By default, the `cp` command will overwrite existing files:

```
$ cat a.txt
A

$ cat directory-1/a.txt
B

$ cp a.txt directory-1/a.txt

$ cat directory-1/a.txt
A
```

> If you're not familiar with the `cat` or "concatenate" command, it prints the contents of a file.

There are two ways to prevent this.

### The interactive flag

To be prompted when an overwrite is about to occur, you can add the `-i` or `--interactive` flag:

```
$ cp -i a.txt directory-1/a.txt
overwrite directory-1/a.txt? (y/n [n])
```

### The no-clobber flag

Or, to prevent overwrites without being prompted, you can add the `-n` or `--no-clobber` flag:

```
$ cat a.txt
A

$ cat directory-1/a.txt
B

$ cp -n a.txt directory-1/a.txt

$ cat directory-1/a.txt
B
```

Here you can see that thanks to the `-n` flag the contents of `directory-1/a.txt` were not overwritten.

## Other options

There are many other useful options to pass to the `cp` command: like `-v` for "verbose" output or `-f` for "force." 

I highly encourage you to read through the `man` page for all of the other useful options.

If you liked this tutorial, I also talk about topics like this [on Twitter](https://twitter.com/johnmosesman), and write about them on [my site](https://johnmosesman.com/).


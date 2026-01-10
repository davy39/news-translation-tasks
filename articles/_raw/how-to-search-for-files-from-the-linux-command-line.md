---
title: How to Search for Files from the Linux Command Line
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-03-17T19:55:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-search-for-files-from-the-linux-command-line
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Copy-of-remove-key-val.gif
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'Searching for files is relatively easy when you are using a GUI. But in
  certain environments like GUI-less servers, you need to search for files using the
  command line.

  There is a powerful command in Linux that helps you search for files and folders
  ...'
---

Searching for files is relatively easy when you are using a GUI. But in certain environments like GUI-less servers, you need to search for files using the command line.

There is a powerful command in Linux that helps you search for files and folders called `find`. In this article, we will discuss the `find` command with some examples.

## What is the find command in Linux?

The `find` command lets you efficiently search for files, folders, and character and block devices. 

Below is the basic syntax of the `find` command:

```bash
find /path/ -type f -name file-to-search

```

Where,

* `/path` is the path where file is expected to be found. This is the starting point to search files. The path can also be`/`or `.` which represent root and current directory, respectively.
* `-type` represents the file descriptors. They can be any of the below:

	`f` – **Regular file** such as text files, images and hidden files.

	`d` – **Directory**. These are the folders under consideration.

	`l` – **Symbolic link**. Symbolic links point to files and are similar to shortcuts.

	`c` – **Character devices**. Files that are used to access character devices are called character device files. Drivers communicate with character devices by sending and receiving single characters (bytes, octets).  Examples include     keyboards, sound cards and mouse.

	`b` – **Block devices**. Files that are used to access block devices are called block device files. Drivers communicate with block devices by sending and receiving entire blocks of data. Examples include USB, CD-ROM

* `-name` is the name of the file type that you want to search.

## Examples of the find command

Now we know the syntax of the `find` command, let's look at some examples.

### How to search files by name or extension

Suppose we need to find files that contain "style" in their name. We'll use this command:

```bash
find . -type f -name "style*"
```

**Output**

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-2.png)

Now let's say we want to find files with a particular extension like `.html`. We'll modify the command like this:

```bash
find . -type f -name "*.html"
```

**Output**

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-3.png)

### How to search hidden files

Hidden files are represented by a dot in the beginning of the filename. They are normally hidden, but can be viewed with `ls -a` in the current directory.

We can modify the `find` command as shown below to search for hidden files.

```bash
find . -type f -name ".*"
```

**Output**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-61.png)
_List of hidden files in my home directory_

### How to search log files and configuration files

Log files usually have the extension `.log`, and we can find them like this:

```bash
 find . -type f -name "*.log"
```

**Output**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-62.png)

Similarly, we can search for configuration files like this:

```bash
 find . -type f -name "*.conf"
```

### How to search other files by type

We can search for character block files by providing `c` to `-type`:

```bash
find / -type c
```

Similarly, device block files can be found by using `b`:

```bash
find / -type b
```

### How to search directories

In the example below, we are finding the folders named `lib`. Note that we are using `-type d`.

```bash
find . -type d -name "lib*"
```

**Output**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-63.png)

💡 Tip: we can identify directories by looking at the `d` flag in the output of `ls -lrt`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-64.png)

### How to search files by size

An incredibly helpful use of the `find` command is to list files based on a particular size.

```bash
find / -size +250M
```

Other units include:

* `G`: GigaBytes.
* `M`: MegaBytes. 
* `K`: KiloBytes 
* `c` : bytes.

Just replace <Unit Type> with the relevant unit.

```bash
find <directory> -type f -size +N<Unit Type>

```

### How to search files by modification time

```bash
find /path -name "*.txt" -mtime -10 


```

* **-mtime +10** means you are looking for a file modified 10 days ago.
* **-mtime -10** means less than 10 days.
* **-mtime 10** If you skip + or – it means exactly 10 days.

Below are the contents of my home directory:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-65.png)

Let's apply an example in my home directory.

```bash
find . -type f -name ".*" -mtime +10
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-66.png)
_Here we have files that were modified more than 10 days ago._

## Practical examples of `find` with bash scripts

We can combine `find` with `rm` or `mv` to create meaningful bash scripts that can be automated.

Let's say we want to create a script that moves log files older than 7 days to a backup path. From there, it deletes log files older that older than 30 days. We can create a script and schedule it with `cron`. You can learn more about `cron` jobs [here](https://www.freecodecamp.org/news/cron-jobs-in-linux/).

Let's view the script:

```bash
#!/bin/bash
# Script to move from logs older than 7 days to backup logs path: /app/backup_logs/ESB0*

# move ESB01 logs to backup
find /logs/esb01/audit  -name "*.tar.gz" -mtime +7 -exec mv {} app/backup_logs/ESB01/ \;

# Remove logs from backup path after 30 days
find /app/backup_logs/ESB01 -name "*.tar.gz" -mtime +30  -exec rm {} \;

```

Note that we are using `exec` with `find`. Basically, `exec` executes the command provided ( `mv` and `rm` in our case). `{}` is the placeholder which holds the results of the command. Lastly, we provide the delimiter `;`. As we do not want the shell to interpret the semicolon, we escape it with `\`.

The shared script is very useful in archiving and removing logs.

## Wrapping up

In this article, we have studied the `find` command in detail and learned how to search files by name, type, size and modification time.

I hope you found this tutorial helpful.

Share your thoughts on  [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

Resources: Banner images from [Office illustrations by Storyset](https://storyset.com/office) and Canva.


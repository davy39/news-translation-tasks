---
title: Rename a File in Linux – Bash Terminal Command
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-09-30T15:06:08.000Z'
originalURL: https://freecodecamp.org/news/rename-file-linux-bash-command
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Copy-of-read-write-files-python--3-.png
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Renaming files is a very common operation whether you are using the command\
  \ line or the GUI. \nCompared to the GUI (or Graphical User Interface), the CLI\
  \ is especially powerful. This is in part because you can rename files in bulk or\
  \ even schedule the..."
---

Renaming files is a very common operation whether you are using the command line or the GUI. 

Compared to the GUI (or Graphical User Interface), the CLI is especially powerful. This is in part because you can rename files in bulk or even schedule the scripts to rename files at a certain point in time.

In this tutorial, you will see how you can rename files in the Linux command line using the built-in `mv` command.

## How to Use the Linux `mv` Command

You can use the built-in Linux command `mv` to rename files. 

The `mv` command follows this syntax:

```bash
mv [options] source_file destination_file
```

Here are some of the options that can come in handy with the `mv` command:

* `-v` , `--verbose`: Explains what is being done.
* `-i`, `--interactive`: Prompts before renaming the file.

Let's say you want to rename `index.html` to `web_page.html`. You use the `mv` command as follows:

```bash
zaira@Zaira:~/rename-files$ mv index.html web_page.html

```

Let's list the files and see if the file has been renamed:

```bash
zaira@Zaira:~/rename-files$ ls
web_page.html
```

## How to Name Files in Bulk Using `mv`

Let's discuss a script where you can rename files in a bulk using a loop and the `mv` command.

Here we have a list of files with the extension `.js`. 

```bash
zaira@Zaira:~/rename-files$ ls -lrt
total 0
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 index.js
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 config.js
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 blog.js
```

Next, you want to convert them to `.html`.

You can use the command below to rename all the files in the folder:

```bash
for f in *.js; do mv -- "$f" "${f%.js}.html"; done
```

Let's break down this long string to see what's happening under the hood:

* The first part [`for f in *.js`] tells the `for` loop to process each “.js” file in the directory.
* The next part [`do mv -- "$f" "${f%.js}.html`] specifies what the processing will do. It is using `mv` to rename each file. The new file is going to be named with the original file’s name excluding the `.js` part. A new extension of `.html` will be appended instead.
* The last part [`done`] simply ends the loop once all the files have been processed.

```bash
zaira@Zaira:~/rename-files$ ls -lrt
total 0
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 index.html
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 config.html
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 blog.html
```

## Conclusion

As you can see, renaming files is quite easy using the CLI. It can be really powerful when deployed in a script.

What’s your favorite thing you learned here? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

[Image by storyset](https://www.freepik.com/free-vector/college-project-concept-illustration_29659818.htm) on Freepik


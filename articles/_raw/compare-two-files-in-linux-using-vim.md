---
title: Linux `Vimdiff` Command – How to Compare Two Files in the Command Line
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-08-08T20:08:39.000Z'
originalURL: https://freecodecamp.org/news/compare-two-files-in-linux-using-vim
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Copy-of-Cast-a-Function-in-SQL---Convert-Char-to-Int-SQL-Server-Example--3-.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: vim
  slug: vim
seo_title: null
seo_desc: "Software development and maintenance can get complicated sometimes. And\
  \ you might find yourself comparing code or configuration changes. \nWhen you compare\
  \ them manually, you might make a mistake, and it's easy to miss minute changes.\
  \ Apart from that,..."
---

Software development and maintenance can get complicated sometimes. And you might find yourself comparing code or configuration changes. 

When you compare them manually, you might make a mistake, and it's easy to miss minute changes. Apart from that, finding changes in large files can be exhausting. 

There are many online tools and text editors that help you efficiently compare files. But there is an easier, hassle-free method to compare files using the Linux command line. 

The Linux command line is very powerful and provides a file comparison utility within `vim` to differentiate files side by side.

Learning file comparison in the command line is helpful because many servers use only a CLI (Command Line Interface). This means that you don't have the luxury of a GUI where you can run the browser or other text editors.

## What is vimdiff?

`Vimdiff` is a Linux command that can edit two, three, or four versions of a file with `Vim` and show their differences.

### `Vimdiff` syntax

For comparing two files, the syntax is the following:

```bash
 vimdiff [options] file1 file2
```

Let's compare two files `index.js` and `index.js.bkp` to see their differences.

```bash
vimdiff index.js index.js.bkp 
```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-13.png)
_`Vimdiff` output_

Here we can see the difference in the highlighted line. 

To make things easier, we can show the line number as well. When you are in `Vim`, go to the extended command mode by pressing escape twice and typing `:set number`. This will reveal the line numbers for the current session.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-14.png)
_Line numbers in `vim`_

Let's have a closer look at the output again:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-16.png)
_Detailed output of `vimdiff`._

* **Uncollapsed lines:** These are the lines of codes that have not been changed. these are wrapped and can be uncollapsed using a combination of the `z+c` and `z+o` keys.
* **Highlighted changes:** These are the differences present in a file.
* **Line numbers:** These are the corresponding line numbers in files.
* **File names:** The file name on the left is the first filename mentioned in the command. The file name on the right is the second filename provided in the command.

There is also a way to enable line numbers in Vim by default so you don't have to set it manually each time.

### How to show line numbers by default in Vim on Linux

If you like to view line numbers by default in `Vim`, you can follow these steps:

1. Locate the `vimrc` file.

`Vim` configurations are present in the `vimrc` file. The file location might vary from one Linux distribution to the other. In Ubuntu, the `vimrc` file is located in `/usr/share/vim/`.

2.  Edit the `vimrc` file.

Simply append `set number` in the file and save and exit.

Now whenever you open `Vim`, the line numbers will be there by default. 

## `Vimdiff` Operations

Let's see how we can utilize the powers of `vimdiff`. 

First, make sure you are in the command mode.

You can go into the command mode by pressing the `escape` key twice.

### How to split screens horizontally

By default, `vimdiff` splits the screen vertically. If you like to see the files split horizontally, you can use the flag `-o` like this:

```bash
vimdiff -o index.js index.js.bkp
```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-17.png)
_Horizontal split_

### How to navigate in diff window

* Navigate between diff windows

To navigate between panes, use a key combination of `Ctrl+W+W`. The cursor will switch between the files once you press the keys.

* Jump to changes

Instead of scrolling down line by line and scanning for the changes, you can jump to the change with a specific key combination. 

1. To move to the previous change use: `[ + c`.
2. To move to the previous change use: `] + c`

### How to apply changes from diff window

* To apply changes from the left file to the right file:

To apply the changes from the left file to the right file, first, move to the highlighted change. Then, use the command:

`:diffput`

Remember that you'll need to be in the command mode.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-18.png)
_Using `diffput` to apply changes from left to right._

* To apply changes from the right file to the left file:

To apply the changes from the right file to the left file, first, move to the highlighted change. Then, use the command:

`:diffget`

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-19.png)
_Using `diffget` to apply changes from right to left._

### How to undo changes

If you make a mistake, you can undo the changes provided you didn't save the file.

When you are in the command mode press `u` to undo the last change.

If you've recently undone a change, you won't be able to see the highlighted changes as before. You'll need to refresh to see the changes once again. You can do this by using the command:

`:diffupdate`

### How to open and close folds

The unchanged lines are wrapped to provide better readability. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-33.png)

To view the uncollapsed lines as shown above, move the cursor there and use the following key combinations:

* To open the folds: `z + o`.
* To close the folds: `z + c`.

### How to exit the diff window

There are many ways to exit the diff window depending on the end result.

* `:qa` to exit all the files without saving.
* `:q` to exit the files one by one without saving.
* `:wq!` to save and exit files one by one.

## Conclusion

Comparing files is easy and fast with `vimdiff` as we compare files within the command line. In this tutorial, you learned how to use the `vimdiff` command to efficiently find differences in code or configuration files. 

I hope you found this tutorial helpful. Thank you for reading till the end.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can also read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

<sub>Image credits:
Programming vector created by storyset - www.freepik.com</sub>



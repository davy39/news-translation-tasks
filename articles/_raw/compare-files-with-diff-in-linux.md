---
title: Linux diff – How to Compare Two Files and Apply Changes with the Patch Command
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2021-09-15T21:01:00.000Z'
originalURL: https://freecodecamp.org/news/compare-files-with-diff-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Compare-files-in-Linux-with-diff.png
tags:
- name: Linux
  slug: linux
- name: version control
  slug: version-control
seo_title: null
seo_desc: "Imagine waking up one day to find out that your production systems are\
  \ down because of a bug that has yet to be traced. One of your worst nightmares\
  \ right? \nAnd you also discover that you need to compare code from two versions\
  \ and the pressure is bui..."
---

Imagine waking up one day to find out that your production systems are down because of a bug that has yet to be traced. One of your worst nightmares right? 

And you also discover that you need to compare code from two versions and the pressure is building to restore the systems. Everyone is panicking and it's totally legit!

Luckily, there is a Linux utility called `diff` that has got your back. 

## What is the `diff` command in Linux?

Comparing files and finding the differences between them is a widely used operation. This is specially useful when you have to compare complex code or configuration files. 

Instead of comparing manually (which has a high chance of human error), Linux gives you a built in and powerful utility called `diff`. It also saves time.

To compliment diff commands, Linux also provides another command to apply changes from one file to another called `patch` . In this article, we'll be looking into these interesting and versatile commands to see how to use them.

## `diff` command syntax

The syntax for `diff` is shared below:

```bash
diff [options] file1 file2
```

The diff command can show three characters based on the changes:

<table>
<thead>
<tr>
<th>Character</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>c</td>
<td>CHANGE- A change needs to be done.</td>
</tr>
<tr>
<td>d</td>
<td>DELETE- Something should be deleted.</td>
</tr>
<tr>
<td>a</td>
<td>ADD- Something needs to be added.</td>
</tr>
</tbody>
</table>

In the output of the `diff` command, the symbol `<` points to the first file and the symbol `>`  points to the second file which is used as a reference.

Let's see some examples of the `diff` command in use.

### Examples of the Linux `diff` command

To state that files are the same, we use the flag `-s` with `diff`. In our example, the two files fileA and sameAsfileA contain the same content.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-63.png)

In the next example, there are two files that don't have the same contents. In the output highlighted below, the `diff` command shows that lines 11 and 14 in showList_v2.js should change to match lines 11 and 13 in showList_v1.js.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-64.png)

The next way you can use diff is my favorite, as you can see differences side by side.

Just use the `-y`  flag like this:

```bash
diff -y file1 file2
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-50.png)
_Compare files side by side_

The last example I am going to discuss is unified output. This output is often used as input to the `patch` command. We'll see how the patch command works as well:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-67.png)
_Unified output, used as an input to patch._

Below are some other useful flags you can use with `diff`.

* `-i` to ignore case. `diff` is case sensitive by default.
* `-w` to ignore whitespaces in a file. By default whitespaces are considered a difference.

## `patch` Command Syntax 

Changes happen all the time in your code, and it is unrealistic and time-consuming to share edited and fixed files for each change. Usually devs share fixes in the code with the team so they are applied instantly. 

And using patches is the safest method to distribute improvements only. 

Let's see how patching works:

```bash
patch file_to_change < patch_file
```

### Examples of the Linux `patch` command

Here's an example for patching: suppose we have a simple JavaScript code [file name: print_in_js.js] that prints a string. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-68.png)

However, there is something wrong in the print function and we need a fixture for that. We send the file print_in_js.js to our colleague who fixes the code and sends it back.

First, our colleague is able to find a type in line #3. They correct the file.

Once file is corrected, and the code is functional, they create a patch.

```bash
diff -u print_in_js.js  print_in_js_Fixed.js > patched_print_js.diff
```

Let's review the contents of the patch:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-69.png)
_contents of patch_

Once we have the patch, we apply it as follows:

```bash
patch print_in_js.js  < patched_print_js.diff
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-72.png)
_Code fixed after patch application_

And yes – our code is fixed!

## Wrapping Up

It is relatively simple and straightforward to create and apply patches using `patch` and `diff`. 

A similar approach works when you're using version control systems like Git or SVN. Learning the basics really helps you transition to and understand how version control works, which is an important aspect of software development.

Thanks for reading until the end. I would love to connect with you. You can find me [here](https://twitter.com/hira_zaira) on twitter. Do share your thoughts.

See you around.


---
title: The Cat Command in Linux – Concatenation Explained with Bash Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-04T23:43:06.000Z'
originalURL: https://freecodecamp.org/news/the-cat-command-in-linux-concatenation-explained-with-bash-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b40740569d1a4ca2aaf.jpg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'By Ryan reid

  Cat in Linux stands for concatenation (to merge things together) and is one of the
  most useful and versatile Linux commands. While not exactly as cute and cuddly as
  a real cat, the Linux cat command can be used to support a number of ope...'
---

By Ryan reid

Cat in Linux stands for concatenation (to merge things together) and is one of the most useful and versatile Linux commands. While not exactly as cute and cuddly as a real cat, the Linux `cat` command can be used to support a number of operations utilizing strings, files, and output.

The cat command has three primary purposes involving text files:

* Create
* Read/Display
* Update/Modify

We'll go over each of these in turn to show the commands and options associated with each operation.

## Getting Started

To start out, let's create a couple of files called foo.txt and spam.txt.

Let's start by creating foo.txt with the command `cat > foo.txt` from the Linux command line. 

**Warning: If there is already a file named foo.txt, the `cat` command using the > operator WILL overwrite it.**

From here the prompt will display a newline that will allow us to input the text we want. For this example we'll use:

```
FILE 1
foo
bar
baz

```

To get back to the command line and create the text file we use CTRL + D.

Now let's create spam.txt with `cat > spam.txt` and put in the following:

```
FILE 2
spam
ham
eggs

```

If we wanted to append or add more text to these files we would use `cat >> FILENAME` and input the text we want to use.

**Note that the >> operator is used for appending as opposed to the > operator.**

Instead of having to open a text editor, we were able to create a quick and simple text file from the command line, saving us time and effort.

The key takeaway from this section is that we use `cat > FILENAME` to create or overwrite a file. Additionally, we can use `cat >> FILENAME` to append to a file that's already there. Then after typing in the text we want we use CTRL + D to exit the editor, return to the command line, and create the file.

## Reading Rainbow

Now that we've created something let's take a look at what we've made.

Notice how we don't have a > or a >> operator in the following command, only cat and the filename.

The command `cat foo.txt` will display the following:

```
FILE 1
foo
bar
baz

```

So `cat foo.txt` will let us read the file, but let's see what else we can do.

Say we wanted to figure out how many lines a file we were working on was. For this the -n option comes in handy.

With the command `cat -n foo.txt` we can see how long our file is:

```
  1  FILE 1
  2  foo
  3  bar
  4  baz

```

With -n we can get an idea of how many lines the file we're working with has. This can come in handy when we're iterating over a file of a fixed length.

## ConCATenating files

Ok, so we've seen that cat can create and display files, but what about concatenating (combining) them?

For this example we'll use files foo.txt and spam.txt. If we want to get fancy we can take a look at the contents of both files at the same time. We'll use the cat command again, this time using `cat foo.txt spam.txt` .

`cat foo.txt spam.txt` results in the following:

```
FILE 1
foo
bar
baz
FILE 2
spam
ham
eggs


```

Note that the above only DISPLAYS the two files. At this point we haven't concatenated them into a new file yet.

To concatenate the files into a new file we want to use `cat foo.txt spam.txt > fooSpam.txt` which gives us the result into a new file fooSpam.txt.

Using `cat fooSpam.txt` outputs the following to the terminal:

```
FILE 1
foo
bar
baz
FILE 2
spam
ham
eggs

```

This command is also useful for when we want to concatenate more than two files into a new file.

The takeaways here are we can view multiple files with `cat FILENAME1 FILENAME 2`.

Furthermore we can concatenate multiple files into one file with the command  `cat FILENAME1 FILENAME 2 > FILENAME3`.

## Other Fun Things to do With Cat(s)

Let's say we're working with a file and we keep getting errors for some reason before the end of the file – and it looks like it might have more lines than we expected it to.

To investigate the file a bit further and possibly solve our problem we can use the -A switch. The -A option will show us where lines end with a $, it will show us tab characters with a ^I, and it also displays other non-printing characters.

If we were looking at an example of a non-printable text file with `cat nonPrintExample.txt` we might get out something like this:

```




       






```

Which is OK but may not tell us a full story of a character or string that might be causing us issues.

Whereas `cat -A nonPrintExample.txt` might give us more useful output:

```
^I^I$
$
^L$
$
^G^H^H^H^Y^I^N^O^P^@$
^@^@^[g^[f^[d^[g^[6^[5^[4^[6^[=$
$
$
^X$

```

Here, we get a clearer representation of what might be going on between tabs, line feeds, returns, and other characters.

The takeaway here is that cat -A FILENAME can tell us more in-depth details about the file that we're working with.

This article should give you a good overview of the cat command, what it can do, and its functionality.


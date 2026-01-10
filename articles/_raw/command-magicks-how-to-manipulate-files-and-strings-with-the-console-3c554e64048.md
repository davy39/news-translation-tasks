---
title: 'Command Magicks: How to Manipulate Files and Strings with the Console'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T19:33:08.000Z'
originalURL: https://freecodecamp.org/news/command-magicks-how-to-manipulate-files-and-strings-with-the-console-3c554e64048
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8SjtkPp6PLAWGnOXY-xxhg.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Luciano Strika

  As developers, there are lots of repetitive things we do every day that take away
  our precious time. Finding ways to automate and optimize those processes is usually
  very lucrative.

  Many times we find ourselves sifting through a pro...'
---

By Luciano Strika

As developers, there are lots of repetitive things we do every day that take away our precious time. Finding ways to automate and optimize those processes is usually very lucrative.

Many times we find ourselves sifting through a program’s output looking for the relevant bits and manually moving them into a different file, changing all the capital letters from a sentence into lowercase, or removing all non-numerical characters from a file. The kind of boring, repetitive and error-prone tasks that can pile up if we do them by hand, and turn into a big headache.

It’s conventional wisdom that we should do these things programmatically not manually. Many times the problem falls into this sweet spot where coding a whole script for it, even in Python, feels like overkill. Doing the thing by hand will take too long or generate too many errors.

Luckily, many of those tasks have already been coded by people way smarter than we are. They can be accessed with just a few key presses. They are all available as shell commands, and I’ll show you some of them today. If you’re completely new to the terminal and have no idea how to navigate your file system or do similar tasks, I suggest you read [my previous introduction to the terminal](https://medium.freecodecamp.org/how-you-can-be-more-productive-right-now-using-bash-29a976fb1ab4).

So without further ado, let me introduce you to the most useful spells any coding wizard should know.

#### echo: Make a string appear in the console

Before we can dive into the arts of divination and transformation, a real programming wizard must dominate the craft of conjuration.  
The echo command, followed by a string, will simply make the console output what was given as input. For instance, running the following line:

```
echo “hello world!”
```

will produce the following output:

```
hello world!
```

This may seem trivial right now, but I promise it will be useful in the future.

#### cat: Showing the input’s true form

Calling the cat command on a file will output its contents into the terminal.  
For instance, we have a directory containing the files ‘file1.txt’ and ‘file2.txt’. Both files contain the text ‘this is a file’. Calling:

```
cat file1.txt
```

will output the file’s contents:

```
this is a file
```

Note that the argument for the cat command can be any shell style name. We can use the wildcard character *, to match any string. This way, we could output different files’ contents one after another, like this:

```
cat *.txt
```

In this case, * matches both file1 and file2, and they both end in .txt, so they’re both printed. That command’s output would be

```
this is a filethis is a file
```

Remember this command — no warlock is really complete without a kitten.

#### grep: finding a needle in a haystack

Switching to divination, grep is the spell for finding a substring in a string.   
Calling

```
grep <some string> filename
```

will output every line of the specified file where the given string appears.

If we wish for it to appear not only in its exact form but also with different casing, we must pass the **-i** argument, to ignore casing.

If we call it on different files in a single command, we will get a list of every file with lines matching the pattern. For instance in the previous directory, calling

```
grep “this” *.txt
```

will yield

```
file1.txt: this is a filetile2.txt: this is a file
```

#### sed: transforming a string into another

The sed command is a transmutation spell. It takes a file’s contents and turns them into different ones. There are many ways of using it. Some of which I confess to knowing little of. (If you’re reading this and think of some cool things sed does that I am not mentioning, please tell me in the comments, as I love to learn new tricks). One of the most common ones is replacing the parts of a string that match a pattern, with different strings.

This is done by calling

```
sed “s/regexp/replacement/optional_flags” file_name
```

What this will do is:

* Look for every line that matches the regexp in the file_name file
* Replace that line’s first _regexp_ instance with _replacement_
* Output the resulting string into the console (without altering the file!).

If we supply the g flag at the end (like this s/old/new/g) it will match all instances on each line, instead of just the first one. Using the **-i** argument (for in-place) will actually write into the input file.

As an example, calling

```
sed “s/is/was/g” file1.txt
```

will output

```
thwas was a file
```

If we want only to match entire words, we must put the \b character surrounding the regexp, like this

```
sed “s/\bis\b/was/g” file1.txt
```

to finally get

```
this was a file
```

## Combining our spells: The Operators

Now you’re proficient in four new schools of magic, each one with its characteristic spell. But to become a real wizard, you must learn to tie the threads of magic into awesome patterns. To do this, you will use three powerful tools.

#### | (Pipe) Operator

The pipe operator takes the previous command’s output, and writes it into the following command’s input, creating a pipeline.  
For instance, calling

```
cat *.txt | grep “is”
```

will first fetch the contents for all text files in the current working directory. Then look for every line that contains the string “is”, before finally printing them.

#### > (write) Operator

The write operator will write its input into its output — usually a file.

So for instance, a quick way of creating a text file with ‘this is a file’ as its contents, would be calling

```
echo “this is a file” > some_file.txt
```

See how that whole conjuring spell thing actually adds up? I told you it would be useful.

Note that if the file already existed, this will overwrite its contents, without even asking. In case that’s not what we wanted, we must use our last tool:

#### >> (append) Operator

The >> operator will write its input into its output, except it won’t overwrite whatever’s already in it.

That’s it, we’re through with this tutorial and you’re now a wizard’s apprentice. Go practice your new spellcasting skills, and you can thank me later. Do remember to check the man pages for all these commands if you get stuck or don’t remember what some flags did — a wizard’s never away from his books.

_Please consider [supporting my writing habit](https://www.buymeacoffee.com/strikingloo) with a small donation._

_Follow me on Medium for more tutorials, tips and tricks. This article was also posted on [datastuff.tech](http://www.datastuff.tech/programming/files-strings-shell-tutorial/), my new website. Check it out!_


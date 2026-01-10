---
title: How to start using the terminal to be more productive
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-07T23:35:35.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-be-more-productive-right-now-using-bash-29a976fb1ab4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*T5VYxE-aik-V7hXOaU9Wuw.jpeg
tags:
- name: '#LifeHacks'
  slug: lifehacks
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Luciano Strika

  As developers, the terminal can be our second home.

  However, we can’t use it until we learn how to, and need to practice using it to
  learn, really — it’s a catch-22!

  I hope this introduction will solve that puzzle for you. I want to...'
---

By Luciano Strika

As developers, the terminal can be our second home.

However, we can’t use it until we learn how to, and need to practice using it to learn, really — it’s a catch-22!

I hope this introduction will solve that puzzle for you. I want to help you start making use of the terminal right away.

### Getting Started

I’ll cover the basics first, so if you know all the things in this article stay tuned for the next ones, where I’ll tackle more advanced topics.

With that taken care of, I’ll start from the very beginning. If you’re on Ubuntu, all you have to do to open your terminal is press _ctrl+alt+._ On a Mac, you should press _cmd+spacebar,_ start typing _terminal_ and press enter when the option appears.

In both cases, you should see a dark background with your username followed by your computer’s name (in Linux) or the reverse order (in a Mac).

I strongly advise you to open your own terminal and try these commands out on an empty directory, to see for yourself and get the hang of them.

You’ll see a prompt inviting you to type commands. To enter a command just type it down and press enter. Some navigation commands are:

#### cd : Moving your working directory.

```
cd <relative path>
```

This will make your terminal point to a different directory, from which you can run new commands. For instance, if you’re in a folder called _animals_ with three folders _cats_, _dogs_, and _turtles_, you’d run

```
cd turtles
```

to move into that directory. To move up one level from the current directory (e.g., moving back to _animals_ from _turtles_), hit

```
cd ..
```

#### mkdir and touch: Creating folders or files.

If you need to create a new, empty directory, all you have to do is run

```
mkdir <directory name>
```

Whereas running

```
touch <file_name>
```

will create an empty file in the current working directory, with the first argument as its name.

If another file with the given name already existed, this will only update the file’s last update date. It will not make any changes to its content.

‘But could I possibly know if the file exists?!’ You ask. Well, I’m glad you’re asking.

#### ls : See a directory’s contents.

The _ls_ command lists the name of every file and directory inside the current working directory, in alphabetical order. You can pass it a few arguments by using dashes, like this:

```
ls -a -l
```

In this case, the _-a_ argument makes _ls_ show invisible files. The _-l_ command makes the output look like a list. It displays one row for each item, with some extra data like the size of each file or its creation date.

One of my favorite arguments for _ls_ is _-R,_ which recursively calls _ls_ on each listed subdirectory for a quick look into a repository or file tree.

Note that for all commands, arguments can actually be combined after a single dash:

```
ls -alR
```

Now I hear you asking ‘How in the world am I going to remember all of these arguments and options? Do all commands have so many crazy features?’  
But don’t worry — we got you covered.

#### man : Never stop learning!

If you’ve been in Stack Overflow or Reddit, you’ve probably come across the phrase ‘read the man pages’ used either educationally or as an insult.   
I’m here for the first use.

Try running

```
man <command name>
```

It will display that command’s man page — official documentation, with all of its possible arguments and uses. Most of us use it when we’re sure a certain program did something, but we can’t quite remember which flag made it do it. It’s also very good to call man on a command the first time you use it (for instance, if it shows up in a google result), to learn a bit more about it and maybe find better ways to invoke it. To close a man page, just press _Q_.

#### head and tail, cat and less : Read a file’s contents.

Calling _head_ or _tail_ on a file will show you its first or last 10 lines, respectively.  
Some cool arguments you can call it with are:

* **-n <number**>: di_splay n_umber lines instead of the default 10
* **-f** (for _tail_) : Show the lines in real time and don’t stop (perfect for keeping tabs on a log file when you _ssh_ into a server)

Calling _cat_ will simply display a file’s content. Make sure you’re using it on actual text files, or you’ll see some trippy stuff.

If you call _cat_ on a large (or even large-_ish_, to be honest) file, you’ll probably find it pretty awkward to keep scrolling up and down, looking for the relevant lines. There’s actually a more convenient way of doing that: the _less_ command.

_less_ will show you _less_ of a file by loading its contents in a buffered way. You can scroll the file with the arrow keys instead of using the mouse wheel/touchpad, which is a lot more comfortable. You can also press /, type something in and press _Enter_ to search the file (like using _ctrl+f_).  
To exit _less_ mode, just press _Q._

#### cp and mv : Copy, cut and paste.

_cp_ (copy) and _mv_ (move) are the bash equivalents to _copy_ and _cut,_ respectively. You can use them like this:

```
cp <source> <destination>
```

To copy the file(s) in _source_ to _destination._

The source can either be a file, or a set of files. To select more than one file, you can leverage bash’s wildcard character: *****. This character will match any string, even an empty one.

For instance, this command will copy all files in the _some_folder_ folder into the _some_other_folder_ folder, situated one level upwards in the file system.

```
cp some_folder/* ../some_other_folder
```

But if we wanted to only move the .txt files into a directory called _texts,_ we’d use:

```
cp *.txt texts/
```

since * matches any string. Ee are enforcing its ending in _.txt._ (for instance, _*.txt_ matches _filename.txt,_ since _*_ matches _filename,_ but not _filename.xtt,_ since even though * matches the whole name, there’s nothing that matches _.txt)._

The destination can be a file’s path (overwriting the current file in that path, if it exists, or creating a new one otherwise) if the source is a single file, or a directory name if you wish to copy/move many files.

#### rm : Deleting files and directories.

The opposite of _touch, rm_ deletes a file or directory.

Using it in its default form

```
rm file_name
```

will work when deleting a file, but throw an error when deleting a directory. This prevents us from deleting important files in a directory, or a whole directory thinking it’s just a file.

To bypass this, if you feel courageous, just add _-r,_ to recursively delete every file in a directory until it’s empty, before deleting it like some kind of serial deleter. If you only feel like deleting the empty directories, use _-d_ instead.

Note that you can always use the wildcard (*) character to delete many files or directories in a single command. For instance, calling

```
rm *.txt
```

removes all text files from the current working directory.

#### The end… for now.

Whew, that was some introduction. You’re now familiar with the most common commands you’ll be using in your daily programming life.

There are a lot of things I didn’t cover yet. I plan to make a follow up with more use cases, more commands and more real problems to solve.

While I prepare the next article, I’d like to encourage you to try these commands on your own. See which ones save you time, and get used to this whole terminal thing. Maybe bookmark this article and use it for reference. I won’t tell anyone.

I promise you, after a while you’ll start to see why it’s worth it. (I know it took _me_ a while). Eventually you’ll just instinctively open the terminal every time you start doing something.

I hope you found some of this introduction useful, and if so please let me know! I value my readers’ feedback a lot. This is the main reason I’m writing, so please tell me if some part was hard to understand, some commands seem useless, or my tutorial is simply too boring. Also let me know if some part was interesting!

[_Part 2 is already available_](https://medium.freecodecamp.org/command-magicks-how-to-manipulate-files-and-strings-with-the-console-3c554e64048).

_Follow me for more programming tutorials, tips and tricks._   
_You can also read my articles on [www.datastuff.tech](http://www.dataden.tech/blog)_


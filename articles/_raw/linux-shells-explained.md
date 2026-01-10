---
title: Linux Shells for Beginners – Bash, Zsh, and Fish Explained
subtitle: ''
author: Anthony Behery
co_authors: []
series: null
date: '2022-12-13T21:55:05.000Z'
originalURL: https://freecodecamp.org/news/linux-shells-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-oleksandr-pidvalnyi-320260.jpg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
- name: zsh
  slug: zsh
seo_title: null
seo_desc: 'When you open up your terminal, chances are that it uses Bash as its UNIX
  shell environment. But other "shell" environments exist.

  There are other environments such as the C Shell, Korn Shell, Z Shell, and even
  the Fish Shell. All of these different ...'
---

When you open up your terminal, chances are that it uses Bash as its UNIX shell environment. But other "shell" environments exist.

There are other environments such as the C Shell, Korn Shell, Z Shell, and even the Fish Shell. All of these different shell environments have their own pros and cons, and you should consider them before you choose one to use on your own system.

In this article, I'll go over a few popular shells along with their main features to help you pick one.

## The Bash Shell

The Bash Shell (or the Bourne Again Shell) is a UNIX shell and command language. It was written by Brain Fox for the GNU Project as a free software replacement for the Bourne Shell (sh). 

Bash was first released in 1989, and for most Linux distributions it's the default Shell environment. Other distros, like Kali Linux, use the Z Shell as their default shell. 

Bash is one of the first programs that Linus Torvalds (the creator of Linux) ported to Linux. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/cli_example.png)
_[Image Source](https://www.geeksforgeeks.org/introduction-linux-shell-shell-scripting/)_

Something you should not get confused about is that Bash is also a programming language. So it's a "Shell", but you can also program behavior in Bash. For example:

``` bash
#!/bin/bash
echo "Hello World"
```

### Key points about Bash

* Most users use Bash, since it is the default shell environment on most systems
* Bash does not have an inline wildcard expression. A wildcard expression is when you would want to search for patterns in your Shell, similar to Regex. The three main wildcards are `*`, `?`, and `[]`.
* You can't automatically change the directory name
* `#` is treated as a comment in scripting 
* It has `shopt` settings
* Prompt has backslash escapes
* User configuration settings are in `.bashrc`

## The Z Shell

The Z Shell, or Zsh is also a UNIX shell that is very similar to Bash. You can also script and use the shell as a command interpreter. 

Zsh is an extension of the Bourne shell with a lot of improvements. Zsh was released in 1990 by Paul Falstad, and it has some features that Bash, Korn Shell, and C Shell share. 

macOS by default uses the Zsh Shell. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/nebirhos.jpg)
_[Image Source](https://ohmyz.sh/)_

### Key points about Zsh

* Comes with autocompletion when using the terminal. So when you press `Tab ↹` in order to autocomplete whatever command you want to run, not only does it autocomplete for you but will bring down a drop-down of all the other possible files and directories:

![Zsh Toggle](https://i.ibb.co/bswYkn0/0f8c8e1a6016.gif)

* Supports inline wildcard expressions
* Much more configurable than Bash
* Supports plugins and themes. Here's a [list of plugins](https://github.com/unixorn/awesome-zsh-plugins) available for Zsh.

There are also frameworks built around the Z Shell. One of the most popular ones is [Oh My Zsh](https://ohmyz.sh/), which is a community driven, open-source framework for managing Zsh configuration. (I use Oh My Zsh 😄) 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/oh-my-zsh-mac.jpg)
_[Image Source](https://osxdaily.com/2021/11/15/how-install-oh-my-zsh-mac/)_

Zsh and Oh My Zsh are similar but not the same exact things. To reiterate, Oh My Zsh is a way of managing your Zsh configurations, it is not the Shell itself. 

## The Fish Shell

Fish is a UNIX shell environment with an emphasis on interactivity and usability. Unlike Zsh, Fish aims to give the user interactivity by default instead of trusting the user to implement their own configuration.  

It was created by Axel Liljencrantz in 2005. Fish is considered to be an "exotic shell" due to the fact that it does not comply to the POSIX shell standards. [[Source](https://en.wikipedia.org/wiki/Fish_(Unix_shell)]

![Image](https://www.freecodecamp.org/news/content/images/2022/12/fish-shell-screenshot.png)
_[Image Source](https://blog.sudobits.com/2015/06/05/fish-a-user-friendly-command-line-shell-for-ubuntulinux/)_

### Key points about Fish

* Fish has "search as you type" automatic suggestions based on your command history and the directory you are in. Similar to Bash's history search, Fish Shell's search history is **always** turned on. That way the user will be able to get interactive feedback when working in their terminal. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/fish.gif)
_[Image Source](https://taskwarrior.org/news/news.20140906/)_

* Fish also prefers features as commands rather than syntax. This makes features visible in terms of commands with options and help texts
* Since Fish by default comes with a lot of configurations already set, it is believed to be more beginner friendly than other `sh` options like Zsh.
* Fish's scripting language is different than Zsh and Bash. Zsh uses more aliases whereas Fish avoids using aliases in the scripting language.

If you were to just make scripts using basic commands such as, `cd`, `cp`, `vim`, `ssh`, and so on, you would not notice any difference in the way Fish and Bash's scripting languages work. 

One of the biggest differences is when you try capturing output from a command. In Bash you may be used to this:

```bash
todays_date=$(date)
echo "Todays date is $todays_date"
```

![Output](https://i.ibb.co/0hrF0Y3/fa71b0032fba.gif)

```
Todays Date is Tue Dec 13 15:29:28 CST 2022

```

Whereas in Fish, capturing output works differently. The equivalent for Fish in scripting would look like this:

```bash
set date (date)
echo "Todays Date $date"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/ezgif.com-gif-maker.gif)

```bash
todays date is Tue Dec 13 21:35:03 UTC 2022                                   

```

## Conclusion

Bash, Z Shell, and Fish Shell all have their merits, along with some similarities. You can use each of them effectively in your work environment now that you know a bit more about them. 

If you want something more configurable, you could use Zsh (or even install Oh My Zsh). If you want more of an interactive terminal experience without a lot of configuration, you could use Fish Shell. If you want the classic feel, you can just keep Bash. 

It all really comes down to your preferences as a developer - so just choose the shell that works best for you.

_Hope this helped you! Thank you for reading_ 🐚🐚🐚


---
title: How to code like a Hacker in the terminal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-17T19:55:16.000Z'
originalURL: https://freecodecamp.org/news/coding-like-a-hacker-in-the-terminal-79e22954968e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V73Ai9Nc8NhSRrs8zOvcHA.png
tags:
- name: hacking
  slug: hacking
- name: General Programming
  slug: programming
- name: satire
  slug: satire
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Caleb Taylor

  You are a hacker. Your home is the terminal. You know every key stroke is valuable.
  If something is less than 100% efficient, you will spend hours figuring out the
  right tool to save yourself seconds. Because it’s always worth it.


  _S...'
---

By Caleb Taylor

You are a hacker. Your home is the terminal. You know every key stroke is valuable. If something is less than 100% efficient, you will spend hours figuring out the right tool to save yourself seconds. Because it’s always worth it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GMvdjMQAjokYEFzTXjsp6Q.jpeg)
_Source: [Twitter](https://www.pablostanley.com/" rel="noopener" target="_blank" title="">Pablo Stanley</a> via <a href="https://twitter.com/pablostanley/status/963469081910296576" rel="noopener" target="_blank" title=")_

Does your constant search for newer and better ways to do things detract from actually doing things? Some may say yes, but you say nay. No work is worth doing unless you can lecture your coworkers on why you were able to do it so efficiently (setup time not included).

The following is a list of tools/features that every good hacker should know about.

> **Dislcaimer**: This article is written with a heavy dose of satire. It’s a twist on the [“Me, an Intellectual” meme.](https://knowyourmeme.com/memes/me-an-intellectual) While the suggestions are sincere (and by no means complete), the references to being a “hacker” are just for fun.

### **Shell (zsh)**

> **Average developer**: A shell is a shell. It doesn’t really matter which one I use. They all suck anyway.

> **You, a Hacker**: The shell is the lifeblood of my work. My passion for efficiency and features knows no bounds. My shell must be one worthy of a true hacker.

You live in the terminal, and that’s why you want to use a great shell. That’s why you use [zsh](http://www.zsh.org/).

It comes with a whole slew of features:

* Auto-correct of misspelled commands
* Easy drop-in replacement of bash
* Better `cd` completion using `<t`ab>
* Path expansion: `cd /u/c/c/j` + `<t`ab`> =cd /user/caleb/code/`jarvis
* [Much more](http://zsh.sourceforge.net/Doc/Release/zsh_toc.html)

It also comes with a great framework for managing your zsh configuration: [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh). It includes 200+ plugins and 140+ themes to add all sorts of awesome features to your terminal. A small sample:

* [git](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugin:git) - tons of aliases and useful functions for git
* t[mux](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/tmux/tmux.plugin.zsh) - alias and settings for integrating zsh with tmux
* [node](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/node) - adds `node-docs` command for opening website docs
* [osx](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/osx) - several utilities for working with OSX
* [web-search](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/web-search) - initialize web searches from command line
* [auto-suggestions](https://github.com/zsh-users/zsh-autosuggestions) - fast, unobtrusive suggestions as you type based on history

You can find the full list of plugins [here](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins).

### Session Management ([tmux](https://github.com/tmux/tmux))

> **Average developer**: Okay I’ve got my files open for lame_project_1. But I also need to do work in boring_project_2. I also need to ssh into a server and look at the logs. I guess I’ll just create a huge mess in my terminal that has files/tabs from multiple projects open in a way that I’ll eventually lose control of and be forced to close and start over.

> **You, a Hacker**: I work on several projects at once, so I need a tool to help me keep it organized. It should work across multiple platforms, and allow me to create organized work spaces and have a lot of other features that help with productivity.

You know that development can get messy. Sometimes, you have to work on several projects at once. That’s why you use [tmux](https://github.com/tmux/tmux).

It allows you to create sessions. Each session can be customized to the exact layout you need. You can name sessions for easy switching, and even save and restore sessions if your terminal is closed. Plus, it has its own customizable status line that will allow you display things like time, date, CPU usage, and more. And if you don’t know your CPU usage at any given moment, are you even a hacker?

![Image](https://cdn-media-1.freecodecamp.org/images/1*1aaEQExjdaueLgsLWxfr1g.gif)
_Organize your terminal with sessions and use fzf for fuzzy create/finding/deleting of sessions_

It even has a [plugin manager](https://github.com/tmux-plugins/tpm) and a [whole slew of awesome plugins & features](https://github.com/rothgar/awesome-tmux) that will take your hacking to the next level.

**Super-Pro Hacker Tip:**  
Use tmux with fzf via some [awesome scripts](https://github.com/junegunn/fzf/wiki/examples#tmux) to quickly create/delete/navigate to push your hacker level to over 9000.

### Search (ripgrep)

> **Average developer**: Where did I define that constant at? I know it’s somewhere in here. I’ll try to grep for it. What are the arguments again? Let me google that. Ah crap, now it’s searching my node_modules folder. This is the worst.

> **You, a Hacker**: When I search for something, it should be blazing fast. Also, it should use sensible default settings, like ignoring binaries or hidden files.

You know that searching your project is a common task. It should be fast, and it should not waste your time. This means things like ignoring anything that your `.gitignore` file ignores, and skipping binaries and hidden files. That’s why you use [ripgrep](https://github.com/BurntSushi/ripgrep). It’s like grep on steroids.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5Nt_6zoCkF0THdmdNtGoQw.gif)
_ripgrep in action_

In the [words of its creator](https://blog.burntsushi.net/ripgrep/): _“Use ripgrep if you like speed, filtering by default, fewer bugs and Unicode support.”_

### Fuzzy Finding ([fzf](https://github.com/junegunn/fzf))

> **Average developer**: It’s sure hard to remember the exact location of so many files within my project. I guess I’ll stumble around until I find the right one.

> **You, a Hacker**: I should be able to fuzzy-find files. I can type the file name, or some of the path, or all of it, and quickly find the file I’m looking for.

You know you shouldn’t have to type any more than you need to. So you use [fzf](https://github.com/junegunn/fzf), a general-purpose command-line fuzzy finder. It can also do much more than fuzzy-find files. It can used with any list: “files, command history, processes, hostnames, bookmarks, git commits, etc”.

**Super-Pro Hacker Tip:** You know that aliases are a great way to make shortcuts to take advantage of fzf’s features. For example, if you wanted to fuzzy-find a file, and then open up the selection in your default editor, you can add this to your `zsh` config:

![Image](https://cdn-media-1.freecodecamp.org/images/1*c4DFt6p5PDhOxHTx2p_lag.gif)
_Now you can run “fo” fuzzy-find and open a file_

Many more examples can be found on the [fzf wiki](https://github.com/junegunn/fzf/wiki/examples).

### Terminal Prompt ([Spaceship](https://github.com/denysdovhan/spaceship-prompt))

> **Average developer**: Who cares what my terminal prompt looks like? There’s no way it could possibly give me any useful information. I’ll just leave it as the default.

> **You, a Hacker**: I want my prompt to be amazing. It should be context-aware. It should give me useful info and be configurable. Also, it would be sweet if it was related to space.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vtc9ZCR2p7a_9-6MuFB-hw.gif)
_Welcome to the future… but actually the present. Hackers/astronauts only._

You know a prompt should be simple, clean, and provide only relevant information. It should also blow people’s minds when they see its beauty. That’s why you use [spaceship-prompt](https://github.com/denysdovhan/spaceship-prompt). It provides git/mercurial integration, battery level indicator, clever host name and user data, version numbers for a variety of libraries, gorgeous icons, and much more.

### Changing directories ([z](https://github.com/rupa/z))

> **Average developer:** I need to change my directory to my “hacker” project, which is inside of my cool folder, which is inside of my personal folder, which is inside of my code folder, which is in my home directory.

```
cd ~/code/personal/cool/hacker
```

> **You, a Hacker:** I need to change my directory to my “hacker” project.

```
z hacker
```

Typing out full file paths is what average developers do. You are a hacker. You rely on [z](https://github.com/rupa/z). Once installed, it will start learning which directories you visit. Then, you can give it a regex (or simple folder name) to hop to the most likely candidate.

### Bonus Hacker Tools

The following tools are additional ways to truly elevate your hacking game.

1. [wttr.in](https://github.com/chubin/wttr.in) — There’s only one right way to check the weather.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eoCAnuHdh9I69SiGJU_aOg.png)

2. Star Wars — Cool people like Star Wars. Hackers watch it in the terminal.

```
telnet towel.blinkenlights.nl
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*VHd1lA9C36pYxi_a5-afYQ.gif)
_Pro Tip: Watch star wars in another tmux pane while working. No one will question you._

3. [haxor-news](https://github.com/donnemartin/haxor-news) - Are you even a hacker if you don’t read [Hacker News](https://news.ycombinator.com/)?

![Image](https://cdn-media-1.freecodecamp.org/images/1*lcF0nWWF74IZCcc8I-ULBQ.gif)

4. Spotify - Using [shpotify](https://github.com/hnarayanan/shpotify), you can play music from the terminal (OSX only… Hey, stop booing! Put that chair down! Who threw that tomato!?), or [mopidy](https://www.mopidy.com/) for something that’s cross-platform.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ued2Pipg7m16DOKuwpAUdw.gif)
_God bless the commands in the terminal_

That about wraps it up. This is by no means a comprehensive list. Do you have any other amazing hacker tools? Leave a comment and let me know.

If you are interested in seeing more of these tools in action, checkout out my [dotfiles](https://github.com/ctaylo21/jarvis) that I use for development. As a bonus, here’s a screenshot of the glorious terminal in action:

![Image](https://cdn-media-1.freecodecamp.org/images/1*V73Ai9Nc8NhSRrs8zOvcHA.png)


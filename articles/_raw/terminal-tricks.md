---
title: 5 Awesome Terminal Tricks to Help You Level Up as a Developer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-21T03:04:36.000Z'
originalURL: https://freecodecamp.org/news/terminal-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/termtrick.png
tags:
- name: command line
  slug: command-line
- name: terminal
  slug: terminal
- name: tips
  slug: tips
seo_title: null
seo_desc: 'By Jackson Bates

  There are plenty of beginner tutorials around that help you learn command line basics,
  such as cd, ls, pwd and so on...but what about that fancy magic you''ve seen more
  experienced developers use?

  Here are my five favourite terminal c...'
---

By Jackson Bates

There are plenty of beginner tutorials around that help you learn command line basics, such as `cd`, `ls`, `pwd` and so on...but what about that fancy magic you've seen more experienced developers use?

Here are my five favourite terminal commands and utilities (in no particular order), to help you feel like the wizard you aspire to be! This is based on Ubuntu, but should be similar across other platforms (with maybe a little Googling). 

If you want to mention how to achieve similar results on MacOS or Windows, or there are other terminal tricks you would like to share, let me know in the comments below.

_This is adapted from my recent [YouTube video](https://www.youtube.com/watch?v=CmNTuq7M71U), which you can view to see these tricks in action!_

## sudo !!

`sudo !!` (or as I like to shout SUDO BANG BANG) will repeat the last command you typed, but with `sudo` in front of it.

If you have ever forgotten to use your `sudo` privilege when doing something that needs your administrator credentials (such as `apt update`for example), then `sudo !!` is a handy way to correct it without having to type the whole command again.

## tig

`tig` and `tig status` are probably the tools I use most often in my day-to-day work.

The eagle-eyed among you may have noticed that this is `git` spelled backwards, and indeed `tig` is an excellent git utility.

One of gits shortcomings for me is the lack of interactivity available in some of the basic actions. For example, while `git log` and `git status` give me useful information, it requires more manual git commands to do anything useful with that information.

`tig` acts like `git log`, but allows you to navigate up and down the log, and examine the contents of each commit from the command line.

`tig status` acts like `git status` except that it also allows for the same navigation as `tig`, and it also allows you to add files to staging easily from the command line.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/tig.png)

Both commands can be navigated using the `j` and `k` keys to move up and down, and pressing `enter` will open the information about the file (such as the commit diff). `q` also exits out of each command.

To add or remove specific files from your staging area in git, simply press `u`.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/tigstatus.png)

Now when you go to `git commit...` as usual, your  files have already been added, so no need to use the `git add` command.

## grep

This is a very well known 'trick' but it's incredibly useful all the same.

`grep` allows you to return the relevant lines from text output that match a particular pattern you pass it.

For example, if you are looking in a long `.log` file for an error, it can be hard to see amongst all irrelevant output. Grep can narrow down your search to only the relevant lines.

E.g. `grep error system.log`

With other commands that produce lots of terminal output, you can pipe it to `grep error` to do the same. For example, if you wanted to look at your Rails routes, but you were only interested in those related to admin you could do this:

`rake routes | grep admin` 

## history

`history` simply returns every command you have ever typed into your terminal. Why is this useful? Well, if, like me, you are super forgetful, the `history` command can show you what you've done before to jog your memory.

For example, whenever I have to restore a database back-up, I can never remember the syntax. `history | grep pg_restore` will show me every time I've used the `pg_restore` command, with the exact flags and arguments I had to use.

Notice the use of `grep` to narrow down the search? Work smart, not hard!

## spd-say

This one can be achieved a number of ways, and with various tools on each platform. `spd-say` is the default Ubuntu text-to-speech utility.

Using your terminal's ability to chain commands, you can use your speech utility tool of choice to tell you when a long running process has finished.

Example: `sudo apt update; spd-say done` 

Notice the `;` between the commands? This will basically run the `apt update` to completion and then invoke the next command. In this case it will helpfully say 'done' when it's finished. 

Feel free to make it say 'booyah!' if you feel like your day needs more celebrations of tiny wins in it.

---

## Share yours with me!

Devs love two things: laptop stickers and snazzy terminal commands. I've run out of room for stickers, but I'd love to hear your favourite terminal commands in the comments below!

You can also connect with me on Twitter [@JacksonBates](https://twitter.com/jacksonbates)


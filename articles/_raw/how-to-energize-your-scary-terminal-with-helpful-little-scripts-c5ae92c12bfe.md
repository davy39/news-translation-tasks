---
title: How to energize your scary terminal with helpful little scripts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-05T11:58:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-energize-your-scary-terminal-with-helpful-little-scripts-c5ae92c12bfe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ip_q_6I-kNpUjuPMOutuTA.jpeg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Vijayabharathi Balasubramanian

  I’m going to talk about three valuable tools that will finally help conquer your
  fear of terminals: Git Aliases, Bash Aliases, and One click snippets.

  A combination of aliases and bash scripts can make you very produ...'
---

By Vijayabharathi Balasubramanian

I’m going to talk about three valuable tools that will finally help conquer your fear of terminals: Git Aliases, Bash Aliases, and One click snippets.

A combination of aliases and bash scripts can make you very productive in your development workflow. Use it long enough and you’ll even forget the original commands beneath the aliases. Which isn’t actually a bad thing — until you get a shiny new laptop and have no idea where you placed your aliases in the old one :)

You may have used Git aliases. You might find bash aliases new. **But, don’t miss** the `gif` showing one-click icons at work towards the end. Those one-click desktop icons are my line of defense. They help me dive straight into coding/writing before the harmless “**top visited**” list on the browser’s new tab can send me off track.

By the way, I’m using Firefox’s nightly and it is easy to set up a clean slate as your new tab. All right, down to business.

### 1: Git Aliases

If terminal is the dungeon to people new to tech, Git tends to be the darkest passage, intimidating with long stretches of commands.

**But, Git is beautiful.** Try this [game](https://try.github.io/).

Part of making `git` easier to use is setting up your own aliases. That is, once you understand the underlying commands. This is not to give you **all** the useful aliases. Instead, I’ll point you towards the possibilities so that you can **build your own list of aliases.**

#### Flying Solo

Let’s say you are hacking on your own. You stage and commit all day, maybe your code or your writings for the blog. You’ll find a bunch of aliases very useful.

```
git config --global alias.s statusgit config --global alias.aa 'add --all'git config --global alias.cm 'commit -am'git config --global alias.up 'push'
```

Make sure you have a well defined `.gitignore` to avoid tracking unnecessary files such as `node_modules`. This will help you when you use `git aa` to stage all files.

All these aliases are stored in a config file under home directory. Take a look into `~/.gitconfig`. You can even edit the config file directly — just make sure you don’t trip it off.

#### Code Collaboration

When you are collaborating with a team, a whole other list of commands may be useful. Remember, rebase rewrites history. It is [advised only for local branches](https://coderwall.com/p/7aymfa/please-oh-please-use-git-pull-rebase), to clean up your code on top of remote branch.

```
git config --global alias.pr 'pull --rebase upstream master'
```

Here is one from [Harry](https://csswizardry.com/2017/05/little-things-i-like-to-do-with-git/) about aliasing `blame` to `praise` and other nuggets that you may find useful.

#### Advanced Aliases

```
git config --global alias.ls 'log --pretty=format:"%C(yellow)%h %C(green)%s %Creset(%ad)" --date=relative'
```

`%C(yellow)` marks the token following the color code in red. In our case above, `%h` stands for the commit hash, which will be painted yellow on our terminal. %Creset, without brackets, takes you back to default terminal font color. `--date=relative` tells you `days/weeks ago` instead of an actual date.

All those words may try hard to explain how it looks, but here it is:

![Image](https://cdn-media-1.freecodecamp.org/images/xSc0RQ1OUSbkrbmbpDk3zJreEWA2Sn96GH8X)
_color-coded git log_

#### References

You can learn more about decorating in [git-scm.com](https://git-scm.com/docs/pretty-formats). There is a whole bunch of information that you can extract such as `%h`, `%n` and so on. By the way, **that’s a whole free book on Git**. Start from page 1.

I learned a lot of useful tricks from Nicola a while back from his 2014 Atlassian summit talk. I couldn’t find the video, but I found [his slide](https://www.slideshare.net/GoAtlassian/becoming-a-git-master-nicola-paolucci). Don’t miss that anonymous function within aliases.

Here is a list of his G[it aliases](http://bit.do/git-aliases). But, in his own words, do not just copy aliases. Build them as you go, adding only the aliases that are useful to you. Otherwise, it’ll just be like spending hours curating articles/books that we’ll never read.

### 2: Bash Aliases

`Git` is not the only `command line interface` (CLI) that asks for some typing on the terminal. Think about `bundle exec rails db:migrate` on a terminal or `docker-compose exec npm run script` that you run on a container. How about something shorter?

If you use commands that are longer, on a daily basis, consider setting up bash aliases.

The syntax is very simple.

```
alias new_cmd='never-ending-command; and another command'
```

**You add this at the end of the `.bashrc` file in your home folder.** Normally `~/.bashrc` is where it is located. The recent one I have set up is for docker commands. It should serve as an example.

```
alias dc='docker-compose'alias de='docker-compose exec' alias up='cd ~/Projects/docker_project/; dc up'
```

I used to log out and log back in to make it work on terminals. However, this cool command from S[tackoverflow](https://stackoverflow.com/questions/2518127/how-do-i-reload-bashrc-without-logging-out-and-back-in) rescued me. Run this on your terminal and start using new aliases right away: `source ~/.bashrc`

Are you thinking what I am thinking? Forget about Git aliases? What do we name bash alias for `git pull --rebase upstream master`? How about `gprum`?

Go wild! Be cautious **not to reuse existing commands.** For example, `df` shows free disk space in Linux, so I wouldn’t use that as an alias for anything else.

### 3: One-Click Snippets

My favorites. One click, on your custom designed desktop icon, with your own logo, and you’ll have these ready to roll:

* Opens your project folder in VS Code/atom
* A terminal running dev server on one tab
* Another tab running tests / hot reloading
* Last tab that opens with Git status
* The last tab stays open for you to `git` things done.
* If your dev server doesn’t open browser, you can open it here

There is something magical when you can just tap on an icon and the entire environment springs up for you. One tap and you get your text editor, web server and tests running already.

The bash file `get-to-work.sh` looks like this. By the way, this is on Linux.

```
#!/bin/bashexport WD="~/development"code $WD gnome-terminal \ --tab --working-directory=$WD \ -e 'bash -c "export BASH_POST_RC=\"npm start\"; exec bash"' \ --tab --working-directory=$WD \ -e 'bash -c "export BASH_POST_RC=\"npm run watch\"; exec bash"' \ --tab --working-directory=$WD \ -e 'bash -c "export BASH_POST_RC=\"git status\"; exec bash"'
```

We have a working directory set up under variable `WD`. Then starts a very long line that folds for 7 lines on a terminal width of 80 characters. Don’t let it scare you. If you watch closely, we are opening gnome-terminal with three tabs and running three different commands on them.

Run this command to mark the bash script executable.

```
chmod +x get-to-work.sh
```

You can already check if the script is working. `cd` into the folder where you have the shell script and type this on your terminal.

```
./get-to-work.sh
```

Let’s add a nice desktop icon to our script. `Exec` and `Icon` are important. They need to be in a `.desktop` file. I’ve named mine as `get-to-work.desktop`.

By the way, this is for Linux. Most of the desktops use [freedesktop](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html) specification. Reading between the lines, I might have broken a few guidelines (such as not removing any fields even if they are not applicable).

```
[Desktop Entry] Name=Get To Work Comment=Start coding in an instant. GenericName=Development Environment Exec=/home/username/snippets/get-to-work.sh Icon=/usr/share/icons/logo.png Type=Application Terminal=true StartupNotify=true Categories=Utility;
```

Remember to use the correct path instead of `/home/username/...`. Make sure you place the `Icon` in an accessible folder where you have permission to at least read the file.

Validate and install the `.desktop` file.

```
desktop-file-validate get-to-work.desktop desktop-file-install get-to-work.desktop
```

In case you have permission issues, it is better to install it locally, like this:

```
desktop-file-install get-to-work.desktop --dir=.local/share/applications
```

That’s it. You’ll have your logo ready as an application within your launcher. You can set it up in the dock too.

#### Watch One-click Icon in Action

Here is a gif showing my recent one-click script.

![Image](https://cdn-media-1.freecodecamp.org/images/9HPhZCIGUJQhUVIH51ptARU7z2HocD-syzns)

A larger one, 2.6MB, can be found [here](https://www.pineboat.in/img/005_one_click/one-click.gif) if you want to take a closer look.

Here is one more I use to start writing my blog.

* Opens up blog folder on VS code
* Loads up `localhost` on firefox
* Opens up `hugo server` on terminal

Unlike the previous example, in this one, I use the elementary OS and default `pantheon-terminal` that comes with it. But this doesn’t open multiple tabs, and I haven’t figured out how to make `pantheon-terminal` do it (like we saw earlier with `gnome-terminal` ). That little `&` at the end of `firefox` gives control back to the script. Otherwise, my terminal wouldn’t open until I close `firefox`.

```
#!/bin/bash  export WORK_DIR="~/pineboat" /opt/firefox/firefox localhost:1313 & code $WORK_DIR pantheon-terminal -e 'bash -c "cd $WORK_DIR;hugo server -wvFD"'
```

Finally, I’ve setup a desktop file with the logo of my blog. Pretty sweet, isn’t it?

Hope that was useful and saves few keystrokes. Clap/Share/Tweet to let your network know, if you think they’ll enjoy this post. Any issues, log it under this [github issue](https://github.com/pineboat/pineboat.github.io/issues/4). Or in the conversations below.

Thanks for your time and attention!

_Originally published at [www.pineboat.in](https://www.pineboat.in/post/energize-terminal-with-git-bash-aliases-one-click-icon/) — an uncharted island in the internet._


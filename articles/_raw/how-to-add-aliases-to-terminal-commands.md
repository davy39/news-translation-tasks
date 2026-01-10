---
title: How to Add Aliases to Terminal Commands in Linux and Mac
subtitle: ''
author: Kaushal Joshi
co_authors: []
series: null
date: '2024-04-15T15:37:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-aliases-to-terminal-commands
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/terminal-alias.jpg
tags:
- name: Linux
  slug: linux
- name: mac
  slug: mac
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'In this article, we''ll explore a simple trick that can save you hours
  of typing repetitive commands in the terminal.

  As developers, we spend a substantial amount of time executing commands on the terminal.
  Whether it''s navigating through directories,...'
---

In this article, we'll explore a simple trick that can save you hours of typing repetitive commands in the terminal.

As developers, we spend a substantial amount of time executing commands on the terminal. Whether it's navigating through directories, running scripts, changing Node.js versions, or version control commands, manually typing every command is a time consuming task. 

For those who struggle to remember commands or their associated flags, this can become even more tedious.

Worry not! There's a simple yet powerful solution to this problem. It's called terminal aliases.

## The `alias` Command

The `alias` command allows you to create shortcuts for existing commands, making them easier to remember and quicker to execute. When you define an alias, you are creating a new label for an existing command.

### Syntax of `alias` Command

The syntax is straightforward: you can assign a command to a label like you'd assign a value to a variable in most programming languages.

```bash
alias alias_name='long command'
```

Let's dissect this command to understand it better:

* `alias`: The terminal command that enables defining an alias.
* `alias_name`: This is the name or the label you are assigning to the command. Basically, you will type this in the terminal instead of the full command.
* `'long command'`: This is the command that you want to add an alias to. Make sure that you are wrapping the command with single quotes (`'`) as almost all commands contain spaces or special characters. 

## Predefined Aliases

There are some predefined aliases already set within terminals. And there is a high chance that you were using them without even knowing.

Such aliases are defined within the system (`/etc/bash.bashrc`) or user specific (`~/.bsahrc`) shell configuration files. 

You can find a list of all predefined aliases by executing the `alias` command without any options or flags.

```
alias
```

## How to Create an Alias that Persists Across Sessions

By default, aliases only persist in the current session. That means, if you close the terminal, the alias will be erased and you cannot use it afterwards.

To tackle this, you must define the alias in the shell's configuration file. Shell is an interpreter that resides inside a terminal and establishes an interface between you and the operating system. Hence, accessing the correct shell as well as modifying the correct configuration file is very important.

Here are the configuration files for the three most commonly used shell applications:

1. **Bash**: `~/.bashrc`
2. **Zsh**: `~/.zshrc`
3. **Fish**: `~/.config/fish/config.fish`

Let's try adding a new alias to Bash.

```
echo "alias nrd='npm run dev'" >> ~/.bashrc
```

Let's dissect this command:

* `echo`: A terminal command that lets you write content within the terminal command.
* `"alias ..."`: This is the content we talked about in the previous point. It's an alias command that adds `nrd` as an alias for the `npm run dev` command. 
* `>>`: Tells the terminal to append the content on the left (alias command) to the file on the right. In our case, we are storing it in the bash configuration file.
* `~/.bashrc`: This is the file to which the content from the echo command will be added.

Don't forget to replace `~/.bashrc` with your shell's configuration file.

## How to Create a Dynamic Alias

Oftentimes, you need to use repetitive commands but with some little changes based on what you want. The best example of this is Git commands. In this case, you can add a substitute to your command which would be replaced by the dynamic option/parameter while executing it in the terminal.

```
alias gpll='git pull --rebase origin ${branch}'
```

While executing the command, you need to replace `${branch}` with the branch you want to pull changes from. This is how you would do it to pull changes from the `main` branch:

```
gpll main
```

You can also add multiple substitutes to your alias. Just make sure you are writing the alias with the correct order of actual values:

```
alias gpll='git pull --rebase ${remote} ${branch}
```

While executing the command, you need to replace `${remote}` and `${branch}` with appropriate values, like the following:

```
gpll origin main

```

## How to Create an Alias for Multiple Commands

There are cases where you need to use multiple commands sequentially. You can create an alias for that as well. Separate each command by `&&` which executes the command on the right after the command on the left is executed.

```
gpsh='git pull --rebase && git push'
```

## How to Delete an Alias

If you want to delete an alias from the current session, you can use the `unalias` command. This command takes only one argument — the alias name.

```
unalias my-alias-name
```

However, if you want to delete an alias saved in the configuration file, you need to delete it from the file itself. You can use a simple text editor like [Nano](https://help.ubuntu.com/community/Nano) to do this.

```
nano ~/.bashrc
```

Scroll down to the bottom to find all of your aliases and delete the ones you don't want anymore.

When you're done, you can exit the editor after saving. This is the place where I can introduce a meme about not being able to exit terminal-based text editors. But with Nano, it's very simple:

1. Press `ctrl`+`x` if you are on Linux and `^`+`x` if you are on Mac.
2. Press `Y` to confirm changes
3. Hit Enter or return based on your operating system to save the file.

See? Nothing difficult :)

## Caveats

There are two important things that you must remember while creating an alias.

### Aliases are shell-restricted

Aliases are specific to the shell you are using. An alias created in one shell won't work in another shell.

You must create a new alias if you want to use it in a different session. There is no workaround to this caveat. One trick you can do is to manually save the alias to the config files of all the shells you use.

### Aliases are session bound by default

Aliases are only available in the current session. If you open a new terminal window or log out, the alias will not be available.

Hence, it's recommended to always save an alias to a configuration file so you use it anytime you want.

## TL;DR

* `alias` command adds _shortcuts_ to a command or series of commands. `alias shortcut='existing valid command`.
* Save an alias to the shell's config file so it is persisted across sessions. Every shell has a unique config file. `echo "nrd='npm run dev'" >> ~/.bashrc`.
* Create a dynamic alias by substituting the dynamic value with a placeholder. The placeholder must be wrapped by `${}`. `alias gp='git pull origin ${branch}` should be executed as `gp main` in the terminal.
* Add multiple commands to an alias by joining them with `&&`.
* Delete an alias by manually erasing it from the config file. 

## Wrapping up

I hope this blog helps you optimize your time and boosts your developer productivity. If it did, don't forget to share this with your peers so they can improve their efficiency as well.

What other techniques do you use to work efficiently? I would love to know more about it. I am most active on [Twitter](https://twitter.com/clumsy_coder) and [Peerlist](https://peerlist.io/kaushal), if you want to say hi!

Until then, happy scripting! 👨‍💻


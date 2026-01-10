---
title: How to Manage Directory-Scoped Variables with direnv in POSIX Systems
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-22T21:39:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-directory-scoped-envs-with-direnv-in-posix-systems
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pexels-aleksejs-bergmanis-681335.jpg
tags:
- name: Productivity
  slug: productivity
- name: unix
  slug: unix
- name: variables
  slug: variables
seo_title: null
seo_desc: 'By Otavio Ehrenberger

  A common practice in software projects is to keep certain information separated
  but accessible from the codebase which uses it. Developers usually do this with
  secrets such as passwords or private keys, or with user or context-s...'
---

By Otavio Ehrenberger

A common practice in software projects is to keep certain information separated but accessible from the codebase which uses it. Developers usually do this with secrets such as passwords or private keys, or with user or context-specific info pieces. 

But managing environment variables can be a pain. There are a number of solutions to ease that pain, and there are even built-in ones such as [bash_profile](https://www.baeldung.com/linux/bashrc-vs-bash-profile-vs-profile).

One solution I've discovered recently and found particularly convenient is [direnv](https://github.com/direnv/direnv). It's a shell extension which lets you define environment variables scoped by directory. 

After installing and hooking the extension to your shell, `direnv` will execute every time you change directories, looking for an `.envrc` file in the same or in a superior directory tree level. It will then load the defined variables to the current environment, and unload them if it ceases to detect the same `.envrc`.

Note that `direnv` will load the first detected `.envrc` file, which means that _the environment will_ **not** _inherit values from a_ `.envrc` _in a parent directory_.

It is also important to keep in mind that the environment variables _will only be loaded to your shell session once you move to a directory affected by a_ `.envrc` _file_. So if you try something like running a script which loads an environment defined in a directory below your current level, the variables won't be accessible.

## How to Install `direnv`

Here's a [list of supported systems](https://direnv.net/docs/installation.html). It is very likely that your UNIX-based system's main open source package manager has it available. 

Suppose we are on Debian, we can install `direnv` by running the standard external package install command in the terminal:

```bash
sudo apt-get install direnv

```

## How to Setup `direnv`

After you install it, you need to hook `direnv` to your shell. If you're using bash, you can do this by appending this line to the end of your shell startup config file:

```bash
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc

```

It's almost the same for ZShell:

```bash
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc

```

Direnv also supports FISH, TCSH, and Elvish. [Here are the hooking instructions for each supported shell](https://direnv.net/docs/hook.html).

## How to Use `direnv`

Now we must create an `.envrc` file for the directory we would like to scope the environment variables to.

Say we create it for the directory `~/project`.

```bash
echo export FOO='I love Linux!' >> ~/project/.envrc

```

You will then receive a warning that the current `.envrc` wasn't read. `direnv` will block loading `.envrc` every time it detects changes which were not explicitly allowed. So now run:

```bash
direnv allow ~/project

```

and voilà!, you now have a directory-scoped environment.

Remember when I told you that '`direnv` will block loading `.envrc` every time it detects changes which were not explicitly allowed'? This isn't limited to newly introduced changes – the whole file will be unauthorized. So when you do this:

```bash
echo export BAR='It is actually called GNU/Linux!' >> ~/project/.envrc

```

you will have to run `direnv allow ~/project` again, even to access `$FOO`. Kinda boring, but biased towards safety.

Every time an `.envrc` is loaded, direnv will output a message with the file path and also the names of the variables loaded, so you don't need to worry about forgetting your setup. It will also tell you whenever an environment was unloaded.

### Thanks for reading!

That's it! It's pretty straightforward, and I hope you find it as convenient as I did.


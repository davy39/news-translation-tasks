---
title: How to Install Python 3 on Mac – Brew Install Update Tutorial
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2021-04-06T03:19:47.000Z'
originalURL: https://freecodecamp.org/news/python-version-on-mac-update
coverImage: https://cdn-media-2.freecodecamp.org/w1280/606ba4e1d5756f080ba94d0c.jpg
tags:
- name: mac
  slug: mac
- name: Python
  slug: python
seo_title: null
seo_desc: 'MacOS comes with Python pre-installed. But it''s Python Version 2.7, which
  is now deprecated (abandoned by the Python developer community).

  The entire Python community has now moved on to using Python 3.x (the current version
  as of writing this is 3.9...'
---

MacOS comes with Python pre-installed. But it's Python Version 2.7, which is now deprecated (abandoned by the Python developer community).

The entire Python community has now moved on to using Python 3.x (the current version as of writing this is 3.9). And Python 4.x will be out soon, but it will be completely backward compatible.

If you try to run Python from your MacOS terminal, you'll even see this warning:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-_freecodecamp_MacBook-Pro_-___-_-zsh_-_84-24-1.png)
_WARNING: Python 2.7 is not recommended. This version is included in macOS for compatibility with legacy software. Future versions of macOS will not include Python 2.7. Instead, it is recommended that you transition to using 'python3' from within Terminal._

Until Apple decides to set Python 3.x, as the default you're going to have to install it yourself.

## A Single Command to Run Python 3

For some of you reading this, this command may be enough. You can run Python 3 using this command (with the 3 at the end).

```bash
python3
```

If that's all you came for, no worries. Have a fun day and happy coding.

But if you want a proper Python version control system to keep track of various versions – and have fine-grain control over which version you use – this tutorial will show you exactly how to accomplish this.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Megaman-810x600.jpeg)
_By the way, if you're wondering why I keep referring to Python 3.x – the x is a stand-in for sub-versions (or point releases as developers call them.) This means any version of Python 3._

## How to Install Homebrew on Mac

First you need to install Homebrew, a powerful package manager for Mac.

Open up your terminal. You can do this by using MacOS spotlight (command+space) and typing "terminal".

Now that you're in a command line, you can install the latest version of Homebrew by running this command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Your terminal will ask for Super User-level access. You will need to type your password to run this command. This is the same password you type when you log into your Mac. Type it and hit enter.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-__bin_bash_-c__-__bin_bash_-_sudo_-_bash_-c____bin_bash_012set_-u_012_012abort___-_012__printf___s_n_______012__exit_1_012-_012_012if___-z___-BASH_VERSION_--_____then_012__abort__Bash_is_required_to_interpret_this_script___012.png)
_A screenshot of my heavily customized terminal. Your terminal will probably look different from this._

Homebrew will ask you to confirm you want to install the following. You have to press enter to continue. (Or press any other key if you get cold feet.)

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-__bin_bash_-c__-__bin_bash_-_bash_-c____bin_bash_012set_-u_012_012abort___-_012__printf___s_n_______012__exit_1_012-_012_012if___-z___-BASH_VERSION_--_____then_012__abort__Bash_is_required_to_interpret_this_script___012fi_012_.png)

## How to Install pyenv to Manage Your Python Versions

Now let's take a moment to install PyEnv. This library will help you switch between different versions of Python (in case you need to run Python 2.x for some reason, and in anticipation of Python 4.0 coming).

Run this command:

```bash
brew install pyenv
```

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-_freecodecamp_MacBook-Pro_-___-_-zsh_-_90-24.png)
_PyEnv installing_

Now you can install the latest version of Python.

## How to Use pyenv to Install Python or Update Your Python Version

Now you just need to run the following command:

```bash
pyenv install 3.9.2 
```

Note that you can substitute 3.9.2 for whatever the latest version of Python is. For example, once Python 4.0.0 comes out, you can run this:

```bash
pyenv install 4.0.0
```

## Troubleshooting pyenv Installation

If you encounter an error that "C compiler cannot create executables" then the simplest way to solve this is to reinstall Apple's Xcode.

Xcode is a tool created by Apple that includes all the C libraries and other tools that Python uses when it runs on MacOS. Xcode is a whopping 11 gigabytes, but you'll want to be up-to-date. You may want to run this while you're sleeping. 

You can [get the latest version of Apple's Xcode here](https://developer.apple.com/download/). I had to do this after upgrading to MacOS Big Sur, but once I did, all the following commands worked fine. Just re-run the above `pyenv install 3.9.2` and it should now work.

## How to Set Up Your MacOS PATH for pyenv (Bash or ZSH)

First you need to update your Unix path to pave a way for PyEnv to be able to interact with your system.

This is a long explanation of how PATH works in MacOS (and Unix), straight from [the pyenv GitHub repo](https://github.com/pyenv/pyenv).

> When you run a command like `python` or `pip`, your operating system searches through a list of directories to find an executable file with that name. This list of directories lives in an environment variable called `PATH`, with each directory in the list separated by a colon:

```
/usr/local/bin:/usr/bin:/bin

```

> Directories in `PATH` are searched from left to right, so a matching executable in a directory at the beginning of the list takes precedence over another one at the end. In this example, the `/usr/local/bin` directory will be searched first, then `/usr/bin`, then `/bin`.

And here is their explanation of what a Shim is. I'm quoting them at length again because I really can't explain this better myself.

> pyenv works by inserting a directory of _shims_ at the front of your `PATH`:

```
$(pyenv root)/shims:/usr/local/bin:/usr/bin:/bin

```

> Through a process called _rehashing_, pyenv maintains shims in that directory to match every Python command across every installed version of Python—`python`, `pip`, and so on.

> Shims are lightweight executables that simply pass your command along to pyenv.

Here's how to update your `.bash_profile` in Bash (which is installed in MacOS by default):

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
```

Then run:

```
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
```

**Note:** if you do not have a `/bin` directory in your `pyenv_root` folder (you may only have a `/shims` directory) you may need to instead run this version of the command: 

```
`echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.bash_profile`
```

Then you want to add PyEnv Init to your terminal. Run this command if you're using Bash (again, this is the default with MacOS):

```
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

```

Now reset your terminal by running this command:

```
reset
```

## How to Set Up Your MacOS PATH for pyenv in ZSH or OhMyZSH

If instead of using the Mac default Bash, you're using ZSH (or OhMyZSH) like I am, you'll want to edit the `.zshrc` file instead:

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
```

Then run this:

```
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init --path)"\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
```

## How to Set a Version of Python to Global Default (Bash or ZSH)

You can set the latest version of Python to be global, meaning it will be the default version of Python MacOS uses when you run Python applications.

Run this command:

```bash
pyenv global 3.9.2
```

Again, you can replace 3.9.2 with whatever the latest version is.

Now you can verify that this worked by checking the global version of Python:

```bash
pyenv versions
```

You should see this output:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-_freecodecamp_MacBook-Pro_-_-zsh_-_84-24.png)
_The * means that version is now the global default_

## The Final Step: Close Your Terminal and Restart it

Once you've restarted your terminal, you run the `python` command and you'll launch the new version of Python instead of the old one.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/freecodecamp_-_python_-_python_-_python_-_119-36.png)
_Yay. Python 3.9.2 and no deprecation warnings_

Congratulations. Thank you for reading this, and happy coding.


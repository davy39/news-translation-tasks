---
title: How to Configure your macOs Terminal with Zsh like a Pro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T18:05:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-configure-your-macos-terminal-with-zsh-like-a-pro-c0ab3f3c1156
coverImage: https://cdn-media-1.freecodecamp.org/images/1*REqZX2_JqQjbH9Ly3QsgLg.png
tags:
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: terminal
  slug: terminal
- name: zsh
  slug: zsh
seo_title: null
seo_desc: 'By Chiamaka Ikeanyi

  Sometimes, using the default terminal sucks. You want to go out of the ordinary,
  to add life to the boring terminal and improve your productivity.

  Z shell (Zsh) is a Unix shell built on top of bash (the default shell for macOS)
  wi...'
---

By Chiamaka Ikeanyi

Sometimes, using the default terminal sucks. You want to go out of the ordinary, to add life to the boring terminal and improve your productivity.

[Z shell](https://en.wikipedia.org/wiki/Z_shell) (Zsh) is a Unix shell built on top of bash (the default shell for macOS) with a large number of improvements.

In this walk-through, we will configure iTerm2 with ZSH and its dependencies. This is a no-brainer, and after this, you’ll ponder the reason for not discovering ZSH earlier. Well, since you’re here already, let’s kick-start this.

### Keynotes

* Homebrew installation
* iTerm2 installation
* ZSH and Oh My ZSH installations
* Setting up the dependencies to create a beautiful terminal

### Step 1: Install Homebrew

[Homebrew](https://brew.sh/) is a free and open-source software package management system that simplifies the installation of software on Apple’s macOS.

Before installing Homebrew, we need to install the CLI tools for Xcode. Open your terminal and run the command:

```bash
xcode-select —-install
```

If you get an error, run `xcode-select -r` to reset `xcode-select`.

Then, install Homebrew.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

```

### Step 2: Install iTerm2

iTerm2 is a replacement for terminal and the successor to iTerm. Most software engineers prefer i[Term2](https://www.iterm2.com/) over the default terminal that ships with macOS as a result of [its cool features](https://www.iterm2.com/features.html). You can integrate zsh into iTerm2 to increase productivity.

To install iTerm2, run the command:

```bash
brew cask install iterm2
```

### Step 3: Install ZSH

> _Zsh is a shell designed for interactive use, although it is also a powerful scripting language._

By default, macOs ships with zsh located in`/bin/zsh`.

Let’s install zsh using brew and make iTerm2 use it.

```bash
brew install zsh
```

### Step 4: Install Oh My Zsh

> “Oh My Zsh is an open source, community-driven framework for managing your [zsh](https://www.zsh.org/) configuration. It will not make you a 10x developer…but you might feel like one”

> — Robby Russell

It runs on Zsh to provide cool features configurable within the ~/.zhrc config file. Install [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh) by running the command

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

Check the installed version

```bash
zsh --version
```

You can upgrade it to get the latest features it offers.

```bash
upgrade_oh_my_zsh
```

Restart iTerm2 to dive into the new experience of using Zsh. Welcome to the “Oh My Zsh” world ?.

That’s not all. Now, we will install the dependencies to get the best out of Zsh.

### Step 5: Change the Default Theme

Oh My Zsh comes bundled with a lot of themes. The default theme is robbyrussell, but you can change it to any theme of your choice. In this scenario, I changed it to agnoster, an already pre-installed theme.

You then need to select this theme in your `~/.zshrc`. To open the config file (.zshrc), run the command:

```bash
nano ~/.zshrc
```

![Image](https://cdn-media-1.freecodecamp.org/images/czy8LqFZcWJnyNWPq8MLpU-u6r74ozW-ndAz)
_Zsh theme set to agnoster_

Or open the file in a text editor with

```bash
open ~/.zshrc
```

![Image](https://cdn-media-1.freecodecamp.org/images/umcC5b7qtng38UbZngNRwMXq6NzwmR8SqIes)

Set the zsh theme and update your changes

```bash
source ~/.zhrc
```

### Using a Custom Theme

To install another theme not pre-installed, clone the repository into `custom/themes`directory. In this scenario, we’ll install [powerlevel9k](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions#option-2-install-for-oh-my-zsh),

```bash
$ git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```

Then, select this theme in your `~/.zshrc`

```bash
ZSH_THEME="powerlevel9k/powerlevel9k"
```

Update your changes by running the command `source ~/.zshrc`

Navigate to `iTerm2 > Preferences > Profiles > Colors` if you wish to change the background color of the terminal.

The selected theme in this scenario requires powerline fonts. So, let’s install that.

### Step 6: Install Fonts

I will be using [Inconsolata](https://github.com/powerline/fonts/tree/master/Inconsolata). Get your preferred font out of these [powerline fonts](https://github.com/powerline/fonts). Then, download and install it.

![Image](https://cdn-media-1.freecodecamp.org/images/l-nkEZ87vggoFrm5xPNGvyNMv9hyxZc2tE1U)

Or download the entire font.

```bash
git clone https://github.com/powerline/fonts.git

cd fonts

./install.sh
```

To change the font, navigate to `iTerm2 > Preferences > Profiles > Text > Change Font`.

Now, you can see Inconsolata listed as one of the fonts. Select your preferred font. For fonts that support ligatures like [FiraCode](https://github.com/tonsky/FiraCode), check the “Use ligatures” option to view your arrows and other operators in a stylish manner like ( **→** ).

![Image](https://cdn-media-1.freecodecamp.org/images/flJ1CL1uDv0QoX-TK0MBgn7CVuyG0wOG388V)
_Select a powerline font_

### Step 7: Install Color Scheme

Let’s change the color scheme to bring out the beauty of our terminal. Navigate to [iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) and download the ZIP folder. Then, extract the downloaded folder cos what we need resides in the schemes folder.

Navigate to `iTerm2 > Preferences > Profile > Colors > Color Presets > Import`

* Navigate to the schemes folder and select your preferred color schemes to import them.
* Click on a specific color scheme to activate it. In this scenario, I activated Batman which is my preferred color scheme.

![Image](https://cdn-media-1.freecodecamp.org/images/0NGtEWFgLWeyM4tzGVtQ4xTNNqBdnHMdZMGw)

Tada! ? We’re done with the basic settings.

![Image](https://cdn-media-1.freecodecamp.org/images/tFnT1hiSKgWYMYYTNIzUfjD1Z5vIe2QnjSlI)
_Batman color scheme_

### Step 8: Install Plugins

Oh My ZSH comes preloaded with a git plugin. To add more, for instance, docker, auto-suggestion, syntax highlighting and more:

* Clone the Git repository

```bash
git clone https://github.com/zsh-users/zsh-docker.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-docker
```

* Head over to `.oh-my-zsh > custom > plugins` directory to view the cloned directory. To access this, run the command `open ~/.oh-my-zsh`
* Add the plugin to the plugin section of the config file `~/.zshrc` shown below
* Update your changes by running the command `source ~/.zshrc`

![Image](https://cdn-media-1.freecodecamp.org/images/oK1lzMvgGrsycWUoueagV0a99eq00akzwiEW)

### Step 9: Add Aliases

Aliases are shortcuts used to reduce the time spent on typing commands. Add aliases to commands you run in the section shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/VmmW4SCRGXW2cQ74o4nODyLOlNgZYeJEgOyR)
_Typing `**dckimgs**` executes docker images command_

**_Thanks for reading_**.

If you know about other means of improving productivity using ZSH, you can drop them on the comment section, I will be glad to hear from you.


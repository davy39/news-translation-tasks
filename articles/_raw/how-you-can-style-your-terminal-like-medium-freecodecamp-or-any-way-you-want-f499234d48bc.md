---
title: How you can style your terminal like Medium, freeCodeCamp, or any way you want
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-13T20:28:29.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-style-your-terminal-like-medium-freecodecamp-or-any-way-you-want-f499234d48bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7eesI0V6YMEx6E67J2HBOQ.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By ryanwhocodes

  Learn how to configure your own terminal theme using Powerlevel9k for Zsh and iTerm2!

  This tutorial will show you how to personalise your terminal design by configuring
  iTerm2 with Powerlevel9k. Powerlevel9k is a popular and highly cu...'
---

By ryanwhocodes

**Learn how to configure your own terminal theme using Powerlevel9k for Zsh and iTerm2!**

This tutorial will show you how to personalise your terminal design by configuring iTerm2 with [Powerlevel9k](https://github.com/bhilburn/powerlevel9k). Powerlevel9k is a popular and highly customisable terminal theme for the shell Zsh. I will explain how to set this up with icons from [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts), your choice of [color scheme](https://iterm2colorschemes.com/), and your own custom prompt sections.

![Image](https://cdn-media-1.freecodecamp.org/images/ug6M6AJBYTzNKyyAfbUXPKGHg7BX9Ag4xZ3w)

Here are some possible ways you could style your terminal, using example custom prompt sections based on Medium and freeCodeCamp:

![Image](https://cdn-media-1.freecodecamp.org/images/N7mfF0pbY0MNMReE3VmJeiOXRjmDnJ4ZfqzJ)

![Image](https://cdn-media-1.freecodecamp.org/images/DCLseVcFoHlgOfja7tDw1w4uDHKhGdfgcLf5)

![Image](https://cdn-media-1.freecodecamp.org/images/vhx-YfOYZ8Y4zGPibWdmS7lkUiGxSZ6RIp9p)
_Example color schemes | Left: based on [Solarised Dark](https://design-style-guide.freecodecamp.org/" rel="noopener" target="_blank" title="">freeCodeCamp’s style guide</a> | Center: <a href="https://draculatheme.com/iterm" rel="noopener" target="_blank" title="">Dracula</a> | Right: <a href="https://iterm2colorschemes.com/" rel="noopener" target="_blank" title="). Click on the images to view the screenshot larger._

#### Tutorial

* [Prerequisites: install Homebrew, iTerm2 and Zsh](#30b5)
* [Choose and set a colour scheme](#8c3a)
* [Download Nerd Fonts and configure iTerm2 to use it](#57a5)
* [Add the Powerlevel9k theme for Zsh](#8f6c)
* [Customise your prompt](#c8bd)
* [The complete .zshrc](#c9d7)
* [Some bonus options to try](#d063)
* [Find out more](#8c3a)

### Prerequisites: install Homebrew, iTerm2 and Zsh

* If you haven’t already, install the mac package manager [**Homebrew**](https://docs.brew.sh/Installation.html).
* Install the terminal **iTerm2** [here](https://www.iterm2.com/downloads.html) or through homebrew using `brew cask install iterm2`
* Then install the shell [**Zsh**](http://www.zsh.org/) (a alternative to [bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))) using `brew install zsh`
* Open iTerm2. To change the default shell to Zsh rather than bash, run the change shell command in your terminal. `chsh -s /bin/zsh`

The Zsh resource file, `~/.zshrc`, is a script that is run whenever you start Zsh. This tutorial will add commands and variables to this file to configure your terminal.

### Choose and set a colour scheme

There are many iTerm colour schemes out there. One source is [iterm2colorschemes](https://iterm2colorschemes.com/), which gives you about 175 choices. Once you have downloaded them, select `iTerm -> Preferences -> Profiles -> Colors -> Color Prese`ts -> Import then select the colour scheme you like, such as the Dracula and Solarised Dark themes pictured at the top of this article.

![Image](https://cdn-media-1.freecodecamp.org/images/QtBxNWJHnkv5BYnG2c86mBlZaRf9bQlRoEty)
_freeCodeCamp theme added to the original [Powerlevel9k logo](https://github.com/bhilburn/powerlevel9k" rel="noopener" target="_blank" title=")_

You can also create your own color sheme by setting the ANSI colors to ones you like, then click on Color Presets → Export it to save it.

If you are interested in finding out the color scheme freeCodeCamp uses for its brand, you can view this at [design-style-guide.freecodecamp.org](https://design-style-guide.freecodecamp.org/).

### Download Nerd Fonts and configure iTerm2 to use it

To be able to have prompt with extra programming icons you need to install a special font set. This will show you how to install and configure [nerd-fonts](https://github.com/ryanoasis/nerd-fonts#font-installation).

> _Nerd Fonts is a project that patches developer targeted fonts with a high number of glyphs (icons). Specifically to add a high number of extra glyphs from popular ‘iconic fonts’ such as [Font Awesome ➶](https://github.com/FortAwesome/Font-Awesome), [Devicons ➶](https://vorillaz.github.io/devicons/), [Octicons ➶](https://github.com/primer/octicons), and [others](https://github.com/ryanoasis/nerd-fonts#glyph-sets)._  
>  _— [Nerd Fonts on GitHub](https://github.com/ryanoasis/nerd-fonts)_

#### Download Nerd Fonts with curl

There are [various options for installing Nerd Fonts](https://github.com/ryanoasis/nerd-fonts#font-installation). Here is the [option to install using homebrew](https://github.com/ryanoasis/nerd-fonts#option-4-homebrew-fonts).

```
brew tap caskroom/fontsbrew cask install font-hack-nerd-font
```

To learn about using Nerd Fonts in more detail, check out my article:

[**Nerd Fonts: How to install, configure, and remove programming fonts on a mac**](https://medium.com/the-code-review/nerd-fonts-how-to-install-configure-and-remove-programming-fonts-on-a-mac-178833b9daf3)

![Image](https://cdn-media-1.freecodecamp.org/images/QC7uMM0W2ijqY9xIeZ2B6NMa6zCvtC8I20y6)

#### Configure iTerm2 with Nerd Fonts

Next setup **iTerm2** to use the font by going to:

```
iTerm2 -> Preferences -> Profiles -> Text -> Font -> Change Font
```

![Image](https://cdn-media-1.freecodecamp.org/images/mAHoFMzKIMhIOnlZZ0Y6o0SmHfCVimuavG69)

Select the font **Hack Regular Nerd Font Complete** and adjust the size if your want too. Also check the box for `Use a different font for non-ASCII text` and select the font again. It should be displaying the new font and icons in the prompt.

![Image](https://cdn-media-1.freecodecamp.org/images/GBrkB7DoD-KWTvr6M-oP2zDwF5omEEiNmwbZ)
_Powerlevel9k: The most awesome Powerline theme for ZSH around! [https://github.com/bhilburn/powerlevel9k](https://github.com/bhilburn/powerlevel9k" rel="noopener" target="_blank" title=")_

### Add the Powerlevel9k theme for Zsh

My favourite theme for Zsh is [Powerlevel9k](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions#step-1-install-powerlevel9k). It styles your prompt with coloured segments for different purposes and can include the Nerd Font programming icons.

#### Installation

You need to tell Powerlevel9k to use the Nerd Fonts in your `~/.zshrc`.

```
echo "POWERLEVEL9K_MODE='nerdfont-complete'" >> ~/.zshrc
```

Next install the Powerleve9k theme from [GitHub](https://github.com/bhilburn/powerlevel9k) and add the command to load it when Zsh starts.

```
git clone https://github.com/bhilburn/powerlevel9k.git ~/powerlevel9kecho 'source  ~/powerlevel9k/powerlevel9k.zsh-theme' >> ~/.zshrc
```

**Note**: The font needs to be set before Powerlevel9k is initialised in order to use it. If you open your `~/.zshrc`, it should have the commands in this order.

```
POWERLEVEL9K_MODE='nerdfont-complete'source ~/powerlevel9k/powerlevel9k.zsh-theme
```

Powerlevel9k is highly configurable. For example, you can adjust the spacing and prompt segments — and these have various options too.

### Customise your prompt

#### Configure prompt elements and layout

Powerlevel9k comes with some preconfigured prompt segments, which you can simply add in to an environment variable in order to use. These cover many different aspects of using your terminal, version control system (eg git), and some software development tools, such as for Node.js and Ruby.

To change your setup, open your `~/.zshrc` and add in the [configuration](https://github.com/bhilburn/powerlevel9k#prompt-customization) you prefer. It’s best practice to declare all the configuration before you call the Powerlevel9k theme’s script. This is an example of a basic setup, which is listed in my `~/.zshrc`.

```
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir vcs newline status)POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()POWERLEVEL9K_PROMPT_ADD_NEWLINE=truePOWERLEVEL9K_MODE='nerdfont-complete'
```

```
source ~/powerlevel9k/powerlevel9k.zsh-theme
```

The main things customised here are the segments for the left prompt where there is the:

* Working directory
* Version control system (that displays the git status and branch)
* A newline
* Return code of the previous command

A right hand prompt is also available, but I don’t like using it. The last option is to add a new line after each command is executed.

**Next I will show you how to make your own personalised prompt sections.**

![Image](https://cdn-media-1.freecodecamp.org/images/Z6LjqgHnlR2hDMj-ISRMzVWRYvGysw7H9DGj)
_Powerlevel9k allows you to add your own prompt sections that include icons, text and choices of background and foreground colors. So for example, you could create a section based on freeCodeCamp’s style._

#### Create custom prompt segments

In the screenshot at the top of the post, I showed the Medium icon as well as a freeCodeCamp segment. This part of the tutorial will explain in depth how these were configured and how you can customise your own prompt sections.

**This is an opportunity to be really creative.** You could design something code related, such as [the programming language you are using](https://medium.com/the-code-review/powerlevel9k-personalise-your-prompt-for-any-programming-language-68974c127c63), or something completely different!

Powerlevel9k allows you to easily add custom prompt segments by adding them to certain environment variables. It has to follow the below syntax, where they are prefixed by “custom”. This is the configuration for the custom Medium and freeCodeCamp elements used in the terminal screenshots at the top of this article.

```
# Customise the Powerlevel9k promptsPOWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(  custom_medium custom_freecodecamp dir vcs newline status)POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()POWERLEVEL9K_PROMPT_ADD_NEWLINE=true
```

```
# Add the custom Medium M icon prompt segmentPOWERLEVEL9K_CUSTOM_MEDIUM="echo -n '\uF859'"POWERLEVEL9K_CUSTOM_MEDIUM_FOREGROUND="black"POWERLEVEL9K_CUSTOM_MEDIUM_BACKGROUND="white"
```

```
# Add the custom freeCodeCamp prompt segmentPOWERLEVEL9K_CUSTOM_FREECODECAMP="echo -n ’\uE242' freeCodeCamp"POWERLEVEL9K_CUSTOM_FREECODECAMP_FOREGROUND="white"POWERLEVEL9K_CUSTOM_FREECODECAMP_BACKGROUND="cyan"
```

#### Set variable names for a custom prompt section

Powerlevel9k includes code to dynamically create prompt elements based on environment variables. Follow this structure to add your own custom prompt section.

→ Add `custom_<YOUR PROMPT SECTION NA`ME&g`t; to POWERLEVEL9K_LEFT_PROMPT_EL`EMEN`TS or POWERLEVEL9K_RIGHT_PROMPT_EL`EMENTS

→ Set a color for `POWERLEVEL9K_CUSTOM_<YOUR PROMPT SECTION NAME>_FORE`GROUND

→ Set a color for `POWERLEVEL9K_CUSTOM_<YOUR PROMPT SECTION NAME>_BACK`GROUND

→ Set the icon and text for the content of the section defined to `POWERLEVEL9K_CUSTOM_<YOUR PROMPT SECTION NA`ME>

#### Add your own choice of Nerd Font icon and text

The following prints the code associated with the Nerd Font icon — you can browse them on the [Nerd Fonts website](http://nerdfonts.com/#cheat-sheet).

```
POWERLEVEL9K_CUSTOM_FREECODECAMP="echo -n ’\uE242' freeCodeCamp"
```

Just replace the 4 characters after `\u` with the code for the icon you want to use. Follow the icon with your choice of text.

The `-n` option for the command `echo` tells Zsh to not output the new line character at the end of the string, which keeps the prompt segments on the same row.

#### Set the background and foreground colors

These set ANSI escape sequences to use certain colors, which is why you might want to set a different color for the freeCodeCamp green, eg “cyan,” to differentiate it from the green used for other purposes in the terminal.

> **ANSI escape sequences** are a standard for [in-band signaling](https://en.wikipedia.org/wiki/In-band_signaling) to control the cursor location, color, and other options on video [text terminals](https://en.wikipedia.org/wiki/Text_terminal). Certain sequences of [bytes](https://en.wikipedia.org/wiki/Byte), most starting with [Esc](https://en.wikipedia.org/wiki/Escape_character) and ‘[[](https://en.wikipedia.org/wiki/Bracket)‘, are embedded into the text, which the terminal looks for and interprets as commands, not as [character codes](https://en.wikipedia.org/wiki/Character_encoding).  
>  — [ANSI Escape Code | Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code)

#### Programming language prompt sections

Another idea for prompt sections is to base them on a programming language you use. For more on how to create them for languages, such as JavaScript, Python and Ruby check out [Powerlevel9k: personalise your prompt for any programming language](https://medium.com/the-code-review/powerlevel9k-personalise-your-prompt-for-any-programming-language-68974c127c63).

![Image](https://cdn-media-1.freecodecamp.org/images/Gy9iZlkWW8Zrs8O52ekrveRqN1KQU64bfhWA)

### The complete .zshrc

This is the entire configuration for `~/.zshrc` after following this tutorial. You can use it as a basis for creating your custom setup.

```
# Customise the Powerlevel9k promptsPOWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(  custom_medium custom_freecodecamp dir vcs newline status)POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()POWERLEVEL9K_PROMPT_ADD_NEWLINE=true
```

```
# Add the custom Medium M icon prompt segmentPOWERLEVEL9K_CUSTOM_MEDIUM="echo -n $'\uF859'"POWERLEVEL9K_CUSTOM_MEDIUM_FOREGROUND="black"POWERLEVEL9K_CUSTOM_MEDIUM_BACKGROUND="white"
```

```
# Add the custom freeCodeCamp prompt segmentPOWERLEVEL9K_CUSTOM_FREECODECAMP="echo -n $'\uE242' freeCodeCamp"POWERLEVEL9K_CUSTOM_FREECODECAMP_FOREGROUND="white"POWERLEVEL9K_CUSTOM_FREECODECAMP_BACKGROUND="cyan"
```

```
# Load Nerd Fonts with Powerlevel9k theme for ZshPOWERLEVEL9K_MODE='nerdfont-complete'
```

```
source ~/powerlevel9k/powerlevel9k.zsh-theme
```

### Some bonus options to try

You can also add this to your .zshrc to configure iTerm2’s tab title text and background color.

```
# Set a color for iTerm2 tab title background using rgb valuesfunction title_background_color {  echo -ne "\033]6;1;bg;red;brightness;$ITERM2_TITLE_BACKGROUND_RED\a"  echo -ne "\033]6;1;bg;green;brightness;$ITERM2_TITLE_BACKGROUND_GREEN\a"  echo -ne "\033]6;1;bg;blue;brightness;$ITERM2_TITLE_BACKGROUND_BLUE\a"}
```

```
ITERM2_TITLE_BACKGROUND_RED="18"ITERM2_TITLE_BACKGROUND_GREEN="26"ITERM2_TITLE_BACKGROUND_BLUE="33"
```

```
title_background_color
```

```
# Set iTerm2 tab title textfunction title_text {    echo -ne "\033]0;"$*"\007"}
```

```
title_text freeCodeCamp
```

Below is a terminal styled with the [Dracula](https://draculatheme.com/iterm/) color scheme, the [chruby Powerlevel9k prompt segment](https://github.com/bhilburn/powerlevel9k#chruby) to show the Ruby version, as well as [the Ruby gems artii, lolcat and colorls to add more colored output to the terminal](https://medium.freecodecamp.org/lolcat-colorls-catpix-and-other-ruby-gems-to-add-color-to-your-terminal-16f4d9499ac7) — just a few of the possible other ideas to try.

![Image](https://cdn-media-1.freecodecamp.org/images/beh2vvFJN-yUmHhMfpCj3WtlcnlI8vTDzj4L)

### Find out more

There are many other options that you can checkout on the Powerlevel9k page for [Stylizing Your Prompt](https://github.com/bhilburn/powerlevel9k/wiki/Stylizing-Your-Prompt). For more on custom prompt segments, check out [Powerlevel9k: Custom Command](https://github.com/bhilburn/powerlevel9k#custom_command).

If you are proud of you configuration, some people share theirs online, such as at [Show-Off-Your-Config](https://github.com/bhilburn/powerlevel9k/wiki/Show-Off-Your-Config).

**_Changed your mind?_** You can always remove this theme and go back to the default settings. Check out this guide that explains how you can do this step-by-step.

* [Back to Bash: Remove Zsh and terminal themes on a Mac step-by-step](https://medium.com/the-code-review/back-to-bash-remove-zsh-and-terminal-themes-on-a-mac-step-by-step-f89f69d2ec73)

#### Read more from [ryanwhocodes](https://www.freecodecamp.org/news/how-you-can-style-your-terminal-like-medium-freecodecamp-or-any-way-you-want-f499234d48bc/undefined)

* [Powerlevel9k: personalise your prompt for any programming language](https://medium.com/the-code-review/powerlevel9k-personalise-your-prompt-for-any-programming-language-68974c127c63)
* [Nerd Fonts: How to install, configure, and remove programming fonts on a mac](https://medium.com/the-code-review/nerd-fonts-how-to-install-configure-and-remove-programming-fonts-on-a-mac-178833b9daf3)
* [Lolcat, Colorls, Catpix, and other Ruby Gems to add color to your terminal](https://medium.freecodecamp.org/lolcat-colorls-catpix-and-other-ruby-gems-to-add-color-to-your-terminal-16f4d9499ac7)
* [Top 10 Bash file system commands you can’t live without](https://medium.com/@RyanDavidson/top-10-bash-file-system-commands-you-cant-live-without-4cd937bd7df1)


---
title: Lolcat, Colorls, Catpix, and other Ruby Gems to add color to your terminal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-20T20:43:09.000Z'
originalURL: https://freecodecamp.org/news/lolcat-colorls-catpix-and-other-ruby-gems-to-add-color-to-your-terminal-16f4d9499ac7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U5qJqhlGM-xDL18zyKz0Sg.png
tags:
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'As well as making your terminal more colorful and productive through the
  prompt theme, font, and plugins, you can add even more features by using Ruby Gems,
  such as lolcat, colorls, and catpix.

  To use them, ensure you have Ruby installed on your comp...'
---

As well as making your [terminal more colorful and productive through the prompt theme, font, and plugins](https://hackernoon.com/make-your-terminal-more-colourful-and-productive-with-iterm2-and-zsh-11b91607b98c), you can add even more features by using [Ruby](https://www.ruby-lang.org/en/) Gems, such as lolcat, colorls, and catpix.

To use them, ensure you have Ruby installed on your computer, and then you can install each one using the command `gem install <GEM_NA`ME>.

### [lolcat](https://github.com/busyloop/lolcat)

This Gem adds a rainbow gradient to anything that you pipe through to it. The image at the top of the post pipes ASCII art text generated with the [aarti Gem](https://github.com/miketierney/artii) through lolcat to create a colorful heading in the terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/ZwzujfO4aOxwBN3avPlNgnXSGBmxUAqV1f6v)

You can combine extra bash commands to animate it, in this case `echo` to print the string passed to it, `-a` to animate, and `-d` for duration.

```
echo I ❤  Ruby | lolcat -a -d 500
```

![Image](https://cdn-media-1.freecodecamp.org/images/8lb5t0cCU554GFCZcVe91P7uVNPPpVgOoUxr)

There is a Gem based on lolcat called [lolize](https://github.com/miaout17/lolize), which adds the rainbow colour to Ruby output. One use of it is to generate more colourful logs for your [Ruby on Rails](https://rubyonrails.org/) projects.

![Image](https://cdn-media-1.freecodecamp.org/images/pKwAQSBPggUMey2gLt7spU2vBsvgGbxTtcDQ)
_The lolize Gem in action coloring Ruby on Rails logs_

### [Artii](https://github.com/miketierney/artii)

The Artii gem generates ASCII art based on text you pass to it as arguments. You can see this demonstrated in the header image at the top of this tutorial. If you pass the output to lolcat you get ascii art text with multiple colors.

```
artii 'Ruby Gems' --font slant | lolcat
```

It is based on the [Figlet](http://www.figlet.org/) library, which you can also install on a Mac with `brew install figlet`.

### [Colorls](https://github.com/athityakumar/colorls)

This enhances the terminal command `[ls](https://en.wikipedia.org/wiki/Ls)` with color and icons. Below is a screenshot from its [Github repo](https://github.com/athityakumar/colorls). This configuration is an [iTerm2](https://www.iterm2.com/) terminal (Mac OS), with `[oh-my-zsh](http://ohmyz.sh/)` with `[powerlevel9k](https://github.com/bhilburn/powerlevel9k)` theme and `powerline [nerd-font](https://github.com/ryanoasis/nerd-fonts) + awesome-config` font with the `Solarized Dark` color theme.

![Image](https://cdn-media-1.freecodecamp.org/images/de2yPYFDVt2GAKcxSJNKV0vDjSjb9VWe7OfW)

You can make it as easy to use as `ls` by adding an alias for `lc` to your `~/.bashrc` or `~/.zshrc` file.

```
alias lc="colorls"
```

### [Catpix](https://github.com/pazdera/catpix)

This converts images to a format that can render on a terminal screen. You can try having an image loaded into your terminal when it starts or when there is an event — for example when your tests pass.

![Image](https://cdn-media-1.freecodecamp.org/images/GX76uyNuda8nxxdfB-L5WLcjosfmmyjkcVh1)

### Find out more

These are just some of the Ruby Gems that can enhance your terminal, and learning how they work means you can customize your command line. You could even take it further by adding a special setup for [irb](http://ruby-doc.org/stdlib-2.0.0/libdoc/irb/rdoc/IRB.html) and [pry](https://github.com/pry/pry/wiki/Customization-and-configuration), such as [irbtools](https://github.com/janlelis/irbtools).

#### Find out more about the Gems on Github

* [lolcat](https://github.com/busyloop/lolcat)
* [lolize](https://github.com/miaout17/lolize)
* [colorls](https://github.com/athityakumar/colorls)
* [catpix](https://github.com/pazdera/catpix)
* [artii](https://github.com/miketierney/artii)

#### Read more from [ryanwhocodes](https://www.freecodecamp.org/news/lolcat-colorls-catpix-and-other-ruby-gems-to-add-color-to-your-terminal-16f4d9499ac7/undefined)

* [Make your terminal more colourful and productive with iTerm2 and Zsh!](https://medium.com/the-code-review/make-your-terminal-more-colourful-and-productive-with-iterm2-and-zsh-11b91607b98c)
* [Powerlevel9k: personalise your prompt for any programming language](https://medium.com/the-code-review/powerlevel9k-personalise-your-prompt-for-any-programming-language-68974c127c63)
* [Top 10 Bash file system commands you can’t live without](https://medium.com/the-code-review/top-10-bash-file-system-commands-you-cant-live-without-4cd937bd7df1)
* [How you can add Bootstrap to your Ruby on Rails project](https://medium.freecodecamp.org/add-bootstrap-to-your-ruby-on-rails-project-8d76d70d0e3b)


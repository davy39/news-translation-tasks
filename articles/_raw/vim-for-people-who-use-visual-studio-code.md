---
title: An Intro to Vim for People Who Use Visual Studio Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-24T17:55:14.000Z'
originalURL: https://freecodecamp.org/news/vim-for-people-who-use-visual-studio-code
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/vimvsvscode.png
tags:
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: vim
  slug: vim
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jared Nutt

  Hot tips to bring the awesomeness of Visual Studio Code to Vim.

  Front-Matter

  I want to start by saying, this is not an editor-shame article. You can use whatever
  text editor you want. It really doesn’t matter. I’m only writing this beca...'
---

By Jared Nutt

Hot tips to bring the awesomeness of Visual Studio Code to Vim.

### Front-Matter

I want to start by saying, this is not an editor-shame article. You can use whatever text editor you want. It really doesn’t matter. I’m only writing this because I found a level of productivity in Vim that I haven’t had in any of the editors I used before (Sublime Text, Atom or VSCode).

If you’ve heard about Vim, and want to try it out, I hope this article can provide a bit of familiarity you’d find from VSCode.

<figure class="kg-card kg-image-card" style="text-align: center;">
    <iframe src="https://giphy.com/embed/5b26kbDYzsqGartaXz" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</figure>

### Why Vim?

There are lots of reasons to use Vim, so here’s a few of mine.

#### Keep your hands at 10 and 2

<figure class="kg-card kg-image-card" style="text-align: center;">
    <iframe src="https://giphy.com/embed/11Qm8y698eYC8U" width="480" height="198" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</figure>

When you are solely using the keyboard, there is going to be an inherent speed boost just from not having to physically move your hands. And hey, maybe you’re a black belt in mouse movement, and you can move back in forth with a speed invisible to the naked eye. For the rest of us simple humans, it takes time.

Let’s do some quick math.

<figure class="kg-card kg-image-card" style="text-align: center;">
    <iframe src="https://giphy.com/embed/Fh28yu3oxWRlm" width="480" height="210" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</figure>

It takes 600ms to move my hand from the “home keys” to the mouse. On average, for sake of argument, I do that once a minute while I’m writing [code](https://www.java67.com/2018/06/21-websites-to-learn-how-to-code-for.html). Whether that be to scroll, navigate to a new file, or something similar.

600 (wasted time in ms) x 60 (times per hour) x 5 (hours I am actually coding) = 180,000ms wasted =

> 3. Minutes. Every. Day.

Yeah, okay, maybe that doesn’t sound so bad, but, those 3 minutes could be spent writing a function, or [refactoring code](http://www.java67.com/2016/02/5-books-to-improve-coding-skills-of.html), not flailing your hand about like you're Harry Potter!

#### Speed

<figure class="kg-card kg-image-card kg-card-hascaption" style="text-align: center;">
    <iframe src="https://giphy.com/embed/4wEFKQgMGLlqU" width="480" height="264" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
    <figcaption>Okay, so maybe 65 isn’t really that fast anymore, but hey, this was 1994!</figcaption>
</figure>

My favorite quote that describes what it’s like to code in VIM:

> “Code at the speed of thought”

Vim is built around the idea that you are directly communicating with your computer. You tell it what you want, and it does it for you. The biggest eye-opener for me was this little tidbit:

To delete everything in between two objects (parentheses, quotes, etc), it's as simple as:

`di'`

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Hnet.com-image.gif)
_Computer: Delete, inside, single-quotes._

That’s just the surface of amazing shorthand things you can do with Vim.

#### I’m a real programmer!

<figure class="kg-card kg-image-card" style="text-align: center;">
    <iframe src="https://giphy.com/embed/v5OtzSjwSu3w4" width="480" height="240" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</figure>

Part of the journey of learning VIM is exposing yourself to how UNIX works. I’m under the impression that the more you expose yourself to things like bash, the [better programmer](https://javarevisited.blogspot.com/2014/01/10-tips-to-improve-programming-skill-become-better-programmer.html) you are going to be.

Chances are, you have a pretty sweet command line setup. Wouldn’t it be nice if your code editor and your command line worked in concert?

#### How do you exit Vim?

Probability is high that you’ve ever edited a file on a Linux server, and couldn’t figure out how to exit the file. Let’s say, for example, changing an SSH key on Digital Ocean. If you know VIM…you don’t have to worry about that!

#### The real reason I switched to Vim

Honesty time. The real catalyst for wanting to switch to Vim was watching Kyle Mathews (creator of Gatsby.js) using it during a demo.

<figure class="kg-card kg-image-card kg-card-hascaption" style="text-align: center;">
    <iframe src="https://giphy.com/embed/UUypRspZCaF94uKasd" width="480" height="269" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
    <figcaption>Ya caught me.</figcaption>
</figure>

### VS Code Features and their equivalents

Convinced? Cool, here’s some tools!

#### Plugin System

Vim by itself is pretty barebones. In order to add plugins, we have to have a mechanism to manage them. Enter Plug:

[**junegunn/vim-plug**](https://github.com/junegunn/vim-plug)

> Note: There are a few plugin managers out there. I landed on Plug for no particular reason. I like it, and I’ve had no issues with it. FYI, Vundle is deprecated.

#### File Search

There has been a bunch of solutions for file searching over the years, as indicated by the multitude of answers in forums. I tried a couple of different ones, but landed on this combination:

[Fuzzy Finder(fzf)](https://github.com/junegunn/fzf) + [Ripgre](https://github.com/BurntSushi/ripgrep)p

![Image](https://www.freecodecamp.org/news/content/images/2019/09/fzf.gif)
_Fuzzy search for "theme"_

Fzf is a really well built/maintained fuzzy search that works in both the command line and vim.

> Note: You may see Ag(Silver searcher) in a lot of articles, however the Ag related vim plugin is no longer maintained, so it's suggested to use RipGrep.

#### Intellisense

The auto-completion system (Intellisense) in VSCode is arguably its best feature. Lucky for us, it’s been ported over to Vim!

[**neoclide/coc.nvim**](https://github.com/neoclide/coc.nvim)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/CoC.gif)
_autocompletion for importing a function written in another file in React_

CoC has its own extension system, that mirrors that of VSCodes. It's easy to use and well-documented (the most important part).

> Note: You may see some old articles talking about YouCompleteMe, but as far as I can tell, that isn’t maintained anymore.

#### File System Explorer

VSCode, like most modern text editors, comes with a file explorer. Vim’s native `netrw` is alright, and I’ve seen quite a few articles saying you don’t need anything else, like [here](https://shapeshed.com/vim-netrw/). However, I find NERDTree is too useful to not use.

[**scrooloose/nerdtree**](https://github.com/scrooloose/nerdtree)

#### Git integration

I gotta be honest here, I do most of my git stuff straight in Iterm. However, VSCode has an incredibly nice Git Diff split screen. To get that level of git integration, check out this plugin:

[**tpope/vim-fugitive**](https://github.com/tpope/vim-fugitive)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/gitdiff.gif)

### Additional plugins that you may want

This is some of the stuff I used in Visual Studio Code, that I wanted to bring into Vim.

#### Autocomplete Brackets

This nice little package will auto close those pesky brackets.

[**jiangmiao/auto-pairs**](https://github.com/jiangmiao/auto-pairs)

#### File Icons

This will add icons to stuff like NERDTree.

[**ryanoasis/vim-devicons**](https://github.com/ryanoasis/vim-devicons)

#### Prettier

Wouldn’t you know it, but the official prettier team has a vim plugin. How nice! Also, incredibly simple to set up.

[**prettier/vim-prettier**](https://github.com/prettier/vim-prettier)

Get it to work on autosave, check out [this article](https://www.dailysmarty.com/posts/how-to-setup-prettier-with-vim).

#### Snippets

Wouldn’t you know it, using the Conquer of Completion, you can import VSCode snippets!

Check this out to show you how to do that:

[**neoclide/coc.nvim**](https://github.com/neoclide/coc.nvim/wiki/Using-snippets)

Here is the React snippets package I’m using.

[**xabikos/vscode-react**](https://github.com/xabikos/vscode-react)

#### Additional Stuff

THE home for Vim plugins is Vim Awesome.

[**Vim Awesome**](https://vimawesome.com/)

Great place to watch people use Vim:

[**Vimcasts - Free screencasts about the text editor Vim**](http://vimcasts.org/)

### Dotfiles

I have a few remapped keys to make things easier. Check out my dotfiles for all those.

[**DarthOstrich/dotfiles**](https://github.com/DarthOstrich/dotfiles)

### Final Thoughts

#### My Journey

I solely use Vim now, after spending about a year to learn it. Initially, I was using it just for my personal projects, because my productivity level was low. I had to keep stopping to look up how to do something. However, I dropped VSCode completely about 4 months ago, and I don’t plan on going back.

#### It takes discipline

Learning Vim can seem daunting, and frankly, it is. It requires self-imposed discipline. However, doesn’t everything in development? There is no tool/language/framework I’ve ever learned that didn’t require some level of [deliberate practice](http://www.calnewport.com/blog/2011/12/28/how-i-used-deliberate-practice-to-destroy-my-computer-science-final/).

Vim is a lifestyle choice. It will take a while to get used to it, and it WILL be frustrating at times. However, if you stick to it, I guarantee it’ll improve your workflow. If you have any additional tips or questions, please drop them below. As always, happy coding!

<figure class="kg-card kg-image-card" style="text-align: center;">
    <iframe src="https://giphy.com/embed/hv4TC2Ide8rDoXy0iK" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</figure>

## Additional Resources for learning

[**Mastering Vim Quickly — Jovica Ilic**](https://jovicailic.org/mastering-vim-quickly/)

[**8 Vim Tricks That Will Take You From Beginner to Expert**](https://medium.com/swlh/8-vim-tricks-that-will-take-you-from-beginner-to-expert-817ff4870245)

## References

[**Switching to Vim**](http://brendandawes.com/blog/vim)

[**10 simple Linux tips which save 50% of my time in the command line**](https://dev.to/javinpaul/10-simple-linux-tips-which-save-50-of-my-time-in-the-command-line-4moo)

  


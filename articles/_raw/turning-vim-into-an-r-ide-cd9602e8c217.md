---
title: Turning Vim Into An R IDE
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-10T20:22:52.000Z'
originalURL: https://freecodecamp.org/news/turning-vim-into-an-r-ide-cd9602e8c217
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cRo1ybQbVMMbAHRjgUhXqg.png
tags:
- name: Data Science
  slug: data-science
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kade Killary

  Warning: No, this is not the R setup to use if you are a beginner. The RStudio IDE
  is amazing and should probably always be your default tool. However, if you happen
  to belong to the outcast realms of Vim / Emacs land, then this post ...'
---

By Kade Killary

_Warning_: **No**, this is not the R setup to use if you are a beginner. The [RStudio IDE](https://www.rstudio.com/products/RStudio/) is amazing and should probably always be your default tool. However, if you happen to belong to the outcast realms of [Vim](http://www.vim.org/) / [Emacs](https://www.gnu.org/software/emacs/) land, then this post might be for you. Also, I’m going to mention Vim and [Neovim](https://neovim.io/) throughout the post, at this point they are largely one in the same. So, if you are tied to one or the other it shouldn’t matter.

### Why Not Just Use RStudio?

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

A great question indeed. For me, the main reasons are speed and familiarity. Yes, I know RStudio has Vim keybindings, but it isn’t the _real_ thing. At this point, I’m ruined by Vim. A lone madman vigorously hitting `<e`sc>`; and` <C-f> in Microsoft Word only to be disappointed.

> However, all is not lost.

### R In Vim

At first, the pursuit of R in Vim seems like an exercise in brutalism. You’re options are few and support seems bleak.

Your best option will be to utilize a separate `:terminal` buffer. The basic workflow goes as follows:

* Write code in `myFile.R`
* Visually select code
* Paste code in `:terminal` buffer
* Execute code
* Rinse and repeat

This may not seem too bad, however it gets tedious fairly quickly. Plus, this approach leaves a lot to be desired. Mainly, viewing what’s defined, perusing the data, and some basic completion + linting.

### Nvim-R To The Rescue

[Nvim-R](https://github.com/jalvesaq/Nvim-R) is easily one of my favorite plugins for Vim. It takes an old water pistol and transforms it into a fully functioning machine gun. It comes stocked with many gems that will make you regret you haven’t been using it all along. So, enough with the poetic waxing. Let’s jump into making Vim our new R home.

The first step to R enlightenment is…you guessed it, installing [Nvim-R](https://github.com/jalvesaq/Nvim-R). I use [Vim-Plug](https://github.com/junegunn/vim-plug), so that’s what I show below. However, you can just as easily install it using whatever plugin manager you choose.

```
Plug 'jalvesaq/Nvim-R'
```

Now if you open an R file and hit `\rf` you’ll see a terminal buffer appear with an R console tied to your current session. To end it, hit `\rq`.

![Image](https://cdn-media-1.freecodecamp.org/images/dUyfYbzNF7juie4gwzaDMFl2roeFckvY1naV)
_R file + R console_

One important thing to note, the console is not tied to just the current buffer. This means that you can have multiple buffers all feeding into the same console. This can be good / bad depending on your personal preferences. I enjoy it, but it can definitely throw you for a loop if you’re careless. For a deeper dive on how R and Vim communicate in Nvim-R you can head [here](https://github.com/jalvesaq/Nvim-R).

### Secret Sauce

Now that you’ve got the basics up and running we can dive into all that Nvim-R has to offer. There are a vast amount of built-in shortcuts, for the full list you can read the documentation [here](https://github.com/jalvesaq/Nvim-R/blob/master/doc/Nvim-R.txt). I will briefly cover a handful of useful commands that will serve you well on a daily basis.

#### Sending Lines

The most immediate need is to be able to send lines of code. There are a variety of ways to do so in Nvim-R:

* Send :: Entire File `\aa`
* Send :: Entire Block `\bb`
* Send :: Entire Function `\ff`
* Send :: Entire Selection `\ss`
* Send :: Entire Line `\l`

As you can begin to see the forward slash `\` is the leader for many operations. However, most of these, and the minor distinctions between them, are superfluous. You will likely be better served by remapping a few of them.

```
" in your .vimrc /init.vim
```

```
“ remapping the basic :: send linenmap , <Plug>RDSendLine
```

```
“ remapping selection :: send multiple linesvmap , <Plug>RDSendSelection
```

```
“ remapping selection :: send multiple lines + echo linesvmap ,e <Plug>RESendSelection
```

I chose to remap the basic send line + multiple lines to my comma key. This significantly cuts down on the number of keys I have to utilize. Furthermore, the `,e` mapping allows me to check that the lines I sent were computed correctly. For the most part, these three mappings will allow you to do everything you need to. There are a few more worth mentioning though, and may add something to your workflow if remapped.

#### Object Browser

First up, the object browser. This feature, solicited by typing `\ro` will allow you to see what variables and libraries are active in your current environment.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Objects can also be viewed by typing `\rl`, which will run the `ls()` function in your current console.

#### Documentation

In order to get a better understanding of your code you have a couple options. From within Nvim-R there are two of particular note `\rh` — help and `\re` — example. Each of these will open in a split buffer with the relevant information.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Another worthwhile option is the [Dash plugin](https://github.com/rizzatti/dash.vim). The easiest path to usage is as follows:

```
“ install plugin :: using vim-plugPlug ‘rizzatti/dash.vim’
```

```
“ remap search keynmap <silent> <leader>d <Plug>DashSearch<CR>
```

Now, when you are seeking more information on a piece of R code, or any other language, all you have to do is place your key over the word and hit `<leade`r>d. The Dash app will then pop up with the relevant information. You can also search Google and Stack Overflow from within it. It’s a great tool, especially for Vimmers who utilize Vim for a variety of languages.

#### Viewing Data

Next up is getting a quick peak at your data. RStudio comes with a beautiful built in data viewer, which can be handy for getting a sense of the data. In Vim, it’s a little harder, but not impossible.

Nvim-R allows you to view a data frame by using the `\rv` command. This will either show the data frame using X Quartz, on Mac, or the [CSV plugin](https://github.com/chrisbra/csv.vim) for Vim, if you have it installed.

The CSV plugin comes with a whole host of additional features for manipulating data, but that is outside of the scope of this article. By and large, my suggestion would be to use Excel. While overly beloved by many, it does serve as a good data viewer.

### Other Tips & Tricks

Despite what you may think, there is still more, and even more that I won’t cover. But, these next few tricks are definitely worth keeping in mind.

#### Inline Code Output

If you have a line of code and hit `\o` you’ll see the output rendered as comments in your current file.

![Image](https://cdn-media-1.freecodecamp.org/images/EwV3DlUikbtra6tEpT0LIphRz2ji-XHUY3ai)

#### Functions

Instead of doing the basic flow of `str()` + `plot()`, etc…Nvim-R allows for a simplified flow.

* summary() :: `\rs`
* plot() :: `\rg`
* args() :: `\ra`
* setwd() :: `\rd`
* print() :: `\rp`
* names() :: `\rn`

#### Arrows

Arrows can be a pain to type. Luckily, Nvim-R makes it easier by mapping `_` to `&l`t;-. This may, or may not, completely bewilder you. If you’re someone who prefers snake case, then you’ll have to hit the underscore twice in order to get an actual underscore, and not an arrow. However, you can override this setting. I find it useful, and have adjusted, but can certainly understand others being irked.

### Completion

Often I see lack of code completion as a major reason people skip Vim. This notion is incorrect though. Code completion is very much apart of Vim. For our specific purpose, namely completion for R, there are, yet again, a few options.

#### Nvim-R Completion

Nvim-R supports code completion out of the box. You will have to manually engage it by using `<C-X>`;<C-O> for an obje`ct name, o`r <C-X><C-A> for a function argument. For some people this workflow is ideal, but in the current age of VS Code’s Intellisense, and other such options, this feels clunky.

#### Ncm-R

[Ncm-R](https://github.com/gaalcaras/ncm-R) is your best bet for as-you-type sort of completions. It’s a fairly new package, but a much welcomed addition. It integrates with Nvim-R to provide asynchronous completions for R via [nvim-completion-manager](https://github.com/roxma/nvim-completion-manager).

![Image](https://cdn-media-1.freecodecamp.org/images/nWIAYtf-zxwmjx7tXAJddKOyH1cIbjREXj1s)

Ncm-R provides rich completions for all of the following:

* Objects from the global R environment
* Functions from all loaded packages
* Packages inside `library()` and `require()`
* Datasets inside `data()`
* Arguments inside functions
* Variables inside pipes `%&g`t;% and ggplo`t`s +

For a basic set up add the code below to your Vim configuration file.

```
Plug ‘roxma/nvim-completion-manager’Plug ‘gaalcaras/ncm-R’
```

```
“ Optional: for snippet supportPlug ‘sirver/UltiSnips’
```

#### R Language Server

If you are unfamiliar with what a language server is head [here](https://github.com/Microsoft/language-server-protocol). If you are familiar, then [this project](https://github.com/REditorSupport/languageserver) may be of interest. It is still in the early days, and largely experimental, but does work and currently supports both code completion and linting.

### Linting

Last but not least, linting. The set up for quality linting is fairly straightforward. You’ll want to use [ALE](https://github.com/w0rp/ale), Asynchronous Lint Engine, as your driver. You can set this up in your .vimrc as follows:

```
Plug ‘w0rp/ale’
```

Now all you need to do is install [lintr](https://github.com/jimhester/lintr). This can be done by using `install.packages(‘lintr’)`.

Now, the next time you open up an .R file you should be good to go.

### Conclusion

At this point, you have a killer set up for R in Vim. There is certainly more to do though if you’re curious. Areas for further exploration include looking through all of the documentation in the plugins I have linked throughout this article. You’ll find many helpful tips and tricks in there, as well as useful settings. I hope this helped to get you up and running with R in Vim!

[**_For more about Vim head to my blog!_**](https://kadekillary.work/)

### Bonus Section

While I know I said you should explore on your own. It doesn't’ hurt to provide some additional settings that can make your life easier.

```
“ settings :: Nvim-R plugin
```

```
“ R output is highlighted with current colorschemelet g:rout_follow_colorscheme = 1
```

```
“ R commands in R output are highlightedlet g:Rout_more_colors = 1
```


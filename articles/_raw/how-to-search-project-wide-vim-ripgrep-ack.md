---
title: How I Made VIM's Project-wide Search Seamless with ripgrep
subtitle: ''
author: Rahul gupta
co_authors: []
series: null
date: '2020-06-08T16:57:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-search-project-wide-vim-ripgrep-ack
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/markus-winkler-afW1hht0NSs-unsplash--1-.jpg
tags:
- name: Productivity
  slug: productivity
- name: vim
  slug: vim
seo_title: null
seo_desc: 'Yes, I ditched grep & the_silver_searcher(ag) for ripgrep.

  Whether you''re forced to use VIM at your workplace or you''re a mad VIM fan like
  I am who obsesses about productivity, the project-wide keyword search is a basic
  requirement every developer ne...'
---

Yes, I ditched grep & the\_silver\_searcher(ag) for ripgrep.

Whether you're forced to use VIM at your workplace or you're a mad VIM fan like I am who obsesses about productivity, the project-wide keyword search is a basic requirement every developer needs in their editor's arsenal. And we expect it to be blazing fast. ⚡️

I've been using VIM for about 3 years now. And coming from a [Sublime](https://www.sublimetext.com/) background, the need for project-wide search was essential.

[ripgrep](https://github.com/BurntSushi/ripgrep) and [a](https://github.com/mileszs/ack.vim)ck.vim were things I adopted early on after my unfulfilling experiences with grep and the\_silver\_searcher(ag). I haven't looked back since then.

This article is the result of experimenting with different search tools and incremental improvements I made over a period of time until it felt just right.

## Why ack.vim & ripgrep?

1. **Fast:** I've worked on Symfony and JavaScript projects with thousands of files and it is just blazing fast. Here's a quick [comparison](https://github.com/BurntSushi/ripgrep#quick-examples-comparing-tools) with other search tools.  
    My benchmark for speed is, "it should never feel slow". I noticed a tremendous improvement after I moved from grep, the\_silver\_searcher and ack.
    
2. **Quick navigation**: ack.vim takes care of populating the Quickfix list, which lets you conveniently move through all those search results across different files.
    
3. **Sensible defaults:** ripgrep by default considers gitignore and automatically skips hidden files/directories and binary files.
    

## Overview

**ack.vim** is a VIM plugin that acts as a wrapper to search keywords and populate the Quickfix list for navigating the results.

**ripgrep (rg)** is a command-line tool that ack.vim will internally use to perform the actual project-wide search.

## Steps

### **Step 1**: Install ripgrep

If you prefer [Homebrew](https://brew.sh/) like I do, run the following to install rg:

```bash
brew tap burntsushi/ripgrep https://github.com/BurntSushi/ripgrep.git
brew install burntsushi/ripgrep/ripgrep-bin
```

Here's an [automated script](https://gist.github.com/PezCoder/72ba0f5eba3ca5dc7271bde1a1fcfe5e) which I use as part of my [dotfiles](https://github.com/pezcoder/dotfiles).

If you prefer any other mode of installation, refer to ripgrep's official [installation](https://github.com/BurntSushi/ripgrep#installation) section.

### **Step 2**: Install ack.vim

To install ack.vim using the [vim-plug](https://github.com/junegunn/vim-plug) package manager, add the following in your vimrc:

```plaintext
Plug 'mileszs/ack.vim'
```

or refer to the ack.vim's [installation](https://github.com/mileszs/ack.vim#installation) section.

### **Step 3**: Configure ack.vim to use rg

Add the following configuration in your vimrc:

```plaintext
" ack.vim --- {{{

" Use ripgrep for searching ⚡️
" Options include:
" --vimgrep -> Needed to parse the rg response properly for ack.vim
" --type-not sql -> Avoid huge sql file dumps as it slows down the search
" --smart-case -> Search case insensitive if all lowercase pattern, Search case sensitively otherwise
let g:ackprg = 'rg --vimgrep --type-not sql --smart-case'

" Auto close the Quickfix list after pressing '<enter>' on a list item
let g:ack_autoclose = 1

" Any empty ack search will search for the work the cursor is on
let g:ack_use_cword_for_empty_search = 1

" Don't jump to first match
cnoreabbrev Ack Ack!

" Maps <leader>/ so we're ready to type the search keyword
nnoremap <Leader>/ :Ack!<Space>
" }}}

" Navigate quickfix list with ease
nnoremap <silent> [q :cprevious<CR>
nnoremap <silent> ]q :cnext<CR>
```

Note: `let g:ackprg` defines the command which ack.vim will internally run.  
Also note that we're using `rg` here with some options. Look at the `man rg` to modify the options that may meet your requirements.

To explore options for ack.vim, look into the following [documentation](https://github.com/mileszs/ack.vim/blob/master/doc/ack.txt).

## Usage

Now that we're up and ready, here are the most common use-cases:

### Look for a word under the cursor

*Press / followed by enter*.  
Since we've set `let g:ack_use_cword_for_empty_search = 1`, Ack falls back to the current word under the cursor for the search, so no need to type that word.

### Word search

*Press / followed by the word (without any quotes) & enter.*  
Since we're using smart case with ripgrep, that'll do a case insensitive search if the word is all lowercase, and a case sensitive search otherwise.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-04-at-3.33.02-AM-1.png align="left")

*word search with ack.vim*

### Regex search

*Press / followed by a regex pattern in quotes & enter.*

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-04-at-3.38.21-AM.png align="left")

*regex search with ack.vim*

### Navigation through the results

Ack.vim populates the results in the Quickfix list, which opens up as a separate bottom window. There are multiple ways to navigate the results list:

* You can navigate the Quickfix list using `j/k` and press `enter` to close the Quickfix list. VIM will take you to the exact location of the found word.
    
* You can also use the hotkeys `]q` or `[q`. VIM will move the cursor to the next/previous result and will open the file in a new buffer if required.  
    To close the Quickfix list once you're done, you can either go to the bottom Quickfix window and close it or just run `:cclose`
    
* To open the Quickfix list back up, run `:copen`
    

## Closing Note

And there you have it, a seamless search and navigation for your next project-wide keyword search!

If you're stuck anywhere, look for the respective ack.vim and ripgrep docs/issues in their respective repositories, or send me a message. Share the configuration you're proud of, so it can help others improve theirs.

Here are my [dotfiles](https://github.com/pezcoder/dotfiles).

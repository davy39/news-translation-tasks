---
title: Make Your Vim Smarter Using Ctrlp and Ctags
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-09T21:59:53.000Z'
originalURL: https://freecodecamp.org/news/make-your-vim-smarter-using-ctrlp-and-ctags-846fc12178a4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-DMqWWZ_btpEiyNgKpc8NQ.gif
tags:
- name: Ctrlp
  slug: ctrlp
- name: ctags
  slug: ctags
- name: JavaScript
  slug: javascript
- name: Software Engineering
  slug: software-engineering
- name: vim
  slug: vim
seo_title: null
seo_desc: 'By _haochuan

  I absolutely love Vim, and I use Vim for all my coding and writing from year to
  year. Although more are more people, especially for those are working with JavaScript,
  prefer modern code editors such as Sublime Text or VSCode, I’d rather ...'
---

By _haochuan

I absolutely love Vim, and I use Vim for all my coding and writing from year to year. Although more are more people, especially for those are working with JavaScript, prefer modern code editors such as Sublime Text or VSCode, I’d rather spend a little time trying to make my toy more intelligent.

### [CtrlP](https://github.com/ctrlpvim/ctrlp.vim)

If you are a Sublime Text, Atom, or VSCode guy, you must use `ctrl + p` thousands of times to improve productivity. Well, don’t be jealous if you are a Vim guy because this fancy Vim plugin CtrlP will give you all you need.  
Check this [official doc](http://ctrlpvim.github.io/ctrlp.vim/) for installation and setup.

![Image](https://cdn-media-1.freecodecamp.org/images/xakiKSsq2OC4UyFPHEszv9x5Qr96KNHcbRXy)

### [Ctags](http://ctags.sourceforge.net/)

Ctags is a tool that will sift through your code, indexing methods, classes, variables, and other identifiers, storing the index in a tags file. The tags file contains a single tag per line. Depending on command line arguments and the language ctags is run against, a lot of information can be obtained from this index.

Ctags currently supports [41 programming languages](http://ctags.sourceforge.net/languages.html), and it’s relatively easy to add definitions for more.

Ctags makes it much easier to navigate a larger project, particularly if the code you’re working with is unfamiliar. If you’re unsure of what a method does or how it’s supposed to be called, you can jump straight to its definition. If you’re in the downward spiral of a 500+ line Perl script and want to know where a variable was defined three hours ago, you can jump right back to it. And afterward, you can jump right back to where you were working.

You can install Ctags using Homebrew in OSX:

```bash
brew install ctags
```

Please note that OS X comes with a Ctags executable, but it’s not exuberant-Ctags and is missing most of the useful features. If you see an error like `Invalid Parameter` when you run `ctags`, it means that the system is not using the one you installed with Homebrew. To solve this:

```bash
$ alias ctags="`brew --prefix`/bin/ctags"
```

When you’re sitting in the directory you want to index, just run:

```bash
ctags -R.
```

Ctags will walk through the directory recursively, tagging all source files it encounters. For very large projects, this might take a while, but normally it’s pretty fast.

You may also need some extra config for Ctags, below is the `~/.ctags` I'm using:

```
--langmap=javascript:.js.es6.es.jsx
--javascript-kinds=-c-f-m-p-v

--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([A-Za-z0-9_$]+)[ \t]*=[ \t]*\[/\2/A,Array,Arrays/

--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([A-Z][A-Za-z0-9_$]+)[ \t]*=[ \t]*function/\2/C,Class,Classes/
--regex-javascript=/^[ \t]*class[ \t]+([A-Za-z0-9_$]+)/\1/C,Class,Classes/

--regex-javascript=/^[ \t]*export[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\3/E,Export,Exports/
--regex-javascript=/^[ \t]*export[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\5/E,export,Exports/
--regex-javascript=/^[ \t]*export[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\7/E,Export,Exports/
--regex-javascript=/^[ \t]*export[ \t]?(var|let|const)[ \t]+([A_Za-z0-9_$]+)/\2/E,Export,Exports/
--regex-javascript=/^[ \t]*export[ \t]?(var|let|const)[ \t]+([A_Za-z0-9_$]+)[ \t]*[^,]+,[ \t]*([A_Za-z0-9_$]+)/\3/E,Export,Exports/
--regex-javascript=/^[ \t]*export[ \t]?(var|let|const)[ \t]+([A_Za-z0-9_$]+)[ \t]*[^,]+,[ \t]*([A_Za-z0-9_$]+)[ \t]*[^,]+,[ \t]*([A_Za-z0-9_$]+)/\4/E,Export,Exports/

--regex-javascript=/^[ \t]*function[ \t]*([A-Za-z0-9_$]+)[ \t\(]/\1/F,Function,Functions/
--regex-javascript=/^[ \t]*[\(]function[ \t]*([A-Za-z0-9_$]+)[ \t\(]/\1/F,Function,Functions/
--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([a-z][A-Za-z0-9_$]+)[ \t]*=[ \t]*function[^\*][^\*]/\2/F,Function,Functions/
--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([a-z][A-Za-z0-9_$]+)[ \t]*=[ \t]*\([^\*]/\2/F,Function,Functions/

--regex-javascript=/^[ \t]*function[ \t]*\*[ \t]*([A-Za-z0-9_$]+)/\1/G,Generator,Generators/
--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([a-z][A-Za-z0-9_$]+)[ \t]*=[ \t]*function([ \t]*\*)/\2/G,Generator,Genrators/
--regex-javascript=/^[ \t]*(\*[ \t])([A-Za-z0-9_$]+)[ \t]*\(.*\)[ \t]*{/\2/G,Generator,Generators/

--regex-javascript=/^[ \t]*import[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\3/I,Import,Imports/
--regex-javascript=/^[ \t]*import[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\5/I,Import,Imports/
--regex-javascript=/^[ \t]*import[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\7/I,Import,Imports/

--regex-javascript=/^[ \t]*this\.([A-Za-z0-9_$]+)[ \t]*=.*{$/\1/M,Method,Methods/
--regex-javascript=/^[ \t]*([A-Za-z0-9_$]+)[ \t]*[:=][ \t]*[\(]*function[ \t]*\(/\1/M,Method,Methods/
--regex-javascript=/^[ \t]*static[ \t]+([A-Za-z0-9_$]+)[ \t]*\(/\1/M,Method,Methods/
--regex-javascript=/^[ \t]*([A-Za-z0-9_$]+)\(.*\)[ \t]*{/\1/M,Method,Methods/

--regex-javascript=/^[ \t]*(this\.)*([A-Za-z0-9_$]+)[ \t]*[:=].*[,;]*[^{]$/\2/P,Property,Properties/

--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([A-Za-z0-9_$]+)[ \t]*=[ \t]*{/\2/O,Object,Objects/

--regex-javascript=/\/\/[ \t]*(FIXME|TODO|BUG|NOBUG|\?\?\?|\!\!\!|HACK|XXX)[ \t]*\:*(.*)/\1/T,Tag,Tags/

--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([A-Za-z0-9_$]+)[ \t]*=[ \t]*[^\[{]*;$/\2/V,Variable,Variables/

--exclude=min
--exclude=vendor
--exclude=\*.min.\*
--exclude=\*.map
--exclude=\*.swp
--exclude=\*.bak
--exclude=tags
--exclude=node_modules
--exclude=bower_components
--exclude=test
--exclude=__test__
--exclude=build
--exclude=dist
--exclude=*.bundle.*
```

Here is how it looks like going to function definition:

![Image](https://cdn-media-1.freecodecamp.org/images/DSIuLEu-PDITYUoQVBxz7UJAklOA5DBgKKKO)

Also you can use Ctrlp to search for tags instead of files. To do this, first you need to map a shortcut in your `.vimrc`:

```
nnoremap <leader>. :CtrlPTag<cr>
```

Here is how it works:

![Image](https://cdn-media-1.freecodecamp.org/images/4RHDaqFDwqBHZSKKegGHckqoSlAa6eBJ0bkz)

Hope it helps :)

I write code for audio and web, and play guitar on YouTube. If you want to see more stuff from me or know more about me, you can always find me in:

Website:  
[https://haochuan.io/](https://haochuan.io/)

GitHub:  
[https://github.com/haochuan](https://github.com/haochuan)

Medium:  
[https://medium.com/@haochuan](https://medium.com/@haochuan)

YouTube: [https://www.youtube.com/channel/UCNESazgvF_NtDAOJrJMNw0g](https://www.youtube.com/channel/UCNESazgvF_NtDAOJrJMNw0g)


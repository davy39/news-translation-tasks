---
title: A guide to modern Web Development with (Neo)vim
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T16:25:42.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-modern-web-development-with-neo-vim-333f7efbf8e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VwtBkUpu7nSToAEP8N2IOQ.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: vim
  slug: vim
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Caleb Taylor

  There are a lot of great editors out there that provide a ton of features for web
  development. Recreating those features in Vim has always been a challenge. I love
  Vim, but I’ve also dedicated a ton of time to tweaking my setup. This ...'
---

By Caleb Taylor

There are a lot of great editors out there that provide a ton of features for web development. Recreating those features in Vim has always been a challenge. I love Vim, but I’ve also dedicated a **_ton_** of time to tweaking my setup. This article is a summary of the result of my work.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VwtBkUpu7nSToAEP8N2IOQ.png)
_Jarvis in action_

I use [coc.nvim](https://github.com/neoclide/coc.nvim) and [denite](https://github.com/Shougo/denite.nvim) to power my coding experience. Denite is used to fuzzy find files, manage open files, and search your project. Coc.nvim drives the [intellisense](https://docs.microsoft.com/en-us/visualstudio/ide/using-intellisense?view=vs-2019) engine by wrapping many of the same core extensions that drive the [VSCode IDE](https://code.visualstudio.com/). For my full setup, including how I configure these plugins and more, check out [my dotfiles](https://github.com/ctaylo21/jarvis).

> **Note**: I’ll just reference Vim in this article, but I actually use [Neovim](https://neovim.io/). The plugins all work with Vim as well — depending on the version — but things like the “floating window” feature will be specific to Neovim.

### **Intro**

I write TypeScript/JavaScript on a daily basis, and I know how stark the difference is between Vim and an editor like VSCode out of the box. There are many features available in modern editors that take time, expertise, and/or plugins to achieve in Vim.

I’ve created the following list of features that I expect out of a modern editor. Standard editor features (like syntax highlighting) aren’t included.

1. **Fuzzy File Finding** — If you know the file name in the project, you should be able to open it quickly (such as — two keystrokes + minimum number of characters to unique filename).
2. **File Switching** — You should be able to see open files, and quickly switch between open files, both with fuzzy finding and manual browsing.
3. **Linting** — Code linting should be automatic and fast**,** and you should be able to use a code fixer.
4. **Project Searching** — You should be able to search for an arbitrary string, search for a symbol, find definitions, and find usages of a symbol.
5. **Code Intellisense** — Having your IDE provide relevant, seamless suggestions and auto-completions can be a huge boost to productivity. In my opinion, the “white whale” for most Vim users.

Getting all of these things working in Vim can be a pain. There are tons of plugins to choose from, configurations to tweak, and docs to read. After 7 years of trial and error, I’ve finally got my setup to a great place. The best part?

**I’m going to show you how to get all of the core functionality with just two plugins.**

I won’t be covering every feature of these awesome plugins, or listing all the possible alternatives (and there are a lot of great ones). I will focus on highlighting the core functionality I use, as well as any mappings or configurations I use to elevate the experience.

So without further ado, let’s get to it.

### **Denite**

**What you get:** Fuzzy file finding, file management, project searching

I’m not going to lie, [Denite](https://github.com/Shougo/denite.nvim) is pretty insane. Just take a look at [the docs](https://github.com/Shougo/denite.nvim/blob/master/doc/denite.txt). At a basic level, it provides a fuzzy-finding layer on top of a bunch of core functionality. It was built by the legendary [Shougo](https://github.com/Shougo), a Jedi master of Vim.

Denite is built on [lambdalisue/neovim-prompt](https://github.com/lambdalisue/neovim-prompt). It has a full-featured interface that can take a while to get used to. You can create custom menus, and use many custom sources with Denite as a layer on top.

#### **Basics**

I primarily use [Denite](https://github.com/Shougo/denite.nvim) for finding files in my project, and managing my open files. I have configured Denite to use [ripgrep](https://github.com/BurntSushi/ripgrep) to power my searching. You can see [how I’ve configured](https://github.com/ctaylo21/jarvis/blob/master/config/nvim/init.vim#L58) it in my setup.

I have all of key features mapped for quick and easy access. The keys I use for these mappings are just personal preference, and should be customized per user. I use the “floating window” option for my Denite mappings, but other variations are supported as well (like horizontal/vertical splits).

#### **Managing Open Files**

`;` brings up a list of currently open files. You can start typing and it will allow you to fuzzy-search through your current open files. With the file list open,`<ctr`l>o lets you browse the list like you a`re in` normal mode, where you can open and/or delete any files from the list.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oVQVFnE9i41t_tmK9chiUQ.gif)
_Managing open buffers with Denite_

#### **Fuzzy Finding Files**

`<leade`r>t fuzzy-searches files in the current directory. With ripgrep, any files in `your .git`ignore are also ignored.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YiZ9RVBkO1xunJW8V3_DoQ.gif)
_Fuzzy-finding files in the current directory_

#### **Project Searching**

`<leade`r>`g and <`;leader>j search the entire project for a given term, and searching the term under cursor, respectively.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bwBvzXB5iv94W7KCmvwK8w.gif)
_Searching with Denite_

#### **Configuration**

Denite can be a pretty tough tool to wrap your head around. It’s well documented, but it does reference some concepts that may be unfamiliar to most users. All of my [Denite configurations](https://github.com/ctaylo21/jarvis/blob/master/config/nvim/init.vim#L58) are documented in my setup, so you should be able to use it as a reference. Here’s a quick sample of configuring the base options of Denite for things like customizing highlight groups and layouts.

### Coc.nvim

**What you get:** Intellisense code engine, auto-completion, linting, code fixing

One of the biggest challenges with modern development in Vim is setting up [intellisense code completion](https://en.wikipedia.org/wiki/Intelligent_code_completion). Most modern editors like [Visual Studio Code](https://code.visualstudio.com/) come with intellisense engines built in, or easily available with a plugin (with minimal setup).

I have tried a few solutions, and [coc.nvim](https://github.com/neoclide/coc.nvim) is the best I’ve used. It comes with several major features that are the crux of bringing Vim to the same level as modern IDEs.

There are a few main reasons I think it’s one of the better solutions to intellisense in Vim:

1. It was **incredibly** easy to setup, and immediately worked with both my TypeScript and JavaScript projects.
2. It’s built upon [language servers](https://langserver.org/), which power intellisense in many modern editors.
3. Language server extensions like [coc-tsserver](https://github.com/neoclide/coc-tsserver) are built on top of the [TypeScript/JavaScript code extension](https://github.com/Microsoft/vscode/tree/master/extensions/typescript-language-features) that is built into VSCode. So as VSCode server extensions improve, Vim users can benefit as well.

#### **Basics**

Getting coc.nvim up and running is very straightforward. Once you follow the [installation instructions](https://github.com/neoclide/coc.nvim/wiki/Install-coc.nvim), you can install language server extensions by running `:CocInstall` .

For example, in my current web-based projects, I can have a fully-functioning intellisense engine for most modern TypeScript/JavaScript projects by running:

```
:CocInstall coc-tsserver coc-eslint coc-json coc-prettier coc-css
```

#### **LSP Extension**

This is core of coc.nvim experience. With a language server extension like [coc-tsserver](https://github.com/neoclide/coc-tsserver), you get a [ton of features](https://github.com/neoclide/coc-tsserver#features). I’ll highlight a few:

* Code completion support
* Go to definition
* Find references
* Signature help
* Code validation
* Support for Javascript & TypeScript and JSX/TSX

![Image](https://cdn-media-1.freecodecamp.org/images/1*gveAH1EA0tK3LIPCMkq-pw.gif)
_coc-tsserver in action with React and Typescript_

By default, you get fast, automatic code completion. Types are automatically imported, and you can see function signatures and relevant code completions as you type.

I have a few key mappings set up to quickly utilize a few key features of the language server:

These mappings allow you to quickly jump to a symbol definition, see the implementation for a symbol, or find where it’s referenced. I use them all frequently and find them to be a huge productivity boost.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sugrSH6xNNPIxRuw-Rw1mA.gif)
_Using coc.nvim mappings_

#### **Linting**

I rely on [ESLint](https://eslint.org/) for linting both my JavaScript and TypeScript projects. Now that [TSLint is being deprecated](https://medium.com/palantir/tslint-in-2019-1a144c2317a9), the choice is even easier. I initially used [Ale](https://github.com/w0rp/ale) (which is a great tool), but it had some issues when used together with coc.nvim.

Now, using the [coc-eslint language server extension](https://github.com/neoclide/coc-eslint), you can get real-time feedback from your linter and language server using the same tool. I also use [coc-prettier](https://github.com/neoclide/coc-prettier) to have coc.nvim format my code to [prettier](https://prettier.io/) standards on file save.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0nZE62WR2LxaufaX2anB0g.gif)
_Using eslint and prettier via coc.nvim_

#### **Configuration**

You can configure your coc.nvim setup by creating a configuration file. Right now, [mine](https://github.com/ctaylo21/jarvis/blob/master/config/nvim/coc-settings.json) is pretty simple:

You can read more about setting up your own coc.nvim configuration file [here](https://github.com/neoclide/coc.nvim/wiki/Using-configuration-file).

### Conclusion

That about wraps it up. I’d love to hear any feedback or suggestions, so please leave a comment! In case you missed it above, for my full setup, check out my [dotfiles](https://github.com/ctaylo21/jarvis) and [my article on the rest of my setup](https://medium.freecodecamp.org/coding-like-a-hacker-in-the-terminal-79e22954968e) outside of Vim. Thanks for reading!


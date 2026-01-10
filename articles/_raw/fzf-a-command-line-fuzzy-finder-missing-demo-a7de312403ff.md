---
title: Why you should be using fzf, the command line fuzzy finder
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-19T12:25:50.000Z'
originalURL: https://freecodecamp.org/news/fzf-a-command-line-fuzzy-finder-missing-demo-a7de312403ff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LTR424sh7y8E8rUzsUnFsQ.gif
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Alexey Samoshkin

  Missing demo found

  In this tutorial, I’ll help you take your command line habits to a next level with
  fzf . Start searching files like a pro. Learn less known features, like changing
  directory, searching through a command history,...'
---

By Alexey Samoshkin

#### Missing demo found

In this tutorial, I’ll help you take your command line habits to a next level with `fzf` . Start searching files like a pro. Learn less known features, like changing directory, searching through a command history, looking up the host name to SSH into, killing a process, having instant file’s preview with syntax highlighting, and more…

![Image](https://cdn-media-1.freecodecamp.org/images/iXHjTDv9FFfDA2fnIvojr2s5AA3y0PNvBFgm)
_quick demo_

Today I’m going to tell you about a tool that can change your tech life into “before” and “after” parts. Trust me — it’s not a hyperbole. Meet [fzf](https://github.com/junegunn/fzf), which stands for fuzzy finder. As the definition claims, **it’s a general purpose command-line fuzzy finder**. That doesn’t sound very descriptive and attractive for those who are hearing about it for the first time. But it’s a very popular project ranked at around 21,000 stars [on the Github](https://github.com/junegunn/fzf). So it’s time to clear the fog and get a deeper insight.

This post accompanies [my recent screencast](https://www.youtube.com/watch?v=qgG5Jhi_Els) on the topic. So, if you’re a person who learns by watching, check it out. Otherwise, check it out too ?, because tools like f`zf` are best introduced with a live demo rather than tons of text.

As the `fzf` project page doesn’t have any demo video so far, I’ve called this post “missing demo found”. But now, this video has already been pulled into the `fzf` repo and has become a part of the [project’s readme](https://github.com/junegunn/fzf#demo).

### Searching for files

People who are used to a command line environment are likely familiar with the concept of Unix filters. This is when several independent utilities are composed together into a pipeline to produce the desired output step by step. For instance, this pipeline produces a list of strings:

```
$ yes | head -10 | awk '{ print NR, NR % 2 == 0 ? "even" : "odd" }'
```

```
1 odd2 even3 odd4 even5 odd6 even7 odd8 even9 odd10 even
```

Each program acts as a filter. In simple terms, `fzf` is just another Unix filter. It reads lines from `stdin`, launches an interactive finder dialogue, and finally writes selected items to `stdout`. The key point and difference from tools like GNU `find`, is its interactive finder dialogue that filters items instantly as you type.

![Image](https://cdn-media-1.freecodecamp.org/images/EATLQiPcYRHl0IpEhyE0aups3iUThho5j7Vu)
_“fzf” as a interactive unix filter_

It might not sound too practical so far, but the primary use case for `fzf` is to search for files on the command line. With fuzzy matching and instant feedback, you’re only few characters away from finding the right file no matter how deeply it’s lost in the directory hierarchy. No need to jump back to your file manager, traverse the directory hierarchy, copy a file’s path and paste it back to the shell. Compare “file manager” vs “fzf” workflows below.

![Image](https://cdn-media-1.freecodecamp.org/images/YrD36K2ENGCVEPlslYvMzSwTG1xTsZRiIlHS)
_fzf vs file manager comparison_

`fzf` supports fuzzy matching so you can just type several characters in a row and it will match lines with those characters scattered across the string. Alternatively, prefix a search term with a single quote, like `'string`, to opt for exact matches only, or run as `fzf --exact` .

![Image](https://cdn-media-1.freecodecamp.org/images/3-ePamsGZmgtdsmzIF3IbbZJCTUkNslI-BDk)
_fuzzy vs exact match_

It does not support regular expressions or glob patterns, so `*.sh` pattern would not work. But keep it simple — productivity and speed is your goal today. You don’t have spare time to compose and type correct regular expressions. Instead just type several words, or even parts of the words, delimited by a space, and that would cover >90% of the use cases. For the remaining 10%, u`s`e ^ a`n`d $ to match the start and end of the string respectively, and u`s`e ! to negate matching.

![Image](https://cdn-media-1.freecodecamp.org/images/kV5hgH2rvYEEBRMWUnjsDwBIL7LN9mU3C5E6)
_fzf matching syntax_

Printing selected files to a command line is not super useful, so usually search is combined with some further action. For instance, you might open it with Vim, or pipe selected items to the next program.

```
# Open file in a Vimvim -o `fzf`
```

```
# Print info for each selected filefzf | xargs ls -l
```

### Fuzzy completion for bash and zsh

To make it more convenient, fuzzy completion can be triggered if the word before the cursor ends with the trigger sequence which is by default `**`. For example, type `vim ~/path/**` and press `TAB` . Voilà, fzf steps in!

![Image](https://cdn-media-1.freecodecamp.org/images/PvhRo5LV4UvRpN8gCoo-1tJ0s5Imyal0Hjbb)
_Double star fuzzy completion_

`**` sequence triggers `fzf` finder and it resembles `*` which is for native shell expansion. At some point, you might even forget about `fzf`’s presence and get the impression it’s a native shell feature.

[Format is as follows](https://github.com/junegunn/fzf#fuzzy-completion-for-bash-and-zsh), where `FUZZY_PATTERN` is optional.

```
COMMAND [DIRECTORY/][FUZZY_PATTERN]**<TAB>
```

If you don’t like the `**` sequence, you can use keyboard shortcuts. `CTRL+T` triggers `fzf` and pastes the selected file onto the command line, whereas `ALT+C` changes into the selected directory.

### Changing directory

Ok, enough about searching files. Let’s talk about other useful applications. Changing your working directory is such a common operation. But nevertheless I’m always stuck a bit trying to recall and type the right directory’s path, making several mistakes along the way. It slows down my tempo. Even zsh completions do not compensate for it. But with `fzf`, changing directories is a breeze, no matter how deep and far it is. Just type `cd **` and you’re almost there.

![Image](https://cdn-media-1.freecodecamp.org/images/t8dzyyZ0vMSFwpFU7PgKtfH86AhM3C6fIvoH)
_changing directory is like a breeze_

Notice that while fzf is indexing your directory tree, you can start searching right away. Changing directories is my favourite use case, and fuzzy matching really excels here. It requires from you the same effort to change a directory whether it’s one level deep or ten levels deep.

`ALT+C` shortcut is an alternate way to trigger `fzf` in a change directory mode.

### Command history

You might be using `Ctrl+R` keyboard shortcut to search through your command history. Great, but how about supercharging it with fuzzy finder? Look and compare.

![Image](https://cdn-media-1.freecodecamp.org/images/y2wgBR9TUloRfQVgpmChaTtTrrjHfrQR374y)
_Searching through command history_

It pastes the selected item on the command line, so you can tweak it further.

### Search the host name to SSH into

If you’re a backend developer and working with a number of remote servers, you might appreciate `ssh+fzf` combo. Use the same double star trigger sequence and type `ssh **` . It pulls recently used IP addresses and host names from your `~/.ssh/config` and brings up an interactive finder.

![Image](https://cdn-media-1.freecodecamp.org/images/-khneINrdlXrPo00zg2ZcZc4jrnrVOKZSpUn)
_“fzf + ssh” combo_

### Send a signal to a process

Sometimes we want to send a signal to a process, but first we need to obtain its PID by name. Usually one uses `pgrep <process_na`me> to resolve PID followed `by a kill <pro`cess_pid> referring tha`t P`ID. With fzf you can combine both `steps. Typ`e kill <TAB> and fzf steps in listing all your processes. No need to switch to a dedicated process monitor any more, like “Activity Monitor” on Mac.

![Image](https://cdn-media-1.freecodecamp.org/images/BvbjoYPcKfZPTGuEV2XyhTfelQ69EIA4EP2-)
_Find a process and send a signal_

### Preview files as you search

Suppose you’re searching for files, but sometimes the file name itself does not tell you enough. So you might want to peek into a file’s content for a moment to make a decision. `fzf` covers you here as well.

![Image](https://cdn-media-1.freecodecamp.org/images/l3wJ44GjRyqJN8iyiDBmrGIH8EdpYwZZergy)
_Preview window_

By default I have preview window off, but I toggle it on when I want to peek into the files. Plus, I’ve enhanced it with a coloured output and syntax highlighting using [bat](https://github.com/sharkdp/bat) as a preview command.

### Customization

There are two main ways to customize the stock version of `fzf`:

* Change the behaviour of the finder dialogue (preview window, keyboard shortcuts, dimensions, custom actions, etc). See `FZF_DEFAULT_OPTS` environment variable.
* Change the underlying find backend. By default it uses GNU `find` utility, but you can switch to the more advanced tools like [fd](https://github.com/sharkdp/fd) or [ripgrep](https://github.com/BurntSushi/ripgrep). First, it’s faster than the stock `find` utility. Second, those tools respect `.gitignore` rules, so you don’t get `node_modules` or `.git` files in your search results. You [can also use](https://github.com/junegunn/fzf#git-ls-tree-for-fast-traversal) `git ls-tree` to list files when you’re in a Git repo. See `FZF_DEFAULT_COMMAND` environment variable.

Configuration is done through the environment variables. Here is the snippet from my setup. Not sure if it would work as is when copy-n-pasted, most likely there’re some other missing dependencies. But this is just to give you an idea of how the configuration looks.

### Fzf and Vim

So far we’ve seen command-line usage only. But `fzf` is also shipped as a [Vim plugin](https://github.com/junegunn/fzf.vim). And trust me, if you are a Vimmer, its worth adding to your `vimrc`. Vim usage is out of the scope of this post, otherwise no one would read it ?. But I talk about it thoroughly in the second part of the m[y video,](https://www.youtube.com/watch?v=qgG5Jhi_Els) also linked at the beginning of the post.

If you’re impatient, here is a small excerpt to draw your attention. Use `:grep` command for project-wide text search, open matches in `fzf` window in a full screen mode, further filter matches within `fzf`, and jump to the selected match. And don’t forget about instant file preview at the precise line position. That’s awesome, isn’t it?

![Image](https://cdn-media-1.freecodecamp.org/images/ADmJjvj-Jy35K2UAyAfpnUx8mi-1MqdRl-IJ)
_fzf ❤️ vim_

### Conclusion

I hope you’re impressed of how super awesome [fzf](https://github.com/junegunn/fzf) is. Chances are you already willing to install and give it a try.

Keep in mind that `fzf` is not only for file searching, although it’s the primary feature of it. As you can see, “**search + action**” is a general principle, but it’s abstract and powerful enough to work with any kind of list: files, directories, processes, host names, etc. Remember at the beginning of this post — **fzf is just a Unix filter**. Unlock your imagination, feed it any list, and tailor it for your own needs. You might take some inspiration from a [wealth of examples](https://github.com/junegunn/fzf/wiki/examples).

BTW, appreciate how superior Unix philosophy is. `fzf` is a great example of a program that adheres to these principles.

* let the program to do one thing and do it well (single responsibility principle)
* make it abstract enough to be agnostic of irrelevant details or data types
* compose separate individual programs using standard well-defined interfaces.

Stick with those principles in your software development career. Knowing fundamental principles that stand behind the rapid birth and death of multiple tools, languages, and frameworks out there is what differentiates professional developers from amateurs.

### Resources

junegunn/fzf: A command-line fuzzy finder — [https://github.com/junegunn/fzf](https://github.com/junegunn/fzf)

Vim universe. fzf — command line fuzzy finder — YouTube — [https://www.youtube.com/watch?v=qgG5Jhi_Els](https://www.youtube.com/watch?v=qgG5Jhi_Els)

My Youtube channel. There’re only a few videos, as I’m taking my first steps into making screencasts. Be patient, I promise to make more videos. Alexey Samoshkin — YouTube — [https://www.youtube.com/channel/UCfju8u-YOpNMO4CbyzIsc9Q](https://www.youtube.com/channel/UCfju8u-YOpNMO4CbyzIsc9Q).

sharkdp/fd: A simple, fast and user-friendly alternative to ‘find’ — [https://github.com/sharkdp/fd](https://github.com/sharkdp/fd)

BurntSushi/ripgrep: ripgrep recursively searches directories for a regex pattern — [https://github.com/BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)

junegunn/fzf.vim: fzf vim — [https://github.com/junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)


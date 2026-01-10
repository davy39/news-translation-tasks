---
title: How not to be afraid of Vim anymore
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T16:37:47.000Z'
originalURL: https://freecodecamp.org/news/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae
coverImage: https://cdn-media-1.freecodecamp.org/images/0*idcJObABQVEH2BVq
tags:
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: vim
  slug: vim
seo_title: null
seo_desc: 'By Neil Kakkar

  A curation of the most popular commands and how to use them

  If you’ve ever used Vim, you know how difficult it can get to reach the same speed
  as in a “normal” GUI editor. But once you do, the payoff is exponential — you get
  much more ...'
---

By Neil Kakkar

#### A curation of the most popular commands and how to use them

If you’ve ever used Vim, you know how difficult it can get to reach the same speed as in a “normal” GUI editor. But once you do, the payoff is exponential — you get much more efficient at writing code. Of course, this isn’t the main reason for this post.

The majority of the time goes — or should go — into designing a solution to your problem, not actually coding it; so optimizing the how-fast-you-code bit seems like the last thing to focus on. It’s not a leverage point.

This post took shape because of another reason: the non-existence of GUIs on SSH’ed machines. What are you going to do now? Any machine where you have access to the terminal and you want to edit a file — You have 2 options:

1. Give up, try to close Vim
2. Master Vim

Just making a copy of `[vimtutor](https://superuser.com/questions/246487/how-to-use-vimtutor)` wouldn’t help anyone. So here I’m using a different approach: I aggregated the best bits of vim that I use in everyday life as a software developer, along with mnemonics to remember the stuff by. This contains almost everything you need for regular editing and writing.

### The basics

Stick with me, this isn’t about the commands but the ideology behind them!

#### Modes

Vim has 2 modes:

* Normal ( Command mode)
* Insert ( Edit mode )

When you open Vim, you start in normal mode. To enter back into normal mode at anytime, press the `ESC` key. Normal mode is where you can issue commands: the list of commands is endless!

There are a lot of ways to enter insert mode. The most intuitive one is to use the `i` command. `i` for insert. In normal mode, press `i` and you’ll enter insert mode. Now anything you type will show up in the editor. One of the biggest hurdles, sorted.

The mental model — to understand the idea: Since there is no GUI, there’s no concept of mouse clicks. There’s no menu to choose options from, there’s no right click. Hence, you need a way to get all this on the keyboard — your only input source.

Having two modes achieves this! You can think of the Normal ( Command) mode as the Menu bar and mouse on steroids, while the Insert mode is like the normal mode in GUI editors ( where what you type shows up on the screen ).

#### Words

To Vim, words mean almost the same as what they mean to us — A set of characters separated by whitespace or special characters. The command is `w`.

#### Command Anatomy

Commands in Vim follow a set pattern. Knowing this would help put each command into a certain bucket of commands, thus building a better mental model for the same.

Commands look like this:

[action] <number> [motion]

The action is what you want to do,

The number is how many times you want to do that action,

The motion is the range of that action.

The motion is the scope. An example would make this clearer. Let us say, we want to delete the next 3 words, starting from the cursor. Here, the action is delete, the number is 3 and the motion is a word. The command action for delete is `d`.

Hence, we get the final command as: `d3w` — delete the next 3 words.

Omitting the number defaults to once.

Motions can be used without an action, which defaults to navigation. Hence, typing `w` in command mode would move the cursor forward one word.

We are well equipped now to start learning about the commands themselves (and a range of motions to use with them)

### Useful commands

#### How to close Vim

First things first, we don’t want to get stuck in Vim land without having an exit plan. Always have an exit strategy.

`:q` to quit

`:q!` to force quit

`:wq` to save and quit

#### Command Actions

`d` : delete

`i` : insert

`p` : put / paste

`y` : yank / copy

`x` : cut

`u` : **undo**

`di`: delete inside*, `yi` : yank inside*

`v` : visual / selection

`/` : search

`%` : parentheses matching, developers rejoice!

`:s` : substitute! In other words, find-replace on steroids

Since actions on the entire line are very frequent, the developers of vim created a new shorthand for them — omitting the need to add a motion. Repeat the action to apply on the entire line. For example:

To delete the current line: `dd`

To copy the current line: `yy`

Neat, ain’t it?

#### Command motions

Motions go with actions as we have seen, and the available motions changes with the action. However, some motions are pretty uniform.

`w` : beginning of next word (we’ve seen this before!)

`e` : ending of current word

`b` : beginning of previous word

Arrow keys / <h,j,k,l> : respective motions. h,j,k,l are a substitute to the arrow keys, and the source of speed in Vim: You don’t have to move your hands away from the typing part of the keyboard.

`$` : end of line

`0` : beginning of line

`G` : end of file

`nG` : jump to line number `n`

`)` : jump forward a sentence

`}` : jump forward a paragraph

This helps visualise better:

```
           ge      b          w                             e
           <-     <-         --->                          --->
    This is-a line, with special/separated/words (and some more). ~
       <----- <-----         -------------------->         ----->
         gE      B                   W                       E
```

Armed with these actions and motions, we can create most of the basic commands in Vim. Here’s a list of 8 every day functions. Figure out the command to make them happen!

1. Delete the next 3 lines ( including current line)
2. Copy current word — cursor is at beginning of word
3. Copy current word — it has special characters — cursor is in the middle of the word
4. Navigate down 10 lines
5. Delete everything inside the curly brackets
6. Go up 2 paragraphs
7. Paste the previously selected text 5 times.
8. Edit where the cursor is present: “I can Vim now!”

…

Wait for it…

…

Here are the solutions:

1. `d3j`
2. `yw`
3. `yiW` : the yank inside is to yank inside, and `W` is inside what to yank ( current word). This is amazingly useful, you can use all sorts of combinations with `inside` !
4. `10j`
5. `di}` : just like #3.
6. `2{` : this was slightly more intuitive. `{` is to go up a para, `}` is to go down a para
7. `5p` : remember the optional numbers from the command anatomy? They can be used almost anywhere
8. `i` `I can Vim now!` : `i` is to go into insert mode, then you can work like in a “normal” editor

Alright, you made it! Congratulations, this is enough Vim to go about exploring on your own, adventurer. The tutorial is over. Good luck.

If someone asks you about Vim, you can do better than using this meme. Explain it to them, or point them here ;)

![Image](https://cdn-media-1.freecodecamp.org/images/QkqAG7RCyNb08rhtBYp24mYBdLK5UoHRDhII)

> *Note: This is my model of Vim. It isn’t exactly how things work internally. If you look at the documentation ( :help user-manual ), you’ll see that d is the command, and the motion is iw, or “inside word”. There’s a deviation.  
> Why? — because I feel this helps explain better.

### Bonus

Here are some extra commands that come in handy:

#### Split screen

`:vsplit <filena`me>

Creates a vertical splitting. Enables you to copy-paste from one screen to another.

To cycle between screen-splits: `<ctrl-w> &l`t;ctrl-w>

Alternatively, you could use the arrow keys / `hjkl` like so:

`<ctrl-w`> h to go to previous screen.

You can close windows as you normally do (`:q`), or —

`:only` — to close all other windows

#### Multiple Tabs

`:tabnew <filena`me> opens a new file in a new tab on Vim

`:tabn` to go to next tab ( or `:gt` )

`:tabp` to go to previous tab ( or `:gT` )

Again, you can copy-paste from one tab into another.

You can map this combination to a key of your choice too!

I tried `<Ctrl-T`ab>, but that’s already reserved. What a bummer. Instead, we have:

```
map <C-t><left> :tabp<cr>
map <C-t><right> :tabn<cr>
```

Which means <Ctrl-t> followed by the left or right right arrow key would let you switch between tabs.

How exactly did I come up with this mapping? [Check out this tutorial](http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_1)).

Other stories in this series:

* [How not to be afraid of Python anymore](https://medium.freecodecamp.org/how-not-to-be-afraid-of-python-anymore-b37b58871795)
* [How not to be afraid of GIT anymore](https://medium.freecodecamp.org/how-not-to-be-afraid-of-git-anymore-fe1da7415286)

Enjoyed this? [Don’t miss a post again — subscribe to my mailing list!](http://neilkakkar.com/subscribe/)


---
title: How to Use Spell Check on your Linux Terminal
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-01-20T16:17:10.000Z'
originalURL: https://freecodecamp.org/news/spell-check-on-your-linux-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/BB---Spell-Check-in-Linux-Terminal.png
tags:
- name: Linux
  slug: linux
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "Did you know you can use the terminal to check the spelling of a passage\
  \ you've written? \nThe terminal has a lot of utility commands, but most people\
  \ are unaware of many of them. \nI've seen people using Microsoft Word or Google\
  \ to check the spelling ..."
---

Did you know you can use the terminal to check the spelling of a passage you've written? 

The terminal has a lot of utility commands, but most people are unaware of many of them. 

I've seen people using Microsoft Word or Google to check the spelling of a word. But this utility command is a handy alternative tool for developers to check their spelling. The fact that it comes pre-installed with the terminal is an added advantage. 

## How to Use the Linux Spell Check Command

`ispell` and `aspell` are the 2 commands you can use to check the spelling of a word. Out of these 2, `ispell` is the old spellchecker from GNU which has a limited capability to read different kinds of encoded files. 

`aspell` is an interactive spell checker which checks the spelling via standard input or by reading through the file. It checks spelling on UTF-8 encoded files. It can read and check the spelling on markdown files, too. 

`aspell` has a lot of options. Running `--help` with the command shows the list of all the available options. 

```bash
aspell --help
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-146.png)
_`aspell --help` command output_

If you encounter errors while running the above command, it means that you don't have it installed. Run the following command to install `aspell` in your machine:

```bash
sudo apt install aspell
```

## How to Check the Spelling of Words One-by-one Interactively? 

Pass the `-a` flag with the `aspell` command to open it in interactive mode. 

```bash
aspell -a
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-147.png)
_`aspell -a` command to open `aspell` in interactive mode_

In this mode, you can enter the words with possible incorrect spelling one by one and you will get a list of words with the correct spelling that are the closest to the entered word. 

Here's an example screenshot: 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-156.png)
_Correct word suggestions from `aspell` command_

From the above screenshot, you can see that `aspell` suggests multiple words for each incorrectly-spelled word I entered. 

The close alternatives for the word `sampee` are `sample`, `simper`, `sampler`. Similarly, you can see the suggestions for other words too (waier, calendrr, moble, bqttle). 

This can be quite handy for developers since they can quickly switch to the terminal and find the correct spelling of a word during their development. The fact that it does not require the internet is an added advantage. 

## How to Check the Spelling of Words from a File

Using the terminal to check the spelling of words from a file is the best alternative approach if you don't have internet access. Grammarly and Google Docs will best assist you with a good internet connection. 

You can write the passage in a text file and pass the file path as an argument to the `-c` flag in the `aspell` command. This accepts an HTML or Markdown file too. 

```bash
aspell -c <filename>
```

I've created a file named `computer.txt` and added the below content:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-157.png)
_Content of `computer.txt` file_

I've made some spelling mistakes in the middle. You might be able to spot them easily. Some of them are macine instead of machine, intrenet instead of internet, etc. 

Let's ask `aspell` to find the spelling mistakes in this passage. 

```bash
aspell -c computer.txt
```

Once you run the above command, you'll be shown a screen similar to the following screenshot:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-158.png)
_`aspell` command to find spelling mistakes in a file_

This means that `aspell` has figured out some spelling mistakes in our passage. It will highlight the misspelled words one-by-one with the appropriate alternative correctly spelled words at the bottom. 

There will be 10 options shown with a row number. You can choose the correctly spelled word by entering the corresponding row number. 

For example, in the above screenshot, the word "macine" is highlighted and the right replacement for this misspelled word is "machine", which is the 1st option. So, I press 1. 

Immediately after I press 1, the correction was made and aspell moves to the next misspelled word. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-159.png)
_`aspell` command corrects and moves to the next misspelled word in the file_

In addition to the 10 options, `aspell` shows 8 different options. You can choose one of the them if you did not find the right word from the above 10 alternate options. 

Let's understand each option you can use with `aspell`:

<table><tbody><tr><td><strong>Character</strong></td><td><strong>Action</strong></td><td><strong>Description</strong></td></tr><tr><td>i</td><td>Ignore</td><td>Ignore this occurrence and move on to next misspelled word</td></tr><tr><td>r</td><td>Replace</td><td>Replace this word by manually entering a new word</td></tr><tr><td>a</td><td>Add</td><td>Add this word to the dictionary</td></tr><tr><td>b</td><td>Abort</td><td>Abort this operation (The changes you applied will not be saved)</td></tr><tr><td>I</td><td>Ignore all</td><td>Ignore all occurrences of this word</td></tr><tr><td>R</td><td>Replace all</td><td>Replace all occurrences of this word by manually entering a new word</td></tr><tr><td>l</td><td>Add Lower</td><td>Add the word to the dictionary</td></tr><tr><td>x</td><td>Exit</td><td>Exit the operation (The changes you applied will be saved)</td></tr></tbody></table>

The above table describes the action for each character in the `aspell check` command. 

Once you're done with correcting the spelling of all the misspelled words, the file will be automatically saved by `aspell`. 

In addition to that, a new file will be created with the name **<existing_file_name>.bak**, which is a backup of the same file without applying spell check. 

## How to Ignore Creating a New File While Correcting Spelling in a File

This is quite simple and can be easily achieved by passing a flag with the `aspell` command. The flag is `--dont-backup`. 

Let's look at an example command:

```bash
aspell check --dont-backup computer.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-160.png)
_Ignore creating a backup file by passing `--dont-backup` flag_

From the above screenshot, you can see that I've removed the existing `computer.txt.bak` file and run the spell check by passing the `--dont-backup` flag. No more `.bak` file has been created after I complete the spell check. 

You may also notice one more change from the previous example and the above command. That is `check` and `-c`. In my previous command, I used `-c`, but in the above command, I used `check` to pass the file name. 

You can either use `-c` or `check` to pass the file name. Both of them do the same job. 

## Can You Check the Spelling on Other Files? 

Absolutely yes. `aspell` checks for spelling by reading Markdown and HTML files, too. You have to pass the mode of the file as a separate argument ( `--mode` ). 

Here's the syntax, 

```bash
aspell check --mode=<mode_type> file_name
```

The supported modes are `none`, `url`, `email`, `markdown`, `html`, `tex`, `texinfo`, and `nroff`. 

Let's see a quick example of fixing the spelling mistakes on a markdown file. 

```bash
aspell check --dont-backup --mode=markdown spellcheck.md
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-161.png)
_Running `aspell` with the markdown file_

It opened a similar interface, but it understood the markdown format and highlighted only the misspelled word. 

I want to bring one important item to your attention. You can find a misspelled word (blok) in the middle of the backtick (``` ... ```) block. The content inside this block will not be evaluated by the aspell command. So, you'll not be able to spot and correct the misspelled words inside the block. 

Similarly, you can evaluate the spelling in the HTML files by changing the mode to html. 

## Conclusion

In this article, you have learned to check spelling using your Linux Terminal. I hope you enjoy reading it. 

Subscribe to my newsletter by visiting my [site](https://5minslearn.gogosoon.com/?ref=fcc_spell_check) and also have a look at the consolidated list of all my blogs. 



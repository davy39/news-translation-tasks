---
title: How to Search-and-replace Across Multiple Files in Vim
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-08-28T15:01:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-search-and-replace-across-multiple-files-in-vim
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cover-5.png
tags:
- name: Productivity
  slug: productivity
- name: vim
  slug: vim
seo_title: null
seo_desc: 'In this article, you''ll learn how to interactively search-and-replace
  across many files with just two commands, thanks to Vim.

  While a multitude of methods exist to search for and replace words in a single file,
  what do you do when you’ve got a strin...'
---

In this article, you'll learn how to interactively search-and-replace across many files with just two commands, thanks to Vim.

While a multitude of methods exist to search for and replace words in a single file, what do you do when you’ve got a string to update across multiple unrelated files, all with different names? You harness the power of command line tools, of course!

First, you’ll need to `find` all the files you want to change. Stringing together what are effectively search queries for `find` is really only limited by your imagination. 

Here’s a simple example that finds Python files:

```sh
find . -name '*.py'

```

The `-name` test searches for a pattern, such as all files ending in `.py`. But `find` can do a lot more with other test conditions, including `-regex` tests. Run `find --help` to see the multitude of options.

Further tune your search by using `grep` to get only the files that contain the string you want to change, such as by adding:

```sh
grep -le '\<a whale\>'

```

The `-l` option gives you just the file names for all files containing a pattern (denoted with `-e`) that match “a whale”.

You can also use Vim’s impressive `:bufdo` which lets you run the same command across multiple buffers. It interactively works with all of these files without the tedium of opening, saving, and closing each file, one at a time.

Let’s plug your powerful `find`+`grep` results into Vim with:

```sh
vim `find . -name '*.py' \
-exec grep -le '\<a whale\>' {} \;`

```

Using backtick-expansion to pass our search to Vim opens up multiple buffers ready to go. (Do `:h backtick-expansion` in Vim for more.) 

Now you can apply the Vim command `:bufdo` to all of these files and perform actions such as interactive search-and-replace:

```vim
:bufdo %s/a whale/a bowl of petunias/gce

```

The `g` for “global” will change occurrences of the pattern on all lines. The `e` will omit errors if the pattern is not found. The `c` option makes this interactive. If you’re feeling confident, you can omit it to make the changes without reviewing each one.

When you’ve finished going through all the buffers, save all the work you’ve completed with:

```vim
:bufdo wq!

```

Then bask in the glory of your saved time and effort.


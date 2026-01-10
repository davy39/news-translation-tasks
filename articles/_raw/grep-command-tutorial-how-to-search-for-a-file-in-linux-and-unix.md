---
title: Grep Command Tutorial – How to Search for a File in Linux and Unix with Recursive
  Find
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-13T22:56:11.000Z'
originalURL: https://freecodecamp.org/news/grep-command-tutorial-how-to-search-for-a-file-in-linux-and-unix
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b0c740569d1a4ca2969.jpg
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: unix
  slug: unix
seo_title: null
seo_desc: 'By Dillion Megida

  grep stands for Globally Search For Regular Expression and Print out. It is a command
  line tool used in UNIX and Linux systems to search a specified pattern in a file
  or group of files.

  grep comes with a lot of options which allow u...'
---

By Dillion Megida

`grep` stands for _Globally Search For Regular Expression and Print out_. It is a command line tool used in UNIX and Linux systems to search a specified pattern in a file or group of files.

`grep` comes with a lot of options which allow us to perform various search-related actions on files. In this article, we'll look at how to use `grep` with the options available as well as basic regular expressions to search files.

## How to use `grep`

Without passing any option, `grep` can be used to search for a pattern in a file or group of files. The syntax is:

```bash
grep '<text-to-be-searched>' <file/files>
```

**Note that** single or double quotes are required around the text if it is more than one word.

You can also use the **wildcard (\*)** to select all files in a directory.

The result of this is the occurences of the pattern (by the line it is found) in the file(s). If there is no match, no output will be printed to the terminal. 

For example, say we have the following files (called grep.txt):

```default
Hello, how are you
I am grep
Nice to meet you
```

The following `grep` command will search for all occurences of the word 'you':

```bash
grep you grep.txt
```

The result for this is:

```bash
Hello, how are you
Nice to meet you
```

`you` is expected to have a different color than the other text to easily identify what was searched for.

But `grep` comes with more options which help us achieve more during a search operation. Let's look at nine of them while applying them to the example above.

### Options used with `grep`

#### 1. `-n` (--line-number) - list line numbers

This prints out the matches for the text along with the line numbers. If you look at the result we have above, you'll notice there are no line numbers, just the matches.

```bash
grep you grep.txt -n
```

Result:

```bash
1: Hello, how are you
3: Nice to meet you
```

#### 2. `-c` (--count) - prints the number of lines of matches

```bash
grep you grep.txt -c
```

Result:

```bash
2
```

**Note that** if there was another 'you' on line one, option `-c` would still print 2. This is because it is concerned with the number of lines where the matches appear, not the number of matches.

#### 3. `-v` (--invert-match) - prints the lines that do not match the specified pattern

```bash
grep you grep.txt -v -n
```

Result:

```bash
2. I am grep
```

Notice that we also used option `-n`? Yes, you can apply multiple options in one command.

#### 4. `-i` (--ignore-case) - used for case insensitivity

```bash
# command 1
grep You grep.txt
# command 2
grep YoU grep.txt -i
```

Results:

```bash
# result 1
# no result
# result 2
Hello, how are you
Nice to meet you
```

#### 5. `-l` (--files-with-matches) - print file names that match a pattern

```bash
# command 1
grep you grep.txt -l
# command 2
grep You grep.txt -i -l
```

Results:

```bash
# result 1
grep.txt
# result 2
# all files in the current directory that matches
# the text 'You' case insensitively
```

    #### 6. `-w` (--word-regexp) - print matches of the whole word

By default, `grep` matches strings which contain the specified pattern. This means that `grep yo grep.txt` will print the same results as `grep yo grep.txt` because 'yo' can be found in you. Similarly, 'ou'. 

With the option `-w`, `grep` ensures that the matches are exactly the same pattern as specified. Example:

```bash
grep yo grep.txt -w
```

Result:

No result!

#### 7. `-o` (--only-matching) - print only the matched pattern

By default, `grep` prints the line where the matched pattern is found. With option `-o`, only the matched pattern is printed line by line. Example:

```bash
grep yo grep.txt -o
```

Result:

```bash
yo
```

#### 8. `-A` (--after-context) and `-B` (--before-context) - print the lines after and before (respectively) the matched pattern

```bash
grep grep grep.txt -A 1 -B 1
```

Result:

```bash
Hello, how are you
I am grep
Nice to meet you
```

This matched pattern is on line 2. `-A 1` means one line after the matched line and `-B 1` means one line before the matched line.

There's also a `-C` (--context) option which is equal to `-A` + `-B`. The value passed to `-C` would be used for `-A` and `-B`.

#### 9. `-R` (--dereference-recursive) - recursive search

By default, `grep` cannot search directories. If you try doing so, you'll get an error ("Is a directory"). With option `-R`, searching files within directories and subdirectories becomes possible. Example:

```bash
grep you .
```

Result:

```bash
# 'you' matches in a folders
# and files starting from the
# current directory
```

### Regular expressions for patterns

`grep` also allows basic regular expressions for specifying patterns. Two of them are:

#### 1. `^pattern` - start of a line

This pattern means that the `grep` will match the strings whose lines begin with the string specified after `^`. Example:

```bash
grep ^I grep.txt -n
```

Result:

```bash
2: I
```

#### 2. `pattern$` - end of a line

In contrast with `^`, `$` specifies patterns that will be matched if the line ends with the string before `$`. Example:

```bash
grep you$ grep.txt
```

Result:

```bash
1: Hello, how are you
3: Nice to meet you
```

## Wrap up

`grep` is a powerful tool for searching files in the terminal. Understanding how to use it gives you the ability to easily find files via the terminal. 

There are more options attached to this tool. You can find with `man grep`.




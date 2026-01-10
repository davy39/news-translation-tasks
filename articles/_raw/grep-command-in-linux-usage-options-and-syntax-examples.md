---
title: Grep Command in Linux – Usage, Options, and Syntax Examples
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2023-01-17T22:40:13.000Z'
originalURL: https://freecodecamp.org/news/grep-command-in-linux-usage-options-and-syntax-examples
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Copy-of-Copy-of-Cast-a-Function-in-SQL---Convert-Char-to-Int-SQL-Server-Example.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Grep is a useful command to search for matching patterns in a file. grep\
  \ is short for \"global regular expression print\". \nIf you are a system admin\
  \ who needs to scrape through log files or a developer trying to find certain occurrences\
  \ in the code fi..."
---

`Grep` is a useful command to search for matching patterns in a file. `grep` is short for "global regular expression print". 

If you are a system admin who needs to scrape through log files or a developer trying to find certain occurrences in the code file, then `grep` is a powerful command to use.

In this article, we will discuss the `grep` command's syntax and its usage with some examples.

## Syntax of the `grep` Command

 The syntax of the `grep` command is as follows:

```bash
grep [OPTION...] PATTERNS [FILE...]
```

In the above syntax, grep searches for PATTERNS in each FILE. `Grep` finds each line that matched the provided PATTERN. It is a good practice to close the PATTERN in quotes when `grep` is used in a shell command.

In this article, we will discuss the following options that can be used with `grep`:

* `-i`, `--ignore-case`: Ignores case distinctions in patterns and input data.
* `-v`, `--invert-match`: Selects the non-matching lines of the provided input pattern.
* `-n`, `--line-number`: Prefix each line of the matching output with the line number in the input file.
* `-w`: Find the exact matching word from the input file or string.
* `-c`: Count the number of occurrences of the provided pattern.

In the coming examples, we will use the file `fruits.txt` with the following content: 

```
apples and pears
citrus – oranges, grapefruits, mandarins and limes
stone fruit – nectarines, apricots, peaches and plums
tropical and exotic – bananas and mangoes
berries – strawBERRIES, raspberries, blueberries, kiwifruit and passionfruit
melons – watermelons, rockmelons and honeydew melons
tomatoes and avocados.
```

## How to Find a Matching String with `grep`

If we want to find the string "fruit" in the file `fruits.txt`, we can do so like this:

```bash
grep "fruit" fruits.txt
```

Here's the output:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-73.png)

## How to Ignore Case Distinctions using `-i`

We can command `grep` to return results while ignoring the case of the matching string. Let's find the word "berries" from our sample file. It should match all occurrences of "berries" regardless of their case.

```bash
 grep -i "berries" fruits.txt
```

 Output:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-74.png)

## How to Select the Non-Matching Lines using `-v`

We can reverse the results of the `grep` command to include non-matching results. Let's say, if we want to get all the lines that do not contain the word "berries", the command would look like this: 

```bash
grep -v "berries" fruits.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-75.png)

The output returned all the lines that do not contain "berries".

## How to Find the Line Numbers Against Matching Input using `-n`

There are times when we want to get the line numbers against the matching string. For that, we can supply the `-n` flag to `grep` like this:

```bash
 grep -n "berries" fruits.txt
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-76.png)

From the output, we can see that the word "berries" occurs on line #5 of the file.

## How to Find the Exact Matching Word from the Input File or String using `-w`

If you were to match an exact word rather than just the occurrence of a pattern, you can do so by using the `-w` flag.

If we `grep` "fruit" without any flags, it would return any occurrence of the word "fruit".  This would include occurrences like "grape**fruit**", "dragon**fruit**" and so on like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-77.png)

But, if we only want "fruit" in our results, we can use the `-w` flag like this:

```bash
 grep -w  "fruit" fruits.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-78.png)

Do you see the difference? The latter result returned only one line where the exact word "fruit" was found.

## How to Count the Number of Occurrences of the Provided Pattern using `-c`

We can count the number of times the matched string appears in the file. This is how the `-c` flag works:

```bash
grep -c "fruit" fruits.txt
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-79.png)

The word "fruit" appears 3 times in the file.

Tip: The `-c` flag can be very useful if you have to count the number of times an error message appeared in a log file. 

## How to Scan Files for Matching Input

Until now we had discussed how to search for matching patterns in a file or input string. We can also use `grep` to narrow down the files that contain a matching pattern. We can use the following flags to separate files that contain the matching pattern:

* `-l, --files-with-matches`: Prints the file name that contains the provided matching pattern.
* `-L, --files-without-match`: Prints the file name that does not contain the provided matching pattern.

Let's say we have the following files in our folder:

```bash
zaira@Zaira:~/grep-tutorial$ ls -lrt
total 12
-rw-r--r-- 1 zaira zaira 327 Jan 16 19:25 fruits.txt
-rw-r--r-- 1 zaira zaira  47 Jan 16 20:31 vegetables.txt
-rw-r--r-- 1 zaira zaira 194 Jan 16 20:33 more-fruits.txt
```

 The files have the following content:

```
zaira@Zaira:~/grep-tutorial$ cat fruits.txt
apples and pears
citrus – oranges, grapefruits, mandarins and limes
stone fruit – nectarines, apricots, peaches and plums
tropical and exotic – bananas and mangoes
berries – strawBERRIES, raspberries, blueberries, kiwifruit and passionfruit
melons – watermelons, rockmelons and honeydew melons
tomatoes and avocados.
```

```bash
zaira@Zaira:~/grep-tutorial$ cat more-fruits.txt
passionfruit
dragon fruit
kiwis
pears
grapefruits, mandarins and limes
stone fruit – nectarines, apricots, peaches and plums
tropical and exotic – bananas and mangoes
tomatoes and avocados.
```

```bash
zaira@Zaira:~/grep-tutorial$ cat vegetables.txt
# Vegetables only

Cabbage
Onion
Carrot
Potato
```

Next, we want to see files that contain the pattern "fruit". We can do that like this:

```bash
 grep -l "fruit" *
```

Note that the `*` searches for all the files in the folder.

Here is the output::

```bash
zaira@Zaira:~/grep-tutorial$  grep -l "fruit" *
fruits.txt
more-fruits.txt
```

Let's say we want to list files that do not contain the word "fruit". We can achieve that using the command below:

```bash
 grep -L "fruit" *
```

Here is the output:

```bash
zaira@Zaira:~/grep-tutorial$  grep -L "fruit" *
vegetables.txt
```

## Wrapping Up

If you want to study the `grep` command in depth, have a look at the man pages. You can get additional information on the command line with `grep --help`.

I hope you found this tutorial helpful!

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

Image credits:

[Image by upklyak](https://www.freepik.com/free-vector/electronic-documents-management-doodle-concept_29314820.htm#query=file%20search&position=7&from_view=search&track=sph) on Freepik


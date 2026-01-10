---
title: The Linux AWK Command – Linux and Unix Usage Syntax Examples
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-10-12T15:34:47.000Z'
originalURL: https://freecodecamp.org/news/the-linux-awk-command-linux-and-unix-usage-syntax-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/florian-klauer-mk7D-4UCfmg-unsplash.jpg
tags:
- name: Linux
  slug: linux
- name: unix
  slug: unix
seo_title: null
seo_desc: 'In this beginner-friendly guide, you''ll learn the very basics of the awk
  command. You''ll also see some of the ways you can use it when dealing with text.

  Let''s get started!

  What is the awk command?

  awk is a scripting language, and it is helpful when ...'
---

In this beginner-friendly guide, you'll learn the very basics of the `awk` command. You'll also see some of the ways you can use it when dealing with text.

Let's get started!

## What is the `awk` command?

`awk` is a scripting language, and it is helpful when working in the command line. It's also a widely used command for text processing.

When using `awk`, you are able to select data – one or more pieces of individual text – based on a pattern you provide.

For example, some of the operations you can do with `awk` are searching for a specific word or pattern in a piece of text given, or even select a certain line or a certain column in a file you provide.

### The Basic Syntax of the `awk` command

In its simplest form, the `awk` command is followed by a set of single quotation marks and a set of curly braces, with the name of the file you want to search through mentioned last. 

It looks something like this:

```
awk '{action}' your_file_name.txt
```

When you want to search for text that has a specific pattern or you're looking for a specific word in the text, the command would look something like this:

```
awk '/regex pattern/{action}' your_file_name.txt
```

### How to create a sample file

To create a file in the command line, you use the `touch` command. 
For example: `touch filename.txt` where `filename`, is the name of your file.

You can then use the `open` command (`open filename.txt`), and a word processor program like TextEdit will open where you can add the contents of the file.

So, say you have a text file, `information.txt`, that contains data separated into different columns. 

The file contents could look something like this:

```
fristName       lastName        age     city       ID

Thomas          Shelby          30      Rio        400
Omega           Night           45      Ontario    600
Wood            Tinker          54      Lisbon     N/A
Giorgos         Georgiou        35      London     300
Timmy           Turner          32      Berlin     N/A
```

In my example, there is one column for `firstName`, `lastName`, `age`, `city`, and `ID`.

At any time, you can view the output of the contents of your file by typing `cat text_file`, where `text_file` is the name of your file.

### How to print all the contents of the file using `awk`

To print *all* the contents of a file, the action you specify inside the curly braces is `print $0`.

This will work in exactly the same way as the `cat` command mentioned previously.

```shell
awk '{print $0}' information.txt
```

Ouptut:

```
fristName       lastName        age     city       ID

Thomas          Shelby          30      Rio        400
Omega           Night           45      Ontario    600
Wood            Tinker          54      Lisbon     N/A
Giorgos         Georgiou        35      London     300
Timmy           Turner          32      Berlin     N/A
```

If you would like each line to have a line-number count, you would use the `NR` built-in variable:

```shell
awk '{print NR,$0}' information.txt 
```

```
1 fristName     lastName        age     city       ID
2 
3 Thomas        Shelby          30      Rio        400
4 Omega         Night           45      Ontario    600
5 Wood          Tinker          54      Lisbon     N/A
6 Giorgos       Georgiou        35      London     300
7 Timmy         Turner          32      Berlin     N/A

```


### How to print specific columns using `awk`

When using `awk`, you can specify certain columns you want printed.

To have the first column printed, you use the command:

```shell
awk '{print $1}' information.txt
```

Ouput:

```
Thomas
Omega
Wood
Giorgos
Timmy
```

The `$1` stands for the first field, in this case the first column.

To print the second column,you would use `$2`:

```shell
awk '{print $2}' information.txt
```

Output:

```
lastName

Shelby
Night
Tinker
Georgiou
Turner
```

The way `awk` determines where each column starts and ends is with a space, by default.

To print more than one column, for example the first and forth columns, you would do:

```shell
awk '{print $1, $4}' information.txt
```

Ouput:

```
fristName city
 
Thomas    Rio
Omega     Ontario
Wood      Lisbon
Giorgos   London
Timmy     Berlin
```

The `$1` represents the first input field (first column), and the `$4` represents the forth. You separate them with a comma, `$1,$4`, so the output has a space and is more readable.

To print the last field (the last column), you can also use `$NF` which represents the *last* field in a record:

```shell
awk '{print $NF}' information.txt 
```

Output:

```
ID

400
600
N/A
300
N/A
```


### How to print specific lines of a column

You can also specify the line you want printed from your chosen column:

```shell
awk '{print $1}' information.txt | head -1 
```

Ouput:

```
FirstName
```

Let's break that command down. `awk '{print $1}' information.txt` prints the first column. Then the output of that command (which you saw earlier on) is *piped*, using the pipe symbol `|`, to the head command, where its `-1` argument selects the first line of the column.

If you wanted two lines printed, you'd do:

```shell
awk '{print $1}' information.txt | head -2 
```


Output:

```
FirstName
Dionysia
```

### How to print out lines with a specific pattern in `awk`

You can print a line that **starts** with a specific letter.

For example:

```shell
awk '/^O/' information.txt
```

Output:

```
Omega           Night           45      Ontario    600
```

That command selects any line with text that *starts* with an `O`. 

You use the up arrow symbol (`^`) first, which indicates the beginning of a line, and then the letter you want a line to start with.

You can also print a line that **ends** in a specific pattern:

```shell
awk '/0$/' information.txt 
```

Output:

```
Thomas          Shelby          30      Rio        400
Omega           Night           45      Ontario    600
Giorgos         Georgiou        35      London     300
```

This prints out the lines that end in a `0` – the `$` symbol is used after a character to siginify how a line will end.

That command could also be changed to:

```shell
awk '! /0$/' information.txt 
```

The `!` is used as a `NOT`, so in this case it selects the lines that DON'T end in a `0`.

```
fristName       lastName        age     city       ID

Wood            Tinker          54      Lisbon     N/A
Timmy           Turner          32      Berlin     N/A
```

#### How to use regular expressions in `awk`

To output words that contain certain letters and print out words that match a pattern you specify, you again use the slashes, `//`, shown previously.

If you want to look for words containing `on`, you'd do:

```shell
awk ' /io/{print $0}' information.txt 
```

Output:

```
Thomas          Shelby          30      Rio        400
Omega           Night           45      Ontario    600
Giorgos         Georgiou        35      London     300
```

This matches all entries that contain `io`.


Say you had an extra column – a `department` column:

```
fristName       lastName        age     city       ID   department

Thomas          Shelby          30      Rio        400  IT
Omega           Night           45      Ontario    600  Design
Wood            Tinker          54      Lisbon     N/A  IT
Giorgos         Georgiou        35      London     300  Data
Timmy           Turner          32      Berlin     N/A  Engineering
```

To find all the information of people working in `IT`, you would need to speficy the string you're searching for between the slashes, `//`:

```shell
awk '/IT/' information.txt 
```

Output:

```
Thomas          Shelby          30      Rio        400  IT
Wood            Tinker          54      Lisbon     N/A  IT
```

What if you wanted to see only the first and last names of the people working in `IT`?

You can specify the column like such:

```shell
awk '/IT/{print $1, $2}' information.txt 
```

Output:

```
Thomas Shelby
Wood   Tinker
```

This will only display the first and second columns where `IT` appears, instead of presenting all fields.

When searching for words with a specific pattern, there may be times when you'll need to use an escape character, like such:

```shell
awk '/N\/A$/' information.txt 
```

Output:

```shell
Wood            Tinker          54      Lisbon     N/A
Timmy           Turner          32      Berlin     N/A
```

I wanted to find lines that end with the pattern `N/A`. 

So, when searching between the `' // '` like shown so far, I had to use an escape character (`\`) between `N/A`, otherwise I would've gotten an error.


### How to use comparisson operators in `awk`

If, for example, you wanted to find all the information of employees that were under the age of `40`, you would use the `<` comparisson operator like so:

```shell
awk '$3 <  40 { print $0 }' information.txt
```

Output:

```
Thomas          Shelby          30      Rio        400
Giorgos         Georgiou        35      London     300
Timmy           Turner          32      Berlin     N/A
```

The output shows only the information of people under 40.

## Conclusion

And there you have it! You now know the absolute basics to start working with `awk` and manipulate text data.

To learn more about Linux, freeCodeCamp has a wide variety of learning materials available. 

Here are a couple of them get you started:

- [Linux Basics - Hands-On Workshop](https://www.youtube.com/watch?v=0Qnwqe2P3eY)
- [Linux for Ethical Hackers (Kali Linux Tutorial)](https://www.youtube.com/watch?v=lZAoFs75_cs&t=77s)
- [The Linux Command Handbook](https://www.freecodecamp.org/news/the-linux-commands-handbook/)


Thanks for reading and happy learning 😊




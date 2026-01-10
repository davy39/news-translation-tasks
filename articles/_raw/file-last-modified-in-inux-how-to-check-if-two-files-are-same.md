---
title: What is Checksum? How to Check if a File was Modified Using the cksum Command
  in Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-07-19T15:33:13.000Z'
originalURL: https://freecodecamp.org/news/file-last-modified-in-inux-how-to-check-if-two-files-are-same
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Copy-of-Cast-a-Function-in-SQL---Convert-Char-to-Int-SQL-Server-Example.gif
tags:
- name: command line
  slug: command-line
- name: information security
  slug: information-security
- name: Linux
  slug: linux
seo_title: null
seo_desc: "When you are working with files on the command line, you might need to\
  \ check their modification time and content integrity. \nLinux has a powerful command\
  \ line which allows you to explore multiple aspects of files and filesystems.\n\
  In case you need to ..."
---

When you are working with files on the command line, you might need to check their modification time and content integrity. 

Linux has a powerful command line which allows you to explore multiple aspects of files and filesystems.

In case you need to check if file was modified, you can follow these two approaches:

## How to Check if a File Was Modified by Checking Modification Time

When a file is edited, its timestamp changes to match the modification time.

We can view the last modified time of a file using long listing( `ls -l`).

In the output below, we can see that the file was modified on `Jul 19 13:22`.

```bash
zaira@Zaira:~$ ls -lrt | grep calculator.py
-rw-r--r--  1 zaira zaira  263 Jul 19 13:22 calculator.py
```

## How to Check if a File Was Modified by Checking File Size

If we know the previous size of the file, we can compare it with the current file size to see if was changed.

We can view the file size using long listing( `ls -l`). The 5th column shows the size of the file in bytes.

```bash
zaira@Zaira:~$ ls -lrt | grep calculator.py
-rw-r--r--  1 zaira zaira  263 Jul 19 13:22 calculator.py
```

The methods mentioned above usually get the task done, but there is an advanced method to check file integrity using a hash. The method is called 'checksum' and the corresponding command for that in Linux is `cksum`.

## What is Checksum in Linux?

Sometimes the data gets corrupted during transmission or storage. To ensure that the data remains consistent, we can use checksum. 

Checksum is the result of an algorithm called a cryptographic hash function. It's applied to blocks of the data in the file. 

In networking, you can use checksum to compare the hash value at sender and receiver ends. If the hash value is same, it implies that your copy of the file is genuine and error free.

Some commonly used cryptographic hash functions include MD5 and SHA-1.

Next we will see how we can calculate the hash in Linux.

## How to Find the Checksum in Linux using `cksum`

**`cksum`** is a command found in *nix-like operating systems that generates a checksum value for a file or stream of data. 

According to the man page of `cksum`, the command prints CRC (cyclic redundancy check) checksum and byte counts of each FILE.

To learn more about the CRC algorithm, refer to [this](https://www.tutorialspoint.com/what-is-algorithm-for-computing-the-crc) page.

### Syntax of `cksum`

The `cksum` command takes the filename as an argument and generates its hash value. The basic syntax is as follows:

```bash
cksum [FILE]
```

### How to Use `cksum`

Let's suppose we have a file named `calculator.py`. We can calculate its checksum like this:

```bash
zaira@Zaira:~$ cksum calculator.py
1991291549 262 calculator.py
```

In the output, we get three columns:

* The first column is the hash value.
* The second value is the amount of data in bytes for the given file.
* The third column is the file name.

Even a slight modification changes the hash value. Let's see how that looks with an example.

Let's modify our original file `calculator.py` by adding an extra line at the end:

```bash
zaira@Zaira:~$ echo >> "this file is now changed" >> calculator.py
```

Let's calculate the checksum again and see if the hash value has changed:

```bash
zaira@Zaira:~$ cksum calculator.py
331872555 263 calculator.py
```

The first column is the hash value and it has changed since we appended the text.

Now we know that the file has changed as the checksum hash values are no longer the same.

We can use the same method to compare files with the same name, size, and modification time across different machines to ensure that both files are the same. 

## Conclusion

There are cases when you need to compare the files across systems, specially when they are transferred from one location to the other. We can use a combination of the three methods to verify if our file is intact:

* Viewing the file modification time.
* Verifying the file size.
* Generating and comparing the hash value using `cksum` .

I hope you found this tutorial helpful. Thank you for reading till the end.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can also read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).


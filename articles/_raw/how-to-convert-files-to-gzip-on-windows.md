---
title: How to Compress Files to ".gz" on the Windows Operating System
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2024-03-01T19:15:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-files-to-gzip-on-windows
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/freeCodeCamp---Fahim.png
tags:
- name: compression
  slug: compression
- name: Windows
  slug: windows
seo_title: null
seo_desc: "You may often need to compress files and folders for various reasons. And\
  \ \"Gzip\" compression is a good choice for many scenarios. \nRecently, I have faced\
  \ an issue where I needed to compress a lot of files individually, and manual intervention\
  \ to comp..."
---

You may often need to compress files and folders for various reasons. And "Gzip" compression is a good choice for many scenarios. 

Recently, I have faced an issue where I needed to compress a lot of files individually, and manual intervention to compress each file one by one using traditional 7zip became a hassle.

If you are in love with the Windows operating system like I am (I know, I know, sometimes Windows can become quite a pain. Maybe I like the pain and also like to resolve issues all by myself, who knows!), then you may also face issues in batch processing compressing multiple files to the `.gzip` format.

There are multiple ways to compress a file into the `.gzip` format. The main issue is that most of the ways do not support batch processing the conversion. In this article, I will talk about two of the decent ways you can do this.

## Method 1: Using 7zip (No Batch Processing)

[7zip](https://www.7-zip.org/) is a free software available for Windows, Linux, and ARM64. Installing 7zip in the Windows operating system is very simple and straightforward.

If you simply want to compress any single file to `.gzip` format, you need to simply select that file and add it to the 7zip archive. In the GUI, you can select the Archive format as "gzip" and that's it!

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-21_12-36.png)
_gzip in 7zip_

## Method 2: Using `gzip` from Chocolatey (Batch Processing is the Main Benefit of This)

There are several tools that we can use to compress files and folders on our computers. However, Linux-based operating systems come with a lot of tools and there are a lot of CLI (Command Line Interface) type tools that we can also use to compress multiple files altogether in a batch. 

If you use Linux based operating system, then you might have also used GZip. Gzip is a file format and software application that compresses and decompresses files. It also makes files smaller and allows for faster network transfers. However, there are not any official installers of GZip for the Windows operating system.

But, we can install "gzip" directly on Windows and work like we're in a Linux OS. I prefer to download GZip via [Chocolatey](https://chocolatey.org/), a very good package manager for the Windows operating system. 

> Chocolatey is a machine-level, command-line package manager and installer for software on Microsoft Windows. It uses the NuGet packaging infrastructure and Windows PowerShell to simplify the process of downloading and installing software.

If you are using Chocolatey for the first time, then you need to install it first. All of the methods are explained in detail on their official website: [https://chocolatey.org/install](https://chocolatey.org/install).

![Image](https://www.freecodecamp.org/news/content/images/2024/02/2024-02-21_12-48.png)
_Chocolatey Installation_

Open your Terminal and run the command for installing "gzip".

```powershell
choco install gzip
```

Write "Yes" when it asks for your permission. After a few seconds, you should be ready to use it.

Let's say I want to batch-compress a lot of files into ".gzip". I can open my terminal and go to that directory (where my raw files are that I want to compress using gzip) using the `cd path/to/where/I/have/the/files` command. 

Or, I can simply open my terminal directly using the "Open In Terminal" context menu in that specific directory where I have the files that I want to compress using gzip. Then I can simply use the following command.

```powershell
gzip * -r
```

This will iterate through every folder and subfolder in that specific location and compress all of the files to `.gzip` recursively (the `-r` flag). Keep in mind that it will **replace** all your files to `.gzip` in that directory.

**But**, if you also want to keep the original files side by side during the batch compression process, you can use the command below.

```bash
gzip * -r -k
```

Here, the `-k` flag indicates the `--keep` option to keep the original files.

**If** you want to use all your CPU cores in parallel, then follow the command below.

```bash
parallel gzip ::: *
```

You have to add the necessary suffixes to suit your needs obviously in this process.

That's it!

## Conclusion

I hope you have gained some valuable insights from this article.

If you have enjoyed the procedures step-by-step, then don't forget to let me know on [Twitter/X](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/). I would appreciate it if you could endorse me for some relevant skillsets of mine on [LinkedIn](https://www.linkedin.com/in/fahimfba/).

You can follow me on [GitHub](https://github.com/FahimFBA) as well if you are interested in open source. Make sure to check [my website](https://fahimbinamin.com/) ([https://fahimbinamin.com/](https://fahimbinamin.com/)) as well.

Thank you so much!


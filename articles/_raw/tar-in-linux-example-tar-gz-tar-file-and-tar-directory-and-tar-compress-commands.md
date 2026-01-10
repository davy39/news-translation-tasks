---
title: Tar in Linux – Tar GZ, Tar File, Tar Directory, and Tar Compress Command Examples
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-02T17:57:00.000Z'
originalURL: https://freecodecamp.org/news/tar-in-linux-example-tar-gz-tar-file-and-tar-directory-and-tar-compress-commands
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/tar-article.jpg
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'Do you want to combine a bunch of files and directories into a single file?
  The tar command in Linux is what you''re looking for!

  The tar command is used to compress a group of files into an archive. The command
  is also used to extract, maintain, or m...'
---

Do you want to combine a bunch of files and directories into a single file? The `tar` command in Linux is what you're looking for!

The `tar` command is used to compress a group of files into an archive. The command is also used to extract, maintain, or modify tar archives.

Tar archives combine multiple files and/or directories together into a single file. Tar archives are not necessarily compressed but they can be. Permissions are preserved and it supports many compression formats.

Learn how to use `tar` in this quick article.

## Syntax

`tar [options] [archive-file] [file or directory to be archived]`

**Options:**  
**-c :** Creates archive  
**-x :** Extracts the archive  
**-f :** creates archive with given filename  
**-t :** displays or lists files in archived file  
**-u :** archives and adds to an existing archive file  
**-v :** Displays verbose information  
**-A :** Concatenates the archive files  
**-z :** compresses the tar file using gzip  
**-j :** compresses the tar file using bzip2  
**-W :** Verifies an archive file  
**-r :** updates or adds file or directory in already existing .tar file

## Usage Examples

**Extract an archive:**  
`tar xfv archive.tar`  
(Options: x = extract, f = file, v = verbose)

**Create an archive with files or folder:**  
`tar cfv archive.tar file1 file2 file3`  
(Options: c = create)

**Create compressed archives:**  
`tar cfzv archive.tar file1 file2 file3`   
(Options: z = compress with gzip)

**Show all files of an archive:**  
`tar tvf archive.tar` 

**Create an uncompressed archive of all .txt files in current directory:**  
`tar cfv archive.tar *.txt`

**Extract files from gzip tar Archive archive.tar.gz:**  
`tar xvzf archive.tar.gz`

**Create a compressed tar archive file using bzip2:**  
`tar cvfj archive.tar.tbz example.cpp`  
(Options: j = compress with bzip2, smaller file size but takes longer than `-z`)

**Update existing tar file by adding todo.txt file to archive:**  
`tar rvf archive.tar todo.txt`  
(Options: r = add file)

**List contents of tar file:**  
`tar tf file.tar`  
(Options: t = display, f = file)

**Create a compressed archive of current directory but exclude certain directories:**  
`tar --exclude='./folder' --exclude='./upload/folder2' cfzv archive.tar .`("folder" and "folder2" are excluded)


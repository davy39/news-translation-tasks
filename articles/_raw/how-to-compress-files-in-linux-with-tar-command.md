---
title: Linux tar Command – How to Compress Files in Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2021-10-06T16:19:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-compress-files-in-linux-with-tar-command
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Linux-File-Tar-Compression.png
tags:
- name: compression
  slug: compression
- name: data compression
  slug: data-compression
- name: Linux
  slug: linux
seo_title: null
seo_desc: "File compression is an essential utility across all platforms. It helps\
  \ you reduce file size and share files efficiently. And compressed files are also\
  \ easier to copy to remote servers. \nYou can also compress older and rarely used\
  \ files and save them..."
---

File compression is an essential utility across all platforms. It helps you reduce file size and share files efficiently. And compressed files are also easier to copy to remote servers. 

You can also compress older and rarely used files and save them for future use which helps you conserve disk space.

In this post, we'll look at how to compress files with the `tar` command in Linux, along with some examples of `tar` in action.

## What is the tar command?

We use the `tar` command to compress and expand files from the command line. The syntax is shown below:

```bash
tar [flags] destinationFileName sourceFileName
```

 The `tar` command uses the following flags to customize the command input:

<table>
<thead>
<tr>
<th>Flag</th>
<th>Explanation</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr>
<td>-c</td>
<td>Create a new archive.</td>
<td>We use this flag whenever we need to create a new archive.</td>
</tr>
<tr>
<td>-z</td>
<td>Use gzip compression.</td>
<td>When we specify this flag, it means that archive will be created using gzip compression.</td>
</tr>
<tr>
<td>-v</td>
<td>Provide verbose output.</td>
<td>Providing the -v flag shows details of the files compressed.</td>
</tr>
<tr>
<td>-f</td>
<td>Archive file name.</td>
<td>Archive file names are mapped using the -f flag.</td>
</tr>
<tr>
<td>-x</td>
<td>Extract from a compressed file.</td>
<td>We use this flag when files need to be extracted from an archive.</td>
</tr>
</tbody>
</table>

### How to create an archive

We have a list of the following files which we'll compress with `tar`.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-1.png)
_List of files to be compressed._

To compress them, we'll use `tar` like this:

```bash
tar -czvf logs_archive.tar.gz *
```

Let's break down this command and look into each flag.

`-c` is creating and archive.

`-z` is using gzip compression.

`-v` is providing details of the files that have been archived.

`-f` is creating an archive with the name 'logs_archive.tar.gz' as supplied in the command above.

In the results below, we can see that the archive has been created successfully.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-13.png)
_Archive has been created with supplied command._

### How to remove files after compression

Let's say we don't want to keep the original files after creating an archive. For that, we can use the `--remove-files` flag.

```bash
tar -czvf logs_archive.tar.gz * --remove-files
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-3.png)
_Files removed once archive has been created_

Here, the `-czvf` flags are working as demonstrated before, but the original files are also removed. Once we list the files, we only see the archive.

### How to view the contents of an archive

You might need to view the contents of an archive without actually extracting it. You can do this with the `-t` flag.

```bash
tar -tvf logs_archive.tar.gz
```

In this command, `-t` flag specifies that we need to only view the contents of the archive. `-f` specifies the filename and `-v` displays the detailed contents.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-4.png)
_Viewing contents of an archive._

### How to extract an archive

To extract files from an archive, you use the `-x` flag like this:

```bash
tar -xzvf logs_archive.tar.gz
```

Let's break down this command and look into each flag.

`-x` is extracting and archive.

`-z` specifies that the archive is gzip.

`-v` is providing details of the files that have been archived.

`-f` is extracting from the archive named 'logs_archive.tar.gz'.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-14.png)
_Extracting an archive._

Here's a useful tip: commands that take a long time to execute can continue in the background with `&`. 

Adding files to an archive and extracting an archive can take a while. To keep the commands running in the background while you keep working, pair the command with `&` like this:

```bash
tar -xzvf logs_archive.tar.gz &
```

### How to search in compressed log files

You might still need to access certain files once they're archived. Luckily, there is a method you can use to search and view compressed log files without decompressing them and compromising disk space.

The command you can use to search in compressed files is `zgrep`:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-6.png)
_Contents of a file 'audit.log' in an archive._

We can search for a string in an archive using the below command:

```bash
 zgrep -Hna 'string-to-search' compressedFile.tar.gz
```

Let's briefly look at the flags.

`-H` lists the file name that contains the match.

`-n` displays the line number that contains the matched string.

`-a` treats all files as text files. 

This is the result:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-15.png)

## Wrapping Up

File compression helps us save time and resources when sharing files. Servers are almost always rotating and archiving huge log files. 

You can also schedule file compression via `cron` jobs to automate disk cleaning. I highly recommend that you take advantage of this utility.

Thanks for reading until the end. I would love to connect with you. You can find me [here](https://twitter.com/hira_zaira) on Twitter. Do share your thoughts.

See you around.





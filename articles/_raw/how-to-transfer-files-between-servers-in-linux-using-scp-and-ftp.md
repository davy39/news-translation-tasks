---
title: How to Transfer Files Between Servers in Linux using SCP and FTP
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2021-12-20T16:02:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-transfer-files-between-servers-in-linux-using-scp-and-ftp
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Transfer-files-FTP-and-SCP.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Transferring files between machines is a very common operational task that\
  \ you'll do all the time as a developer. \nLinux provides a number of utilities\
  \ to transfer files. In this tutorial we will discuss FTP and SCP. Many automated\
  \ scripts also deplo..."
---

Transferring files between machines is a very common operational task that you'll do all the time as a developer. 

Linux provides a number of utilities to transfer files. In this tutorial we will discuss `FTP` and `SCP`. Many automated scripts also deploy FTP or SCP to move files.

## What is FTP?

FTP is a network protocol used for exchanging files over the network. It uses port 21. FTP enables you to access a remote system for exchanging files using the `ftp` command.

### FTP Syntax

FTP syntax is as below:

```bash
ftp host
```

Here, `host` can either be the hostname or IP address of the remote host.

### FTP Commands

FTP commands are similar to Linux commands. We'll discuss some of these.

<table>
<thead>
<tr>
<th>Command</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr>
<td>open</td>
<td>Opens a remote connection with another computer.</td>
</tr>
<tr>
<td>get</td>
<td>Copies a file from the remote system to the local system.</td>
</tr>
<tr>
<td>put</td>
<td>Copies a file from the local system to a directory on the remote system.</td>
</tr>
<tr>
<td>mget</td>
<td>Transfers multiple files from the remote system to the local system’s current directory.</td>
</tr>
<tr>
<td>mput</td>
<td>Transfers multiple files from the local system to a directory on the remote system.</td>
</tr>
<tr>
<td>bye/quit</td>
<td>Prepares to exit the FTP environment.</td>
</tr>
<tr>
<td>close</td>
<td>Terminates the FTP connection.</td>
</tr>
<tr>
<td>ascii</td>
<td>Enables file transfer mode to ASCII</td>
</tr>
<tr>
<td>binary</td>
<td>Enables file transfer mode to binary.</td>
</tr>
</tbody>
</table>

### How to Transfer Files via FTP

FTP offers two transfer modes: ASCII and Binary.

1. **ASCII stands for **American Standard Code for Information Interchange**.** It is used to transfer plain files such as text files.
2. **Binary mode**: Binary mode is used to transfer non-text files such as images.

The default transfer mode is ASCII.

#### Step 1 – Connect to FTP

In the example below, `hostA` is the remote host. You will be prompted for a username and password.

```bash
$ ftp hostA
Connected to hostA.
220 hostA FTP server ready.
Name (hostA:user): user
331 Password required for user.
Password: password
230 User user logged in.
Remote system type is LINUX.

```

Once the connection is successful, you'll notice the `ftp>` symbol in the beginning. Now we can run the FTP commands.

#### Step 2 – Choose file transfer mode

You can choose the mode (binary or ASCII) depending on your file type.

```bash
ftp> ascii
200 Type set to A.
```

#### Step 3 – Transfer files

We use the `get` command to transfer the file `sample.txt` from remote FTP server to local machine.

```bash
ftp> get sample.txt
200 PORT command successful.
150 Opening ASCII mode data connection for sample.txt (22 bytes).
226 Transfer complete.
local: sample.txt remote: sample.txt
22 bytes received in 0.012 seconds (1.54 Kbytes/s)
```

#### Step 4. End the session

```bash
ftp> bye
221-You have transferred 22 bytes in 1 files.
221-Total traffic for this session was 126 bytes in 2 transfers. 221-Thank you for using the FTP service on hostA.
221 Goodbye.
```

### How to Transfer Multiple Files via FTP

To transfer files in bulk, there are two commands: `mget` and `mput`.

You use `mget` to download the files, whereas you use `mput` to upload the files.

```bash
ftp> mget sample_file.1 sample_file.2
```

```bash
ftp> mput sample_file.1 sample_file.2
```

All the steps we just learned can be placed in an executable file and be scheduled. You can find the code for automation [here](https://github.com/zairahira/FTP-Automation-Script).

## What is SCP?

SCP stands for Secure Copy. It uses SSH and port 22. The data transferred through SCP is encrypted and sniffers can't access it. This makes SCP very secure.

You can use SCP to:

* Transfer files from local machine to remote host.
* Transfer files from remote host to local machine.

### SCP syntax

Let's explore the syntax of SCP.

```bash
scp [FLAG] [user@]SOURCE_HOST:]/path/to/file1 [user@]DESTINATION_HOST:]/path/to/file2

```

* `[FLAG]` specifies the options that can be given to SCP. Here are some details about flags:

<table>
<thead>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>-r</td>
<td>To recursively copy directories.</td>
</tr>
<tr>
<td>-q</td>
<td>Used to hide the progress meter and any other info other than errors.</td>
</tr>
<tr>
<td>-C</td>
<td>Used to compress the data when sending it to its destination.</td>
</tr>
<tr>
<td>-P</td>
<td>Specifies the destination SSH port.</td>
</tr>
<tr>
<td>-p</td>
<td>Preserves file access times.</td>
</tr>
</tbody>
</table>

* `[user@]SOURCE_HOST` is the source machine.
* `[user@]DESTINATION_HOST:]` is the destination machine.

**Note**: _To transfer files via SCP, credentials must be known and the user should have the permissions to write_.

### How to Transfer Files from Local Machine to Remote Host via `SCP`

To transfer files to a remote host, use the command below:

```bash
scp source_file.txt remote_username@10.13.13.11:/path/to/remote/directory
```

In the command above, `source_file.txt` is the file to be copied. `Remote_username` is the username for remote host `10.13.13.11`. After `:` the destination path is specified.

Sample output:

```bash
remote_username@10.13.13.11's password:
source_file.txt                             100%    0     0.0KB/s   00:00

```

The file `source_file.txt` will now be placed in `/path/to/remote/directory`.

To copy directories, use the `-r` flag as demonstrated below.

```bash
scp -r /local/directory remote_username@10.13.13.11:/path/to/remote/directory
```

### How to Transfer Files from Remote Host to Local Machine via `SCP`

To transfer files from a remote host to a local machine, use the command below:

```bash
scp remote_username@10.13.13.11:/remote/source_file.txt /path/to/local/directory
```

> Be extra careful when transferring files as SCP **overwrites** the already existing files.

## Wrapping up

In this tutorial, you learned how to transfer files and directories using FTP and SCP via command line. 

When automated, these commands serve even greater purposes in data warehousing, ETL (Extract, Transform, Load), reporting, archiving and bulk file processing. Do give these commands a try. Let's connect on [Twitter](https://twitter.com/hira_zaira).


---
title: SCP Linux Command – How to SSH File Transfer from Remote to Local
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2021-09-21T21:41:38.000Z'
originalURL: https://freecodecamp.org/news/scp-linux-command-example-how-to-ssh-file-transfer-from-remote-to-local
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/uide-to-writting-a-good-readme-file--3-.png
tags:
- name: File sharing
  slug: file-sharing
- name: information security
  slug: information-security
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'Whenever you''re working with computers or any electronic device that has
  storage capacity, you might need to distribute or share information and files in
  various ways.

  Some of the most commonly shared files include audio files, images, videos, pdfs
  o...'
---

Whenever you're working with computers or any electronic device that has storage capacity, you might need to distribute or share information and files in various ways.

Some of the most commonly shared files include audio files, images, videos, pdfs or any form of word documents.

Most of the time, the information being shared will be private or confidential – meaning it's meant for a specific person or a group of people, so protecting it is essential.

When it comes to devices like mobile phones we have app the facilitate the transfer of files like xender, appshare or even sometimes the use of bluetooth. Now, when it comes to computers the case is not different we have softwares and even sites that facilitate the same.

When it comes to sharing data in operating systems like Linux, there are multiple commands you can choose from to share information. But today we'll be focusing on the **SCP** command. It lets you share files and data securely and easily.

In today's market gap, having Linux skills is very essential and helpful more so if you are a system administrator. As a system admin sharing of data will be among your day to day activity and you will need the data being shared to be safe, and by using SCP command you will be able to achieve this.

Before we get started, let's begin by understanding what SCP is, and then we'll learn some commands you can use for file transfer.

## What are SCP Commands?

SCP is an acronym for Secure Copy Protocol. It is a command line utility that allows the user to securely copy files and directories between two locations usually between unix or linux systems.

The protocol ensures the transmission of files is encrypted to prevent anyone with suspicious intentions from getting sensitive information.

In simpler words we can say that SCP is a safer option for the `cp` (_copy_) command.

It is also important to note that SCP uses encryption over an SSH (Secure Shell) connection, this ensures that the data being transferred is protected from suspicious attacks.

## SCP Syntax

Just like any other commands used in the terminal, the SCP also have a format that is used for a successful execution to happen. By understanding the syntax it makes it easier for you to write down the commands:

```bash
scp [OPTIONS] [[user@]src_host:]file1 [[user@]dest_host:]file2

```

* `scp` - It initializes the command and ensures a secure shell is in place.
* `OPTIONS` - They grant different permissions depending on how they have been used. Some of the most common options include:
* **P**(Caps) - specifies the port to establish connection with the remote host.
* **p**(lowercase) - preserves the times-tamp for ease of modification and access.
* **r** - copies the entire directory recursively
* **q** - copies files quietly, doesn't display the progress messages. Also known as quiet mode.
* **C** - for compression of data during transmission.  
To understand more about OPTIONS read [scp options](https://linux.die.net/man/1/scp)
* `src_host` - where the file is hosted. The source can either be a client or server depending on the origin of the file.
* `dest_host` - where the file will be copied to.

Since we are dealing with file transmission, it definitely means that there have to be an involvement of more than one machine to make the process possible. We are able to use SCP in the following cases:

* Copy files within same machine.
* Copy files from a local host to remote host and vice versa.
* Copy files between two different remote servers.

At this point, it will be fair to state that before you use any SCP commands you will need to have a few things in place:

* SSh installed on both the client and the server machines.
* Root access to both client and server machines.

With two thing's ready you are good to go. Let's get started by seeing the commands in action.

## Common SCP Commands

### Copy File From Local Host to Remote Server

When copying files, being able to transfer files/data from local storage to remote server is very essential. When using the SCP commands you will need to specify a few things for this to happen.

You will have to specify the path to the file as the source and also specify the remote host path, where the files are being copied to.

Let's take a scenario where we have a file `test.txt` and we need to copy it to a remote server, our command will look like below:

```
scp test.txt userbravo@destination:/location2

```

We are not limited to the number of files we can copy. Let's say we are on our desktop in the folder called web where we have `.php` file extensions and we need to copy the to remote server home directory. Our command will look like:

```
scp *.php userbravo@destination_host:/~/

```

***.php** - copies all the files with the .php extension in the currently specified folder.  
**/~/** - means copy them to the home directory.

Let's say you wanted to copy a file named test.txt and save it with a different name in the remote server this time round using an option of port. The command will be:

```
scp -P 8080 test.txt userbravo@destination_host:/user/home/test2.txt

```

In this example we have copied a file test.txt from local machine into remote where it will be saved as test2.txt using port 8080.

### Copy Files From Remote to Local

A better way to understand this is by use of an example. Take a scenario where you want to copy files from remote system. To copy the files you will need to first invoke the SCP, followed by the remote username@IP address, path to file.

If you do not specify the path, it is assumed as default in this case which will be the user's home directory, this will be followed the path where the file will be stored locally.

**The Syntax**

```
scp <remote_username>@<IPorHost>:<PathToFile>   <LocalFileLocation>

```

Let's say I wanted to copy a file named _linuxcheatsheet_ from the remote device with this address _192.168.1.100_.

The _linuxcheatsheet_ file is stored on the kali user’s home directory, the user I will authenticate. Therefore after the colon, I don’t need specify the path because it's the default one, which is the home directory, and I just type the filename (“linuxcheatsheet”). Then, I specify the current directory as the local location to store the file by typing a dot.

```
scp lary@192.168.1.100:linuxcheatsheet .
```

### Copy Files From Remote Host to Another

The beauty of using SCP in file transferring, is that it does not only allow connection between local machines but also it allows for you to connect to remote servers.

Let's say we wanted to copy a file named test.txt, to another remote server the command would look like below:

```
scp user1@host1.com:/files/test.txt user2@host2.com:/files
```

What this command will do is copy test.txt from files folder in the the user1 and create a replicate of it in user2 which runs on _host2.com_ still on the files folder.

### Copying Multiple Files

When copying multiple files, all you need to do is specify the file name as the source path. for example.

**The Syntax**

```
scp file1 file2 ... user@<ip_address_of_user>: Destination

```

Let's say we wanted to copy files 1,2,3 and 4. The command would look like below:

```
scp file1.txt file2.txt file3.txt file4.txt user1@host1.com:/home/user1/Desktop
```

## Takeaway Points:

* To be able to copy files, you must have read permissions on the source file and write permission on the target system.
* The SCP command relies on SSH for secure data transfer, meaning it requires a password to authenticate on remote systems.
* Watch out when copying files with the same name and location, as SCP will overwrite them without warning you.
* To be able to distinguish between local and remote locations, use full colon **:**.

## Wrap Up

Whether you are a support engineer, system admin, or even a growing developer like myself who uses Linux or wants to learn it – it's likely that you will have to transfer files at some point. And knowing these simple SCP commands will come in handy.

In this article, we have covered some of the most common scenarios where you'd want to use SCP and hopefully you have learned something new.

Enjoy Coding ❤



---
title: RSync Examples – Rsync Options and How to Copy Files Over SSH
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-08T20:54:31.000Z'
originalURL: https://freecodecamp.org/news/rsync-examples-rsync-options-and-how-to-copy-files-over-ssh
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/rsync.png
tags:
- name: ssh
  slug: ssh
seo_title: null
seo_desc: 'Rsync stands for “remote synchronization”. It is a remote and local file
  synchronization tool that helps you efficiently transfer files.

  What RSync Is

  Rsync is faster than tools like Secure Copy Protocol (SCP). It uses the delta-transfer
  algorithm th...'
---

Rsync stands for “remote synchronization”. It is a remote and local file synchronization tool that helps you efficiently transfer files.

## What RSync Is

Rsync is faster than tools like [Secure Copy Protocol (SCP)](https://www.geeksforgeeks.org/scp-command-in-linux-with-examples/). It uses the [delta-transfer](https://www.dynamsoft.com/help/SAW%20Standalone/Getting%20Started/Delta%20Transfer.htm) algorithm that minimizes the data transfer by copying only the sections of a file that have been updated.

Some of the additional features of Rsync include:

* Supports copying links, devices, owners, groups, and permissions
* Does not require super-user privileges
* Pipelines file transfers to [minimize latency costs](https://whatis.techtarget.com/definition/latency)

You can only transfer files from local  to  remote or remote  to  local. Rsync does not support remote  to  remote file transfers.

## How RSync Works

Now that you know what Rsync is, let's look at how to work with it.

Rsync works similarly to other remote server management tools like SSH and SCP.

Here is the basic syntax of Rsync:

```
rsync [options] source [destination]
```

Here is the syntax to transfer a file from your local system to a remote server. It is also called a “push” operation.

```
rsync local_file_path user@remote-host:remote_file_path
```

Here's how to transfer a file from a remote server to your local system, also called a “pull” operation.

```
rsync user@remote-host:remote_file_path local_file_path
```

> Note: When working with remote systems, make sure you have [SSH access to the remote system](https://www.hostinger.in/tutorials/ssh-tutorial-how-does-ssh-work?__cf_chl_jschl_tk__=f550a12fdfece557e30dc21901117b432d5a8e1d-1599060891-0-AQrE-UcUtiSpJOvL7PClSP8WK3uhRkd2Va_WJS_Hr7mHzy4lylrjibVz-sFxPrqTOYzEL8kjWnc_WKPSFQq4_CGDfTHPmPF3uv3IBQyDJnHm3v_FHx9-6uH7IG663DhoKDAdMayU1_iN33sQ5fsuniN5ga8w33sjEXqwdW-0-dKQeXXGPN37aTbwu7NlmtFf8MGAvsqbs2NEFChJ2Mpi9qasX6dy0guXG446JenTxsOz_P3g9wzw1qv8hXZtfC7UOdR4s_guli8xDi_EOuzgNoYVRe2r2nRBQ3jNb0fzLwK5frAhmmbv6LClLgrF5r8NRYqxsBPD4FCXp8wvFo7agjs). Rsync establishes the connection using SSH in order to enable file transfer.

## How to Use Flags in RSync

Rsync lets you add additional options via command-line flags. Let's look at a few useful flags.

### Recursive

If you add the **-r** option, RSync will execute a recursive file transfer. This is useful when working with directories. Here is an example:

```
rsync -r user@remote-host:remote_directory/ local_directory
```

### Archive

The **-a** flag is used to preserve [symbolic links](https://www.geeksforgeeks.org/soft-hard-links-unixlinux/) while transferring files. The archive flag also preserves special and device files, modification times, and permissions from the source directory.

The archive flag also syncs files recursively, so it is used more than the recursive flag. Here is how you use it:

```
rsync -a user@remote-host:remote_directory/ local_directory
```

### Compression

You can also compress files using the **-z** flag. Compressing files can reduce network load and speed up file transfer. 

```
rsync -az user@remote-host:remote_directory/ local_directory
```

### Progress

For large file transfers, it is useful to know the progress of the operation. You can use the **-P** flag to know the progress of the file transfer. With Rsync, you can also resume file transfers if they are interrupted. 

```
rsync -aP user@remote-host:remote_directory/ local_directory
```

### Verbose

Finally, the verbose command can help you understand every step of the file transfer. You can use the **-v** flag for this. 

```
rsync -av user@remote-host:remote_directory/ local_directory
```

You can also use the help command with RSnsc to get a list of all the options and flags. 

```
rsync --help
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-02-at-9.07.47-PM.png)
_rsync help_

## Conclusion

Rsync simplifies the whole file transfer process by offering a robust, versatile, and flexible tool compared to alternatives like SCP. 

RSync is great for maintenance operations, backups, and general file operations between local and remote machines.

## References

* [https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps)
* [https://linux.die.net/man/1/rsync](https://linux.die.net/man/1/rsync)
* [https://www.geeksforgeeks.org/rsync-command-in-linux-with-examples/](https://www.geeksforgeeks.org/rsync-command-in-linux-with-examples/)

I am [Manish](https://www.manishmshiva.com/) and I write about Cybersecurity, Artificial Intelligence, and DevOps. If you liked this article, [you can find my blog here](https://medium.com/manishmshiva).


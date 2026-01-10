---
title: Linux Permissions – How to Find Permissions of a File
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-04-19T21:49:02.000Z'
originalURL: https://freecodecamp.org/news/linux-permissions-how-to-find-permissions-of-a-file
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Copy-of-python-append.png
tags:
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: null
seo_desc: "Linux is a multi-user Operating System which means it supports multiple\
  \ users on a single system. \nEach user has its own rights which might be limited\
  \ as well to increase security. For example, users have a particular set of permissions\
  \ to access a f..."
---

Linux is a multi-user Operating System which means it supports multiple users on a single system. 

Each user has its own rights which might be limited as well to increase security. For example, users have a particular set of permissions to access a file – some users might be able to write while others can only read.

In this tutorial we will learn:

* What are users and groups and the different types of users in Linux..
* Viewing ownerships and permissions. 
* Understanding read, write, and execute permissions.
* Reading permissions through symbolic mode.

## Users and Groups in Linux

Before understanding permissions, we should understand `users` and `groups`, as ownerships and permissions apply to these entities. 

### Users and User types in Linux

There are two types of users: `system users` and `regular users`.

* **System users** are responsible for running non-interactive and background processes on a system. For example: `mail`, `daemon`, `syslog`, and so on.
* **Regular users** are the users that actually log into the system and perform their designated tasks interactively.

We can check details of users on a system by looking into the /etc/passwd file. The first column before `:` shows the username.

```bash
cat /etc/passwd
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-144.png)
_Contents of /etc/passwd file_

### Superuser or the `root` user.

In addition to the two user types, there is the superuser, or `root` user, that has elevated rights. This user has the power create and modify users as well as to override any file ownership and permission. 

Other user accounts can also be configured to have "superuser" rights. The best practice is to allow elevated privilege to regular users using 'sudo'. Users who are able to 'sudo' can also perform the same tasks as the root user.

### Groups in Linux

Users can belong to groups. Groups are a collection of users. A group defines the collective rights for users it contains. A user can belong to more than one group as well. 

We can view groups on a system by viewing the `/etc/group` file.

```bash
cat /etc/group

```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-145.png)
_Contents of `/etc/group` file._

## How to View Ownerships and Permissions in Linux

Now we know about users and groups. Let's see how we can view the permissions of a file or folder.

We can use long listing which is the `ls` command with flag `-l`.

`ls -l`

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-146.png)
_Output of long listing_

Let's have a closer look into the mode column in the output above.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-147.png)
_Mode details in long listing._

**Mode** defines two things:

* **File type:** File type defines the type of the file. For regular files that contain simple data it is blank `-`. For other special file types the symbol is different. For a directory which is a special file, it is `d`. Special files are treated differently by the OS.
* **Permission classes:** The next set of characters define the permissions for user, group, and others respectively.  
– **User**: This is the owner of a file and owner of the file belongs to this class.  
– **Group**: The members of the file’s group belong to this class  
– **Other**: Any users that are not part of the user or group classes belong to this 		 class.

### How to Read Symbolic Permissions

The `rwx` representation is known as the Symbolic representation of permissions. In the set of permissions, 

* **`r`** stands for **read**. It is indicated in the first character of the triad.
* **`w`** stands for **write**. It is indicated in the second character of the triad.
* **`x`** stands for **execution**. It is indicated in the third character of the triad.

## Understanding symbolic permissions

### Read

For regular files, read permissions allow the file to be opened and read only. Users can't modify the file. 

Similarly for directories, read permissions allow the listing of directory content without any modification in the directory.

### Write

When files have write permissions, the user can modify (edit, delete) the file and save it. 

For folders, write permissions enable a user to modify its contents (create, delete, and rename the files inside it), and modify the contents of files that the user has write permissions to.

### Execute

For files, execute permissions allows the user to run an executable script. For directories, the user can access them, and access details about files in the directory.

## Examples of Permissions in Linux

Now we know how to read permissions. Let's see some examples.

* `-rwx------`: A file that is only accessible and executable by its owner.
* `-rw-rw-r--`: A file that is open to modification by its owner and group but not by others.
* `drwxrwx---`: A directory that can be modified by its owner and group.

## Wrapping up

In this tutorial we have learned about users and groups in Linux. We have also learned how to read and view permissions. 

It is important to understand these permissions as they are a critical part of system administration.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).


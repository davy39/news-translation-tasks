---
title: File Permissions in Linux – How to Use the chown and chgrp Commands
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-01-13T16:25:20.000Z'
originalURL: https://freecodecamp.org/news/file-permissions-in-linux-how-to-use-the-chown-chgrp-command-s
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/BB---Manage-Users-and-Groups-in-Linux.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "When it comes to large organizations, Users and Groups in Linux play an\
  \ important role in helping keep systems secure and properly functioning. \nThere\
  \ can be different levels of users in an organization with different roles and permissions.\
  \ And you'l..."
---

When it comes to large organizations, Users and Groups in Linux play an important role in helping keep systems secure and properly functioning. 

There can be different levels of users in an organization with different roles and permissions. And you'll need a good understanding Linux permissions to manage and/or understand them.

To protect files and directories in Linux from access by certain types of users, we can use the `chown` and `chgrp` commands. These commands let you manage which type of user can read, write, and execute a file.

Before discussing the specifics of these commands, though, you need to understand the basics of how groups and users work in Linux. You'll also need to know how you can manipulate permissions for them.

Let's get into the topic without any further ado. 

## What are Group and Users in Linux?

A user is a regular entity that can manipulate files, directories, and perform various types of actions in a system. We can create any number of users in Linux.

A group contains zero or more users in it. Users in a group share the same permissions. The group allows you to set permissions on the group level instead of having to set permissions for individual users.

Let's consider a scenario in software development where a machine gets used by various types of people like Administrators, Developers, and Testers.

Each person should have an individual level of access to the files in the system. Accordingly, there will be a common set of permissions for developers, testers and admins, in their respective groups. 

Let's say there are 10 developers and 8 testers on your team and you're using 1 shared computer (each of you has a laptop too).

You want to create a file that should be accessible only to the developers. Can you achieve this without using the concept of groups? Yes – it's doable. But, that means you'll have to assign permissions individually to each developer.

The next day, say you get news that your team is expanding to 150 developers and 20 testers due to an immediate client requirement.

Again, you could assign all those additional permissions individually. But, it's not scalable. It's so tedious to manage permissions for each and every developer – so why not do it all together if they share common permissions?

Here comes the usefulness of groups. If we have all 10 (or 150) developers in a group called `dev_group`, we can simply give permission to the group `dev_group`. 

There are other use cases aside from permissions for groups, but we won't get into that here.

## What are Primary and Secondary Groups in Linux? 

As the name implies, a primary group is a group that a user belongs to by default. 

For example, let's assume your username is `arun`, and you create a group called `admin`. Then you will belong to the group `admin` by default. 

A secondary group is a group to which you can add any number of users.

## How to Create a User

You can create a user by using the `useradd` command. Each user in a Linux system has a unique user id. 

```bash
useradd [OPTIONS] <user_name>
```

Let's create a new user named `developer`:

```bash
useradd developer
```

## How to Create a Group

Groups are created by using the `groupadd` command. Similar to users, each group in a Linux system has a unique group id. 

```
groupadd [OPTIONS] <group_name>
```

Let's create a new group named `developers_group`:

```
groupadd developers_group
```

## How to Add a User to a Group

So, we created a user and a group. Let's add the user (`developer`) to the group (`developers_group`). The command to add a user to a group is `usermod -aG`. 

```bash
sudo usermod -aG <group_name> <user_name>
```

Here's the actual command to add the user `developer` to `developers_group` group:

```bash
sudo usermod -aG developers_group developer
```

## How to List Out Groups

You might wonder how you can verify if the created group exists, and how to verify if the user has been added to the group. The list of groups and the users who have permissions in the group are stored in a file called `group`. It will be located under the `/etc` directory. 

We can see the available groups by reading that file using the `cat` command like this:

```bash
cat /etc/group
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-40.png)
_Beginning of `group` file_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-41.png)
_End of `group` file_

This will be huge file. By default it has 70 to 100 lines. So, I've cropped the top and bottom part of the command's output in the above screenshots. 

The last 2 lines of the above screenshot describe that there's a new user called `developer`, a new group called `developers_group`, and the user `developer` has been added to the `developers_group` group. 

## How to Find the Current Owner and Group Ownership of a File 

There's a powerful – and likely familiar – command in Linux which shows the permissions involved in a file/directory. This is the `ls -l` command:

```bash
ls -l test.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-42.png)
_Ownership of `test.sh` file_

Let's go over the output separated by spaces and understand each part of it:

* `-rw-rw-r-- 1` – Permission for file test.sh
* 1st occurrence of `gogosoon` – Owner of the file
* 2nd occurrence of `gogosoon` – Group ownership of the file

## How to Change the Owner of a File or Directory

You can use the `chown` command to change the ownership of a file. The `chown` command is abbreviated from "change owner".  

From our previous example, we have seen the file `test.sh` owned by the user named `gogosoon`.  

```bash
chown <user_name> <file_name>
```

Let's change the ownership of the file to the user `admin` using the `chown` command. We can do that like this:

```bash
sudo chown admin test.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-43.png)
_Change the ownership of the file `test.sh` using `chown` command_

From the above screenshot, you can clearly see that the owner of the file `test.sh` has been changed from `gogosoon` to `admin`. 

## How to Copy Ownership from One File to Another 

I have faced this scenario once in my career. We use a common system in some rare use cases. Here's what was going on:

One day I was working on that system to complete a POC which required me to create hundreds of files with a different user ownership. A file was created with default permissions (owned by me) whenever it was created. 

But I want the file to be owned by another user. I was too lazy to change the ownership for each file manually. If I changed the ownership for one file, I wanted to be able to copy the same ownership for other files. I was sure that there must be some command that allowed me to do this. 

So I did a quick Google search about how to copy ownership from one file to another. After few seconds, I found the solution and it was so simple. You can do this by adding a `--reference` flag. 

```bash
chown --reference=<source_file_name> <destination_file_name>
```

Let's explore this with an example:

Let's create a new file named `copy.sh` with my user account `gogosoon`. 

The owner of the `test.sh` file is the `admin` user (from our previous example). I want the ownership of `test.sh` file to be copied to the newly created `copy.sh` file which is owned by the `gogosoon` user. 

```bash
sudo chown --reference=test.sh copy.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-44.png)
_Ownership of `test.sh` file copied to `copy.sh` file_

From the above screenshot, you can see that the first command describes the ownership of the `test.sh` file, which is owned by the `admin` user. 

The second command describes the ownership of the `copy.sh` file which is owned by the `gogosoon` user. 

The third command copies the ownership of the `test.sh` to the `copy.sh` file. 

The last command again describes the ownership of the `copy.sh` file which is now owned by `admin` user. 

You may wonder that at the beginning I told that I created hundreds of files – but how did I change the ownership of all the files at once? 

That's a different story. But here's a quick answer: I wrote a script that looped over all the files and changed the ownership by referencing a single master file. 

## How to Change Ownership of Multiple Files with a Single Command

You can do this by passing multiple file names to the `chown` command with one user name. This sets the ownership of all the given files to that particular user. 

```bash
sudo chown <user_name> file1 file2 ...
```

Here's an example where I want to set the ownership of the files `copy.sh` and `test.sh` to the `admin` user:

```bash
sudo chown admin copy.sh test.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-45.png)
_Set ownership of `copy.sh` and `test.sh` files to `admin` user_

## How to Change the Group Ownership of a File

Almost all the operations related to groups can be achieved with `chgrp` command (an abbreviation of "change group"). It's pretty similar to the `chown` command. 

Syntax of the `chgrp` command:

```bash
sudo chgrp <group_name> <file/dir_name>
```

I have already created a group called `admin` . I do not belong to this group. Let's change the group ownership of the `test.sh` file from `gogosoon` to the `admin` group. 

```bash
sudo chgrp admin test.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-46.png)
_Change group ownership of `test.sh` file to `admin`_

From the above screenshot, you can see that I changed group ownership of the `test.sh` file from `gogosoon` to `admin`. Since I do not belong to this group, I will not have write access to the file. 

Let's verify the same by opening the file in write mode using `nano test.sh`:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-47.png)
_You can see that I do not have write permission for this file_

## How to Change the Group Ownership of a Directory 

The same syntax for files is applicable to directories also. Here's a quick example:

```bash
sudo chgrp test group_test/
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-48.png)
_Change group ownership of `group_test` directory to `test` group_

But remember that the above command changes the group ownership of only the files in that directory. To recursively change the group permissions of all the directories inside that directory, we have to add the `-R` flag to it like this:

```
sudo chgrp -R admin group_test/
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-51.png)

Now the group ownership for all the files and directories inside group_test have been changed from `gogosoon` to `admin`. 

Let's verify the output by trying to write a file from the directory `group_test` as the `gogosoon` user:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-52.png)
_Trying to edit the files `hello1.sh` and `hello3.sh`_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-53.png)
_Error showing `hello1.sh` file not writable_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-54.png)
_Error showing `hello3.sh` file not writable_

Hurray! The ownership has been applied appropriately. 

## Conclusion

In this article, you have learned about handling user and group ownership of files and folders. I hope you enjoyed reading it. 

Subscribe to my newsletter by visiting my [site](https://5minslearn.gogosoon.com/?ref=fcc_grp_own_blog) and also have a look at the consolidated list of all my blogs. 

Cheers! 



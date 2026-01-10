---
title: 'Linux User Groups Explained: How to Add a New Group, a New Group Member, and
  Change Groups'
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-12-13T17:57:00.000Z'
originalURL: https://freecodecamp.org/news/linux-user-groups-explained-how-to-add-a-new-group-a-new-group-member-and-change-groups
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eba740569d1a4ca3ebb.jpg
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: Linux allows multiple users to have access to the system at one time. Setting
  permissions protects users from each other. Users can be assigned to groups that
  are created for users who share privilege, security, and access. Files and devices
  may be g...
---

Linux allows multiple users to have access to the system at one time. Setting permissions protects users from each other. Users can be assigned to groups that are created for users who share privilege, security, and access. Files and devices may be granted access based on a specific user or a group of users.

Groups are often used to give members certain permissions to modify a file or directory. 

The two main types of groups are primary groups and secondary groups. A user's primary group is the default group the account is associated with. Directories and files the user creates will have this Group ID. A secondary group is any group(s) a user is a member of other than the primary group.

## **Creating groups**

Let's create two groups called "writers" and "editors". Use the `groupadd` command like this ( You may have to use `sudo` at the beginning so you have the appropriate permission to create a group):

```
groupadd writers
groupadd editors
```

## **Creating users**

You may already have users to add to your group. If not, here is the basic syntax to create a user with the `useradd` command:

`useradd [options] username`

Here is the command to create a user named "quincy". The `-m` will create the user's home directory to match the username. The `-p p4ssw0rd` creates a password for the user of "p4ssw0rd".

`useradd -m quincy -p password`

The user will be able to change their password with the `passwd` command. They will have to enter their current password and then their new password.

## **Adding a user to a group**

You can use the `usermod` command to add a user to a group. Here is how to add the user "quincy" to the group "writers". The `-a` parameter means "append" and the `-G` parameter adds a group as a secondary group. 

`usermod -a -G writers quincy`

When a user is created with the `adduser` command, the user is automatically assigned to a primary group with the same name as the username. So currently the user "quincy" has a primary group of "quincy" and a secondary group of "writers".

You can also add a user to many groups at once by separating the group names with commas. `-G group1,group2,group3`.

The following command changes the primary group of the user quincy to "editors":

`usermod -g editors quincy`

## Removing a user from a secondary group

To remove a user from a secondary group you need to overwrite the current groups of a user with a new set of groups that does not contain the group that is being removed.

First, use the `id` command to check what secondary groups a user belongs to:

`id -nG quincy`

Let's say that this returns `editors writers` indicating that quincy is part of the "editors" and "writers" group. If you want to remove the "writers" group, use this command:

`usermod -G editors quincy`

That command sets the secondary group of quincy to "editors". Since the `-a` flag was not used, the previous set of groups was overwritten.

## Conclusion

You should now be ready to start managing users and groups. The next step is to determine which privileges each group will have.


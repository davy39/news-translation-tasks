---
title: How to Manage Users and Groups in Red Hat Enterprise Linux
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-01-08T17:41:44.000Z'
originalURL: https://freecodecamp.org/news/manage-users-and-groups-in-rhel
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/manage-users-and-groups-in-rhel-cover.jpg
tags:
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: null
seo_desc: 'To effectively safeguard your system and regulate access when working in
  Red Hat Enterprise Linux (RHEL), you''ll need to understand user and group management.

  This is a critical component that''s significant for both individual and complex
  network env...'
---

To effectively safeguard your system and regulate access when working in Red Hat Enterprise Linux (RHEL), you'll need to understand user and group management.

This is a critical component that's significant for both individual and complex network environments, as it's key to adeptly handle user accounts and groups.

In this guide, we'll dive into the fundamentals of user and group management within RHEL. You'll gain the knowledge and skills necessary to confidently create, modify, and optimize user accounts and groups, according to your specific security and operational needs.

You'll also learn the ins and outs of granting user permissions and implementing group-based access controls, and master the essential tools and proven methods for ensuring robust system integrity and regulating resource access.

## Prerequisite

* Familiarity with basic Linux commands. You can read my previous [tutorial on RHEL commands and key concepts](https://www.freecodecamp.org/news/red-hat-enterprise-linux-guide/) if you need to brush up.
    

## **Table Of Contents**

Here's what we'll cover in this comprehensive guide:

* [useradd](#heading-the-useradd-command)
    
* [What is sudo?](#heading-what-is-sudo)
    
* [usermod](#heading-the-usermod-command)
    
* [What is /etc/login.defs?](#heading-what-is-etclogindefs)
    
* [What is /etc/skel?](#heading-what-is-etcskel)
    
* [What is /etc/shadow?](#heading-what-is-etcshadow)
    
* [groupadd](#heading-the-groupadd-command)
    
* [groupmod](#heading-the-groupmod-command)
    
* [Practical Exercise](#heading-practical-exercise)
    
* [Wrapping Up](#heading-wrapping-up)
    

## The `useradd` Command

The `useradd` command is an essential tool in RHEL for creating new user accounts. This command not only adds the user's information to the system files, but also sets up their home directory and default configurations.

### Syntax of the `useradd` command:

```bash
useradd [options] username
```

## What is sudo?

In the world of Linux/Unix, `sudo` stands for "Superuser Do." Essentially, it's a command that grants regular users the ability to run commands with full administrative or root permissions. This is especially useful for commands that may be restricted for regular users due to security reasons.

### Examples:

Just a quick reminder – if you're not currently logged in as the root user, be sure to utilize `sudo` before using commands such as `useradd` that we'll be discussing in this tutorial. Consider `sudo` as a handy tool that grants you some of the root user's abilities. We'll go more in-depth on this topic in future tutorials.

At the moment, I am logged in as a root user. So I won't be using `sudo` before any commands.

#### Create a user:

```bash
useradd kedar
```

This command makes a new user called 'kedar' and sets up a home folder for them by default. Later on, we'll learn more about `useradd` and how we can change these defaults.

In RHEL, some values are already set when creating a user, but we'll explore them further in this tutorial.

#### Check a newly added user:

```bash
tail -1 /etc/passwd
```

`/etc/passwd` serves as a centralized repository containing essential information about user accounts. The output of the above command will be displayed in following way:

```bash
kedar:x:1001:1001:John Doe:/home/john:/bin/bash
```

If the user was added successfully, you will see the above output. Now there may be some changes, but it should look essentially the same.

Let's break this output down and try to understand it:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Frame-1000004542.svg align="left")

*Breakdown of the above output*

1. Username – the name of the user account.
    
2. Password Placeholder (Obsolete) – historically, this field contained an 'x' character, indicating that the encrypted password for the user was stored in the `/etc/shadow` file.
    
3. User ID (UID) – unique numerical identifier assigned to the user.
    
4. Group ID (GID) – the numerical identifier of the primary group associated with the user.
    
5. User Information (GECOS) – this field usually includes additional information like the user's full name, contact details, and so on.
    
6. Home Directory – the path to the user's home directory.
    
7. Login Shell – the default shell or program executed upon login for the user.
    

Once the user is created, we can set password for that user. This can be only done from a root account.

#### Set a password for a newly created account

```bash
passwd kedar
```

This will ask you to type password for the kedar user. Once the password is set you can login to kedar user using the GUI. Setting password is important if you want to login through the GUI.

#### Set different options for the user while creating a new user

Now that we know what options are available while creating a user, we can set them according to our needs.

1. User Id (`-u`)
    

```bash
useradd -u 1234 kedar
```

Above command with the `-u` option will set User Id to 1234 while creating the user kedar.

2. Primary Group (`-g`)
    

```bash
useradd -g 1232 kedar
```

If there is an existing group and you know the group Id or group Name, you can add that group as a primary group for the kedar user.

3. Secondary Group (`-G`)
    

```bash
useradd -G developers kedar
```

User kedar will be added to a secondary group called developers which already exists. We can add the user to multiple secondary groups.

Think of a secondary group in Linux as a coveted club membership for users. While they are automatically included in a primary group when working on the computer, joining secondary groups allows users to expand their membership and gain access to additional files and features.

Essentially, it's like being a part of multiple groups simultaneously, providing users with additional privileges and the ability to explore different parts of the system.

4. User Information
    

```bash
useradd -c "2 Month Intern" kedar
```

This adds more information to user kedar as "2 Month Intern". This will be displayed in the `/etc/passwd` file.

5. Home Directory
    

```bash
useradd -d /etc/kedar/home kedar
```

Now this will set the home directory to `/etc/kedar/home` for the kedar user. By default in RHEL, the home directory, if not specified, is `/home/kedar`.

6. Login Shell
    

```bash
useradd -s /bin/shell kedar
```

Here, the kedar user will have access to the shell which is in /bin/shell. This will give access to the shell to the user kedar.

The /bin/bash access pertains to a user's default shell upon logging into the system.

In the Linux world, the /bin/bash shell is commonly known as the Bash shell, short for "Bourne Again SHell," and is readily available on most Linux distributions. When a user is granted /bin/bash access, it means that upon login, they will be greeted with the Bash shell's command-line interface.

This powerful shell equips them with the ability to interact with the system, run commands, and execute Bash-specific scripts using its unique syntax and functionality.

Given its widespread usage, advanced capabilities, and compatibility with a variety of scripting languages and command-line tasks, the /bin/bash shell is a preferred option for many users as their default shell.

If you want to remove shell access from a particular user, you can set shell access like this: `/sbin/nologin`. This will restrict access to this user to logging into their account until shell access is set to `/bin/shell`.

```bash
useradd -s /sbin/nologin kedar
```

## The `usermod` Command

The usermod command is super important in Linux. It helps admins easily change things about user accounts after they're made. This saves time because you don't have to delete and make the accounts again. It's a handy way to manage users without much hassle.

### Syntax of the `usermod` command:

```bash
usermod [options] username
```

### Examples:

#### Change username:

```bash
usermod -l newusername oldusername
```

This command changes the username from `oldusername` to `newusername`.

#### Change User ID (UID):

```bash
usermod -u <newUID> username
```

This command replaces `<newUID>` with the desired new UID for the user.

#### Change Group ID (GID):

```bash
usermod -g <newGID> username
```

This command replaces `<newGID>` with the desired new primary group ID for the user.

#### Add user to supplementary groups:

```bash
usermod -aG group1,group2 username
```

This command adds the user to additional supplementary groups (`group1`, `group2`, etc.).

#### Change home directory:

```bash
usermod -d /newhome username
```

This command changes the user's home directory to `/newhome`.

#### Change default shell:

```bash
usermod -s /bin/bash username
```

This command changes the default shell for the user to `/bin/bash`.

#### Set expiry date for account:

```bash
usermod -e YYYY-MM-DD username
```

This command sets an expiration date (`YYYY-MM-DD`) for the user's account.

You can explore more about this command using `man usermod`. You have the same options as with `useradd` to manipulate the information of a user when you use the `usermod` command.

## What is `/etc/login.defs`?

The `/etc/login.defs` file is a crucial configuration file that sets default parameters for login, password policies, and user account creation. It can be found at the usual location, /etc/login.defs, and plays a key role in determining system-wide defaults for user management and authentication.

There is also a fixed range for user UIDs, as shown in the following table:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Frame-1000004563-1.svg align="left")

*UID range table - Privileged users: 0-99, System users: 201-999, Normal users: 1000-60000*

The directory /etc/login.defs contains a variety of default configurations. By accessing this directory, we can modify these settings to our liking.

This file contains several different options that we can adjust, some of which are listed below:

```bash
PASS_MAX_DAYS   90
PASS_MIN_DAYS   7
PASS_WARN_AGE   14
PASS_MIN_LEN    8

UID_MIN         1000
UID_MAX         60000
GID_MIN         1000
GID_MAX         60000

LOGIN_RETRIES   5
LOGIN_TIMEOUT   60
CREATE_HOME     yes
UMASK           077

ENCRYPT_METHOD  SHA512
CHFN_AUTH       yes
CHFN_RESTRICT   rwh
DEFAULT_HOME    /home
```

Now you know where the default settings come from when we create a user. You can change these settings according to your needs.

## What is `/etc/skel`?

In Linux and similar systems, the `/etc/skel/` folder is like a starter pack for new users. It's called "skel" short for "skeleton" because it sets up the basics for new users.

This folder contains a set of files and folders that are copied into a new user's home folder. Whenever a new user is made, these essential files from /etc/skel/ are automatically put into their home folder, making sure it has what they need to get started.

This helps set up a simple starting point for the user. It gives them basic configurations, default settings, and sometimes example files. This method ensures that every new user starts with a standard setup and the required files.

In the /etc/skel/ folder, you might find common files like .bashrc, .profile, and similar configuration files.

## What is `/etc/shadow`?

The `/etc/shadow` file is a crucial component of Unix-based operating systems (like Linux), as it serves as a repository for encrypted user passwords and other password-related data. This enhanced security measure surpasses previous methods of storing passwords in the /etc/passwd file.

The /etc/shadow file contains crucial information pertaining to user account passwords. Each line in the file represents a particular user and is divided into multiple fields, each separated by a colon (:).

These fields typically include the username, the encrypted password (hashed using a cryptographic algorithm, not the actual password), the number of days since the last password change (starting from January 1, 1970), information about password expiry such as minimum and maximum age, and a warning period. It also specifies the number of days of inactivity allowed before the account is locked, and if the account has an expiration date.

### Sample entry of /etc/shadow file

`user:$6$PswrdHash$E7KLkQIGo7mxG5vDi7JelC5D8L0qbg38z1/WgNhAZDpCoe2GyGB6JefT9ftb/Rfm3uZOlFkktj/SkJTfSJziO.:18830:0:90:7:::`

Where:

* `user`: Username
    
* `$6$PswrdHash$E7KLkQIG...`: Encrypted password hash
    

1. **$1$** is MD5
    
2. **$2a$** is Blowfish
    
3. **$2y$** is Blowfish
    
4. **$5$** is SHA-256
    
5. **$6$** is SHA-512
    
6. **$y$** is yescrypt
    

These symbols help identify the hashing algorithm used for each password hash stored in the `/etc/shadow` file. For instance, if you see a password hash starting with `$6$`, it indicates that SHA-512 encryption has been used for that particular password.

* `18830`: Last password change date (days since Jan 1, 1970)
    
* `0`: Minimum password age
    
* `90`: Maximum password age
    
* `7`: Password warning period
    
* Other fields for account inactivity and expiration
    

Access: In order to access and modify the `/etc/shadow` file, you must have root user permissions or specialized privileges granted.

Modification: For enhanced security, it is advised to use designated commands such as `passwd`, which handles password encryption and updates the /etc/shadow file effectively.

## The `groupadd` Command

In RHEL, you use the `groupadd` command to create new groups on the system. It's a fundamental command for managing user groups, allowing system administrators to add groups, set their properties, and define their membership.

All default settings for groups are in `/etc/login.defs`. The /etc/login.defs file contains important settings, such as GID\_MIN, which determines the minimum GID value for regular groups, and GID\_MAX, which sets the maximum GID value. Additionally, SYS\_GID\_MIN and SYS\_GID\_MAX determine the minimum and maximum GID values for system groups.

These settings play a crucial role in the management of groups within the system.

### Syntax of the `groupadd` command:

```bash
groupadd [options] groupname
```

### Examples:

#### Creating a group:

```bash
groupadd developers
```

The above command create a new group named "developers".

#### Assigning a specific GID:

```bash
groupadd -g 1001 developers
```

This command creates a group with a specified GID (for example, GID 1001).

You can explore more options according to your needs using the `man groupadd` command. This will give you documentation of the `groupadd` command.

## The `groupmod` Command

The `groupmod` command in RHEL is a valuable tool for system administrators, as it enables them to effortlessly modify existing group attributes.

With this powerful command, you can alter groups without the need for recreating them, making it a crucial asset for system maintenance.

### Syntax of the `groupmod` command:

```bash
groupmod [options] groupname
```

### Examples:

#### Change group name:

```bash
groupmod -n newgroupname oldgroupname
```

This command changes the group name from `oldgroupname` to `newgroupname`.

#### Change GID (Group ID):

```bash
groupmod -g <newGID> groupname
```

This command changes the group's GID to `<newGID>`.

#### Add group to supplementary groups:

```bash
groupmod -aG group1,group2 groupname
```

This command adds the group to additional supplementary groups (`group1`, `group2`, and so on).

#### Add users from a group:

```bash
groupmod -m -m user1,user2 developers
```

This will add user1 and user2 to the developers group.

#### Remove users from a group:

```bash
groupmod -M user1,user2 developers
```

This will remove user1 and user2 from the developers group.

You can explore more options according to your needs using the `man groupmod` command. This will give you documentation of the `groupmod` command.

## Practical Exercise

### Exercise 1: Basic User and Group Management

1. **Creating Users and Groups**
    

* Use `useradd` to create a new user named "testuser."
    
* Use `groupadd` to create a group named "testgroup."
    
* Ensure the user "testuser" is part of the group "testgroup."
    

### Exercise 2: User Modifications

1. **Modifying User Attributes**
    

* Use `usermod` to change the default shell for "testuser" to `/bin/bash`.
    
* Modify the user's login name from "testuser" to "newuser" using `usermod`.
    
* Confirm the changes by checking `/etc/passwd`.
    

### Exercise 3: Group Modifications

1. **Group Modifications**
    

* Use `groupmod` to rename "testgroup" to "newgroup."
    
* Change the GID (Group ID) of "newgroup" using `groupmod`.
    
* Add "newuser" to the "newgroup" using `usermod`.
    

### Exercise 4: Advanced User and Group Management

1. **Setting User and Group Limits**
    

* Set password policies using parameters in `/etc/login.defs`.
    
* Configure group default settings like GID\_MIN and GID\_MAX in `/etc/login.defs`.
    

### Exercise 5: Understanding `/etc/shadow` and `/etc/skel`

1. **Exploring Password Storage and Defaults**
    

* Examine the `/etc/shadow` file to understand the password storage format.
    
* Create a new user and observe their entry in `/etc/shadow`.
    
* Explore `/etc/skel` and understand its purpose by creating a new user and observing their home directory.
    

### Exercise 6: Challenge

1. **Managing Permissions and Access Control**
    

* Set up directory permissions so that only "newuser" in "newgroup" can read/write to a specific folder.
    
* Experiment with `chown` and `chmod` commands to change ownership and permissions.
    

### Exercise 7: Real-world Scenario

1. **Creating Users with Specific Configurations**
    

* Create a user named "admin" with a customized home directory (/opt/admin) and a specific default shell.
    
* Set a password policy that applies only to the "admin" user.
    

## **Wrapping Up**

Thank you for exploring how to manage users and groups in RHEL with me today. You can dive deeper into the realm of Linux expertise and stay tuned for more insightful content in my future tutorials.

You can follow me on:

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)

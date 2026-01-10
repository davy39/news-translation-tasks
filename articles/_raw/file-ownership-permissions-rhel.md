---
title: How File Ownership and Permissions Work in RHEL
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-01-16T20:56:12.000Z'
originalURL: https://freecodecamp.org/news/file-ownership-permissions-rhel
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/file-ownership-permissions-rhel-cover.jpg
tags:
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: null
seo_desc: 'Linux commands give you precise control over file ownership and permissions,
  ensuring data security and access control.

  This guide will delve into several essential commands: chown, chgrp, chmod, and
  umask. The examples will showcase their functional...'
---

Linux commands give you precise control over file ownership and permissions, ensuring data security and access control.

This guide will delve into several essential commands: `chown`, `chgrp`, `chmod`, and `umask`. The examples will showcase their functionality, variations, and practical applications.

## **Table Of Contents**

Here's what we'll cover in this comprehensive guide

* [ls -l – View File Permissions](#heading-ls-l-view-file-permissions)
    
* [chown – Change File Ownership](#heading-chown-change-file-ownership)
    
* [chgrp – Change File Group Ownership](#heading-chgrp-change-file-group-ownership)
    
* [chmod – Modify File Permissions](#heading-chmod-modify-file-permissions)
    
* [Access Control Lists](#heading-access-control-lists)
    
* [The umask Command](#heading-the-umask-command)
    
* [Practical Exercise](#heading-practical-exercises)
    
* [Wrapping Up](#heading-wrapping-up)
    

## `ls -l` – View File Permissions

In the world of Red Hat Enterprise Linux, using the `ls -l` command is like taking a peek into a directory's secret diary. It's a way to get a detailed, up-close look at what's inside, almost like flipping through a catalog with all the nitty-gritty details.

### `ls -l` example

Running this command displays file permissions, ownership, and other details for files in the current directory.

```bash
ls -l /mydirectory
```

Here's the output:

```bash
OUTPUT

drwxr-xr-x 2 username group 4096 Jan 5 09:30 mydirectory
```

Let's break down this output part by part. Here's an illustration that shows what each part represents, and I'll go through it in detail below:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Frame-1000004565.svg align="left")

*Detail output for ls -l command*

* File Type and Permissions: The first column represents the file type and permissions. It consists of ten characters:
    
* The first character indicates the file type (`-` for a regular file, `d` for a directory, `l` for a symbolic link, and so on.).
    
* The next nine characters represent permissions for the owner, group, and others (read, write, execute).
    
* Number of Links: The second column shows the number of hard links to the file or directory.
    
* Owner and Group: The third and fourth columns display the owner and group associated with the file or directory.
    
* File Size: The fifth column indicates the size of the file in bytes.
    
* Last Modified Time: The sixth column shows the timestamp of the last modification.
    
* File or Directory Name: The final column lists the file or directory name.
    

## `chown` – Change File Ownership

In Red Hat Enterprise Linux (RHEL), the mighty `chown` command stands for "change owner" and lets users to modify the ownership of files and directories. This versatile tool is a valuable resource for system administrators in effectively managing permissions and access control.

### Syntax of `chown`:

```bash
chown [OPTIONS] [NEW_OWNER][:NEW_GROUP] FILE(s)/DIRECTORY(s)
```

Options:

* R, `--recursive`: Recursively change ownership of directories and their contents.
    
* v, `--verbose`: Display a message for each file processed.
    

Note: Only the root user or a user with appropriate permissions can use chown to change ownership.

### `chown` examples:

Changing file ownership:

```bash
chown newowner myfile.txt
```

This will change the owner of a file to `newowner`.

Changing group ownership:

```bash
chown :newgroup myfile.txt
```

This command makes a file called `myfile.txt` join a new group named `newgroup`, and it doesn't mess with the person who owns the file. You can do this group change using a command called `chown`. Oh, and there's another special command just for switching groups that we'll talk about soon.

Changing both owner and group:

```bash
chown newowner:newgroup myfile.txt
```

This changes the owner to `newowner` and group to `newgroup` for the file myfile.txt.

Recursive change (applying changes to subdirectories):

```bash
chown -R newowner:newgroup /path/to/directory
```

The above command is instructing the system to change the ownership of all files and directories within the specified directory and its subdirectories to the specified new owner and group. This ensures that the operation is performed recursively across the entire directory structure.

Verbose mode:

```bash
chown -v newowner:newgroup myfile.txt
```

The command is instructing the system to change the ownership of the specified file, providing a detailed output of the modifications made. The detailed output is shown because we are using `-v` option with `chown`.

Ownership by UID/GID:

```bash
chown 1001:1002 myfile.txt
```

The command instructs the system to modify the ownership of the specified file, assigning it to a specific user and group identified by their respective numerical IDs (1001, 1002).

## `chgrp` – Change File Group Ownership

The `chgrp` command in Red Hat Enterprise Linux (RHEL) is used to change the group ownership of files or directories. It's particularly useful when you want to modify only the group ownership without affecting the file's user owner or permissions.

### Syntax of `chgrp`:

```bash
chgrp [OPTIONS] NEW_GROUP FILE...
```

### `chgrp` examples:

Change group ownership of a file:

```bash
chgrp newgroup myfile.txt
```

This changes the group ownership of a file named `myfile.txt` to a group called `newgroup`.

Change group ownership of a directory recursively:

```bash
chgrp -R newgroup /path/to/directory
```

This modifies the group ownership not only of the specified directory but of all its contents recursively. This ensures that everything within that directory structure is now associated with the group named `newgroup`.

Change group ownership and verbosely display changes:

```bash
chgrp -v newgroup myfile.txt
```

This changes the group ownership of `myfile.txt` to `newgroup` but also provides a message confirming this action. This makes the process more transparent and informs you of the change as they happen.

## `chmod` – Modify File Permissions

The ability to control file permissions is a crucial aspect of Red Hat Enterprise Linux (RHEL). The `chmod` command is a powerful tool for this purpose. By utilizing this command, you can specify the accessibility levels for reading, writing, and executing a file.

### Syntax of `chmod`:

```bash
chmod [OPTIONS] MODE FILE...
```

#### Permissions:

* Read (`r`): Allows reading or viewing the contents of a file.
    
* Write (`w`): Permits modifying or deleting the file.
    
* Execute (`x`): Grants execution permission to a file (for scripts or binaries).
    

#### Numeric representation:

* **0**: No permission.
    
* **1**: Execute.
    
* **2**: Write.
    
* **3**: Write and execute. (2+1)
    
* **4**: Read.
    
* **5**: Read and execute. (4+1)
    
* **6**: Read and write. (4+2)
    
* **7**: Read, write, and execute. (4+2+1)
    

#### Symbolic representation:

* `u`: User/Owner.
    
* `g`: Group.
    
* `o`: Others.
    
* `a`: All (equivalent to `ugo`).
    

### `chmod` examples:

Assign read and write Permissions for owner:

```bash
chmod 600 myfile.txt
```

After executing `chmod 600 myfile.txt`, the owner of `myfile.txt` will have full read and write access to the file (the `6` in `**6**00`), while the group and others will have no permissions whatsoever (the following two 0s in `6**00**`).

Allow read and execute for owner, read for group, and no access for others:

```bash
chmod 540 script.sh
```

The owner of the file has both read and execute permissions (`5`). The group associated with the file has read-only access (`4`). Other users (those not in the owner group) have no permissions at all for the file (`0`).

Provide full permissions for all (Read, Write, Execute):

```bash
chmod 777 important_file.txt
```

The owner, the group, and all other users have complete access to read from, write to, and execute `important_file.txt`. This setting grants the broadest permissions possible, which might be risky for sensitive or important files due to unrestricted access.

Assign read and write permissions to the User:

```bash
chmod u+rw myfile.txt
```

The owner of `myfile.txt` (`u`) gains read and write permissions (`rw`), allowing them to both read from and write to the file.

Remove write permission for Others

```bash
chmod o-w myfile.txt
```

Others (users not in the owner group – `o`) lose their write permission on `myfile.txt` (`-w`). They'll be able to read the file but won't be allowed to modify it.

## Access Control Lists

Access Control Lists (ACLs) in Red Hat Enterprise Linux (RHEL) are extensions of standard file permissions. They offer more granular control over who can access a file or directory by enabling you to set permissions for specific users or groups beyond the traditional owner, group, and others.

* Traditional permissions (read, write, execute) govern access based on owner, group, and others.
    
* ACLs extend this by allowing permissions for multiple users and groups.
    

In Red Hat Enterprise Linux (RHEL), `getfacl` and `setfacl` are commands used to manage Access Control Lists (ACLs) on files and directories.

### Access Control List examples:

How to view ACLs:

```bash
getfacl filename
```

This retrieves and displays the ACL information for that specific file or directory. It provides a more comprehensive view of the access rights and permissions configured for that particular file in the system.

How to set ACLs:

**Syntax:**

```bash
setfacl -m u:username:permissions filename
```

**Example:**

```bash
setfacl -m u:john:rw important_file.txt
```

The code above modifies the ACL of `important_file.txt`, specifically granting read and write permissions to the user named `john`. This allows them to read from and write to the file without affecting other users' permissions.

Let's break down the code:

* `setfacl`: The command used to set ACLs.
    
* `-m`: This option stands for "modify" and is used to modify the existing ACLs of a file or directory without altering other permissions that might already be set.
    
* `u:username:permissions`: This part specifies the user, their username, and the permissions being granted or modified for that user.
    
* `u`: Indicates that the following entry pertains to a specific user.
    
* `username`: Represents the username of the user whose permissions are being modified.
    
* `permissions`: Denotes the specific permissions being assigned to the user.
    

## The `umask` Command

In Red Hat Enterprise Linux (RHEL), `umask` stands for "user file creation mask." It's a command and a file mode creation mask that determines the default file permissions when a new file or directory is created.

It's represented as a three-digit octal number (for example, 022, 002, etc.).

**Calculation:** The `umask` value subtracts permissions from the maximum default permissions:

* For files: Start with 666 (rw-rw-rw-) and subtract the `umask` value.
    
* For directories: Start with 777 (rwxrwxrwx) and subtract the `umask` value.
    

### Example of calculating `umask`

Let's consider an example where the umask value is `022`.

For files:

* Default maximum permissions: `666` (`rw-rw-rw-`)
    
* Umask value: `022`
    
* Subtracting the umask value (`022`) from the default file permissions (`666`):
    
* For the owner: `6 (rw)` - `0 (no write)` = `6 (rw-)`
    
* For the group: `6 (rw)` - `2 (no write)` = `4 (r--)`
    
* For others: `6 (rw)` - `2 (no write)` = `4 (r--)`
    

After applying the umask (`022`), the resulting permissions for new files becomes `644` (`rw-r--r--`).

For directories:

* Default maximum permissions: `777` (`rwxrwxrwx`)
    
* Umask value: `022`
    
* Subtracting the umask value (`022`) from the default directory permissions (`777`):
    
* For the owner: `7 (rwx)` - `0 (no write)` = `7 (rwx)`
    
* For the group: `7 (rwx)` - `2 (no write)` = `5 (r-x)`
    
* For others: `7 (rwx)` - `2 (no write)` = `5 (r-x)`
    

After applying the umask (`022`), the resulting permissions for new directories becomes `755` (`rwxr-xr-x`).

So with a umask value of `022`, new files will have default permissions of `644` (`rw-r--r--`) and new directories will have default permissions of `755` (`rwxr-xr-x`).

### `umask` examples:

Check the current `umask`:

```bash
umask
```

Temporarily change the `umask`

```bash
umask [new_umask_value]
```

* The first digit represents the permissions removed for the file owner.
    
* The second digit represents the permissions removed for the group.
    
* The third digit represents the permissions removed for others (users not in the owner group).
    

Examples of umask values and their implications:

* `000`: No permissions are removed, resulting in full read, write, and execute permissions for everyone (not recommended due to security implications).
    
* `022`: Removes write permission for others, commonly used for ensuring others can read but not modify files created by the owner.
    
* `077`: Removes all permissions for group and others, only allowing the owner full read, write, and execute permissions.
    
* `002`: Similar to `022`, but additionally allows group members to write to the files they create.
    

#### Permanent `umask` change

If you want or need to, you can change system-wide `umask` (which is permanent). Here's how to do that:

* For system-wide changes, modify the system configuration files like `/etc/profile`, `/etc/bashrc`, or shell-specific files.
    
* Edit the file using a text editor with administrative privileges:
    

```bash
 sudo nano /etc/profile
```

* Locate the line setting the `umask` value and adjust it accordingly.
    
* Save the file and exit the text editor.
    

You can also change user-specific `umask` (also permanent). Here's how to do that:

* For changes specific to a user, edit their initialization file (for example, `~/.bashrc`, `~/.bash_profile`, `~/.profile`)
    

```bash
vim ~/.bashrc
```

* Add or modify the `umask` line as needed.
    
* Save the file and exit the text editor.
    

To confirm the changes, type this command:

```bash
umask
```

## Practical Exercises

Here are some exercises to help you practice what we've covered here. Try to run through them on your own.

### Viewing File Permissions:

* Use the `ls -l` command to view the detailed file permissions of files in your current directory.
    
* Interpret the output, understanding the file type, permissions, number of links, owner, group, file size, last modified time, and file/directory name.
    

### Changing File Ownership:

* Create a file named `example.txt` using any text editor (for example, `touch example.txt`).
    
* Use the `ls -l` command to verify the ownership of `example.txt`.
    
* Use the `chown` command to change the ownership of `example.txt` to a different user (replace `newowner` with an actual username).
    
* Verify the ownership change using `ls -l`.
    

#### Changing File Group Ownership:

* Create another file named `data.txt`.
    
* Use the `ls -l` command to verify the group ownership of `data.txt`.
    
* Use the `chgrp` command to change the group ownership of `data.txt` to a different group (replace `newgroup` with an actual group name).
    
* Confirm the group ownership change using `ls -l`.
    

#### Modifying File Permissions:

* Create a third file named `script.sh`.
    
* Use the `ls -l` command to view the default permissions of `script.sh`.
    
* Use the `chmod` command to give the owner read and execute permissions, the group read permissions, and no permissions for others.
    
* Verify the permission changes using `ls -l`.
    

#### Setting ACLs:

* Create a directory named `secure_folder`.
    
* Use `getfacl` to view the ACLs of the directory.
    
* Use `setfacl` to grant read and write permissions to a specific user (replace `john` with an actual username).
    
* Verify the ACL changes using `getfacl`.
    

#### Understanding Umask:

* Check the current umask value using the `umask` command.
    
* Create a new file named `confidential.txt`.
    
* Use `ls -l` to view the default permissions of `confidential.txt`.
    
* Temporarily change the umask value to `027` using the `umask` command.
    
* Create another file named `secret.txt` and check its default permissions.
    

#### Permanent Change of Umask:

* For system-wide changes, modify the system configuration file (for example, `/etc/profile`, `/etc/bashrc`) to set a new default umask.
    
* For user-specific changes, edit the user's initialization file (for example, `~/.bashrc`, `~/.bash_profile`) to set a new umask.
    
* Verify the changes by creating a new file and checking its default permissions.
    

## Wrapping Up

Thank you for exploring the world of Red Hat Enterprise Linux (RHEL) administration with me today.

We covered the core commands essential for precise file management in Red Hat Enterprise Linux, offering practical examples and exercises to reinforce understanding and proficiency.

You can dive deeper into the realm of Linux expertise and stay tuned for more insightful content in my future tutorials.

You can follow me on:

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)

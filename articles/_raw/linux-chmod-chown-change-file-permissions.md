---
title: Linux chmod and chown – How to Change File Permissions and Ownership in Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-04-27T00:38:38.000Z'
originalURL: https://freecodecamp.org/news/linux-chmod-chown-change-file-permissions
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/guided-exercise--1-.png
tags:
- name: information security
  slug: information-security
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: null
seo_desc: "Linux is a multi user OS which means that it supports multiple users at\
  \ a time. \nAs many people can access the system simultaneously and some resources\
  \ are shared, Linux controls access through ownership and permissions. \nLinux file\
  \ ownership\nIn Linu..."
---

Linux is a multi user OS which means that it supports multiple users at a time. 

As many people can access the system simultaneously and some resources are shared, Linux controls access through ownership and permissions. 

## Linux file ownership

In Linux, there are three types of owners: `user`, `group`, and `others` .

### **Linux User**

A user is the default owner and creator of the file. So this user is called owner as well.

### **Linux Group**

A user-group is a collection of users. Users that belonging to a group will have the same Linux group permissions to access a file/ folder. 

You can use groups to assign permissions in a bulk instead of assigning them individually. A user can belong to more than one group as well.

### **Other**

Any users that are not part of the user or group classes belong to this class. 

## Linux File Permissions

File permissions fall in three categories: `read`, `write`, and `execute`.

### **Read permission**

For regular files, read permissions allow users to open and read the file only. Users can't modify the file.

Similarly for directories, read permissions allow the listing of directory content without any modification in the directory.

### **Write permission**

When files have write permissions, the user can modify (edit, delete) the file and save it.

For folders, write permissions enable a user to modify its contents (create, delete, and rename the files inside it), and modify the contents of files that the user has write permissions to.

### **Execute permission**

For files, execute permissions allows the user to run an executable script. For directories, the user can access them, and access details about files in the directory.

Below is the symbolic representation of permissions to user, group, and others.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-157.png)
_Symbolic representation of permissions_

Note that we can find permissions of files and folders using long listing (`ls -l`) on a Linux terminal. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-158.png)
_Output of long listing_

In the output above, `d` represents a directory and`-` represents a regular file.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-159.png)



## **How to Change Permissions in Linux Using the `chmod` Command**

Now that we know the basics of ownerships and permissions, let's see how we can modify permissions using the `chmod` command.

**Syntax of `chmod`:**

```bash
chmod permissions filename
```

Where,

* `permissions` can be read, write, execute or a combination of them.
* `filename` is the name of the file for which the permissions need to change. This parameter can also be a list if files to change permissions in bulk.

We can change permissions using two modes:

1. **Symbolic mode**: this method uses symbols like `u`, `g`, `o` to represent users, groups, and others. Permissions are represented as  `r, w, x` for read write and execute, respectively. You can modify permissions using +, - and =.
2. **Absolute mode**: this method represents permissions as 3-digit octal numbers ranging from 0-7.

Now, let's see them in detail.

### How to Change Permissions using Symbolic Mode

The table below summarize the user representation:

<table>
<thead>
<tr>
<th>User representation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>u</td>
<td>user/owner</td>
</tr>
<tr>
<td>g</td>
<td>group</td>
</tr>
<tr>
<td>o</td>
<td>other</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

We can use mathematical operators to add, remove, and assign permissions. The table below shows the summary:

<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>+</td>
<td>Adds a permission to a file or directory</td>
</tr>
<tr>
<td>–</td>
<td>Removes the permission</td>
</tr>
<tr>
<td>=</td>
<td>Sets the permission if not present before. Also overrides the permissions if set earlier.</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Example:

Suppose, I have a script and I want to make it executable for owner of the file `zaira`.

Current file permissions are as follows:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-161.png)

Let's split the permissions like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-160.png)

To add execution rights (`x`) to owner (`u`) using symbolic mode, we can use the command below:

```bash
chmod u+x mymotd.sh
```

**Output:**

Now, we can see that the execution permissions have been added for owner `zaira`.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-162.png)

**Additional examples for changing permissions via symbolic method:**

* Removing `read` and `write` permission for `group` and `others`: `chmod go-rw`.
* Removing `read` permissions for `others`: `chmod o-r`.
* Assigning `write` permission to `group` and overriding existing permission: `chmod g=w`.

### How to Change Permissions using Absolute Mode

Absolute mode uses numbers to represent permissions and mathematical operators to modify them.

The below table shows how we can assign relevant permissions:

<table>
<thead>
<tr>
<th>Permission</th>
<th>Provide permission</th>
</tr>
</thead>
<tbody>
<tr>
<td>read</td>
<td>add 4</td>
</tr>
<tr>
<td>write</td>
<td>add 2</td>
</tr>
<tr>
<td>execute</td>
<td>add 1</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Permissions can be revoked using subtraction. The below table shows how you can remove relevant permissions.

<table>
<thead>
<tr>
<th>Permission</th>
<th>Revoke permission</th>
</tr>
</thead>
<tbody>
<tr>
<td>read</td>
<td>subtract 4</td>
</tr>
<tr>
<td>write</td>
<td>subtract 2</td>
</tr>
<tr>
<td>execute</td>
<td>subtract 1</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

**Example**:

* Set `read` (add 4) for `user`, `read` (add 4) and `execute` (add 1) for group, and only `execute` (add 1) for others.

`chmod 451 file-name`

This is how we performed the calculation:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-163.png)

Note that this is the same as `r--r-x--x`.

* Remove `execution` rights from `other` and `group`.

To remove execution from `other` and `group`, subtract 1 from the execute part of last 2 octets. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-164.png)

* Assign `read`, `write` and `execute` to `user`, `read` and `execute` to `group` and only `read` to others.

This would be the same as `rwxr-xr--`.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-165.png)

## How to Change Ownership using the `chown` Command

Next, we will learn how to change the ownership of a file. You can change the ownership of a file or folder using the `chown` command. In some cases, changing ownership requires `sudo` permissions.

Syntax of `chown`:

```bash
chown user filename

```

### How to change user ownership with `chown`

Let's transfer the ownership from user `zaira` to user `news`. 

`chown news mymotd.sh`

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-167.png)

Command to change ownership: `sudo chown news mymotd.sh`

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-168.png)

### How to change user and group ownership simultaneously

We can also use `chown` to change user and group simultaneously.

```bash
chown user:group filename
```

### How to change directory ownership

You can change ownership recursively for contents in a directory. The example below changes the ownership of the `/opt/script` folder to allow user `admin`.

```bash
chown -R admin /opt/script
```

### How to change group ownership

In case we only need to change the group owner, we can use `chown` by preceding the group name by a colon `:`

```bash
chown :admins /opt/script
```

## Linux Permissions Guided Exercise

Up until now we have explored permissions, ownerships, and the methods to change them. Now we will reinforce our learning with a guided exercise.

**Goal**: To create groups and assign relevant permissions to its members. Verify access by accessing it from unauthorized users.

**Task**: Create a group called `dev-team` and add two members (John and Bob) to it. Create a folder `/home/dev-team` and change ownership to group `dev-team`. Verify that both users in the `dev-team` group have _read_ and _write_ access to the folder.

Create another group `project-manager` and add a user `Fatima` to it. Verify if the folder `/home/dev-team` is accessible by `Fatima`.

### Visualization of the problem

We can visualize the problem like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Notes_220426_040131_1.jpg)

**Step 1: Switch to root user.**
Switch to root user so that we have the rights to create new users and groups.

<details>
<summary> Show hint
</summary><br>

Use the `sudo` command with flag `i`.

If you have the root password, you can login using that as well.

</details>

<details>
<summary> Show solution
</summary><br>

Enter `sudo -i` to switch to the root user.

Enter `whoami` to find out if you are the root user:

![step1-1](https://www.freecodecamp.org/news/content/images/2022/04/step1-1.PNG)

If you do not have `root` access, use the commands with appending `sudo`.

</details>

--- 

**Step 2: Create a group `dev-team`**

<details>
<summary> Show hint
</summary><br>

Use the `groupadd` command.

Syntax: `groupadd group-name`

</details>

<details>
<summary> Show solution
</summary><br>

Enter `groupadd dev-team` to create the `dev-team` group

Verify: `cat /etc/group | grep dev-team`

</details>

--- 

**Step 3: Create two new users John and Bob and add them to the `dev-team` group**


<details>
<summary> Show hint
</summary><br>

Use command `useradd`.

`useradd` creates a new user and adds to the specified group.

Syntax: `useradd -G groupname username`

Where `-G` specifies the group.

</details>

<details>
<summary> Show solution
</summary><br>

`useradd -G dev-team John`

`useradd -G dev-team Bob`

Verify: `cat /etc/group | grep dev-team`

![step3-1](https://www.freecodecamp.org/news/content/images/2022/04/step3-1.PNG)

</details>


--- 

**Step 4:  Provide passwords for users John and Bob**


<details>
<summary> Show hint
</summary><br>


Use command `passwd`

`passwd` creates a password for users.

Syntax: `passwd username`


</details>

<details>
<summary> Show solution
</summary><br>

`passwd John`

`passwd Bob`

</details>



--- 

**Step 5: Create a directory in /home and name it `dev-team`**


<details>
<summary> Show hint
</summary><br>


Use command `mkdir`

`mkdir` creates a directory.

Syntax: `mkdir directory-name`


</details>

<details>
<summary> Show solution
</summary><br>

`mkdir /home/dev-team`

Verify:

![correction](https://www.freecodecamp.org/news/content/images/2022/04/correction.png)

</details>



--- 


**Step 6: Change the group ownership of the folder `dev-team` to group `dev-team`**


<details>
<summary> Show hint
</summary><br>

Use command `chown`

Syntax: `chown :group-name folder`


</details>

<details>
<summary> Show solution
</summary><br>

`chown :dev-team /home/dev-team/`
    
![step6](https://www.freecodecamp.org/news/content/images/2022/04/step6.png)

</details>



--- 

**Step 7: Make sure the permissions of folder `dev-team` allow group members to create and delete files.**


<details>
<summary> Show hint
</summary><br>

Use command `chmod`

Write permissions allow users and groups to create and delete files.

Syntax: `chmod permissions folder`

</details>

<details>
<summary> Show solution
</summary><br>

`chmod g+w /home/dev-team/`

![step7](https://www.freecodecamp.org/news/content/images/2022/04/step7.png)

</details>




--- 


**Step 8: Ensure that 'others' don't have any access to the files of `dev-team` folder.**


<details>
<summary> Show hint
</summary><br>

Use command `chmod`

Remove read, write, execute  permissions from 'others' if they exist.

Syntax: `chmod permissions folder`


</details>

<details>
<summary> Show solution
</summary><br>

`chmod o-rx dev-team `

![correction2](https://www.freecodecamp.org/news/content/images/2022/04/correction2.png)



</details>



--- 

**Step 9: Exit the `root` session and switch to `John`**


<details>
<summary> Show hint
</summary><br>

Use command `exit` to logout of the root user.

Use `su` to switch users.

Syntax: `su - user`

To confirm current user, use command `whoami`.

</details>

<details>
<summary> Show solution
</summary><br>

`exit`

`su - John`

Verify with command `whoami`.

</details>



--- 


**Step 10: Navigate to folder: `/home/dev-team`**


<details>
<summary> Show hint
</summary><br>

Use command `cd` to switch folders.

Syntax: `cd /path/to/folder`

Confirm current path with `pwd`.

</details>

<details>
<summary> Show solution
</summary><br>

`cd /home/dev-team`

</details>



--- 


**Step 11: Create an empty file in the folder: `/home/dev-team`**


<details>
<summary> Show hint
</summary><br>

Use command `touch` to create an empty file.

Syntax: `touch filename`

</details>

<details>
<summary> Show solution
</summary><br>

`touch john-file.txt`

Verify: `ls -lrt`
  
![john](https://www.freecodecamp.org/news/content/images/2022/04/john.png)
    
</details>







--- 


**Step 12:  Change the group ownership of the created file to `dev-team` and verify.**


<details>
<summary> Show hint
</summary><br>

Use command `chown` to change ownership.

Syntax: `chown :group file-name`

</details>

<details>
<summary> Show solution
</summary><br>

`chown :dev-team john-file.txt`

Once group ownership is modified, all members of the group can access this file.

Verify `ls -lrt`

![step10](https://www.freecodecamp.org/news/content/images/2022/04/step10.PNG)

</details>




--- 


**Step 13:  Exit the shell and switch to user `Bob`**


<details>
<summary> Show hint
</summary><br>

Use command `exit` to exit the terminal.

Use `su` to switch users.

Syntax: `su - user`

To confirm current user, use command `whoami`.

</details>

<details>
<summary> Show solution
</summary><br>

`exit`

`su - Bob`

Verify the current user with command `whoami`.



</details>





--- 


**Step 14: Navigate to the path `/home/dev-team`**


<details>
<summary> Show hint
</summary><br>

Use command `cd` to switch folders.

Syntax: `cd /path/to/folder`

Confirm current path with `pwd`.



</details>

<details>
<summary> Show solution
</summary><br>

`cd /home/dev-team`


</details>





--- 


**Step 15: Find out `Bob's` privileges to access `john-file.txt `**


<details>
<summary> Show hint
</summary><br>


Use command `ls -l` for long listing.

Syntax: `ls -l | grep file-name`

Does group have `rw-` permissions?



</details>

<details>
<summary> Show solution
</summary><br>

`ls -l | grep john-file.txt`

   
![step13](https://www.freecodecamp.org/news/content/images/2022/04/step13.PNG)

</details>



--- 


**Step 16: Modify the file `john-file.txt ` while logged in as `Bob`**


<details>
<summary> Show hint
</summary><br>

Use command `echo` to add some text to the file.

Syntax: `echo "Some text" >>file-name`

This would redirect the quoted text to end of the file.

</details>

<details>
<summary> Show solution
</summary><br>

`echo "This is Bob's comment" > john-file.txt`

If all the permissions are correctly set, `Bob` would be allowed to edit and save this file. Otherwise you would get an error like this: `Permission denied`.

Verify `cat john-file.txt`
 
![bob-comment](https://www.freecodecamp.org/news/content/images/2022/04/bob-comment.png)
    
</details>



--- 



**Step 17: Create another group `project-manager` and assign a member `Fatima` to it**


<details>
<summary> Show hint
</summary>

Use command `groupadd` to add a new group.

Syntax: `groupadd group-name`


Create a new user with command `useradd`.
    
Use flag `-G` to assign a user to it.

</details>

<details>
<summary> Show solution
</summary>

```
groupadd project-manager
useradd -G project-manager Fatima
passwd Fatima
```

</details>

--- 


**Step 18: Navigate to folder `/home/dev-team` and verify if  `Fatima` can access it**


<details>
<summary> Show hint
</summary>

Use `cd` to navigate to `/home/dev-team`.

</details>

<details>
<summary> Show solution



</summary>

`cd /home/dev-team`.

We get this error:

![fatima](https://www.freecodecamp.org/news/content/images/2022/04/fatima.png)

This is because, `others` don't have any access to the folder `dev-team`.

If we recall, below are the rights of the `dev-team` folder.

![recall](https://www.freecodecamp.org/news/content/images/2022/04/recall.png)

</details>

## Wrapping up

Permissions and ownerships are useful concepts for enforcing security across multi-user operating systems. I hope you were able to learn about changing permissions and ownerships in depth. 

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can also read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

Thanks to [Tom Mondloch](https://twitter.com/moTness) for his help with the guided exercise.



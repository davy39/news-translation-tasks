---
title: How to Manage Users in Linux
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2023-09-06T00:08:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-users-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/gabriel-heinzer-xbEVM6oJ1Fs-unsplash-1.jpg
tags:
- name: Linux
  slug: linux
- name: management
  slug: management
- name: Security
  slug: security
seo_title: null
seo_desc: Linux is an open-source operating system that is widely used in various
  applications due to its flexibility, stability, and security. One of the fundamental
  aspects of Linux is user management, which enables administrators to control access
  to resour...
---

Linux is an open-source operating system that is widely used in various applications due to its flexibility, stability, and security. One of the fundamental aspects of Linux is user management, which enables administrators to control access to resources and maintain security of the system.

In the fast-paced world of technology, efficient user management is crucial for maintaining a secure and well-organized Linux environment. This article serves as a comprehensive guide to user management in Linux, focusing on the needs of CTechCo, a hypothetical technology company. 

By understanding the various aspects of user management, which includes creating, modifying, and deleting user accounts, implementing user authentication. By following user management best practices, CTechCo can ensure the security and productivity of its Linux systems.

# Table Of Contents

* [What are Users in Linux?](#heading-what-are-users-in-linux)
* [Types of Users in Linux](#heading-type-of-users-in-linux)
* [User Account Properties](#heading-user-account-properties)
* [How to Create Users](#heading-how-to-create-users)
* [How to Delete Users](#heading-how-to-delete-users)
* [How to Modify User Accounts](#heading-how-to-modify-user-accounts)
* [Password Management](#heading-password-management)
* [Group Management](#heading-group-management)
* [User Authentication](#heading-user-authentication)
* [Best Practices for User Management in Linux](#heading-best-practices-for-user-management-in-linux) 
* [Principle of Least Privilege](#heading-principle-of-least-privilege)
* [User Permissions](#heading-user-permissions)
* [Monitoring and Auditing](#heading-monitoring-and-auditing)
* [User Training](#heading-user-training)
* [Conclusion](#heading-conclusion)

## What are Users in Linux?

In a Linux system, users refer to individuals or entities that interact with the operating system by logging in and performing various tasks. User management plays a crucial role in ensuring secure access control, resource allocation, and system administration.

A user in Linux is associated with a user account, which consists of several properties defining their identity and privileges within the system. These properties are a username, UID (User ID), GID (Group ID), home directory, default shell, and password.

Each user account possesses these unique properties listed above.

## Type of Users in Linux

Linux supports two types of users: system users and regular users.

**System users** are created by the system during installation and are used to run system services and applications. 

**Regular users** are created by the administrator and can access the system and its resources based on their permissions.

Let's meet CTechCo's diverse workforce, consisting of individuals who interact with the Linux system through user accounts. Meet John, a developer; Lisa, a system administrator; and Sarah, a marketing manager. They each have unique usernames such as "johndoe," "lisasmith," and "sarahsmith," respectively. These usernames act as their identification within the Linux system.

## How to Create Users

CTechCo's system administrator, Alex, needs to create user accounts for John, Lisa, and Sarah. Alex initiates the process using the `useradd` command. For example, to create John's account, Alex executes the command below:

```bash
useradd -u 1002 -d /home/john -s /bin/bash john
```

This command creates John's account with uid (`-u`) as 1002, the home directory (`-d`) as **/home/john** and sets (`-s`) **/bin/bash** as his default shell.

Similarly, Alex will create a user account for Lisa and Sarah using same format

Alex can verify the new user account by running the `id` command:

```bash
id john
```

This will display the user ID and group memberships for the user "john".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/id-john.png)
_uid, gid, and groups information for john user_

## User Account Properties

Within CTechCo's Linux environment, user accounts possess various properties that define their characteristics and access privileges. Let's explore these properties in the context of our use case.

1. **Username**: Each user is assigned a unique username that serves as their identifier within the Linux system. For example, John's username is "john".
2. **UID (User ID) and GID (Group ID)**: Every user account is associated with a UID and GID. The UID is a numerical value assigned to the user, while the GID represents the primary group to which the user belongs. For instance, John's UID may be `1002,` and his primary group's GID is `1002` as well.
3. **Home Directory**: Each user has a designated home directory where their personal files and settings reside. John's home directory is **/home/john**.
4. **Default Shell**: The default shell determines the command interpreter used when a user logs in. It defines the user's interactive environment. In our case, John's default shell is set to **/bin/bash**, which is a popular shell in Linux.
5. **Password**: User accounts require passwords to authenticate and access the system. CTechCo's users, including John, must create strong passwords to ensure security.
6. **Group**: The group membership determines which system resources the user can access, as well as which users can access the user's files.

Alex could take a look at the users on their Linux by running the `cat /etc/passwd` command. The users will be displayed in this format:

```bash
john:x:1002:1002:,,,:/home/john:/bin/bash
```

Here's what each of the fields in the format above represents:

* `john`: This is the username of the user account.
* `x`: This field contains the encrypted password of the user. It is replaced with an 'x' character to indicate that the password is stored in the `/etc/shadow` file for security reasons.
* `1002`: This is the UID (User ID) of the user account, which is a unique numerical identifier assigned to the user by the system.
* `1002`: This is the GID (Group ID) of the user account, which represents the primary group membership of the user.
* `,,,`: This is the GECOS field, which stands for "General Electric Comprehensive Operating System". This field is used to store additional information about the user, such as their full name or contact information. In this case, the field is empty, as no additional information was provided while creating the user account.
* `/home/john`: This is the home directory of the user account, which is the location where the user's files and personal data are stored.
* `/bin/bash`: This is the default shell for the user account, which is the command interpreter used to process commands entered by the user in the terminal. In this case, the default shell is Bash, which is the most commonly used shell in Linux.

## How to Delete Users

Let's assume that Lisa has left CTechCo. To remove her account and associated files, Alex has to utilize the `userdel` command. For instance, to delete Lisa's account, Alex runs:

```bash
sudo userdel lisa
```

This will delete the user account for `lisa`, along with their home directory and any files or directories owned by the user.

## How to Modify User Accounts

As CTechCo's workforce evolves, the IT team may need to make adjustments to user accounts. Let's explore how they can modify user accounts to accommodate changing needs and permissions.

For example, John (the developer), is assigned additional responsibilities within the company. To reflect this change, the IT team can modify John's account using the `usermod` command. Let's consider the following scenario:

### How to Modify User Groups in Linux

CTechCo creates a new group called `development` to manage access to development-related resources. To add John to the `development` group, the following command can be used:

`sudo usermod -aG development john`

This command adds John to the `development` group, granting him the necessary access privileges.

### How to Change Default Shell in Linux

In a case where John prefers to use a different shell other than the default **/bin/bash** shell. The IT team can modify his account accordingly. For example, to change John's default shell to **/bin/zsh**, the following command can be used:

`sudo usermod -s /bin/zsh john`

This command updates John's account to use the new default shell — **/bin/zsh**.

You can run the `cat /etc/passwd` again to see that the shell for john has changed from **/bin/bash** to **/bin/zsh**.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/zsh.png)

## Group Management

Effective group management is crucial for controlling access to resources within CTechCo's Linux environment. Let's explore how the IT team can create and manage groups to ensure proper access control.

### How to Create a New Group in Linux

To create a new group, such as the `marketing`  group, the following command can be used:

`sudo groupadd marketing`

The command above creates the `marketing` group, which can be used to grant specific permissions and access to marketing-related resources.

To view the group you just added, run the command below:

```bash
cat /etc/group
```

This returns all the groups on your Linux machine and when you scroll to the bottom, you can find the most recent groups.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/linux-group.png)

You can also use the command to return a specific group (`marketing` in our case):

```bash
cat /etc/group | grep marketing
```

### How to Assign Users to Groups in Linux

Once a group is created, users can be added to it. For example, to add Sarah (the marketing manager) to the `marketing` group, the following command can be used:

`sudo usermod -aG marketing sarahsmith`

This command adds Sarah to the `marketing` group, enabling her to access the resources associated with that group.

## Password Management

Ensuring strong password management practices is essential for maintaining the security of user accounts within CTechCo's Linux environment. Let's explore how the IT team can enforce password policies and manage user passwords effectively.

**Setting Password Policies:** The IT team can establish password policies to enforce strong passwords, including complexity requirements, password expiration, and account lockouts. These policies can be configured in the **/etc/login.defs** file.

**Changing User Passwords:** Users should be encouraged to change their passwords periodically. They can do so using the `passwd` command. For example, John can change his password with the following command:

`sudo passwd john`

This command prompts John to enter his current password and then allows him to set a new, secure password.

## User Authentication

User authentication is a crucial aspect of user management in Linux, ensuring that only authorized users can access the system. CTechCo can employ various authentication mechanisms to safeguard their Linux environment.

### Password-Based Authentication

Password-based authentication is the most common method for user authentication in Linux. When users log in, they provide their username and corresponding password to authenticate their identity.

For example, John logs into the system by entering his username and password at the login prompt. The system then verifies the provided password against the stored password hash associated with John's account.

### SSH Key-Based Authentication

Secure Shell (SSH) key-based authentication provides a more secure alternative to password-based authentication. Users generate a public-private key pair, where the public key is stored on the server and the private key is kept securely on the user's device.

With SSH key-based authentication, users like Lisa, a system administrator at CTechCo, can authenticate without entering a password. Instead, the server verifies the user's identity based on the possession of the private key.

To configure SSH key-based authentication for Lisa, the following steps can be taken:

1. Generate an SSH key pair on Lisa's machine using the `ssh-keygen` command.
2. Copy the public key to the server's **/home/lisasmith/.ssh/authorized_keys** file.
3. Configure the server to allow SSH key-based authentication.

## Best Practices for User Management in Linux

To ensure the security and efficiency of user management in Linux, CTechCo can follow several best practices. These practices minimize security risks and enhance the overall management process.

### Principle of Least Privilege

The principle of least privilege (PoLP) is a fundamental concept in user management. It states that users should only be granted the minimum privileges necessary to perform their tasks effectively.

CTechCo can apply the PoLP to limit user access and mitigate the impact of potential security breaches. For example, John is granted administrative privileges using the `sudo` command only when required for specific tasks. By running the following command, John can execute commands with elevated permissions:

`sudo command`

### User Permissions

CTechCo's IT team can assign appropriate permissions to users and groups to control access to files, directories, and resources. They can use the `chmod` command to set permissions for files and directories, such as read, write, and execute permissions for the owner, group, and others.

For instance, to grant read and write permissions to the owner and read-only permissions to the group and others, the following command can be used:

`chmod 640 filename`

To view the permissions for the file, you can use the `ls -l` command. This will display the file's permissions in the following format:

```bash
-rw-r--r-- 1 username username 0 Apr 5 11:24 filename.txt
```

In the format above, the first three characters represent the file's permissions for the owner of the file. 

The second three characters represent the permissions for members of the file's group.

The last three characters represent the permissions for all other users. 

In this case, the owner of the file has **read** and **write** permissions, while members of the group and all other users only have read permissions.

### Monitoring and Auditing

CTechCo can implement monitoring and auditing mechanisms to track user activities and identify potential security breaches. They utilize tools like auditd to collect and analyze system logs, enabling them to detect suspicious activities and take appropriate actions.

For example, the IT team can configure auditd to monitor critical system files and directories, as well as user logins and administrative commands.

Also, to view system logs in Linux, Alex can use the `tail` command. For example, to view the last 10 lines of the system log file, you can use the following command:

```bash
sudo tail /var/log/syslog
```

### User Training

CTechCo recognizes the importance of user training in maintaining a secure Linux environment. They can conduct regular training sessions to educate users about password security, best practices for data handling, and awareness of social engineering attacks.

Additionally, they can encourage users to report any suspicious activities or security incidents promptly, fostering a culture of security awareness and responsibility.

By adhering to these best practices, CTechCo can ensure a robust user management process and minimizes security risks in their Linux environment.

## Conclusion

Managing users in a Linux environment is essential for maintaining a secure and organized system. In the context of CTechCo, we have explored various aspects of user management and authentication such as:

* The concept of users in Linux, types and their roles within the system.
* User account properties, such as usernames, UIDs, GIDs, home directories, default shells, and passwords.
* User management tasks, including creating, deleting, and modifying user accounts with the use of commands like `useradd`, `userdel`, and `usermod`.
* How group management works using the `groupadd` and `usermod` commands.
* User authentication mechanisms, including password-based authentication and SSH key-based authentication.
* Best practices for user management, such as following the principle of least privilege.
* The use of the `sudo` command for elevated permissions.
* User permissions and access control configured through the `chmod` command.
* Monitoring and auditing user activities using tools like `auditd`.
* User training and awareness programs to promote password security and data handling best practices.

We began by understanding the concept of users in Linux, including their roles and importance within the system. We discussed the different types of users, such as regular users and system users, and their respective account properties, including usernames, UIDs, GIDs, home directories, default shells, and passwords.

Moving on to user management, we covered the process of creating, deleting, and modifying user accounts. We saw how the `useradd`, `userdel`, and `usermod` commands can be used to perform these operations. Additionally, we explored group management, where the `groupadd` command is used to create groups and the `usermod` command is utilized to assign users to groups.

User authentication mechanisms were also discussed. We examined password-based authentication, where users provide their username and password for verification. Additionally, we explored the more secure SSH key-based authentication, which relies on public-private key pairs.

We the highlighted some best practices that CTechCo could follow like the principle of least privilege, granting users only the necessary privileges for their tasks. They can utilize the `sudo` command for elevated permissions when required. User permissions, configured through the `chmod` command, are implemented to control access to files and directories. Monitoring and auditing mechanisms, such as using the `auditd` tool, are employed to track user activities and detect potential security breaches. Furthermore, user training and awareness programs can be conducted to educate users about password security, data handling best practices, and social engineering awareness.

By incorporating these best practices, CTechCo's IT team can ensure a secure user management process, minimizing security risks and maintaining a well-structured Linux environment.

As always, I hope you enjoyed the article and learned something new. If you want, you can also follow me on [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) or [Twitter](https://twitter.com/caesar_sage).


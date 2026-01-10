---
title: How to Secure Linux Servers with SE Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2021-10-26T17:33:34.000Z'
originalURL: https://freecodecamp.org/news/securing-linux-servers-with-se-linux
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/Enhance-Linux-server-security-with-SE-Linux--1-.png
tags:
- name: Linux
  slug: linux
- name: Security
  slug: security
- name: servers
  slug: servers
seo_title: null
seo_desc: "Security is an extremely important aspect of software development, server\
  \ management, and application development these days. \nAnd if you use Linux, you're\
  \ in luck – it comes with an excellent feature called SE Linux that helps you add\
  \ an additional ..."
---

Security is an extremely important aspect of software development, server management, and application development these days. 

And if you use Linux, you're in luck – it comes with an excellent feature called SE Linux that helps you add an additional layer of security.

## What is SE Linux?

SE Linux was developed by the NSA (National Security Agency) to serve government-related security tasks.  

SE Linux stands for Security Enhanced Linux. It gives system administrators more control for providing access to files and processes. With SE Linux, admins can define a context and tag files and permit them within that context.

Access and permissions are usually inherited based on user groups. But there are some sources (like web servers and processes) that need access to network ports and kernel processes. These are usually spawned by the root user or users with special access. SE Linux helps you limit who can access these special processes.

## How to work with SE Linux

SE Linux comes by default in most Linux distros. In this post, I will be working on Fedora. 

Just keep in mind that working with SE Linux requires `sudo` or `root` access.

The SE Linux configuration file is located in the `/etc/sysconfig/selinux` folder. Let's view its contents:

### SE Linux Modes

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-69.png)
_SE Linux config file_

In the config file, we can change the modes and choose any one from the below:

1. **Enforced** – Enabled by default, filters based on defined policies.
2. **Permissive** – Does not enforce the defined policies, but records all of the attempts in log files. This mode is useful for troubleshooting.
3. **Disabled** – SE Linux is completely disabled. This is not recommended as it might expose your system to threats. Also, reverting back to enforced could create certain discrepancies.

You can check your current SE Linux mode with the below commands:

1. `getenforce`
2. `sestatus`

If you only need to change the mode for the current session, you can use the below commands: 

1. `sudo setenforce 0` – sets permissive mode for current session
2. `sudo setenforce 1` – sets enforcing mode for current session

## SE Linux Policies

In SE Linux, policies define access to users. Users define access to roles and roles define access to domains. Domains then provide access to certain files.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-61.png)
_SE Linux Policies_

To change and modify accesses, 'booleans' are defined. We'll look into booleans in the next section.

### How to manage SE Linux policies with booleans

As you now know, SE Linux policies are managed by booleans.

Let's see a working example of how you'd view and set a boolean. In this example, we will set booleans specific to `httpd`.

First, list all modules specific to http – `getsebool -a | grep httpd`.

_Here **`-a`** lists all booleans._

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-80.png)
_List of Booleans_

Next, let's select and change the yellow highlighted boolean in the code above:

```bash
getsebool httpd_can_connect_ftp
```

Now, set the value to `allow`.

```bash
setsebool -P httpd_can_connect_ftp 1
```

In the command above,

* The flag P is used to make the change permanent even after reboot.
* `1` is enabling the boolean.

Now, when you list the process again, its value will be allowed.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-81.png)
_Boolean 'on'_

## SE Linux Architecture

The diagram below explains how SE Linux validates an attempt from source:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-62.png)

## Troubleshooting and SE Linux Logs

SE Linux produces very detailed logs for each attempt. You can find the logs and view them here: `/var/log/audit`.

While troubleshooting, you should move into 'permissive' mode so all events can be recorded in the logs. Although policies are not being enforced, attempts are being recorded in logs.

## How to disable and enable SE Linux

Disabling SE Linux completely is never a good option. But there are certain scenarios where policies can be by-passed such as when troubleshooting. 

Instead of disabling SE Linux if you run into a small issued, it is better to invest some time in troubleshooting. 

But if you really need to disable SE Linux, follow these steps: 

1. Change the mode from 'enforcing' to 'permissive'.
2. Change mode from 'permissive' to 'disabled'.

## Wrapping up

Learning SE Linux is worth your time and there are endless possibilities you can explore when using it. 

SE Linux provides admins with a fine-grained level of control. So why not learn it and leverage it to increase your security?

Thanks for reading until the end. Let's connect on [Twitter](https://twitter.com/hira_zaira).


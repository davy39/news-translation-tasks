---
title: How to Set an Environment Variable in Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-10-26T18:38:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-an-environment-variable-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Copy-of-Copy-of-read-write-files-python--3-.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "In programming, you use variables to store information like strings and\
  \ numbers temporarily. \nVariables can be used repeatedly throughout the code or\
  \ by your operating system to provide values. You can edit them, overwrite them,\
  \ and delete them.\nIn t..."
---

In programming, you use variables to store information like strings and numbers temporarily. 

Variables can be used repeatedly throughout the code or by your operating system to provide values. You can edit them, overwrite them, and delete them.

In this tutorial, I'll teach you what environment variables are and how to set them in Linux. 

## What Are Environment Variables?

Environment variables are the variables specific to a certain environment. For example, each user in an operating system has its own environment. An admin user has a different environment than other users do, for example. 

You might declare an environment variable only required by your user (for example a secret token) that doesn't need to be exposed to other users. 

Here are some examples of environment variables in Linux:

* `USER` – This points to the currently logged-in user.
* `HOME` – This shows the home directory of the current user.
* `SHELL` – This stores the path of the current user’s shell, such as bash or zsh.
* `LANG` – This variable points to the current language/locales settings.
* `MAIL` – This shows the location of where the current user’s mail is stored.

These environment variables vary based on the current user session.

## How to List Environment Variables in Linux

The command used to display all the environment variables defined for a current session is `env`. 

Here is the output for my session:

```bash
root@Zaira:~# env
SHELL=/bin/bash
PWD=/root
LOGNAME=root
HOME=/root
LANG=C.UTF-8
LESSOPEN=| /usr/bin/lesspipe %s
USER=root
SHLVL=1
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
MAIL=/var/mail/root
_=/usr/bin/env
```

## How to Print Environment Variables in Linux

There are two ways to print the already defined environment variables:

* `printenv VARIABLE_NAME`
* `echo $varname`

Let's print the value of the variable `SHELL` using both methods. Here's an example of printing using `printenv`:

```bash
root@Zaira:~# printenv SHELL
/bin/bash
```

And here's an example of using `echo`:

```bash
root@Zaira:~# echo $SHELL
/bin/bash
```

## How to Set Environment Variables in Linux

The basic syntax to define an environment variable is as follows:

```bash
export VARIABLE_NAME=value
```

Let's define an environment variable, list it, and print its value.

* Define the variable `JAVA_HOME`:

```bash
root@Zaira:~# export JAVA_HOME=/usr/bin/java
```

* Verify by listing it:

```bash
root@Zaira:~# env
SHELL=/bin/bash
JAVA_HOME=/usr/bin/java
PWD=/root
LOGNAME=root
HOME=/root
LANG=C.UTF-8
LESSCLOSE=/usr/bin/lesspipe %s %s
TERM=xterm-256color
global22=yolo
LESSOPEN=| /usr/bin/lesspipe %s
USER=root
SHLVL=1
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
MAIL=/var/mail/root
_=/usr/bin/env
```

* Print its value:

```bash
root@Zaira:~# echo $JAVA_HOME
/usr/bin/java
```

However, the variables defined using this method are stored for the current session only. They won't be available for the next session. 

Let's verify by opening a new session and printing the variable's value.

```bash
zaira@Zaira:/etc$ echo $JAVA_HOME


```

But, we can make the definitions persistent as shown in the next section.

## How to Make Environment Variables Persistent in Linux

To make the `JAVE_HOME` variable persistent, edit the file `.bashrc` and define its value in it. 

The `.bashrc` is a script file that's executed whenever a user logs in. It is hidden and located in the user's home directory by default. 

I have edited my `.bashrc` file as follows:

```bash
vi ~/.bashrc
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-194.png)
_Add the definition of the environment variable at the end of the `.bashrc` file_

For the changes to take effect, update the `.bashrc`  file using the `source` command:

```bash
source .bashrc
```

Let's verify by opening a new session.

```bash
root@Zaira:~# echo $JAVA_HOME
/usr/bin/java
```

## How to Create a Persistent Global Variable in Linux

Sometimes you might need to define a global environment variable that is accessible by all users. 

For that, we need to first declare a variable and make changes in relevant files where environment variables are read from.

 Let's go step by step.

1. I am logged in as the user `Zaira`. I am creating a global variable `GLOBAL_VARIABLE` like this:

```bash
zaira@Zaira:~$ export GLOBAL_VARIABLE="This is a global variable"
```

2.  Edit the following files:

* `/etc/environment` – This file is used to set up system-wide environment variables.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-196.png)
_Update the ``/etc/environment`` file_

For the changes to take effect, use the command `source /etc/environment`.

* `/etc/profile` – Variables set in this file are read whenever a bash shell is logged in. Edit this file and use the `export` command:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-198.png)
_Update the `/etc/profile`_

Time to test!

Now, I'll switch the user to the root user and verify if I can access the variable `GLOBAL_VARIABLE`.

```bash
root@Zaira:~# echo $GLOBAL_VARIABLE
This is a global variable
```

It worked! I have been able to access the global variable defined by the user `Zaira` through the `root` user as well. The same would apply to other users too. So now you also know how to define global environment variables.

## Conclusion

In this tutorial, you learned how to create and define environment variables in Linux. You also learned how to make them persistent so that you can use them across multiple sessions. 

What’s your favorite thing you learned here? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

[Image by catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm#query=programmer&position=2&from_view=search&track=sph) on Freepik.


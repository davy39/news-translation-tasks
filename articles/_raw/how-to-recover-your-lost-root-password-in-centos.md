---
title: How to recover your lost root password in CentOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-05T13:47:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-recover-your-lost-root-password-in-centos
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/Untitled-design--1-.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'By Thanoshan MV

  In Linux, when you forget your account password, you can easily reset it using a
  root account. But when you forget your root account password, then you''re in a
  bad situation.

  You can’t reset your root account password using a regular ...'
---

By Thanoshan MV

In Linux, when you forget your account password, you can easily reset it using a root account. But when you forget your root account password, then you're in a bad situation.

You can’t reset your root account password using a regular user account as a user account can't perform such tasks in general.

In this article we’ll be covering how to recover your CentOS root password. So let's see how to do it.

## How to recover your root password - step-by-step

In CentOS, it’s possible to have the scripts that run from the initramfs debug the shell at certain points, provide a root shell, and continue when that shell exists. 

While this is mostly meant for debugging, it can also be used to recover a lost root password.

Follow these steps to recover your lost root password.

First, reboot the system.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/1.png)

Interrupt the boot loader countdown by pressing any key.

Move the cursor to the entry that needs to be booted.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/2.png)

Press “e” to select that entry. After selecting that entry, the below kernel commands will appear.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/3.png)

In the kernel command line, move the cursor to the line that starts with linux16.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/4.png)

Press the “End” key to move the cursor to the end of it. Type “rd.break” (This will break just before control is handed from the initramfs to the actual system).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/5.png)

Then press “Ctrl+x” to save those changes. The Initramfs debug shell will appear.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/6.png)

Next, we have to provide read and write permissions to /sysroot by typing the below command:

```
mount -o remount,rw /sysroot/
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/7.png)

Now switch into chroot jail.

```
chroot /sysroot
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/8.png)

In here, /sysroot is treated as the root of the file system tree.

Next you'll set a new root password.

```
passwd root
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/9.png)

And relabel the files.

```
touch /.autorelabel
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/10.png)

Finally, type “exit” twice.

The first one will exit from the chroot jail.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/11.png)

The next one will exit from the initramfs debug shell and reboots the system.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/12.png)

Now you can login as root with your updated password.

Please feel free to let me know if you have any questions. You can contact and connect with me on [Twitter](https://twitter.com/ThanoshanMV).

Thank you for reading.

**Happy Coding!**


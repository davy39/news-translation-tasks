---
title: 'Linux: How to Add Users and Create Users with useradd'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-17T02:11:12.000Z'
originalURL: https://freecodecamp.org/news/linux-how-to-add-users-and-create-users-with-useradd
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c8c740569d1a4ca32d2.jpg
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "By Jackson Bates\nIf more than one person is using your Linux machine at\
  \ home, or you are managing a server that provides access to multiple users, the\
  \ useradd command is essential for creating users. \nAlso, many of the services\
  \ you use as a developer..."
---

By Jackson Bates

If more than one person is using your Linux machine at home, or you are managing a server that provides access to multiple users, the `useradd` command is essential for creating users. 

Also, many of the services you use as a developer may require their own user accounts to function. So even as a solo dev on your own machine, you may find yourself reaching for these commands when you install MySQL or something similar.

You can get a full overview of the various options available to you by viewing the man page for the utility: `man useradd`

But if that is overwhelming, here's a breakdown of some of the common options you might use when creating a user.

## Create a user

The simple format for this command is `useradd [options] USERNAME`.

For example `useradd test` (as the root user - prefix with `sudo` if you are not logged in as root).

This will create a user called test, but it's a limited operation and will not create other useful things like their home directory or password!

## Add a password

You then add a password for the test user by using the `passwd` command: `passwd test`. This will prompt you to enter a password for the user.

_There is an option for adding an encrypted password via the `-p` option on `useradd`, but this is not recommended for security purposes._ 

Note that the `-p` option doesn't allow you to input a plaintext password, it expects you to encrypt it first. This is intentionally difficult, because you should **not** do it! Just use the `passwd` command.

## Other common options

### Home directories

In order to create a user with the default home directory use the following option:

`useradd -m test`

This user now has a /home/test directory.

To change the home directory, you can pass an extra option to modify this, for example:

`useradd -m -d /alternate test`

### Shell

By default, your created users will likely have the default login shell bin/bash or bin/sh, which will be defined in `/etc/default/useradd`.

You can override this default with the `-s` option:

`useradd -s usr/bin/zsh test`

## Putting it all together

To construct the whole command, you put the options in one after another - the order does not matter - and end with the username you wish to create.

So creating a user with a home directory and a customized shell would look like this:

`useradd -m -s /usr/bin/zsh user`

And then you would add a password for the user: `passwd user`

## Read the Fine Manual

Now that you've seen the basics of what this tool can do, hopefully the man page is a little more navigable.

`man useradd` will show you how to add things like expiry dates on the account, assign groups, and so on.





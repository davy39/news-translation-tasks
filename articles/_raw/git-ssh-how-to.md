---
title: How to Get and Configure Your Git and GitHub SSH Keys
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T17:46:00.000Z'
originalURL: https://freecodecamp.org/news/git-ssh-how-to
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e49740569d1a4ca3c4e.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: ssh
  slug: ssh
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'If you use GitHub without setting up an SSH key, you''re really missing
  out. Just think–all of that time you spent entering your email address and password
  into the console every time you push a commit could have been spent coding.

  Well no more. Here''...'
---

If you use GitHub without setting up an SSH key, you're really missing out. Just think–all of that time you spent entering your email address and password into the console every time you push a commit could have been spent coding.

Well no more. Here's a quick guide to generate and configure an SSH key with GitHub so you never have to authenticate the old fashioned way again.

### Check for an existing SSH key

First, check if you've already generated SSH keys for your machine. Open a terminal and enter the following command:

```shell
ls -al ~/.ssh
```

If you've already generated SSH keys, you should see output similar to this:

```sh
-rw-------  1 user_name user_name  1766 Jul  7  2018 id_rsa
-rw-r--r--  1 user_name user_name   414 Jul  7  2018 id_rsa.pub
-rw-------  1 user_name user_name 12892 Feb  5 18:39 known_hosts
```

If your keys already exist, skip ahead to the **Copy your public SSH key** section below.

If you don't see any output or that directory doesn't exist (you get a `No such file or directory` message), then run:

```shell
mkdir $HOME/.ssh
```

Then generate a new set of keys with:

```shell
ssh-keygen -t rsa -b 4096 -C your@email.com
```

Now check that your keys exist with the `ls -al ~/.ssh` command and ensure that the output is similar to the one listed above.

**Note:** SSH keys are always generated as a pair of public (`id_rsa.pub`) and private (`id_rsa`) keys. It's extremely important that you **never reveal your private** key, and **only use your public** key for things like GitHub authentication. You can read more about how SSH / RSA key pairs work [here](https://www.freecodecamp.org/news/a-top-down-introduction-to-ssh-965f4fadd32e/).

### Add your SSH key to ssh-agent 

`ssh-agent` is a program that starts when you log in and stores your private keys. For it to work properly, it needs to be running and have a copy of your private key.

First, make sure that `ssh-agent` is running with:

```shell
eval "$(ssh-agent -s)" # for Mac and Linux
```

or:

```shell
eval `ssh-agent -s`
ssh-agent -s # for Windows
```

Then, add your private key to `ssh-agent` with:

```shell
ssh-add ~/.ssh/id_rsa
```

### Copy your public SSH key

Next, you need to copy your public SSH key to the clipboard.

For Linux or Mac, print the contents of your public key to the console with:

```shell
cat ~/.ssh/id_rsa.pub # Linux
```

Then highlight and copy the output.

Or for Windows, simply run:

```shell
clip < ~/.ssh/id_rsa.pub # Windows
```

### Add your public SSH key to GitHub

Go to your GitHub [settings](https://github.com/settings/keys) page and click the "New SSH key" button:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image-14.png)

Then give your key a recognizable title and paste in your public (`id_rsa.pub`) key:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image-15.png)

Finally, test your authentication with:

```shell
ssh -T git@github.com
```

If you've followed all of these steps correctly, you should see this message:

```sh
Hi your_user_name! You've successfully authenticated, but GitHub does not provide shell access.

```

### More info on SSH:

* [Ultimate guide to SSH](https://www.freecodecamp.org/news/the-ultimate-guide-to-ssh-setting-up-ssh-keys/)
* [A top-down intro to SSH](https://www.freecodecamp.org/news/a-top-down-introduction-to-ssh-965f4fadd32e/)


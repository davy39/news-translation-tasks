---
title: Upgrading to MacOS Sierra will break your SSH keys and lock you out of your
  own servers.
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2016-10-11T00:54:24.000Z'
originalURL: https://freecodecamp.org/news/upgrading-to-macos-sierra-will-break-your-ssh-keys-and-lock-you-out-of-your-own-servers-f413ac96139a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4BPoUrWcf67bdaKyZPARMg.png
tags:
- name: Apple
  slug: apple
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'Do not upgrade to macOS Sierra if you have a cloud server (AWS, Digital
  Ocean, etc.) Read this post first. It will walk you through safely updating to Sierra
  and updating your SSH keys.

  Like many developers, I got a notice from Apple bugging me to in...'
---

Do not upgrade to macOS Sierra if you have a cloud server (AWS, Digital Ocean, etc.) Read this post first. It will walk you through safely updating to Sierra and updating your SSH keys.

Like many developers, I got a notice from Apple bugging me to install its new macOS Sierra. I clicked “remind me tomorrow” a few days in a row. Then I finally caved one night before going to bed.

When I woke up, I was no longer able to access Free Code Camp’s servers. It took me a while to realize what had happened. Luckily [BerkeleyTrue](https://www.freecodecamp.org/news/upgrading-to-macos-sierra-will-break-your-ssh-keys-and-lock-you-out-of-your-own-servers-f413ac96139a/undefined) hadn’t upgraded yet, and was able to add my new SSH keys.

It turns out Apple decided to quietly force 2048-bit RSA keys on everyone, which has been a mild inconvenience for some, and a confused panic for others.

If you’re wondering why RSA keys are more secure than the old DSA keys, [they aren’t inherently so](http://security.stackexchange.com/a/5100). But DSA keys can usually only be 1024 bits, while RSA keys can be longer, which is the case with Sierra’s default 2048-bit RSA keys. Those extra bits make these new keys substantially harder to crack.

Let’s set up your new 2048-bit RSA SSH key.

### Step #1: delete your old key and create a new one

First, let’s check and make sure you indeed need a new key.

Open up your terminal and type:

```
ssh-keygen -l -f ~/.ssh/id_rsa.pub
```

If the prompt responds with a string that starts with “2048 SHA256” you’re done and don’t need to take any further action.

Otherwise, create a new key by running:

```
ssh-keygen -t rsa
```

The prompt should respond with:

```
Generating public/private rsa key pair.Enter file in which to save the key (/Users/freecodecamp/.ssh/id_rsa):
```

You can just press enter to save it in the default place. Note that this will overwrite your old (broken) key.

```
Enter passphrase (empty for no passphrase):
```

You can leave this blank or add a password for a little extra security (and a lot more typing).

Then you’ll get with a cool random “art” that always seems to be shaped like a Christmas tree:

![Image](https://cdn-media-1.freecodecamp.org/images/1*NkRrhr4WF93hhtIKS2eIrg.png)
_This was created for this article — it’s not the one I use._

Now make sure your key has the right access permissions by running:

```
sudo chmod 600 ~/.ssh/id_rsa
```

You can check the contents of your public key by running:

```
cat ~/.ssh/id_rsa.pub
```

Which should return something like:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDijWK+s3ybgzEdaJ5LneNU11BsIyoNS51SV11Vi5auPJW9+Ji6OUSJ9OguZh4T019ULyFF/Qq66fhH9TvMzw80lTNoChgTRMpjs2+Qg75yTINKSde+Gv4TK6UvNw6EINORcTpb32Im9hgtdTj6WqJ/hCbSltv7IfFZU5ChV7SxTaoNZTa9M5H3N8YdQ/aGt3puh222Cq5DTjV8fRWaNVvjVQRe/huHAHEzEUr1T/eTlXtoFtGeC1z+pLfYllVzizoS7tyuUksfgqox1jJJMpaZ25V/R/p/MDUc936za/8zgB8OQFRBbrP6JvXXN99DLcvs9coz9vfb2GCVrhxi1aJ5 quincy@FreeCodeCamp
```

You’ll need to put this key on your server. To ensure you copy all of it, I recommend you can copy it directly to your clipboard by running:

```
pbcopy < ~/.ssh/id_rsa.pub
```

### Step #2: add your new public key to your server

If you can SSH into your server without your key, then try to gain access using a password if you have one.

Otherwise you’ll need to ask someone else who has access to the server to do this for you.

If you’ve disabled password access to your server (which many experts would recommend for security reasons), you may be able to [temporarily re-enable password access](http://jeffreifman.com/2016/10/01/fix-macos-sierra-upgrade-breaking-ssh-keys/).

Once you have root access to your server — assuming it’s a Linux server — you just need to run this command:

```
nano ~/.ssh/authorized_keys
```

This will open up your authorized key file using the minimalist text editor “nano” that is included with most Linux distributions. Or you could use Vim.

Then paste in your public SSH key from earlier. Hit control+o to save your changes, then control+x to quit nano.

Disconnect from your server. Now you’re ready to try logging in using your new SSH key.

### Step #3: SSH into your server

Run this command to SSH in, replacing root@0.0.0.0 with your server’s login and IP address:

```
ssh -i ~/.ssh/id_rsa root@0.0.0.0
```

You should gain normal SSH access to your to your server, without needing to enter a password.

Congratulations! You’re back where you were yesterday, except now Apple will quit bugging you about upgrading your operating system. ?

**I only write about programming and technology. If you [follow me on Twitter](https://twitter.com/ossia) I won’t waste your time. ?**


---
title: What to do when key-based authentication isn’t working after ssh-copy-id
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-06T16:54:49.000Z'
originalURL: https://freecodecamp.org/news/key-based-authentication-not-working-after-ssh-copy-id-abef7f401d23
coverImage: https://cdn-media-1.freecodecamp.org/images/1*azA9xUZXf6WuDEcVBZ5W-g.png
tags:
- name: authentication
  slug: authentication
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Ubuntu
  slug: ubuntu
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Arit Amana

  I recently provisioned a Ubuntu virtual private server (VPS) on Vultr. I’m partial
  to CentOS myself, but the task I was working on recommended Ubuntu.

  To set up key-based authentication from my laptop to the server,


  I generated a new S...'
---

By Arit Amana

I recently provisioned a Ubuntu virtual private server (VPS) on Vultr. I’m partial to CentOS myself, but the task I was working on recommended Ubuntu.

To set up key-based authentication from my laptop to the server,

* I generated a new SSH keypair (named “ubuntu”) on my Mac using the command: `ssh-keygen -t rsa -b 4096`
* I then used the `ssh-copy-id` utility to copy my public key over to the `authorized_keys` file on my Vultr VPS: `ssh-copy-id -i .ssh/ubuntu aritdev@123.456.789.000`

As I expected, the utility asked for my VPS password in order to complete the public key transfer. When all was done, I attempted to login to my VPS.

It should have let me through without requiring a password:

`ssh -i .ssh/ubuntu aritdev@123.456.789.000`

But I kept getting prompted for a password. ?

* I checked my `authorized_keys` file over on the VPS to make sure my public key had been copied over correctly. Check. ??
* I made sure that the file was read-write only for myself and none others. Check. ??
* I made sure that the following options were enabled in `/etc/ssh/sshd_config`:`PubkeyAuthentication yes` and `AuthorizedKeysFile .ssh/authorized_keys`. Check. ??

Still, I kept getting prompted for a password upon login from my laptop.

After a few minutes on StackOverflow, I learned about Encrypted Home Directories, which are default in some environments, including Ubuntu.

Encrypted home directories aren’t decrypted until the initial login is successful. However, my `authorized_keys` file is stored in my home directory.

Therefore, my first connection attempt will require a password. Subsequent connections will succeed without a password, since the SSH service will then be able to read my `authorized_keys` file in my decrypted home directory.

To get around this, I created a directory named after my username `aritdev` outside of my home directory (I chose `/etc/`), and gave it full permissions for myself, but read-execute permissions for everyone else. Next, I moved my `authorized_keys` file into `/etc/aritdev/`. Then, I updated the `AuthorizedKeysFile` parameter in `/etc/ssh/sshd_config`:

`AuthorizedKeysFile /etc/%u/authorized_keys`

Finally, I restarted the SSH service. To test, I logged out of my VPS, then attempted to log back in. BOOM - it worked! ??

What issues related to server authentication have you experienced? How did you solve them? Please share below! ??


---
title: How to Use SFTP to Securely Transfer Files with a Remote Server
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d1c740569d1a4ca35f2.jpg
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: toothbrush
  slug: toothbrush
- name: unix
  slug: unix
seo_title: null
seo_desc: 'This article is a quick tutorial on how to use Secure File Transfer Protocol
  (SFTP) to exchange files with a server. This is useful for programming, as it allows
  you to code and test locally, and then send your work to the server when you are
  done.

  T...'
---

This article is a quick tutorial on how to use Secure File Transfer Protocol (SFTP) to exchange files with a server. This is useful for programming, as it allows you to code and test locally, and then send your work to the server when you are done.

### **Testing SSH**

If you haven’t already, test that you are able to SSH into the server. SFTP uses the Secure Shell (SSH) protocol, so if you are unable to SSH you probably won’t be able to SFTP either.

```unix
ssh your_username@hostname_or_ip_address
```

### **Start SFTP Session**

This uses the same syntax as SSH and opens a session in which you can transfer files.

```unix
sftp your_username@hostname_or_ip_address
```

To list helpful commands:

```unix
help
```

### **Transfer files and folders**

To download a file:

```unix
get <filename>
```

To download a folder and its contents, use the “-r” flag (also works for uploading):

```unix
get -r <foldername>
```

To upload a file:

```unix
put <filename>
```

### **Change folders**

To change the local folder:

```unix
lcd <path/to/folder>
```

To change the remote folder:

```unix
cd <path/to/folder>
```


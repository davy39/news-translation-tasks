---
title: Install and configure an FTP server in Redhat/Centos Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-13T19:10:00.000Z'
originalURL: https://freecodecamp.org/news/install-and-configure-ftp-server-in-redhat-centos-linux
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9de9740569d1a4ca3a50.jpg
tags:
- name: Linux
  slug: linux
- name: servers
  slug: servers
seo_title: null
seo_desc: 'FTP stands for File Transfer Protocol. It was written by Abhay Bhushan
  and published as RFC 114 on 16 April 1971. It is supported by all operating systems
  and browsers. It is built on a client-server architecture.

  How to Install and configure FTP ser...'
---

FTP stands for File Transfer Protocol. It was written by Abhay Bhushan and published as RFC 114 on 16 April 1971. It is supported by all operating systems and browsers. It is built on a client-server architecture.

## **How to Install and configure FTP server in Redhat/Centos Linux**

Step 1: We will use localhost for our machine to setup the ftp server.

Step 2: Install the vsftpd (very secure FTP daemon) package.

`yum install -y vsftpd`

Step 3: Start the FTP Server when the system is on.

`systemctl enable vsftpd.service`

Step 4: Check the status of the ftp server

`systemctl status vsftpd.service`

Step 5: Configure the vsftpd package. We will edit `/etc/vsftpd/vsftpd.conf`.

`Change the line which contain anonymous_enable=NO to anonymous_enable=YES`  
`This will give permit any one to access FTP server with authentication.`  
`Change the following to YES`  
`local_enable=YES`  
`write_enable=YES<br>`

Step 6: Start the FTP Server  
`systemctl start vsftpd.service`

Step 7: Install the FTP Client  
`yum install -y lftpd`

Step 8: Connect ftp to localhost  
`lftp localhost`


---
title: Installer et configurer un serveur FTP sous Redhat/Centos Linux
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
seo_title: Installer et configurer un serveur FTP sous Redhat/Centos Linux
seo_desc: 'FTP stands for File Transfer Protocol. It was written by Abhay Bhushan
  and published as RFC 114 on 16 April 1971. It is supported by all operating systems
  and browsers. It is built on a client-server architecture.

  How to Install and configure FTP ser...'
---

FTP signifie File Transfer Protocol. Il a été écrit par Abhay Bhushan et publié sous le nom de RFC 114 le 16 avril 1971. Il est pris en charge par tous les systèmes d'exploitation et les navigateurs. Il est basé sur une architecture client-serveur.

## **Comment installer et configurer un serveur FTP sous Redhat/Centos Linux**

Étape 1 : Nous utiliserons localhost pour notre machine afin de configurer le serveur FTP.

Étape 2 : Installez le paquet vsftpd (very secure FTP daemon).

`yum install -y vsftpd`

Étape 3 : Démarrez le serveur FTP lorsque le système est en marche.

`systemctl enable vsftpd.service`

Étape 4 : Vérifiez l'état du serveur FTP

`systemctl status vsftpd.service`

Étape 5 : Configurez le paquet vsftpd. Nous allons éditer `/etc/vsftpd/vsftpd.conf`.

`Changez la ligne qui contient anonymous_enable=NO en anonymous_enable=YES`  
`Cela permettra à quiconque d'accéder au serveur FTP avec authentification.`  
`Changez les éléments suivants en YES`  
`local_enable=YES`  
`write_enable=YES<br>`

Étape 6 : Démarrez le serveur FTP  
`systemctl start vsftpd.service`

Étape 7 : Installez le client FTP  
`yum install -y lftpd`

Étape 8 : Connectez FTP à localhost  
`lftp localhost`
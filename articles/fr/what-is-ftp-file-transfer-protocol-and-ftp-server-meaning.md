---
title: Qu'est-ce que le FTP ? Protocole de transfert de fichiers et signification
  du serveur FTP
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-21T01:01:16.000Z'
originalURL: https://freecodecamp.org/news/what-is-ftp-file-transfer-protocol-and-ftp-server-meaning
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/thisisengineering-raeng-zBLtU0zbJcU-unsplash--1-.jpg
tags:
- name: computer network
  slug: computer-network
- name: Security
  slug: security
seo_title: Qu'est-ce que le FTP ? Protocole de transfert de fichiers et signification
  du serveur FTP
seo_desc: "FTP stands for File Transfer Protocol. This is a network/communication\
  \ protocol for transferring files between computers over a TCP/IP (Transmission\
  \ Control Protocol/Internet Protocol) network. \nExamples of TCP/IP networks are:\n\
  \nHTTP (Hypertext Trans..."
---

FTP signifie File Transfer Protocol (Protocole de Transfert de Fichiers). Il s'agit d'un protocole de réseau/communication permettant de transférer des fichiers entre des ordinateurs sur un réseau TCP/IP (Transmission Control Protocol/Internet Protocol).

Exemples de réseaux TCP/IP :

* HTTP (Hypertext Transfer Protocol).
* HTTPS (Hypertext Transfer Protocol Secure).
* FTP (File Transfer Protocol).

## Comment fonctionne le protocole de transfert de fichiers ?

Pour transférer des fichiers entre des ordinateurs en utilisant le FTP, vous devez visiter un serveur FTP (j'expliquerai ce qu'est un serveur FTP ci-dessous).

Selon le type de serveur que vous visitez, il peut être nécessaire d'entrer un nom d'utilisateur et un mot de passe pour accéder aux fichiers du serveur. Les connexions de serveur qui ne nécessitent aucune forme d'authentification avant d'accéder aux fichiers sont appelées FTP anonyme.

Lorsque l'utilisateur a réussi à visiter/se connecter à un serveur FTP, il peut soit télécharger, soit téléverser des fichiers sur le serveur.

Il existe deux façons générales d'accéder à un serveur FTP :

* Via un navigateur web. Vous pouvez le faire en tapant l'adresse du serveur dans votre navigateur. Cette adresse pourrait ressembler à ceci : ftp.monftpfichiers.com ou https://www.monftpfichiers.com. Une fois sur le serveur, vous pouvez alors interagir avec les fichiers téléversés sur le serveur par le propriétaire.
* Via un client FTP. Nous discuterons des clients FTP dans la section suivante.

## Qu'est-ce qu'un client FTP ?

Un client FTP est un logiciel qui crée une connexion entre l'ordinateur demandant l'accès et le serveur où les fichiers sont stockés.

Il existe de nombreux logiciels clients FTP disponibles. Ils fournissent une interface graphique (GUI) avec laquelle nous pouvons interagir.

Ci-dessous, nous verrons à quoi ressemble un client FTP et comment nous pouvons l'utiliser. Nous utiliserons [FileZilla](https://filezilla-project.org/).

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--270--1.png)

Dans l'image ci-dessus, il y a différents champs de texte. Le champ de texte `Host` est l'endroit où l'adresse du serveur est tapée.

Les champs de texte `Username` et `Password` sont pour les serveurs qui nécessitent une authentification avant d'accorder l'accès.

Le champ de texte `Port` est généralement 21. Il s'agit d'un port dédié aux FTP.

Une fois que vous avez rempli les champs de texte nécessaires, vous pouvez cliquer sur `Quickconnect` pour vous connecter au serveur.

Sur le côté gauche du logiciel se trouve le `site local` qui est mon ordinateur avec une liste des répertoires existants.

Sur le côté droit se trouve le `site distant` où toutes les informations et fichiers d'un serveur seront affichés.

## Qu'est-ce qu'un serveur FTP ?

Un serveur FTP est essentiellement l'ordinateur où tous les fichiers sont initialement téléversés. Chaque serveur a une adresse FTP qu'un utilisateur peut visiter via un TCP/IP à travers un navigateur ou un client FTP.

Le serveur permet au visiteur de télécharger et de téléverser des fichiers.

## Les serveurs FTP sont-ils sécurisés ?

Bien que de nombreux serveurs FTP nécessitent une authentification, ils ne sont pas sécurisés car le protocole manque de chiffrement. Cela rend plus probable l'accès aux fichiers stockés sur un serveur FTP par un tiers non désiré.

Le protocole le plus préféré et plus sécurisé que le FTP est le SFTP, qui signifie Secure File Transfer Protocol. Tout comme HTTP et HTTPS.

Le SFTP est plus sécurisé car les données stockées sur le serveur sont chiffrées.

D'autres alternatives incluent :

* FTPS (File Transfer Protocol Secure).
* HTTPS (Hypertext Transfer Protocol Secure).
* AS2 (Applicability Statement 2).

## Avantages de l'utilisation du FTP

Voici quelques-uns des avantages de l'utilisation du FTP :

* Transfert plus rapide des fichiers.
* Supporté par de nombreux hôtes.
* Supporte le transfert de gros fichiers.
* Capacité à planifier des transferts.
* Les transferts peuvent être repris lorsqu'ils sont interrompus.

## Inconvénients de l'utilisation du FTP

Voici quelques-uns des inconvénients de l'utilisation du FTP :

* Les serveurs FTP manquent de sécurité.
* Les principaux navigateurs comme Chrome et Firefox ne supportent plus le FTP.
* Les identifiants de l'utilisateur et les fichiers ne sont pas chiffrés.
* Certains serveurs peuvent contenir des fichiers nuisibles.

## Conclusion

Dans cet article, nous avons parlé du protocole de transfert de fichiers qui nous permet de transférer des fichiers entre des ordinateurs sur un réseau.

Nous avons vu ce qu'est un client FTP et un serveur FTP. Nous avons également parlé de pourquoi les serveurs FTP sont non sécurisés et d'autres alternatives sécurisées que nous pouvons utiliser.

Enfin, nous avons vu les avantages et les inconvénients de l'utilisation du FTP.

Merci d'avoir lu !
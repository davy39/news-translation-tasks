---
title: Comment installer sbt sur Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-15T03:46:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-sbt-on-linux
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/sbt-1.png
tags:
- name: coding
  slug: coding
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment installer sbt sur Linux
seo_desc: 'By Sanjula Madurapperuma

  Introduction

  Hi! I am Sanjula, and in this guide I hope to teach you how to install sbt on Linux.

  Let’s get started!

  What is sbt?

  sbt is an open-source, cross-platform build tool for Scala and Java projects.

  Some of its main ...'
---

Par Sanjula Madurapperuma

### Introduction

Bonjour ! Je suis [Sanjula](https://www.linkedin.com/in/sanjula-madurapperuma/), et dans ce guide, j'espère vous apprendre à installer sbt sur Linux.

Commençons !

### Qu'est-ce que sbt ?

sbt est un outil de construction open-source et multiplateforme pour les projets Scala et Java.

Quelques-unes de ses principales caractéristiques sont :

* Prise en charge de la compilation, des tests et du déploiement continus.
* Prise en charge native de la compilation du code Scala.
* Gestion des dépendances utilisant Ivy.
* Capacité à construire des descriptions écrites en Scala en utilisant un DSL (Domain-Specific Language).

### Étapes pour installer sbt

* Tout d'abord, vous devez vous assurer qu'un JDK est installé. sbt recommande l'Oracle JDK 8 ou OpenJDK 8.
* Ouvrez un terminal et tapez la commande suivante, qui pointera vers la distribution debian de sbt et ajoutera sbt à la liste des sources.

```
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*KgNADEh4KyRZf98H4d0T4g.png)
_Figure-2 : Ajout de l'URL sbt à la liste des sources_

* Ensuite, entrez la commande ci-dessous, qui ajoute la clé de scala à la liste des clés utilisée par apt pour authentifier les paquets.

```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*JNJINkN6aWH64wi7aIyBsw.png)
_Figure-3 : Ajout de sbt à la liste des clés utilisée par apt_

* Maintenant, téléchargez les listes de paquets depuis les dépôts pour vous assurer que la liste d'informations sur la dernière version des paquets et leurs dépendances est mise à jour localement.sudo apt-get update
* Enfin, exécutez la commande suivante pour installer sbt.sudo apt-get install sbt

![Image](https://cdn-media-1.freecodecamp.org/images/1*R8eFHroAfiqfwjLTbwB4kQ.png)
_Figure-4 : J'ai déjà sbt installé :)_

**Félicitations !!!** Vous avez maintenant installé l'outil de construction sbt sur votre PC Linux ! Vous pouvez maintenant facilement travailler avec des projets Scala et Java.

**En attendant, vous** pouvez partager **cet article si vous l'avez aimé, ou me** contacter **pour toute préoccupation. Veuillez également consulter mon profil sur** [**LinkedIn**](https://www.linkedin.com/in/sanjula-madurapperuma/) **et me suivre sur Twitter !**
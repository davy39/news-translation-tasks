---
title: Comment installer Arch Linux à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-18T20:13:22.000Z'
originalURL: https://freecodecamp.org/news/installing-arch-linux-from-scratch-b595095ddd48
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb6ec740569d1a4cae100.jpg
tags:
- name: Archibold
  slug: archibold
- name: ArchLinux
  slug: archlinux
- name: Linux
  slug: linux
- name: technology
  slug: technology
- name: 'VirtualBox '
  slug: virtualbox
seo_title: Comment installer Arch Linux à partir de zéro
seo_desc: 'By Andrea Giammarchi

  In this article, you''ll learn how to install Arch Linux from scratch… and in about
  5 minutes. So let''s get to it.

  As of today, it’s been more or less 3 years I am happily using Arch Linux as my
  primary Operating System, and I’ve ...'
---

Par Andrea Giammarchi

Dans cet article, vous apprendrez comment installer Arch Linux à partir de zéro… et en environ 5 minutes. Alors, commençons.

À ce jour, cela fait plus ou moins 3 ans que j'utilise heureusement Arch Linux comme mon système d'exploitation principal, et je l'ai utilisé quotidiennement non seulement sur mon ordinateur portable, mais aussi sur mon [PC de Gaming](https://medium.com/@WebReflection/a-gaming-pc-without-breaking-the-bank-b56c73bba1e7#.ktf73jt1x) et de nombreux [Single Board Computers](https://benja.io/) également.

J'ai utilisé mon installeur [archibold.io](https://archibold.io/) pendant un certain temps, et récemment je l'ai réécrit après avoir appris de plus en plus sur Arch Linux.

Ce post est à propos de _moi_ qui donne en retour quelques choses que j'ai apprises du projet [Arch Linux](https://www.archlinux.org/) et de sa communauté, en espérant simplifier la vie à quiconque souhaiterait adopter cette distribution géniale !

### Démarrage d'un système d'exploitation Linux en un clin d'œil

Vous avez besoin d'une partition spéciale reconnue comme amorçable, et avec un fichier binaire automatiquement reconnu capable de dire à la carte mère comment démarrer, et où démarrer.

Dans le monde d'Arch Linux, il y a essentiellement 3 acteurs majeurs : [U-Boot](http://www.denx.de/wiki/U-Boot/WebHome), le chargeur de démarrage par défaut utilisé par les ports [Arch Linux ARM](https://archlinuxarm.org/), [Syslinux](http://www.syslinux.org/wiki/index.php?title=The_Syslinux_Project), qui est le choix préféré de l'installeur ISO d'Arch Linux lui-même, et [Grub](https://www.gnu.org/software/grub/), généralement plus facile à configurer sur les systèmes multi-démarrage, ce qui n'est pas dans le cadre de ce post.

Les outils pour gérer les partitions sont généralement au nombre de 2 : **parted**, préféré lorsqu'il s'agit de fonctionnalités avancées comme la partition UEFI et l'alignement optimisé du disque, ou **fdisk**, qui fonctionne simplement et fait le travail de manière "moins scriptée".

#### Comment démarrer ?

Il existe quelques façons de dire à une carte mère comment démarrer un système : la configuration [UEFI](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface), qui est principalement adaptée aux systèmes d'exploitation Windows fonctionnant sur les processeurs Intel mais utilisable également pour démarrer des distributions Linux, et le mode compatible BIOS hérité, qui a moins de fonctionnalités que l'UEFI mais qui fonctionne toujours (et est le plus largement disponible).

En plus de cette distinction, bien que l'UEFI ait un mode de démarrage sécurisé, qui est encore une fois essentiellement une chose spécifique à Windows uniquement, un démarrage peut également inclure des commandes spéciales capables d'activer ou de désactiver un mode [EDD](https://en.wikipedia.org/wiki/INT_13H#EDD), qui est une bonne vieille technologie _Enhanced Disk Drive_ qui peut ne pas être nécessaire au moment du démarrage et dans certains cas devrait être explicitement désactivée comme dans les images VirtualBox ou certains SBC basés sur AMD comme la carte Gizmo 2.

#### Démarrer quoi ?

Il existe un seul système de fichiers consolidé, multiplateforme et universel, et c'est malheureusement ou heureusement le bon vieux [FAT](https://en.wikipedia.org/wiki/File_Allocation_Table).

Il existe sûrement des options plus adaptées, plus sécurisées, plus rapides et plus respectueuses du matériel, mais FAT avec un chargeur est un choix sûr avec UEFI et le mode hérité.

En quelques mots, le nombre le plus basique de partitions sur votre système devrait être de 2 : une FAT amorçable, et une autre "ce que vous voulez". Veuillez noter que [ext4](https://en.wikipedia.org/wiki/Ext4) est encore un choix très valable pour les tâches quotidiennes, mais il existe quelques alternatives valables à considérer, bien que cela ne fasse pas partie du cadre de ce post.

#### Échange (Swap) ?

Si vous installez Arch Linux sur un système avec plus de 4 Go de RAM, et que vous ne prévoyez pas d'utiliser ce système pour développer des logiciels complexes, je dirais que vous ne devriez pas trop vous soucier d'avoir une partition d'échange (swap) de secours.

En général, les vieux ordinateurs portables que j'ai testés, avec seulement 2 Go de RAM, ont très bien fonctionné sans échange supplémentaire et avec un bureau graphique comme [GNOME](https://www.gnome.org/) sans effort.

Cependant, si vous souhaitez avoir un peu plus d'espace pour construire des logiciels plus complexes, et que vous avez plus de 1 Go de RAM, utilisez 1/4 de la quantité de votre RAM et vous serez bien.

### OK, mais où sont toutes les commandes pour installer Linux ?

C'est la meilleure partie de ce post, le moment où vous avez atteint cette partie est le moment où vous êtes auto-formé pour répondre à toutes les questions de base que l'installeur **archibold.io** va vous poser.

Téléchargez l'[ISO d'Arch Linux](https://www.archlinux.org/download/) depuis le site web, et utilisez-le pour un démarrage VirtualBox, ou [gravez-le sur une clé USB en suivant cette page Wiki](https://wiki.archlinux.org/index.php/USB_flash_installation_media), vous aurez tout ce dont vous avez besoin pour démarrer dans un terminal et exécuter le code suivant :

```
$ bash <(curl -s archibold.io/base)
```

C'est à peu près tout, la procédure installera l'Arch Linux le plus basique que vous puissiez imaginer sur votre machine ou, comme le montre la vidéo en haut de ce post, sur une VirtualBox, au cas où vous voudriez l'essayer d'abord.

### OK, cool… mais j'aimerais aussi avoir un bureau !

Dans ce cas, une fois que vous avez démarré dans votre compte, vous pouvez vérifier si vous avez une connexion internet en tapant :

```
ip addr
```

et si rien n'apparaît sous le nom de votre wifi ou ethernet, suivez ces instructions :

```
# si vous n'êtes pas connecté en tant que root, tapez 'su'su# utilisez root comme mot de passe par défaut# maintenant, dans le cas où vous avez une connexion filaireip addr # pour voir le nom de l'adaptateurdhcpcd enp0s3 # où enp0s3 est juste un nom inventé, utilisez le vôtre
```

```
# si c'était une carte wi-fiwifi-menu # et configurez-la
```

```
exit # pour revenir à votre utilisateur
```

Une fois que vous avez une connexion internet, vous pouvez simplement utiliser un autre assistant :

```
bash <(curl -s archibold.io/install/gnome)
```

Ce dernier vous guidera pour installer le meilleur environnement de bureau disponible.

#### C'est bien… mais…

Si vous êtes bloqué à un moment donné, n'hésitez pas à signaler un bug dans le [dépôt open source archibold](https://github.com/WebReflection/archibold.io/tree/gh-pages), ou simplement me poser des questions ici.

Je suis assez sûr de pouvoir répondre à la plupart d'entre elles… alors, à vous de jouer ! :-)
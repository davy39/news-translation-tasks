---
title: Comment faire un dual boot Windows 10 et Ubuntu – Tutoriel de dual boot Linux
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-24T20:09:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-dual-boot-windows-10-and-ubuntu-linux-dual-booting-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/dualBoot--1-.png
tags:
- name: Linux
  slug: linux
- name: Windows 10
  slug: windows-10
seo_title: Comment faire un dual boot Windows 10 et Ubuntu – Tutoriel de dual boot
  Linux
seo_desc: "You don’t have to have two different computers to use Linux and Windows\
  \ 10. It's possible to have a Linux distro installed on a computer with Windows\
  \ 10 preinstalled. \nIn this article, I will show you how to dual boot Windows 10\
  \ and the popular Ubunt..."
---

Vous n'avez pas besoin d'avoir deux ordinateurs différents pour utiliser Linux et Windows 10. Il est possible d'avoir une distribution Linux installée sur un ordinateur avec Windows 10 préinstallé. 

Dans cet article, je vais vous montrer comment faire un dual boot Windows 10 et la populaire distribution Linux Ubuntu. Mais avant cela, vous devez installer Ubuntu sur votre PC Windows 10.

Avant de suivre ce processus, vous devez sauvegarder vos fichiers. C'est parce que l'installation d'un système d'exploitation est un processus risqué. Parfois, cela peut écraser le système d'exploitation existant et supprimer tous vos fichiers.

**N.B.** : La plupart des processus de cet article prennent du temps à se terminer, donc vous devez être patient.

## Ce que nous allons couvrir – Un guide étape par étape pour le dual boot Windows 10 et Linux
- [Prérequis](#heading-prerequisites) 
- [Comment partitionner votre disque dur pour Ubuntu](#heading-comment-partitionner-votre-disque-dur-pour-ubuntu)
- [Comment optimiser votre disque dur pour plus d'espace de partition (Optionnel)](#heading-comment-optimiser-votre-disque-dur-pour-plus-d-espace-de-partition-optionnel)
- [Comment télécharger Ubuntu au format ISO](#heading-comment-telecharger-ubuntu-au-format-iso)
- [Comment créer une clé USB bootable Ubuntu (Linux)](#heading-comment-creer-une-cle-usb-bootable-ubuntu-linux) 
- [Comment installer la distribution Linux Ubuntu avec Windows 10](#heading-comment-installer-la-distribution-linux-ubuntu-avec-windows-10)
- [Maintenant vous pouvez faire un dual boot Ubuntu et Windows 10](#heading-maintenant-vous-pouvez-faire-un-dual-boot-ubuntu-et-windows-10)
- [Conclusion](#heading-conclusion)

## Prérequis
Plus important encore, il y a certaines choses que vous devez avoir en place si vous voulez utiliser (et faire un dual boot) Ubuntu et Windows 10 sur le même PC :

- Un ordinateur préinstallé avec Windows 10
- Un disque dur partitionné 
- Un BIOS en mode UEFI (Unified Extensible Firmware Interface)
- Une clé USB vide d'au moins 4 Go pour créer un disque bootable
- Une connexion internet pour télécharger l'image ISO d'Ubuntu (la distribution Linux) et Rufus (un outil de création de disque bootable)

## Comment vérifier si le BIOS de votre PC est en mode UEFI
Pour vérifier si le BIOS de votre PC est en mode UEFI, recherchez "informations système" et appuyez sur `ENTRÉE`.
![ss1-5](https://www.freecodecamp.org/news/content/images/2022/08/ss1-5.png) 

Regardez sous le mode BIOS pour confirmer que le mode BIOS de votre PC est UEFI.
![ss2-5](https://www.freecodecamp.org/news/content/images/2022/08/ss2-5.png)

Si le BIOS de votre PC n'est pas en mode UEFI, les deux systèmes d'exploitation ne se verront pas l'un l'autre. Vous pouvez en savoir plus sur [la différence entre ces deux modes ici](https://www.freecodecamp.org/news/uefi-vs-bios/).

## Comment partitionner votre disque dur pour Ubuntu
Vous devez partitionner votre disque dur car vous devez réserver au moins 20 Go pour Ubuntu pour y vivre et démarrer.

**Pour partitionner votre disque dur, suivez les étapes ci-dessous** :

**Étape 1** : Faites un clic droit sur Démarrer et sélectionnez "Gestion des disques".
![ss3-5](https://www.freecodecamp.org/news/content/images/2022/08/ss3-5.png) 

**Étape 2** : Faites un clic droit sur votre disque C et sélectionnez réduire le volume.
![ss4-6](https://www.freecodecamp.org/news/content/images/2022/08/ss4-6.png) 

**Étape 3** : Sélectionnez au moins (20000) 20 Go pour Ubuntu et cliquez sur "Réduire". Cela peut prendre un certain temps, donc soyez patient.
![ss5-6](https://www.freecodecamp.org/news/content/images/2022/08/ss5-6.png) 

**Étape 4** (optionnelle) : Vous pouvez continuer et attribuer une lettre au nouveau volume. Faites un clic droit sur l'espace non alloué et sélectionnez "Nouveau volume simple".
![ss6-5](https://www.freecodecamp.org/news/content/images/2022/08/ss6-5.png) 

**Étape 5** : Suivez l'assistant et attribuez une lettre au lecteur, puis suivez le reste.
![ss7-4](https://www.freecodecamp.org/news/content/images/2022/08/ss7-4.png) 

Après avoir terminé l'assistant, le lecteur doit être listé sur votre ordinateur.
![ss8-4](https://www.freecodecamp.org/news/content/images/2022/08/ss8-4.png) 

Félicitations ! Vous avez partitionné avec succès votre disque dur. 

**N.B.** : Si vous avez beaucoup d'espace libre sur votre disque dur mais que votre PC ne vous a pas donné jusqu'à 20 Go d'espace de partition, alors vous devez optimiser le disque dur de votre PC. Passez à la section suivante de cet article pour le faire.


## Comment optimiser votre disque dur pour plus d'espace de partition (Optionnel)

Le but commun de l'optimisation du disque dur est d'accélérer votre ordinateur pendant le temps de démarrage et de le faire fonctionner plus doucement. 

En même temps, le processus va défragmenter le disque dur et rendre l'espace libre plus disponible pour le partitionnement.

Pour optimiser votre disque dur, cliquez sur Démarrer (touche du logo Windows), recherchez "defrag" et sélectionnez "Défragmenter et optimiser les lecteurs".
![ss9-3](https://www.freecodecamp.org/news/content/images/2022/08/ss9-3.png)

Assurez-vous que votre disque C est surligné, puis cliquez sur "Optimiser".
![ss10-3](https://www.freecodecamp.org/news/content/images/2022/08/ss10-3.png) 

Après avoir réussi à réserver au moins 20 Go pour Ubuntu en partitionnant votre disque dur, il est temps de télécharger Ubuntu et de créer une clé USB bootable.

## Comment télécharger Ubuntu au format ISO
La prochaine étape est de télécharger Ubuntu au format ISO afin de pouvoir installer Ubuntu. Vous pouvez le télécharger depuis le site web de la distribution Ubuntu.
![ss11-3](https://www.freecodecamp.org/news/content/images/2022/08/ss11-3.png) 

Après avoir téléchargé Ubuntu, ne faites rien avec pour l'instant. Vous devez créer une clé USB bootable et y mettre Ubuntu. C'est ainsi que vous pourrez l'utiliser. 

La raison pour laquelle vous ne pouvez pas installer Ubuntu comme ça est qu'il ne vient pas sous forme d'exécutable. Il vient sous forme d'ISO (image de disque optique). Cela signifie que vous devez trouver un disque pour le mettre avant qu'il ne puisse fonctionner.

La partie suivante de ce guide montre comment vous pouvez mettre l'ISO Ubuntu téléchargé sur une clé USB.

## Comment créer une clé USB bootable Ubuntu (Linux) 

Vous ne pourrez pas créer une clé USB bootable pour Ubuntu en plaçant simplement l'image ISO téléchargée dessus. Suivez ces étapes pour le faire :

**Étape 1** : Vous devez télécharger un outil de création de clé USB bootable comme Rufus. Vous pouvez [télécharger Rufus depuis leur site web](https://rufus.ie/en/).
![ss12-3](https://www.freecodecamp.org/news/content/images/2022/08/ss12-3.png) 

**Étape 2** : Insérez la clé USB vide dans votre PC Windows 10. Faites un clic droit sur Rufus et sélectionnez "Ouvrir".
![ss13-1](https://www.freecodecamp.org/news/content/images/2022/08/ss13-1.png) 

**Étape 3** : Sous "Périphérique", sélectionnez votre clé USB. Et sous "Sélection de démarrage", cliquez sur le bouton "Sélectionner" et choisissez le fichier ISO Ubuntu que vous avez téléchargé.

**Étape 4** : Laissez tout le reste par défaut et cliquez sur le bouton "DÉMARRER" pour commencer à graver la distribution Ubuntu sur le lecteur.
![ss14-1](https://www.freecodecamp.org/news/content/images/2022/08/ss14-1.png) 

**Étape 5** : Cliquez sur OK pour démarrer le processus.
![ss15-1](https://www.freecodecamp.org/news/content/images/2022/08/ss15-1.png) 
![ss16-1](https://www.freecodecamp.org/news/content/images/2022/08/ss16-1.png)

Une fois le processus terminé, vous devriez voir "PRÊT" sur un fond vert. Cliquez sur le bouton Fermer. Il est temps d'installer Ubuntu.

Félicitations ! Maintenant vous avez un lecteur bootable avec lequel vous pouvez installer Linux.

L'étape suivante est d'installer la distribution Ubuntu sur votre PC Windows 10. Pour ce faire, vous devez démarrer votre PC à partir de la clé USB bootable que vous avez créée.

## Comment installer la distribution Linux Ubuntu avec Windows 10
**Étape 1** : Assurez-vous que le lecteur bootable est inséré dans votre PC Windows 10

**Étape 2** : Faites un clic droit sur Démarrer, maintenez la touche SHIFT enfoncée et sélectionnez Redémarrer.
![ss18-3](https://www.freecodecamp.org/news/content/images/2022/08/ss18-3.png)

**Étape 2** : Sélectionnez "Utiliser un périphérique".
![1-use-a-device-1](https://www.freecodecamp.org/news/content/images/2022/08/1-use-a-device-1.jpg)

**Étape 3** : Sur l'écran suivant, vous devriez voir plusieurs périphériques à partir desquels vous pouvez démarrer. 

Vous pouvez voir le lecteur bootable sous le nom de la marque de la clé USB. 
![disk-1](https://www.freecodecamp.org/news/content/images/2022/08/disk-1.jpg)

Il est possible de le voir comme "Ubuntu" aussi. Parfois, vous ne le verrez peut-être pas, donc vous devez cliquer sur "Voir plus de périphériques".

Si vous ne voyez toujours pas votre lecteur bootable, allez dans votre menu de démarrage en entrant dans le BIOS. Vous le verrez là.

**N.B.** : Vous devez être très prudent lorsque vous apportez des modifications dans le BIOS. Tout ce que vous faites là a un effet durable sur votre ordinateur. Si vous n'êtes pas sûr de ce que vous faites, vous devriez contacter un professionnel de l'informatique.

**Étape 4** : Choisissez "Installer Ubuntu". Vous pouvez aussi l'essayer avant de l'installer.
![3-select-install-ubuntu](https://www.freecodecamp.org/news/content/images/2022/08/3-select-install-ubuntu.jpg)

Suivez les autres invites de l'assistant d'installation et assurez-vous de ne pas remplacer votre installation de Windows 10 par Ubuntu. C'est pourquoi je vous ai suggéré de sauvegarder tous vos fichiers.

Lorsque vous arrivez à l'étape de sélection de la partition que vous avez créée, faites défiler jusqu'à [la partition que vous avez créée précédemment](#heading-comment-partitionner-votre-disque-dur-pour-ubuntu) et appuyez sur `ENTRÉE`.
![1-1-select-disk](https://www.freecodecamp.org/news/content/images/2022/08/1-1-select-disk.jpg)

Cliquez sur OK pour sélectionner tout l'espace dans la partition. 
![1-2-select-disk](https://www.freecodecamp.org/news/content/images/2022/08/1-2-select-disk.jpg)

Cette fois-ci, le bouton "Installer maintenant" ne sera plus grisé. 
![1-3-select-disk](https://www.freecodecamp.org/news/content/images/2022/08/1-3-select-disk.jpg)

Suivez les autres invites jusqu'à ce que Ubuntu commence à s'installer.

Après l'installation, Ubuntu vous invitera à retirer le lecteur bootable et à appuyer sur `ENTRÉE` pour redémarrer votre ordinateur.


## Maintenant vous pouvez faire un dual boot Ubuntu et Windows 10
Immédiatement après avoir redémarré l'ordinateur, vous devriez voir un écran qui ressemble à celui montré ci-dessous :
![Snapchat-2063128211](https://www.freecodecamp.org/news/content/images/2022/08/Snapchat-2063128211.jpg) 

Maintenant, vous pouvez choisir lequel démarrer entre Ubuntu et Windows 10. 

Pour démarrer Ubuntu, sélectionnez Ubuntu. Et pour démarrer Windows 10, sélectionnez Windows Boot Manager.

Vous pouvez également accéder à votre BIOS depuis le même endroit en choisissant UEFI Firmware Settings.
![Snapchat-778941832](https://www.freecodecamp.org/news/content/images/2022/08/Snapchat-778941832.jpg) 

## Conclusion
J'espère que cet article vous aide à faire un dual boot Ubuntu et Windows 10 sur votre ordinateur.

Le but ultime de cet article était de vous montrer comment faire un dual boot Ubuntu et Windows 10. 

Mais l'article est allé au-delà pour vous montrer comment :
- vérifier si le BIOS de votre PC est en mode UEFI 
- partitionner votre disque dur
- optimiser votre disque dur
- créer une clé USB bootable 
- installer la distribution Linux Ubuntu avec Windows sur votre PC Windows 10.

Si vous trouvez cet article utile, partagez-le avec vos amis et votre famille.
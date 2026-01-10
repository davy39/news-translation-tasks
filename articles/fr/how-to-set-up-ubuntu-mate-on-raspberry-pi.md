---
title: Comment installer Ubuntu MATE sur un Raspberry PI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-30T15:46:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-ubuntu-mate-on-raspberry-pi
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/1593285574373_plus-1.jpg
tags:
- name: Computers
  slug: computers
- name: Linux
  slug: linux
- name: Raspberry Pi
  slug: raspberry-pi
- name: technology
  slug: technology
- name: Ubuntu
  slug: ubuntu
seo_title: Comment installer Ubuntu MATE sur un Raspberry PI
seo_desc: "By Goran Aviani\nA few days ago a Raspberry Pi I use for CI on my personal\
  \ projects stopped working. The error was easily fixable, but since running anything\
  \ on that PI was slow from day one, I decided not to proceed in that direction.\
  \ \nAlso, because ..."
---

Par Goran Aviani

Il y a quelques jours, un Raspberry Pi que j'utilise pour l'intégration continue sur mes projets personnels a cessé de fonctionner. L'erreur était facilement réparable, mais comme tout ce qui tournait sur ce PI était lent depuis le premier jour, j'ai décidé de ne pas continuer dans cette direction. 

De plus, à cause du même problème, j'ai toujours voulu passer à un autre système d'exploitation – mais je n'ai jamais eu la motivation nécessaire puisque tout fonctionnait sur ce Raspberry PI, n'est-ce pas ? Eh bien, la motivation est venue avec cet article :)

**Note** : La configuration originale sur le Raspberry PI était assez simple : OS Raspibian, serveur VNC et Jenkins.

Pour ceux qui découvrent les Raspberry, voici un peu de contexte sur ce qu'ils sont et à quoi ils peuvent servir. 

Les Raspberry Pi sont essentiellement de petits ordinateurs utilisés le plus souvent pour apprendre les compétences en programmation, construire des projets matériels, faire de la domotique, et certains ont même trouvé une utilisation dans des applications industrielles. 

Il existe quelques types différents de PI sur le marché aujourd'hui. Pour en savoir plus sur eux, veuillez visiter leur page Wikipedia : [https://en.wikipedia.org/wiki/Raspberry_Pi#Generations](https://en.wikipedia.org/wiki/Raspberry_Pi#Generations)

Outils dont vous aurez besoin pour compléter ce tutoriel :

* Raspberry PI
* Carte Micro SD
* Adaptateur de carte Micro SD pour votre ordinateur portable
* Windows
* Souris pour Raspberry PI
* Câble HDMI pour connecter votre Raspberry PI à un téléviseur ou tout autre type d'écran
* Un clavier pour Raspberry PI est bon à avoir mais pas nécessaire car Ubuntu MATE offre un clavier à l'écran

Une fois que nous aurons terminé toutes les étapes, cet article vous montrera comment :

* Installer Ubuntu MATE sur une carte SD en utilisant Windows
* Installer Ubuntu MATE sur Raspberry PI
* Choses à faire après l'installation d'Ubuntu MATE

Il existe plusieurs options de système d'exploitation pour Raspberry PI, et Ubuntu Mate n'est qu'une option. Pour plus d'informations sur les autres options, vous pouvez consulter cet article : 

%[https://www.ubuntupit.com/best-raspberry-pi-os-available/]

## Flasher Ubuntu MATE sur une carte Micro SD

Les cartes SD et les clés USB sont appelées des lecteurs flash car elles ont une mémoire de type flash. Ainsi, flasher signifie créer un lecteur amorçable avec un système d'exploitation (OS) spécifique dessus. 

Rendez-vous sur la page de téléchargement d'Ubuntu MATE et téléchargez l'image d'architecture recommandée pour Raspberry PI :

%[https://ubuntu-mate.org/]



![Image](https://lh6.googleusercontent.com/HJ1b4UY1H8tqnWldXMWh1inaYVTuMQEvFyY6ia-MvNw-pKmx0B42YQ96i2x4UmB3gBfAmtkrOeeoAHr4H4DNU_I025ionZRQY0ZKXDaDLrBBWCP3R_vZrzUR3SC2f0O7-TNYLzne)
_Téléchargez la version 32 bits pour Raspberry PI (recommandée)_

### Configuration de la carte SD

Après avoir téléchargé l'image d'Ubuntu MATE, nous devons l'écrire sur la carte SD. Pour cela, nous utiliserons l'outil Balena Etcher. Etcher est un outil que nous téléchargeons ici :

%[https://www.balena.io/etcher/]



![Image](https://lh6.googleusercontent.com/1vYIoox0YKBcjUKbaZeGySgpiBgGl5VvcibE_vHRG15r1lq8geFO44TBdszTA-qRU2eUYqX2rkUoTiregfWz78BZ5IjQKIOwMAfoZc5ltVtgsVNxwrJ0EswWNXrM-DNOLVdDwsfC)
_Page de téléchargement de Balena Etcher_

Installez Etcher et lancez-le. Ensuite, sélectionnez le fichier image Ubuntu MATE que vous avez précédemment téléchargé, ainsi que votre carte SD, et commencez le processus de flashage.

**Note** : Le flashage d'Ubuntu MATE sur la carte SD prend un certain temps, alors n'hésitez pas à vous prendre une tasse de café.

![Image](https://lh3.googleusercontent.com/BAvIy-shTq645HjARX0MI0DqE5eZvfNqd2A8srKGtB8sVsDfxPOfhz-v6B7qSUl6JddF7O8dP7C9U_hJmgmhrGB02gZ2Ub0tgsOJfQOaocBdoHgUDQ1tYODhSARSLd2STl_G43Id)
_Balena Etcher décompresse l'image Ubuntu MATE_

![Image](https://lh4.googleusercontent.com/iL3a8osNs-fgqcoqbiWljsfpQItxMB2lsY6ibHOAValUdYoNetN0DoqwV4K2a0enatDXAvulVmuuOckdtcQn3QcyXr-OfZRBgg02_2jSG2Ms7bTzYL5LGVXu5irD6-cL6T03NLo7)
_Balena Etcher valide l'image Ubuntu MATE_

Une fois le flashage terminé, retirez la carte SD de l'adaptateur et insérez-la dans le Raspberry PI. C'est également l'étape où vous devrez connecter le PI avec la souris et un écran.

## Installation d'Ubuntu MATE sur Raspberry PI

Une fois que vous avez terminé de connecter tous les périphériques du Raspberry PI, connectez-le à la source d'alimentation et laissez-le démarrer.

Le processus d'installation d'Ubuntu MATE est exactement le même que pour Ubuntu ordinaire. Au cours de ce processus, vous serez invité à sélectionner la disposition de votre clavier, le fuseau horaire, le nom d'utilisateur et le mot de passe. Voici le guide d'installation étape par étape pour Ubuntu 18.04 : [Installation d'Ubuntu](https://phoenixnap.com/kb/how-to-install-ubuntu-18-04-bionic-beaver). 

Une fois l'installation terminée, vous serez accueilli par l'écran du bureau.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/ubuntu-mate-home.png)
_Écran d'accueil du bureau Ubuntu Mate_

## Choses à faire après l'installation d'Ubuntu MATE

### Mettre à jour la base de données locale

Cette commande met à jour/carte la base de données locale de vos packages locaux avec les mises à jour, permettant ainsi à votre système de récupérer de nouvelles versions des packages.

sudo apt update

### Mise à niveau des packages installés

Cette commande récupère de nouvelles versions des packages existants sur la machine que vous avez précédemment mappée avec la commande _sudo apt update_.

sudo apt upgrade

Note : La mise à jour d'Ubuntu MATE prend beaucoup de temps, alors n'hésitez pas à vous prendre une autre tasse de café, et une pâtisserie pour l'accompagner. Si vous n'avez pas de pâtisserie sous la main, n'hésitez pas à aller à la boulangerie la plus proche, car le temps que vous reveniez, votre système sera probablement mis à niveau à 50 %.

### Installation de l'application Ubuntu Software

Software Boutique est le centre logiciel par défaut sur Ubuntu MATE. Cependant, il a une sélection très limitée d'applications, et l'une des applications les plus intéressantes nécessaires pour mon projet est manquante. 

Heureusement, puisque c'est une distribution Ubuntu, il existe un moyen d'installer le centre logiciel standard d'Ubuntu qui offre plus de choix d'applications. 
  
Apparemment, il existe un moyen d'installer le centre logiciel Ubuntu via Software Bundle. Mais lorsque j'ai sélectionné l'option pour le faire, j'ai été bloqué et rien ne semblait se passer pour moi, alors j'ai simplement utilisé la commande terminal :

sudo apt install ubuntu-software

Bra gjort ! Vous venez de terminer l'installation du système d'exploitation Ubuntu Mate sur votre appareil Raspberry PI !

Consultez d'autres articles comme celui-ci sur mon [profil freeCodeCamp](https://www.freecodecamp.org/news/author/goran/), mon [profil Medium](https://medium.com/@goranaviani), et d'autres choses amusantes que je construis sur ma [page GitHub](https://github.com/GoranAviani).
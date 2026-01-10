---
title: Comment construire le système de domotique le plus robuste et sécurisé
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-29T11:55:28.000Z'
originalURL: https://freecodecamp.org/news/the-most-robust-and-secure-home-automation-system-6d0ddbb39f29
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ekrneFlaBAAqotbwcJ0pDA.png
tags:
- name: Internet of Things
  slug: internet-of-things
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Raspberry Pi
  slug: raspberry-pi
- name: technology
  slug: technology
seo_title: Comment construire le système de domotique le plus robuste et sécurisé
seo_desc: 'By Amir Off

  In this article, I’ll discuss how I built a Smart Home Automation System with Angular
  and Node.js on a Raspberry Pi without relying on any external cloud services.

  Intro

  Over the last few days, I spent some nights designing and developing...'
---

Par Amir Off

_Dans cet article, je vais expliquer comment j'ai construit un système de domotique intelligent avec Angular et Node.js sur un Raspberry Pi sans dépendre de services cloud externes._

### Introduction

Au cours des derniers jours, j'ai passé quelques nuits à concevoir et développer un système de domotique basé sur JavaScript, en utilisant Angular et Node.js. Et, comme pour tout autre projet, la planification a impliqué quelques recherches approfondies sur Internet.

Il s'avère qu'il y a beaucoup de poissons dans la mer — beaucoup de solutions sur la façon de mettre en œuvre un système de domotique. Certains offrent des services payants dans "le cloud" et d'autres expliquent comment construire le vôtre en utilisant une technologie appelée MQTT.

Aucune des solutions n'avait de sens pour moi. Toutes les options étaient soit coûteuses, soit avaient des implémentations peu pratiques, voire des failles de sécurité.

Mais, avant d'aller plus loin, expliquons ce qu'est MQTT. MQTT signifie **MQ Telemetry Transport**. C'est un protocole de messagerie publish/subscribe, extrêmement simple et léger. MQTT est conçu pour les appareils contraints et les réseaux à faible bande passante, à haute latence ou peu fiables.

Les principes de conception sont de minimiser la bande passante du réseau et les exigences de ressources des appareils tout en tentant d'assurer la fiabilité et un certain degré de garantie de livraison. Ces principes font également du protocole un choix [idéal](http://mqtt.org) pour le monde émergent de la "machine-to-machine" (M2M) ou de l'"Internet des objets" des appareils connectés, et pour les applications mobiles où la bande passante et la puissance de la batterie sont limitées.

![Image](https://cdn-media-1.freecodecamp.org/images/mNpCeEZHwF1UuwYj01abd-sbVPrKW-4yy8-t)
_Architecture Publish/Subscribe de MQTT (Source de l'image : [HiveMQ.com](www.hivemq.com))_

Pourquoi n'étais-je pas convaincu d'utiliser MQTT, ou par l'une des solutions que j'ai trouvées sur Internet ? Deux raisons :

1. Bien que la technologie MQTT semble très pratique pour les appareils IoT, je pensais toujours qu'elle était inutile. Le système que je vais montrer dans le tutoriel suivant fonctionne dans le même environnement où vivent les appareils IoT. Tous les avantages que MQTT offre en étant "rapide" et ayant une "faible bande passante" deviennent irrélevants. De plus, il y a tout le tracas impliqué dans sa mise en œuvre et tout le surcoût supplémentaire avec les packages npm requis pour qu'il fonctionne dans un environnement JavaScript. Au lieu de cela, j'utiliserai uniquement des bibliothèques JavaScript et Node.js génériques, rien de plus !
2. Qu'en est-il de la partie sécurité ? Eh bien, je ne suis pas un grand fan du "cloud" ou du cloud computing en général. Dans certains cas, cela peut être très bénéfique, mais dans la plupart des cas, c'est juste inutile. Réfléchissez-y : pourquoi auriez-vous un service nécessaire pour contrôler vos appareils domestiques hébergé ailleurs dans "le cloud" et non dans votre propre réseau ?

![Image](https://cdn-media-1.freecodecamp.org/images/6PYFXtvRMHaKIfhgJC68Ux7p5uJMqe5K1wE4)
_Bande dessinée par [Geek and Poke](http://geekandpoke.typepad.com/geekandpoke/2009/11/good-consultants.html" rel="noopener" target="_blank" title=")_

On pourrait penser que "le cloud" offre la possibilité d'accéder à vos appareils domestiques de n'importe où dans le monde via Internet.

Mais réfléchissez à ceci : lorsque votre réseau domestique n'a pas de connexion Internet, "le cloud" devient redondant. Plus important encore, vous pouvez toujours rendre votre système de domotique accessible depuis Internet en utilisant le port-forwarding, même s'il est hébergé sur votre réseau local.

C'est à ce moment-là que cela a "cliqué" pour moi, et j'ai pensé à héberger tout le système sur un Raspberry Pi et à le garder dans mon réseau local.

![Image](https://cdn-media-1.freecodecamp.org/images/IkTlTjziky8EUtdFX8G4BCVGwMa9aijqLZh7)
_Un Raspberry Pi 3 Model B_

### La technologie

1. **Logiciel** : La raison pour laquelle j'ai choisi Angular et Node.js est qu'ils sont basés sur JavaScript et que je suis déjà familier avec ce langage. Après tout, je voulais concevoir et développer une application web progressive qui communique avec mes appareils IoT via HTTP — et JavaScript offrait toutes les fonctionnalités dont j'avais besoin.
2. **Matériel** : Le système fonctionne avec des microcontrôleurs comme l'Arduino Uno/Mega/Du/MKR1000, Adafruit HUZZAH CC3000, et tout autre microcontrôleur avec une connexion WiFi. J'utilise l'[**ESP8266**](https://medium.com/p/deb7bd1841c1?source=user_profile---------3------------------) comme composant de base pour mon système de domotique. C'est une micropuce WiFi à faible coût avec des capacités de microcontrôleur. Elle a tout ce dont j'ai besoin et à un prix abordable ! Enfin, nous devons héberger le système quelque part sur notre réseau local — alors quoi de mieux que le Raspberry Pi ?

Ce ne sera pas un tutoriel de codage où je plonge profondément dans le codage, puisque ce projet est open-source et je vais tout publier sur GitHub. Je vais seulement démontrer comment implémenter votre propre système de domotique et passer par chaque étape. Si vous êtes un développeur, veuillez [**forker**](https://github.com/ameer157/smarthaus) le dépôt et vous impliquer dans son amélioration.

### L'installation

J'estime qu'il faudra environ 40 minutes pour terminer toute cette installation plus le temps passé en ligne à rechercher des solutions pour les erreurs d'installation.

#### **Ce dont vous avez besoin ?**

Un Raspberry Pi est requis. Dans mon exemple, j'utilise un Raspberry Pi 3, mais cela devrait fonctionner avec la plupart des versions. Les composants nécessaires sont :

1. Carte Raspberry Pi
2. Carte MicroSD (Une classe 10 avec 16 Go ou plus est recommandée)
3. Un lecteur de carte USB MicroSD ou un adaptateur de carte SD
4. Moniteur HDMI et un clavier USB (nécessaires temporairement pour le premier démarrage du Raspberry Pi)
5. Câble Ethernet (non nécessaire pour le Raspberry Pi 3 car il dispose d'un WiFi intégré)

#### Installation du système d'exploitation Raspbian sur le Raspberry Pi

Raspbian est un système d'exploitation gratuit basé sur Debian Linux, et il est optimisé pour Raspberry Pi.

**Je recommande** la version "LITE" sans tête. Elle n'a pas d'environnement de bureau ni d'interface graphique, et elle est accessible à distance depuis un ordinateur ou un appareil sur le même réseau via SSH. Nous gardons les choses simples puisque c'est la seule façon dont nous allons accéder au Raspberry Pi. La version LITE a toutes les fonctionnalités que nous recherchons.

1. Téléchargez [**la dernière**](https://www.raspberrypi.org/downloads/raspbian/) image de Raspbian depuis le site officiel de Raspberry Pi.
2. Flashez l'image du système d'exploitation Raspbian sur la carte SD avec [**Etcher**](https://etcher.io/) ou tout autre logiciel de gravure d'image de système d'exploitation de votre choix.

#### Configuration du Raspberry Pi

Pour préparer le Raspberry Pi au démarrage, nous devons :

1. Insérer la carte MicroSD dans le Raspberry Pi
2. Connecter le clavier USB et le câble HDMI
3. Connecter le câble Ethernet ou, si vous avez un Raspberry Pi 3 et souhaitez utiliser le WiFi, vous devez configurer le réseau dans la section suivante

Lorsque le Raspberry Pi a terminé le démarrage, connectez-vous en utilisant le nom d'utilisateur `pi` et le mot de passe `raspberry`

#### Activation du WiFi et connexion au réseau

**Sautez cette étape** si vous avez choisi de vous connecter avec un câble Ethernet.

1. Ouvrez le fichier de configuration "wpa-supplicant"

```
$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

2. Ajoutez ce qui suit à la fin du fichier en ajoutant le nom et le mot de passe de votre WiFi :

```
network={
```

```
   ssid="votre_nom_de_réseau"   psk="votre_mot_de_passe_réseau"
```

```
}
```

**3.** Appuyez sur `Ctrl+X` pour enregistrer le code. Confirmez avec `Y` puis `Enter`

**4.** Redémarrez le Raspberry Pi avec la commande suivante :

```
$ sudo reboot
```

#### **Activation de SSH et changement du nom d'utilisateur et du mot de passe**

Maintenant que le Raspberry Pi est connecté à Internet, il est recommandé de changer le mot de passe par défaut.

1. Ouvrez l'outil de configuration du Raspberry Pi et cliquez sur la deuxième option "Change User Password" et suivez les instructions

```
$ sudo raspi-config
```

![Image](https://cdn-media-1.freecodecamp.org/images/dtaG9lRXQkYqmnIqANMtcZOb0IoxB9sfhDmz)

**2.** Sélectionnez l'option 5 "Interfacing Options" puis activez SSH

**3.** Redémarrez le Raspberry Pi. Lorsqu'il est démarré, vous avez SSH activé et il est prêt à être accessible à distance depuis votre ordinateur de bureau

```
$ sudo reboot
```

#### Configuration de l'accès à distance au Raspberry Pi

Maintenant, enfin, la partie où nous installons le logiciel requis sur le Raspberry Pi. Cette partie peut être exécutée directement sur le Pi via le terminal en utilisant un moniteur HDMI et un clavier USB. Pour plus de commodité — et puisque nous avons activé la connexion SSH à distance — nous allons nous connecter depuis un autre environnement de bureau. C'est la meilleure et la plus facile façon d'accéder et de contrôler le Pi à distance chaque fois que des changements et des configurations sont nécessaires.

Donc, en gros, voici comment vous pouvez accéder à l'interface de ligne de commande d'un Raspberry Pi à distance depuis un autre ordinateur ou tout appareil sur le même réseau en utilisant SSH. Cela peut être fait de deux manières :

1. En utilisant l'invite de commande ou PowerShell (j'utilise Windows sur un ordinateur de bureau), remplacez par votre nom d'utilisateur et votre adresse IP

```
$ ssh username@ipaddress
```

Si vous **ne connaissez pas** l'adresse IP, tapez "`hostname -I`" dans la ligne de commande du Raspberry Pi.

![Image](https://cdn-media-1.freecodecamp.org/images/p9TrkcLo-EaANTz2-5xivbif9p3RXm5wIGYA)

**2.** La deuxième méthode consiste à utiliser un programme client comme [**PuTTY**](https://www.putty.org/) ou tout autre logiciel client SSH fonctionnel [**autre**](https://www.google.co.il/search?q=ssh+client). Voici un guide facile [**guide**](https://www.raspberrypi.org/documentation/remote-access/ssh/windows.md) pour utiliser PuTTY.

#### Installation du logiciel requis sur le Raspberry Pi

Avant d'installer quoi que ce soit, il est recommandé de mettre à jour le système d'exploitation et les packages du Raspberry Pi. Faire cela régulièrement le gardera à jour.

1. Mettez à jour la liste des packages du système en utilisant la commande suivante :

```
$ sudo apt-get update
```

**2.** Mettez à niveau tous vos packages installés à leur dernière version :

```
$ sudo apt-get dist-upgrade
```

**3.** Téléchargez et installez la dernière version de Node.js :

```
// Pour télécharger$ curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
```

```
// Pour installer$ sudo apt-get install -y nodejs
```

```
// Vérifiez si l'installation a réussi :$ node -v
```

**4.** Installez l'Angular CLI globalement :

```
$ npm install -g @angular/cli
```

**5.** Installez le système de contrôle de version Git :

```
$ sudo apt-get install git
```

#### Installation de la base de données (MongoDB)

Nous avons besoin d'une base de données pour stocker les utilisateurs enregistrés et leurs identifiants. Voici les étapes requises :

1. Installez MongoDB

```
$ sudo apt-get install mongodb
```

2. Démarrez le processus MongoDB

```
$ sudo service mongodb start
```

3. Démarrez le shell mongo

```
$ mongo
```

3. Créez une base de données appelée "smarthaus"

```
$ use smarthaus
```

Dans MongoDB, la base de données par défaut est test. Si vous n'avez pas créé de base de données, alors les collections seront stockées dans la base de données test.

#### Installation de Smart Haus

**1.** Vérifiez le répertoire de travail actuel avec cette commande :

```
$ pwd
```

```
/* Il imprimera probablement "/home/pi" où "pi" est le répertoire utilisateur actuel */
```

**Il est recommandé** de cloner le dépôt du projet sous le répertoire utilisateur pi mais vous pouvez naviguer ailleurs si vous êtes sûr.

**2.** Clonez le dépôt depuis :

```
$ git clone https://github.com/ameer157/smarthaus.git
```

Assurez-vous de naviguer à l'intérieur du répertoire en utilisant :

```
$ cd smarthaus
```

Avant d'installer des packages npm en utilisant "npm install", veuillez vous référer au [**guide npm pour corriger les permissions**](https://docs.npmjs.com/getting-started/fixing-npm-permissions#option-two-change-npms-default-directory) pour apprendre comment corriger les erreurs "**EACCESS**" que vous pourriez rencontrer pendant l'installation. Cela est **très important** car cela empêchera toute erreur de permission npm et vous permettra d'installer des packages globalement sans utiliser sudo. L'utilisation de sudo avec npm n'est pas recommandée et [**doit être évitée**](https://medium.com/@ExplosionPills/dont-use-sudo-with-npm-still-66e609f5f92).

**3.** Installez tous les packages requis pour le projet :

```
$ npm install
```

![Image](https://cdn-media-1.freecodecamp.org/images/iCw2rJLK34PWv0B-UGGeoWcwO8i10-mgY2FI)

#### Démarrage du serveur Node.js

Avant de démarrer le serveur, nous devons construire le projet en utilisant l'outil Angular CLI. Enfin, nous configurons le Raspberry Pi pour qu'il exécute le serveur à chaque démarrage.

1. Construisez le projet en utilisant :

```
$ ng build --prod
```

**2.** Modifiez le fichier `rc.local` en utilisant `nano` :

```
$ sudo nano /etc/rc.local
```

**3.** Ajoutez ce qui suit sur la ligne avant `exit 0` puis quittez et enregistrez le fichier :

```
su pi -c 'cd /home/pi/smarthaus/backend && sudo node server.js > log.txt &'
```

![Image](https://cdn-media-1.freecodecamp.org/images/jHBDN5kBPqJ6oiWY269MJ1o0dAe7TlEPrL7X)

Le serveur Node.js est maintenant prêt ! Il s'exécutera à chaque démarrage du système et enregistrera les logs dans le même répertoire dans un fichier "log.txt".

Lançons-le maintenant et voyons si cela fonctionne en utilisant cette commande :

```
$ sudo node server
```

Le système est maintenant accessible depuis n'importe quel appareil sur votre réseau via l'adresse IP du Raspberry Pi.

Veuillez aller de l'avant et [**forker**](https://github.com/ameer157/smarthaus) ce projet et vous impliquer dans le développement des parties manquantes ?

### La fin

Nous avons un système de domotique fonctionnel qui s'exécute en toute sécurité sur un Raspberry Pi dans notre réseau local sans utiliser "le cloud" ou le serveur de quelqu'un d'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/3JIKPjo9dQos9Ua-10JPxsJnQPVt4PvH1EJF)

![Image](https://cdn-media-1.freecodecamp.org/images/BdA31vbNfgwI0goItUDCZLdNlAv7XF5akvsu)
_Synchronisation en temps réel de l'état des appareils_

![Image](https://cdn-media-1.freecodecamp.org/images/TAQatUFW1P3nbEaFN5v3Lm495VfROtRNnkKo)

![Image](https://cdn-media-1.freecodecamp.org/images/tULxNb2WIueLALx-z-A5D6AMPMtw8h0hJ2Tw)
_Ajout d'un nouvel appareil synchronisant les données à la demande_

Mon Raspberry Pi posé à côté de ma [**Fingbox**](http://bit.ly/2OiO1Pm) et de mon routeur dans le salon ?

![Image](https://cdn-media-1.freecodecamp.org/images/UbJPvVTIOvQXwBXNclgpBCxqWVFnUqtbocMZ)
_Rick et Morty fournissant un support technique ??_

J'espère que vous avez apprécié la lecture, 
Veuillez [**suivre**](https://medium.com/@ameer157) et **partager** pour plus de contenu tech ??

![Image](https://cdn-media-1.freecodecamp.org/images/dc-iMjp94vVUVYzJKTYxFuVd8UYPENjRMPTH)
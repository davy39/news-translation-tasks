---
title: Comment créer une application React Native à l'ancienne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-30T12:42:38.000Z'
originalURL: https://freecodecamp.org/news/building-react-native-app-in-old-school-style-43f854a82a62
coverImage: https://cdn-media-1.freecodecamp.org/images/1*voZnfNFpIwpswufxZ6OKqg.png
tags:
- name: internet
  slug: internet
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
seo_title: Comment créer une application React Native à l'ancienne
seo_desc: 'By Panth Solanki

  As we all know, it’s high time to learn React Native. There are two ways to develop
  it as a doc. This section focuses on creating apps in Expo, directly on your Android
  device without any internet connection on your device.

  I know it...'
---

Par Panth Solanki

Comme nous le savons tous, il est grand temps d'apprendre React Native. Il existe deux façons de le développer en tant que document. Cette section se concentre sur la création d'applications dans Expo, directement sur votre appareil Android sans aucune connexion Internet sur votre appareil.

Je sais que c'est très facile en utilisant l'application Expo Client sur votre appareil avec Internet, mais que faire si vous avez un problème de connexion ? Vous ne voulez pas utiliser vos MB limités pour le développement. Alors, que faire si la connectivité WiFi de votre mobile a un problème de stabilité, ou si vous voulez simplement développer une application à l'ancienne... ou pour toute autre raison ?

Commençons, ce processus comprend juste trois petites étapes. Souvenez-vous, c'est juste pour le développement sur OS Windows et cible OS Android.

#### **Conditions préalables à l'installation**

Vous devez installer un pilote adb sur votre PC à partir d'[**ici**](http://adbdriver.com/downloads/). La procédure est également [**ici**](http://adbdriver.com/documentation/how-to-install-adb-driver-on-windows-8-10-x64.html).

Une fois le processus terminé, connectez votre mobile à votre PC. Ouvrez l'_Invite de commandes_ et exécutez la commande **adb devices**. Si un nom d'appareil apparaît sous _liste des appareils_, alors votre installation est terminée. Mais si aucun nom n'est affiché, vous devez installer correctement les pilotes adb.

Note : Votre mobile doit avoir le débogage USB activé dans les options pour les développeurs.

Installez l'application Expo Client depuis le Play Store [**ici**](https://play.google.com/store/apps/details?id=host.exp.exponent&hl=en_IN).

#### Installation du projet React Native

Suivez les étapes décrites dans la documentation [**ici**](https://facebook.github.io/react-native/docs/getting-started.html).

Je copie simplement les étapes ici. En supposant que vous avez _Node 10+_ installé, exécutez les commandes suivantes :

_npm install -g expo-cli_

_expo init AwesomeProject_

_cd AwesomeProject_

_npm start_

Les commandes ci-dessus ouvriront le navigateur avec [**_http://localhost:19002_**](http://localhost:19002) (si cela ne s'ouvre pas automatiquement, ouvrez-le manuellement).

Une fois que vous avez ouvert le localhost, il affichera un message comme **Tunnel Ready** comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/zYHDe2I9we1PUpcQ3LnBoAzpC3ThfLaSXrX9)
_Tunnel Ready signifie qu'il est temps de créer de la magie :)_

#### Étapes post-installation

Maintenant, il est temps de connecter votre appareil et d'ouvrir une autre invite de commandes pour exécuter les commandes suivantes :

**adb devices** // pour trouver le nom de l'appareil parmi vos appareils connectés

**adb -s <nom de l'appareil> reverse tcp:8081 tcp:8081** // cela n'affichera rien

Allez sur [**http://localhost:19002**](http://localhost:19002) dans le navigateur et cliquez sur **Run on Android device/emulator**.

![Image](https://cdn-media-1.freecodecamp.org/images/VD-QK3SNqyRSVLFLsb11kdTL9NSvhpo09yck)
_Cliquez sur Run on Android device/emulator pour voir la magie sur votre appareil_

Maintenant, vous verrez les bundles se charger sur votre appareil. Après avoir chargé tous les bundles, votre application sera en direct sur votre appareil et votre navigateur sera comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/zamalXDcwXipHylOzpd9S274xeVzgqp7F6cy)
_La barre latérale affichera votre appareil_

Vous pouvez déboguer votre application en cliquant sur le bouton en haut à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/NScWO4d1NZ0LB1y1HY3NxW4IWqcfPpJAEHlV)
_Cliquez sur le bouton en haut à droite et vous pouvez voir quelles données sont transmises à votre appareil._

Je serai heureux si ces informations vous sont utiles d'une manière ou d'une autre. Si vous avez des questions, n'hésitez pas à commenter — je serai plus qu'heureux de vous aider.

Merci d'avoir lu.
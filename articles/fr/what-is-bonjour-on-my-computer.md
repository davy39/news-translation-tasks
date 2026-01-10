---
title: Qu'est-ce que Bonjour sur mon ordinateur ? Guide PC du programme Bonjour Windows
  10
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-11-02T18:23:02.000Z'
originalURL: https://freecodecamp.org/news/what-is-bonjour-on-my-computer
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/bonjour.png
tags:
- name: configuration
  slug: configuration
- name: Linux
  slug: linux
- name: mac
  slug: mac
- name: Windows 10
  slug: windows-10
seo_title: Qu'est-ce que Bonjour sur mon ordinateur ? Guide PC du programme Bonjour
  Windows 10
seo_desc: 'Apple devices work well and connect readily with other Apple devices. But
  they have a hard time communicating with devices running other operating systems
  like Windows and Linux.

  If you have both Apple and Windows devices, you might want to share fil...'
---

Les appareils Apple fonctionnent bien et se connectent facilement avec d'autres appareils Apple. Mais ils ont du mal à communiquer avec des appareils utilisant d'autres systèmes d'exploitation comme Windows et Linux.

Si vous possédez à la fois des appareils Apple et Windows, vous pourriez vouloir partager des fichiers entre eux via un réseau local. Et c'est ce que le service Bonjour d'Apple permet en coulisses.

Dans ce guide, je vais vous expliquer ce qu'est Bonjour et comment vous pouvez le faire fonctionner sur votre ordinateur Windows 10.

## Qu'est-ce que le programme Bonjour d'Apple ?

Bonjour est l'implémentation par Apple du réseau zéro-configuration (zeroconf). Il permet aux appareils fonctionnant sous Windows et les systèmes d'exploitation Apple (comme macOS et iOS) de se connecter et de partager des ressources sans aucun paramètre de configuration.

Avec Bonjour, vous pouvez localiser d'autres appareils tels que des scanners et des imprimantes sur un réseau local et vous connecter à eux. Vous pouvez également partager des fichiers, quel que soit le système d'exploitation que vous utilisez, qu'il s'agisse de Windows, macOS ou Linux.

## Comment Bonjour fonctionne sur un ordinateur

Bonjour n'est pas un produit logiciel classique. Contrairement à d'autres logiciels et applications, vous n'utilisez pas Bonjour directement.

Au lieu de cela, Bonjour fonctionne en arrière-plan et connecte les appareils ensemble en utilisant un "schéma d'adressage de liaison", qui attribue automatiquement des adresses IP aux appareils sur un réseau local.

Des exemples d'applications qui utilisent Bonjour incluent iTunes, Skype, iChat et iPhoto.

## Comment installer et exécuter Bonjour sur Windows 10

Contrairement aux appareils Apple qui fonctionnent main dans la main avec Bonjour, vous devrez peut-être installer manuellement Bonjour sur votre ordinateur Windows 10.

Bonjour n'est pas disponible en téléchargement en tant qu'application autonome, vous devrez donc télécharger une application qui l'utilise.

Auparavant, il était inclus avec les applications Mac telles que iTunes et le navigateur Safari dans un dossier zip, mais de nos jours, l'application iTunes peut le télécharger pour vous via un réseau WiFi.

Cependant, vous pouvez installer Bonjour pour votre ordinateur Windows 10 en téléchargeant le Bonjour SDK (Software Development Kit) depuis le [site web des développeurs Apple](https://developer.apple.com/bonjour/).

Assurez-vous de sélectionner Bonjour SDK pour Windows comme montré ci-dessous :
![bonjour-sdk](https://www.freecodecamp.org/news/content/images/2021/11/bonjour-sdk.jpg)

Une fois cela fait, vous devrez vous connecter avec votre identifiant Apple. Si vous n'en avez pas, vous pouvez en créer un.

Lorsque vous vous connectez avec succès, vous verrez différentes versions de Bonjour SDK. Téléchargez celle que vous souhaitez et installez-la en ouvrant l'installateur et en suivant les instructions.
![versions](https://www.freecodecamp.org/news/content/images/2021/11/versions.png)

Lorsque le Bonjour SDK est installé, le programme Bonjour est installé avec lui.

## Avez-vous besoin de Bonjour sur votre ordinateur Windows 10 ?

Si vous utilisez une application qui dépend de Bonjour pour fonctionner sur un ordinateur Windows, vous avez définitivement besoin de Bonjour pour que l'application fonctionne efficacement.

De plus, si vous utilisez des appareils qui fonctionnent sous plusieurs systèmes d'exploitation tels que macOS, Windows et Linux, vous pourriez avoir besoin de les connecter ensemble pour partager des ressources telles que des fichiers et des appareils – et vous aurez besoin de Bonjour pour que cela se produise. Cela vous donnera également l'avantage de la configuration zéro.

Enfin, si vous n'utilisez pas d'appareil Apple comme un Mac mais que vous avez des amis qui en utilisent, vous devriez envisager d'installer Bonjour sur votre appareil, afin de pouvoir partager des fichiers et d'autres ressources avec eux.

## Comment arrêter ou désinstaller Bonjour sur Windows 10

Si vous arrêtez d'utiliser une application qui dépend de Bonjour pour fonctionner, ou si vous voulez vous en débarrasser pour une autre raison, vous pourriez vouloir arrêter Bonjour. Vous pouvez le faire depuis le Gestionnaire des tâches.

**Étape 1** : Cliquez sur Démarrer, ou appuyez sur la touche `WIN` (Windows) de votre clavier.

**Étape 2** : Recherchez "gestionnaire des tâches" et appuyez sur `ENTRÉE`.
![ss-1a](https://www.freecodecamp.org/news/content/images/2021/11/ss-1a.png)

**Étape 3** : Cliquez sur l'onglet Services. Ici, vous verrez le Service Bonjour, qui est parfois disponible sous le nom de `"mDNSResponder.exe"`.
![ss-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-1.jpg)

**Étape 4** : Faites un clic droit dessus et sélectionnez "Arrêter".
![ss-2](https://www.freecodecamp.org/news/content/images/2021/11/ss-2.jpg)

### Pour désinstaller Bonjour, vous pouvez le faire dans l'application Paramètres.

**Étape 1** : Cliquez sur Démarrer, ou appuyez sur la touche `WIN` (Windows) de votre clavier, et sélectionnez Paramètres pour ouvrir l'application Paramètres.
![ss-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-3.jpg)

**Étape 2** : Sélectionnez Applications.
![ss-4](https://www.freecodecamp.org/news/content/images/2021/11/ss-4.jpg)

**Étape 3** : Dans l'onglet Applications et fonctionnalités, faites défiler jusqu'à trouver Bonjour, ou recherchez-le.
![ss-5](https://www.freecodecamp.org/news/content/images/2021/11/ss-5.jpg)

**Étape 4** : Sélectionnez désinstaller, puis à nouveau, désinstaller.
![ss-6](https://www.freecodecamp.org/news/content/images/2021/11/ss-6.jpg)

Veuillez noter que pour vous débarrasser complètement du service Bonjour, vous devrez peut-être désinstaller l'application qui l'utilise également. Si vous avez installé Bonjour via le Bonjour SDK, assurez-vous de désinstaller également le Bonjour SDK.

## Conclusion

Bonjour est un service utile qui vous offre plus de flexibilité si vous travaillez avec des appareils utilisant plusieurs systèmes d'exploitation.

Ce guide vous a montré ce qu'est le service Bonjour, ce qu'il fait et comment vous pouvez en avoir plus de contrôle sur votre ordinateur Windows 10.

Merci d'avoir lu. Si vous trouvez cet article utile, veuillez le partager avec vos amis et votre famille.
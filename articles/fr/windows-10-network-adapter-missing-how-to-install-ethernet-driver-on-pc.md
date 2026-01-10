---
title: Adaptateur réseau Windows 10 manquant – Comment installer le pilote Ethernet
  sur PC
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-07T16:34:05.000Z'
originalURL: https://freecodecamp.org/news/windows-10-network-adapter-missing-how-to-install-ethernet-driver-on-pc
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/adapter-g446e52e4c_1280.jpg
tags:
- name: internet
  slug: internet
- name: Windows 10
  slug: windows-10
seo_title: Adaptateur réseau Windows 10 manquant – Comment installer le pilote Ethernet
  sur PC
seo_desc: 'On Windows 10 and other versions of the Windows operating system, you need
  a network adapter to connect to the internet through a wired or wireless network.

  Sometimes, you might get an error that your network adapter is missing. This can
  be very frus...'
---

Sur Windows 10 et d'autres versions du système d'exploitation Windows, vous avez besoin d'un adaptateur réseau pour vous connecter à Internet via un réseau filaire ou sans fil.

Parfois, vous pouvez obtenir une erreur indiquant que votre adaptateur réseau est manquant. Cela peut être très frustrant car vous ne pourrez pas vous connecter à Internet.

Il existe quelques solutions simples que vous pouvez utiliser pour résoudre ce problème, notamment :

- retirer et réinsérer la batterie de votre ordinateur
- désactiver les applications Antivirus et VPN
- redémarrer votre ordinateur

Mais cela pourrait ne pas suffire pour résoudre le problème.

Alors, dans cet article, je vais vous montrer 5 meilleures façons de corriger l'erreur d'adaptateur réseau manquant afin que vous puissiez recommencer à connecter votre ordinateur à Internet.

## Comment corriger l'adaptateur réseau manquant en utilisant l'outil de réinitialisation réseau intégré

Windows 10 dispose d'un outil de réinitialisation réseau intégré qui peut réinitialiser vos paramètres par défaut. Cela résout souvent ce problème pour vous.

Pour corriger l'erreur d'adaptateur réseau manquant avec cette solution, suivez les étapes détaillées ci-dessous :

**Étape 1** : Cliquez sur Démarrer et sélectionnez Paramètres.
![opensettings](https://www.freecodecamp.org/news/content/images/2022/01/opensettings.jpg)

**Étape 2** : Choisissez Réseau et Internet parmi les vignettes du menu.
![ss-1-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-1.jpg)

**Étape 3** : Sous « État », cliquez sur le lien Réinitialisation réseau.
![ss-2-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-1.jpg)

**Étape 4** : Cliquez sur le lien Réinitialiser maintenant.
![ss-3-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-1.jpg)

Si vous utilisez cette solution, sachez que vous devez réinstaller toute application VPN sur votre ordinateur et également ressaisir les mots de passe WiFi.

## Comment corriger l'adaptateur réseau manquant en vérifiant les paramètres de gestion de l'alimentation du pilote

Windows 10 est optimisé pour une meilleure gestion de l'alimentation, donc lorsque la batterie de votre ordinateur portable est faible, certains périphériques peuvent être éteints pour économiser de l'énergie. 

Vous pourriez rencontrer l'erreur d'adaptateur réseau manquant en raison de cette optimisation de l'alimentation.

Pour désactiver cette fonctionnalité pour votre pilote d'adaptateur réseau, suivez les étapes ci-dessous :

**Étape 1** : Cliquez avec le bouton droit sur Démarrer et sélectionnez Gestionnaire de périphériques.
![devicemanager-1](https://www.freecodecamp.org/news/content/images/2022/01/devicemanager-1.jpg)

**Étape 2** : Développez Adaptateurs réseau.
![ss-4-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-1.jpg)

**Étape 3** : Cliquez avec le bouton droit sur l'adaptateur réseau concerné et sélectionnez Propriétés.
![ss-5-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-1.jpg)

**Étape 4** : Passez à l'onglet Gestion de l'alimentation et décochez "Autoriser l'ordinateur à éteindre ce périphérique pour économiser l'énergie" et cliquez sur "OK". 
![ss-6-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-6-1.jpg)

## Comment corriger l'adaptateur réseau manquant en réinitialisant les paramètres Winsock dans la ligne de commande

Winsock est un programme qui détermine comment les services réseau sont utilisés sur un ordinateur Windows.

Si des problèmes surviennent avec Winsock, cela pourrait provoquer l'erreur d'adaptateur réseau manquant.

Pour réinitialiser Winsock, suivez les étapes ci-dessous : 

**Étape 1** : Cliquez sur Démarrer et recherchez "cmd", puis sélectionnez "Exécuter en tant qu'administrateur" à droite.
![cmd-admin](https://www.freecodecamp.org/news/content/images/2022/01/cmd-admin.jpg)

**Étape 2** : Dans la ligne de commande, tapez "netsh winsock reset" et appuyez sur `ENTRÉE`.
![ss-7](https://www.freecodecamp.org/news/content/images/2022/01/ss-7.png)

**Étape 3** : Redémarrez votre ordinateur.

## Comment corriger l'adaptateur réseau manquant en réinstallant ou en mettant à jour le pilote de l'adaptateur réseau

Si les solutions déjà discutées ne fonctionnent pas pour votre ordinateur, vous devriez essayer de réinstaller ou de mettre à jour le pilote de votre adaptateur réseau pour résoudre le problème.

Pour réinstaller le pilote de votre adaptateur réseau, vous devez suivre les étapes ci-dessous :

**Étape 1** : Cliquez sur Démarrer et sélectionnez Gestionnaire de périphériques.
![devicemanager-1](https://www.freecodecamp.org/news/content/images/2022/01/devicemanager-1.jpg)

**Étape 2** : Développez Adaptateurs réseau.
![ss-4-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-1.jpg)

**Étape 3** : Cliquez avec le bouton droit sur le pilote concerné et sélectionnez Désinstaller le périphérique.
![ss-8-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-8-1.jpg)

**Étape 4** : Choisissez Rechercher automatiquement un logiciel de pilote mis à jour. 
![ss-10-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-10-1.jpg)

**Étape 5** : Redémarrez votre ordinateur et le pilote sera automatiquement réinstallé pour vous.

## Conclusion

Dans ce guide détaillé, vous avez appris comment corriger l'erreur d'adaptateur réseau manquant afin de pouvoir vous connecter à Internet à nouveau avec votre ordinateur.

Si vous trouvez cet article utile, envisagez de le partager avec vos amis et votre famille afin qu'il puisse également les aider.

Merci d'avoir lu.
---
title: Ethernet n'a pas de configuration IP valide – Comment corriger une connexion
  invalide dans Windows 10
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-11-17T18:40:14.000Z'
originalURL: https://freecodecamp.org/news/ethernet-doesnt-have-a-valid-ip-configuration-how-to-fix-invalid-connection-in-windows-10
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/network-g101278015_1280.png
tags:
- name: internet
  slug: internet
- name: Windows 10
  slug: windows-10
seo_title: Ethernet n'a pas de configuration IP valide – Comment corriger une connexion
  invalide dans Windows 10
seo_desc: 'Every computer or device that you can use to surf the web has an IP address
  assigned to it. This IP address allows the device to be identified on the internet
  or within a local area network.

  But sometimes, you might get an error that says your Ethern...'
---

Chaque ordinateur ou appareil que vous pouvez utiliser pour surfer sur le web possède une adresse IP qui lui est assignée. Cette adresse IP permet à l'appareil d'être identifié sur internet ou au sein d'un réseau local.

Mais parfois, vous pouvez obtenir une erreur indiquant que votre Ethernet n'a pas de configuration IP valide.

Cette erreur est causée par divers problèmes avec la carte d'interface réseau (NIC) - le matériel qui connecte un ordinateur à un réseau. Elle peut également survenir en raison de pilotes défectueux et d'un routeur ou modem mal configuré.

Dans ce guide, je vais vous montrer quatre façons de corriger le problème de votre Ethernet n'ayant pas de configuration IP valide.

## Comment corriger les problèmes de configuration IP Ethernet en désactivant le démarrage rapide

Windows 10 est optimisé pour une récupération rapide depuis le mode veille, l'arrêt et l'hibernation. Si cette fonctionnalité n'est pas désactivée, elle pourrait affecter les performances de votre appareil car il pourrait ne pas être bien préparé à reprendre son fonctionnement.

Si vous désactivez cette fonctionnalité, cela pourrait corriger cette erreur pour vous.

**Suivez chaque étape ci-dessous pour désactiver le démarrage rapide dans Windows 10 :**

**Étape 1** : Lancez le Panneau de configuration en appuyant sur la touche `WIN` de votre clavier, tapez "panneau de configuration" (sans les guillemets) et appuyez sur `ENTRÉE` pour ouvrir le premier résultat de recherche.
![ss-1-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-1-1.png)

**Étape 2** : Dans le Panneau de configuration, changez le mode d'affichage en grandes icônes.
![ss-2-8](https://www.freecodecamp.org/news/content/images/2021/11/ss-2-8.jpg)

**Étape 3** : Sélectionnez "Options d'alimentation".
![ss-3-8](https://www.freecodecamp.org/news/content/images/2021/11/ss-3-8.jpg)

**Étape 4** : Cliquez sur "Choisir l'action des boutons d'alimentation".
![ss-4-9](https://www.freecodecamp.org/news/content/images/2021/11/ss-4-9.jpg)

**Étape 5** : Ouvrez le lien "Modifier les paramètres actuellement non disponibles".
![ss-5-7](https://www.freecodecamp.org/news/content/images/2021/11/ss-5-7.jpg)

**Étape 6** : Décochez "Activer le démarrage rapide (recommandé)" et cliquez sur Enregistrer les modifications.
![ss-6-8](https://www.freecodecamp.org/news/content/images/2021/11/ss-6-8.jpg)

## Comment corriger les problèmes de configuration IP Ethernet en mettant à jour votre pilote de carte réseau

Vous pouvez également corriger ce problème en mettant à jour ou en réinstallant votre pilote de carte réseau. Si votre pilote est défectueux, obsolète ou corrompu, il peut causer des problèmes.

**Étape 1** : Sur votre bureau, cliquez avec le bouton droit sur Démarrer (logo Windows) et cliquez sur "Gestionnaire de périphériques".
![ss-1-9](https://www.freecodecamp.org/news/content/images/2021/11/ss-1-9.jpg)

**Étape 2** : Développez Cartes réseau.

**Étape 3** : Cliquez avec le bouton droit sur la connexion Ethernet et sélectionnez "mettre à jour le pilote".
![ss-7-4](https://www.freecodecamp.org/news/content/images/2021/11/ss-7-4.jpg)

**Étape 4** : Sélectionnez "Rechercher automatiquement un pilote mis à jour".
![ss-8-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-8-3.jpg)

**Étape 5** : Redémarrez votre PC.

## Comment corriger les problèmes de configuration IP Ethernet en effaçant le cache réseau de votre ordinateur dans l'invite de commande

Effacer votre cache réseau peut supprimer les configurations IP invalides et les informations obsolètes. Mais vous ne pouvez pas faire cela simplement en effaçant les données de votre navigateur comme l'historique et le cache.

**Suivez les étapes ci-dessous pour effacer votre cache réseau :**

**Étape 1** : Appuyez sur la touche `WIN` de votre clavier et recherchez "cmd". Cette fois-ci, vous devez utiliser l'invite de commande en tant qu'administrateur, donc vous devez sélectionner "Exécuter en tant qu'administrateur" sur la droite.
![ss-9-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-9-3.jpg)

**Étape 2** : Entrez et exécutez les commandes suivantes une après l'autre :
- `ipconfig /release`
- `ipconfig /flushdns`
- `ipconfig /renew`
![ss-10](https://www.freecodecamp.org/news/content/images/2021/11/ss-10.png)

**Étape 3** : Redémarrez votre ordinateur.

## Comment corriger les problèmes de configuration IP Ethernet en réinitialisant le TCP et l'IP de votre ordinateur dans l'invite de commande

Le protocole de contrôle de transmission (TCP) est conçu pour transmettre des données d'un appareil à un autre, tandis que le protocole Internet (IP) agit comme l'identifiant d'un ordinateur sur internet.

Réinitialiser l'IP et le TCP de votre ordinateur peut parfois corriger l'erreur "Ethernet n'a pas de configuration IP valide" pour vous.

**Passez en revue les étapes ci-dessous pour réinitialiser votre IP et TCP dans l'invite de commande :**

**Étape 1** : Cliquez sur Démarrer et recherchez "invite de commande", puis sélectionnez "Exécuter en tant qu'administrateur" sur la droite.
![ss-9-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-9-3.jpg)

**Étape 2** : Tapez `netsh winsock reset` (sans les guillemets) et appuyez sur `ENTRÉE` pour réinitialiser votre TCP.

**Étape 3** : Tapez `netsh int IP reset` et appuyez sur `ENTRÉE` pour réinitialiser votre adresse IP.
![ss-11](https://www.freecodecamp.org/news/content/images/2021/11/ss-11.png)

**Étape 4** : Redémarrez votre PC.

## Conclusion

Dans cet article, vous avez appris comment corriger l'erreur "Ethernet n'a pas de configuration IP valide" de 4 manières différentes.

En plus de ces correctifs que nous avons discutés, je vous recommande également de redémarrer tous les appareils que vous utilisez pour accéder à internet. Cela inclut votre ordinateur, modem ou routeur.

Merci d'avoir lu et passez une bonne journée.
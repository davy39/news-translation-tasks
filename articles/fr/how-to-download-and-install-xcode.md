---
title: Comment télécharger Xcode et l'installer sur votre Mac – et le mettre à jour
  pour le développement iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-30T03:58:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-download-and-install-xcode
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b61740569d1a4ca2b7b.jpg
tags:
- name: mac
  slug: mac
- name: macOS
  slug: macos
seo_title: Comment télécharger Xcode et l'installer sur votre Mac – et le mettre à
  jour pour le développement iOS
seo_desc: 'By Ai-Lyn Tang

  Xcode is the tool developers use to build apps for the Apple ecosystem – MacOS,
  iOS, and all things Apple.

  This guide will walk you through how to successfully install Xcode onto your Mac,
  from start to finish.

  Here are some handy tips...'
---

Par Ai-Lyn Tang

Xcode est l'outil que les développeurs utilisent pour créer des applications pour l'écosystème Apple – MacOS, iOS et tout ce qui concerne Apple.

Ce guide vous expliquera comment installer Xcode sur votre Mac, de A à Z.

Voici quelques conseils utiles à connaître avant de commencer :

* Xcode ne fonctionne que sur un Mac. Si vous êtes sur un PC, vous ne pourrez malheureusement pas utiliser Xcode.
* Vous aurez besoin d'une bonne connexion Internet stable. La dernière version fait environ 8 gigaoctets.
* Assurez-vous d'avoir au moins 30 gigaoctets d'espace libre sur votre ordinateur. Le dernier fichier `.xip` (v11.4.1 au moment de la rédaction) fait ~8 gigaoctets compressé. Une fois décompressé, cela représente 17 gigaoctets supplémentaires. Ensuite, vous aurez besoin de l'outil en ligne de commande, qui représente encore 1,5 gigaoctet.

## Voici un aperçu des étapes pour installer Xcode

1. Télécharger Xcode
2. Installer l'outil en ligne de commande
3. Ouvrir la nouvelle version
4. Supprimer les fichiers

Notez que j'ai listé quelques commandes Terminal dans les étapes ci-dessous. Ces commandes peuvent être tapées dans votre répertoire de travail actuel. Cela signifie que vous n'avez pas besoin de naviguer vers un dossier particulier.

Si vous le souhaitez vraiment, vous pouvez d'abord taper `cd` avant de taper les commandes dans les étapes ci-dessous. Cela vous ramènera au dossier principal.

## Étape #1 : Télécharger Xcode

Il existe deux façons de procéder. Pour la dernière version et une installation théoriquement "facile", vous pouvez utiliser l'App Store. Je ne recommande pas cette option.

Je préfère utiliser le site des développeurs. Cela offre l'avantage de pouvoir télécharger n'importe quelle version que vous souhaitez.

### Option #1 : Télécharger via l'App Store pour la dernière version (non mon option préférée)

En théorie, cela devrait être un processus fluide et sans problème. Mais si l'installation échoue pour une raison quelconque à la dernière étape, il est très difficile de résoudre le problème.

Il existe plusieurs raisons possibles à un échec, et aucun moyen facile de savoir quelle est la cause sous-jacente. Si vous rencontrez un échec, vous devrez retélécharger l'intégralité du fichier à chaque fois que vous essayez de corriger le problème. Comme la dernière version fait 8 gigaoctets, je n'ai pas particulièrement apprécié cette approche.

Mais si vous vous sentez courageux, voici les étapes :

* Ouvrez l'App Store sur votre Mac
* Connectez-vous
* Recherchez Xcode
* Cliquez sur installer ou mettre à jour

### Option 2 : Télécharger via le site des développeurs pour une version spécifique (mon option préférée)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-258.png)
_Une capture d'écran de [https://developer.apple.com/download/more/](https://developer.apple.com/download/more/)_

1. Rendez-vous dans la section "plus" du [site web des développeurs Apple](https://developer.apple.com/download/more/)
2. Connectez-vous avec votre identifiant de compte iTunes
3. Tapez la version que vous souhaitez, et téléchargez le fichier `Xcode_x_x_x.xip`. Gardez à l'esprit que Xcode 11.4.1 fait 8 gigaoctets, donc cela prendra un certain temps en fonction de votre connexion Internet.
4. Une fois le fichier téléchargé, cliquez sur `.xip` pour l'extraire. Votre ordinateur l'extraira dans le même dossier où vous l'avez téléchargé. Ce processus d'extraction est automatique. Vous n'avez rien d'autre à faire après avoir cliqué sur le fichier `.xip`. Cette étape prendra quelques minutes.
5. [Facultatif] Une fois extrait, renommez l'application en « Xcode11.x.x » si vous utilisez plusieurs versions.
6. Glissez l'application dans le dossier Applications
7. [Facultatif] Définissez la nouvelle version de Xcode comme version par défaut. Ouvrez le Terminal et tapez `sudo xcode-select -switch /Applications/Xcodex.x.x.app`. Remplacez `x.x.x` par le numéro de version. Par exemple : `Xcode11.4.1.app`. Vous devrez entrer le mot de passe administrateur de votre ordinateur. Je suis presque sûr que cela mettra à jour la version par défaut de Xcode pour tous les utilisateurs de votre ordinateur, donc mieux vaut vérifier avec les autres utilisateurs d'abord.

## Étape #2 : Installer l'outil en ligne de commande (CLT)

Si vous avez plusieurs utilisateurs sur votre ordinateur, vous devrez mettre à jour le CLT pour chaque utilisateur.

**Télécharger `.dmg`**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-269.png)
_Une capture d'écran de [https://developer.apple.com/download/more/](https://developer.apple.com/download/more/)_

Pour mettre à jour le CLT, rendez-vous sur le [site web des développeurs d'applications](https://idmsa.apple.com/IDMSWebAuth/signin?appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&path=%2Fdownload%2Fmore%2F&rv=1) et téléchargez l'outil en ligne de commande `.dmg`.

Si vous n'avez jamais installé Xcode auparavant, vous pourrez peut-être le mettre à jour avec votre Terminal en tapant `xcode-select --install` au lieu de visiter le site web des développeurs.

Mais si vous avez une version existante de Xcode installée sur votre machine, vous verrez probablement cette erreur :

```
xcode-select: error: command line tools are already installed, use "Software Update" to install updates
```

Cela signifie que vous devrez vous rendre sur le site web des développeurs à la place.

### Installation du CLT

Lorsque le téléchargement du `.dmg` est terminé, double-cliquez sur le fichier pour l'ouvrir. Cela ouvrira une petite fenêtre qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-271.png)

Double-cliquez sur la boîte et suivez les invites pour installer le CLT. Cela prendra quelques minutes.

À la fin de l'installation, il peut vous demander si vous souhaitez déplacer ce fichier dans la corbeille. Lorsqu'il fait cela, il parle de déplacer le fichier `.dmg` dans la corbeille. Comme vous n'aurez plus besoin de ce fichier, je dis toujours oui.

## Étape #3 : Ouvrir Xcode

Ouvrez le dossier Applications et ouvrez la nouvelle version de Xcode. Si vous avez renommé Xcode, assurez-vous d'ouvrir l'application correcte.

Xcode peut vous demander d'installer des composants supplémentaires. Cliquez sur installer. Cela prendra quelques minutes.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-273.png)

Pendant l'installation, vérifiez que votre version par défaut de Xcode est celle que vous venez de télécharger :

* Ouvrez le Terminal
* Tapez `brew config`
* Vous devriez voir les versions "CLT" et "Xcode", ainsi que tout le reste. Cela devrait refléter la version que vous venez de télécharger. Dans mon cas, j'ai téléchargé Xcode 11.4.1.

```
CLT: 11.4.1.0.1.1586360307
Xcode: 11.4.1 => /Applications/Xcode11.4.1.app/Contents/Developer
```

Une fois les composants installés, Xcode sera lancé. Vous devriez pouvoir reprendre vos anciens projets et continuer là où vous vous étiez arrêté sans problème*.

_*Notez que si vous utilisez des outils proxy, tels que Charles, vous devrez réinstaller ces certificats dans votre simulateur._

Si vous rencontrez des erreurs en essayant de construire ou d'exécuter un projet, vérifiez quel appareil vous essayez de lancer. La nouvelle version peut ne pas se souvenir de l'appareil que vous utilisiez auparavant. Si c'est le cas, cliquez sur l'appareil et choisissez "Ajouter des simulateurs supplémentaires" dans le menu déroulant pour ajouter l'appareil que vous souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-275.png)

## Étape #4 : Supprimer les fichiers

Si vous n'avez pas besoin des anciennes versions de Xcode sur votre ordinateur, vous pouvez les désinstaller et récupérer de l'espace sur le disque dur.

Vous pouvez également supprimer le fichier `.xip` de la version que vous venez de télécharger, ainsi que le fichier `CLT.dmg`.

C'est tout. J'espère que cela vous a aidé à installer Xcode avec succès. Amusez-vous bien !
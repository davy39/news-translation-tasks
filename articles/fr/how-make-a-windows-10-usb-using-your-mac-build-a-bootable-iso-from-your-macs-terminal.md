---
title: Comment créer une clé USB Windows 10 à partir de votre Mac - Créer un ISO bootable
  depuis le Terminal de votre Mac
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2019-09-25T17:07:13.000Z'
originalURL: https://freecodecamp.org/news/how-make-a-windows-10-usb-using-your-mac-build-a-bootable-iso-from-your-macs-terminal
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca043740569d1a4ca4791.jpg
tags:
- name: mac
  slug: mac
- name: Windows 10
  slug: windows-10
seo_title: Comment créer une clé USB Windows 10 à partir de votre Mac - Créer un ISO
  bootable depuis le Terminal de votre Mac
seo_desc: 'Most new PCs don''t come with DVD drives anymore. So it can be a pain to
  install Windows on a new computer.

  Luckily, Microsoft makes a tool that you can use to install Windows from a USB storage
  drive (or "thumbdrive" as they are often called).

  But wh...'
---

La plupart des nouveaux PC ne sont plus équipés de lecteurs DVD. Il peut donc être fastidieux d'installer Windows sur un nouvel ordinateur.

Heureusement, Microsoft propose un outil que vous pouvez utiliser pour installer Windows à partir d'une clé USB (ou "clé USB" comme on les appelle souvent).

Mais que faire si vous n'avez pas de second PC pour préparer cette clé USB en premier lieu ?

Dans ce tutoriel, nous allons vous montrer comment faire cela à partir d'un Mac.

# Étape 1 : Télécharger le fichier ISO de Windows 10

Vous pouvez télécharger le fichier ISO directement depuis Microsoft. C'est exact - tout ce que nous allons faire ici est 100% légal et approuvé par Microsoft.

Vous pouvez télécharger Windows 10 directement depuis Microsoft gratuitement en utilisant [ce lien](https://www.microsoft.com/en-us/software-download/windows10). Si vous visitez le lien depuis un appareil Windows, vous serez redirigé vers l'[Outil de création de support Windows](https://www.microsoft.com/en-us/software-download/windows10%20) comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-106.png)

Si vous visitez le même lien depuis un appareil non-Windows, comme un Mac, un appareil Linux ou un smartphone, vous arriverez sur la page officielle de téléchargement de l'ISO :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-28-at-23-44-48-Download-Windows-10-Disc-Image--ISO-File--2.png)

Sélectionnez l'édition souhaitée dans le menu déroulant et cliquez sur _Confirmer_.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-28-at-23-44-48-Download-Windows-10-Disc-Image--ISO-File--1.png)

À ce moment-là, Windows 10 (ISO multi-éditions) était la seule option disponible. Une fois que vous avez confirmé votre édition, vous obtiendrez un autre menu déroulant qui vous permet de choisir une langue. Sélectionnez celle que vous souhaitez et cliquez sur le bouton _Confirmer_.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-28-at-23-47-47-Download-Windows-10-Disc-Image--ISO-File--1.png)

Une fois que vous avez confirmé votre langue, vous obtiendrez deux liens de téléchargement, l'un pour l'édition 64 bits et l'autre pour l'édition 32 bits. Les deux liens sont valides pendant 24 heures et la page indiquera également quand ils expireront.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-28-at-23-48-22-Download-Windows-10-Disc-Image--ISO-File--1.png)

Si vous ne savez pas comment choisir entre 64 bits et 32 bits, voici ce que vous devez faire. Si vous avez un processeur qui supporte l'architecture 64 bits et que vous avez plus de 4 Go de RAM, choisissez la version 64 bits. Les systèmes d'exploitation 32 bits ont une limite de 4 Go de RAM.

Pour savoir si votre processeur supporte l'architecture 64 bits ou non, rendez-vous sur un site comme [WikiChip](https://en.wikichip.org/wiki/WikiChip) et recherchez le modèle de votre processeur.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-107.png)

Comme vous pouvez le voir sur la capture d'écran ci-dessus, mon Ryzen 5 3600 supporte l'architecture 64 bits. J'ai également 16 Go de RAM, ce qui est bien plus que 4 Go, donc je vais opter pour l'édition 64 bits.

# Étape 2 : Insérez votre clé USB dans votre Mac

Le fichier ISO ne fait qu'environ 5 gigaoctets, mais je vous recommande d'utiliser une clé USB d'au moins 16 gigaoctets au cas où Windows aurait besoin de plus d'espace pendant le processus d'installation.

J'ai acheté une clé USB de 32 gigaoctets chez Walmart pour seulement 3 $, donc cela ne devrait pas être très cher.

Insérez votre clé USB dans votre Mac. Ensuite, ouvrez votre terminal. Vous pouvez le faire en utilisant la recherche Spotlight de MacOS en appuyant simultanément sur les touches ⌘ et la barre d'espace, puis en tapant "terminal" et en appuyant sur Entrée.

Ne soyez pas intimidé par l'interface de ligne de commande. Je vais vous dire exactement quelles commandes entrer.

# Étape 3 : Utilisez la commande diskutil pour identifier sur quel disque votre clé USB est montée

Ouvrez Spotlight Mac en utilisant le raccourci clavier ⌘ + espace. Ensuite, tapez le mot "terminal" et sélectionnez Terminal dans la liste déroulante.

Collez la commande suivante dans votre terminal et appuyez sur Entrée :

`diskutil list`

Vous verrez une sortie comme celle-ci (notez que votre terminal Mac peut afficher du texte noir sur fond blanc si vous ne l'avez pas personnalisé).

![Image](https://www.freecodecamp.org/news/content/images/2019/09/default_-_default_freeCodeCamp_-_-zsh_-_130-33.png)

Copiez le texte que je pointe ici. Il sera probablement quelque chose comme

`/dev/disk2`.

# Étape 4 : Formatez votre clé USB pour qu'elle fonctionne avec Windows

Formatez ensuite votre clé USB en format FAT32 de Windows. Il s'agit d'un format que Windows 10 reconnaîtra.

Notez que vous devez remplacer `disk2` par le nom de votre disque de l'étape 3 s'il n'était pas `disk2`. (Il peut s'agir de `disk3` ou `disk4`).

Exécutez cette commande en utilisant le numéro de disque correct pour votre USB :

`diskutil eraseDisk MS-DOS "WIN10" GPT /dev/disk2`

Vous verrez alors une sortie de terminal comme celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/default_-_default_freeCodeCamp_-_-zsh_-_130-33-1.png)

Cela ne prendra probablement que 20 secondes sur un ordinateur récent, mais peut prendre plus de temps sur un ordinateur plus ancien.

Notez que pour certains matériels, vous devrez peut-être exécuter cette commande, qui utilise le format MBR pour le partitionnement au lieu de GPT. Revenez et essayez cette commande si l'étape 7 échoue, puis refaites les étapes 5, 6 et 7 :

```
diskutil eraseDisk MS-DOS "WIN10" MBR /dev/disk2
```

# Étape 5 : Utilisez `hdiutil` pour monter le dossier Windows 10 et le préparer pour le transfert.

Maintenant, nous allons préparer notre fichier ISO téléchargé afin de pouvoir le copier sur notre clé USB.

Vous devrez vérifier où se trouve votre fichier ISO Windows 10 téléchargé et l'utiliser. Mais votre fichier se trouve probablement dans votre dossier `~/Downloads` avec un nom comme `Win10_1903_V1_English_x64.iso`.

`hdiutil mount ~/Downloads/Win10_1903_V1_English_x64.iso`

# Étape 6 : Copiez l'ISO Windows 10 sur votre clé USB

**Mise à jour d'avril 2020 :** L'un des fichiers de l'ISO Windows 10 - install.wim - est désormais trop volumineux pour être copié sur une clé USB formatée en FAT-32. Je vais donc vous montrer comment le copier séparément.

Merci à [@alexlubbock](https://twitter.com/alexlubbock) pour avoir trouvé cette solution de contournement.

Exécutez d'abord cette commande pour copier tout sauf ce fichier :

`rsync -vha --exclude=sources/install.wim /Volumes/CCCOMA_X64FRE_EN-US_DV9/* /Volumes/WIN10`

Ensuite, exécutez cette commande pour installer Homebrew (si vous ne l'avez pas encore installé sur votre Mac) :

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

Ensuite, utilisez Homebrew pour installer un outil appelé wimlib avec cette commande terminal :

`brew install wimlib`

Ensuite, créez le répertoire dans lequel vous allez écrire les fichiers :

`mkdir /Volumes/WIN10/sources`

Ensuite, exécutez cette commande. Notez que ce processus peut prendre plusieurs heures, vous pouvez voir 0 % de progression jusqu'à ce qu'il se termine. Ne l'interrompez pas. Il utilisera wimlib pour diviser le fichier install.wim en 2 fichiers de moins de 4 Go chacun (j'utilise 3,8 Go dans la commande suivante), puis les copiera sur votre clé USB :

`wimlib-imagex split /Volumes/CCCOMA_X64FRE_EN-US_DV9/sources/install.wim /Volumes/WIN10/sources/install.swm 3800`

Une fois cela fait, vous pouvez éjecter votre clé USB de votre Mac dans Finder. Notez que Windows réassemblera automatiquement ces fichiers plus tard lors de l'installation.

# Étape 7 : Insérez votre clé USB dans votre nouveau PC et commencez à charger Windows

Félicitations - votre ordinateur devrait maintenant démarrer directement depuis votre clé USB. Si ce n'est pas le cas, vous devrez peut-être vérifier le BIOS de votre nouveau PC et changer l'ordre de démarrage pour démarrer depuis votre clé USB.

Windows affichera un écran et lancera le processus d'installation.

Profitez de votre nouveau PC et de votre nouvelle copie de Windows fraîchement installée.
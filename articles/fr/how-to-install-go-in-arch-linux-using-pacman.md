---
title: Comment installer Go dans Arch Linux en utilisant Pacman
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-29T20:14:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-go-in-arch-linux-using-pacman
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e65740569d1a4ca3ce4.jpg
tags:
- name: ArchLinux
  slug: archlinux
- name: golang
  slug: golang
seo_title: Comment installer Go dans Arch Linux en utilisant Pacman
seo_desc: "Using the Arch Linux Package Manager (pacman) is the easiest way to install\
  \ Go. Based on the Arch Linux philosophy of providing new software versions very\
  \ fast, you will get a very current version of Go. \nBefore you can install the\
  \ Go package, you ha..."
---

Utiliser le gestionnaire de paquets d'Arch Linux (`pacman`) est le moyen le plus simple d'installer Go. Basé sur la philosophie d'Arch Linux de fournir des versions de logiciels très rapidement, vous obtiendrez une version très récente de Go. 

Avant de pouvoir installer le paquet Go, vous devez mettre à jour le système et tous vos paquets installés. Cependant, avant de mettre à jour votre système et ses paquets, n'oubliez pas de consulter d'abord la [page d'accueil d'Arch Linux](https://www.archlinux.org/). Toute étape inhabituelle que vous devez effectuer pour éviter que les paquets ne se cassent sera listée dans un article là-bas.

Une fois que vous avez confirmé qu'il est sûr de mettre à jour votre système, exécutez simplement la commande suivante :

```sh
$ sudo pacman -Syu
```

Rappelez-vous que le drapeau `-S` est utilisé pour installer un seul paquet ou une liste de paquets, l'option `y` rafraîchit la liste de tous les paquets Arch Linux, et l'option `u` met à jour tous les paquets qui sont obsolètes.

Après que votre système soit complètement à jour, installez Go avec la commande suivante :

```sh
$ sudo pacman -S go
```

### Vérifier l'installation et la version de Go

Pour vérifier si Go a été installé avec succès, exécutez :

```sh
$ go version
> go version go1.13.8 linux/amd64
```

Cela affichera la version installée de Go dans la console, tout en vérifiant que l'installation s'est déroulée sans problème.

## Plus d'informations sur Go :

[Apprendre Go dans ce cours vidéo gratuit](https://www.freecodecamp.org/news/go-golang-course/)

[Comment créer un flux photo avec Go et Vue.js](https://www.freecodecamp.org/news/how-to-build-a-photo-feed-with-go-and-vue-js-9d7f7f39c1b4/)

## Plus d'informations sur Arch Linux :

[Comment installer Arch Linux à partir de zéro](https://www.freecodecamp.org/news/installing-arch-linux-from-scratch-b595095ddd48/)

## Bonus : Comment installer Go sur Ubuntu / Linux Mint :

Utiliser le gestionnaire de paquets source d'Ubuntu (`apt`) est le moyen le plus simple d'installer Go. Alors que le `pacman` d'Arch Linux est à la pointe, les paquets installés avec `apt` et ses variantes sont souvent plusieurs versions en retard. 

L'avantage de cette approche est la stabilité – bien que vous ne puissiez pas installer la dernière version de n'importe quel paquet, vous pouvez être certain que votre système ne se cassera pas.

Tout d'abord, mettez à jour votre système avec les commandes suivantes :

```sh
$ sudo apt update
$ sudo apt upgrade
```

Ensuite, installez Go en exécutant :

```sh
$ sudo apt install golang-go
```

### Vérifier l'installation et la version de Go

Pour vérifier si Go a été installé avec succès, ouvrez votre terminal et exécutez :

```sh
$ go version
```

Cela affichera la version installée de Go dans la console.

## Bonus : Comment installer Go sur macOS :

### **Installer Go dans Mac OS X en utilisant l'installateur de paquets**

Depuis la [page de téléchargement de golang](https://golang.org/dl/), obtenez l'installateur de paquets Mac (se terminant par .pkg) et exécutez-le.

![capture d'écran de la page de téléchargement de golang au moment de l'écriture, mettant en évidence le lien](https://raw.githubusercontent.com/AlexandroPerez/resources/master/img/mac_package_installer.jpg)

### Vérifier l'installation et la version de Go

Pour vérifier si Go a été installé avec succès, ouvrez votre terminal et exécutez :

```sh
$ go version
```

Cela affichera la version installée de Go dans la console.

### Installer Go dans Mac OS X en utilisant l'archive tarball

Vous pouvez obtenir le lien vers l'archive tarball pour Mac OS depuis la section Dernière Version Stable de la [page de téléchargement de golang](https://golang.org/dl/).

![capture d'écran de la page de téléchargement de golang au moment de l'écriture, mettant en évidence le lien](https://raw.githubusercontent.com/AlexandroPerez/resources/master/img/mac_tarball.jpg)

### Processus d'installation

Dans ce processus d'installation, nous utiliserons la dernière version stable au moment de l'écriture (Go 1.9.1). Pour une version plus récente ou plus ancienne, remplacez simplement le lien dans la première étape. Consultez la [page de téléchargement de golang](https://golang.org/dl/) pour voir quelles versions sont actuellement disponibles.

##### **Installer Go 1.9.1**

```text
$ curl -O https://storage.googleapis.com/golang/go1.9.1.darwin-amd64.tar.gz
$ sudo tar -C /usr/local -xzf go1.9.1.darwin-amd64.tar.gz
$ export PATH=$PATH:/usr/local/go/bin
```

### Vérifier l'installation et la version de Go

Pour vérifier si Go a été installé avec succès, utilisez :

```sh
$ go version
```

Cela affichera la version installée de Go dans la console.
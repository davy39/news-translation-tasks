---
title: Comment installer Node sur un MacOS, Linux ou Windows en utilisant NVM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-22T21:42:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-node-in-your-machines-macos-linux-windows
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a1a740569d1a4ca238a.jpg
tags:
- name: install
  slug: install
- name: node
  slug: node
- name: node js
  slug: node-js
- name: npm
  slug: npm
- name: Tutorial
  slug: tutorial
seo_title: Comment installer Node sur un MacOS, Linux ou Windows en utilisant NVM
seo_desc: 'By Adeel Imran

  Before you can start making super awesome apps in NodeJS, you have to install it.
  Fortunately, installing NodeJS is super simple.

  In this tutorial we will cover how to install NodeJS/NPM in


  macOS/linux

  Windows


  Once you install NodeJS...'
---

Par Adeel Imran

Avant de pouvoir commencer à créer des applications super géniales en NodeJS, vous devez l'installer. Heureusement, l'installation de NodeJS est super simple.

Dans ce tutoriel, nous allons couvrir comment installer NodeJS/NPM sur

* macOS/Linux
* Windows

Une fois que vous avez installé NodeJS/NPM, vous pouvez facilement mettre à niveau ou rétrograder vers n'importe quelle version de Node avec une seule commande. La vidéo suivante montre comment télécharger NodeJS sur votre machine.

## Guide d'installation pour Mac OS & Linux

%[https://www.youtube.com/watch?v=TmT_CGFnUuM&feature=youtu.be]

Ouvrez un nouveau terminal. Tapez ce qui suit et appuyez sur entrée :

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```

Fermez votre terminal, puis ouvrez-en un nouveau et tapez ceci :

```
nvm ls
```

Vous verrez quelque chose comme ceci :

```
system
iojs -> N/A (default)
node -> stable (-> N/A) (default)
unstable -> N/A (default)
nvm_list_aliases:36: no matches found: /Users/adeelimran/.nvm/alias/lts/*
```

Ensuite, dans votre terminal, tapez :

```
nvm install 12.18.1
```

Une fois installé, il est prêt à être utilisé. Pour utiliser cette version, tapez simplement ceci dans votre terminal :

```
nvm use 12.18.1
```

Maintenant qu'il est installé, vérifions-le en faisant ce qui suit :

```
node --v
```

Et c'est tout — vous avez terminé. Amusez-vous bien.

Maintenant, si dans le futur, pour une raison quelconque, vous souhaitez désinstaller NVM (node version manager), ouvrez simplement votre terminal et tapez ce qui suit :

```
rm -rf $NVM_DIR ~/.npm ~/.bower
```

## Guide d'installation pour Windows

%[https://www.youtube.com/watch?v=QWdSDo9V1Ho]

###

Tout d'abord, allez dans la section des releases du dépôt `nvm-windows` [https://github.com/coreybutler/nvm-windows/releases](https://github.com/coreybutler/nvm-windows/releases). Sélectionnez la dernière version.

Ensuite, choisissez le fichier `nvm-setup.zip` et téléchargez-le.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/tempsnip.png)

Une fois le fichier téléchargé, décompressez-le et cliquez sur l'installateur, puis suivez les étapes. (J'utilise [7zip](https://www.7-zip.org/) pour l'extraction des fichiers .zip, car il est GRATUIT.)

Ensuite, pour vérifier si `nvm` est correctement installé, ouvrez un nouveau terminal d'invite de commande et tapez `nvm`. Une fois que vous avez vérifié qu'il est installé, vous pouvez passer à l'étape suivante.

Installez NodeJS en utilisant `nvm` comme ceci :

```
nvm install <version_number> // supposons que ce soit 12.18.1
```

La version peut être une version de NodeJS ou "latest" (pour la dernière version stable).

Pour utiliser la version spécifique de Node que vous venez d'installer, tapez simplement ce qui suit dans votre terminal :

```
nvm use 12.18.1;
```

Vérifiez la version de Node avec node -v. Cela devrait afficher v12.18.1 dans votre terminal.

Si vous souhaitez installer une autre version de Node, répétez les étapes avec une version différente.

Vous devriez maintenant avoir une version fonctionnelle de NodeJS en cours d'exécution sur votre machine. Bon codage les amis. :)

Faites-moi savoir si vous avez trouvé ce guide utile. Envoyez-moi un message sur [twitter](https://twitter.com/adeelibr) ([twitter.com/adeelibr](https://twitter.com/adeelibr)).
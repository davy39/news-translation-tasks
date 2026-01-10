---
title: Créer une application Node.js sur Android, Partie 1
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-21T00:24:17.000Z'
originalURL: https://freecodecamp.org/news/building-a-node-js-application-on-android-part-1-termux-vim-and-node-js-dfa90c28958f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vBw9_VPFiEcxgxDx-Oghzw.png
tags:
- name: Android
  slug: android
- name: Design
  slug: design
- name: Linux
  slug: linux
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
seo_title: Créer une application Node.js sur Android, Partie 1
seo_desc: 'By Aurélien Giraud

  If you are excited about Node.js and own an Android device, no doubt you’ll enjoy
  running Node.js on it. Thanks to Termux a terminal emulator and Linux environment
  for Android, the fun of developping Node.js web applications is jus...'
---

Par Aurélien Giraud

Si vous êtes passionné par Node.js et possédez un appareil Android, vous apprécierez sans doute exécuter Node.js dessus. Grâce à [Termux](https://termux.com/), un émulateur de terminal et un environnement Linux pour Android, le plaisir de développer des applications web Node.js n'est qu'à quelques 'npm install' !

### Ce que nous allons faire

Je vais montrer comment commencer avec Node.js en utilisant Termux sur Android. Nous allons également utiliser Express et voir comment stocker les données de notre application dans NeDB, une base de données JavaScript légère, dont l'API est un sous-ensemble de celle de MongoDB.

Dans ce premier article, nous allons nous limiter à la configuration de notre environnement de développement Node.js, c'est-à-dire :

1. **Installer et configurer Termux.**
2. **Installer et voir comment utiliser Vim comme éditeur de texte.** (Cette section peut être ignorée si vous connaissez déjà Vim.)
3. **Installer et exécuter Node.js.**

### 1. Termux

![Image](https://cdn-media-1.freecodecamp.org/images/1*wYX0neSQDAo5NSNdozrovw.jpeg)
_L'interface en ligne de commande de Termux_

Termux combine l'émulation de terminal avec une collection de paquets Linux. Il est disponible sous forme d'application gratuite qui peut être installée directement depuis le [Play Store](https://play.google.com/store/apps/details?id=com.termux) ou depuis le catalogue [F-Droid](https://f-droid.org/en/packages/com.termux/).

#### Configuration

Lorsque vous ouvrez Termux, vous êtes accueilli par une [interface en ligne de commande](https://en.wikipedia.org/wiki/Shell_%28computing%29) (CLI). Juste après l'installation de Termux, il est recommandé de vérifier les mises à jour et de les installer si nécessaire. Tapez donc les commandes suivantes à l'invite — c'est-à-dire après le signe '$' — et appuyez sur <Entrée> :

```bash
$ apt update && apt upgrade
```

Termux est livré avec un système de base minimal, vous devriez donc également installer 'coreutils' pour les variantes complètes des [utilitaires CLI de base tels que 'mv', 'ls', etc.](https://devdactic.com/10-basic-bash-commands/)

```bash
$ apt install coreutils
```

#### Stockage

Il existe trois principaux types de [stockage dans Termux](https://wiki.termux.com/wiki/Internal_and_external_storage) :

1. **Stockage privé de l'application** : C'est là où vous vous trouvez lorsque vous démarrez Termux.
2. **Stockage interne partagé** : Stockage dans l'appareil disponible pour toutes les applications.
3. **Stockage externe** : Stockage sur les cartes SD externes.

Bien que la configuration de l'environnement dans Termux soit similaire à celle d'une distribution Linux moderne, l'exécution sur Android implique des différences et jusqu'à présent, je n'ai réussi à exécuter Node.js complètement qu'en stockant mes données dans le stockage privé de Termux (option 1 ci-dessus).

Créons donc un répertoire pour notre application et changeons pour ce répertoire :

```bash
$ mkdir test-node && cd test-node
```

#### Clavier

J'ai jusqu'à présent utilisé uniquement un clavier logiciel et j'ai rencontré quelques problèmes avec le clavier tactile par défaut tout en utilisant [la touche de volume haut](https://termux.com/touch-keyboard.html) comme remplacement pour <Esc>, <Tab> ou les touches fléchées.

Pour contourner ces problèmes, j'ai installé [Hacker's Keyboard](https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard) depuis le Play Store et je l'apprécie vraiment. C'est un clavier tactile qui peut être utilisé à la place de celui par défaut et qui possède toutes les touches nécessaires pour écrire du code et utiliser le terminal.

Vous pouvez trouver des informations utiles sur l'utilisation d'un clavier tactile ou matériel avec Termux directement sur [la page d'aide](https://termux.com/help.html).

![Image](https://cdn-media-1.freecodecamp.org/images/1*4f2hjcG-q9zh_xn6dDOFNg.jpeg)
_Le clavier Hacker's Keyboard_

#### Utilisation de plusieurs sessions

Une autre chose que je voudrais mentionner à propos de Termux : si vous balayez l'écran de gauche à droite à partir de son bord gauche, cela ouvre un menu qui permet de démarrer ou de basculer entre plusieurs sessions Termux.

#### Accéder à l'aide dans Termux

Dans Termux, vous pouvez accéder à la documentation d'aide, qui contient toutes les informations nécessaires, en appuyant longuement sur l'écran, puis en cliquant d'abord sur 'More', puis sur 'Help'. Notez cependant que cette documentation d'aide ne peut pas être consultée lorsque votre appareil n'est pas connecté à Internet.

### 2. Vim

Vim est un éditeur de texte qui peut être utilisé directement dans l'interface en ligne de commande et il est disponible en tant que paquet dans Termux. Installons-le donc :

```bash
$ apt install vim
```

L'interface de Vim n'est pas basée sur des menus ou des icônes, mais sur des commandes données dans une interface utilisateur en mode texte. Au cas où vous seriez nouveau dans ce domaine, je vais vous guider à travers les bases de Vim.

Tout d'abord, créez le fichier 'server.js' :

```bash
$ touch server.js 
```

Pour éditer ce fichier avec Vim, tapez simplement :

```bash
$ vim server.js
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*iMAqPtrYe5nBk5PsBEEILQ.png)
_Vim affichant le contenu du fichier vide server.js_

#### Utilisation des différents modes

Vim se comporte différemment selon le mode dans lequel vous vous trouvez. Au démarrage, vous êtes dans ce qu'on appelle le _mode commande_. Vous devriez voir un curseur sur la première ligne, des tildes (~) sur les autres lignes et le nom du fichier tout en bas.

Les lignes avec des tildes sont là pour indiquer que ces lignes ne font pas partie du contenu du fichier.

Pour commencer à écrire dans le fichier, vous devez passer en _mode écriture_. Tapez simplement la lettre 'i'. Tout en bas, vous devriez maintenant voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lIx7lVL_ijhNrd9Nc2w0pQ.jpeg)
_Vim est maintenant en mode écriture_

Alors, allez-y. Écrivez quelque chose.

Terminé ? Voici comment vous pouvez enregistrer vos modifications/quitter Vim. Tout d'abord, vous devez revenir au _mode commande_ en appuyant sur <Échap> et ensuite vous avez le choix :

1. Tapez **:w** et appuyez sur <Entrée> pour enregistrer (write) les modifications.
2. Tapez **:wq** et appuyez sur <Entrée> pour enregistrer les modifications et quitter.
3. Tapez **:q!** et appuyez sur <Entrée> pour quitter sans enregistrer les modifications.

Et c'est à peu près tout pour notre très courte introduction à Vim.

#### Ne pas se perdre et en apprendre davantage sur Vim

Si vous êtes perdu, vous pouvez appuyer sur <Échap> et **taper** :help suivi de <Entrée>. Cela ouvrira la documentation d'aide de Vim.

Quelque chose comme ce simple [Référence Vim](https://simpletutorials.com/c/1238/Simple+Vim+Reference) pourrait être utile si vous êtes nouveau dans Vim. Alternativement, vous pouvez taper 'vimtutor' dans le terminal pour un tutoriel de 30 minutes, jouer à un jeu d'apprentissage sur [http://vim-adventures.com/](http://vim-adventures.com/) ou suivre le tutoriel interactif sur [http://www.openvim.com/](http://www.openvim.com/).

### 3. Node.js

L'installation de [Node.js](https://nodejs.org/en/) est très simple :

```bash
$ apt install nodejs
```

Si vous ne l'avez pas encore fait, créez un dossier pour l'application, déplacez-vous dedans et tapez :

```bash
$ npm init
```

Cela vous posera une série de questions, puis écrira un fichier 'package.json' pour vous. (Vous pouvez simplement appuyer sur <Entrée> pour chaque question posée.)

Maintenant, vérifions que tout fonctionne correctement. Ouvrez server.js

```bash
$ vim server.js
```

et tapez dedans

```js
console.log('Ceci est Node.js qui s\'exécute sur Android.')
```

Enregistrez les modifications et quittez Vim.

Maintenant, nous avons tout en place et nous pouvons enfin exécuter node :

```bash
$ node server.js
```

Cela devrait afficher le texte « Ceci est Node.js qui s'exécute sur Android. » dans le terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XqfRST9jFzNJQPzdWrBITw.jpeg)

### En résumé

Pour récapituler, voici tout le processus à nouveau (avec des différences mineures car tout est fait directement depuis la ligne de commande).

```
Mettre à jour et améliorer Termux :
  $ apt update && apt upgrade
  
Installer quelques utilitaires de base, Vim et Node.js :
  $ apt install coreutils
  $ apt install vim
  $ apt install nodejs
  
Créer un répertoire appelé test-node et s'y déplacer :
  $ mkdir test-node && cd test-node
  
Créer un fichier vide appelé server.js :
  $ touch server.js
  
Créer un fichier package.json de manière interactive :
  $ npm init
  
Ajouter du contenu à server.js :
  $ echo "console.log('Ceci est Node.js qui s\'exécute sur Android.')" > server.js
  
Exécuter node :
  $ node server.js
```

### Conclusion

Nous avons vu comment utiliser Termux sur Android, comment éditer des fichiers avec Vim et comment exécuter Node.js.

Voici les principaux liens liés à Termux : sa [page web](https://termux.com/), son [wiki](https://wiki.termux.com/) et ses [dépôts GitHub](https://github.com/termux). Il peut être installé depuis le [Play Store](https://play.google.com/store/apps/details?id=com.termux) ou depuis le catalogue [F-Droid](https://f-droid.org/en/packages/com.termux/).

Dans [le prochain article](https://medium.freecodecamp.com/building-a-node-js-application-on-android-part-2-express-and-nedb-ced04caea7bb), nous allons construire une application Node.js de base en utilisant le framework web [Express](http://expressjs.com/) et une base de données JavaScript légère appelée [NeDB](https://github.com/louischatriot/nedb) qui utilise l'API de [MongoDB](https://www.mongodb.org/) et peut être utilisée pour développer et exécuter une application web dans Termux.

En attendant, bon codage !
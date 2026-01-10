---
title: Créer une application Electron avec create-react-app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-12T00:43:43.000Z'
originalURL: https://freecodecamp.org/news/building-an-electron-application-with-create-react-app-97945861647c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PQwgjFvq8KcaNOyjZqC5ig.jpeg
tags:
- name: Electron
  slug: electron
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
seo_title: Créer une application Electron avec create-react-app
seo_desc: 'By Christian Sepulveda

  No webpack configuration or “ejecting” necessary.

  I recently built an Electron app using create-react-app. I didn’t need to muck about
  with Webpack, or “eject” my app, either. I’ll walk you through how I accomplished
  this.

  I wa...'
---

Par Christian Sepulveda

### Aucune configuration webpack ou « éjection » nécessaire.

J'ai récemment construit une application [Electron](http://electron.atom.io/) en utilisant [create-react-app](https://github.com/facebookincubator/create-react-app). Je n'ai pas eu besoin de bidouiller avec Webpack, ni d'« éjecter » mon application. Je vais vous expliquer comment j'ai accompli cela.

J'ai été attiré par l'idée d'utiliser [create-react-app](https://github.com/facebookincubator/create-react-app) car il masque les détails de configuration de webpack. Mais ma recherche de guides existants pour utiliser Electron et create-react-app ensemble n'a pas donné de résultats, alors je me suis lancé et j'ai compris par moi-même.

Si vous êtes impatient, vous pouvez plonger directement et regarder mon code. Voici le [dépôt GitHub](https://github.com/csepulv/electron-with-create-react-app) de mon application.

Avant de commencer, laissez-moi vous parler d'Electron et de React, et pourquoi create-react-app est un outil si formidable.

### Electron et React

React est le framework de vue JavaScript de Facebook.

[**_Une bibliothèque JavaScript pour construire des interfaces utilisateur_ - React**](https://facebook.github.io/react/)  
[Une bibliothèque JavaScript pour construire des interfaces utilisateurfacebook.github.io](https://facebook.github.io/react/)

Et Electron est le framework de GitHub pour construire des applications de bureau multiplateformes en JavaScript.

[**Electron**](http://electron.atom.io/)  
[_Construire des applications de bureau multiplateformes avec JavaScript, HTML et CSS._electron.atom.io](http://electron.atom.io/)

La plupart utilisent [webpack](https://webpack.github.io/) pour la configuration nécessaire au développement React. webpack est un outil de configuration et de construction que la plupart de la communauté React a adopté par rapport à des alternatives comme [Gulp](http://gulpjs.com/) et [Grunt](http://gruntjs.com).

Les frais généraux de configuration varient (plus sur cela plus tard), et il existe de nombreux générateurs de modèles et d'applications disponibles, mais en juillet 2016, [Facebook Incubator](https://github.com/facebookincubator) a publié un outil, [create-react-app](https://github.com/facebookincubator/create-react-app). Il masque la plupart de la configuration et permet au développeur d'utiliser des commandes simples, telles que `npm start` et `npm run build` pour exécuter et construire leurs applications.

#### Qu'est-ce que l'éjection, et pourquoi voulez-vous l'éviter ?

create-react-app fait certaines hypothèses sur une configuration React typique. Si ces hypothèses ne vous conviennent pas, il existe une option pour [**éjecter**](https://github.com/facebookincubator/create-react-app#converting-to-a-custom-setup) une application (`npm run eject`). L'éjection d'une application copie toute la configuration encapsulée de create-react-app dans votre projet, fournissant une configuration de modèle que vous pouvez modifier comme vous le souhaitez.

Mais c'est un voyage _sans retour_. Vous ne pouvez pas annuler l'éjection et revenir en arrière. Il y a eu 49 versions (au moment de ce post) de create-react-app, chacune apportant des améliorations. Mais pour une application éjectée, vous devriez soit renoncer à ces améliorations, soit trouver comment les appliquer.

Une configuration éjectée compte plus de 550 lignes réparties sur 7 fichiers (au moment de ce post). Je ne comprends pas tout (en fait, la plupart) et je ne veux pas.

#### Objectifs

Mes objectifs sont simples :

* éviter d'éjecter l'application React
* minimiser la colle pour faire fonctionner React et Electron ensemble
* préserver les valeurs par défaut, les hypothèses et les conventions faites par Electron et create-react-app/React. (Cela peut faciliter l'utilisation d'autres outils qui supposent/nécessitent de telles conventions.)

#### Recette de base

1. exécuter `create-react-app` pour générer une application React de base
2. exécuter `npm install --save-dev electron`
3. ajouter `main.js` depuis `[electron-quick-start](https://github.com/electron/electron-quick-start)` (nous le renommerons en `electron-starter.js`, pour plus de clarté)
4. modifier l'appel à `mainWindow.loadURL` (dans `electron-starter.js`) pour utiliser `localhost:3000` (webpack-dev-server)
5. ajouter une entrée principale à `package.json` pour `electron-starter.js`
6. ajouter une cible d'exécution pour démarrer Electron à `package.json`
7. `npm start` suivi de `npm run electron`

Les étapes 1 et 2 sont assez simples. Voici le code pour les étapes 3 et 4 :

```javascript
const electron = require('electron');
// Module pour contrôler la vie de l'application.
const app = electron.app;
// Module pour créer une fenêtre de navigateur native.
const BrowserWindow = electron.BrowserWindow;

const path = require('path');
const url = require('url');

// Gardez une référence globale de l'objet window, si vous ne le faites pas, la fenêtre sera
// fermée automatiquement lorsque l'objet JavaScript sera garbage collecté.
let mainWindow;

function createWindow() {
    // Créez la fenêtre du navigateur.
    mainWindow = new BrowserWindow({width: 800, height: 600});

    // et chargez le index.html de l'application.
    mainWindow.loadURL('http://localhost:3000');

    // Ouvrez les DevTools.
    mainWindow.webContents.openDevTools();

    // Émis lorsque la fenêtre est fermée.
    mainWindow.on('closed', function () {
        // Déréférencez l'objet window, généralement vous stockeriez les fenêtres
        // dans un tableau si votre application supporte plusieurs fenêtres, c'est le moment
        // où vous devriez supprimer l'élément correspondant.
        mainWindow = null
    })
}

// Cette méthode sera appelée lorsque Electron aura terminé
// l'initialisation et sera prêt à créer des fenêtres de navigateur.
// Certaines API ne peuvent être utilisées qu'après cet événement.
app.on('ready', createWindow);

// Quittez lorsque toutes les fenêtres sont fermées.
app.on('window-all-closed', function () {
    // Sur OS X, il est courant pour les applications et leur barre de menu
    // de rester actives jusqu'à ce que l'utilisateur quitte explicitement avec Cmd + Q
    if (process.platform !== 'darwin') {
        app.quit()
    }
});

app.on('activate', function () {
    // Sur OS X, il est courant de recréer une fenêtre dans l'application lorsque
    // l'icône du dock est cliquée et qu'il n'y a pas d'autres fenêtres ouvertes.
    if (mainWindow === null) {
        createWindow()
    }
});

// Dans ce fichier, vous pouvez inclure le reste du code spécifique du processus principal de votre application
// Vous pouvez également les mettre dans des fichiers séparés et les inclure ici.
```

([Gist](https://gist.github.com/csepulv/d4a97eaf9438cb4f7f102a1b2d075b93#file-electron-starter-js))

Et pour les étapes 5 et 6 :

```javascript
{
  "name": "electron-with-create-react-app",
  "version": "0.1.0",
  "private": true,
  "devDependencies": {
    "electron": "^1.4.14",
    "react-scripts": "0.8.5"
  },
  "dependencies": {
    "react": "^15.4.2",
    "react-dom": "^15.4.2"
  },
  "main": "src/electron-starter.js",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject",
    "electron": "electron ."
  }
}
```

([Gist](https://gist.github.com/csepulv/d4a97eaf9438cb4f7f102a1b2d075b93#file-package-json))

Lorsque vous exécutez les commandes npm de l'étape 7, vous devriez voir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/sJ4H86R1flN7pTYswhLYhoXMwBHTa9xe3XaX)

Vous pouvez apporter des modifications en direct au code React et vous devriez les voir reflétées dans l'application Electron en cours d'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/FlDGGzcvBH1uEMNToEmmBz8uDDJDV6GpsLoD)

Cela fonctionne bien pour le développement, mais présente deux inconvénients :

* la production n'utilisera pas `webpack-dev-server`. Elle doit utiliser le fichier statique de la construction du projet React
* (petit) désagrément d'exécuter les deux commandes npm

#### Spécification de l'URL de chargement en production et en développement

En développement, une variable d'environnement peut spécifier l'URL pour `mainWindow.loadURL` (dans `electron-starter.js`). Si la variable d'environnement existe, nous l'utiliserons ; sinon, nous utiliserons le fichier HTML statique de production.

Nous ajouterons une cible d'exécution npm (à `package.json`) comme suit :

```
"electron-dev": "ELECTRON_START_URL=http://localhost:3000 electron ."
```

Mise à jour : Les utilisateurs de Windows devront faire ce qui suit : (merci à [@bfarmilo](http://twitter.com/bfarmilo))

```
"electron-dev": "set ELECTRON_START_URL=http://localhost:3000 && electron ."
```

Dans `electron-starter.js`, nous modifierons l'appel à `mainWindow.loadURL` comme suit :

```javascript
const startUrl = process.env.ELECTRON_START_URL || url.format({
            pathname: path.join(__dirname, '/../build/index.html'),
            protocol: 'file:',
            slashes: true
        });
    mainWindow.loadURL(startUrl);
```

([Gist](https://gist.github.com/csepulv/d4a97eaf9438cb4f7f102a1b2d075b93#file-electron-starter-use-env-var-js))

Il y a un problème avec cela : `create-react-app` (par défaut) construit un `index.html` qui utilise des chemins absolus. Cela échouera lors du chargement dans Electron. Heureusement, il existe une option de configuration pour changer cela : définissez une propriété `homepage` dans `package.json`. (La documentation de Facebook sur la propriété est [ici](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#building-for-relative-paths).)

Nous pouvons donc définir cette propriété sur le répertoire courant et `npm run build` l'utilisera comme un chemin relatif.

```
"homepage": "./",
```

#### Utilisation de Foreman pour gérer les processus React et Electron

Pour plus de commodité, je préfère ne pas

1. lancer/gérer à la fois le serveur de développement React et les processus Electron (je préfère gérer un seul)
2. attendre que le serveur de développement React démarre puis lancer Electron

[Foremen](https://github.com/strongloop/node-foreman) est un bon outil de gestion de processus. Nous pouvons l'ajouter,

```
npm install --save-dev foreman
```

et ajouter le `Procfile` suivant

```
react: npm startelectron: npm run electron
```

([Gist](https://gist.github.com/csepulv/d4a97eaf9438cb4f7f102a1b2d075b93#file-procfile-initial-js))

Cela traite le point (1). Pour le point (2), nous pouvons ajouter un simple script node (`electron-wait-react.js`) qui attend que le serveur de développement React démarre, puis démarre Electron.

```javascript
const net = require('net');
const port = process.env.PORT ? (process.env.PORT - 100) : 3000;

process.env.ELECTRON_START_URL = `http://localhost:${port}`;

const client = new net.Socket();

let startedElectron = false;
const tryConnection = () => client.connect({port: port}, () => {
        client.end();
        if(!startedElectron) {
            console.log('starting electron');
            startedElectron = true;
            const exec = require('child_process').exec;
            exec('npm run electron');
        }
    }
);

tryConnection();

client.on('error', (error) => {
    setTimeout(tryConnection, 1000);
});
```

([Gist](https://gist.github.com/csepulv/d4a97eaf9438cb4f7f102a1b2d075b93#file-electron-wait-react-js))

> NOTE : Foreman décalera le numéro de port de 100 pour les processus de différents types. (Voir [ici](https://github.com/strongloop/node-foreman#advanced-usage).) Donc, `electron-wait-react.js` soustrait 100 pour définir correctement le numéro de port du serveur de développement React.

Maintenant, modifiez le `Procfile`

```
react: npm startelectron: node src/electron-wait-react
```

([Gist](https://gist.github.com/csepulv/d4a97eaf9438cb4f7f102a1b2d075b93#file-profile-final-js))

Enfin, nous modifierons les cibles d'exécution dans `package.json` pour remplacer `electron-dev` par :

```
"dev" : "nf start"
```

Et maintenant, nous pouvons exécuter :

```
npm run dev
```

> MISE À JOUR (25/01/17) : J'ai ajouté la section suivante en réponse à certains commentaires d'utilisateurs ([ici](https://medium.com/@luke_schmuke/hey-there-a84bcaf41f17#.szbo7b33n) et [ici](https://medium.com/@bfarmilo/hi-again-christian-f2601fb40e03#.5sj6cpnih)). Ils ont besoin d'accéder à Electron depuis l'application react et un simple require ou import génère une erreur. Je note une solution ci-dessous.

#### Accéder à Electron depuis l'application React

Une application Electron a deux processus principaux : l'hôte/wrapper Electron et votre application. Dans certains cas, vous souhaitez accéder à Electron depuis votre application. Par exemple, vous pourriez vouloir accéder au système de fichiers local ou utiliser l'[ipcRenderer](http://electron.atom.io/docs/api/ipc-renderer/) d'Electron. Mais si vous faites ce qui suit, vous obtiendrez une erreur

```javascript
const electron = require('electron')
//ou
import electron from 'electron';
```

Il y a une certaine discussion sur cette erreur dans divers problèmes GitHub et Stack Overflow, comme celui-ci [one](https://github.com/electron/electron/issues/7300). La plupart des solutions proposent des modifications de la configuration webpack, mais cela nécessiterait d'éjecter l'application.

Cependant, il existe une solution de contournement/un hack simple.

```
const electron = window.require('electron');
```

```javascript
const electron = window.require('electron');
const fs = electron.remote.require('fs');
const ipcRenderer  = electron.ipcRenderer;
```

#### Conclusion

Pour plus de commodité, voici un [dépôt GitHub](https://github.com/csepulv/electron-with-create-react-app) qui contient toutes les modifications ci-dessus, avec des tags pour chaque étape. Mais il n'y a pas beaucoup de travail à faire pour démarrer une application Electron qui utilise create-react-app. (Ce post est beaucoup plus long que le code et les modifications dont vous auriez besoin pour intégrer les deux.)

Et si vous utilisez create-react-app, vous pourriez vouloir consulter mon post, [Debugging tests in WebStorm and create-react-app](https://medium.com/justideas-io/debugging-tests-in-webstorm-and-create-react-app-b38f389ae7c8#.4qb90t1f1).

Merci d'avoir lu. Vous pouvez consulter plus de mes posts sur [justideas.io](https://justideas.io)

> MISE À JOUR (02/02/17). Un lecteur, [Carl Vitullo](https://github.com/vcarl), a suggéré d'utiliser `npm start` au lieu de `npm run dev` et a soumis une pull request avec les modifications, sur GitHub. Ces ajustements sont disponibles dans cette [branche](https://github.com/csepulv/electron-with-create-react-app/tree/npm-start).
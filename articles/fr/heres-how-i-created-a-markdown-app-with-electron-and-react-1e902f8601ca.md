---
title: Voici comment j'ai créé une application markdown avec Electron et React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-07T17:12:38.000Z'
originalURL: https://freecodecamp.org/news/heres-how-i-created-a-markdown-app-with-electron-and-react-1e902f8601ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AUYsysbayWGQXG23G0L-3g.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Voici comment j'ai créé une application markdown avec Electron et React
seo_desc: 'By Tzahi Vidas

  This article is a step-by-step tutorial on how to create a basic markdown application
  using Electron and React.

  I’ll describe why, how, and what I used to create the markdown app, which I call
  Mook.

  The source code for Mook can be foun...'
---

Par Tzahi Vidas

Cet article est un tutoriel étape par étape sur la création d'une application markdown de base en utilisant [Electron](https://electron.atom.io/) et [React.](https://facebook.github.io/react/)

Je vais décrire pourquoi, comment et ce que j'ai utilisé pour créer l'application markdown, que j'appelle **Mook**.

Le code source de Mook peut être trouvé sur [GitHub](https://github.com/kazuar/mook).

### Motivation

Il y a plusieurs raisons pour lesquelles j'ai commencé ce projet.

Récemment, j'ai vu plus de choses impressionnantes et intéressantes que vous pouvez faire avec JavaScript. J'avais aussi envie de faire quelque chose avec [Electron](https://electron.atom.io/) depuis un certain temps.

J'ai toujours trouvé bizarre de coder avec JavaScript, et, par conséquent, je l'ai évité. Chaque fois que j'ai essayé de faire quelque chose avec JavaScript, j'avais toujours l'impression de simplement taper sur un clavier pour faire fonctionner ce que je voulais.

![Image](https://cdn-media-1.freecodecamp.org/images/utrP4W38SfxvfTxeSADlp9z-cV8e6T3Copww)

Cependant, je me suis récemment retrouvé à regarder plus en détail JavaScript. Cela a soudainement semblé être un bon outil à utiliser pour résoudre certains des problèmes sur lesquels je travaille.

Sur une autre note (voir le jeu de mots ?), chaque fois que j'utilise une application de prise de notes, j'ai toujours l'impression qu'il manque une fonctionnalité que je peux trouver dans une autre application. Mais l'autre application n'aura pas les fonctionnalités que la troisième application pourrait fournir. Et ainsi, je suis toujours à la recherche de nouvelles et meilleures applications de prise de notes.

Avec ces pensées en tête, j'ai décidé d'apprendre JavaScript tout en construisant un éditeur de notes markdown avec Electron.

### Exigences

Certaines des exigences que j'ai établies pour l'application markdown sont listées ci-dessous.  
Notez qu'il y en a beaucoup plus, mais les suivantes sont sur ma liste initiale.

* Panneaux d'édition et de prévisualisation
* Écran divisé entre les panneaux d'édition et de prévisualisation qui peut être déplacé dynamiquement
* Support pour les blocs de code et la coloration syntaxique des langages de code
* Support pour la sauvegarde et la synchronisation des notes sur GitHub
* Une hiérarchie de carnets et de notes markdown
* Support pour LaTeX / équations mathématiques dans l'éditeur
* Capacité à regrouper différents carnets avec un sujet partagé
* Capacité à partager des carnets sur GitHub et sur Dropbox, Google Docs et autres.

### La pile technologique

J'ai dû prendre quelques décisions pour ce projet. Par exemple :

Dois-je utiliser un [boilerplate](https://github.com/chentsulin/electron-react-boilerplate) ?

Dois-je utiliser React, [AngularJS](https://en.wikipedia.org/wiki/AngularJS), [Riot](http://riotjs.com/), ou [Vue](https://vuejs.org/) ?

Quels types de packages devrais-je utiliser ?

Et ainsi de suite.

En fin de compte, j'ai décidé d'éviter l'approche boilerplate (au moins pour l'instant). Je l'ai fait parce que je voulais construire les fondations de l'application moi-même et en apprendre davantage à ce sujet dans le processus.

J'ai essayé de construire l'application avec React parce que j'en ai beaucoup entendu parler de la part d'amis. Il semble que ce soit ce que les enfants cool utilisent ces jours-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/ICDj0frNAuq-cLLBJApvUQ7frLzuVitvq3lw)

### Création de l'environnement pour l'application

Parce que nous utilisons React, nous allons commencer par créer une application React de base puis ajouter Electron à celle-ci.

Nous allons démarrer notre projet en utilisant [create-react-app](https://github.com/facebookincubator/create-react-app).

#### Préparation de l'environnement

Un moyen facile de créer des applications React avec une configuration de base est d'utiliser **create-react-app**.

Tout d'abord, assurez-vous d'avoir les dernières versions de node et npm sur votre machine. Pour vérifier, exécutez les commandes suivantes :

```
node -v
npm -v
yarn --version
```

Lorsque j'écrivais cet article, voici les versions sur ma machine :

```
node = v8.4.0
npm = 5.3.0
yarn = 1.0.1
```

#### Créer une application React avec create-react-app

Pour installer **create-react-app** en tant que package global, tapez la commande suivante :

```
npm install -g create-react-app
```

Pour créer une nouvelle application React et `cd` dedans :

```
create-react-app mook
cd mook
```

Voici à quoi ressemble notre projet maintenant. J'ai exclu le dossier `**node_modules**` de la vue pour que vous puissiez avoir une vue claire du projet.

```
tree -I "node_modules"
.
├── README.md
├── package.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
├── src
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   └── registerServiceWorker.js
└── yarn.lock

2 directories, 13 files
```

Maintenant que nous avons une application React de base, pour voir à quoi elle ressemble, exécutons le script `start` qui est défini dans le fichier `**package.json**` :

```
yarn run start
```

Cela ouvre une nouvelle fenêtre de navigateur avec la page suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/lsK3QALqqYu3tMMGYdKdP9z5l4qDsQFkoTbN)

#### Installer Electron

Electron nous permet de construire une application capable de s'exécuter sur plusieurs plateformes.

Pour installer le package Electron :

```
yarn add electron --dev
```

Ouvrez le fichier `**package.json**`.

Si tout est OK, vous devriez pouvoir voir le package Electron dans la section `**devDependencies**` du fichier.

Mettez à jour le fichier `**package.json**` avec les modifications suivantes :

* Pour ajouter la ligne suivante à la section des scripts :

```
"electron-start": "electron ."
```

* Pour ajouter une propriété `**main**` de niveau supérieur et la pointer vers le fichier principal d'Electron (ce fichier n'existe pas encore, mais nous allons le créer bientôt) :

```
"main": "public/main.js"
```

Le fichier `**package.json**` ressemble maintenant à ceci :

```json
{
  "name": "mook",
  "version": "0.1.0",
  "main": "public/main.js",
  "private": true,
  "dependencies": {
    "react": "^15.6.1",
    "react-dom": "^15.6.1",
    "react-scripts": "1.0.13"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject",
    "electron-start": "electron ."
  },
  "devDependencies": {
    "electron": "^1.7.6"
  }
}
```

Ensuite, nous allons ajouter certains des [événements d'Electron](https://github.com/electron/electron/blob/master/docs/api/app.md) pour contrôler le cycle de vie de l'application. Nous allons implémenter les événements suivants :

* [**ready**](https://github.com/electron/electron/blob/master/docs/api/app.md#event-ready) : S'exécute lorsque Electron a terminé l'initialisation. Dans le code, cela exécutera `**createWindow**`, qui crée une fenêtre de navigateur avec l'URL locale de React, `**http://localhost:3000**`, et définit le panneau à propos et la `**mainWindow**` à `null` lors de la fermeture.
* [**activate**](https://github.com/electron/electron/blob/master/docs/api/app.md#event-activate-macos) : S'exécute lorsque l'application est activée. Nous voudrons appeler la fonction `**createWindow**` pour créer une nouvelle fenêtre.
* [**window-all-closed**](https://github.com/electron/electron/blob/master/docs/api/app.md#event-window-all-closed) : Émis lorsque toutes les fenêtres ont été fermées. Cela fermera l'application sur toutes les plateformes, sauf Mac, qui ne fermera que la fenêtre mais nécessitera explicitement que l'utilisateur quitte le programme.

Ajoutez le code suivant à `**public/main.js**` :

```js
const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({width: 900, height: 680});
  mainWindow.loadURL('http://localhost:3000');
                    
  app.setAboutPanelOptions({
    applicationName: "Mook",
    applicationVersion: "0.0.1",
  })
  
  mainWindow.on('closed', () => mainWindow = null);
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
```

Assurez-vous que React est toujours en cours d'exécution en arrière-plan. Si ce n'est pas le cas, relancez-le avec la commande suivante :

```
yarn run start
```

Ouvrez une nouvelle fenêtre de ligne de commande dans le dossier du projet et exécutez la commande suivante :

```
yarn run electron-start
```

Après avoir exécuté la commande, la fenêtre suivante s'ouvre :

![Image](https://cdn-media-1.freecodecamp.org/images/Mo590jpoclfSSANaDlvQ8r7tIlPeQifWNh7L)

Si React n'est pas en cours d'exécution en arrière-plan, l'application Electron s'ouvrira avec une fenêtre blanche vide.

#### Création d'un processus de développement et de construction stable

Maintenant que nous avons un modèle fonctionnel pour notre projet utilisant Electron et React, nous devons nous assurer que nous avons une version stable pour le développement et la distribution.

Ce que nous avons créé jusqu'à présent est idéal pour le développement, mais finalement nous voulons créer les versions de distribution de l'application pour OS X, Windows et Linux.

Je n'aimais pas non plus le fait que nous devons exécuter séparément le serveur React et l'application Electron dans deux shells de ligne de commande différents.

Après avoir fait quelques recherches sur le sujet, j'ai trouvé l'article suivant, « [From React to an Electron app ready for production](https://medium.com/@kitze/🚀-from-react-to-an-electron-app-ready-for-production-a0468ecb1da3) » par [@thekitze](http://twitter.com/thekitze), qui m'a beaucoup aidé.

Nous devrons ajouter les packages suivants à notre projet :

* [electron-builder](https://www.electron.build/) — Une solution complète pour packager et construire une application Electron prête pour la distribution pour MacOS, Windows et Linux avec un support « auto update » intégré. Nous utiliserons ce package pour construire notre application pour la distribution.
* [concurrently](https://github.com/kimmobrunfeldt/concurrently) — Exécute des commandes de manière concurrente. Nous utiliserons ce package pour exécuter React et Electron de manière concurrente en une seule commande.
* [wait-on](https://github.com/jeffbski/wait-on) — Utilitaire de ligne de commande et API Node.js, qui attendra que des fichiers, ports, sockets et ressources http(s) deviennent disponibles. Nous utiliserons ce package pour attendre que le serveur React commence à fonctionner avant de démarrer l'application Electron.

Exécutez les commandes suivantes pour ajouter ces packages à notre application :

```
yarn add electron-builder wait-on concurrently --dev
```

Puisque ces packages ne sont nécessaires que pour le développement, nous ajouterons le flag `--dev` à la commande `yarn add`. Cela ajoutera également automatiquement les packages à la partie `**devDependencies**` de `**package.json**`.

#### Créer un script de développement

Nous voulons créer un script de développement à utiliser pendant que nous construisons l'application. Cela nous aidera à tester les nouvelles fonctionnalités que nous avons développées dans l'application et également à déboguer et à nous assurer que nous ne cassons rien pendant que nous éditons le code.

Nous ajouterons un nouveau script dans la section `**scripts**` de notre fichier `**package.json**` :

```
"electron-dev": "concurrently \"BROWSER=none yarn start\" \"wait-on http://localhost:3000 && electron .\""
```

Il se passe beaucoup de choses dans cette ligne, alors décomposons-la :

![Image](https://cdn-media-1.freecodecamp.org/images/4vjCPBpvCmt8MH03cfx56EoQ4dm6wSMUv1Bv)

1. « **concurrently** » — Exécute les commandes suivantes en même temps.
2. « **BROWSER=none yarn start** » — Démarre l'application react et définit « **BROWSER=none** ». Cela signifie que le navigateur n'ouvrira pas automatiquement l'application React.
3. « **wait-on http://localhost:3000 && electron** » — Attend que le serveur de développement démarre. Une fois qu'il est démarré, il démarrera l'application Electron.

Maintenant, si vous exécutez la commande suivante depuis votre ligne de commande, vous n'obtiendrez qu'une seule fenêtre d'application Electron avec le logo React.

```
yarn run electron-dev
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1__2brQgn4gVrugCl65hwQXQ.png)

#### Créer un script de build

Créer le script de build est un peu plus facile.

Nous devons ajouter quelques scripts à la section `**scripts**` dans le fichier `**package.json**` :

* Voici un script pour construire l'application React avant de construire l'application Electron :

```
"preelectron-pack": "yarn build"
```

* Voici un script pour packager l'application Electron. Ce script construit le package de l'application avec **electron-builder**.

```
"electron-pack": "build --em.main=build/electron.js"
```

Ensuite, nous devrons spécifier la propriété `**build**`. Cela est dû à un léger conflit entre **create-react-app** et **electron-builder**. Les deux utilisent le dossier `**build**` pour un but différent.

Pour résoudre ce conflit, nous devons configurer manuellement les dossiers corrects de **electron-builder** pour l'étape de build. Ajoutez la section `**build**` suivante au fichier `**package.json**` :

```json
"build": {
  "appId": "com.mook",
  "files": [
    "build/**/*",
    "node_modules/**/*"
  ],
  "directories": {
    "buildResources": "assets"
  }
}
```

Nous devons également ajouter la propriété `**homepage**` pour permettre à l'application Electron packagée de trouver les fichiers JavaScript et CSS :

```
"homepage": "./"
```

À ce stade, votre fichier `**package.json**` devrait ressembler à ceci :

```json
{
  "name": "mook",
  "version": "0.1.0",
  "main": "public/main.js",
  "homepage": "./",
  "private": true,
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject",
    "electron-start": "electron .",
    "electron-dev": "concurrently \"BROWSER=none yarn start\" \"wait-on http://localhost:3000 && electron .\"",
    "electron-pack": "build --em.main=build/main.js",
    "preelectron-pack": "yarn build"
  },
  "dependencies": {
    "react": "^15.6.1",
    "react-dom": "^15.6.1",
    "react-scripts": "1.0.13",
    "electron-is-dev": "^0.3.0"
  },
  "devDependencies": {
    "concurrently": "^3.5.0",
    "electron": "^1.7.6",
    "electron-builder": "^19.27.7",
    "wait-on": "^2.0.2"
  },
  "build": {
    "appId": "com.mook",
    "files": [
      "build/**/*",
      "node_modules/**/*"
    ],
    "directories": {
      "buildResources": "assets"
    }
  }
}
```

La dernière étape consistera à mettre à jour `**public/main.js**`. Jusqu'à présent, nous n'avons pris en charge que la version de développement de l'application. En production, nous ne pourrons pas utiliser `**localhost:3000**`, nous servirons plutôt le fichier `**index.html**` depuis le dossier `**build**`.

Tout d'abord, nous devons installer [electron-is-dev](https://github.com/sindresorhus/electron-is-dev), qui nous aidera à déterminer si Electron est en cours d'exécution en développement.

Pour installer le package **electron-is-dev** :

```
yarn add electron-is-dev
```

Pour mettre à jour `**public/main.js**` afin d'utiliser [electron-is-dev :](https://github.com/sindresorhus/electron-is-dev)

* Pour ajouter le package au code :

```js
const isDev = require('electron-is-dev');
const path = require('path');
```

* Pour changer la fonctionnalité `**mainWindow.loadURL**` dans la fonction `**createWindow**` :

```js
mainWindow.loadURL(isDev ? 'http://localhost:3000' : `file://${path.join(__dirname, '../build/index.html')}`);
```

Ce code vérifie si nous sommes en mode développement, et si c'est le cas, il utilisera `**localhost:3000**`. Sinon, il servira `**/build/index.html**`.

Votre fichier `**public/main.js**` devrait maintenant ressembler à ceci :

```
const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const isDev = require('electron-is-dev');
const path = require('path');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({width: 900, height: 680});
  mainWindow.loadURL(isDev ? 'http://localhost:3000' : `file://${path.join(__dirname, '../build/index.html')}`);
  
  app.setAboutPanelOptions({
    applicationName: "Mook",
    applicationVersion: "0.0.1",
  })
  
  mainWindow.on('closed', () => mainWindow = null);
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
```

Maintenant, essayons d'exécuter le script de build avec la commande suivante :

```
yarn run electron-pack
```

Lorsque l'exécution du script est terminée, vous devriez voir un nouveau dossier nommé `**dist**` dans le répertoire de votre projet. Vous pouvez trouver votre application packagée dans le dossier nommé d'après votre système d'exploitation. Par exemple, les utilisateurs de Mac pourront trouver l'application packagée `**mook.app**` dans le dossier `**dist/mac**`.

Lorsque vous exécutez ce fichier, vous devriez obtenir le même écran que pour la version de débogage :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1__2brQgn4gVrugCl65hwQXQ-1.png)

Excellent, nous venons de terminer l'infrastructure de build pour notre application.

![Image](https://cdn-media-1.freecodecamp.org/images/lInY6KaaZ7USQOYq9c1KZoiKFmJ-tVpUxt7G)

### Ajout des fonctionnalités principales

Maintenant, nous sommes en mesure de commencer à ajouter des blocs de construction à notre application markdown.

#### Création d'un écran divisé

Commençons par ajouter le composant de panneau divisé, [react-split-pane](https://github.com/tomkp/react-split-pane), à notre application.

Pour installer le package **react-split-pane** :

```
yarn add react-split-pane
```

Pour ajouter le code JavaScript suivant au fichier `**src/App.js**` :

* Importer `**react-split-pane**` :

```js
import SplitPane from 'react-split-pane';
```

* Remplacer la fonction de rendu par le code suivant. Ce code ajoute l'élément `**SplitPane**` à la fonction de rendu avec deux divs, une pour l'éditeur et une pour le panneau de prévisualisation :

```jsx
render() {
  return (
    <div className="App">
      <SplitPane split="vertical" defaultSize="50%">
        <div className="editor-pane">
        </div>
        <div className="view-pane">
        </div>
      </SplitPane>
    </div>
  );
}
```

Nous devons également ajouter un peu de CSS.

Pour ajouter le code suivant à `**src/App.css**` :

```css
.Resizer {
  background: #000;
  opacity: 0.4;
  z-index: 1;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -moz-background-clip: padding;
  -webkit-background-clip: padding;
  background-clip: padding-box;
}
.Resizer:hover {
  -webkit-transition: all 2s ease;
  transition: all 2s ease;
}
.Resizer.horizontal {
  height: 11px;
  margin: -5px 0;
  border-top: 5px solid rgba(255, 255, 255, 0);
  border-bottom: 5px solid rgba(255, 255, 255, 0);
  cursor: row-resize;
  width: 100%;
}
.Resizer.horizontal:hover {
  border-top: 5px solid rgba(0, 0, 0, 0.5);
  border-bottom: 5px solid rgba(0, 0, 0, 0.5);
}
.Resizer.vertical {
  width: 11px;
  margin: 0 -5px;
  border-left: 5px solid rgba(255, 255, 255, 0);
  border-right: 5px solid rgba(255, 255, 255, 0);
  cursor: col-resize;
}
.Resizer.vertical:hover {
  border-left: 5px solid rgba(0, 0, 0, 0.5);
  border-right: 5px solid rgba(0, 0, 0, 0.5);
}
.Resizer.disabled {
  cursor: not-allowed;
}
.Resizer.disabled:hover {
  border-color: transparent;
}

```

Si vous actualisez l'application ou l'exécutez avec la commande `**yarn run electron-dev**`, vous devriez voir l'écran suivant, qui est actuellement juste une page vide divisée en deux panneaux :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_N7OaT0YRZHck2YnRZ6BHyA.png)

Vous pouvez jouer avec la barre de séparation et voir comment elle redimensionne les différents panneaux.

### Création des panneaux d'édition et de prévisualisation

Maintenant que nous avons notre écran divisé, nous devons ajouter des fonctionnalités pour les panneaux d'édition et de prévisualisation.

Nous voulons configurer les panneaux comme ils sont généralement configurés dans les éditeurs markdown, avec le panneau d'édition à gauche et le panneau de prévisualisation à droite. Nous allons écrire notre markdown dans le panneau d'édition, et le panneau de prévisualisation se mettra à jour chaque fois que nous changerons quelque chose dans le panneau d'édition.

#### Création du panneau d'édition

Commençons par le panneau d'édition.

Nous allons utiliser [CodeMirror](https://codemirror.net/), qui est un éditeur de texte JavaScript.

Installez le package React pour code mirror [React-CodeMirror](https://github.com/JedWatson/react-codemirror). Parce que « [Code mirror value doesn't update with state change](https://github.com/JedWatson/react-codemirror/issues/106) » dans **React-CodeMirror**, nous allons installer `[**@skidding/react-codemirror**](http://twitter.com/skidding/react-codemirror)`, qui résout ce problème :

```
yarn add @skidding/react-codemirror
```

Créez un nouveau fichier appelé `**src/editor.js**`, avec une nouvelle classe appelée `Editor` qui étend la classe Component de React :

```jsx
import React, { Component } from 'react';

class Editor extends Component {
}

export default Editor;
```

Cette classe enveloppera essentiellement le package **react-codemirror** qui est un composant React pour CodeMirror.

Ensuite, nous importerons `**@skidding/react-codemirror**` et certains fichiers CSS que nous voulons utiliser pour le composant CodeMirror, la coloration syntaxique et le mode markdown.

Nous ajouterons également une fonction `render` qui retournera l'élément CodeMirror et ajouterons un `**constructor**` à la classe `**Editor**`. Ce **constructor** nous permet d'initialiser CodeMirror avec une valeur provenant du fichier principal.

Nous définirons le composant `CodeMirror` en mode `**markdown**` et le thème en `**monokai**` :

```jsx
import React, { Component } from 'react';
import CodeMirror from '@skidding/react-codemirror';

require('codemirror/lib/codemirror.css');
require('codemirror/mode/javascript/javascript');
require('codemirror/mode/python/python');
require('codemirror/mode/xml/xml');
require('codemirror/mode/markdown/markdown');
require('codemirror/theme/monokai.css');

class Editor extends Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    var options = {
      mode: 'markdown',
      theme: 'monokai',
    }
    return (
      <CodeMirror value={this.props.value} 
 options={options} height="100%"
/>
    );
  }
}

export default Editor;
```

Dans le fichier `**src/App.js**`, nous importerons `**editor.js**` (ajoutez au début du fichier) :

```js
import Editor from './editor.js';
```

Dans la classe `**App**`, ajoutons un constructeur avec une valeur initiale pour notre éditeur :

```jsx
constructor(props) {
  super();
  
  this.state = {
    markdownSrc: "# Hello World",
  }
}
```

Dans la fonction `**render**` de la classe `**App**`, ajoutez le composant `**Editor**` et définissez la valeur sur `**markdownSrc**` :

```jsx
render() {
  return (
    <div className="App">
      <SplitPane split="vertical" defaultSize="50%">
        <div className="editor-pane">
          <Editor className="editor" value={this.state.markdownSrc}/>
        </div>
        <div className="view-pane">
        </div>
      </SplitPane>
    </div>
  );
}
```

Le fichier `**src/App.js**` devrait ressembler à ceci :

```jsx
import React, { Component } from 'react';
import logo from './logo.svg';
import SplitPane from 'react-split-pane';
import Editor from './editor.js';

import './App.css';

class App extends Component {
  constructor(props) {
    super();
    
    this.state = {
      markdownSrc: "# Hello World",
    }
  }
  
  render() {
    return (
      <div className="App">
        <SplitPane split="vertical" defaultSize="50%">
          <div className="editor-pane">
            <Editor className="editor" value={this.state.markdownSrc}/>
          </div>
          <div className="view-pane">
          </div>
        </SplitPane>
      </div>
    );
  }
}

export default App;
```

Mettez à jour le fichier CSS `**src/App.css**` avec les modifications suivantes :

1. Dans la section `**_._App**` (en haut du fichier), supprimez `text-align: center_;_` pour que le texte ne soit pas aligné au centre.
2. Ajoutez le code CSS suivant, afin qu'il étire l'éditeur à la hauteur complète et ajoute un peu de remplissage du côté droit du texte :

```css
.editor-pane {
  height: 100%;
}

.CodeMirror {
  height: 100%;
  padding-top: 20px;
  padding-left: 20px;
}

.ReactCodeMirror {
  height: 100%;
}
```

Actualisez l'application ou exécutez-la avec la commande `**yarn run electron-dev**`, et vous devriez voir l'écran suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/qrzujQdXJKWkneuwg3GkQ9VJwI-9pmvY4Lsj)

#### Création du panneau de prévisualisation

Nous voulons que le panneau de droite soit une prévisualisation en direct de l'éditeur qui se trouve dans le panneau de gauche.

Pour ce faire, nous utiliserons le package [React-Markdown](https://github.com/rexxars/react-markdown) :

```
yarn add react-markdown
```

Dans le fichier `**src\App.js**`, ajoutez l'importation suivante :

```js
import ReactMarkdown from 'react-markdown';
```

Ajoutez le composant `**ReactMarkdown**` à l'intérieur de la div `view-pane` :

```jsx
<div className="view-pane">
  <ReactMarkdown className="result" source={this.state.markdownSrc} />
</div>
```

Définissez la source du composant `**ReactMarkdown**` pour qu'elle soit la même que celle de l'éditeur, `**this.state.markdownSrc**`.

Vous pouvez maintenant exécuter l'application yarn et voir le panneau de prévisualisation :

```
yarn run electron-dev
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_xJEfP8eefOh1U-_u1P6BBA.png)

Nous pouvons voir le texte dans le panneau de prévisualisation. Cependant, si nous tapons quelque chose dans le panneau de l'éditeur (à gauche), il ne sera pas transféré vers le panneau de prévisualisation (à droite).

Ce que nous allons faire, c'est faire en sorte que chaque changement dans l'éditeur soit transmis à la prévisualisation, via la classe `**App**`.

L'ajout de la fonction `onMarkdownChange` à `**src\App.js**` mettra à jour `**markdownSrc**` avec le texte mis à jour de l'éditeur. Cette fonction s'exécutera à chaque changement qui se produit dans l'éditeur.

Ajoutez le code suivant à `**src\App.js**` :

```jsx
constructor(props) {
  super();
  
  this.state = {
    markdownSrc: "# Hello World"
  }
  
  this.onMarkdownChange = this.onMarkdownChange.bind(this);
}

onMarkdownChange(md) {
  this.setState({
    markdownSrc: md
  });
}
```

Dans la fonction `render`, ajoutez ce qui suit à l'élément `Editor` :

```jsx
<Editor className="editor" value={this.state.markdownSrc} onChange={this.onMarkdownChange}/>
```

Dans le fichier `**src/editor.js**`, liez la fonction `onChange` de **CodeMirror** à la fonction `onChange` du parent :

```jsx
constructor(props) {
  super(props);
  
  this.updateCode = this.updateCode.bind(this);
}

updateCode(e) {
  this.props.onChange(e);
}
```

Dans la fonction `**render**`, ajoutez ce qui suit à l'élément `**CodeMirror**` :

```jsx
<CodeMirror
  value={this.props.value}
  onChange={this.updateCode}
  options={options}
  height="100%"
/>
```

Le fichier `**src/App.js**` devrait ressembler à ceci :

```jsx
import React, { Component } from 'react';
import logo from './logo.svg';
import SplitPane from 'react-split-pane';
import Editor from './editor.js';
import ReactMarkdown from 'react-markdown';

import './App.css';

class App extends Component {
  constructor(props) {
    super();
    
    this.state = {
      markdownSrc: "# Hello World"
    }
    
    this.onMarkdownChange = this.onMarkdownChange.bind(this);
  }
  
  onMarkdownChange(md) {
    this.setState({
      markdownSrc: md
    });
  }
  
  render() {
    return (
      <div className="App">
        <SplitPane split="vertical" defaultSize="50%">
          <div className="editor-pane">
            <Editor className="editor" value={this.state.markdownSrc} onChange={this.onMarkdownChange}/>
          </div>
          <div className="view-pane">
            <ReactMarkdown className="result" source={this.state.markdownSrc} />
          </div>
        </SplitPane>
      </div>
    );
  }
}

export default App;
```

Le fichier `**src/editor.js**` ressemble maintenant à ceci :

```jsx
import React, { Component } from 'react';
import CodeMirror from '@skidding/react-codemirror';

require('codemirror/lib/codemirror.css');
require('codemirror/mode/javascript/javascript');
require('codemirror/mode/python/python');
require('codemirror/mode/xml/xml');
require('codemirror/mode/markdown/markdown');
require('codemirror/theme/monokai.css');

class Editor extends Component {
  constructor(props) {
    super(props);
    
    this.updateCode = this.updateCode.bind(this);
  }
  
  updateCode(e) {
    this.props.onChange(e);
  }
  
  render() {
    var options = {
      mode: 'markdown',
      theme: 'monokai',
    }
    return (
      <CodeMirror value={this.props.value} onChange={this.updateCode} options={options} height="100%"
/>
    );
  }
}

export default Editor;
```

Lorsque vous rechargez l'application, vous devriez être en mesure de mettre à jour l'éditeur à gauche avec du texte et voir les changements dans le panneau de prévisualisation à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/YCGmL8j7lBA8FXFxS2lhipmwEtWomD82DJx5)

Le code source complet peut être trouvé sur [GitHub](https://github.com/kazuar/mook).

### Qu'est-ce qui suit ?

Il reste encore beaucoup de choses à accomplir ici :

1. Sauvegarder et ouvrir des fichiers
2. Sauvegarde automatique pendant l'édition
3. Barre d'outils / contrôle sur la disposition des panneaux
4. Sauvegarder les notes sur GitHub, Dropbox et autres.
5. Prise en charge de la sauvegarde des notes en groupes ou unifiées dans un « carnet »
6. Prise en charge des équations mathématiques dans M[edium](https://medium.com/@kazuarous/1e902f8601ca)
7. Plus de fonctionnalités incroyables !

Je suppose que c'est ce que nous ferons la prochaine fois...

![Image](https://cdn-media-1.freecodecamp.org/images/QyZbClSqx8tpBopkHwX7uxeV8TQP429pojtE)

Suivez-moi sur [Twitter](http://@kazuarous) pour des mises à jour sur les progrès, les fonctionnalités à venir, ou pour toute autre raison.

### Contributions

Vous pouvez contribuer de n'importe quelle manière. Toute aide est appréciée.  
N'hésitez pas à partager vos suggestions ou commentaires.

De plus, si vous souhaitez voir une fonctionnalité que vous pensez importante, n'hésitez pas à demander dans les commentaires ci-dessous ou à ouvrir un problème sur [GitHub](https://github.com/kazuar/mook).
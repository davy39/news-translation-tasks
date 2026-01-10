---
title: Comment créer des extensions Chrome avec React + Parcel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-25T13:00:07.000Z'
originalURL: https://freecodecamp.org/news/building-chrome-extensions-in-react-parcel-79d0240dd58f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GIwcjdd76nYEvw-0nnJHvQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer des extensions Chrome avec React + Parcel
seo_desc: 'By Atakan Goktepe

  This month, I started to build my new product. It helps convert any website to JSON,
  XML, CSV, or any other format. I wrote my own Chrome extension for pointing to the
  fields in websites.

  Most articles show how you can render it in ...'
---

Par Atakan Goktepe

Ce mois-ci, j'ai commencé à construire mon nouveau produit. Il aide à convertir n'importe quel site web en JSON, XML, CSV, ou tout autre format. J'ai écrit ma propre extension Chrome pour pointer les champs dans les sites web.

La plupart des articles montrent comment vous pouvez le rendre dans une popup. Dans cet article, nous allons rendre notre application directement dans le contenu (avec [Content Scripts](https://developer.chrome.com/apps/content_scripts)). Je vais vous montrer comment commencer à écrire une extension Chrome en utilisant ReactJS et Parcel à partir de zéro. Je vais supposer que vous avez des connaissances de base en JavaScript.

> **Note :** Si vous ne voulez pas lire cet article et que vous voulez simplement commencer à coder, vous pouvez trouver le dépôt Git à la fin.

#### Le Scénario

Nous devons rendre notre application sur le site web visité lorsque l'utilisateur clique sur le bouton de rendu de l'élément dans la popup.

Alors, commençons.

### À quoi ressemblera notre projet

![Image](https://cdn-media-1.freecodecamp.org/images/1*QnRGBL1cXupOHMcs9j-8jA.png)
*Une version terminée d'un projet*

```
├── icon.png
├── manifest.json
├── node_modules
├── .babelrc
├── package.json
└── src
    ├── build 
    │   └── main.js [Nous utiliserons ce fichier de build comme script de contenu]
    ├── js [Où notre fichier de développement est stocké]
    │   ├── components [Nous stockons les composants dans ce dossier]
    │   │   └── Header.js
    │   ├── main.js [Notre fichier principal, qui rend notre application]
    │   └── popup.js [Notre fichier JavaScript pour la popup]
    └── popup.html [Notre fichier HTML pour rendre la popup après avoir cliqué sur l'icône dans la barre]
```

### Étape 1 : Création des fichiers du projet

Tout d'abord, créez `manifest.json`, car nous avons besoin de ce fichier pour fournir des informations sur notre extension Chrome.

Chaque extension a un fichier manifest au format **JSON**, nommé `manifest.json`, qui fournit des informations importantes comme le nom, la version et les permissions.

Et voici à quoi il ressemble :

```json
{
  "manifest_version": 2,

  "name": "Nom de votre extension Chrome",
  "description": "Description de votre extension Chrome.",
  "version": "1.0",

  "browser_action": {
    "default_icon": "icon.png",
    "default_popup": "src/popup.html"
  },

  "permissions": [
    "activeTab",
    "tabs"
  ],

  "content_scripts": [
    {
      "matches": ["http://*/*", "https://*/*"],
      "js": ["src/build/main.js"]
    }
  ]
}
```

Après avoir créé le fichier manifest, nous devons configurer notre environnement et la structure du projet.

Commençons à créer la structure de notre projet — alors ouvrez votre terminal et suivez mes étapes !

#### Étape 2 : Création de package.json

Comme vous pouvez le voir, il y a deux scripts `build` et `watch`

* La commande `watch` surveille votre `main.js` et compile s'il y a eu un changement ou si des dépendances sont importées depuis `main.js`.
* La commande `build` construit vos fichiers dans le fichier `src/build/main.js`.

```json
{
  "name": "nom-de-extension",
  "version": "0.1.0",
  "description": "Description",
  "main": "src/js/main.js",
  "scripts": {
    "build": "parcel build src/js/main.js -d src/build/ -o main.js",
    "watch": "parcel watch src/js/main.js -d src/build/ -o main.js"
  },
  "author": "Atakan Goktepe",
  "dependencies": {
    "babel-preset-env": "^1.6.1",
    "babel-preset-react": "^6.24.1",
    "parcel-bundler": "^1.6.2",
    "react": "^16.2.0",
    "react-dom": "^16.2.0"
  }
}
```

#### Étape 3 : Création des fichiers et dossiers

* Créez un dossier source

```
mkdir src
```

* Créez un dossier components dans le dossier `src`

```
mkdir src/js/components
```

* Créez les fichiers `main.js`, `popup.js` et `popup.html`

```
touch src/js/main.js src/js/popup.js src/popup.html
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fw0Q_Psa48utH2QyuMyTvA.png)
*Structure du projet*

#### Étape 4 : Écriture de la Popup

![Image](https://cdn-media-1.freecodecamp.org/images/1*to2qoGcoYAra7-NP7cG-Tw.png)
*Popup*

La popup apparaît en haut de la barre dans Chrome lorsque l'utilisateur clique sur l'icône de l'extension.

L'application React sera rendue dans le contenu lorsqu'un message `startApp` provient de la popup. La popup partagera un message `startApp` avec l'application.

Modifiez votre fichier `popup.html` avec le HTML suivant :

```html
<!doctype html>
<!--
 Cette page est affichée lorsque le bouton de l'extension est cliqué, car le
 champ "browser_action" dans manifest.json contient la clé "default_popup" avec
 la valeur "popup.html".
 -->
<html>
  <head>
    <title>Popup de l'extension Getting Started</title>
    <style type="text/css">
      body {
        margin: 10px;
        white-space: nowrap;
      }

      #container {
        align-items: center;
        display: flex;
        justify-content: space-between;
      }

      .start {
        border: 1px solid #000;
        border-radius: 15px;
        padding: 5px 15px;
        cursor: pointer;
      }
    </style>

    <script src="js/popup.js"></script>
  </head>

  <body>
    <div id="container">
     <!--
      Rendre l'application React dans le site web visité lorsque le bouton .start est cliqué.
     -->
      <button class="start">
        Rendre l'application
      </button>
    </div>
  </body>
</html>
```

Il y a un bouton dans la popup qui envoie un message à notre fichier `main.js` lorsque l'utilisateur clique dessus.

Et modifiez votre fichier `popup.js` avec ce qui suit :

```js
window.onload = () => {
  const $startButton = document.querySelector('.start');

  $startButton.onclick = () => {
    // Obtenir l'onglet actif
    chrome.tabs.query({
      active: true,
      currentWindow: true,
    }, (tabs) => {
      // Envoyer un message au fichier de script
      chrome.tabs.sendMessage(
        tabs[0].id,
        { injectApp: true },
        response => window.close()
      );
    });
  };
}
```

La méthode `chrome.tabs.sendMessage` partage le message avec un écouteur. Notre écouteur fonctionne dans le `main.js`.

#### Étape 5 : Rendu de l'application React

À ce stade, `main.js` doit écouter les messages provenant de `popup.js`.

Nous pouvons écouter les messages avec la méthode `chrome.runtime.onMessage.addListener`. Et voici à quoi ressemble notre fichier `main.js` :

```jsx
import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  render() {
    return (
      <div> Votre application a été injectée dans le DOM avec succès ! </div>
    )
  }
}

// Fonction d'écoute des messages
chrome.runtime.onMessage.addListener((request, sender, response) => {
  // Si le message est injectApp
  if(request.injectApp) {
    // Injecter notre application dans le DOM et envoyer une réponse
    injectApp();
    response({
      startedExtension: true,
    });
  }
});

function injectApp() {
  const newDiv = document.createElement("div");
  newDiv.setAttribute("id", "chromeExtensionReactApp");
  document.body.appendChild(newDiv);
  ReactDOM.render(<App />, newDiv);
}
```

#### Examinons ce que nous avons fait dans `main.js` :

1. Importé les bibliothèques React et ReactDOM.
2. Créé une classe App pour rendre un élément React.
3. Ajouté une fonction d'écoute d'événement pour écouter les messages provenant de `popup.js`.
4. Créé une fonction `injectApp` qui a créé une div et l'a injectée dans le body. Nous avons rendu notre composant `<App />` à l'intérieur.

### Test

Pour tester votre extension :

* Si vous n'avez pas construit vos fichiers, construisez-les en exécutant la commande `npm run build`.
* Allez sur "chrome://extensions".
* Activez le bouton "Mode Développeur".
* Cliquez sur le bouton "Charger l'extension non empaquetée", puis sélectionnez votre dossier de projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FbvvIlSBVLPVpJo5GkwrSQ.png)

Et voilà ! Vous avez créé une extension pour Google Chrome. Vous êtes génial !

![Image](https://cdn-media-1.freecodecamp.org/images/1*C-HOj6XRiQ7eolnH8YjTGA.png)
*Votre extension rendue !*

Ouvrez vos outils de développement et regardez à la fin du body — votre élément a été rendu avec succès !

### Code Source

Voici le dépôt final :

[**atakangktepe/react-parcel-extension-boilerplate**](https://github.com/atakangktepe/react-parcel-extension-boilerplate)  
[_react-parcel-extension-boilerplate - Un modèle d'extension Chrome construit avec ReactJS et Parcel (rend dans le contenu..._github.com](https://github.com/atakangktepe/react-parcel-extension-boilerplate)

### Terminé !

Merci d'avoir lu ce tutoriel. C'était mon premier article en anglais ! Si cela vous a été utile, veuillez le recommander en cliquant sur le bouton d'applaudissements ? ou (encore mieux) partagez-le. ??

Suivez-moi sur [Twitter](https://twitter.com/GoktepeAtakan) et [Github](https://github.com/atakangktepe) !
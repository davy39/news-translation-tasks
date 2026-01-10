---
title: Comment gérer les permissions d'entrée microphone et la reconnaissance vocale
  dans les extensions Chrome
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T13:00:42.000Z'
originalURL: https://freecodecamp.org/news/handling-mic-input-permissions-and-speech-recognition-in-chrome-extensions-ff7e3ca84cb0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kCWG1pjJyxUfKwblYn1gKA.jpeg
tags:
- name: Google Chrome
  slug: chrome
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment gérer les permissions d'entrée microphone et la reconnaissance
  vocale dans les extensions Chrome
seo_desc: 'By Palash Taneja

  This tutorial assumes that you have a basic understanding of Chrome extensions and
  the associated configuration files. If not, then you can refer to this article which
  sets up the files for this tutorial.

  Setting up microphone record...'
---

Par Palash Taneja

Ce tutoriel suppose que vous avez une compréhension de base des extensions Chrome et des fichiers de configuration associés. Si ce n'est pas le cas, vous pouvez vous référer à [cet article](https://medium.freecodecamp.org/how-to-create-a-chrome-extension-part-1-ad2a3a77541) qui configure les fichiers pour ce tutoriel.

La configuration des permissions d'enregistrement microphone dans une extension Chrome est une zone grise. Il n'existe aucune méthode officiellement documentée pour le faire, et les développeurs sont forcés d'utiliser un "hack" pour obtenir les permissions microphone pour leur extension Chrome.

Dans cet article court, nous utilisons la page `options.html` pour obtenir les permissions microphone et utilisons la bibliothèque populaire `[annyang.js](https://github.com/TalAter/annyang)` pour détecter la parole de l'utilisateur.

### 1. Création d'un script et d'une page de déclenchement des permissions

Pour contourner les restrictions de Chrome, nous utilisons une page web de notre extension comme `options.html` et `popup.html` pour obtenir les permissions microphone pour toute l'extension.

Tout d'abord, nous devons créer un fichier JavaScript pour obtenir les permissions microphone sur une page web. J'ai créé un fichier minimal qui demande la permission d'utiliser le microphone à Chrome.

```js
$(document).ready(function(){
    navigator.mediaDevices.getUserMedia({audio: true})
});
```

Si vous n'êtes pas un fan de l'utilisation de JQuery, vous pouvez intégrer ce code JS à la fin du fichier HTML que vous prévoyez d'utiliser comme déclencheur de permission.

Pour notre extension, TalkToMe, nous avons utilisé `options.html` comme notre page de déclenchement de permission.

### 2. Ouverture automatique de la page de déclenchement

La fenêtre contextuelle de permission microphone ne sera ouverte que si la page de déclenchement a été ouverte dans la session actuelle du navigateur. Faire ouvrir manuellement cette page par l'utilisateur à chaque fois est une mauvaise expérience utilisateur. Nous avons créé un script d'arrière-plan pour contourner cela.

```js
setTimeout(() => {
    navigator.mediaDevices.getUserMedia({ audio: true })
    .catch(function() {
        chrome.tabs.create({
            url: chrome.extension.getURL("options.html"),
            selected: true
        })
    });
}, 100);
```

Il essaie d'accéder au microphone toutes les 100 ms, et ouvre la page de déclenchement de permission si la demande est refusée par Chrome.

Pour que le script fonctionne, vous devez l'ajouter à votre `manifest.json` avec d'autres scripts d'arrière-plan.

```js
... 

"background": {
    "scripts": [
      ..
      "js/auto-trigger.js", // ajoutez le script ici
      ..
    ],
    "persistent": false
  },

...
```

### 3. Intégration d'Annyang pour la reconnaissance vocale

Annyang fournit une bibliothèque polyvalente pour la reconnaissance vocale, et elle est 100% gratuite à utiliser.

Elle fonctionne sur une structure basée sur les commandes, en ce sens qu'elle appelle des fonctions basées sur la parole de l'utilisateur. Cette fonctionnalité en a fait un choix parfait pour TalkToMe.

Vous pouvez ajouter le code `annyang.js` à un script d'arrière-plan et commencer à l'utiliser. Ici, je vous montre l'exemple Hello World des documents.

```js
if (annyang) {
  // Définissons une commande.
  var commands = {
    'hello': function() { alert('Hello world!'); }
  };

  // Ajoutons nos commandes à annyang
  annyang.addCommands(commands);

  // Commencez à écouter.
  annyang.start();
}
```

Et voilà, juste comme ça, vous avez répliqué nos heures de recherche sur StackOverflow pour ajouter des permissions microphone à votre extension Chrome.

Si ce tutoriel vous a aidé, nous serions ravis si vous pouviez donner votre avis sur notre extension [TalkToMe](https://chrome.google.com/webstore/detail/talktome/nefaaifpggpfdjlfhfbcgfcjimlgpocc), même si vous n'êtes peut-être pas un utilisateur malvoyant.
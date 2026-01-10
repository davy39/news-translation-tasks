---
title: Comment voir l'état et les props de React dans le navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T21:40:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-see-your-react-state-props-in-the-browser-774098a50fcc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QeEbGcmtoQ3T_zUdpG8TZw.jpeg
tags:
- name: Google Chrome
  slug: chrome
- name: coding
  slug: coding
- name: Firefox
  slug: firefox
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
seo_title: Comment voir l'état et les props de React dans le navigateur
seo_desc: 'By Andrew Bales

  If you’re building a web app with React, you may want to see the state or props
  of components in real-time. Here’s a quick solution for Chrome & FireFox!

  React Developer Tools

  Install the React Developer Tools extension for Chrome or ...'
---

Par Andrew Bales

Si vous construisez une application web avec React, vous pourriez vouloir voir l'état ou les props des composants en temps réel. Voici une solution rapide pour Chrome et FireFox !

### Outils de développement React

Installez l'extension React Developer Tools pour [Chrome](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) ou [FireFox](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/). Elle vous permet d'inspecter les hiérarchies des composants React dans les outils de développement — de la même manière que vous examineriez les éléments du DOM, la console ou le réseau.

### Inspection des composants React

1. Ouvrez votre application et inspectez la page avec les outils de développement (Command+Option+I).
2. Sélectionnez les React Developer Tools

![Image](https://cdn-media-1.freecodecamp.org/images/nRV4nSI2fdxIBQyhGSDu69Vz83ruxGJHk3tL)

3. Choisissez un composant dans l'arborescence pour voir son état et ses props actuels.

![Image](https://cdn-media-1.freecodecamp.org/images/Wo9vvCc3YMSTCGv2R55u87Ttgi8mLdGdBR1E)

Vous pouvez également sélectionner un élément React directement depuis la page en le survolant avec l'outil de sélection :

![Image](https://cdn-media-1.freecodecamp.org/images/-uN55RQ0UWYdHrjJ0quyPHmAEY5dlpumQlzF)
_Icône du menu de l'outil de sélection dans les outils de développement_

### Modification de l'état

Si vous souhaitez mettre à jour votre état dans le navigateur, vous pouvez le faire ! Modifiez-le en cliquant et en éditant les attributs d'état dans l'onglet React. Cela va ré-afficher le DOM, en transmettant l'état à travers les props.

Bon codage ! ?
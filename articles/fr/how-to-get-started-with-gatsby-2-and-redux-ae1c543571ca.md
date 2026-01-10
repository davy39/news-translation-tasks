---
title: Comment commencer avec Gatsby 2 et Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T22:38:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-gatsby-2-and-redux-ae1c543571ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KSVHAT4_AtBt2UpjrJNMBg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment commencer avec Gatsby 2 et Redux
seo_desc: 'By Carl-Johan Kihl

  Gatsby + Redux is a powerful combination when building static web-apps with dynamic
  features. With Gatsby 2, it has never been easier to get up and running. Today,
  I’m going to guide you through the steps needed.

  Not a big fan of r...'
---

Par Carl-Johan Kihl

Gatsby + Redux est une combinaison puissante pour construire des applications web statiques avec des fonctionnalités dynamiques. Avec Gatsby 2, il n'a jamais été aussi facile de se lancer. Aujourd'hui, je vais vous guider à travers les étapes nécessaires.

Pas fan de lecture ? ? Rendez-vous directement sur le starter Redux : 
[https://github.com/caki0915/gatsby-redux-test/](https://github.com/caki0915/gatsby-redux-test/) 
or utilisez le CLI de Gatsby :

```bash
npx gatsby new gatsby-redux-test https://github.com/caki0915/gatsby-redux-test/
```

### Qu'est-ce que Gatsby ?

Gatsby est l'un des générateurs de sites statiques les plus populaires. Préconfiguré avec Webpack, React et GraphQL, il vous donne un excellent point de départ pour construire des applications web. Il dispose également d'un écosystème riche en plugins qui facilite la connexion à une variété de sources de données. [En savoir plus sur Gatsby sur leur site web.](https://www.gatsbyjs.org/)

### Qu'est-ce que Redux ?

Redux est un conteneur d'état souvent utilisé avec les applications React. Cet article suppose que vous savez déjà comment fonctionne Redux. Si vous êtes nouveau dans Redux ou avez besoin d'un rappel, vous [trouverez plus d'informations sur leur site web](https://redux.js.org/).

**? C'est parti ! ?**

Commencez par créer un nouveau projet Gatsby. Dans le terminal, exécutez : *(Remplacez **gatsby-redux-test** par un nom de votre choix)*

```bash
npx gatsby new gatsby-redux-test && cd gatsby-redux-test
```

L'étape suivante consiste à installer les packages `redux` et `react-redux` depuis NPM.

```bash
npm install --save redux react-redux
```

![Image](https://cdn-media-1.freecodecamp.org/images/tDGPhNznARAWd8r52f0WYn-dzo4iMfHY1rAH)
_Packages Redux et React-redux installés_

Ok, super, ajoutons un état !

Créez un nouveau dossier appelé `state` à l'intérieur de votre dossier `src` et créez un fichier `app.js`. Pour les besoins de ce tutoriel, nous allons ajouter une fonctionnalité simple qui vous permet de basculer une variable « **darkMode** » on et off.

Tout d'abord, ajoutez l'état initial :

```js
const initialState = {
  isDarkMode: false,
};
```

Ajoutez le créateur d'action (pour basculer **darkMode** on et off) :

```js
const TOGGLE_DARKMODE = 'TOGGLE_DARKMODE';

export const toggleDarkMode = isDarkMode => ({
  type: TOGGLE_DARKMODE, isDarkMode
});
```

Ajoutez le réducteur :

```js
export default (state = initialState, action) => {
  switch (action.type) {
    case TOGGLE_DARKMODE:
      return { ...state, isDarkMode: action.isDarkMode };
    default:
      return state;
  }
};
```

![Image](https://cdn-media-1.freecodecamp.org/images/WXaLfdUTvndbGMYRSdXsItbuMssFsHBvLEgW)
_État initial, créateur d'action et réducteur_

Ok, super ! Maintenant, ajoutons le réducteur racine. Créez un nouveau fichier `index.js` à l'intérieur du dossier `state`.

```js
import { combineReducers } from 'redux';
import app from './app';

export default combineReducers({ app });
```

![Image](https://cdn-media-1.freecodecamp.org/images/SygFdoV3ZU0bJVAdkc7TCNS1xOgq94R1njfn)
_Notre réducteur racine._

Maintenant, nous allons créer un Store et un Provider. Créez un nouveau fichier `ReduxWrapper.js` dans le dossier `state`. Ce composant va envelopper notre composant racine dans Gatsby.

```js
import React from 'react';
import { Provider } from 'react-redux';
import { createStore as reduxCreateStore } from 'redux';
import rootReducer from '.';

const createStore = () => reduxCreateStore(rootReducer);

export default ({ element }) => (
  <Provider store={createStore()}>{element}</Provider>
);
```

![Image](https://cdn-media-1.freecodecamp.org/images/dBEjRTDy9TrJl2GQxhNHBM6KGLVO0YlIwACe)
_Créer un Store et un Provider_

Gatsby va rendre notre application à la fois sur le serveur et dans le navigateur, et heureusement pour nous, Gatsby dispose d'une API très flexible qui nous permet de nous brancher sur le rendu. ? Nous pouvons implémenter les hooks depuis deux fichiers : `gatsby-browser.js` et `gatsby-ssr.js`.

Le hook qui nous intéresse s'appelle **wrapRootElement** et vous permet d'envelopper votre application avec un élément personnalisé. Exactement ce dont nous avons besoin pour notre Provider Redux. ? Vous pouvez en savoir plus sur **wrapRootElement** dans la [documentation](https://www.gatsbyjs.org/docs/browser-apis/#wrapRootElement).

Puisque nous voulons exporter notre **ReduxWrapper** en tant que **wrapRootElement** depuis `gatsby-browser.js` et `gatsby-ssr.js`, ajoutez cette ligne aux deux fichiers :

```js
export { default as wrapRootElement } from './src/state/ReduxWrapper';
```

![Image](https://cdn-media-1.freecodecamp.org/images/s6o3N7q-NrniTa6CrgQoDP9gLM7bV7wT0Zzg)
_Exporter notre ReduxWrapper depuis gatsby-ssr.js et gatsby-browser.js_

Ok, c'est fait. Gatsby et Redux fonctionnent maintenant ensemble ! ? Maintenant, nous avons seulement besoin d'un moyen de le tester.

Choisissons la méthode la plus simple à laquelle je peux penser : un bouton sur la page d'accueil où l'on peut basculer **darkMode** on et off. Lorsque **darkMode** est activé, le bouton sera sombre avec du texte blanc.

![Image](https://cdn-media-1.freecodecamp.org/images/svVswSsAToLN9w9eeilVcaH8nRNP2Upc36ZL)
_Un test simple pour voir que Redux fonctionne réellement._

Dans le terminal, exécutez :

```bash
npm run develop
```

Et… voyez le thème sombre en action !

![Image](https://cdn-media-1.freecodecamp.org/images/DV4uT4GsHpfTkRhlqJ-FnCmG05W9GircsXf8)
_Exemple minimal de Redux_

Ok, peut-être que ce n'était pas si impressionnant, mais l'exemple fait son travail et je suis sûr que vous trouverez une bien meilleure application pour Redux dans votre application Gatsby. ?

### Résumé

Gatsby + Redux est une combinaison puissante si vous souhaitez construire des applications web statiques avec des fonctionnalités dynamiques. [Je l'utilise pour mes projets](https://carljohan.me) également. Si vous trouvez cet article utile, veuillez ajouter un commentaire et un lien vers votre application Gatsby/Redux géniale. ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1VoLeHHA0WEqGAO4k-Dsgkm71UG0K9zVZW-4)
_[https://carljohan.me](https://carljohan.me" rel="noopener" target="_blank" title=") - Un tiroir est un bon cas d'utilisation pour Redux_
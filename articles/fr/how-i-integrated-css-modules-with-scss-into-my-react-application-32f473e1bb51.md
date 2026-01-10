---
title: Comment j'ai intégré CSS Modules avec SCSS dans mon application React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-23T11:52:30.000Z'
originalURL: https://freecodecamp.org/news/how-i-integrated-css-modules-with-scss-into-my-react-application-32f473e1bb51
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jszn_9GOtyFLexwyKFcQrw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment j'ai intégré CSS Modules avec SCSS dans mon application React
seo_desc: 'By Max Goh

  I recently started on an Isomorphic React project. I wanted to use this opportunity
  to utilize tools that were on my “potential to use” list, and CSS Modules was one
  of them.

  Take a look at this image, do you notice something different?


  F...'
---

Par Max Goh

J'ai récemment commencé un projet React Isomorphique. Je voulais utiliser cette opportunité pour utiliser des outils qui étaient sur ma liste de "potentiels à utiliser", et [CSS Modules](https://github.com/css-modules/css-modules) en faisait partie.

Jetez un œil à cette image, remarquez-vous quelque chose de différent ?

![Image](https://www.freecodecamp.org/news/content/images/2024/02/facebook-console-snippet.jpeg)
_Extrait de la console du site web de Facebook_

Les noms de classe ressemblent à un hachage aléatoire illisible. C'est à cela que ressemblent les CSS Modules en production. Ils permettent d'avoir des noms de classe uniques, évitant les conflits entre les noms de classe courants dans votre application.

Voici un exemple de l'utilisation d'un module CSS :

```sass
/** App.scss */
.app {
  background: red;
}
/** App.jsx */
import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import styles from './App.scss'
class App extends Component {
  render() {
    return (
      <div className={styles.app}>Hello App!</div>
    )
  }
}

```

## Pourquoi CSS Modules avec SCSS

CSS Modules permettent d'avoir un style modulaire dans vos composants. Cela signifie plus de conflits de noms de classe dans votre application. Pendant ce temps, SCSS est un pré-processeur CSS qui offre des fonctionnalités telles que les mixins, les variables globales, la nesting, etc.

## Intégration avec SCSS

En tant qu'utilisateur de SCSS moi-même, je voulais combiner la puissance de CSS Modules et de SCSS dans mon application. Après de nombreuses recherches sur Google, il semblait qu'il n'y avait pas beaucoup de ressources pour intégrer SCSS et CSS Modules.

Facebook a ajouté la prise en charge de CSS Modules dans Create React App v2.

Êtes-vous intéressé à découvrir comment utiliser les modules CSS avec SCSS dans votre propre projet ? Alors, commençons !

## Mise en route

J'utiliserai le kit de démarrage [create-react-app](https://github.com/facebook/create-react-app) de Facebook comme base du projet.

```bash
# Installation du package create-react-app dans votre système
$ npm install --global create-react-app

# Création du projet
$ create-react-app scss-module-react

# Changement de répertoire vers l'application
$ cd ./scss-module-react

```

Comme nous devons apporter des modifications à la configuration de [webpack](https://webpack.js.org/), nous devons éjecter de la configuration par défaut fournie par Create React App.

```bash
$ yarn eject  # Cette commande éjecte votre application des configurations par défaut, vous permettant d'accéder aux scripts et configurations de webpack.

$ yarn add -D sass-loader node-sass

```

### Implémentation

Maintenant que nous avons configuré notre application racine, nous pouvons commencer à modifier les configurations de webpack fournies. Après avoir éjecté, vous remarquerez que vous avez accès à un nouveau dossier nommé `config`. C'est là que sont stockées les configurations de webpack de l'application.

### Développement

Nous pouvons commencer par modifier l'environnement de développement.

```js
/** webpack.config.dev.js */
// Ajoutez ce snippet après la ligne 12

const CSSModuleLoader = {
  loader: 'css-loader',
  options: {
    modules: true,
    sourceMap: true,
    localIdentName: '[local]__[hash:base64:5]',
    minimize: true
  }
}

const CSSLoader = {
  loader: 'css-loader',
  options: {
    modules: false,
    sourceMap: true,
    minimize: true
  }
}

const postCSSLoader = {
  loader: 'postcss-loader',
  options: {
    ident: 'postcss',
    sourceMap: true,
    plugins: () => [
      autoprefixer({
        browsers: ['>1%', 'last 4 versions', 'Firefox ESR', 'not ie < 9']
      })
    ]
  }
}
Ajoutez ceci après la ligne 180
{
  test: /\.scss$/,
  exclude: /\.module\.scss$/,
  use: ['style-loader', CSSLoader, postCSSLoader, 'sass-loader']
},
{
  test: /\.module\.scss$/,
  use: [
    'style-loader',
    CSSModuleLoader,
    postCSSLoader,
    'sass-loader',
  ]
},
    
```

Ce que nous faisons ici, c'est configurer webpack pour lire et importer à la fois les fichiers `.scss` et `.module.scss`.

Cela nous permet d'utiliser à la fois `import styles from './app.module.scss'` et `import './app.scss'` dans notre application.

De plus, `localIndentName` nous permet de configurer comment les noms de classe SCSS compilés seront formatés. Par exemple, un élément dont le nom de classe est `button` sera alors compilé en `button__1mDap`, ce qui suit la structure que nous avons fournie à `localIndentName`.

### Production

La configuration pour la production serait similaire, sauf que nous ne voulons probablement pas afficher les noms de classe locaux, mais seulement les hachages. Nous pouvons apporter les mêmes modifications dans `webpack.config.prod.js`, avec juste une petite différence pour utiliser `localIdentName: '[hash:base64:5]'`.

### C'est tout !

Maintenant que notre configuration et notre application sont prêtes, essayez de créer quelques fichiers SCSS de test et donnez-leur un essai. Vous pouvez exécuter l'application CRA avec ces commandes :

```bash
$ yarn add -g serve
$ serve -s build

```

# Conclusion

Avec les modules CSS, vous êtes maintenant en mesure d'isoler le style pour chaque composant unique, rendant ainsi chaque composant absolument modulaire.

Trouvez le code dans le dépôt GitHub [ici](https://github.com/MaxGoh/scss-module-create-react-app).

**Merci d'avoir lu, les commentaires sont les bienvenus !**

**Je parle principalement de technologie et de programmation. N'hésitez pas à visiter mon site web à l'adresse [maxgoh.xyz](https://maxgoh.xyz/).**

**Si l'occasion se présente, j'adorerais interagir avec les lecteurs. Vous pouvez me suivre sur [Twitter](https://twitter.com/maxgoh222) ou [LinkedIn](https://www.linkedin.com/in/maxgohjh/).**
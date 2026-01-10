---
title: 'Introduction à Webpack : qu''est-ce que c''est et comment l''utiliser'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-15T17:37:32.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-webpack-what-it-is-and-how-to-use-it-8304ecdc3c60
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6ItHoU8x6M-m7-Pt2UG7cw.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: 'Introduction à Webpack : qu''est-ce que c''est et comment l''utiliser'
seo_desc: 'By Ashish Nandan Singh

  Introduction

  Okay, so I assume you have heard of webpack — that’s why you are here, right? The
  real question is what do you know about it? You might know a few things about it,
  like how it works, or you might have absolutely no...'
---

Par Ashish Nandan Singh

### Introduction

D'accord, je suppose que vous avez entendu parler de webpack — c'est pourquoi vous êtes ici, n'est-ce pas ? La vraie question est : que savez-vous à ce sujet ? Vous connaissez peut-être quelques choses, comme son fonctionnement, ou vous n'en avez peut-être aucune idée. Dans les deux cas, je peux vous assurer qu'après avoir lu cet article, vous vous sentirez probablement à l'aise avec toute cette **situation webpack**.

Après tout — **la nécessité** est la mère de **l'invention…**

Une façon parfaite de dire pourquoi webpack existe est la citation ci-dessus. Mais pour mieux la comprendre, nous devons remonter le temps, à l'époque où JavaScript n'était pas la nouvelle chose à la mode, à ces âges anciens où un site web n'était qu'un petit ensemble de bon vieux fichiers _._html, CSS, et probablement un ou quelques fichiers JavaScript dans certains cas. Mais très bientôt, tout cela allait changer.

#### Quel était le problème ?

Toute la communauté des développeurs était impliquée dans une quête constante d'amélioration de l'expérience globale des utilisateurs et des développeurs autour de l'utilisation et de la construction d'applications javascript/web. Par conséquent, nous avons vu l'introduction de nombreuses nouvelles **bibliothèques et frameworks**.

Quelques **design patterns** ont également évolué au fil du temps pour donner aux développeurs un moyen meilleur, plus puissant et pourtant très simple d'écrire des applications JavaScript complexes. Les sites web n'étaient plus qu'un petit package avec un nombre impair de fichiers. Ils ont commencé à devenir volumineux, avec l'introduction des **modules JavaScript**, car écrire des petits morceaux de code encapsulés était la nouvelle tendance. Finalement, tout cela a conduit à une situation où nous avions 4x ou 5x plus de fichiers dans le package global de l'application.

**Non seulement la taille globale de l'application était un défi**, mais il y avait aussi un énorme fossé entre le type de code que les développeurs écrivaient et le type de code que les navigateurs pouvaient comprendre. Les développeurs devaient utiliser beaucoup de code d'assistance appelé **polyfills** pour s'assurer que les navigateurs pouvaient interpréter le code dans leurs packages.

Pour répondre à ces problèmes, webpack a été créé. **Webpack est un bundler de modules statique.**

#### Comment Webpack était-il la réponse ?

En bref, Webpack parcourt votre package et crée ce qu'il appelle un **graphe de dépendances** qui se compose de divers **modules** dont votre application web aurait besoin pour fonctionner comme prévu. Ensuite, en fonction de ce graphe, il crée un nouveau package qui se compose du nombre minimal de fichiers requis, souvent juste un seul fichier bundle.js qui peut être facilement intégré au fichier html et utilisé pour l'application.

Dans la prochaine partie de cet article, je vais vous guider à travers la configuration étape par étape de webpack. À la fin, j'espère que vous comprendrez les bases de Webpack. Alors, commençons…

### Que construisons-nous ?

Vous avez probablement entendu parler de **ReactJS**. Si vous connaissez ReactJS, vous savez probablement ce qu'est **create-react-app**. Pour ceux d'entre vous qui ne savent pas ce que sont ces deux choses, **ReactJS est une bibliothèque UI** qui est très utile pour construire des interfaces utilisateur intelligentes et complexes, et **create-react-app est un outil CLI** pour configurer ou démarrer une configuration de développement boilerplate pour créer des applications React.

Aujourd'hui, nous allons créer une simple application React mais sans utiliser l'outil CLI create-react-app. J'espère que cela vous semble assez amusant. :)

### Phase d'installation

#### npm init

C'est exact, c'est ainsi que commencent presque toutes les bonnes choses : le bon vieux npm init. J'utiliserai VS Code, mais n'hésitez pas à utiliser l'éditeur de code que vous préférez pour commencer.

Avant de pouvoir faire quoi que ce soit, assurez-vous d'avoir les dernières versions de [nodeJS](https://nodejs.org/en/download/) et de [npm](https://www.npmjs.com/get-npm) installées localement sur votre machine. Cliquez sur chacun de ces liens pour en savoir plus sur le processus.

```
$ npm init
```

Cela créera un package de démarrage et ajoutera un fichier package.json pour nous. C'est ici que toutes les dépendances nécessaires à la construction de cette application seront mentionnées.

Maintenant, pour créer une simple application React, nous avons besoin de deux bibliothèques principales : React et ReactDOM. Ajoutons-les donc comme dépendances à notre application en utilisant npm.

```
$ npm i react react-dom --save
```

Ensuite, nous devons ajouter webpack, afin de pouvoir bundler notre application ensemble. Non seulement bundler, mais nous aurons également besoin du rechargement à chaud, ce qui est possible en utilisant le serveur de développement webpack.

```
$ npm i webpack webpack-dev-server webpack-cli --save-dev
```

Le `--save-dev` est utilisé pour spécifier que ces modules sont simplement des dépendances de développement. Maintenant, puisque nous travaillons avec React, nous devons garder à l'esprit que React utilise des classes ES6 et des instructions d'importation, quelque chose que tous les navigateurs ne peuvent pas comprendre. Pour s'assurer que le code est lisible par tous les navigateurs, nous avons besoin d'un outil comme babel pour transpiler notre code en code normal lisible par les navigateurs.

```
$ npm i babel-core babel-loader @babel/preset-react @babel/preset-env html-webpack-plugin --save-dev
```

Eh bien, que puis-je dire, c'était le nombre maximum d'installations que je promets. Dans le cas de babel, nous avons d'abord chargé la bibliothèque principale de babel, puis le chargeur, et enfin 2 plugins ou presets pour travailler spécifiquement avec React et tout le code ES2015 et ES6.

Passons à autre chose, ajoutons un peu de code et commençons la configuration de webpack.

Voici à quoi devrait ressembler le fichier package.json après toutes les installations jusqu'à présent. Vous pourriez avoir un numéro de version différent selon le moment où vous suivez cet article.

### Le Code

Commençons par ajouter un fichier **webpack.config.js** à la racine de notre structure d'application. Ajoutez le code suivant dans votre fichier webpack.config.

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  // Cette propriété définit où l'application commence
  entry:'./src/index.js',
  
  // Cette propriété définit le chemin du fichier et le nom du fichier qui sera utilisé pour déployer le fichier bundlé
  output:{
    path: path.join(__dirname, '/dist'),
    filename: 'bundle.js'
  },
  
  // Configuration des loaders
  module: {
    rules: [
      {
        test: /\.js$/, 
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  
  // Configuration du plugin pour utiliser un fichier HTML pour servir les fichiers js bundlés
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html'
    })
  ]
}
```

D'accord, essayons de comprendre les lignes ci-dessus.

Tout d'abord, nous commençons par nécessiter le module de chemin par défaut pour accéder à l'emplacement du fichier et apporter des modifications à l'emplacement du fichier.

Ensuite, nous nécessitons le HTMLWebpackPlugin pour générer un fichier HTML à utiliser pour servir le ou les fichiers JavaScript bundlés. En savoir plus sur [HTMLWebpackPlugin](https://github.com/jantimon/html-webpack-plugin) en cliquant sur le lien.

Ensuite, nous avons l'objet export.module avec certaines propriétés. La première est la **propriété entry**, qui est utilisée pour spécifier quel fichier webpack doit utiliser pour créer le graphe de dépendances interne.

```js
module.exports = {
  entry:'./src/index.js'
}
```

Ensuite, nous avons la propriété output qui spécifie où le fichier bundlé doit être généré et quel sera le nom du fichier bundlé. Cela est fait par les propriétés **output.path** et **output.filename**.

```js
module.exports = {
  // Cette propriété définit le chemin du fichier et le nom du fichier qui sera utilisé pour déployer le fichier bundlé
  output:{
    path: path.join(__dirname, '/dist'),
    filename: 'bundle.js'
  },
}
```

Ensuite, nous avons les loaders. Cela permet de spécifier ce que webpack doit faire pour un type de fichier spécifique. Rappelez-vous que webpack, par défaut, ne comprend que JavaScript et JSON, mais si votre projet utilise un autre langage, ce serait l'endroit pour spécifier quoi faire avec ce nouveau langage.

```js
module.exports = {
  // Configuration des loaders
  module: {
    rules: [
      {
        test: /\.js$/, 
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  }
}
```

Les informations doivent être spécifiées dans un objet pour chaque propriété de module, qui contient un tableau de règles. Il y aura un objet pour chaque cas. J'ai également spécifié d'exclure tout ce qui se trouve dans mon dossier node_modules.

Ensuite, nous avons la propriété plugin. Cela est utilisé pour étendre les capacités de webpack. Avant qu'un plugin puisse être utilisé dans le tableau de plugins à l'intérieur de l'objet module exports, nous devons le nécessiter.

```js
module.exports = {
  // Configuration du plugin pour utiliser un fichier HTML pour servir les fichiers js bundlés
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html'
    })
  ]
}
```

Ce plugin particulier, comme expliqué précédemment, utilisera le fichier spécifié dans notre dossier src. Il l'utilisera ensuite comme modèle pour notre fichier HTML où tous les fichiers bundlés seront automatiquement injectés. Il existe de nombreux autres plugins prêts à l'emploi que nous pourrions utiliser — consultez la [page officielle](https://webpack.js.org/plugins/) pour plus d'informations.

La dernière chose que nous devons faire est de créer un fichier .babelrc pour utiliser le preset babel que nous avons installé et prendre en charge les classes ES6 et les instructions d'importation dans notre code. Ajoutez les lignes de code suivantes au fichier .babelrc.

```
{
  "presets": ["env", "react"]
}
```

Et juste comme ça, maintenant babel pourra utiliser ces presets. D'accord, assez de configuration — ajoutons un peu de code React pour voir comment cela fonctionne.

### Code React

Puisque le point de départ de l'application est le fichier index.js dans le dossier src, commençons par celui-ci. Nous allons commencer par nécessiter à la fois **React** et **ReactDOM** pour notre utilisation dans ce cas. Ajoutez le code ci-dessous dans votre fichier index.js.

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './Components/App';

ReactDOM.render(<App />, document.getElementById('app'));
```

Nous importons simplement un autre fichier de notre dossier components, que vous créerez, et ajoutons un autre fichier dans le dossier appelé App.js. Alors, voyons ce qu'il y a dans le fichier App.js :

```jsx
import React, { Component } from 'react'

class App extends Component {
  render() {
    return (
      <div>
        <h1>Configuration Webpack + React</h1>
      </div>
    )
  }
}

export default App;
```

Nous avons presque terminé. La seule chose qui reste maintenant est d'activer le rechargement à chaud. Cela signifie que chaque fois qu'un changement est détecté, le navigateur recharge automatiquement la page et a la capacité de construire et de bundler l'ensemble de l'application lorsque le moment est venu.

Nous pouvons faire cela en ajoutant des valeurs de script dans le fichier package.json. Supprimez la propriété test dans l'objet scripts de votre fichier package.json et ajoutez ces deux scripts :

```json
"start": "webpack-dev-server --mode development --open --hot",
"build": "webpack --mode production"
```

Vous êtes prêt ! Allez dans votre terminal, naviguez jusqu'au dossier racine et exécutez **npm start**. Cela devrait démarrer un serveur de développement sur votre ordinateur et servir le fichier HTML dans votre navigateur. Si vous apportez des modifications mineures/majeures et enregistrez le code, votre navigateur sera automatiquement actualisé pour afficher le dernier ensemble de modifications.

Une fois que vous pensez être prêt à bundler l'application, vous devez simplement exécuter la commande **npm build**, et webpack créera un bundle optimisé dans votre dossier de projet qui peut être déployé sur n'importe quel serveur web.

### Conclusion

Ce n'est qu'une petite application ou un cas d'utilisation de webpack et babel, mais les applications sont illimitées. J'espère que vous êtes assez excité pour explorer plus d'options et de façons de faire des choses avec webpack et babel. Veuillez vous référer à leurs sites officiels pour en savoir plus et lire en profondeur.

J'ai créé un dépôt Github avec tout le code, alors n'hésitez pas à vous y référer en cas de questions.

[**ashishcodes4/webpack-react-setup**](https://github.com/ashishcodes4/webpack-react-setup)
[_Création d'une application React à partir de zéro sans utiliser le CLI - ashishcodes4/webpack-react-setup_github.com](https://github.com/ashishcodes4/webpack-react-setup)

Mon avis sur webpack ? Eh bien, parfois vous pourriez penser que ce n'est rien de plus qu'un outil, et pourquoi devriez-vous vous soucier autant d'un outil ? Mais croyez-moi quand je dis cela : la lutte initiale lors de l'apprentissage de webpack vous fera économiser un nombre énorme d'heures que vous auriez autrement investi dans le développement sans webpack.

C'est tout pour l'instant, j'espère revenir avec un autre article intéressant très bientôt. J'espère que vous avez apprécié la lecture de celui-ci !

En cas de difficulté ou de problème lors du suivi de l'une des étapes/processus mentionnés ci-dessus, n'hésitez pas à nous contacter et à laisser des commentaires.

LinkedIn : [https://www.linkedin.com/in/ashish-nandan-singh-490987130/](https://www.linkedin.com/in/ashish-nandan-singh-490987130/)

Twitter : [https://twitter.com/ashishnandansin](https://twitter.com/ashishnandansin)
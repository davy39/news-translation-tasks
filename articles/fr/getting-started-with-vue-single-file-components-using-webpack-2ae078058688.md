---
title: Comment commencer avec les composants Vue en fichier unique en utilisant Webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T20:07:17.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-vue-single-file-components-using-webpack-2ae078058688
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tag8gBfSQ9I4dxLJOAg3QQ@2x.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: webpack
  slug: webpack
seo_title: Comment commencer avec les composants Vue en fichier unique en utilisant
  Webpack
seo_desc: 'By Dushyant Sabharwal

  This guide assumes that you have some idea about vue. It aims to save you time,
  trying to help you understand the webpack config for starting with vue and its single
  file components. You can use vue-cli for creating the project ...'
---

Par Dushyant Sabharwal

_Ce guide suppose que vous avez une certaine idée de `vue`. Il vise à vous faire gagner du temps, en essayant de vous aider à comprendre la configuration `webpack` pour commencer avec `vue` et ses composants en fichier unique. Vous pouvez utiliser `vue-cli` pour créer le modèle de projet, mais ceci est pour les personnes qui veulent approfondir._

Vous êtes probablement un développeur qui connaît le front-end. Vous avez décidé de faire passer votre application au niveau supérieur en adoptant `vue` comme framework front-end. Vous plongez dans la documentation et commencez à lire comment développer des composants, tout en établissant des parallèles dans votre tête avec des cas d'utilisation pour le premier composant de votre projet. Le framework et la documentation s'avèrent excellents et vous ne pouvez pas attendre pour commencer à utiliser `vue`.

Si cela vous semble familier, alors c'est génial !

TL;DR vous pouvez cloner ou forker le dépôt [ici](https://github.com/dushyant89/vue-webpack) et commencer.

### Commençons

Notre objectif est d'écrire notre premier composant, mais **pas de la manière dont c'est fait ci-dessous**. Bien qu'il n'y ait rien de mal à charger le fichier de script de cette manière, cela devient plus compliqué lorsque vous finissez par charger plusieurs fichiers de script de cette façon.

Nous utiliserons `[webpack](https://webpack.js.org/configuration/devtool/)` pour bundler notre application. Si vous n'avez pas encore regardé `webpack`, alors c'est le moment de configurer votre première application. Cela peut sembler intimidant au début, mais la dernière version (v4) est super facile et intuitive à utiliser.

### Installation des packages

Pour en arriver là, installons quelques packages de base dont nous aurons besoin. Nous utiliserons `npm` pour gérer les packages. Si vous n'êtes pas à l'aise avec `npm`, ne vous inquiétez pas ! Suivez simplement les instructions. Assurez-vous d'avoir installé `node` et `npm` sur votre machine.

**Note** : Si vous avez le temps, alors [lisez ceci](https://hackernoon.com/things-which-every-developer-should-know-when-starting-with-modern-front-end-development-7030486bf092) pour comprendre comment npm fonctionne et ce que cela signifie pour la sécurité de votre application.

Continuons...

```
npm install vue
```

```
npm install webpack --save-dev
```

Puisque nous écrirons notre code en `ES6` et au-delà, nous avons besoin de quelque chose pour transpiler ou transformer notre code. Nous utiliserons `babel` avec `webpack` pour nous aider à produire une version du code qui s'exécutera dans les navigateurs qui ne supportent pas encore la spécification complète de `ES6`.

[Cet](https://www.fullstackreact.com/articles/what-are-babel-plugins-and-presets/) article donne un bon aperçu de babel, et expliquera en détail pourquoi nous avons besoin des packages ci-dessous.

```
npm install babel-core --save-dev
```

```
npm install babel-loader --save-dev
```

```
npm install babel-preset-env --save-dev
```

```
npm install babel-preset-stage-2 --save-dev
```

Votre `package.json` devrait ressembler à ceci. Vos versions peuvent être différentes lorsque vous installez les packages ci-dessous, ce qui est normal tant que l'application ne se casse pas.

Si vous souhaitez installer les versions spécifiques comme vous le voyez ci-dessus, alors faites simplement

```
npm install webpack-cli@^3.0.2 --save-dev
```

Maintenant que notre ensemble d'outils de base est configuré, concentrons notre attention sur l'idée de la manière dont nous allons écrire la partie `template` ou `html` de notre premier composant. Sera-t-elle dans un fichier `.html` séparé ? Ou inclura-t-elle un fichier existant comme `index.html` ? Ou sera-t-elle dans une `string` qui est ensuite compilée en utilisant une bibliothèque ? J'ai déjà suivi ce train de pensée.

`Vue` résout ce problème en fournissant un moyen d'écrire des composants où vous pouvez associer la partie `template` et la partie `script` du composant dans un seul fichier. N'est-ce pas génial ?

Par exemple, si vous construisez un simple composant `table`, alors vous pouvez nommer le fichier `table.vue` qui contient tout ce dont le composant a besoin. Et si je vous disais que vous pouvez avoir des `styles` également dans le même fichier `.vue` qui sont spécifiques à ce composant ? Je sais ! Cela semble fou !

Installons les packages ci-dessous pour que nous puissions avoir des composants en fichier unique, ou `SFCs` :

```
npm install vue-template-compiler --save-dev
```

```
npm install vue-loader --save-dev
```

```
npm install css-loader --save-dev
```

```
npm install vue-style-loader --save-dev
```

`vue-template-compiler` est utilisé pour comprendre la section `template` du composant.

`vue-loader` permet à `webpack` de charger des composants en fichier unique.

`css-loader` et `vue-style-loader` nous permettent d'écrire des styles dans le composant.

Votre `package.json` devrait maintenant ressembler à ceci :

### Webpack

Maintenant que nous avons tous les packages dont nous avons besoin dans notre arsenal, tout ce dont nous avons besoin est un moyen d'instruire `webpack`. Si vous essayez de comprendre `webpack` et son fonctionnement, il est préférable de comprendre l'intuition de pourquoi cet outil existe en premier lieu. Peu importe si nous utilisons `webpack` ou non, nous avons simplement besoin d'un outil qui peut faire des choses comme :

* Traiter les points d'entrée dans notre application pour démarrer le processus
* Nommer les fichiers de sortie/traités et spécifier leur emplacement
* Traiter différents types de fichiers comme `.css`, `.js` ou `.vue`
* Recharger à chaud les fichiers modifiés afin de reconstruire le tout

Webpack fait toutes ces choses (et bien plus) si vous spécifiez simplement ce qui doit être fait via un objet de configuration.

Nous utiliserons `webpack-dev-server` pour servir les actifs statiques et dynamiques dans notre projet, parce que pourquoi pas.

### Examiner le code

Clonons ou forkons (si vous voulez améliorer) [ce projet](https://github.com/dushyant89/vue-webpack).

Vous verrez que le projet a le même `package.json` que mentionné ci-dessus. Installons et exécutons le projet en suivant les instructions du dépôt.

`index.html` contient notre premier composant appelé `main-content` :

```
<div id="mainContent">    <main-content></main-content></div>
```

Notre `main-content.vue`, qui est un `SFC`, ressemble à ceci. Comme vous pouvez le voir, il a trois sections : `template`, `script` et `style`. Tout est lié à notre composant de manière ordonnée et `webpack` s'occupe du reste.

Rendez-vous sur [http://localhost:8010/](http://localhost:8010/) dans votre navigateur et vous remarquerez notre composant `main-content`. Changez quelque chose dans le composant comme ci-dessous :

```
<template>    <div class="main-content">        <h1> C'est mon premier composant modifié dans Vue </h1>        <h3> {{ webpack }} </h3>    </div></template>
```

et remarquez comment le titre change dans le navigateur. Pour comprendre comment cela fonctionne, jetez un œil à `webpack.config.js`. Chaque section de la configuration contient des commentaires expliquant pourquoi nous en avons besoin.

Divisons la configuration `webpack` en trois parties principales.

#### **L'entrée/sortie de Webpack**

#### **Traitement des composants Vue en fichier unique et autres modules JS**

#### **Configuration du serveur de développement Webpack**

Chacune des options dans la configuration est assez explicite, et vous pouvez les ajuster pour mieux les comprendre. Par exemple, vous pouvez supprimer l'une des propriétés et remarquer les erreurs.

**Note** : chaque fois que vous modifiez la configuration, vous devez arrêter (cmd + C) et exécuter `npm run start` pour que les changements soient pris en compte.

Vous pouvez ajouter plus d'options à l'application en lisant la [documentation](https://webpack.js.org/configuration/devtool/), et n'hésitez pas à forker le [projet](https://github.com/dushyant89/vue-webpack) pour des améliorations.

Si vous pensez que cet article vous a aidé, alors vous pouvez [m'offrir un café](https://www.buymeacoffee.com/dushyant) ou simplement le partager avec d'autres. Santé ?

[**Offrez un café à Dushyant Sabharwal - BuyMeACoffee.com**](https://www.buymeacoffee.com/dushyant)  
[_Je suis un développeur full stack qui aime écrire des choses qui peuvent aider d'autres développeurs à gagner du temps_www.buymeacoffee.com](https://www.buymeacoffee.com/dushyant)
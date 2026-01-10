---
title: Apprendre à utiliser le CLI de Vue.js
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-06-07T17:57:40.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-use-the-vue-js-cli-8349fb23a566
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tAKfoNTaWdTFxxFgOlXHfg.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Apprendre à utiliser le CLI de Vue.js
seo_desc: 'Interested in learning Vue.js? Get my ebook at vuehandbook.com


  One of them is the Vue Command Line Interface (CLI).

  Note: There is a huge rework of the CLI going on right now, going from version 2
  to 3. While not yet stable, I will describe version ...'
---

> Intéressé par l'apprentissage de Vue.js ? Obtenez mon ebook sur [vuehandbook.com](https://vuehandbook.com)

L'un d'eux est l'interface en ligne de commande (CLI) de Vue.

**Note : Il y a une refonte majeure du CLI en cours, passant de la version 2 à la version 3. Bien que pas encore stable, je vais décrire la version 3 car c'est une énorme amélioration par rapport à la version 2, et assez différente.**

### Installation

Le CLI de Vue est un utilitaire en ligne de commande, et vous l'installez globalement en utilisant npm :

```
npm install -g @vue/cli
```

ou en utilisant yarn :

```
yarn global add @vue/cli
```

Une fois cela fait, vous pouvez invoquer la commande `vue`.

![Image](https://cdn-media-1.freecodecamp.org/images/Ezi3VXVa2p5CpgoyCZCa75QNoW-MTTI7m5G6)

### Que fournit le CLI de Vue ?

Le CLI est essentiel pour le développement rapide avec Vue.js.

Son objectif principal est de s'assurer que tous les outils dont vous avez besoin fonctionnent ensemble, pour effectuer ce dont vous avez besoin. Il abstrait tous les détails de configuration fastidieux que l'utilisation de chaque outil isolément nécessiterait.

Il peut effectuer une configuration initiale de projet et un échafaudage.

C'est un outil flexible. Une fois que vous avez créé un projet avec le CLI, vous pouvez aller modifier la configuration, sans avoir à **éjecter** votre application (comme vous le feriez avec `create-react-app`). Vous pouvez configurer n'importe quoi et toujours être en mesure de mettre à jour facilement.

Après avoir créé et configuré l'application, il agit comme un outil de dépendance d'exécution, construit sur webpack.

La première rencontre avec le CLI est lors de la création d'un nouveau projet Vue.

### Comment utiliser le CLI pour créer un nouveau projet Vue

La première chose que vous allez faire avec le CLI est de créer une application Vue :

```
vue create example
```

Le truc cool, c'est que c'est un processus interactif. Vous devez choisir un preset. Par défaut, il y a un preset qui fournit l'intégration de Babel et ESLint :

![Image](https://cdn-media-1.freecodecamp.org/images/mJgJ2biDiceJFpTng3CCs0KLestOD0OkIdK3)

Je vais appuyer sur la flèche vers le bas ↓️ et choisir manuellement les fonctionnalités que je veux :

![Image](https://cdn-media-1.freecodecamp.org/images/VHH9GRYaGmHXrK-R14mSeabWaTfziYHV3u1T)

Appuyez sur `espace` pour chaque fonctionnalité dont vous avez besoin, puis appuyez sur `entrée` pour continuer. Comme j'ai choisi « Linter/Formatter », Vue CLI me demande la configuration. J'ai choisi « ESLint + Prettier » car c'est ma configuration préférée :

![Image](https://cdn-media-1.freecodecamp.org/images/xlJKu3wPlvEbvaUMYYNw324pye5TTNlBot9S)

L'étape suivante consiste à choisir comment appliquer le linting. J'ai choisi « Lint on save ».

![Image](https://cdn-media-1.freecodecamp.org/images/4piDaNMeerzha0yl8EHNTl5fTEV8M8OXLaeZ)

Ensuite : les tests. J'ai choisi les tests, et Vue CLI me propose les deux solutions les plus populaires : « Mocha + Chai » vs « Jest ».

![Image](https://cdn-media-1.freecodecamp.org/images/HdNBSsWDIFdwx74QuBsMdT3tDN3LdGXXBJqG)

Vue CLI me demande où mettre toute la configuration. Les choix sont dans le fichier « package.json », ou dans des fichiers de configuration dédiés, un pour chaque outil. J'ai choisi ce dernier.

![Image](https://cdn-media-1.freecodecamp.org/images/5Ksk5IoNHC5ojo5PgGw5llQIjuCr784BJQBD)

Ensuite, Vue CLI me demande si je veux sauvegarder ces presets, et me permet de les choisir comme option la prochaine fois que j'utilise Vue CLI pour créer une nouvelle application. C'est une fonctionnalité très pratique. Avoir une configuration rapide avec toutes mes préférences est un soulagement de complexité :

![Image](https://cdn-media-1.freecodecamp.org/images/Ltghrk2SQRhcEbstlnXkMh1R-mgzrsAnHSki)

Vue CLI me demande ensuite si je préfère utiliser yarn ou npm :

![Image](https://cdn-media-1.freecodecamp.org/images/6sqjc-L31QY39KzP6ap1iCWGTTkRX1YeqMd6)

et c'est la dernière chose qu'il me demande. Il télécharge ensuite les dépendances et crée l'application Vue :

![Image](https://cdn-media-1.freecodecamp.org/images/zr1V90so3ThCT2YS3MillgY7d2aXxkXzTuNe)

### Comment démarrer la nouvelle application Vue CLI

Vue CLI a créé l'application pour nous, et nous pouvons aller dans le dossier « example » et exécuter `yarn serve` pour démarrer notre première application en mode développement :

![Image](https://cdn-media-1.freecodecamp.org/images/my8YXCSW3AQxC80gMSi2TW6HSI7Pee6zf0gF)

L'application exemple de démarrage contient quelques fichiers, y compris « package.json » :

![Image](https://cdn-media-1.freecodecamp.org/images/vYdRUaFtp8mqXnNdmxTDFi5SijA769JwVvjo)

C'est là que toutes les commandes CLI sont définies, y compris `yarn serve`, que nous avons utilisé il y a une minute. Les autres commandes sont

* `yarn build`, pour démarrer une construction de production
* `yarn lint`, pour exécuter le linter
* `yarn test:unit`, pour exécuter les tests unitaires

Je décrirai l'application exemple générée par Vue CLI dans un tutoriel séparé.

### Dépôt Git

Remarquez le mot `master` dans le coin inférieur gauche de VS Code ? C'est parce que Vue CLI crée automatiquement un dépôt, et fait un premier commit. Nous pouvons nous lancer, changer des choses, et nous savons ce que nous avons changé :

![Image](https://cdn-media-1.freecodecamp.org/images/CZ1J7IPrBEr2TZ3BzOe33lANVrbu43xDy1mB)

C'est assez cool. Combien de fois vous plongez-vous et changez-vous des choses pour réaliser, lorsque vous voulez commiter le résultat, que vous n'avez pas commité l'état initial ?

### Utiliser un preset depuis la ligne de commande

Vous pouvez sauter le panneau interactif et instruire Vue CLI d'utiliser un preset particulier :

```
vue create -p favourite example-2
```

### Où les presets sont stockés

Les presets sont stockés dans le fichier « .vuejs » dans votre répertoire personnel. Voici le mien après avoir créé le premier preset « favourite » :

```
{  "useTaobaoRegistry": false,  "packageManager": "yarn",  "presets": {    "favourite": {      "useConfigFiles": true,      "plugins": {        "@vue/cli-plugin-babel": {},        "@vue/cli-plugin-eslint": {          "config": "prettier",          "lintOn": [            "save"          ]        },        "@vue/cli-plugin-unit-jest": {}      },      "router": true,      "vuex": true    }  }}
```

### Plugins

Comme vous pouvez le voir en lisant la configuration, un preset est essentiellement une collection de plugins, avec une configuration optionnelle.

Une fois un projet créé, vous pouvez ajouter plus de plugins en utilisant `vue add` :

```
vue add @vue/cli-plugin-babel
```

Tous ces plugins sont utilisés à la dernière version disponible. Vous pouvez forcer Vue CLI à utiliser une version spécifique en passant la propriété de version :

```
"@vue/cli-plugin-eslint": {  "version": "^3.0.0"}
```

Cela est utile si une nouvelle version a des changements majeurs ou un bug, et que vous devez attendre un peu avant de l'utiliser.

### Stocker les presets à distance

Un preset peut être stocké dans GitHub (ou sur d'autres services) en créant un dépôt qui contient un fichier « preset.json », qui contient une seule configuration de preset.

Extrait de ce qui précède, j'ai fait un preset exemple dans [https://github.com/flaviocopes/vue-cli-preset/blob/master/preset.json](https://github.com/flaviocopes/vue-cli-preset/blob/master/preset.json) qui contient cette configuration :

```
{  "useConfigFiles": true,  "plugins": {    "@vue/cli-plugin-babel": {},    "@vue/cli-plugin-eslint": {      "config": "prettier",      "lintOn": [        "save"      ]    },    "@vue/cli-plugin-unit-jest": {}  },  "router": true,  "vuex": true}
```

Il peut être utilisé pour démarrer une nouvelle application en utilisant :

```
vue create --preset flaviocopes/vue-cli-preset example3
```

### Une autre utilisation du Vue CLI : le prototypage rapide

Jusqu'à présent, j'ai expliqué comment utiliser le Vue CLI pour créer un nouveau projet à partir de zéro, avec tous les éléments nécessaires. Mais pour un prototypage vraiment rapide, vous pouvez créer une application Vue très simple — une qui est auto-contenue dans un seul fichier .vue — et la servir, sans avoir à télécharger toutes les dépendances dans le dossier `node_modules`.

Comment ? Tout d'abord, installez le package global `cli-service-global` :

```
npm install -g @vue/cli-service-global 
```

```
//ou yarn 
```

```
global add @vue/cli-service-global
```

Créez un fichier « app.vue » :

```
<template>    <div>        <h2>Bonjour le monde !</h2>        <marquee>Heyyy</marquee>    </div></template>
```

et ensuite exécutez

```
vue serve app.vue
```

![Image](https://cdn-media-1.freecodecamp.org/images/LVFDuVO3plJc0u2w0GQ0F0PCMDrhvVZumQ9K)

Vous pouvez servir des projets plus organisés, composés de fichiers JavaScript et HTML également. Vue CLI utilise par défaut « main.js » / « index.js » comme point d'entrée. Vous pouvez avoir un « package.json » et toute configuration d'outil mise en place. `vue serve` la prendra en compte.

Puisque cela utilise des dépendances globales, ce n'est pas une approche optimale pour autre chose que la démonstration ou les tests rapides.

L'exécution de la commande `vue build` préparera le projet pour le déploiement, et générera les fichiers JavaScript résultants dans le dossier `dist/`, de sorte qu'il sera prêt pour la production. Tous les avertissements que Vue.js génère pendant le développement sont supprimés, et le code est optimisé pour une utilisation réelle.

### Webpack

En interne, Vue CLI utilise Webpack, mais la configuration est abstraite et nous ne voyons même pas le fichier de configuration dans notre dossier. Vous pouvez toujours y accéder en appelant `vue inspect` :

![Image](https://cdn-media-1.freecodecamp.org/images/0LXsf4FKpRzswYbuxqSdCtKhPzOeKXgW-XnQ)

> Intéressé par l'apprentissage de Vue.js ? Obtenez mon ebook sur [vuehandbook.com](https://vuehandbook.com)

![Image](https://cdn-media-1.freecodecamp.org/images/yptuVaTEKOeOJ7ChmJnzYc1lKq9LjqeewymF)
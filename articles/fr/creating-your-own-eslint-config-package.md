---
title: Comment créer votre propre package de configuration ESLint
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-17T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/creating-your-own-eslint-config-package
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/susan-holt-simpson-2nSdQEd-Exc-unsplash.jpg
tags:
- name: eslint
  slug: eslint
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
seo_title: Comment créer votre propre package de configuration ESLint
seo_desc: "By Leonardo Faria\nESLint is a powerful tool that helps you enforce consistent\
  \ coding conventions and ensure quality in your JavaScript codebase. \nCoding conventions\
  \ are sometimes difficult to decide on, and having a tool that automates their enforcem..."
---

Par Leonardo Faria

ESLint est un outil puissant qui vous aide à appliquer des conventions de codage cohérentes et à garantir la qualité de votre base de code JavaScript. 

Les conventions de codage sont parfois difficiles à décider, et avoir un outil qui automatise leur application aide à éviter des discussions inutiles. Garantir la qualité est également une fonctionnalité bienvenue : les linters sont d'excellents outils pour détecter les bugs, tels que ceux liés à la portée des variables.

ESLint est conçu pour être complètement configurable, vous donnant l'option d'activer/désactiver chaque règle, ou de mélanger les règles pour correspondre à vos besoins. 

Avec cela à l'esprit, la communauté JavaScript et les entreprises qui utilisent JavaScript peuvent étendre la configuration originale d'ESLint. Il y a [plusieurs exemples](https://www.npmjs.com/search?q=eslint-config) dans le registre npm : [eslint-config-airbnb](https://www.npmjs.com/package/eslint-config-airbnb) est l'un des plus connus.

Dans votre routine quotidienne, vous combinerez probablement plus d'une configuration, car il n'y a pas de configuration universelle. Cet article montrera comment créer votre propre dépôt de configurations, vous donnant l'option de centraliser toutes vos définitions de règles.

## Créer le projet

Tout d'abord, vous devrez créer un nouveau dossier et un projet npm. [Par convention](https://eslint.org/docs/developer-guide/shareable-configs), le nom du module commence par `eslint-config-`, comme `eslint-config-test`.

```bash
mkdir eslint-config-test
cd eslint-config-test
npm init

```

Vous aurez un fichier package.json qui ressemblera au snippet suivant :

```json
{
  "name": "eslint-config-test",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}

```

Ensuite, il est temps d'ajouter vos dépendances ESLint :

```bash
npm install -D eslint eslint-config-airbnb eslint-config-prettier eslint-plugin-import eslint-plugin-jsx eslint-plugin-prettier eslint-plugin-react eslint-plugin-react-hooks prettier

```

Les packages changeront selon vos besoins. Dans ce cas, je travaille avec des bases de code React et j'utilise [Prettier](https://prettier.io/) pour formater mon code. La [documentation](https://eslint.org/docs/developer-guide/shareable-configs#publishing-a-shareable-config) mentionne que si votre configuration partageable dépend d'un plugin, vous devriez également le spécifier comme une `peerDependency`.

Ensuite, je vais créer un `.eslintrc.js` avec ma configuration - cela ressemble à ce que vous faites déjà dans vos applications :

```js
module.exports = {
  extends: [
    'airbnb',
    'eslint:recommended',
    'plugin:import/errors',
    'plugin:react/recommended',
    'plugin:jsx-a11y/recommended',
    'plugin:prettier/recommended',
    'prettier/react',
  ],
  plugins: [
    'react-hooks',
  ],
  rules: {
  },
};

```

L'objet `rules` stocke toute règle que vous souhaitez remplacer. Dans le snippet ci-dessus, `rules` est vide, mais n'hésitez pas à consulter [mes remplacements](https://github.com/leonardofaria/eslint-config-leozera/blob/master/.eslintrc.js#L14:L58). Dans le dépôt Airbnb/JavaScript, vous pouvez [trouver une liste de règles remplacées](https://github.com/airbnb/javascript/issues/1089) par la communauté.

### Créer des règles personnalisées

Il est temps de créer un `.prettierrc` avec vos règles personnalisées - c'est une partie délicate car Prettier et ESLint peuvent entrer en conflit sur quelques règles :

```json
{
  "tabWidth": 2
}

```

Il est important de mentionner que le fichier `.prettierrc` doit se trouver à la racine du projet qui utilise votre package. Pour l'instant, je le copie manuellement. 

L'étape suivante consiste à exporter votre configuration dans le fichier `index.js` :

```js
const eslintrc = require('./.eslintrc.js');

module.exports = eslintrc;

```

Il est techniquement possible de créer toutes les configurations dans le fichier `index.js`. Mais si vous faites cela, vous n'aurez pas l'objet de configuration vérifié (insérez votre blague [Inception](https://www.imdb.com/title/tt1375666/) ici).

### Vous avez terminé !

_Voilà !_ C'est tout ce dont vous avez besoin pour démarrer votre propre package de configurations. Vous pouvez tester localement votre package de configuration en exécutant la commande suivante dans un projet JavaScript :

```bash
npm install /Users/leonardo/path/to/eslint-config-test

```

Gardez à l'esprit que les dépendances de votre package de configuration peuvent également être installées.

Si tout semble correct, vous pouvez publier dans le registre npm :

```bash
npm publish

```

## Exemple complet

J'ai un projet GitHub fonctionnel montrant la configuration de cet article : [eslint-config-leozera](https://github.com/leonardofaria/eslint-config-leozera). Vous pouvez également le voir ci-dessous :

%[https://codesandbox.io/embed/github/leonardofaria/eslint-config-leozera/tree/master/?fontsize=14&theme=dark]

## Plus d'informations sur le projet

* [Configurer ESLint](https://eslint.org/docs/user-guide/configuring) : documentation officielle d'ESLint. Vous savez, _lisez la documentation_
* [Comment publier votre premier package NPM](https://medium.com/@bretcameron/how-to-publish-your-first-npm-package-b224296fc57b) : citant le sous-titre de l'article – "tout ce que vous devez savoir pour créer un package NPM."
* [eslint-config-wesbos](https://github.com/wesbos/eslint-config-wesbos) : un projet de [Wes Bos](https://www.wesbos.com/) qui m'a aidé pendant ce travail

Également publié sur [mon blog](https://bit.ly/2AKW42t). Si vous aimez ce contenu, suivez-moi sur [Twitter](https://twitter.com/leozera) et [GitHub](https://github.com/leonardofaria). Photo de couverture par [Susan Holt Simpson/Unsplash](https://unsplash.com/photos/2nSdQEd-Exc).
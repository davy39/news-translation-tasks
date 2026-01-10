---
title: Introduction à Webpack pour les débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-06-13T18:34:33.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-introduction-to-webpack-2620415e46b3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*iCgamjcfG4fe8Yhr.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: webpack
  slug: webpack
seo_title: Introduction à Webpack pour les débutants
seo_desc: 'Webpack is a tool that lets you compile JavaScript modules. It’s also known
  as a module bundler.

  Given a large number of files, it generates a single file (or a few files) that
  run your app.

  It can perform many operations:


  helps you bundle your reso...'
---

Webpack est un outil qui vous permet de compiler des modules JavaScript. Il est également connu sous le nom de **module bundler**.

Étant donné un grand nombre de fichiers, il génère un seul fichier (ou quelques fichiers) qui exécute votre application.

Il peut effectuer de nombreuses opérations :

* vous aide à regrouper vos ressources.
* surveille les changements et relance les tâches.
* peut exécuter la transpilation Babel vers ES5, vous permettant d'utiliser les dernières fonctionnalités de [JavaScript](https://flaviocopes.com/javascript/) sans vous soucier de la compatibilité avec les navigateurs.
* peut transpiler CoffeeScript en JavaScript
* peut convertir les images en ligne en URI de données.
* vous permet d'utiliser require() pour les fichiers CSS.
* peut exécuter un serveur web de développement.
* peut gérer le remplacement de modules à chaud.
* peut diviser les fichiers de sortie en plusieurs fichiers pour éviter d'avoir un énorme fichier JS à charger lors de la première visite de la page.
* peut effectuer le [tree shaking](https://flaviocopes.com/javascript-glossary/#tree-shaking).

Webpack n'est pas limité à une utilisation front-end, mais est également utile dans le développement backend Node.js.

Il existe de nombreux prédécesseurs de Webpack et de nombreuses similitudes dans ce que ces outils et Webpack font. La principale différence est que ces outils sont connus sous le nom de **task runners**, tandis que Webpack est né en tant que module bundler.

Webpack est un outil plus ciblé. Vous devez simplement spécifier un point d'entrée pour votre application (il peut même s'agir d'un fichier HTML avec des balises script) et Webpack analyse les fichiers et les regroupe dans un seul fichier JavaScript de sortie qui inclut tout ce dont vous avez besoin pour exécuter l'application.

### Installation de Webpack

Webpack peut être installé globalement ou localement pour chaque projet.

### Installation globale

Voici comment l'installer globalement avec [Yarn](https://flaviocopes.com/yarn/) :

```
yarn global add webpack webpack-cli
```

avec [npm](https://flaviocopes.com/npm/) :

```
npm i -g webpack webpack-cli
```

une fois cela fait, vous devriez pouvoir exécuter

```
webpack-cli
```

![Image](https://cdn-media-1.freecodecamp.org/images/D8QBAOc2eqjQsHVi4ieq-pf6wBtZfrhMv5-n)

### Installation locale

Webpack peut également être installé localement. C'est la configuration recommandée, car Webpack peut être mis à jour par projet, et vous avez moins de résistance à utiliser les dernières fonctionnalités pour un petit projet plutôt que de mettre à jour tous les projets que vous avez qui utilisent Webpack.

Avec [Yarn](https://flaviocopes.com/yarn/) :

```
yarn add webpack webpack-cli -D
```

avec [npm](https://flaviocopes.com/npm/) :

```
npm i webpack webpack-cli --save-dev
```

Une fois cela fait, ajoutez ceci à votre fichier `package.json` :

```
{   //...   "scripts": {     "build": "webpack"   } }
```

Une fois cela fait, vous pouvez exécuter Webpack en tapant

```
yarn build
```

dans la racine du projet.

### Configuration de Webpack

Par défaut, Webpack (à partir de la version 4) ne nécessite aucune configuration si vous respectez ces conventions :

* le **point d'entrée** de votre application est `./src/index.js`
* la sortie est placée dans `./dist/main.js`.
* Webpack fonctionne en mode production

Vous pouvez bien sûr personnaliser chaque petit détail de Webpack lorsque vous en avez besoin. La configuration de Webpack est stockée dans le fichier `webpack.config.js`, dans le dossier racine du projet.

### Le point d'entrée

Par défaut, le point d'entrée est `./src/index.js`. Cet exemple simple utilise le fichier `./index.js` comme point de départ :

```
module.exports = {  /*...*/  entry: './index.js'  /*...*/}
```

### La sortie

Par défaut, la sortie est générée dans `./dist/main.js`. Cet exemple place le bundle de sortie dans `app.js` :

```
module.exports = {  /*...*/  output: {    path: path.resolve(__dirname, 'dist'),    filename: 'app.js'  }  /*...*/}
```

L'utilisation de Webpack vous permet d'utiliser des instructions `import` ou `require` dans votre code JavaScript non seulement pour inclure d'autres fichiers JavaScript, mais aussi pour tout type de fichier (par exemple CSS).

Webpack vise à gérer toutes nos dépendances, pas seulement JavaScript, et les loaders sont un moyen de le faire.

Par exemple, dans votre code, vous pouvez utiliser :

```
import 'style.css'
```

en utilisant cette configuration de loader :

```
module.exports = {  /*...*/  module: {    rules: [      { test: /\.css$/, use: 'css-loader' },    ]  }  /*...*/}
```

L'[expression régulière](https://flaviocopes.com/javascript-regular-expressions/) cible tout fichier CSS.

Un loader peut avoir des options :

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.css$/,        use: [          {            loader: 'css-loader',            options: {              modules: true            }          }        ]      }    ]  }  /*...*/}
```

Vous pouvez nécessiter plusieurs loaders pour chaque règle :

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.css$/,        use:          [            'style-loader',            'css-loader',          ]      }    ]  }  /*...*/}
```

Dans cet exemple, `css-loader` interprète la directive `import 'style.css'` dans le CSS. `style-loader` est ensuite responsable de l'injection de ce CSS dans le DOM, en utilisant une balise `<style>`.

L'ordre est important et il est inversé (le dernier est exécuté en premier).

Quels types de loaders existent-ils ? Beaucoup ! [Vous pouvez trouver la liste complète ici](https://webpack.js.org/loaders/).

Un loader couramment utilisé est [Babel](https://flaviocopes.com/babel/), qui est utilisé pour transpiler le JavaScript moderne en code ES5 :

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.js$/,        exclude: /(node_modules|bower_components)/,        use: {          loader: 'babel-loader',          options: {            presets: ['@babel/preset-env']          }        }      }    ]  }  /*...*/}
```

Cet exemple fait en sorte que Babel pré-traite tous nos fichiers React/JSX :

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.(js|jsx)$/,        exclude: /node_modules/,        use: 'babel-loader'      }    ]  },  resolve: {    extensions: [      '.js',      '.jsx'    ]  }  /*...*/}
```

Voir les options de `babel-loader` [ici](https://webpack.js.org/loaders/babel-loader/).

### Plugins

Les plugins sont comme des loaders, mais en plus puissants. Ils peuvent faire des choses que les loaders ne peuvent pas faire, et ils sont les principaux éléments de construction de Webpack.

Prenons cet exemple :

```
module.exports = {  /*...*/  plugins: [    new HTMLWebpackPlugin()  ]  /*...*/}
```

Le plugin `HTMLWebpackPlugin` fait le travail de créer automatiquement un fichier HTML et d'ajouter le chemin du bundle JS de sortie, afin que le JavaScript soit prêt à être servi.

Il existe [beaucoup de plugins disponibles](https://webpack.js.org/plugins/).

Un plugin utile, `CleanWebpackPlugin`, peut être utilisé pour vider le dossier `dist/` avant de créer une sortie, afin que vous ne laissiez pas de fichiers lorsque vous changez les noms des fichiers de sortie :

```
module.exports = {  /*...*/  plugins: [    new CleanWebpackPlugin(['dist']),  ]  /*...*/}
```

### Le mode Webpack

Ce mode (introduit dans Webpack 4) définit l'environnement dans lequel Webpack fonctionne. Il peut être défini sur `development` ou `production` (par défaut en production, vous ne le définissez donc que lorsque vous passez en développement).

```
module.exports = {  entry: './index.js',  mode: 'development',  output: {    path: path.resolve(__dirname, 'dist'),    filename: 'app.js'  }}
```

Mode développement :

* construit très rapidement
* est moins optimisé que la production
* ne supprime pas les commentaires
* fournit des messages d'erreur et des suggestions plus détaillés
* offre une meilleure expérience de débogage

Le mode production est plus lent à construire, car il doit générer un bundle plus optimisé. Le fichier JavaScript résultant est plus petit, car il supprime de nombreuses choses qui ne sont pas nécessaires en production.

J'ai créé une application d'exemple qui imprime simplement une instruction `console.log`.

Voici le bundle de production :

![Image](https://cdn-media-1.freecodecamp.org/images/alm5uVDatSP2YQ6MJ6QcXBIAvq3CQggpEzIs)

Voici le bundle de développement :

![Image](https://cdn-media-1.freecodecamp.org/images/OKvuW1qYszkWflVJPEDXjK8QBuheqi28UpaQ)

### Exécution de Webpack

Webpack peut être exécuté manuellement depuis la ligne de commande s'il est installé globalement. Mais généralement, vous écrivez un script à l'intérieur du fichier `package.json`, qui est ensuite exécuté en utilisant `npm` ou `yarn`.

Par exemple, cette définition de scripts `package.json` que nous avons utilisée précédemment :

```
"scripts": {  "build": "webpack"}
```

nous permet d'exécuter `webpack` en exécutant

```
npm run build
```

ou

```
yarn run build
```

ou simplement

```
yarn build
```

### Surveillance des changements

Webpack peut reconstruire automatiquement le bundle lorsqu'un changement se produit dans votre application, et il continue à écouter le prochain changement.

Il suffit d'ajouter ce script :

```
"scripts": {  "watch": "webpack --watch"}
```

et exécuter

```
npm run watch
```

ou

```
yarn run watch
```

ou simplement

```
yarn watch
```

Une fonctionnalité intéressante du mode watch est que le bundle n'est modifié que si la construction n'a pas d'erreurs. S'il y a des erreurs, `watch` continuera à écouter les changements et tentera de reconstruire le bundle, mais le bundle actuel et fonctionnel n'est pas affecté par ces constructions problématiques.

### Gestion des images

Webpack vous permet d'utiliser des images de manière très pratique, en utilisant le loader `[file-loader](https://webpack.js.org/loaders/file-loader/)`.

Cette configuration simple :

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.(png|svg|jpg|gif)$/,        use: [          'file-loader'        ]      }    ]  }  /*...*/}
```

Vous permet d'importer des images dans votre JavaScript :

```
import Icon from './icon.png'const img = new Image()img.src = Iconelement.appendChild(img)
```

Où `img` est un HTMLImageElement. Consultez la [documentation sur Image](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/Image).

`file-loader` peut également gérer d'autres types d'actifs, comme les polices, les fichiers CSV, XML, et plus encore.

Un autre outil pratique pour travailler avec les images est le loader `url-loader`.

Cet exemple charge tout fichier PNG de moins de 8 Ko sous forme d'[URL de données](https://flaviocopes.com/data-urls/).

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.png$/,        use: [          {            loader: 'url-loader',            options: {              limit: 8192            }          }        ]      }    ]  }  /*...*/}
```

### Traiter votre code SASS et le transformer en CSS

En utilisant `sass-loader`, `css-loader` et `style-loader` :

```
module.exports = {  /*...*/  module: {    rules: [      {        test: /\.scss$/,        use: [          'style-loader',          'css-loader',          'sass-loader'        ]      }    ]  }  /*...*/}
```

### Générer des Source Maps

Puisque Webpack regroupe le code, les Source Maps sont obligatoires pour obtenir une référence au fichier original qui a déclenché une erreur. Par exemple :

Vous dites à Webpack de générer des source maps en utilisant la propriété `devtool` de la configuration :

```
module.exports = {  /*...*/  devtool: 'inline-source-map',  /*...*/}
```

`devtool` a [de nombreuses valeurs possibles](https://webpack.js.org/configuration/devtool/), les plus utilisées sont probablement :

* `none` : n'ajoute pas de source maps
* `source-map` : idéal pour la production, fournit une source map séparée qui peut être minimisée, et ajoute une référence dans le bundle, afin que les outils de développement sachent que la source map est disponible. Bien sûr, vous devez configurer le serveur pour éviter de livrer cela, et l'utiliser uniquement à des fins de débogage
* `inline-source-map` : idéal pour le développement, intègre la source map en tant qu'URL de données

> Je publie 1 tutoriel de programmation gratuit par jour sur [flaviocopes.com](https://flaviocopes.com), allez y faire un tour !

_Originalement publié sur [flaviocopes.com](https://flaviocopes.com/webpack)._
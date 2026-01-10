---
title: Comment créer une configuration Webpack 4 prête pour la production à partir
  de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-29T02:40:01.000Z'
originalURL: https://freecodecamp.org/news/creating-a-production-ready-webpack-4-config-from-scratch
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9beb740569d1a4ca2ec5.jpg
tags:
- name: Bundler
  slug: bundler
- name: dependency management
  slug: dependency-management
- name: Developer Tools
  slug: developer-tools
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: webpack
  slug: webpack
seo_title: Comment créer une configuration Webpack 4 prête pour la production à partir
  de zéro
seo_desc: 'By Tyler Hawkins

  Webpack is a powerful bundler and dependency manager used by many enterprise-level
  companies as tooling for their front-end code.

  Typically, webpack is configured when a project is first set up, and small tweaks
  are then made to the ...'
---

Par Tyler Hawkins

[Webpack](https://webpack.js.org/) est un bundler puissant et un gestionnaire de dépendances utilisé par de nombreuses entreprises de niveau entreprise comme outil pour leur code front-end.

Typiquement, webpack est configuré lorsqu'un projet est initialement mis en place, et de petites modifications sont ensuite apportées aux fichiers de configuration selon les besoins de temps en temps. En raison de cela, de nombreux développeurs n'ont pas beaucoup d'expérience de travail avec webpack.

Dans ce tutoriel pratique, nous allons passer par les bases de la mise en place de votre propre configuration webpack prête pour la production en utilisant webpack 4. Nous discuterons de la gestion des sorties, de la gestion des actifs, des configurations de développement et de production, de Babel, de la minification, du cache busting, et plus encore.

![Webpack bundle votre code](https://www.freecodecamp.org/news/content/images/2020/03/webpack-js-opt.png)
_Webpack bundle votre code_

Commençons !

## Application de démonstration

Pour les besoins de cette démonstration, nous allons configurer une configuration webpack à partir de zéro en utilisant webpack 4. Notre application utilisera simplement du JavaScript vanilla afin de ne pas nous encombrer avec des détails spécifiques à un framework. Le code réel de l'application sera assez petit afin que nous puissions nous concentrer davantage sur webpack.

Si vous souhaitez suivre, tout le code de cet article peut être trouvé sur GitHub. Le [point de départ se trouve ici](https://github.com/thawkin3/webpack-training-1/tree/demo/start), et le [résultat final se trouve ici](https://github.com/thawkin3/webpack-training-1).

## Point de départ

Pour commencer, nous allons commencer avec quelques fichiers dans notre répertoire de projet. La structure du répertoire ressemble à ceci :

```
webpack-demo
 |_ src
    |_ index.js
 |_ .gitignore
 |_ index.html
 |_ package.json
 |_ README.md
 |_ yarn.lock
```

Le fichier `index.html` est simple, juste un en-tête de page et une balise `script` :

```html
<!doctype html>
<html>
  <head>
    <title>Webpack Training 1</title>
  </head>
  <body>
    <h1>Webpack Training 1</h1>
    <script src="./src/index.js"></script>
  </body>
</html>
```

La balise `script` référence notre fichier `./src/index.js`, qui contient quelques lignes de JavaScript qui affichent le texte "Hello from webpack!" :

```javascript
const p = document.createElement('p')
p.textContent = 'Hello from webpack!'
document.body.append(p)
```

Si vous glissez le fichier `index.html` dans votre navigateur, vous devriez pouvoir voir notre simple page web :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-27-at-3.10.23-PM.png)
_Sortie de l'application de démonstration 1 - hello from webpack_

---

## Installer les dépendances

J'ai inclus `webpack` et `webpack-cli` comme `devDependencies` dans le fichier `package.json`.

Pour les installer, exécutez :

```bash
yarn install
```

## Test de Webpack

Webpack 4 est configuré comme un outil "zero config", ce qui signifie que vous pouvez l'exécuter directement sans effectuer de configuration initiale. Maintenant, pour tout projet réel, vous aurez besoin de faire une certaine configuration, mais c'est bien que vous puissiez au moins faire une vérification rapide pour vous assurer que webpack peut fonctionner sans avoir à passer par une série d'étapes de configuration initiale.

Alors, vérifions cela. Exécutez :

```bash
yarn webpack
```

Vous devriez maintenant voir un répertoire `dist` créé dans votre répertoire de projet. Et à l'intérieur, vous devriez voir un fichier `main.js`, qui est notre code minifié.

Super ! Webpack semble fonctionner.

## Référencer le code de sortie

OK, maintenant que nous avons du code JavaScript dans notre répertoire `dist`, faisons en sorte que notre fichier `index.html` référence cela. Au lieu que la balise `script` ressemble à ceci :

```html
<script src="./src/index.js"></script>
```

Changeons-la pour cela :

```html
<script src="./dist/main.js"></script>
```

Maintenant, actualisez la page dans votre navigateur, et vous devriez toujours voir la même sortie exacte, seulement cette fois le texte "Hello from webpack!" est généré par le fichier `./dist/main.js`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-27-at-3.10.23-PM-1.png)
_Sortie de l'application de démonstration 2 - aucun changement_

## Créer un fichier de configuration Webpack

Maintenant que nous avons installé webpack et que nous avons fait un exercice de vérification rapide, créons un vrai fichier de configuration webpack. Créez un fichier appelé `webpack.config.js` et placez le code suivant à l'intérieur :

```javascript
const path = require('path')

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  }
}
```

La propriété `entry` indique à webpack où se trouve notre code source. C'est le "point d'entrée" pour notre application.

La propriété `output` indique à webpack comment appeler le fichier de sortie et dans quel répertoire le placer.

Assez simple, n'est-ce pas ?

Maintenant, créons un script npm dans notre fichier `package.json` :

```json
"scripts": {
  "build": "webpack --config=webpack.config.js"
}
```

Maintenant, nous pouvons exécuter notre processus de construction avec la commande `yarn build`. Allez-y et exécutez cette commande pour vérifier que vous avez tout configuré correctement. Vous pourriez même supprimer votre répertoire `dist` avant d'exécuter la commande `yarn build` pour vérifier que le répertoire est généré.

## Changer le nom du fichier de sortie

Maintenant, juste pour le fun, changeons le nom du fichier de sortie. Pour cela, nous allons ouvrir notre fichier `webpack.config.js` et changer la propriété `output` de ceci :

```javascript
output: {
  filename: 'main.js',
  path: path.resolve(__dirname, 'dist')
}
```

À ceci :

```javascript
output: {
  filename: 'tacos.js',
  path: path.resolve(__dirname, 'dist')
}
```

Maintenant, exécutez `yarn build` à nouveau pour générer la sortie. Vous devriez voir un fichier `tacos.js` dans votre répertoire `dist` maintenant.

Mais attendez ! Nous voyons aussi l'ancien fichier `main.js` dans notre répertoire `dist` ! Ne serait-ce pas bien si webpack pouvait supprimer l'ancienne sortie inutile à chaque fois que nous faisons une nouvelle construction ?

Il doit y avoir un plugin pour cela.

## Plugins Webpack

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-178.png)
_Photo par [Unsplash](https://unsplash.com/@feelfarbig?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Feelfarbig Magazine</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Webpack dispose d'un riche écosystème de modules appelés "[plugins](https://webpack.js.org/concepts/#plugins)", qui sont des bibliothèques pouvant modifier et améliorer le processus de construction de webpack. Nous explorerons une poignée de plugins utiles alors que nous continuons à améliorer notre configuration webpack tout au long du reste de cet article.

## CleanWebpackPlugin

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-179.png)
_Photo par [Unsplash](https://unsplash.com/@honest?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">The Honest Company</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

OK, revenons à notre problème. Ce serait bien si nous pouvions nettoyer le répertoire `dist` avant chaque nouvelle construction. Il y a un plugin pour cela !

Nous pouvons utiliser le [CleanWebpackPlugin](https://github.com/johnagan/clean-webpack-plugin) pour nous aider ici. D'abord, nous devons l'installer dans notre projet :

```bash
yarn add --dev clean-webpack-plugin
```

Pour l'utiliser, nous allons simplement `require` le plugin dans notre fichier `webpack.config.js` et ensuite l'inclure dans le tableau `plugins` dans notre configuration :

```javascript
const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new CleanWebpackPlugin()
  ]
}
```

Maintenant, exécutez `yarn build` à nouveau, et vous devriez voir un seul fichier de sortie dans votre répertoire `dist`. Problème résolu !

## HTMLWebpackPlugin

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-180.png)
_Photo par [Unsplash](https://unsplash.com/@rxspawn?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Florian Olivo</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Une autre chose qui est un peu ennuyeuse avec notre configuration est que chaque fois que nous changeons le nom du fichier `output` dans notre fichier `webpack.config.js`, nous devons également changer ce nom de fichier que nous référençons dans notre balise `script` dans notre fichier `index.html`. Ne serait-ce pas bien si webpack pouvait gérer cela pour nous ?

Il y a un plugin pour cela ! Nous pouvons utiliser le [HTMLWebpackPlugin](https://webpack.js.org/plugins/html-webpack-plugin/) pour nous aider à gérer notre fichier HTML. Installons-le dans notre projet maintenant :

```bash
yarn add --dev html-webpack-plugin
```

Maintenant, déplaçons notre fichier `index.html` à l'intérieur de notre répertoire `src` afin qu'il soit un frère du fichier `index.js`.

```
webpack-demo
 |_ src
    |_ index.html
    |_ index.js
 |_ .gitignore
 |_ package.json
 |_ README.md
 |_ yarn.lock
```

Nous pouvons également supprimer la balise `script` dans notre fichier `index.html` puisque nous allons laisser webpack gérer l'insertion de la balise `script` appropriée pour nous. Supprimez cette ligne afin que votre fichier `index.html` ressemble à ceci :

```html
<!doctype html>
<html>
  <head>
    <title>Webpack Training 1</title>
  </head>
  <body>
    <h1>Webpack Training 1</h1>
  </body>
</html>
```

Maintenant, `require` ce plugin dans notre fichier `webpack.config.js` et ensuite l'inclure dans le tableau `plugins` dans notre configuration, tout comme nous l'avons fait pour le premier plugin :

```javascript
const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      inject: true,
      template: path.resolve(__dirname, 'src', 'index.html'),
    }),
  ]
}
```

Dans ces options pour le `HtmlWebpackPlugin`, nous spécifions le `filename` pour ce que nous aimerions que le fichier de sortie soit appelé.

Nous spécifions pour `inject` que nous aimerions que notre fichier JavaScript soit injecté dans la balise `body` en définissant la valeur sur `true`.

Et enfin, pour le `template`, nous fournissons l'emplacement de notre fichier `index.html` dans le répertoire `src`.

## Vérification de bon sens

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-181.png)
_Photo par [Unsplash](https://unsplash.com/@glenncarstenspeters?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Glenn Carstens-Peters</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

OK, assurons-nous que tout fonctionne toujours correctement. Exécutez `yarn build`, et vérifiez que vous voyez deux fichiers dans votre répertoire `dist` : `index.html` et `main.js`.

Si vous regardez de près dans votre fichier `index.html`, vous verrez le fichier `main.js` référencé.

Maintenant, ouvrez le fichier `./dist/index.html` dans votre navigateur pour vérifier que votre page se charge correctement. Si vous avez suivi ces étapes correctement, votre page devrait toujours fonctionner :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-27-at-3.10.23-PM-2.png)
_Sortie de l'application de démonstration 3 - aucun changement_

## Créer un serveur de développement

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-182.png)
_Photo par [Unsplash](https://unsplash.com/@tvick?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Taylor Vick</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Nous avons fait quelques bonnes améliorations jusqu'à présent en utilisant le `CleanWebpackPlugin` et le `HtmlWebpackPlugin`. Au fur et à mesure que nous avons apporté ces modifications, nous avons dû exécuter manuellement la commande `yarn build` chaque fois pour voir les nouvelles modifications dans notre application. Nous avons également simplement visualisé le fichier dans notre navigateur plutôt que de visualiser le contenu servi par un serveur en cours d'exécution localement. Améliorons notre processus en créant un serveur de développement.

Pour cela, nous allons utiliser `webpack-dev-server`. D'abord, nous devons l'installer :

```bash
yarn add --dev webpack-dev-server
```

Maintenant, divisons notre fichier unique `webpack.config.js` en deux fichiers de configuration séparés, un pour la production et un pour le développement. Nous appellerons le fichier pour la production `webpack.config.prod.js` et le fichier pour le développement `webpack.config.dev.js`.

## Configuration Webpack de développement

Voici notre fichier de configuration de développement :

```javascript
const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  mode: 'development',
  devtool: 'inline-source-map',
  devServer: {
    contentBase: './dist',
  },
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      inject: true,
      template: path.resolve(__dirname, 'src', 'index.html'),
    }),
  ]
}
```

Notez que nous avons spécifié le `mode` comme `development` maintenant, et nous avons spécifié que nous aimerions une `inline-source-map` pour nos fichiers JavaScript, ce qui signifie qu'une source map est incluse à la fin de chaque fichier JavaScript. Pour notre serveur de développement, nous avons spécifié que notre contenu se trouvera dans le répertoire `dist`.

Toute la configuration de développement est restée la même.

## Configuration Webpack de production

Maintenant, voici notre fichier de configuration de production :

```javascript
const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  mode: 'production',
  devtool: 'source-map',
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      inject: true,
      template: path.resolve(__dirname, 'src', 'index.html'),
    }),
  ]
}
```

Ce fichier ressemble également beaucoup à notre fichier de configuration original. Ici, nous avons spécifié que le `mode` est `production` et que nous aimerions l'option `source-map` pour les source maps, qui fournit des fichiers de source map séparés pour le code minifié.

## Scripts NPM de production et de développement

Enfin, ajoutons quelques scripts npm supplémentaires dans notre fichier `package.json` afin que nous puissions travailler avec nos configurations webpack de développement et de production :

```json
"scripts": {
  "build": "webpack --config=webpack.config.prod.js",
  "build-dev": "webpack --config=webpack.config.dev.js",
  "start": "webpack-dev-server --config=webpack.config.dev.js --open"
}
```

Maintenant, essayons chacun de ces scripts.

Exécutez `yarn build` pour voir la sortie de la construction de production. Vous devriez voir que le fichier `main.js` dans votre répertoire `dist` est minifié et qu'il a un fichier de source map `main.js.map` accompagnant.

Maintenant, exécutez `yarn build-dev` pour voir la sortie de la construction de développement. Vous devriez voir le fichier `main.js` dans votre répertoire `dist`, mais notez maintenant qu'il n'est **pas** minifié.

Enfin, exécutez `yarn start` pour démarrer le serveur de développement. Cela ouvrira l'application sur `http://localhost:8080/`. Plus besoin de visualiser les fichiers directement en les glissant simplement dans votre navigateur ! Nous avons maintenant un vrai serveur de développement en direct !

La sortie que vous voyez devrait toujours être la même que d'habitude :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-27-at-3.10.23-PM-3.png)
_Sortie de l'application de démonstration 4 - aucun changement_

## Faire des modifications pendant le développement

Maintenant que nous avons un serveur de développement fonctionnel, expérimentons en apportant quelques modifications simples à notre fichier `./src/index.js`. Au lieu d'afficher "Hello from webpack!", changeons-le pour qu'il dise "Hello from dev server!".

Enregistrez le fichier, puis voyez la page sur votre serveur de développement se recharger et se mettre à jour automatiquement pour vous ! Cela sera un bon coup de pouce à votre productivité de développeur.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-27-at-4.16.13-PM.png)
_Sortie de l'application de démonstration 5 - hello from dev server_

## Ne vous répétez pas (DRY)

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-183.png)
_Photo par [Unsplash](https://unsplash.com/@tobey_j?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Tobias Jelskov</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Maintenant que nous avons deux fichiers de configuration webpack séparés, un pour le développement et un pour la production, vous avez peut-être remarqué que nous avons beaucoup de code dupliqué entre les deux fichiers.

Chaque développeur a eu le principe DRY martelé dans sa tête depuis le premier jour : Ne vous répétez pas. Si vous vous retrouvez à écrire le même code à plusieurs endroits, il peut être bon de transformer cela en code partagé qui peut être écrit en un seul endroit et ensuite utilisé à plusieurs endroits. De cette façon, lorsque vous devez apporter des modifications, vous n'avez besoin de les implémenter qu'à un seul endroit.

Alors, comment pouvons-nous nettoyer la duplication dans nos fichiers de configuration webpack ? Il y a un plugin pour cela !

## WebpackMerge

![Merge](https://www.freecodecamp.org/news/content/images/2020/03/merge.png)
_Merge_

Nous pouvons utiliser le plugin [webpack-merge](https://github.com/survivejs/webpack-merge) pour gérer le code partagé sur lequel plusieurs fichiers de configuration s'appuient. Pour cela, nous allons d'abord installer le package :

```bash
yarn add --dev webpack-merge
```

Maintenant, nous allons créer un troisième fichier de configuration webpack appelé `webpack.config.common.js`. C'est ici que nous garderons notre code partagé. Pour l'instant, nos fichiers de configuration de développement et de production partagent le même point d'entrée, la même sortie et les mêmes plugins. Tout ce qui diffère entre les deux fichiers est le mode, la source map et le serveur de développement.

Ainsi, le contenu de notre fichier `webpack.config.common.js` sera :

```javascript
const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      inject: true,
      template: path.resolve(__dirname, 'src', 'index.html'),
    }),
  ]
}
```

Et maintenant, nous pouvons fusionner cet objet de configuration partagé dans notre configuration de développement comme ceci :

```javascript
const merge = require('webpack-merge')
const commonConfig = require('./webpack.config.common')

module.exports = merge(commonConfig, {
  mode: 'development',
  devtool: 'inline-source-map',
  devServer: {
    contentBase: './dist',
  },
})
```

Et nous pouvons fusionner l'objet de configuration partagé dans notre configuration de production comme ceci :

```javascript
const merge = require('webpack-merge')
const commonConfig = require('./webpack.config.common')

module.exports = merge(commonConfig, {
  mode: 'production',
  devtool: 'source-map',
})
```

Regardez comme ces deux fichiers sont plus courts et plus propres ! Magnifique !

## Styliser notre application

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-184.png)
_Photo par [Unsplash](https://unsplash.com/@madebyvadim?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Vadim Sherbakov</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Les choses se présentent plutôt bien avec nos configurations webpack jusqu'à présent. Nous avons un serveur de développement fonctionnel et nous avons divisé notre code en fichiers de configuration de développement, de production et partagés.

Commençons à travailler sur notre code d'application réel maintenant. La page noire et blanche est un peu ennuyeuse à regarder. Stylisons-la !

Dans notre répertoire `src`, créons un fichier `index.css` et plaçons les lignes de CSS suivantes à l'intérieur :

```css
body {
  background: deeppink;
  color: white;
}
```

Ensuite, dans notre fichier `./src/index.js`, importons ce fichier CSS :

```javascript
import './index.css'
```

Maintenant, exécutez `yarn start` pour relancer notre serveur de développement.

Oh non ! Nous obtenons une erreur !

```
ERROR in ./src/index.css 1:5
Module parse failed: Unexpected token (1:5)
You may need an appropriate loader to handle this file type, currently no loaders are configured to process this file. See https://webpack.js.org/concepts#loaders
> body {
|   background: deeppink;
|   color: white;
 @ ./src/index.js 1:0-20
```

Quels sont ces "loaders" dont il parle ?

## Loaders Webpack

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-185.png)
_Photo par [Unsplash](https://unsplash.com/@kevin_butz?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Kevin Butz</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Plus tôt, nous avons discuté des plugins webpack, qui vous permettent d'étendre le processus de construction de webpack. Il existe également un écosystème de "[loaders](https://webpack.js.org/loaders/)" webpack, qui aident webpack à savoir comment comprendre et charger différents types de fichiers. Par défaut, webpack sait comment gérer nos fichiers JavaScript, mais il ne sait pas encore quoi faire avec les fichiers CSS. Corrigons cela.

## StyleLoader et CSSLoader

Il y a deux loaders en particulier qui seront utiles pour nous ici : [style-loader](https://webpack.js.org/loaders/style-loader/) et [css-loader](https://webpack.js.org/loaders/css-loader/). Incluons-les dans notre projet et discutons ensuite de leur fonctionnement.

Pour commencer, comme toujours, nous devons installer ces deux dépendances :

```bash
yarn add --dev style-loader css-loader
```

Ensuite, nous pouvons les ajouter à notre fichier `webpack.config.common.js` dans la section des règles de module en bas :

```javascript
const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      inject: true,
      template: path.resolve(__dirname, 'src', 'index.html'),
    }),
  ],
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  }
}
```

Cette section configure des règles pour webpack afin qu'il sache quoi faire avec chaque fichier qu'il rencontre. La propriété `test` est une expression régulière que webpack vérifie par rapport au nom du fichier. Dans ce cas, nous voulons gérer les fichiers avec une extension `.css`.

Ensuite, la propriété `use` indique à webpack quel loader ou loaders utiliser pour gérer les fichiers correspondant aux critères. Notez que l'ordre ici est important !

Les loaders webpack sont lus de droite à gauche. Donc, d'abord le `css-loader` sera appliqué, puis le `style-loader` sera appliqué.

Maintenant, que font réellement ces loaders pour nous ?

`css-loader` interprète et résout les fichiers CSS importés que vous référencez dans votre JavaScript. Donc, dans ce cas, `css-loader` aide à faire fonctionner cette ligne :

```javascript
import './index.css'
```

Ensuite, `style-loader` injecte le CSS dans le DOM. Par défaut, `style-loader` prend le CSS qu'il rencontre et l'ajoute au DOM à l'intérieur d'une balise `style`.

Redémarrons notre serveur de développement en tuant le processus actuel (si vous l'avez toujours en cours d'exécution) puis en le redémarrant avec `yarn start`. Maintenant, dans le navigateur web, vous devriez voir ceci sur `https://localhost:8080/` :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-28-at-1.07.03-PM.png)
_Sortie de l'application de démonstration 6 - ajoute des couleurs rose et blanc_

Oooh, si coloré !

## Une note sur les autres loaders Webpack

Nous n'aborderons pas les loaders pour d'autres types de fichiers dans cet article, mais sachez qu'il existe un loader pour tout ce que vous pouvez imaginer ! Vous pouvez utiliser [file-loader](https://webpack.js.org/loaders/file-loader/) ou [url-loader](https://webpack.js.org/loaders/url-loader/) pour charger des images et d'autres actifs. Vous pouvez utiliser [sass-loader](https://webpack.js.org/loaders/sass-loader/) pour gérer la conversion des fichiers Sass/SCSS en CSS avant de transmettre cette sortie à `css-loader` et `style-loader`. Webpack peut également gérer les fichiers Less avec [less-loader](https://webpack.js.org/loaders/less-loader/) si c'est votre préférence.

La morale de l'histoire est : Pour tout type de fichier donné, il existe un loader qui peut le gérer.

## BabelLoader

OK, revenons à notre application de démonstration. Nous n'avons écrit que quelques lignes de JavaScript jusqu'à présent. Ce serait bien si nous pouvions écrire notre JavaScript en utilisant de nouvelles fonctionnalités qui ne sont pas encore bien supportées dans tous les navigateurs. [Babel](https://babeljs.io/) est un compilateur JavaScript qui peut transformer du code ES6+ en code ES5.

Et (vous l'avez deviné), il y a un loader pour cela : [babel-loader](https://babeljs.io/setup#installation).

Pour configurer `babel-loader`, nous allons suivre les instructions de leur guide d'installation lié ci-dessus.

Tout d'abord, nous allons installer nos dépendances :

```bash
yarn add --dev babel-loader @babel/core
```

Ensuite, nous allons ajouter une nouvelle règle à notre tableau de règles de module dans notre fichier `webpack.config.common.js` :

```javascript
const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      inject: true,
      template: path.resolve(__dirname, 'src', 'index.html'),
    }),
  ],
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.(js|jsx)$/,
        exclude: /[\\/]node_modules[\\/]/,
        use: {
          loader: 'babel-loader',
        },
      },
    ]
  }
}
```

Cela indiquera à webpack que lorsqu'il rencontre des fichiers `.js` ou `.jsx`, il doit utiliser Babel pour transformer le code. Nous utilisons la propriété `exclude` pour nous assurer que Babel n'essaie pas de transformer les fichiers JavaScript dans notre répertoire `node_modules`. Ce sont des dépendances tierces qui devraient déjà avoir été prises en charge par leurs créateurs.

Ensuite, nous allons ajouter une dépendance supplémentaire pour un preset Babel :

```bash
yarn add --dev @babel/preset-env
```

Puis nous allons créer un fichier `.babelrc` où nous pourrons faire d'autres configurations Babel si nécessaire. Nous allons garder notre fichier assez simple et simplement spécifier le preset Babel que nous voulons utiliser :

```json
{
  "presets": ["@babel/preset-env"]
}
```

Et enfin, écrivons un peu de code ES6 dans notre fichier `./src/index.js` :

```javascript
import './index.css'

const p = document.createElement('p')
p.textContent = 'Hello from webpack!'
document.body.appendChild(p)

const p2 = document.createElement('p')
const numbers1 = [1, 2, 3, 4, 5, 6]
const numbers2 = [7, 8, 9, 10]
const numbers3 = [...numbers1, ...numbers2]
p2.textContent = numbers3.join(' ')
document.body.appendChild(p2)
```

C'est un exemple vraiment trivial, mais nous utilisons ici l'[opérateur de décomposition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) pour concaténer deux tableaux.

Maintenant, si nous tuons notre processus en cours et exécutons `yarn start` à nouveau, nous devrions voir ceci dans le navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-28-at-1.25.19-PM.png)
_Sortie de l'application de démonstration 7 - ajoute des nombres_

Super ! Tout fonctionne bien.

## Styles temporairement manquants

Si vous désactivez le cache dans votre navigateur et rechargez la page de notre application de démonstration, vous pouvez remarquer un léger scintillement où la page apparaît avec simplement le HTML non stylisé, puis l'arrière-plan de la page devient rose et le texte devient blanc lorsque les styles sont appliqués.

Ce comportement résulte de la manière dont `style-loader` fonctionne. Comme mentionné ci-dessus, `style-loader` prend le CSS et le place dans une balise `style` dans votre HTML. À cause de cela, il y a une brève période de temps où la balise `style` n'a pas encore été ajoutée !

Maintenant, cela est acceptable pour un environnement de développement, mais nous ne voudrions certainement pas que ce type de comportement se produise en production. Corrigons cela.

## MiniCssExtractPlugin

Plutôt que d'injecter le CSS dans notre HTML sous forme de balises `style`, nous pouvons utiliser le [MiniCssExtractPlugin](https://webpack.js.org/plugins/mini-css-extract-plugin/) pour générer des fichiers CSS séparés pour nous. Nous l'utiliserons dans notre configuration de production tout en continuant à utiliser `style-loader` dans notre configuration de développement.

Tout d'abord, installons la dépendance dans notre projet :

```bash
yarn add --dev mini-css-extract-plugin
```

Maintenant, dans notre fichier `webpack.config.common.js`, supprimons la règle CSS puisque nous allons gérer cela différemment en développement et en production. Il nous reste ceci dans notre configuration partagée :

```javascript
const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      inject: true,
      template: path.resolve(__dirname, 'src', 'index.html'),
    }),
  ],
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /[\\/]node_modules[\\/]/,
        use: {
          loader: 'babel-loader',
        },
      },
    ]
  }
}
```

Maintenant, dans notre fichier `webpack.config.dev.js`, ajoutons à nouveau `style-loader` et `css-loader` que nous venons de supprimer de notre configuration partagée :

```javascript
const merge = require('webpack-merge')
const commonConfig = require('./webpack.config.common')

module.exports = merge(commonConfig, {
  mode: 'development',
  devtool: 'inline-source-map',
  devServer: {
    contentBase: './dist',
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
    ]
  }
})
```

Et enfin, dans notre fichier `webpack.config.prod.js`, ajoutons notre nouveau `mini-css-extract-plugin` :

```
const merge = require('webpack-merge')
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const commonConfig = require('./webpack.config.common')

module.exports = merge(commonConfig, {
  mode: 'production',
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css',
    }),
  ]
})
```

Celui-ci est un peu différent car il est à la fois un plugin et un loader, donc il va dans les règles de module et dans les sections de plugins.

Notez également que nous utilisons les crochets dans notre nom de fichier pour définir dynamiquement le `name` comme le nom du fichier source original et inclure également le `contenthash`, qui est un hachage (une chaîne alphanumérique) représentant le contenu du fichier.

Maintenant, si vous exécutez `yarn build` cette fois pour générer la construction de production, vous devriez obtenir une sortie dans votre terminal qui ressemble à ceci :

![Sortie de la construction de production Webpack](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-28-at-1.57.28-PM.png)
_Sortie de la construction de production Webpack_

Notez qu'il génère en fait un fichier CSS maintenant, et le hachage de contenu est inclus dans le nom du fichier.

D'accord, problème résolu ! Plus de scintillement lorsque la page se charge en production puisque nous avons les styles inclus comme une balise `link` vers un fichier CSS réel.

## Cache Busting

Puisque nous avons inclus le hachage de contenu dans le fichier CSS généré, c'est le bon moment pour parler du cache busting. Pourquoi, demandez-vous, voulons-nous que le hachage de contenu soit inclus dans nos noms de fichiers ? Pour aider le navigateur à comprendre quand un fichier a changé !

Votre navigateur essaie d'être utile en mettant en cache les fichiers qu'il a déjà vus. Par exemple, si vous avez visité un site web, et que votre navigateur a dû télécharger des actifs comme des fichiers JavaScript, CSS ou des images, votre navigateur peut mettre en cache ces fichiers afin de ne pas avoir à les demander à nouveau au serveur.

Cela signifie que si vous visitez à nouveau le site, votre navigateur peut utiliser les fichiers mis en cache au lieu de les demander à nouveau, vous obtenez donc un temps de chargement de page plus rapide et une meilleure expérience.

Alors, quel est le problème ici ? Imaginez si nous avions un fichier appelé `main.js` utilisé dans notre application. Ensuite, un utilisateur visite votre application et son navigateur met en cache le fichier `main.js`.

Maintenant, à un moment ultérieur, vous avez publié un nouveau code pour votre application. Le contenu du fichier `main.js` a changé. Mais, lorsque cet utilisateur visite à nouveau votre application, le navigateur voit qu'il a besoin d'un fichier `main.js`, note qu'il a un fichier `main.js` mis en cache, et utilise simplement la version mise en cache. L'utilisateur n'obtient pas votre nouveau code !

Pour résoudre ce problème, une pratique courante consiste à inclure le hachage de contenu dans le nom de chaque fichier. Comme discuté précédemment, le hachage de contenu est une représentation sous forme de chaîne du contenu du fichier. Si le contenu du fichier ne change pas, le hachage de contenu ne change pas. Mais, si le contenu du fichier change, alors le hachage de contenu change également.

Parce que le nom du fichier changera maintenant lorsque le code changera, le navigateur téléchargera le nouveau fichier puisqu'il n'aura pas ce nom de fichier spécifique dans son cache.

## Inclure le hachage de contenu

Pour inclure le hachage de contenu dans nos noms de fichiers JavaScript, nous allons modifier une seule ligne de code dans notre fichier `webpack.config.common.js`. Cette ligne :

```javascript
filename: 'main.js'
```

Changera en cette ligne :

```javascript
filename: '[name].[contenthash].js'
```

Ainsi, le fichier entier ressemble à ceci :

```javascript
const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  entry: './src/index.js',
  output: {
    filename: '[name].[contenthash].js', // cette ligne est la seule différence
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      inject: true,
      template: path.resolve(__dirname, 'src', 'index.html'),
    }),
  ],
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /[\\/]node_modules[\\/]/,
        use: {
          loader: 'babel-loader',
        },
      },
    ]
  }
}
```

Maintenant, si vous exécutez `yarn build`, vous verrez que votre JavaScript et votre CSS incluent tous deux des hachages de contenu :

![Sortie de la construction de production Webpack avec les hachages de contenu inclus](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-28-at-2.12.27-PM.png)
_Sortie de la construction de production Webpack avec les hachages de contenu inclus_

Si vous exécutez `yarn build` à nouveau et comparez votre nouvelle sortie à votre ancienne sortie, vous remarquerez que les hachages de contenu sont exactement les mêmes les deux fois.

Mais, si vous modifiez votre fichier `./src/index.js` de quelque manière que ce soit et exécutez ensuite `yarn build` à nouveau, vous obtiendrez un nouveau hachage de contenu car le contenu a changé ! Essayez-le !

## Minification du CSS

Enfin, mais non des moindres, nous pouvons vouloir minifier notre CSS. Nous minifions déjà notre JavaScript pour la construction de production, mais nous ne minifions pas encore notre CSS. Faisons cela.

Nous pouvons minimiser notre CSS en utilisant le [optimize-css-assets-webpack-plugin](https://github.com/NMFR/optimize-css-assets-webpack-plugin). Installons cette dépendance maintenant :

```bash
yarn add --dev optimize-css-assets-webpack-plugin
```

Maintenant, nous pouvons ajouter cela à une section d'optimisation de notre fichier `webpack.config.prod.js` :

```javascript
const merge = require('webpack-merge')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')
const commonConfig = require('./webpack.config.common')

module.exports = merge(commonConfig, {
  mode: 'production',
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css',
    }),
  ],
  optimization: {
    minimizer: [
      new OptimizeCssAssetsPlugin({
        cssProcessorOptions: {
          map: {
            inline: false,
            annotation: true,
          },
        },
      }),
    ],
  },
})
```

Maintenant, si nous exécutons `yarn build` et vérifions ensuite le contenu de notre répertoire `dist`, nous pouvons voir que le CSS résultant est minifié. Bien !

```css
body{background:#ff1493;color:#fff}
/*# sourceMappingURL=main.66e0d6aeae6f3c6fb895.css.map */
```

Mais attendez ! Si nous regardons notre fichier JavaScript résultant, il n'est pas minifié ! Hmmm. Il était minifié avant, alors qu'est-ce qui s'est passé ici ?

Le problème est que nous configurons maintenant manuellement la section de minimisation d'optimisation de notre configuration webpack. Lorsque cette section n'est pas dans le fichier de configuration webpack, webpack utilise par défaut ses propres préférences de minimisation, qui incluent la minification du JavaScript lorsque le `mode` est défini sur `production`.

Puisque nous remplaçons maintenant ces valeurs par défaut en ajoutant nos préférences pour la minification des actifs CSS, nous devrons également inclure explicitement des instructions sur la manière dont nous voulons que webpack minifie les actifs JavaScript.

## TerserWebpackPlugin

Nous pouvons minifier nos fichiers JavaScript en utilisant le [TerserWebpackPlugin](https://webpack.js.org/plugins/terser-webpack-plugin/). Commençons par installer cette dépendance :

```bash
yarn add --dev terser-webpack-plugin
```

Ensuite, dans notre fichier `webpack.config.prod.js`, ajoutons le `terser-webpack-plugin` à nos paramètres de minimisation d'optimisation en bas du fichier :

```javascript
const merge = require('webpack-merge')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')
const TerserPlugin = require('terser-webpack-plugin')
const commonConfig = require('./webpack.config.common')

module.exports = merge(commonConfig, {
  mode: 'production',
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css',
    }),
  ],
  optimization: {
    minimizer: [
      new OptimizeCssAssetsPlugin({
        cssProcessorOptions: {
          map: {
            inline: false,
            annotation: true,
          },
        },
      }),
      new TerserPlugin({
        // Utiliser l'exécution parallèle multi-processus pour améliorer la vitesse de construction
        // Nombre par défaut d'exécutions simultanées : os.cpus().length - 1
        parallel: true,
        // Activer la mise en cache des fichiers
        cache: true,
        sourceMap: true,
      }),
    ],
  },
})
```

Maintenant, si nous exécutons `yarn build` et regardons la sortie dans le répertoire `dist`, nous devrions voir que nos fichiers CSS et nos fichiers JavaScript sont minifiés. Nous y voilà !

## Conclusion

Si vous avez suivi jusqu'ici, je vous félicite !

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-186.png)
_Photo par [Unsplash](https://unsplash.com/@katya?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Katya Austin</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Récapitulons ce que nous avons appris jusqu'à présent :

* Webpack est un outil de construction pour le bundling d'actifs et la gestion des dépendances.
* Webpack peut être configuré par un fichier de configuration.
* Les plugins modifient et étendent le processus de construction de webpack.
* Les loaders instruisent webpack sur la manière de gérer différents types de fichiers.
* Le `clean-webpack-plugin` peut être utilisé pour supprimer les anciens artefacts de construction du répertoire `dist`.
* Le `html-webpack-plugin` aide à gérer le fichier HTML, y compris l'injection de JavaScript dans le fichier via des balises `script`.
* `webpack-dev-server` crée un serveur de développement pour faciliter le développement local.
* Il est utile d'avoir des configurations webpack séparées pour le développement et la production. Vous pouvez partager et fusionner des fichiers de configuration en utilisant le plugin `webpack-merge`.
* Nous pouvons gérer le style de notre application en incluant des loaders comme `css-loader`, `style-loader`, `sass-loader`, `less-loader`, et le `mini-css-extract-plugin` (qui fonctionne à la fois comme un plugin et un loader).
* Nous pouvons inclure une nouvelle syntaxe et des fonctionnalités JavaScript en utilisant Babel et `babel-loader`.
* Nous pouvons inclure des hachages de contenu dans nos noms de fichiers pour aider au cache busting et à la gestion des nouvelles versions de notre code publié.
* Nous pouvons minifier notre CSS avec le `optimize-css-assets-webpack-plugin`.
* Nous pouvons minifier notre JavaScript avec le `terser-webpack-plugin`.

## Qu'est-ce qui suit ?

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-187.png)
_Photo par [Unsplash](https://unsplash.com/@tomparkes?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Tom Parkes</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Tout au long de cet article, nous avons créé une configuration webpack assez respectable. Toutes ces techniques que nous avons discutées sont des normes de l'industrie et sont courantes dans les projets de niveau entreprise.

Mais il y a encore plus ! D'autres sujets avancés de webpack incluent le [code splitting](https://webpack.js.org/guides/code-splitting/), le [lazy loading](https://webpack.js.org/guides/lazy-loading/), le [tree shaking](https://webpack.js.org/guides/tree-shaking/), et plus encore !

Si vous êtes intéressé à explorer webpack plus par vous-même, je vous recommande vivement de lire les [guides officiels de webpack](https://webpack.js.org/guides/).

Encore une fois, tout le code que nous avons parcouru dans ce tutoriel peut être trouvé sur GitHub. Le [point de départ se trouve ici](https://github.com/thawkin3/webpack-training-1/tree/demo/start), et le [résultat final se trouve ici](https://github.com/thawkin3/webpack-training-1).

Merci d'avoir lu, et bon codage !
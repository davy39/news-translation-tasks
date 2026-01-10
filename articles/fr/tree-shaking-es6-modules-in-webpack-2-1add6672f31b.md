---
title: Tree-shaking des modules ES6 dans webpack 2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-16T21:19:21.000Z'
originalURL: https://freecodecamp.org/news/tree-shaking-es6-modules-in-webpack-2-1add6672f31b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oD1_oAmOuY4X0k5QdqaQow.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: Tree-shaking des modules ES6 dans webpack 2
seo_desc: 'By Jake Wiesler

  Webpack 2 was just released from beta last week. It brings with it a variety of
  anticipated features, including native support for ES6 modules.

  Instead of using the var module = require(''module'') syntax, webpack 2 supports
  ES6 imports...'
---

Par Jake Wiesler

[Webpack 2](https://webpack.js.org/) vient d'être publié en version stable la semaine dernière. Il apporte avec lui une variété de fonctionnalités attendues, y compris le support natif des modules ES6.

Au lieu d'utiliser la syntaxe `var module = require('module')`, webpack 2 supporte les `imports` et `exports` ES6. Cela ouvre la porte à des optimisations de code comme le **tree-shaking**.

### Qu'est-ce que le tree-shaking ?

Popularisé par le bundler de modules [Rollup.js](http://rollupjs.org/) de Rich Harris, le _tree-shaking_ est la capacité à n'inclure dans votre bundle que le code qui est _utilisé_.

Lorsque j'ai commencé à jouer avec Rollup, j'ai été émerveillé par la façon dont il fonctionnait avec les modules ES6. L'expérience de développement semblait simplement... juste. Je pouvais créer des modules séparés écrits en JavaScript "futur", puis les inclure n'importe où dans mon code. Tout code non utilisé ne se retrouve pas dans mon bundle. Génial !

#### Quel problème résout-il ?

Si vous écrivez du JavaScript en 2017 et que vous _comprenez_ (voir : [JavaScript fatigue](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f#.nk6chuvta)) les divers outils disponibles, votre expérience de développement est probablement assez fluide. Cela est important, mais ce qui est également important, c'est l'_expérience utilisateur_. Beaucoup de ces outils modernes finissent par alourdir les applications web avec des fichiers JavaScript massifs, ce qui entraîne des performances plus lentes.

Ce que j'aime dans Rollup, c'est qu'il s'attaque à ce problème et apporte une solution au premier plan de la communauté JavaScript. Maintenant, des noms comme webpack tentent de l'itérer.

Le tree-shaking n'est peut-être pas _"la solution ultime"_, mais c'est une pièce importante dans un puzzle plus grand.

#### Un exemple simple

Avant de commencer, je veux vous fournir un exemple trivial de tree-shaking. Votre application est composée de 2 fichiers, `index.js` et `module.js`.

À l'intérieur de `module.js`, vous exportez 2 fonctions fléchées nommées :

```js
// module.js 

export const sayHello = name => `Hello ${name}!`; 

export const sayBye = name => `Bye ${name}!`;
```

Seul `sayHello` est importé dans le fichier `index.js` :

```js
// index.js 

import { sayHello } from './module'; 

sayHello('World');
```

`sayBye` est exporté mais _jamais_ importé. Nulle part. Par conséquent, grâce au tree-shaking, il ne sera pas inclus dans votre bundle :

```js
// bundle.js 

const sayHello = name => `Hello ${name}!`; 

sayHello('World');
```

Selon le bundler utilisé, le fichier de sortie ci-dessus peut avoir un aspect différent. Il s'agit simplement d'une version simplifiée, mais vous comprenez l'idée.

Récemment, j'ai lu un article écrit par [Roman Liutikov](https://medium.com/@roman01la/dead-code-elimination-and-tree-shaking-in-javascript-build-systems-fb8512c86edf#.69aadkgrb), et il a fait une excellente analogie pour visualiser le concept de tree-shaking :

> _"Si vous vous demandez pourquoi cela s'appelle tree-shaking : imaginez votre application comme un graphe de dépendances, c'est un arbre, et chaque export est une branche. Donc, si vous secouez l'arbre, les branches mortes tomberont."_ — Roman Liutikov_

### Tree-shaking dans webpack 2

Malheureusement pour ceux d'entre nous qui utilisent webpack, le tree-shaking est "derrière un interrupteur", si vous voulez. Contrairement à Rollup, une certaine configuration doit être effectuée avant de pouvoir obtenir la fonctionnalité que vous recherchez. La partie "derrière un interrupteur" peut confondre certaines personnes. Je vais expliquer.

#### Étape 1 : Installation du projet

Je vais supposer que vous comprenez les bases de webpack et que vous pouvez vous repérer dans un fichier de configuration webpack de base.

Commençons par créer un nouveau répertoire :

```bash
mkdir webpack-tree-shaking && cd webpack-tree-shaking
```

Une fois à l'intérieur, initialisons un nouveau projet `npm` :

```bash
npm init -y
```

L'option `-y` génère le `package.json` rapidement sans que vous ayez à répondre à une série de questions.

Ensuite, installons quelques dépendances de projet :

```bash
npm i --save-dev webpack@beta html-webpack-plugin
```

La commande ci-dessus installera la dernière version bêta de webpack 2 localement dans votre projet ainsi qu'un plugin utile nommé `html-webpack-plugin`. Ce dernier n'est pas nécessaire pour l'objectif de ce guide, mais rendra les choses un peu plus rapides.

**Note** : La commande `npm i --save-dev webpack@beta` est toujours recommandée par l'équipe webpack au moment de la rédaction. `webpack@beta` sera progressivement abandonné au profit de la commande `webpack` latest. Consultez la section _How To Download?_ du [dernier article de publication de webpack](https://medium.com/webpack/webpack-2-2-the-final-release-76c3d43bf144#.soqt6oma5) pour plus de détails.

Ouvrez `package.json` et assurez-vous qu'ils ont été installés en tant que `devDependencies`.

#### Étape 2 : Créer des fichiers JS

Pour voir le tree-shaking en action, vous devez avoir du JavaScript avec lequel jouer. Dans la racine de votre projet, créez un dossier `src` avec 2 fichiers à l'intérieur :

```bash
mkdir src && cd src 

touch index.js 

touch module.js
```

**Note** : La commande `touch` crée un nouveau fichier via le terminal.

Copiez le code ci-dessous dans les fichiers corrects :

```js
// module.js 

export const sayHello = name => `Hello ${name}!`; 

export const sayBye = name => `Bye ${name}!`;
```

```js
// index.js 

import { sayHello } from './module'; 

const element = document.createElement('h1'); 

element.innerHTML = sayHello('World'); 

document.body.appendChild(element);
```

Si vous êtes arrivé jusqu'ici, votre structure de dossier devrait ressembler à ceci :

```
/ 
| - node_modules/ 
| - src/ 
|    | - index.js 
|    | - module.js 
| - package.json
```

#### Étape 3 : Webpack depuis la CLI

Puisque vous n'avez pas de fichier de configuration créé pour votre projet, la seule façon de faire fonctionner webpack pour l'instant est via la CLI de webpack. Faisons un test rapide.

Dans votre terminal, exécutez la commande suivante à la racine de votre projet :

```bash
node_modules/.bin/webpack
```

Après avoir exécuté cette commande, vous devriez voir une sortie comme ceci :

```bash
No configuration file found and no output filename configured via CLI option. A configuration file could be named 'webpack.config.js' in the current directory. Use --help to display the CLI options.
```

La commande ne fait rien, et la CLI de webpack le confirme. Vous n'avez pas donné à webpack d'informations sur les fichiers que vous souhaitez bundler. Vous pourriez fournir ces informations via la ligne de commande _ou_ un fichier de configuration. Choisissons la première option juste pour tester que tout fonctionne :

```bash
node_modules/.bin/webpack src/index.js dist/bundle.js
```

Ce que vous avez fait maintenant, c'est passer à webpack un fichier `entry` et un fichier `output` via la CLI. Ces informations disent à webpack, "allez dans `src/index.js` et bundlez tout le code nécessaire dans `dist/bundle.js`". Et c'est exactement ce qu'il fait. Vous remarquerez que vous avez maintenant un répertoire `dist` contenant `bundle.js`.

Ouvrez-le et jetez un coup d'œil. Il y a du JavaScript supplémentaire dans le bundle nécessaire pour que webpack fasse son travail, mais au bas du fichier, vous devriez voir votre propre code également.

#### Étape 4 : Créer un fichier de configuration webpack

Webpack peut gérer beaucoup de choses. J'ai passé une bonne partie de mon temps libre à plonger dans ce bundler et j'ai à peine effleuré la surface. Une fois que vous avez dépassé les exemples triviaux, il est préférable de laisser la CLI de côté et de créer un fichier de configuration pour gérer le travail lourd.

Dans la racine de votre projet, créez un fichier `webpack.config.js` :

```bash
touch webpack.config.js
```

Ce fichier peut être aussi compliqué que vous le souhaitez. Nous allons le garder léger pour les besoins de cet article :

```js
// webpack.config.js
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: 'dist'
  },
  plugins: [
    new HtmlWebpackPlugin({ title: 'Tree-shaking' })
  ]
}
```

Ce fichier fournit à webpack les mêmes informations que vous avez données à la CLI précédemment. Vous avez défini `index.js` comme votre fichier `entry` et `bundle.js` comme votre fichier `output`. Vous avez également ajouté votre `html-webpack-plugin` qui générera un fichier html dans votre répertoire `dist`. Pratique.

Allez-y et testez cela pour vous assurer que tout fonctionne encore. Supprimez votre répertoire `dist`, et dans la ligne de commande, tapez :

```bash
webpack
```

Si tout s'est bien passé, vous pouvez ouvrir `dist/index.html` et voir "Hello World !".

**Note** : L'utilisation d'un fichier de configuration nous donne la commodité de taper `webpack` au lieu de `node_modules/.bin/webpack`. Petites victoires.

#### Étape 5 : Babel

J'ai mentionné précédemment que webpack 2 apporte un support natif pour les modules ES6. Tout cela est vrai, mais cela ne change pas le fait que ES6 n'est pas entièrement supporté dans tous les navigateurs. Pour cette raison, vous devez _transformer_ votre code ES6 en JavaScript acceptable en utilisant un outil comme [Babel](http://babeljs.io/). En conjonction avec webpack, Babel nous donne la capacité d'écrire votre JavaScript "futur" sans vous soucier des implications des navigateurs non supportés.

Allons-y et installons Babel dans votre projet :

```bash
npm i --save-dev babel-core babel-loader babel-preset-es2015
```

Notez le package `babel-preset-es2015`. Ce petit gars est la raison pour laquelle je me suis assis pour écrire tout cela.

#### Étape 6 : `babel-loader`

Webpack peut être configuré pour transformer des fichiers spécifiques en modules via des [loaders](https://webpack.js.org/concepts/#loaders). Une fois qu'ils sont transformés, ils sont ajoutés à un graphe de dépendances. Webpack utilise le graphe pour résoudre les dépendances et n'inclut que ce qui est nécessaire dans le bundle final. C'est la base de fonctionnement de webpack.

Vous pouvez maintenant configurer webpack pour utiliser `babel-loader` afin de transformer tous vos fichiers `.js` :

```js
// webpack.config.js
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: { filename: 'bundle.js', path: 'dist' },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        options: { 
          presets: [ 
            'es2015' 
          ] 
        }
      }
    ]
  },
  plugins: [ 
    new HtmlWebpackPlugin({ title: 'Tree-shaking' }) 
  ]
};
```

La propriété `module` fournit un ensemble d'instructions pour webpack. Elle dit : "prenez tous les fichiers se terminant par `.js` et transformez-les en utilisant `babel-loader`, mais ne transformez aucun fichier à l'intérieur de `node_modules` !"

Nous passons également le package `babel-preset-es2015` comme option à `babel-loader`. Cela indique simplement à `babel-loader` _comment_ transformer le JavaScript.

Exécutez `webpack` à nouveau pour vous assurer que tout est bon. Oui ? Super ! Ce que nous avons fait, c'est bundler vos fichiers JavaScript tout en les compilant en JavaScript supporté par les navigateurs.

### Le problème sous-jacent

Le package `babel-preset-es2015` contient un autre package nommé `babel-plugin-transform-es2015-modules-commonjs` qui transforme tous vos modules ES6 en modules `CommonJS`. Ce n'est pas idéal, et voici pourquoi.

Les bundlers JavaScript tels que webpack et Rollup ne peuvent effectuer le tree-shaking que sur des modules ayant une structure statique. Si un module est statique, alors le bundler peut déterminer sa structure au moment de la construction, supprimant en toute sécurité le code qui n'est pas importé quelque part.

Les modules `CommonJS` n'ont pas une structure statique. Pour cette raison, webpack ne pourra pas effectuer le tree-shaking du code non utilisé dans le bundle final. Heureusement, Babel a atténué ce problème en fournissant aux développeurs une option que vous pouvez passer à votre tableau `presets` avec `babel-preset-es2015` :

```bash
options: { presets: [ [ 'es2015', { modules: false } ] ] }
```

Selon la [documentation](https://github.com/babel/babel/tree/master/packages/babel-preset-es2015#options) de Babel :

`_modules - Active la transformation de la syntaxe des modules ES6 en un autre type de module (Activé par défaut en "commonjs"). Peut être `false` pour ne pas transformer les modules, ou l'un de `["amd", "umd", "systemjs", "commonjs"]"_.

Glissez ce petit bout de code dans votre configuration et vous serez en train de cuisiner à l'huile d'arachide.

L'état final de `webpack.config.js` ressemble à ceci :

```js
// webpack.config.js
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: { filename: 'bundle.js', path: 'dist' },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        options: { 
          presets: [ 
            [ 'es2015', { modules: false } ] 
          ] 
        }
      }
    ]
  },
  plugins: [ new HtmlWebpackPlugin({ title: 'Tree-shaking' }) ]
};
```

### Le Grand Finale

Exécutez `webpack` à nouveau et ouvrez votre fichier `bundle.js`. Vous ne remarquerez aucune différence. Avant de devenir fou, sachez ceci ! C'est normal. Nous avons exécuté webpack en mode développement tout ce temps. Webpack sait que vous avez des exports inutilisés dans votre code. Même s'il est inclus dans le bundle final, `sayBye` ne se retrouvera jamais en production.

Si vous ne me croyez toujours pas, exécutez `webpack -p` dans votre terminal. L'option `-p` signifie _production_. Webpack effectuera quelques optimisations de performance supplémentaires, y compris la minification, en supprimant tout code inutilisé en cours de route.

Ouvrez `bundle.js`. Puisqu'il est minifié, allez-y et recherchez `Hello`. Il _devrait_ être là. Recherchez `Bye`. Il _ne devrait pas_.

Voilà ! Vous avez maintenant une implémentation fonctionnelle du tree-shaking dans webpack 2 !

Pour les curieux, j'ai lentement itéré sur ma propre configuration légère de webpack dans un dépôt GitHub :

[**jake-wies/webpack-hotplate**](https://github.com/jake-wies/webpack-hotplate)  
[_webpack-hotplate - Un boilerplate webpack pour les projets personnels_](https://github.com/jake-wies/webpack-hotplate)  
[github.com](https://github.com/jake-wies/webpack-hotplate)

Il n'est pas censé être excessivement verbeux et gonflé. Il est axé sur l'approche d'un boilerplate accessible avec des guides à chaque étape. Si vous êtes intéressé, jetez un coup d'œil !

Si vous avez des questions, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/jakewies) !
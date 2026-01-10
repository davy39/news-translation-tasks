---
title: Comment rationaliser votre processus de développement React.js avec Webpack
  4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-09T12:55:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-react-js-apps-fast-using-webpack-4-3d772db957e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NLzcqb-jEMHg9K5Ov0oAyw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: Comment rationaliser votre processus de développement React.js avec Webpack
  4
seo_desc: 'By Margarita Obraztsova

  In the real world of development, we have to add new features very quickly. In this
  tutorial, I will show you everything you can do to streamline this process and reach
  120% of your dev speed.

  Why, you might ask?

  Because doing...'
---

Par Margarita Obraztsova

Dans le monde réel du développement, nous devons ajouter de nouvelles fonctionnalités très rapidement. Dans ce tutoriel, je vais vous montrer tout ce que vous pouvez faire pour rationaliser ce processus et atteindre 120% de votre vitesse de développement.

**Pourquoi**, pourriez-vous demander ?

Parce que faire du travail manuel est extrêmement contre-productif en matière de programmation. Nous voulons automatiser autant que possible. Je vais donc vous montrer quelles parties du processus de développement avec React nous pouvons ajuster en utilisant Webpack v4.6.0.

Je ne couvrirai pas les premières étapes de la configuration de Webpack, car je l'ai déjà fait dans mon [**précédent article**](https://hackernoon.com/a-tale-of-webpack-4-and-how-to-finally-configure-it-in-the-right-way-4e94c8e7e5c1)**.** Là, j'ai décrit comment configurer Webpack en détail. Je vais supposer que vous êtes déjà familiarisé avec les bases de la configuration de Webpack, afin que nous puissions commencer avec une configuration prête.

### Installation de Webpack

Dans votre fichier _webpack.config.js_, entrez le code suivant :

```
// webpack v4const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');
```

```
module.exports = {  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[chunkhash].js'  },  module: {    rules: [      {        test: /\.js$/,        exclude: /node_modules/,        use: {          loader: "babel-loader"        }      }    ]  },  plugins: [     new CleanWebpackPlugin('dist', {} ),    new HtmlWebpackPlugin({      inject: false,      hash: true,      template: './src/index.html',      filename: 'index.html'    }),    new WebpackMd5Hash()  ]};
```

et dans votre fichier _package.json_ :

```
{ "name": "post", "version": "1.0.0", "description": "", "main": "index.js", "scripts": {  "build": "webpack --mode production",  "dev": "webpack --mode development" },  "author": "", "license": "ISC", "devDependencies": {    "babel-cli": "^6.26.0",    "babel-core": "^6.26.0",    "babel-loader": "^7.1.4",    "babel-preset-env": "^1.6.1",    "babel-preset-react": "^6.24.1",    "babel-runtime": "^6.26.0",    "clean-webpack-plugin": "^0.1.19",    "html-webpack-plugin": "^3.2.0",    "react": "^16.3.2",    "react-dom": "^16.3.2",    "webpack": "^4.6.0",    "webpack-cli": "^2.0.13",    "webpack-md5-hash": "0.0.6"  }}
```

Maintenant, vous pouvez télécharger vos modules node :

```
npm i
```

et ajouter le dossier _src/_ à votre projet avec _index.html_ et _index.js_

D'abord dans _src/index.html_ :

```
<html>  <head>  </head>  <body>    <div id="app"></div>    <script src="<%= htmlWebpackPlugin.files.chunks.main.entry %>"></script>  </body></html>
```

et ensuite dans _src/index.js_ :

```
console.log("hello, world");
```

Lançons le script de développement :

```
npm run dev
```

**Et voilà, ça compile !** Maintenant, configurons React également.

### Configuration de votre projet React

Puisque React utilise une syntaxe spéciale appelée JSX, nous devons transpiler notre code. Si nous allons sur le site de Babel, il a le [préréglage pour React](https://babeljs.io/docs/plugins/preset-react/).

```
npm install --save-dev babel-cli babel-preset-react
```

Notre fichier _.babelrc_ devrait ressembler à ceci :

```
{  "presets": ["env", "react"]}
```

Ajoutez une initialisation d'application à votre fichier _index.js_ :

```
import React from 'react';import { render } from 'react-dom';
```

```
class App extends React.Component {
```

```
render() {    return (      <div>        'Hello world!'      </div>    );  }}
```

```
render(<App />, document.getElementById('app'));
```

et exécutez le script de développement :

```
npm run dev
```

Si vous avez réussi à générer un dossier _./dist_ avec _index.html_ et un fichier principal avec un hash, **vous avez fait du bon travail ! Nous avons notre application qui compile !**

### Configuration de webpack-dev-server

Techniquement, nous n'avons pas à le faire, car il existe de nombreux serveurs basés sur Node pour les applications front-end. Mais je recommande **webpack-dev-server** car il est conçu pour fonctionner avec Webpack, et il prend en charge un ensemble de fonctionnalités intéressantes telles que **le remplacement de modules à chaud**, **les cartes sources, et ainsi de suite**.

Comme ils le mentionnent dans la [page de documentation officielle](https://github.com/webpack/webpack-dev-server) :

> Utilisez [webpack](https://webpack.js.org/) avec un serveur de développement qui fournit un rechargement en direct. Cela devrait être utilisé uniquement pour le développement.

**Voici où cela peut devenir un peu confus :** comment faire en sorte que webpack-dev-server ne fonctionne que pour le mode dev ?

```
npm i webpack-dev-server --save-dev
```

dans votre fichier _package.json_, ajustez

```
"scripts": {  "dev": "webpack-dev-server --mode development --open",  "build": "webpack --mode production"}
```

**Maintenant, il devrait lancer un serveur et ouvrir automatiquement votre navigateur avec votre application.**

Votre fichier _package.json_ ressemble à ceci à ce stade :

```
{ "name": "post", "version": "1.0.0", "description": "", "main": "index.js", "scripts": {  "dev": "webpack-dev-server --mode development --open",  "build": "webpack --mode production" }, "author": "", "license": "ISC", "devDependencies": {  "babel-cli": "^6.26.0",  "babel-core": "^6.26.0",  "babel-loader": "^7.1.4",  "babel-preset-env": "^1.6.1",  "babel-preset-react": "^6.24.1",  "babel-runtime": "^6.26.0",  "clean-webpack-plugin": "^0.1.19",  "html-webpack-plugin": "^3.2.0",  "react": "^16.3.2",  "react-dom": "^16.3.2",  "webpack": "^4.6.0",  "webpack-cli": "^2.0.13",  "webpack-dev-server": "^3.1.3",  "webpack-md5-hash": "0.0.6" }}
```

Maintenant, si vous essayez de modifier quelque chose dans votre application, le navigateur devrait rafraîchir automatiquement la page.

![Image](https://cdn-media-1.freecodecamp.org/images/d-pNaItP95QgGseyYPF4vnf59hE6ZzN3dEhw)

Ensuite, vous devez télécharger React devtools en tant qu'extension Chrome.

![Image](https://cdn-media-1.freecodecamp.org/images/xvAiMTS9dt3ldDHDTZpttKKA4VocFOA5k35I)

**De cette façon, vous pouvez déboguer votre application à partir de la console Chrome beaucoup plus facilement.**

### Configuration d'ESLint

Pourquoi en avons-nous besoin ? Eh bien, généralement, nous n'avons pas à l'utiliser. Mais ESLint est un outil pratique. Dans notre cas, il rendra notre code (dans l'éditeur et le terminal, et sur le navigateur) et mettra en évidence nos erreurs, fautes de frappe et erreurs si nous en avons. Cela s'appelle **linting**.

ESLint est un utilitaire de linting JavaScript open-source créé à l'origine par Nicholas C. Zakas en juin 2013. Il existe des alternatives, mais jusqu'à présent, il fonctionne bien avec ES6 et React, trouve des problèmes courants et s'intègre avec d'autres parties de l'écosystème.

Pour l'instant, installons-le localement pour notre propre nouveau projet. Bien sûr, ESLint à ce stade a un grand nombre de paramètres. Vous pouvez en lire plus à leur sujet [sur le site officiel](https://eslint.org/docs/about/).

```
npm install eslint --save-dev
```

```
./node_modules/.bin/eslint --init
```

La dernière commande créera un fichier de configuration. Vous serez invité à choisir parmi trois options :

![Image](https://cdn-media-1.freecodecamp.org/images/jqwXQg5EbMzBcHH5Ay2h5J-A7D4dvWXcH6MG)

Dans ce tutoriel, j'ai choisi la première : répondre aux questions. Voici mes réponses :

![Image](https://cdn-media-1.freecodecamp.org/images/4z0Do2YSSauRT3AE4mJMpJXkGUVrfqEoef15)

Cela ajoutera un fichier _.eslintrc.js_ à votre répertoire de projet. Mon fichier généré ressemble à ceci :

```
module.exports = {    "env": {        "browser": true,        "commonjs": true,        "es6": true    },    "extends": "eslint:recommended",    "parserOptions": {        "ecmaFeatures": {            "experimentalObjectRestSpread": true,            "jsx": true        },        "sourceType": "module"    },    "plugins": [        "react"    ],    "rules": {        "indent": [            "error",            4        ],        "linebreak-style": [            "error",            "unix"        ],        "quotes": [            "error",            "single"        ],        "semi": [            "error",            "always"        ]    }};
```

Rien ne se passe pour l'instant. Bien que ce soit une configuration parfaitement valide, ce n'est pas suffisant — nous devons l'intégrer avec Webpack et notre éditeur de texte pour qu'il fonctionne. Comme je l'ai mentionné, nous pouvons l'avoir dans l'éditeur de code, le terminal (en tant que linter), ou en tant que hook de pré-commit. Nous allons le configurer pour notre éditeur pour l'instant.

#### Configuration pour Visual Studio Code

Au cas où vous vous poseriez la question, ESLint a un plugin pour presque tous les principaux éditeurs de code, y compris **Visual Studio Code, Visual Studio, SublimeText**, **Atom, WebStorm, et même vim.** Alors allez-y et téléchargez la version pour [votre propre éditeur de texte](https://prettier.io/docs/en/editors.html). J'utiliserai **VS Code dans cette démonstration.**

![Image](https://cdn-media-1.freecodecamp.org/images/4WU65-eeeoKswMvDEoS1Sxt8k57aCQ8Xik15)

Maintenant, nous pouvons voir certaines erreurs de code apparaître. Cela est dû au fait que le projet a un fichier de configuration qui vérifie le code et se plaint lorsque certaines règles ne sont pas respectées.

![Image](https://cdn-media-1.freecodecamp.org/images/cpz3JPvXphCHG7q28iT0d8JgDQ0j6W4W5xvj)

Vous pouvez le déboguer manuellement en vérifiant le message d'erreur, ou vous pouvez en tirer parti et simplement appuyer sur sauvegarder et il corrigera automatiquement les choses.

![Image](https://cdn-media-1.freecodecamp.org/images/4RkUDknKdYAVnRAC6EWBm0ej7XXMp2nVj1TY)

Vous pouvez maintenant aller et ajuster les paramètres d'ESLint :

```
module.exports = {    "env": {        "browser": true,        "commonjs": true,        "es6": true    },    "extends": ["eslint:recommended", "plugin:react/recommended"],    "parserOptions": {        "ecmaFeatures": {            "experimentalObjectRestSpread": true,            "jsx": true        },        "sourceType": "module"    },    "plugins": [        "react"    ],    "rules": {        "indent": [            "error",            2        ],        "linebreak-style": [            "error",            "unix"        ],        "quotes": [            "warn",            "single"        ],        "semi": [            "error",            "always"        ]    }};
```

Cela ne cassera pas la construction si vous avez inclus des guillemets doubles par erreur au lieu de guillemets simples. Cela ajoutera également certaines vérifications pour JSX.

#### Ajouter Prettier

![Image](https://cdn-media-1.freecodecamp.org/images/z0E8DoSQUWzpFCR7d5doOsaKYsWnPsl2KvTp)

Prettier est l'un des formatteurs les plus populaires de nos jours, et il est bien accepté par la communauté de codage. Il peut être ajouté à ESLint, [votre éditeur](https://prettier.io/docs/en/editors.html), et également installé en tant que hook de pré-commit.

![Image](https://cdn-media-1.freecodecamp.org/images/fXTBqX11LT895GhaapTmE8rylLpcmGAGmnGI)
_Je vais l'installer dans mon VS code ici_

Une fois que vous l'avez installé, vous pouvez essayer de vérifier votre code à nouveau. Si nous écrivons une indentation bizarre et appuyons sur sauvegarder, il devrait automatiquement formater le code maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/iqk2-ROG6uExr-DzS4qculgcmJySHCUBNs6k)

Ce n'est pas encore suffisant. Afin qu'ESLint fonctionne de manière synchronisée et n'émette pas les mêmes erreurs deux fois, ou même ait des conflits de règles, vous [devez l'intégrer avec votre ESLint.](https://prettier.io/docs/en/eslint.html)

```
npm i --save-dev prettier eslint-plugin-prettier
```

Dans la documentation officielle, ils recommandent d'utiliser yarn, mais npm fera l'affaire pour l'instant. À votre fichier _.eslintrc.json_, ajoutez :

```
...  sourceType: "module"},plugins: ["react", "prettier"],extends: ["eslint:recommended", "plugin:react/recommended"],rules: {  indent: ["error", 2],  "linebreak-style": ["error", "unix"],  quotes: ["warn", "single"],  semi: ["error", "always"],  "prettier/prettier": "error"}...
```

**Maintenant, nous voulons étendre nos règles ESLint pour inclure les règles de prettier :**

```
npm i --save-dev eslint-config-prettier
```

et ajoutez quelques extensions à votre configuration eslint :

```
...extends: [  "eslint:recommended",  "plugin:react/recommended",  "prettier",  "plugin:prettier/recommended"]...
```

![Image](https://cdn-media-1.freecodecamp.org/images/yJwhMkcxckkojkR4zFcLCtYSkUZTC6R6yjDI)

Ajoutons quelques [configurations](https://prettier.io/docs/en/options.html) supplémentaires. Vous devriez le faire afin d'éviter les incompatibilités entre les règles par défaut de Prettier et vos règles ESLint, comme celle que j'ai maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/65ROjVeRyoZJZseJhXSsNYAqAklzJNO69Bzc)

Prettier emprunte le format de remplacement d'ESLint [override format](http://eslint.org/docs/user-guide/configuring#example-configuration). Cela vous permet d'appliquer une configuration à des fichiers spécifiques.

Vous pouvez maintenant créer un fichier de configuration pour cela sous la forme d'un fichier _.js_.

```
nano prettier.config.js
```

Maintenant, collez dans ce fichier :

```
module.exports = {  printWidth: 80,  tabWidth: 2,  semi: true,  singleQuote: true,  bracketSpacing: true};
```

![Image](https://cdn-media-1.freecodecamp.org/images/zpZDUaO29kqcucuV8sPL5nJSyg7IAq1UXUTF)

Maintenant, lorsque vous appuyez sur sauvegarder, vous voyez votre code être automatiquement formaté. N'est-ce pas bien plus joli ? Jeu de mots très intentionnel.

Mon fichier _package.json_ ressemble à ceci :

```
{ "name": "post", "version": "1.0.0", "description": "", "main": "index.js", "scripts": {  "build": "webpack --mode production",  "dev": "webpack-dev-server --mode development --open" }, "author": "", "license": "ISC", "devDependencies": {  "babel-cli": "^6.26.0",  "babel-core": "^6.26.0",  "babel-loader": "^7.1.4",  "babel-preset-env": "^1.6.1",  "babel-preset-react": "^6.24.1",  "babel-runtime": "^6.26.0",  "clean-webpack-plugin": "^0.1.19",  "eslint": "^4.19.1",  "eslint-config-prettier": "^2.9.0",  "eslint-plugin-prettier": "^2.6.0",  "eslint-plugin-react": "^7.7.0",  "html-webpack-plugin": "^3.2.0",  "prettier": "^1.12.1",  "react": "^16.3.2",  "react-dom": "^16.3.2",  "webpack": "^4.6.0",  "webpack-cli": "^2.0.13",  "webpack-dev-server": "^3.1.4",  "webpack-md5-hash": "0.0.6" }}
```

Maintenant que nous avons tout cela configuré, faisons un rapide récapitulatif : ESLint surveille votre code pour les erreurs, et Prettier est un outil de formatage de style. ESLint a beaucoup plus de moyens pour attraper les erreurs, tandis que Prettier formate votre code joliment.

```
// webpack v4const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');module.exports = {  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[chunkhash].js'  },  module: {    rules: [      {        test: /\.js$/,        exclude: /node_modules/,        use: {          loader: "babel-loader"        }      }    ]  },  plugins: [     new CleanWebpackPlugin('dist', {} ),    new HtmlWebpackPlugin({      inject: false,      hash: true,      template: './src/index.html',      filename: 'index.html'    }),    new WebpackMd5Hash()  ]};
```

#### Problème : Prettier ne formate pas automatiquement le code dans Visual Studio Code

Quelques personnes ont souligné que VS Code ne fonctionne pas avec Prettier.

Si votre plugin Prettier ne formate pas automatiquement le code lors de l'enregistrement, vous pouvez le corriger en ajoutant ce code aux paramètres de VS Code :

```
"[javascript]": {    "editor.formatOnSave": true  }
```

comme décrit [ici](https://github.com/prettier/prettier-vscode/issues/290).

#### Ajout du chargeur ESLint à votre pipeline

Puisque ESLint est configuré dans le projet, il se plaindra également dans votre terminal une fois que vous aurez lancé le serveur de développement.

![Image](https://cdn-media-1.freecodecamp.org/images/qC75GumM19s12yF560UnLoZxe9rQ7SeUXQEx)

> **Note** : Bien qu'il soit possible de le faire, à ce moment-là, je ne recommande pas d'utiliser ESLint comme chargeur. Cela cassera la configuration de la carte source, que j'ai décrite en détail dans mon article précédent [Comment résoudre les problèmes de Webpack. Le cas pratique.](https://medium.com/@riittagirl/how-to-solve-webpack-problems-the-practical-case-79fb676417f4) Je vais montrer comment le configurer ici, au cas où les gars auraient déjà corrigé le bug qu'ils avaient.

Webpack a son propre [chargeur ESLint](https://www.npmjs.com/package/eslint-loader).

```
npm install eslint-loader --save-dev
```

Vous devez ajouter ESLint aux règles. Lorsque vous l'utilisez avec des chargeurs de transpilation (comme `babel-loader`), assurez-vous qu'ils sont dans le bon ordre (de bas en haut). Sinon, les fichiers seront vérifiés après avoir été traités par `babel-loader`

```
...module: {  rules: [    {      test: /\.js$/,      exclude: /node_modules/,      use: [{ loader: "babel-loader" }, { loader: "eslint-loader" }]    }  ]},...
```

![Image](https://cdn-media-1.freecodecamp.org/images/D71Nvppu6zikxFMGUd6zlfyrHnljsJUe36nb)

Voici quelques problèmes possibles que vous pourriez avoir :

* ajoutez une variable inutilisée à votre fichier index

![Image](https://cdn-media-1.freecodecamp.org/images/ci5uN3rhDzJlXhM4Y9iHShgeInPidFNrnDu3)

Si vous tombez sur cette erreur (no-unused-vars), elle est assez bien expliquée dans [cet issue](https://github.com/babel/babel-eslint/issues/6) sur GitHub et [ici](https://github.com/yannickcr/eslint-plugin-react/issues/1146).

Nous pouvons résoudre ce problème en ajoutant quelques règles, expliquées [ici](https://github.com/yannickcr/eslint-plugin-react#recommended) et [ici](https://github.com/yannickcr/eslint-plugin-react/blob/master/docs/rules/jsx-uses-vars.md).

Comme vous l'avez peut-être remarqué, vous obtenez l'erreur [no-unused-vars](https://eslint.org/docs/rules/no-unused-vars) ici. Vous devez en faire un avertissement et non une erreur, car ainsi, il est beaucoup plus facile de faire un développement rapide. Vous devez ajouter une nouvelle règle à votre ESLint afin de ne pas obtenir l'erreur par défaut.

Vous pouvez lire plus sur cette configuration [ici](https://eslint.org/docs/rules/no-unused-vars) et [ici](https://eslint.org/docs/user-guide/formatters/).

```
...semi: ['error', 'always'],'no-unused-vars': [  'warn',  { vars: 'all', args: 'none', ignoreRestSiblings: false }],'prettier/prettier': 'error'}...
```

De cette façon, nous obtiendrons de jolis messages d'erreur et d'avertissement.

J'aime l'idée d'avoir une fonctionnalité de correction automatique, mais soyons clairs : je ne suis pas le plus grand fan de voir les choses changer magiquement. Pour éviter cette situation, nous pouvons valider la correction automatique pour l'instant.

### Hook de pré-commit

Les gens sont généralement très prudents lorsqu'il s'agit d'utiliser les outils Git. Mais je vous assure, celui-ci est très facile et direct. Les hooks de pré-commit avec Prettier sont utilisés afin que les équipes aient un style de base de code cohérent dans tous les fichiers du projet, et que personne ne puisse valider du code non stylisé. Configurez l'intégration Git pour votre projet comme ceci :

```
git initgit add .nano .gitignore (ajoutez vos node_modules là)git commit -m "First commit"git remote add origin your origingit push -u origin master
```

Voici quelques excellents articles sur les [hooks git](https://www.atlassian.com/git/tutorials/git-hooks) et [l'utilisation de Prettier](https://prettier.io/docs/en/precommit.html).

Pour les personnes qui disent que vous ne pouvez le faire qu'en local — non, ce n'est pas vrai !

Vous pouvez le faire en utilisant l'outil lint-stage de [ce](https://github.com/okonet/lint-staged) dépôt par [Andrey Okonetchnikov](https://www.freecodecamp.org/news/how-to-develop-react-js-apps-fast-using-webpack-4-3d772db957e4/undefined).

### Ajout de propTypes

Créons un nouveau composant dans notre application. Jusqu'à présent, notre fichier _index.js_ ressemble à ceci :

```
import React from 'react';import { render } from 'react-dom';
```

```
class App extends React.Component {  render() {    return <div>Hello</div>;  }}render(<App />, document.getElementById('app'));
```

Nous allons créer un nouveau composant appelé Hello.js à des fins de démonstration.

```
import React from 'react';class Hello extends React.Component {  render() {    return <div>{this.props.hello}</div>;  }}export default Hello;
```

Maintenant, importez-le dans votre fichier _index.js_ :

```
import React from 'react';import { render } from 'react-dom';import Hello from './Hello';class App extends React.Component {  render() {    return (      <div>      <Hello hello={'Hello, world! And the people of the world!'} />     </div>   );  }}render(<App />, document.getElementById('app'));
```

Nous devions voir l'élément, mais ESLint se plaint :

![Image](https://cdn-media-1.freecodecamp.org/images/wlBU1cD2o9NHRzZGQaF3hrtgD-04Vh3XMvDG)

**Erreur : [eslint] 'hello' est manquant dans la validation des props (react/prop-types)**

Dans React v16, il est obligatoire d'ajouter des [prop types](https://www.tutorialspoint.com/reactjs/reactjs_props_validation.htm) afin d'éviter la confusion des types. Vous pouvez en lire plus à ce sujet [ici](https://reactjs.org/docs/typechecking-with-proptypes.html).

```
import React from 'react';import PropTypes from 'prop-types';class Hello extends React.Component {  render() {    return <div>{this.props.hello}</div>;  }}Hello.propTypes = {  hello: PropTypes.string};export default Hello;
```

![Image](https://cdn-media-1.freecodecamp.org/images/mL3rIeJQSVAMX9tJdJHff-fMT2NQiFm3IL8W)

### Remplacement de module à chaud

Maintenant que votre code est vérifié, il est temps d'ajouter plus de composants à votre application React. Jusqu'à présent, vous n'en avez que deux, mais dans la plupart des cas, vous en avez des dizaines.

Bien sûr, recompiler toute l'application à chaque rafraîchissement lorsque vous changez quelque chose dans votre projet n'est pas une option. Vous avez besoin d'un moyen plus rapide de le faire.

Alors ajoutons le remplacement de module à chaud, alias HMR. Dans la [documentation](https://webpack.js.org/concepts/hot-module-replacement/), il est décrit comme :

> Le remplacement de module à chaud (HMR) échange, ajoute ou supprime des [modules](https://webpack.js.org/concepts/modules/) pendant qu'une application est en cours d'exécution, sans rechargement complet. Cela peut accélérer considérablement le développement de plusieurs manières :

> Conserver l'état de l'application qui est perdu lors d'un rechargement complet.

> Économiser un temps de développement précieux en ne mettant à jour que ce qui a changé.

> Ajustez le style plus rapidement — presque comparable à changer les styles dans le débogueur du navigateur.

Je n'entre pas dans les détails techniques de son fonctionnement ici : ce serait le sujet d'un autre article. Mais voici comment le configurer :

```
...output: {  path: path.resolve(__dirname, 'dist'),  filename: '[name].[chunkhash].js'},devServer: {  contentBase: './dist',  hot: true},module: {  rules: [...
```

### Résolution de petits problèmes avec HMR

![Image](https://cdn-media-1.freecodecamp.org/images/0HqMo1Jp2CVMIvzcIkm2fBtG45IYABKaVHAE)

Nous avons dû remplacer chunkhash par hash, car évidemment webpack a corrigé ce problème depuis la dernière fois. Maintenant, nous avons le remplacement de module à chaud qui fonctionne !

```
...module.exports = {   entry: { main: './src/index.js' },   output: {     path: path.resolve(__dirname, 'dist'),     filename: '[name].[hash].js'   },   devServer: {     contentBase: './dist',     open: true  },   ...
```

### Résolution de bugs

Si nous exécutons le script de développement ici :

![Image](https://cdn-media-1.freecodecamp.org/images/az0baD-dHQtpAHDWDUaWlbviGXQ4N22RtTG8)

puis utilisez les conseils de [cet issue](https://github.com/webpack/webpack/issues/1151) pour le corriger.

Ensuite, ajoutez le drapeau --hot au script de développement dans _package.json_ :

```
..."scripts": {   "build": "webpack --mode production",   "dev": "webpack-dev-server --hot"}...
```

### Cartes sources :

Comme je l'ai mentionné ci-dessus, **les cartes sources ne fonctionneront pas avec le chargeur ESLint.** J'ai signalé un problème [ici](https://github.com/webpack-contrib/eslint-loader/issues/227#issuecomment-386798932).

> Généralement, vous ne les voulez pas dans votre projet de toute façon (puisque vous voulez déboguer votre projet à partir des messages d'erreur ESLint). Ils sont également connus pour rendre le HMR plus lent.

Vous pouvez en lire plus à ce sujet [ici](https://github.com/facebook/create-react-app/pull/109#issuecomment-234674331) et [ici](https://github.com/facebook/create-react-app/pull/109#issuecomment-234674331).

![Image](https://cdn-media-1.freecodecamp.org/images/QUFF4U8Vt7PdTJWSqq04-W5psU5NlOxl5UeS)

Mais si vous voulez des cartes sources de toute façon, le moyen le plus simple de les ajouter est via l'option [devtools](https://webpack.js.org/configuration/devtool/).

```
...module.exports = {  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[hash].js'  },  devtool: 'inline-source-map',  devServer: {    contentBase: './dist',    hot: true  },  ...
```

Note : les cartes sources ne fonctionneront pas tant que vous n'aurez pas spécifié l'environnement de la bonne manière. Vous pouvez lire plus sur mon processus de débogage [ici](https://medium.com/@riittagirl/how-to-solve-webpack-problems-the-practical-case-79fb676417f4). Ci-dessous, je vous fournirai un spoiler et une explication de la manière dont j'ai résolu ce problème.

Si nous allons maintenant créer une erreur dans notre code, cela sera affiché dans la console et nous pointera vers le bon endroit :

![Image](https://cdn-media-1.freecodecamp.org/images/wXVCuAbBa8BcSY6jrZGSCa6HwOFW0I9hUZM8)

... ou du moins, c'est ce que nous pensions. Mais non :

![Image](https://cdn-media-1.freecodecamp.org/images/tCFjvqd9RKbsqtS2XkXqNp0rX0i9TeHjlpTI)
_Ce comportement est incorrect_

Vous devez changer la variable d'environnement comme ceci :

```
..."main": "index.js","scripts": {  "build": "webpack --mode=production",  "start": "NODE_ENV=development webpack-dev-server --mode=development --hot"},"author": ""...
```

_webpack.config.js_

```
...devtool: 'inline-source-map',devServer: {  contentBase: './dist',  open: true}...
```

Maintenant, ça marche !

![Image](https://cdn-media-1.freecodecamp.org/images/Jf8CqfuPZHFJEop3n61YRBRhBFgrzG07TdSb)
_Comme vous pouvez le voir, nous sommes dirigés vers le fichier exact où l'erreur s'est produite !_

Vous avez maintenant configuré avec succès l'environnement de développement pour votre projet !

Faisons un récapitulatif :

* Nous avons configuré webpack
* Nous avons créé notre premier composant React
* Nous avons inclus ESLint pour vérifier le code pour les erreurs
* Nous avons configuré le remplacement de module à chaud
* Nous avons (peut-être) ajouté des cartes sources

**Note** : puisque beaucoup de dépendances npm peuvent changer au moment où vous lisez ceci, la même configuration peut ne pas fonctionner pour vous. Je vous demande gentiment de laisser vos erreurs dans les commentaires ci-dessous afin que je puisse les corriger plus tard.

**Veuillez vous abonner et applaudir pour cet article ! Merci !**

**Plus de matériaux :**

[**SurviveJS — Webpack**](https://survivejs.com/webpack/)  
[_Après des semaines d'échec de configuration de webpack, je suis tombé sur le livre SurviveJS en cherchant un autre tutoriel..._survivejs.com](https://survivejs.com/webpack/)[**Un guide du débutant pour Webpack 4 et le bundling de modules — SitePoint**](https://www.sitepoint.com/beginners-guide-webpack-module-bundling/)  
[_Webpack est un bundler de modules. Son but principal est de bundler des fichiers JavaScript pour une utilisation dans un navigateur, mais il est également..._www.sitepoint.com](https://www.sitepoint.com/beginners-guide-webpack-module-bundling/)
---
title: Comment créer votre propre boilerplate React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-24T16:13:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-own-react-boilerplate-2f8cbbeb9b3f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g3L9F6AO-jUW-QuQRFI3JA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer votre propre boilerplate React
seo_desc: 'By Nick Karnik

  What is a Boilerplate?

  In programming, the term boilerplate code refers to blocks of code used over and
  over again.

  Let’s assume your development stack consists of several libraries, such as React,
  Babel, Express, Jest, Webpack, etc. W...'
---

Par Nick Karnik

### Qu'est-ce qu'un Boilerplate ?

En programmation, le terme "boilerplate code" fait référence à des blocs de code utilisés encore et encore.

Supposons que votre stack de développement se compose de plusieurs bibliothèques, telles que React, Babel, Express, Jest, Webpack, etc. Lorsque vous commencez un nouveau projet, vous initialisez toutes ces bibliothèques et les configurez pour qu'elles fonctionnent ensemble.

Avec chaque nouveau projet que vous commencez, vous allez vous répéter. Vous pourriez également introduire des incohérences dans la façon dont ces bibliothèques sont configurées dans chaque projet. Cela peut causer de la confusion lorsque vous passez d'un projet à l'autre.

C'est là que les boilerplates interviennent. Un boilerplate est un modèle que vous pouvez cloner et réutiliser pour chaque projet.

L'écosystème Javascript modulaire simplifie le développement d'applications grâce à diverses bibliothèques, frameworks et outils. Les boilerplates peuvent être intimidants si vous ne comprenez pas les fondamentaux de leurs composants sous-jacents. Apprenons-en davantage sur ces blocs de construction de base tout en créant le nôtre.

> [_Cliquez ici pour la source sur GitHub_](https://github.com/theoutlander/react-boilerplate)

> J'utilise Webstorm, Git, NodeJS 8.9, NPM 5.6, et React 16. Lancez votre IDE préféré, créez un projet vide, et commençons !

### Dépôt Git : Installation

Créez un dossier de projet et initialisez un dépôt Git :

```
mkdir react-boilerplate && cd react-boilerplategit init
```

> Vous pouvez connecter ce projet à votre propre dépôt sur GitHub en utilisant [ces instructions](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/).

### Fichier Readme

Chaque projet doit contenir une page d'accueil avec des instructions utiles pour les autres développeurs. Créons un fichier README.md sous la racine du projet avec le contenu suivant :

```
# React-BoilerplateCeci est mon react-boilerplate
```

```
## Installationnpm installnpm run buildnpm start
```

GitHub affiche le contenu du fichier readme sur la page d'accueil du projet.

Maintenant, validez les modifications ci-dessus dans Git :

```
git add .git commit -m "created readme"
```

À la fin de chaque section, vous devez valider votre code dans Git.

### Structure des dossiers

Créez la structure de dossiers suivante pour votre projet :

```
react-boilerplate    |--src       |--client       |--server
```

avec la commande :

```
mkdir -p src/client src/server
```

Cette structure de dossiers est basique et évoluera à mesure que vous intégrerez d'autres bibliothèques dans le projet.

### Git Ignore

Une fois que nous avons construit notre projet, il y aura quelques fichiers et dossiers générés automatiquement. Disons à Git d'ignorer certains de ces fichiers auxquels nous pouvons penser à l'avance.

Créez .gitignore sous le dossier racine avec le contenu suivant :

```
# Nodenode_modules/
```

```
# Webstorm.idea/
```

```
# Projetdist/
```

Les commentaires dans un fichier .gitignore sont précédés de #.

### Gestionnaire de paquets Node

Le point de départ pour un projet node est d'initialiser son gestionnaire de paquets qui crée un fichier appelé package.json. Ce fichier doit être validé dans Git.

Il contient généralement :

* Une description de votre projet pour NPM
* Liste des références à tous les paquets installés
* Scripts de ligne de commande personnalisés
* Configuration pour les paquets installés

Allez à la racine de votre projet et tapez ce qui suit :

```
npm init
```

Remplissez tous les détails, et après les avoir acceptés, npm créera un fichier package.json qui ressemble à ceci :

```
{  "name": "react-boilerplate",  "version": "1.0.0",  "description": "Basic React Boilerplate",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "repository": {    "type": "git",    "url": "git+https://github.com/theoutlander/react-boilerplate.git"  },  "keywords": [    "Node",    "React"  ],  "author": "Nick Karnik",  "license": "Apache-2.0",  "bugs": {    "url": "https://github.com/theoutlander/react-boilerplate/issues"  },  "homepage": "https://github.com/theoutlander/react-boilerplate#readme"}
```

### Contenu statique

Créons un fichier HTML statique src/client/index.html avec le contenu suivant :

```
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>React Boilerplate</title></head><body>    <div id="root">        Bienvenue dans React Boilerplate !    </div></body></html>
```

### Serveur Web Express

Pour servir le fichier statique ci-dessus, nous devons créer un serveur web dans [ExpressJS](http://expressjs.com/).

> NPM v5 sauvegarde automatiquement les paquets installés sous la section des dépendances dans package.json, donc l'attribut --save n'est pas nécessaire

```
npm install express
```

Je recommanderais de suivre une convention de nommage où les noms de fichiers sont en minuscules et les mots multiples sont séparés par un point. Vous éviterez ainsi les problèmes de sensibilité à la casse sur différentes plateformes, et simplifierez également la nomination des fichiers avec plusieurs mots au sein de grandes équipes.

Créez un fichier src/server/web.server.js et ajoutez le code suivant pour héberger un serveur web via une application express et servir le fichier HTML statique :

```
const express = require('express')
```

```
export default class WebServer {  constructor () {    this.app = express()    this.app.use(express.static('dist/public'))  }
```

```
  start () {    return new Promise((resolve, reject) => {      try {        this.server = this.app.listen(3000, function () {          resolve()        })      } catch (e) {        console.error(e)        reject(e)      }    })  }
```

```
  stop () {    return new Promise((resolve, reject) => {      try {        this.server.close(() => {          resolve()        })      } catch (e) {        console.error(e.message)        reject(e)      }    })  }}
```

Nous avons créé un simple serveur web ci-dessus avec une commande de démarrage et d'arrêt.

[Cliquez ici pour en savoir plus sur les Promesses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

### Fichier de démarrage

Ensuite, nous devons créer un fichier d'index qui initialisera divers composants de haut niveau. Dans notre exemple, nous allons initialiser le serveur web. Cependant, à mesure que votre projet grandit, vous pouvez également initialiser d'autres composants tels que la configuration, la base de données, le logger, etc.

Créez un fichier src/server/index.js avec le code suivant :

```
import WebServer from './web.server'
```

```
let webServer = new WebServer();webServer.start()  .then(() => {    console.log('Serveur web démarré !')  })  .catch(err => {    console.error(err)    console.error('Échec du démarrage du serveur web')  });
```

### Babel

Pour exécuter le code [ES6](http://es6-features.org/) ci-dessus, nous devons d'abord le transformer en [ES5](https://es5.github.io/) via Babel. Installons [Babel](http://babeljs.io/) et la dépendance [babel-preset-env](https://github.com/babel/babel/tree/master/experimental/babel-preset-env) qui prend en charge la transpilation ES2015 :

```
npm i babel-cli babel-preset-env --save-dev
```

Créez un fichier de configuration Babel appelé .babelrc sous la racine et ajoutez les détails suivants :

```
{  "presets": ["env"]}
```

Le preset env inclut implicitement babel-preset-es2015, babel-preset-es2016 et babel-preset-es2017 ensemble, ce qui signifie que vous pouvez exécuter du code ES6, ES7 et ES8.

### Commandes de construction

Créons des commandes pour construire les composants serveur et client du projet et démarrer le serveur. Sous la section scripts de package.json, supprimez la ligne avec la commande test et ajoutez ce qui suit :

```
"scripts": {    "build": "npm run build-server && npm run build-client",    "build-server": "babel src/server --out-dir ./dist",    "build-client": "babel src/client --copy-files --out-dir ./dist/public",    "start": "node ./dist/index.js"}
```

La commande build ci-dessus créera un dossier dist/public sous la racine. La commande build-client copie simplement le fichier index.html dans le dossier dist/public.

### Démarrage

Vous pouvez exécuter le transpileur Babel sur le code ci-dessus et démarrer le serveur web en utilisant les commandes suivantes :

```
npm run buildnpm start
```

Ouvrez votre navigateur et accédez à [http://localhost:3000](http://localhost:3000/). Vous devriez voir le résultat de votre fichier HTML statique.

![Image](https://cdn-media-1.freecodecamp.org/images/0*u2ynUivrvLjs-av0.png)

Vous pouvez arrêter le serveur web en appuyant sur <Ctrl> C

### Harnais de test : Jest

Je ne peux pas assez insister sur l'importance d'introduire des tests unitaires dès le début d'un projet. Nous allons utiliser le [Framework de test Jest](https://facebook.github.io/jest/) qui est conçu pour être rapide et convivial pour les développeurs.

Tout d'abord, nous devons installer Jest et l'enregistrer dans les dépendances de développement.

```
npm i jest --save-dev
```

### Tests unitaires

Ajoutons deux cas de test pour démarrer et arrêter le serveur web.

Pour les fichiers de test, vous devez ajouter une extension .test.js. Jest analysera le dossier src pour tous les fichiers contenant .test dans le nom de fichier, vous pouvez garder vos cas de test sous le même dossier que les fichiers qu'ils testent.

Créez un fichier appelé src/server/web.server.test.js et ajoutez le code suivant :

```
import WebServer from './web.server'
```

```
describe('Started', () => {  let webServer = null
```

```
  beforeAll(() => {    webServer = new WebServer()  })
```

```
  test('should start and trigger a callback', async () => {    let promise = webServer.start()    await expect(promise).resolves.toBeUndefined()  })
```

```
  test('should stop and trigger a callback', async () => {    let promise = webServer.stop()    await expect(promise).resolves.toBeUndefined()  })})
```

### Commande de test

Ajoutons une commande npm pour exécuter le test sous la section scripts de package.json. Par défaut, Jest exécute tous les fichiers contenant le mot .test dans leur nom de fichier. Nous voulons le limiter à l'exécution des tests sous le dossier src.

```
"scripts": {...    "test": "jest ./src"...}
```

Babel-jest est automatiquement installé lors de l'installation de Jest et transformera automatiquement les fichiers si une configuration Babel existe dans votre projet.

Exécutons nos tests via la commande suivante :

```
npm test
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*4OQroTGQMuSlEg3j.png)

Notre application est configurée pour servir un fichier HTML statique via un serveur web Express. Nous avons intégré Babel pour activer ES6 et Jest pour les tests unitaires. Concentrons-nous maintenant sur la configuration du front-end.

### Configuration de React

Installez les bibliothèques react et react-dom :

```
npm i react react-dom
```

Créez un fichier appelé src/client/app.js avec :

```
import React, {Component} from 'react'
```

```
export default class App extends Component {    render() {        return <div>Bienvenue dans l'application React Boilerplate</div>    }}
```

Rendons l'application App via un fichier d'index sous src/client/index.js avec :

```
import React from 'react'import ReactDOM from 'react-dom'import App from './app'
```

```
ReactDOM.render(<App />, document.getElementById('root'))
```

### Babel React

Si vous exécutez npm run build-client, vous obtiendrez une erreur car nous n'avons pas dit à Babel comment gérer React / JSX.

![Image](https://cdn-media-1.freecodecamp.org/images/0*W-9sbHjloV7lyDfq.png)

Corrigeons cela en installant la dépendance [babel-preset-react](http://babeljs.io/docs/plugins/preset-react/) :

```
npm install --save-dev babel-preset-react
```

Nous devons également modifier le fichier de configuration .babelrc pour activer la transpilation de react :

```
{  "presets": ["env", "react"]}
```

Maintenant, lorsque vous exécutez npm run build-client, il créera app.js et index.js sous dist/public avec le code ES6 transpilé en ES5.

### Charger le script dans HTML

Pour connecter notre application React au fichier HTML, nous devons charger index.js dans notre fichier index.html. N'oubliez pas de vider le texte du nœud #root puisque l'application React sera montée dessus :

```
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>React Boilerplate</title></head><body>    <div id="root"></div>    <script src="index.js"></script></body></html>
```

### Exécuter le serveur

Si vous lancez votre serveur web et allez sur [http://localhost:3000](http://localhost:3000/), vous verrez une page blanche avec une erreur dans la console.

Uncaught ReferenceError: require is not defined.

![Image](https://cdn-media-1.freecodecamp.org/images/0*C0et_W8a6-CIWpJK.png)

C'est parce que Babel est juste un transpileur. Pour supporter le chargement dynamique des modules, nous devons installer Webpack.

Commencez par changer les commandes de construction sous scripts dans package.json en build-babel :

```
"scripts": {    "build-babel": "npm run build-babel-server && npm run build-babel-client",    "build-babel-server": "babel src/server --out-dir ./dist",    "build-babel-client": "babel src/client --copy-files --out-dir ./dist/public",    "start": "node ./dist/index.js",    "test": "jest ./src"  }
```

### Webpack

Webpack nous permet de modulariser facilement notre code et de le regrouper en un seul fichier Javascript. Il est soutenu par de nombreux plugins, et il y a de fortes chances qu'il existe un plugin pour presque toutes les tâches de construction que vous pouvez imaginer. Commencez par installer Webpack :

> Ce tutoriel a été publié juste avant la sortie de webpack v4, nous allons donc installer explicitement webpack v3.

```
npm i webpack@^3
```

Par défaut, Webpack recherche un fichier de configuration appelé webpack.config.js, alors créons-le dans le dossier racine et définissons deux points d'entrée, un pour l'application web et l'autre pour le serveur web. Créons deux objets de configuration et exportons-les comme une collection :

```
const client = {    entry: {        'client': './src/client/index.js'    }};
```

```
const server = {    entry: {        'server': './src/server/index.js'    }};
```

```
module.exports = [client, server];
```

Maintenant, spécifions où Webpack va sortir le bundle et définissons la cible de construction [target](https://webpack.js.org/concepts/targets/) afin qu'il ignore les modules natifs de node comme 'fs' et 'path' pour qu'ils ne soient pas bundlés. Pour le client, nous allons le définir sur web, et pour le serveur nous allons le définir sur node.

```
let path = require('path');
```

```
const client = {    entry: {        'client': './src/client/index.js'    },    target: 'web',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist/public')    }};
```

```
const server = {    entry: {        'server': './src/server/index.js'    },    target: 'node',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist')    }};
```

```
module.exports = [client, server];
```

### Babel Loader

Avant de pouvoir exécuter Webpack, nous devons le configurer pour gérer le code ES6 et JSX. Cela se fait via des loaders. Commençons par installer [babel-loader](https://github.com/babel/babel-loader) :

```
npm install babel-loader --save-dev
```

Nous devons modifier la configuration de Webpack pour inclure babel-loader afin qu'il s'exécute sur tous les fichiers .js. Nous allons créer un objet partagé définissant la section module que nous pouvons réutiliser pour les deux cibles.

```
const path = require('path');
```

```
const moduleObj = {    loaders: [        {            test: /\.js$/,            exclude: /node_modules/,            loaders: ["babel-loader"],        }    ],};
```

```
const client = {    entry: {        'client': './src/client/index.js',    },    target: 'web',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist/public')    },    module: moduleObj};
```

```
const server = {    entry: {        'server': './src/server/index.js'    },    target: 'node',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist')    },    module: moduleObj}
```

```
module.exports = [client, server];
```

Pour fusionner des objets partagés imbriqués, je recommande de consulter le module [Webpack Merge](https://github.com/survivejs/webpack-merge).

### Exclusion de fichiers

Webpack va bundler les bibliothèques référencées, ce qui signifie que tout ce qui est inclus depuis node_modules sera empaqueté. Nous n'avons pas besoin de bundler le code externe, car ces paquets sont généralement minifiés, et ils augmenteront également le temps et la taille de la construction.

Configurons Webpack pour exclure tous les paquets sous le dossier node_modules. Cela est facilement accompli via le module [webpack-node-externals](https://www.npmjs.com/package/webpack-node-externals) :

```
npm i webpack-node-externals --save-dev
```

Suivi de la configuration de webpack.config.js pour l'utiliser :

```
let path = require('path');let nodeExternals = require('webpack-node-externals');
```

```
const moduleObj = {    loaders: [        {            test: /\.js$/,            exclude: /node_modules/,            loaders: ["babel-loader"],        }    ],};
```

```
const client = {    entry: {        'client': './src/client/index.js',    },    target: 'web',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist')    },    module: moduleObj};
```

```
const server = {    entry: {        'server': './src/server/index.js'    },    target: 'node',    output: {        filename: '[name].js',        path: path.resolve(__dirname, 'dist')    },    module: moduleObj,    externals: [nodeExternals()]}
```

```
module.exports = [client, server];
```

### Mettre à jour la commande de construction

Enfin, nous devons apporter des modifications à la section scripts sous package.json pour inclure une commande de construction qui utilise Webpack, et pour renommer index.js en server.js pour npm start car c'est ce que Webpack est configuré pour produire.

```
"scripts": {    "build": "webpack",    "build-babel": "npm run build-babel-server && npm run build-babel-client",    "build-babel-server": "babel src/server --out-dir ./dist",    "build-babel-client": "babel src/client --copy-files --out-dir ./dist/public",    "start": "node ./dist/server.js",    "test": "jest ./src"  }
```

### Construction propre

Ajoutons une commande pour nettoyer nos dossiers dist et node_modules afin que nous puissions faire une construction propre et nous assurer que notre projet fonctionne toujours comme prévu. Avant de pouvoir faire cela, nous devons installer un package appelé [rimraf](https://github.com/isaacs/rimraf) (qui est la commande rm -rf).

```
npm install rimraf
```

La section scripts doit maintenant contenir :

```
"scripts": {..."clean": "rimraf dist node_modules",...}
```

### Construction propre avec Webpack

Vous pouvez maintenant nettoyer et construire votre projet avec succès en utilisant Webpack :

```
npm run cleannpm installnpm run build
```

Cela créera dist/server.js et dist/public/client.js sous le dossier racine.

### Plugin HTML Webpack

Cependant, vous avez peut-être remarqué que index.html est manquant. C'est parce que, précédemment, nous avons demandé à Babel de copier les fichiers qui n'étaient pas transpilés. Cependant, Webpack n'est pas capable de faire cela, donc nous devons utiliser le [HTML Webpack Plugin](https://github.com/jantimon/html-webpack-plugin).

Installons le HTML Webpack Plugin :

```
npm i html-webpack-plugin --save-dev
```

Nous devons inclure le plugin en haut du fichier de configuration webpack :

```
const HtmlWebPackPlugin = require('html-webpack-plugin')
```

Ensuite, nous devons ajouter une clé plugins à la configuration client :

```
const client = {  entry: {    'client': './src/client/index.js'  },  target: 'web',  output: {    filename: '[name].js',    path: path.resolve(__dirname, 'dist/public')  },  module: moduleObj,  plugins: [    new HtmlWebPackPlugin({      template: 'src/client/index.html'    })  ]}
```

Avant de construire le projet, modifions notre fichier HTML et supprimons la référence au script index.js, car le plugin ci-dessus l'ajoutera pour nous. Cela est particulièrement utile lorsqu'il y a un ou plusieurs fichiers avec des noms de fichiers dynamiques (par exemple lorsque les fichiers sont générés avec un timestamp unique pour le cache busting).

```
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>React Boilerplate</title></head><body>    <div id="root"></div></body></html>
```

Reconstruisons le projet :

```
npm run cleannpm installnpm run build
```

Et, vérifions que nos tests existants sont toujours en cours d'exécution :

```
npm test
```

Nous avons mis à jour le boilerplate pour intégrer React et Webpack, créé des commandes NPM supplémentaires, référencé dynamiquement index.js dans le fichier HTML, et exporté.

### Configuration d'Enzyme

Avant d'ajouter un test React, nous devons intégrer [Enzyme](https://github.com/airbnb/enzyme), qui nous permettra d'affirmer, de manipuler et de parcourir les composants react.

Commençons par installer Enzyme et enzyme-adapter-react-16, qui est requis pour connecter Enzyme à un projet utilisant react v16 et au-dessus.

> _enzyme-adapter-react-16 a des dépendances de pairs sur react, react-dom, et react-test-renderer_

```
npm i --save-dev enzyme enzyme-adapter-react-16 react-test-renderer
```

Créez un fichier src/enzyme.setup.js avec le contenu suivant :

```
import Enzyme from 'enzyme'import Adapter from 'enzyme-adapter-react-16'
```

```
Enzyme.configure({    adapter: new Adapter()})
```

Nous devons configurer Jest pour utiliser src/enzyme.setup.js dans package.json en ajoutant la section suivante sous l'objet racine :

```
{..."jest": {    "setupTestFrameworkScriptFile": "./src/enzyme.setup.js"  }...}
```

### Test de composant React

Testons le composant App et assurons-nous qu'il rend le texte attendu. De plus, nous allons prendre un instantané de ce composant afin de pouvoir nous assurer que sa structure n'a pas changé avec chaque exécution de test.

[Cliquez ici pour en savoir plus sur les tests d'instantanés](https://facebook.github.io/jest/docs/en/snapshot-testing.html).

Créez un cas de test sous src/client/app.test.js avec le contenu suivant :

```
import App from './app'import React from 'react'import {shallow} from 'enzyme'
```

```
describe('App', () => {  test('should match snapshot', () => {    const wrapper = shallow(&lt;App/>)
```

```
    expect(wrapper.find('div').text()).toBe('Welcome to React Boilerplate App')    expect(wrapper).toMatchSnapshot()  })})
```

Si nous exécutons ce test maintenant, il passera avec un avertissement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*y44uqej9jGRMqLOm0lmRWw.png)

Corrigeons cela en installant un polyfill appelé [raf](https://github.com/chrisdickinson/raf) :

```
npm i --saveDev raf
```

Et en changeant la configuration Jest sous package.json en :

```
{..."jest": {    "setupTestFrameworkScriptFile": "./src/enzyme.setup.js",    "setupFiles": ["raf/polyfill"]  }...}
```

Maintenant, vous pouvez vérifier que tous nos tests passent :

```
npm test
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*IK1jRFuIfXrdkmez.png)

Après avoir exécuté le test react, vous remarquerez un nouveau fichier à src/client/snapshots/app.test.js.snap. Il contient la structure sérialisée de notre composant react. Il doit être validé dans Git afin qu'il puisse être utilisé pour comparer avec l'instantané généré dynamiquement lors d'une exécution de test.

### Exécution finale

Démarrons le serveur web une dernière fois et naviguons vers [http://localhost:3000](http://localhost:3000/) pour nous assurer que tout fonctionne :

```
npm start 
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*oNefrz8voxKjaDNY.png)

J'espère que cet article vous a donné des informations sur la rationalisation du processus de démarrage d'un nouveau projet à partir de zéro avec Express | React | Jest | Webpack | Babel. Il est bon de créer votre propre boilerplate réutilisable afin de comprendre ce qui se passe sous le capot, et en même temps de prendre une longueur d'avance lors de la création de nouveaux projets.

Nous avons à peine effleuré la surface et il y a beaucoup de place pour l'amélioration afin de rendre ce boilerplate prêt pour la production.

Voici quelques choses à essayer :

* Activer le [cache busting](https://webpack.js.org/guides/caching/) dans Webpack
* Bundling de fichiers CSS en utilisant [css-loader dans webpack](https://github.com/webpack-contrib/css-loader)
* [Activer](https://github.com/webpack-contrib/css-loader) les source maps dans webpack
* Ajouter des [commandes de débogage](https://nodejs.org/en/docs/guides/debugging-getting-started/) à package.json
* [Hot module replacement](https://webpack.js.org/concepts/hot-module-replacement/)
* Redémarrage automatique du serveur web lorsque des changements sont détectés via [nodemon](https://github.com/remy/nodemon)

Si vous souhaitez en savoir plus sur l'écosystème react, je vous recommande vivement de suivre [The Complete React Web Developer Course](https://www.udemy.com/react-2nd-edition/?couponCode=LEARNING) par [Andrew Mead](https://www.freecodecamp.org/news/how-to-build-your-own-react-boilerplate-2f8cbbeb9b3f/undefined).

#### Si cet article vous a été utile, ??? et suivez-moi sur Twitter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-sqS5Sd479XE60HoKAn0g.jpeg)
_[Cycle de vie des composants React](https://twitter.com/intent/follow?screen_name=theoutlander" rel="noopener" target="_blank" title="">Vous aimerez peut-être aussi mon tutoriel YouTube sur </a><a href="https://youtu.be/7iHepe36m0c" rel="noopener" target="_blank" title=")_
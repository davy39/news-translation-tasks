---
title: Comment créer une application Vue.js en utilisant des composants mono-fichier,
  sans le CLI.
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2018-12-04T20:48:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-vue-js-app-using-single-file-components-without-the-cli-7e73e5b8244f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*L2343t5yIriMN69KY6jWEw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: ' Single Page Applications '
  slug: single-page-applications
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
- name: webpack
  slug: webpack
seo_title: Comment créer une application Vue.js en utilisant des composants mono-fichier,
  sans le CLI.
seo_desc: 'An understanding of Vue’s single-file components (SFCs) and Node Package
  Manager (NPM) will be helpful for this article.

  A framework’s command line interface, or CLI, is the preferred method to scaffold
  a project. It provides a starting point of file...'
---

*Une compréhension des composants mono-fichier (SFCs) de Vue et du gestionnaire de paquets Node (NPM) sera utile pour cet article.*

L'interface en ligne de commande (CLI) d'un framework est la méthode préférée pour échafauder un projet. Elle fournit un point de départ de fichiers, de dossiers et de configuration. Cet échafaudage fournit également un processus de développement et de construction. Un processus de développement permet de voir les mises à jour se produire au fur et à mesure que vous modifiez votre projet. Le processus de construction crée la version finale des fichiers à utiliser en production.

L'installation et l'exécution de Vue.js ("Vue") peuvent être effectuées avec une balise de script qui pointe vers le réseau de diffusion de contenu (CDN) de Vue. Aucun processus de construction ou de développement n'est nécessaire. Mais, si vous utilisez des composants mono-fichier de Vue (SFCs), vous devez convertir ces fichiers en quelque chose que le navigateur peut comprendre. Les fichiers doivent être convertis en Hyper-Text Markup Language (HTML), Cascading Style Sheets (CSS) et JavaScript (JS). Dans ce cas, un processus de développement et de construction doit être utilisé.

Au lieu de nous appuyer sur le CLI de Vue pour échafauder notre projet et nous fournir un processus de développement et de construction, nous allons construire un projet à partir de zéro. Nous allons créer notre propre processus de développement et de construction en utilisant Webpack.

#### Qu'est-ce que Webpack ?

Webpack est un bundler de modules. Il fusionne le code de plusieurs fichiers en un seul. Avant Webpack, l'utilisateur incluait une balise de script pour chaque fichier JavaScript. Bien que les navigateurs *commencent lentement* à supporter les modules ES6, Webpack continue d'être la manière préférée de construire du code modulaire.

En plus d'être un bundler de modules, Webpack peut également transformer du code. Par exemple, Webpack peut prendre du JavaScript moderne (ECMAScript 6+) et le convertir en ECMAScript 5. Alors que Webpack *bundle* le code lui-même, il transforme le code avec des loaders et des plugins. Considérez les loaders et les plugins comme des add-ons pour Webpack.

#### Webpack et Vue

Les composants mono-fichier nous permettent de construire un composant entier (structure, style et fonction) dans un seul fichier. Et, la plupart des éditeurs de code fournissent une coloration syntaxique et un linting pour ces SFCs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*anBAz9QzClNtmAxp4ujdGA.png align="left")

[Composant Mono-Fichier Vue](https://vuejs.org/v2/guide/single-file-components.html" rel="noopener" target="*blank" title="): remarquez l'extension .vue.*

*Remarquez que le fichier se termine par .vue. Le navigateur ne sait pas quoi faire avec cette extension. Webpack, grâce à l'utilisation de loaders et de plugins, transforme ce fichier en HTML, CSS et JS que le navigateur peut consommer.*

### Le Projet : Construire une Application Hello World Vue en Utilisant des Composants Mono-Fichier.

#### Étape 1 : Créer la structure du projet

Le projet Vue le plus basique inclura un fichier HTML, JavaScript et un fichier Vue (le fichier se terminant par *.vue*). Nous placerons ces fichiers dans un **dossier appelé** `src`. Le dossier source nous aidera à séparer le code que nous écrivons du code que Webpack construira éventuellement.

Puisque nous utiliserons Webpack, nous avons besoin **d'un fichier de configuration Webpack**.

De plus, nous utiliserons un compilateur appelé Babel. Babel nous permet d'écrire du code ES6 qu'il compile ensuite en ES5. Babel est l'une de ces "fonctionnalités supplémentaires" pour Webpack. **Babel a également besoin d'un fichier de configuration.**

Enfin, puisque nous utilisons NPM, nous aurons également **un dossier node_modules** et **un fichier package.json**. Ceux-ci seront créés automatiquement lorsque nous initialiserons notre projet en tant que projet NPM et commencerons à installer nos dépendances.

Pour commencer, créez un dossier appelé `hello-world`. À partir de la ligne de commande, changez de répertoire et exécutez `npm init`. Suivez les invites à l'écran pour créer le projet. Ensuite, créez le reste des dossiers (sauf pour `node_modules`*)* comme décrit ci-dessus. La structure de votre projet devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jLNggGBoQ6A6xnqVyltFEA.png align="left")

*La structure de projet SFC Vue la plus simple.*

#### Étape 2 : Installer les dépendances

Voici un bref aperçu des dépendances que nous utilisons :

**vue** : Le framework JavaScript

**vue-loader et vue-template-compiler** : Utilisés pour convertir nos fichiers Vue en JavaScript.

**webpack** : L'outil qui nous permettra de faire passer notre code à travers certaines transformations et de le bundler en un seul fichier.

**webpack-cli** : Nécessaire pour exécuter les commandes Webpack.

**webpack-dev-server** : Bien que non nécessaire pour notre petit projet (puisque nous ne ferons aucune requête HTTP), nous "servirons" toujours notre projet à partir d'un serveur de développement.

**babel-loader** : Transforme notre code ES6 en ES5. (Il a besoin de l'aide des deux dépendances suivantes.)

**@babel/core et @babel/preset-env** : Babel seul ne fait rien à votre code. Ces deux "add-ons" nous permettront de transformer notre code ES6 en code ES5.

**css-loader** : Prend le CSS que nous écrivons dans nos fichiers `.vue` ou tout CSS que nous pourrions importer dans l'un de nos fichiers JavaScript et résout le chemin vers ces fichiers. En d'autres termes, il détermine où se trouve le CSS. C'est un autre loader qui, seul, ne fera pas grand-chose. Nous avons besoin du loader suivant pour faire quelque chose avec le CSS.

**vue-style-loader** : Prend le CSS que nous avons obtenu de notre `css-loader` et l'injecte dans notre fichier HTML. Cela créera et injectera une balise de style dans l'en-tête de notre document HTML.

**html-webpack-plugin** : Prend notre *index.html* et injecte notre fichier JavaScript bundlé dans l'en-tête. Ensuite, copie ce fichier dans le dossier `dist`.

**rimraf** : Nous permet, à partir de la ligne de commande, de supprimer des fichiers. Cela sera utile lorsque nous construirons notre projet plusieurs fois. Nous utiliserons cela pour supprimer les anciennes constructions.

Installons ces dépendances maintenant. À partir de la ligne de commande, exécutez :

```bash
npm install vue vue-loader vue-template-compiler webpack webpack-cli webpack-dev-server babel-loader @babel/core @babel/preset-env css-loader vue-style-loader html-webpack-plugin rimraf -D
```

***Note :*** *Le "-D" à la fin marque chaque dépendance comme une dépendance de développement dans notre package.json. Nous bundlons toutes les dépendances en un seul fichier, donc, pour notre petit projet, nous n'avons pas de dépendances de production.*

#### Étape 3 : Créer les fichiers (sauf pour notre fichier de configuration Webpack).

```js
<template>
  <div id="app">
    {{ message }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello World',
    };
  },
};
</script>

<style>
#app {
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  color: blue;
}
</style>
```

```html
<html>
  <head>
    <title>Vue Hello World</title>
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>
```

```js
import Vue from 'vue';
import App from './App.vue';

new Vue({
  el: '#app',
  render: h => h(App),
});
```

```js
module.exports = {
  presets: ['@babel/preset-env'],
}
```

Jusqu'à présent, rien ne devrait sembler trop étranger. J'ai gardé chaque fichier très basique. J'ai seulement ajouté un minimum de CSS et de JS pour voir notre flux de travail en action.

#### Étape 4 : Instruire Webpack sur ce qu'il doit faire

Toute la configuration dont Webpack a besoin est maintenant présente. Nous devons faire deux choses finales : dire à Webpack quoi faire et exécuter Webpack.

Voici le fichier de configuration Webpack (`webpack.config.js`). Créez ce fichier dans le répertoire racine du projet. Ligne par ligne, nous discuterons de ce qui se passe.

```js
const HtmlWebpackPlugin = require('html-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
  entry: './src/main.js',
  module: {
    rules: [
      { test: /\.js$/, use: 'babel-loader' },
      { test: /\.vue$/, use: 'vue-loader' },
      { test: /\.css$/, use: ['vue-style-loader', 'css-loader']},
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    }),
    new VueLoaderPlugin(),
  ]
};
```

**Lignes 1 et 2 :** Nous importons les deux plugins que nous utilisons ci-dessous. Remarquez, nos loaders n'ont généralement pas besoin d'être importés, juste nos plugins. Et dans notre cas, le `vue-loader` (que nous utilisons à la ligne 9) a également besoin d'un plugin pour fonctionner (Cependant, Babel, par exemple, n'en a pas besoin).

**Ligne 4 :** Nous exportons notre configuration sous forme d'objet. Cela nous donne accès à celle-ci lorsque nous exécutons les commandes Webpack.

**Ligne 5 :** C'est notre module d'entrée. Webpack a besoin d'un point de départ. Il regarde dans notre fichier `main.js` et commence ensuite à parcourir notre code à partir de ce point.

**Ligne 6 et 7 :** C'est l'objet module. Ici, nous passons principalement un tableau de règles. Chaque règle indique à Webpack comment gérer certains fichiers. Ainsi, alors que Webpack utilise le point d'entrée de `main.js` pour commencer à parcourir notre code, il utilise les règles pour transformer notre code.

**Ligne 8 (règle) :** Cette règle indique à Webpack d'utiliser le `babel-loader` sur tous les fichiers se terminant par `.js`*.* Rappelez-vous, Babel transformera ES6+ en ES5.

**Ligne 9 (règle) :** Cette règle indique à Webpack d'utiliser `vue-loader` (et n'oubliez pas le plugin associé à la ligne 17) pour transformer nos fichiers `.vue` en JavaScript.

**Ligne 10 (règle) :** Parfois, nous voulons faire passer un fichier à travers deux loaders. De manière contre-intuitive, Webpack passera le fichier de droite à gauche au lieu de gauche à droite. Ici, nous utilisons deux loaders et disons à Webpack : "obtenez mon CSS de mon fichier Vue ou de tout fichier JavaScript (`css-loader`) et injectez-le dans mon HTML en tant que balise de style (`vue-style-loader`).

**Lignes 11 et 12 :** Fermons notre tableau de règles et notre objet module.

**Ligne 13 :** Créons un tableau de plugins. Ici, nous ajouterons les deux plugins dont nous avons besoin.

**Ligne 14-16 (plugin) :** Le `HtmlWebpackPlugin` prend l'emplacement de notre fichier *index.html* et ajoute notre fichier JavaScript bundlé via une balise de script. Ce plugin copiera également le fichier HTML dans notre dossier de distribution lorsque nous construirons notre projet.

**Ligne 17 (plugin) :** Le `VueLoaderPlugin` fonctionne avec notre `vue-loader` pour analyser nos fichiers `.vue`.

**Ligne 18 :** Fermons le tableau de plugins.

**Ligne 19 :** Fermons l'objet Webpack que nous exportons.

#### Étape 5 : Configurer notre fichier package.json pour pouvoir exécuter Webpack

Notre configuration est complète, maintenant nous voulons voir notre application. Idéalement, à mesure que nous apportons des modifications à notre application, le navigateur se mettra à jour automatiquement. Cela est possible avec `webpack-dev-server`.

Supprimez le script `test` dans notre fichier `package.json`, et remplacez-le par un script pour servir notre application :

```json

{
  "name": "hello-world",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "scripts": {
    "serve": "webpack-dev-server --mode development"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@babel/core": "^7.1.6",
    "@babel/preset-env": "^7.1.6",
    "babel-loader": "^8.0.4",
    "css-loader": "^1.0.1",
    "html-webpack-plugin": "^3.2.0",
    "rimraf": "^2.6.2",
    "vue": "^2.5.17",
    "vue-loader": "^15.4.2",
    "vue-style-loader": "^4.1.2",
    "vue-template-compiler": "^2.5.17",
    "webpack": "^4.26.0",
    "webpack-cli": "^3.1.2",
    "webpack-dev-server": "^3.1.10"
  },
  "dependencies": {}
}
```

Le nom de cette commande est votre choix. J'ai choisi de l'appeler `serve` puisque nous allons "servir" notre application.

À partir de notre terminal ou de la ligne de commande, nous pouvons exécuter `npm run serve` et cela exécutera à son tour `webpack-dev-server --mode development`.

*Le* `--mode development` est ce qu'on appelle un flag ou une option. Nous n'en avons pas parlé, mais il indique essentiellement à Webpack que vous êtes en mode développement. Nous pouvons également passer `--mode production` que nous ferons lorsque nous construirons notre projet. Ceux-ci ne sont pas nécessairement requis pour que Webpack fonctionne. Sans ceux-ci, vous recevrez un message d'avertissement vous demandant de fournir un mode lorsque vous exécutez Webpack.

*Je dis "nécessairement requis" parce que Webpack minimisera notre code en mode production mais pas en développement. Donc, ne pensez pas que ces commandes ne font rien – elles font quelque chose.*

Exécutons `npm run serve` et voyons ce qui se passe.

Lorsque nous exécutons `npm run serve`, nous obtenons une sortie dans notre terminal. Et, si tout se passe bien :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UNoqxigEpgvVZRjs2VqxTA.png align="left")

Et si nous faisons défiler un peu vers le haut :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ye4_gCeGPXcwgPcGUQf_rg.png align="left")

Pointez votre navigateur vers `http://localhost:8080`. Vous verrez votre message Hello World bleu dans la police Roboto.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kKYxmKJ_rTBzT7rOvjZtgg.png align="left")

Maintenant, mettons à jour le projet et changeons le message en `Hello Universe`. Remarquez que la page web se rafraîchit automatiquement. C'est bien, n'est-ce pas ? Pouvez-vous penser à un inconvénient ?

Changeons un peu l'application et incluons une entrée à laquelle nous lierons une variable (avec `v-model`). Nous afficherons la variable dans une balise `<h2>` sous l'entrée. J'ai également mis à jour la section de style pour styliser le message maintenant. Notre fichier `App.vue` devrait ressembler à ceci :

```js
<template>
  <div id="app">
    <input
      v-model="message"
      type="text">
      <h2 class="message">{{ message }}</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello world!',
    };
  },
};
</script>

<style>
.message {
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  color: blue;
}
</style>
```

Lorsque nous servons notre application, nous aurons une entrée avec un message `Hello World` en dessous. L'entrée est liée à la variable `message`, donc lorsque nous tapons, nous changeons le contenu de `<h2>`. Allez-y, tapez dans l'entrée pour changer le contenu de `<h2>`.

Maintenant, retournez à votre éditeur, et sous la balise `<h2>`, ajoutez ce qui suit :

`<h3>Some Other Message</h3>`

Enregistrez votre `App.vue` et regardez ce qui se passe.

Le `h2` que nous venons de mettre à jour en tapant dans notre entrée est revenu à `Hello World`. Cela est dû au fait que le navigateur se rafraîchit réellement, et la balise de script et la page sont rechargées. En d'autres termes, nous n'avons pas pu maintenir l'état de notre application. Cela peut ne pas sembler un gros problème, mais lorsque vous testez votre application et ajoutez des données, il sera frustrant si votre application "réinitialise" à chaque fois. Heureusement, Webpack nous offre une solution appelée Hot Module Replacement.

Le hot module replacement est un plugin fourni par Webpack lui-même. Jusqu'à présent, nous n'avons pas utilisé l'objet Webpack lui-même dans notre fichier de configuration. Cependant, nous allons maintenant importer Webpack afin de pouvoir accéder au plugin.

En plus du plugin, nous passerons une option supplémentaire à Webpack, l'option `devServer`. Dans cette option, nous définirons `hot` sur `true`. De plus, nous apporterons une mise à jour (optionnelle) à notre flux de travail de construction : nous ouvrirons automatiquement la fenêtre du navigateur lorsque nous exécuterons `npm run serve`. Nous faisons cela en définissant `open` sur `true` qui se trouve également dans l'option `devServer`.

```js
const HtmlWebpackPlugin = require('html-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const webpack = require('webpack');

module.exports = {
  entry: './src/main.js',
  module: {
    rules: [
      { test: /\.js$/, use: 'babel-loader' },
      { test: /\.vue$/, use: 'vue-loader' },
      { test: /\.css$/, use: ['vue-style-loader', 'css-loader']},
    ]
  },
  devServer: {
    open: true,
    hot: true,
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    }),
    new VueLoaderPlugin(),
    new webpack.HotModuleReplacementPlugin(),
  ]
};
```

Remarquez que nous avons importé Webpack afin de pouvoir accéder au `hotModuleReplacementPlugin`. Nous l'avons ajouté au tableau `plugins`, puis avons dit à Webpack de l'utiliser avec `hot: true`. Nous ouvrons automatiquement la fenêtre du navigateur lorsque nous servons l'application avec `open: true`.

Exécutez `npm run serve` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*59LVTDT3pEk3RzQ7dodmvw.png align="left")

La fenêtre du navigateur devrait s'ouvrir, et si vous ouvrez vos outils de développement, vous devriez remarquer un léger changement dans la sortie. Il nous indique maintenant que le hot module replacement est activé. Tapons dans notre entrée pour changer le contenu de `<h2>`. Ensuite, changez la balise `h3` pour qu'elle lise : `One More Message`.

Enregistrez votre fichier et remarquez ce qui se passe.

Le navigateur ne se rafraîchit pas, mais notre changement de `<h3>` est reflété ! Le message que nous avons tapé dans l'entrée reste, mais le `h3` se met à jour. Cela permet à notre application de conserver son état pendant que nous l'éditons.

#### Étape 7 : Construire notre projet

Jusqu'à présent, nous avons servi notre application. Mais, que faire si nous voulons construire notre application afin de pouvoir la distribuer ?

Si vous avez remarqué, lorsque nous servons notre application, aucun fichier n'est créé. Webpack crée une version de ces fichiers qui n'existe que dans la mémoire temporaire. Si nous voulons distribuer notre application Hello World à notre client, nous devons *construire* le projet.

C'est très simple. Tout comme avant, nous allons créer un script dans notre fichier package.json pour dire à Webpack de construire notre projet. Nous utiliserons `webpack` comme commande au lieu de `webpack-dev-server`. Nous passerons également le flag `--mode production`.

Nous utiliserons également le package `rimraf` d'abord pour supprimer les constructions précédentes que nous pourrions avoir. Nous faisons cela simplement par `rimraf dist`.

`_dist_` *est le dossier que Webpack créera automatiquement lorsqu'il construira notre projet. "Dist" est l'abréviation de distribution – c'est-à-dire que nous "distribuons" le code de nos applications.*

La commande `rimraf dist` indique au package `rimraf` de supprimer le répertoire `dist`. **Assurez-vous de ne pas** `rimraf src` **par accident !**

*Webpack offre également un plugin qui accomplira ce processus de nettoyage appelé* `clean-webpack-plugin`. J'ai choisi `dist` pour montrer une alternative.

Notre fichier package.json devrait ressembler à ceci :

```json
{
  "name": "hello-world",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "scripts": {
    "clean": "rimraf dist",
    "build": "npm run clean && webpack --mode production",
    "serve": "webpack-dev-server --mode development"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@babel/core": "^7.1.6",
    "@babel/preset-env": "^7.1.6",
    "babel-loader": "^8.0.4",
    "css-loader": "^1.0.1",
    "html-webpack-plugin": "^3.2.0",
    "rimraf": "^2.6.2",
    "vue": "^2.5.17",
    "vue-loader": "^15.4.2",
    "vue-style-loader": "^4.1.2",
    "vue-template-compiler": "^2.5.17",
    "webpack": "^4.26.0",
    "webpack-cli": "^3.1.2",
    "webpack-dev-server": "^3.1.10"
  },
  "dependencies": {}
}
```

Il y a trois choses à remarquer :

1. J'ai créé un script `clean` séparé afin que nous puissions l'exécuter indépendamment de notre script de construction.

2. `npm run build` appellera le script `clean` indépendant que nous avons créé.

3. J'ai `&&` entre `npm run clean` et `webpack`. Cette instruction dit : "exécutez `npm run clean` d'abord, *puis* exécutez `webpack`".

Construisons le projet.

`npm run build`

Webpack crée un répertoire `dist`, et notre code est à l'intérieur. Puisque notre code ne fait aucune requête HTTP, nous pouvons simplement ouvrir notre fichier `index.html` dans notre navigateur et il fonctionnera comme prévu.

*Si nous avions du code qui faisait des requêtes HTTP, nous rencontrerions des erreurs de cross-origin lorsque nous ferions ces requêtes. Nous devrions exécuter ce projet à partir d'un serveur pour qu'il fonctionne.*

Examinons le `index.html` que Webpack a créé dans le navigateur et l'éditeur de code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y0hwAs2CRmCuBrn7h1pFUw.png align="left")

*R*

Si nous l'ouvrons dans notre éditeur ou jetons un coup d'œil au code source dans nos outils de développement, vous verrez que Webpack a injecté la balise de script. Dans notre éditeur, cependant, vous ne verrez pas les styles car la balise de style est injectée dynamiquement au moment de l'exécution avec JavaScript !

De plus, remarquez que nos informations de console de développement ne sont plus présentes. Cela est dû au fait que nous avons passé le flag `--production` à Webpack.

### Conclusion

Comprendre le processus de construction derrière les frameworks que vous utilisez vous aidera à mieux comprendre le framework lui-même. Prenez le temps d'essayer de construire un projet Angular, React ou un autre projet Vue sans utiliser les CLIs respectifs. Ou, construisez simplement un site basique à trois fichiers (index.html, styles.css et app.js), mais utilisez Webpack pour servir et construire une version de production.

Merci d'avoir lu !

woz
---
title: Comment utiliser ReactJS avec Webpack 4, Babel 7 et Material Design
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-10T16:06:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-reactjs-with-webpack-4-babel-7-and-material-design-ff754586f618
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3XcVWZvLKvLukdJ2zbDDpQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: webpack
  slug: webpack
seo_title: Comment utiliser ReactJS avec Webpack 4, Babel 7 et Material Design
seo_desc: 'By Nazare Emanuel Ioan

  For the past year and some, I have been working with React at Creative Tim. I have
  been using create-react-app for developing some nice products. There have been a
  lot of clients asking how can someone migrate our product templ...'
---

Par Nazare Emanuel Ioan

Depuis un peu plus d'un an, je travaille avec React chez [Creative Tim](https://www.creative-tim.com/). J'ai utilisé [create-react-app](https://github.com/facebook/create-react-app) pour développer quelques beaux produits. De nombreux clients ont demandé comment migrer nos modèles de produits sur Webpack.

Après plusieurs demandes, nous avons créé ce petit tutoriel sur la façon de commencer à utiliser [React](https://reactjs.org/tutorial/tutorial.html) avec [Webpack 4](https://webpack.js.org/concepts/) et [Babel 7](https://babeljs.io/docs/en). À la fin du tutoriel, je vais vous montrer comment ajouter [Material Dashboard React](https://www.creative-tim.com/product/material-dashboard-react) sur le dessus de la nouvelle application créée.

Avant de commencer, assurez-vous d'avoir les dernières versions de [npm](https://www.npmjs.com/get-npm) et [Nodejs](https://nodejs.org/en/) installées globalement sur votre machine. Au moment de la rédaction de cet article, les dernières versions étaient 6.4.1 pour npm et 8.12.0 (lts) pour Nodejs sur ma machine.

### Création d'un nouveau dossier de projet avec package.json

Tout d'abord, créons un **nouveau dossier** pour notre nouvelle **application** et entrons dedans :

```
mkdir react-webpack-babel-tutorial
cd react-webpack-babel-tutorial
```

Maintenant que nous avons créé **le dossier** dans lequel nous allons développer **l'application**, nous devons y ajouter un fichier **package.json**. Nous pouvons le faire de deux manières et vous devriez en choisir une :

1. créez simplement le fichier **package.json** sans aucune autre configuration :

```
npm init -y
```

Comme vous pouvez le voir, le fichier **package.json** a été créé avec quelques informations très basiques.

![Image](https://cdn-media-1.freecodecamp.org/images/C6yK7U8NQyAzlbp8UVom5nih2sDoa4uWSgGd)

![Image](https://cdn-media-1.freecodecamp.org/images/SxwoqQVgiOTRJMKEsCLYLaHZxOqX2ze-r1L6)
_**npm init -y** output_

2. créez le fichier **package.json** avec quelques paramètres de configuration supplémentaires

```
npm init
```

J'ai ajouté quelques éléments à notre nouveau fichier **package.json**, comme quelques mots-clés sympas, **un dépôt** et ainsi de suite...

![Image](https://cdn-media-1.freecodecamp.org/images/EwG79ZpRTwXbKsLwLRTQ0oG6IaJ2r7TYFUux)

![Image](https://cdn-media-1.freecodecamp.org/images/kQl4c2u06gAReYzAZHUFJHQ0q7nKtyb13A4p)
_**npm init** output_

Après cela, ajoutons des fichiers **index.html** et **index.js** à notre nouveau dossier de projet, à l'intérieur d'un dossier **src**.

1. Commandes Linux/MacOS

```
mkdir src
touch src/index.html
touch src/index.js
```

2. Commandes Windows

```
mkdir src
echo "" > src\index.html
echo "" > src\index.js
```

Après cela, ajoutons le modèle suivant à l'intérieur de **index.html**.

```
<!DOCTYPE html><html lang="en">  <head>    <meta charset="utf-8">    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">    <meta name="theme-color" content="#000000">    <title>React Tutorial</title>  </head>  <body>    <noscript>      You need to enable JavaScript to run this app.    </noscript>    <div id="root"></div>    <!--      This HTML file is a template.      If you open it directly in the browser, you will see an empty page.      You can add webfonts, meta tags, or analytics to this file.      The build step will place the bundled scripts into the <body> tag.    -->  </body></html>
```

Ajoutons quelque chose à l'intérieur de **index.js** juste pour le plaisir de voir une démonstration un peu plus loin.

```
(function () {  console.log("hey mister");}());
```

Et voici ce que nous avons jusqu'à présent :

![Image](https://cdn-media-1.freecodecamp.org/images/S7g7x-2CQxrd7FMWFHhCeHBbhZnh0YCOsdNb)
_folder project structure_

### Ajout de Webpack au projet

Commençons à ajouter tous les **paquets Webpack** dont nous allons avoir besoin. Nous allons les installer en tant que **devDependencies** car ils ne seront utilisés qu'en mode développement.

```
npm install --save-dev webpack webpack-cli webpack-dev-server
```

* [**webpack**](https://www.npmjs.com/package/webpack)  
- utilisé pour configurer notre nouvelle application  
- au moment de la rédaction de cet article, la version était **_4.19.0_**
* [**webpack-cli**](https://www.npmjs.com/package/webpack-cli)  
- utilisé pour que nous puissions utiliser Webpack dans la ligne de commande  
- au moment de la rédaction de cet article, la version était **_3.1.0_**
* [**webpack-dev-server**](https://www.npmjs.com/package/webpack-dev-server)  
- utilisé pour que lorsque nous apportons une modification à un fichier dans notre nouvelle application, nous n'ayons pas besoin de rafraîchir la page. Il rafraîchit automatiquement la page du navigateur chaque fois que nous modifions un fichier dans notre application  
- comme son nom l'indique, c'est un serveur qui fonctionne en continu  
- au moment de la rédaction de cet article, la version était **_3.1.8_**

![Image](https://cdn-media-1.freecodecamp.org/images/3glsVLrGXniNvJktKumKkM5BSjuYUIyJyS92)
_**npm install --save-dev webpack webpack-cli webpack-dev-server** output_

Si nous regardons à l'intérieur du fichier **package.json**, nous allons voir que ces trois paquets ont été ajoutés à ce fichier comme suit :

```
"devDependencies": {  "webpack": "^4.19.0",  "webpack-cli": "^3.1.0",  "webpack-dev-server": "^3.1.8"}
```

Je vais supprimer le **_^_** (caret) de chaque version. C'est parce que je ne peux pas dire si la prochaine version de ces plugins fonctionnera toujours avec ce que je construis. Je pense que c'est quelque chose qui devrait être du bon sens. Lorsque vous créez une nouvelle application, utilisez les versions disponibles et faites ensuite, peut-être, quelques mises à jour vers des versions plus récentes. Vous ne savez peut-être pas ce qu'une nouvelle version cassera dans votre application.

Comme vous le verrez, l'installation de ces plugins a apporté quelques modifications à notre dossier de projet. Il a ajouté le dossier **node_modules** et **package-lock.json** à celui-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/qiz12CYpaSzAXjliX2tvca9fNMTUvD7bDDjj)
_project folder after installing **webpack**_

Maintenant, nous devons ajouter un nouveau fichier à notre projet, le fichier de configuration pour **Webpack** appelé **webpack.config.js** :

1. Commande Linux/MacOS

```
touch webpack.config.js
```

2. Commande Windows

```
echo "" > webpack.config.js
```

Ou vous pouvez simplement créer manuellement le nouveau fichier si vous ne souhaitez pas utiliser la ligne de commande.

Avant de commencer à modifier le fichier de configuration **Webpack**, installons d'abord quelques éléments dont nous allons avoir besoin dans notre application.

Tout d'abord, nous allons travailler avec certains chemins à l'intérieur du fichier de configuration Webpack. Installons **path** dans notre projet en tant que **devDependency.**

```
npm install --save-dev path
```

De plus, puisque nous ne voulons pas injecter manuellement le fichier **index.js** à l'intérieur du fichier HTML, nous allons avoir besoin d'un plugin appelé **html-webpack-plugin. Ce plugin** injectera le **index.js** à l'intérieur du fichier HTML sans aucune opération manuelle.

```
npm install --save-dev html-webpack-plugin
```

Une fois de plus, je vais modifier mon fichier **package.json** et supprimer toutes les occurrences de **^** (caret) de celui-ci.

Une autre modification que nous allons apporter à notre **package.json** est d'ajouter quelques nouveaux scripts à l'intérieur de l'objet **scripts**, après le script **test** (voir le deuxième exemple ci-dessous).

```
"webpack": "webpack",
"start": "webpack-dev-server --open"
```

Voici à quoi devrait ressembler votre **package.json** à ce stade :

```
{  "name": "react-webpack-babel-tutorial",  "version": "1.0.0",  "description": "This is a Tutorial to showcase the usage of React with Webpack and Babel",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1",    "webpack": "webpack",    "start": "webpack-dev-server --open"  },  "repository": {    "type": "git",    "url": "git+https://github.com/creativetimofficial/react-webpack-babel-tutorial.git"  },  "keywords": [    "react",    "webpack",    "babel",    "creative-tim",    "material-design"  ],  "author": "Creative Tim <hello@creative-tim.com> (https://www.creative-tim.com/)",  "license": "MIT",  "bugs": {    "url": "https://github.com/creativetimofficial/react-webpack-babel-tutorial/issues"  },  "homepage": "https://github.com/creativetimofficial/react-webpack-babel-tutorial#readme",  "devDependencies": {    "html-webpack-plugin": "3.2.0",    "path": "0.12.7",    "webpack": "4.19.0",    "webpack-cli": "3.1.0",    "webpack-dev-server": "3.1.8"  }}
```

Exécutons ces commandes une par une et voyons ce qui se passe.

```
npm run webpack
```

**Webpack** prendra automatiquement le fichier **src/index.js**, le compilera et le sortira dans **dist/main.js** et minimisera ce code. C'est parce que nous n'avons pas encore configuré le fichier de configuration **Webpack**. De plus, puisque nous n'avons pas configuré le fichier, nous allons avoir quelques avertissements dans notre console.

![Image](https://cdn-media-1.freecodecamp.org/images/v15-OCKAfjb8luDhCWn5AwUSUw5ycEhKGhG1)

![Image](https://cdn-media-1.freecodecamp.org/images/bNMwYyHV30uBZh72CRyEwmK5OwxaQZ32u7Pu)

![Image](https://cdn-media-1.freecodecamp.org/images/GXJDfTYb1lD7ShgiDXWUmG1k2zS7CrefyiaX)
_**npm run webpack** output_

Si nous exécutons l'autre commande

```
npm start
```

**webpack-dev-server** démarrera automatiquement un serveur et ouvrira le navigateur par défaut avec ce serveur. Mais une fois de plus, puisque nous n'avons pas notre fichier **webpack.config.js** configuré, la sortie ne sera pas celle attendue.

![Image](https://cdn-media-1.freecodecamp.org/images/i3-94F8yjyeIuQK7BYDwf8cznxfp-30I4v7i)

![Image](https://cdn-media-1.freecodecamp.org/images/ekoyHmE44SRFZNtwnELPLhyHHlLgPKQMFH2I)
_npm start output_

Si vous souhaitez arrêter le serveur, appuyez simplement en même temps sur les touches **CTRL** + **C** dans la ligne de commande.

Ajoutons le modèle suivant à l'intérieur de notre fichier de configuration **Webpack** :

```
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {  entry: path.join(__dirname,'src','index.js'),  output: {    path: path.join(__dirname,'build'),    filename: 'index.bundle.js'  },  mode: process.env.NODE_ENV || 'development',  resolve: {    modules: [path.resolve(__dirname, 'src'), 'node_modules']  },  devServer: {    contentBase: path.join(__dirname,'src')  },  plugins: [    new HtmlWebpackPlugin({      template: path.join(__dirname,'src','index.html')    })  ]};
```

* **entry** et **output**  
  ceux-ci sont utilisés pour dire à notre serveur ce qui doit être compilé et d'où (_entry: path.join(__dirname,'src','index.js'),_). Il indique également où placer la version compilée sortie (_output_  le dossier et le nom de fichier)
* **mode**  
  il s'agit du mode de notre sortie. Nous le définissons sur 'development'. Si dans les scripts nous spécifions la variable **NODE_ENV**, elle prendra celle-ci à la place. Voir l'exemple ci-dessous sur la façon d'utiliser **NODE_ENV** _(notez que les modifications ci-dessous ne seront pas apportées dans le fichier **package.json** dans ce tutoriel, il s'agit simplement d'un exemple pour que vous puissiez voir comment cela fonctionne)_

```
"webpack": "NODE_ENV=production webpack",
```

* **resolve**  
  ceci est utilisé afin que nous puissions importer n'importe quoi depuis le dossier **src** en chemins relatifs au lieu de chemins absolus. Il en va de même pour les **node_modules.** Nous pouvons importer n'importe quoi depuis node_modules directement sans chemins absolus
* **devServer**  
  ceci indique au **webpack-dev-server** quels fichiers doivent être servis. Tout ce qui se trouve dans notre dossier **src** doit être servi (sorti) dans le navigateur
* **plugins**  
  ici nous définissons les plugins dont nous avons besoin dans notre application. Pour le moment, nous avons seulement besoin du **html-webpack-plugin** qui indique au serveur que le **index.bundle.js** doit être injecté (ou ajouté si vous voulez) à notre fichier **index.html**

Si nous exécutons maintenant les commandes précédentes, nous verrons quelques différences.

```
npm run webpack
```

![Image](https://cdn-media-1.freecodecamp.org/images/5yaSP7i-hw1ukwiuQqM5S1YqtG7dmaO3vSTq)

![Image](https://cdn-media-1.freecodecamp.org/images/MpUjyMVp0Ia9P8rUNboekHJXeWUzzHOMjqjH)

![Image](https://cdn-media-1.freecodecamp.org/images/v9rZ1x9m41pTHXDHunyTa-pEi92Z0UBNYPNO)
_**npm run webpack** output with **webpack.config.js**_

Nous avons changé où la sortie devrait être (du dossier **dist** au dossier **build**). En changeant le **mode** de **Webpack**, maintenant le code a un aspect différent. Il n'est pas **minifié** comme la dernière fois sans **config**.

```
npm start
```

![Image](https://cdn-media-1.freecodecamp.org/images/L43AkjlELlcrnI-pfDrNXo-XEvjTlvyY3GfP)

![Image](https://cdn-media-1.freecodecamp.org/images/vGrdllxByyx9DfMu2fvTlwwQYpoUOAV4kNTd)

![Image](https://cdn-media-1.freecodecamp.org/images/lZkAY5xg3uGXH7JLUf9wN3-mZKLm2X5183jx)
_**npm start** output with **webpack.config.js**_

Le **webpack-dev-server** a pris tout ce qui se trouvait dans le dossier **src** et l'a sorti dans notre navigateur.

Nous sommes sur la bonne voie, mais nous n'avons ajouté que Webpack à notre projet. Où sont React et Babel ? Eh bien, c'est ce que nous allons faire ensuite.

### React, Babel et quelques chargeurs sympas pour les styles

Ajoutez **React** et **ReactDOM** à notre projet en tant que **dépendances normales**.

```
npm install --save react react-dom
```

À ce stade de notre développement, si nous devions ajouter du code **React** à l'intérieur de notre fichier JS, **Webpack** nous donnerait une erreur. Il ne sait pas comment compiler **React** à l'intérieur du fichier **bundle.js**.

Modifions le fichier **index.js** comme suit :

```
import React from "react";
import ReactDOM from "react-dom";
let HelloWorld = () => {  return <h1>Hello there World!</h1>}
ReactDOM.render(  <HelloWorld/>,  document.getElementById("root"));
```

Et après cela, redémarrons le serveur.

```
npm start
```

Et voici l'erreur :

![Image](https://cdn-media-1.freecodecamp.org/images/WnrYazPSPDnZvmlOOvAIdz9GCagpszoEycZO)

![Image](https://cdn-media-1.freecodecamp.org/images/i4DEG4wPgI2a176rOq5CjXTydAUfJkMBWK0p)
_**webpack** error for not having appropriate **loaders** for **react**_

C'est là que **Babel** vient à notre aide. **Babel** dira à **Webpack** comment compiler notre code **React**.

Ajoutons un ensemble de paquets Babel à notre application en tant que **devDependencies**.

```
npm install --save-dev @babel/core @babel/node @babel/preset-env @babel/preset-react babel-loader
```

* **@babel/core**  
  ceci est utilisé pour compiler **ES6** et au-dessus en **ES5**
* **@babel/node**  
  ceci est utilisé afin que nous puissions **importer** nos plugins et paquets à l'intérieur de **webpack.config.js** plutôt que de les **requérir** (c'est juste quelque chose que j'aime, et peut-être que vous l'aimerez aussi)
* **@babel/preset-env**  
  ceci déterminera quelles transformations ou plugins utiliser et polyfills (c'est-à-dire qu'il fournit une fonctionnalité moderne sur les anciens navigateurs qui ne la supportent pas nativement) en fonction de la matrice de navigateurs que vous souhaitez supporter
* **@babel/preset-react**  
  ceci va compiler le code **React** en code **ES5**
* **babel-loader**  
  ceci est un assistant **Webpack** qui transforme vos dépendances **JavaScript** avec **Babel** (c'est-à-dire qu'il transformera les instructions **import** en instructions **require**)

Puisque vous allez probablement avoir besoin d'ajouter quelques styles à votre projet (je sais que j'en ai besoin), nous allons ajouter un chargeur qui nous permettra d'**importer** et d'utiliser des fichiers **CSS** et **SCSS**.

```
npm install --save-dev style-loader css-loader sass-loader node-sass
```

* **style-loader**  
  ceci ajoutera au **DOM** les styles (injectera une balise **<style>** à l'intérieur du fichier HTML)
* **css-loader**  
  permettra d'importer des fichiers **CSS** dans notre projet
* **sass-loader**  
  permettra d'importer des fichiers **SCSS** dans notre projet
* **node-sass**  
  compilera les fichiers **SCSS** en fichiers **CSS** normaux

Nous allons créer un nouveau fichier **SCSS** et l'ajouter à nos dossiers.

1. Commande Linux/MacOS

```
touch src/index.scss
```

2. Commande Windows

```
echo "" > src/index.scss
```

Et ajoutons également quelques styles sympas.

```
body {  div#root{    background-color: #222;    color: #8EE4AF;  }}
```

Et changeons notre **index.js** en ajoutant un import pour le fichier **SCSS**.

```
import React from "react";
import ReactDOM from "react-dom";
```

```
// this line is new
// we now have some nice styles on our react app
import "index.scss";
```

```
let HelloWorld = () => {  return <h1>Hello there World!</h1>}
```

```
ReactDOM.render(  <HelloWorld/>,  document.getElementById("root"));
```

N'oubliez pas de supprimer les carets (^) de **package.json**.

Voici à quoi devrait ressembler votre **package.json** :

```
{  "name": "react-webpack-babel-tutorial",  "version": "1.0.0",  "description": "This is a Tutorial to showcase the usage of React with Webpack and Babel",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1",    "webpack": "webpack",    "start": "webpack-dev-server --open"  },  "repository": {    "type": "git",    "url": "git+https://github.com/creativetimofficial/react-webpack-babel-tutorial.git"  },  "keywords": [    "react",    "webpack",    "babel",    "creative-tim",    "material-design"  ],  "author": "Creative Tim <hello@creative-tim.com> (https://www.creative-tim.com/)",  "license": "MIT",  "bugs": {    "url": "https://github.com/creativetimofficial/react-webpack-babel-tutorial/issues"  },  "homepage": "https://github.com/creativetimofficial/react-webpack-babel-tutorial#readme",  "devDependencies": {    "@babel/core": "7.0.1",    "@babel/node": "7.0.0",    "@babel/preset-env": "7.0.0",    "@babel/preset-react": "7.0.0",    "babel-loader": "8.0.2",    "css-loader": "1.0.0",    "html-webpack-plugin": "3.2.0",    "node-sass": "4.9.3",    "path": "0.12.7",    "sass-loader": "7.1.0",    "style-loader": "0.23.0",    "webpack": "4.19.0",    "webpack-cli": "3.1.0",    "webpack-dev-server": "3.1.8"  },  "dependencies": {    "react": "16.5.1",    "react-dom": "16.5.1"  }}
```

Si nous exécutons l'une des commandes ci-dessus, l'erreur persistera. Nous n'avons pas encore dit à **Webpack** qu'il devait utiliser **Babel** et les chargeurs de style pour compiler notre code **React** et **SCSS**.

La prochaine chose à faire est d'ajouter un fichier de configuration pour **Babel**. Pour cela, nous devons créer un fichier nommé **.babelrc** dans lequel nous allons configurer **Babel**.

J'ai entendu dire que vous pouvez ajouter la configuration pour **Babel** directement dans le fichier **webpack.config.js**. Pour cela, vous pouvez consulter la [documentation officielle de babel-loader](https://github.com/babel/babel-loader). En ce qui me concerne, je pense qu'il est préférable d'avoir la configuration **Babel** dans son propre fichier. Ainsi, vous ne surchargez pas votre configuration **Webpack**.

Donc, exécutons dans la ligne de commande ce qui suit :

1. Commande Linux/MacOS

```
touch .babelrc
```

2. Commande Windows

```
echo "" > .babelrc
```

Et ajoutons le code suivant à l'intérieur de **.babelrc** afin que **babel-loader** sache quoi utiliser pour compiler le code :

```
{  "presets": [    "@babel/env",    "@babel/react"  ]}
```

Après ces étapes, nous devrons ajouter quelque chose à notre projet afin de pouvoir importer toutes sortes de fichiers tels que des images. Nous devrons également ajouter un plugin qui nous permettra de travailler avec des classes et bien plus encore. Ajoutons des propriétés de classe dans nos classes. Basiquement, cela nous permettra de travailler avec la [Programmation Orientée Objet](https://en.wikipedia.org/wiki/Object-oriented_programming)  sympa.

```
npm install --save-dev file-loader @babel/plugin-proposal-class-properties
```

Maintenant que nous avons fait cela, nous devons apporter quelques modifications à l'intérieur de **webpack.config.js** afin que **Webpack** utilise maintenant **Babel**. Nous allons également configurer **Webpack** pour écouter les fichiers **style** et nous allons changer les instructions **require** en instructions **import**.

Cela étant dit, modifions notre **webpack.config.js** comme suit (j'ai également ajouté quelques commentaires, peut-être qu'ils vous aideront) :

```
// old
// const path = require('path');
// const HtmlWebpackPlugin = require('html-webpack-plugin');
// new
import path from 'path';
import HtmlWebpackPlugin from 'html-webpack-plugin';
module.exports = {  entry: path.join(__dirname,'src','index.js'),  output: {    path: path.join(__dirname,'build'),    filename: 'index.bundle.js'  },  mode: process.env.NODE_ENV || 'development',  resolve: {    modules: [path.resolve(__dirname, 'src'), 'node_modules']  },  devServer: {    contentBase: path.join(__dirname,'src')  },  module: {    rules: [      {        // this is so that we can compile any React,        // ES6 and above into normal ES5 syntax        test: /\.(js|jsx)$/,        // we do not want anything from node_modules to be compiled        exclude: /node_modules/,        use: ['babel-loader']      },      {        test: /\.(css|scss)$/,        use: [          "style-loader", // creates style nodes from JS strings          "css-loader", // translates CSS into CommonJS          "sass-loader" // compiles Sass to CSS, using Node Sass by default        ]      },      {        test: /\.(jpg|jpeg|png|gif|mp3|svg)$/,        loaders: ['file-loader']      }    ]  },  plugins: [    new HtmlWebpackPlugin({      template: path.join(__dirname,'src','index.html')    })  ]};
```

Il y a encore une modification que nous devons apporter au fichier **package.json**. Nous devons dire à nos scripts que dans les fichiers de configuration de **Webpack**, nous utilisons **import** au lieu des instructions **require**. Sinon, il nous donnera une erreur indiquant qu'il ne sait pas ce que **import** signifie.

```
{  "name": "react-webpack-babel-tutorial",  "version": "1.0.0",  "description": "This is a Tutorial to showcase the usage of React with Webpack and Babel",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1",    "webpack": "babel-node ./node_modules/webpack/bin/webpack",    "start": "babel-node ./node_modules/webpack-dev-server/bin/webpack-dev-server --open"  },  "repository": {    "type": "git",    "url": "git+https://github.com/creativetimofficial/react-webpack-babel-tutorial.git"  },  "keywords": [    "react",    "webpack",    "babel",    "creative-tim",    "material-design"  ],  "author": "Creative Tim <hello@creative-tim.com> (https://www.creative-tim.com/)",  "license": "MIT",  "bugs": {    "url": "https://github.com/creativetimofficial/react-webpack-babel-tutorial/issues"  },  "homepage": "https://github.com/creativetimofficial/react-webpack-babel-tutorial#readme",  "devDependencies": {    "@babel/core": "7.0.1",    "@babel/node": "7.0.0",    "@babel/plugin-proposal-class-properties": "7.0.0",    "@babel/preset-env": "7.0.0",    "@babel/preset-react": "7.0.0",    "babel-loader": "8.0.2",    "css-loader": "1.0.0",    "file-loader": "2.0.0",    "html-webpack-plugin": "3.2.0",    "node-sass": "4.9.3",    "path": "0.12.7",    "sass-loader": "7.1.0",    "style-loader": "0.23.0",    "webpack": "4.19.0",    "webpack-cli": "3.1.0",    "webpack-dev-server": "3.1.8"  },  "dependencies": {    "react": "16.5.1",    "react-dom": "16.5.1"  }}
```

Une autre chose que nous devons encore ajouter est le **@babel/plugin-proposal-class-properties** au fichier **.babelrc**. Babel saura comment gérer les propriétés de classe.

```
{  "presets": [    "@babel/env",    "@babel/react"  ],  "plugins": [    "@babel/plugin-proposal-class-properties"  ]}
```

Maintenant, nous avons terminé. Nous pouvons exécuter l'une des commandes ci-dessus et cela ne devrait pas nous donner d'erreurs. Voyons-les en action.

```
npm run webpack
```

![Image](https://cdn-media-1.freecodecamp.org/images/2e1EkHvGTSgkr6K8q0owtTeKfJgy9zaWv3qL)
_**npm run webpack** with no errors_

Et maintenant, voyons le script principal de notre application.

```
npm start
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZxgR7MwCMF07iPeCjljtUhjPho2POqJHttYP)

![Image](https://cdn-media-1.freecodecamp.org/images/wr9GAci8MufySHuCI9wf7IgfcBctM1Nc5TKo)
_**npm start** output_

### Ajouter Material Design à notre nouveau projet React avec Webpack et Babel

Comme je vous l'ai dit au début de cet article, nous n'allons pas créer des styles pour Material Design à partir de zéro. Cela nécessiterait beaucoup de travail. Nous n'avons pas le temps pour cela.

Au lieu de cela, nous allons ajouter un beau produit qui implémente le [Material Design de Google](https://material.io/design/) avec quelques touches mineures de l'équipe [Creative Tim](https://www.creative-tim.com/presentation). Nous allons ajouter [Material Dashboard React](https://www.creative-tim.com/product/material-dashboard-react) à celui-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/j0jyL4PSfmiVRF6ja4nue98YAAazqxWVM5P7)

Tout d'abord, vous devez obtenir le produit. Voici quelques moyens d'obtenir le produit :

* Clonez le dépôt dans un autre dossier :

```
git clone https://github.com/creativetimofficial/material-dashboard-react.git
```

* [Télécharger depuis Github](https://github.com/creativetimofficial/material-dashboard-react/archive/master.zip)
* [Télécharger depuis Creative Tim](https://www.creative-tim.com/product/material-dashboard-react)

D'accord, maintenant nous avons les deux projets  Material Dashboard React et notre nouveau projet avec **Webpack** et **Babel ** avec **React**.

![Image](https://cdn-media-1.freecodecamp.org/images/2vNjpDKZYsJcMG2FkMpEh3D1NMcE-l7zW9iM)
_**material-dashboard-react** et **react-webpack-babel-tutorial**_

Maintenant, nous ne pouvons pas simplement copier le dossier src de **Material Dashboard React** dans notre nouveau projet. Cela nous donnera beaucoup d'erreurs. Comme des erreurs de dépendances manquantes, de module introuvable, vous voyez le tableau, beaucoup d'erreurs.

Donc, je suggère que nous commençons par ajouter les dépendances de **Material Dashboard React** à notre **package.json**. Nous n'avons pas besoin de toutes les dépendances des paquets de **Material Dashboard React**, puisque nous avons construit notre propre serveur en utilisant **Webpack.** Nous avons ajouté d'autres chargeurs de style au-delà de ce que le produit a.

Cela étant dit, nous avons besoin de ce qui suit :

```
npm install --save @material-ui/core@3.1.0 @material-ui/icons@3.0.1 @types/googlemaps@3.30.11 @types/markerclustererplus@2.1.33 chartist@0.10.1 classnames@2.2.6 perfect-scrollbar@1.4.0 react-chartist@0.13.1 react-google-maps@9.4.5 react-router-dom@4.3.1 react-swipeable-views@0.12.15
```

Nous ne passons pas en revue tous ces éléments. Ils peuvent être trouvés sur [npmjs.com](https://www.npmjs.com/) avec tous les détails et leur propre documentation.

Une fois de plus, nous allons dans le fichier **package.json** et supprimons les carets (^) des paquets que nous venons d'installer.

D'accord, nous avons presque terminé. Nous allons copier tout le contenu du dossier **src** de **Material Dashboard React** dans le dossier **src** de notre projet et remplacer le fichier **index.js**. Mais gardez-le dans le fichier **index.html**.

![Image](https://cdn-media-1.freecodecamp.org/images/lu9OnRtupBWtPeeIjyHgyfYaxXTosauatNAR)

![Image](https://cdn-media-1.freecodecamp.org/images/23WMOaVa6tr6cHawZi1FIbUX8leJuTAc1kJL)
_Folder structure before and after adding the Material Dashboard React **src** folder_

Maintenant, nous devons ajouter quelques styles et polices cdns à l'intérieur de notre **index.html**.

```
<!DOCTYPE html><html lang="en">  <head>    <meta charset="utf-8">    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">    <meta name="theme-color" content="#000000">    <link rel="stylesheet" href="//cdn.jsdelivr.net/chartist.js/latest/chartist.min.css">    <script src="//cdn.jsdelivr.net/chartist.js/latest/chartist.min.js"></script>    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons">    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">    <title>React Tutorial</title>  </head>  <body>    <noscript>      You need to enable JavaScript to run this app.    </noscript>    <div id="root"></div>    <!--      This HTML file is a template.      If you open it directly in the browser, you will see an empty page.      You can add webfonts, meta tags, or analytics to this file.      The build step will place the bundled scripts into the <body> tag.    -->  </body></html>
```

Et nous y sommes presque. Nous avons encore un petit problème. Lorsque nous actualisons la page, nous avons une erreur **Cannot GET /dashboard_.** Si nous naviguons vers une autre page, nous obtiendrons, par exemple, **Cannot GET /user** et ainsi de suite. Donc, en gros, nos routes ne fonctionnent pas. Nous devons apporter quelques modifications à l'intérieur de **src/index.js** ou à l'intérieur de notre **webpack.config.js**.

Je vais choisir la première option car elle est assez simple et facile à comprendre.

Nous naviguons à l'intérieur du nouveau index.js et nous changeons le type d'historique. Nous mettons **createHashHistory()** au lieu de **createBrowserHistory()**.

Cela nous permettra d'actualiser la page sans aucune autre erreur. Maintenant, nous avons terminé.

```
import React from "react";
import ReactDOM from "react-dom";
import { createHashHistory } from "history";
import { Router, Route, Switch } from "react-router-dom";
import "assets/css/material-dashboard-react.css?v=1.5.0";
import indexRoutes from "routes/index.jsx";
const hist = createHashHistory();
ReactDOM.render(  <Router history={hist}>    <Switch>      {indexRoutes.map((prop, key) => {        return <Route path={prop.path} component={prop.component} key={key} />;      })}    </Switch>  </Router>,  document.getElementById("root"));
```

J'espère vraiment que vous avez aimé ce tutoriel et je suis très impatient d'entendre vos réflexions à ce sujet. Laissez simplement un commentaire sur ce fil et je serai plus qu'heureux de répondre.

Des remerciements spéciaux doivent également aller à [Linh Nguyen My](https://pinglinh.com/) pour son [tutoriel](https://medium.freecodecamp.org/part-1-react-app-from-scratch-using-webpack-4-562b1d231e75) qui m'a donné une compréhension très nécessaire sur **Webpack**.

Liens utiles :

* Obtenez le code de ce tutoriel depuis [Github](https://github.com/creativetimofficial/react-webpack-babel-md-tutorial)
* Lisez plus sur ReactJS sur [leur site officiel](https://reactjs.org/)
* Lisez plus sur [Webpack ici](https://webpack.js.org/)
* Lisez plus sur Babel sur [ce lien ici](https://babeljs.io/)
* Lisez plus sur [Material Design](https://material.io/)
* Consultez notre plateforme pour voir [ce que nous faisons](https://www.creative-tim.com/) et [qui nous sommes](https://www.creative-tim.com/presentation)
* Obtenez Material Dashboard React depuis [www.creative-tim.com](https://www.creative-tim.com/product/material-dashboard-react) ou depuis [Github](https://github.com/creativetimofficial/material-dashboard-react)
* Lisez plus sur [Material-UI](https://material-ui.com/), le cœur de Material Dashboard React

Trouvez-moi sur :

* Email : [manu@creative-tim.com](mailto:manu@creative-tim.com)
* Facebook : [https://www.facebook.com/NazareEmanuel](https://www.facebook.com/NazareEmanuel)
* Instagram : [https://www.instagram.com/manu.nazare/](https://www.instagram.com/manu.nazare/)
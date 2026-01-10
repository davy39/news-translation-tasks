---
title: Comment partager des variables entre HTML, CSS et JavaScript en utilisant Webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-20T00:30:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-share-variables-across-html-css-and-javascript-using-webpack
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/4kzz7px14mtv34rcfp73.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Tutorial
  slug: tutorial
- name: webpack
  slug: webpack
seo_title: Comment partager des variables entre HTML, CSS et JavaScript en utilisant
  Webpack
seo_desc: 'By Adrien Zaganelli

  Earlier this week, I read an article explaining how CSS-in-JS slows down the rendering
  of some React apps and how static CSS is faster. But CSS-in-JS is very popular because,
  among other features, you can style dynamically using J...'
---

Par Adrien Zaganelli

Plus tôt cette semaine, j'ai lu [un article](https://calendar.perfplanet.com/2019/the-unseen-performance-costs-of-css-in-js-in-react-apps/) expliquant comment le CSS-in-JS ralentit le rendu de certaines applications React et comment le CSS statique est plus rapide. Mais le CSS-in-JS est très populaire car, entre autres fonctionnalités, vous pouvez styliser dynamiquement en utilisant des variables JavaScript.

Dans ce tutoriel, je vais vous montrer comment recréer cet avantage dans n'importe quel projet web grâce à Webpack (et je suppose que vous savez comment l'utiliser). Pour commencer, nous voulons que Webpack regroupe nos fichiers sources dans un dossier statique `dist/`.

Vous pouvez consulter [le code source ici](https://glitch.com/~shared-variables-webpack).

## 1. Installer notre application

### La partie ennuyeuse

Créez un dossier pour ce tutoriel, ouvrez votre terminal et initialisez un projet :

```
npm init -y

```

Tout d'abord, si ce n'est pas déjà fait, installez [node.js](https://nodejs.org/en/) et [Webpack](https://webpack.js.org/) :

```
npm install webpack webpack-cli --save-dev

```

Créons un script dans notre `package.json` qui indique à Webpack d'utiliser notre fichier de configuration :

```json
  "scripts": {
    "build": "webpack --config webpack.config.js"
  }

```

À la racine de votre dossier, créez un fichier `globals.js`, où nos variables partagées seront stockées :

```javascript
module.exports = {
  myTitle: 'Bonjour freeCodeCamp !',
  myColor: '#42ff87',
};

```

Le fichier de configuration Webpack ressemble à ceci (`webpack.config.js`). Créez-le à la racine de votre dossier :

```javascript
module.exports = {
  entry: __dirname + '/app/index.js',
  output: {
    path: __dirname + '/dist',
    filename: 'index_bundle.js'
  },
};

```

Notre code source sera situé dans un dossier `app`. Créez-le comme ceci :

```
mkdir app && cd app

```

Vous aurez besoin des fichiers `index.html` et `index.js` à ce stade. Créez ces fichiers dans le dossier `app` :

```
touch index.html index.js

```

Parfait ! Vous êtes prêt. ?

Votre dossier devrait ressembler à ceci :

```
|-- node_modules/
|-- package.json
|-- webpack.config.js
|-- globals.js
|-- app/
	|-- index.html
	|-- index.js

```

## 2. Rendre nos fichiers HTML avec le `html-webpack-plugin`

Ce `app/index.html` est vide. Ajoutons-y quelques balises et ajoutons ensuite une variable personnalisée :

```html
<html lang="en">
<head>
  <title>Variables partagées avec Webpack !</title>
</head>
<body>
  <h1><%= myTitle %></h1>
</body>
</html>

```

Comme vous pouvez le voir, nous essayons d'imprimer une variable dans notre HTML... ce qui est impossible ! Pour que cela fonctionne, nous utiliserons le [html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin) qui nous donne la possibilité d'utiliser la syntaxe [EJS](https://ejs.co/) et **d'injecter des données dedans**.

Le plugin générera un fichier HTML valide. En attendant, vous devriez renommer votre fichier `app/index.html` en `app/index.ejs`.

```
npm install --save-dev html-webpack-plugin

```

Retour à notre fichier de configuration. `html-webpack-plugin` a une option intéressante `templateParameters` qui nous permet de passer un objet en paramètre. Activez le plugin comme suit dans `webpack.config.js` :

```javascript
const HtmlWebpackPlugin = require('html-webpack-plugin');
const globals = require('./globals.js')

module.exports = {
	// ... configuration précédente, entry, output...
  plugins: [
    new HtmlWebpackPlugin({
      template: 'app/index.ejs',
      templateParameters: globals,
    })
  ]
};

```

Exécutez `npm run build` et _ta-daaaaa_ « <%= myTitle %> » est devenu « Bonjour freeCodeCamp » ! Le travail est fait par Webpack pendant la compilation lorsqu'il exécute le `html-webpack-plugin`.

Vous voyez ? C'était assez simple avec le bon outil : HTML ✅

## 3. Utiliser nos variables en JavaScript

Ouf, tant de lignes juste pour imprimer une variable ! ? Avec Webpack, les choses deviennent souvent compliquées. Eh bien, celle-ci est très simple : en JavaScript, il suffit d'importer votre fichier. Dans votre `app/index.js` :

```javascript
import globals from '../globals.js'

document.write(
'<pre>' +
  JSON.stringify(globals, null, 2) +
'</pre>'
);

```

Cela imprimera notre objet globals sur la page. Maintenant, passons au CSS.

## 4. Utiliser des variables partagées dans notre CSS

Voici notre dernier boss ?

D'accord les gars, vous m'avez eu... J'ai menti. Nous ne pouvons pas utiliser nos globals directement dans CSS – nous devons utiliser un pré-processeur. Dans cet exemple, nous utiliserons [SASS](https://sass-lang.com/).

Côté Webpack, un plugin ne suffira pas. Nous devons utiliser un [loader](https://webpack.js.org/loaders/) pour convertir SASS en CSS. Dans ce cas, nous avons besoin du package [sass-loader](https://github.com/webpack-contrib/sass-loader), alors installez-le selon la documentation :

```
npm install sass-loader node-sass css-loader style-loader --save-dev

```

Retour au codage. Maintenant que nous avons SASS, créez votre fichier de style, `app/style.scss` :

```scss
h1 {
  color: $myColor;
}

```

Notre SASS est configuré – maintenant, comment pouvons-nous injecter des données dedans ? Le package `sass-loader` a une option [prependData](https://github.com/webpack-contrib/sass-loader#prependdata) ! Mais il prend une chaîne de caractères comme paramètre, ce qui signifie que vos données doivent ressembler à ceci : `"$myColor: red; myTitle: '...'";`.

Nous devons automatiser cela et convertir un objet JavaScript en une chaîne de caractères. Je n'ai pas trouvé de package sur `npm` qui me satisfaisait, alors j'ai écrit [mon propre convertisseur](https://gist.github.com/adrienZ/0257e37bf4788b903ba76fa82dac1ed1). Téléchargez le fichier et ajoutez-le à votre projet (dans mon exemple, c'est `utils/jsToScss.js`).

Votre fichier final `webpack.config.js` devrait ressembler à ceci :

```javascript
const globals = require("./globals.js");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const jsToScss = require("./utils/jsToScss.js");

module.exports = {
  entry: __dirname + "/app/index.js",
  output: {
    path: __dirname + "/dist",
    filename: "index_bundle.js"
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "app/index.ejs",
      templateParameters: globals
    })
  ],
  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          // Crée des nœuds `style` à partir de chaînes JS
          "style-loader",
          // Traduit le CSS en CommonJS
          "css-loader",
          // Compile Sass en CSS
          {
            loader: "sass-loader",
            options: {
              prependData: jsToScss(globals)
            }
          }
        ]
      }
    ]
  }
};

```

Voici ce que vous devriez voir :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/Capture-d-e-cran-2019-12-23-23.44.11.png)
_[https://glitch.com/edit/#!/shared-variables-webpack?path=webpack.config.js](https://glitch.com/edit/#!/shared-variables-webpack?path=webpack.config.js)_

Si vous lisez toujours ce tutoriel, merci pour votre attention. J'espère que cela vous aide ! Webpack est un outil très puissant que vous devriez explorer davantage ?

NB : Dans votre dossier `dist/`, vous pouvez voir qu'il n'y a aucun CSS généré. C'est parce que j'utilise le `style-loader` pour garder cette démonstration simple. Pour générer le fichier CSS, consultez le [mini-css-extract-plugin](https://webpack.js.org/plugins/mini-css-extract-plugin/).
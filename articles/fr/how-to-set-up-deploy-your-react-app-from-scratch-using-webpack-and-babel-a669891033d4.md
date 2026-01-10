---
title: Comment configurer et déployer votre application React à partir de zéro en
  utilisant Webpack et Babel
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2019-02-14T21:41:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-deploy-your-react-app-from-scratch-using-webpack-and-babel-a669891033d4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NluDivebM4nQi0OLMYuVHw.png
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment configurer et déployer votre application React à partir de zéro
  en utilisant Webpack et Babel
seo_desc: So you’ve been using create-react-app a.k.a CRA for a while now. It’s great
  and you can get straight to coding. But when do you need to eject from create-react-app
  and start configuring your own React application? There will be a time when we have
  to...
---

Vous avez donc utilisé create-react-app, alias CRA, depuis un certain temps. C'est génial et vous pouvez commencer à coder directement. Mais quand devez-vous quitter create-react-app et commencer à configurer votre propre application React ? Il viendra un moment où nous devrons laisser tomber la vérification de sécurité et commencer à nous aventurer par nous-mêmes.

Ce guide couvrira la configuration React la plus simple que j'ai personnellement utilisée pour presque tous mes projets React. À la fin de ce tutoriel, nous aurons notre propre modèle de base et apprendrons quelques configurations.

#### Table des matières

* Pourquoi créer votre propre configuration ?
* Configurer webpack 4
* Configurer Babel 7
* Ajouter Prettier
* Ajouter une source map pour de meilleurs journaux d'erreurs
* Configurer ESLint
* J'ai trouvé des erreurs ! Que faire ?
* Ajouter un processeur CSS LESS
* Déployer l'application React sur Netlify
* Conclusion

### Pourquoi créer votre propre configuration ?

Il existe certaines raisons qui rendent la création de votre propre configuration React pertinente. Vous êtes probablement à l'aise avec React et vous souhaitez apprendre à utiliser des outils comme webpack et Babel par vous-même. Ces outils de construction sont puissants, et si vous avez un peu de temps supplémentaire, il est toujours bon de les comprendre.

Les développeurs sont naturellement des personnes curieuses, donc si vous sentez que vous aimeriez savoir comment les choses fonctionnent et quelle partie fait quoi, alors laissez-moi vous aider.

De plus, la dissimulation de la configuration React par create-react-app est destinée aux développeurs commençant à apprendre React, car [la configuration ne devrait pas faire obstacle au démarrage](https://youtu.be/G39lKaONAlA?t=873). Mais lorsque les choses deviennent sérieuses, bien sûr, vous avez besoin de plus d'outils à intégrer dans votre projet. Pensez à :

* Ajouter des chargeurs webpack pour less, sass
* Faire du rendu côté serveur
* Utiliser de nouvelles versions ES
* Ajouter MobX et Redux
* Créer votre propre configuration juste pour l'apprentissage

Si vous regardez autour de vous sur Internet, il existe quelques astuces pour contourner les limitations de CRA comme [create-react-app rewired](https://github.com/timarney/react-app-rewired). Mais vraiment, pourquoi ne pas simplement apprendre la configuration React par vous-même ? Je vais vous aider à y parvenir. Étape par étape.

Maintenant que vous êtes convaincu d'apprendre quelques configurations, commençons par initialiser un projet React à partir de zéro.

Ouvrez la ligne de commande ou Git bash et créez un nouveau répertoire

```
mkdir react-config-tutorial && cd react-config-tutorial
```

Initialisez le projet NPM en exécutant :

```
npm init -y
```

Maintenant, installez React

```
npm install react react-dom
```

De plus, vous pouvez consulter le [code source](https://github.com/nsebhastian/my-react-boilerplate) sur GitHub tout en lisant ce tutoriel pour des explications sur les paramètres.

### Configurer webpack 4

Notre première étape sera webpack. C'est un outil très populaire et puissant pour configurer non seulement React, mais presque tous les projets front-end. La fonction principale de webpack est qu'il prend un ensemble de fichiers JavaScript que nous écrivons dans notre projet et les transforme en un seul fichier minifié, afin qu'il soit rapide à servir. À partir de webpack 4, nous ne sommes pas obligés d'écrire un fichier de configuration pour l'utiliser, mais dans ce tutoriel, nous allons en écrire un afin de mieux le comprendre.

Tout d'abord, faisons quelques installations

```
npm install --save-dev webpack webpack-dev-server webpack-cli
```

Cela installera :

* **module webpack** — qui inclut toutes les fonctionnalités principales de webpack
* **webpack-dev-server** — ce serveur de développement relance automatiquement webpack lorsque notre fichier est modifié
* **webpack-cli** — permet d'exécuter webpack à partir de la ligne de commande

Essayons d'exécuter webpack en ajoutant le script suivant à `package.json`

```js
"scripts": {
 "start": "webpack-dev-server --mode development",
},
```

Maintenant, créez un fichier `index.html` dans votre projet racine avec le contenu suivant :

```html
<!DOCTYPE html>
<html>
 <head>
 <title>Ma configuration React</title>
 </head>
 <body>
 <div id="root"></div>
 <script src="./dist/bundle.js"></script>
 </body>
</html>
```

Créez un nouveau répertoire nommé `src` et à l'intérieur, créez un nouveau fichier `index.js`

```
mkdir src && cd src && touch index.js
```

Ensuite, écrivez un composant React dans le fichier :

```js
import React from "react";
import ReactDOM from "react-dom";
class Welcome extends React.Component {
  render() {
    return <h1>Bonjour le monde depuis le modèle React</h1>;
  }
}
ReactDOM.render(<Welcome />, document.getElementById("root"));
```

Exécutez webpack en utilisant `npm run start` … Et une erreur sera déclenchée.

```
Vous avez peut-être besoin d'un chargeur approprié pour gérer ce type de fichier
```

### Configurer Babel 7

Le composant React que nous avons écrit ci-dessus a utilisé la syntaxe `class`, qui est une fonctionnalité de ES6. Webpack a besoin de Babel pour traiter ES6 en syntaxes ES5 afin que cette classe fonctionne.

Installons Babel dans notre projet

```
npm install --save-dev @babel/core @babel/preset-env \@babel/preset-react babel-loader
```

Pourquoi avons-nous besoin de ces packages ?

* **@babel/core** est la dépendance principale qui inclut le script de transformation babel.
* **@babel/preset-env** est le preset Babel par défaut utilisé pour transformer ES6+ en code ES5 valide. Configure optionnellement les polyfills du navigateur automatiquement.
* **@babel/preset-react** est utilisé pour transformer la syntaxe JSX et les classes React en code JavaScript valide.
* **babel-loader** est un chargeur webpack qui intègre Babel dans webpack. Nous exécuterons Babel à partir de webpack avec ce package.

Pour intégrer Babel dans notre webpack, nous devons créer un fichier de configuration webpack. Écrivons un fichier `webpack.config.js` :

```js
module.exports = {
  entry: './src/index.js',
  output: {
    path: __dirname + '/dist',
    publicPath: '/',
    filename: 'bundle.js'
  },
  devServer: {
    contentBase: './dist',
  },
  module: {
    rules: [
    {
      test: /\.(js|jsx)$/,
      exclude: /node_modules/,
      use: ['babel-loader']
    }
    ]
  },
};
```

Cette configuration webpack indique essentiellement que le point d'`entry` de notre application est index.js, donc récupérez tout ce dont ce fichier a besoin, puis placez la sortie du processus de bundling dans le répertoire _dist_, nommé _bundle.js_. Oh, si nous exécutons `webpack-dev-server`, alors dites au serveur de servir le contenu à partir de la configuration `contentBase`, qui est le même répertoire que cette configuration. Pour tous les fichiers .js ou .jsx, utilisez `babel-loader` pour transpiler le tout.

Pour utiliser les presets Babel, créez un nouveau fichier `.babelrc`

```
touch .babelrc
```

Écrivez le contenu suivant :

```js
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react"
  ]
}
```

Maintenant, exécutez `npm run start` à nouveau. Cette fois, cela fonctionnera.

### Ajouter Prettier

Pour accélérer davantage le développement, formatons notre code en utilisant Prettier. Installez la dépendance localement et utilisez l'argument --save-exact puisque Prettier introduit des changements stylistiques dans les versions de correctifs.

```
npm install --save-dev --save-exact prettier
```

Maintenant, nous devons écrire le fichier de configuration `.prettierrc` :

```js
{
 "semi": true,
 "singleQuote": true,
 "trailingComma": "es5"
}
```

Les règles signifient que nous voulons ajouter un point-virgule à la fin de chaque instruction, utiliser des guillemets simples chaque fois que c'est approprié et mettre des virgules finales pour le code ES5 multi-lignes comme les objets ou les tableaux.

Vous pouvez exécuter Prettier à partir de la ligne de commande avec :

```
npx prettier --write "src/**/*.js"
```

Ou ajouter un nouveau script à notre fichier `package.json` :

```js
"scripts": {
 "test": "echo \"Erreur : aucun test spécifié\" && exit 1",
 "start": "webpack-dev-server --mode development",
 "format": "prettier --write \"src/**/*.js\""
},
```

Maintenant, nous pouvons exécuter Prettier en utilisant `npm run format`.

De plus, si vous utilisez VSCode pour le développement, vous pouvez installer l'[extension Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) et l'exécuter à chaque fois que vous enregistrez vos modifications en ajoutant ce paramètre :

```
"editor.formatOnSave": true
```

### Ajouter une source map pour de meilleurs journaux d'erreurs

Puisque webpack regroupe le code, les source maps sont obligatoires pour obtenir une référence au fichier original qui a déclenché une erreur. Par exemple, si vous regroupez trois fichiers sources (`a.js`, `b.js`, et `c.js`) en un seul bundle (`bundler.js`) et que l'un des fichiers sources contient une erreur, la trace de la pile pointera simplement vers `bundle.js`. Cela pose problème car vous voulez probablement savoir exactement si c'est le fichier a, b ou c qui cause une erreur.

Vous pouvez dire à webpack de générer des source maps en utilisant la propriété devtool de la configuration :

```js
module.exports = {
  devtool: 'inline-source-map',
  // … le reste de la config
};
```

Bien que cela ralentira la construction, cela n'a aucun effet sur la production. Les source maps ne sont téléchargées que [si vous ouvrez les outils de développement du navigateur](https://stackoverflow.com/a/44316255).

### Configurer ESLint

Un linter est un programme qui vérifie notre code pour toute erreur ou avertissement pouvant causer des bugs. Le linter de JavaScript, ESLint, est un programme de linting très flexible qui peut être configuré de nombreuses manières.

Mais avant d'aller plus loin, installons ESLint dans notre projet :

```
npm --save-dev install eslint eslint-loader babel-eslint eslint-config-react eslint-plugin-react
```

* **eslint** est la dépendance principale pour toutes les fonctionnalités, tandis que eslint-loader nous permet d'intégrer eslint dans webpack. Maintenant, puisque React utilise la syntaxe ES6+, nous ajouterons **babel-eslint** — un parseur qui permet à eslint de vérifier tous les codes ES6+ valides.
* **eslint-config-react** et **eslint-plugin-react** sont tous deux utilisés pour permettre à ESLint d'utiliser des règles pré-établies.

Puisque nous avons déjà webpack, nous devons simplement modifier légèrement la configuration :

```js
module.exports = {
  // modifier le module
  module: {
    rules: [{
      test: /\.(js|jsx)$/,
      exclude: /node_modules/,
      use: ['babel-loader', 'eslint-loader'] // inclure eslint-loader
    }]
  },
};
```

Ensuite, créez un fichier de configuration eslint nommé `.eslintrc` avec ce contenu :

```
{
  "parser": "babel-eslint",
  "extends": "react",
  "env": {
    "browser": true,
    "node": true
  },
  "settings": {
    "react": {
      "version": "detect"
    }
  }
}
```

La configuration dit essentiellement : _"Hey ESLint, s'il te plaît, analyse le code en utilisant `babel-eslint` avant de le vérifier, et quand tu le vérifies, s'il te plaît, vérifie si toutes les règles de notre configuration de règles React sont respectées. Prends les variables globales de l'environnement du navigateur et de node. Oh, et si c'est du code React, prends la version du module lui-même. Ainsi, l'utilisateur n'aura pas à spécifier la version manuellement."_

Plutôt que de spécifier nos propres règles manuellement, nous étendons simplement les règles `react` qui ont été rendues disponibles par `eslint-config-react` et `eslint-plugin-react`.

### J'ai trouvé des erreurs ! Que faire ?

Malheureusement, la seule façon de vraiment comprendre comment corriger les erreurs ESLint est de consulter la documentation pour les [règles](https://eslint.org/docs/rules/). Il existe un moyen rapide de corriger les erreurs ESLint en utilisant `eslint--fix`, et c'est en fait bien pour une correction rapide. Ajoutons un script à notre fichier `package.json` :

```js
"scripts": {
  "test": "echo \"Erreur : aucun test spécifié\" && exit 1",
  "start": "webpack-dev-server --mode development",
  "format": "prettier --write \"src/**/*.js\"",
  "eslint-fix": "eslint --fix \"src/**/*.js\"", // le script eslint
  "build": "webpack --mode production"
},
```

Ensuite, exécutez-le avec `npm run eslint-fix`. Ne vous inquiétez pas si vous êtes encore un peu confus à propos d'ESLint pour l'instant. Vous en apprendrez plus sur ESLint en l'utilisant.

### Ajouter un processeur CSS LESS

Pour ajouter le processeur LESS à notre application React, nous aurons besoin des packages less et loader de webpack :

```
npm install --save-dev less less-loader css-loader style-loader
```

`less-loader` compilera notre fichier less en css, tandis que `css-loader` résoudra la syntaxe css comme `import` ou `url()`. Le `style-loader` prendra notre css compilé et le chargera dans la balise `<style>` dans notre bundle. C'est génial pour le développement car cela nous permet de mettre à jour notre style à la volée, sans avoir besoin de rafraîchir le navigateur.

Maintenant, ajoutons quelques fichiers css pour créer un nouveau répertoire de style dans `src/style`

```
cd src && mkdir style && touch header.less && touch main.less
```

Contenu de `header.less` :

```js
.header {
  background-color: #3d3d;
}
```

Contenu de `main.less` :

```css
@import "header.less";
@color: #f5adad;
body {
  background-color: @color;
}
```

Maintenant, importons notre fichier `main.less` depuis `index.js` :

```
import "./style/main.less";
```

Ensuite, mettons à jour notre propriété de configuration `module` de webpack :

```js
module: {
  rules: [{
    test: /\.(js|jsx)$/,
    exclude: /node_modules/,
    use: ['babel-loader', 'eslint-loader']
  },
  {
    test: /\.less$/,
    use: [
      'style-loader',
      'css-loader',
      'less-loader',
    ],
  },
 ]
},
```

Exécutez le script de démarrage et nous sommes prêts à partir !

### Déployer l'application React sur Netlify

Toutes les applications doivent être déployées pour la dernière étape, et pour les applications React, le déploiement est très facile.

Tout d'abord, changeons la sortie de construction et le `contentBase` de développement de `dist` à `build` dans notre configuration Webpack.

```js
module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'build'), // changez ceci
    publicPath: '/',
    filename: 'bundle.js'
  },
  devServer: {
    contentBase: "./build",
  },
//...
```

Maintenant, installons un nouveau plugin Webpack nommé HtmlWebpackPlugin

```
npm install html-webpack-plugin -D
```

Ce plugin générera un fichier `index.html` dans le même répertoire où notre `bundle.js` est créé par Webpack. Dans ce cas, le répertoire `build`.

Pourquoi avons-nous besoin de ce plugin ? Parce que Netlify nécessite qu'un seul répertoire soit fait le répertoire racine, donc nous ne pouvons pas utiliser `index.html` dans notre répertoire racine avec Netlify. Vous devez mettre à jour votre configuration webpack pour qu'elle ressemble à ceci :

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {
  entry: //...
  output: {
    //...
  },
  devServer: {
    contentBase: "./build",
  },
  module: {
    //...
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.resolve('./index.html'),
    }),
  ]
};
```

Et veuillez supprimer la balise `script` de votre `index.html` :

```html
<!DOCTYPE html><html>  <head>    <title>Ma configuration React</title>  </head>  <body>    <div id="root"></div>  </body></html><!DOCTYPE html>
<html>
  <head>
    <title>Ma configuration React</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

Maintenant, vous pouvez tester la configuration avec la commande `npm run build`. Une fois terminé, poussez votre modèle dans un dépôt GitHub. Il est temps de déployer notre application !

Maintenant, enregistrons un compte [Netlify](https://netlify.com). Si vous n'avez jamais entendu parler de Netlify auparavant, c'est un hébergement de site statique incroyable qui fournit tous les outils dont vous avez besoin pour déployer un site statique gratuitement. Qu'est-ce qu'un site statique ? C'est un site web créé à partir d'une collection de pages HTML statiques, sans aucun backend. Notre modèle React tel qu'il est maintenant compte comme un site statique, car nous n'avons pas de backend configuré et ce n'est que du HTML et du JavaScript.

Après l'inscription, sélectionnez un nouveau site à partir de Git et choisissez GitHub comme votre fournisseur Git :

![Image](https://cdn-media-1.freecodecamp.org/images/WfWqORsZjfHKwOpZ63d-nZUC6N2FF9CPzDrg)

Vous devez accorder des permissions à Netlify, puis sélectionner votre dépôt de modèle React.

![Image](https://cdn-media-1.freecodecamp.org/images/MtKFlYYRZVZ7JNcmP8AHiiDV5OLlJoy4hBk5)

Maintenant, vous devez entrer la commande de construction et le répertoire de publication. Comme vous pouvez le voir, c'est pourquoi nous avons besoin de _HtmlWebpackPlugin_, car nous devons tout servir à partir d'un seul répertoire. Plutôt que de mettre à jour manuellement notre fichier `index.html` racine pour les modifications, nous le générons simplement en utilisant le plugin.

![Image](https://cdn-media-1.freecodecamp.org/images/aecd4gyxtTE22EuPoHzXRe1yA9I9BqTaPfa1)

Assurez-vous d'avoir la même commande que dans la capture d'écran ci-dessus, sinon votre application risque de ne pas fonctionner.

![Image](https://cdn-media-1.freecodecamp.org/images/T3GN2LRCZtTIfNNOSVPV-tKgrmlllnRVcmcs)

Une fois que le statut de déploiement passe à `publié` (numéro 2 ci-dessus), vous pouvez accéder au nom de site aléatoire que Netlify a attribué à votre application (numéro 1).

Votre application React est déployée. Génial !

### Conclusion

Vous venez de créer votre propre modèle de projet React et de le déployer en direct sur Netlify. Félicitations ! Certes, je ne suis pas allé très loin dans les configurations de webpack, car ce modèle est destiné à être un point de départ générique. Dans certains cas où nous avons besoin de fonctionnalités avancées comme le rendu côté serveur, nous devons à nouveau ajuster la configuration.

Mais détendez-vous ! Vous en êtes arrivé là, ce qui signifie que vous comprenez déjà ce que font webpack, Babel, Prettier et ESLint. Webpack dispose de nombreux chargeurs puissants qui peuvent vous aider dans de nombreux cas que vous rencontrerez fréquemment lors de la création d'une application web.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine fois !
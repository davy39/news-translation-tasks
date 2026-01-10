---
title: Comment combiner Webpack 4 et Babel 7 pour créer une application React fantastique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-11T21:21:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CU4VcsMlDhlRLrCEkjNUvw.jpeg
tags:
- name: Babel
  slug: babel
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: React
  slug: react
- name: webpack
  slug: webpack
seo_title: Comment combiner Webpack 4 et Babel 7 pour créer une application React
  fantastique
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@visualsbydanny?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">daniel
  odame / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  I previ...'
---

Par Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-250.png)
_Photo par [Unsplash](https://unsplash.com/@visualsbydanny?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">daniel odame</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

J'ai précédemment écrit un article intitulé **[Comment maîtriser Webpack 4 et construire une application React géniale](https://medium.freecodecamp.org/how-to-conquer-webpack-4-and-build-a-sweet-react-app-236d721e6745).** Peu de temps après avoir écrit l'article, Babel est intervenu avec un changement majeur et de nombreux packages sont devenus obsolètes. J'ai donc décidé d'écrire un nouveau tutoriel.

Je vais me concentrer sur la configuration de **webpack** avec **React** qui aura un support **.scss** ainsi que la **division de code**

Le but de réécrire cela est simple : je veux que tout le monde se sente à l'aise. Parce que configurer webpack peut être vraiment intimidant. Surtout pour les nouveaux développeurs. Suivez le guide, et ce qui semblait difficile et peut-être effrayant semblera un jeu d'enfant.

Avant de commencer, voici le [**code source**](https://github.com/adeelibr/react-starter-kit). Je sais que cela contient beaucoup de choses. Je prévois d'utiliser la même base de code pour parler de webpack, react, SCSS, remplacement de module à chaud, tests avec jest et enzyme, linting de code, et ajout d'un formateur de code comme prettier dans d'autres articles à venir, donc je continuerai à mettre à jour cette base de code. Je ne gonflerai pas cette base de code — je le promets.

Note : Si vous avez envie de faire une PR pour le [dépôt](https://github.com/adeelibr/react-starter-kit), vous êtes plus que bienvenu :) Alors commençons.

Pour simplifier, cet article va seulement se concentrer sur ;

* Configuration de Webpack 4 avec Babel 7 pour React
* Support pour .SCSS
* Division de code
* Environnement de développement avec HMR (Hot Module Replacement)
* Configuration de production
* Division de votre configuration Webpack en morceaux
* Gestion des environnements de staging, démo, production, test et autres dans le code
* Génération d'un visualiseur dans la build de production pour vérifier quelle partie du code a pris combien d'espace et quelles sont les dépendances des morceaux. Super utile.

### Prérequis

Vous devez avoir node installé pour utiliser npm (node package manager).

D'abord, créez un dossier appelé `app` puis ouvrez votre terminal et allez dans ce dossier `app` et tapez :

```
npm init -y
```

Cela créera un fichier `package.json` pour vous.

Ensuite, créez un dossier appelé `src` dans votre dossier `app`. À l'intérieur de `app/src`, créez un fichier appelé `index.js` et écrivez le code suivant.

```javascript
console.warn('Je suis un nerd de Star Trek');
console.log('Tout au long de ce tutoriel, vous verrez beaucoup de citations de Star Trek');
console.log('En commençant maintenant');
console.log("La compassion : c'est la seule chose qu'aucune machine n'a jamais eue. Peut-être que c'est la seule chose qui maintient les hommes devant eux. -Dr McCoy");
```

Vous pouvez bien sûr écrire n'importe quoi ci-dessus. J'ai choisi Star Trek.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YPG3f4mWE9454CRPt53RiQ.jpeg)
_Le changement est le processus essentiel de toute existence. — Spock_

Ensuite, nous devons installer quelques dépendances. Vous pouvez simplement copier les `dependencies` et `devDependencies` du `package.json` ci-dessous dans le vôtre et faire un `**npm install**`**:**

```json
{
  "name": "react-boiler-plate",
  "version": "1.0.0",
  "description": "Un modèle de base pour React",
  "main": "src/index.js",
  "author": "Adeel Imran",
  "license": "MIT",
  "scripts": {
    "start": "un script viendra ici"
  },
  "dependencies": {
    "react": "^16.5.2",
    "react-dom": "^16.5.2"
  },
  "devDependencies": {
    "@babel/core": "^7.0.0",
    "@babel/plugin-proposal-class-properties": "^7.0.0",
    "@babel/plugin-proposal-export-namespace-from": "^7.0.0",
    "@babel/plugin-proposal-throw-expressions": "^7.0.0",
    "@babel/plugin-syntax-dynamic-import": "^7.0.0",
    "@babel/polyfill": "^7.0.0-beta.51",
    "@babel/preset-env": "^7.0.0-beta.51",
    "@babel/preset-react": "^7.0.0-beta.51",
    "babel-loader": "^8.0.0-beta.0",
    "copy-webpack-plugin": "^4.5.1",
    "css-loader": "^0.28.11",
    "html-webpack-plugin": "^3.2.0",
    "mini-css-extract-plugin": "^0.4.3",
    "node-sass": "^4.8.3",
    "optimize-css-assets-webpack-plugin": "^4.0.0",
    "sass-loader": "^7.0.3",
    "style-loader": "^0.21.0",
    "uglifyjs-webpack-plugin": "^1.2.5",
    "webpack": "^4.12.0",
    "webpack-cli": "^3.0.8",
    "webpack-dev-server": "^3.1.4",
    "webpack-merge": "^4.1.3",
    "webpack-visualizer-plugin": "^0.1.11"
  }
}
```

Oui, je sais, je sais ! C'est beaucoup pour créer une application React hello world. Mais attendez, c'est tout ce dont vous aurez besoin. Même si vous voulez créer une application de niveau entreprise. (Peut-être une ou deux choses de plus selon vos besoins, mais c'est l'épine dorsale.)

Alors parlons de chacun d'entre eux avant de plonger profondément dans le code.

[webpack](http://webpack.js.org) : Nous avons besoin de Webpack pour bundler notre code.

[webpack-cli](https://github.com/webpack/webpack-cli) : Nous allons utiliser certaines fonctionnalités CLI de Webpack pour faciliter notre vie lors de l'écriture de certains scripts.

[webpack-dev-server](https://github.com/webpack/webpack-dev-server) : Je vais créer un serveur en utilisant le package webpack-dev-server. Cela n'est destiné qu'à être utilisé dans l'environnement de développement, et non pour la production. Cela signifie que pendant le développement et le travail sur mon code, je n'ai pas besoin d'un serveur séparé comme NodeJS à configurer manuellement.

[webpack-merge](https://github.com/survivejs/webpack-merge) : Pour diviser notre configuration en morceaux, plus sur cela plus tard

[webpack-visualizer-plugin](https://github.com/chrisbateman/webpack-visualizer#readme) : Pour voir une représentation visuelle de chaque taille de bundle — combien d'espace ils prennent et quelles sont leurs dépendances.

[style-loader](https://github.com/webpack-contrib/style-loader) : Cela ajoute du CSS au DOM en injectant une balise `<script` /> dans l'en-tête

[sass-loader](https://github.com/webpack-contrib/sass-loader) : Pour le support SCSS

[node-sass](https://github.com/sass/node-sass) : Une dépendance pour sass-loader

[css-loader](https://github.com/webpack-contrib/css-loader) : Pour convertir nos fichiers .scss en .css

[mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin) : Ce plugin extrait le CSS dans des fichiers séparés. Il crée un fichier CSS par fichier JS qui contient du CSS.

[uglifyjs-webpack-plugin](https://github.com/webpack-contrib/uglifyjs-webpack-plugin) : Pour minifier le code JavaScript pour la production

[optimize-css-assets-webpack-plugin](https://github.com/NMFR/optimize-css-assets-webpack-plugin) Pour minifier le code CSS pour la production

[html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin) : Cela fait plus que générer un fichier HTML, il supporte les fichiers .css et .js à la demande automatiquement ajoutés à vos fichiers HTML à la demande

[copy-webpack-plugin](https://webpack.js.org/plugins/copy-webpack-plugin/) : Copie des fichiers/dossiers dans votre dossier de build.

[babel-loader](https://github.com/babel/babel-loader) : C'est le loader qui aide webpack à compiler les fichiers .js

[@babel/core](https://github.com/babel/babel/tree/master/packages/babel-core) : Compilateur principal de Babel, c'est une dépendance qui vous permet d'utiliser babel-loader

[@babel/preset-react](https://www.npmjs.com/package/@babel/preset-react) Préréglage Babel pour le code React

[@babel/preset-env](https://github.com/babel/babel/tree/master/packages/babel-preset-env) : Préréglage Babel qui vous permet d'utiliser le dernier JavaScript

[@babel/pollyfill](https://babeljs.io/docs/en/next/babel-polyfill.html) : Babel inclut un [polyfill](https://en.wikipedia.org/wiki/Polyfill_(programming)) qui inclut un runtime [regenerator](https://github.com/facebook/regenerator/blob/master/packages/regenerator-runtime/runtime.js) personnalisé et [core-js](https://github.com/zloirock/core-js). Cela émulera un environnement ES2015+ complet. Cela signifie un support pour le type de syntaxe sugar `async/await`.

> _Jusqu'à présent, c'est à peu près ce que j'ai écrit dans [**Comment maîtriser Webpack 4 et construire une application React géniale**](https://medium.freecodecamp.org/how-to-conquer-webpack-4-and-build-a-sweet-react-app-236d721e6745)**.**_

**Alors, qu'est-ce qui a changé ?**

Eh bien ! Babel a introduit un changement majeur (pour le plus grand bien, croyez-moi) que vous pouvez lire ici : [**Suppression des préréglages de stage de Babel**](https://babeljs.io/blog/2018/07/27/removing-babels-stage-presets)**.** Ce que cela signifiait, c'est qu'avant, si vous incluez babel-preset-stage-2 par exemple, il inclurait toutes les propositions liées au stage-2, ce qui alourdirait votre code. Mais vous pourriez avoir besoin d'une seule fonctionnalité spécifique du stage-2.

Alors, pour combattre cela, Babel a obsolète tous ces plugins de préréglage et a expédié des fonctionnalités individuelles. Vous devez maintenant les configurer manuellement. **Cool, non ?** Alors parlons un peu de ces packages individuels et de ce qu'ils font.

[@babel/plugin-proposal-class-properties](https://babeljs.io/docs/en/next/babel-plugin-proposal-class-properties.html) : Convertit votre syntaxe `class` en une `function` pour les navigateurs qui ne supportent pas la syntaxe `class`

[@babel/plugin-proposal-export-namespace-from](https://babeljs.io/docs/en/next/babel-plugin-proposal-export-namespace-from.html) Supporte la syntaxe comme `import * as ns from '../path/to/module';`

[@babel/plugin-proposal-throw-expressions](https://github.com/tc39/proposal-throw-expressions) Nouvelle syntaxe pour lancer des exceptions depuis un contexte d'expression. **J'adore cette fonctionnalité :D**

[@babel/plugin-syntax-dynamic-import](https://babeljs.io/docs/en/next/babel-plugin-syntax-dynamic-import.html) C'est ce qui aide à la division de code. Webpack est livré avec la division de code par défaut (depuis webpack 1). Mais lorsque vous voulez diviser le code dans webpack tout en utilisant **babel**, alors vous devez utiliser ce plugin.

Note : pour ce tutoriel, vous n'aurez pas besoin de `@babel/plugin-proposal-export-namsespace-from` et `@babel/plugin-proposal-throw-expressions`

> _Voici également une liste de tous les plugins babel. Je veux dire tous. Consultez la liste [**ici**](https://babeljs.io/docs/en/plugins)**.**_

Et maintenant que vous savez pourquoi nous avons besoin de ce dont nous avons besoin — rien d'extra — vous vous sentirez plus confiant pour implémenter la configuration webpack.

Commençons par ajouter un fichier `.babelrc` à la racine de notre dossier `app` :

```
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react"
  ],
  "plugins": [
    "@babel/plugin-syntax-dynamic-import",
    "@babel/plugin-proposal-class-properties",
    "@babel/plugin-proposal-export-namespace-from",
    "@babel/plugin-proposal-throw-expressions"
  ]
}
```

Nous avons 2 presets principaux `preset-env` et `preset-react`. Le reste sont nos plugins pour ajouter des "**ailes**" à notre code.

Et pour citer le Capitaine Kirk de Star Trek (parce que pourquoi pas) :

> _Peut-être que l'homme n'était pas fait pour le paradis. Peut-être qu'il était fait pour se battre, pour se battre tout au long du chemin. Capitaine Kirk_

En sa défense, le Capitaine Kirk était confronté à des ennemis comme le Général Chang, Khan, les Borgs et tant d'autres ennemis dangereux. Tout ce à quoi nous sommes confrontés, c'est le beau **Webpack** et **Babel**. Alors peut-être que nous, les développeurs, sommes faits pour le paradis.

Alors configurons notre webpack.

Créez un dossier `config` dans votre `app`. Si vous vous sentez perdu, vous pouvez à tout moment vous référer au dépôt GitHub [repository](https://github.com/adeelibr/react-starter-kit/tree/master/config) pour cela. Maintenant, à l'intérieur de notre dossier `config`, créons un fichier appelé `webpack.base.config.js`. La raison pour laquelle je l'appelle `base` est qu'il va être utilisé pour notre développement et pour la production. _Parce que pourquoi écrire la même chose deux fois ?_ Encore une fois, si cela n'a pas beaucoup de sens, restez avec moi quelques minutes de plus.

Dans votre `config/webpack.base.config.js`, écrivez ceci :

```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      },
    ]
  }
}
```

Une fois que vous l'avez en place, exécutez cette commande dans votre répertoire racine `app`. (Je vous dirai ce que fait cette commande un peu plus tard avec le code que nous avons écrit ci-dessus, je le promets.)

```
$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

Une fois que vous avez exécuté cette commande, vous verrez cet écran :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nAW_kvzNLvtce5cyTsbaVg.png)
_Oh ! Une Erreur Fancy !_

Alors, qu'est-ce qui s'est passé ici ? Eh bien, lorsque nous avons exécuté la commande webpack, il a bien trouvé notre fichier `index.js` que nous avons écrit précédemment dans `app/src/index.js` — mais il n'avait pas de `.html` pour l'exécuter. Alors créons un fichier `index.html` dans notre dossier `app/src` :

```html
<!DOCTYPE HTML>

<html>

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <base href="/">
  <title>Tutoriel</title>
</head>

<body>
  <div id="app"></div>
</body>

</html>
```

Mettons également à jour notre `webpack.base.config.js` :

```javascript
var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({ 
      template: './src/index.html', 
      filename: './index.html' 
    })
  ]
}
```

Exécutons cette commande à nouveau maintenant :

```
$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

Votre navigateur s'ouvrira. Si vous utilisez Google Chrome, appuyez sur `ctrl+shift+j` et la console de votre navigateur s'ouvrira. Vous verrez quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qXyjH3FzHCPHZqBeJTDbIg.png)
_Hé, regardez ça, c'est ce que j'ai écrit dans ma console ! Vous devriez voir quelque chose de similaire de votre côté aussi._

Alors parlons de ce qui s'est passé ici. Notre `webpack.base.config.js` a deux choses principales : les modules et les plugins. Un module peut avoir plusieurs règles, et chaque règle est appliquée à un certain type de fichier. Le certain type de fichier auquel nous voulons appliquer cette règle est dans `test` de cette règle :

```javascript
rules: [      
  {        
    test: /\.js$/,        
    exclude: /node_modules/,        
    use: {          
      loader: 'babel-loader'        
    }      
  },    
]
```

Ici, en disant `test: /\.js$./,` nous disons à webpack d'appliquer cette règle uniquement pour les fichiers `.js`. L'autre chose est `exclude` qui prend également une expression regex de ce qu'il ne faut pas inclure. C'est là que nous lui disons de ne pas compiler `node_modules` car cela compilerait tout, et il y a beaucoup de dépendances installées. Vérifiez vous-même le `node_modules`. La dernière partie est `use`.

Maintenant, webpack sait où appliquer la règle en utilisant `test` et où ne pas appliquer la règle en utilisant `exclude` — mais quelle est exactement la règle ? C'est là que `use` entre en jeu : ici nous spécifions `loader: 'babel-loader'`. Maintenant, ce que fait `babel-loader`, c'est qu'il cherche le fichier `.babelrc` que nous avons écrit précédemment. Et tous les presets et plugins que nous y avons écrits. Il les prend tous et les applique à nos fichiers `.js`.

Ce qui nous amène à la question suivante : comment **Webpack 4** trouve-t-il ces fichiers ? Eh bien, Webpack 4 est livré avec beaucoup de choses par défaut déjà configurées pour vous. Deux d'entre elles sont `entry` et `output`.

Le point d'`entry` par défaut est le répertoire `src` que nous avons écrit dans notre dossier `app`.

Le point `output` est l'endroit où tout le code bundlé compilé est généré, qui sera le dossier `dist` dans notre dossier `app`. (Vous ne le verrez pas maintenant, car nous n'avons pas encore compilé notre code pour la production.)

Ensuite, nous parlerons de `html-webpack-plugin`. Le but de ce plugin est simple comme son nom l'indique. Il crée des fichiers HTML pour servir tous vos fichiers bundlés. (Tous — .js, .css, .scss, .img etc.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*9KgKgHb2QFjZY_Gk05OtkA.gif)
_Si vous avez suivi jusqu'à présent. Vous êtes géniaux_

Parlons de ce qui se passe lorsque nous exécutons ce qui suit :

```
$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

Cette commande ouvrira le port `[http://localhost:8080](http://localhost:8080)` ou un autre port si `8080` est pris. (Je parlerai plus en détail de ce que fait cette commande plus tard — pour l'instant, continuons.)

L'_index.html_ généré ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nm_1jPCBvb0lXTTWuAl5XQ.png)
_Je viens de cliquer sur **ctrl + shift + i**, cela a ouvert l'inspecteur d'éléments dans mon navigateur Chrome_

**Partie bleue :** La partie bleue est simplement l'endroit où j'ai mis mes balises meta et défini un titre pour l'application.

**Partie jaune :** La partie jaune mise en évidence est la partie codée en dur que nous avons écrite dans notre fichier `**index.html**`. C'est là que résidera notre future application React.

**Partie rouge :** La partie que j'ai soulignée en rouge est la partie la plus intéressante. Nous ne l'avons jamais écrite dans notre fichier index.html, alors d'où vient-elle ?

Webpack est très intelligent. Il a pris ce fichier dans votre `**index.js**`, l'a bundlé proprement, et l'a ajouté proprement dans le fichier appelé `**main.js**`. Ensuite, il l'a injecté dans notre fichier `**index.html**`. Super Cool !

> _Nous sommes à environ 60% **terminés !** Croyez-moi, la partie difficile est terminée…_

### Ajoutons React

Le truc cool, c'est que toutes nos dépendances sont déjà installées. Et tout est déjà configuré. Donc dans votre `app/src/index.js`, supprimez tout le code et remplacez-le par ceci :

```javascript
import React from 'react';
import ReactDOM from 'react-dom';

const App = () => {
  return (
    <div>
      <p>
        Nous sommes une espèce des plus prometteuses, Monsieur Spock, en tant que prédateurs. Le saviez-vous ? J'ai fréquemment
        des doutes. Je n'en ai plus. Plus maintenant. Et peut-être dans mille ans ou plus, nous serons capables
        de le prouver.
      </p>
      <p>- Capitaine Kirk</p>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('app'));
```

Maintenant, si votre terminal exécute toujours le script `webpack-dev-server`, vérifiez simplement le navigateur. Sinon, voici le script. Je ne veux pas que vous remontiez tout en haut.

```
$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

Voici ce que vous verrez :

![Image](https://cdn-media-1.freecodecamp.org/images/1*k2GbkHxf8qrs3lqM6R-bAg.png)
_C'est notre application React en direct._

Maintenant, assurez-vous de ne pas fermer le terminal, et allez dans votre `app/src/index.js` et faites quelques modifications à votre composant `<App` />. Essayez de changer la phrase dans le paragraphe. Une fois modifié, retournez à votre navigateur et le contenu est déjà mis à jour. N'est-ce pas cool ? :D

> _Cela résume 70% de notre tutoriel — il ne reste plus que 30%. Vous faites du bon travail._

### **Ajoutons le support SCSS**

Commençons par mettre à jour notre `config/webpack.base.config.js` en ajoutant une autre règle pour les fichiers `.scss`

```javascript
var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      },
      {
        test: /\.scss$/,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader'
        ]
      },
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      filename: './index.html'
    }),
  ]
}
```

Donc, l'`use` que j'utilise ici prend un tableau au lieu d'un objet comme ce que j'ai fait pour les fichiers `.js`. C'est parce que nous devons appliquer un ensemble de règles ici :

```
use: [ 'style-loader','css-loader','sass-loader' ]
```

Alors lisons le tableau `use` de `droite à gauche` — c'est **important**. Ce que nous disons à Webpack, c'est de prendre tous les fichiers `.scss` qu'il trouve et de les analyser pour sa propre compréhension en utilisant le **sass-loader**. Une fois qu'il les a convertis en sass, nous demandons ensuite à Webpack de convertir le sass en CSS. Pour cela, nous appliquons **css-loader**.

À ce stade, nous avons converti le .scss en .css. Mais il n'y a aucun moyen pour nous d'ajouter les fichiers convertis dans notre `.html`. Pour cela, nous utilisons le dernier loader appelé **style-loader** qui prend tout le .css converti et l'injecte dans notre fichier `index.html`.

Alors ajoutons un peu de `.scss` pour tester cela. Dans votre dossier `src/`, ajoutez un fichier appelé `myStyles.scss`. Le mien ressemble à celui ci-dessous :

```css
body {
  background-color: skyblue;
  color: black;
}

.app {
  width: 450px;
  margin: 0 auto;
  padding-top: 50px;
}
```

Et mon fichier `src/index.js` ressemble à ceci :

```javascript
import React from 'react';
import ReactDOM from 'react-dom';

import './myStyles.scss';;

const App = () => {
  return (
    <div className="app">
      <p>
        Nous sommes une espèce des plus prometteuses, Monsieur Spock, en tant que prédateurs. Le saviez-vous ? J'ai fréquemment
        des doutes. Je n'en ai plus. Plus maintenant. Et peut-être dans mille ans ou plus, nous serons capables
        de le prouver.
      </p>
      <p>- Capitaine Kirk</p>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('app'));
```

Redémarrez votre `webpack-dev-server` en exécutant à nouveau cette commande :

```
$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

> _C'était la dernière fois que je vous faisais écrire manuellement ce script. Après cela, nous déplacerons cette commande dans notre section `scripts` dans notre `package.json`._

Votre navigateur s'ouvrira, voici à quoi cela ressemble maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_S0JUOyiRMMbXQKfl_lv1Q.png)
_Nice! non ?_

Maintenant, dans votre fichier `myStyles.scss`, essayez de faire quelques modifications. Comme faire `font-size: white;` revenez à votre navigateur. Il reflète ces changements. Vous n'avez pas besoin de redémarrer votre serveur à nouveau — juste pour que le `.scss` compile.

Avec cela, la plupart de notre configuration de développement est terminée. Notre application React est en direct, et a un remplacement de module à chaud pour les fichiers `.js` ainsi que les fichiers `.scss`

Alors, avant d'aller plus loin, ajoutons le script `webpack-dev-server` dans notre `package.json`. Dans votre section `**scripts**`, ajoutez le code suivant :

```json
"scripts": {
    "start": "webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback --env.PLATFORM=local --env.VERSION=stag",
    "prebuild": "webpack --mode production --config config/webpack.prod.config.js --env.PLATFORM=production --env.VERSION=stag --progress",
    "build": "node server",
},
```

Pour l'instant, je vais parler de la commande `start`. Je parlerai des scripts `prebuild` et `build` plus tard dans la section de configuration de production.

Alors, que fait cette commande : `npm run start`

```
"start": "webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback"
```

Décomposons cela. Lorsque nous exécutons `npm run start`, nous lui disons d'exécuter un package appelé `webpack-dev-server`. Ensuite, nous lui passons quelques configurations.

* `webpack-dev-server` sert une application webpack et met à jour le navigateur en cas de changements.
* `--mode development` indique à `webpack` de compiler le code en mode développement. Cela est principalement pour rendre le temps de compilation plus rapide.
* `--config config/webpack.base.config.js` Donc par défaut, si vous avez un fichier `webpack.config.js` dans votre dossier racine `app`, vous n'avez pas besoin de fournir le drapeau `--config`. Mais comme je veux ajouter explicitement toutes mes configurations liées à webpack dans le dossier `config`, je passe l'option `--config` qui indique à webpack où chercher la configuration
* La commande `--open` ouvre le navigateur, lorsque webpack a terminé sa compilation.
* Le drapeau `--hot` indique à webpack de surveiller activement les changements de code dans le dossier `src`. Si des changements se produisent, il recharge le navigateur.
* `--history-api-fallback` Cette option active la prise en charge de [History API Fallback](https://github.com/bripkens/connect-history-api-fallback) dans `webpack-dev-server`, demandant effectivement au serveur de revenir à `index.html` dans le cas où une ressource demandée ne peut pas être trouvée.
* `--env.PLATFORM` et `--env.VERSION` sont des drapeaux personnalisés que je passe dans ma configuration (plus sur cela plus tard).

Maintenant que nous avons terminé, passons à nos configurations de **production**.

Mais avant de faire cela, parlons de `webpack-merge`. Maintenant, c'est un vrai gagnant. Il prend une configuration et une autre et les fusionne pour nous donner une seule. La façon dont cela fonctionne est que vous devez envelopper votre configuration avec `merge` comme celle ci-dessous. Commençons par faire de notre fichier `webpack.base.config.js` un morceau utilisable par `webpack-merge` :

```javascript
const webpack = require('webpack');
const merge = require("webpack-merge");

const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = env => {
  const { PLATFORM, VERSION } = env;
  return merge([
      {
        module: {
          rules: [
            {
              test: /\.js$/,
              exclude: /node_modules/,
              use: {
                loader: 'babel-loader'
              }
            },
            {
              test: /\.scss$/,
              use: [
                'style-loader',
                'css-loader',
                'sass-loader'
              ]
            }
          ]
        },
        plugins: [
          new HtmlWebpackPlugin({
            template: './src/index.html',
            filename: './index.html'
          }),
          new webpack.DefinePlugin({ 
            'process.env.VERSION': JSON.stringify(env.VERSION),
            'process.env.PLATFORM': JSON.stringify(env.PLATFORM)
          }),
        ],
    }
  ])
};
```

Auparavant, où nous exportions un `object`, maintenant nous exportons une `function` qui retourne `merge` et prend la configuration.

Décomposons cela pour voir ce que cela fait. La première chose dont nous parlons est ceci :

```
module.exports = function(env) {}
```

Les nouveaux drapeaux ajoutés dans notre commande `start` ` env.PLATFORM=local  env.VERSION=stag` sont passés à nos configurations webpack, auxquels nous pouvons accéder avec le paramètre `env` dans `module.exports = function (env) {}`. Alors, que pouvons-nous faire avec cela ?

* Nous pouvons mettre en place une instruction conditionnelle dans notre configuration webpack, qui si une certaine condition est remplie, alors faire ceci ou cela (plus sur cela plus tard). Basiquement, nous allons changer notre configuration au moment de la compilation pour répondre à l'environnement qui est exécuté  production ou développement.
* L'autre chose que nous pouvons faire ici est de les passer dans notre code également. Alors, que veux-je dire par passer dans notre code ? Un nouveau plugin que j'ai ajouté pour cela s'appelle `**new webpack.DefinePlugin**`**.** (C'est aussi pourquoi j'ai dû inclure webpack en haut de `webpack.base.config.js`.) Ce que cela fait est : _The `DefinePlugin` vous permet de créer des constantes globales qui peuvent être configurées au moment de la compilation._ Vous pouvez en lire plus à ce sujet [**ici**](https://webpack.js.org/plugins/define-plugin/)**.**

Ensuite, nous retournons une configuration à l'intérieur de la fonction comme ceci :

```
return merge({ 
   // notre configuration webpack ici
});
```

Eh bien, pas grand-chose n'a changé ici. Tout ce que nous avons fait, c'est envelopper notre configuration dans `merge`. Cela nous donne la capacité de `fusionner` cette configuration entière dans l'autre que nous allons créer.

Une chose ajoutée est un nouveau plugin appelé `DefinePlugin` dont j'ai déjà parlé.

> _Si vous êtes un nerd comme moi et que vous voulez creuser plus profondément dans `webpack-merge`, je vous suggère de plonger dans [**ici**](https://github.com/survivejs/webpack-merge) **** cela a été développé par les gens cool de `[**SurviveJS**](https://survivejs.com/)`**.**_

Avant de passer aux paramètres de `production`, vérifions si nos configurations de base fonctionnent.

Dans votre fichier `src/index.js`, ajoutez ceci quelque part :

```
console.log('process.env.VERSION', process.env.VERSION);
```

```
console.log('process.env.PLATFORM', process.env.PLATFORM);
```

```
console.log('process.env.NODE_ENV', process.env.NODE_ENV);
```

Dans votre terminal, exécutez `npm run start`. Attendez que votre navigateur se charge. Ouvrez votre terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1XyF_YqUH8LZflGjtBSC1w.png)
_Cliquez sur **ctrl+shift+j** pour ouvrir la console dans votre navigateur_

Les deux premiers que vous voyez dans la console sont le résultat de notre passage des drapeaux `--env` de notre script à notre configuration webpack et de leur définition avec DefinePlugin. Le troisième est avec le drapeau `--mode` que nous passons dans notre script. Si le mode est développement ou production, alors cela est configuré dans notre drapeau `process.env.NODE_ENV`.

Maintenant que cela est clarifié, continuons.

Dans votre dossier `config`, créez un nouveau fichier appelé `webpack.prod.config.js` et ajoutez-y le code suivant comme montré ci-dessous :

```
var merge = require('webpack-merge');

// Plugins
var OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
var UglifyJsPlugin = require('uglifyjs-webpack-plugin');
var Visualizer = require('webpack-visualizer-plugin');

var baseConfig = require('./webpack.base.config');

const prodConfiguration = env => {
  return merge([
    {
      optimization: {
        runtimeChunk: 'single',
        splitChunks: {
          cacheGroups: {
            vendor: {
              test: /[\\/]node_modules[\\/]/,
              name: 'vendors',
              chunks: 'all'
            }
          }
        },
        minimizer: [new UglifyJsPlugin()],
      },
      plugins: [
        new OptimizeCssAssetsPlugin(),
        new Visualizer({ filename: './statistics.html' })
      ],
    },
  ]);
}

module.exports = env => {
  return merge(baseConfig(env), prodConfiguration(env));
}
```

Commençons par le bas avec `module.exports = env =>` {}

Nous fusionnons deux configurations : l'une est notre `baseConfig` et l'autre est `prodConfiguration`. Les drapeaux `--env` que nous passons dans nos scripts sont transmis en tant qu'objet dans les paramètres `env =>` {} de notre fonction. Nous les transmettons ensuite aux deux configurations `baseConfig` et `prodConfig`.

> Alors, qu'est-ce que `prodConfig` ?

C'est essentiellement une liste des optimisations que nous voulons effectuer lorsque notre code est mis en production.

L'`optimization.minimizer` prend un `new UglifyJsPlugin`. Ce que cela fait, c'est uglifier et minifier nos fichiers .js.

L'`optimization.splitChunks` prend en fait tout votre code commun et crée un fichier `vendor.bundle.js`. Il n'en créera pas un maintenant. Mais à mesure que notre base de code grandit, nous avons plusieurs routes, et il y a différents modules utilisés comme `date-fns` `moment` `lodash` `material-ui` etc. Il prendra tout le code commun de l'application entière et créera un fichier commun appelé `vendor.bundle.js`. De cette façon, le code répété n'est pas utilisé encore et encore. (Je suis contre cette approche, mais à des fins éducatives, je l'ai décrite ici.)

En allant de l'avant, je vais commenter `optimization.splitChunks`, mais il existera dans le dépôt de code si vous voulez l'utiliser. Vous devez simplement décommenter cette section. Je préfère diviser mon code en fonction des routes. Avoir un code commun extrait dans un module séparé signifie que tout votre code commun va être chargé en premier. Cela peut être énorme, et par conséquent, la première interaction de l'utilisateur prendra plus de temps (car maintenant toutes ces dépendances sont chargées, ce qui peut ne pas être nécessaire dans la page respective que l'utilisateur voit/consulte).

Ensuite, nous avons quelques plugins. L'un d'eux est `new OptimizeCssAssetsPlugin()`. Tout ce qu'il fait, c'est prendre tous nos fichiers `.css` générés et les minifier/optimiser. Cela ne fonctionne pas pour l'instant, car nous utilisons `style-loader` et style loader injecte directement le `.css` généré dans le DOM.

Tout d'abord, nous devons dire à webpack d'extraire tout le `.css` généré dans un fichier séparé, puis les optimisations ajoutées par ce plugin sont appliquées. (Nous ferons cela un peu plus tard.)

L'autre plugin ajouté ici s'appelle `new Visualizer({ filename: ./statistics.html })`. Ce plugin est génial : il génère un fichier `statistics.html` dans le dossier `dist/` pour vous. Ouvrez le fichier, et vous verrez un graphique comme celui ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V5_yljYjlwuTgQIiTtzkCQ.png)
_Image prise de [https://github.com/chrisbateman/webpack-visualizer](https://github.com/chrisbateman/webpack-visualizer" rel="noopener" target="_blank" title=")_

Pour l'instant, nous n'avons qu'un seul module appelé `main.js`. Mais avec le temps, à mesure que nous ajoutons plus de modules et que nous avons ajouté la division de code. Plus de modules commenceront à apparaître ici et nous pourrons réellement voir quels modules prennent quelle taille. Cela peut être vraiment utile lorsque vous essayez de réduire la taille de votre application.

Revenons à `OptimizeCssAssetsPlugin()`. Afin d'optimiser le .css généré, nous devons le déplacer dans un module séparé. Pour cela, je vais utiliser `mini-css-extract-plugin`. Cela nécessitera des modifications dans nos deux fichiers webpack, les fichiers `.base` et `.prod`.

```javascript
// webpack.base.config.js
const webpack = require('webpack');
const merge = require("webpack-merge");

const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = env => {
  const { PLATFORM, VERSION } = env;
  return merge([
      {
        module: {
          rules: [
            {
              test: /\.js$/,
              exclude: /node_modules/,
              use: {
                loader: 'babel-loader'
              }
            },
            {
              test: /\.scss$/,
              use: [
                PLATFORM === 'production' ? MiniCssExtractPlugin.loader : 'style-loader',
                'css-loader',
                'sass-loader'
              ]
            }
          ]
        },
        plugins: [
          new HtmlWebpackPlugin({
            template: './src/index.html',
            filename: './index.html'
          }),
          new webpack.DefinePlugin({ 
            'process.env.VERSION': JSON.stringify(env.VERSION),
            'process.env.PLATFORM': JSON.stringify(env.PLATFORM)
          }),
        ],
    }
  ])
};
```

```javascript
// webpack.prod.config.js
/* eslint-disable */
const merge = require('webpack-merge');
// Plugins
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const Visualizer = require('webpack-visualizer-plugin');
// Configs
const baseConfig = require('./webpack.base.config');

const prodConfiguration = env => {
  return merge([
    {
      optimization: {
        // runtimeChunk: 'single',
        // splitChunks: {
        //   cacheGroups: {
        //     vendor: {
        //       test: /[\\/]node_modules[\\/]/,
        //       name: 'vendors',
        //       chunks: 'all'
        //     }
        //   }
        // },
        minimizer: [new UglifyJsPlugin()],
      },
      plugins: [
        new MiniCssExtractPlugin(),
        new OptimizeCssAssetsPlugin(),
        new Visualizer({ filename: './statistics.html' })
      ],
    },
  ]);
}

module.exports = env => {
  return merge(baseConfig(env), prodConfiguration(env));
}
```

Parlons des changements que j'ai apportés dans `webpack.base.config.js`. Un seul module a été ajouté appelé `const MiniCssExtractPlugin = require(mini-css-extract-plugin);`. Ensuite, dans nos règles `.scss`, nous avons vérifié si le drapeau `PLATFORM` passé a la valeur `production`. Si c'est le cas, nous ajoutons `MiniCssExtractPlugin.loader`, sinon nous ajoutons le `style-loader`.

`style-loader` est utilisé pour surveiller activement et changer notre `.css` compilé en mode développement, tandis que `MiniCssExtractPlugin.loader` est utilisé lorsque nous devons extraire ce CSS généré dans un module séparé. Cela n'est que pour la production.

Dans l'autre fichier `webpack.prod.config.js`, nous avons ces deux plugins ajoutés :

```javascript
new MiniCssExtractPlugin(),
new OptimizeCssAssetsPlugin(),
```

Le premier extraira cela dans un module séparé appelé `main.css` et l'autre minifiera/uglifiera le CSS généré.

Ayant fait cela, nous sommes presque à 90% terminés. Si vous êtes resté jusqu'ici, félicitations à vous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vJuq08E4psbspTTfzRcHig.gif)
_Génial !_

Avant de continuer, voici ce que le Capitaine Kirk a à dire

> _Vous savez, le plus grand danger qui nous menace est nous-mêmes, et la peur irrationnelle de l'inconnu. Il n'y a pas de chose telle que l'inconnu. Seulement des choses temporairement cachées, temporairement non comprises._

> - James T. Kirk, La Maneuvre Corbomite

Ajoutons plus de fonctionnalités à notre code. Il y a deux façons d'ajouter des fichiers dans votre code. L'une est d'utiliser un autre loader appelé `file-loader` qui vous aidera à ajouter des fichiers de n'importe quel type dans vos fichiers .js comme nous l'avons fait avec les fichiers .scss.

Je veux parler d'une autre approche ici, car je pense que des actifs comme les polices, les images et autres devraient être chargés en parallèle plutôt que dans vos fichiers .js. Cela aide à fournir une meilleure expérience pour l'utilisateur. À cette fin, nous chargerons nos images de manière statique.

Pour cela, nous utiliserons un plugin appelé `copy-webpack-plugin`. Le meilleur dans tout cela, c'est que vous l'avez déjà installé. Dans votre `webpack.base.config.js`, ajoutez un autre plugin, comme ci-dessous :

```javascript
const CopyWebpackPlugin = require('copy-webpack-plugin'); // Ajoutez ceci en haut

module.exports = env => {
  return merge([
      {
        module: {},
        plugins: [
          new CopyWebpackPlugin([ { from: 'src/static' } ]), // Ajoutez ceci dans la section plugins
        ],
    }
  ])
};
```

Le `copy-webpack-plugin` prend un argument appelé `from`. Cela indique au plugin où localiser les fichiers statiques et ensuite les copier dans le dossier `dist`. Ici, je lui dis de chercher un dossier appelé `src/static` et de copier tout son contenu dans le dossier `dist/`.

Une fois que vous avez ajouté cela et l'avez configuré, tout ce que vous avez à faire est, dans votre dossier `app/src`, créer un nouveau dossier appelé `static`. Dans ce dossier, créez un autre dossier appelé `images` afin que votre dossier ait une structure de répertoire comme celle-ci : `app/src/static/images`

Je vais mettre une image ici appelée `header.jpg`, mais vous pouvez l'appeler comme vous voulez. Voici l'image que j'utilise : [https://unsplash.com/photos/Idi6I490p7I](https://unsplash.com/photos/Idi6I490p7I) (Photo par [Felix Mittermeier](https://unsplash.com/photos/Idi6I490p7I?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)).

Maintenant, pour que cela fonctionne, vous devez exécuter la commande `npm run prebuild` (je parlerai plus de `npm run prebuild` et `npm run build` plus tard lorsque nous configurerons notre serveur NodeJS avec ExpressJS) car nous devons que nos fichiers `static` soient copiés. La commande `npm run start` ne copiera pas cela dans le dossier `dist/` car elle ne compile pas le code dans le dossier `dist/`.

Une fois que vous avez exécuté la commande `npm run prebuild`, voici ce que vous verrez :

![Image](https://cdn-media-1.freecodecamp.org/images/1*IC58DnGCTt_KH7FMEmFNFg.png)
_Comme vous pouvez le voir, nous avons un dossier images et à l'intérieur de ce dossier, nous avons le fichier `header.jpg`_

Alors, comment pouvons-nous accéder à ce fichier dans notre code ?

Je vais apporter quelques modifications à mon fichier `index.js` ainsi qu'à `myStyles.scss`. Vous pouvez suivre également — nous ajoutons simplement une balise `<img` /> ainsi que `some` .scss

```javascript
import React from 'react';
import ReactDOM from 'react-dom';

import './myStyles.scss';

const App = () => {
  return (
    <div className="app">
      <img alt="header" src="/dist/images/header.jpg" className="app-header" />
      <p>
        Nous sommes une espèce des plus prometteuses, Monsieur Spock, en tant que prédateurs. Le saviez-vous ? J'ai fréquemment
        des doutes. Je n'en ai plus. Plus maintenant. Et peut-être dans mille ans ou plus, nous serons capables
        de le prouver.
      </p>
      <p>- Capitaine Kirk</p>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('app'));
```

```scss
body {
  background-color: skyblue;
  color: black;
}

.app {
  width: 450px;
  margin: 0 auto;
  padding-top: 50px;

  & .app-header {
    height: 250px;
    width: inherit;
    object-fit: cover;
  }
}
```

La seule chose à noter ici est dans le fichier `index.js` où j'ajoute une image :

```html
<img    
  alt="header"   
  src="/dist/images/header.jpg"
  className="app-header"
/>
```

La chose principale est le chemin que nous donnons dans le `src`.

Une fois que vous avez ajouté cela, vérifions comment cela apparaît dans le navigateur. Allez et exécutez la commande `npm run start`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EzP9VCYITSrahax4nkw8Dg.png)
_Hé ! Regardez, maman ! J'ai ajouté une image. Avec cela ajouté, notre configuration webpack est terminée._

#### Récapitulons ce que nous avons accompli jusqu'à présent

* Configuration de Webpack 4 avec Babel 7 pour React
* Support pour .SCSS
* Environnement de développement avec HMR [Pour .js et .scss]
* Configuration de production
* Division de votre configuration Webpack en morceaux
* Génération d'un visualiseur dans la build de production pour vérifier la taille de chaque morceau de code et leurs dépendances. Super utile.
* Support pour les fichiers statiques

#### Ce que nous devons encore accomplir

* Ajouter le support pour `async/await` dans notre code
* Créer un serveur NodeJS utilisant ExpressJS pour notre build de production
* Division de code

Commençons par `async/await`. À cette fin, je vais créer un composant `<App` /> intelligent. À l'intérieur de ce composant, je vais appeler une API qui me donne des informations sur le Capitaine Kirk, car il est génial. Donc dans notre `index.js`, ajoutez le code suivant :

```javascript
import React from 'react';
import ReactDOM from 'react-dom';

import './myStyles.scss';

class App extends React.Component {
  state = {
    CaptainKirkBio: {},
  };

  componentDidMount() {
    this.onGetKirkBio();
  }

  onGetKirkBio = async () => {
    try {
      const URL = 'http://stapi.co/api/v1/rest/character/search';
      const result = await fetch(URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: {
          title: 'James T. Kirk',
          name: 'James T. Kirk',
        },
      });
      const resultJSON = await result.json();
      const character = resultJSON.characters[0];
      this.setState({ CaptainKirkBio: character });
    } catch (error) {
      console.log('error', error);
    }
  };

  render() {
    const { CaptainKirkBio } = this.state;
    return (
      <div className="app">
        <img alt="header" src="/dist/images/header.jpg" className="app-header" />
        <p>
          Nous sommes une espèce des plus prometteuses, Monsieur Spock, en tant que prédateurs. Le saviez-vous ? J'ai fréquemment
          des doutes. Je n'en ai plus. Plus maintenant. Et peut-être dans mille ans ou plus, nous serons capables
          de le prouver.
        </p>
        <p>- Capitaine Kirk</p>
        <section>
          {Object.values(CaptainKirkBio).length === 0 ? (
            <p>Chargement des informations utilisateur</p>
          ) : (
            <p style={{ wordBreak: 'break-all' }}>{JSON.stringify(CaptainKirkBio)}</p>
          )}
        </section>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
```

Tout ce que je fais ici, c'est appeler une API en utilisant `try/catch` `async/await` et obtenir des informations sur le Capitaine Kirk. Simple, non ? Cela devrait fonctionner. Allumons cela dans le navigateur.

Exécutez la commande :

```
npm run start
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*EI1U0MLC_mu5i__W-ZzIsg.png)
_Notre application a planté ici ! Je me demande pourquoi ?_

Si vous appuyez sur `ctrl+shift+j`, votre console s'ouvrira, et vous verrez une erreur appelée `**regeneratorRuntime**`. Alors, qu'est-ce que cette erreur et comment s'en débarrasser ?

Cette erreur est lancée lorsque le navigateur ne supporte pas `async/await` ou les `generators` pour cela.

> Mais **Adeel** ! C'est la seule raison pour laquelle nous utilisons babel, non ?

Oui ! Voici ce que [**Henry Zhu**](https://twitter.com/left_pad), le gars génial derrière babel, a à dire à ce sujet :

> Si vous utilisez des générateurs/async et que l'environnement ne les supporte pas nativement, nous compilons en utilisant regenerator qui **utilise** un runtime. Vous devrez donc inclure regeneratorRuntime soit vous-même, soit utiliser babel-polyfill.

> Référence prise d'un [**problème**](https://github.com/babel/babel-preset-env/issues/92#issuecomment-266869180).

Maintenant que vous savez pourquoi cela existe, résolvons-le. Nous devons apporter quelques modifications à notre `webpack.base.config.js` :

```javascript
const path = require('path');
const webpack = require('webpack');
const merge = require("webpack-merge");

const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

const APP_DIR = path.resolve(__dirname, '../src'); // <===== nouveau contenu ajouté ici

module.exports = env => {
  const { PLATFORM, VERSION } = env;
  return merge([
      {
        entry: ['@babel/polyfill', APP_DIR], // <===== nouveau contenu ajouté ici
        module: {
          rules: [
            {
              test: /\.js$/,
              exclude: /node_modules/,
              use: {
                loader: 'babel-loader'
              }
            },
            {
              test: /\.scss$/,
              use: [
                PLATFORM === 'production' ? MiniCssExtractPlugin.loader : 'style-loader',
                'css-loader',
                'sass-loader'
              ]
            }
          ]
        },
        plugins: [
          new HtmlWebpackPlugin({
            template: './src/index.html',
            filename: './index.html'
          }),
          new webpack.DefinePlugin({ 
            'process.env.VERSION': JSON.stringify(env.VERSION),
            'process.env.PLATFORM': JSON.stringify(env.PLATFORM)
          }),
          new CopyWebpackPlugin([ { from: 'src/static' } ]),
        ],
    }
  ])
};
```

Vérifiez la `ligne no.8` et la `ligne no.14` dans l'extrait ajouté ci-dessus.

Par défaut, Webpack 4 prend le point d'entrée de `src/`. Mais si nous voulons avoir plusieurs points d'entrée, nous pouvons également personnaliser le point `entry`. Dans mon point d'entrée, je lui dis simplement deux choses :

```
entry: ['@babel/polyfill', APP_DIR],
```

* `@babel/polyfill` Plugin Babel qui inclut un [polyfill](https://en.wikipedia.org/wiki/Polyfill_(programming)) qui inclut un runtime [regenerator](https://github.com/facebook/regenerator/blob/master/packages/regenerator-runtime/runtime.js) personnalisé et [core-js](https://github.com/zloirock/core-js).
* `APP_DIR` le chemin vers notre dossier `src/` que j'ai écrit à la `ligne no.8` `const APP_DIR = path.resolve(__dirname, ../src);` Tout ce que fait cette ligne, c'est pointer vers le chemin du dossier `src/` dans notre dossier `app/`.

Donc, l'`entry` prend simplement des "points" sur ce qu'il faut compiler.

Maintenant que cela est clarifié, exécutons à nouveau la commande `npm run start`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KU6jA1T_EPqnCaV6JXQj-Q.png)
_Notre méthode async/await fonctionne. Super :D_

Jusqu'à présent, tout va bien !

#### Maintenant que tout est configuré, créons un serveur NodeJS en utilisant ExpressJS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RxqfJ9N01QH_K4BR-MRydg.gif)
_En citant les mots immortels de **Khan Noonien Singh**_

La première chose que nous devons installer est Express, alors dans votre terminal, écrivez ceci :

```
npm install express --save 
```

Ou si vous utilisez **yarn** (comme moi) :

```
yarn add express
```

Ensuite, dans le dossier racine `app`, créez un nouveau dossier appelé `server`. À l'intérieur du dossier, créez un fichier `index.js` comme celui montré ci-dessous :

```js
const express = require('express');
const path = require('path');
const http = require('http');

const app = express();

// Pointer le chemin statique vers dist
app.use('/', express.static(path.join(__dirname, '..', 'dist')));
app.use('/dist', express.static(path.join(__dirname, '..', 'dist')));

const routes = require('./routes');

app.use('/', routes);

/** Obtenir le port de l'environnement et le stocker dans Express. */
const port = process.env.PORT || '3000';
app.set('port', port);

/** Créer un serveur HTTP. */
const server = http.createServer(app);
/** Écouter sur le port fourni, sur toutes les interfaces réseau. */
server.listen(port, () => console.log(`Serveur en cours d'exécution sur le port ${port}`));
```

Discutons de ce code avant d'aller plus loin.

Nous instancions notre application avec `express()` puis nous configurons un dossier public statique appelé `**dist**`**.** C'est le même dossier créé par Webpack lorsque nous exécutons notre commande de production.

Nous incluons notre fichier `**routes**` — nous allons le créer dans une seconde — et nous définissons le fichier `**routes**` sur le répertoire `/`.

Ensuite, nous configurons un port. Si aucun n'est fourni via l'interface de ligne de commande node, nous utilisons le port `3000`. Après cela, nous créons un serveur HTTP et nous écoutons sur ce serveur via le port. Tout à la fin, nous affichons dans notre terminal que nous exécutons le serveur sur ce port spécifique.

Créons notre dernier fichier appelé `**routes/index.js`**:**

```javascript
const path = require('path');
const router = require('express').Router();

router.get('*', (req, res) => {
  const route = path.join(__dirname, '..', '..', 'dist', 'index.html');
  res.sendFile(route);
});

module.exports = router;
```

Ici, nous vérifions que, quelle que soit la page sur laquelle l'utilisateur arrive, le chemin redirige l'utilisateur vers `**dist/index.html**` où réside notre application React.

Et c'est tout. Nous avons terminé.

Maintenant, allez dans votre terminal et tapez :

```
npm run build
```

Cela prendra un moment. Il vous montrera la progression pendant la compilation. Après cela, il affiche un message dans la console indiquant qu'il écoute sur le port 3000 si aucun port n'est fourni.

Maintenant, allez dans votre navigateur `http:localhost:3000/` et votre application est en vie.

Puisque nous y sommes, parlons en détail de ce que font `npm run prebuild` et `npm run build`.

En fait, si nous écrivons le mot `pre` pour un script, dans ce cas `prebuild`, chaque fois que nous exécutons notre commande `npm run build`, il exécutera d'abord `npm run prebuild` puis exécutera le script `npm run build`.

Tout ce que fait `npm run build`, c'est exécuter `node server/index.js` (Vous n'avez pas besoin d'écrire /index.js) dans la commande. NodeJS est assez intelligent pour savoir qu'il doit exécuter le `index.js` à l'intérieur du dossier `server`.

Cela résume également la configuration de notre application NodeJS.

Un dernier sujet à aborder. Je vais donner un aperçu très bref de la division de code et de la manière dont vous pouvez l'atteindre.

### Division de code

Au début de ce tutoriel, nous avons ajouté `@babel/plugin-syntax-dynamic-import`. Cela nous donne la possibilité de charger paresseusement notre code à l'intérieur de notre application.

À l'intérieur de mon dossier `src/`, je vais créer un composant appelé `Foo.js` qui ressemble à ceci.

```jsx
import React from 'react';

export default () => (
  <div>
    <p>Je suis Foo ! Enchanté de vous rencontrer.</p>
  </div>
);
```

Rien de spécial à propos de Foo ici.

La chose spéciale commence lorsque nous incluons ce composant dans notre fichier `src/index.js`.

Vous pourriez penser à quelque chose comme ceci :

```jsx
import Foo from './Foo';
class App extends React.Component {
   state = {};
   render() {
      return (
        <div>
          <p>Je suis App</p>
          <Foo />
        </div>
      )
   }
}
```

Eh bien non, pour une importation dynamique, nous devons faire ceci :

```javascript
import React from 'react';
import ReactDOM from 'react-dom';

import './myStyles.scss';

class App extends React.Component {
  state = {
    CaptainKirkBio: {},
    Foo: null, // Foo est notre composant
  };

  componentDidMount() {
    this.onGetKirkBio();
    import(/* webpackChunkName: 'Foo' */ './Foo').then(Foo => {
      this.setState({ Foo: Foo.default });
    });
  }

  onGetKirkBio = async () => {
    try {
      const result = await fetch('http://stapi.co/api/v1/rest/character/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: {
          title: 'James T. Kirk',
          name: 'James T. Kirk',
        },
      });
      const resultJSON = await result.json();
      const character = resultJSON.characters[0];
      this.setState({ CaptainKirkBio: character });
    } catch (error) {
      console.log('error', error);
    }
  };

  render() {
    const { CaptainKirkBio, Foo } = this.state;
    return (
      <div className="app">
        <img alt="header" src="/dist/images/header.jpg" className="app-header" />
        <p>
          Nous sommes une espèce des plus prometteuses, Monsieur Spock, en tant que prédateurs. Le saviez-vous ? J'ai fréquemment
          des doutes. Je n'en ai plus. Plus maintenant. Et peut-être dans mille ans ou plus, nous serons capables
          de le prouver.
        </p>
        <p>- Capitaine Kirk</p>
        <section>
          {Object.values(CaptainKirkBio).length === 0 ? (
            <p>Chargement des informations utilisateur</p>
          ) : (
            <p style={{ wordBreak: 'break-all' }}>{JSON.stringify(CaptainKirkBio)}</p>
          )}
        </section>
        {Foo ? <Foo /> : <p>Foo est en cours de chargement</p>}
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
```

Les choses à noter ici sont à la `ligne 9`, `ligne 14, 15, 16`, `ligne 40`, `ligne 57` :

* `Ligne 9` : Nous définissons `Foo` comme `null`
* `Ligne 14, 15, 16` : Dès que notre composant est monté, nous importons notre composant `<Foo` />

Parlons-en plus :

```javascript
import(/* webpackChunkName: 'Foo' */ './Foo').then(Foo => {     
   this.setState({Foo: Foo.default });    
})
```

Décomposons cela encore plus.

`import(/* webpackChunkName: Foo */ ./Foo)` : Cela a 2 parties, nous définissons un nom de chunk appelé `Foo` dans `/* webpackChunkName: Foo */`. Vous pouvez l'appeler comme vous voulez. Ce que cela fait, c'est que lorsque votre application charge le fichier `./Foo`, il sera chargé avec le nom de `Foo` comme défini dans `/* webpackChunkName: Foo */`

![Image](https://cdn-media-1.freecodecamp.org/images/1*DXWGMYT736qRci3pjmoz3A.png)
_`/* webpackChunkName: Foo */ Essayez de changer Foo en autre chose dans le commentaire /* */`_

Cette fonctionnalité est appelée commentaires magiques dans webpack, car elle vous permet de nommer le fichier lorsque vous le chargez dans votre code.

L'autre partie de `import(/* webpackChunkName: Foo */ ./Foo)` est le `./Foo` à la toute fin de l'instruction. C'est le chemin d'où nous incluons notre fichier.

Cela nous retourne une promesse `.then(Foo =>` {}). Puisque notre exportation de `<`Foo /`> était export default lorsque nous avons défini notre état de Foo, nous l'avons défini à this.setState({Foo: Foo.de`fault }); afin d'assigner le composant Foo à la variable d'état Foo.

`ligne 57` : C'est là où nous affichons notre composant `<Foo` />. À moins qu'il ne soit pas chargé, c'est-à-dire qu'il est null, nous affichons un message de chargement. Et une fois que nous avons le composant &`lt;Foo />, nous l'affichons.

Et cela, mes amis, est la division de code.

J'espère vraiment que cela vous a été utile. Si c'est le cas, faites-le moi savoir afin que je puisse écrire plus de choses comme celle-ci. Vous pouvez toujours me contacter sur [**Twitter**](https://twitter.com/adeelibr) et encore une fois, si vous avez suivi jusqu'à la fin, je suis vraiment fier de vous. VOUS ÊTES GÉNIAUX !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Blqgt4v2Nz8jUdg8O2RQTA.gif)

---

Cet article a été initialement publié dans la publication Freecodecamp précédemment sur Medium. [Lire ici](https://medium.com/free-code-camp/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff)
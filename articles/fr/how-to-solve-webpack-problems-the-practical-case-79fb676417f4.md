---
title: Comment j'ai résolu et débogué mon problème Webpack par essais, erreurs et
  un peu d'aide extérieure.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-02T09:34:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-webpack-problems-the-practical-case-79fb676417f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*foxbYY6DryL2han-19rLEA.jpeg
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
seo_title: Comment j'ai résolu et débogué mon problème Webpack par essais, erreurs
  et un peu d'aide extérieure.
seo_desc: 'By Margarita Obraztsova

  I would say that this was quite a journey. I knew that Webpack was not easy to configure:
  there are many parts with many options, there’s npm hell, and they change with new
  releases. No wonder it can easily become a troublesom...'
---

Par Margarita Obraztsova

Je dirais que ce fut un véritable parcours. Je savais que Webpack n'était pas facile à configurer : il y a de nombreuses parties avec de nombreuses options, il y a l'enfer npm, et elles changent avec les nouvelles versions. Pas étonnant que cela puisse facilement devenir **une tâche fastidieuse à déboguer lorsque quelque chose ne se passe pas comme prévu** (c'est-à-dire, pas comme dans la documentation).

### Essayer de déboguer

Mon parcours de débogage a commencé avec la configuration suivante :

_webpack.config.js_

```
// webpack v4.6.0
```

```
const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');const webpack = require('webpack');
```

```
module.exports = {  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[chunkhash].js'  },  devServer: {    contentBase: './dist',    hot: true,    open: true  },  module: {    rules: [      {         test: /\.js$/,        exclude: /node_modules/,        use: [          { loader: 'babel-loader' },          {            loader: 'eslint-loader',            options: {               formatter: require('eslint/lib/formatters/stylish')             }           }         ]       }     ]  },  plugins: [    new CleanWebpackPlugin('dist', {}),    new HtmlWebpackPlugin({      inject: false,      hash: true,      template: './src/index.html',      filename: 'index.html'    }),    new WebpackMd5Hash()  ]
```

```
};
```

_package.json_

```
{  "name": "post",  "version": "1.0.0",  "description": "",  "main": "index.js",  "scripts": {    "build": "webpack --mode production",    "dev": "webpack-dev-server"   },  "author": "",  "license": "ISC",  "devDependencies": {    "babel-cli": "^6.26.0",    "babel-core": "^6.26.0",    "babel-loader": "^7.1.4",    "babel-preset-env": "^1.6.1",    "babel-preset-react": "^6.24.1",    "babel-runtime": "^6.26.0",    "clean-webpack-plugin": "^0.1.19",    "eslint": "^4.19.1",    "eslint-config-prettier": "^2.9.0",    "eslint-loader": "^2.0.0",    "eslint-plugin-prettier": "^2.6.0",    "eslint-plugin-react": "^7.7.0",    "html-webpack-plugin": "^3.2.0",    "prettier": "^1.12.1",    "react": "^16.3.2",    "react-dom": "^16.3.2",    "webpack": "^4.6.0",    "webpack-cli": "^2.0.13",    "webpack-dev-server": "^3.1.3",    "webpack-md5-hash": "0.0.6"  }}
```

_.babelrc_

```
{  "presets": ["env", "react"]}
```

_.eslintrc.js_

```
module.exports = {  env: {    browser: true,    commonjs: true,    es6: true  },  extends: [    'eslint:recommended',    'plugin:react/recommended',    'prettier',    'plugin:prettier/recommended'  ],  parserOptions: {    ecmaFeatures: {      experimentalObjectRestSpread: true,      jsx: true    },    sourceType: 'module'  },  plugins: ['react', 'prettier'],  rules: {    indent: ['error', 2],    'linebreak-style': ['error', 'unix'],    quotes: ['warn', 'single'],    semi: ['error', 'always'],    'no-unused-vars': [      'warn',      { vars: 'all', args: 'none', ignoreRestSiblings: false }    ],    'prettier/prettier': 'error'   }};
```

_prettier.config.js_

```
// .prettierrc.js
```

```
module.exports = {  printWidth: 80,  tabWidth: 2,  semi: true,  singleQuote: true,  bracketSpacing: true};
```

Et dans le dossier _src/_ :

_index.html_

```
<html> <head></head> <body>    <div id="app"></div>    <script src="<%= htmlWebpackPlugin.files.chunks.main.entry %>"></script> </body></html>
```

_index.js_

```
import React from 'react';import { render } from 'react-dom';import Hello from './Hello';
```

```
class App extends React.Component {  render() {    return (      <div>        <Hello hello={'Hello, world! And the people of the world!'} />     </div>    );  }}render(<App />, document.getElementById('app'));
```

_Hello.js_

```
import React from 'react';import PropTypes from 'prop-types';
```

```
class Hello extends React.Component {  render() {    return <div>{this.props.hello}</div>;  }}
```

```
Hello.propTypes = {  hello: PropTypes.string};
```

```
export default Hello;
```

Voici la structure globale du projet :

![Image](https://cdn-media-1.freecodecamp.org/images/IA4bRe-OgTy6uExvsJwfk8WTW8uc-atToltw)

### Alors, quel était le problème ?

Comme vous pouvez le voir, j'ai configuré l'environnement, ESLint, et ainsi de suite. J'ai créé tout cela pour pouvoir commencer à coder et ajouter mes nouveaux composants à ma nouvelle bibliothèque de composants.

Mais que se passe-t-il si j'ai une erreur ? Allons-y, cassons quelque chose.

![Image](https://cdn-media-1.freecodecamp.org/images/5SfyW4tlIrnZSnRqM7h1z-5X4Kx218yWsVeN)

**Si nous essayons de retracer l'origine de l'erreur à partir de la console du navigateur Google Chrome, cela sera très difficile pour nous.** Nous tomberions sur quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/IAUMuN5vGBRK02XiutfpKGAV-qnuQlhqjVwx)

![Image](https://cdn-media-1.freecodecamp.org/images/PiUlbODsL34GCkasgETv-gePRv-KYohgEBsU)

Les source maps ne sont pas configurées !

Je veux qu'elle pointe vers un fichier **Hello.js** et non vers un fichier bundlé, un peu comme ce gars l'a fait [ici](http://erikaybar.name/webpack-source-maps-in-chrome/).

### C'est probablement une petite chose

Ou du moins, c'est ce que je pensais. J'ai donc essayé de configurer les source maps comme [décrit dans la documentation](https://webpack.js.org/guides/development/#using-webpack-dev-server) en ajoutant [**devtool**](https://webpack.js.org/configuration/devtool/).

> Lorsque webpack bundle votre code source, il peut devenir difficile de retracer les erreurs et les avertissements à leur emplacement d'origine. Par exemple, si vous bundlez trois fichiers source (`a.js`, `b.js`, et `c.js`) en un seul bundle (`bundle.js`) et que l'un des fichiers source contient une erreur, la trace de la pile pointera simplement vers `bundle.js`. Ce n'est pas toujours utile car vous voulez probablement savoir exactement quel fichier source a provoqué l'erreur.

> Afin de faciliter le suivi des erreurs et des avertissements, JavaScript offre des [source maps](http://blog.teamtreehouse.com/introduction-source-maps), qui mappent votre code compilé à votre code source d'origine. Si une erreur provient de `b.js`, la source map vous indiquera exactement cela. ([Source](https://webpack.js.org/guides/development/))

J'ai donc naïvement supposé que cela fonctionnerait dans mon _webpack.config.js_ :

```
...
```

```
module.exports = {  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[chunkhash].js'  },  devtool: 'inline-source-map',  devServer: {    contentBase: './dist',    hot: true,    open: true  },  ...
```

et _package.json_

```
..."scripts": {  "build": "webpack --mode production",  "dev": "webpack-dev-server --mode development"}...
```

Vous devez ajouter un flag de développement lorsque vous le faites, sinon cela ne fonctionnera pas comme le disent les docs. Pourtant, même avec la valeur suggérée, la source map n'a pas agi comme je le voulais.

![Image](https://cdn-media-1.freecodecamp.org/images/NN9n-KUqtxlW6sfANLqiIJHAB6Nka6XfiSkr)

Si vous lisez [ce guide](https://survivejs.com/webpack/building/source-maps/#-sourcemapdevtoolplugin-and-evalsourcemapdevtoolplugin-) de SurviveJS, que vous devriez faire, vous verrez.

Après avoir essayé toutes les options, j'ai eu recours à la chasse aux problèmes sur GitHub.

### Chasse aux problèmes sur GitHub

Essayer toutes les suggestions des problèmes GitHub ne m'a pas aidé.

À un moment donné, j'ai pensé qu'il y avait un problème avec webpack-dev-server. Et il s'est avéré que webpack-dev-server est en mode maintenance depuis quelques mois déjà.

![Image](https://cdn-media-1.freecodecamp.org/images/5bNNZcWIaA8PlUQgFKo9KprA3gkMyCY1i6Fx)

J'ai découvert cela après être tombé sur [ce problème](https://github.com/webpack/webpack-dev-server/issues/1161) où **ils recommandent d'utiliser webpack-serve au lieu de webpack-dev-server.**

Honêtement, c'était la première fois que j'entendais parler d'une alternative appelée **webpack-serve**. Les docs ne semblaient pas prometteuses non plus. Mais j'ai quand même décidé de lui donner une chance.

```
npm install webpack-serve --save-dev
```

J'ai créé _serve.config.js_

```
const serve = require('webpack-serve');
```

```
const config = require('./webpack.config.js');
```

```
serve({ config });
```

J'ai remplacé **webpack-dev-server par webpack serve** dans mon package.json.

Mais essayer webpack-serve n'a pas résolu le problème non plus.

Donc, à ce stade, j'ai eu l'impression d'avoir utilisé **toutes les suggestions que j'ai pu trouver sur GitHub** :

* [Webpack 4 — Sourcemaps](https://stackoverflow.com/questions/48986641/webpack-4-sourcemaps) : ce problème suggère que `devtool: 'source-map'` devrait fonctionner directement, mais ce n'était pas le cas pour moi
* [comment faire en sorte que webpack sourcemap pointe vers les fichiers originaux](https://stackoverflow.com/questions/34185748/how-to-make-webpack-sourcemap-to-original-files) : ajouter `devtoolModuleFilenameTemplate: info =>'file://' + path.resolve(info.absoluteResourcePath).replace(/\\/g, '`/') à ma configuration de sortie n'a pas beaucoup aidé. Mais au lieu de client.js, il m'a montré index.js.
* [https://github.com/webpack/webpack/issues/6400](https://github.com/webpack/webpack/issues/6400) : celui-ci n'est pas une description précise de mon problème, donc essayer les méthodes ici ne semblait pas m'aider
* J'ai essayé d'utiliser `webpack.SourceMapDevToolPlugin` mais cela n'a pas fonctionné avec ma configuration, même lorsque j'ai supprimé devtools ou les ai mis à false
* Je n'ai pas utilisé le plugin UglifyJS ici, donc configurer des options pour lui n'était pas une solution
* Je sais que webpack-dev-server est en maintenance maintenant, donc j'ai essayé webpack-serve, mais il semblait que les source maps ne fonctionnent pas avec lui non plus
* J'ai également essayé le package source-map-support, mais sans succès. J'ai une situation similaire à celle vue [ici](https://github.com/webpack/webpack/issues/3165).

### Le Saint StackOverflow

Cela m'a pris une éternité pour configurer les source maps, donc j'ai créé un [problème](https://stackoverflow.com/questions/50105741/webpack-4-devtool-option-does-not-work-with-webpack-dev-server) sur StackOverflow.

Le débogage de la configuration webpack est généralement une tâche fastidieuse : la meilleure façon de procéder est de créer une configuration à partir de zéro. Si quelque chose de la documentation ne fonctionne pas comme prévu, il peut être bon d'essayer de trouver un problème similaire sur une branche, ou de créer votre propre problème. Je le pensais, en tout cas.

Le premier gars qui a répondu à mon problème essayait vraiment de m'aider. Il a partagé sa propre configuration fonctionnelle. Il m'a même aidé en créant [une pull request](https://github.com/marharyta/webpack-fast-development/pull/1/files).

Le seul problème ici : **pourquoi sa configuration fonctionne-t-elle** ? Je veux dire, ce n'est probablement pas de la magie, et il y a une incompatibilité de module quelque part. Malheureusement, je n'ai pas pu comprendre pourquoi ma configuration ne fonctionnait pas :

![Image](https://cdn-media-1.freecodecamp.org/images/WqPfJ5e4-WAP3mCeLTFwwA2c-0qXMBAmzwKV)

Le problème est qu'il l'a fait avec les meilleures intentions en restructurant le projet à sa manière.

Cela signifiait que j'aurais une configuration supplémentaire dans le projet et que je devrais changer pas mal de choses. Cela aurait pu être acceptable si je faisais une configuration de test, mais **j'ai décidé d'apporter des changements progressifs aux fichiers pour voir où cela cassait.**

#### Dissection du problème

Alors, examinons les différences entre son Webpack et _package.json_ et les miens. Juste pour le dossier, j'ai utilisé un dépôt différent dans la question, donc voici mon [lien vers le dépôt](https://github.com/marharyta/webpack-fast-development) et ma configuration.

```
// webpack v4.6.0
```

```
const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');const stylish = require('eslint/lib/formatters/stylish');const webpack = require('webpack');
```

```
module.exports = {  entry: { main: './src/index.js' },  output: {   devtoolModuleFilenameTemplate: info => 'file://' + path.resolve(info.absoluteResourcePath).replace(/\\/g, '/'),
```

```
   path: path.resolve(__dirname, 'dist'),   filename: '[name].[hash].js'  },  mode: 'development',  devtool: 'eval-cheap-module-source-map',  devServer: {    contentBase: './dist',    hot: true  },  module: {    rules: [      {        test: /\.js$/,        exclude: /node_modules/,        loader: 'babel-loader'      },      {        test: /\.js$/,        exclude: /node_modules/,        loader: 'eslint-loader',        options: {          formatter: stylish         }       }     ]   },   plugins: [    // new webpack.SourceMapDevToolPlugin({    //   filename: '[file].map',    //   moduleFilenameTemplate: undefined,    //   fallbackModuleFilenameTemplate: undefined,    //   append: null,    //   module: true,    //   columns: true,    //   lineToLine: false,    //   noSources: false,    //   namespace: ''    // }),    new CleanWebpackPlugin('dist', {}),    new HtmlWebpackPlugin({      inject: false,      hash: true,      template: './src/index.html',      filename: 'index.html'    }),    new WebpackMd5Hash(),    // new webpack.NamedModulesPlugin(),    new webpack.HotModuleReplacementPlugin()  ]
```

```
};
```

_package.json_

```
{
```

```
"name": "post","version": "1.0.0","description": "","main": "index.js","scripts": {  "storybook": "start-storybook -p 9001 -c .storybook",  "dev": "webpack-dev-server --mode development --open",  "build": "webpack --mode production"},"author": "","license": "ISC","devDependencies": {  "@storybook/addon-actions": "^3.4.3",  "@storybook/react": "v4.0.0-alpha.4",  "babel-cli": "^6.26.0",  "babel-core": "^6.26.0",  "babel-loader": "^7.1.4",  "babel-preset-env": "^1.6.1",  "babel-preset-react": "^6.24.1",  "babel-runtime": "^6.26.0",  "clean-webpack-plugin": "^0.1.19",  "eslint": "^4.19.1",  "eslint-config-prettier": "^2.9.0",  "eslint-loader": "^2.0.0",  "eslint-plugin-prettier": "^2.6.0",  "eslint-plugin-react": "^7.7.0",  "html-webpack-plugin": "^3.2.0",  "prettier": "^1.12.1",  "react": "^16.3.2",  "react-dom": "^16.3.2",  "webpack": "v4.6.0",  "webpack-cli": "^2.0.13",  "webpack-dev-server": "v3.1.3",  "webpack-md5-hash": "0.0.6",  "webpack-serve": "^0.3.1"},"dependencies": {  "source-map-support": "^0.5.5"}
```

```
}
```

Je les ai laissés intacts exprès pour que vous puissiez voir mes tentatives de débogage. **Tout fonctionnait sauf les source maps**. Ci-dessous, je vais partager ce qu'il a changé dans ma configuration — mais il est bien sûr préférable de vérifier la pull request complète [ici](https://github.com/marharyta/webpack-fast-development/pull/1/files?diff=unified).

```
 // webpack v4.6.0 const path = require('path'); const HtmlWebpackPlugin = require('html-webpack-plugin'); // suppression de ce module de la config-const WebpackMd5Hash = require('webpack-md5-hash'); const CleanWebpackPlugin = require('clean-webpack-plugin'); const stylish = require('eslint/lib/formatters/stylish'); const webpack = require('webpack');  module.exports = {  // ajout du paramètre mode ici au lieu d'un flag+  mode: 'development',   entry: { main: './src/index.js' },   output: {  // suppression du chemin et du modèle de la sortie-    devtoolModuleFilenameTemplate: info =>-      'file://' + path.resolve(info.absoluteResourcePath).replace(/\\/g, '/'),-    path: path.resolve(__dirname, 'dist'),     filename: '[name].[hash].js'   },  // ajout de l'option resolve ici+  resolve: {+    extensions: ['.js', '.jsx']+  },   // changement de l'option devtool   devtool: 'eval-cheap-module-source-map',  // changement des paramètres devServer   devServer: {-    contentBase: './dist',-    hot: true+    hot: true,+    open: true   },   module: {     rules: [    // mise de mes deux vérifications en une (plus tard, il m'a demandé dans le chat de supprimer complètement l'option eslint)       {-        test: /\.js$/,-        exclude: /node_modules/,-        loader: 'babel-loader'-      },-      {-        test: /\.js$/,+        test: /\.jsx?$/,         exclude: /node_modules/,-        loader: 'eslint-loader',-        options: {-          formatter: stylish-        }+        use: [+          { loader: 'babel-loader' },+          { loader: 'eslint-loader', options: { formatter: stylish } }+        ]       }     ]   },   plugins: [    // nettoyage de certaines options-    new CleanWebpackPlugin('dist', {}),+    new CleanWebpackPlugin('dist'),    // suppression de certains paramètres de HtmlWebpackPlugin     new HtmlWebpackPlugin({-      inject: false,-      hash: true,-      template: './src/index.html',-      filename: 'index.html'+      template: './src/index.html'     }),  // suppression complète du plugin de hachage et ajout d'un plugin de remplacement de module à chaud
```

```
-    new WebpackMd5Hash(),-    new webpack.NamedModulesPlugin(),+    new webpack.HotModuleReplacementPlugin()   ] };
```

_package.json_

```
"main": "index.js",   "scripts": {     "storybook": "start-storybook -p 9001 -c .storybook",  // ajout de différents flags pour webpack-dev-server-    "dev": "webpack-dev-server --mode development --open",+    "dev": "webpack-dev-server --config ./webpack.config.js",     "build": "webpack --mode production"   },   "author": "",@@ -31,11 +31,6 @@     "react-dom": "^16.3.2",     "webpack": "v4.6.0",     "webpack-cli": "^2.0.13",-    "webpack-dev-server": "v3.1.3",-    "webpack-md5-hash": "0.0.6",-    "webpack-serve": "^0.3.1"-  },-  "dependencies": {// déplacement du serveur de développement vers les dépendances
```

```
-    "source-map-support": "^0.5.5"+    "webpack-dev-server": "v3.1.3"   } }
```

Comme vous pouvez le voir, il a supprimé un tas de modules et ajouté le mode à l'intérieur de la configuration. Et en regardant la pull request, vous pouvez voir qu'il a également ajouté un HMR spécifique à React.

Cela a aidé les source maps à fonctionner en sacrifiant beaucoup de plugins, mais il n'y avait pas d'explication concrète sur pourquoi il a fait ce qu'il a fait. En tant que personne qui lit les docs, ce n'était pas très satisfaisant pour moi.

Plus tard, j'ai pris mon webpack.config.js initial et j'ai commencé à ajouter les changements étape par étape pour voir quand les source maps ont finalement commencé à fonctionner.

**Changement 1 :**

```
-    new CleanWebpackPlugin('dist', {}),+    new CleanWebpackPlugin('dist'),
```

**Changement 2 :**

J'ai ajouté webpack-dev-server aux dépendances, pas aux devDependencies :

```
...
```

```
},
```

```
"dependencies": {
```

```
  "webpack-dev-server": "^3.1.3"
```

```
}
```

```
}
```

```
...
```

**Changement 3 :**

Ensuite, j'ai supprimé certains paramètres devServer :

```
devServer: {-    contentBase: './dist',+    hot: true,+    open: true   },
```

**Changement 4 :**

Supprimons stylish :

```
...
```

```
},
```

```
devtool: 'inline-source-map',  devServer: {    hot: true,    open: true  },
```

```
...
```

```
use: [  { loader: 'babel-loader' },  {    loader: 'eslint-loader'  }
```

```
]
```

```
....
```

**Changement 5 :**

Essayons de supprimer le plugin de hachage WebpackMd5Hash maintenant :

```
...
```

```
module.exports = {mode: 'development',entry: { main: './src/index.js' },output: {  path: path.resolve(__dirname, 'dist'),  filename: '[name].js'  },devtool: 'inline-source-map',...
```

```
plugins: [  new CleanWebpackPlugin('dist'),  new HtmlWebpackPlugin({    inject: false,    hash: true,    template: './src/index.html',    filename: 'index.html'  })-    new WebpackMd5Hash(), ]
```

```
};
```

**Changement 6 :**

Maintenant, essayons de supprimer certains paramètres de HtmlWebpackPlugin :

```
...
```

```
plugins: [  new CleanWebpackPlugin('dist'),  new HtmlWebpackPlugin({    template: './src/index.html'  })]};
```

```
...
```

**Changement 7 :**

Comme nous pouvons le voir dans son code, il a ajouté certaines options de résolution ici. Personnellement, je ne comprends pas pourquoi nous en avons besoin ici. Et je n'ai pas pu trouver l'information dans les docs non plus.

```
...
```

```
resolve: {  extensions: ['.js', '.jsx']},module: {
```

```
...
```

**Changement 8 :**

Suppression du chemin de sortie :

```
...
```

```
entry: { main: './src/index.js' },output: {  filename: '[name].js'},devtool: 'inline-source-map',
```

```
...
```

**Changement 9 :**

Ajout du plugin de remplacement de module à chaud :

```
...
```

```
const HtmlWebpackPlugin = require('html-webpack-plugin');const CleanWebpackPlugin = require('clean-webpack-plugin');const webpack = require('webpack');
```

```
...
```

```
plugins: [  new CleanWebpackPlugin('dist'),  new HtmlWebpackPlugin({    template: './src/index.html'  }),  new webpack.HotModuleReplacementPlugin()]};
```

```
...
```

**Changement 10 :**

Ajout de — config dans package.json :

```
-    "dev": "webpack-dev-server --mode development --open",+    "dev": "webpack-dev-server --config ./webpack.config.js",
```

**Clarifions une chose : à ce stade, j'avais presque réécrit la configuration.**

C'est un problème majeur, car nous ne pouvons pas simplement la réécrire chaque fois que quelque chose ne fonctionne pas !

### Create-react-app est la meilleure source pour apprendre sur webpack

En dernier recours, je suis allé vérifier comment create-react-app implémente le source mapping. C'était la bonne décision après tout. Voici la configuration de la [version dev de webpack](https://github.com/facebook/create-react-app/blob/next/packages/react-scripts/config/webpack.config.dev.js).

Si nous vérifions comment **devtool** est implémenté là-bas, nous verrons :

> // Vous préférerez peut-être 'eval' si vous souhaitez voir la sortie compilée dans DevTools.

> // Voir la discussion dans [https://github.com/facebook/create-react-app/issues/343.](https://github.com/facebook/create-react-app/issues/343.)

> devtool: 'cheap-module-source-map'

Donc ce problème m'a dirigé vers un autre problème, trouvé [ici](https://github.com/facebook/create-react-app/issues/343).

```
// webpack v4
```

```
const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');
```

```
module.exports = {
```

```
mode: "development",entry: { main: './src/index.js' },output: {  path: path.resolve(__dirname, 'dist'),  filename: '[name].[hash].js'},devtool: 'cheap-module-source-map',devServer: {  contentBase: './dist',  hot: true,  open: true},module: {
```

Changer les lignes n'a toujours pas fonctionné — pas encore ! J'ai appris que la source map est un problème de longue date.

### **Demander aux bonnes personnes**

Chaque projet open source a des mainteneurs. Donc, dans ce cas, c'était définitivement le bon mouvement de demander directement aux gars.

Bien que la méthode d'essais et d'erreurs de Daniel n'ait pas vraiment fonctionné pour moi, j'ai été agréablement surpris par la mobilité de l'équipe de mainteneurs.

![Image](https://cdn-media-1.freecodecamp.org/images/dcdxfW7u7weQbhJK1zspAgQblsQxbH9ObSzj)

![Image](https://cdn-media-1.freecodecamp.org/images/GP1mi8Ahmtigeeq-bzIxmVzcbs6LDUsf66zP)

J'ai donc créé un dépôt avec la configuration que vous pouvez voir [ici](https://github.com/marharyta/webpack-4.6.0-test). Consultez le deuxième commit.

Pour vous faciliter la tâche, voici mon fichier webpack.js où j'ai restauré ma configuration initiale, plus propre :

```
// webpack v4
```

```
const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');
```

```
module.exports = {  mode: 'development',  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[hash].js'  },  devtool: 'inline-source-map',  devServer: {    contentBase: './dist',    hot: true,    open: true  },  module: {    rules: [      {        test: /\.js$/,        exclude: /node_modules/,        use: [          { loader: 'babel-loader' },          {            loader: 'eslint-loader',            options: {               formatter: require('eslint/lib/formatters/stylish')             }          }         ]        }      ]  },  plugins: [    new CleanWebpackPlugin('dist'),    new HtmlWebpackPlugin({      inject: false,      hash: true,      template: './src/index.html',      filename: 'index.html'    }),    new WebpackMd5Hash()  ]};
```

Après avoir vérifié mon code, le mainteneur a créé un [problème](https://github.com/marharyta/webpack-4.6.0-test/issues/1).

Récapitulons ce qu'il a inclus là-bas :

> Définir l'option `mode`

> Le premier problème que j'ai trouvé est la façon dont l'option `mode` était définie. Dans les scripts npm, le mode était défini comme :

> **webpack --mode production**

> La bonne façon serait :

> **webpack --mode=production**

> L'état final des scripts npm ressemble à ceci pour moi :

> **"scripts": {**  
>  **"build": "webpack --mode=production",**  
>  **"start": "webpack-dev-server --mode=development --hot"**  
> **}**

> J'ai également changé `dev` en `start` car c'est plus standard et attendu par les autres développeurs comme commande. Vous pouvez en fait faire `npm start`, sans la commande `run` ?

```
...
```

```
"scripts": {  "build": "webpack --mode production",  "dev": "webpack-dev-server --mode=development --hot"},
```

```
...
```

Ensuite, il a suggéré ce qui suit :

> devtool pour les source maps

> Je recommande toujours l'option `inline-source-map`, c'est la plus simple et elle est incluse dans le bundle lui-même sous forme de commentaire à la fin.

> **module.exports = {**  
> **+ devtool: 'inline-source-map',**  
>  **// reste de votre config**  
> **}**

> Je recommande également de créer un objet séparé et de le remplir uniquement en développement :

> commande

> **webpack-dev-server --mode=development NODE_ENV=development**

> webpack.config.js

> **const webpackConfig = {}**

> **if (process.env.NODE_ENV === 'development') {**  
>  **webpackConfig.devtool = 'inline-source-map'**  
> **}**

> De cette façon, vous vous assurez que le bundle en production n'est pas affecté par cela.

Ensuite, il a suggéré de supprimer ESLint des loaders :

> Linting et expérience développeur

> **Honêtement, je supprimerais `eslint` en tant que loader, c'est super spammy et cela perturbe le flux de développement. Je préfère ajouter un precommit githook pour vérifier cela.**

> C'est super facile en ajoutant un script comme ceci :

> **"scripts": {**  
> **+ "lint": "eslint ./src/**/*.js"**  
>  **"build": "webpack --mode=production",**  
>  **"start": "webpack-dev-server --mode=development --hot"**  
> **}**

> Et puis en le combinant avec husky.

et en l'ajoutant aux scripts :

```
...
```

```
"scripts": {
```

```
"lint": "eslint ./src/**/*.js",
```

```
"build": "webpack --mode production",
```

```
"dev": "webpack-dev-server --mode=development --hot"
```

```
},
```

```
...
```

J'ai fait une erreur dans src/_Hello.js_ **exprès** pour voir comment les source maps fonctionnaient cette fois-ci.

```
import React from 'react';import PropTypes from 'prop-types';
```

```
class Hello extends React.Component {  console.log(hello.world);  render() {    return <div>{this.props.hello}</div>;  }}Hello.propTypes = {  hello: PropTypes.string};export default Hello;
```

### Comment j'ai résolu le problème

Le problème était ESLint. Mais après avoir spécifié les modes correctement et supprimé l'eslint-loader, les source maps fonctionnaient bien !

En suivant l'exemple que le mainteneur m'a donné, j'ai mis à jour mon Webpack vers :

```
// webpack v4
```

```
const path = require('path');const HtmlWebpackPlugin = require('html-webpack-plugin');const WebpackMd5Hash = require('webpack-md5-hash');const CleanWebpackPlugin = require('clean-webpack-plugin');module.exports = {  entry: { main: './src/index.js' },  output: {    path: path.resolve(__dirname, 'dist'),    filename: '[name].[hash].js'  },  devtool: 'inline-source-map',  devServer: {    contentBase: './dist',    hot: true,    open: true  },  module: {    rules: [     {      test: /\.js$/,      exclude: /node_modules/,      use: [{ loader: 'babel-loader' }]     }    ]  },  plugins: [    new CleanWebpackPlugin('dist'),    new HtmlWebpackPlugin({      inject: false,      hash: true,      template: './src/index.html',      filename: 'index.html'    }),    new WebpackMd5Hash()  ]};
```

et mon package JSON vers :

```
{
```

```
"name": "post","version": "1.0.0","description": "","main": "index.js","scripts": {  "build": "webpack --mode=production",  "start": "NODE_ENV=development webpack-dev-server --mode=development --hot"},"author": "","license": "ISC","devDependencies": {  "babel-cli": "^6.26.0",  "babel-core": "^6.26.0",  "babel-loader": "^7.1.4",  "babel-preset-env": "^1.6.1",  "babel-preset-react": "^6.24.1",  "babel-runtime": "^6.26.0",  "clean-webpack-plugin": "^0.1.19",  "eslint": "^4.19.1",  "eslint-config-prettier": "^2.9.0",  "eslint-loader": "^2.0.0",  "eslint-plugin-prettier": "^2.6.0",  "eslint-plugin-react": "^7.7.0",  "html-webpack-plugin": "^3.2.0",  "prettier": "^1.12.1",  "react": "^16.3.2",  "react-dom": "^16.3.2",  "webpack": "^4.6.0",  "webpack-cli": "^2.0.13",  "webpack-md5-hash": "0.0.6"},"dependencies": {  "webpack-dev-server": "^3.1.3"}
```

```
}
```

**Enfin, les source maps fonctionnent !**

![Image](https://cdn-media-1.freecodecamp.org/images/XVzSiRqwXEr337uejbZq3-O2XJ5QsdmDOlrv)

![Image](https://cdn-media-1.freecodecamp.org/images/1TSTZwHiJF7pv36uyNBtEi2wbLNx-qLJLJ3K)

### **Conclusions :**

Les source maps ont fait l'objet de multiples discussions et bugs depuis 2016, comme vous pouvez le voir [ici](https://github.com/webpack/webpack/issues/3165).

**Webpack a besoin d'aide pour l'audit !**

Après avoir trouvé ce bug, j'ai soumis un [problème](https://github.com/webpack-contrib/eslint-loader/issues/227) au package eslint-loader.

En ce qui concerne la vérification de la qualité des source maps, nous pouvons utiliser [cet outil](http://sokra.github.io/source-map-visualization/).

### Que pouvez-vous faire si vous avez un problème avec webpack ?

Au cas où vous tomberiez sur un problème avec Webpack, ne paniquez pas ! Suivez ces étapes :

* Recherchez dans les problèmes GitHub similaires au vôtre.
* Essayez de vérifier les boilerplates et voyez comment la fonctionnalité est implémentée là-bas, comme create-react-app par exemple.
* Posez des questions sur StackOverflow — n'ayez pas peur ! Assurez-vous simplement d'avoir épuisé toutes les façons de résoudre votre problème par vous-même.
* N'hésitez pas à tweeter à ce sujet et à demander directement aux mainteneurs.
* Créez des problèmes une fois que vous les trouvez. Cela aidera beaucoup les contributeurs !

Dans cet article, je vous ai fourni mon fichier de configuration et le processus que j'ai utilisé pour le configurer étape par étape.

Note : comme beaucoup de dépendances npm peuvent changer d'ici à ce que vous lisiez ceci, la même configuration peut ne pas fonctionner pour vous ! Je vous demande gentiment de laisser vos erreurs dans les commentaires ci-dessous afin que je puisse les éditer plus tard.

**S'il vous plaît, abonnez-vous et applaudissez pour cet article ! Merci !**
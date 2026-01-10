---
title: 'Comment utiliser Webpack avec React : un tutoriel approfondi'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T22:54:32.000Z'
originalURL: https://freecodecamp.org/news/learn-webpack-for-react-a36d4cac5060
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6PbJ291MHulQWCmPW9fzDg.jpeg
tags:
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: webpack
  slug: webpack
seo_title: 'Comment utiliser Webpack avec React : un tutoriel approfondi'
seo_desc: 'By Esau Silva

  Updated to Babel 7

  In this tutorial we will see the basics of Webpack for React to get you started,
  including React Router, Hot Module Replacement (HMR), Code Splitting by Route and
  Vendor, production configuration and more.

  Before we s...'
---

Par Esau Silva

_Mis à jour pour Babel 7_

Dans ce tutoriel, nous verrons les bases de Webpack pour React afin de vous aider à démarrer, y compris [React Router](https://github.com/ReactTraining/react-router), [Hot Module Replacement](https://github.com/gaearon/react-hot-loader) (HMR), le fractionnement de code par [Route](https://github.com/theKashey/react-imported-component) et [Vendor](https://webpack.js.org/plugins/commons-chunk-plugin/), la configuration de production et bien plus encore.

Avant de commencer, voici la liste complète des fonctionnalités que nous allons configurer ensemble dans ce tutoriel :

* React 16
* React Router 5
* Semantic UI comme Framework CSS
* Hot Module Replacement (HMR)
* CSS Autoprefixer
* CSS Modules
* @babel/plugin-proposal-class-properties
* @babel/plugin-syntax-dynamic-import
* Webpack 4
* Fractionnement de code par Route et Vendor
* Webpack Bundle Analyzer

#### Prérequis

Avoir les éléments suivants préinstallés :

* [Yarn](https://yarnpkg.com/) — Gestionnaire de paquets, similaire à [npm](https://www.npmjs.com/)
* [Node](https://nodejs.org/en/)

Et vous devriez avoir au moins quelques connaissances de base de React et React Router.

**_Note:_** _Vous pouvez utiliser npm si vous le souhaitez, bien que les commandes varieront légèrement._

#### Dépendances initiales

Commençons par créer notre répertoire et `package.json`.

Dans votre terminal, tapez ce qui suit :

```
mkdir webpack-for-react && cd $_
yarn init -y
```

Cette première commande créera notre répertoire et s'y déplacera, puis initialisera un `package.json` en acceptant les valeurs par défaut.   
Si vous l'inspectez, vous verrez la configuration de base :

```js
{
  "name": "webpack-for-react",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT"
}
```

Maintenant, nous installons nos dépendances initiales (production) et les dépendances de développement.   
Dans votre terminal, tapez ce qui suit :

```
yarn add react react-dom prop-types react-router-dom semantic-ui-react
yarn add @babel/core babel-loader @babel/preset-env @babel/preset-react @babel/plugin-proposal-class-properties @babel/plugin-syntax-dynamic-import css-loader style-loader html-webpack-plugin webpack webpack-dev-server webpack-cli -D
```

Les dépendances de développement ne seront utilisées, comme leur nom l'indique, que pendant la phase de développement, et les dépendances (production) sont ce dont notre application a besoin en production.

```js
{
  "name": "webpack-for-react",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "dependencies": {
    "react": "^16.2.0",
    "react-dom": "^16.2.0",
    "prop-types": "^15.6.2",
    "react-router-dom": "^4.2.2",
    "semantic-ui-react": "^0.77.1"
  },
  "devDependencies": {
    "@babel/core": "^7.0.0",
    "@babel/plugin-proposal-class-properties": "^7.0.0",
    "@babel/plugin-syntax-dynamic-import": "^7.0.0",
    "@babel/preset-env": "^7.0.0",
    "@babel/preset-react": "^7.0.0", 
    "babel-loader": "^8.0.1",
    "css-loader": "^0.28.10",
    "html-webpack-plugin": "^3.0.4",
    "style-loader": "^0.19.1",
    "webpack": "^4.0.0",
    "webpack-cli": "^2.0.14",
    "webpack-dev-server": "^3.0.0"
  }
}
```

**_Note:_** _Les modifications apportées aux fichiers précédemment créés seront en gras._  
**_Note:_** _Les versions des dépendances peuvent être différentes des vôtres au moment de la rédaction de ce document._

* [react](https://reactjs.org/) — Je suis sûr que vous savez ce qu'est React
* [react-dom](https://reactjs.org/docs/react-dom.html) — Fournit des méthodes spécifiques au DOM pour le navigateur
* [prop-types](https://github.com/facebook/prop-types) — Vérification des types de props React à l'exécution
* [react-router-dom](https://github.com/ReactTraining/react-router) — Fournit des capacités de routage à React pour le navigateur
* [semantic-ui-react](https://react.semantic-ui.com/introduction) — Framework CSS
* [@babel/core](https://babeljs.io/docs/en/babel-core/) — Dépendances principales pour Babel
* [Babel](https://babeljs.io/) est un transpileur qui compile JavaScript ES6 en JavaScript ES5, vous permettant d'écrire du JavaScript « du futur » afin que les navigateurs actuels le comprennent. [Description détaillée sur Quora](https://www.quora.com/What-exactly-is-BabelJs-Why-does-it-understand-JSX-React-components).
* [babel-loader](https://webpack.js.org/loaders/babel-loader/) — Ce package permet de transpiler des fichiers JavaScript en utilisant Babel et webpack
* [@babel/preset-env](https://babeljs.io/docs/en/next/babel-preset-env.html) — Avec cela, vous n'avez pas à spécifier si vous allez écrire en ES2015, ES2016 ou ES2017. Babel détectera et transpilera automatiquement en conséquence.
* [@babel/preset-react](https://babeljs.io/docs/en/babel-preset-react/) — Indique à Babel que nous allons utiliser React
* [@babel/plugin-proposal-class-properties](https://babeljs.io/docs/en/babel-plugin-proposal-class-properties) — Utilise les propriétés de classe. Nous n'utilisons pas les propriétés de classe dans ce projet, mais vous les utiliserez très probablement dans votre projet
* [@babel/plugin-syntax-dynamic-import](https://babeljs.io/docs/en/babel-plugin-syntax-dynamic-import) — Permet d'utiliser les imports dynamiques
* [css-loader](https://webpack.js.org/loaders/css-loader/) — Interprète `@import` et `url()` comme `import/require()` et les résoudra
* [html-webpack-plugin](https://webpack.js.org/plugins/html-webpack-plugin/) — Peut générer un fichier HTML pour votre application, ou vous pouvez fournir un modèle
* [style-loader](https://webpack.js.org/loaders/style-loader/) — Ajoute du CSS au DOM en injectant une balise `<style>`
* [webpack](https://webpack.js.org/) — Bundler de modules
* [webpack-cli](https://github.com/webpack/webpack-cli) — Interface en ligne de commande, nécessaire pour Webpack 4.0.1 et versions ultérieures
* [webpack-dev-server](https://webpack.js.org/configuration/dev-server/) — Fournit un serveur de développement pour votre application

### Configuration de Babel

Dans le répertoire racine (`webpack-for-react`), nous créons le fichier de configuration Babel.

```
touch .babelrc
```

À ce stade, vous pouvez ouvrir votre éditeur préféré (le mien est VS Code, soit dit en passant), puis pointer l'éditeur vers la racine de ce projet et ouvrir le fichier `.babelrc` et copier ce qui suit :

```js
{
  "presets": ["@babel/preset-env", "@babel/preset-react"],
  "plugins": [
    "@babel/plugin-syntax-dynamic-import",
    "@babel/plugin-proposal-class-properties"
  ]
}
```

Cela indique à Babel d'utiliser les presets (plugins) que nous avons précédemment installés. Plus tard, lorsque nous appellerons `babel-loader` depuis Webpack, c'est ici qu'il regardera pour savoir quoi faire.

### Configuration de Webpack

Maintenant, le plaisir commence ! Créons le fichier de configuration Webpack.

Dans votre terminal, tapez ce qui suit :

```
touch webpack.config.js
```

Ouvrez `webpack.config.js` et copiez ce qui suit :

```js
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const port = process.env.PORT || 3000;

module.exports = {
  // La configuration Webpack va ici
};
```

C'est la structure de base pour Webpack. Nous avons besoin de `webpack` et `html-webpack-plugin`. Nous fournissons un port par défaut si la variable d'environnement PORT n'existe pas et exportons le module.

Les éléments suivants seront des ajouts pour `webpack.config.js` (l'un après l'autre).

```js
...
module.exports = {
  mode: 'development',
};
```

`mode` indique à Webpack que cette configuration sera pour soit `development` soit `production`. « Le mode développement [est] optimisé pour la vitesse et l'expérience du développeur... Les valeurs par défaut de production vous donneront un ensemble de valeurs par défaut utiles pour déployer votre application ([webpack 4 : mode et optimisation](https://medium.com/webpack/webpack-4-mode-and-optimization-5423a6bc597a)). »

```js
...
module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.[hash].js'
  },
};
```

Pour obtenir une instance fonctionnelle de Webpack, nous avons besoin de :

* `entry` — Spécifie le point d'entrée de votre application ; c'est là que vit votre application React et où le processus de bundling commencera ([Docs](https://webpack.js.org/concepts/entry-points/))

_Webpack 4 a introduit quelques valeurs par défaut, donc si vous n'incluez pas `entry` dans votre configuration, Webpack supposera que votre point d'entrée se trouve sous le répertoire `./src`, rendant `entry` optionnel contrairement à Webpack 3. Pour ce tutoriel, j'ai décidé de laisser `entry` car cela rend évident où se trouvera notre point d'entrée, mais vous êtes libre de le supprimer si vous le souhaitez._

* `output` — Indique à Webpack comment écrire les fichiers compilés sur le disque ([Docs](https://webpack.js.org/concepts/output/))
* `filename` — Ce sera le nom de fichier de l'application bundlée. La partie `[hash]` du nom de fichier sera remplacée par un hash généré par Webpack chaque fois que votre application change et est recompilée (aide avec la mise en cache).

```js
...
module.exports = {
  ...
  devtool: 'inline-source-map',
};
```

`devtool` créera des [source maps](https://developer.mozilla.org/fr/docs/Tools/Debugger/How_to/Use_a_source_map) pour vous aider à déboguer votre application. Il existe plusieurs types de source maps et cette carte particulière (`inline-source-map`) ne doit être utilisée qu'en développement. (Voir la [documentation](https://webpack.js.org/configuration/devtool/) pour plus d'options).

```js
...
module.exports = {
  ...
  module: {
    rules: [

      // Première règle
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },

      // Deuxième règle
      {
        test: /\.css$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader',
            options: {
              modules: true,
              localsConvention: 'camelCase',
              sourceMap: true
            }
          }
        ]
      }
    ]
  },
};
```

* [module](https://webpack.js.org/configuration/module/) — Quels types de modules votre application inclura, dans notre cas, nous supporterons ESNext (Babel) et CSS Modules
* [rules](https://webpack.js.org/configuration/module/#module-rules) — Comment nous gérons chaque type de module différent

#### **Première règle**

Nous testons les fichiers avec une extension `.js` en excluant le répertoire `node_modules` et utilisons Babel, via `babel-loader`, pour transpiler en JavaScript vanilla (basiquement, en cherchant nos fichiers React).

Vous vous souvenez de notre configuration dans `.babelrc` ? C'est ici que Babel regarde ce fichier.

#### **Deuxième règle**

Nous testons les fichiers CSS avec une extension `.css`. Ici, nous utilisons deux loaders, `style-loader` et `css-loader`, pour gérer nos fichiers CSS. Ensuite, nous instruisons `css-loader` d'utiliser les _CSS Modules_, le camel case et de créer des source maps.

**CSS Modules et Camel Case**

Cela nous donne la possibilité d'utiliser la syntaxe `import Styles from './styles.css'` (ou la déstructuration comme ceci `import { style1, style2 } from './styles.css'`).

Ensuite, nous pouvons l'utiliser comme ceci dans une application React :

```js
...
<div className={Style.style1}>Hello World</div>
// ou avec la syntaxe de déstructuration
<div className={style1}>Hello World</div>
...
```

Le camel case nous donne la possibilité d'écrire nos règles CSS comme ceci :

```
.home-button {...}
```

Et de l'utiliser dans nos fichiers React comme ceci :

```
...
import { homeButton } from './styles.css'
...
...
module.exports = {
  ...
  plugins: [
    new HtmlWebpackPlugin({
      template: 'public/index.html',
      favicon: 'public/favicon.ico'
    })
  ],
};
```

Cette section est l'endroit où nous configurons (comme le nom l'indique) les plugins.

`html-webpack-plugin` accepte un objet avec différentes options. Dans notre cas, nous spécifions le modèle HTML que nous allons utiliser et le favicon. (Voir la [documentation](https://github.com/jantimon/html-webpack-plugin#configuration) pour plus d'options).

Plus tard, nous ajouterons d'autres plugins pour Bundle Analyzer et HMR.

```
...
module.exports = {
  ...
  devServer: {
    host: 'localhost',
    port: port,
    historyApiFallback: true,
    open: true
  }
};
```

Enfin, nous configurons le serveur de développement. Nous spécifions `localhost` comme hôte et attribuons la variable `port` comme port (si vous vous souvenez, nous avons attribué le port 3000 à cette variable). Nous définissons `historyApiFallback` sur true et `open` sur true. Cela ouvrira automatiquement le navigateur et lancera votre application sur [http://localhost:3000](http://localhost:3000). ([Docs](https://webpack.js.org/configuration/dev-server/))

Voici la configuration complète de Webpack. (`webpack.config.js`) :

```
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const port = process.env.PORT || 3000;

module.exports = {
  mode: 'development',  
  entry: './src/index.js',
  output: {
    filename: 'bundle.[hash].js'
  },
  devtool: 'inline-source-map',
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.css$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader',
            options: {
              modules: true,
              localsConvention: 'camelCase',
              sourceMap: true
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: 'public/index.html',
      favicon: 'public/favicon.ico'
    })
  ],
  devServer: {
    host: 'localhost',
    port: port,
    historyApiFallback: true,
    open: true
  }
};
```

### Création de l'application React

Nous allons créer une simple application Hello World avec trois routes : une _accueil_, une _page non trouvée_ et une _page dynamique_ que nous chargerons de manière asynchrone lorsque nous implémenterons le fractionnement de code plus tard.

**_Note:_** _En supposant que vous avez une compréhension de base de React et React Router, je ne vais pas entrer dans les détails et ne mettrai en évidence que ce qui est pertinent pour ce tutoriel._

Nous avons actuellement la structure de projet suivante :

```
|-- node_modules
|-- .babelrc
|-- package.json
|-- webpack.config.js
|-- yarn.lock
```

Dans votre terminal, tapez ce qui suit :

```
mkdir public && cd $_
touch index.html
```

Nous créons un répertoire `public`, nous y déplaçons et créons également un fichier `index.html`. C'est aussi ici que nous avons le `favicon`. Vous pouvez le récupérer [ici](https://github.com/esausilva/react-starter-boilerplate-hmr/blob/master/public/favicon.ico) et le copier dans le répertoire public.

Ouvrez le fichier `index.html` et copiez ce qui suit :

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.13/semantic.min.css"></link>
  <title>webpack-for-react</title>
</head>

<body>
  <div id="root"></div>
</body>

</html>
```

Rien de bien compliqué ici (juste un modèle HTML standard), nous ajoutons simplement la feuille de style Semantic UI et créons également une `div` avec un ID `root`. C'est ici que notre application React sera rendue.

Retournez à votre terminal et tapez ce qui suit :

```
cd ..
mkdir src && cd $_
touch index.js
```

Ouvrez `index.js` et copiez ce qui suit :

```
import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';

ReactDOM.render(<App />, document.getElementById('root'));
```

Dans votre terminal, tapez ce qui suit :

```
mkdir components && cd $_
touch App.js Layout.js Layout.css Home.js DynamicPage.js NoMatch.js

```

Après avoir créé les fichiers de composants React, nous avons la structure de projet suivante :

```
|-- node_modules
|-- public
    |-- index.html
    |-- favicon.ico
|-- src
    |-- components
        |-- App.js
        |-- DynamicPage.js
        |-- Home.js
        |-- Layout.css
        |-- Layout.js
        |-- NoMatch.js
    |-- index.js
|-- .babelrc
|-- package.json
|-- webpack.config.js
|-- yarn.lock
```

Ouvrez `App.js` et copiez ce qui suit :

```js
import React from 'react';
import { Switch, BrowserRouter as Router, Route } from 'react-router-dom';

import Home from './Home';
import DynamicPage from './DynamicPage';
import NoMatch from './NoMatch';

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/dynamic" component={DynamicPage} />
          <Route component={NoMatch} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
```

Nous créons notre « coquille » de base avec React Router et avons une route _accueil_, _page dynamique_ et _page non trouvée_.

Ouvrez `Layout.css` et copiez ce qui suit :

```
.pull-right {
  display: flex;
  justify-content: flex-end;
}

.h1 {
  margin-top: 10px !important;
  margin-bottom: 20px !important;
}
```

Ouvrez `Layout.js` et copiez ce qui suit :

```js
import React from 'react';
import { Link } from 'react-router-dom';
import { Header, Container, Divider, Icon } from 'semantic-ui-react';

import { pullRight, h1 } from './layout.css';

const Layout = ({ children }) => {
  return (
    <Container>
      <Link to="/">
        <Header as="h1" className={h1}>
          webpack-for-react
        </Header>
      </Link>
      {children}
      <Divider />
      <p className={pullRight}>
        Made with <Icon name="heart" color="red" /> by Esau Silva
      </p>
    </Container>
  );
};

export default Layout;
```

C'est notre composant conteneur où nous définissons la mise en page du site. En utilisant les CSS Modules, nous importons deux règles CSS depuis `layout.css`. Remarquez également comment nous utilisons le _camel case_ pour `pullRight`.

Ouvrez `Home.js` et copiez ce qui suit :

```js
import React from 'react';
import { Link } from 'react-router-dom';

import Layout from './Layout';

const Home = () => {
  return (
    <Layout>
      <p>Hello World of React and Webpack!</p>
      <p>
        <Link to="/dynamic">Navigate to Dynamic Page</Link>
      </p>
    </Layout>
  );
};

export default Home;
```

Ouvrez `DynamicPage.js` et copiez ce qui suit :

```js
import React from 'react';
import { Header } from 'semantic-ui-react';

import Layout from './Layout';

const DynamicPage = () => {
  return (
    <Layout>
      <Header as="h2">Dynamic Page</Header>
      <p>This page was loaded asynchronously!!!</p>
    </Layout>
  );
};

export default DynamicPage;
```

Ouvrez `NoMatch.js` et copiez ce qui suit :

```js
import React from 'react';
import { Icon, Header } from 'semantic-ui-react';

import Layout from './Layout';

const NoMatch = () => {
  return (
    <Layout>
      <Icon name="minus circle" size="big" />
      <strong>Page not found!</strong>
    </Layout>
  );
};

export default NoMatch;
```

Nous avons terminé la création des composants React. Pour une dernière étape avant d'exécuter notre application, ouvrez `package.json` et ajoutez les lignes en gras :

```js
{
  "name": "webpack-for-react",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "scripts": {
    "start": "webpack-dev-server"
  },
  "dependencies": {
    "react": "^16.2.0",
    "react-dom": "^16.2.0",
    "prop-types": "^0.4.0",
    "react-router-dom": "^4.2.2",
    "semantic-ui-react": "^0.77.1"
  },
  "devDependencies": {
    "@babel/core": "^7.0.0",
    "@babel/plugin-proposal-class-properties": "^7.0.0",
    "@babel/plugin-syntax-dynamic-import": "^7.0.0",
    "@babel/preset-env": "^7.0.0",
    "@babel/preset-react": "^7.0.0",
    "babel-loader": "^8.0.1",
    "css-loader": "^0.28.10",
    "html-webpack-plugin": "^3.0.4",
    "style-loader": "^0.19.1",
    "webpack": "^4.0.0",
    "webpack-cli": "^2.0.14",
    "webpack-dev-server": "^3.0.0"
  }
}
```

Nous ajoutons la clé `scripts` ainsi que la clé `start`. Cela nous permettra d'exécuter React avec le serveur de développement Webpack. Si vous ne spécifiez pas de fichier de configuration, `webpack-dev-server` recherchera le fichier `webpack.config.js` comme entrée de configuration par défaut dans le répertoire racine.

Maintenant, le moment de vérité ! Tapez ce qui suit dans votre terminal (n'oubliez pas d'être dans le répertoire racine) et Yarn appellera notre script `start`.

```
yarn start
```

![Image](https://cdn-media-1.freecodecamp.org/images/iHJNOlQ4O11i7ONPbmXDRkbKF7WAGqZRFcCY)
_Exécution de React_

Nous avons maintenant une application React fonctionnelle alimentée par notre propre configuration Webpack. Remarquez à la fin du GIF que je mets en évidence le fichier JavaScript bundlé généré par Webpack pour nous, et comme nous l'avons indiqué dans la configuration, le nom du fichier a un hash unique, `bundle.d505bbab002262a9bc07.js`.

### Configuration du Hot Module Replacement (HMR)

Retournez à votre terminal, installez [React Hot Loader](https://github.com/gaearon/react-hot-loader) comme dépendance de développement.

```
yarn add react-hot-loader @hot-loader/react-dom -D
```

Ouvrez `.babelrc` et ajoutez les lignes 3 et 9. N'oubliez pas d'inclure la virgule (,) à la fin de la ligne 3 :

```js
{
  "presets": [
    ["@babel/preset-env", { "modules": false }],
    "@babel/preset-react"
  ],
  "plugins": [
    "@babel/plugin-syntax-dynamic-import",
    "@babel/plugin-proposal-class-properties",
    "react-hot-loader/babel"
  ]
}
```

Ouvrez `webpack.config.js` et modifiez-le comme suit.

_Je n'inclus que le code pertinent et omets le code qui est resté le même pour plus de concision._

```js
...
module.exports = {
  entry: './src/index.js',
  output: {
    ...
    publicPath: '/'
  },
  resolve: {
    alias: {
      "react-dom": "@hot-loader/react-dom",
    },
  },
  ...
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    ...
  ],
  devServer: {
    ...
    hot: true
  }
};
```

* `publicPath: '/'` — Le rechargement à chaud ne fonctionnera pas comme prévu pour les routes imbriquées sans cela
* `webpack.HotModuleReplacementPlugin` — Affiche des noms de modules plus lisibles dans le terminal du navigateur lors des mises à jour HMR
* `hot: true` — Active le HMR sur le serveur
* `resolve: alias` — remplace `react-dom` par le `react-dom` personnalisé de `hot-loader`

Ouvrez `index.js` et modifiez-le comme suit.

```js
import { hot } from "react-hot-loader/root";
import React from "react";
import ReactDOM from "react-dom";
import App from "./components/App";

import "./index.css";

const render = (Component) =>
  ReactDOM.render(<Component />, document.getElementById("root"));

render(hot(App));
```

Nous sommes maintenant prêts à tester le HMR ! Retournez dans le terminal, exécutez votre application, faites une modification et regardez l'application se mettre à jour sans rechargement complet de la page.

```
yarn start
```

![Image](https://cdn-media-1.freecodecamp.org/images/tBaz3tT6Vsnxk7ijy1xFl03YFWmktaaktUWH)
_HMR en action_

Après avoir mis à jour le fichier, la page change sans rechargement complet. Pour montrer ce changement dans le navigateur, je sélectionne **Rendering -> Paint flashing** dans Chrome DevTools, ce qui met en évidence les zones de la page, en vert, qui ont changé. Je mets également en évidence dans le terminal le changement que Webpack a envoyé au navigateur pour que cela se produise.

### Fractionnement de code

Avec le [fractionnement de code](https://webpack.js.org/guides/code-splitting/), au lieu d'avoir votre application dans un seul gros bundle, vous pouvez avoir plusieurs bundles se chargeant de manière asynchrone ou en parallèle. Vous pouvez également séparer le code du fournisseur de votre code d'application, ce qui peut potentiellement diminuer le temps de chargement.

#### Par route

Il existe plusieurs façons d'atteindre le fractionnement de code par route, cependant dans notre cas, nous utiliserons [react-imported-component](https://github.com/theKashey/react-imported-component).

Nous aimerions également afficher un _spinner de chargement_ lorsque l'utilisateur navigue vers une route différente. C'est une bonne pratique car nous ne voulons pas que l'utilisateur fixe un écran vide pendant qu'il/elle attend que la nouvelle page se charge. Nous allons donc créer un composant _Loading_.

Cependant, si la nouvelle page se charge vraiment rapidement, nous ne voulons pas que l'utilisateur voie un spinner de chargement clignoter pendant quelques millisecondes, nous allons donc retarder le composant _Loading_ de 300 millisecondes. Pour y parvenir, nous utiliserons [React-Delay-Render](https://github.com/arnthor3/react-delay-render).

Commencez par installer les deux dépendances supplémentaires.

Dans votre terminal, tapez ce qui suit :

```
yarn add react-imported-component react-delay-render
```

Maintenant, nous allons créer les composants _Loading_.

Dans votre terminal, tapez ce qui suit :

```
touch ./src/components/Loading.js
```

Ouvrez `Loading.js` et copiez ce qui suit :

```js
import React from 'react';
import { Loader } from 'semantic-ui-react';
import ReactDelayRender from 'react-delay-render';

const Loading = () => <Loader active size="massive" />;

export default ReactDelayRender({ delay: 300 })(Loading);
```

Maintenant que nous avons le composant _Loading_, ouvrez `App.js` et modifiez-le comme suit :

```js
import React from 'react';
import { Switch, BrowserRouter as Router, Route } from 'react-router-dom';
import importedComponent from 'react-imported-component';

import Home from './Home';
import Loading from './Loading';

const AsyncDynamicPAge = importedComponent(
  () => import(/* webpackChunkName:'DynamicPage' */ './DynamicPage'),
  {
    LoadingComponent: Loading
  }
);
const AsyncNoMatch = importedComponent(
  () => import(/* webpackChunkName:'NoMatch' */ './NoMatch'),
  {
    LoadingComponent: Loading
  }
);

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/dynamic" component={AsyncDynamicPAge} />
          <Route component={AsyncNoMatch} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
```

Cela créera trois bundles, ou chunks, un pour le composant `DynamicPage`, un pour le composant `NoMatch`, et un pour l'application principale.

Changeons également le nom du fichier bundle. Ouvrez `webpack.config.js` et modifiez-le comme suit :

```js
...
module.exports = {
  ...
  output: {
    filename: '[name].[hash].js',
    ...
  },
}
```

Il est temps d'exécuter l'application et de voir le fractionnement de code par route en action.

```
yarn start
```

![Image](https://cdn-media-1.freecodecamp.org/images/dNGa5cqDKitNHQAKtH7ZDce3fvrCCWuE1zYh)
_Fractionnement de code par route_

Dans le GIF, je mets d'abord en évidence les trois chunks différents créés par Webpack dans le terminal. Ensuite, je mets en évidence le fait qu'au lancement de l'application, seul le chunk principal a été chargé. Enfin, nous voyons qu'en cliquant sur _Navigate to Dynamic Page_, le chunk correspondant à cette page a été chargé de manière asynchrone.

Nous voyons également que le chunk correspondant à la _page non trouvée_ n'a jamais été chargé, économisant ainsi la bande passante de l'utilisateur.

#### Par fournisseur

Maintenant, fractionnons l'application par fournisseur. Ouvrez `webpack.config.js` et apportez les modifications suivantes :

```js
...
module.exports = {
  entry: {
    vendor: ['semantic-ui-react'],
    app: './src/index.js'
  },
  ...
  optimization: {
    splitChunks: {
      cacheGroups: {
        styles: {
          name: 'styles',
          test: /\.css$/,
          chunks: 'all',
          enforce: true
        },
        vendor: {
          chunks: 'initial',
          test: 'vendor',
          name: 'vendor',
          enforce: true
        }
      }
    }
  },
  ...
};
```

* `entry.vendor: ['semantic-ui-react']` — Spécifie quelle bibliothèque nous voulons extraire de notre application principale et dans le chunk _vendor_
* `optimization` — si vous omettez cette entrée, Webpack fractionnera toujours votre application par fournisseur, cependant j'ai remarqué que les tailles des bundles étaient grandes et après avoir ajouté cette entrée, les tailles des bundles ont été considérablement réduites. (Je l'ai obtenu à partir de [Webpack 4 migration draft](https://github.com/webpack/webpack/issues/6357) _CommonsChunkPlugin -> Initial vendor chunk_)

**_Note:_** _Auparavant, Webpack 3 utilisait le `CommonsChunkPlugin` pour fractionner le code par fournisseur et/ou communs, mais il a été déprécié dans Webpack 4 et beaucoup de ses fonctionnalités sont maintenant activées par défaut. Avec la suppression de `CommonsChunkPlugin`, ils ont ajouté `optimization.splitChunks` pour ceux qui ont besoin d'un contrôle fin sur leur stratégie de mise en cache (Voir [ceci](https://gist.github.com/sokra/1522d586b8e5c0f5072d7565c2bee693) pour une explication approfondie)._

Dans le terminal, lancez l'application :

```
yarn start
```

![Image](https://cdn-media-1.freecodecamp.org/images/L5D5dDH3r5DkNfhN2oilt1BaejnhCYfpdnQw)
_Fractionnement de code par fournisseur_

Dans le terminal, je mets en évidence les trois chunks précédents plus le nouveau chunk _vendor_. Ensuite, lorsque nous inspectons le HTML, nous voyons que les chunks vendor et app ont été chargés.

Puisque nous avons apporté plusieurs mises à jour à notre configuration Webpack, vous trouverez ci-dessous le fichier complet `webpack.config.js`.

```js
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const port = process.env.PORT || 3000;
module.exports = {
  mode: 'development',
  entry: {
    vendor: ['semantic-ui-react'],
    app: './src/index.js'
  },
  output: {
    filename: '[name].[hash].js'
  },
  resolve: {
    alias: {
      "react-dom": "@hot-loader/react-dom",
    },
  },
  devtool: 'inline-source-map',
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.css$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader',
            options: {
              modules: true,
              localsConvention: 'camelCase',
              sourceMap: true
            }
          }
        ]
      }
    ]
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        styles: {
          name: 'styles',
          test: /\.css$/,
          chunks: 'all',
          enforce: true
        },
        vendor: {
          chunks: 'initial',
          test: 'vendor',
          name: 'vendor',
          enforce: true
        }
      }
    }
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new HtmlWebpackPlugin({
      template: 'public/index.html',
      favicon: 'public/favicon.ico'
    })
  ],
  devServer: {
    host: 'localhost',
    port: port,
    historyApiFallback: true,
    open: true,
    hot: true
  }
};
```

### Configuration de production

Renommez la configuration Webpack de `webpack.config.js` en `webpack.config.**development**.js`. Ensuite, faites une copie et nommez-la `webpack.config.production.js`.

Dans votre terminal, tapez ce qui suit :

```js
mv webpack.config.js webpack.config.development.js
cp webpack.config.development.js webpack.config.production.js
```

Nous aurons besoin d'une dépendance de développement, [Extract Text Plugin](https://github.com/webpack-contrib/extract-text-webpack-plugin). D'après leur documentation : « Il déplace tous les modules `*.css` requis dans les chunks d'entrée vers un fichier CSS séparé. Ainsi, vos styles ne sont plus intégrés dans le bundle JS, mais dans un fichier CSS séparé (`styles.css`). Si le volume total de votre feuille de style est important, ce sera plus rapide car le bundle CSS est chargé en parallèle du bundle JS. »

Dans votre terminal, tapez ce qui suit :

```
yarn add mini-css-extract-plugin -D
```

Ouvrez `webpack.config.production.js` et apportez les modifications en gras suivantes :

_Faisons quelque chose de différent ici... J'ajouterai des explications avec des commentaires en ligne._

```js
const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
module.exports = {
  mode: 'production',
  entry: {
    vendor: ['semantic-ui-react'],
    app: './src/index.js'
  },
  output: {
    // Nous voulons créer les bundles JavaScript sous un
    // répertoire 'static'
    filename: 'static/[name].[hash].js',
    // Chemin absolu vers le répertoire de sortie souhaité. Dans notre
    // cas, un répertoire nommé 'dist'
    // '__dirname' est une variable Node qui nous donne le chemin absolu
    // vers notre répertoire actuel. Ensuite, avec 'path.resolve', nous
    // joignons les répertoires
    // Webpack 4 suppose que votre chemin de sortie sera './dist', donc vous
    // pouvez simplement laisser cette
    // entrée.
    path: path.resolve(__dirname, 'dist'),
    publicPath: '/'
  },
  // Changer pour les source maps de production
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.css$/,
          use: [
            {
              // Nous configurons 'MiniCssExtractPlugin'              
              loader: MiniCssExtractPlugin.loader,
            }, 
            {
              loader: 'css-loader',
              options: {
                modules: true,
                // Permet de configurer combien de loaders 
                // avant css-loader doivent être appliqués
                // aux ressources @import(ées)
                importLoaders: 1,
                localsConvention: 'camelCase',
                // Créer des source maps pour les fichiers CSS
                sourceMap: true
              }
            },
            {
              // PostCSS s'exécutera avant css-loader et 
              // minifiera et autopréfixera nos règles CSS.
              loader: 'postcss-loader',
            }
          ]
      }
    ]
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        styles: {
          name: 'styles',
          test: /\.css$/,
          chunks: 'all',
          enforce: true
        },
        vendor: {
          chunks: 'initial',
          test: 'vendor',
          name: 'vendor',
          enforce: true
        }
      }
    }
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: 'public/index.html',
      favicon: 'public/favicon.ico'
    }),
    
    // Créer la feuille de style sous le répertoire 'styles'
    new MiniCssExtractPlugin({
      filename: 'styles/styles.[hash].css'
    })
  ]
};
```

Remarquez que nous avons supprimé la variable `port`, les plugins liés au HMR et l'entrée `devServer`.

De plus, puisque nous avons ajouté PostCSS à la configuration de production, nous devons l'installer et créer un fichier de configuration pour celui-ci.

Dans votre terminal, tapez ce qui suit :

```
yarn add postcss-loader autoprefixer cssnano postcss-preset-env -D
touch postcss.config.js
```

Ouvrez `postcss.config.js` et copiez ce qui suit :

```js
const postcssPresetEnv = require('postcss-preset-env');
module.exports = {
  plugins: [
    postcssPresetEnv({
      browsers: ['>0.25%', 'not ie 11', 'not op_mini all']
    }),
    require('cssnano')
  ]
};
```

Ici, nous spécifions les navigateurs que nous voulons que `autoprefixer` (voir la [documentation](https://webpack.js.org/loaders/postcss-loader/) pour plus d'options) prenne en charge et minifions la sortie CSS.

Maintenant, pour la dernière étape avant de créer notre build de production, nous devons créer un script _build_ dans `package.json`.

Ouvrez le fichier et apportez les modifications suivantes à la section `scripts` :

```js
...
"scripts": {
  "dev":"webpack-dev-server --config webpack.config.development.js",
  "prebuild": "rimraf dist",
  "build": "cross-env NODE_ENV=production webpack -p --config webpack.config.production.js"
},
...
```

La première chose à remarquer ici est que nous avons changé le script de démarrage de `start` à `dev`, puis nous avons ajouté deux scripts supplémentaires, `prebuild` et `build`.

Enfin, nous indiquons quelle configuration utiliser en développement ou en production.

* `prebuild` — S'exécutera avant le script de build et supprimera le répertoire `dist` créé par notre dernier build de production. Nous utilisons la bibliothèque [rimraf](https://github.com/isaacs/rimraf) pour cela
* `build` — Tout d'abord, nous utilisons la bibliothèque [cross-env](https://github.com/kentcdodds/cross-env) au cas où quelqu'un utiliserait Windows. De cette façon, la configuration des variables d'environnement avec `NODE_ENV` fonctionnera. Ensuite, nous appelons Webpack avec le drapeau `-p` pour lui indiquer d'optimiser ce build pour la production, et enfin nous spécifions la configuration de production.

Dans votre terminal, installez les deux nouvelles dépendances que nous avons incluses dans `package.json` :

```
yarn add rimraf cross-env -D
```

Avant de créer le build de production, examinons notre nouvelle structure de projet :

```
|-- node_modules
|-- public
    |-- index.html
    |-- favicon.ico
|-- src
    |-- components
        |-- App.js
        |-- DynamicPage.js
        |-- Home.js
        |-- Layout.css
        |-- Layout.js
        |-- Loading.js
        |-- NoMatch.js
    |-- index.js
|-- .babelrc
|-- package.json
|-- postcss.config.js
|-- webpack.config.development.js
|-- webpack.config.production.js
|-- yarn.lock
```

Enfin, nous pouvons créer notre bundle de production.

Dans votre terminal, tapez ce qui suit :

```
yarn build
```

![Image](https://cdn-media-1.freecodecamp.org/images/T81PYokNYP1m76WiEbGipkFrmGYKee46P4IR)
_Création du bundle de production_

Comme vous l'avez remarqué, après avoir exécuté le script `build`, Webpack a créé un répertoire `dist` contenant notre application prête pour la production. Maintenant, inspectez les fichiers qui ont été créés et remarquez qu'ils sont minifiés et que chacun a une source map correspondante. Vous remarquerez également que PostCSS a ajouté des préfixes automatiques au fichier CSS.

Maintenant, prenons nos fichiers de production et lançons un serveur Node pour servir notre site, et voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/A44vaXq-Jc68ClNMgWe5O0o4a3XjIfj3XLrU)
_Exécution du build de production_

**_Note:_** _J'utilise [ce serveur](https://github.com/esausilva/quick-node-server) dans le GIF ci-dessus pour servir nos fichiers de production._

À ce stade, nous avons deux configurations Webpack fonctionnelles, une pour le développement et une pour la production. Cependant, comme les deux configurations sont très similaires, elles partagent de nombreux paramètres. Si nous voulions ajouter autre chose, nous devrions l'ajouter aux deux fichiers de configuration. Corrigons cet inconvénient.

### Composition Webpack

Commençons par installer [webpack-merge](https://github.com/survivejs/webpack-merge) et [Chalk](https://github.com/chalk/chalk) comme dépendances de développement.

Dans votre terminal, tapez ce qui suit :

```
yarn add webpack-merge chalk -D
```

Nous aurons également besoin de quelques nouveaux répertoires et de quelques nouveaux fichiers.

Dans votre terminal, tapez ce qui suit :

```js
mkdir -p build-utils/addons
cd build-utils
touch build-validations.js common-paths.js webpack.common.js webpack.dev.js webpack.prod.js
```

Maintenant, regardons notre nouvelle structure de projet :

```js
|-- build-utils
    |-- addons
    |-- build-validations.js
    |-- common-paths.js
    |-- webpack.common.js
    |-- webpack.dev.js
    |-- webpack.prod.js
|-- node_modules
|-- public
    |-- index.html
    |-- favicon.ico
|-- src
    |-- components
        |-- App.js
        |-- DynamicPage.js
        |-- Home.js
        |-- Layout.css
        |-- Layout.js
        |-- Loading.js
        |-- NoMatch.js
    |-- index.js
|-- .babelrc
|-- package.json
|-- postcss.config.js
|-- webpack.config.development.js
|-- webpack.config.production.js
|-- yarn.lock
```

Ouvrez `common-paths.js` et copiez ce qui suit :

```
const path = require('path');
const PROJECT_ROOT = path.resolve(__dirname, '../');

module.exports = {
  projectRoot: PROJECT_ROOT,
  outputPath: path.join(PROJECT_ROOT, 'dist'),
  appEntry: path.join(PROJECT_ROOT, 'src')
};
```

Ici, nous définissons, comme le nom l'indique, les chemins communs pour nos configurations Webpack. `PROJECT_ROOT` doit regarder un répertoire plus haut car nous travaillons sous le répertoire `build-utils` (un niveau en dessous du chemin racine réel dans notre projet).

Ouvrez `build-validations.js` et copiez ce qui suit :

```js
const chalk = require('chalk');
const ERR_NO_ENV_FLAG = chalk.red(
  `You must pass an --env.env flag into your build for webpack to work!`
);

module.exports = {
  ERR_NO_ENV_FLAG
};
```

Plus tard, lorsque nous modifierons notre `package.json`, nous nécessiterons le drapeau `--env.env` dans les scripts. Ces validations sont pour vérifier que le drapeau est présent ; sinon, il lancera une erreur.

Dans les trois fichiers suivants, nous allons séparer les configurations Webpack en configurations partagées entre le développement et la production, configurations uniquement pour le développement et configurations uniquement pour la production.

Ouvrez `webpack.common.js` et copiez ce qui suit :

```js
const commonPaths = require('./common-paths');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const config = {
  entry: {
    vendor: ['semantic-ui-react']
  },
  output: {
    path: commonPaths.outputPath,
    publicPath: '/'
  },
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        styles: {
          name: 'styles',
          test: /\.css$/,
          chunks: 'all',
          enforce: true
        },
        vendor: {
          chunks: 'initial',
          test: 'vendor',
          name: 'vendor',
          enforce: true
        }
      }
    }
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: 'public/index.html',
      favicon: 'public/favicon.ico'
    })
  ]
};
module.exports = config;
```

Nous avons essentiellement extrait ce qui était partagé entre `webpack.config.development.js` et `webpack.config.production.js` et l'avons transféré dans ce fichier. En haut, nous avons besoin de `common-paths.js` pour définir le `output.path`.

Ouvrez `webpack.dev.js` et copiez ce qui suit :

```js
const commonPaths = require('./common-paths');
const webpack = require('webpack');
const port = process.env.PORT || 3000;
const config = {
  mode: 'development',
  entry: {
    app: `${commonPaths.appEntry}/index.js`
  },
  output: {
    filename: '[name].[hash].js'
  },
  resolve: {
    alias: {
      "react-dom": "@hot-loader/react-dom",
    },
  },
  devtool: 'inline-source-map',
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader',
            options: {
              modules: true,
              localsConvention: 'camelCase',
              sourceMap: true
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ],
  devServer: {
    host: 'localhost',
    port: port,
    historyApiFallback: true,
    hot: true,
    open: true
  }
};
module.exports = config;
```

C'est le même concept que pour le fichier précédent. Ici, nous avons extrait les configurations uniquement pour le développement.

Ouvrez `webpack.prod.js` et copiez ce qui suit :

```js
const commonPaths = require('./common-paths');
const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const config = {
  mode: 'production',
  entry: {
    app: [`${commonPaths.appEntry}/index.js`]
  },
  output: {
    filename: 'static/[name].[hash].js'
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.css$/,
          use: [
            {
              // Nous configurons 'MiniCssExtractPlugin'              
              loader: MiniCssExtractPlugin.loader,
            }, 
            {
              loader: 'css-loader',
              options: {
                modules: true,
                importLoaders: 1,
                localsConvention: 'camelCase',
                sourceMap: true
              }
            },
            {
              loader: 'postcss-loader'
            }
          ]
      }
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'styles/styles.[hash].css'
    })
  ]
};
module.exports = config;
```

Nous avons extrait les configurations uniquement pour la production.

Maintenant que nous avons les configurations partagées et celles spécifiques au développement et à la production dans des fichiers séparés, il est temps de tout rassembler.

Dans le terminal, si vous êtes toujours dans le répertoire `build-utils`, remontez d'un niveau à la racine du projet, puis supprimez les configurations Webpack précédentes et créez une nouvelle configuration Webpack. Nommez-la `webpack.config.js`.

Dans votre terminal, tapez ce qui suit :

```
cd ..
rm webpack.config.development.js webpack.config.production.js
touch webpack.config.js
```

Avant de configurer `webpack.config.js`, ouvrons `package.json` et mettons à jour la section `scripts`.

Modifiez la section comme suit :

```js
...
"scripts": {
  "dev": "webpack-dev-server --env.env=dev",
  "prebuild": "rimraf dist",
  "build": "cross-env NODE_ENV=production webpack -p --env.env=prod"
},
...
```

Puisque nous avons supprimé le drapeau `--config`, Webpack recherchera maintenant la configuration par défaut, qui est `webpack.config.js`. Nous utilisons maintenant le drapeau [--env](https://webpack.js.org/guides/environment-variables/) pour passer une variable d'environnement à Webpack, `env=dev` pour le développement et `env=prod` pour la production.

Ouvrez `webpack.config.js` et copiez ce qui suit :

_Explications avec des commentaires en ligne._

```js
const buildValidations = require('./build-utils/build-validations');
const commonConfig = require('./build-utils/webpack.common');

const webpackMerge = require('webpack-merge');

// Nous pouvons inclure des plugins Webpack, via des addons, qui
// n'ont pas besoin de s'exécuter chaque fois que nous développons.
// Nous verrons un exemple lorsque nous configurerons 'Bundle Analyzer'
const addons = (/* string | string[] */ addonsArg) => {
  
  // Normaliser le tableau des addons (aplatir)
  let addons = [...[addonsArg]] 
    .filter(Boolean); // Si addons est indéfini, le filtrer

  return addons.map(addonName =>
    require(`./build-utils/addons/webpack.${addonName}.js`)
  );
};

// 'env' contiendra la variable d'environnement de la section 'scripts'
// dans 'package.json'.
// console.log(env); => { env: 'dev' }
module.exports = env => {

  // Nous utilisons 'buildValidations' pour vérifier le drapeau 'env'
  if (!env) {
    throw new Error(buildValidations.ERR_NO_ENV_FLAG);
  }

  // Sélectionner quelle configuration Webpack utiliser ; développement
  // ou production
  // console.log(env.env); => dev
  const envConfig = require(`./build-utils/webpack.${env.env}.js`);
  
  // 'webpack-merge' combinera nos configurations partagées, les
  // configurations spécifiques à l'environnement et tous les addons que nous
  // incluons
  const mergedConfig = webpackMerge(
    commonConfig,
    envConfig,
    ...addons(env.addons)
  );

  // Puis retourner la configuration finale pour Webpack
  return mergedConfig;
};
```

Cela peut sembler être beaucoup de configuration, mais à long terme, cela sera utile.

À ce stade, vous pouvez lancer l'application ou créer les fichiers de production, et tout fonctionnera comme prévu (désolé, pas de GIF cette fois).

```
yarn dev
yarn build
```

**_Note:_** _Cette technique de « Composition Webpack » a été tirée de [Webpack Academy](https://webpack.academy/), un cours gratuit de Sean Larkin que je recommande de suivre pour en apprendre davantage sur Webpack, non spécifique à React._

### BONUS : Configuration de Webpack Bundle Analyzer

Vous n'avez pas nécessairement besoin de [Webpack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer), mais il peut être utile lorsque vous essayez d'optimiser vos builds.

Commencez par installer la dépendance et créer le fichier de configuration.

Dans votre terminal, tapez ce qui suit :

```
yarn add webpack-bundle-analyzer -D
touch build-utils/addons/webpack.bundleanalyzer.js
```

Ouvrez `webpack.bundleanalyzer.js` et copiez ce qui suit :

```
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer')
  .BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'server'
    })
  ]
};
```

Nous exportons simplement la section des plugins, qui inclut Bundle Analyzer, pour Webpack. Ensuite, `webpack-merge` la combinera dans la configuration finale de Webpack. Vous vous souvenez des _addons_ dans `webpack.config.js` ? Eh bien, c'est là que cela entre en jeu.

Pour la dernière étape, ouvrons `package.json` et incluons les nouveaux scripts comme suit :

```
"scripts": {
  "dev": "webpack-dev-server --env.env=dev",
  "dev:bundleanalyzer": "yarn dev --env.addons=bundleanalyzer",
  "prebuild": "rimraf dist",
  "build": "cross-env NODE_ENV=production webpack -p --env.env=prod",
  "build:bundleanalyzer": "yarn build --env.addons=bundleanalyzer"
},
```

* `dev:bundleanalyzer` — Appelle le script `dev` et passe une nouvelle variable d'environnement `addons=bundleanalyzer`
* `build:bundleanalyzer` — Appelle le script `build` et passe une nouvelle variable d'environnement `addons=bundleanalyzer`

Il est temps d'exécuter l'application avec l'addon bundle analyzer.

Dans votre terminal, tapez ce qui suit :

```
yarn dev:bundleanalyzer
```

![Image](https://cdn-media-1.freecodecamp.org/images/EFwowawQtLlHdJQGL9gwuz77O2wfhz784xW2)
_Webpack Bundle Analyzer_

L'application se lance aux côtés de Webpack Bundle Analyzer.

Inclure des addons avec la composition Webpack peut être très utile, car il existe de nombreux plugins que vous souhaiteriez utiliser uniquement à certains moments.

### Conclusion

Tout d'abord, vous pouvez obtenir le code complet sur le [dépôt GitHub](https://github.com/esausilva/react-starter-boilerplate-hmr).

Eh bien, vous êtes arrivé à la fin. Félicitations !! ? Maintenant que vous connaissez les bases (et un peu plus) de Webpack pour React, vous pouvez continuer à explorer et à apprendre des fonctionnalités et techniques plus avancées.

Merci d'avoir lu et j'espère que vous l'avez apprécié. Si vous avez des questions, des suggestions ou des corrections, faites-le moi savoir dans les commentaires ci-dessous. N'oubliez pas de partager cet article et de lui donner quelques applaudissements ??.

Vous pouvez me suivre ici sur [Medium](https://medium.com/@_esausilva), [Twitter](https://twitter.com/_esausilva), [GitHub](https://github.com/esausilva/), [LinkedIn](https://www.linkedin.com/in/esausilva/) ou sur tous ces réseaux.

Cet article a été initialement publié sur mon [site web de blog personnel](https://esausilva.com/2018/01/13/learn-webpack-for-react/).

---

**<ins>Mise à jour du 25/08/19 :</ins>** J'ai été en train de construire une application web de prière appelée « **My Quiet Time - A Prayer Journal** ». Si vous souhaitez rester informé, veuillez vous inscrire via le lien suivant : [http://b.link/mqt](http://b.link/mqt)  

L'application sera lancée avant la fin de l'année, j'ai de grands projets pour cette application. Pour voir quelques captures d'écran de maquettes, suivez le lien suivant : [http://pc.cd/Lpy7](http://pc.cd/Lpy7)

Mes DM sur [Twitter](https://twitter.com/_esausilva) sont ouverts si vous avez des questions concernant l'application ?
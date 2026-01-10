---
title: Comment créer une application React à partir de zéro en utilisant Webpack 4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-12T07:24:31.000Z'
originalURL: https://freecodecamp.org/news/part-1-react-app-from-scratch-using-webpack-4-562b1d231e75
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5CEuIhC7lvb5jxiTr0sihg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer une application React à partir de zéro en utilisant Webpack
  4
seo_desc: 'By Linh Nguyen My

  For the past three weeks, I have been trying to create a React app from scratch
  to understand the set-up with Webpack. My aim was to set up a simple configuration
  which can then be grown upon. It’s been a struggle to understand Webp...'
---

Par Linh Nguyen My

Au cours des trois dernières semaines, j'ai essayé de créer une application React à partir de zéro pour comprendre la configuration avec Webpack. Mon objectif était de mettre en place une configuration simple qui peut ensuite être développée. Cela a été un défi de comprendre Webpack. Mais grâce à ce [tutorial](https://www.valentinog.com/blog/webpack-4-tutorial/) de [Valentino Gagliardi](https://twitter.com/gagliardi_vale), je suis beaucoup plus éclairée.

Ce que je prévois de faire est de créer une fonctionnalité de recherche avec des données JSON fictives (ou réelles). Dans cet article de blog, je vais passer en revue la configuration de mon projet. Dans le prochain, je prévois de montrer comment configurer les tests. J'aimerais également ajouter un serveur à cela en utilisant Node.js, mais je ne suis pas sûre si le cadre de mon projet nécessitera cela.

_(**Note** : J'ai fourni ma configuration Webpack à la fin de cet article de blog)_

Sans plus tarder, commençons la configuration !

Créez un **nouveau projet** et **cd** dedans :

```
mkdir react_search
cd react_search
```

Créez un fichier **package.json** :

```
npm init
```

Si vous souhaitez ignorer toutes les questions, ajoutez le drapeau -y :

```
npm init -y
```

Nous devons installer **webpack** comme une dépendance de développement et **webpack-cli** afin que vous puissiez utiliser webpack dans la ligne de commande :

```
npm i webpack webpack-cli -D
```

* i : install
* -D : --save-dev

Créez un **dossier src** avec **index.js** et placez le code suivant comme exemple :

```
console.log("hello");
```

Maintenant, ajoutez les scripts suivants à votre package.json (en gras) :

```
{
  "name": "react_search",
  "version": "1.0.0",
  "description": "Application de recherche utilisant React",
  "main": "index.js",
  
"scripts": {
    "start": "webpack --mode development",
    "build": "webpack --mode production"
  
},
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "webpack": "^4.0.1",
    "webpack-cli": "^2.0.10"
  }
}
```

Webpack 4 dispose maintenant de deux modes, **development** et **production**, où le code est minimisé dans ce dernier.

Voyez cela par vous-même en exécutant :

```
npm run start
```

Cela créera un **dossier dist** avec un fichier **main.js** à l'intérieur (contenant votre code src).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fz0Ulaqaz1K4jSQCYL13zg.png)

Si vous exécutez maintenant :

```
npm run build
```

La sortie suivante est maintenant comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*P3Mq87Jp9w0iaT8Sqb0jfw.png)

### Configuration de React et Babel

Pour travailler avec React, nous devons l'installer ainsi que Babel. Cela transpilera le code de ES6 à ES5, car tous les navigateurs ne supportent pas encore ES6 (par exemple Internet Explorer).

Installez **react** et **react-dom** comme une dépendance

```
npm i react react-dom -S
```

* -S : --save

Ensuite, installez **babel-core**, **babel-loader**, **babel-preset-env** et **babel-preset-react** comme une dépendance de développement :

```
npm i babel-core babel-loader babel-preset-env babel-preset-react -D
```

* **babel-core** : Transforme votre code ES6 en ES5
* **babel-loader** : Aide de Webpack pour transformer vos dépendances JavaScript (par exemple, lorsque vous importez vos composants dans d'autres composants) avec Babel
* **babel-preset-env** : Détermine quelles transformations/plugins utiliser et les polyfills (fournir des fonctionnalités modernes sur les anciens navigateurs qui ne les supportent pas nativement) en fonction de la matrice de navigateurs que vous souhaitez supporter
* **babel-preset-react** : Préréglage Babel pour tous les plugins React, par exemple transformer JSX en fonctions

Nous devons créer un fichier **webpack.config.js** pour indiquer les règles pour notre babel-loader.

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};
```

Nous devons ensuite créer un fichier séparé appelé **.babelrc** pour fournir les options pour babel-loader. Vous pouvez l'inclure dans le fichier webpack.config.js, mais j'ai vu que la plupart des projets ont cela séparé. Cela résulte en une lisibilité plus claire, et il peut être utilisé par d'autres outils non liés à webpack. Lorsque vous indiquez que vous utilisez babel-loader dans votre configuration webpack, il recherchera le fichier .babelrc s'il y en a un.

```js
{
  "presets": ["env", "react"]
}
```

Ensuite, changez votre fichier **index.js** pour rendre un composant :

```js
import React from "react";
import ReactDOM from "react-dom";

const Index = () => {
  return <div>Hello React!</div>;
};

ReactDOM.render(<Index />, document.getElementById("index"));
```

Nous devrons également créer un fichier **index.html** dans le **dossier src** où nous pouvons ajouter notre élément de section avec l'id `index`. C'est là que nous rendons notre composant principal React :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>React et Webpack4</title>
</head>
<body>
  <section id="index"></section>
</body>
</html>
```

Maintenant, nous devons installer **html-webpack-plugin** et l'utiliser dans notre fichier de configuration webpack. Ce plugin génère un fichier HTML avec <script> injecté, écrit cela dans **dist/index**.html, et minimise le fichier.

Installez **html-webpack-plugin** comme une dépendance de développement :

```
npm i html-webpack-plugin -D
```

Mettez à jour la configuration webpack comme suit :

```js
const HtmlWebPackPlugin = require("html-webpack-plugin");

const htmlPlugin = new HtmlWebPackPlugin({
  template: "./src/index.html",
  filename: "./index.html"
});

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },
  plugins: [htmlPlugin]
};
```

Vous pouvez également entrer le plugin comme ceci :

```
plugins: [
    new HtmlWebPackPlugin({
    template: "./src/index.html",
    filename: "./index.html"
  });
]
```

Mais je préfère extraire cela dans une variable afin que je puisse voir la liste des plugins que j'utilise.

La valeur que je donne à la clé `template` est l'endroit où je cherche mon fichier HTML. La valeur du nom de fichier est le nom du HTML minimisé qui sera généré dans le dossier dist.

Si vous exécutez maintenant `npm run start`, vous devriez voir **index.html** être généré dans le dossier dist.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rF3Cnp3lRfgfZfFbn3CWEw.png)

Exécutez `open dist/index.html` et vous devriez voir "Hello React" dans votre navigateur.

### Configuration de webpack-dev-server

Il est un peu fastidieux de continuer à exécuter cette commande chaque fois que vous voulez voir vos modifications dans le navigateur. Pour que webpack "surveille" nos modifications et rafraîchisse chaque fois que nous avons apporté des modifications à l'un de nos composants, nous pouvons utiliser le module **webpack-dev-server**.

Allez-y et installez cela comme une dépendance de développement

```
npm i webpack-dev-server -D
```

Ensuite, changez vos scripts de démarrage de package.json comme suit (en gras) :

```
{
  "name": "react_search",
  "version": "1.0.0",
  "description": "Application de recherche utilisant React",
  "main": "index.js",
  "scripts": {
  
  "start": "webpack-dev-server --mode development --open",    "build": "webpack --mode production"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "react": "^16.2.0",
    "react-dom": "^16.2.0"
  "devDependencies": {
    "babel-core": "^6.26.0",
    "babel-loader": "^7.1.4",
    "babel-preset-env": "^1.6.1",
    "babel-preset-react": "^6.24.1",
    "html-webpack-plugin": "^3.0.6",
    "webpack": "^4.1.1",
    "webpack-cli": "^2.0.10",
    "webpack-dev-server": "^3.1.0"
  }
}
```

Si vous exécutez maintenant `npm run start`, vous devriez voir **localhost:8080** s'ouvrir dans votre navigateur par défaut — c'est à quoi sert le drapeau `--open`. Maintenant, chaque fois que vous apportez des modifications, il rafraîchira la page.

Vous pouvez également ajouter un drapeau `--hot` à votre script de démarrage npm qui vous permettra de recharger uniquement le composant que vous avez modifié au lieu de faire un rechargement complet de la page. Cela est [Hot Module Replacement](https://webpack.js.org/concepts/hot-module-replacement/#src/components/Sidebar/Sidebar.jsx).

### Configuration de CSS

La dernière partie consiste à configurer notre CSS. Comme nous allons importer des fichiers CSS dans nos composants React, nous avons besoin du module **css-loader** pour les résoudre. Une fois cela résolu, nous avons également besoin d'un **style-loader** pour injecter cela dans notre DOM — ajoutant une balise <style> dans l'élément <head> de notre HTML.

Allez-y et installez ces deux modules comme une dépendance de développement :

```
npm i css-loader style-loader -D
```

Nous devons ensuite mettre à jour notre fichier webpack.config.js comme suit :

```js
const HtmlWebPackPlugin = require("html-webpack-plugin");

const htmlWebpackPlugin = new HtmlWebPackPlugin({
  template: "./src/index.html",
  filename: "./index.html"
});

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      }
    ]
  },
  plugins: [htmlWebpackPlugin]
};
```

Notez que l'ordre d'ajout de ces loaders est important. Tout d'abord, nous devons résoudre les fichiers CSS avant de les ajouter au DOM avec le style-loader. Par défaut, webpack utilise les loaders de droite (dernier élément du tableau) à gauche (premier élément du tableau).

#### Rendre le CSS modulaire

Nous pouvons également rendre le CSS modulaire en utilisant webpack. Cela signifie que le nom de la classe sera limité localement et spécifique uniquement au composant en question.

Pour ce faire, nous pouvons fournir certaines options à css-loader :

```js
const HtmlWebPackPlugin = require("html-webpack-plugin");

const htmlWebpackPlugin = new HtmlWebPackPlugin({
  template: "./src/index.html",
  filename: "./index.html"
});

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.css$/,
        use: [
          {
            loader: "style-loader"
          },
          {
            loader: "css-loader",
            options: {
              modules: true,
              importLoaders: 1,
              localIdentName: "[name]_[local]_[hash:base64]",
              sourceMap: true,
              minimize: true
            }
          }
        ]
      }
    ]
  },
  plugins: [htmlWebpackPlugin]
};
```

Comme nous devons donner des options, chaque loader est maintenant un objet avec une paire clé-valeur. Pour activer les modules CSS, nous devons définir l'option **module** pour css-loader à **true**. L'option **importLoaders** configure combien de loaders avant css-loader doivent être appliqués. Par exemple, sass-loader devrait venir avant css-loader.

Le **localIdentName** vous permet de configurer l'identification générée.

* **[name]** prendra le nom de votre composant
* **[local]** est le nom de votre classe/id
* **[hash:base64]** est le hash généré aléatoirement qui sera unique dans le CSS de chaque composant

Pour rendre cela un peu plus visuel, je vais vous donner un exemple. Supposons que j'ai un composant nommé `Form` et que j'ai un bouton avec une classe CSS `primaryButton`. J'ai également un autre composant appelé `Search` et un bouton avec une classe CSS `primaryButton`. Cependant, ces deux classes ont des CSS différents :

```css
Form button.primaryButton {
  background-color: green;
}
Search button.primaryButton {
  background-color: blue;
}
```

Lorsque webpack regroupe votre application, selon quel CSS arrive en dernier, vos deux boutons pourraient avoir la couleur verte ou bleue au lieu que Form ait du vert et Search du bleu.

C'est là que le localIdentName entre en jeu. Avec cela, une fois votre application regroupée, vos boutons auront un nom de classe unique !

![Image](https://cdn-media-1.freecodecamp.org/images/1*r9EZ9GzG_Xkya_ON1uGqIQ.png)

Comme vous pouvez le voir, le nom de la classe du bouton dans le composant Form est différent de celui dans le composant Search — leur nom commence par le nom du composant, le nom de la classe et le code de hachage unique.

Ainsi, avec cela, vous n'aurez pas à vous soucier de savoir si vous avez donné le même nom de classe dans toute votre application — vous n'aurez à vous soucier que de l'avoir utilisé dans le même composant.

Cela conclut la première partie de la création d'une application React à partir de zéro. Dans le prochain article de blog, je vise à expliquer comment configurer les tests pour le TDD et comment les écrire.

Veuillez me faire savoir si quelque chose n'est pas clair et je l'expliquerai du mieux que je peux. J'apprécie et accueille les commentaires constructifs car cela m'aide à m'améliorer :)

J'espère que cela aide !

### ÉDITION

#### Importation de CSS

J'ai eu quelques commentaires me demandant comment ils peuvent rendre le CSS que je n'ai pas abordé précédemment. Ce que vous devez faire est d'importer le fichier CSS dans votre composant React. Par exemple, supposons que vous avez un composant Search et que voici votre arborescence de répertoires :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vwqGrtJO4VBWYvXWE38yAg.png)

Vous devrez importer votre fichier CSS dans votre composant Search comme suit :

```
import style from "./Search.css"
```

Vous pouvez ensuite appliquer différents styles de classe CSS tels que :

```js
const Search = () => {
  return <div className={style.
nameOfYourCSSClass}>
           Hello Search Component :)
         </div>
}
```

Vous n'êtes pas obligé de l'appeler style, mais ce que j'ai trouvé, c'est que la plupart des gens lui ont donné ce nom dans leurs projets.

#### Mon modèle de base Webpack

Pour ceux qui veulent un clone rapide de cette configuration Webpack, je l'ai sur mon [GitHub](https://github.com/pinglinh/simple_webpack_boilerplate). J'ai également inclus un guide plus succinct dans le README.

#### Points d'entrée et de sortie

Webpack 4 par défaut a un point d'entrée par défaut de **index.js** dans votre **dossier src**. Si vous souhaitez pointer vers un fichier différent, vous pouvez le faire en spécifiant un point d'entrée dans votre fichier de configuration webpack :

ex. :

```js
module.exports = {
  
entry: "./src/app.js",  module: {
   ...
  }
}
```

Vous pouvez également spécifier le fichier de sortie comme suit :

```js
const path = require('path')
module.exports = {
  entry: "./src/app.js",
  
output: {
    path: path.resolve('dist'),
    filename: 'bundled.js'
  },
  
module: {
    ...
  }
}
```

Merci à [Gudu Kassa](https://www.freecodecamp.org/news/part-1-react-app-from-scratch-using-webpack-4-562b1d231e75/undefined) pour avoir souligné cela !

_Si vous avez trouvé cela utile, veuillez le partager sur les réseaux sociaux :)_

[www.pinglinh.com](http://www.pinglinh.com)

Suivez-moi sur [Twitter](http://twitter.com/pinglinh) | Consultez mon [LinkedIn](http://linkedin.com/in/lnguyenmy/) | Voir mon [GitHub](http://github.com/pinglinh)
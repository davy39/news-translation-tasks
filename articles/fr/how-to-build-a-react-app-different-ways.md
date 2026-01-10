---
title: Comment créer une application React – Un tour d'horizon des différentes méthodes
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-03-13T19:01:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-react-app-different-ways
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/randy-fath-ymf4_9Y9S_A-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment créer une application React – Un tour d'horizon des différentes
  méthodes
seo_desc: 'Hi everyone! In this article we''re going to take a look at some of the
  many ways you can build a React application these days. We''ll compare their main
  characteristics, along with their pros and cons.

  We''ll start by explaining what React is and what ...'
---

Salut à tous ! Dans cet article, nous allons examiner quelques-unes des nombreuses façons de créer une application React de nos jours. Nous comparerons leurs caractéristiques principales, ainsi que leurs avantages et inconvénients.

Nous commencerons par expliquer ce qu'est React et quelles améliorations il a apportées par rapport à l'ère précédente du développement web. Ensuite, nous allons construire une application React de zéro pour avoir une bonne idée des bibliothèques qui composent React, et comment il interagit avec des dépendances telles que les bundlers (comme Webpack) et les compilateurs (comme Babel).

Enfin, nous allons passer en revue des approches plus réalistes comme CRA (create-react-app) et des alternatives modernes comme Vite, Astro, Gatsby, Next et Remix.

Cet article devrait être assez long mais intéressant à lire si vous vous demandez comment React fonctionne sous le capot, ou si vous voulez en savoir plus sur les différences entre les nombreux outils de build disponibles.

C'est parti !

# Table des matières

* [Qu'est-ce que React et que fait-il ?](#heading-quest-ce-que-react-et-que-fait-il)
    
    * [Le développement web avant React](#heading-le-developpement-web-avant-react)
        
    * [Les avantages de React](#heading-les-avantages-de-react)
        
    * [Comment React fonctionne sous le capot](#heading-comment-react-fonctionne-sous-le-capot)
        
* [Comment créer une application React](#heading-comment-creer-une-application-react)
    
    * [Créer une application React de zéro avec Webpack et Babel](#heading-creer-une-application-react-de-zero-avec-webpack-et-babel)
        
    * [Qu'est-ce que CRA (create-react-app) ?](#quest-ce-que-cra-create-react-app)
        
    * [Qu'est-ce que Vite ?](#heading-quest-ce-que-vite)
        
* [Client side rendering (CSR) vs Server side rendering (SSR)](#heading-client-side-rendering-csr-vs-server-side-rendering-ssr)
    
* [Outils de build SSR](#heading-outils-de-build-ssr)
    
    * [Qu'est-ce qu'Astro ?](#heading-quest-ce-quastro)
        
    * [Qu'est-ce que Gatsby ?](#heading-quest-ce-que-gatsby)
        
* [Les metaframeworks de React](#heading-les-metaframeworks-de-react)
    
    * [Qu'est-ce que Next ?](#heading-quest-ce-que-nextjs)
        
    * [Qu'est-ce que Remix ?](#heading-quest-ce-que-remix)
        
* [Conclusion](#heading-conclusion)
    

# Qu'est-ce que React et que fait-il ?

React.js est une bibliothèque JavaScript open-source populaire pour la création d'interfaces utilisateur (UI) qui a été développée par Facebook. Elle permet aux développeurs de créer des composants UI réutilisables et de spécifier de manière déclarative à quoi l'interface utilisateur doit ressembler et comment elle doit se comporter en fonction des changements de l'état de l'application.

Si vous vous demandez ce que signifie "déclarativement", vous pourriez être intéressé par [cet article sur les paradigmes de programmation](https://www.freecodecamp.org/news/an-introduction-to-programming-paradigms/) que j'ai écrit il y a quelque temps.

React suit une architecture basée sur les composants, où chaque élément de l'interface utilisateur est représenté comme un composant distinct pouvant être réutilisé dans toute l'application. React permet aux développeurs de créer ces composants en utilisant une combinaison de syntaxe de type HTML appelée JSX et de code JavaScript.

React utilise un DOM virtuel (Document Object Model) pour mettre à jour efficacement le DOM réel lorsque l'état de l'application change. Cela signifie qu'au lieu de mettre à jour toute la page à chaque fois qu'un changement survient, React ne met à jour que les composants spécifiques qui doivent être modifiés. Cela rend les applications React plus rapides et plus réactives par rapport aux frameworks JavaScript traditionnels.

Vous pouvez utiliser React pour créer des applications à page unique (SPA), des applications mobiles et même des applications de bureau en utilisant des outils tels qu'Electron. Vous pouvez également le combiner avec d'autres bibliothèques et frameworks pour créer des applications plus complexes.

React dispose d'une communauté vaste et active, avec une multitude de ressources et de bibliothèques tierces disponibles pour aider les développeurs à démarrer rapidement.

Tout cela semble très bien, mais il est difficile de comprendre la valeur d'un outil comme React si vous ne savez pas comment se passait le développement web avant lui. Jetons donc un coup d'œil rapide à cela maintenant.

## Le développement web avant React

Avant React.js, le développement web reposait fortement sur les scripts traditionnels côté client utilisant du JavaScript pur (vanilla) et des bibliothèques comme jQuery.

Les développeurs web construisaient des applications web en manipulant directement le Document Object Model (DOM) des pages web à l'aide de JavaScript. Cette approche était souvent chronophage et sujette aux erreurs, en particulier pour les applications complexes.

[jQuery](https://jquery.com/), une bibliothèque JavaScript populaire, a été introduite comme un moyen de simplifier le processus de manipulation du DOM et de gestion des événements du navigateur. Elle fournissait une syntaxe concise et facile à utiliser pour sélectionner et manipuler les éléments HTML sur une page.

jQuery a été largement adoptée par les développeurs web en raison de sa simplicité, et elle a aidé à améliorer l'efficacité des scripts côté client.

D'autres frameworks JavaScript tels qu'[AngularJS](https://angularjs.org/) et [Backbone.js](https://backbonejs.org/) ont également gagné en popularité au début des années 2010.

AngularJS offrait une approche plus structurée pour la création d'applications web et était fortement axé sur le [data binding](https://www.youtube.com/watch?v=OoLI8nb-VH8) (liaison de données) et l'[injection de dépendances](https://www.youtube.com/watch?v=yunF2PgJlHU). Backbone.js était un Framework léger qui permettait aux développeurs de créer des applications web simples avec un minimum de surcharge.

Mais malgré leur popularité, ces frameworks JavaScript présentaient diverses limitations. Par exemple, ils ne fournissaient pas de moyen efficace de gérer l'état des applications web, ce qui pouvait entraîner des problèmes de performance et des temps de chargement de page lents. Ils n'offraient pas non plus de moyen facile de créer des composants réutilisables, ce qui pouvait rendre difficile la création d'applications web complexes.

React.js a répondu à bon nombre de ces limitations en introduisant une nouvelle façon de penser la construction d'applications web.

React.js a permis aux développeurs de créer des composants UI réutilisables qui pouvaient être assemblés pour construire des interfaces complexes. Il a également introduit le concept de DOM virtuel, qui a amélioré les performances des applications web en minimisant le nombre de mises à jour requises pour le DOM réel.

Dans l'ensemble, bien que le JavaScript pur et les bibliothèques comme jQuery aient été essentiels aux débuts du développement web, ils étaient limités dans leur capacité à gérer des applications complexes. L'émergence de frameworks comme React.js a facilité la tâche des développeurs pour créer des applications web évolutives et efficaces.

## Les avantages de React

React.js a apporté plusieurs améliorations par rapport aux scripts traditionnels côté client utilisant du JavaScript pur et des bibliothèques comme jQuery, ainsi que par rapport à d'autres frameworks JavaScript comme Backbone.js, AngularJS et [Knockout.js](https://knockoutjs.com/). Certaines de ces améliorations incluent :

1. **Architecture basée sur les composants :** React.js a introduit le concept d'architecture basée sur les composants, où les éléments de l'interface utilisateur sont représentés comme des composants réutilisables distincts qui peuvent être assemblés pour créer des interfaces complexes. Cette approche facilite la gestion des applications web complexes, améliore la réutilisabilité du code et permet des tests et un débogage plus efficaces.
    
2. **DOM virtuel :** React.js a introduit le concept de DOM virtuel, qui est une représentation légère du DOM réel. Le DOM virtuel permet de mettre à jour l'interface utilisateur sans re-générer toute la page. Cela se traduit par des temps de chargement plus rapides et une performance améliorée, surtout pour les applications complexes.
    
3. **JSX :** React.js a introduit JSX, une extension de syntaxe qui permet aux développeurs d'écrire du code semblable à du HTML dans des fichiers JavaScript. Cela facilite l'écriture et la maintenance du code, en particulier pour les développeurs qui sont plus familiers avec le HTML qu'avec le JavaScript.
    
4. **Une façon différente de séparer les préoccupations :** Dans les paradigmes précédents, nous avions l'habitude d'avoir le HTML, le CSS et le JavaScript divisés en fichiers différents. Sous le paradigme de React, en utilisant JSX, nous pouvons avoir le HTML, le JS et (facultativement) le CSS dans le même fichier, et diviser nos fichiers selon les composants UI dont ils sont responsables.
    
5. **Data Binding :** React.js a introduit un flux de données unidirectionnel, ce qui signifie que les données circulent dans une seule direction, des composants parents vers les composants enfants. Cette approche simplifie la gestion des données et réduit le risque d'incohérences de données ou de bugs.
    
6. **Évolutivité :** React.js est hautement évolutif et peut être utilisé pour créer des applications de n'importe quelle taille. Il est particulièrement bien adapté à la création d'applications à grande échelle qui nécessitent des interfaces complexes et des mises à jour fréquentes.
    
7. **Soutien de la communauté :** React.js dispose d'une communauté vaste et active qui fournit une documentation complète, des bibliothèques tierces et des tutoriels. Cela facilite l'apprentissage de React.js pour les développeurs et la recherche de solutions aux problèmes courants.
    

Dans l'ensemble, React.js a apporté plusieurs améliorations significatives par rapport aux scripts traditionnels côté client utilisant du JavaScript pur et des bibliothèques comme jQuery, ainsi qu'à d'autres frameworks JavaScript comme Backbone.js, AngularJS et Knockout.js. Ces améliorations ont facilité la tâche des développeurs pour construire des applications web évolutives, efficaces et maintenables.

Si vous voulez approfondir cette transition qui s'est opérée entre les anciens outils et des frameworks comme React, je vous recommande [cette vidéo de uidotdev](https://youtu.be/Wm_xI7KntDs).

## Comment React fonctionne sous le capot

React est une bibliothèque JavaScript qui fonctionne en créant une représentation virtuelle de l'interface utilisateur, appelée le DOM Virtuel. Cette représentation virtuelle est une copie légère du DOM réel, et elle permet à React de gérer et de mettre à jour efficacement l'interface utilisateur.

Lorsqu'un composant React est créé, React génère un arbre de DOM Virtuel correspondant qui représente l'état actuel du composant. L'arbre de DOM Virtuel est essentiellement un objet JavaScript qui décrit la structure de l'interface utilisateur, y compris tous les éléments HTML, leurs attributs et leurs enfants.

Lorsque l'état d'un composant React change, React met à jour l'arbre de DOM Virtuel correspondant pour refléter le nouvel état. L'arbre de DOM Virtuel mis à jour est ensuite comparé à l'arbre de DOM Virtuel précédent pour identifier les différences entre les deux.

React génère ensuite une liste de mises à jour minimales à apporter au DOM réel pour le synchroniser avec le nouvel arbre de DOM Virtuel. Ces mises à jour sont ensuite appliquées au DOM réel, ce qui donne une interface utilisateur mise à jour.

L'un des principaux avantages de cette approche est qu'elle permet à React de mettre à jour l'interface utilisateur efficacement, sans avoir à redessiner toute la page. Cela peut entraîner des améliorations de performance significatives, en particulier pour les applications complexes comportant de nombreux composants et des mises à jour fréquentes.

Un autre avantage de l'utilisation d'un DOM Virtuel est qu'il facilite la création de composants réutilisables. En faisant abstraction des détails du DOM réel, les composants React peuvent être plus facilement assemblés pour construire des interfaces complexes.

Dans l'ensemble, l'approche du DOM Virtuel de React permet un développement d'interface utilisateur efficace et évolutif, et elle a joué un rôle important dans la popularité de React en tant que Framework de développement front-end.

# Comment créer une application React

Super, maintenant que nous avons une idée claire de ce qu'est React et des améliorations qu'il apporte au développement web, commençons réellement à construire des applications !

## Créer une application React de zéro avec Webpack et Babel

Nous allons voir de nombreuses options différentes disponibles, mais nous allons d'abord en construire une de zéro. Cela signifie que nous allons installer et configurer manuellement toutes les dépendances dont React a besoin pour fonctionner réellement.

Gardez à l'esprit qu'il s'agit d'une approche rare à l'heure actuelle, car la plupart des applications sont créées via des scripts qui s'occupent rapidement de tout ce code répétitif. Mais l'idée ici est de voir et de comprendre les différents composants qui interagissent pour faire fonctionner React sous le capot.

Pour construire une application React, nous devrons installer les 4 dépendances suivantes :

**Webpack :** [Webpack](https://webpack.js.org/) est un module bundler open-source populaire pour les applications JavaScript. Il prend plusieurs fichiers JavaScript et leurs dépendances et les regroupe dans un seul bundle optimisé pour une utilisation dans un navigateur web. Il a également la capacité de transformer et de regrouper d'autres types d'actifs tels que le CSS, les images et les polices.

Gardez à l'esprit que Webpack n'est qu'une option parmi de nombreux autres bundlers disponibles. Nous allons l'utiliser car c'est une option assez standard.

Si vous souhaitez en savoir plus sur les modules JS et comment les regrouper avec Webpack, vous pouvez consulter [cet article que j'ai écrit](https://www.freecodecamp.org/news/modules-in-javascript/).

**Babel :** [Babel](https://babeljs.io/) est un compilateur JavaScript open-source populaire qui permet aux développeurs d'écrire du code dans les dernières versions de JavaScript et de le traduire en un code capable de s'exécuter sur des navigateurs et des environnements plus anciens. Il prend en charge les dernières fonctionnalités d'ECMAScript et peut également transpiler d'autres langages qui se compilent en JavaScript, tels que TypeScript et JSX.

Gardez à l'esprit que Babel n'est qu'une option parmi de nombreux autres transpileurs disponibles. Nous allons l'utiliser car c'est une option assez standard.

**React :** React est une bibliothèque JavaScript pour la création d'interfaces utilisateur. Elle se concentre sur la fourniture d'un moyen déclaratif et efficace de construire des interfaces utilisateur complexes en les décomposant en composants plus petits et réutilisables.

**react-dom :** React-DOM est un package qui fournit des méthodes spécifiques au DOM que React utilise pour interagir avec le DOM du navigateur, comme le rendu des composants React dans le DOM, la mise à jour des composants et la gestion des événements utilisateur.

Ainsi, nous avons `react` et `react-dom` qui fournissent les fonctionnalités de base de React, un bundler pour unifier tous les différents fichiers en quelques-uns, et un transpileur pour rendre notre code compatible avec la plupart des navigateurs. C'est tout. Maintenant, passons au code !

1. Démarrez un projet Node en exécutant cette commande dans votre terminal :
    

```plaintext
npm init -y
```

2. Installez les dépendances suivantes :
    

```plaintext
npm i webpack babel-loader @babel/preset-react @babel/core babel-preset-react html-webpack-plugin webpack-dev-server css-loader style-loader @babel/plugin-proposal-class-properties webpack-cli -D && npm i react react-dom -S
```

Ici, nous installons les 4 dépendances mentionnées précédemment ainsi que quelques plugins et outils supplémentaires qui aident Webpack et Babel à fonctionner.

Comme nous faisons cela pour les bases théoriques, nous n'irons pas trop loin dans ces détails. Gardez simplement à l'esprit que les dépendances de base sont les bibliothèques de React, un bundler et un transpileur (plus d'autres éléments mineurs).

Si vous êtes intéressé par une approche plus détaillée, vous pouvez consulter [cet article](https://medium.com/@JedaiSaboteur/creating-a-react-app-from-scratch-f3c693b84658).

3. Maintenant, créez un dossier `src` et deux fichiers `index.js` et `index.html` à l'intérieur en exécutant les deux commandes suivantes :
    

```plaintext
mkdir src && cd src && touch index.js
touch index.html
```

4. Allez dans le fichier `index.html` et insérez ceci :
    

```plaintext
<!doctype html>
<html lang="fr">
<head>
 <meta charset="utf-8">
 <title>Mon application React de zéro</title>
</head>
<body>
 <div id="app"></div>
</body>
</html>
```

C'est l'unique fichier HTML qui sera présent dans notre projet. Lorsque nous construirons finalement le projet, c'est ce fichier qui sera envoyé au client. Initialement, il sera tel que nous l'avons codé (presque vide), puis React fera sa magie et rendra tout le contenu via JavaScript.

5. Allez dans le fichier `index.js` et insérez ceci :
    

```plaintext
import ReactDOM from 'react-dom';
import React from 'react';
const App = () => {
 return <h1>C'est mon application React !</h1>;
 }
ReactDOM.render(<App />, document.getElementById('app'));
```

Ici, nous créons un composant factice appelé `App` et demandons à `react-dom` de l'afficher dans l'élément HTML ayant `app` comme identifiant. Vous voyez, nous venons de coder cet élément comme une div à l'étape précédente. ;)

6. Nous devons maintenant ajouter des fichiers de configuration pour Babel et Webpack. Dans votre répertoire racine, exécutez ce qui suit :
    

```plaintext
touch .babelrc && touch webpack.config.js
```

7. Dans votre fichier `webpack.config.js`, mettez ce qui suit :
    

```plaintext
const HtmlWebPackPlugin = require("html-webpack-plugin");
const htmlPlugin = new HtmlWebPackPlugin({
 template: "./src/index.html",
 filename: "./index.html"
});
module.exports = {
mode: 'development',
  module: {
    rules: [{
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
]},
 plugins: [htmlPlugin]
};
```

6. Dans votre fichier `.babelrc`, mettez ce qui suit :
    

```plaintext
{
 "presets": ["@babel/preset-react"],
 "plugins": ["@babel/plugin-proposal-class-properties"]
}
```

7. Enfin, allez dans votre fichier `package.json` et ajoutez ceci dans la section `scripts` :
    

```plaintext
"start": "webpack serve --config webpack.config.js"
```

À la fin de tout cela, votre structure de fichiers devrait ressembler à ceci :

```plaintext
my-app-from-scratch/
┣ node_modules/
┣ src/
 ┣ index.html
 ┗ index.js
┣ .babelrc
┣ package-lock.json
┣ package.json
┗ webpack.config.js
```

Et votre fichier `package.json` devrait contenir ceci :

```plaintext
{
 "name": "my-app-from-scratch ",
 "version": "1.0.0",
 "description": "",
 "main": "webpack.config.js",
 "scripts": {
   "test": "echo \"Erreur : aucun test spécifié\" && exit 1",
   "start": "webpack serve --config webpack.config.js"
},
 "keywords": [],
 "author": "",
 "license": "ISC",
 "devDependencies": {
 "@babel/preset-react": "^7.12.13",
 "babel-core": "^6.26.3",
 "babel-loader": "^8.2.2",
 "babel-preset-react": "^6.24.1",
 "css-loader": "^5.0.2",
 "html-webpack-plugin": "^5.1.0",
 "style-loader": "^2.0.0",
 "webpack": "^5.22.0",
 "webpack-cli": "^4.5.0",
 "webpack-dev-server": "^3.11.2"
 },
 "dependencies": {
 "react": "^17.0.1",
 "react-dom": "^17.0.1"
 }
}
```

Maintenant, si vous lancez `npm run start`, vous devriez voir votre application prendre vie ! =D

## Qu'est-ce que CRA (create-react-app) ?

Comme nous l'avons vu, configurer une application React à partir de zéro n'est pas SI compliqué. Mais cela peut être pénible de faire tout cela chaque fois que vous voulez démarrer un nouveau projet. De plus, si vous voulez une configuration particulière pour votre bundler et vos transpileurs, cela peut devenir délicat si vous ne maîtrisez pas ces outils.

C'est à cause de ce problème que nous avons obtenu des outils comme Create-react-app (CRA). ;)

[Create-React-App (CRA)](https://create-react-app.dev/) est un outil populaire et officiellement supporté pour créer des applications React rapidement et facilement. C'est un outil d'interface en ligne de commande (CLI) qui automatise la configuration d'un nouveau projet React en générant une structure de fichiers de base, des fichiers de configuration et des scripts de build.

CRA offre une expérience de développement simplifiée en configurant un serveur de développement préconfiguré, le rechargement à chaud (live-reloading) et une optimisation automatique du build pour la production. Il est également livré avec un outil intégré pour exécuter des tests et générer des rapports de couverture de code.

En utilisant CRA, les développeurs peuvent créer une nouvelle application React avec une seule commande, sans avoir à configurer manuellement des fichiers de configuration ou à installer et configurer des outils de build. Cela permet aux développeurs de se concentrer sur l'écriture du code et la construction de leur application, plutôt que de passer du temps sur la configuration.

CRA fournit également un ensemble de configurations de projet par défaut, telles que Webpack et Babel, qui sont optimisées pour la création d'applications React. Cela signifie que les développeurs peuvent démarrer rapidement avec un projet optimisé pour la performance, la maintenabilité et l'évolutivité.

Dans l'ensemble, Create-React-App est un outil puissant qui simplifie le processus de mise en place et de configuration d'un nouveau projet React.

### Comment construire une application avec create-react-app

Démarrer une application React avec CRA est un jeu d'enfant. Il suffit d'exécuter `npx create-react-app <appName>` et il configurera de lui-même tout le boilerplate pour nous.

Après l'exécution, votre structure de dossiers devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-19.png align="left")

Et votre `package.json` devrait contenir ce qui suit :

```javascript
{
  "name": "testapp",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

Vous vous demandez peut-être où sont passés Webpack et Babel, n'est-ce pas ? Eh bien, puisque CRA s'en occupe sous le capot, ils sont initialement cachés. Si nous voulons voir ces fichiers et dossiers cachés, nous pouvons exécuter `npm run eject`.

Vous pouvez maintenant voir que la structure des dossiers contient quelques éléments supplémentaires :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-20.png align="left")

Et votre fichier `package.json` contient la liste complète des dépendances :

```javascript

  "name": "testapp",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@babel/core": "^7.16.0",
    "@pmmmwh/react-refresh-webpack-plugin": "^0.5.3",
    "@svgr/webpack": "^5.5.0",
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "babel-jest": "^27.4.2",
    "babel-loader": "^8.2.3",
    "babel-plugin-named-asset-import": "^0.3.8",
    "babel-preset-react-app": "^10.0.1",
    "bfj": "^7.0.2",
    "browserslist": "^4.18.1",
    "camelcase": "^6.2.1",
    "case-sensitive-paths-webpack-plugin": "^2.4.0",
    "css-loader": "^6.5.1",
    "css-minimizer-webpack-plugin": "^3.2.0",
    "dotenv": "^10.0.0",
    "dotenv-expand": "^5.1.0",
    "eslint": "^8.3.0",
    "eslint-config-react-app": "^7.0.1",
    "eslint-webpack-plugin": "^3.1.1",
    "file-loader": "^6.2.0",
    "fs-extra": "^10.0.0",
    "html-webpack-plugin": "^5.5.0",
    "identity-obj-proxy": "^3.0.0",
    "jest": "^27.4.3",
    "jest-resolve": "^27.4.2",
    "jest-watch-typeahead": "^1.0.0",
    "mini-css-extract-plugin": "^2.4.5",
    "postcss": "^8.4.4",
    "postcss-flexbugs-fixes": "^5.0.2",
    "postcss-loader": "^6.2.1",
    "postcss-normalize": "^10.0.1",
    "postcss-preset-env": "^7.0.1",
    "prompts": "^2.4.2",
    "react": "^18.2.0",
    "react-app-polyfill": "^3.0.0",
    "react-dev-utils": "^12.0.1",
    "react-dom": "^18.2.0",
    "react-refresh": "^0.11.0",
    "resolve": "^1.20.0",
    "resolve-url-loader": "^4.0.0",
    "sass-loader": "^12.3.0",
    "semver": "^7.3.5",
    "source-map-loader": "^3.0.0",
    "style-loader": "^3.3.1",
    "tailwindcss": "^3.0.2",
    "terser-webpack-plugin": "^5.2.5",
    "web-vitals": "^2.1.4",
    "webpack": "^5.64.4",
    "webpack-dev-server": "^4.6.0",
    "webpack-manifest-plugin": "^4.0.2",
    "workbox-webpack-plugin": "^6.4.1"
  },
  "scripts": {
    "start": "node scripts/start.js",
    "build": "node scripts/build.js",
    "test": "node scripts/test.js"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "jest": {
    "roots": [
      "<rootDir>/src"
    ],
    "collectCoverageFrom": [
      "src/**/*.{js,jsx,ts,tsx}",
      "!src/**/*.d.ts"
    ],
    "setupFiles": [
      "react-app-polyfill/jsdom"
    ],
    "setupFilesAfterEnv": [
      "<rootDir>/src/setupTests.js"
    ],
    "testMatch": [
      "<rootDir>/src/**/__tests__/**/*.{js,jsx,ts,tsx}",
      "<rootDir>/src/**/*.{spec,test}.{js,jsx,ts,tsx}"
    ],
    "testEnvironment": "jsdom",
    "transform": {
      "^.+\\.(js|jsx|mjs|cjs|ts|tsx)$": "<rootDir>/config/jest/babelTransform.js",
      "^.+\\.css$": "<rootDir>/config/jest/cssTransform.js",
      "^(?!.*\\.(js|jsx|mjs|cjs|ts|tsx|css|json)$)": "<rootDir>/config/jest/fileTransform.js"
    },
    "transformIgnorePatterns": [
      "[/\\\\]node_modules[/\\\\].+\\.(js|jsx|mjs|cjs|ts|tsx)$",
      "^.+\\.module\\.(css|sass|scss)$"
    ],
    "modulePaths": [],
    "moduleNameMapper": {
      "^react-native$": "react-native-web",
      "^.+\\.module\\.(css|sass|scss)$": "identity-obj-proxy"
    },
    "moduleFileExtensions": [
      "web.js",
      "js",
      "web.ts",
      "ts",
      "web.tsx",
      "tsx",
      "json",
      "web.jsx",
      "jsx",
      "node"
    ],
    "watchPlugins": [
      "jest-watch-typeahead/filename",
      "jest-watch-typeahead/testname"
    ],
    "resetMocks": true
  },
  "babel": {
    "presets": [
      "react-app"
    ]
  }
}
```

Encore une fois, si vous lancez `npm start`, vous verrez votre application s'animer. ;)

## Qu'est-ce que Vite ?

CRA a l'air plutôt cool, non ? C'était un outil vraiment utile pour les développeurs React, car il apportait une grande amélioration par rapport à la construction d'applications de zéro.

Mais le problème avec create-react-app est qu'il est un peu lent. En particulier dans les grandes applications qui possèdent des milliers de lignes de code et des centaines de composants et de fichiers, des outils comme Webpack mettent beaucoup de temps à regrouper et à construire l'application. C'est le genre de problème que des outils comme Vite.js sont venus résoudre.

Pour plus d'informations sur les raisons pour lesquelles CRA n'est pas le meilleur outil de build disponible aujourd'hui, je vous recommande [cette vidéo](https://youtu.be/kvkAoCbTM3Q) et [cette vidéo](https://youtu.be/7m14f0ZzMyY).

[Vite.js](https://vitejs.dev/) est un outil de build et un serveur de développement conçu pour optimiser l'expérience de développement pour les applications web modernes. Il a été créé par [Evan You](https://twitter.com/youyuxi), le créateur du célèbre Framework JavaScript [Vue.js](https://vuejs.org/).

Vite.js est construit sur des modules ES natifs, ce qui permet un chargement de modules plus rapide et plus efficace pendant le développement. Cela signifie que le serveur de développement peut démarrer rapidement et que les modifications apportées au code peuvent être répercutées instantanément dans le navigateur, sans avoir besoin d'un rechargement complet de la page.

Vite.js comprend également un certain nombre d'autres fonctionnalités conçues pour rationaliser le processus de développement. Par exemple, il inclut une prise en charge intégrée de TypeScript, des préprocesseurs CSS et du hot module replacement (HMR). Cela permet d'apporter des modifications au code sans avoir besoin d'un rechargement complet de la page.

Une autre caractéristique clé de Vite.js est son processus de build de production optimisé. Vite.js génère des builds de production hautement optimisés qui exploitent les fonctionnalités modernes des navigateurs telles que le fractionnement du code (code splitting), le chargement différé (lazy loading) et le tree shaking pour réduire la taille du bundle final et améliorer les performances.

Dans l'ensemble, Vite.js est un outil de build puissant et moderne conçu pour rationaliser le processus de développement et améliorer les performances des applications web modernes. Bien qu'il ait été conçu à l'origine pour être utilisé avec Vue.js, vous pouvez l'utiliser avec d'autres frameworks front-end modernes tels que React et [Svelte](https://svelte.dev/).

### Vite.js vs Create React App

Vite.js et Create React App (CRA) sont tous deux des outils de build et des serveurs de développement conçus pour améliorer l'expérience de développement des applications React. Bien qu'il y ait un certain chevauchement dans leurs fonctionnalités, il existe également des différences clés entre les deux outils.

Certaines des améliorations que Vite.js apporte par rapport à Create React App incluent :

1. **Serveur de développement plus rapide :** Vite.js exploite les modules ES natifs pour fournir un serveur de développement plus rapide et plus efficace. Cela signifie que les modifications apportées au code peuvent être répercutées instantanément dans le navigateur sans avoir besoin d'un rechargement complet de la page. CRA, quant à lui, utilise Webpack pour alimenter son serveur de développement, ce qui peut être plus lent et moins efficace.
    
2. **Temps de build plus rapides :** Vite.js génère des builds de production hautement optimisés qui exploitent les fonctionnalités modernes des navigateurs telles que le code splitting, le lazy loading et le tree shaking pour réduire la taille du bundle final et améliorer les performances. Cela peut se traduire par des temps de build considérablement plus rapides par rapport à CRA.
    
3. **Prise en charge d'autres frameworks :** Alors que CRA est conçu spécifiquement pour les applications React, Vite.js peut être utilisé avec d'autres frameworks front-end modernes tels que Vue.js, Svelte et d'autres. Cela fait de Vite.js un outil plus polyvalent pour le développement front-end.
    
4. **Prise en charge intégrée de TypeScript :** Vite.js inclut une prise en charge intégrée de TypeScript, ce qui peut simplifier le processus de développement pour les projets qui utilisent TypeScript.
    
5. **Configuration simplifiée :** Vite.js utilise un format de configuration simple et intuitif qui facilite la prise en main de l'outil. CRA, quant à lui, peut nécessiter une configuration plus complexe pour certains cas d'utilisation.
    

Dans l'ensemble, Vite.js apporte un certain nombre d'améliorations par rapport à Create React App en termes de performance, de polyvalence et de facilité d'utilisation. Cependant, les deux outils ont leurs forces et leurs faiblesses, et le meilleur outil pour un projet particulier dépendra des exigences et des contraintes spécifiques de ce projet.

### Comment construire une application avec Vite

Pour créer une application React avec Vite, allez dans votre ligne de commande et exécutez `npm create vite@latest`.

Suivez ensuite les instructions (il vous sera demandé de fournir le nom du projet et le type de modèle avec lequel vous souhaitez commencer). Après avoir sélectionné les options utilisant React et JavaScript, votre structure de dossiers devrait ressembler à peu près à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-49.png align="left")

Vous verrez qu'elle est assez similaire à celle générée par CRA.

Et voici ce que sera votre `package.json` :

```javascript
{
  "name": "vite-project",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.0.27",
    "@types/react-dom": "^18.0.10",
    "@vitejs/plugin-react": "^3.1.0",
    "vite": "^4.1.0"
  }
}
```

Pour lancer votre application, exécutez simplement `npm run dev` et vous êtes prêt !

Vite est une excellente option pour construire des applications React de nos jours. Il nous offre toute la simplicité et la commodité que CRA nous apportait, avec en plus de grandes optimisations. Cependant, une chose qu'il ne possède pas est le support natif pour le SSR (Server Side Rendering).

Pour comprendre pourquoi cela compte, nous allons passer par une brève explication de ce que sont le CSR (Client Side Rendering) et le SSR, et dans quelles situations l'un peut être plus bénéfique que l'autre. Ensuite, nous examinerons deux outils qui fournissent réellement un support pour le SSR avec React.

# Client Side Rendering (CSR) vs Server Side Rendering (SSR)

Le rendu côté client (CSR) et le rendu côté serveur (SSR) sont deux approches de rendu des pages web dans le développement web.

Le rendu côté client consiste à générer le HTML et à rendre une page web entièrement dans le navigateur web du client à l'aide de JavaScript.

Dans le CSR, le client demande un fichier HTML minimal qui inclut des liens vers des fichiers JavaScript et CSS. Le navigateur du client récupère ensuite les fichiers nécessaires, exécute le JavaScript et met à jour le DOM pour afficher la page web.

Cette approche est souvent utilisée pour les applications à page unique (SPA) où le contenu est généré dynamiquement et change fréquemment. Le rendu côté client peut offrir une expérience utilisateur plus rapide et plus interactive car le navigateur peut mettre à jour l'interface utilisateur sans recharger la page.

Le rendu côté serveur, quant à lui, consiste à générer le HTML complet d'une page web côté serveur avant de l'envoyer au navigateur du client.

Dans le SSR, le serveur traite la demande, récupère les données, génère le HTML et envoie le HTML entièrement rendu au client. Cette approche est souvent utilisée pour les sites web riches en contenu qui nécessitent une optimisation pour les moteurs de recherche (SEO) ou lorsque le contenu change peu fréquemment.

Le rendu côté serveur peut offrir une meilleure vitesse de chargement initiale et un meilleur SEO car les robots des moteurs de recherche peuvent lire le contenu HTML complet.

Le choix entre CSR et SSR dépend des exigences et des contraintes spécifiques d'un projet.

Le rendu côté client peut être plus pratique pour les applications nécessitant un contenu dynamique et des interfaces utilisateur interactives. D'un autre côté, le rendu côté serveur peut être plus approprié pour les sites web riches en contenu qui doivent être optimisés pour le SEO ou pour les projets nécessitant de bons temps de chargement initiaux, en particulier pour les utilisateurs ayant des connexions internet lentes ou des appareils plus anciens.

Certains projets peuvent même utiliser une approche hybride, combinant CSR et SSR pour tirer le meilleur des deux mondes.

Si vous souhaitez explorer davantage les nombreuses options de rendu disponibles dans le développement web, vous pouvez vous référer à [l'article que j'ai récemment écrit sur les patterns de rendu.](https://www.freecodecamp.org/news/rendering-patterns/)

# Outils de build SSR

## Qu'est-ce qu'Astro ?

[Astro](https://astro.build/) est un générateur de sites statiques moderne et un Framework de développement web qui permet aux développeurs de construire des sites et des applications web rapides et efficaces en combinant le rendu côté serveur et le rendu côté client.

Astro utilise une architecture modulaire qui permet aux développeurs de mélanger et d'associer différentes stratégies de rendu, offrant ainsi un maximum de flexibilité et de performance.

Par exemple, Astro prend en charge le rendu côté serveur (SSR) pour les chargements initiaux de pages, ce qui peut améliorer les performances et le SEO, tout en prenant également en charge le rendu côté client (CSR) pour les interactions suivantes, ce qui peut offrir une expérience utilisateur plus interactive et dynamique.

En plus de ses capacités de rendu flexibles, Astro comprend également un certain nombre d'autres fonctionnalités qui en font un outil puissant pour le développement web. Celles-ci incluent :

1. Une prise en charge intégrée des frameworks front-end populaires tels que React, Vue.js et Svelte.
    
2. Un système de build puissant conçu pour optimiser les performances et minimiser la taille des bundles.
    
3. Un modèle de composants flexible qui permet aux développeurs de créer des composants UI et des mises en page réutilisables.
    
4. Un serveur de développement intégré et un hot reloading qui permettent un développement rapide et efficace.
    
5. La prise en charge d'un large éventail de technologies web, notamment le HTML, le CSS, le JavaScript, le Markdown, et plus encore.
    

Dans l'ensemble, Astro est un outil puissant et polyvalent pour la création de sites statiques et d'applications web modernes. Son modèle de rendu flexible, son système de build performant et sa prise en charge des frameworks front-end populaires en font un excellent choix pour les développeurs qui souhaitent créer des expériences web rapides, efficaces et attrayantes.

### Comment construire une application avec Astro

Pour construire une application avec Astro, nous pouvons lancer la commande `npm create astro@latest`.

Suivez ensuite les instructions (il vous sera demandé de fournir le nom du projet et le type de modèle avec lequel vous souhaitez commencer). Une fois cela terminé, votre structure de dossiers ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-50.png align="left")

Et voici ce que sera votre `package.json` :

```javascript
{
  "name": "satellite-series",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@astrojs/react": "^2.0.2",
    "@types/react": "^18.0.28",
    "@types/react-dom": "^18.0.11",
    "astro": "^2.0.17",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```

À partir de la [documentation d'Astro](https://docs.astro.build/en/core-concepts/project-structure/), nous pouvons voir comment fonctionne la structure du projet :

> **src/components** : Les composants sont des unités de code réutilisables pour vos pages HTML. Il peut s'agir de composants Astro ou de composants de framework UI comme React ou Vue. Il est courant de regrouper et d'organiser tous les composants de votre projet dans ce dossier. **src/layouts** : Les Layouts sont un type spécial de composant qui enveloppe du contenu dans une mise en page plus large. Ils sont le plus souvent utilisés par les pages Astro et les pages Markdown ou MDX pour définir la structure de la page. Tout comme src/components, ce répertoire est une convention courante mais n'est pas obligatoire. **src/pages** : Les Pages sont un type spécial de composant utilisé pour créer de nouvelles pages sur votre site. Une page peut être un composant Astro ou un fichier Markdown représentant une page de contenu. src/pages est un sous-répertoire obligatoire dans votre projet Astro. Sans lui, votre site n'aura ni pages ni routes ! **src/styles** : C'est une convention courante de stocker vos fichiers CSS ou Sass dans un répertoire src/styles, mais ce n'est pas obligatoire. Tant que vos styles se trouvent quelque part dans le répertoire src/ et sont importés correctement, Astro les gérera et les optimisera. **public/** : Le répertoire public/ est destiné aux fichiers et actifs qui n'ont pas besoin d'être traités pendant le processus de build d'Astro. Ces fichiers seront copiés tels quels dans le dossier de build. Ce comportement rend public/ idéal pour les actifs courants comme les images et les polices, ou des fichiers spéciaux tels que robots.txt et manifest.webmanifest. Vous pouvez placer du CSS et du JavaScript dans votre répertoire public/, mais sachez que ces fichiers ne seront ni regroupés ni optimisés dans votre build final.

Comme vous pouvez le voir, Astro ajoute des fonctionnalités par-dessus ce que React propose (comme l'optimisation du bundling, les composants Astro et le routage natif). C'est ce que l'on appelle un "metaframework" (nous y reviendrons plus en détail plus tard).

Si vous souhaitez obtenir un aperçu plus détaillé du fonctionnement d'Astro, je vous recommande de [consulter leur documentation](https://docs.astro.build/en/getting-started/). Elle est très bien écrite et facile à suivre.

## Qu'est-ce que Gatsby ?

[Gatsby](https://www.gatsbyjs.com/) est un Framework web moderne basé sur React qui permet aux développeurs de construire des sites et des applications rapides et dynamiques en utilisant les dernières technologies web. Il a été initialement publié en 2015 par [Kyle Mathews](https://twitter.com/kylemathews), et est depuis devenu l'un des générateurs de sites statiques et frameworks web les plus populaires au monde.

L'une des principales caractéristiques de Gatsby est son accent sur la performance et la vitesse. Gatsby utilise une technique appelée pré-rendu pour générer des fichiers HTML, CSS et JavaScript statiques qui peuvent être servis aux utilisateurs presque instantanément, ce qui se traduit par une expérience utilisateur plus rapide et plus réactive.

De plus, l'utilisation de React.js par Gatsby permet aux développeurs de créer des applications web hautement dynamiques et interactives qui ressemblent à des applications natives.

Gatsby offre également un puissant système de plugins qui facilite l'ajout de nouvelles fonctionnalités à votre site ou application. Les plugins Gatsby peuvent aider pour tout, de l'optimisation des images et l'amélioration des performances à l'intégration avec des services externes et des bases de données.

Certains des avantages de l'utilisation de Gatsby incluent :

* Expérience utilisateur rapide et réactive : L'utilisation du pré-rendu et de React.js par Gatsby permet une expérience utilisateur hautement performante.
    
* Communauté vaste et active : Gatsby possède une grande communauté de développeurs et de contributeurs, ce qui signifie qu'il y a beaucoup de ressources et de soutien disponibles.
    
* Système de plugins : Le système de plugins de Gatsby facilite l'ajout de nouvelles fonctionnalités à votre site sans avoir à écrire du code personnalisé.
    
* Intégration avec des services externes : Gatsby peut facilement s'intégrer à des services externes et des bases de données, ce qui en fait un bon choix pour les applications qui doivent accéder et traiter des données provenant de sources variées.
    

Certains des inconvénients de l'utilisation de Gatsby incluent :

* Courbe d'apprentissage abrupte : Gatsby peut être complexe et difficile à apprendre pour les développeurs novices en React ou en développement web en général.
    
* Rendu côté serveur limité : L'utilisation du pré-rendu par Gatsby signifie qu'il n'est peut-être pas le meilleur choix pour les applications nécessitant un rendu côté serveur intensif.
    
* Limitations du site statique : Parce que Gatsby génère des fichiers statiques, il peut ne pas être le meilleur choix pour les applications nécessitant des mises à jour fréquentes de la base de données ou des données en temps réel.
    

Gatsby est un bon choix pour une grande variété d'applications web, y compris les blogs, les sites d'e-commerce, les sites de marketing et d'autres sites axés sur le contenu. Il est particulièrement bien adapté aux applications qui nécessitent des chargements de page rapides et une expérience utilisateur performante, ainsi qu'aux applications qui doivent s'intégrer à des services externes.

### Comment construire une application avec Gatsby

Pour initier un projet Gatsby, lancez `npm init gatsby` et suivez les instructions du CLI.

Votre structure de dossiers pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-51.png align="left")

Dans le dossier `pages`, nous avons un fichier pour chacune des pages du site. Gatsby intègre le routage nativement, tout comme Astro.

Un projet typique d'application front-end React utilisant Gatsby.js comme générateur de site statique aura la structure suivante :

1. Dossier `src/` : Ce dossier contient tout le code source de l'application. Il comprend généralement des sous-dossiers pour les pages, les composants, les images, les styles et les données.
    
2. `gatsby-config.js` : Ce fichier contient les paramètres de configuration de Gatsby. Il inclut des métadonnées telles que le titre du site, la description et l'auteur, ainsi que les paramètres des plugins et d'autres fonctionnalités.
    
3. Dossier `public/` : Ce dossier contient les actifs statiques compilés que Gatsby génère lors de la construction du site. Ces actifs peuvent être déployés sur un serveur web ou un CDN.
    

# Les metaframeworks de React

Les metaframeworks de React sont des frameworks de haut niveau qui fournissent des abstractions et des fonctionnalités supplémentaires **au-dessus** de la bibliothèque React.

Ils sont conçus pour simplifier le développement d'applications complexes et fournir des fonctionnalités supplémentaires qui ne sont pas disponibles dans la seule bibliothèque React.

Quelques exemples de metaframeworks React.js incluent :

1. **Next.js :** [Next.js](https://nextjs.org/) est un metaframework qui fournit le rendu côté serveur, le fractionnement automatique du code et un routage côté client simplifié. Il comprend également une prise en charge intégrée de la génération de sites statiques, des routes API et d'autres fonctionnalités avancées.
    
2. **Remix :** [Remix](https://remix.run/) est un metaframework pour construire des applications React rendues côté serveur. Il fournit un système de gestion de données unifié, un système de routage simple et intuitif, et d'autres fonctionnalités qui peuvent simplifier la construction d'applications web complexes. Remix vise à améliorer la productivité des développeurs en offrant une expérience de développement plus simple et plus rationalisée pour la construction de grandes applications web complexes.
    

Dans l'ensemble, les metaframeworks React.js fournissent des abstractions et des fonctionnalités puissantes qui peuvent simplifier le développement d'applications complexes et aider les développeurs à construire un code de haute qualité, efficace et maintenable.

Commentaire au passage : Astro et Gatsby peuvent également être considérés comme des metaframeworks. Je les ai simplement placés dans une section différente pour introduire ce qu'est le SSR, et aussi parce que Next et Remix offrent plus de fonctionnalités supplémentaires par rapport à React que les deux autres.

## Qu'est-ce que Next.js ?

Next.js est un metaframework populaire pour la construction d'applications React rendues côté serveur (SSR). C'est un projet open-source développé par [Vercel](https://vercel.com/) (anciennement Zeit) qui a gagné en popularité grâce à sa facilité d'utilisation, ses performances et sa flexibilité.

Next.js offre un certain nombre de fonctionnalités prêtes à l'emploi, telles que le fractionnement automatique du code, le rendu côté serveur et le hot module replacement. Il dispose également d'un support intégré pour diverses fonctionnalités front-end, notamment le routage côté client, le service de fichiers statiques et les routes API.

L'un des principaux avantages de Next.js est sa prise en charge du rendu côté serveur, qui peut améliorer les performances et le SEO des applications web. Avec Next.js, le HTML initial est généré sur le serveur, puis il peut être rapidement réhydraté avec du JavaScript côté client.

Si vous vous demandez ce que signifie "hydratation", vous pouvez à nouveau vous référer à [l'article que j'ai écrit sur les patterns de rendu](https://www.freecodecamp.org/news/rendering-patterns/#the-concept-of-hydration). ;)

Next.js prend également en charge la génération de sites statiques, où les pages peuvent être pré-construites et servies statiquement pour une performance plus rapide et une charge serveur réduite. Cette fonctionnalité facilite la création de sites rapides, évolutifs et optimisés pour le SEO avec Next.js.

En plus de ces fonctionnalités, Next.js dispose d'une communauté vaste et active qui fournit de nombreux plugins et outils pour étendre ses fonctionnalités. Il est également conçu pour être facile à utiliser, avec un processus de configuration simple et une API bien documentée.

Une autre chose intéressante à mentionner est que l'équipe de développement de Next travaille main dans la main avec l'équipe de développement de React, de sorte que le Framework Next et la bibliothèque React sont très bien intégrés et profitent mutuellement de leurs dernières fonctionnalités.

Dans l'ensemble, Next.js est un outil puissant et flexible pour construire des applications web modernes avec React. Sa prise en charge du rendu côté serveur et de la génération de sites statiques en fait un choix populaire pour les développeurs cherchant à optimiser leurs applications web pour la performance et le SEO.

### Comment construire une application avec Next.js

Pour créer une application Next, nous pouvons exécuter la commande suivante : `npx create-next-app@latest <appName>`. Suivez ensuite les instructions.

Votre structure de dossiers pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-131.png align="left")

Un projet typique d'application front-end React utilisant Next.js comme Framework aura la structure suivante :

1. Dossier `pages/` : Ce dossier contient toutes les pages de l'application. Chaque fichier de ce dossier représente une route dans l'application, et le nom du fichier correspond au chemin de la route. Par exemple, un fichier nommé `index.js` représente la route racine (`/`), et un fichier nommé `about.js` représente la route `/about`.
    
2. Dossier `public/` : Ce dossier contient les actifs statiques servis directement par le serveur web, tels que les images, les vidéos et les polices.
    
3. Dossier `styles/` : Ce dossier contient tous les styles de l'application. Il comprend des styles globaux, comme la famille de polices et le jeu de couleurs, ainsi que des styles spécifiques aux composants.
    
4. `next.config.js` : Ce fichier contient les paramètres de configuration de Next.js. Il peut être utilisé pour personnaliser des fonctionnalités telles que Webpack, le CSS et la gestion des images.
    

Pour approfondir le fonctionnement de Next, consultez [leur excellente documentation](https://nextjs.org/learn/foundations/about-nextjs).

## Qu'est-ce que Remix ?

Remix est un metaframework pour construire des applications React rendues côté serveur. C'est un projet open-source développé par l'équipe de Remix Software, et il vise à fournir une approche plus simple et plus unifiée de la construction d'applications React rendues côté serveur.

L'une des principales caractéristiques de Remix est son accent sur le code splitting et le lazy loading. Il divise automatiquement votre application en petits morceaux chargés à la demande. Cela peut améliorer les performances et réduire le temps de chargement initial de votre application.

Remix fournit également un système de gestion de données unifié, ce qui facilite la gestion des données dont votre application a besoin pour fonctionner. Avec Remix, vous pouvez définir vos besoins en données en un seul endroit et les récupérer sur le serveur ou le client selon les besoins.

Une autre caractéristique clé de Remix est son système de routage, conçu pour être simple et intuitif. Vous pouvez définir vos routes à l'aide d'une API déclarative, et Remix générera automatiquement le code nécessaire pour gérer le rendu côté client et côté serveur.

Remix offre également une prise en charge intégrée de l'authentification, de l'autorisation et d'autres fonctionnalités courantes des applications web. Il est hautement extensible, avec un système de plugins qui permet d'ajouter facilement des fonctionnalités personnalisées à votre application.

Dans l'ensemble, Remix est un metaframework puissant et flexible pour construire des applications React rendues côté serveur. Son accent sur le code splitting, la gestion des données et le routage facilite la construction d'applications rapides, évolutives et maintenables.

### Comment construire une application avec Remix

Pour créer une application Remix, nous pouvons lancer la commande suivante : `npx create-remix@latest`. Suivez ensuite les instructions.

Votre structure de dossiers pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-132.png align="left")

Un projet typique d'application front-end React utilisant Remix comme Framework aura la structure suivante :

* `public/` : Ce répertoire contient les fichiers publiquement accessibles de l'application, tels que le fichier index.html et d'autres actifs comme les images, les polices, etc.
    
* `app/` : Ce répertoire contient le code source de l'application.
    
* `routes.js` : Ce fichier définit les routes de l'application et les mappe aux composants de page correspondants.
    
* `remix.config.js` : Ce fichier contient les options de configuration pour Remix.js, comme la mise en place du rendu côté serveur et la définition des routes.
    

Pour approfondir le fonctionnement de Remix, consultez [leur documentation](https://remix.run/docs/en/1.14.1/tutorials/blog).

# Conclusion

Il existe plusieurs outils de build React.js populaires, chacun ayant son propre ensemble unique de caractéristiques et d'avantages.

Voici une comparaison des principales caractéristiques, avantages et inconvénients de cinq outils de build React.js populaires : create-react-app, Vite, Astro, Gatsby, Next.js et Remix.

### create-react-app :

* **Caractéristiques** : Un outil en ligne de commande qui configure une application React de base avec une structure de fichiers et un processus de build simples.
    
* **Avantages** : Facile à utiliser, avec un processus de configuration simple et aucune configuration requise. Fournit un bon point de départ pour les nouveaux projets React.
    
* **Inconvénients** : Flexibilité et options de personnalisation limitées. Peut ne pas convenir à des projets plus grands ou plus complexes.
    
* **Idéal pour** : Projets de petite à moyenne taille avec des exigences simples.
    

### Vite :

* **Caractéristiques** : Un outil de build rapide qui exploite les fonctionnalités modernes des navigateurs pour offrir des temps de développement et de build rapides.
    
* **Avantages** : Extrêmement rapide, avec un hot module replacement instantané et d'autres optimisations pour des builds plus rapides. Prend en charge une large gamme de frameworks et de technologies front-end.
    
* **Inconvénients** : Moins mature que d'autres outils, avec une communauté plus petite et moins de plugins disponibles.
    
* **Idéal pour** : Flux de travail de développement modernes et rapides, mettant l'accent sur la vitesse et l'efficacité.
    

### Astro :

* **Caractéristiques** : Un générateur de sites statiques qui peut être utilisé avec React et d'autres frameworks front-end.
    
* **Avantages** : Extrêmement rapide, avec un accent sur la génération de sites statiques pouvant être déployés n'importe où. Fournit une API simple et intuitive pour construire des sites statiques.
    
* **Inconvénients** : Moins mature que d'autres outils, avec une communauté plus petite et moins de plugins disponibles. Peut ne pas convenir à des applications dynamiques ou à des besoins de routage complexes.
    
* **Idéal pour** : Sites statiques ou applications web simples pouvant être générés et servis statiquement.
    

### Gatsby :

* **Caractéristiques principales** : Gatsby est un générateur de sites statiques populaire qui utilise React pour créer des sites et des applications rapides et performants. Il comprend un puissant système de plugins pour ajouter de nouvelles fonctionnalités et prend en charge des fonctions telles que le rendu côté serveur et l'approvisionnement en données à partir de diverses API et bases de données.
    
* **Avantages** : Très performant, système de plugins puissant, bon pour les sites et applications riches en contenu.
    
* **Inconvénients** : Peut être plus limité en termes de mises à jour de données dynamiques et de données en temps réel.
    
* **Idéal pour** : Projets nécessitant des sites ou des applications rapides axés sur le contenu, ou pour les développeurs qui préfèrent une architecture de site statique.
    

### Next.js :

* **Caractéristiques** : Un metaframework pour construire des applications React rendues côté serveur.
    
* **Avantages** : Offre une prise en charge native du rendu côté serveur, de la génération de sites statiques et d'autres fonctionnalités améliorant les performances et le SEO. Dispose d'une communauté vaste et active avec de nombreux plugins et outils disponibles.
    
* **Inconvénients** : Peut être plus complexe à mettre en place et à configurer que certains autres outils. Peut ne pas convenir à des projets plus petits ou plus simples.
    
* **Idéal pour** : Grandes applications web complexes avec des exigences pointues en matière de routage, de gestion des données ou de SEO.
    

### Remix :

* **Caractéristiques** : Un metaframework pour construire des applications React rendues côté serveur.
    
* **Avantages** : Fournit un système de gestion de données unifié, un système de routage simple et intuitif, et d'autres fonctionnalités simplifiant la construction d'applications web complexes. Possède un système de plugins facilitant l'ajout de fonctionnalités personnalisées.
    
* **Inconvénients** : Moins mature que d'autres outils, avec une communauté plus petite et moins de plugins disponibles.
    
* **Idéal pour** : Grandes applications web complexes avec une gestion de données, un routage ou d'autres exigences complexes.
    

En fin de compte, le meilleur choix d'outil de build React.js dépend des besoins spécifiques de votre projet.

Pour les projets de petite à moyenne taille avec des exigences simples et des flux de travail de développement rapides axés sur la vitesse et l'efficacité, Vite peut être le meilleur choix en raison de sa simplicité et de sa facilité d'utilisation.

Pour les sites statiques ou les applications web simples pouvant être générés et servis de manière statique, Astro peut être la meilleure option.

Et pour les projets plus importants et plus complexes avec des exigences de routage, de gestion de données ou de SEO élaborées, Next.js peut être un meilleur choix.

Eh bien tout le monde, c'est tout pour aujourd'hui. Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/03/23b4b79490fdda967ee0fcc8d9c57402_w200.gif align="left")
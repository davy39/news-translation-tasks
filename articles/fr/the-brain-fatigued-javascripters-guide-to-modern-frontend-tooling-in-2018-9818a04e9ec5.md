---
title: Le guide du développeur JavaScript épuisé pour l'outil moderne de frontend
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-29T01:05:45.000Z'
originalURL: https://freecodecamp.org/news/the-brain-fatigued-javascripters-guide-to-modern-frontend-tooling-in-2018-9818a04e9ec5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mbiAnHlVRgaTRr8tgNU5zg.jpeg
tags:
- name: Angular
  slug: angularjs
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: webpack
  slug: webpack
seo_title: Le guide du développeur JavaScript épuisé pour l'outil moderne de frontend
seo_desc: 'By Amin Mohamed Ajani

  From package managers to ESLint, CommonJS to AMD, and ES6 Modules to Babel and Webpack
  — that’s a lot of tools! In this article, we’ll migrate an old AngularJS app where
  we’ll decode the tools NOW.

  I’m tired…

  Yes, I got the fati...'
---

Par Amin Mohamed Ajani

Des gestionnaires de paquets à ESLint, de CommonJS à AMD, et des modules ES6 à Babel et Webpack — c'est beaucoup d'outils ! Dans cet article, nous allons migrer une ancienne application AngularJS où nous allons décoder les outils MAINTENANT.

### Je suis fatigué...

Oui, j'ai [la fatigue](https://medium.com/@ericclemmons/javascript-fatigue-48d4011b6fc4) aujourd'hui.

%[https://twitter.com/reverentgeek/status/1006942235366223872?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1006942235366223872&ref_url=https%3A%2F%2Fmedium.com%2Fmedia%2Fac2b60273f3275b4dd489fc315bc01ac%3FpostId%3D9818a04e9ec5] 

Cela m'a fait réfléchir, j'aurais pu continuer à travailler dans les ventes et ne pas faire un détour vers le développement web frontend. Mais ensuite, j'ai réalisé que le développement frontend est pour les cœurs courageux, et les cœurs courageux n'abandonnent pas. Ils gagnent.

Alors je choisis de gagner en écrivant quelque chose de valable pour les victimes fatiguées du développement frontend et de ses outils. J'écrirai sur la façon dont j'ai transformé du code de débutant en une application de niveau production à part entière, et les outils que j'ai configurés dans le processus.

Commençons !

### Ce que nous construisons

Rien de fantaisiste. Nous construisons une application web qui récupère certains utilisateurs aléatoires à partir d'une API et les affiche sur le frontend. Elle n'aura **aucun routage extraordinaire***. L'objectif final de l'article est de vous équiper pour vous habituer à l'outil frontend.

J'utilise AngularJS sans code standard, donc nous ne sommes pas abstraits des CLIs qui nous laissent sans souffle et dans l'admiration de la magie noire. Remarque : J'utilise AngularJS et non Angular. AngularJS parce que je n'ai pas trouvé de posts liés à l'outil et au bundling AngularJS.

Commençons par créer un fichier index dans notre répertoire racine.

```html
<html>
<head>
    <title>Utilisateur Aléatoire !</title>
    <link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre.min.css">
</head>
<body>
<div class="container">
    <h1 class="text-center">Utilisateur Aléatoire !</h1>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.7.0/angular.min.js"></script>
</body>
```

Le bon vieux temps. Nous avons un fichier AngularJS et un framework CSS minimal à partir du CDN, puis nous commençons à cuisiner notre code JavaScript et à l'attacher ligne par ligne à l'index.

Mais à mesure que votre application grandira, il sera nécessaire de garder une trace de toutes vos dépendances (dans ce cas, Angular).

#### Entrée des Gestionnaires de Paquets

Beaucoup de gens ont recours à un gestionnaire de paquets qui garde une trace des versions des dépendances qu'ils utilisent sur leur projet. Le principal avantage d'un gestionnaire de paquets est d'aller sur le GitHub de la dépendance, de la télécharger dans votre dossier et de garder une trace de la version téléchargée. Cela vous aide à ne pas casser votre code si vous déplacez votre dépôt et téléchargez une autre version plus tard.

Il y avait [duojs](http://github.com/duojs/duo), [jspm](https://github.com/jspm/jspm-cli), [bower](https://github.com/bower/bower), [npm](https://github.com/npm/npm) et maintenant, il y a :

%[https://twitter.com/yarnpkg/status/785857780838232064?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E785857780838232064&ref_url=https%3A%2F%2Fmedium.com%2Fmedia%2F6e083025c03285c9318802ed8f8c1632%3FpostId%3D9818a04e9ec5] 

Allez-y, [installez-le](https://yarnpkg.com/en/docs/install). Nous allons en avoir besoin. Lorsque nous **ajoutons** une dépendance dans notre application, yarn téléchargera le contenu et le gardera dans le dossier node\_modules. À partir de ce moment, si vous avez besoin du fichier, vous pouvez le référencer dans votre index.

```javascript
yarn add angular
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*MMK6im0fzHzttrpiHHqL5Q.jpeg align="left")

Pendant que nous faisons cela, ajoutons également les fichiers app.js, userController.js et userFactory.js dans notre répertoire racine et relions-les à notre fichier index.

App.js :

```js
/**
 * /app.js
 */

var app = angular.module("RandomApp", []);
```

userFactory.js :

```js
// /userFactory.js
app.factory("UserF", function($http) {
    var UserF = {};
    UserF.getUsers = function(){
        return $http({
            method: 'GET',
            url: 'https://www.reqres.in/api/users',
        })
    };
    return UserF;
});
```

userController.js :

```js
// /userController.js
app.controller("userController", function($scope, UserF){
    $scope.users = [];
    UserF.getUsers()
        .then(function(res) {
            $scope.users = res.data.data;
        })
});
```

index.html :

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Utilisateur Aléatoire !</title>
    <link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre.min.css">
</head>
<body>
<div class="container" ng-app="RandomApp">
    <h1 class="text-center">Utilisateur Aléatoire !</h1>
    <div ng-controller="userController">
        <div ng-repeat="user in users">
            <div class="card">
                <div class="card-image">
                    <img ng-src="{{user.avatar}}" class="img-responsive">
                </div>
                <div class="card-header">
                    <div class="card-title h5">{{user.first_name}} {{user.last_name}}</div>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="node_modules/angular/angular.min.js"></script>
<script src="app.js"></script>
<script src="userController.js"></script>
<script src="userFactory.js"></script>
</body>
</html>
```

#### Problèmes avec cette approche

L'ordre de nos balises de script doit être dans cet ordre spécifique. app.js crée la variable app puis l'attache à l'objet window global. Cette variable app est ensuite utilisée par le reste des fichiers de script. Cela s'appelle souvent la pollution de l'espace de noms global, et si vous utilisez encore cette approche, ne le faites pas. De plus, si nous ouvrons un fichier JS à un moment donné, nous n'aurons aucune idée de ce que contient la variable app.

Un autre problème sémantique avec ce code est qu'il utilise des fonctions anonymes. Les fonctions anonymes sont à la fois une bénédiction et un fléau pour JavaScript. Nommez toujours vos fonctions anonymes. Cela rendra les traces de pile plus faciles à déboguer.

Maintenant, ne serait-ce pas cool si nous avions une police JS qui nous indiquait ces choses pendant que nous écrivons ?

#### ESLint

ESLint est un linter. Un peu comme du code-pairing avec une version plus stricte de vous-même. Les linters vous font gagner du temps en déboguant votre code avant même que vous n'exécutiez votre application. De plus, cela vous force, vous et votre équipe, à suivre des pratiques de code propre. Qui dit non à un tel enseignant génial ?

%[https://twitter.com/TheOrigenStudio/status/1009391662135513088?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1009391662135513088&ref_url=https%3A%2F%2Fmedium.com%2Fmedia%2Fcfe7864721895d9ab6f2c5486bf9e5c4%3FpostId%3D9818a04e9ec5] 

#### Configuration d'ESLint

```javascript
yarn add eslint eslint-config-airbnb eslint-config-airbnb-base -D
```

Nous allons utiliser la [configuration de style d'Airbnb](https://github.com/airbnb/javascript/tree/es5-deprecated/es5) qui parcourt notre code et nous indique partout où nous écrivons le code de manière non standard. La commande ci-dessus installera les configurations dans le dossier node\_modules, mais nous devrons dire à ESLint de les utiliser. Créez un fichier appelé .eslintrc.json et remplissez-le avec :

```js
// .eslintrc.json
{
  "extends": [
    "airbnb/legacy"
  ],
  "env": {
    "browser": true
  }
}
```

La pile extends indique à ESLint d'utiliser les règles d'Airbnb en plus de ses propres règles. La variable env indique à ESLint de ne pas crier si nous utilisons des variables comme **window** sans les initialiser. Pour lint tous nos fichiers, vous pouvez utiliser un wildcard \*.

```javascript
node_modules/.bin/eslint *.js
```

Lançons ESLint sur nos fichiers et voyons ce qui se passe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*F47YGCwPC3b-B08jqMd0Mw.jpeg align="left")

Ce sont toutes les règles définies dans le guide de style d'Airbnb. Je vous laisse corriger vos fichiers. Il est toujours préférable d'avoir un linter dès le début. Bien sûr, vous pouvez également désactiver une règle particulière. Par exemple, si vous préférez l'absence de point-virgule, ou le style de guillemets doubles plutôt que simples, vous pouvez les désactiver. ESLint vous offrira cette flexibilité.

#### Modules

Maintenant, parlons de modularité. Lors de la création d'applications à grande échelle, nous devons avoir notre code bien structuré afin qu'il soit plus facile à mettre à l'échelle. Nous mettons en place une séparation des préoccupations en regroupant des morceaux de code dans des modules séparés. JavaScript ne supportait pas les modules jusqu'à l'arrivée d'ES6. Mais le concept de modularité est apparu bien avant ES6.

#### CommonJS

Avant ES6, cette norme a été adoptée comme un modèle où vous écrivez votre morceau de code et dites à l'environnement d'exporter ce morceau. Ensuite, vous utilisiez une bibliothèque comme [RequireJS](http://requirejs.org/) pour importer le module.

```js
// util.js
module.export = {
    noop: function(){},
    validateUrl: function(s){
      return s.matches(/https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/)
    } 
};
```

```js
// postController.js
var validateUrl = require('./util').validateUrl;
var handleSubmit = function handleSubmit(e) {
    if(!validateUrl(e.target.value)) {
       return;
    }
    submitUrl(e.target.value);
}
```

Si vous avez bricolé avec Node, vous trouverez peut-être ce morceau de code très familier. Mais il y a des inconvénients à cette norme, car elle est synchrone. Cela signifie que tant que validateUrl n'est pas **requis***,* handleSubmit à la ligne 3 de postController ci-dessus n'est pas exécuté. Le code s'arrête.

Cette idéologie fonctionne bien dans Node.js. Dans Node, nous pouvons avoir beaucoup de dépendances avant de démarrer un serveur. Par exemple, configurer des fichiers de log, se connecter à la base de données dans le cloud, configurer des clés secrètes. Mais sur le frontend, ce n'est pas toujours requis.

#### Définition de Module Asynchrone (AMD)

Comme le suggère le nom, il charge les modules de manière asynchrone et [a quelques avantages supplémentaires par rapport aux modèles CommonJS](http://2ality.com/2012/04/declaring-module-exports.html). Voici à quoi ressemble le code en AMD (j'ai ajouté quelques fonctions). Voyez-vous quelque chose de familier ?

```js
define(['validateSpam', 'blockUser', function(validateSpam, blockUser){
  return {
    noop: function(){},
    validateUrl: function(s) {
      return s.matches(/https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/)
    },
    validateSpammyComment: function validateSpammyComment(comment, userID) {
      if(validateSpam(comment)) {
        blockUser(userID);
        return false;
      }
      return true;
  }
```

Cela ressemble un peu à la façon dont nous injectons les dépendances dans AngularJS à la ligne 1.

#### Modules ES6

Puisque le comité de TC39 a vu les développeurs utiliser des bibliothèques externes, ils ont clairement ressenti le besoin pour JavaScript de supporter les modules. Alors ils les ont introduits dans ES6. Utilisons-les !

utils.js :

```js
function noop(){};
function validateUrl(s) {
  return s.matches(/https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/)
}
export {
  noop,
  validateUrl
}
```

postController.js :

```js

import { validateUrl } from './util';

var handleSubmit = function handleSubmit(e) {
    if(!validateUrl(e.target.value)) {
       return;
    }
    submitUrl(e.target.value);
}
```

Pas de bibliothèque externe à appeler. Import/export supporté nativement. Mais il existe encore des versions de navigateurs [qui ne supportent pas complètement toutes les fonctionnalités d'ES6](http://kangax.github.io/compat-table/es6/). Cette incohérence de support des navigateurs n'a pas empêché les programmeurs d'écrire la prochaine génération de JavaScript. Des outils comme [babel](https://babeljs.io/) sont disponibles pour scanner le JavaScript et le **transpiler** en code compatible avec les navigateurs. Et comme ça, votre code supporte les anciens navigateurs comme IE (oh IE, meurs déjà !).

**Babel et ES6**

D'accord, convertissons notre ancien JavaScript en JavaScript plus récent. Un peu, afin que nous puissions ajouter un peu de modularité. Tout ce temps, gardons notre linter de crier.

```js
// /userFactory.js
let angular = window.angular;
let app = angular.module('RandomApp');

/**
 * Une usine d'utilisateurs qui obtient la liste des utilisateurs
 * @param $http
 */

let userFactory = $http => {
  let UserF = {};
  UserF.getUsers = () => $http({
    method: 'GET',
    url: 'https://www.reqres.in/api/users'
  });
  return UserF;
};
app.factory('UserF', userFactory);
```

```js
// /userController.js

let angular = window.angular;
let app = angular.module('RandomApp');

/**
 * Contrôle l'utilisateur
 * @param $scope
 * @param UserF
 */
let userController = ($scope, UserF) => {
  $scope.users = [];
  UserF.getUsers().then(res => $scope.users = res.data.data);
};
userController.$inject = ['$scope', 'UserFactory'];

app.controller('userController', userController);
```

#### Problème avec ce code

Ce code ne fonctionnera pas. Parce que le mot-clé let d'ES6 crée des variables de portée de bloc, et nous ne pouvons pas redéfinir une variable de portée de bloc dans sa propre portée. Rappelez-vous : nous sommes toujours sur la portée globale. Nous allons corriger cela.

La raison pour laquelle je vous ai demandé de refactoriser le code est que je veux que vous utilisiez babel sur celui-ci et que vous voyiez la magie par vous-même. Il est temps d'allumer ce terminal.

```javascript
yarn add babel-cli babel-preset-env
```

Cela ajoutera babel-cli et babel-preset-env.

#### Plugins et présélections de Babel

Le code passe par une série de transformations, et vous pouvez choisir les types de transformations que vous souhaitez. Vous pouvez le faire convertir des fonctions fléchées en fonctions anonymes, transformer les opérateurs de propagation, transformer les boucles for...of et bien plus encore. Ces transformations sont ce que nous appelons des plugins.

Vous pouvez choisir les types de transformations que vous souhaitez. Les groupes de plugins sont appelés présélections. Babel-preset-env crée une cible mouvante pour votre babel. Vous ne pointez pas la version réelle de JavaScript, mais vous demandez à babel de suivre les dernières versions *n* de tous les navigateurs.

Maintenant, créez un fichier de configuration babel : .babelrc et placez-le dans le dossier racine.

```js
{
  "presets": [
    ["env", {
      "targets": {
        "browsers": "last 2 versions"
      }
    }]
  ]
}
```

Maintenant, si vous exécutez la commande suivante sur votre terminal, babel fera son travail. Allez-y, essayez-le :

```javascript
node_modules/.bin/babel *.js
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*P6hqhWvB52pMsILqo708Zw.jpeg align="left")

*il n'y a que tant que je peux capturer. Mais vous comprenez le principe..*

Des trucs astucieux, non ? Babel a donné un aperçu de l'apparence des fichiers s'il devait les convertir pour nous.

Maintenant, prenons une pause et réfléchissons à tout ce que nous avons accompli jusqu'à présent. Nous avons décomposé un fichier JavaScript en plusieurs fichiers. Nous avons ajouté un linter pour qu'il nous crie dessus si nous écrivons du code drôle. Nous écrivons du JavaScript dans le futur et le rendons disponible pour le navigateur dans une version qu'il comprend. Nous avons pollué l'espace de noms global, mais nous l'avons fait de manière géniale, ce que nous corrigerons bientôt.

Si seulement il y avait un outil qui fait tout cela automatiquement. Nous lui dirions de prendre notre code, d'exécuter le linter pour détecter les erreurs avant que le code n'atteigne la production, et de le transpiler en code compatible avec le navigateur. Oui, il existe un tel outil.

Automatisons tout cela.

### Bundling avec Webpack

Tout d'abord, déplacez tous les fichiers JS dans un dossier. Et utilisons des mnémoniques standard et nommons le dossier **build**. De plus, refactorisons nos fichiers JavaScript afin que nous puissions avoir tous nos fichiers construits dans un seul fichier.

```js

// /build/userController.js

/**
 * Contrôle l'utilisateur
 * @param $scope
 * @param UserF
 */
let userController = ($scope, UserF) => {
    $scope.users = [];
    UserF.getUsers().then(res => $scope.users = res.data.data);
};
userController.$inject = ['$scope', 'userFactory'];

export default userController;
```

```js
// /build/userFactory.js
/**
 * Une usine d'utilisateurs qui obtient la liste des utilisateurs
 * @param $http
 */

let userFactory = $http => {
    let UserF = {};
    UserF.getUsers = () => $http({
        method: 'GET',
        url: 'https://www.reqres.in/api/users'
    });
    return UserF;
};
userFactory.$inject = ['$http'];

export default userFactory;
```

```js
// /build/app.js
import angular from 'angular';

import userController from './userController';
import userFactory from './userFactory';

angular.module('RandomApp', [])
  .factory('userFactory', userFactory)
  .controller('userController', userController);
```

```javascript
yarn add webpack webpack-dev-server babel-loader eslint-loader -D
```

Et maintenant, créez un fichier webpack.config.js :

```js
var path = require('path');

module.exports = {
    mode: 'development', // indique à webpack que cela est une build de développement. le commutateur 'production' minifiera le code entre autres choses
    devtool: 'cheap-eval-source-map', // génère des source maps pour un meilleur débogage et ne prend pas beaucoup de temps.
    context: __dirname, // puisque cela s'exécute dans un environnement node, webpack aura besoin du nom du répertoire courant
    entry: './build/app.js', // prend ce fichier et ajoute au fichier bundlé tout ce que ce fichier importe
    output: {
        path: path.join(__dirname, 'dist'), // sortie dans un dossier dist
        filename: 'bundle.js' // et nommez-le bundle.js
    },
  // lisez le post medium pour savoir ce que sont module et devServer car je n'ai pas beaucoup de place pour les commentaires
    module: {
      rules: [{
        enforce: 'pre',
        loader: 'eslint-loader',
        test: /\.js$/
      }, {
        loader: 'babel-loader',
        test: /\.js$/
      }]
    },
    devServer: {
        publicPath: '/dist/',
        filename: 'bundle.js',
        historyApiFallback: true,
        overlay: true
    }
};
```

Si vous lancez maintenant Webpack, vous verrez tous les fichiers regroupés dans un seul fichier dans un dossier dist.

```javascript
webpack
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vz4cQWFXYZdkU-TCJAVyIg.jpeg align="left")

Bonheur.

#### Dissection de la Configuration Webpack

Félicitations. Donnez-vous une tape dans le dos. Vous avez regroupé vos fichiers pour qu'ils soient presque prêts pour la production. Maintenant, parlons de la configuration. Je vais la décomposer et vous dire exactement ce que chaque clé est. Pour plus d'informations, [vous pouvez toujours lire le manuel](https://webpack.js.org/).

J'ai commenté la plupart des trucs. Ici, je parle des trucs laissés de côté :

#### Chargeurs Webpack (objet module)

Pensez à cela comme une chaîne d'unités de chargement de code dans un pipeline. Le dernier de la pile (babel-loader dans notre cas) est le premier que Webpack utilise pour charger les morceaux de code. Nous demandons à Webpack de parcourir notre code et de le transpiler d'abord en ES5 en utilisant le babel-loader.

Un objet chargeur aura également besoin d'une clé de test. Il utilise cette clé pour trouver tous les fichiers qu'il doit ramasser (dans notre cas, une regex qui correspond aux fichiers se terminant par l'extension point JS). Une fois transpilé, passez au chargeur suivant (eslint-loader dans notre cas). Et à la fin, écrivez les modifications de la mémoire dans un fichier et déposez-le dans le fichier que nous avons spécifié dans l'objet de sortie.

Mais ce n'est pas ce que fait notre config. Nous avons ajouté un enforce-pre sur notre chargeur ESLint parce que nous voulons le linting en premier. Parce que la sortie sera un seul fichier. Et ce fichier sera dans un format à peine lisible par l'homme si nous utilisons [la minification et l'obfuscation](https://webpack.js.org/guides/production/) (ce qui est souvent le cas en production). Le Linter deviendra fou en regardant notre code final. Nous ne voulons pas cela. Donc Webpack va d'abord lint puis **transpiler**.

Outre ceux-ci, il existe de nombreux chargeurs que vous pouvez utiliser, que ce soit pour charger vos fichiers de style, vos SVGs ou vos polices. Un chargeur que j'utilise presque toujours au travail est le html-loader.

#### Chargeur HTML

Dans le cas d'Angular, lorsque nous avons des templates dans les directives/composants, nous pouvons utiliser un html-loader dans Webpack.

```javascript
templateUrl: './users/partial/user.tpl.html' // au lieu de cela,
templateUrl: require('./users/partial/user.tpl.html')
```

Webpack prospère grâce à une [super grande communauté](https://github.com/webpack-contrib) qui propose des chargeurs géniaux avec une excellente documentation. Pour tous vos besoins, il y a de fortes chances qu'il y ait au moins un chargeur écrit.

#### Serveur de Développement Webpack (devServer)

Le serveur de développement Webpack est un module qui vient séparément de Webpack. Il lance son propre serveur et surveille les fichiers que nous modifions. Si vous apportez des modifications, le WDS les regroupera à nouveau et rafraîchira la page. S'il y a des erreurs, il rafraîchira la page vers un écran de superposition (configuré par la clé overlay) et vous montrera l'erreur directement dans le navigateur. Et c'est super rapide car il fait tout cela dans la mémoire et non sur le stockage dur.

Bien sûr, pour le faire fonctionner, vous devez d'abord avoir un fichier de build de base (c'est-à-dire exécuter Webpack au moins une fois pour avoir un fichier de build). Une fois que vous avez cela, vous pouvez lancer cette commande. Elle démarrera le serveur et servira les fichiers statiques, ouvrira le navigateur pour vous sur le port 8080 par défaut et surveillera les modifications.

```javascript
webpack-dev-server --open
```

C'est tout !

Mais ce n'est pas la fin si vous y réfléchissez. Il y a encore tant de choses que vous pouvez faire. Au travail, nous utilisons [Flow](https://flow.org/en/) pour la vérification de type statique pendant que nous codons. Un vérificateur de type statique regarde votre code et vous avertit si vous, par exemple, appelez des fonctions avec le mauvais type d'arguments. Vous pouvez également l'intégrer dans Webpack.

Nous utilisons également [Prettier](https://prettier.io/) pour formater notre code automatiquement au fur et à mesure que nous tapons. Cela rend simplement le code plus lisible.

> N'importe quel idiot peut écrire du code qu'un ordinateur peut comprendre. Les bons programmeurs écrivent du code que les humains peuvent comprendre — Martin Fowler.

Je vais bientôt l'afficher comme une affiche sur mon bureau.

### Conclusion

Félicitations ! Vous l'avez fait !

Si vous avez survécu à la lecture de cet article plus grand que nature, permettez-moi de vous donner une tape dans le dos par internet et de vous dire qu'aujourd'hui, vous avez gagné. Survivre à JavaScript n'est pas facile pour moi. J'aurais souhaité connaître tout cela en travaillant sur mon premier projet en tant que développeur UI. Mais je suppose que c'est ainsi que se passe le développement frontend pour moi. Continuez à apprendre, continuez à évoluer.

Je m'amuse avec React pour l'instant, et je pourrais bientôt sortir un autre article si vous avez aimé celui-ci. Peut-être inclure [ReasonML](https://reasonml.github.io/), [GraphQL](https://graphql.org/) ou [Redux](https://redux.js.org/). Si vous avez aimé cet article ou l'avez détesté ou avez des commentaires, veuillez me le faire savoir.

Je vis sur Twitter en tant que [@AminSpeaks](https://www.twitter.com/AminSpeaks) et partout ailleurs en tant que @binarybaba.

Santé et bonne vitesse.
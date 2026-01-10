---
title: Comment configurer Babel dans Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-16T13:58:10.000Z'
originalURL: https://freecodecamp.org/news/setup-babel-in-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/CREATE.png
tags:
- name: Babel
  slug: babel
- name: node js
  slug: node-js
seo_title: Comment configurer Babel dans Node.js
seo_desc: "By Alvin Okoro\nNode.js is one of the most popular back-end technologies\
  \ out there right now. It is friendly, robust, and well-maintained and it's not\
  \ going anywhere anytime soon. \nTo help you learn how to use it effectively, in\
  \ this article we will c..."
---

Par Alvin Okoro

Node.js est l'une des technologies back-end les plus populaires actuellement. Il est convivial, robuste et bien maintenu, et il n'est pas prêt de disparaître. 

Pour vous aider à apprendre à l'utiliser efficacement, dans cet article, nous allons créer un serveur simple en utilisant Node avec Babel configuré dans notre code. 

Mais avant de plonger dans la création de notre serveur, apprenons-en plus sur ce qu'est Babel.

## Qu'est-ce que Babel ? 

Babel est un compilateur JavaScript. C'est un outil populaire qui vous aide à utiliser les dernières fonctionnalités du langage de programmation JavaScript.

## Pourquoi utiliser Babel dans Node.js ?

Avez-vous déjà ouvert un dépôt back-end construit avec Node.js/Express – et la toute première chose que vous avez vue était les instructions d'import et d'export ES6 ainsi que certaines autres fonctionnalités cool de la syntaxe ES6 ? 

Eh bien, Babel a rendu tout cela possible. Rappelez-vous que Babel est un outil populaire qui vous permet d'utiliser les dernières fonctionnalités de JavaScript. Et de nombreux frameworks aujourd'hui utilisent Babel sous le capot pour compiler leur code.

Par exemple, Node ne peut pas utiliser les instructions d'import et d'export ES6 et certaines autres fonctionnalités cool de la syntaxe ES6 sans l'aide d'un compilateur comme Babel. 

Donc dans ce tutoriel, je vais vous montrer comment configurer rapidement votre application Node pour qu'elle soit compatible avec la plupart des syntaxes ES6. 

Génial, non ? Plongeons-nous dedans.

## Prérequis

Ce tutoriel suppose que vous avez les éléments suivants :

* Connaissance de base de Node.js
* Node installé sur votre machine
* Un éditeur de code ou de texte de votre choix

## Commencer

Configurons une application Node de base que nous utiliserons pour ce tutoriel.

Créez un nouveau dossier. Pour ce tutoriel, je vais appeler le mien node-babel. Ajoutez maintenant le dossier à l'espace de travail et ouvrez votre terminal. 

Initialisons et créons un fichier package.json pour notre application :

```js
npm init
```

Cette commande affichera quelques étapes de configuration que nous voulons laisser telles quelles. Donc, appuyer sur la touche Entrée ou Retour tout au long de la configuration fonctionnera bien. 

Une fois que vous avez terminé, créez un nouveau fichier appelé "index.js" qui servira de point d'entrée.

### Comment configurer et installer Babel

Maintenant, nous allons installer trois packages de la famille Babel qui sont : 

```js
@babel/cli, @babel/core et @babel/preset-env
```

Pour installer, nous utilisons la commande suivante pour installer le package :

```js
npm install --save-dev @babel/cli @babel/core @babel/preset-env
```

Nous voulons utiliser **--save-dev** pour les installer en tant que dépendances pour le développement de votre module.  
  
Une fois l'installation terminée, créez un nouveau fichier appelé **.babelrc** pour configurer Babel. 

```js
touch .babelrc
```

Ce fichier hébergera toutes les options que nous voulons ajouter à Babel. Donc pour l'instant, utilisons la configuration que j'utilise normalement pour le développement dans mon application. Vous pouvez la copier et l'ajouter à la vôtre :

```js
{
  "presets": [
    ["@babel/env", {
      "targets": {
        "node": "current"
      }
    }]
  ],
  "plugins": [
    "@babel/plugin-proposal-class-properties",
    "@babel/plugin-proposal-object-rest-spread"
  ]
}
```

La configuration ci-dessus est ce que j'utilise pour dire à Babel que oui, je veux utiliser non seulement mes instructions d'import et d'export, mais aussi la fonctionnalité de classe ainsi que les opérateurs rest et spread d'ES6.

Génial, non ? Continuons.

### Comment configurer un serveur simple

Ouvrez maintenant le fichier "index.js" que nous avons créé précédemment, et ajoutez ce code pour générer un serveur simple :

```js
import http from 'http';

const server = http.createServer((req, res) => {
  res.end('Bonjour depuis le serveur');
}).listen(4001);

console.log('Le serveur est en cours d\'exécution');

export default server;
```

Avec le code d'exemple ci-dessus, notre serveur écoutera sur le port 4001 et nous enverra une réponse "Bonjour depuis le serveur" chaque fois que nous visiterons le port.

### Configurations des scripts de package.json.

Nous avons maintenant un serveur simple. Pour l'exécuter, nous devons transpiler notre code avant de l'exécuter avec Node. Pour ce faire, ouvrez le fichier **"package.json"** et ajoutez ce script de build et de démarrage :

```js
  "scripts": {
+   "build": "babel index.js -d dist",
    "start": "npm run build && node dist/index.js"
  }

```

Bien – alors démarrons notre serveur avec cette commande :

```js
npm start
```

Vous devriez obtenir cette réponse une fois que vous visitez localhost:4001

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot_16.png)

## Comment utiliser Nodemon pour surveiller et redémarrer votre serveur

Pour éviter de redémarrer le serveur vous-même chaque fois que vous apportez des modifications à votre application, nous devons installer nodemon. Vous pouvez installer nodemon dans votre application en utilisant cette commande pour l'installer en tant que dépendance de développement :

```js
npm install --save-dev nodemon

```

Et ensuite, nous reconfigurons nos scripts package.json :

```js
  "scripts": {
    "build": "babel index.js -d dist",
    "start": "npm run build && nodemon dist/index.js"
  }

```

Génial, voici le code final de notre application Node et ce que vous devriez obtenir lorsque vous exécutez "npm start" pour démarrer votre serveur.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot_13.png)

Comme vous pouvez le voir sur l'image ci-dessus, notre serveur est en cours d'exécution. Vous pouvez maintenant utiliser les instructions d'import et d'export de la syntaxe es6 et d'autres fonctionnalités géniales que es6 fournit comme les opérateurs rest et spread dans votre application Node.

## Conclusion

Dans ce tutoriel, nous avons appris comment utiliser la syntaxe ES6 géniale dans notre application Node en utilisant Babel. 

Notez que vous pouvez ajouter plus de configurations dans votre fichier .babelrc. Il n'est pas limité à ce que nous avons dans ce tutoriel – alors n'hésitez pas à le modifier ou à le changer.

Vous pouvez trouver le code d'exemple ici : [https://github.com/Veri5ied/node-babel](https://github.com/Veri5ied/node-babel)

Bon codage !
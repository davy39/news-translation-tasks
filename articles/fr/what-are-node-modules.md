---
title: Qu'est-ce que les modules Node et comment les utiliser ?
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2022-12-06T17:54:33.000Z'
originalURL: https://freecodecamp.org/news/what-are-node-modules
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/stock.jpg
tags:
- name: Express
  slug: express
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: node
  slug: node
- name: npm
  slug: npm
seo_title: Qu'est-ce que les modules Node et comment les utiliser ?
seo_desc: 'Every Node.js application has modules. These modules form part of the building
  blocks of the application. They help developers work faster and write more structured
  code.

  In this tutorial, you will learn what node modules are. You will also learn abo...'
---

Chaque application Node.js utilise des modules. Ces modules constituent une partie des éléments de base de l'application. Ils aident les développeurs à travailler plus rapidement et à écrire un code plus structuré.

Dans ce tutoriel, vous apprendrez ce que sont les modules Node. Vous découvrirez également les trois types de modules Node. Et nous passerons en revue la bonne façon de les utiliser dans vos applications.

## Qu'est-ce qu'un module en JavaScript ?

En termes simples, un module est un morceau de code JavaScript réutilisable. Il peut s'agir d'un fichier `.js` ou d'un répertoire contenant des fichiers `.js`. Vous pouvez exporter le contenu de ces fichiers et les utiliser dans d'autres fichiers.

Les modules aident les développeurs à respecter le principe DRY (Don't Repeat Yourself) en programmation. Ils aident également à décomposer une logique complexe en petits morceaux simples et gérables.

## Types de modules Node

Il existe trois principaux types de modules Node avec lesquels vous travaillerez en tant que développeur Node.js. Ils incluent les suivants.

* Modules intégrés

* Modules locaux

* Modules tiers

### Modules intégrés

Node.js est livré avec certains modules prêts à l'emploi. Ces modules sont disponibles à l'utilisation lorsque vous installez Node.js. Voici quelques exemples courants de modules Node intégrés :

* http

* url

* path

* fs

* os

Vous pouvez utiliser les modules intégrés avec la syntaxe ci-dessous.

```javascript
const someVariable = require('nameOfModule')
```

Vous chargez le module avec la fonction `require`. Vous devez passer le nom du module que vous chargez en tant qu'argument à la fonction `require`.

**Note :** Le nom du module doit être entre guillemets. De plus, l'utilisation de `const` pour déclarer la variable garantit que vous ne réécrivez pas la valeur lors de son appel.

Vous devez également enregistrer la valeur retournée par la fonction `require` dans `someVariable`. Vous pouvez nommer cette variable comme vous le souhaitez. Mais souvent, vous verrez les programmeurs donner le même nom à la variable que le nom du module (voir exemple ci-dessous).

```javascript
const http = require('http')

server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/plain'})
    res.end('Hello World!')
})

server.listen(3000)
```

Vous utilisez la fonction `require` pour charger le module intégré `http`. Ensuite, vous enregistrez la valeur retournée dans une variable nommée `http`.

La valeur retournée par le module `http` est un objet. Puisque vous l'avez chargé en utilisant la fonction `require`, vous pouvez maintenant l'utiliser dans votre code. Par exemple, appelez la propriété `.createServer` pour créer un serveur.

### Modules locaux

Lorsque vous travaillez avec Node.js, vous créez des modules locaux que vous chargez et utilisez dans votre programme. Voyons comment faire cela.

Créez un module simple `sayHello`. Il prend un `userName` comme paramètre et imprime "hello" et le nom de l'utilisateur.

```javascript
function sayHello(userName) {
	console.log(`Hello ${userName}!`)
}

module.exports = sayHello
```

Tout d'abord, vous devez créer la fonction. Ensuite, vous l'exportez en utilisant la syntaxe `module.exports`. Cela ne doit pas nécessairement être une fonction, cependant. Votre module peut exporter un objet, un tableau ou tout type de données.

#### Comment charger vos modules locaux

Vous pouvez charger vos modules locaux et les utiliser dans d'autres fichiers. Pour ce faire, vous utilisez la fonction `require` comme vous l'avez fait pour les modules intégrés.

Mais avec vos fonctions personnalisées, vous devez fournir le chemin du fichier comme argument. Dans ce cas, le chemin est `'./sayHello'` (qui fait référence au fichier `sayHello.js`).

```javascript
const sayHello = require('./sayHello')
sayHello("Maria") // Hello Maria!
```

Une fois que vous avez chargé votre module, vous pouvez y faire référence dans votre code.

### Modules tiers

Une chose intéressante à propos de l'utilisation des modules dans Node.js est que vous pouvez les partager avec d'autres. Le Node Package Manager (NPM) rend cela possible. Lorsque vous installez Node.js, NPM est inclus.

Avec NPM, vous pouvez partager vos modules en tant que packages via [le registre NPM](https://www.npmjs.com/). Et vous pouvez également utiliser les packages que d'autres ont partagés.

#### Comment utiliser les packages tiers

Pour utiliser un package tiers dans votre application, vous devez d'abord l'installer. Vous pouvez exécuter la commande ci-dessous pour installer un package.

```javascript
npm install <name-of-package>
```

Par exemple, il existe un package appelé `capitalize`. Il effectue des fonctions comme la mise en majuscule de la première lettre d'un mot.

L'exécution de la commande ci-dessous installera le package capitalize :

```javascript
npm install capitalize
```

Pour utiliser le package installé, vous devez le charger avec la fonction `require`.

```javascript
const capitalize = require('capitalize')
```

Et ensuite vous pouvez l'utiliser dans votre code, comme ceci par exemple :

```javascript
const capitalize = require('capitalize')
console.log(capitalize("hello")) // Hello
```

Ceci est un exemple simple. Mais il existe des packages qui effectuent des tâches plus complexes et peuvent vous faire gagner beaucoup de temps.

Par exemple, vous pouvez utiliser le package Express.js qui est un framework Node.js. Il rend la création d'applications plus rapide et simple. Pour en savoir plus sur NPM, lisez cet [article de freeCodeCamp sur le Node Package Manager](https://www.freecodecamp.org/news/what-is-npm-a-node-package-manager-tutorial-for-beginners/).

## Conclusion

Dans cet article, vous avez appris ce que sont les modules Node et les trois types de modules Node. Vous avez également appris comment utiliser les différents types dans votre application.

Merci d'avoir lu. Et bon codage !
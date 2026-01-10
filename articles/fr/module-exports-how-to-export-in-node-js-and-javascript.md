---
title: module.exports – Comment exporter en Node.js et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-25T21:03:11.000Z'
originalURL: https://freecodecamp.org/news/module-exports-how-to-export-in-node-js-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-conrad-marshall-615670.jpg
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: node js
  slug: node-js
seo_title: module.exports – Comment exporter en Node.js et JavaScript
seo_desc: "By Dillion Megida\nIn programming, modules are components of a program\
  \ with one or more functions or values. \nThese values can also be shared across\
  \ the entire program and can be used in different ways.\nIn this article, I will\
  \ show you how to share fu..."
---

Par Dillion Megida

En programmation, les modules sont des composants d'un programme avec une ou plusieurs fonctions ou valeurs. 

Ces valeurs peuvent également être partagées dans l'ensemble du programme et peuvent être utilisées de différentes manières.

Dans cet article, je vais vous montrer comment partager des fonctions et des valeurs en exportant et en important des modules dans Node.js.

## Pourquoi exporter des modules ?

Vous voudrez exporter des modules afin de pouvoir les utiliser dans d'autres parties de votre application. 

Les modules peuvent servir à différentes fins. Ils peuvent fournir des utilitaires simples pour modifier des chaînes de caractères. Ils peuvent fournir des méthodes pour effectuer des requêtes API. Ou ils peuvent même fournir des constantes et des valeurs primitives.

Lorsque vous exportez un module, vous pouvez l'importer dans d'autres parties de vos applications et l'utiliser.

Node.js supporte les [Modules CommonJS](https://nodejs.org/api/modules.html) et les [Modules ECMAScript](https://nodejs.org/api/esm.html).

Pour le reste de cet article, nous nous concentrerons sur les Modules CommonJS, l'approche originale pour packager des modules dans Node.js.

Si vous souhaitez en savoir plus sur les Modules ES (ainsi que sur les modules CommonJS), vous pouvez [consulter ce guide approfondi](https://www.freecodecamp.org/news/modules-in-javascript/).

## Comment exporter des modules dans Node

Node.js exporte déjà des modules intégrés qui incluent [fs](https://nodejs.dev/learn/the-nodejs-fs-module), [path](https://nodejs.dev/learn/the-nodejs-path-module) et [http](https://nodejs.dev/learn/the-nodejs-http-module) pour en nommer quelques-uns. Mais vous pouvez créer vos propres modules.

Node.js traite chaque fichier dans un projet Node comme un module qui peut exporter des valeurs et des fonctions depuis le fichier.

Supposons, par exemple, que vous avez un fichier utilitaire `utility.js` avec le code suivant :

```js
// utility.js

const replaceStr = (str, char, replacer) => {
  const regex = new RegExp(char, "g")
  const replaced = str.replace(regex, replacer)
  return replaced
}
```

`utility.js` est un module depuis lequel d'autres fichiers peuvent importer des éléments. Mais `utility.js` n'exporte actuellement rien. 

Vous pouvez vérifier cela en examinant l'objet global `module` dans chaque fichier. Lorsque vous imprimez l'objet global `module` dans ce fichier utilitaire, vous avez :

```js
console.log(module)

// {
//   id: ".",
//   path: "...",
//   exports: {},
//   parent: null,
//   filename: "...",
//   loaded: false,
//   children: [],
//   paths: [
//     ...
//   ],
// }
```

L'objet `module` a une propriété `exports` qui, comme vous pouvez le voir, est un objet vide. 

Ainsi, toute tentative d'importer quoi que ce soit depuis ce fichier lèvera une erreur.

Le fichier `utility.js` a une méthode `replaceStr` qui remplace des caractères dans une chaîne par d'autres caractères. Nous pouvons exporter cette fonction depuis ce module pour qu'elle soit utilisée par d'autres fichiers.

Voici comment faire :

```js
// utility.js

const replaceStr = (str, char, replacer) => {
  const regex = new RegExp(char, "g")
  const replaced = str.replace(regex, replacer)
  return replaced
}

module.exports = { replaceStr }
// ou
exports.replaceStr = replaceStr
```

Maintenant, `replaceStr` est disponible pour être utilisée dans d'autres parties de l'application. Pour l'utiliser, vous l'importez comme ceci :

```js
const { replaceStr } = require('./utility.js')

// puis utilisez la fonction n'importe où
```

## module.exports vs exports dans Node

Vous pouvez exporter des fonctions et des valeurs depuis un module en utilisant soit `module.exports` :

```js
module.exports = { value1, function1 }
```

soit en utilisant `exports` :

```js
exports.value1 = value1
exports.function1 = function1
```

Quelle est la différence ?

Ces méthodes sont assez identiques. En fait, `exports` sert de référence à `module.exports`. Pour mieux comprendre cela, remplissons l'objet `exports` en utilisant les deux façons d'exporter des valeurs :

```js
const value1 = 50
exports.value1 = value1

console.log(module)
// {
//   id: ".",
//   path: "...",
//   exports: { value1: 50 },
//   parent: null,
//   filename: "...",
//   loaded: false,
//   children: [],
//   paths: [
//     ...
//   ],
// }

const function1 = function() {
  console.log("I am a function")
}
module.exports = { function1, ...module.exports }

console.log(module)

// {
//   id: ".",
//   path: "...",
//   exports: { function1: [Function: function1] },
//   parent: null,
//   filename: "...",
//   loaded: false,
//   children: [],
//   paths: [
//     ...
//   ],
// }
```

Il y a deux choses à remarquer ici :

- Le mot-clé `exports` est une référence à l'objet `exports` dans l'objet `modules`. En faisant `exports.value1 = value1`, il a ajouté la propriété `value1` à l'objet `module.exports`, comme vous pouvez le voir dans le premier log.
- Le deuxième log ne contient plus l'export `value1`. Il n'a que la fonction exportée en utilisant `module.exports`. Pourquoi en est-il ainsi ?

`module.exports = ...` est une façon de réassigner un nouvel objet à la propriété `exports`. Le nouvel objet ne contient que la fonction, donc `value1` n'est plus exporté.

Alors, quelle est la différence ?

Exporter des valeurs avec simplement le mot-clé `exports` est un moyen rapide d'exporter des valeurs depuis un module. Vous pouvez utiliser ce mot-clé en haut ou en bas, et tout ce qu'il fait est de remplir l'objet `module.exports`. Mais si vous utilisez `exports` dans un fichier, tenez-vous à l'utiliser tout au long de ce fichier.

Utiliser `module.exports` est un moyen de spécifier explicitement les exports d'un module. Et cela devrait idéalement exister qu'une seule fois dans un fichier. S'il existe deux fois, la deuxième déclaration réassigne la propriété `module.exports`, et le module n'exporte que ce que la deuxième déclaration indique.

Ainsi, en solution au code précédent, vous exportez soit comme ceci :

```js
// ...
exports.value1 = value1

// ...
exports.function1 = function1
```

soit comme ceci :

```js
// ...
module.exports = { value1, function1 }
```

## Conclusion

Chaque fichier dans un projet Node.js est traité comme un module qui peut exporter des valeurs pour être utilisées par d'autres modules. 

`module.exports` est un objet dans un fichier Node.js qui contient les valeurs et fonctions exportées depuis ce module.

Déclarer un objet `module.exports` dans un fichier spécifie les valeurs à exporter depuis ce fichier. Une fois exportées, un autre module peut importer ces valeurs avec la méthode globale `require`.
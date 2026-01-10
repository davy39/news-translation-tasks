---
title: Exports de Modules Node Expliqués – Avec des Exemples de Fonctions d'Exportation
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-17T20:16:29.000Z'
originalURL: https://freecodecamp.org/news/node-module-exports-explained-with-javascript-export-function-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/cover-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: Node.js
  slug: nodejs
seo_title: Exports de Modules Node Expliqués – Avec des Exemples de Fonctions d'Exportation
  JavaScript
seo_desc: 'By Stanley Nguyen

  One of the most powerful things about software development is the ability to reuse
  and build upon the foundations of other people. This code sharing has helped software
  progress at an amazing rate.

  Such a wonderful mechanism is crit...'
---

Par Stanley Nguyen

L'une des choses les plus puissantes du développement logiciel est la capacité de réutiliser et de construire sur les fondations des autres. Ce partage de code a aidé le logiciel à progresser à un rythme incroyable.

Un mécanisme aussi merveilleux est crucial à un niveau micro pour les projets individuels et les équipes.

Pour Node.js, ce processus de partage de code – à la fois au sein des projets individuels et dans les dépendances npm externes – est facilité en utilisant `module.exports` ou `exports`.

# Comment fonctionnent les Modules Node

Comment utilisons-nous les exports de modules pour brancher un module externe, ou diviser judicieusement notre projet en plusieurs fichiers (modules) ?

Le système de modules Node.js a été créé parce que ses concepteurs ne voulaient pas qu'il souffre du même problème de portée globale brisée, comme son homologue navigateur. Ils ont implémenté la [spécification CommonJS](https://en.wikipedia.org/wiki/CommonJS) pour y parvenir.

Les deux pièces importantes du puzzle sont `module.exports` et la fonction `require`.

## Comment fonctionne module.exports

`module.exports` est en fait une propriété de l'objet `module`. Voici à quoi ressemble l'objet `module` lorsque nous faisons `console.log(module)` :

```bash
Module {
  id: '.',
  path: '/Users/stanleynguyen/Documents/Projects/blog.stanleynguyen.me',
  exports: {},
  parent: null,
  filename: '/Users/stanleynguyen/Documents/Projects/blog.stanleynguyen.me/index.js',
  loaded: false,
  children: [],
  paths: [
    '/Users/stanleynguyen/Documents/Projects/blog.stanleynguyen.me/node_modules',
    '/Users/stanleynguyen/Documents/Projects/node_modules',
    '/Users/stanleynguyen/Documents/node_modules',
    '/Users/stanleynguyen/node_modules',
    '/Users/node_modules',
    '/node_modules'
  ]
}

```

L'objet ci-dessus décrit essentiellement un module encapsulé à partir d'un fichier JS avec `module.exports` étant le composant exporté de n'importe quel type - objet, fonction, chaîne, etc. L'exportation par défaut dans un module Node.js est aussi simple que ceci :

```js
module.exports = function anExportedFunc() {
  return "yup simple as that";
};

```

Il existe une autre façon d'exporter à partir d'un module Node.js appelée "exportation nommée". Au lieu d'assigner tout `module.exports` à une valeur, nous assignons des propriétés individuelles de l'objet `module.exports` par défaut à des valeurs. Quelque chose comme ceci :

```js
module.exports.anExportedFunc = () => {};
module.exports.anExportedString = "this string is exported";

// ou regroupées ensemble dans un objet
module.exports = {
  anExportedFunc,
  anExportedString,
};

```

L'exportation nommée peut également être faite de manière plus concise avec la variable prédéfinie `exports` de portée de module, comme ceci :

```js
exports.anExportedFunc = () => {};
exports.anExportedString = "this string is exported";

```

Cependant, assigner toute la variable `exports` à une nouvelle valeur ne fonctionnera pas (nous discuterons pourquoi dans une section ultérieure), et cela confond souvent les développeurs Node.js.

```js
// Cela ne fonctionnera pas comme nous pourrions nous y attendre
exports = {
  anExportedFunc,
  anExportedString,
};

```

Imaginez que les exports de modules Node.js sont des conteneurs d'expédition, avec `module.exports` et `exports` comme du personnel portuaire à qui nous dirions quel "navire" (c'est-à-dire, valeurs) que nous voulons envoyer à un "port étranger" (un autre module dans le projet).

Eh bien, "l'exportation par défaut" serait dire à `module.exports` quel "navire" faire naviguer tandis que "l'exportation nommée" serait charger différents conteneurs sur le navire que `module.exports` va faire naviguer.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/ship-analogy.png)
_Mon analogie "navire amiral" pour le rôle de module.exports de Node.js_

Maintenant que nous avons envoyé les navires naviguer, comment nos "ports étrangers" récupèrent-ils le navire exporté ?

## Comment fonctionne le mot-clé require de Node.js

À l'extrémité de réception, les modules Node.js peuvent importer en `require`-ant la valeur exportée.

Disons que ceci était écrit dans `ship.js` :

```js
...
module.exports = {
  containerA,
  containerB,
};

```

Nous pouvons facilement importer le "navire" dans notre `receiving-port.js` :

```js
// importer le navire entier en tant que variable unique
const ship = require("./ship.js");
console.log(ship.containerA);
console.log(ship.containerB);
// ou importer directement les conteneurs via la destructuration d'objet
const { containerA, containerB } = require("./ship.js");
console.log(containerA);
console.log(containerB);

```

Un point important à noter sur cet opérateur de port étranger – `require` – est que la personne insiste pour recevoir des navires qui ont été **envoyés par `module.exports` de l'autre côté de la mer**. Cela nous amène à la section suivante où nous aborderons un point de confusion courant.

## `module.exports` vs `exports` – Quelle est la différence et lequel utiliser quand ?

Maintenant que nous avons parcouru les bases de l'exportation et de l'importation de modules, il est temps d'aborder l'une des sources courantes de confusion dans les modules Node.js.

Il s'agit d'une erreur courante d'exportation de modules que les personnes qui commencent avec Node.js font souvent. Elles assignent `exports` à une nouvelle valeur, pensant que c'est la même chose que "l'exportation par défaut" via `module.exports`.

Cependant, cela ne fonctionnera pas parce que :

* `require` n'utilisera que la valeur de `module.exports`
* `exports` est une variable de portée de module qui fait référence à `module.exports` initialement

Ainsi, en assignant `exports` à une nouvelle valeur, nous pointons effectivement la valeur de `exports` vers une autre référence, loin de la référence initiale au même objet que `module.exports`.

Si vous souhaitez en savoir plus sur cette explication technique, [la documentation officielle de Node.js](https://nodejs.org/api/modules.html#modules_exports_shortcut) est un bon point de départ.

Revenons à l'analogie que nous avons faite précédemment en utilisant des navires et des opérateurs : `exports` est un autre personnel portuaire que nous pourrions informer sur le navire sortant. Au début, `module.exports` et `exports` ont la même information sur le navire "sortant".

Mais que se passe-t-il si nous disons à `exports` que le navire sortant sera un autre (c'est-à-dire, assigner `exports` à une valeur complètement nouvelle) ? Ensuite, tout ce que nous leur disons par la suite (comme assigner des propriétés de `exports` à des valeurs) ne sera pas sur le navire que `module.exports` fait réellement naviguer pour être reçu par `require`.

D'un autre côté, si nous disons seulement à `exports` de "charger quelques conteneurs sur le navire sortant" (assigner des propriétés de `exports` à une valeur), nous finirions effectivement par charger des "conteneurs" (c'est-à-dire, valeur de propriété) sur le navire qui est réellement en train de naviguer.

Sur la base de l'erreur courante expliquée ci-dessus, nous pourrions certainement développer de bonnes conventions autour de l'utilisation des modules CommonJS dans Node.js.

## Bonnes pratiques d'exportation Node.js – une stratégie sensée

Bien sûr, la convention offerte ci-dessous est entièrement basée sur mes propres évaluations et raisonnements. Si vous avez un argument plus solide pour une alternative, n'hésitez pas à me tweeter [@stanley_ngn](https://twitter.com/stanley_ngn).

Les principales choses que je veux atteindre avec cette convention sont :

* éliminer la confusion autour de `exports` vs `module.exports`
* faciliter la lecture et augmenter la lisibilité en ce qui concerne l'exportation de modules

Je propose donc de consolider les valeurs exportées en bas du fichier comme ceci :

```js
// exportation par défaut
module.exports = function defaultExportedFunction() {};
// exportation nommée
module.exports = {
  something,
  anotherThing,
};

```

Faire cela éliminerait tout inconvénient en termes de concision que `module.exports` a par rapport à `exports` en abrégé. Cela supprimerait toutes les incitations à utiliser `exports`, qui est confus et potentiellement nuisible.

Cette pratique rendrait également très facile pour les lecteurs de code de jeter un coup d'œil et d'apprendre sur les valeurs exportées d'un module spécifique.

## Aller au-delà de CommonJS

Il existe un nouveau standard, et meilleur (bien sûr !) qui a été récemment introduit dans Node.js appelé `modules ECMAScript`. Les [modules ECMAScript](https://nodejs.org/api/esm.html) n'étaient disponibles que dans le code nécessitant une transpilation de [Babel](https://babeljs.io/), ou dans le cadre d'une fonctionnalité expérimentale dans Node.js version 12 ou antérieure.

C'est une manière assez simple et élégante de gérer l'exportation de modules. L'essentiel peut être résumé avec l'exportation par défaut étant :

```js
export default function exportedFunction() {}

```

et l'exportation nommée ressemblant à ceci :

```js
// exportations nommées sur des LOC séparées
export const constantString = "CONSTANT_STRING";
export const constantNumber = 5;
// exportations nommées consolidées
export default {
  constantString,
  constantNumber,
};

```

Ces valeurs peuvent ensuite être facilement importées à l'extrémité de réception, comme ceci :

```js
// valeur exportée par défaut
import exportedFunction from "exporting-module.js";
// importer des valeurs exportées nommées via la destructuration d'objet
import { constantString, constantNumber } from "exporting-module.js";

```

Cela élimine toute confusion entre `module.exports` et `exports` et offre une syntaxe agréable et naturelle !

Il existe définitivement des projets qui n'ont pas encore été migrés vers Node.js version 14 et supérieures et qui ne peuvent donc pas utiliser cette nouvelle syntaxe.

Cependant, si vous en avez l'occasion (parce que vous commencez un nouveau projet, ou que votre projet a été migré avec succès vers Node.js 14 et supérieures), il n'y a aucune raison de ne pas passer à cette manière futuriste et géniale de faire les choses.

### Merci d'avoir lu !

Enfin, si vous aimez mes écrits, rendez-vous sur [mon blog](https://blog.stanleynguyen.me/) pour des commentaires similaires et suivez [moi sur Twitter](https://twitter.com/stanley_ngn). 🎉
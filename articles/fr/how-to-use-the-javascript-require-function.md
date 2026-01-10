---
title: JavaScript Require – Comment utiliser la fonction require() en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-01-31T00:07:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-javascript-require-function
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/cover-template--11-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Require – Comment utiliser la fonction require() en JS
seo_desc: 'In JavaScript, modules refer to a file that holds JavaScript code which
  performs a specific purpose.

  Modules are self-contained, making it easy to add, remove, and update functionalities
  without affecting your entire code because they are decoupled f...'
---

En JavaScript, les modules font référence à un fichier qui contient du code JavaScript exécutant une fonction spécifique.

Les modules sont autonomes, ce qui facilite l'ajout, la suppression et la mise à jour de fonctionnalités sans affecter l'ensemble de votre code, car ils sont découplés des autres parties du code.

Lorsque vous avez ces modules dans des fichiers JavaScript séparés, vous souhaiterez les utiliser dans le fichier JavaScript d'origine.

Dans cet article, vous apprendrez ce que fait la fonction `require()`, comment vous pouvez l'utiliser et quelques différences distinctes entre les fonctions require et import.

Pendant longtemps, le système de modules CommonJS a été le système de modules par défaut dans l'écosystème Node.js. Mais un nouveau système de modules a été introduit dans [Node.js v8.5.0](https://github.com/nodejs/node/blob/master/doc/changelogs/CHANGELOG_V8.md#8.5.0), qui est le système de modules ES.

Les modules CommonJS et ECMAScript (modules ES) fonctionnent désormais parfaitement dans Node.js. La principale différence entre eux est leur exécution.

## Comment exécuter les modules CommonJS et ES

Dans le navigateur, l'exécution des modules JavaScript dépend des instructions `import` et `export`. Ces instructions chargent et exportent les modules ES, respectivement. C'est la méthode standard et officielle pour réutiliser les modules en JavaScript, et c'est ce que la plupart des navigateurs web supportent nativement.

Node.js, par défaut, supporte le format de module CommonJS, qui charge les modules en utilisant la fonction `require()`, et les exporte avec `module.exports`.

## Qu'est-ce que la fonction require() de JavaScript ?

La fonction `require()` est une fonction de module CommonJS intégrée, supportée dans Node.js, qui vous permet d'inclure des modules dans votre projet. Cela est dû au fait que, par défaut, Node.js traite le code JavaScript comme des modules CommonJS.

### Comment utiliser la fonction require() en JS

La fonction `require()` est simple à utiliser et à comprendre, car tout ce que vous avez à faire est d'assigner la fonction à une variable.

Dans cette fonction, vous passerez le nom de l'emplacement comme argument. Voici la syntaxe générale :

```js
const varName = require(locationName);
```

Supposons que vous avez un module CommonJS qui exporte une fonction `*getFullName*` comme vu ci-dessous :

```js
// utils.js
const getFullName = (firstname, lastName) => {
    return `My fullname is ${firstname} ${lastName}`;
};
module.exports = getFullName;
```

Ensuite, vous pouvez utiliser la fonction require() pour utiliser/inclure ce module dans votre fichier JavaScript :

```js
// index.js
const getFullName = require('./utils.js');
console.log(getFullName('John', 'Doe')); // My fullname is John Doe
```

Le module est situé dans un fichier local dans le code ci-dessus, c'est pourquoi l'adresse locale est référencée en utilisant le nom du fichier.

Mais dans une situation où vous souhaitez inclure un module externe depuis le web, vous utilisez alors l'emplacement basé sur le web :

```js
const myVar = require('http://web-module.location');
```

## Fonctions require() vs import()

Les fonctions/instructions require et import sont utilisées pour inclure des modules dans votre fichier JavaScript, mais elles possèdent quelques différences. Les deux principales différences sont :

* La fonction require() peut être appelée depuis n'importe où dans le programme, alors que import() ne peut pas être appelée conditionnellement. Elle s'exécute toujours au début du fichier.

* Pour inclure un module avec la fonction require(), ce module doit être enregistré avec une extension .js au lieu de .mjs lorsque l'instruction import() est utilisée.

## Conclusion

Dans cet article, vous avez appris ce que fait la fonction require(), comment elle fonctionne et quand vous pouvez l'utiliser dans Node.js.

Il est crucial de comprendre que l'instruction import n'est autorisée que dans les modules ES et ne peut pas être utilisée dans des scripts intégrés sans l'attribut `type="module"`. De plus, pour utiliser les modules ES dans Node.js, vous devez enregistrer ces modules avec une extension .mjs :

```js
// utils.mjs
export const getFullName = (firstname, lastName) => {
    return `my fullname is ${firstname} ${lastName}`;
};

// index.js
import { getFullName } from './utils.mjs';
console.log(getFullName('John', 'Doe')); // My fullname is John Doe
```

Amusez-vous bien en codant !

Vous pouvez accéder à plus de 180 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.
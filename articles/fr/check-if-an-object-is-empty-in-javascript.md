---
title: Comment vérifier si un objet est vide en JavaScript – Équivalent JS Java isEmpty
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-28T15:29:23.000Z'
originalURL: https://freecodecamp.org/news/check-if-an-object-is-empty-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover-template--21-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment vérifier si un objet est vide en JavaScript – Équivalent JS Java
  isEmpty
seo_desc: "An object is one of the most commonly used data types in programming. An\
  \ object is a collection of related data stored as key-value pairs. For example:\n\
  let userDetails = {\n  name: \"John Doe\",\n  username: \"jonnydoe\",\n  age: 14,\n\
  }\n\nWhen working with ob..."
---

Un objet est l'un des types de données les plus couramment utilisés en programmation. Un objet est une collection de données liées stockées sous forme de paires clé-valeur. Par exemple :

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14,
}
```

Lorsque vous travaillez avec des objets, vous pouvez avoir besoin de vérifier si un objet est vide avant d'exécuter une fonction.

En JavaScript, il existe diverses façons de vérifier si un objet est vide. Dans cet article, vous apprendrez les différentes méthodes pour le faire, les options qui peuvent être attachées, et pourquoi.

**Note :** Un objet est considéré comme vide lorsqu'il n'a aucune paire clé-valeur.

Au cas où vous seriez pressé, voici un exemple de base :

```js
const myEmptyObj = {};

// Fonctionne mieux avec les nouveaux navigateurs
Object.keys(myEmptyObj).length === 0 && myEmptyObj.constructor === Object

// Fonctionne avec tous les navigateurs
_.isEmpty(myEmptyObj)
```

Les deux méthodes retourneront `true`. Comprenons maintenant ces méthodes et d'autres options que vous pouvez utiliser pour vérifier si un objet est vide en JavaScript.

## Comment vérifier si un objet est vide avec `Object.keys()`

La méthode `Object.keys()` est une méthode statique d'objet introduite dans ECMAScript6 (ES6) et est prise en charge dans tous les navigateurs modernes. Cette méthode retourne un tableau avec les clés d'un objet. Par exemple :

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

console.log(Object.keys(userDetails)); // ["name","username","age"]
```

Avec cela, vous pouvez maintenant appliquer la propriété `.length`. Si elle retourne zéro (0), l'objet est vide.

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};

console.log(Object.keys(userDetails).length); // 3
console.log(Object.keys(myEmptyObj).length); // 0
```

Vous pouvez maintenant utiliser cette méthode pour vérifier si un objet est vide avec une instruction if ou créer une fonction qui vérifie.

```js
const isObjectEmpty = (objectName) => {
  return Object.keys(objectName).length === 0
}
```

Cela retournera soit `true` soit `false`. Si l'objet est vide, il retournera `true`, sinon, il retournera `false`.

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};

const isObjectEmpty = (objectName) => {
  return Object.keys(objectName).length === 0
}

console.log(isObjectEmpty(userDetails)); // false
console.log(isObjectEmpty(myEmptyObj)); // true
```

**Note :** Vérifier la longueur seule n'est pas la meilleure option lorsque vous vérifiez si un objet est vide ou pour tout type de données. Il est toujours préférable de confirmer si le type de données est correct.

Pour ce faire, vous pouvez utiliser la vérification du constructeur :

```js
const isObjectEmpty = (objectName) => {
  return Object.keys(objectName).length === 0 && objectName.constructor === Object;
}
```

De cette manière, vous êtes susceptible d'obtenir une vérification plus approfondie.

Jusqu'à présent, tout a bien fonctionné. Mais vous pouvez également vouloir éviter de lancer une `TypeError` lorsqu'une variable est `undefined` ou qu'une valeur de `null` est passée au lieu de `{}`.

Pour corriger cela, vous pouvez ajouter une vérification supplémentaire :

```js
const isObjectEmpty = (objectName) => {
  return (
    objectName &&
    Object.keys(objectName).length === 0 &&
    objectName.constructor === Object
  );
};
```

Dans le code ci-dessus, une vérification supplémentaire est ajoutée. Cela signifie qu'il retournera soit `null` soit `undefined` si ce n'est pas un objet vide, comme le montre l'exemple ci-dessous :

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};
let nullObj = null;
let undefinedObj;

const isObjectEmpty = (objectName) => {
  return (
    objectName &&
    Object.keys(objectName).length === 0 &&
    objectName.constructor === Object
  );
};

console.log(isObjectEmpty(userDetails)); // false
console.log(isObjectEmpty(myEmptyObj)); // true
console.log(isObjectEmpty(undefinedObj)); // undefined
console.log(isObjectEmpty(nullObj)); // null
```

**Note :** Cela s'applique à d'autres méthodes statiques d'objet, ce qui signifie que vous pouvez utiliser `Object.entries()` ou `Object.values()` au lieu de `Object.keys()`.

## Comment vérifier si un objet est vide avec une boucle `for...in`

Une autre méthode que vous pouvez utiliser est la boucle `for...in` ES6. Vous pouvez utiliser cette boucle avec la méthode `hasOwnProperty()`.

```js
const isObjectEmpty = (objectName) => {
  for (let prop in objectName) {
    if (objectName.hasOwnProperty(prop)) {
      return false;
    }
  }
  return true;
};
```

La méthode ci-dessus parcourra chaque propriété de l'objet. Si elle trouve une seule itération, l'objet n'est pas vide. De plus, `hasOwnProperty()` retournera un booléen indiquant si l'objet possède la propriété spécifiée comme sa propriété.

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};

const isObjectEmpty = (objectName) => {
  for (let prop in objectName) {
    if (objectName.hasOwnProperty(prop)) {
      return false;
    }
  }
  return true;
};

console.log(isObjectEmpty(userDetails)); // false
console.log(isObjectEmpty(myEmptyObj)); // true
```

## Comment vérifier si un objet est vide avec `JSON.stringify()`

Vous pouvez également utiliser la méthode `JSON.stringify()`, qui est utilisée pour convertir une valeur JavaScript en une chaîne JSON. Cela signifie qu'elle convertira vos valeurs d'objet en une chaîne de l'objet. Par exemple :

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

console.log(JSON.stringify(userDetails));

Sortie :
"{'name':'John Doe','username':'jonnydoe','age':14}"
```

Cela signifie que lorsqu'il s'agit d'un objet vide, il retournera `"{}"`. Vous pouvez utiliser cela pour vérifier un objet vide.

```js
const isObjectEmpty = (objectName) => {
  return JSON.stringify(objectName) === "{}";
};
```

Cela retournera `true` si l'objet est vide, sinon `false` :

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};

const isObjectEmpty = (objectName) => {
  return JSON.stringify(objectName) === "{}";
};

console.log(isObjectEmpty(userDetails)); // false
console.log(isObjectEmpty(myEmptyObj)); // true
```

## Comment vérifier si un objet est vide avec Lodash

Enfin, certaines des méthodes que j'ai expliquées ici peuvent fonctionner pour les anciennes versions de navigateurs, tandis que d'autres peuvent ne pas fonctionner. Si vous êtes préoccupé par une solution qui fonctionnera pour les anciennes et les modernes versions de navigateurs, vous pouvez utiliser [Lodash](https://lodash.com/).

Lodash est une bibliothèque utilitaire JavaScript moderne qui peut effectuer de nombreuses fonctionnalités JavaScript avec une syntaxe très basique.

Par exemple, si vous voulez vérifier si un objet est vide, vous n'avez besoin que de la méthode "isEmpty".

```js
_.isEmpty(objectName);
```

L'installation de Lodash dans votre projet est assez facile. Tout ce que vous avez à faire est d'utiliser cette commande :

```js
$ npm install lodash
```

Vous pouvez maintenant initialiser la méthode underscore et utiliser cette méthode.

```js
const _ = require('lodash');

let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};

const isObjectEmpty = (objectName) => {
  return _.isEmpty(objectName);
};

console.log(isObjectEmpty(userDetails)); // false
console.log(isObjectEmpty(myEmptyObj)); // true
```

## C'est tout ! 💪

J'ai apprécié explorer les différentes façons de vérifier si un objet est vide. N'hésitez pas à utiliser la meilleure méthode qui convient à votre projet ou tâche.

Amusez-vous bien en codant !

Embarquez dans un voyage d'apprentissage ! [Parcourez 200+ articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.
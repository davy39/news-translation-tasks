---
title: JS Copier un Objet – Comment Cloner un Objet en JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-11T17:13:52.000Z'
originalURL: https://freecodecamp.org/news/clone-an-object-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover-template--20-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JS Copier un Objet – Comment Cloner un Objet en JavaScript
seo_desc: "A JavaScript object is a collection of key-value pairs. It is a non-primitive\
  \ data type that can contain various data types. For example:\nconst userDetails\
  \ = {\n  name: \"John Doe\",\n  age: 14,\n  verified: false\n};\n\nWhen working\
  \ with objects in JavaScri..."
---

Un objet JavaScript est une collection de paires clé-valeur. Il s'agit d'un type de données non primitif qui peut contenir divers types de données. Par exemple :

```js
const userDetails = {
  name: "John Doe",
  age: 14,
  verified: false
};
```

Lorsque vous travaillez avec des objets en JavaScript, vous pouvez parfois vouloir modifier la valeur ou ajouter une nouvelle propriété à l'objet.

Dans certains scénarios, avant de mettre à jour ou d'ajouter de nouvelles propriétés, vous voudrez créer un nouvel objet et copier ou cloner la valeur de l'original.

Par exemple, si vous voulez copier la valeur de l'objet `userDetails` puis changer le nom en quelque chose de différent. Dans le sens typique, vous voudrez utiliser l'opérateur d'égalité (=).

```js
const newUser = userDetails;
console.log(newUser); // {name: 'John Doe', age: 14, verified: false}
```

Tout semble encore bien, mais voyons ce qui se passe si nous modifions notre deuxième objet :

```js
const newUser = userDetails;
newUser.name = "Jane Doe";

console.log(newUser); // {name: 'Jane Doe', age: 14, verified: false}
```

Tout est bien avec le nouvel objet, mais si vous essayez de vérifier les valeurs de votre objet original, vous remarquerez qu'il est affecté. Pourquoi ? Comment ?

```js
console.log(userDetails); // {name: 'Jane Doe', age: 14, verified: false}
```

C'est le problème. L'objet original est affecté parce que les objets sont des **types de référence**. Cela signifie que toute valeur que vous stockez soit dans le clone ou l'objet original pointe vers le même objet.

Ce n'est pas ce que vous voulez. Vous voulez stocker la valeur d'un objet dans un nouvel objet et manipuler la valeur dans le nouvel objet sans affecter le tableau original.

Dans cet article, vous apprendrez trois méthodes que vous pouvez utiliser pour faire cela. Vous apprendrez également ce que signifient les clones profonds et superficiels et comment ils fonctionnent.

Au cas où vous seriez pressé, voici les trois méthodes et un exemple de leur fonctionnement.

```js
// Méthode Spread
let clone = { ...userDetails }

// Méthode Object.assign()
let clone = Object.assign({}, userDetails)

// Méthode JSON.parse()
let clone = JSON.parse(JSON.stringify(userDetails))
```

Si vous n'êtes pas pressé, commençons.

## Comment Cloner un Objet en JavaScript avec l'Opérateur Spread

L'opérateur spread a été introduit dans ES6 et peut étendre les valeurs dans un objet avec les trois points devant.

```js
// Déclaration de l'objet
const userDetails = {
  name: "John Doe",
  age: 14,
  verified: false
};

// Clonage de l'objet avec l'opérateur Spread
let cloneUser = { ...userDetails };

console.log(cloneUser); // {name: 'John Doe', age: 14, verified: false}
```

Cela n'est plus référencé, ce qui signifie que la modification de la valeur de l'objet n'affectera pas l'objet original.

```js
// Clonage de l'objet avec l'opérateur Spread
let cloneUser = { ...userDetails };

// changement de la valeur de cloneUser
cloneUser.name = "Jane Doe"

console.log(cloneUser.name); // 'Jane Doe'
console.log(cloneUser); // {name: 'Jane Doe', age: 14, verified: false}
```

Lorsque vous vérifiez la valeur du nom dans l'objet original ou l'objet entier, vous remarquerez qu'il n'est pas affecté.

```js
console.log(userDetails.name); // 'John Doe'
console.log(userDetails); // {name: 'John Doe', age: 14, verified: false}
```

**Note :** Vous ne pouvez utiliser la syntaxe spread que pour faire une copie superficielle d'un objet tandis que les objets plus profonds sont référencés. Vous comprendrez lorsque nous arriverons à la dernière section de cet article.

## Comment Cloner un Objet en JavaScript avec `Object.assign()`

Une alternative à l'opérateur spread est la méthode `Object.assign()`. Vous utilisez cette méthode pour copier les valeurs et les propriétés d'un ou plusieurs objets sources vers un objet cible.

```js
// Déclaration de l'objet
const userDetails = {
  name: "John Doe",
  age: 14,
  verified: false
};

// Clonage de l'objet avec la méthode Object.assign()
let cloneUser = Object.assign({}, userDetails);

console.log(cloneUser); // {name: 'John Doe', age: 14, verified: false}
```

Cela n'est plus référencé, ce qui signifie que la modification de la valeur de l'objet n'affectera pas l'objet original.

```js
// Clonage de l'objet avec la méthode Object.assign()
let cloneUser = Object.assign({}, userDetails);

// changement de la valeur de cloneUser
cloneUser.name = "Jane Doe"

console.log(cloneUser.name); // 'Jane Doe'
console.log(cloneUser); // {name: 'Jane Doe', age: 14, verified: false}
```

Lorsque vous vérifiez la valeur du nom dans l'objet original ou l'objet entier, vous remarquerez qu'il n'est pas affecté.

```js
console.log(userDetails.name); // 'John Doe'
console.log(userDetails); // {name: 'John Doe', age: 14, verified: false}
```

**Note :** Vous ne pouvez utiliser la méthode `Object.assign()` que pour faire une copie superficielle d'un objet tandis que les objets plus profonds sont référencés. Vous comprendrez lorsque nous arriverons à la dernière section de cet article.

## Comment Cloner un Objet avec `JSON.parse()`

La méthode finale est JSON.parse(). Vous utiliserez cette méthode avec `JSON.stringify()`. Vous pouvez l'utiliser pour cloner profondément, mais elle a quelques inconvénients. D'abord, voyons comment cela fonctionne.

```js
// Déclaration de l'objet
const userDetails = {
  name: "John Doe",
  age: 14,
  verified: false
};

// Clonage de l'objet avec la méthode JSON.parse()
let cloneUser = JSON.parse(JSON.stringify(userDetails));

console.log(cloneUser); // {name: 'John Doe', age: 14, verified: false}
```

De plus, tout comme les méthodes précédentes, cela n'est plus référencé. Cela signifie que vous pouvez changer une valeur dans le nouvel objet sans affecter l'objet original.

```js
// Clonage de l'objet avec la méthode JSON.parse()
let cloneUser = JSON.parse(JSON.stringify(userDetails));

// changement de la valeur de cloneUser
cloneUser.name = "Jane Doe"

console.log(cloneUser.name); // 'Jane Doe'
console.log(cloneUser); // {name: 'Jane Doe', age: 14, verified: false}
```

Lorsque vous vérifiez la valeur du nom dans l'objet original ou l'objet entier, vous remarquerez qu'il n'est pas affecté.

```js
console.log(userDetails.name); // 'John Doe'
console.log(userDetails); // {name: 'John Doe', age: 14, verified: false}
```

**Note :** Cette méthode peut être utilisée pour le clonage profond mais ne sera pas la meilleure option car elle ne fonctionne pas avec les propriétés `function` ou `symbol`.

Explorons maintenant le clonage superficiel et profond et comment vous pouvez utiliser la méthode `JSON.parse()` pour effectuer un clonage profond. Vous apprendrez également pourquoi ce n'est pas la meilleure option.

## Clone Superficiel vs Clone Profond

Jusqu'à présent, l'exemple utilisé dans cet article est un objet de base avec un seul niveau. Cela signifie que nous n'avons effectué que des clones superficiels. Mais lorsqu'un objet a plus d'un niveau, vous devrez alors effectuer un clone profond.

```js
// Objet superficiel
const userDetails = {
  name: "John Doe",
  age: 14,
  verified: false
};

// Objet profond
const userDetails = {
  name: "John Doe",
  age: 14,
  status: {
    verified: false,
  }
};
```

Remarquez que l'objet profond a plus d'un niveau car il y a un autre objet dans l'objet `userDetails`. Un objet profond peut avoir autant de niveaux que vous le souhaitez.

**Note :** Lorsque vous utilisez l'opérateur spread ou la méthode `Object.assign()` pour cloner un objet profond, les objets plus profonds seront référencés.

```js
const userDetails = {
  name: "John Doe",
  age: 14,
  status: {
    verified: false
  }
};

// Clonage de l'objet avec l'opérateur Spread
let cloneUser = { ...userDetails };

// Changement de la valeur de cloneUser
cloneUser.status.verified = true;

console.log(cloneUser); // {name: 'John Doe', age: 14, status: {verified: true}}
console.log(userDetails); // {name: 'John Doe', age: 14, status: {verified: true}}
```

Vous remarquerez que les objets original et nouveau sont affectés car lorsque vous utilisez l'opérateur spread ou la méthode `Object.assign()` pour cloner un objet profond, les objets plus profonds seront référencés.

### Comment pouvez-vous corriger ce problème

Vous pouvez utiliser la méthode `JSON.parse()`, et tout fonctionnera bien.

```js
const userDetails = {
  name: "John Doe",
  age: 14,
  status: {
    verified: false
  }
};

// Clonage de l'objet avec l'opérateur Spread
let cloneUser = JSON.parse(JSON.stringify(userDetails));

// Changement de la valeur de cloneUser
cloneUser.status.verified = true;

console.log(cloneUser); // {name: 'John Doe', age: 14, status: {verified: true}}
console.log(userDetails); // {name: 'John Doe', age: 14, status: {verified: false}}
```

Mais il y a un problème avec cette méthode. Le problème est que vous pouvez perdre vos données. Comment ?

`JSON.stringify()` fonctionne très bien avec les types de données primitifs comme les nombres, les chaînes ou les booléens, et c'est ce que vous avez vu dans nos exemples précédents. Mais parfois, `JSON.stringify()` est imprévisible si vous n'êtes pas conscient de certaines valeurs et de la manière dont il les gère.

Par exemple, il ne fonctionne pas avec les fonctions, les symboles ou les valeurs `undefined`. Il change également d'autres valeurs comme `Nan` et `Infinity` en `null`, ce qui casse votre code. Lorsque vous avez une fonction, un symbole ou une valeur undefined, il retournera une paire clé-valeur vide et la sautera.

```js
const userDetails = {
  name: "John Doe",
  age: 14,
  status: {
    verified: false,
    method: Symbol(),
    title: undefined
  }
};

// Clonage de l'objet avec l'opérateur Spread
let cloneUser = JSON.parse(JSON.stringify(userDetails));
```

Tout semble fonctionner bien, mais pour le nouvel objet, `JSON.stringify()` ne retournera aucune paire clé-valeur pour les valeurs undefined et symbol.

```js
console.log(cloneUser); 

// Output
{
  name: "John Doe",
  age: 14,
  status: {
    verified: false
  }
};
```

Cela signifie que vous devez être prudent. La meilleure option pour implémenter le clonage profond sera d'utiliser [Lodash](https://lodash.com/docs/#cloneDeep). Vous pouvez alors être sûr que aucune de vos données ne sera perdue.

```js
const userDetails = {
  name: "John Doe",
  age: 14,
  status: {
    verified: false,
    method: Symbol(),
    title: undefined
  }
};

console.log(_.cloneDeep(userDetails));
```

## Conclusion !

Cet article vous a appris comment cloner un objet en JavaScript en utilisant trois méthodes principales. Vous avez vu comment ces méthodes fonctionnent et quand utiliser chacune d'elles. Vous avez également appris le clonage profond.

Vous pouvez lire [cet article](https://medium.com/@pmzubar/why-json-parse-json-stringify-is-a-bad-practice-to-clone-an-object-in-javascript-b28ac5e36521) pour comprendre pourquoi `JSON.parse(JSON.stringify())` est une mauvaise pratique pour cloner un objet en JavaScript.

Amusez-vous bien à coder !
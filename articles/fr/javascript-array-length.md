---
title: Longueur des tableaux JavaScript expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-12T17:56:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-length
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9df3740569d1a4ca3a91.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Longueur des tableaux JavaScript expliquée
seo_desc: 'length is a property of arrays in JavaScript that returns or sets the number
  of elements in a given array.

  The length property of an array can be returned like so.

  let desserts = ["Cake", "Pie", "Brownies"];

  console.log(desserts.length); // 3


  The as...'
---

`length` est une propriété des tableaux en JavaScript qui retourne ou définit le nombre d'éléments dans un tableau donné.

La propriété `length` d'un tableau peut être retournée comme suit.

```js
let desserts = ["Cake", "Pie", "Brownies"];
console.log(desserts.length); // 3
```

L'opérateur d'assignation, en conjonction avec la propriété `length`, peut être utilisé pour définir le nombre d'éléments dans un tableau comme suit.

```js
let cars = ["Saab", "BMW", "Volvo"];
cars.length = 2;
console.log(cars.length); // 2
```

## Plus d'informations sur les tableaux :

### Méthode isArray()

La méthode `Array.isArray()` retourne `true` si un objet est un tableau, `false` si ce n'est pas le cas.

**Syntaxe :**

```text
Array.isArray(obj)
```

**Paramètres :**

**obj** L'objet à vérifier.

[Lien MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray) | [Lien MSDN](https://msdn.microsoft.com/en-us/LIBRary/ff848265%28v=vs.94%29.aspx)

**Exemples :**

```text
// tous les appels suivants retournent true
Array.isArray([]);
Array.isArray([1]);
Array.isArray(new Array());
// Peu connu : Array.prototype lui-même est un tableau :
Array.isArray(Array.prototype); 

// tous les appels suivants retournent false
Array.isArray();
Array.isArray({});
Array.isArray(null);
Array.isArray(undefined);
Array.isArray(17);
Array.isArray('Array');
Array.isArray(true);
Array.isArray(false);
Array.isArray({ __proto__: Array.prototype });
```

### Array.prototype.forEach

La méthode de tableau forEach est utilisée pour itérer à travers chaque élément d'un tableau. La méthode est appelée sur l'objet Array et reçoit une fonction qui est appelée sur chaque élément du tableau.

```javascript
var arr = [1, 2, 3, 4, 5];

arr.forEach(number => console.log(number * 2));

// 2
// 4
// 6
// 8
// 10
```

La fonction de rappel peut également prendre un deuxième paramètre d'un index au cas où vous auriez besoin de référencer l'index de l'élément actuel dans le tableau.

```javascript
var arr = [1, 2, 3, 4, 5];

arr.forEach((number, i) => console.log(`${number} est à l'index ${i}`));

// '1 est à l'index 0'
// '2 est à l'index 1'
// '3 est à l'index 2'
// '4 est à l'index 3'
// '5 est à l'index 4'
```

## Lectures complémentaires sur les tableaux :

[array.prototype.filter](https://guide.freecodecamp.org/javascript/standard-objects/array/array-prototype-filter/)

[array.prototype.reduce](https://guide.freecodecamp.org/javascript/standard-objects/array/array-prototype-reduce/)
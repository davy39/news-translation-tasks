---
title: Le Guide Ultime des Méthodes de Tableaux JavaScript - Map
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-21T18:05:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-javascript-array-methods-map
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f23740569d1a4ca40fc.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Le Guide Ultime des Méthodes de Tableaux JavaScript - Map
seo_desc: "The map() method applies a function to each element in an array and returns\
  \ a copy of the original array with modified values (if any).\nSyntax:\nconst newArr\
  \ = oldArr.map(function(currentValue, index, array) {\n  // Do stuff with currentValue\
  \ (index an..."
---

La méthode `map()` applique une fonction à chaque élément d'un tableau et retourne une copie du tableau original avec des valeurs modifiées (le cas échéant).

## Syntaxe :

```js
const newArr = oldArr.map(function(currentValue, index, array) {
  // Faire des choses avec currentValue (index et array sont optionnels)
});
```

* `newArr` - le nouveau tableau qui est retourné
* `oldArr` - l'ancien tableau sur lequel on travaille. Ce tableau ne sera pas modifié
* `currentValue` - la valeur actuelle en cours de traitement
* `index` - l'index actuel de la valeur en cours de traitement
* `array` - le tableau original

## Exemples :

### ES5

```js
var arr = [1, 2, 3, 4];

var newArray = arr.map(function(element) {
  return element * 2
});

console.log(arr); // [1, 2, 3, 4]
console.log(newArray); // [2, 4, 6, 8]
```

### ES6

```js
const arr = [1, 2, 3, 4];

const newArray = arr.map(element => {
  return element * 2;
});

const newArrayOneLiner = arr.map(element => element * 2);

console.log(arr); // [1, 2, 3, 4]
console.log(newArray); // [2, 4, 6, 8]
console.log(newArrayOneLiner); // [2, 4, 6, 8]
```

## `map` vs `forEach`

À première vue, les méthodes `map()` et `forEach()` sont très similaires. Les deux méthodes parcourent un tableau et appliquent une fonction à chaque élément. La principale différence est que `map()` retourne un nouveau tableau, tandis que `forEach()` ne retourne rien.

Alors, quelle méthode devriez-vous utiliser ? En général, il est préférable d'utiliser `forEach()` si vous n'avez pas besoin de modifier les valeurs du tableau original. `forEach()` est un bon choix si tout ce que vous avez à faire est d'afficher chaque élément d'un tableau dans la console, ou de les enregistrer dans une base de données :

```js
const letters = ['a', 'b', 'c', 'd'];

letters.forEach(letter => {
  console.log(letter);
});
```

`map()` est un meilleur choix si vous devez mettre à jour les valeurs du tableau original. Il est particulièrement utile si vous souhaitez stocker le tableau mis à jour dans une variable et conserver l'original comme référence.

## Comment Utiliser `map` avec d'Autres Méthodes de Tableaux

Puisque `map()` retourne un tableau, vous pouvez l'utiliser avec d'autres méthodes de tableaux pour rendre votre code beaucoup plus concis et lisible.

### Utilisation de `map` avec `filter`

Une chose à retenir lors de l'utilisation de `map()` est qu'il applique une fonction à _chaque_ élément du tableau original et retourne un nouveau tableau de la même longueur que l'ancien. En d'autres termes, il n'est pas possible de sauter les éléments du tableau que vous ne souhaitez pas modifier :

```js
const nums = [5, 10, 15, 20];
const doublesOverTen = nums.map(num => {
  if (num > 10) {
    return num * 2;
  }
});

console.log(doublesOverTen); // [undefined, undefined, 30, 40]
```

C'est là que la méthode `filter()` intervient. `filter()` retourne un nouveau tableau d'éléments filtrés qui répondent à une certaine condition, auquel vous pouvez ensuite enchaîner `map()` :

```js
const nums = [5, 10, 15, 20];
const doublesOverTen = nums.filter(num => {
  return num > 10;
}).map(num => {
  return num * 2;
});

console.log(doublesOverTen); // [30, 40]
```

Ce code peut être simplifié encore davantage :

```js
const nums = [5, 10, 15, 20];
const doublesOverTen = nums.filter(num => num > 10).map(num => num * 2);

console.log(doublesOverTen); // [30, 40]
```

### Utilisation de `map` avec `reverse`

Il peut arriver que vous ayez besoin d'inverser un tableau tout en le parcourant avec `map`. La méthode `reverse()` facilite cela, mais il est important de se rappeler que, bien que `map()` soit immuable, `reverse()` ne l'est pas. En d'autres termes, la méthode `reverse()` modifiera le tableau original :

```js
const nums = [1, 2, 3, 4, 5];
const reversedDoubles = nums.reverse().map(num => num * 2);

console.log(nums); // [5, 4, 3, 2, 1]
console.log(reversedDoubles); // [10, 8, 6, 4, 2]
```

L'un des principaux avantages de `map()` est qu'il ne modifie pas le tableau original, et utiliser `reverse()` de cette manière va à l'encontre de ce principe. Cependant, il existe une solution simple : il suffit de se rappeler d'utiliser `map()` en premier, puis d'inverser le nouveau tableau qu'il retourne :

```js
const nums = [1, 2, 3, 4, 5];
const reversedDoubles = nums.map(num => num * 2).reverse();

console.log(nums); // [1, 2, 3, 4, 5]
console.log(reversedDoubles); // [10, 8, 6, 4, 2]
```

### Utilisation de `map` sur un Objet

Bien que `map()` soit conçu pour fonctionner sur des tableaux, avec un peu de travail supplémentaire, vous pouvez également parcourir des objets. `Object.keys()`, `Object.values()` et `Object.entries()` retournent tous un tableau, ce qui signifie que `map()` peut facilement être enchaîné à chaque méthode :

```js
const obj = { 
  a: 1, 
  b: 2, 
  c: 3 
}
const doubles = Object.values(obj).map(num => num * 2);

console.log(doubles); // [2, 4, 6]
```

Maintenant, allez de l'avant et utilisez `map()` pour tout !
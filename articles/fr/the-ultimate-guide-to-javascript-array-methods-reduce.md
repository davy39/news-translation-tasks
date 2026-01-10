---
title: Le guide ultime des méthodes de tableau JavaScript - Reduce
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-23T18:07:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-javascript-array-methods-reduce
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f19740569d1a4ca40cf.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Le guide ultime des méthodes de tableau JavaScript - Reduce
seo_desc: 'The reduce() method reduces an array of values down to just one value.
  The single value that is returned can be of any type.

  reduce() is like the Swiss Army knife of array methods. While others like map()
  and filter() provide specific functionality, ...'
---

La méthode `reduce()` réduit un tableau de valeurs à une seule valeur. La valeur unique qui est retournée peut être de n'importe quel type.

`reduce()` est comme le couteau suisse des méthodes de tableau. Alors que d'autres comme `map()` et `filter()` fournissent des fonctionnalités spécifiques, `reduce()` peut être utilisé pour transformer un tableau d'entrée en n'importe quelle sortie que vous désirez, tout en préservant le tableau original.

## Syntaxe

```js
const newValue = arr.reduce(function(accumulator, currentValue, index, array) {
  // Faire des choses avec accumulator et currentValue (index, array, et initialValue sont optionnels)
}, initialValue);
```

* `newValue` - le nouveau nombre, tableau, chaîne ou objet qui est retourné
* `arr` - le tableau sur lequel on opère
* `accumulator` - la valeur retournée de l'itération précédente
* `currentValue` - l'élément actuel dans le tableau
* `index` - l'index de l'élément actuel
* `array` - le tableau original sur lequel `reduce()` a été appelé
* `initialValue` - un nombre, tableau, chaîne ou objet qui sert de valeur initiale pour la sortie finale

## Exemples

### ES5

```js
var numbers = [1, 2, 3]; 

var sum = numbers.reduce(function(total, current) {
  return total + current;
}, 0);

console.log(numbers); // [1, 2, 3]
console.log(sum); // 6
```

### ES6

```js
const numbers = [1, 2, 3];

const sum = numbers.reduce((total, current) => {
  return total + current;
}, 0);

const sumOneLiner = numbers.reduce((total, current) => total + current, 0);

console.log(numbers); // [1, 2, 3]
console.log(sum); // 6
console.log(sumOneLiner); // 6
```

## Tout sur `initialValue`

### `initialValue` Fournie

L'argument `initialValue` est optionnel. Si fourni, il sera utilisé comme valeur initiale de l'accumulateur (`total`) dans le premier appel de la fonction de rappel :

```js
const numbers = [2, 3, 4];
const product = numbers.reduce((total, current) => {
  return total * current;
}, 1);

console.log(product); // 24
```

Puisque la valeur `initialValue` de 1 est fournie après la fonction de rappel, `reduce()` commence au début du tableau et définit le premier élément (2) comme valeur actuelle (`current`). Il parcourt ensuite le reste du tableau, mettant à jour la valeur de l'accumulateur et la valeur actuelle en cours de route.

### `initialValue` Omis

Si `initialValue` n'est pas fourni, l'itération commencera au deuxième élément du tableau (à l'index 1), avec `accumulator` égal au premier élément du tableau et `currentValue` égal au deuxième élément :

```js
const numbers = [2, 3, 4];
const product = numbers.reduce((total, current) => {
  return total * current;
});

console.log(product);
```

Dans cet exemple, aucun `initialValue` n'est fourni, donc `reduce()` définit le premier élément du tableau comme valeur de l'accumulateur (`total` est égal à 2), et définit le deuxième élément du tableau comme valeur actuelle (`currentValue` est égal à 3). Il parcourt ensuite le reste du tableau.

Lors de la réduction d'un tableau de chaînes :

```js
const strings = ['one', 'two', 'three'];
const numberString = strings.reduce((acc, curr) => {
  return acc + ', ' + curr;
});

console.log(numberString); // "one, two, three"
```

Bien qu'il soit facile d'omettre l'argument `initialValue` si votre méthode `reduce()` retournera un nombre ou une simple chaîne, vous devriez en inclure un si elle retournera un tableau ou un objet.

## Retourner un Objet

Transformer un tableau de chaînes en un seul objet qui montre combien de fois chaque chaîne apparaît dans le tableau est simple. Il suffit de passer un objet vide (`{}`) comme `initialValue` :

```js
const pets = ["dog", "chicken", "cat", "dog", "chicken", "chicken", "rabbit"];

const petCounts = pets.reduce(function(obj, pet) {
  if (!obj[pet]) {
    // si l'animal n'existe pas encore comme propriété de l'objet accumulateur,
    //   ajoutez-le comme propriété et définissez son compte à 1
    obj[pet] = 1;
  } else {
    // l'animal existe, donc incrémentez son compte
    obj[pet]++;
  }
  
  return obj; // retourne l'objet modifié pour être utilisé comme accumulateur dans la prochaine itération
}, {}); // initialise l'accumulateur comme un objet vide

console.log(petCounts);
/*
{
  dog: 2, 
  chicken: 3, 
  cat: 1, 
  rabbit: 1 
}
*/
```

## Retourner un Tableau

Généralement, si vous prévoyez de retourner un tableau, `map()` est souvent une meilleure option. Cela indique au compilateur (et aux autres lisant votre code) que chaque élément du tableau original sera transformé et retourné comme un nouveau tableau de longueur égale.

D'un autre côté, `reduce()` indique que tous les éléments du tableau original seront transformés en une nouvelle valeur. Cette nouvelle valeur pourrait être un tableau, dont la longueur pourrait être différente de celle de l'original.

Supposons que vous avez une liste de courses sous forme de tableau de chaînes, mais que vous souhaitez supprimer tous les aliments que vous n'aimez pas de la liste. Vous pourriez utiliser `filter()` pour filtrer tout ce que vous n'aimez pas et `map()` pour retourner un nouveau tableau de chaînes, ou vous pourriez simplement utiliser `reduce()` :

```js
const shoppingList = ['apples', 'mangoes', 'onions', 'cereal', 'carrots', 'eggplants'];
const foodsIDontLike = ['onions', 'eggplants'];
const newShoppingList = shoppingList.reduce((arr, curr) => {
  if (!foodsIDontLike.includes(curr)) {
    arr.push(curr);
  }
  
  return arr;
}, []);

console.log(newShoppingList); // ["apples", "mangoes", "cereal", "carrots"]
```

C'est tout ce que vous devez savoir sur la méthode `reduce()`. Comme un couteau suisse, ce n'est pas toujours le meilleur outil pour le travail. Mais vous serez content de l'avoir dans votre poche lorsque vous en aurez vraiment besoin.
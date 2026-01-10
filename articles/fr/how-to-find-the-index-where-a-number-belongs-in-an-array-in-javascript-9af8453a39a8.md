---
title: Comment trouver l'index où un nombre appartient dans un tableau en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-13T20:07:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-the-index-where-a-number-belongs-in-an-array-in-javascript-9af8453a39a8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XdBvGuY3oLB3E3Iv0CD-SA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment trouver l'index où un nombre appartient dans un tableau en JavaScript
seo_desc: 'By Dylan Attal

  Sorting is a very important concept when writing algorithms. There are all kinds
  of sorts: bubble sort, shell sort, block sort, comb sort, cocktail sort, gnome sort
  — I’m not making these up!

  This challenge gives us a glimpse into the ...'
---

Par Dylan Attal

Le tri est un concept très important lors de l'écriture d'algorithmes. Il existe toutes sortes de tris : tri à bulles, tri de Shell, tri par blocs, tri en peigne, tri cocktail, tri gnome — [je n'invente pas ces noms](https://en.wikipedia.org/wiki/Sorting_algorithm) !

Ce défi nous donne un aperçu du merveilleux monde des tris. Nous devons trier un tableau de nombres du plus petit au plus grand et trouver où un nombre donné appartiendrait dans ce tableau.

#### Instructions de l'algorithme

> Retournez l'index le plus bas auquel une valeur (deuxième argument) devrait être insérée dans un tableau (premier argument) une fois qu'il a été trié. La valeur retournée devrait être un nombre.

> Par exemple, `_getIndexToIns([1,2,3,4], 1.5)_` devrait retourner `_1_` car il est plus grand que `_1_` (index 0), mais plus petit que `_2_` (index 1).

> De même, `_getIndexToIns([20,3,5], 19)_` devrait retourner `_2_` car une fois le tableau trié, il ressemblera à `_[3,5,20]_` et `_19_` est plus petit que `_20_` (index 2) et plus grand que `_5_` (index 1).

```js
function getIndexToIns(arr, num) {
  return num;
}

getIndexToIns([40, 60], 50);
```

#### Cas de test fournis

* `getIndexToIns([10, 20, 30, 40, 50], 35)` devrait retourner `3`.
* `getIndexToIns([10, 20, 30, 40, 50], 35)` devrait retourner un nombre.
* `getIndexToIns([10, 20, 30, 40, 50], 30)` devrait retourner `2`.
* `getIndexToIns([10, 20, 30, 40, 50], 30)` devrait retourner un nombre.
* `getIndexToIns([40, 60], 50)` devrait retourner `1`.
* `getIndexToIns([40, 60], 50)` devrait retourner un nombre.
* `getIndexToIns([3, 10, 5], 3)` devrait retourner `0`.
* `getIndexToIns([3, 10, 5], 3)` devrait retourner un nombre.
* `getIndexToIns([5, 3, 20, 3], 5)` devrait retourner `2`.
* `getIndexToIns([5, 3, 20, 3], 5)` devrait retourner un nombre.
* `getIndexToIns([2, 20, 10], 19)` devrait retourner `2`.
* `getIndexToIns([2, 20, 10], 19)` devrait retourner un nombre.
* `getIndexToIns([2, 5, 10], 15)` devrait retourner `3`.
* `getIndexToIns([2, 5, 10], 15)` devrait retourner un nombre.
* `getIndexToIns([], 1)` devrait retourner `0`.
* `getIndexToIns([], 1)` devrait retourner un nombre.

### Solution #1 : .sort( ), .indexOf( )

#### PEDAC

**Comprendre le problème** : Nous avons deux entrées, un tableau et un nombre. Notre objectif est de retourner l'index de notre nombre d'entrée après qu'il ait été trié dans le tableau d'entrée.

**Exemples/Cas de test** : Les bonnes personnes de freeCodeCamp ne nous disent pas de quelle manière le tableau d'entrée doit être trié, mais les cas de test fournis montrent clairement que le tableau d'entrée doit être trié du plus petit au plus grand.

Remarquez qu'il y a un cas particulier dans les deux derniers cas de test fournis où le tableau d'entrée est un tableau vide.

**Structure de données** : Puisque nous retournons finalement un index, rester avec des tableaux va fonctionner pour nous.

Nous allons utiliser une méthode astucieuse nommée `[.indexOf()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)` :

`.indexOf()` retourne le premier index auquel un élément est présent dans un tableau, ou `-1` si l'élément n'est pas présent du tout. Par exemple :

```
let food = ['pizza', 'ice cream', 'chips', 'hot dog', 'cake']
```

```
food.indexOf('chips')// retourne 2food.indexOf('spaghetti')// retourne -1
```

Nous allons également utiliser `[.concat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)` ici au lieu de `[.push()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)`. Pourquoi ? Parce que lorsque vous ajoutez un élément à un tableau en utilisant `.push()`, il retourne la longueur du nouveau tableau. Lorsque vous ajoutez un élément à un tableau en utilisant `.concat()`, il retourne le nouveau tableau lui-même. Par exemple :

```
let array = [4, 10, 20, 37, 45]
```

```
array.push(98)// retourne 6array.concat(98)// retourne [4, 10, 20, 37, 45, 98]
```

**Algorithme** :

1. Insérez `num` dans `arr`.
2. Triez `arr` du plus petit au plus grand.
3. Retournez l'index de `num`.

**Code** : Voir ci-dessous !

```js
function getIndexToIns(arr, num) {
  // Insérez num dans arr, créant un nouveau tableau.
     let newArray = arr.concat(num)
  //             [40, 60].concat(50)
  //             [40, 60, 50]

  // Triez le nouveau tableau du plus petit au plus grand.
     newArray.sort((a, b) => a - b)
  // [40, 60, 50].sort((a, b) => a - b)
  // [40, 50, 60]

  // Retournez l'index de num qui est maintenant
  // à la bonne place dans le nouveau tableau.
     return newArray.indexOf(num);
  // return [40, 50, 60].indexOf(50)
  // 1
}

getIndexToIns([40, 60], 50);
```

Sans variables locales ni commentaires :

```js
function getIndexToIns(arr, num) {
  return arr.concat(num).sort((a, b) => a - b).indexOf(num);
}

getIndexToIns([40, 60], 50);
```

### Solution #2 : .sort( ), .findIndex( )

#### PEDAC

**Comprendre le problème** : Nous avons deux entrées, un tableau et un nombre. Notre objectif est de retourner l'index de notre nombre d'entrée après qu'il ait été trié dans le tableau d'entrée.

**Exemples/Cas de test** : Les bonnes personnes de freeCodeCamp ne nous disent pas de quelle manière le tableau d'entrée doit être trié, mais les cas de test fournis montrent clairement que le tableau d'entrée doit être trié du plus petit au plus grand.

Il y a deux cas particuliers à prendre en compte avec cette solution :

1. Si le tableau d'entrée est vide, nous devons retourner `0` car `num` serait le seul élément dans ce tableau, donc à l'index `0`.
2. Si `num` appartiendrait à la toute fin de `arr` trié du plus petit au plus grand, alors nous devons retourner la longueur de `arr`.

**Structure de données** : Puisque nous retournons finalement un index, rester avec des tableaux va fonctionner pour nous.

Examinons `[.findIndex()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)` pour voir comment il va nous aider à résoudre ce défi :

`.findIndex()` retourne l'index du premier élément dans le tableau qui satisfait la fonction de test fournie. Sinon, il retourne -1, indiquant qu'aucun élément n'a passé le test. Par exemple :

```js
let numbers = [3, 17, 94, 15, 20]
numbers.findIndex((currentNum) => currentNum % 2 == 0)
// retourne 2
numbers.findIndex((currentNum) => currentNum > 100)
// retourne -1
```

Cela est utile pour nous car nous pouvons utiliser `.findIndex()` pour comparer notre `num` d'entrée à chaque nombre dans notre `arr` d'entrée et déterminer où il s'intégrerait dans l'ordre du plus petit au plus grand.

**Algorithme** :

1. Si `arr` est un tableau vide, retournez `0`.
2. Si `num` appartient à la fin du tableau trié, retournez la longueur de `arr`.
3. Sinon, retournez l'index où `num` serait si `arr` était trié du plus petit au plus grand.

**Code** : Voir ci-dessous !

```js
function getIndexToIns(arr, num) {
  // Triez arr du plus petit au plus grand.
    let sortedArray = arr.sort((a, b) => a - b)
  //                  [40, 60].sort((a, b) => a - b)
  //                  [40, 60]

  // Comparez num à chaque nombre dans sortedArray
  // et trouvez l'index où num est inférieur ou égal à 
  // un nombre dans sortedArray.
    let index = sortedArray.findIndex((currentNum) => num <= currentNum)
  //            [40, 60].findIndex(40 => 50 <= 40) --> falsy
  //            [40, 60].findIndex(60 => 50 <= 60) --> truthy
  //            retourne 1 car num s'intégrerait comme suit [40, 50, 60]

  // Retournez l'index correct de num.
  // Si num appartient à la fin de sortedArray ou si arr est vide 
  // retournez la longueur de arr.
    return index === -1 ? arr.length : index
}

getIndexToIns([40, 60], 50);
```

Sans variables locales ni commentaires :

```js
function getIndexToIns(arr, num) {
  let index = arr.sort((a, b) => a - b).findIndex((currentNum) => num <= currentNum)
  return index === -1 ? arr.length : index
}

getIndexToIns([40, 60], 50);
```

Si vous avez d'autres solutions et/ou suggestions, n'hésitez pas à les partager dans les commentaires !

#### Cet article fait partie de la série [freeCodeCamp Algorithm Scripting](https://medium.com/@DylanAttal/freecodecamp-algorithm-scripting-b96227b7f837).

#### Cet article référence [freeCodeCamp Basic Algorithm Scripting : Where do I Belong](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/where-do-i-belong).

Vous pouvez me suivre sur [Medium](https://medium.com/@DylanAttal), [LinkedIn](https://www.linkedin.com/in/dylanattal/), et [GitHub](https://github.com/DylanAttal) !
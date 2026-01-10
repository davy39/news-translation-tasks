---
title: Comment utiliser les méthodes flat() et flatMap() pour aplatir les tableaux
  en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-26T16:47:22.000Z'
originalURL: https://freecodecamp.org/news/flat-and-flatmap-javascript-array-methods
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/js-map-2.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser les méthodes flat() et flatMap() pour aplatir les tableaux
  en JavaScript
seo_desc: 'By Kenechukwu Nwobodo

  In this article I''m going to explain how to use the new array methods introduced
  in ES2019 (EcmaScript 2019) – flat() and flatMap(). You use these methods to flatten
  arrays.

  The methods are very useful and easy to use. It will r...'
---

Par Kenechukwu Nwobodo

Dans cet article, je vais expliquer comment utiliser les nouvelles méthodes de tableau introduites dans ES2019 (EcmaScript 2019) – `flat()` et `flatMap()`. Vous utilisez ces méthodes pour aplatir les tableaux.

Les méthodes sont très utiles et faciles à utiliser. Ce serait vraiment cool d'utiliser ces méthodes dans votre prochain projet. Prenez un café et plongeons-nous dedans.

## Prérequis

Vous devriez être familier avec le concept des tableaux en JavaScript pour suivre ce tutoriel.

## Qu'est-ce qu'un tableau ?

L'objet tableau est une structure de données utilisée dans différents langages de programmation pour stocker différentes collections de données.

### Exemple de tableau en JavaScript

```javascript
const array = [1, 2, 3, true, null, undefined];

console.log(array);

// résultat attendu
1, 2, 3, true, null, undefined
```

Dans le code ci-dessus, nous avons assigné une variable nommée **`arr`** et stocké différents éléments/données de différents types de données dedans.

Le premier élément, qui est 1, est à l'index 0. Le dernier élément, undefined, est à l'index 5.

N'oubliez pas que les objets tableau sont indexés à partir de zéro, ce qui signifie que le premier élément commence à un index de zéro.

## Caractéristiques des tableaux JavaScript

* **Les tableaux sont indexés à partir de zéro** : Cela signifie simplement que le premier élément d'un tableau est à l'index 0. L'index ici signifie position. En JavaScript et dans d'autres langages de programmation, le terme correct à utiliser est index et non position.
* **Les tableaux JavaScript peuvent contenir différents types de données** : Cela signifie que les tableaux JavaScript peuvent contenir un mélange de nombres, de chaînes de caractères, de booléens, de valeurs null, et ainsi de suite.
* **JavaScript crée des copies superficielles** : Cela signifie que le tableau original et la copie pointent vers la même référence – modifier la copie peut altérer le tableau original.

## Nouvelles méthodes de tableau JavaScript

Les tableaux sont l'une des structures de données les plus populaires en JavaScript utilisées pour stocker des données.

Il existe différentes méthodes de tableau que vous pouvez utiliser pour simplifier les opérations et faciliter votre vie. Certaines de ces méthodes incluent `reduce()`, `filter()`, `map()`, `flat()`, `flatMap()`, et bien d'autres.

Mais dans cet article, nous ne discuterons pas de toutes les méthodes de tableau utilisées en JavaScript. Plutôt, nous discuterons des nouvelles méthodes `flat()` et `flatMap()` que vous pouvez utiliser pour convertir un tableau original en un nouveau tableau.

## Comment utiliser la méthode de tableau `flat` en JavaScript

Vous utilisez la méthode `flat` pour convertir un tableau original en un nouveau tableau. Elle le fait en collectant et en concaténant les sous-tableaux d'un tableau en un seul tableau.

Une note importante sur cette méthode de tableau est que vous pouvez calculer l'original en un autre tableau en fonction de la profondeur du tableau. Cette méthode est vraiment utile car elle facilite le calcul des opérations d'un tableau.

## Exemples de la méthode de tableau `flat()`

### Comment définir le paramètre de profondeur

```js
array.flat(profondeur);
```

La valeur de profondeur est 1 par défaut et vous pouvez la laisser vide. La valeur de profondeur prend un nombre comme type de données.

#### Exemple 1 de la méthode de tableau `flat()`

`array.flat(1)` est égal à `array.flat()`.

`array.flat(2);`

La profondeur ci-dessus est **2**.

```javascript
const arr = ["mon", "tues", ["wed", "thurs", ["fri", "sat"]], "sun"] ;

console.log(arr.flat());

// résultat attendu
["mon", "tues", "wed", "thurs", ["fri", "sat"], "sun"];
```

Alors, que se passe-t-il dans ce code ?

Tout d'abord, le tableau contient deux sous-tableaux qui sont `["wed", "thurs", ["fri", "sat"]]`.

Nous utilisons la méthode **flat()** sur le tableau nommé **`arr`** pour concaténer le premier sous-tableau car nous n'avons pas spécifié de valeur de profondeur à l'intérieur de la méthode **flat()**. Rappelez-vous que la valeur de profondeur par défaut est **1**.

Alors, vous pouvez deviner à quoi ressemblerait l'objet tableau si la valeur de profondeur était 2, n'est-ce pas ?

#### Exemple 2 de la méthode de tableau `flat()`

```javascript
const arr = [1, 2, [3, 4, 5], 6, 7];

console.log(arr.flat());

// résultat attendu
[1, 2, 3, 4, 5, 6, 7]
```

Dans le code ci-dessus, le tableau contient un sous-tableau qui est `[3, 4, 5]`.

Nous utilisons la méthode **flat()** sur le tableau nommé **`arr`** pour concaténer les deux tableaux en un seul tableau.

#### Exemple 3 de la méthode de tableau `flat()`

```javascript
// exemple de profondeur 2
const arr2 = [[[1, 2], 3, 4, 5]] ;

console.log(arr2.flat(2));

// résultat attendu
[1, 2, 3, 4, 5]
```

Dans le code ci-dessus, le tableau nommé **`arr2`** contient deux sous-tableaux.

Nous utilisons la méthode **flat()** sur `arr2` pour concaténer les deux tableaux en un seul tableau en raison de la valeur de profondeur 2 utilisée à l'intérieur de la méthode flat(2). Jetez un coup d'œil rapide ci-dessus pour voir ce que fait la valeur de profondeur.

La méthode de tableau est une belle façon de concaténer des éléments dans un tableau de manière récursive.

## Comment utiliser la méthode de tableau `flatMap` en JavaScript

La méthode `flatMap()` utilise une combinaison des méthodes `map()` et `flat()` pour effectuer des opérations.

La méthode `flatMap()` parcourt les éléments d'un tableau et concatène les éléments en un seul niveau. `flatMap()` prend une fonction de rappel qui prend l'élément actuel du tableau original comme paramètre.

### Exemple de la méthode de tableau `flatMap()`

```javascript
const arr3 = [1, 2, [4, 5], 6, 7, [8]] ;

console.log(arr3.flatMap((element) => element)) ;

// résultat attendu
[1, 2, 4, 5, 6, 7, 8]
```

Dans le code ci-dessus, le tableau nommé **`arr3`** contient deux sous-tableaux distincts.

Nous avons utilisé la méthode **flatMap()** sur le tableau en passant une fonction de rappel, **(element) => element** qui parcourt le tableau puis concatène les tableaux en un seul tableau.

Parfois, vous aurez une situation où vous avez plus d'une profondeur de tableau et vous décidez de changer le nouveau tableau en un niveau de base unique. Vous devrez alors utiliser la méthode `flat()` immédiatement après la méthode `flatMap()`.

### Voici un exemple :

```javascript
const arr4 = [1, 2, [3, [4, 5, [6, 7]]]] ;

console.log(arr4.flatMap((element) => element).flat(2)) ;

// résultat attendu
[1, 2, 3, 4, 5, 6, 7]

```

Dans le code ci-dessus, le tableau nommé **`arr4`** contient trois sous-tableaux.

Nous avons utilisé la méthode **flatMap()** sur le tableau en passant une fonction de rappel, **(element) => element** qui parcourt le tableau puis concatène les tableaux.

Nous avons utilisé la méthode **flat(2)** pour concaténer davantage le tableau en un seul tableau en passant une profondeur de **2**.

Assurez-vous de pratiquer l'exemple ci-dessus sans passer la méthode flat(2) et voyez la différence.

C'est tout ce dont vous avez besoin pour commencer avec ces deux nouvelles méthodes de tableau.

## Résumé

Dans cet article, j'ai brièvement discuté de ce que sont les tableaux et de leur utilité en JavaScript. Ensuite, nous avons appris deux nouvelles méthodes de tableau importantes qui ont été introduites dans ECMAScript 2019 et qui vous permettent de changer un tableau original en un nouveau tableau.

Ces nouvelles méthodes de tableau sont les méthodes `flat()` et `flatMap()`.

Vous utilisez la méthode `flat()` pour concaténer des sous-tableaux de manière récursive en un seul tableau. La méthode `flat()` prend une valeur de profondeur comme paramètre, qui est optionnelle en fonction de la profondeur du tableau que vous souhaitez aplatir (concaténer). La méthode `flat()` prend 1 comme profondeur par défaut.

D'autre part, `flatMap()` fonctionne essentiellement de la même manière, sauf qu'il s'agit d'une combinaison des méthodes `map()` et `flat()`. `flatMap()` parcourt les éléments du tableau et concatène les éléments.

Les deux nouvelles méthodes sont utiles lorsque vous changez un tableau original en un nouveau tableau. Elles valent la peine d'être essayées dans votre prochain grand ou petit projet.

### Autres ressources utiles :

* [Référence MDN sur flatMap()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
* [Référence MDN sur flat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)()
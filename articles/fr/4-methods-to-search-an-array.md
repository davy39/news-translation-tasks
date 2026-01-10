---
title: Quatre façons différentes de rechercher un tableau en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-24T18:00:00.000Z'
originalURL: https://freecodecamp.org/news/4-methods-to-search-an-array
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a13740569d1a4ca2358.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Quatre façons différentes de rechercher un tableau en JavaScript
seo_desc: "By Sarah Chima Atuonwu\nThere are different methods in JavaScript that\
  \ you can use to search for an item in an array. Which method you choose depends\
  \ on your specific use case. \nFor instance, do you want to get all items in an\
  \ array that meet a specif..."
---

Par Sarah Chima Atuonwu

Il existe différentes méthodes en JavaScript que vous pouvez utiliser pour rechercher un élément dans un tableau. La méthode que vous choisissez dépend de votre cas d'utilisation spécifique. 

Par exemple, souhaitez-vous obtenir tous les éléments d'un tableau qui répondent à une condition spécifique ? Souhaitez-vous vérifier si un élément répond à la condition ? Souhaitez-vous vérifier si une valeur spécifique se trouve dans le tableau ? Ou souhaitez-vous trouver l'index de la valeur dans le tableau ?

Pour tous ces cas d'utilisation, les méthodes Array.prototype de JavaScript vous couvrent. Dans cet article, nous allons discuter de quatre méthodes que nous pouvons utiliser pour rechercher un élément dans un tableau. Ces méthodes sont :

1. Filter
2. Find
3. Includes
4. IndexOf

Discutons de chacune d'elles.

### Array.filter()

Nous pouvons utiliser la méthode Array.filter() pour trouver des éléments dans un tableau qui répondent à une certaine condition. Par exemple, si nous voulons obtenir tous les éléments d'un tableau de nombres qui sont supérieurs à 10, nous pouvons faire ceci :

```js
const array = [10, 11, 3, 20, 5];

const greaterThanTen = array.filter(element => element > 10);

console.log(greaterThanTen) //[11, 20]
```

La syntaxe pour utiliser la méthode array.filter() est la suivante :

```text
let newArray = array.filter(callback);
```

où

* `newArray` est le nouveau tableau qui est retourné
* `array` est le tableau sur lequel la méthode filter est appelée
* `callback` est la fonction de rappel qui est appliquée à chaque élément du tableau

Si aucun élément du tableau ne répond à la condition, un tableau vide est retourné. Vous pouvez en savoir plus sur [cette méthode ici](https://sarahchima.com/blog/javascript-array-filter/).

Il arrive que nous n'ayons pas besoin de tous les éléments qui répondent à une certaine condition. Nous avons juste besoin d'un élément qui correspond à la condition. Dans ce cas, vous avez besoin de la méthode find().

### Array.find()

Nous utilisons la méthode Array.find() pour trouver le premier élément qui répond à une certaine condition. Tout comme la méthode filter, elle prend un callback comme argument et retourne le premier élément qui répond à la condition du callback.

Utilisons la méthode find sur le tableau de notre exemple ci-dessus.

```js
const array = [10, 11, 3, 20, 5];

const greaterThanTen = array.find(element => element > 10);

console.log(greaterThanTen)//11
```

La syntaxe pour array.find() est

```js
let element = array.find(callback);
```

Le callback est la fonction qui est exécutée sur chaque valeur du tableau et prend trois arguments :

* `element` - l'élément sur lequel on itère (obligatoire)
* `index` - l'index/position de l'élément actuel (optionnel)
* `array` - le tableau sur lequel `find` a été appelé (optionnel)

Notez, cependant, que si aucun élément du tableau ne répond à la condition, il retourne `undefined`.

Mais que faire si vous voulez vérifier si un certain élément est dans un tableau ? Comment faire cela ?

### Array.includes()

La méthode includes() détermine si un tableau inclut une certaine valeur et retourne true ou false selon le cas.

Ainsi, dans l'exemple ci-dessus, si nous voulons vérifier si 20 est l'un des éléments du tableau, nous pouvons faire ceci :

```js
const array = [10, 11, 3, 20, 5];

const includesTwenty = array.includes(20);

console.log(includesTwenty)//true
```

Vous remarquerez une différence entre cette méthode et les autres méthodes que nous avons considérées. Cette méthode accepte une valeur plutôt qu'un callback comme argument. Voici la syntaxe pour la méthode includes :

```js
const includesValue = array.includes(valueToFind, fromIndex)
```

Où 

* `valueToFind` est la valeur que vous recherchez dans le tableau (obligatoire), et
* `fromIndex` est l'index ou la position dans le tableau à partir de laquelle vous voulez commencer à rechercher l'élément (optionnel)

Pour comprendre le concept de l'index, revisitons notre exemple. Si nous voulons vérifier si le tableau contient 10 dans d'autres positions que le premier élément, nous pouvons faire ceci :

```js
const array = [10, 11, 3, 20, 5];

const includesTenTwice = array.includes(10, 1);

console.log(includesTenTwice)//false
```

### Array.indexOf()

La méthode indexOf() retourne le premier index auquel un élément donné peut être trouvé dans un tableau. Elle retourne -1 si l'élément n'existe pas dans le tableau.

Revenons à notre exemple. Trouvons l'index de 3 dans le tableau.

```js
const array = [10, 11, 3, 20, 5];

const indexOfThree = array.indexOf(3);

console.log(indexOfThree)//2
```

Sa syntaxe est similaire à celle de la méthode `includes`.

```js
const indexOfElement = array.indexOf(element, fromIndex)
```

Où 

* `element` est l'élément que vous recherchez dans le tableau (obligatoire), et
* `fromIndex` est l'index ou la position dans le tableau à partir de laquelle vous voulez commencer à rechercher l'élément (optionnel)

Il est important de noter que les méthodes `includes` et `indexOf` utilisent l'égalité stricte( '===' ) pour rechercher dans le tableau. Si les valeurs sont de types différents (par exemple '4' et 4), elles retourneront `false` et `-1` respectivement.

## Résumé

Avec ces méthodes de tableau, vous n'avez pas besoin d'utiliser une boucle for pour rechercher dans un tableau. Selon ce dont vous avez besoin, vous pouvez décider quelle méthode est la mieux adaptée à votre cas d'utilisation. 

Voici un résumé de quand utiliser chaque méthode :

* Utilisez `filter` si vous voulez trouver tous les éléments d'un tableau qui répondent à une condition spécifique.
* Utilisez `find` si vous voulez vérifier si au moins un élément répond à une condition spécifique.
* Utilisez `includes` si vous voulez vérifier si un tableau contient une valeur particulière.
* Utilisez `indexOf` si vous voulez trouver l'index d'un élément particulier dans un tableau.

_Voulez-vous être informé lorsque je publie un nouvel article ? [Cliquez ici](https://mailchi.mp/69ea601a3f64/join-sarahs-mailing-list)._
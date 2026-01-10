---
title: 10 Fonctions Utilitaires JavaScript Créées avec Reduce
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-17T12:59:00.000Z'
originalURL: https://freecodecamp.org/news/10-js-util-functions-in-reduce
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/10-js-utility-functions-using-reduce-1.png
tags:
- name: arrays
  slug: arrays
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Ramda
  slug: ramda
- name: technology
  slug: technology
seo_title: 10 Fonctions Utilitaires JavaScript Créées avec Reduce
seo_desc: 'By Yazeed Bzadough

  The multi-tool strikes again.

  In my last article I offered you a challenge to recreate well-known functions using
  reduce. This article will show you how some of them can be implemented, along with
  some extras!

  In total we''re going ...'
---

Par Yazeed Bzadough

Le multi-outil frappe encore.

Dans [mon dernier article](https://www.yazeedb.com/posts/learn-reduce-in-10-minutes/), je vous ai proposé un défi pour recréer des fonctions bien connues en utilisant `reduce`. Cet article vous montrera comment certaines d'entre elles peuvent être implémentées, ainsi que quelques extras !

Au total, nous allons examiner dix fonctions utilitaires. Elles sont incroyablement pratiques pour vos projets, et surtout, elles sont implémentées en utilisant `reduce` ! Je me suis beaucoup inspiré de la [bibliothèque RamdaJS](https://ramdajs.com/) pour celle-ci, alors allez y jeter un coup d'œil !

## 1. some
### Paramètres
1. `predicate` - Fonction qui retourne `true` ou `false`.
2. `array` - Liste d'éléments à tester.

### Description
Si `predicate` retourne `true` pour _n'importe quel_ élément, `some` retourne `true`. Sinon, il retourne `false`.

### Implémentation
```js
const some = (predicate, array) =>
  array.reduce((acc, value) => acc || predicate(value), false);
```

### Utilisation
```js
const equals3 = (x) => x === 3;

some(equals3, [3]); // true
some(equals3, [3, 3, 3]); // true
some(equals3, [1, 2, 3]); // true
some(equals3, [2]); // false
```

## 2. all
### Paramètres
1. `predicate` - Fonction qui retourne `true` ou `false`.
2. `array` - Liste d'éléments à tester.

### Description
Si `predicate` retourne `true` pour _chaque_ élément, `all` retourne `true`. Sinon, il retourne `false`.

### Implémentation
```js
const all = (predicate, array) =>
  array.reduce((acc, value) => acc && predicate(value), true);
```

### Utilisation
```js
const equals3 = (x) => x === 3;

all(equals3, [3]); // true
all(equals3, [3, 3, 3]); // true
all(equals3, [1, 2, 3]); // false
all(equals3, [3, 2, 3]); // false
```

## 3. none
### Paramètres
1. `predicate` - Fonction qui retourne `true` ou `false`.
2. `array` - Liste d'éléments à tester.

### Description
Si `predicate` retourne `false` pour _chaque_ élément, `none` retourne `true`. Sinon, il retourne `false`.

### Implémentation
```js
const none = (predicate, array) =>
  array.reduce((acc, value) => !acc && !predicate(value), false);
```

### Utilisation
```js
const isEven = (x) => x % 2 === 0;

none(isEven, [1, 3, 5]); // true
none(isEven, [1, 3, 4]); // false
none(equals3, [1, 2, 4]); // true
none(equals3, [1, 2, 3]); // false
```

## 4. map
### Paramètres
1. `transformFunction` - Fonction à exécuter sur chaque élément.
2. `array` - Liste d'éléments à transformer.

### Description
Retourne un nouveau tableau d'éléments, chacun transformé selon la `transformFunction` donnée.

### Implémentation
```js
const map = (transformFunction, array) =>
  array.reduce((newArray, item) => {
    newArray.push(transformFunction(item));

    return newArray;
  }, []);
```

### Utilisation
```js
const double = (x) => x * 2;
const reverseString = (string) =>
  string
    .split('')
    .reverse()
    .join('');

map(double, [100, 200, 300]);
// [200, 400, 600]

map(reverseString, ['Hello World', 'I love map']);
// ['dlroW olleH', 'pam evol I']
```

## 5. filter
### Paramètres
1. `predicate` - Fonction qui retourne `true` ou `false`.
2. `array` - Liste d'éléments à filtrer.

### Description
Retourne un nouveau tableau. Si `predicate` retourne `true`, cet élément est ajouté au nouveau tableau. Sinon, cet élément est exclu du nouveau tableau.

### Implémentation
```js
const filter = (predicate, array) =>
  array.reduce((newArray, item) => {
    if (predicate(item) === true) {
      newArray.push(item);
    }

    return newArray;
  }, []);
```

### Utilisation
```js
const isEven = (x) => x % 2 === 0;

filter(isEven, [1, 2, 3]);
// [2]

filter(equals3, [1, 2, 3, 4, 3]);
// [3, 3]
```

## 6. reject
### Paramètres
1. `predicate` - Fonction qui retourne `true` ou `false`.
2. `array` - Liste d'éléments à filtrer.

### Description
Tout comme `filter`, mais avec le comportement opposé.

Si `predicate` retourne `false`, cet élément est ajouté au nouveau tableau. Sinon, cet élément est exclu du nouveau tableau.

### Implémentation
```js
const reject = (predicate, array) =>
  array.reduce((newArray, item) => {
    if (predicate(item) === false) {
      newArray.push(item);
    }

    return newArray;
  }, []);
```

### Utilisation
```js
const isEven = (x) => x % 2 === 0;

reject(isEven, [1, 2, 3]);
// [1, 3]

reject(equals3, [1, 2, 3, 4, 3]);
// [1, 2, 4]
```

## 7. find
### Paramètres
1. `predicate` - Fonction qui retourne `true` ou `false`.
2. `array` - Liste d'éléments à rechercher.

### Description
Retourne le premier élément qui correspond au `predicate` donné. Si aucun élément ne correspond, alors `undefined` est retourné.

### Implémentation
```js
const find = (predicate, array) =>
  array.reduce((result, item) => {
    if (result !== undefined) {
      return result;
    }

    if (predicate(item) === true) {
      return item;
    }

    return undefined;
  }, undefined);
```

### Utilisation
```js
const isEven = (x) => x % 2 === 0;

find(isEven, []); // undefined
find(isEven, [1, 2, 3]); // 2
find(isEven, [1, 3, 5]); // undefined
find(equals3, [1, 2, 3, 4, 3]); // 3
find(equals3, [1, 2, 4]); // undefined
```

## 8. partition
### Paramètres
1. `predicate` - Fonction qui retourne `true` ou `false`.
2. `array` - Liste d'éléments.

### Description
"Partitionne" ou divise un tableau en deux en fonction du `predicate`. Si `predicate` retourne `true`, l'élément va dans la liste 1. Sinon, l'élément va dans la liste 2.

### Implémentation
```js
const partition = (predicate, array) =>
  array.reduce(
    (result, item) => {
      const [list1, list2] = result;

      if (predicate(item) === true) {
        list1.push(item);
      } else {
        list2.push(item);
      }

      return result;
    },
    [[], []]
  );
```

### Utilisation
```js
const isEven = (x) => x % 2 === 0;

partition(isEven, [1, 2, 3]);
// [[2], [1, 3]]

partition(isEven, [1, 3, 5]);
// [[], [1, 3, 5]]

partition(equals3, [1, 2, 3, 4, 3]);
// [[3, 3], [1, 2, 4]]

partition(equals3, [1, 2, 4]);
// [[], [1, 2, 4]]
```

## 9. pluck
### Paramètres
1. `key` - Nom de la clé à extraire de l'objet
2. `array` - Liste d'éléments.

### Description
Extrait la `key` donnée de chaque élément du tableau. Retourne un nouveau tableau de ces valeurs.

### Implémentation
```js
const pluck = (key, array) =>
  array.reduce((values, current) => {
    values.push(current[key]);

    return values;
  }, []);
```

### Utilisation
```js
pluck('name', [{ name: 'Batman' }, { name: 'Robin' }, { name: 'Joker' }]);
// ['Batman', 'Robin', 'Joker']

pluck(0, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
// [1, 4, 7]
```

## 10. scan
### Paramètres
1. `reducer` - Fonction reducer standard qui reçoit deux paramètres - l'accumulateur et l'élément courant du tableau.
2. `initialValue` - La valeur initiale pour l'accumulateur.
3. `array` - Liste d'éléments.

### Description
Fonctionne comme `reduce`, mais au lieu de retourner un seul résultat, il retourne une liste de chaque valeur réduite sur le chemin vers le résultat unique.

### Implémentation
```js
const scan = (reducer, initialValue, array) => {
  const reducedValues = [];

  array.reduce((acc, current) => {
    const newAcc = reducer(acc, current);

    reducedValues.push(newAcc);

    return newAcc;
  }, initialValue);

  return reducedValues;
};
```

### Utilisation
```js
const add = (x, y) => x + y;
const multiply = (x, y) => x * y;

scan(add, 0, [1, 2, 3, 4, 5, 6]);
// [1, 3, 6, 10, 15, 21] - Chaque nombre ajouté de 1 à 6

scan(multiply, 1, [1, 2, 3, 4, 5, 6]);
// [1, 2, 6, 24, 120, 720] - Chaque nombre multiplié de 1 à 6
```

## Vous voulez un coaching gratuit ?
Si vous souhaitez planifier un appel gratuit pour discuter de questions de développement Front-End concernant le code, les entretiens, la carrière ou autre chose, [suivez-moi sur Twitter et envoyez-moi un DM](https://twitter.com/yazeedBee).

Après cela, si vous appréciez notre première rencontre, nous pouvons discuter d'un coaching continu pour vous aider à atteindre vos objectifs de développement Front-End !

## Merci d'avoir lu
Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">https://yazeedb.com !</a>

À la prochaine !
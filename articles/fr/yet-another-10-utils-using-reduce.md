---
title: Encore 10 fonctions utilitaires créées avec Reduce
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-11T12:59:00.000Z'
originalURL: https://freecodecamp.org/news/yet-another-10-utils-using-reduce
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/Yet-Another-10-Utility-Functions.png
tags:
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
seo_title: Encore 10 fonctions utilitaires créées avec Reduce
seo_desc: 'By Yazeed Bzadough

  Thirty functions total!

  This is my third article on Utility Functions Made with Reduce.


  Part one (10 functions)

  Part two (10 functions)


  Altogether we now have thirty helper functions made using JavaScript''s reduce.
  For more detai...'
---

Par Yazeed Bzadough

Trente fonctions au total !

Il s'agit de mon troisième article sur les fonctions utilitaires créées avec Reduce.

* [Partie un](https://www.freecodecamp.org/news/10-js-util-functions-in-reduce/) (10 fonctions)
* [Partie deux](https://www.freecodecamp.org/news/10-more-js-utils-using-reduce/) (10 fonctions)

Ensemble, nous avons maintenant _trente_ fonctions d'assistance créées en utilisant `reduce` de JavaScript. Pour plus de détails sur `reduce` lui-même, envisagez de lire mon [tutoriel à ce sujet](https://www.yazeedb.com/posts/learn-reduce-in-10-minutes).

Les fonctions listées ci-dessous ont été inspirées par l'incroyable bibliothèque [RamdaJS](https://ramdajs.com/). J'ai également écrit des tests unitaires pour garantir un comportement correct, que vous pouvez trouver sur [mon GitHub](https://github.com/yazeedb/js-utils-using-reduce).

## 1. adjust
### Paramètres
1. `index` - Index du tableau source
2. `fn` - Fonction à appliquer à cet `index`
3. `list` - Liste d'éléments.

### Description
Applique une fonction à la valeur à l'index donné. Retourne le tableau original si l'index fourni est hors limites.

### Utilisation
```js
const double = (x) => x * 2;

adjust(1, double, [1, 2, 3]);
// [1, 4, 3]

adjust(4, double, [1, 2, 3]);
// [1, 2, 3]
```

### Implémentation
```js
const adjust = (index, fn, list) =>
  list.reduce((acc, value, sourceArrayIndex) => {
    const valueToUse = sourceArrayIndex === index ? fn(value) : value;

    acc.push(valueToUse);

    return acc;
  }, []);
```

## 2. fromPairs
### Paramètres
1. `pairs` - Une liste de paires clé-valeur.

### Description
Crée un objet à partir d'une liste de paires clé-valeur.

### Utilisation
```js
fromPairs([['a', 1], ['b', 2], ['c', 3]]);
// { a: 1, b: 2, c: 3 }
```

### Implémentation
```js
const fromPairs = (pairs) =>
  pairs.reduce((acc, currentPair) => {
    const [key, value] = currentPair;

    acc[key] = value;

    return acc;
  }, {});
```

## 3. range
### Paramètres
1. `from` - Nombre de départ.
2. `to` - Nombre de fin.

### Description
Retourne une liste de nombres dans une plage donnée.

### Utilisation
```js
range(1, 5);
// [1, 2, 3, 4, 5]
```

### Implémentation
```js
const range = (from, to) =>
  Array.from({ length: to - from + 1 }).reduce((acc, _, index) => {
    acc.push(from + index);

    return acc;
  }, []);
```

## 4. repeat
### Paramètres
1. `item` - Élément à répéter.
2. `times` - Nombre de fois à répéter.

### Description
Retourne une liste d'une valeur donnée N fois.

### Utilisation
```js
repeat({ favoriteLanguage: 'JavaScript' }, 2);

/*
[{
    favoriteLanguage: 'JavaScript'
}, {
    favoriteLanguage: 'JavaScript'
}],
*/
```

### Implémentation
```js
const repeat = (item, times) =>
  Array.from({ length: times }).reduce((acc) => {
    acc.push(item);

    return acc;
  }, []);
```

## 5. times
### Paramètres
1. `fn` - Fonction à appeler.
2. `numTimes` - Nombre de fois à appeler cette fonction.

### Description
Appelle une fonction donnée N fois. La fonction `fn` fournie reçoit l'index actuel comme paramètre.

### Utilisation
```js
times((x) => x * 2, 3);
// [0, 2, 4]
```

### Implémentation
```js
const times = (fn, numTimes) =>
  Array.from({ length: numTimes }).reduce((acc, _, index) => {
    acc.push(fn(index));

    return acc;
  }, []);
```

## 6. deduplicate
### Paramètres
1. `items` - Liste d'éléments.

### Description
Supprime les doublons dans une liste.

### Utilisation
```js
deduplicate([[1], [1], { hello: 'world' }, { hello: 'world' }]);
// [[1], { hello: 'world' }]
```

### Implémentation
```js
const deduplicate = (items) => {
  const cache = {};

  return items.reduce((acc, item) => {
    const alreadyIncluded = cache[item] === true;

    if (!alreadyIncluded) {
      cache[item] = true;
      acc.push(item);
    }

    return acc;
  }, []);
};
```

## 7. reverse
### Paramètres
1. `list` - Liste d'éléments.

### Description
Inverse une liste _sans_ la muter en retournant une nouvelle liste, contrairement à la méthode native `Array.reverse`.

### Utilisation
```js
reverse([1, 2, 3]);
// [3, 2, 1]
```

### Implémentation
```js
const reverse = (list) =>
  list.reduce((acc, _, index) => {
    const reverseIndex = list.length - index - 1;
    const reverseValue = list[reverseIndex];

    acc.push(reverseValue);

    return acc;
  }, []);
```

## 8. insertAll
### Paramètres
1. `index` - Index où insérer.
2. `subList` - Liste à insérer.
3. `sourceList` - Liste source.

### Description
Insère une sous-liste dans une liste à l'index donné. Ajoute à la fin de la liste si l'index est trop grand.

### Utilisation
```js
insertAll(1, [2, 3, 4], [1, 5]);
// [1, 2, 3, 4, 5]

insertAll(10, [2, 3, 4], [1, 5]);
// [1, 5, 2, 3, 4]
```

### Implémentation
```js
const insertAll = (index, subList, sourceList) => {
  if (index > sourceList.length - 1) {
    return sourceList.concat(subList);
  }

  return sourceList.reduce((acc, value, sourceArrayIndex) => {
    if (index === sourceArrayIndex) {
      acc.push(...subList, value);
    } else {
      acc.push(value);
    }

    return acc;
  }, []);
};
```

## 9. mergeAll
### Paramètres
1. `objectList` - Liste d'objets à fusionner.

### Description
Fusionne une liste d'objets en un seul.

### Utilisation
```js
mergeAll([
    { js: 'reduce' },
    { elm: 'fold' },
    { java: 'collect' },
    { js: 'reduce' }
]);
  
/*
{
    js: 'reduce',
    elm: 'fold',
    java: 'collect'
}
*/
```

### Implémentation
```js
const mergeAll = (objectList) =>
  objectList.reduce((acc, obj) => {
    Object.keys(obj).forEach((key) => {
      acc[key] = obj[key];
    });

    return acc;
  }, {});
```

## 10. xprod
### Paramètres
1. `list1` - Liste d'éléments.
2. `list2` - Liste d'éléments.

### Description
Étant donné une liste, retourne une nouvelle liste de toutes les paires possibles.

### Utilisation
```js
xprod(['Hello', 'World'], ['JavaScript', 'Reduce']);
/*
[
  ['Hello', 'JavaScript'],
  ['Hello', 'Reduce'],
  ['World', 'JavaScript'],
  ['World', 'Reduce']
]
*/
```

### Implémentation
```js
const xprod = (list1, list2) =>
  list1.reduce((acc, list1Item) => {
    list2.forEach((list2Item) => {
      acc.push([list1Item, list2Item]);
    });

    return acc;
  }, []);
```

## Vous voulez un coaching gratuit ?
Si vous souhaitez planifier un appel gratuit pour discuter de questions sur le développement Front-End concernant le code, les entretiens, la carrière ou autre chose, [suivez-moi sur Twitter et envoyez-moi un message](https://twitter.com/yazeedBee).

Après cela, si vous appréciez notre première rencontre, nous pouvons discuter d'un coaching continu pour vous aider à atteindre vos objectifs de développement Front-End !

## Merci d'avoir lu
Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">https://yazeedb.com!</a>

À la prochaine !
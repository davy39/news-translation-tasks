---
title: 10 autres fonctions utilitaires créées avec Reduce
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-05T12:59:00.000Z'
originalURL: https://freecodecamp.org/news/10-more-js-utils-using-reduce
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/cover-image.png
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
seo_title: 10 autres fonctions utilitaires créées avec Reduce
seo_desc: 'By Yazeed Bzadough

  This time, with a test suite!

  Previously I wrote about 10 utility functions implemented with JavaScript''s reduce
  function. It was well-received, and I walked away with an even deeper appreciation
  for this magnificent multi-tool. Wh...'
---

Par Yazeed Bzadough

Cette fois, avec une suite de tests !

[Précédemment](https://www.freecodecamp.org/news/10-js-util-functions-in-reduce/), j'ai écrit sur 10 fonctions utilitaires implémentées avec la fonction [reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce) de JavaScript. Cela a été bien reçu, et j'en suis ressorti avec une appréciation encore plus profonde pour cet outil multi-usage magnifique. Pourquoi ne pas essayer 10 autres ?

Beaucoup de ces fonctions ont été inspirées par les bibliothèques géniales [Lodash](https://lodash.com/) et [Ramda](https://ramdajs.com/) ! J'ai également écrit des tests unitaires pour garantir un comportement correct. Vous pouvez tout voir sur le [dépôt Github ici](https://github.com/yazeedb/js-utils-using-reduce).

## 1. pipe
### Paramètres
1. `...functions` - N'importe quel nombre de fonctions.

### Description
Effectue une composition de fonctions de _gauche à droite_. Le premier argument d'un pipeline agit comme la valeur initiale et est transformé lorsqu'il passe à travers chaque fonction.

### Implémentation
```js
const pipe = (...functions) => (initialValue) =>
  functions.reduce((value, fn) => fn(value), initialValue);
```

### Utilisation
```js
const mathSequence = pipe(
    (x) => x * 2,
    (x) => x - 1,
    (x) => x * 3
  );
  
mathSequence(1); // 3
mathSequence(2); // 9
mathSequence(3); // 15
```

Pour plus de détails, j'ai écrit un [article sur pipe ici](https://www.yazeedb.com/posts/a-quick-intro-to-pipe-and-compose).

## 2. compose
### Paramètres
1. `...functions` - N'importe quel nombre de fonctions.

### Description
Effectue une composition de fonctions de _droite à gauche_. Le premier argument d'un pipeline agit comme la valeur initiale et est transformé lorsqu'il passe à travers chaque fonction.

Fonctionne comme `pipe`, mais dans la direction opposée.

### Implémentation
```js
const compose = (...functions) => (initialValue) =>
  functions.reduceRight((value, fn) => fn(value), initialValue);
```

### Utilisation
```js
const mathSequence = compose(
    (x) => x * 2,
    (x) => x - 1,
    (x) => x * 3
  );
  
mathSequence(1); // 4
mathSequence(2); // 10
mathSequence(3); // 16
```

Pour plus de détails, j'ai écrit un [article sur compose ici](https://www.yazeedb.com/posts/a-quick-intro-to-pipe-and-compose).

## 3. zip
### Paramètres
1. `list1` - Liste d'éléments.
2. `list2` - Liste d'éléments.

### Description
Associe les éléments de deux listes par index. Si les longueurs des listes ne sont pas égales, la longueur de la liste la plus courte est utilisée.

### Implémentation
```js
const zip = (list1, list2) => {
  const sourceList = list1.length > list2.length ? list2 : list1;

  return sourceList.reduce((acc, _, index) => {
    const value1 = list1[index];
    const value2 = list2[index];

    acc.push([value1, value2]);

    return acc;
  }, []);
};
```

### Utilisation
```js
zip([1, 3], [2, 4]); // [[1, 2], [3, 4]]

zip([1, 3, 5], [2, 4]); // [[1, 2], [3, 4]]

zip([1, 3], [2, 4, 5]); // [[1, 2], [3, 4]]

zip(['Decode', 'secret'], ['this', 'message!']);
// [['Decode', 'this'], ['secret', 'message!']]
```

## 4. intersperse
### Paramètres
1. `separator` - Élément à insérer.
2. `list` - Liste d'éléments.

### Description
Insère un séparateur entre chaque élément d'une liste.

### Implémentation
```js
const intersperse = (separator, list) =>
  list.reduce((acc, value, index) => {
    if (index === list.length - 1) {
      acc.push(value);
    } else {
      acc.push(value, separator);
    }

    return acc;
  }, []);
```

### Utilisation
```js
intersperse('Batman', [1, 2, 3, 4, 5, 6]);
// [1, 'Batman', 2, 'Batman', 3, 'Batman', 4, 'Batman', 5, 'Batman', 6]

intersperse('Batman', []);
// []
```

## 5. insert
### Paramètres
1. `index` - Index où insérer l'élément.
2. `newItem` - Élément à insérer.
3. `list` - Liste d'éléments.

### Description
Insère un élément à l'index donné. Si l'index est trop grand, l'élément est inséré à la fin de la liste.

### Implémentation
```js
const insert = (index, newItem, list) => {
  if (index > list.length - 1) {
    return [...list, newItem];
  }

  return list.reduce((acc, value, sourceArrayIndex) => {
    if (index === sourceArrayIndex) {
      acc.push(newItem, value);
    } else {
      acc.push(value);
    }

    return acc;
  }, []);
};
```

### Utilisation
```js
insert(0, 'Batman', [1, 2, 3]);
// ['Batman', 1, 2, 3]

insert(1, 'Batman', [1, 2, 3]);
// [1, 'Batman', 2, 3]

insert(2, ['Batman'], [1, 2, 3]);
// [1, 2, ['Batman'], 3]

insert(10, ['Batman'], [1, 2, 3]);
// [1, 2, 3, ['Batman']]
```

## 6. flatten
### Paramètres
1. `list` - Liste d'éléments.

### Description
Aplatit une liste d'éléments d'un niveau.

### Implémentation
```js
const flatten = (list) => list.reduce((acc, value) => acc.concat(value), []);
```

### Utilisation
```js
flatten([[1, 2], [3, 4]]);
// [1, 2, 3, 4]

flatten([[1, 2], [[3, 4]]]);
// [1, 2, [3, 4]]

flatten([[[1, 2]], [3, 4]]);
// [[1, 2], 3, 4]

flatten([[[1, 2], [3, 4]]]);
// [[1, 2], [3, 4]]
```

## 7. flatMap
### Paramètres
1. `mappingFunction` - Fonction à exécuter sur chaque élément de la liste.
2. `list` - Liste d'éléments.

### Description
Applique une fonction à chaque élément de la liste, puis aplatit le résultat.

### Implémentation
```js
// Un peu de triche, car nous avons déjà implémenté flatten ?
const flatMap = (mappingFunction, list) => flatten(list.map(mappingFunction));
```

### Utilisation
```js
flatMap((n) => [n * 2], [1, 2, 3, 4]);
// [2, 4, 6, 8]

flatMap((n) => [n, n], [1, 2, 3, 4]);
// [1, 1, 2, 2, 3, 3, 4, 4]

flatMap((s) => s.split(' '), ['flatMap', 'should be', 'mapFlat']);
// ['flatMap', 'should', 'be', 'mapFlat']
```

## 8. includes
### Paramètres
1. `item` - Élément à rechercher dans la liste.
2. `list` - Liste d'éléments.

### Description
Vérifie si un élément est présent dans une liste. Si l'élément est trouvé, retourne `true`. Sinon, retourne `false`.

### Implémentation
```js
const includes = (item, list) =>
  list.reduce((isIncluded, value) => isIncluded || item === value, false);
```

### Utilisation
```js
includes(3, [1, 2, 3]); // true
includes(3, [1, 2]); // false
includes(0, []); // false
```

## 9. compact
### Paramètres
1. `list` - Liste d'éléments.

### Description
Supprime les valeurs "falsy" d'une liste.

### Implémentation
```js
const compact = (list) =>
  list.reduce((acc, value) => {
    if (value) {
      acc.push(value);
    }

    return acc;
  }, []);
```

### Utilisation
```js
compact([0, null, 1, undefined, 2, '', 3, false, 4, NaN]);
// [1, 2, 3, 4]
```

## 10. arrayIntoObject
### Paramètres
1. `key` - Chaîne de caractères à utiliser comme clé du nouvel objet.
2. `list` - Liste d'éléments.

### Description
Convertit un tableau en objet, en utilisant la clé donnée comme clé du nouvel objet.

### Implémentation
```js
const arrayIntoObject = (key, list) =>
  list.reduce((acc, obj) => {
    const value = obj[key];

    acc[value] = obj;

    return acc;
  }, {});
```

### Utilisation
```js
const users = [
    { username: 'JX01', status: 'offline' },
    { username: 'yazeedBee', status: 'online' }
];

arrayIntoObject('username', users);
/*
{
  JX01: {
    username: 'JX01',
    status: 'offline'
  },
  yazeedBee: { username: 'yazeedBee', status: 'online' }
}
*/

arrayIntoObject('status', users);
/*
{
  offline: {
    username: 'JX01',
    status: 'offline'
  },
  online: { username: 'yazeedBee', status: 'online' }
}
*/
```

## Vous voulez un coaching gratuit ?
Si vous souhaitez planifier un appel gratuit pour discuter de questions sur le développement Front-End concernant le code, les entretiens, la carrière ou autre chose, [suivez-moi sur Twitter et envoyez-moi un DM](https://twitter.com/yazeedBee).

Après cela, si vous appréciez notre première rencontre, nous pouvons discuter d'un coaching continu pour vous aider à atteindre vos objectifs de développement Front-End !

## Merci d'avoir lu
Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">https://yazeedb.com !</a>

À la prochaine !
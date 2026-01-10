---
title: Comment résoudre le défi Record Collection de freeCodeCamp
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-03-21T18:14:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-the-record-collection-challenge
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/fili-santillan-qp51FQhBnS0-unsplash.jpg
tags:
- name: challenge
  slug: challenge
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
seo_title: Comment résoudre le défi Record Collection de freeCodeCamp
seo_desc: 'freeCodeCamp''s JavaScript certification is filled with hundreds of interactive
  challenges. But one of the hardest ones to tackle for most beginners is the Record
  Collection.

  In this article, I will walk you through Record Collection and help you unde...'
---

La [certification JavaScript de freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) regorge de centaines de défis interactifs. Mais l'un des plus difficiles à relever pour la plupart des débutants est le défi [Record Collection](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/record-collection).

Dans cet article, je vais vous guider à travers [Record Collection](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/record-collection) et vous aider à comprendre comment fonctionnent tous les éléments du défi.

## Comment comprendre les paramètres de la fonction

Les paramètres sont des types spéciaux de variables qui sont passés à la fonction et servent de substituts aux valeurs réelles. Lorsque la fonction est appelée, nous utilisons alors les valeurs réelles, appelées arguments.

Voici un exemple des paramètres de la fonction de [Record Collection](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/record-collection).

```js
function updateRecords(records, id, prop, value)
```

Le paramètre `records` représente un objet littéral. Voici l'objet littéral du défi :

```js
const recordCollection = {
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    albumTitle: '1999',
    artist: 'Prince',
    tracks: ['1999', 'Little Red Corvette']
  },
  1245: {
    artist: 'Robert Palmer',
    tracks: []
  },
  5439: {
    albumTitle: 'ABBA Gold'
  }
};
```

Le paramètre `id` représente les objets imbriqués dans notre objet `recordCollection`. Voici un exemple pour l'un des identifiants.

```js
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
  },
```

Le paramètre `prop` représente le nom de la propriété, ou clé, à l'intérieur des objets. `albumTitle`, `artist` et `tracks` sont tous des exemples de propriétés à l'intérieur des objets `id`.

Le paramètre `value` représente la valeur de la propriété de l'objet. Dans l'exemple ci-dessous, `albumTitle` serait le nom de la propriété, ou clé, tandis que `ABBA Gold` serait la valeur.

```js
albumTitle: 'ABBA Gold'
```

`records`, `id`, `prop` et `value` sont les quatre paramètres que nous allons utiliser à l'intérieur de la fonction.

## Comment aborder les règles du défi

La clé pour réussir ce défi est de décomposer ces quatre règles et de les aborder une par une. Voici les quatre règles que nous devons inclure dans notre fonction :

* Si `prop` n'est pas `tracks` et que `value` n'est pas une chaîne vide, mettez à jour ou définissez la `prop` de cet album à `value`.
* Si `prop` est `tracks` mais que l'album n'a pas de propriété `tracks`, créez un tableau vide et ajoutez-y `value`.
* Si `prop` est `tracks` et que `value` n'est pas une chaîne vide, ajoutez `value` à la fin du tableau `tracks` existant de l'album.
* Si `value` est une chaîne vide, supprimez la propriété `prop` donnée de l'album.

### Comment aborder la première règle

Voici la première règle :

* Si `prop` n'est pas `tracks` et que `value` n'est pas une chaîne vide, mettez à jour ou définissez la `prop` de cet album à `value`.

La première partie de cette règle peut être vue comme une instruction `if`. Dans notre fonction, nous pouvons commencer à écrire la structure de base d'une instruction `if`.

```js
function updateRecords(records, id, prop, value) {
  if (la condition est vraie) {
    // écrire du code
  }
  return records;
}
```

Maintenant, nous devons déterminer quoi écrire pour notre condition ici :

```js
if (la condition est vraie)
```

La première partie de la règle dit : si `prop` n'est pas `tracks`. Nous pouvons reformuler cela par : si `prop` n'est pas égal à `tracks`.

Rappelez-vous que l'opérateur d'inégalité `!==` peut être utilisé pour vérifier si deux opérandes ne sont pas égaux entre eux.

Mais nous ne pouvons pas utiliser `tracks` tel quel dans notre code car nous obtiendrons un message d'erreur.

```js
if(prop !== tracks)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-20-at-12.51.17-AM.png)

Pour supprimer ce message d'erreur, `tracks` doit être une chaîne de caractères.

```js
if(prop !== 'tracks')
```

Mais nous n'avons pas fini avec notre condition car nous devons encore aborder cette partie :

* et `value` n'est pas une chaîne vide

Nous pouvons utiliser à nouveau l'opérateur d'inégalité `!==` pour dire `value !== ""`. Ensuite, nous pouvons remplacer le mot "et" en utilisant l'opérateur ET `&&`.

Voici à quoi ressemble la première condition jusqu'à présent :

```js
  if (prop !== 'tracks' && value !== "") {
    // écrire du code ici
  }
```

Maintenant que nous avons déterminé notre condition, nous devons déterminer ce qui va à l'intérieur. Voici la deuxième partie de cette règle :

* mettez à jour ou définissez la `prop` de cet album à `value`

Nous devons d'abord référencer l'objet littéral entier qui est `records`. Ensuite, nous devons accéder à l'`id` qui représente les albums.

Enfin, nous devons accéder à cette `prop`. Nous allons utiliser la notation à crochets pour accomplir cela.

```js
records[id][prop]
```

La dernière étape consiste à affecter la valeur à la `prop` de l'album. Nous allons utiliser l'opérateur d'affectation `=` pour cela.

```js
records[id][prop] = value
```

Voici à quoi ressemble la première condition complète :

```js
function updateRecords(records, id, prop, value) {
  if (prop !== 'tracks' && value !== "") {
    records[id][prop] = value
  }
  return records;
}
```

### Comment aborder la deuxième règle

Voici la deuxième règle :

* Si `prop` est `tracks` mais que l'album n'a pas de propriété `tracks`, créez un tableau vide et ajoutez-y `value`.

Jetons un coup d'œil à cette première partie ici.

* Si `prop` est `tracks`

Nous pouvons remplacer le mot "est" par l'opérateur d'égalité, car nous vérifions si `prop` est égal à `tracks`.

```js
else if (prop === 'tracks')
```

Voici la deuxième partie de la condition.

* mais l'album n'a pas de propriété `tracks`

Nous devons vérifier si l'album possède une propriété `tracks` et nous pouvons le faire en utilisant la méthode `hasOwnProperty()`.

Voici la syntaxe de base :

```js
objet.hasOwnProperty(prop)
```

L'objet dans ce cas serait `records[id]` car il représente l'album et la propriété serait `"tracks"`.

```js
records[id].hasOwnProperty('tracks')
```

Mais nous devons vérifier si l'album n'a pas la propriété `tracks`. Étant donné que la méthode `hasOwnProperty()` renvoie un booléen (true ou false), nous pouvons écrire ceci :

```js
records[id].hasOwnProperty('tracks') === false
```

Nous pouvons également réécrire cette instruction en utilisant l'opérateur NON `!` comme ceci :

```js
!records[id].hasOwnProperty('tracks')
```

En utilisant l'opérateur NON `!` ici, nous disons essentiellement si quelque chose n'est pas vrai.

Voici à quoi ressemble notre instruction `if` jusqu'à présent :

```js
else if (prop === 'tracks' && records[id].hasOwnProperty('tracks') === false) {
    // écrire du code ici
  }
```

Voici la deuxième partie de la règle :

* créez un tableau vide et ajoutez-y `value`

Nous savons que pour créer un tableau, nous pouvons utiliser des crochets `[]`. Ensuite, nous pouvons y ajouter `value` comme ceci :

```js
[value]
```

La dernière partie consiste à affecter ce tableau à la propriété de l'album comme ceci :

```js
 records[id][prop] = [value]
```

Voici à quoi ressemble la deuxième condition complète :

```js
function updateRecords(records, id, prop, value) {
  if (prop !== 'tracks' && value !== "") {
    records[id][prop] = value
  } else if (prop === 'tracks' && records[id].hasOwnProperty('tracks') === false) {
    records[id][prop] = [value]
  }
  return records;
}
```

### Comment aborder la troisième règle

Voici la troisième règle :

* Si `prop` est `tracks` et que `value` n'est pas une chaîne vide, ajoutez `value` à la fin du tableau `tracks` existant de l'album.

Jetons un coup d'œil à la condition ici :

* Si `prop` est `tracks` et que `value` n'est pas une chaîne vide

Nous savons d'après notre code précédent que "`prop` est `tracks`" peut être réécrit comme `prop === "tracks"`.

Nous pouvons également réécrire "`value` n'est pas une chaîne vide" par `value !== ""`.

Voici à quoi ressemble notre troisième condition jusqu'à présent.

```js
else if (prop === 'tracks' && value !== "") {
    // écrire du code
  }
```

Voici la deuxième partie de la règle :

* ajoutez `value` à la fin du tableau `tracks` existant de l'album.

Nous pouvons utiliser la méthode de tableau `push` qui ajoute des éléments à la fin d'un tableau.

```js
records[id][prop].push(value)
```

Voici à quoi ressemble notre troisième condition complète :

```js
function updateRecords(records, id, prop, value) {
  if (prop !== 'tracks' && value !== "") {
    records[id][prop] = value
  } else if (prop === 'tracks' && records[id].hasOwnProperty('tracks') === false) {
    records[id][prop] = [value]
  } else if (prop === 'tracks' && value !== "") {
    records[id][prop].push(value)
  }
  return records;
}
```

### Comment aborder la quatrième règle

Voici la quatrième et dernière règle.

* Si `value` est une chaîne vide, supprimez la propriété `prop` donnée de l'album.

Jetons un coup d'œil à la première partie ici :

* Si `value` est une chaîne vide,

Nous savons d'après notre code précédent que nous pouvons traduire "`value` est une chaîne vide" par `value === ""`.

Voici à quoi ressemble l'instruction `if` jusqu'à présent :

```js
else if (value === ""){
    // écrire du code
  }
```

Voici la deuxième partie de la règle :

* supprimez la propriété `prop` donnée de l'album.

Si nous devez supprimer une propriété d'un objet, nous pouvons utiliser l'opérateur `delete` de JavaScript.

Voici comment supprimer la prop de l'album :

```js
else if (value === "") {
    delete records[id][prop]
  }
```

Voici à quoi ressemble la fonction complète :

```js
function updateRecords(records, id, prop, value) {
  if (prop !== 'tracks' && value !== "") {
    records[id][prop] = value
  } else if (prop === 'tracks' && records[id].hasOwnProperty('tracks') === false) {
    records[id][prop] = [value]
  } else if (prop === 'tracks' && value !== "") {
    records[id][prop].push(value)
  } else if (value === "") {
    delete records[id][prop]
  }
  return records;
}
```

## Conclusion

J'espère que cette exploration de [Record Collection](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/record-collection) vous a aidé à comprendre comment résoudre le défi. Nous avons couvert de nombreuses méthodes différentes et appris à décomposer un problème en plus petites parties.

Bonne chance pour la suite de votre voyage avec JavaScript.
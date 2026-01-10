---
title: Comment compter les objets dans un tableau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:18:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-count-objects-in-an-array
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a9a740569d1a4ca2696.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: object
  slug: object
- name: toothbrush
  slug: toothbrush
seo_title: Comment compter les objets dans un tableau
seo_desc: 'Knowing how to quickly iterate through an array and count objects is deceptively
  simple. The length() method will tell you the total number of values in the array,
  but what if you only want to count those values based on certain conditions?

  For examp...'
---

Savoir comment parcourir rapidement un tableau et compter les objets est trompeusement simple. La méthode `length()` vous indiquera le nombre total de valeurs dans le tableau, mais que faire si vous souhaitez uniquement compter ces valeurs en fonction de certaines conditions ?

Par exemple, imaginez que vous avez un tableau comme ceci :

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];
```

Et vous souhaitez uniquement compter le nombre d'objets avec `status` défini sur `'0'`.

Comme pour presque tout en programmation, il existe plusieurs façons de procéder. Nous allons passer en revue quelques-unes des méthodes courantes ci-dessous.

## Utiliser une boucle `for`

Probablement la manière la plus simple serait de déclarer une variable `counter`, de parcourir le tableau et d'incrémenter `counter` uniquement si `status` est égal à `'0'` :

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

let counter = 0;
for (let i = 0; i < storage.length; i++) {
  if (storage[i].status === '0') counter++;
}

console.log(counter); // 6
```

Vous pourriez simplifier cela un peu en utilisant une boucle `for...of` :

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

let counter = 0;
for (const obj of storage) {
  if (obj.status === '0') counter++;
}

console.log(counter); // 6
```

De plus, vous pourriez créer une fonction pour faire la même chose si vous avez d'autres tableaux d'objets à compter conditionnellement :

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

function statusCounter(inputs) {
  let counter = 0;
  for (const input of inputs) {
    if (input.status === '0') counter += 1;
  }
  return counter;
}

statusCounter(storage); // 6
```

## Utiliser des méthodes de tableau

JavaScript inclut un ensemble de [méthodes utiles](https://www.freecodecamp.org/news/javascript-standard-objects-arrays/) lors de la manipulation de tableaux. Chacune peut être enchaînée à un tableau et recevoir différents paramètres pour travailler avec lors de l'itération à travers les éléments du tableau.

Les deux méthodes que nous allons examiner sont `filter()` et `reduce()`.

### `filter()`

La méthode filter fait exactement cela – elle parcourt chaque élément du tableau et filtre tous les éléments qui ne répondent pas à la ou aux conditions que vous fournissez. Elle retourne ensuite un nouveau tableau avec tous les éléments qui ont retourné vrai en fonction de votre ou vos conditions.

Par exemple :

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.filter(function(item){
  if (item.status === 0) {
    return true;
  } else {
    return false;
  }
});

/*
[
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' }
] 
*/
```

Maintenant que vous avez filtré l'objet avec `status: '1'`, appelez simplement la méthode `length()` sur le nouveau tableau pour obtenir le nombre total d'objets avec `status: '1'` :

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.filter(function(item){
  if (item.status === 0) {
    return true;
  } else {
    return false;
  }
}).length; // 6
```

Mais cela peut être considérablement raccourci avec la syntaxe ES6 :

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.filter(item => item.status === '0').length; // 6
```

### `reduce()`

Considérez la méthode `reduce()` comme un couteau suisse – elle est extrêmement flexible et vous permet de prendre un tableau en entrée et de le transformer en presque n'importe quoi. Mieux encore, comme `filter()`, cette méthode retourne un nouveau tableau, laissant l'original inchangé.

Vous pouvez en lire plus sur `reduce()` dans [cet article](https://www.freecodecamp.org/news/the-ultimate-guide-to-javascript-array-methods-reduce/).

Pour nos besoins, nous voulons prendre un tableau, examiner son contenu et produire un nombre. Voici une manière simple de faire cela :

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.reduce((counter, obj) => {
  if (obj.status === '0') counter += 1
  return counter;
}, 0); // 6
```

Vous pourriez simplifier davantage en utilisant la syntaxe ES6 et un opérateur ternaire :

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.reduce((counter, obj) => obj.status === '0' ? counter += 1 : counter, 0); // 6
```

Et encore un peu plus en utilisant la [destructuration d'objet](https://www.freecodecamp.org/news/array-and-object-destructuring-in-javascript/) :

```js
const storage = [
  { data: '1', status: '0' },
  { data: '2', status: '0' },
  { data: '3', status: '0' },
  { data: '4', status: '0' },
  { data: '5', status: '0' },
  { data: '6', status: '0' },
  { data: '7', status: '1' },
];

const count = storage.reduce((counter, { status }) => status === '0' ? counter += 1 : counter, 0); // 6
```

Voici donc quelques façons de parcourir les éléments d'un tableau et de les compter conditionnellement. Maintenant, allez-y et comptez avec confiance !
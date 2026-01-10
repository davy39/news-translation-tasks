---
title: Comment découper et épisser des tableaux en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T21:17:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-slice-and-splice-arrays-in-javascript-72bbca45006
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XLAL5nDPpacrVdZ4MhJH2Q.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment découper et épisser des tableaux en JavaScript
seo_desc: 'By Dylan Attal

  .slice() and .splice() are similar methods in JavaScript. They look similar, they
  sound similar, and they do similar things. For those reasons, it’s important to
  know the differences between them. Also, they’re used very often, so unde...'
---

Par Dylan Attal

`.slice()` et `.splice()` sont des méthodes similaires en JavaScript. Elles se ressemblent, elles sonnent de manière similaire, et elles font des choses similaires. Pour ces raisons, il est important de connaître les différences entre elles. De plus, elles sont très souvent utilisées, donc comprendre leur utilisation est bon à apprendre tôt pour tout développeur logiciel.

Dans cet article, nous allons voir comment les utiliser avec un défi spécifique de script d'algorithme. Nous allons insérer des éléments d'un tableau dans un autre et retourner le tableau combiné sans muter les tableaux originaux.

#### Instructions de l'algorithme

> Vous recevez deux tableaux et un index.

> Utilisez les méthodes de tableau `slice` et `splice` pour copier chaque élément du premier tableau dans le second tableau, dans l'ordre.

> Commencez à insérer les éléments à l'index `n` du second tableau.

> Retournez le tableau résultant. Les tableaux d'entrée doivent rester les mêmes après l'exécution de la fonction.

```js
function frankenSplice(arr1, arr2, n) {
  return arr2;
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

#### Cas de test fournis

* `frankenSplice([1, 2, 3], [4, 5], 1)` devrait retourner `[4, 1, 2, 3, 5]`.
* `frankenSplice([1, 2], ["a", "b"], 1)` devrait retourner `["a", 1, 2, "b"]`.
* `frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2)` devrait retourner `["head", "shoulders", "claw", "tentacle", "knees", "toes"]`.
* Tous les éléments du premier tableau doivent être ajoutés au second tableau dans leur ordre original.
* Le premier tableau doit rester le même après l'exécution de la fonction.
* Le second tableau doit rester le même après l'exécution de la fonction.

### Solution #1 : .slice(), .splice(), et opérateur de décomposition

#### PEDAC

**Comprendre le problème** : Nous avons une entrée, une chaîne de caractères. Notre sortie est également une chaîne de caractères. En fin de compte, nous voulons retourner la chaîne d'entrée avec la première lettre — et seulement la première lettre — de chaque mot en majuscule.

**Exemples/Cas de test** : Nos cas de test fournis montrent que nous devrions avoir une lettre majuscule uniquement au début de chaque mot. Nous devons mettre le reste en minuscules. Les cas de test fournis montrent également que nous n'avons pas à gérer des mots composés bizarres séparés par des symboles au lieu d'espaces. C'est une bonne nouvelle pour nous !

**Structure de données** : Nous allons devoir transformer notre chaîne d'entrée en un tableau afin de manipuler chaque mot séparément.

Parlons un peu de `.slice()` et `.splice()` :

Commençons par aborder `[.slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)` :

`.slice()` extrait une section d'une chaîne et la retourne sous forme de nouvelle chaîne. Si vous appelez `.slice()` sur une chaîne sans lui passer d'informations supplémentaires, elle retournera la chaîne entière.

```js
"Bastian".slice()
// retourne "Bastian"
```

Cela nous sera utile dans ce défi de script d'algorithme car les instructions nous disent que nous ne devrions pas modifier directement les tableaux d'entrée. Nous allons donc devoir en faire une copie.

Maintenant, regardons `[.splice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)` :

`.splice()` modifie le contenu d'un tableau en supprimant ou en remplaçant des éléments existants et/ou en ajoutant de nouveaux éléments.

Nous pouvons passer plusieurs arguments à `.splice()` qui déterminent où commence la suppression, combien est supprimé, et ce qui est inséré. `start` est un nombre qui indique à `.splice()` à quel index commencer à supprimer des éléments. `deleteCount` indique à `.splice()` combien d'éléments supprimer.

Attendez une seconde ! Que faire si vous ne voulez pas supprimer quoi que ce soit ? Que faire si vous voulez simplement insérer des éléments ? C'est bien. Il suffit de définir `deleteCount` à zéro. Maintenant, nous pouvons commencer à ajouter des éléments. Il suffit de séparer chaque élément par une virgule, comme ceci `item1, item2, item3, item4`.

```
.splice(start, deleteCount, item1, item2, item3, etc.)
```

Un autre concept à garder à l'esprit pour ce défi de script d'algorithme est l'[opérateur de décomposition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax). ES6 nous a offert l'opérateur de décomposition qui ressemble à des points de suspension — juste trois points à la suite.

L'opérateur de décomposition est le plus couramment utilisé lorsque vous voulez utiliser les éléments d'un tableau comme arguments d'une fonction. C'est exactement ce que nous allons faire avec lui dans ce défi. Nous ne voulons pas insérer le tableau entier `arr1` dans `arr2`. Nous voulons insérer chaque élément de `arr1` dans `arr2`.

**Algorithme** :

1. Créez une copie de `arr2`.
2. Insérez tous les éléments de `arr1` dans `arr2` en commençant à l'index dans `arr2` spécifié par `n`.
3. Retournez les tableaux combinés.

**Code** : Voir ci-dessous !

```js
function frankenSplice(arr1, arr2, n) {
  // Créez une copie de arr2.
  let combinedArrays = arr2.slice()
  //                   [4, 5, 6]

  // Insérez tous les éléments de arr1 dans arr2 en commençant
  // à l'index spécifié par n. Nous utilisons l'opérateur de décomposition
  // "..." pour insérer chaque élément individuel de 
  // arr1 au lieu du tableau entier.
  combinedArrays.splice(n, 0, ...arr1)
  //                   (1, 0, ...[1, 2, 3])
  //                   [4, 1, 2, 3, 5, 6]

  // Retournez les tableaux combinés.
  return combinedArrays
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

Sans commentaires :

```js
function frankenSplice(arr1, arr2, n) {
  let combinedArrays = arr2.slice()
  combinedArrays.splice(n, 0, ...arr1)
  return combinedArrays
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

### Solution #2 : .slice(), .splice(), et boucle for

#### PEDAC

**Comprendre le problème** : Nous avons une entrée, une chaîne de caractères. Notre sortie est également une chaîne de caractères. En fin de compte, nous voulons retourner la chaîne d'entrée avec la première lettre — et seulement la première lettre — de chaque mot en majuscule.

**Exemples/Cas de test** : Nos cas de test fournis montrent que nous devrions avoir une lettre majuscule uniquement au début de chaque mot. Nous devons mettre le reste en minuscules. Les cas de test fournis montrent également que nous n'avons pas à gérer des mots composés bizarres séparés par des symboles au lieu d'espaces. C'est une bonne nouvelle pour nous !

**Structure de données** : Nous allons devoir transformer notre chaîne d'entrée en un tableau afin de manipuler chaque mot séparément.

Parlons un peu de `.slice()` et `.splice()` :

Commençons par aborder `[.slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)` :

`.slice()` extrait une section d'une chaîne et la retourne sous forme de nouvelle chaîne. Si vous appelez `.slice()` sur une chaîne sans lui passer d'informations supplémentaires, elle retournera la chaîne entière.

```js
"Bastian".slice()
// retourne "Bastian"
```

Cela nous sera utile dans ce défi de script d'algorithme car les instructions nous disent que nous ne devrions pas modifier directement les tableaux d'entrée. Nous allons donc devoir en faire une copie.

Maintenant, regardons `[.splice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)` :

`.splice()` modifie le contenu d'un tableau en supprimant ou en remplaçant des éléments existants et/ou en ajoutant de nouveaux éléments.

Nous pouvons passer plusieurs arguments à `.splice()` qui déterminent où commence la suppression, combien est supprimé, et ce qui est inséré. `start` est un nombre qui indique à `.splice()` à quel index commencer à supprimer des éléments. `deleteCount` indique à `.splice()` combien d'éléments supprimer. Attendez une seconde ! Que faire si vous ne voulez pas supprimer quoi que ce soit ? Que faire si vous voulez simplement insérer des éléments ? C'est bien. Il suffit de définir `deleteCount` à zéro. Maintenant, nous pouvons commencer à ajouter des éléments. Il suffit de séparer chaque élément par une virgule, comme ceci `item1, item2, item3, item4`.

```
.splice(start, deleteCount, item1, item2, item3, etc.)
```

Contrairement à la solution précédente, nous n'utiliserons pas l'opérateur de décomposition ici. Nous utiliserons une boucle for pour extraire chaque élément un par un de `arr1` et les insérer dans `arr2`.

Le truc ici est d'incrémenter `n` de 1 à chaque fois que la boucle s'exécute, sinon les éléments de `arr1` ne se retrouveront pas dans le bon ordre lorsqu'ils seront insérés dans `arr2`.

**Algorithme** :

1. Créez une copie de `arr2`.
2. En utilisant une boucle for, insérez chaque élément de `arr1` dans `arr2` en commençant à l'index `n`.
3. Incrémentez `n` de 1 à chaque fois que la boucle s'exécute.
4. Retournez les tableaux combinés.

**Code** : Voir ci-dessous !

```js
function frankenSplice(arr1, arr2, n) {
  // Créez une copie de arr2.
  let combinedArrays = arr2.slice()
  // En utilisant une boucle for, insérez chaque élément de arr1
  // dans combinedArrays en commençant à l'index n.
  for (let i = 0; i < arr1.length; i++) {
      combinedArrays.splice(n, 0, arr1[i])
  //       [4, 5, 6].splice(1, 0, 1)
  //    [4, 1, 5, 6].splice(2, 0, 2)
  // [4, 1, 2, 5, 6].splice(3, 0, 3)
  // [4, 1, 2, 3, 5, 6]

  //  incrémentez n de 1 à chaque fois que la boucle s'exécute
      n++
  }
  // Retournez les tableaux combinés.
  return combinedArrays
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

Sans commentaires :

```js
function frankenSplice(arr1, arr2, n) {
  let combinedArrays = arr2.slice()
  for (let i = 0; i < arr1.length; i++) {
    combinedArrays.splice(n, 0, arr1[i])
    n++
  }
  return combinedArrays
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

Si vous avez d'autres solutions et/ou suggestions, n'hésitez pas à les partager dans les commentaires !

#### Cet article fait partie de la série [freeCodeCamp Algorithm Scripting](https://medium.com/@DylanAttal/freecodecamp-algorithm-scripting-b96227b7f837).

#### Cet article référence [freeCodeCamp Basic Algorithm Scripting: Slice and Splice](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/slice-and-splice)

Vous pouvez me suivre sur [Medium](https://medium.com/@DylanAttal), [LinkedIn](https://www.linkedin.com/in/dylanattal/), et [GitHub](https://github.com/DylanAttal) !
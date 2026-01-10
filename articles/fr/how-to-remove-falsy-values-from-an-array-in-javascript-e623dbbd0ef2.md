---
title: Comment supprimer les valeurs falsy d'un tableau en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-12T17:43:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-falsy-values-from-an-array-in-javascript-e623dbbd0ef2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ArHOj9iu7kJxxEhRukDKJw.jpeg
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
seo_title: Comment supprimer les valeurs falsy d'un tableau en JavaScript
seo_desc: 'By Dylan Attal

  There are a lot of ways to remove elements from an array in JavaScript, but what’s
  the easiest way to remove all falsy values from an array? In order to answer that
  question we’ll take a close look at truthy versus falsy values and typ...'
---

Par Dylan Attal

Il existe de nombreuses façons de supprimer des éléments d'un tableau en JavaScript, mais quelle est la manière la plus simple de supprimer toutes les valeurs falsy d'un tableau ? Pour répondre à cette question, nous allons examiner de près les valeurs truthy et falsy ainsi que la coercition de type dans le contexte d'un défi d'algorithme.

#### Instructions de l'algorithme

> Supprimer toutes les valeurs falsy d'un tableau.

> Les valeurs falsy en JavaScript sont `false`, `null`, `0`, `""`, `undefined`, et `NaN`.

> Indice : Essayez de convertir chaque valeur en booléen.

#### Cas de test fournis

* `bouncer([7, "ate", "", false, 9])` devrait retourner `[7, "ate", 9]`.
* `bouncer(["a", "b", "c"])` devrait retourner `["a", "b", "c"]`.
* `bouncer([false, null, 0, NaN, undefined, ""])` devrait retourner `[]`.
* `bouncer([1, null, NaN, 2, undefined])` devrait retourner `[1, 2]`.

### Solution #1 : .filter() et Boolean()

#### PEDAC

**Comprendre le problème** : Nous avons une entrée, un tableau. Notre objectif est de supprimer toutes les valeurs falsy du tableau puis de retourner le tableau.

Les bonnes personnes de freeCodeCamp nous ont dit que les valeurs falsy en JavaScript sont `false`, `null`, `0`, `_""_`, `undefined`, et `NaN`.

Ils nous ont également donné un indice majeur ! Ils suggèrent de convertir chaque valeur du tableau en booléen afin de relever ce défi. Je pense que c'est un excellent indice !

**Exemples/Cas de test** : Nos cas de test fournis montrent que si le tableau d'entrée ne contient que des valeurs falsy, alors nous devons simplement retourner un tableau vide. C'est assez simple.

**Structure de données** : Nous allons rester avec les tableaux ici.

Parlons de `[.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)` :

`.filter()` crée un nouveau tableau avec tous les éléments qui passent le test implémenté par la fonction fournie.

En d'autres termes, `.filter()` parcourt chaque élément d'un tableau et conserve tous les éléments qui passent un certain test. Tous les éléments du tableau qui échouent à ce test sont filtrés — ils sont supprimés.

Par exemple, si nous avions un tableau de nombres et que nous voulions uniquement les nombres supérieurs à 100, nous pourrions utiliser `.filter()` pour accomplir cela :

```
let numbers = [4, 56, 78, 99, 101, 150, 299, 300]
numbers.filter(number => number > 100)
// retourne [ 101, 150, 299, 300 ]
```

Parlons de l'indice de conversion de chaque élément en booléen. C'est un bon indice car nous pouvons utiliser `.filter()` pour retourner le tableau avec uniquement les valeurs truthy.

Nous allons accomplir cela grâce à la [conversion de type JavaScript](https://www.w3schools.com/js/js_type_conversion.asp).

JavaScript nous offre des fonctions utiles pour convertir un type de données en un autre. `String()` convertit en chaîne de caractères, `Number()` convertit en nombre, et `Boolean()` convertit en booléen.

Par exemple :

```
String(1234)
// retourne "1234"
```

```
Number("47")
// retourne 47
```

```
Boolean("meow")
// retourne true
```

`Boolean()` est la fonction que nous allons implémenter avec ce défi. Si l'argument fourni à `Boolean()` est truthy, alors `Boolean()` retournera `true`. Si l'argument fourni à `Boolean()` est falsy, alors `Boolean()` retournera `false`.

Cela nous est utile car nous savons, d'après les instructions, que seules les valeurs `false`, `null`, `0`, `_""_`, `undefined`, et `NaN` sont falsy en JavaScript. Toutes les autres valeurs sont truthy. Sachant cela, si nous convertissons chaque valeur du tableau d'entrée en booléen, nous pouvons supprimer tous les éléments qui évaluent à `false`, et cela satisfera les exigences de ce défi.

**Algorithme** :

1. Déterminer quelles valeurs dans `arr` sont falsy.
2. Supprimer toutes les valeurs falsy.
3. Retourner le nouveau tableau qui ne contient que des valeurs truthy.

**Code** : Voir ci-dessous !

Sans commentaires et en supprimant la variable locale :

Si vous avez d'autres solutions et/ou suggestions, n'hésitez pas à les partager dans les commentaires !

#### Cet article fait partie de la série [freeCodeCamp Algorithm Scripting](https://medium.com/@DylanAttal/freecodecamp-algorithm-scripting-b96227b7f837).

#### Cet article référence [freeCodeCamp Basic Algorithm Scripting : Falsy Bouncer](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/falsy-bouncer).

Vous pouvez me suivre sur [Medium](https://medium.com/@DylanAttal), [LinkedIn](https://www.linkedin.com/in/dylanattal/), et [GitHub](https://github.com/DylanAttal) !
---
title: JavaScript Array Sort – Comment Utiliser les Méthodes de Tri JS (Avec des Exemples
  de Code)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-24T19:34:05.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-sort-tutorial-how-to-use-js-sort-methods-with-code-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ad9740569d1a4ca2820.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Array Sort – Comment Utiliser les Méthodes de Tri JS (Avec des
  Exemples de Code)
seo_desc: "By Cem Eygi\nIn JavaScript, we can sort the elements of an array easily\
  \ with a built-in method called the sort( ) function. \nHowever, data types (string,\
  \ number, and so on) can differ from one array to another. This means that using\
  \ the sort( ) method..."
---

Par Cem Eygi

En JavaScript, nous pouvons trier les éléments d'un tableau facilement avec une méthode intégrée appelée la fonction sort().

Cependant, les types de données (chaîne de caractères, nombre, etc.) peuvent différer d'un tableau à l'autre. Cela signifie que l'utilisation de la méthode sort() seule n'est pas toujours une solution appropriée.

Dans cet article, vous apprendrez comment trier un tableau en JavaScript en utilisant la méthode sort() pour les chaînes de caractères et les nombres.

## Tableau de Chaînes de Caractères

Commençons par les chaînes de caractères :

```javascript
const teams = ['Real Madrid', 'Manchester Utd', 'Bayern Munich', 'Juventus'];
```

Lorsque nous utilisons la méthode sort(), les éléments seront triés par ordre croissant (A à Z) par défaut :

```javascript
teams.sort();

// ['Bayern Munich', 'Juventus', 'Manchester Utd', 'Real Madrid']
```

Si vous préférez trier le tableau par ordre décroissant, vous devez utiliser la méthode reverse() à la place :

```javascript
teams.reverse();

// ['Real Madrid', 'Manchester Utd', 'Juventus', 'Bayern Munich']
```

## Tableau de Nombres

Le tri des nombres n'est malheureusement pas aussi simple. Si nous appliquons la méthode sort directement à un tableau de nombres, nous obtiendrons un résultat inattendu :

```javascript
const numbers = [3, 23, 12];

numbers.sort(); // --> 12, 23, 3
```

### Pourquoi la méthode sort() ne fonctionne pas pour les nombres

En réalité, elle fonctionne, mais ce problème se produit parce que JavaScript trie les nombres par ordre alphabétique. Laissez-moi expliquer cela en détail.

Imaginons que A=1, B=2 et C=3.

```javascript
const myArray = ['C', 'BC', 'AB'];

myArray.sort(); // [AB, BC, C]
```

Par exemple, si nous avons trois chaînes de caractères C (3), BC (23) et AB (12), JavaScript les triera comme AB, BC et C par ordre croissant, ce qui est alphabétiquement correct.

Cependant, JavaScript triera les nombres (encore alphabétiquement) comme 12, 23 et 3, ce qui est incorrect.

### Solution : La Fonction de Comparaison

Heureusement, nous pouvons soutenir la méthode sort() avec une fonction de comparaison basique qui fera l'affaire :

```javascript
function(a, b) {return a - b}
```

La méthode sort peut, heureusement, trier les valeurs négatives, nulles et positives dans le bon ordre. Lorsque la méthode sort() compare deux valeurs, elle envoie les valeurs à notre fonction de comparaison et trie les valeurs selon la valeur retournée.

* Si le résultat est négatif, a est trié avant b.
* Si le résultat est positif, b est trié avant a.
* Si le résultat est 0, rien ne change.

Tout ce que nous devons faire est d'utiliser la fonction de comparaison à l'intérieur de la méthode sort() :

```javascript
const numbers = [3, 23, 12];

numbers.sort(function(a, b){return a - b}); // --> 3, 12, 23
```

Si nous voulons trier les nombres par ordre décroissant, cette fois nous devons soustraire le deuxième paramètre (b) du premier (a) :

```javascript
const numbers = [3, 23, 12];

numbers.sort(function(a, b){return b - a}); // --> 23, 12, 3
```

## Conclusion

Comme nous pouvons le voir, le tri des éléments d'un tableau peut être fait facilement en JavaScript avec la méthode sort(), si nous savons comment l'utiliser correctement. J'espère que mon article vous aide à comprendre comment utiliser la méthode sort() en JavaScript de la bonne manière.

**Si vous voulez en savoir plus sur le développement Web, n'hésitez pas à visiter ma [chaîne YouTube](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q?view_as=subscriber).**

Merci pour votre lecture !
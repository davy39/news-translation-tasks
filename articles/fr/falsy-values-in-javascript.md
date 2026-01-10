---
title: Valeurs Falsy en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-14T00:09:00.000Z'
originalURL: https://freecodecamp.org/news/falsy-values-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb6740569d1a4ca3ea5.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Valeurs Falsy en JavaScript
seo_desc: 'Description

  A falsy value is something which evaluates to FALSE, for instance when checking
  a variable. There are only six falsey values in JavaScript: undefined, null, NaN,
  0, "" (empty string), and false of course.

  Checking for falsy values on vari...'
---

## **Description**

Une valeur falsy est quelque chose qui évalue à FAUX, par exemple lors de la vérification d'une variable. Il n'y a que six valeurs falsy en JavaScript : `undefined`, `null`, `NaN`, `0`, `""` (chaîne vide), et bien sûr `false`.

## **Vérification des valeurs falsy sur les variables**

Il est possible de vérifier une valeur falsy dans une variable avec une simple condition :

```javascript
if (!variable) {
  // Lorsque la variable a une valeur falsy, la condition est vraie.
}
```

## **Exemples généraux**

```javascript
var string = ""; // <-- falsy

var filledString = "some string in here"; // <-- truthy

var zero = 0; // <-- falsy

var numberGreaterThanZero // <-- truthy

var emptyArray = []; // <-- truthy, nous explorerons cela plus en détail ensuite

var emptyObject = {}; // <-- truthy
```

## **Amusement avec les tableaux**

```javascript
if ([] == false) // <-- truthy, exécutera le code dans le bloc if

if ([]) // <-- truthy, exécutera également le code dans le bloc if

if ([] == true) // <-- falsy, n'exécutera PAS le code dans le bloc if

if (![]) // <-- falsy, n'exécutera également PAS le code dans le bloc if
```

## **Attention**

Soyez conscient du type de données lors de l'évaluation d'une valeur dans un contexte booléen. Si le type de données de la valeur est censé être un _nombre_, l'évaluation truthy/falsy peut entraîner un résultat inattendu :

```javascript
const match = { teamA: 0, teamB: 1 }
if (match.teamA)
  // Ce qui suit ne s'exécutera pas en raison de l'évaluation falsy
  console.log('Team A: ' + match.teamA);
}
```

Une alternative à ce cas d'utilisation consiste à évaluer la valeur en utilisant `typeof` :

```javascript
const match = { teamA: 0, teamB: 1 }
if (typeof match.teamA === 'number')
  console.log('Team A: ' + match.teamA);
}
```

## **Plus d'informations**

* [**truthy**](http://james.padolsey.com/javascript/truthy-falsey/) | Article de blog - Truthy & Falsey
* [Falsy | Glossaire | MDN](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
* [Truthy et Falsy : Quand tout n'est pas égal en JavaScript](https://www.sitepoint.com/javascript-truthy-falsy/)
---
title: Présentation des nouvelles fonctionnalités qu'ECMAScript 2016 (ES7) ajoute
  à JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-14T16:10:59.000Z'
originalURL: https://freecodecamp.org/news/ecmascript-2016-es7-features-86903c5cab70
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UdGS7qrmIMueYfILnJJ6QA.png
tags:
- name: ES6
  slug: es6
- name: es7
  slug: es7
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Présentation des nouvelles fonctionnalités qu'ECMAScript 2016 (ES7) ajoute
  à JavaScript
seo_desc: 'By Sanket Meghani

  Since ECMAScript 2015 (also known as ES6) was released, it has introduced a huge
  set of new features. They include arrow functions, sets, maps, classes and destructuring,
  and much more. In many ways, ES2015 is almost like learning a...'
---

Par Sanket Meghani

Depuis la sortie d'ECMAScript 2015 (également connu sous le nom d'ES6), il a introduit un énorme ensemble de nouvelles fonctionnalités. Elles incluent les fonctions fléchées, les ensembles, les maps, les classes et la destructuration, et bien plus encore. À bien des égards, ES2015 est presque comme apprendre une nouvelle version de JavaScript.

Le Comité Technique 39 d'Ecma gouverne la spécification ECMA. Ils ont décidé de publier une nouvelle version d'ECMAScript chaque année à partir de 2015. Une mise à jour annuelle signifie plus de grosses versions comme ES6.

ECMAScript 2016 a introduit seulement deux nouvelles fonctionnalités :

* Array.prototype.includes()

* Opérateur d'exponentiation

### Array.prototype.includes()

`Array.prototype.includes()` vérifie le tableau pour la `valeur` passée en tant qu'`argument`. Il retourne `true` si le tableau contient la `valeur`, sinon, il retourne `false`.

Auparavant, nous devions utiliser `Array.prototype.indexOf()` pour vérifier si le tableau donné contient un élément ou non.

```javascript
let numbers = [1, 2, 3, 4];

if(numbers.indexOf(2) !== -1) {
  console.log('Array contains value');
}
```

Avec ECMA2016, nous pouvons écrire :

```javascript
if (numbers.includes(2)) {
  console.log('Array contains value');
}
```

`Array.prototype.includes()` gère `NaN` mieux que `Array.prototype.indexOf()`. Si le tableau contient `NaN`, alors `indexOf()` ne retourne pas un index correct lors de la recherche de `NaN`.

`Array.prototype.includes()` retourne la valeur correcte lors de la recherche de `NaN`.

`NaN` est une propriété de l'objet global JavaScript et représente une valeur qui n'est pas un nombre. Il existe des comportements connus lors de la [comparaison de `NaN` à une autre valeur](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN). Ceux-ci sont traités dans `Array.prototype.includes()`, mais pas dans `Array.protoype.indexOf`.

```javascript
let numbers = [1, 2, 3, 4, NaN];

console.log(numbers.indexOf(NaN)); //Affiche -1
console.log(numbers.includes(NaN)); //Affiche true
```

### Opérateur d'exponentiation

JavaScript prend déjà en charge de nombreux opérateurs arithmétiques comme `+, -, *` et plus.

ECMAScript 2016 a introduit l'opérateur d'exponentiation, `**`.

Il a le même but que `Math.pow()`. Il retourne le premier argument élevé à la puissance du second argument.

```javascript
let base = 3;
let exponent = 4;
let result = base**exponent;

console.log(result); //81
```

### Conclusion

Les nouvelles fonctionnalités introduites par ECMA2016 offrent des alternatives pratiques aux fonctionnalités existantes.

En regardant vers l'avenir, ECMA2017 a été finalisé en juin de cette année. Les nouvelles fonctionnalités incluent `async/await`, `SharedArrayBuffer` et quelques méthodes utiles pour `Object.prototype`.
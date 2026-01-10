---
title: Vérification de Null en JS – Vérification de Null en JavaScript Expliquée
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-29T20:16:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-for-null-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover-template--22-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Vérification de Null en JS – Vérification de Null en JavaScript Expliquée
seo_desc: 'Null is a primitive type in JavaScript. This means you are supposed to
  be able to check if a variable is null with the typeof() method. But unfortunately,
  this returns “object” because of an historical bug that cannot be fixed.

  let userName = null;


  ...'
---

Null est un type primitif en JavaScript. Cela signifie que vous devriez pouvoir vérifier si une variable est `null` avec la méthode `typeof()`. Mais malheureusement, cela retourne « object » à cause d'un [bug historique](https://www.turbinelabs.com/blog/the-odd-history-of-javascripts-null) qui ne peut pas être corrigé.

```js
let userName = null;

console.log(typeof(userName)); // object
```

Alors, comment pouvez-vous vérifier null maintenant ? Cet article vous apprendra à vérifier null, ainsi que la différence entre le type null et undefined en JavaScript.

## Null vs Undefined en JavaScript

Null et undefined sont très similaires en JavaScript et sont tous deux des types primitifs.

Une variable a le type `null` si elle contient intentionnellement la valeur `null`. En revanche, une variable a le type `undefined` lorsque vous la déclarez sans initialiser de valeur.

```js
// Ceci est null
let firstName = null;

// Ceci est undefined
let lastName;
```

Undefined fonctionne bien car lorsque vous vérifiez le type en utilisant la méthode `typeof()`, elle retournera `undefined` :

```js
let lastName;

console.log(typeof(lastName)); // undefined
```

Voyons maintenant les deux principales façons de vérifier `null` et comment cela se rapporte à `undefined`.

## Comment vérifier Null en JavaScript avec les opérateurs d'égalité

Les opérateurs d'égalité fournissent le meilleur moyen de vérifier `null`. Vous pouvez utiliser soit l'opérateur d'égalité large/double (`==`), soit l'opérateur d'égalité stricte/triple (`===`).

### Comment utiliser l'opérateur d'égalité large pour vérifier null

Vous pouvez utiliser l'opérateur d'égalité large pour vérifier les valeurs `null` :

```js
let firstName = null;

console.log(firstName == null); // true
```

Mais cela peut être trompeur car si la variable est undefined, cela retournera également `true` car `null` et `undefined` sont largement égaux.

```js
let firstName = null;
let lastName;

console.log(firstName == null); // true
console.log(lastName == null); // true
console.log(firstName == undefined); // true
console.log(lastName == undefined); // true
console.log(firstName == lastName); // true
console.log(null == undefined); // true
```

**Note :** Cela peut être utile lorsque vous voulez vérifier si une variable n'a pas de valeur car lorsqu'une variable n'a pas de valeur, elle peut être soit `null`, soit `undefined`.

Mais supposons que vous voulez seulement vérifier `null` – alors vous pouvez utiliser l'opérateur d'égalité stricte.

### Comment utiliser l'opérateur d'égalité stricte pour vérifier null

L'opérateur d'égalité stricte, comparé à l'opérateur d'égalité large, ne retournera `true` que lorsque vous avez exactement une valeur `null`. Sinon, il retournera `false` (ceci inclut `undefined`).

```js
let firstName = null;
let lastName;

console.log(firstName === null); // true
console.log(lastName === null); // false
console.log(firstName === undefined); // false
console.log(lastName === undefined); // true
console.log(firstName === lastName); // false
console.log(null === undefined); // false
```

Comme vous pouvez le voir, il ne retourne `true` que lorsqu'une variable null est comparée avec `null`, et qu'une variable undefined est comparée avec `undefined`.

## Comment vérifier Null en JavaScript avec la méthode `Object.is()`

`Object.is()` est une méthode ES6 qui détermine si deux valeurs sont identiques. Cela fonctionne comme l'opérateur d'égalité stricte.

```js
// Syntaxe
Object.is(value1, value2)
```

Utilisons l'exemple précédent pour voir si cela fonctionne comme l'opérateur d'égalité stricte :

```js
let firstName = null;
let lastName;

console.log(Object.is(firstName, null)); // true
console.log(Object.is(lastName, null)); // false
console.log(Object.is(firstName, undefined)); // false
console.log(Object.is(lastName, undefined)); // true
console.log(Object.is(firstName, lastName)); // false
console.log(Object.is(null, undefined)); // false
```

Cela se produit car il ne retourne `true` que lorsque les deux valeurs sont identiques. Cela signifie qu'il ne retournera `true` que lorsqu'une variable définie sur `null` est comparée avec `null`, et qu'une variable undefined est comparée avec `undefined`.

## Conclusion

Maintenant, vous savez comment vérifier null avec confiance. Vous pouvez également vérifier si une variable est définie sur `null` ou `undefined`, et vous connaissez la différence entre les opérateurs d'égalité large et stricte.

J'espère que cela vous a été utile. Bon codage !
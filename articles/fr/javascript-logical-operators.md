---
title: Opérateurs logiques JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T22:24:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-logical-operators
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9df5740569d1a4ca3a9c.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Opérateurs logiques JavaScript
seo_desc: 'Logical operators compare Boolean values and return a Boolean response.
  There are two types of logical operators - Logical AND, and Logical OR. These operators
  are often written as && for AND, and || for OR.

  Logical AND ( && )

  The AND operator compar...'
---

Les opérateurs logiques comparent des valeurs booléennes et retournent une réponse booléenne. Il existe deux types d'opérateurs logiques - ET logique et OU logique. Ces opérateurs sont souvent écrits && pour ET et || pour OU.

## ET logique ( && )

L'opérateur ET compare deux expressions. Si la première est évaluée comme ["truthy"](https://developer.mozilla.org/en-US/docs/Glossary/Truthy), l'instruction retournera la valeur de la deuxième expression. Si la première est évaluée comme ["falsy"](https://developer.mozilla.org/en-US/docs/Glossary/Falsy), l'instruction retournera la valeur de la première expression.

Lorsqu'il ne s'agit que de valeurs booléennes (soit `true` soit `false`), il retourne true uniquement si les deux expressions sont vraies. Si une ou les deux expressions sont fausses, l'instruction entière retournera false.

```js
true && true // retourne la deuxième valeur, true
true && false // retourne la deuxième valeur, false
false && false // retourne la première valeur, false
123 && 'abc' // retourne la deuxième valeur, 'abc'
'abc' && null // retourne la deuxième valeur, null
undefined && 'abc' // retourne la première valeur, undefined
0 && false // retourne la première valeur, 0
```

## OU logique ( || )

L'opérateur OU compare deux expressions. Si la première est évaluée comme "falsy", l'instruction retournera la valeur de la deuxième expression. Si la première est évaluée comme "truthy", l'instruction retournera la valeur de la première expression.

Lorsqu'il ne s'agit que de valeurs booléennes (soit `true` soit `false`), il retourne true si l'une ou l'autre des expressions est vraie. Les deux expressions peuvent être vraies, mais une seule est nécessaire pour obtenir true comme résultat.

```js
true || true // retourne la première valeur, true
true || false // retourne la première valeur, true
false || false // retourne la deuxième valeur, false
123 || 'abc' // retourne la première valeur, 123
'abc' || null // retourne la première valeur, 'abc'
undefined || 'abc' // retourne la deuxième valeur, 'abc'
0 || false // retourne la deuxième valeur, false
```

## Évaluation en court-circuit

&& et || se comportent comme des opérateurs en court-circuit.

Dans le cas du ET logique, si le premier opérande retourne false, le deuxième opérande n'est jamais évalué et le premier opérande est retourné.

Dans le cas du OU logique, si la première valeur retourne true, la deuxième valeur n'est jamais évaluée et le premier opérande est retourné.

## NON logique (!)

L'opérateur NON ne fait aucune comparaison comme les opérateurs ET et OU. De plus, il n'opère que sur un seul opérande.

Un point d'exclamation '!' est utilisé pour représenter l'opérateur NON.

## Utilisation des opérateurs NON

1. Conversion de l'expression en booléen.
2. Retourne l'inverse de la valeur booléenne obtenue à l'étape précédente.

```js
var spam = 'rinki'; // spam peut être égal à n'importe quelle chaîne non vide
var booSpam = !spam;
/* retourne false
  puisque lorsqu'une chaîne non vide est convertie en booléen, elle retourne true
  l'inverse de laquelle est évalué à false.
*/

var spam2 = ''; // spam2 est ici égal à une chaîne vide
var booSpam2 = !spam2;
/* retourne true
  puisque lorsqu'une chaîne vide est convertie en booléen, elle retourne false
  l'inverse de laquelle est évalué à true.
*/
```

### Conseils :

Les deux opérateurs logiques retourneront la valeur de la dernière expression évaluée. Par exemple :

```js
"cat" && "dog" // retourne "dog"
"cat" && false // retourne false
0 && "cat"  // retourne 0 (qui est une valeur falsy)

"cat" || "dog" // retourne "cat"
"cat" || false // retourne "cat"
0 || "cat" // retourne "cat"
```

Notez que là où `&&` retourne la première valeur, `||` retourne la deuxième valeur et vice versa.
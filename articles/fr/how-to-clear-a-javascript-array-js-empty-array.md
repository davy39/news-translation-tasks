---
title: Comment vider un tableau JavaScript – JS Empty Array
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-27T15:53:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-clear-a-javascript-array-js-empty-array
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/clear-an-array.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment vider un tableau JavaScript – JS Empty Array
seo_desc: 'By Dillion Megida

  There are multiple ways to empty an existing array in JavaScript. Emptying an array
  means removing all values from it.

  In this article, I''ll show and explain two ways to clear an array.

  1. How to Clear an Array by Modifying the Leng...'
---

Par Dillion Megida

Il existe plusieurs façons de vider un tableau existant en JavaScript. Vider un tableau signifie supprimer toutes les valeurs qu'il contient.

Dans cet article, je vais montrer et expliquer deux façons de vider un tableau.

## 1. Comment vider un tableau en modifiant la propriété Length

La propriété length d'un tableau est **lisible** et **modifiable**. 

Lorsque vous lisez la propriété (`array.length`), elle retourne la longueur du tableau, qui est le nombre de valeurs qu'il contient. Lorsque vous modifiez la propriété (c'est-à-dire que vous la modifiez, comme `array.length = 10`), elle change la longueur du tableau et le nombre de valeurs qu'il contient.

Si la longueur modifiée est plus petite que la longueur originale, les valeurs en excès seront supprimées. Voici ce que je veux dire :

```js
const array = [1, 2, 3]
array.length = 2

console.log(array)
// [1, 2]
```

Parce que la nouvelle longueur est plus petite que l'originale, la valeur en excès (**3**, dans ce cas) est supprimée.

Cependant, si la nouvelle longueur est plus grande que la longueur originale, le tableau sera rempli avec des valeurs `undefined` pour compenser la nouvelle longueur :

```js
const array = [1, 2, 3]
array.length = 4

console.log(array)
// [1, 2, 3, undefined]
```

Maintenant que vous comprenez comment utiliser la propriété `length` pour modifier un tableau, voici comment vider un tableau :

```js
const array = [1, 2, 3]
array.length = 0

console.log(array)
// []
```

Avec une longueur de 0, toutes les valeurs du tableau sont supprimées, et le tableau devient vide.


## 2. Comment vider un tableau en réassignant des valeurs

Vous pouvez réassigner une nouvelle valeur (un tableau vide) à une variable qui avait initialement un tableau non vide assigné.

Si vous déclarez une variable avec `const`, vous ne pouvez pas la réassigner :

```js
const array = [1, 2, 3]
array = []

console.log(array)
```

Le code ci-dessus générera une erreur **TypeError: Assignment to constant variable**. Mais si vous avez déclaré cette variable avec `let`, alors vous pouvez la réassigner avec une valeur de tableau vide :

```js
let array = [1, 2, 3]
array = []

console.log(array)
// []
```

Maintenant, vous avez un tableau vide.

Merci d'avoir lu, et bon codage !
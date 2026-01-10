---
title: Comment fusionner des tableaux en JavaScript – Concatenation de tableaux en
  JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-28T15:37:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-merge-arrays-in-javascript-array-concatenation-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/7.-merge-arrays.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment fusionner des tableaux en JavaScript – Concatenation de tableaux
  en JS
seo_desc: 'By Dillion Megida

  There are multiple ways to merge arrays in JavaScript. You can use long or short
  approaches. I''ll be showing 3 of them in this article.

  When working with arrays in JavaScript, there are cases where you want to combine
  multiple array...'
---

Par Dillion Megida

Il existe plusieurs façons de fusionner des tableaux en JavaScript. Vous pouvez utiliser des approches longues ou courtes. Je vais vous montrer 3 d'entre elles dans cet article.

Lorsque vous travaillez avec des tableaux en JavaScript, il arrive que vous souhaitiez combiner plusieurs tableaux ensemble. Par exemple, des tableaux contenant des données liées provenant de différentes sources peuvent être fusionnés en un seul tableau.

Vous pouvez fusionner des tableaux de différentes manières. Examinons certaines d'entre elles, de ma préférée à ma moins préférée.

Voici une [version vidéo](https://youtu.be/YcPHJLc8ZDY) de cet article si vous souhaitez l'utiliser pour compléter votre apprentissage.

## 1. Comment utiliser l'opérateur de décomposition en JavaScript

L'opérateur de décomposition vous permet de décomposer une collection itérable (objet ou tableau) dans une autre collection. En utilisant cet opérateur sur des tableaux, vous pouvez fusionner le contenu des tableaux ensemble.

Voici un exemple :

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]

const merged = [...array1, ...array2]
// [1, 2, 3, 4, 5, 6]
```

Pour la variable `merged`, nous créons un nouveau tableau puis nous décomposons les valeurs de `array1` suivies de `array2`. Maintenant, vous pouvez voir le tableau `merged` contenant les valeurs de ces tableaux.

Vous pouvez utiliser cet opérateur pour plusieurs tableaux :

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]
const array3 = [7, 8, 9]

const merged = [...array2, ...array3, ...array1]
// [4, 5, 6, 7, 8, 9, 1, 2, 3]
```

Dans le tableau `merged` ici, nous décomposons d'abord `array2`, puis `array3`, et enfin `array1`.

Vous pouvez en apprendre plus sur cet opérateur dans cet article : [Spread Operator Simplified](https://dillionmegida.com/p/spread-operator-simplified/).

## 2. Comment utiliser `Array.concat` en JavaScript

Vous utilisez la méthode `concat` des tableaux pour combiner le contenu d'un tableau avec de nouvelles valeurs pour former un nouveau tableau.

Ces nouvelles valeurs peuvent être des nombres, des chaînes de caractères, des booléens, des objets, ou même des tableaux.

La méthode accepte une liste de valeurs comme arguments :

```js
array.concat(value1, value2, ..., valueN)
```

En spécifiant un tableau comme argument, vous pouvez fusionner un tableau existant avec le tableau spécifié pour former un nouveau tableau. Voici un exemple :

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]

const merged = array1.concat(array2)
// [1, 2, 3, 4, 5, 6]
```

Comme vous pouvez le voir, le contenu de `array1` est concaténé avec le contenu de `array2` pour former un nouveau tableau assigné à `merged`.

Vous pouvez passer plusieurs tableaux pour la fusion également :

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]
const array3 = [7, 8, 9]

const merged = array2.concat(array3, array1)
// [4, 5, 6, 7, 8, 9, 1, 2, 3]
```

Dans cet exemple, nous utilisons la méthode `concat` sur `array2`, ce qui signifie que le contenu de `array2` est en premier dans le tableau fusionné. 

Pour les arguments, nous passons d'abord `array3`, ce qui signifie que le contenu de `array3` est ensuite dans le tableau fusionné, suivi du contenu de `array1`.

Vous pouvez en apprendre plus sur `concat` dans cet article : [Array concat simplified](https://dillionmegida.com/p/array-concat/).

## 3. Comment utiliser `Array.push` en JavaScript

La méthode `push` des tableaux vous permet d'"ajouter" de nouvelles valeurs à la fin d'un tableau.

```js
array.push(value1, value2, ...valueN)
```

En utilisant cette méthode, vous pouvez ajouter un nouveau tableau à un tableau existant pour créer un processus de fusion. Contrairement aux approches précédentes que j'ai mentionnées, l'approche `push` modifie le tableau sur lequel elle est utilisée.

Voici un exemple :

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]

for(let i = 0; i < array2.length; i++) {
  array1.push(array2[i])
}

console.log(array1)
// [1, 2, 3, 4, 5, 6]
```

Ici, nous utilisons une boucle `for` pour parcourir les valeurs de `array2`, et à chaque itération, nous ajoutons la valeur à l'index à `array1`.

À la fin de la boucle, vous voyez `array1` modifié, contenant les valeurs de `array2`.

Au lieu d'une boucle `for`, vous pouvez également utiliser l'opérateur `spread` avec la méthode `push`. Puisque la méthode `push` accepte une liste d'arguments séparés par une virgule, vous pouvez décomposer un autre tableau dans cette méthode, et ils seront tous ajoutés au tableau auquel la méthode est appliquée :

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]

array1.push(...array2)

console.log(array1)
// [1, 2, 3, 4, 5, 6]
```

Vous pouvez faire cela pour plusieurs tableaux :

```js
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]
const array3 = [7, 8, 9]

array3.push(...array2, ...array1)

console.log(array3)
// [7, 8, 9, 4, 5, 6, 1, 2, 3]
```

Ici, nous appelons `push` sur `array3`, puis nous décomposons les valeurs de `array2` suivies de `array1` comme arguments à ajouter à `array3`.

## Conclusion

Dans cet article, nous avons vu trois approches pour fusionner des tableaux en JavaScript. J'aime particulièrement l'opérateur `spread` car il est plus facile et plus simple à utiliser.

Lorsque vous utilisez `push`, soyez prudent, comme je l'ai mentionné, car il modifie le tableau sur lequel il est utilisé (contrairement à `concat` qui retourne un nouveau tableau). Cela peut causer des résultats inattendus si vous ne l'utilisez pas intentionnellement et avec soin.
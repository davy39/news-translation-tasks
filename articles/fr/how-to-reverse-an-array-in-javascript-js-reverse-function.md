---
title: Comment inverser un tableau en JavaScript – Fonction JS .reverse()
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-29T20:12:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-reverse-an-array-in-javascript-js-reverse-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/8.-reverse-array.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment inverser un tableau en JavaScript – Fonction JS .reverse()
seo_desc: 'By Dillion Megida

  In this article, I''ll show you two ways to reverse arrays in JavaScript.

  The reverse method of arrays reverses an array by making the last item the first,
  and making the first item the last. The other items in between also get rever...'
---

Par Dillion Megida

Dans cet article, je vais vous montrer deux façons d'inverser des tableaux en JavaScript.

La méthode `reverse` des tableaux inverse un tableau en faisant du dernier élément le premier, et du premier élément le dernier. Les autres éléments entre eux sont également inversés, respectivement.

Avant de vous montrer des exemples de la méthode `reverse`, laissez-moi vous montrer comment inverser un tableau sans l'utiliser.

J'ai une [version vidéo](https://youtu.be/HXeUEwWT1F4) de cet article que vous pouvez également consulter.

## 1. Comment inverser un tableau en utilisant une boucle `for`

En utilisant une boucle `for` (ou tout autre type de boucle), nous pouvons parcourir un tableau du dernier élément au premier, et pousser ces valeurs vers un nouveau tableau qui devient la version inversée. Voici comment :

```js
const array = [1, 2, 3, 4]

const reversedArray = []

for(let i = array.length - 1; i >= 0; i--) {
  const valueAtIndex = array[i]
  
  reversedArray.push(valueAtIndex)
}

console.log(reversedArray)
// [4, 3, 2, 1]
```

En utilisant une boucle `for`, nous commençons à boucler à partir de l'index de la dernière valeur (`array.length - 1`) jusqu'à l'index de la première valeur (`0`). Ensuite, nous poussons les valeurs en conséquence vers `reversedArray`.

Mais il existe une manière plus facile d'inverser un tableau, qui consiste à utiliser la méthode `reverse`.

## 2. Comment utiliser `Array.reverse` pour inverser un tableau

Vous pouvez utiliser la méthode `reverse`, qui est une approche plus facile à lire/écrire que la boucle `for`, pour inverser un tableau. Cette méthode inverse le tableau en place, ce qui signifie que le tableau sur lequel elle est utilisée est modifié.

Voyons un exemple :

```js
const array = [1, 2, 3, 4]

array.reverse()

console.log(array)
// [ 4, 3, 2, 1 ]
```

Comme vous pouvez le voir dans cet exemple, le `array` est modifié lorsque la méthode `reverse` est appliquée.

Si vous ne souhaitez pas que le `array` soit modifié, vous pouvez le cloner avant d'appliquer le `reverse`. La méthode `reverse` retourne également le tableau inversé, vous pouvez donc assigner ce tableau à une variable.

Voici comment dupliquer et inverser un tableau :

```js
const array = [1, 2, 3, 4]

const reversed = [...array].reverse()

console.log(reversed)
// [ 4, 3, 2, 1 ]

console.log(array)
// [ 1, 2, 3, 4 ]
```

En utilisant l'[opérateur de décomposition](https://dillionmegida.com/p/spread-operator-simplified/) ici, nous clonons d'abord le `array`, puis nous appliquons la méthode `reverse` sur le clone. Le tableau inversé retourné est ensuite assigné à la variable `reverse`.

Comme vous pouvez le voir, en affichant `array`, il n'est pas affecté car nous l'avons d'abord cloné.

## Merci d'avoir lu !

Donc, si vous devez inverser un tableau, j'espère que cet article vous a appris quelque chose.
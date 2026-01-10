---
title: Comment échanger deux éléments d'un tableau en JavaScript – Intervertir des
  éléments en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-29T20:15:18.000Z'
originalURL: https://freecodecamp.org/news/swap-two-array-elements-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--11-.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment échanger deux éléments d'un tableau en JavaScript – Intervertir
  des éléments en JS
seo_desc: 'When you''re working with arrays, there are times when you need to swap
  two elements in an array in JavaScript.

  Maybe you''re working on an algorithm question such as the bubble sort algorithm
  where you need to compare two values and then swap them if ...'
---

Lorsque vous travaillez avec des tableaux, il arrive que vous deviez échanger deux éléments d'un tableau en JavaScript.

Peut-être travaillez-vous sur une question d'algorithme telle que l'algorithme de tri à bulles (bubble sort) où vous devez comparer deux valeurs puis les échanger si votre condition est vraie.

En dehors de cela, de nombreuses autres situations peuvent nécessiter l'échange d'éléments de tableau.

Au cas où vous ne comprendriez pas encore ce que j'entends par « échange » (swapping), voici un exemple. Supposez que vous ayez un tableau de nombres et que vous vouliez échanger l'élément à l'index `1` qui est **-2** avec l'élément à l'index `0` qui est **12**, comme on le voit dans l'image ci-dessous :

![](https://paper-attachments.dropbox.com/s_B08002E277AA9EEDFC6B2A9D153D5485AA9F9B4567270177E695FBE6032A1880_1664460747763_Untitled.drawio+14.png align="left")

L'implémentation de ceci en JavaScript peut devenir déroutante si vous n'êtes pas déjà familier avec la façon dont JS gère ce genre de choses. Vous cherchez peut-être aussi de meilleures façons de gérer cela.

Cet article vous enseignera trois approches : l'utilisation d'une variable temporaire, la déstructuration (destructuring) et l'utilisation de la méthode de tableau `splice()`.

## Comment échanger deux éléments d'un tableau avec une variable temporaire

Pour échanger des éléments, vous pouvez utiliser une variable temporaire et suivre trois étapes.

La première étape consiste à créer une variable temporaire pour stocker la valeur du premier élément. La deuxième étape consiste à affecter la valeur du deuxième élément au premier élément. La troisième étape consiste à affecter la valeur stockée dans la variable temporaire au deuxième élément.

```js
let myArray = [12, -2, 55, 68, 80];

const temp = myArray[0];
myArray[0] = myArray[1];
myArray[1] = temp;

console.log(myArray); // [-2,12,55,68,80]
```

Vous pouvez également créer une fonction réutilisable pour gérer cela, dans laquelle vous spécifiez le tableau et les deux index que vous souhaitez échanger.

```js
const swapElements = (array, index1, index2) => {
    let temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
};

let myArray = [12, -2, 55, 68, 80];
swapElements(myArray, 0, 1);
console.log(myArray); // [-2,12,55,68,80]
```

## Comment échanger deux éléments d'un tableau par déstructuration

Une bien meilleure méthode que vous pouvez utiliser pour échanger des éléments de tableau est la déstructuration (destructuring), car elle permet de faire le travail en une seule ligne de code.

Il suffit de créer un nouveau tableau contenant les deux éléments dans un ordre particulier, puis de l'assigner à un nouveau tableau qui contient ces deux mêmes éléments dans l'ordre inverse.

```js
let myArray = [12, -2, 55, 68, 80];

[myArray[0], myArray[1]] = [myArray[1], myArray[0]];

console.log(myArray); // [-2,12,55,68,80]
```

You can also create a reusable function to handle this whereby you specify the array and the two indexes you wish to swap.

```js
const swapElements = (array, index1, index2) => {
    [myArray[index1], myArray[index2]] = [myArray[index2], myArray[index1]];
};

let myArray = [12, -2, 55, 68, 80];
swapElements(myArray, 0, 1);
console.log(myArray); // [-2,12,55,68,80]
```

## Comment échanger deux éléments d'un tableau avec la méthode `Splice()`

Enfin, vous pouvez utiliser la méthode de tableau `splice()`. Vous pouvez utiliser cette méthode pour supprimer un ou plusieurs élément(s) d'un tableau et les remplacer par n'importe quel élément spécifié.

```js
// Syntaxe
array.splice(index, howmany, element1, ....., elementX)
```

Par exemple, si vous avez un tableau et que vous souhaitez supprimer un élément particulier, vous devez spécifier son index et le nombre d'éléments que vous souhaitez supprimer. Dans notre cas, il n'y en a qu'un seul.

```js
let myArray = [12, -2, 55, 68, 80];

myArray.splice(1, 1);
console.log(myArray); // [12,55,68,80]
```

De plus, si vous souhaitez remplacer l'élément supprimé par un autre, votre code ressemblera à ceci :

```js
let myArray = [12, -2, 55, 68, 80];

myArray.splice(1, 1, 32);
console.log(myArray); // [12,32,55,68,80]
```

Mais si vous voulez échanger deux éléments, vous obtiendrez quelque chose comme ceci :

```js
let myArray = [12, -2, 55, 68, 80];

myArray[0] = myArray.splice(1, 1, myArray[0])[0];

console.log(myArray); // [-2,12,55,68,80]
```

Vous pouvez également créer une fonction réutilisable pour gérer cela, dans laquelle vous spécifiez le tableau et les deux index que vous souhaitez échanger :

```js
const swapElements = (array, index1, index2) => {
    array[index1] = array.splice(index2, 1, array[index1])[0];
};

let myArray = [12, -2, 55, 68, 80];
swapElements(myArray, 0, 1);
console.log(myArray); // [-2,12,55,68,80]
```

## Conclusion

Dans cet article, vous avez appris trois méthodes pour échanger les éléments d'un tableau en JavaScript.

Vous pouvez utiliser n'importe laquelle de ces méthodes, mais il est préférable d'utiliser la méthode de déstructuration ES6 car elle est beaucoup plus facile à comprendre et à utiliser pour tout le monde.

Bon codage !
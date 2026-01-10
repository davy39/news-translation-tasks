---
title: Comment écrire l'algorithme de tri rapide avec JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-15T09:27:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-quick-sort-algorithm-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--6-.png
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
seo_title: Comment écrire l'algorithme de tri rapide avec JavaScript
seo_desc: 'Quick sort is a widely used sorting algorithm that efficiently sorts an
  array of elements by dividing it into smaller subarrays based on a chosen pivot
  element.

  In this article, we will walk through how to write a quick sort algorithm using
  JavaScrip...'
---

Le tri rapide (Quick sort) est un algorithme de tri largement utilisé qui trie efficacement un tableau d'éléments en le divisant en sous-tableaux plus petits basés sur un élément pivot choisi.

Dans cet article, nous allons voir comment écrire un algorithme de tri rapide en utilisant JavaScript et explorer les concepts clés derrière cet algorithme.

## Qu'est-ce que l'algorithme de tri rapide ?

Le tri est une tâche courante en programmation informatique, et il existe de nombreux algorithmes de tri disponibles qui peuvent être utilisés de différentes manières. L'un des algorithmes de tri les plus populaires et les plus efficaces est le tri rapide.

Le tri rapide est un algorithme de type "diviser pour régner" qui trie un tableau en choisissant un élément pivot et en partitionnant le tableau en deux sous-tableaux, l'un contenant les éléments plus petits que le pivot, et l'autre contenant les éléments plus grands que le pivot. Les deux sous-tableaux sont ensuite triés de manière récursive jusqu'à ce que le tableau entier soit trié.

**Note :** Dans l'algorithme de tri rapide, le pivot est un élément sélectionné dans le tableau qui sert de point de référence pour partitionner le tableau en deux sous-tableaux plus petits.

Le pivot est généralement choisi comme le premier ou le dernier élément du tableau, bien qu'il existe d'autres méthodes pour sélectionner le pivot.

## Implémentation de l'algorithme de tri rapide avec JavaScript

Avant de commencer l'implémentation de l'algorithme de tri rapide, comprenons d'abord ses concepts de base. Comme nous l'avons mentionné précédemment, le tri rapide est un algorithme de type "diviser pour régner". L'algorithme peut être décomposé en trois étapes principales :

1. Choisir un élément pivot dans le tableau.
    
2. Partitionner le tableau en deux sous-tableaux, l'un contenant les éléments plus petits que le pivot, et l'autre contenant les éléments plus grands que le pivot.
    
3. Appliquer récursivement l'algorithme de tri rapide aux deux sous-tableaux jusqu'à ce que l'ensemble du tableau soit trié.
    

Avec cette compréhension, passons à l'implémentation de l'algorithme en JavaScript.

```js
const quickSort = (arr) => {
  if (arr.length <= 1) {
    return arr;
  }

  let pivot = arr[0];
  let leftArr = [];
  let rightArr = [];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) {
      leftArr.push(arr[i]);
    } else {
      rightArr.push(arr[i]);
    }
  }

  return [...quickSort(leftArr), pivot, ...quickSort(rightArr)];
};
```

Parcourons cette implémentation étape par étape. Tout d'abord, nous créons une fonction pour gérer l'opération de tri rapide et contenir l'algorithme.

### Étape 1 : Choisir un élément pivot

Nous commençons par choisir un élément pivot dans le tableau. Dans cette implémentation, nous utiliserons le premier élément du tableau comme pivot.

```js
const pivot = arr[0];
```

### Étape 2 : Partitionner le tableau

Après avoir choisi l'élément pivot, l'étape suivante consiste à partitionner le tableau en deux sous-tableaux — l'un contenant les éléments plus petits que le pivot, et l'autre contenant les éléments plus grands que le pivot.

Nous pouvons y parvenir en parcourant le tableau, en comparant chaque élément au pivot et en l'ajoutant au sous-tableau approprié.

```js
let leftArr = [];
let rightArr = [];

for (let i = 1; i < arr.length; i++) {
  if (arr[i] < pivot) {
    leftArr.push(arr[i]);
  } else {
    rightArr.push(arr[i]);
  }
}
```

### Étape 3 : Trier récursivement les sous-tableaux

Ensuite, nous appliquons récursivement l'algorithme de tri rapide aux deux sous-tableaux jusqu'à ce que le tableau entier soit trié. Nous utilisons ensuite l'opérateur de décomposition (spread operator) pour concaténer le sous-tableau gauche trié, le pivot et le sous-tableau droit trié.

```js
return [...quickSort(leftArr), pivot, ...quickSort(rightArr)];
```

Mais pour que cela ne continue pas indéfiniment, il doit y avoir un cas de base pour arrêter la [récursion](https://joelolawanle.com/posts/recursion-in-javascript-explained-for-beginners).

### Étape 4 : Définir un cas de base

La dernière étape consiste à définir un cas de base pour la fonction récursive. Celui-ci est utilisé lorsque le tableau a une longueur de 0 ou 1, car un tableau avec un seul élément est déjà trié.

```js
if (arr.length <= 1) {
  return arr;
}
```

## Tester l'algorithme de tri rapide

Pour tester l'algorithme de tri rapide, nous pouvons créer un tableau de nombres aléatoires et le passer à la fonction `quickSort()`.

Voici un exemple :

```js
let myArray = [3, 7, 2, 5, 1, 4, 6, 8];
console.log(quicksort(myArray)); // Sortie : [1,2,3,4,5,6,7,8]
```

## Conclusion ✨

Dans cet article, vous avez appris ce que signifie l'algorithme de tri rapide et comment vous pouvez créer l'algorithme.

Vous pouvez utiliser n'importe quelle valeur comme nombre pivot en modifiant un peu le code.

Amusez-vous bien en codant !

Vous pouvez accéder à plus de 195 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.
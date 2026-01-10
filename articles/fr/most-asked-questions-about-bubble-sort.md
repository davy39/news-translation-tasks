---
title: Algorithme de Tri à Bulles - Questions les Plus Fréquentes sur le Tri à Bulles
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-04-05T21:40:48.000Z'
originalURL: https://freecodecamp.org/news/most-asked-questions-about-bubble-sort
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-template--6-.png
tags:
- name: algorithms
  slug: algorithms
- name: bubble
  slug: bubble
- name: JavaScript
  slug: javascript
seo_title: Algorithme de Tri à Bulles - Questions les Plus Fréquentes sur le Tri à
  Bulles
seo_desc: 'Bubble sort is a simple sorting algorithm that repeatedly loops through
  a list, compares adjacent elements, and swaps them if they are in the wrong order.

  The bubble sort algorithm is not the most efficient sorting algorithm when it comes
  to time com...'
---

Le tri à bulles est un algorithme de tri simple qui parcourt répétitivement une liste, compare les éléments adjacents et les échange s'ils sont dans le mauvais ordre.

L'algorithme de tri à bulles n'est pas le plus efficace en termes de complexité temporelle. Mais il est encore souvent utilisé comme point de départ pour apprendre et comprendre les principes de base des algorithmes de tri.

Dans cet article, vous explorerez les questions les plus fréquemment posées sur l'algorithme de tri à bulles, y compris sa complexité temporelle et spatiale, le temps d'exécution dans les meilleurs et pires cas, son implémentation en JavaScript, et plus encore.

## Qu'est-ce que l'Algorithme de Tri à Bulles ?

Le tri à bulles est une méthode de tri d'une liste d'éléments, comme des nombres ou des mots, dans un ordre spécifique. Il fonctionne en examinant des paires d'éléments adjacents dans la liste et en les échangeant s'ils sont dans le mauvais ordre.

Par exemple, si vous avez une liste de [3, 1, 4, 2], le tri à bulles comparerait 3 et 1, voyant qu'ils sont dans le mauvais ordre, il les échangerait pour obtenir [1, 3, 4, 2]. Il comparerait ensuite 3 et 4, voyant qu'ils sont dans le bon ordre, il passerait à la paire suivante.

Le tri à bulles continue à comparer les paires adjacentes et à les échanger si nécessaire jusqu'à ce que la liste soit complètement triée. Au fur et à mesure que l'algorithme progresse, les plus petits éléments "remontent" en haut de la liste. C'est pourquoi on l'appelle tri à bulles.

Bien que le tri à bulles soit un algorithme simple et facile à comprendre, il n'est pas le plus efficace. En fait, il a une complexité temporelle dans le pire des cas de O(n^2), ce qui signifie qu'il n'est pas un bon choix pour trier des listes très grandes.

Mais il est encore utile pour enseigner et apprendre les algorithmes de tri et leurs principes de base.

## Implémentation de l'Algorithme de Tri à Bulles avec JavaScript

Voici un exemple d'implémentation de l'algorithme de tri à bulles en JavaScript :

```js
const bubbleSort = (arr) => {
  let swapped;

  do {
    swapped = false;
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        [myArray[i], myArray[i + 1]] = [myArray[i + 1], myArray[i]];
        swapped = true;
      }
    }
  } while (swapped);

  return arr;
};

let myArray = [12, 10, 3, 7, 4];
console.log(bubbleSort(myArray)); // retourne [3, 4, 7, 10, 12]
```

Dans cette implémentation, vous définissez une fonction qui prend un tableau en entrée. La fonction utilise deux boucles imbriquées pour parcourir le tableau et comparer les éléments adjacents.

Vous pouvez en lire plus sur [comment écrire l'algorithme de tri à bulles dans cet article détaillé](https://www.freecodecamp.org/news/how-to-implement-bubble-sort-algorithm-with-javascript/).

## Questions les Plus Fréquentes sur l'Algorithme de Tri à Bulles

Explorons maintenant certaines des questions les plus courantes que vous pourriez poser sur l'algorithme de tri à bulles pour vous éclairer.

### 1. Quelle est la complexité temporelle dans le meilleur des cas du tri à bulles standard ?

La complexité temporelle dans le meilleur des cas du tri à bulles standard est O(n) lorsque le tableau d'entrée est déjà trié et qu'aucun échange d'éléments n'est nécessaire.

```js
let myArray = [3, 4, 7, 10, 12];
console.log(bubbleSort(myArray)); // retourne [3, 4, 7, 10, 12]
```

### 2. Quelle est la complexité temporelle et spatiale du tri à bulles ?

La complexité temporelle du tri à bulles est O(n^2), où n est le nombre d'éléments dans le tableau. La complexité spatiale du tri à bulles est O(1) car il utilise uniquement une quantité constante de mémoire supplémentaire.

### 3. Quel type d'algorithme est le tri à bulles ?

Le tri à bulles est un algorithme de tri simple qui parcourt répétitivement une liste, compare les éléments adjacents et les échange s'ils sont dans le mauvais ordre.

### 4. Quelle est la complexité temporelle dans le meilleur des cas du tri à bulles ?

La complexité temporelle dans le meilleur des cas du tri à bulles est O(n), où n est le nombre d'éléments dans le tableau. Cela se produit lorsque le tableau d'entrée est déjà trié et qu'aucun échange d'éléments n'est nécessaire.

### 5. Quelle est la complexité moyenne du tri à bulles ?

La complexité moyenne du tri à bulles est O(n^2), où n est le nombre d'éléments dans le tableau. Cela se produit lorsque le tableau d'entrée n'est pas trié et que plusieurs éléments doivent être échangés.

### 6. Quelle est la complexité temporelle dans le pire des cas du tri à bulles ?

La complexité temporelle dans le pire des cas du tri à bulles est O(n^2), où n est le nombre d'éléments dans le tableau. Cela se produit lorsque le tableau d'entrée est trié en ordre inverse et que chaque élément doit être échangé.

## Conclusion

Dans cet article, nous avons couvert plusieurs questions fréquemment posées sur le tri à bulles, y compris sa complexité temporelle et spatiale, le temps d'exécution dans les meilleurs et pires cas, et comment l'implémenter en JavaScript.

Espérons que cet article vous a donné une meilleure compréhension du tri à bulles et de ses limitations. N'oubliez pas que bien que le tri à bulles soit un bon point de départ pour apprendre les algorithmes de tri, des algorithmes plus efficaces sont disponibles pour trier de plus grands ensembles de données.

Amusez-vous bien en codant !

Vous pouvez accéder à plus de 200 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.
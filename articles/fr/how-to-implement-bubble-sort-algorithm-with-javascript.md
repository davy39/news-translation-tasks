---
title: Comment Implémenter l'Algorithme de Tri à Bulles avec JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-30T15:34:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-bubble-sort-algorithm-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--2-.png
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
seo_title: Comment Implémenter l'Algorithme de Tri à Bulles avec JavaScript
seo_desc: 'Sorting is an essential task in programming, and the bubble sort algorithm
  is one of the simplest and most commonly used methods.

  As a beginner in solving algorithm questions or preparing for an interview, you
  might wonder how to implement this algor...'
---

Le tri est une tâche essentielle en programmation, et l'algorithme de tri à bulles est l'une des méthodes les plus simples et les plus couramment utilisées.

En tant que débutant dans la résolution de questions d'algorithmes ou en préparation pour un entretien, vous vous demandez peut-être comment implémenter cet algorithme efficacement.

Ne vous inquiétez pas ; dans cet article, je vais vous guider étape par étape sur la façon d'implémenter l'algorithme de tri à bulles avec JavaScript. À la fin de ce tutoriel, vous aurez une compréhension solide de la façon dont cet algorithme fonctionne et serez en mesure de l'appliquer à vos propres projets.

## Qu'est-ce que l'Algorithme de Tri à Bulles ?

L'algorithme de tri à bulles est une technique de tri simple qui compare deux éléments adjacents dans un tableau et les échange s'ils sont dans le mauvais ordre. Il répète ce processus jusqu'à ce que le tableau soit trié.

Par exemple, le diagramme ci-dessous illustre les différents échanges/bulles qui se produisent lorsque l'élément de gauche est plus grand que l'élément de droite.

De plus, à la fin de l'itération du tableau, il vérifie si des échanges ont eu lieu ; si c'est le cas, le processus est répété ; sinon, le tableau est trié.

![](https://paper-attachments.dropboxusercontent.com/s_AA89D639F731C302D3BEA2FB06F0908D85A1AFFFF9C777BBB48943CB5F4958DF_1680155344777_Untitled.drawio.png align="left")

Imaginez des bulles dans un verre de soda où les bulles montent une par une vers le haut. C'est similaire à la façon dont cet algorithme fonctionne.

Le tri à bulles est facile à comprendre et à implémenter, mais peut être lent pour les grands ensembles de données.

## Comment Implémenter l'Algorithme de Tri à Bulles avec JavaScript

Avec l'illustration de la section précédente, vous devriez avoir une idée de la façon dont l'algorithme de tri à bulles est censé fonctionner. Mais comment pouvez-vous écrire cet algorithme avec JavaScript ?

Voici 5 étapes pour rendre le processus facile pour vous :

1. Créez une variable booléenne pour suivre l'échange d'éléments dans l'itération actuelle.

2. Créez une boucle "do-while" qui itère à travers le tableau jusqu'à ce qu'il soit trié.

3. Au début de chaque itération, définissez la variable booléenne sur false.

4. Utilisez une boucle "for" pour comparer les éléments adjacents. Échangez-les s'ils ne sont pas dans le bon ordre, et définissez la variable booléenne sur true si un élément est échangé.

5. Répétez la boucle jusqu'à ce qu'il n'y ait plus d'éléments à échanger dans l'itération actuelle.

En utilisant les étapes ci-dessus, implémentons l'algorithme en JavaScript.

```js
const bubbleSort = (arr) => {
  let swapped;

  do {
    swapped = false;
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        swapped = true;
      }
    }
  } while (swapped);

  return arr;
};
```

Parcourons cette implémentation étape par étape. Tout d'abord, nous créons une fonction pour gérer l'opération de tri à bulles et contenir l'algorithme.

### Étape 1 : Créez une variable booléenne

Vous devrez suivre si un échange a été fait dans l'itération actuelle du tableau. Pour ce faire, créez une variable booléenne nommée "swapped" à cette fin.

```js
let swapped;
```

### Étape 2 : Créez une boucle "do-while" pour itérer jusqu'à ce que le tableau soit trié

Utilisons la boucle "do-while" pour itérer à travers le tableau jusqu'à ce qu'il soit trié. La boucle s'exécute au moins une fois, même si le tableau est déjà trié — c'est pourquoi elle est mieux utilisée pour cela.

Vous utiliserez également la variable "swapped" pour vérifier si un échange a été fait dans l'itération actuelle.

```js
do {
  // code à exécuter
} while (swapped);
```

### Étape 3 : Définissez la variable booléenne sur false au début de chaque itération

Au début de chaque itération, vous devez définir la variable "swapped" sur false. Cela est dû au fait que vous n'avez pas encore fait d'échange dans l'itération actuelle.

```js
do {
  swapped = false;
  // code à exécuter
} while (swapped);
```

### Étape 4 : Utilisez une boucle "for" pour comparer les éléments adjacents

Au sein de la boucle "do-while", nous utilisons une boucle "for" pour comparer chaque élément du tableau avec l'élément suivant. Si l'élément actuel est plus grand que l'élément suivant, ils sont échangés.

Nous définissons également la variable "swapped" sur true si un échange est fait, indiquant que le tableau n'est pas encore trié.

```js
for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      let temp = arr[i];
      arr[i] = arr[i + 1];
      arr[i + 1] = temp;
      swapped = true;
    }
  }
} while (swapped);
```

### Étape 5 : Répétez la boucle jusqu'à ce qu'il n'y ait plus d'échanges

Si aucun échange n'est fait dans l'itération actuelle, la variable "swapped" reste false. Cela signifie que le tableau est trié, et nous pouvons sortir de la boucle.

Si des éléments ont été échangés, la variable "swapped" est définie sur true, et la boucle continue à itérer jusqu'à ce que le tableau soit trié.

## Tester l'Algorithme de Tri à Bulles

Pour tester l'algorithme de tri à bulles, vous pouvez créer un tableau de nombres aléatoires et le passer à la fonction `bubbleSort()`.

Voici un exemple :

```js
let myArray = [12, 10, 3, 7, 4];
console.log(bubbleSort(myArray)); // Sortie : [3, 4, 7, 10, 12]
```

## Complexité Temporelle dans le Pire Cas de l'Algorithme de Tri à Bulles

La complexité temporelle dans le pire cas d'un algorithme fait référence à la quantité maximale de temps que l'algorithme peut prendre pour se terminer, étant donné la pire entrée possible.

Pour le tri à bulles, la complexité temporelle dans le pire cas se produit lorsque le tableau est dans l'ordre inverse. Cela signifie que chaque élément doit être échangé avec chaque autre élément.

Dans ce cas, la complexité temporelle de l'algorithme est O(n^2), où n est le nombre d'éléments dans le tableau.

Cela rend le tri à bulles inefficace pour les grands tableaux, car le temps nécessaire pour trier le tableau croît de manière quadratique avec la taille du tableau.

Cependant, le tri à bulles peut être utile pour les petits tableaux ou dans les cas où le tableau est presque trié, car il a une implémentation simple et nécessite seulement un espace constant.

## Conclusion

Dans cet article, vous avez appris ce que signifie l'algorithme de tri à bulles et comment vous pouvez créer cet algorithme.

Enfin, modifions l'algorithme pour obtenir une version plus courte en échangeant chaque élément par déstructuration :

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

Vous pouvez lire plus sur [comment échanger deux éléments de tableau en JavaScript](https://www.freecodecamp.org/news/swap-two-array-elements-in-javascript/).

Amusez-vous bien à coder !

Vous pouvez accéder à plus de 200 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.
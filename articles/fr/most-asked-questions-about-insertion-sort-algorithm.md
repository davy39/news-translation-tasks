---
title: Algorithme de Tri par Insertion - Questions les Plus Fréquentes sur le Tri
  par Insertion
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-31T19:26:33.000Z'
originalURL: https://freecodecamp.org/news/most-asked-questions-about-insertion-sort-algorithm
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--3-.png
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
seo_title: Algorithme de Tri par Insertion - Questions les Plus Fréquentes sur le
  Tri par Insertion
seo_desc: 'Sorting algorithms are an essential part of computer science. There are
  many sorting algorithms used to sort data.

  The insertion sort algorithm is one of the most basic and simple sorting algorithms.
  It is an efficient algorithm for small input sizes...'
---

Les algorithmes de tri sont une partie essentielle de l'informatique. Il existe de nombreux algorithmes de tri utilisés pour trier des données.

L'algorithme de tri par insertion est l'un des algorithmes de tri les plus basiques et simples. C'est un algorithme efficace pour les petites tailles d'entrée ou pour les données partiellement triées. L'algorithme fonctionne en triant les éléments un par un, en commençant par le premier élément de la liste.

Dans cet article, vous apprendrez ce qu'est l'algorithme de tri par insertion et comment il fonctionne. Vous apprendrez également à implémenter l'algorithme en JavaScript. Cet article répondra également à certaines questions courantes sur l'algorithme de tri par insertion.

## Qu'est-ce que le Tri par Insertion ?

Le tri par insertion est un algorithme de tri qui trie un tableau en insérant chaque élément à sa position correcte dans une sous-liste triée. Il est appelé algorithme de tri par comparaison en place car il trie la liste d'entrée en place sans nécessiter de mémoire supplémentaire.

Il fonctionne en comparant chaque élément avec les éléments précédents, puis en déplaçant l'élément à sa position correcte en décalant les éléments plus grands vers la droite.

## Implémentation du Tri par Insertion avec JavaScript

Voici une implémentation de l'algorithme de tri par insertion en JavaScript :

```js
const insertionSort = (arr) => {
  for (let i = 1; i < arr.length; i++) {
    let currentValue = arr[i];
    let j = i - 1;
    while (j >= 0 && arr[j] > currentValue) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = currentValue;
  }
  return arr;
};
```

La fonction prend un tableau en entrée et exécute l'algorithme de tri par insertion. Elle parcourt le tableau en commençant par le deuxième élément et le compare avec les éléments précédents.

Si un élément est plus grand que la valeur actuelle, il décale l'élément vers la droite jusqu'à ce qu'il trouve sa position appropriée.

Une fois l'élément correctement placé, la boucle passe à l'élément suivant jusqu'à ce que le tableau soit complètement trié. La fonction retourne le tableau trié.

Vous pouvez appeler la fonction avec un tableau comme suit :

```js
let myArray = [3, 7, 4, 10, 12];
console.log(insertionSort(myArray)); // retourne [3, 4, 7, 10, 12]
```

Ce n'est qu'une façon d'implémenter l'algorithme de tri par insertion en JavaScript. Il existe de nombreuses autres façons de l'écrire, mais cela devrait vous donner une idée de son fonctionnement.

## Le Tri par Insertion est-il Stable ?

Oui, le tri par insertion est un algorithme de tri stable.

Un algorithme de tri stable est celui qui maintient l'ordre relatif des éléments égaux dans la sortie triée.

En d'autres termes, si deux éléments ont la même valeur, leur ordre relatif dans le tableau d'entrée doit être préservé dans le tableau trié.

## Quel Type d'Algorithme est le Tri par Insertion ?

Le tri par insertion est un algorithme basé sur les comparaisons.

Il compare les éléments actuels et précédents pour déterminer leur position correcte dans la liste triée. C'est un algorithme simple et efficace qui est facile à implémenter.

## Le Tri par Insertion est-il un Algorithme Glouton ?

Non, le tri par insertion n'est pas un algorithme glouton.

Un algorithme glouton est un algorithme qui fait un choix localement optimal à chaque étape dans l'espoir de trouver un optimum global.

Le tri par insertion ne fait pas de choix localement optimal mais insère plutôt chaque élément à sa position correcte pour atteindre l'optimum global.

## Complexité Temporelle de l'Algorithme de Tri par Insertion

La complexité temporelle de l'algorithme de tri par insertion est O(n^2) dans le pire des cas et O(n) dans le meilleur des cas.

### Meilleur Cas de Temps d'Exécution d'un Algorithme de Tri par Insertion

Le meilleur cas de temps d'exécution d'un algorithme de tri par insertion est O(n). Cela se produit lorsque le tableau d'entrée est trié et qu'aucun élément ne doit être déplacé.

Cela résulte en n-1 comparaisons, ce qui est approximativement égal à n. Par conséquent, la complexité temporelle est O(n).

### Efficacité Temporelle dans le Meilleur Cas du Tri par Insertion

L'efficacité temporelle dans le meilleur cas d'un algorithme de tri par insertion est Ω(n), qui est la borne inférieure du temps d'exécution. Cela se produit lorsque le tableau d'entrée est trié et qu'aucun élément n'a besoin d'être déplacé.

### Pire Complexité Temporelle du Tri par Insertion

La pire complexité temporelle d'un algorithme de tri par insertion est O(n^2).

Cela se produit lorsque le tableau d'entrée est dans l'ordre inverse et que chaque élément doit être déplacé à sa position correcte en décalant tous les éléments plus grands vers la droite.

Le tableau d'entrée est dans l'ordre inverse. Chaque élément doit être comparé et échangé avec chaque autre élément du tableau. Cela résulte en n*(n-1)/2 comparaisons et échanges, approximativement égal à n^2/2. Par conséquent, la complexité temporelle est O(n^2).

### Temps d'Exécution Moyen d'un Algorithme de Tri par Insertion

Le temps d'exécution moyen d'un algorithme de tri par insertion est O(n^2).

Cela se produit lorsque le tableau d'entrée est ordonné de manière aléatoire et que chaque élément doit être déplacé à sa position correcte en décalant tous les éléments plus grands vers la droite.

### Temps d'Exécution Typique pour le Tri par Insertion pour les Listes Chaînées Simples

Le tri par insertion peut également être utilisé pour trier des listes chaînées simples.

Le temps d'exécution typique pour le tri par insertion pour les listes chaînées simples est également O(n^2), comme pour les tableaux. Cependant, la complexité spatiale peut différer en raison de la différence de structure de données.

## Le Tri par Insertion Utilise-t-il Diviser pour Régner ?

Non, le tri par insertion n'utilise pas l'approche Diviser pour Régner.

Diviser pour Régner est un paradigme algorithmique qui consiste à diviser un problème en sous-problèmes, à les résoudre indépendamment, puis à combiner leurs solutions pour résoudre le problème original.

Le tri par insertion fonctionne en triant les éléments individuellement sans diviser le problème en sous-problèmes.

## Pourquoi le Tri par Insertion est-il Lent ?

Le tri par insertion est lent car il a une complexité temporelle de O(n^2) dans le pire des cas.

Cela signifie que lorsque la taille de l'entrée augmente, le temps d'exécution de l'algorithme augmente également rapidement. Le tri par insertion n'est pas le meilleur choix pour les grandes tailles d'entrée, mais il peut être très efficace pour les petites tailles d'entrée ou pour les données partiellement triées.

## Conclusion

Le tri par insertion est un algorithme simple et efficace pour les petites tailles d'entrée ou les données partiellement triées. Il a une complexité temporelle de O(n^2) dans le pire des cas et O(n) dans le meilleur des cas.

C'est un algorithme de tri stable qui maintient l'ordre relatif des éléments égaux. Bien qu'il puisse être lent pour les grandes tailles d'entrée, il peut être très efficace pour les petites tailles d'entrée ou pour les données partiellement triées.

Amusez-vous bien en codant !

Vous pouvez accéder à plus de 200 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.
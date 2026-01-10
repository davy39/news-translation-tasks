---
title: 'QuickSelect: L''algorithme Quick Select Expliqué avec des Exemples de Code'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-03T18:44:00.000Z'
originalURL: https://freecodecamp.org/news/quickselect-algorithm-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ee2740569d1a4ca3fb0.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: 'QuickSelect: L''algorithme Quick Select Expliqué avec des Exemples de
  Code'
seo_desc: 'What is QuickSelect?

  QuickSelect is a selection algorithm to find the K-th smallest element in an unsorted
  list.

  The Algorithm Explained

  After finding the pivot (a position that partitions the list into two parts: every
  element on the left is less th...'
---

## Qu'est-ce que QuickSelect?

QuickSelect est un algorithme de sélection permettant de trouver le K-ième plus petit élément dans une liste non triée.

### L'algorithme expliqué

Après avoir trouvé le pivot (une position qui partitionne la liste en deux parties : chaque élément à gauche est inférieur au pivot et chaque élément à droite est supérieur au pivot), l'algorithme ne récurse que pour la partie qui contient le K-ième plus petit élément.

Si l'index de l'élément partitionné (pivot) est supérieur à K, alors l'algorithme récurse pour la partie gauche. Si l'index (pivot) est égal à K, alors nous avons trouvé le K-ième plus petit élément et il est retourné. Si l'index est inférieur à K, alors l'algorithme récurse pour la partie droite.

#### Pseudocode de sélection

```
Entrée : Liste, left est la première position de la liste, right est la dernière position de la liste et k est le k-ième plus petit élément.
Sortie : Une nouvelle liste est partitionnée.

quickSelect(list, left, right, k)

   if left = right
      return list[left]

   // Sélectionner un pivotIndex entre left et right

   pivotIndex := partition(list, left, right, 
                                  pivotIndex)
   if k = pivotIndex
      return list[k]
   else if k < pivotIndex
      right := pivotIndex - 1
   else
      left := pivotIndex + 1

```

### Partition

La partition consiste à trouver le pivot comme mentionné ci-dessus. (Chaque élément à gauche est inférieur au pivot et chaque élément à droite est supérieur au pivot) Il existe deux algorithmes pour trouver le pivot de la partition.

* Partition de Lomuto
* Partition de Hoare

#### Partition de Lomuto

Cette partition choisit un pivot qui est généralement le dernier élément du tableau. L'algorithme maintient l'index i lors du balayage du tableau à l'aide d'un autre index j tel que les éléments de lo à i (inclus) sont inférieurs ou égaux au pivot, et les éléments de i+1 à j-1 (inclus) sont supérieurs au pivot.

Ce schéma se dégrade en `O(n^2)` lorsque le tableau est déjà en ordre.

```
algorithme Lomuto(A, lo, hi) est
    pivot := A[hi]
    i := lo    
    pour j := lo à hi - 1 faire
        si A[j] < pivot alors
            si i != j alors
                échanger A[i] avec A[j]
            i := i + 1
    échanger A[i] avec A[hi]
    retourner i

```

#### Partition de Hoare

Hoare utilise deux indices qui commencent aux extrémités du tableau à partitionner, puis se déplacent l'un vers l'autre jusqu'à ce qu'ils détectent une inversion : une paire d'éléments, l'un supérieur ou égal au pivot, l'autre inférieur ou égal au pivot, qui sont dans le mauvais ordre relatif l'un par rapport à l'autre.

Les éléments inversés sont ensuite échangés. Lorsque les indices se rencontrent, l'algorithme s'arrête et retourne l'index final. Il existe de nombreuses variantes de cet algorithme.

```
algorithme Hoare(A, lo, hi) est
    pivot := A[lo]
    i := lo - 1
    j := hi + 1
    boucle infinie
        faire
            i := i + 1
        tant que A[i] < pivot

        faire
            j := j - 1
        tant que A[j] > pivot

        si i >= j alors
            retourner j

        échanger A[i] avec A[j]

```
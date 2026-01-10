---
title: Algorithme de Recherche par Saut Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-12T23:00:00.000Z'
originalURL: https://freecodecamp.org/news/jump-search-algorithm-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9def740569d1a4ca3a7d.jpg
tags:
- name: algorithms
  slug: algorithms
- name: toothbrush
  slug: toothbrush
seo_title: Algorithme de Recherche par Saut Expliqué
seo_desc: 'Jump Search

  A jump search locates an item in a sorted array by jumping k itens and then verify
  if the item wanted is between the previous jump and current jump.

  Complexity Worst Case

  O(√N)

  How it works


  Define the value of k, the number of jump: Opti...'
---

## **Recherche par Saut**

Une recherche par saut localise un élément dans un tableau trié en sautant k éléments et vérifie ensuite si l'élément recherché se trouve entre le saut précédent et le saut actuel.

### Complexité dans le pire des cas

O(√N)

## Comment cela fonctionne

1. Définissez la valeur de k, le nombre de sauts : La taille de saut optimale est √N où N est la longueur du tableau
2. Parcourez le tableau par sauts de k en k en recherchant la condition `Array[i] < valeurRecherchée < Array[i+k]`
3. Effectuez une recherche linéaire entre `Array[i]` et `Array[i + k]`

![Recherche par Saut 1](https://i1.wp.com/theoryofprogramming.com/wp-content/uploads/2016/11/jump-search-1.jpg?resize=676%2C290)

## Code

Pour voir des exemples d'implémentation de code de cette méthode, accédez au lien ci-dessous :

[Jump Search - OpenGenus/cosmos](https://github.com/OpenGenus/cosmos/tree/master/code/search/jump_search)

### Crédits

[Image du tableau logique](http://theoryofprogramming.com/2016/11/10/jump-search-algorithm/)
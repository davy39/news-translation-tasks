---
title: 'Algorithmes de recherche : Recherche exponentielle expliquée'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-02T20:02:00.000Z'
originalURL: https://freecodecamp.org/news/search-algorithms-exponential-search-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cdb740569d1a4ca3493.jpg
tags:
- name: algorithms
  slug: algorithms
- name: toothbrush
  slug: toothbrush
seo_title: 'Algorithmes de recherche : Recherche exponentielle expliquée'
seo_desc: 'Exponential Search

  Exponential Search also known as finger search, searches for an element in a sorted
  array by jumping 2^i elements every iteration where i represents the value of loop
  control variable, and then verifying if the search element is pr...'
---

## **Recherche exponentielle**

La recherche exponentielle, également connue sous le nom de recherche par doigt, recherche un élément dans un tableau trié en sautant `2^i` éléments à chaque itération, où i représente la valeur de la variable de contrôle de boucle, puis vérifie si l'élément recherché est présent entre le dernier saut et le saut actuel.

## Complexité dans le pire des cas

O(log(N)) Souvent confondu à cause du nom, l'algorithme n'est pas nommé ainsi à cause de la complexité temporelle. Le nom provient du fait que l'algorithme saute des éléments avec des étapes égales aux exponents de 2.

## Comment cela fonctionne

1. Parcourez le tableau en sautant `2^i` éléments à la fois, à la recherche de la condition `Array[2^(i-1)] < valeurRecherchée < Array[2^i]`. Si `2^i` est supérieur à la longueur du tableau, définissez la borne supérieure à la longueur du tableau.
2. Effectuez une recherche binaire entre `Array[2^(i-1)]` et `Array[2^i]`

## Le Code

```text
// Programme C++ pour trouver un élément x dans un
// tableau trié en utilisant la recherche exponentielle.
#include <bits/stdc++.h>
using namespace std;
 
int binarySearch(int arr[], int, int, int);
 
// Retourne la position de la première occurrence de
// x dans le tableau
int exponentialSearch(int arr[], int n, int x)
{
    // Si x est présent à la première position elle-même
    if (arr[0] == x)
        return 0;
 
    // Trouver la plage pour la recherche binaire par
    // doublement répété
    int i = 1;
    while (i < n && arr[i] <= x)
        i = i*2;
 
    // Appeler la recherche binaire pour la plage trouvée.
    return binarySearch(arr, i/2, min(i, n), x);
}
 
// Une fonction de recherche binaire récursive. Elle retourne
// l'emplacement de x dans le tableau donné arr[l..r] si
// présent, sinon -1
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l)
    {
        int mid = l + (r - l)/2;
 
        // Si l'élément est présent au milieu
        // lui-même
        if (arr[mid] == x)
            return mid;
 
        // Si l'élément est plus petit que le milieu, alors il
        // ne peut être présent que dans le sous-tableau de gauche
        if (arr[mid] > x)
            return binarySearch(arr, l, mid-1, x);
 
        // Sinon l'élément ne peut être présent
        // que dans le sous-tableau de droite
        return binarySearch(arr, mid+1, r, x);
    }
 
    // Nous arrivons ici lorsque l'élément n'est pas présent
    // dans le tableau
    return -1;
}
 
int main(void)
{
   int arr[] = {2, 3, 4, 10, 40};
   int n = sizeof(arr)/ sizeof(arr[0]);
   int x = 10;
   int result = exponentialSearch(arr, n, x);
   (result == -1)? printf("L'élément n'est pas présent dans le tableau")
                 : printf("L'élément est présent à l'index %d", result);
   return 0;
}
```
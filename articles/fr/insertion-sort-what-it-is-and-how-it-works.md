---
title: 'Tri par insertion : ce que c''est et comment ça fonctionne'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-07T21:36:00.000Z'
originalURL: https://freecodecamp.org/news/insertion-sort-what-it-is-and-how-it-works
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e13740569d1a4ca3b36.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: 'Tri par insertion : ce que c''est et comment ça fonctionne'
seo_desc: 'Insertion sort is a simple sorting algorithm for a small number of elements.

  Example:

  In Insertion sort, you compare the key element with the previous elements. If the
  previous elements are greater than the key element, then you move the previous ele...'
---

Le tri par insertion est un algorithme de tri simple pour un petit nombre d'éléments.

### Exemple :

Dans le tri par insertion, vous comparez l'élément `key` avec les éléments précédents. Si les éléments précédents sont plus grands que l'élément `key`, alors vous déplacez l'élément précédent à la position suivante.

Commencez à partir de l'index 1 jusqu'à la taille du tableau d'entrée.

[ 8 3 5 1 4 2 ]

Étape 1 :

![[ 8 3 5 1 4 2 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/1.png?raw=true)

```text
      key = 3 //en commençant par le 1er index.

      Ici, `key` sera comparé avec les éléments précédents.

      Dans ce cas, `key` est comparé avec 8. puisque 8 > 3, déplacez l'élément 8
      à la position suivante et insérez `key` à la position précédente.

      Résultat : [ 3 8 5 1 4 2 ]
```

Étape 2 :

![[ 3 8 5 1 4 2 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/2.png?raw=true)

```text
      key = 5 //2ème index

      8 > 5 //déplacez 8 au 2ème index et insérez 5 au 1er index.

      Résultat : [ 3 5 8 1 4 2 ]
```

Étape 3 :

![[ 3 5 8 1 4 2 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/3.png?raw=true)

```text
      key = 1 //3ème index

      8 > 1     => [ 3 5 1 8 4 2 ]  

      5 > 1     => [ 3 1 5 8 4 2 ]

      3 > 1     => [ 1 3 5 8 4 2 ]

      Résultat : [ 1 3 5 8 4 2 ]
```

Étape 4 :

![[ 1 3 5 8 4 2 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/4.png?raw=true)

```text
      key = 4 //4ème index

      8 > 4   => [ 1 3 5 4 8 2 ]

      5 > 4   => [ 1 3 4 5 8 2 ]

      3 > 4   ≠>  stop

      Résultat : [ 1 3 4 5 8 2 ]
```

Étape 5 :

![[ 1 3 4 5 8 2 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/5.png?raw=true)

```text
      key = 2 //5ème index

      8 > 2   => [ 1 3 4 5 2 8 ]

      5 > 2   => [ 1 3 4 2 5 8 ]

      4 > 2   => [ 1 3 2 4 5 8 ]

      3 > 2   => [ 1 2 3 4 5 8 ]

      1 > 2   ≠> stop

      Résultat : [1 2 3 4 5 8]
```

![[ 1 2 3 4 5 8 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/6.png?raw=true)

L'algorithme présenté ci-dessous est une version légèrement optimisée pour éviter d'échanger l'élément `key` à chaque itération. Ici, l'élément `key` sera échangé à la fin de l'itération (étape).

```text
    InsertionSort(arr[])
      for j = 1 to arr.length
         key = arr[j]
         i = j - 1
         while i > 0 and arr[i] > key
            arr[i+1] = arr[i]
            i = i - 1
         arr[i+1] = key
```

Voici une implémentation détaillée en JavaScript :

```text
function insertion_sort(A) {
    var len = array_length(A);
    var i = 1;
    while (i < len) {
        var x = A[i];
        var j = i - 1;
        while (j >= 0 && A[j] > x) {
            A[j + 1] = A[j];
            j = j - 1;
        }
        A[j+1] = x;
        i = i + 1;
    }
}
```

Une implémentation rapide en Swift est présentée ci-dessous :

```swift
  var array = [8, 3, 5, 1, 4, 2]

  func insertionSort(array:inout Array<Int>) -> Array<Int>{
      for j in 0..<array.count {
          let key = array[j]
          var i = j-1

          while (i > 0 && array[i] > key){
              array[i+1] = array[i]
              i = i-1
          }
          array[i+1] = key
      }
      return array
  }
```

L'exemple en Java est présenté ci-dessous :

```text
public int[] insertionSort(int[] arr)
      for (j = 1; j < arr.length; j++) {
         int key = arr[j]
         int i = j - 1
         while (i > 0 and arr[i] > key) {
            arr[i+1] = arr[i]
            i -= 1
         }
         arr[i+1] = key
      }
      return arr;
```

### Tri par insertion en C....

```c
void insertionSort(int arr[], int n) 
{ 
   int i, key, j; 
   for (i = 1; i < n; i++) 
   { 
       key = arr[i]; 
       j = i-1;
       while (j >= 0 && arr[j] > key) 
       { 
           arr[j+1] = arr[j]; 
           j = j-1; 
       } 
       arr[j+1] = key; 
   } 
} 
```

### Propriétés :

* Complexité spatiale : O(1)

Complexité temporelle : O(n), O(n* n), O(n* n) pour les cas Meilleur, Moyen, Pire respectivement.

* Meilleur cas : le tableau est déjà trié
* Cas moyen : le tableau est trié aléatoirement
* Pire cas : le tableau est trié à l'envers.
* Tri en place : Oui
* Stable : Oui

#### Autres ressources :

* [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)
* [CS50 - YouTube](https://youtu.be/TwGb6ohsvUU)
* [SortInsertion - GeeksforGeeks, YouTube](https://www.youtube.com/watch?v=wObxd4Kx8sE)
* [Visualisation du tri par insertion](https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/visualize/)
* [Tri par insertion - MyCodeSchool](https://www.youtube.com/watch?v=i-SKeOcBwko)
* [Tri par insertion - VisuAlgo](https://visualgo.net/en/sorting)
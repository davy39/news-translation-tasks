---
title: La recherche binaire en C++ – Exemple d'algorithme
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-17T16:52:22.000Z'
originalURL: https://freecodecamp.org/news/binary-search-in-c-algorithm-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/binary-search-algorithm-1.png
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: C++
  slug: c-2
seo_title: La recherche binaire en C++ – Exemple d'algorithme
seo_desc: "The binary search algorithm is a divide and conquer algorithm that you\
  \ can use to search for and find elements in a sorted array. \nThe algorithm is\
  \ fast in searching for elements because it removes half of the array every time\
  \ the search iteration ha..."
---

L'algorithme de recherche binaire est un algorithme de type « diviser pour régner » que vous pouvez utiliser pour rechercher et trouver des éléments dans un tableau trié. 

L'algorithme est rapide pour rechercher des éléments car il supprime la moitié du tableau à chaque itération de la recherche. 

Ainsi, au lieu de parcourir l'ensemble du tableau, l'algorithme élimine la moitié du tableau où l'élément recherché ne peut pas se trouver. Il procède ainsi continuellement jusqu'à ce que l'élément soit trouvé. 

Dans le cas où l'élément recherché n'existe pas, il renvoie une valeur de -1. Si l'élément existe, il renvoie alors l'index de l'élément. 

Si les explications ci-dessus vous semblent complexes, vous devriez consulter ce [guide visuel sur le fonctionnement de l'algorithme de recherche binaire](https://www.freecodecamp.org/news/binary-search-in-java-algorithm-example/#:~:text=How%20Does%20the%20Binary%20Search%20Algorithm%20Work%3F). 

Dans cet article, vous verrez une implémentation de l'algorithme de recherche binaire en C++.

C'est parti !

## Exemple d'algorithme de recherche binaire en C++

Dans cette section, nous allons décomposer et expliquer l'implémentation de la recherche binaire en C++.

Voici le code :

```c++
#include <iostream>
using namespace std;

int binarySearch(int array[], int low, int high, int number_to_search_for) {

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (number_to_search_for == array[mid]){
            return mid;
        }

        if (number_to_search_for > array[mid]){
            low = mid + 1;
        }
      
        if (number_to_search_for < array[mid]){
            high = mid - 1;
        }

    }

  return -1;
}

int main(void) {
  int arrayOfNums[] = {2,4,7,9,10,13,20};
  
  int n = sizeof(arrayOfNums) / sizeof(arrayOfNums[0]);
  
  int result = binarySearch(arrayOfNums, 0, n - 1, 13);
  
  if (result == -1){
      printf("L'élément n'existe pas dans le tableau");
  }
  else{
      printf("L'index de l'élément est %d", result);
  }
  
  // L'index de l'élément est 5
}
```

Pour commencer, nous avons créé une méthode appelée `binarySearch` qui possède quatre paramètres :

* `array[]` représente le tableau dans lequel effectuer la recherche.
* `low` représente le premier élément du tableau. 
* `high` représente le dernier élément du tableau. 
* `number_to_search_for` représente le nombre à rechercher dans `array[]`. 

Ensuite, nous avons créé une boucle `while` qui s'exécutera continuellement jusqu'à ce que l'opération de recherche renvoie une valeur – soit l'index de l'élément, soit -1. 

Dans la boucle `while` :

`mid` est utilisé pour représenter le centre/milieu du tableau : `int mid = low + (high - low) / 2;`.

Le premier bloc `if` est exécuté si `mid` a la même valeur que l'élément recherché :

```c++
if (number_to_search_for == array[mid]){
	return mid;
}
```

Le deuxième bloc `if` déplace la position de `low` vers l'index situé après le milieu du tableau :

```c++
if (number_to_search_for > array[mid]){
	low = mid + 1;
}
```

Ceci supprime tous les éléments du côté gauche du tableau car l'élément recherché est plus grand qu'eux, il n'est donc pas nécessaire de chercher dans cette partie du tableau.

Le troisième bloc `if` fait l'inverse du deuxième – il déplace la position de `high` vers l'index situé avant le milieu du tableau :

```c++
if (number_to_search_for < array[mid]){
	high = mid - 1;
}
```

Hier's un résumé du code dans les blocs `if` :

1. Si le nombre à rechercher est égal à `mid`, l'index `mid` sera renvoyé.
2. Si le nombre à rechercher est supérieur à `mid`, la recherche se poursuit parmi les éléments du côté droit de `mid`.
3. Si le nombre à rechercher est inférieur à `mid`, la recherche se poursuit parmi les éléments du côté gauche de `mid`.

Si le nombre recherché n'existe pas, -1 sera renvoyé. Vous pouvez le voir après la boucle `while` dans le code. 

Enfin, nous avons testé la méthode `binarySearch` :

```c++
int main(void) {
  int arrayOfNums[] = {2,4,7,9,10,13,20};
  
  int n = sizeof(arrayOfNums) / sizeof(arrayOfNums[0]);
  
  int result = binarySearch(arrayOfNums, 0, n - 1, 13);
  
  if (result == -1){
      printf("L'élément n'existe pas dans le tableau");
  }
  else{
      printf("L'index de l'élément est %d", result);
  }
  
  // L'index de l'élément est 5
}
```

Dans le code ci-dessus, nous avons passé les valeurs des paramètres créés dans la méthode `binarySearch` : `binarySearch(arrayOfNums, 0, n - 1, 13)`. 

* `arrayOfNums` représente le tableau à parcourir : {2,4,7,9,10,13,20}. 
* `0` représente le premier index du tableau. 
* `n - 1` représente le dernier index du tableau. Regardez le code pour voir comment `n` a été créé. 
* `13` est le nombre à rechercher dans `arrayOfNums`.

Lorsque vous exécutez le code, « L'index de l'élément est 5 » s'affichera dans la console. C'est parce que l'index du nombre recherché (13) est 5. 

Vous pouvez vous amuser avec le code en changeant la valeur du nombre à rechercher.

## Résumé

Dans cet article, nous avons abordé l'implémentation de l'algorithme de recherche binaire en C++. 

Nous avons vu un exemple de code comportant une méthode `binarySearch` qui prend des paramètres, effectue une recherche dans un tableau de nombres et renvoie la valeur appropriée après l'opération de recherche. 

Nous avons également vu une explication détaillée de chaque partie du code. 

Bon codage !
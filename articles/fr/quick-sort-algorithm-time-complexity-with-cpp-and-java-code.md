---
title: Quick Sort – Complexité Temporelle de l'Algorithme avec Exemple de Code en
  C++ et Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-11-03T00:43:11.000Z'
originalURL: https://freecodecamp.org/news/quick-sort-algorithm-time-complexity-with-cpp-and-java-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/kelly-sikkema-377gw1wN0Ic-unsplash.jpg
tags:
- name: algorithms
  slug: algorithms
- name: C++
  slug: c-2
- name: Java
  slug: java
seo_title: Quick Sort – Complexité Temporelle de l'Algorithme avec Exemple de Code
  en C++ et Java
seo_desc: "In this article, you'll learn about one of the most commonly used programming\
  \ algorithms – the quick sort algorithm. \nYou'll get to know how the algorithm\
  \ works with the help of visual guides. You'll also see some code examples that\
  \ will help you imp..."
---

Dans cet article, vous apprendrez l'un des algorithmes de programmation les plus couramment utilisés – l'algorithme de tri rapide.

Vous découvrirez comment l'algorithme fonctionne à l'aide de guides visuels. Vous verrez également des exemples de code qui vous aideront à implémenter l'algorithme en C++ et Java.

Enfin, mais non des moindres, nous parlerons de la [complexité temporelle](https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/) de l'algorithme de tri rapide dans les scénarios de complexité pire, moyenne et meilleure.

Commençons !

## Comment Fonctionne l'Algorithme de Tri Rapide ?

L'algorithme de tri rapide est basé sur la règle diviser pour régner. Dans un tableau donné d'éléments non ordonnés (nombres), un pivot est choisi. Le pivot est important car les autres éléments seront triés par rapport à sa valeur.

À la fin de l'opération de tri, tous les nombres inférieurs au pivot seront déplacés vers le côté gauche du pivot tandis que tous les nombres supérieurs seront à droite. Cela s'appelle également le partitionnement.

À ce stade, les nombres à droite et à gauche du pivot peuvent/seront probablement non ordonnés.

Ensuite, les nombres non ordonnés avant et après le pivot sont placés dans des tableaux séparés – un tableau pour les nombres à gauche et un autre pour ceux à droite.

Un pivot sera ensuite choisi dans chaque tableau et le processus depuis le début est répété jusqu'à ce que chaque nombre soit trié séparément. En combinant tous les nombres, vous aurez un tableau trié par ordre croissant.

Voici un résumé des explications ci-dessus :

**Étape #1 :** Un tableau de nombres non ordonnés est donné.

**Étape #2 :** Un nombre est choisi comme pivot.

**Étape #3 :** Les nombres inférieurs au pivot se déplacent vers le côté gauche du pivot.

**Étape #4 :** Les nombres supérieurs au pivot se déplacent vers le côté droit du pivot.

**Étape #5 :** Le tableau est divisé en deux tableaux – le premier tableau contiendra les éléments du côté gauche du pivot tandis que le second tableau contiendra les éléments du côté droit.

**Étape #6 :** Les étapes #2 à #5 sont répétées pour chaque tableau jusqu'à ce que chaque élément ait été trié par ordre croissant.

Les étapes ci-dessus peuvent sembler confuses. Vous les comprendrez mieux dans la section suivante à l'aide de guides visuels.

## Comment Fonctionne le Tri Rapide ?

Dans la dernière section, j'ai donné un bref résumé de ce qui se passe lorsque vous utilisez l'algorithme de tri rapide pour trier un tableau de nombres. Mais cela n'a pas expliqué comment l'opération de tri fonctionne sous le capot.

Dans cette section, en utilisant des guides visuels, vous comprendrez comment les nombres sont déplacés soit vers le côté gauche, soit vers le côté droit du pivot, et comment les sous-tableaux sont créés (également connu sous le nom de partitionnement). Cela vous aidera également à comprendre le code facilement lorsque nous en arriverons à cette partie.

Voici le tableau avec lequel nous allons travailler : `9,4,8,3,7,1,6,2,5`.

Le tableau ci-dessus contient un ensemble de nombres non ordonnés. Alors, comment fonctionne le tri rapide ?

Comme je l'ai expliqué dans la section précédente, nous devons sélectionner un élément pour agir comme pivot.

Prenons donc 5 comme pivot. Nous aurons également besoin de deux variables : `X` et `Y`. Elles seront utilisées pour comparer et échanger les positions des nombres par rapport au pivot.

Voici à quoi cela ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort.png)
_paramètres de quick-sort_

Dans l'image ci-dessus, nous avons trois flèches : rouge, bleue et jaune qui désignent respectivement `X`, `Y` et le pivot.

L'opération est assez simple :

* Si la valeur de `y` est supérieure au pivot, incrémentez `Y`.
* Si la valeur de `y` est inférieure ou égale au pivot, incrémentez `X`, et échangez `x` avec `y`.

Démontrons cela en utilisant le tableau dans l'image ci-dessus : `9,4,8,3,7,1,6,2,5`.

### Itération #1

Pivot = 5.
Y = 9.

Y est-il inférieur ou égal au pivot ? Non.

Incrémentez Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort1.png)

### Itération #2

Pivot = 5.
Y = 4.

Y est-il inférieur ou égal au pivot ? Oui.

##### Étape #1 - Incrémentez X

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort2.png)

##### Étape #2 - Échangez la valeur de X et Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort2i.png)

##### Étape #3 - Incrémentez Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort2ii.png)

Les itérations #1 et #2 sont essentiellement tout ce qui se passe pendant l'opération de tri.

Pour vous aider à mieux comprendre, je vais passer en revue toutes les itérations jusqu'à ce que nous ayons des nombres plus petits que le pivot à gauche et ceux plus grands à droite.

### Itération #3

Pivot = 5.
Y = 8.

Y est-il inférieur ou égal au pivot ? Non.

Incrémentez Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort3.png)

### Itération #4

Pivot = 5.
Y = 3.

Y est-il inférieur ou égal au pivot ? Oui.

##### Étape #1 - Incrémentez X

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort4.png)

##### Étape #2 - Échangez la valeur de X et Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort4i.png)

##### Étape #3 - Incrémentez Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort4ii.png)

### Itération #5

Pivot = 5.
Y = 7.

Y est-il inférieur ou égal au pivot ? Non.

Incrémentez Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort5.png)

### Itération #6

Pivot = 5.
Y = 1.

Y est-il inférieur ou égal au pivot ? Oui.

##### Étape #1 - Incrémentez X

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort6.png)

##### Étape #2 - Échangez la valeur de X et Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort6i.png)

##### Étape #3 - Incrémentez Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort6ii.png)

### Itération #7

Pivot = 5.
Y = 6.

Y est-il inférieur ou égal au pivot ? Non.

Incrémentez Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort7.png)

### Itération #8

Pivot = 5.
Y = 6.

Y est-il inférieur ou égal au pivot ? Oui.

##### Étape #1 - Incrémentez X

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort8.png)

##### Étape #2 - Échangez la valeur de X et Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort8i.png)

##### Étape #3 - Incrémentez Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort8ii.png)

### Itération #9

À ce stade, `Y` pointe maintenant sur le pivot. Vous pouvez soit incrémenter `X` et l'échanger avec `Y`, soit utiliser le format des itérations précédentes. Je vais opter pour ce dernier.

Pivot = 5.
Y = 5.

Y est-il inférieur ou égal au pivot ? Oui.

##### Étape #1 - Échangez la valeur de X et Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort9i.png)

Notre tableau ressemble maintenant à ceci : `4,3,1,2,5,8,6,9,7`

Si vous regardez l'état actuel du tableau, vous réaliserez que :

* Le pivot est maintenant au centre.
* Tous les nombres du côté gauche du pivot sont inférieurs au pivot.
* Tous les nombres du côté droit du pivot sont supérieurs au pivot.

Mais nous n'avons pas encore terminé. Les nombres sont toujours non ordonnés. Pour les trier, nous allons diviser le tableau en deux sous-tableaux (en excluant l'élément pivot).

Le premier tableau contiendra tous les nombres du côté gauche du pivot : `4,3,1,2`.

Le second tableau contiendra tous les nombres du côté droit du pivot : `8,6,9,7`.

Trions le premier tableau. Comme d'habitude, vous avez besoin d'un pivot.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array-1.png)

### Itération #1

Pivot = 2.
Y = 4.

Y est-il inférieur ou égal au pivot ? Non.

Incrémentez Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array.png)

### Itération #2

Pivot = 2.
Y = 3.

Y est-il inférieur ou égal au pivot ? Non.

Incrémentez Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array2.png)

### Itération #3

Pivot = 2.
Y = 1.

Y est-il inférieur ou égal au pivot ? Oui.

##### Étape #1 - Incrémentez X

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array3.png)

##### Étape #2 - Échangez la valeur de X et Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array3i.png)

##### Étape #3 - Incrémentez Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array4.png)

### Itération #3

Pivot = 2.
Y = 2.

Y est-il inférieur ou égal au pivot ? Oui.

##### Étape #1 - Échangez la valeur de X et Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array6.png)

Encore une fois, nous divisons le tableau en sous-tableaux en excluant le pivot (2). Notez que nous traitons toujours les nombres du côté gauche du tableau initial.

Le premier tableau contiendra ceci : `1`.

Le second tableau contiendra ceci : `4,3`.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/partition.png)

Le premier tableau n'a qu'un seul élément, il est donc déjà trié. Trions le second tableau :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/array.png)

### Itération #1

Pivot = 3.
Y = 4.

Y est-il inférieur ou égal au pivot ? Non.

Incrémentez Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/array2.png)

### Itération #2

Pivot = 3.
Y = 3.

Y est-il inférieur ou égal au pivot ? Oui.

##### Étape #1 - Échangez la valeur de X et Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/array3.png)

Nous aurons maintenant les nombres dans cet ordre :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sorted.png)

Tous les nombres du côté gauche du premier pivot ont été triés par ordre croissant : `1,2,3,4,5,8,6,9,7`.

Le processus est le même pour trier les nombres du côté droit. Il est temps d'essayer de le faire vous-même ! Suivez simplement les étapes des exemples précédents.

## Exemple de Code Java pour l'Algorithme de Tri Rapide

Voici un exemple de code en Java pour l'algorithme de tri rapide. J'ai inclus des commentaires pour rendre le code plus facile à comprendre.

Si vous avez suivi les sections précédentes, cela devrait être explicite.

```java
// Quick sort en Java

import java.util.Arrays;

class Quicksort {
    
    // méthode pour échanger les éléments x et y
    static void swap(int[] arr, int x, int y) {
        int temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
    }

  // méthode de partition
  static int partition(int array[], int low, int high) {
    
    // pivot
    int pivot = array[high];
    
    int x = (low - 1);
    
    

    // boucle pour comparer tous les éléments avec l'élément pivot
    for (int y = low; y < high; y++) {
      if (array[y] <= pivot) {
        x++;
        
        swap(array, x, y);
      }

    }

    int temp = array[x + 1];
    array[x + 1] = array[high];
    array[high] = temp;

    return (x + 1);
  }

  static void quickSort(int array[], int low, int high) {
    if (low < high) {

      int array_partition = partition(array, low, high);
      
      // tri rapide des éléments à gauche de manière récursive
      quickSort(array, low, array_partition - 1);

      // tri rapide des éléments à droite de manière récursive
      quickSort(array, array_partition + 1, high);
    }
  }
}

class Main {
  public static void main(String args[]) {

    int[] my_array = { 9,4,8,3,7,1,6,2,5 };

    int size = my_array.length;

    Quicksort.quickSort(my_array, 0, size - 1);

    System.out.println("Tableau Trié : ");
    System.out.println(Arrays.toString(my_array));
    // Tableau Trié : [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
}
```

## Exemple de Code C++ pour l'Algorithme de Tri Rapide

Voici un exemple de l'algorithme de tri rapide en C++ :

```c++
#include <bits/stdc++.h>
using namespace std;

// fonction pour échanger les éléments x et y
void swap(int* x, int* y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

int partition(int arr[], int low, int high)
{
    // pivot
	int pivot = arr[high]; 
	int x = (low- 1); 

    // boucle pour comparer tous les éléments avec l'élément pivot
	for (int y = low; y <= high - 1; y++) {
		
		if (arr[y] < pivot) {
			x++; 
			swap(&arr[x], &arr[y]);
		}
	}
	swap(&arr[x + 1], &arr[high]);
	return (x + 1);
}

void quickSort(int arr[], int low, int high)
{
	if (low < high) {
		
		int array_partition = partition(arr, low, high);
        
        // tri rapide des éléments à gauche de manière récursive
		quickSort(arr, low, array_partition - 1);
		
		// tri rapide des éléments à droite de manière récursive
		quickSort(arr, array_partition + 1, high);
	}
}

// fonction pour imprimer le tableau
void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}

int main()
{
	int arr[] = { 9,4,8,3,7,1,6,2,5 };
	
	int size = sizeof(arr) / sizeof(arr[0]);
	
	quickSort(arr, 0, size - 1);
	cout << "Tableau trié : ";
	printArray(arr, size);
    // Tableau trié : 1 2 3 4 5 6 7 8 9 
	
	return 0;
}

```

## Complexité Temporelle de l'Algorithme de Tri Rapide

Cas le pire => O(n<sup>2</sup>)

Cas moyen => O(n*log(n))

Cas le meilleur => O(n*log(n))

## Résumé

Dans cet article, nous avons parlé de l'algorithme de tri rapide.

Nous avons donné une brève explication de son fonctionnement. Après cela, nous avons vu un exemple qui expliquait comment il fonctionne sous le capot en utilisant des guides visuels pour trier un tableau non ordonné.

Nous avons également vu comment implémenter l'algorithme de tri rapide en Java et C++.

Enfin, nous avons listé la complexité temporelle du tri rapide pour les cas pire, moyen et meilleur.

Bon codage !
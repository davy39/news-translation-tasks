---
title: Algorithmes de tri expliqués avec des exemples en JavaScript, Python, Java
  et C++
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-04T22:06:00.000Z'
originalURL: https://freecodecamp.org/news/sorting-algorithms-explained-with-examples-in-python-java-and-c
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/5f9c9ede740569d1a4ca3f9d-1.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Java
  slug: java
- name: Python
  slug: python
seo_title: Algorithmes de tri expliqués avec des exemples en JavaScript, Python, Java
  et C++
seo_desc: 'What is a Sorting Algorithm?

  Sorting algorithms are a set of instructions that take an array or list as an input
  and arrange the items into a particular order.

  Sorts are most commonly in numerical or a form of alphabetical (or lexicographical)
  order,...'
---

## Qu'est-ce qu'un algorithme de tri ?

Les algorithmes de tri sont un ensemble d'instructions qui prennent un tableau ou une liste en entrée et organisent les éléments dans un ordre particulier.

Les tris sont le plus souvent numériques ou sous une forme d'ordre alphabétique (ou lexicographique), et peuvent être en ordre croissant (A-Z, 0-9) ou décroissant (Z-A, 9-0).

## Pourquoi les algorithmes de tri sont importants

Puisqu'ils peuvent souvent réduire la complexité d'un problème, les algorithmes de tri sont très importants en informatique. Ces algorithmes ont des applications directes dans les algorithmes de recherche, les algorithmes de base de données, les méthodes de division et de conquête, les algorithmes de structure de données, et bien d'autres.

## Compromis des algorithmes de tri

Lors du choix d'un algorithme de tri, certaines questions doivent être posées – Quelle est la taille de la collection à trier ? Quelle quantité de mémoire est disponible ? La collection doit-elle croître ?

Les réponses à ces questions peuvent déterminer quel algorithme fonctionnera le mieux pour chaque situation. Certains algorithmes comme le tri fusion peuvent nécessiter beaucoup d'espace ou de mémoire pour fonctionner, tandis que le tri par insertion n'est pas toujours le plus rapide, mais ne nécessite pas beaucoup de ressources pour fonctionner.

Vous devez déterminer quelles sont vos exigences et considérer les limitations de votre système avant de décider quel algorithme de tri utiliser.

## Quelques algorithmes de tri courants

Certains des algorithmes de tri les plus courants sont :

* Tri par sélection
* Tri à bulles
* Tri par insertion
* Tri fusion
* Tri rapide
* Tri par tas
* Tri par comptage
* Tri par base
* Tri par compartiment

Mais avant d'aborder chacun de ces algorithmes, apprenons un peu plus sur ce qui classe un algorithme de tri.

## Classification d'un algorithme de tri

Les algorithmes de tri peuvent être catégorisés en fonction des paramètres suivants :

1. **Le nombre d'échanges ou d'inversions requis :** Il s'agit du nombre de fois où l'algorithme échange des éléments pour trier l'entrée. Le tri par sélection nécessite le nombre minimum d'échanges.
2. **Le nombre de comparaisons :** Il s'agit du nombre de fois où l'algorithme compare des éléments pour trier l'entrée. En utilisant la [notation Big-O](https://guide.freecodecamp.org/computer-science/notation/big-o-notation/), les exemples d'algorithmes de tri listés ci-dessus nécessitent au moins `O(nlogn)` comparaisons dans le meilleur des cas, et `O(n^2)` comparaisons dans le pire des cas pour la plupart des résultats.
3. **S'ils utilisent ou non la récursion :** Certains algorithmes de tri, tels que le tri rapide, utilisent des techniques récursives pour trier l'entrée. D'autres algorithmes de tri, tels que le tri par sélection ou le tri par insertion, utilisent des techniques non récursives. Enfin, certains algorithmes de tri, tels que le tri fusion, utilisent à la fois des techniques récursives et non récursives pour trier l'entrée.
4. **S'ils sont stables ou instables :** Les algorithmes de tri stables maintiennent l'ordre relatif des éléments ayant des valeurs égales, ou des clés. Les algorithmes de tri instables ne maintiennent pas l'ordre relatif des éléments ayant des valeurs/clés égales.

Par exemple, imaginez que vous avez le tableau d'entrée `[1, 2, 3, 2, 4]`. Et pour aider à différencier les deux valeurs égales, `2`, mettons-les à jour en `2a` et `2b`, ce qui donne le tableau d'entrée `[1, 2a, 3, 2b, 4]`.

Les algorithmes de tri stables maintiendront l'ordre de `2a` et `2b`, ce qui signifie que le tableau de sortie sera `[1, 2a, 2b, 3, 4]`. Les algorithmes de tri instables ne maintiennent pas l'ordre des valeurs égales, et le tableau de sortie peut être `[1, 2b, 2a, 3, 4]`.

Le tri par insertion, le tri fusion et le tri à bulles sont stables. Le tri par tas et le tri rapide sont instables.
5. **La quantité d'espace supplémentaire requis :** Certains algorithmes de tri peuvent trier une liste sans créer une nouvelle liste entièrement. Ce sont les algorithmes de tri en place, et ils nécessitent un espace supplémentaire constant `O(1)` pour le tri. Pendant ce temps, les algorithmes de tri hors place créent une nouvelle liste pendant le tri.

Le tri par insertion et le tri rapide sont des algorithmes de tri en place, car les éléments sont déplacés autour d'un point de pivot, et n'utilisent pas un tableau séparé.

Le tri fusion est un exemple d'algorithme de tri hors place, car la taille de l'entrée doit être allouée au préalable pour stocker la sortie pendant le processus de tri, ce qui nécessite une mémoire supplémentaire.

## Tri par compartiment

Le tri par compartiment est un algorithme de tri par comparaison qui fonctionne sur des éléments en les divisant en différents compartiments et en triant ensuite ces compartiments individuellement. Chaque compartiment est trié individuellement en utilisant un algorithme de tri séparé comme le tri par insertion, ou en appliquant récursivement l'algorithme de tri par compartiment.

Le tri par compartiment est principalement utile lorsque l'entrée est uniformément distribuée sur une plage. Par exemple, imaginez que vous avez un grand tableau d'entiers à virgule flottante distribués uniformément entre une borne supérieure et une borne inférieure.

Vous pourriez utiliser un autre algorithme de tri comme le tri fusion, le tri par tas ou le tri rapide. Cependant, ces algorithmes garantissent une complexité de temps dans le meilleur des cas de `O(nlogn)`.

En utilisant le tri par compartiment, le tri du même tableau peut être complété en temps `O(n)`.

### Pseudo-code pour le tri par compartiment :

```
void bucketSort(float[] a,int n)

{

    for(each floating integer 'x' in n)

    {
        insert x into bucket[n*x]; 
    }

    for(each bucket)

    {
        sort(bucket);
    }

}

```

## Tri par comptage

L'algorithme de tri par comptage fonctionne en créant d'abord une liste des comptes ou des occurrences de chaque valeur unique dans la liste. Il crée ensuite une liste triée finale basée sur la liste des comptes.

Une chose importante à retenir est que le tri par comptage ne peut être utilisé que lorsque vous connaissez la plage des valeurs possibles dans l'entrée au préalable.

### Exemple :

```
Disons que vous avez une liste d'entiers de 0 à 5 :
 
input = [2, 5, 3, 1, 4, 2]

Tout d'abord, vous devez créer une liste de comptes pour chaque valeur unique dans
the `input` list. Puisque vous connaissez la plage de `input` est de 0 à
5, vous pouvez créer une liste avec cinq placeholders pour les valeurs 0 à 5,
respectivement :

count = [0, 0, 0, 0, 0, 0]
  # val: 0  1  2  3  4  5

Ensuite, vous parcourez la liste `input` et incrémentez l'index pour chaque valeur de un.

Par exemple, la première valeur dans la liste `input` est 2, donc vous ajoutez un
à la valeur à la deuxième index de la liste `count`, qui représente
the valeur 2 :

count = [0, 0, 1, 0, 0, 0]
  # val: 0  1  2  3  4  5
       
La prochaine valeur dans la liste `input` est 5, donc vous ajoutez un à la valeur à
the dernier index de la liste `count`, qui représente la valeur 5 :

count = [0, 0, 1, 0, 0, 1]
  # val: 0  1  2  3  4  5

Continuez jusqu'à ce que vous ayez le compte total pour chaque valeur dans la liste `input` :

count = [0, 1, 2, 1, 1, 1]
  # val: 0  1  2  3  4  5

Enfin, puisque vous savez combien de fois chaque valeur dans la liste `input`
apparaît, vous pouvez facilement créer une liste `output` triée. Parcourez
the liste `count`, et pour chaque compte, ajoutez la valeur correspondante
(0 - 5) à la liste `output` autant de fois.

Par exemple, il n'y avait pas de 0 dans la liste `input`, mais il y avait une
occurrence de la valeur 1, donc vous ajoutez cette valeur à la liste `output`
une fois :

output = [1]

Ensuite, il y avait deux occurrences de la valeur 2, donc vous les ajoutez à la
liste `output` :

output = [1, 2, 2]

Et ainsi de suite jusqu'à ce que vous ayez la liste `output` triée finale :

output = [1, 2, 2, 3, 4, 5]

```

### Propriétés

* Complexité spatiale : `O(k)`
* Meilleure performance : `O(n+k)`
* Performance moyenne : `O(n+k)`
* Pire performance : `O(n+k)`
* Stable : Oui (`k` est la plage des éléments dans le tableau)

### Implémentation en JavaScript

```js
let numbers = [1, 4, 1, 2, 7, 5, 2];
let count = [];
let output =[];
let i = 0;
let max = Math.max(...numbers);

// initialiser le compteur
for (i = 0; i <= max; i++) {
  count[i] = 0;
}

// initialiser le tableau de sortie
for (i = 0; i < numbers.length; i++) {
  output[i] = 0;
}

for (i = 0; i < numbers.length; i++) {
  count[numbers[i]]++;
}

for (i = 1; i < count.length; i++) {
  count[i] += count[i-1];
}

for (i = numbers.length - 1; i >= 0; i--) { 
  output[--count[numbers[i]]] = numbers[i];
}

// sortie du tableau trié
for (i = 0; i < output.length; i++) {
  console.log(output[i]);
}
```

### Implémentation en C++

```cpp
#include <iostream>

#include <vector>

void countSort(int upperBound, int lowerBound, std::vector < int > numbersToSort) // Lower and upper bounds of numbers in vector
{
  int i;
  int range = upperBound - lowerBound; // Create a range large enough to get every number between the min and max
  std::vector < int > counts(range + 1); // Initialize of counts of the size of the range
  std::fill(counts.begin(), counts.end(), 0); // Fill vector of zeros
  std::vector < int > storedNumbers(numbersToSort.size()); // Initialize of storedNumbers of the same size as the input vector
  std::fill(storedNumbers.begin(), storedNumbers.end(), 0); // Fill storedNumbers vector of zeros

  for (i = 0; i < numbersToSort.size(); i++) {
    int index = numbersToSort[i] - lowerBound; // For example, if 5 is the lower bound and numbersToSort[i] is 5, the index will be 0 and the
    counts[index] += 1; // count of 5 will be stored in counts[0]
  }

  for (i = 1; i < counts.size(); i++) {
    counts[i] += counts[i - 1];
  }

  for (i = numbersToSort.size() - 1; i >= 0; i--) { // Copy elements from numbersToSort to storedNumbers according to the count
    storedNumbers[--counts[numbersToSort[i] - lowerBound]] = numbersToSort[i];
  }

  for (i = 0; i < storedNumbers.size(); i++) {
    std::cout << storedNumbers[i];
    if (i != storedNumbers.size() - 1)
      std::cout << ", ";
  }
  std::cout << std::endl;
}
```

### Implémentation en Swift

```swift
func countingSort(_ array: [Int]) {
  // Create an array to store the count of each element
  let maxElement = array.max() ?? 0
  var countArray = [Int](repeating: 0, count: Int(maxElement + 1))
  
  for element in array {
    countArray[element] += 1
  }
  
  for i in 1 ..< countArray.count {
    countArray[i] += countArray[i-1];
  }
  
  var sortedArray = [Int](repeating: 0, count: array.count)
  
  // copy elements from array to sortedArray according to the count
  for i in (0 ..< array.count) .reversed() {
    countArray[array[i]] -= 1
    sortedArray[countArray[array[i]]] = array[i];
  }
  
  print(sortedArray)
}
```

## Tri par insertion

Le tri par insertion est un algorithme de tri simple pour un petit nombre d'éléments.

### Exemple :

Dans le tri par insertion, vous comparez l'élément `key` avec les éléments précédents. Si les éléments précédents sont plus grands que l'élément `key`, alors vous déplacez l'élément précédent à la position suivante.

Commencez à partir de l'index 1 jusqu'à la taille du tableau d'entrée.

[ 8 3 5 1 4 2 ]

Étape 1 :

![[ 8 3 5 1 4 2 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/1.png?raw=true)

```
      key = 3 //en commençant par le 1er index.

      Ici, `key` sera comparé avec les éléments précédents.

      Dans ce cas, `key` est comparé avec 8. puisque 8 > 3, déplacez l'élément 8
      à la position suivante et insérez `key` à la position précédente.

      Résultat : [ 3 8 5 1 4 2 ]

```

Étape 2 :

![[ 3 8 5 1 4 2 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/2.png?raw=true)

```
      key = 5 //2ème index

      8 > 5 //déplacez 8 au 2ème index et insérez 5 au 1er index.

      Résultat : [ 3 5 8 1 4 2 ]

```

Étape 3 :

![[ 3 5 8 1 4 2 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/3.png?raw=true)

```
      key = 1 //3ème index

      8 > 1     => [ 3 5 1 8 4 2 ]  

      5 > 1     => [ 3 1 5 8 4 2 ]

      3 > 1     => [ 1 3 5 8 4 2 ]

      Résultat : [ 1 3 5 8 4 2 ]

```

Étape 4 :

![[ 1 3 5 8 4 2 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/4.png?raw=true)

```
      key = 4 //4ème index

      8 > 4   => [ 1 3 5 4 8 2 ]

      5 > 4   => [ 1 3 4 5 8 2 ]

      3 > 4   ≠>  stop

      Résultat : [ 1 3 4 5 8 2 ]

```

Étape 5 :

![[ 1 3 4 5 8 2 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/5.png?raw=true)

```
      key = 2 //5ème index

      8 > 2   => [ 1 3 4 5 2 8 ]

      5 > 2   => [ 1 3 4 2 5 8 ]

      4 > 2   => [ 1 3 2 4 5 8 ]

      3 > 2   => [ 1 2 3 4 5 8 ]

      1 > 2   ≠> stop

      Résultat : [1 2 3 4 5 8]

```

![[ 1 2 3 4 5 8 ]](https://github.com/blulion/freecodecamp-resource/blob/master/insertion_sort/6.png?raw=true)

L'algorithme montré ci-dessous est une version légèrement optimisée pour éviter d'échanger l'élément `key` à chaque itération. Ici, l'élément `key` sera échangé à la fin de l'itération (étape).

```
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

```js
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

Une implémentation rapide en Swift est montrée ci-dessous :

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

L'exemple en Java est montré ci-dessous :

```java
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

Et en C....

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
* Complexité temporelle : O(n), O(n* n), O(n* n) pour les meilleurs, moyens, pires cas respectivement.
* Meilleur cas : le tableau est déjà trié
* Cas moyen : le tableau est trié aléatoirement
* Pire cas : le tableau est trié à l'envers.
* Tri en place : Oui
* Stable : Oui

## Tri par tas

Le tri par tas est un algorithme de tri efficace basé sur l'utilisation de tas max/min. Un tas est une structure de données basée sur les arbres qui satisfait la propriété de tas – c'est-à-dire pour un tas max, la clé de tout nœud est inférieure ou égale à la clé de son parent (s'il a un parent).

Cette propriété peut être exploitée pour accéder à l'élément maximum dans le tas en temps O(logn) en utilisant la méthode maxHeapify. Nous effectuons cette opération n fois, chaque fois en déplaçant l'élément maximum dans le tas au sommet du tas et en l'extrayant du tas et dans un tableau trié. Ainsi, après n itérations, nous aurons une version triée du tableau d'entrée.

L'algorithme n'est pas un algorithme en place et nécessiterait une structure de données de tas à construire d'abord. L'algorithme est également instable, ce qui signifie que lors de la comparaison d'objets avec la même clé, l'ordre d'origine ne serait pas préservé.

Cet algorithme s'exécute en temps O(nlogn) et en espace supplémentaire O(1) [O(n) incluant l'espace requis pour stocker les données d'entrée] puisque toutes les opérations sont effectuées entièrement en place.

La meilleure, pire et moyenne complexité temporelle du tri par tas est O(nlogn). Bien que le tri par tas ait une meilleure complexité dans le pire des cas que le tri rapide, un tri rapide bien implémenté s'exécute plus rapidement en pratique. Il s'agit d'un algorithme basé sur la comparaison, il peut donc être utilisé pour des ensembles de données non numériques dans la mesure où une relation (propriété de tas) peut être définie sur les éléments.

Une implémentation en Java est montrée ci-dessous :

```java
import java.util.Arrays;
public class Heapsort {

	public static void main(String[] args) {
		//test array
		Integer[] arr = {1, 4, 3, 2, 64, 3, 2, 4, 5, 5, 2, 12, 14, 5, 3, 0, -1};
		String[] strarr = {"hope you find this helpful!", "wef", "rg", "q2rq2r", "avs", "erhijer0g", "ewofij", "gwe", "q", "random"};
		arr = heapsort(arr);
		strarr = heapsort(strarr);
		System.out.println(Arrays.toString(arr));
		System.out.println(Arrays.toString(strarr));
	}
	
	//O(nlogn) TIME, O(1) SPACE, NOT STABLE
	public static <E extends Comparable<E>> E[] heapsort(E[] arr){
		int heaplength = arr.length;
		for(int i = arr.length/2; i>0;i--){
			arr = maxheapify(arr, i, heaplength);
		}
		
		for(int i=arr.length-1;i>=0;i--){
			E max = arr[0];
			arr[0] = arr[i];
			arr[i] = max;
			heaplength--;
			arr = maxheapify(arr, 1, heaplength);
		}
		
		return arr;
	}
	
	//Creates maxheap from array
	public static <E extends Comparable<E>> E[] maxheapify(E[] arr, Integer node, Integer heaplength){
		Integer left = node*2;
		Integer right = node*2+1;
		Integer largest = node;
		
		if(left.compareTo(heaplength) <=0 && arr[left-1].compareTo(arr[node-1]) >= 0){
			largest = left;
		}
		if(right.compareTo(heaplength) <= 0 && arr[right-1].compareTo(arr[largest-1]) >= 0){
			largest = right;
		}	
		if(largest != node){
			E temp = arr[node-1];
			arr[node-1] = arr[largest-1];
			arr[largest-1] = temp;
			maxheapify(arr, largest, heaplength);
		}
		return arr;
	}
}

```

Implémentation en C++

```cpp
#include <iostream>
using namespace std;
void heapify(int arr[], int n, int i) 
{ 
    int largest = i; 
    int l = 2*i + 1;  
    int r = 2*i + 2;
    if (l < n && arr[l] > arr[largest]) 
        largest = l;
    if (r < n && arr[r] > arr[largest]) 
        largest = r;
    if (largest != i) 
    { 
        swap(arr[i], arr[largest]); 
  
        
        heapify(arr, n, largest); 
    } 
} 
  
 
void heapSort(int arr[], int n) 
{ 
    
    for (int i = n / 2 - 1; i >= 0; i--) 
        heapify(arr, n, i); 
  
    
    for (int i=n-1; i>=0; i--) 
    { 

        swap(arr[0], arr[i]); 
  
        
        heapify(arr, i, 0); 
    } 
} 
void printArray(int arr[], int n) 
{ 
    for (int i=0; i<n; ++i) 
        cout << arr[i] << " "; 
    cout << "\n"; 
} 
int main() 
{ 
    int arr[] = {12, 11, 13, 5, 6, 7}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
  
    heapSort(arr, n); 
  
    cout << "Sorted array is \n"; 
    printArray(arr, n); 
}

```

## Tri par base

Prérequis : Tri par comptage

QuickSort, MergeSort et HeapSort sont des algorithmes de tri basés sur la comparaison. CountSort ne l'est pas. Il a une complexité de O(n+k), où k est l'élément maximum du tableau d'entrée. Donc, si k est O(n), CountSort devient un tri linéaire, ce qui est meilleur que les algorithmes de tri basés sur la comparaison qui ont une complexité temporelle de O(nlogn).

L'idée est d'étendre l'algorithme CountSort pour obtenir une meilleure complexité temporelle lorsque k va O(n2). Voici l'idée du tri par base.

### L'algorithme :

Pour chaque chiffre i où i varie du chiffre le moins significatif au chiffre le plus significatif d'un nombre, triez le tableau d'entrée en utilisant l'algorithme de tri par comptage selon le ième chiffre. Nous avons utilisé le tri par comptage car il s'agit d'un tri stable.

Exemple : Supposons que le tableau d'entrée est :

10, 21, 17, 34, 44, 11, 654, 123

Selon l'algorithme, nous allons trier le tableau d'entrée selon le chiffre des unités (chiffre le moins significatif).

0: 10  
1: 21 11  
2:  
3: 123  
4: 34 44 654  
5:  
6:  
7: 17  
8:  
9:

Ainsi, le tableau devient 10, 21, 11, 123, 24, 44, 654, 17. 

Maintenant, nous allons trier selon le chiffre des dizaines :

0:  
1: 10 11 17  
2: 21 123  
3: 34  
4: 44  
5: 654  
6:  
7:  
8:  
9:

Maintenant, le tableau devient : 10, 11, 17, 21, 123, 34, 44, 654.

Enfin, nous trions selon le chiffre des centaines (chiffre le plus significatif) :

0: 010 011 017 021 034 044  
1: 123  
2:  
3:  
4:  
5:  
6: 654  
7:  
8:  
9:

Le tableau devient : 10, 11, 17, 21, 34, 44, 123, 654 qui est trié. C'est ainsi que fonctionne notre algorithme.

Une implémentation en C :

```c
void countsort(int arr[],int n,int place){

        int i,freq[range]={0};         //range for integers is 10 as digits range from 0-9
        int output[n];

        for(i=0;i<n;i++)
                freq[(arr[i]/place)%range]++;

        for(i=1;i<range;i++)
                freq[i]+=freq[i-1];
        
        for(i=n-1;i>=0;i--){
                output[freq[(arr[i]/place)%range]-1]=arr[i];
                freq[(arr[i]/place)%range]--;
        }
        
        for(i=0;i<n;i++)
                arr[i]=output[i];
}

void radixsort(ll arr[],int n,int maxx){            //maxx is the maximum element in the array

        int mul=1;
        while(maxx){
                countsort(arr,n,mul);
                mul*=10;
                maxx/=10;
        }
}

```

## Tri par sélection

Le tri par sélection est l'un des algorithmes de tri les plus simples. Cet algorithme tire son nom de la manière dont il parcourt le tableau : il sélectionne l'élément actuel le plus petit et l'échange à sa place.

Voici comment cela fonctionne :

1. Trouvez le plus petit élément dans le tableau et échangez-le avec le premier élément.
2. Trouvez le deuxième plus petit élément et échangez-le avec le deuxième élément du tableau.
3. Trouvez le troisième plus petit élément et échangez-le avec le troisième élément du tableau.
4. Répétez le processus de recherche de l'élément suivant le plus petit et échangez-le à la position correcte jusqu'à ce que le tableau entier soit trié.

Mais, comment écrire le code pour trouver l'index de la deuxième plus petite valeur dans un tableau ?

Une manière facile est de remarquer que la plus petite valeur a déjà été échangée à l'index 0, donc le problème se réduit à trouver le plus petit élément dans le tableau commençant à l'index 1.

Le tri par sélection prend toujours le même nombre de comparaisons de clés – N(N - 1)/2.

### Implémentation en C/C++

Le programme C++ suivant contient une implémentation itérative ainsi qu'une implémentation récursive de l'algorithme de tri par sélection. Les deux implémentations sont invoquées dans la fonction `main()`.

```cpp
#include <iostream>
#include <string>
using namespace std;

template<typename T, size_t n>
void print_array(T const(&arr)[n]) {
    for (size_t i = 0; i < n; i++)
        std::cout << arr[i] << ' ';
    cout << "\n";
}

int minIndex(int a[], int i, int j) {
    if (i == j)
        return i;
    int k = minIndex(a, i + 1, j);
    return (a[i] < a[k]) ? i : k;
}

void recurSelectionSort(int a[], int n, int index = 0) {
    if (index == n)
        return;
    int k = minIndex(a, index, n - 1);
    if (k != index)
        swap(a[k], a[index]);
    recurSelectionSort(a, n, index + 1);
}

void iterSelectionSort(int a[], int n) {
    for (int i = 0; i < n; i++)
    {
        int min_index = i;
        int min_element = a[i];
        for (int j = i + 1; j < n; j++)
        {
            if (a[j] < min_element)
            {
                min_element = a[j];
                min_index = j;
            }
        }
        swap(a[i], a[min_index]);
    }
}

int main() {
    int recurArr[6] = { 100,35, 500, 9, 67, 20 };
    int iterArr[5] = { 25, 0, 500, 56, 98 };

    cout << "Recursive Selection Sort"  << "\n";
    print_array(recurArr); // 100 35 500 9 67 20
    recurSelectionSort(recurArr, 6);
    print_array(recurArr); // 9 20 35 67 100 500

    cout << "Iterative Selection Sort" << "\n";
    print_array(iterArr); // 25 0 500 56 98
    iterSelectionSort(iterArr, 5);
    print_array(iterArr); // 0 25 56 98 500
}

```

### Implémentation en JavaScript

```js
function selection_sort(A) {
    var len = A.length;
    for (var i = 0; i < len - 1; i = i + 1) {
        var j_min = i;
        for (var j = i + 1; j < len; j = j + 1) {
            if (A[j] < A[j_min]) {
                j_min = j;
            } else {}
        }
        if (j_min !== i) {
            swap(A, i, j_min);
        } else {}
    }
}

function swap(A, x, y) {
    var temp = A[x];
    A[x] = A[y];
    A[y] = temp;
}

```

### Implémentation en Python

```ps
def seletion_sort(arr):
         if not arr:
         return arr
    for i in range(len(arr)):
         min_i = i
         for j in range(i + 1, len(arr)):
              if arr[j] < arr[min_i]:
                  min_i = j
         arr[i], arr[min_i] = arr[min_i], arr[i]

```

### Implémentation en Java

```java
public void selectionsort(int array[])
{
    int n = array.length;            //method to find length of array 
    for (int i = 0; i < n-1; i++)
    {
        int index = i;
        int min = array[i];          // taking the min element as ith element of array
        for (int j = i+1; j < n; j++)
        {
            if (array[j] < array[index])
            {
                index = j;
                min = array[j];
            }
        }
        int t = array[index];         //Interchange the places of the elements
        array[index] = array[i];
        array[i] = t;
    }
}

```

### Implémentation en MATLAB

```
function [sorted] = selectionSort(unsorted)
    len = length(unsorted);
    for i = 1:1:len
        minInd = i;
        for j = i+1:1:len
           if unsorted(j) < unsorted(minInd) 
               minInd = j;
           end
        end
        unsorted([i minInd]) = unsorted([minInd i]);    
    end
    sorted = unsorted;
end

```

### Propriétés

* Complexité spatiale : **O(n)**
* Complexité temporelle : **O(n2)**
* Tri en place : **Oui**
* Stable : **Non**

## Tri à bulles

Tout comme les bulles remontent du fond d'un verre, le **tri à bulles** est un algorithme simple qui trie une liste, permettant aux valeurs inférieures ou supérieures de remonter à la surface. L'algorithme parcourt une liste et compare les valeurs adjacentes, les échangeant si elles ne sont pas dans le bon ordre.

Avec une complexité dans le pire des cas de O(n^2), le tri à bulles est très lent par rapport à d'autres algorithmes de tri comme le tri rapide. L'avantage est qu'il est l'un des algorithmes de tri les plus faciles à comprendre et à coder à partir de zéro.

D'un point de vue technique, le tri à bulles est raisonnable pour trier des tableaux de petite taille ou spécialement lors de l'exécution d'algorithmes de tri sur des ordinateurs avec des ressources mémoire remarquablement limitées.

### Exemple :

### Premier passage à travers la liste :

* En commençant par `[4, 2, 6, 3, 9]`, l'algorithme compare les deux premiers éléments du tableau, 4 et 2. Il les échange car 2 < 4 : `[2, 4, 6, 3, 9]`
* Il compare les deux valeurs suivantes, 4 et 6. Comme 4 < 6, elles sont déjà dans l'ordre, et l'algorithme continue : `[2, 4, 6, 3, 9]`
* Les deux valeurs suivantes sont également échangées car 3 < 6 : `[2, 4, 3, 6, 9]`
* Les deux dernières valeurs, 6 et 9, sont déjà dans l'ordre, donc l'algorithme ne les échange pas.

### Deuxième passage à travers la liste :

* 2 < 4, donc il n'est pas nécessaire d'échanger les positions : `[2, 4, 3, 6, 9]`
* L'algorithme échange les deux valeurs suivantes car 3 < 4 : `[2, 3, 4, 6, 9]`
* Pas d'échange car 4 < 6 : `[2, 3, 4, 6, 9]`
* Encore une fois, 6 < 9, donc aucun échange ne se produit : `[2, 3, 4, 6, 9]`

La liste est déjà triée, mais l'algorithme de tri à bulles ne le réalise pas. Plutôt, il doit compléter un passage entier à travers la liste sans échanger de valeurs pour savoir que la liste est triée.

### Troisième passage à travers la liste :

* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`
* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`
* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`
* `[2, 4, 3, 6, 9]` => `[2, 4, 3, 6, 9]`

Clairement, le tri à bulles est loin d'être l'algorithme de tri le plus efficace. Pourtant, il est simple à comprendre et à implémenter soi-même.

#### Propriétés

* Complexité spatiale : O(1)
* Meilleure performance : O(n)
* Performance moyenne : O(n*n)
* Pire performance : O(n*n)
* Stable : Oui

### Explication vidéo

[Algorithme de tri à bulles](https://www.youtube.com/watch?v=Jdtq5uKz-w4)

### Exemple en JavaScript

```js
let arr = [1, 4, 7, 45, 7,43, 44, 25, 6, 4, 6, 9],
    sorted = false;

while(!sorted) {
  sorted = true;
  for(var i=0; i < arr.length; i++) {
    if(arr[i] < arr[i-1]) {
      let temp = arr[i];
      arr[i] = arr[i-1];
      arr[i-1] = temp;
      sorted = false;
    }
  }
}

```

### Exemple en Java

```java
public class BubbleSort {
    static void sort(int[] arr) {
        int n = arr.length;
        int temp = 0;
         for(int i=0; i < n; i++){
                 for(int x=1; x < (n-i); x++){
                          if(arr[x-1] > arr[x]){
                                 temp = arr[x-1];
                                 arr[x-1] = arr[x];
                                 arr[x] = temp;
                         }

                 }
         }

    }
    public static void main(String[] args) {

		for(int i=0; i < 15; i++){
			int arr[i] = (int)(Math.random() * 100 + 1);
		}

                System.out.println("array before sorting\n");
                for(int i=0; i < arr.length; i++){
                        System.out.print(arr[i] + " ");
                }
                bubbleSort(arr);
                System.out.println("\n array after sorting\n");
                for(int i=0; i < arr.length; i++){
                        System.out.print(arr[i] + " ");
                }

        }
}

```

### Exemple en C++

```cpp
// Implémentation récursive
void bubblesort(int arr[], int n)
{
	if(n==1)	//Cas initial
		return;
	bool swap_flag = false;
	for(int i=0;i<n-1;i++)	//Après ce passage, le plus grand élément se déplacera à sa position souhaitée.
	{
		if(arr[i]>arr[i+1])
		{
			int temp=arr[i];
			arr[i]=arr[i+1];
			arr[i+1]=temp;
			swap_flag = true;
		}
	}
        // SI aucun élément n'a été échangé dans la boucle, alors retourner, car le tableau est trié 
	if(swap_flag == false)
		return;
	bubblesort(arr,n-1);	//Récursion pour le tableau restant
}

```

### Exemple en Swift

```swift
func bubbleSort(_ inputArray: [Int]) -> [Int] {
    guard inputArray.count > 1 else { return inputArray } // make sure our input array has more than 1 element
    var numbers = inputArray // function arguments are constant by default in Swift, so we make a copy
    for i in 0..<(numbers.count - 1) {
        for j in 0..<(numbers.count - i - 1) {
            if numbers[j] > numbers[j + 1] {
                numbers.swapAt(j, j + 1)
            }
        }
    }
    return numbers // return the sorted array
} 

```

### Exemple en Python

```py
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1):
                if arr[j] > arr[j+1] : 
                        arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

```

### Exemple en PHP

```php
function bubble_sort($arr) {
    $size = count($arr)-1;
    for ($i=0; $i<$size; $i++) {
        for ($j=0; $j<$size-$i; $j++) {
            $k = $j+1;
            if ($arr[$k] < $arr[$j]) {
                // Swap elements at indices: $j, $k
                list($arr[$j], $arr[$k]) = array($arr[$k], $arr[$j]);
            }
        }
    }
    return $arr;// return the sorted array
}

$arr = array(1,3,2,8,5,7,4,0);
print("Before sorting");
print_r($arr);

$arr = bubble_sort($arr);
print("After sorting by using bubble sort");
print_r($arr);

```

### Exemple en C

```c
#include <stdio.h>

int BubbleSort(int array[], int n);

int main(void) {
  int arr[] = {10, 2, 3, 1, 4, 5, 8, 9, 7, 6};
  BubbleSort(arr, 10);

  for (int i = 0; i < 10; i++) {
    printf("%d", arr[i]);
  }
  return 0;
}
int BubbleSort(int array[], n)
{
for (int i = 0 ; i < n - 1; i++)
  {
    for (int j = 0 ; j < n - i - 1; j++)     //n est la longueur du tableau
    {
      if (array[j] > array[j+1])      // Pour l'ordre décroissant, utilisez 
      {
        int swap   = array[j];
        array[j]   = array[j+1];
        array[j+1] = swap;
      }
    }
  }
}

```

## Tri rapide

Le tri rapide est un algorithme de tri efficace de type diviser pour régner. La complexité temporelle moyenne du tri rapide est O(nlog(n)) avec une complexité temporelle dans le pire des cas de O(n^2) en fonction de la sélection de l'élément pivot, qui divise le tableau actuel en deux sous-tableaux.

Par exemple, la complexité temporelle du tri rapide est approximativement `O(nlog(n))` lorsque la sélection du pivot divise le tableau original en deux sous-tableaux de taille presque égale.

D'autre part, si l'algorithme, qui sélectionne l'élément pivot des tableaux d'entrée, produit systématiquement 2 sous-tableaux avec une grande différence en termes de tailles de tableaux, l'algorithme de tri rapide peut atteindre la complexité temporelle dans le pire des cas de O(n^2).

Les étapes impliquées dans le tri rapide sont :

* Choisissez un élément pour servir de pivot, dans ce cas, le dernier élément du tableau est le pivot.
* Partitionnement : Triez le tableau de manière à ce que tous les éléments inférieurs au pivot soient à gauche, et tous les éléments supérieurs au pivot soient à droite.
* Appelez Quicksort récursivement, en tenant compte du pivot précédent pour subdiviser correctement les tableaux de gauche et de droite. (Une explication plus détaillée peut être trouvée dans les commentaires ci-dessous)

## Exemples d'implémentation dans divers langages

### Implémentation en JavaScript :

```js
const arr = [6, 2, 5, 3, 8, 7, 1, 4];

const quickSort = (arr, start, end) => {

  if(start < end) {

    // Vous pouvez apprendre comment la valeur du pivot est dérivée dans les commentaires ci-dessous
    let pivot = partition(arr, start, end);

    // Assurez-vous de lire les commentaires ci-dessous pour comprendre pourquoi pivot - 1 et pivot + 1 sont utilisés
    // Ce sont les appels récursifs à quickSort
    quickSort(arr, start, pivot - 1);
    quickSort(arr, pivot + 1, end);
  } 

}

const partition = (arr, start, end) => { 
  let pivot = end;
  // Définissez i à start - 1 afin qu'il puisse accéder au premier index dans le cas où la valeur à arr[0] est supérieure à arr[pivot]
  // Les commentaires suivants développeront le commentaire ci-dessus
  let i = start - 1,
      j = start;

  // Incrémentez j jusqu'à l'index précédant le pivot
  while (j < pivot) {

    // Si la valeur est supérieure au pivot, incrémentez j
    if (arr[j] > arr[pivot]) {
      j++;
    }

    // Lorsque la valeur à arr[j] est inférieure au pivot :
    // incrémentez i (arr[i] sera une valeur supérieure à arr[pivot]) et échangez la valeur à arr[i] et arr[j]
    else {
      i++;
      swap(arr, j, i);
      j++;
    }

  }

  // La valeur à arr[i + 1] sera supérieure à la valeur de arr[pivot]
  swap(arr, i + 1, pivot);

  // Vous retournez i + 1, car les valeurs à sa gauche sont inférieures à arr[i+1], et les valeurs à droite sont supérieures à arr[i + 1]
  // Ainsi, lorsque les tris rapides récursifs sont appelés, les nouveaux sous-tableaux n'incluront pas cette valeur de pivot précédemment utilisée
  return i + 1;
}

const swap = (arr, firstIndex, secondIndex) => {
  let temp = arr[firstIndex];
  arr[firstIndex] = arr[secondIndex];
  arr[secondIndex] = temp;
}

quickSort(arr, 0, arr.length - 1);
console.log(arr);

```

### Implémentation en C

```c
#include<stdio.h>  
void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
}
int partition (int arr[], int low, int high) 
{ 
    int pivot = arr[high];     
    int i = (low - 1);  
  
    for (int j = low; j <= high- 1; j++) 
    { 
        if (arr[j] <= pivot) 
        { 
            i++;    
            swap(&arr[i], &arr[j]); 
        } 
    } 
    swap(&arr[i + 1], &arr[high]); 
    return (i + 1); 
}
void quickSort(int arr[], int low, int high) 
{ 
    if (low < high) 
    {
        int pi = partition(arr, low, high); 
  
        quickSort(arr, low, pi - 1); 
        quickSort(arr, pi + 1, high); 
    } 
} 
  

void printArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("n"); 
} 
  

int main() 
{ 
    int arr[] = {10, 7, 8, 9, 1, 5}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    quickSort(arr, 0, n-1); 
    printf("Sorted array: n"); 
    printArray(arr, n); 
    return 0; 
} 

```

### Implémentation en Python3

```
import random

z=[random.randint(0,100) for i in range(0,20)]

def quicksort(z):
    if(len(z)>1):        
        piv=int(len(z)/2)
        val=z[piv]
        lft=[i for i in z if i<val]
        mid=[i for i in z if i==val]
        rgt=[i for i in z if i>val]

        res=quicksort(lft)+mid+quicksort(rgt)
        return res
    else:
        return z
        
ans1=quicksort(z)
print(ans1)

```

### Implémentation en MATLAB

```
a = [9,4,7,3,8,5,1,6,2];

sorted = quicksort(a,1,length(a));

function [unsorted] =  quicksort(unsorted, low, high)
    if low < high
        [pInd, unsorted] = partition(unsorted, low, high);
        unsorted = quicksort(unsorted, low, pInd-1);
        unsorted = quicksort(unsorted, pInd+1, high);
    end

end

function [pInd, unsorted] = partition(unsorted, low, high)
    i = low-1;
    for j = low:1:high-1
        if unsorted(j) <= unsorted(high)
            i = i+1;
            unsorted([i,j]) = unsorted([j,i]);
            
        end
    end
    unsorted([i+1,high]) = unsorted([high,i+1]);
    pInd = i+1;

end

```

La complexité spatiale du tri rapide est `O(n)`. Il s'agit d'une amélioration par rapport aux autres algorithmes de tri diviser pour régner, qui prennent `O(nlong(n))` d'espace.

Le tri rapide atteint cela en changeant l'ordre des éléments dans le tableau donné. Comparez cela avec l'algorithme de [tri fusion](https://guide.freecodecamp.org/algorithms/sorting-algorithms/merge-sort) qui crée 2 tableaux, chacun de longueur `n/2`, à chaque appel de fonction.

Cependant, il existe le problème que cet algorithme de tri peut être de temps `O(n*n)` si le pivot est toujours gardé au milieu. Cela peut être surmonté en utilisant un pivot aléatoire.

### Complexité

Meilleur, moyen, pire, mémoire : n log(n)n log(n)n 2log(n). Ce n'est pas un algorithme stable, et le tri rapide est généralement fait en place avec O(log(n)) d'espace de pile.

La complexité spatiale du tri rapide est O(n). Il s'agit d'une amélioration par rapport aux autres algorithmes de tri diviser pour régner, qui prennent O(n log(n)) d'espace.

## Timsort

Timsort est un algorithme de tri rapide fonctionnant à une complexité stable de O(N log(N)).

Timsort est un mélange de tri par insertion et de tri fusion. Cet algorithme est implémenté dans Arrays.sort() de Java ainsi que dans sorted() et sort() de Python. Les petites parties sont triées en utilisant le tri par insertion et sont ensuite fusionnées ensemble en utilisant le tri fusion.

Une implémentation rapide en Python :

```py
def binary_search(the_array, item, start, end):
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = round((start + end)/ 2)

    if the_array[mid] < item:
        return binary_search(the_array, item, mid + 1, end)

    elif the_array[mid] > item:
        return binary_search(the_array, item, start, mid - 1)

    else:
        return mid

"""
Insertion sort that timsort uses if the array size is small or if
the size of the "run" is small
"""
def insertion_sort(the_array):
    l = len(the_array)
    for index in range(1, l):
        value = the_array[index]
        pos = binary_search(the_array, value, 0, index - 1)
        the_array = the_array[:pos] + [value] + the_array[pos:index] + the_array[index+1:]
    return the_array

def merge(left, right):
    """Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.
    [1, 2, 3, 4, 5, 6]
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def timsort(the_array):
    runs, sorted_runs = [], []
    length = len(the_array)
    new_run = [the_array[0]]

    # for every i in the range of 1 to length of array
    for i in range(1, length):
        # if i is at the end of the list
        if i == length - 1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        # if the i'th element of the array is less than the one before it
        if the_array[i] < the_array[i-1]:
            # if new_run is set to None (NULL)
            if not new_run:
                runs.append([the_array[i]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = []
        # else if its equal to or more than
        else:
            new_run.append(the_array[i])

    # for every item in runs, append it using insertion sort
    for item in runs:
        sorted_runs.append(insertion_sort(item))
    
    # for every run in sorted_runs, merge them
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    print(sorted_array)

timsort([2, 3, 1, 5, 6, 7])

```

### Complexité :

Tim sort a une complexité stable de O(N log(N)) et se compare très bien avec Quicksort. Une comparaison des complexités peut être trouvée sur ce [graphique](https://cdn-images-1.medium.com/max/1600/1*1CkG3c4mZGswDShAV9eHbQ.png).

## Tri fusion

Le tri fusion est un algorithme de type [Diviser pour régner](https://guide.freecodecamp.org/algorithms/divide-and-conquer-algorithms). Il divise le tableau d'entrée en deux moitiés, s'appelle lui-même pour les deux moitiés et fusionne ensuite les deux moitiés triées. La majeure partie de l'algorithme consiste à prendre deux tableaux triés et à les fusionner en un seul tableau trié. Le processus entier de tri d'un tableau de N entiers peut être résumé en trois étapes :

* Diviser le tableau en deux moitiés.
* Trier la moitié gauche et la moitié droite en utilisant le même algorithme récursif.
* Fusionner les moitiés triées.

Il existe quelque chose appelé l'[algorithme des deux doigts](https://en.wikipedia.org/wiki/Cheney%27s_algorithm) qui nous aide à fusionner deux tableaux triés ensemble. En utilisant cette sous-routine et en appelant la fonction de tri fusion sur les moitiés du tableau de manière récursive, nous obtiendrons le tableau trié final que nous recherchons.

Puisque cela est un algorithme basé sur la récursion, nous avons une relation de récurrence pour celui-ci. Une relation de récurrence est simplement une manière de représenter un problème en termes de ses sous-problèmes.

`T(n) = 2 * T(n / 2) + O(n)`

En termes simples, nous décomposons le sous-problème en deux parties à chaque étape et nous avons une certaine quantité de travail linéaire que nous devons effectuer pour fusionner les deux moitiés triées à chaque étape.

### Complexité

Le plus grand avantage d'utiliser le tri fusion est que la [complexité temporelle](https://www.youtube.com/watch?v=V42FBiohc6c&list=PL2_aWCzGMAwI9HK8YPVBjElbLbI3ufctn) est seulement n*log(n) pour trier un tableau entier. C'est beaucoup mieux que le temps d'exécution n^2 du tri à bulles ou du tri par insertion.

Avant d'écrire du code, comprenons comment fonctionne le tri fusion à l'aide d'un diagramme.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/4712ef1a5d856dbb4af393fcc08a820a38787395.png)

* Initialement, nous avons un tableau de 6 entiers non triés Arr(5, 8, 3, 9, 1, 2)
* Nous divisons le tableau en deux moitiés Arr1 = (5, 8, 3) et Arr2 = (9, 1, 2).
* Encore une fois, nous les divisons en deux moitiés : Arr3 = (5, 8) et Arr4 = (3) et Arr5 = (9, 1) et Arr6 = (2)
* Encore une fois, nous les divisons en deux moitiés : Arr7 = (5), Arr8 = (8), Arr9 = (9), Arr10 = (1) et Arr6 = (2)
* Nous allons maintenant comparer les éléments dans ces sous-tableaux afin de les fusionner.

### Propriétés :

* Complexité spatiale : O(n)
* Complexité temporelle : O(n*log(n)). La complexité temporelle pour le tri fusion peut ne pas être évidente au premier abord. Le facteur log(n) qui intervient est dû à la relation de récurrence que nous avons mentionnée précédemment.
* Tri en place : Non dans une implémentation typique
* Stable : Oui
* Parallelisable : oui (Plusieurs variantes parallèles sont discutées dans la troisième édition de Cormen, Leiserson, Rivest, et Stein's Introduction to Algorithms.)

### **Implémentation en C++**

```cpp
void merge(int array[], int left, int mid, int right)
{
    int i, j, k;

    // Taille de la sous-liste de gauche
int size_left = mid - left + 1;

// Taille de la sous-liste de droite
int size_right =  right - mid;

/* créer des tableaux temporaires */
int Left[size_left], Right[size_right];

/* Copier les données dans les tableaux temporaires L[] et R[] */
for(i = 0; i < size_left; i++)
{
    Left[i] = array[left+i];
}

for(j = 0; j < size_right; j++)
{
    Right[j] = array[mid+1+j];
}

// Fusionner les tableaux temporaires dans arr[left..right]
i = 0; // Index initial du sous-tableau de gauche
j = 0; // Index initial du sous-tableau de droite
k = left; // Index initial du sous-tableau fusionné

while (i < size_left && j < size_right)
{
    if (Left[i] <= Right[j])
    {
        array[k] = Left[i];
        i++;
    }
    else
    {
        array[k] = Right[j];
        j++;
    }
    k++;
}

// Copier les éléments restants de Left[]
while (i < size_left)
{
    array[k] = Left[i];
    i++;
    k++;
}

// Copier les éléments restants de R[]
while (j < size_right)
{
    array[k] = Right[j];
    j++;
    k++;
}
}

void mergeSort(int array[], int left, int right)
{
    if(left < right)
    {
        int mid = (left+right)/2;

        // Trier les moitiés gauche et droite
    mergeSort(array, left, mid);
    mergeSort(array, mid+1, right);

    // Enfin, les fusionner
    merge(array, left, mid, right);
}
}
```

### **Implémentation en JavaScript**

```js
function mergeSort (arr) {
  if (arr.length < 2) return arr;
  var mid = Math.floor(arr.length /2);
  var subLeft = mergeSort(arr.slice(0,mid));
  var subRight = mergeSort(arr.slice(mid));
  return merge(subLeft, subRight);
}
```

Tout d'abord, nous vérifions la longueur du tableau. Si elle est de 1, nous retournons simplement le tableau. Ce serait notre cas de base. Sinon, nous allons trouver la valeur médiane et diviser le tableau en deux moitiés. Nous allons maintenant trier les deux moitiés avec des appels récursifs à la fonction MergeSort.

```js
function merge (a,b) {
    var result = [];
    while (a.length >0 && b.length >0)
        result.push(a[0] < b[0]? a.shift() : b.shift());
    return result.concat(a.length? a : b);
}
```

Lorsque nous fusionnons les deux moitiés, nous stockons le résultat dans un tableau auxiliaire. Nous allons comparer l'élément de départ du tableau de gauche à l'élément de départ du tableau de droite. Celui qui est le plus petit sera poussé dans le tableau des résultats et nous le supprimerons de leurs tableaux respectifs en utilisant l'opérateur [shift(). Si nous finissons toujours avec des valeurs dans le tableau de gauche ou de droite, nous les concaténerons simplement à la fin du résultat. Voici le résultat trié :

```js
var test = [5,6,7,3,1,3,15];
console.log(mergeSort(test));

>> [1, 3, 3, 5, 6, 7, 15]
```

### Un tutoriel YouTube sur le tri fusion

Voici une bonne vidéo YouTube qui [parcourt le sujet en détail](https://www.youtube.com/watch?v=TzeBrDU-JaY).

### Implémentation en JS

```js
const list = [23, 4, 42, 15, 16, 8, 3]

const mergeSort = (list) =>{
  if(list.length <= 1) return list;
  const middle = list.length / 2 ;
  const left = list.slice(0, middle);
  const right = list.slice(middle, list.length);
  return merge(mergeSort(left), mergeSort(right));
}

const merge = (left, right) => {
  var result = [];
  while(left.length || right.length) {
    if(left.length && right.length) {
      if(left[0] < right[0]) {
        result.push(left.shift())
      } else {
        result.push(right.shift())
      }
    } else if(left.length) {
        result.push(left.shift())
      } else {
        result.push(right.shift())
      }
    }
  return result;
}

console.log(mergeSort(list)) // [ 3, 4, 8, 15, 16, 23, 42 ]

```

### Implémentation en C

```c
#include<stdlib.h> 
#include<stdio.h>
void merge(int arr[], int l, int m, int r) 
{ 
    int i, j, k; 
    int n1 = m - l + 1; 
    int n2 =  r - m; 
  
    
    int L[n1], R[n2]; 
  
    for (i = 0; i < n1; i++) 
        L[i] = arr[l + i]; 
    for (j = 0; j < n2; j++) 
        R[j] = arr[m + 1+ j];
    i = 0; 
    j = 0; 
    k = l; 
    while (i < n1 && j < n2) 
    { 
        if (L[i] <= R[j]) 
        { 
            arr[k] = L[i]; 
            i++; 
        } 
        else
        { 
            arr[k] = R[j]; 
            j++; 
        } 
        k++; 
    } 
  
    
    while (i < n1) 
    { 
        arr[k] = L[i]; 
        i++; 
        k++; 
    } 
  
    while (j < n2) 
    { 
        arr[k] = R[j]; 
        j++; 
        k++; 
    } 
} 
  
void mergeSort(int arr[], int l, int r) 
{ 
    if (l < r) 
    {  
        int m = l+(r-l)/2; 
  
        
        mergeSort(arr, l, m); 
        mergeSort(arr, m+1, r); 
  
        merge(arr, l, m, r); 
    } 
}
void printArray(int A[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", A[i]); 
    printf("\n"); 
} 
int main() 
{ 
    int arr[] = {12, 11, 13, 5, 6, 7}; 
    int arr_size = sizeof(arr)/sizeof(arr[0]); 
  
    printf("Given array is \n"); 
    printArray(arr, arr_size); 
  
    mergeSort(arr, 0, arr_size - 1); 
  
    printf("\nSorted array is \n"); 
    printArray(arr, arr_size); 
    return 0; 

```

### Implémentation en C++

Considérons le tableau A = {2,5,7,8,9,12,13} et le tableau B = {3,5,6,9,15} et nous voulons que le tableau C soit également en ordre croissant.

```cpp
void mergesort(int A[],int size_a,int B[],int size_b,int C[])
{
     int token_a,token_b,token_c;
     for(token_a=0, token_b=0, token_c=0; token_a<size_a && token_b<size_b; )
     {
          if(A[token_a]<=B[token_b])
               C[token_c++]=A[token_a++];
          else
               C[token_c++]=B[token_b++];
      }
      
      if(token_a<size_a)
      {
          while(token_a<size_a)
               C[token_c++]=A[token_a++];
      }
      else
      {
          while(token_b<size_b)
               C[token_c++]=B[token_b++];
      }

}

```

### Implémentation en Python

```py
def merge(left,right,compare):
	result = [] 
	i,j = 0,0
	while (i < len(left) and j < len(right)):
		if compare(left[i],right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while (i < len(left)):
		result.append(left[i])
		i += 1
	while (j < len(right)):
		result.append(right[j])
		j += 1
	return result

def merge_sort(arr, compare = lambda x, y: x < y):
     #Used lambda function to sort array in both(increasing and decresing) order.
     #By default it sorts array in increasing order
	if len(arr) < 2:
		return arr[:]
	else:
		middle = len(arr) // 2
		left = merge_sort(arr[:middle], compare)
		right = merge_sort(arr[middle:], compare)
		return merge(left, right, compare) 

arr = [2,1,4,5,3]
print(merge_sort(arr))

```

### Implémentation en Java

```java
public class mergesort {

	public static int[] mergesort(int[] arr,int lo,int hi) {
		
		if(lo==hi) {
			int[] ba=new int[1];
			ba[0]=arr[lo];
			return ba;
		}
		
		int mid=(lo+hi)/2;
		int arr1[]=mergesort(arr,lo,mid);
		int arr2[]=mergesort(arr,mid+1,hi);
		return merge(arr1,arr2);
	}
	
	public static int[] merge(int[] arr1,int[] arr2) {
		int i=0,j=0,k=0;
		int n=arr1.length;
		int m=arr2.length;
		int[] arr3=new int[m+n];
		while(i<n && j<m) {
			if(arr1[i]<arr2[j]) {
				arr3[k]=arr1[i];
				i++;
			}
			else {
				arr3[k]=arr2[j];
				j++;
			}
			k++;
		}
		
		while(i<n) {
			arr3[k]=arr1[i];
			i++;
			k++;
		}
		
		while(j<m) {
			arr3[k]=arr2[j];
			j++;
			k++;
		}
		
		return arr3;
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[]= {2,9,8,3,6,4,10,7};
		int[] so=mergesort(arr,0,arr.length-1);
		for(int i=0;i<arr.length;i++)
			System.out.print(so[i]+" ");
	}

}

```

### Exemple en Java

```java
public class mergesort {
  public static int[] mergesort(int[] arr, int lo, int hi) {
    if (lo == hi) {
      int[] ba = new int[1];
      ba[0] = arr[lo];
      return ba;
    }
    int mid = (lo + hi) / 2;
    int arr1[] = mergesort(arr, lo, mid);
    int arr2[] = mergesort(arr, mid + 1, hi);
    return merge(arr1, arr2);
  }

  public static int[] merge(int[] arr1, int[] arr2) {
    int i = 0, j = 0, k = 0;
    int n = arr1.length;
    int m = arr2.length;
    int[] arr3 = new int[m + n];
    while (i < n && j < m) {
      if (arr1[i] < arr2[j]) {
        arr3[k] = arr1[i];
        i++;
      } else {
        arr3[k] = arr2[j];
        j++;
      }
      k++;
    }
    while (i < n) {
      arr3[k] = arr1[i];
      i++;
      k++;
    }
    while (j < m) {
      arr3[k] = arr2[j];
      j++;
      k++;
    }
    return arr3;
  }

  public static void main(String[] args) {
    int arr[] = {2, 9, 8, 3, 6, 4, 10, 7};
    int[] so = mergesort(arr, 0, arr.length - 1);
    for (int i = 0; i < arr.length; i++)
      System.out.print(so[i] + " ");
  }
}

```
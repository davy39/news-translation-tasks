---
title: Tri à bulles – Algorithme en Java, C++, Python avec des exemples de code
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-29T17:34:36.000Z'
originalURL: https://freecodecamp.org/news/bubble-sort-algorithm-in-java-cpp-python-with-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/bubbleSortCover.png
tags:
- name: C++
  slug: c-2
- name: algorithms
  slug: algorithms
- name: Java
  slug: java
- name: Python
  slug: python
seo_title: Tri à bulles – Algorithme en Java, C++, Python avec des exemples de code
seo_desc: 'Bubble sort is a type of sorting algorithm you can use to arrange a set
  of values in ascending order. If you want, you can also implement bubble sort to
  sort the values in descending order.

  A real-world example of a bubble sort algorithm is how the c...'
---

Le tri à bulles (bubble sort) est un type d'algorithme de tri que vous pouvez utiliser pour organiser un ensemble de valeurs par ordre croissant. Si vous le souhaitez, vous pouvez également implémenter le tri à bulles pour trier les valeurs par ordre décroissant.

Un exemple concret d'algorithme de tri à bulles est la façon dont la liste de contacts de votre téléphone est triée par ordre alphabétique. Ou encore le tri des fichiers sur votre téléphone selon l'heure à laquelle ils ont été ajoutés.

Dans cet article, j'expliquerai tout ce que vous devez savoir sur l'algorithme de tri à bulles avec quelques infographies que j'ai préparées. Je vous montrerai ensuite des exemples de code de l'algorithme de tri à bulles en Python, Java et C++.

## Table des matières
- [Comment fonctionne l'algorithme de tri à bulles](#heading-comment-fonctionne-lalgorithme-de-tri-a-bulles)
  - [Première itération du tri](#heading-premiere-iteration-du-tri)
  - [Deuxième itération du tri et le reste](#heading-deuxieme-iteration-du-tri-et-le-reste)
- [Exemple de code Python de l'algorithme de tri à bulles](#heading-exemple-de-code-python-de-lalgorithme-de-tri-a-bulles)
- [Exemple de code Java de l'algorithme de tri à bulles](#heading-exemple-de-code-java-de-lalgorithme-de-tri-a-bulles)
- [Exemple de code C++ de l'algorithme de tri à bulles](#heading-exemple-de-code-c-de-lalgorithme-de-tri-a-bulles)
- [Dernières réflexions](#heading-dernieres-reflexions)

## Comment fonctionne l'algorithme de tri à bulles

Pour implémenter un algorithme de tri à bulles, les développeurs écrivent souvent une fonction, puis une boucle à l'intérieur d'une boucle – une boucle interne et une boucle externe. Vous le verrez en action lorsque je vous montrerai le code en Python, C++ et Java.

Disons que nous voulons trier une série de nombres 5, 3, 4, 1 et 2 afin qu'ils soient disposés par ordre croissant…

Le tri commence la première itération en comparant les deux premières valeurs. Si la première valeur est supérieure à la seconde, l'algorithme déplace la première valeur à l'index de la seconde valeur.

### Première itération du tri
**Étape 1** : Dans le cas de 5, 3, 4, 1 et 2, 5 est plus grand que 3. Donc 5 prend la position de 3 et les nombres deviennent 3, 5, 4, 1 et 2.

![bubble1](https://www.freecodecamp.org/news/content/images/2022/09/bubble1.png) 

**Étape 2** : L'algorithme a maintenant 3, 5, 4, 1 et 2 à comparer. Cette fois-ci, il compare les deux valeurs suivantes, qui sont 5 et 4. 5 est plus grand que 4, donc 5 prend l'index de 4 et les valeurs deviennent maintenant 3, 4, 5, 1 et 2.

![bubble2](https://www.freecodecamp.org/news/content/images/2022/09/bubble2.png) 

**Étape 3** : L'algorithme a maintenant 3, 4, 5, 1 et 2 à comparer. Il compare les deux valeurs suivantes, qui sont 5 et 1. 5 est plus grand que 1, donc 5 prend l'index de 1 et les nombres deviennent 3, 4, 1, 5 et 2.

![bubble3](https://www.freecodecamp.org/news/content/images/2022/09/bubble3.png) 

**Étape 4** : L'algorithme a maintenant 3, 4, 1, 5 et 2 à comparer. Il compare les deux valeurs suivantes, qui sont 5 et 2. 5 est plus grand que 2, donc 5 prend l'index de 2 et les nombres deviennent 3, 4, 1, 2 et 5.

![bubble4](https://www.freecodecamp.org/news/content/images/2022/09/bubble4.png) 

C'est la première itération. Et les nombres sont maintenant disposés comme suit : 3, 4, 1, 2 et 5 – à partir des nombres initiaux 5, 3, 4, 1 et 2. Comme vous pouvez le constater, 5 devrait être le dernier nombre si les nombres sont triés par ordre croissant. Cela signifie que la première itération est réellement terminée.    

### Deuxième itération du tri et le reste
L'algorithme commence la deuxième itération avec le dernier résultat de 3, 4, 1, 2 et 5. Cette fois-ci, 3 est plus petit que 4, donc aucun échange n'a lieu. Cela signifie que les nombres resteront les mêmes.

![bubbleb1](https://www.freecodecamp.org/news/content/images/2022/09/bubbleb1.png) 

L'algorithme procède à la comparaison de 4 et 1. 4 est plus grand que 1, donc 4 est échangé avec 1 et les nombres deviennent 3, 1, 4, 2 et 5.

![bubbleb2](https://www.freecodecamp.org/news/content/images/2022/09/bubbleb2.png) 

L'algorithme procède maintenant à la comparaison de 4 et 2. 4 est plus grand que 2, donc 4 est échangé avec 2 et les nombres deviennent 3, 1, 2, 4 et 5. 

![bubbleb4](https://www.freecodecamp.org/news/content/images/2022/09/bubbleb4.png) 

4 est maintenant à la bonne place, donc aucun échange ne se produit entre 4 et 5 car 4 est plus petit que 5. 

![bubbleb5](https://www.freecodecamp.org/news/content/images/2022/09/bubbleb5.png) 

C'est ainsi que l'algorithme continue de comparer les nombres jusqu'à ce qu'ils soient disposés par ordre croissant : 1, 2, 3, 4 et 5.

![bubblebFinal](https://www.freecodecamp.org/news/content/images/2022/09/bubblebFinal.png) 

## Exemple de code Python de l'algorithme de tri à bulles
Voici un exemple de code montrant l'implémentation de l'algorithme de tri à bulles en Python :

```py
def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        flag = 0
        for j in range(0, arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                if flag == 0:
                    break
    return arr

arr = [5, 3, 4, 1, 2]
print("Liste triée avec le tri à bulles par ordre croissant : ", bubble_sort(arr))

# Sortie : Liste triée avec le tri à bulles par ordre croissant :  [1, 2, 3, 4, 5]
```

Pour que le tri apparaisse par ordre décroissant, remplacez simplement le symbole supérieur à (>) par le symbole inférieur à (<) :

```py
def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        flag = 0
        for j in range(0, arr_len-i-1):
            if arr[j] < arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                if flag == 0:
                    break
    return arr

arr = [5, 3, 4, 1, 2]
print("Liste triée avec le tri à bulles par ordre décroissant : ", bubble_sort(arr))

# Sortie : Liste triée avec le tri à bulles par ordre décroissant :  [5, 4, 3, 2, 1]
```

Voici une version du code où j'ai ajouté des commentaires pour que vous puissiez comprendre ce qui se passe :

```py
# Définir une fonction pour créer le tri et passer un tableau en paramètre
def bubble_sort(arr):
    # Obtenir la longueur du tableau
    arr_len = len(arr)
    # Parcourir le tableau pour accéder aux éléments, y compris le dernier - boucle externe
    for i in range(arr_len-1):
        # déclarer une variable flag pour vérifier si un échange a eu lieu - pour l'optimisation
        flag = 0
        # créer une boucle pour comparer chaque élément du tableau jusqu'au dernier
        for j in range(0, arr_len-i-1):
            # comparer 2 éléments adjacents et les trier par ordre croissant
            if arr[j] > arr[j+1]:
                # Échanger les éléments s'ils ne sont pas dans le bon ordre
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                # sortir de la boucle à 0
                if flag == 0:
                    break
    # la valeur de retour doit être dans le bloc de la boucle externe
    return arr

arr = [5, 3, 4, 1, 2]
print("Liste triée avec le tri à bulles par ordre croissant : ", bubble_sort(arr))

# Sortie : Liste triée avec le tri à bulles par ordre croissant :  [1, 2, 3, 4, 5]
```

## Exemple de code Java de l'algorithme de tri à bulles
Pour implémenter l'algorithme de tri à bulles en Java, vous devez écrire plus de code qu'en Python.

C'est pourquoi j'ai ajouté des commentaires pour vous informer des étapes au fur et à mesure de leur exécution :

```js
import java.util.Arrays;

class Main {
  static void bubbleSort(int array[]) {
    int size = array.length;
    // parcourir chaque élément du tableau pour y accéder
    for (int i = 0; i < size - 1; i++)
      // comparer les éléments du tableau avec une boucle
      for (int j = 0; j < size - i - 1; j++)
        // comparer deux éléments adjacents dans le tableau
        if (array[j] > array[j + 1]) {
          // Échanger si les éléments ne sont pas dans le bon ordre
          int temp = array[j];
          array[j] = array[j + 1];
          array[j + 1] = temp;
        }
  }

  public static void main(String args[]) {
    int[] data = { 5, 3, 4, 1, 2 };
    // appeler la méthode en utilisant le nom de la classe
    Main.bubbleSort(data);
    
    System.out.println("Tableau trié avec le tri à bulles : ");
    System.out.println(Arrays.toString(data));
  }
}

// Sortie : Tableau trié avec le tri à bulles : [1, 2, 3, 4, 5]
```


## Exemple de code C++ de l'algorithme de tri à bulles
Comme je l'ai fait pour Java, j'ai également ajouté des commentaires à l'implémentation de l'algorithme de tri à bulles en C++ car il est plus verbeux que celui de Python et Java :

```cpp
#include <iostream>

using namespace std;

// créer une fonction pour exécuter le tri à bulles
void bubble_sort(int array[], int size) {
  // parcourir chaque élément du tableau pour y accéder - boucle externe
  for (int step = 0; step < (size-1); ++step) {
    // vérifier si un échange a lieu
    int swapped = 0;
    // parcourir chaque élément du tableau pour les comparer - boucle interne
    for (int i = 0; i < (size-step-1); ++i) {
     // comparer 2 éléments adjacents et les trier par ordre croissant
      if (array[i] > array[i + 1]) {

        // Échanger les éléments s'ils ne sont pas dans le bon ordre
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
        
        swapped = 1;
      }
    }

    // sortir de la boucle si plus aucun échange n'a lieu
    if (swapped == 0)
      break;
  }
}

// afficher un tableau
void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    cout << "  " << array[i];
  }
  cout << "\n";
}

int main() {
  int data[] = {5, 3, 4, 1, 2};
  // trouver la longueur du tableau
  int size = sizeof(data) / sizeof(data[0]);

  // appeler la fonction   
  bubble_sort(data, size);
  
  cout << "Tableau trié avec le tri à bulles : \n";
  printArray(data, size);
}

// Sortie : Tableau trié avec le tri à bulles : 1  2  3  4  5
```

## Dernières réflexions
Je ne dirais pas que l'implémentation de l'algorithme de tri à bulles est simple ou difficile. Pour un programmeur expérimenté, ce n'est pas difficile, mais pour un débutant, cela pourrait être intimidant au début.

Cependant, pour vraiment comprendre comment l'algorithme fonctionne, vous devez savoir que :

- vous devez écrire une fonction pour y passer les données [ou le tableau]
- vous devez écrire une boucle externe pour accéder aux éléments
- vous devez écrire une boucle interne pour comparer les éléments  
- vous devez appeler la fonction et passer les données (tableau)

J'espère que cet article vous aidera à comprendre l'algorithme de tri à bulles et comment l'implémenter.

Merci de votre lecture.
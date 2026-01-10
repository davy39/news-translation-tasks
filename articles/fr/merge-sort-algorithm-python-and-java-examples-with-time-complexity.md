---
title: Algorithme de Tri Fusion – Exemples en Python et Java avec Complexité Temporelle
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-08T18:55:36.000Z'
originalURL: https://freecodecamp.org/news/merge-sort-algorithm-python-and-java-examples-with-time-complexity
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/merge-sort-main-1.png
tags:
- name: algorithms
  slug: algorithms
- name: Java
  slug: java
- name: Python
  slug: python
seo_title: Algorithme de Tri Fusion – Exemples en Python et Java avec Complexité Temporelle
seo_desc: 'In this article, we we talk about the merge sort algorithm. We will see
  some visual examples to help understand the algorithm and then implement it using
  Java and Python code.

  What Is a Merge Sort Algorithm?

  A merge sort algorithm is an efficient sor...'
---

Dans cet article, nous allons parler de l'algorithme de tri fusion. Nous verrons quelques exemples visuels pour aider à comprendre l'algorithme, puis nous l'implémenterons en utilisant du code Java et Python.

## Qu'est-ce qu'un Algorithme de Tri Fusion ?

Un algorithme de tri fusion est un algorithme de tri efficace basé sur l'algorithme **diviser pour régner**. Il divise une collection (tableau) d'éléments en unités simples, puis les fusionne de manière ordonnée.

Regardons un exemple pour comprendre comment fonctionne le tri fusion.

Nous allons utiliser l'algorithme de tri fusion pour trier ce tableau de nombres : 4, 10, 6, 14, 2, 1, 8, 5

Voici une image pour vous montrer le processus de "division" :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/merge-sort-divide.png)

Le tableau a d'abord été divisé en deux tableaux séparés. Ensuite, ces tableaux ont également été divisés. Cette division s'est poursuivie jusqu'à ce que tous les éléments du tableau deviennent une unité simple.

Après cette étape, la fusion commence. Voici comment cela se passe :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/merge-sort-merge.png)

Les éléments sont regroupés dans des tableaux, mais cette fois dans un ordre trié. De la même manière qu'ils ont été divisés, ils sont fusionnés.

Avant d'implémenter cet algorithme en code, vous devez comprendre comment nous sommes capables de collecter ces éléments dans un ordre trié.

Nous allons utiliser la section où nous avons regroupé les éléments en deux tableaux séparés – 4, 6, 10, 14 et 1, 2, 5, 8. Voici une illustration pour comprendre comment nous sommes arrivés au tableau final :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/merge-sort-arrows.png)

Comme on peut le voir ci-dessus, nous avons deux flèches pointant vers le premier index des deux tableaux. Une comparaison sera faite pour déterminer quel index est le plus petit. Dans notre cas, 1 est plus petit que 4, donc il sera poussé dans le tableau fusionné. Ensuite, la flèche rouge se déplacera vers l'index suivant. C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/merge-sort-arrows2.png)

Une autre comparaison sera faite : est-ce que 2 < 4 ?

2 est inférieur à 4, donc il sera poussé dans le tableau fusionné et la flèche se déplace vers l'index suivant.

Pour la comparaison suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/merge-sort-arrows3.png)

4 est inférieur à 5, donc 4 sera poussé dans le tableau fusionné et la flèche cyan se déplacera vers l'index suivant.

Cette comparaison se poursuivra jusqu'à ce que le tableau fusionné soit rempli. Si cela arrive à un point où un tableau devient vide, le tableau avec les éléments restants sera copié dans le tableau fusionné dans un ordre trié.

Regardons quelques exemples de code !

## **Exemple de Tri Fusion en Java**

Si nous voulons implémenter le tri fusion avec Java, voici à quoi cela ressemblerait :

```java
public class MergeSort {
  public static void main(String[] args) {

    int[] numbers = {4, 10, 6, 14, 2, 1, 8, 5};

    mergeSort(numbers); 

    System.out.println("Tableau trié :");
    for (int i = 0; i < numbers.length; i++) {
      System.out.println(numbers[i]);
    }
  }


  private static void mergeSort(int[] inputArray) {
    int arrayLength = inputArray.length;
    
    if (arrayLength < 2) {
      return;
    }
    
    int midPoint = arrayLength / 2;
    int[] leftArray = new int[midPoint];
    int[] rightArray = new int[arrayLength - midPoint];
    
    for (int i = 0; i < midPoint; i++) {
      leftArray[i] = inputArray[i];
    }
    for (int i = midPoint; i < arrayLength; i++) {
      rightArray[i - midPoint] = inputArray[i];
    }
    
    mergeSort(leftArray);
    mergeSort(rightArray);
    
    merge(inputArray, leftArray, rightArray);
  }

  private static void merge (int[] inputArray, int[] leftArray, int[] rightArray) {
    int leftArrayLength = leftArray.length;
    int rightArrayLength = rightArray.length;
    
    int x = 0;
    int y = 0;
    int z = 0;
    
    while (x < leftArrayLength && y < rightArrayLength) {
      if (leftArray[x] <= rightArray[y]) {
        inputArray[z] = leftArray[x];
        x++;
      }
      else {
        inputArray[z] = rightArray[y];
        y++;
      }
      z++;
    }
    
    while (x < leftArrayLength) {
      inputArray[z] = leftArray[x];
      x++;
      z++;
    }
    
    while (y < rightArrayLength) {
      inputArray[z] = rightArray[y];
      y++;
      z++;
    }
    
  }
}

```

Décomposons le code.

```java
public static void main(String[] args) {

    int[] numbers = {4, 10, 6, 14, 2, 1, 8, 5};
    // 1, 2, 4, 5, 6, 8, 10, 14

    mergeSort(numbers); 

    System.out.println("Tableau trié :");
    for (int i = 0; i < numbers.length; i++) {
      System.out.println(numbers[i]);
    }
  }
```

Ci-dessus, nous avons créé notre tableau de nombres. Après cela, nous avons appelé la méthode `mergeSort` pour trier les nombres. Ensuite, nous avons parcouru le tableau de nombres triés et les avons imprimés sur la console.

```java
private static void mergeSort(int[] inputArray) {
    int arrayLength = inputArray.length;
    
    if (arrayLength < 2) {
      return;
    }
    
    int midPoint = arrayLength / 2;
    int[] leftArray = new int[midPoint];
    int[] rightArray = new int[arrayLength - midPoint];
    
    for (int i = 0; i < midPoint; i++) {
      leftArray[i] = inputArray[i];
    }
    for (int i = midPoint; i < arrayLength; i++) {
      rightArray[i - midPoint] = inputArray[i];
    }
    
    mergeSort(leftArray);
    mergeSort(rightArray);
    
    merge(inputArray, leftArray, rightArray);
  }
```

Nous avons obtenu le point médian du tableau en divisant la longueur du tableau par deux. Le tableau de gauche commence à partir du premier index jusqu'au point médian, tandis que le tableau de droite commence à partir de l'index après le point médian jusqu'à la fin du tableau.

Nous avons ensuite créé deux boucles pour copier les éléments dans les tableaux de gauche et de droite en fonction de la position des éléments. Nous avons ensuite appelé la méthode `mergeSort` sur les tableaux de gauche et de droite. Cela continuera à diviser le tableau de manière récursive jusqu'à ce que les tableaux aient été réduits à des unités simples (comme nous l'avons vu dans les images de la dernière section).

Enfin, nous avons appelé la méthode `merge` pour fusionner les tableaux en un seul tableau dans un ordre trié. Regardons la logique utilisée dans la méthode `merge`.

```java
private static void merge (int[] inputArray, int[] leftArray, int[] rightArray) {
    int leftArrayLength = leftArray.length;
    int rightArrayLength = rightArray.length;
    
    int x = 0;
    int y = 0;
    int z = 0;
    
    while (x < leftArrayLength && y < rightArrayLength) {
      if (leftArray[x] <= rightArray[y]) {
        inputArray[z] = leftArray[x];
        x++;
      }
      else {
        inputArray[z] = rightArray[y];
        y++;
      }
      z++;
    }
    
    while (x < leftArrayLength) {
      inputArray[z] = leftArray[x];
      x++;
      z++;
    }
    
    while (y < rightArrayLength) {
      inputArray[z] = rightArray[y];
      y++;
      z++;
    }
    
  }

```

Vous vous souvenez des flèches des images de la dernière section ? Nous les avons désignées ici en utilisant `x` et `y`, puis `z` pour le tableau fusionné où les nombres seront poussés dans un ordre trié.

Les boucles while ont été utilisées pour faire la comparaison sur les deux tableaux et changer la position de `x`, `y` et `z` à mesure que les éléments étaient poussés dans le tableau fusionné.

## **Exemple de Tri Fusion en Python**

```python

def mergeSort(array):
    if len(array) > 1:

        midPoint = len(array)//2
        leftArray = array[:midPoint]
        rightArray = array[midPoint:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        x = 0
        y = 0
        z = 0

        while x < len(leftArray) and y < len(rightArray):
            if leftArray[x] < rightArray[y]:
                array[z] = leftArray[x]
                x += 1
            else:
                array[z] = rightArray[y]
                y += 1
            z += 1

        
        while x < len(leftArray):
            array[z] = leftArray[x]
            x += 1
            z += 1

        while y < len(rightArray):
            array[z] = rightArray[y]
            y += 1
            z += 1


def printSortedArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]

    mergeSort(numbers)

    print("Tableau trié :")
    printSortedArray(numbers)
```

La logique ici est exactement la même que dans la dernière section. Ci-dessus, nous avons implémenté l'algorithme de tri fusion en utilisant Python. Vous pouvez trouver une explication de comment le code fonctionne dans la dernière section.

La complexité temporelle du tri fusion est O(n*Log n) pour tous les cas (meilleur, moyen et pire).

## Conclusion

Dans cet article, nous avons appris comment fonctionne l'algorithme de tri fusion. Nous avons ensuite vu quelques exemples et comment l'appliquer dans notre code Java et Python.

Bon codage !
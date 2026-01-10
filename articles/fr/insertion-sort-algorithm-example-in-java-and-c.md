---
title: Tri par insertion – Exemple d'algorithme en Java et C++
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-28T23:44:34.000Z'
originalURL: https://freecodecamp.org/news/insertion-sort-algorithm-example-in-java-and-c
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/insertion-sort-algorithm.png
tags:
- name: algorithms
  slug: algorithms
- name: C++
  slug: c-2
- name: Java
  slug: java
seo_title: Tri par insertion – Exemple d'algorithme en Java et C++
seo_desc: "Insertion sort is a sorting algorithm that creates a sorted array of items\
  \ from an unsorted array, one item at a time. \nIn this article, we will see how\
  \ the algorithm works and how to apply it in our code.\nHow to Use Insertion Sort\n\
  Consider an array ..."
---

**Le tri par insertion** est un algorithme de tri qui crée un tableau trié d'éléments à partir d'un tableau non trié, un élément à la fois.

Dans cet article, nous verrons comment fonctionne l'algorithme et comment l'appliquer dans notre code.

## Comment utiliser le tri par insertion

Considérons un tableau de nombres : 7, 3, 10, 4, 1, 11. Ces nombres ne sont pas triés/organisés dans un ordre quelconque (croissant ou décroissant). Avec l'algorithme de tri par insertion, nous pouvons les trier du plus petit au plus grand nombre.

Le tableau original sera divisé en deux – le tableau trié et le tableau non trié. Nous allons ensuite prendre des nombres dans le tableau non trié et les placer au bon endroit.

Lorsque qu'un nombre est pris dans le tableau non trié, nous commençons le tri à partir de la partie arrière du tableau trié. Si le nombre pris est inférieur au dernier nombre du tableau trié, le dernier nombre sera déplacé vers la droite et le nombre sélectionné prendra sa position. L'itération continue jusqu'à ce que le nombre sélectionné atteigne une position où le nombre suivant à comparer n'est pas plus grand que lui.

Cela peut sembler beaucoup d'informations, mais vous comprendrez mieux avec un exemple :

Voici notre tableau de nombres : 7, 3, 10, 4, 1, 11

Nous allons diviser ce tableau en deux – le tableau trié et le tableau non trié. Comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/insertion-sort-sides.png)

Par défaut, nous plaçons le premier nombre dans la section triée car nous commencerons notre comparaison avec lui.

Alors, comment trions-nous ce tableau ?

Le premier nombre dans le tableau non trié est 3, donc il devient le nombre sélectionné. Lorsque nous déplaçons 3 vers le tableau trié, le nombre qui s'y trouve est 7. Puisque 7 est plus grand que 3, il sera déplacé vers la droite et ensuite 3 prendra sa position.

Le tableau ressemblera maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/insertion-sort-1.png)

Pour 10, nous commençons notre comparaison avec le tableau trié à partir de l'arrière et le premier nombre de l'arrière est 7. Puisque 7 est inférieur à 10, il n'y a pas besoin de décalage de position donc 10 resterait directement après 7.

Voici maintenant la position actuelle des nombres de chaque côté :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/insertion-sort-2.png)

Vous pourriez être un peu confus quant à la manière dont ces nombres changent de position lorsqu'ils se déplacent sur la zone triée. Démontrons cela avec l'exemple suivant.

Le nombre suivant à trier est 4.

Voici à quoi ressemble notre tableau trié à ce moment-là : 3, 7, 10.

Maintenant, le nombre actuel à trier est 4. Donc, en commençant à nouveau par l'arrière, nous comparons 4 et 10. 10 est plus grand que 4, donc il se déplace d'un espace vers la droite et crée un espace vide pour quatre. Quelque chose comme ceci : 3, 7, ?, 10.

Le point d'interrogation est l'espace créé. Mais nous ne pouvons pas insérer 4 tout de suite ; nous devons le comparer avec le nombre suivant qui est 7. Un autre espace sera créé car 7 est plus grand que 4 et notre tableau ressemblera à ceci : 3, ?, 7, 10.

Le nombre suivant est 3. Nous sommes arrivés au point où le nombre comparé est inférieur au nombre actuel que nous avons pris dans le tableau non trié. Puisque 3 est inférieur à 4, 4 sera inséré dans le dernier espace créé. Notre tableau trié ressemblera maintenant à ceci : 3, 4, 7, 10.

Pour 1, si vous avez compris le dernier exemple, alors cela devrait être facile à résoudre. Vous devriez essayer de trier et d'insérer les deux derniers nombres par vous-même.

Pour rappel, si le nombre actuel du tableau non trié est inférieur à un nombre auquel il est comparé dans le tableau trié, celui dans le tableau trié se déplacera vers la droite et créera un espace vide à sa position précédente pour insérer le nombre actuel.

Cela continuera jusqu'à ce que le nombre actuel atteigne une position où il est plus grand que le nombre auquel il est comparé. À ce stade, vous insérez le nombre actuel dans le dernier espace créé.

Lorsque vous avez terminé, le tableau ressemblera à ceci : 1, 3, 4, 7, 10, 11.

Regardons quelques exemples de code !

## Exemple de tri par insertion en Java

Si nous voulons faire cela avec du code, voici à quoi cela ressemblerait :

```java
public class InsertionSort {
	
	void sortArray(int arr[])
	{
		int n = arr.length;
		for (int i = 1; i < n; i++) {
			int current = arr[i];
			int j = i - 1;
            
			while (j >= 0 && arr[j] > current) {
				arr[j + 1] = arr[j];
				j = j - 1;
			}
			arr[j + 1] = current;
		}
	}

	static void printArray(int arr[])
	{
		int n = arr.length;
		for (int i = 0; i < n; i++)
			System.out.print(arr[i] + " ");

		System.out.println();
	}

	public static void main(String args[])
	{
		int arr[] = { 7, 3, 10, 4, 1, 11 };

		InsertionSort arrayOfNumbers = new InsertionSort();
		arrayOfNumbers.sortArray(arr);

		printArray(arr);
        
        // imprime 1 3 4 7 10 11
	}
} 

```

Décomposons le code.

```java
void sortArray(int arr[])
	{
		int n = arr.length;
		for (int i = 1; i < n; i++) {
			int current = arr[i];
			int j = i - 1;
            
			while (j >= 0 && arr[j] > current) {
				arr[j + 1] = arr[j];
				j = j - 1;
			}
			arr[j + 1] = current;
		}
	}
```

Ci-dessus, nous avons créé une fonction pour trier un tableau. Elle prend un type de données de tableau comme argument. Nous avons ensuite stocké la longueur du tableau dans une variable appelée `n`.

Dans notre boucle, vous avez peut-être remarqué que la variable `i` est 1. Vous avez peut-être l'habitude de voir cela comme 0 dans les boucles. Elle est 1 ici car nous commençons notre tri à partir de la deuxième valeur du tableau.

La variable `current` est la valeur actuelle en cours de tri. La variable `j` est utilisée pour déplacer la position de la variable `current` vers la gauche en diminuant sa valeur.

La boucle while qui suit nous aide à vérifier quand arrêter de diminuer la position de la variable `current` grâce aux conditions fournies.

Lorsque ces conditions sont remplies, la valeur actuelle est insérée au bon endroit. C'est la même chose que l'exemple que nous avons vu dans la dernière section.

```java
static void printArray(int arr[])
	{
		int n = arr.length;
		for (int i = 0; i < n; i++)
			System.out.print(arr[i] + " ");

		System.out.println();
	}
```

Le code ci-dessus est simplement une fonction pour imprimer les valeurs de notre tableau.

```
public static void main(String args[])
	{
		int arr[] = { 7, 3, 10, 4, 1, 11 };

		InsertionSort arrayOfNumbers = new InsertionSort();
		arrayOfNumbers.sortArray(arr);

		printArray(arr);
        
        // imprime 1 3 4 7 10 11
	}
```

Maintenant, nous l'avons utilisé pour trier notre tableau, puis nous avons imprimé la valeur en utilisant la fonction que nous avions déjà créée.

## Exemple de tri par insertion en C++

```c++
#include <bits/stdc++.h>
using namespace std;

void insertionSort(int arr[], int n)
{
	int i, current, j;
	for (i = 1; i < n; i++)
	{
		current = arr[i];
		j = i - 1;

		while (j >= 0 && arr[j] > current)
		{
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = current;
	}
}

void printArray(int arr[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;
}

int main()
{
	int arrayOfNumbers[] = { 7, 3, 10, 4, 1, 11 };
	int n = sizeof(arrayOfNumbers) / sizeof(arrayOfNumbers[0]);

	insertionSort(arrayOfNumbers, n);
	printArray(arrayOfNumbers, n); // 1 3 4 7 10 11 

	return 0;
}


```

Ce code est identique à celui que nous avons utilisé dans la dernière section. La seule différence est que nous l'avons écrit dans cette section avec C++. Vous pouvez donc consulter l'explication donnée dans la dernière section pour mieux comprendre.

## Conclusion

Dans cet article, nous avons appris comment fonctionne l'algorithme de tri par insertion avec quelques exemples et comment l'appliquer dans notre code Java et C++.

Bon codage !
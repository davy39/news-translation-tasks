---
title: Tableaux multidimensionnels en Python – Matrices expliquées avec des exemples
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-04-06T17:28:05.000Z'
originalURL: https://freecodecamp.org/news/multi-dimensional-arrays-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/gids.JPG
tags:
- name: arrays
  slug: arrays
- name: Python
  slug: python
seo_title: Tableaux multidimensionnels en Python – Matrices expliquées avec des exemples
seo_desc: 'Multi-dimensional arrays, also known as matrices, are a powerful data structure
  in Python. They allow you to store and manipulate data in multiple dimensions or
  axes.

  You''ll commonly use these types of arrays in fields such as mathematics, statistics...'
---

Les tableaux multidimensionnels, également connus sous le nom de matrices, sont une structure de données puissante en Python. Ils permettent de stocker et de manipuler des données dans plusieurs dimensions ou axes.

Vous utiliserez couramment ces types de tableaux dans des domaines tels que les mathématiques, les statistiques et l'informatique pour représenter et traiter des données structurées, telles que des images, des vidéos et des données scientifiques.

En Python, vous pouvez créer des tableaux multidimensionnels en utilisant diverses bibliothèques, telles que NumPy, Pandas et TensorFlow. Dans cet article, nous nous concentrerons sur NumPy, qui est l'une des bibliothèques les plus populaires et largement utilisées pour travailler avec des tableaux en Python.

NumPy fournit un objet de tableau N-dimensionnel puissant que vous pouvez utiliser pour créer et manipuler des tableaux multidimensionnels efficacement. Nous allons maintenant examiner quelques exemples de création et de manipulation de tableaux multidimensionnels en Python en utilisant NumPy.

## Comment créer des tableaux multidimensionnels en utilisant NumPy

Pour créer un tableau multidimensionnel en utilisant NumPy, nous pouvons utiliser la fonction `np.array()` et passer une liste imbriquée de valeurs comme argument. La liste extérieure représente les lignes du tableau, et les listes intérieures représentent les colonnes.

Voici un exemple de création d'un tableau à deux dimensions en utilisant NumPy :

```python
import numpy as np

# Créer un tableau à deux dimensions avec 3 lignes et 4 colonnes
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Afficher le tableau
print(arr)
```

Sortie :

```python
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

Dans cet exemple, nous importons d'abord la bibliothèque NumPy en utilisant l'instruction `import`. Ensuite, nous créons un tableau à deux dimensions en utilisant la fonction `np.array()` et passons une liste de listes comme argument. Chaque liste intérieure représente une ligne du tableau, et la liste extérieure contient toutes les lignes. Enfin, nous affichons le tableau en utilisant la fonction `print()`.

NumPy fournit également d'autres fonctions pour créer des tableaux multidimensionnels, telles que `np.zeros()`, `np.ones()` et `np.random.rand()`. Vous pouvez utiliser ces fonctions pour créer des tableaux de formes et de tailles spécifiques avec des valeurs par défaut ou aléatoires.

## Comment accéder et modifier des tableaux multidimensionnels en utilisant NumPy

Une fois que nous avons créé un tableau multidimensionnel, nous pouvons accéder et modifier ses éléments en utilisant l'indexation et le découpage. Nous utilisons la notation d'index `[i, j]` pour accéder à un élément à la ligne `i` et à la colonne `j`, où `i` et `j` sont des indices basés sur zéro.

Voici un exemple de la façon d'accéder et de modifier des éléments d'un tableau à deux dimensions en utilisant NumPy :

```python
import numpy as np

# Créer un tableau à deux dimensions avec 3 lignes et 4 colonnes
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Accéder à un élément à la ligne 1, colonne 2
print(arr[1, 2])  # Sortie : 7

# Modifier un élément à la ligne 0, colonne 3
arr[0, 3] = 20

# Afficher le tableau modifié
print(arr)
```

Sortie :

```python
7
array([[ 1,  2,  3, 20],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

Dans cet exemple, nous créons un tableau à deux dimensions en utilisant la fonction `np.array()`, puis nous accédons à un élément à la ligne 1, colonne 2 en utilisant l'indexation. Nous modifions ensuite un élément à la ligne 0, colonne 3 en utilisant à nouveau l'indexation. Enfin, nous affichons le tableau modifié en utilisant la fonction `print()`.

Nous pouvons également utiliser le découpage pour accéder et modifier plusieurs éléments d'un tableau multidimensionnel à la fois. Nous utilisons la notation de découpage `arr[i:j, k:l]` pour accéder à un sous-tableau qui contient les lignes `i` à `j-1` et les colonnes `k` à `l-1`.

Voici un exemple de la façon d'utiliser le découpage pour accéder et modifier des éléments d'un tableau à deux dimensions en utilisant NumPy :

```python
import numpy as np

# Créer un tableau à deux dimensions avec 3 lignes et 4 colonnes
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Accéder à un sous-tableau qui contient les lignes 0 à 1 et les colonnes 1 à 2
subarr = arr[0:2, 1:3]

# Afficher le sous-tableau
print(subarr)

# Modifier le sous-tableau en le multipliant par 2
subarr *= 2

# Afficher le tableau modifié
print(arr)
```

Sortie :

```python
array([[2, 3],
       [6, 7]])
array([[ 1,  4,  6,  4],
       [ 5, 12, 14,  8],
       [ 9, 10, 11, 12]])
```

Dans cet exemple, nous créons un tableau à deux dimensions en utilisant la fonction `np.array()`, puis nous utilisons le découpage pour accéder à un sous-tableau qui contient les lignes 0 à 1 et les colonnes 1 à 2. Nous modifions ensuite le sous-tableau en le multipliant par 2, et nous affichons le tableau original modifié en utilisant la fonction `print()`.

## Comment effectuer des opérations sur des tableaux multidimensionnels

NumPy fournit une large gamme de fonctions mathématiques et statistiques que vous pouvez utiliser pour effectuer des opérations sur des tableaux multidimensionnels efficacement. Ces fonctions peuvent vous aider à effectuer des opérations élément par élément, des opérations matricielles et d'autres opérations sur des tableaux de différentes formes et tailles.

Voici un exemple de la façon d'effectuer quelques opérations courantes sur un tableau à deux dimensions en utilisant NumPy :

```python
import numpy as np

# Créer un tableau à deux dimensions avec 3 lignes et 4 colonnes
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Calculer la somme de tous les éléments
print(np.sum(arr))  # Sortie : 78

# Calculer la moyenne de chaque ligne
print(np.mean(arr, axis=1))  # Sortie : [ 2.5  6.5 10.5]

# Calculer le produit scalaire de deux matrices
b = np.array([[2, 3], [4, 5], [6, 7], [8, 9]])
print(np.dot(arr, b))  # Sortie : [[ 60  72]
                        #          [140 172]
                        #          [220 272]]
```

Dans cet exemple, nous créons un tableau à deux dimensions en utilisant la fonction `np.array()`, puis nous utilisons diverses fonctions NumPy pour effectuer des opérations sur le tableau.

Nous calculons d'abord la somme de tous les éléments en utilisant la fonction `np.sum()`. Ensuite, nous calculons la moyenne de chaque ligne en utilisant la fonction `np.mean()` et spécifions le paramètre `axis=1` pour calculer la moyenne le long de chaque ligne. Enfin, nous calculons le produit scalaire du tableau à deux dimensions et d'un autre tableau à deux dimensions `b` en utilisant la fonction `np.dot()`.

## Conclusion

Les tableaux multidimensionnels sont une structure de données puissante et importante en Python. Ils nous permettent de stocker et de manipuler de grandes quantités de données efficacement.

Dans cet article, nous avons couvert les bases de la création et de la manipulation de tableaux multidimensionnels en utilisant NumPy en Python. Nous avons également examiné quelques opérations courantes que nous pouvons effectuer sur des tableaux multidimensionnels en utilisant les fonctions NumPy.

Avec les connaissances acquises dans cet article, vous devriez maintenant être capable de créer et de manipuler des tableaux multidimensionnels pour répondre à vos besoins spécifiques en Python.

Restons en contact sur [Twitter](https://twitter.com/Olujerry19) et [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).
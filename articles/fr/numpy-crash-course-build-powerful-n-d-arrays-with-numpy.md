---
title: Cours accéléré sur Python NumPy – Comment construire des tableaux N-dimensionnels
  pour le Machine Learning
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-22T17:34:36.000Z'
originalURL: https://freecodecamp.org/news/numpy-crash-course-build-powerful-n-d-arrays-with-numpy
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/numpy-1.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: numpy
  slug: numpy
seo_title: Cours accéléré sur Python NumPy – Comment construire des tableaux N-dimensionnels
  pour le Machine Learning
seo_desc: 'NumPy is a Python library for performing large scale numerical computations.
  It is extremely useful, especially in machine learning. Let''s look at what NumPy
  has to offer.

  Introduction to NymPy

  NumPy is a Python library used to perform numerical comp...'
---

NumPy est une bibliothèque Python permettant d'effectuer des calculs numériques à grande échelle. Elle est extrêmement utile, notamment en apprentissage automatique. Examinons ce que NumPy a à offrir.

# Introduction à NymPy

NumPy est une bibliothèque Python utilisée pour effectuer des calculs numériques avec de grands ensembles de données. Le nom signifie Numerical Python et c'est une bibliothèque populaire utilisée par les scientifiques des données, en particulier pour les problèmes d'apprentissage automatique. 

NumPy est utile lors du prétraitement des données avant de les entraîner à l'aide d'un algorithme d'apprentissage automatique.

Travailler avec des tableaux n-dimensionnels est plus facile dans NumPy par rapport aux listes Python. Les tableaux NumPy sont également plus rapides que les listes Python puisque, contrairement aux listes, les tableaux NumPy sont stockés à un endroit continu en mémoire. Cela permet au processeur d'effectuer des calculs efficacement.

Dans cet article, nous examinerons les bases de l'utilisation de NumPy, y compris les opérations sur les tableaux, les transformations de matrices, la génération de valeurs aléatoires, et ainsi de suite.

# Installation

Des instructions d'installation claires sont fournies sur le site officiel de NumPy, donc je ne vais pas les répéter dans cet article. [Veuillez trouver ces instructions ici](https://numpy.org/install/).

# Travailler avec NumPy

## Importer NumPy

Pour commencer à utiliser NumPy dans votre script, vous devez l'importer.

```
import numpy as np
```

## Convertir des tableaux en tableaux NumPy

Vous pouvez convertir vos listes Python existantes en tableaux NumPy en utilisant la méthode np.array(), comme ceci :

```
arr = [1,2,3]
np.array(arr)
```

Cela s'applique également aux tableaux multidimensionnels. NumPy gardera une trace de la forme (dimensions) du tableau.

```
nested_arr = [[1,2],[3,4],[5,6]]
np.array(nested_arr)
```

## Fonction NumPy Arrange

Lorsque vous travaillez avec des données, vous rencontrerez souvent des cas d'utilisation où vous devez générer des données.

NumPy dispose d'une méthode "arrange()" avec laquelle vous pouvez générer une plage de valeurs entre deux nombres. La fonction arrange prend les paramètres de début, de fin et une distance optionnelle.

```
print(np.arange(0,10)) # sans paramètre de distance
SORTIE:[0 1 2 3 4 5 6 7 8 9]

print(np.arange(0,10,2)) # avec paramètre de distance
SORTIE: [0 2 4 6 8]
```

## Zéros et Uns

Vous pouvez également générer un tableau ou une matrice de zéros ou de uns en utilisant NumPy (croyez-moi, vous en aurez besoin). Voici comment faire.

```
print(np.zeros(3))
SORTIE: [0. 0. 0.]

print(np.ones(3))
SORTIE: [1. 1. 1.]
```

Ces deux fonctions supportent également les tableaux n-dimensionnels. Vous pouvez ajouter la forme sous forme de tuple avec des lignes et des colonnes.

```
print(np.zeros((4,5)))
SORTIE:
[
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
]

print(np.ones((4,5)))
SORTIE:
[
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
]
```

## Matrice Identité

Vous pouvez également générer une [matrice identité](https://en.wikipedia.org/wiki/Identity_matrix) en utilisant une fonction intégrée de NumPy appelée "eye".

```
np.eye(5)
SORTIE:
[[1., 0., 0., 0., 0.]
[0., 1., 0., 0., 0.]
[0., 0., 1., 0., 0.]
[0., 0., 0., 1., 0.]
[0., 0., 0., 0., 1.]]
```

## Fonction NumPy Linspace

NumPy dispose d'une méthode linspace qui génère des points régulièrement espacés entre deux nombres.

```
print(np.linspace(0,10,3))
SORTIE:[ 0.  5. 10.]
```

Dans l'exemple ci-dessus, les premier et deuxième paramètres sont les points de départ et de fin, tandis que le troisième paramètre est le nombre de points dont vous avez besoin entre le début et la fin.

Voici la même plage avec 20 points.

```
print(np.linspace(0,10,20))
SORTIE:[ 0. 0.52631579  1.05263158  1.57894737  2.10526316  2.63157895   3.15789474  3.68421053  4.21052632  4.73684211  5.26315789  5.78947368   6.31578947  6.84210526  7.36842105  7.89473684  8.42105263  8.94736842   9.47368421 10.]
```

## Génération de nombres aléatoires

Lorsque vous travaillez sur des problèmes d'apprentissage automatique, vous aurez souvent besoin de générer des nombres aléatoires. NumPy dispose également de fonctions intégrées pour cela.

Mais avant de commencer à générer des nombres aléatoires, examinons deux principaux types de distributions.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/distro-1.png)

### Distribution Normale

Dans une [distribution normale standard](https://www.mathsisfun.com/data/standard-normal-distribution.html), les valeurs culminent au milieu. 

La distribution normale est un concept très important en statistiques car elle est observée dans de nombreux phénomènes naturels. Elle est également appelée "courbe en cloche".

### Distribution Uniforme

Si les valeurs de la distribution ont une probabilité constante, on parle de [distribution uniforme](https://www.investopedia.com/terms/u/uniform-distribution.asp). 

Par exemple, un lancer de pièce a une distribution uniforme puisque la probabilité d'obtenir pile ou face lors d'un lancer de pièce est la même.

Maintenant que vous savez comment fonctionnent les deux principales distributions, générons quelques nombres aléatoires.

* Pour générer des nombres aléatoires dans une distribution uniforme, utilisez la fonction **rand()** de **np.random** :

```
print(np.random.rand(10)) # tableau
SORTIE: [0.46015141 0.89326339 0.22589334 0.29874476 0.5664353  0.39257603  0.77672998 0.35768031 0.95087408 0.34418542]

print(np.random.rand(3,4)) # matrice 3x4
SORTIE:[[0.63775985 0.91746663 0.41667645 0.28272243]  [0.14919547 0.72895922 0.87147748 0.94037953]  [0.5545835  0.30870297 0.49341904 0.27852723]]
```

* Pour générer des nombres aléatoires dans une distribution normale, utilisez la fonction **randn()** de **np.random** :

```
print(np.random.randn(10))
SORTIE:[-1.02087155 -0.75207769 -0.22696798  0.86739858  0.07367362 -0.41932541   0.86303979  0.13739312  0.13214285  1.23089936]

print(np.random.randn(3,4))
SORTIE: [[ 1.61013773  1.37400445  0.55494053  0.23133522]  [ 0.31290971 -0.30866402  0.33093618  0.34868954]  [-0.11659865 -1.22311073  0.36676476  0.40819545]]
```

* Pour générer des entiers aléatoires entre une valeur basse et haute, utilisez la fonction **randint()** de **np.random** :

```
print(np.random.randint(1,100,10))
SORTIE:[64 37 62 27  4 33 23 52 70  7]

print(np.random.randint(1,100,(2,3)))
SORTIE:[[92 42 38]  [87 69 38]]
```

Une [valeur de graine](https://en.wikipedia.org/wiki/Random_seed) est utilisée si vous souhaitez que vos nombres aléatoires soient les mêmes lors de chaque calcul. Voici comment définir une valeur de graine dans NumPy.

* Pour définir une valeur de graine dans NumPy, procédez comme suit :

```
np.random.seed(42)
print(np.random.rand(4))
SORTIE:[0.37454012, 0.95071431, 0.73199394, 0.59865848]
```

Chaque fois que vous utilisez un nombre de graine, vous obtiendrez toujours le même tableau généré sans aucun changement.

## Redimensionnement des tableaux

En tant que scientifique des données, vous travaillerez avec le redimensionnement des ensembles de données pour différents types de calculs. Dans cette section, nous examinerons comment travailler avec les formes des tableaux.

* Pour obtenir la forme d'un tableau, utilisez la propriété **shape**.

```
arr = np.random.rand(2,2)
print(arr)
print(arr.shape)
SORTIE:[
[0.19890857 0.00806693]
[0.48199837 0.55373954]
]
(2, 2)
```

* Pour redimensionner un tableau, utilisez la fonction **reshape()**.

```
print(arr.reshape(1,4))
SORTIE: [[0.19890857 0.00806693 0.48199837 0.55373954]]
print(arr.reshape(4,1))
SORTIE:[
[0.19890857]
[0.00806693]
[0.48199837]
[0.55373954]
]
```

Pour redimensionner définitivement un tableau, vous devez assigner le tableau redimensionné à la variable 'arr'. 

De plus, le redimensionnement ne fonctionne que si la structure existante a du sens. Vous ne pouvez pas redimensionner un tableau 2x2 en un tableau 3x1.

## Découpage de données

Examinons comment récupérer des données à partir de tableaux NumPy. Les tableaux NumPy fonctionnent de manière similaire aux listes Python lors des opérations de récupération.

* Pour découper un tableau, procédez comme suit :

```
myarr = np.arange(0,11)
print(myarr)
SORTIE:[ 0  1  2  3  4  5  6  7  8  9 10]

sliced = myarr[0:5]
print(sliced)
SORTIE: [0 1 2 3 4]

sliced[:] = 99
print(sliced)
SORTIE: [99 99 99 99 99]

print(myarr)
SORTIE:[99 99 99 99 99  5  6  7  8  9 10]
```

Si vous regardez l'exemple ci-dessus, même si nous avons assigné la tranche de "myarr" à la variable "sliced", changer la valeur de "sliced" affecte le tableau original. Cela est dû au fait que la "tranche" pointait simplement vers le tableau original.

Pour créer une section indépendante d'un tableau, utilisez la fonction **copy()**.

```
sliced = myarr.copy()[0:5]
```

* Le découpage de tableaux multidimensionnels fonctionne de manière similaire aux tableaux unidimensionnels.

```
my_matrix = np.random.randint(1,30,(3,3))
print(my_matrix)
SORTIE: [
[21  1 20]
[22 16 27]
[24 14 22]
]

print(my_matrix[0]) # imprimer une seule ligne
SORTIE: [21  1 20]

print(my_matrix[0][0]) # imprimer une seule valeur ou ligne 0, colonne 0
SORTIE: 21

print(my_matrix[0,0]) # méthode alternative pour imprimer la valeur de la ligne 0, colonne 0
SORTIE: 21
```

## Calculs sur les tableaux

Examinons maintenant les calculs sur les tableaux. NumPy est connu pour sa rapidité lors de l'exécution de calculs complexes sur de grands tableaux multidimensionnels.

Essayons quelques opérations de base.

```
new_arr = np.arange(1,11)
print(new_arr)
SORTIE: [ 1  2  3  4  5  6  7  8  9 10]
```

* Addition

```
print(new_arr + 5)
SORTIE: [ 6  7  8  9 10 11 12 13 14 15]
```

* Soustraction

```
print(new_arr - 5)
SORTIE: [-4 -3 -2 -1  0  1  2  3  4  5]
```

* Addition de tableaux

```
print(new_arr + new_arr)
SORTIE: [ 2  4  6  8 10 12 14 16 18 20]
```

* Division de tableaux

```
print(new_arr / new_arr)
SORTIE:[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
```

Pour les [erreurs de division par zéro](https://airbrake.io/blog/python-exception-handling/zerodivisionerror-2), Numpy convertira la valeur en NaN (not a number).

Il existe également quelques méthodes de calcul intégrées disponibles dans NumPy pour calculer des valeurs comme la moyenne, l'écart type, la variance, et autres.

* Somme — np.sum()
* Racine carrée — np.sqrt()
* Moyenne — np.mean()
* Variance — np.var()
* Écart type — np.std()

Lorsque vous travaillez avec des tableaux 2D, vous aurez souvent besoin de calculer la somme, la moyenne, la variance, etc., par ligne ou par colonne. Vous pouvez utiliser le paramètre axis optionnel pour spécifier si vous souhaitez choisir une ligne ou une colonne.

```
arr2d = np.arange(25).reshape(5,5)
print(arr2d)
SORTIE: [
[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]
]

print(arr2d.sum())
SORTIE: 300

print(arr2d.sum(axis=0))  # somme des colonnes
SORTIE: [50 55 60 65 70]

print(arr2d.sum(axis=1)) # somme des lignes
SORTIE: [ 10  35  60  85 110]
```

## Opérations conditionnelles

Vous pouvez également effectuer un filtrage conditionnel avec NumPy en utilisant la notation entre crochets. Voici un exemple :

```
arr = np.arange(0,10)
SORTIE: [0,2,3,4,5,6,7,8,9]

print(arr > 4)
SORTIE: [False False False False False  True  True  True  True  True]

print(arr[arr > 4])
SORTIE: [5 6 7 8 9]
```

# Résumé

Lorsque vous travaillez avec de grands ensembles de données, NumPy est un outil puissant à avoir dans votre boîte à outils. Il est capable de gérer des calculs numériques avancés et des opérations complexes sur des tableaux n-dimensionnels.

Je recommande vivement d'apprendre NumPy si vous prévoyez de commencer une carrière dans le machine learning.

[Voici un notebook Google Colab si vous souhaitez essayer ces exemples](https://colab.research.google.com/drive/1Oa8J_sZXACQJEiMqANIHkftMgUrqSpVt#scrollTo=ITrCTnT6RkWP).

[**Obtenez un résumé de mes articles**](https://tinyletter.com/manishmshiva) et vidéos envoyés à votre email chaque lundi matin. Vous pouvez également [**me contacter**](https://www.manishmshiva.com/) ici.
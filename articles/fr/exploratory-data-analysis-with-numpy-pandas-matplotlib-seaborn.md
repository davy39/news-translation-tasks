---
title: Qu'est-ce que l'analyse de données ? Comment visualiser des données avec Python,
  Numpy, Pandas, Matplotlib & Seaborn Tutoriel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-24T00:11:01.000Z'
originalURL: https://freecodecamp.org/news/exploratory-data-analysis-with-numpy-pandas-matplotlib-seaborn
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/blog-cover-4.png
tags:
- name: data analysis
  slug: data-analysis
- name: data visualization
  slug: data-visualization
- name: Matplotlib
  slug: matplotlib
- name: numpy
  slug: numpy
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: Qu'est-ce que l'analyse de données ? Comment visualiser des données avec
  Python, Numpy, Pandas, Matplotlib & Seaborn Tutoriel
seo_desc: "By Aakash NS\nData Analysis is the process of exploring, investigating,\
  \ and gathering insights from data using statistical measures and visualizations.\
  \ \nThe objective of data analysis is to develop an understanding of data by uncovering\
  \ trends, relati..."
---

Par Aakash NS

L'analyse de données est le processus d'exploration, d'investigation et de collecte d'informations à partir de données en utilisant des mesures statistiques et des visualisations. 

L'objectif de l'analyse de données est de développer une compréhension des données en découvrant des tendances, des relations et des motifs.

L'analyse de données est à la fois une science et un art. D'une part, elle nécessite que vous connaissiez les statistiques, les techniques de visualisation et les outils d'analyse de données comme Numpy, Pandas et Seaborn. 

D'autre part, elle nécessite que vous posiez des questions intéressantes pour guider l'investigation, puis que vous interprétiez les chiffres et les figures pour générer des informations utiles.

Ce tutoriel sur l'analyse de données couvre les sujets suivants :

1. [Qu'est-ce que le calcul numérique ? Python et Numpy pour les débutants](#heading-installation)
2. [Comment analyser des données tabulaires en utilisant Python et Pandas](#heading-comment-analyser-des-donnees-tabulaires-en-utilisant-python-et-pandas)
3. [Visualisation de données en utilisant Python, Matplotlib et Seaborn](#heading-visualisation-de-donnees-en-utilisant-python-matplotlib-et-seaborn)

## Qu'est-ce que le calcul numérique ? Python et Numpy pour les débutants

![Image](https://i.imgur.com/mg8O3kd.png)
_Source : [Elegant Scipy](https://github.com/elegant-scipy/elegant-scipy/blob/master/figures/NumPy_ndarrays_v2.png)_

Vous pouvez suivre le tutoriel et exécuter le code ici : [https://jovian.ai/aakashns/python-numerical-computing-with-nump](https://jovian.ai/aakashns/python-numerical-computing-with-numpy)y

Cette section couvre les sujets suivants :

* Comment travailler avec des données numériques en Python
* Comment transformer des listes Python en tableaux Numpy
* Tableaux Numpy multidimensionnels et leurs avantages
* Opérations sur les tableaux, diffusion, indexation et découpage
* Comment travailler avec des fichiers de données CSV en utilisant Numpy

### Comment travailler avec des données numériques en Python

Les "données" dans l'_Analyse de Données_ font généralement référence à des données numériques, comme les prix des actions, les chiffres de vente, les mesures des capteurs, les scores sportifs, les tables de base de données, et ainsi de suite. 

La bibliothèque [Numpy](https://jovian.ai/outlink?url=https%3A%2F%2Fnumpy.org) fournit des structures de données spécialisées, des fonctions et d'autres outils pour le calcul numérique en Python. Travaillons à travers un exemple pour voir pourquoi et comment utiliser Numpy pour travailler avec des données numériques.

Supposons que nous voulons utiliser des données climatiques comme la température, les précipitations et l'humidité pour déterminer si une région est bien adaptée à la culture des pommes. 

Une approche simple pour faire cela serait de formuler la relation entre le rendement annuel des pommes (tonnes par hectare) et les conditions climatiques comme la température moyenne (en degrés Fahrenheit), les précipitations (en millimètres) et l'humidité relative moyenne (en pourcentage) comme une équation linéaire.

`rendement_pommes = w1 * température + w2 * précipitations + w3 * humidité`

Nous exprimons le rendement des pommes comme une somme pondérée de la température, des précipitations et de l'humidité. 

Cette équation est une approximation, puisque la relation réelle peut ne pas être nécessairement linéaire, et il peut y avoir d'autres facteurs impliqués. Mais un modèle linéaire simple comme celui-ci fonctionne souvent bien en pratique.

Sur la base de certaines analyses statistiques des données historiques, nous pourrions obtenir des valeurs raisonnables pour les poids `w1`, `w2` et `w3`. Voici un exemple de valeurs :

```py
w1, w2, w3 = 0.3, 0.2, 0.5
```

Étant donné certaines données climatiques pour une région, nous pouvons maintenant prédire le rendement des pommes. Voici quelques données d'exemple :

![Image](https://i.imgur.com/TXPBiqv.png)

Pour commencer, nous pouvons définir quelques variables pour enregistrer les données climatiques d'une région.

```py
temp_kanto = 73
precipitations_kanto = 67
humidite_kanto = 43
```

Nous pouvons maintenant substituer ces variables dans l'équation linéaire pour prédire le rendement des pommes.

```py
rendement_pommes_kanto = temp_kanto * w1 + precipitations_kanto * w2 + humidite_kanto * w3
rendement_pommes_kanto
# 56.8

print("Le rendement attendu de pommes dans la région de Kanto est de {} tonnes par hectare.".format(rendement_pommes_kanto))
# Le rendement attendu de pommes dans la région de Kanto est de 56.8 tonnes par hectare.
```

Pour faciliter légèrement l'exécution du calcul ci-dessus pour plusieurs régions, nous pouvons représenter les données climatiques de chaque région sous forme de vecteur, c'est-à-dire une liste de nombres.

```py
kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]
```

Les trois nombres dans chaque vecteur représentent respectivement les données de température, de précipitations et d'humidité.

Nous pouvons également représenter l'ensemble des poids utilisés dans la formule sous forme de vecteur.

```py
poids = [w1, w2, w3]
```

Nous pouvons maintenant écrire une fonction `rendement_culture` pour calculer le rendement des pommes (ou de toute autre culture) étant donné les données climatiques et les poids respectifs.

```py
def rendement_culture(region, poids):
    resultat = 0
    for x, w in zip(region, poids):
        resultat += x * w
    return resultat
    
rendement_culture(kanto, poids)
# 56.8

rendement_culture(johto, poids)
# 76.9

rendement_culture(unova, poids)
# 74.9
```

### Comment transformer des listes Python en tableaux Numpy

Le calcul effectué par `rendement_culture` (multiplication élément par élément de deux vecteurs et prise d'une somme des résultats) est également appelé le _produit scalaire_. En savoir plus sur les produits scalaires [ici](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/dot-cross-products/v/vector-dot-product-and-vector-length).

La bibliothèque Numpy fournit une fonction intégrée pour calculer le produit scalaire de deux vecteurs. Cependant, nous devons d'abord convertir les listes en tableaux Numpy.

Installons la bibliothèque Numpy en utilisant le gestionnaire de paquets `pip`.

```py
!pip install numpy --upgrade --quiet
```

Ensuite, importons le module `numpy`. Il est courant de l'importer avec l'alias `np`.

```py
import numpy as np
```

Nous pouvons maintenant utiliser la fonction `np.array` pour créer des tableaux Numpy.

```py
kanto = np.array([73, 67, 43])

kanto
# array([73, 67, 43])

poids = np.array([w1, w2, w3])

poids
# array([0.3, 0.2, 0.5])
```

Les tableaux Numpy ont le type `ndarray`.

```py
type(kanto)
# numpy.ndarray

type(poids)
# numpy.ndarray
```

Tout comme les listes, les tableaux Numpy supportent la notation d'indexation `[]`.

```py
poids[0]
# 0.3

kanto[2]
#43
```

### Comment opérer sur les tableaux Numpy

Nous pouvons maintenant calculer le produit scalaire des deux vecteurs en utilisant la fonction `np.dot`.

```py
np.dot(kanto, poids)
# 56.8
```

Nous pouvons obtenir le même résultat avec des opérations de bas niveau supportées par les tableaux Numpy : effectuer une multiplication élément par élément et calculer la somme des nombres résultants.

```py
(kanto * poids).sum()
# 56.8
```

L'opérateur `*` effectue une multiplication élément par élément de deux tableaux s'ils ont la même taille. La méthode `sum` calcule la somme des nombres dans un tableau.

```py
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr1 * arr2
# array([ 4, 10, 18])

arr2.sum()
# 15
```

### Quels sont les avantages de l'utilisation des tableaux Numpy ?

Les tableaux Numpy offrent les avantages suivants par rapport aux listes Python pour opérer sur des données numériques :

* **Ils sont faciles à utiliser** : Vous pouvez écrire de petites expressions mathématiques concises et intuitives comme `(kanto * poids).sum()` plutôt que d'utiliser des boucles et des fonctions personnalisées comme `rendement_culture`.
* **Performance** : Les opérations et fonctions Numpy sont implémentées en interne en C++, ce qui les rend beaucoup plus rapides que l'utilisation d'instructions et de boucles Python qui sont interprétées à l'exécution.

Voici une comparaison des produits scalaires effectués en utilisant des boucles Python vs. des tableaux Numpy sur deux vecteurs avec un million d'éléments chacun.

```py
# Listes Python
arr1 = list(range(1000000))
arr2 = list(range(1000000, 2000000))

# Tableaux Numpy
arr1_np = np.array(arr1)
arr2_np = np.array(arr2)

%%time
result = 0
for x1, x2 in zip(arr1, arr2):
    result += x1*x2
result

# CPU times: user 300 ms, sys: 3.26 ms, total: 303 ms
# Wall time: 302 ms
# 833332333333500000

%%time
np.dot(arr1_np, arr2_np)

# CPU times: user 2.11 ms, sys: 951 µs, total: 3.07 ms
# Wall time: 1.58 ms
# 833332333333500000
```

Comme vous pouvez le voir, l'utilisation de `np.dot` est 100 fois plus rapide que l'utilisation d'une boucle `for`. Cela rend Numpy particulièrement utile lors du travail avec de très grands ensembles de données contenant des dizaines de milliers ou des millions de points de données.

### Tableaux Numpy multidimensionnels

Nous pouvons maintenant aller plus loin et représenter les données climatiques de toutes les régions à l'aide d'un seul tableau Numpy à deux dimensions.

```py
donnees_climatiques = np.array([[73, 67, 43],
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]])
                         
 donnees_climatiques
# array([[ 73,  67,  43],
#        [ 91,  88,  64],
#        [ 87, 134,  58],
#        [102,  43,  37],
#        [ 69,  96,  70]])
```

Si vous avez suivi un cours d'algèbre linéaire au lycée, vous pouvez reconnaître le tableau 2D ci-dessus comme une matrice avec cinq lignes et trois colonnes. Chaque ligne représente une région, et les colonnes représentent respectivement la température, les précipitations et l'humidité.

Les tableaux Numpy peuvent avoir n'importe quel nombre de dimensions et différentes longueurs le long de chaque dimension. Nous pouvons inspecter la longueur le long de chaque dimension en utilisant la propriété `.shape` d'un tableau.

![Image](https://fgnt.github.io/python_crashkurs_doc/_images/numpy_array_t.png)
_Source : [Elegant Scipy](https://github.com/elegant-scipy/elegant-scipy/blob/master/figures/NumPy_ndarrays_v2.png)_

```py
# Tableau 2D (matrice)
donnees_climatiques.shape
# (5, 3)

poids
# array([0.3, 0.2, 0.5])

# Tableau 1D (vecteur)
poids.shape
# (3,)

# Tableau 3D 
arr3 = np.array([
    [[11, 12, 13], 
     [13, 14, 15]], 
    [[15, 16, 17], 
     [17, 18, 19.5]]])

arr3.shape
# (2, 2, 3)
```

Tous les éléments d'un tableau numpy ont le même type de données. Vous pouvez vérifier le type de données d'un tableau en utilisant la propriété `.dtype`.

```py
poids.dtype
# dtype('float64')

donnees_climatiques.dtype
# dtype('int64')
```

Si un tableau contient même un seul nombre à virgule flottante, tous les autres éléments sont également convertis en flottants.

```py
arr3.dtype
# dtype('float64')
```

Nous pouvons maintenant calculer les rendements prédits de pommes dans toutes les régions, en utilisant une seule multiplication de matrices entre `donnees_climatiques` (une matrice 5x3) et `poids` (un vecteur de longueur 3). Voici à quoi cela ressemble visuellement :

![Image](https://i.imgur.com/LJ2WKSI.png)

Vous pouvez en apprendre davantage sur les matrices et la multiplication de matrices en regardant les 3-4 premières vidéos de [cette playlist YouTube](https://www.youtube.com/watch?v=xyAuNHPsq-g&list=PLFD0EB975BA0CC1E0&index=1).

Nous pouvons utiliser la fonction `np.matmul` ou l'opérateur `@` pour effectuer la multiplication de matrices.

```py
np.matmul(donnees_climatiques, poids)
# array([56.8, 76.9, 81.9, 57.7, 74.9])

donnees_climatiques @ poids
# array([56.8, 76.9, 81.9, 57.7, 74.9])
```

### Comment travailler avec des fichiers de données CSV

Numpy fournit également des fonctions d'assistance pour la lecture et l'écriture de fichiers. Téléchargeons un fichier `climate.txt`, qui contient 10 000 mesures climatiques (température, précipitations et humidité) au format suivant :

```
temperature,rainfall,humidity
25.00,76.00,99.00
39.00,65.00,70.00
59.00,45.00,77.00
84.00,63.00,38.00
66.00,50.00,52.00
41.00,94.00,77.00
91.00,57.00,96.00
49.00,96.00,99.00
67.00,20.00,28.00
...

```

Ce format de stockage de données est connu sous le nom de _valeurs séparées par des virgules_ ou CSV.

> **CSV** : Un fichier de valeurs séparées par des virgules (CSV) est un fichier texte délimité qui utilise une virgule pour séparer les valeurs. Chaque ligne du fichier est un enregistrement de données. Chaque enregistrement se compose d'un ou plusieurs champs, séparés par des virgules. Un fichier CSV stocke généralement des données tabulaires (nombres et texte) en texte brut, auquel cas chaque ligne aura le même nombre de champs. (Wikipedia)

Pour lire ce fichier dans un tableau numpy, nous pouvons utiliser la fonction `genfromtxt`.

```py
import urllib.request

urllib.request.urlretrieve(
    'https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv', 
    'climate.txt')
    
climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)

climate_data
# array([[25., 76., 99.],
#        [39., 65., 70.],
#        [59., 45., 77.],
#        ...,
#        [99., 62., 58.],
#        [70., 71., 91.],
#        [92., 39., 76.]])

climate_data.shape
# (10000, 3)
```

Nous pouvons maintenant effectuer une multiplication de matrices en utilisant l'opérateur `@` pour prédire le rendement des pommes pour l'ensemble du jeu de données en utilisant un ensemble donné de poids.

```py
poids = np.array([0.3, 0.2, 0.5])

rendements = climate_data @ poids
rendements
# array([72.2, 59.7, 65.2, ..., 71.1, 80.7, 73.4])

rendements.shape
# (10000,)
```

Ajoutons les `rendements` à `climate_data` en tant que quatrième colonne en utilisant la fonction [`np.concatenate`](https://jovian.ai/outlink?url=https%3A%2F%2Fnumpy.org%2Fdoc%2Fstable%2Freference%2Fgenerated%2Fnumpy.concatenate.html).

```py
climate_results = np.concatenate((climate_data, rendements.reshape(10000, 1)), axis=1)

climate_results
# array([[25. , 76. , 99. , 72.2],
#        [39. , 65. , 70. , 59.7],
#        [59. , 45. , 77. , 65.2],
#        ...,
#        [99. , 62. , 58. , 71.1],
#        [70. , 71. , 91. , 80.7],
#        [92. , 39. , 76. , 73.4]])
```

Il y a quelques subtilités ici :

* Puisque nous souhaitons ajouter de nouvelles colonnes, nous passons l'argument `axis=1` à `np.concatenate`. L'argument `axis` spécifie la dimension pour la concaténation.
* Les tableaux doivent avoir le même nombre de dimensions et la même longueur le long de chaque dimension sauf celle utilisée pour la concaténation. Nous utilisons la fonction [`np.reshape`](https://jovian.ai/outlink?url=https%3A%2F%2Fnumpy.org%2Fdoc%2Fstable%2Freference%2Fgenerated%2Fnumpy.reshape.html) pour changer la forme de `rendements` de `(10000,)` à `(10000,1)`.

Voici une explication visuelle de `np.concatenate` le long de `axis=1` (pouvez-vous deviner ce que `axis=0` donne ?) :

![Image](https://www.w3resource.com/w3r_images/python-numpy-image-exercise-58.png)
_Source : [w3resource.com](w3resource.com)_

La meilleure façon de comprendre ce que fait une fonction Numpy est d'expérimenter avec elle et de lire la documentation pour en apprendre davantage sur ses arguments et ses valeurs de retour. Utilisez les cellules ci-dessous pour expérimenter avec `np.concatenate` et `np.reshape`.

Écrivons les résultats finaux de notre calcul ci-dessus dans un fichier en utilisant la fonction `np.savetxt`.

```py
np.savetxt('climate_results.txt', 
           climate_results, 
           fmt='%.2f', 
           delimiter=',',
           header='temperature,rainfall,humidity,yeild_apples', 
           comments='')
```

Les résultats sont écrits au format CSV dans le fichier `climate_results.txt`.

```
temperature,rainfall,humidity,yeild_apples
25.00,76.00,99.00,72.20
39.00,65.00,70.00,59.70
59.00,45.00,77.00,65.20
84.00,63.00,38.00,56.80
...
```

Numpy fournit des centaines de fonctions pour effectuer des opérations sur les tableaux. Voici quelques fonctions couramment utilisées :

* Mathématiques : `np.sum`, `np.exp`, `np.round`, opérateurs arithmétiques
* Manipulation de tableaux : `np.reshape`, `np.stack`, `np.concatenate`, `np.split`
* Algèbre linéaire : `np.matmul`, `np.dot`, `np.transpose`, `np.eigvals`
* Statistiques : `np.mean`, `np.median`, `np.std`, `np.max`

**Alors, comment trouver la fonction dont vous avez besoin ?** La manière la plus simple de trouver la bonne fonction pour une opération ou un cas d'utilisation spécifique est de faire une recherche sur le web. Par exemple, rechercher "Comment joindre des tableaux numpy" mène à [ce tutoriel sur la concaténation de tableaux](https://jovian.ai/outlink?url=https%3A%2F%2Fcmdlinetips.com%2F2018%2F04%2Fhow-to-concatenate-arrays-in-numpy%2F).

Vous pouvez trouver une [liste complète des fonctions de tableaux ici](https://numpy.org/doc/stable/reference/routines.html).

### Opérations arithmétiques Numpy, diffusion et comparaison

Les tableaux Numpy supportent les opérateurs arithmétiques comme `+`, `-`, `*`, etc. Vous pouvez effectuer une opération arithmétique avec un seul nombre (également appelé scalaire) ou avec un autre tableau de même forme. 

Les opérateurs facilitent l'écriture d'expressions mathématiques avec des tableaux multidimensionnels.

```py
arr2 = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 1, 2, 3]])
                 
arr3 = np.array([[11, 12, 13, 14], 
                 [15, 16, 17, 18], 
                 [19, 11, 12, 13]])
                 
# Ajout d'un scalaire
arr2 + 3

# array([[ 4,  5,  6,  7],
#        [ 8,  9, 10, 11],
#        [12,  4,  5,  6]])

# Soustraction élément par élément
arr3 - arr2

# array([[10, 10, 10, 10],
#        [10, 10, 10, 10],
#        [10, 10, 10, 10]])

# Division par un scalaire
arr2 / 2

# array([[0.5, 1. , 1.5, 2. ],
#        [2.5, 3. , 3.5, 4. ],
#        [4.5, 0.5, 1. , 1.5]])

# Multiplication élément par élément
arr2 * arr3

# array([[ 11,  24,  39,  56],
#        [ 75,  96, 119, 144],
#        [171,  11,  24,  39]])

# Modulo avec un scalaire
arr2 % 4

# array([[1, 2, 3, 0],
#        [1, 2, 3, 0],
#        [1, 1, 2, 3]])
```

#### **Diffusion des tableaux Numpy**

Les tableaux Numpy supportent également la _diffusion_, permettant des opérations arithmétiques entre deux tableaux avec des nombres de dimensions différents mais des formes compatibles. Regardons un exemple pour voir comment cela fonctionne.

```py
arr2 = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 1, 2, 3]])               
arr2.shape
# (3, 4)

arr4 = np.array([4, 5, 6, 7])
arr4.shape
# (4,)

arr2 + arr4
# array([[ 5,  7,  9, 11],
#        [ 9, 11, 13, 15],
#        [13,  6,  8, 10]])
```

Lorsque l'expression `arr2 + arr4` est évaluée, `arr4` (qui a la forme `(4,)`) est répliqué trois fois pour correspondre à la forme `(3, 4)` de `arr2`. Numpy effectue la réplication sans créer trois copies du tableau de dimension inférieure, améliorant ainsi les performances et utilisant moins de mémoire.

![Image](https://jakevdp.github.io/PythonDataScienceHandbook/figures/02.05-broadcasting.png)
_Source : [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html)_

La diffusion ne fonctionne que si l'un des tableaux peut être répliqué pour correspondre à la forme de l'autre tableau.

```py
arr5 = np.array([7, 8])
arr5.shape
# (2,)

arr2 + arr5
# ValueError: operands could not be broadcast together with shapes (3,4) (2,) 
```

Dans l'exemple ci-dessus, même si `arr5` est répliqué trois fois, il ne correspondra pas à la forme de `arr2`. Donc `arr2 + arr5` ne peut pas être évalué avec succès. [En savoir plus sur la diffusion ici](https://numpy.org/doc/stable/user/basics.broadcasting.html).

#### **Comparaison des tableaux Numpy**

Les tableaux Numpy supportent également les opérations de comparaison comme `==`, `!=`, `>` et ainsi de suite. Le résultat est un tableau de booléens.

```py
arr1 = np.array([[1, 2, 3], [3, 4, 5]])
arr2 = np.array([[2, 2, 3], [1, 2, 5]])

arr1 == arr2
# array([[False,  True,  True],
#        [False, False,  True]])

arr1 != arr2
# array([[ True, False, False],
#        [ True,  True, False]])

arr1 >= arr2
# array([[False,  True,  True],
#        [ True,  True,  True]])

arr1 < arr2
# array([[ True, False, False],
#        [False, False, False]])
```

La comparaison de tableaux est fréquemment utilisée pour compter le nombre d'éléments égaux dans deux tableaux en utilisant la méthode `sum`. N'oubliez pas que `True` évalue à `1` et `False` évalue à `0` lorsque vous utilisez des booléens dans des opérations arithmétiques.

```py
(arr1 == arr2).sum()
# 3
```

### Indexation et découpage des tableaux Numpy

Numpy étend la notation d'indexation des listes Python en utilisant `[]` à plusieurs dimensions de manière intuitive. Vous pouvez fournir une liste séparée par des virgules d'indices ou de plages pour sélectionner un élément spécifique ou un sous-tableau (également appelé une tranche) à partir d'un tableau Numpy.

```py
arr3 = np.array([
    [[11, 12, 13, 14], 
     [13, 14, 15, 19]], 
    
    [[15, 16, 17, 21], 
     [63, 92, 36, 18]], 
    
    [[98, 32, 81, 23],      
     [17, 18, 19.5, 43]]])
     
arr3.shape
# (3, 2, 4)

# Élément unique
arr3[1, 1, 2]

# 36.0

# Sous-tableau utilisant des plages
arr3[1:, 0:1, :2]

# array([[[15., 16.]],
# 
#        [[98., 32.]]])

# Mélange d'indices et de plages
arr3[1:, 1, 3]

# array([18., 43.])

arr3[1:, 1, :3]
# array([[63. , 92. , 36. ],
#        [17. , 18. , 19.5]])

# Utilisation de moins d'indices
arr3[1]

# array([[15., 16., 17., 21.],
#        [63., 92., 36., 18.]])

arr3[:2, 1]
# array([[13., 14., 15., 19.],
#        [63., 92., 36., 18.]])

# Utilisation de trop d'indices
arr3[1,3,2,1]

# IndexError: too many indices for array: array is 3-dimensional, but 4 were indexed
```

La notation et ses résultats peuvent sembler déroutantes au début, alors prenez votre temps pour expérimenter et vous familiariser avec elle. 

Utilisez les cellules ci-dessous pour essayer quelques exemples d'indexation et de découpage de tableaux, avec différentes combinaisons d'indices et de plages. Voici quelques exemples supplémentaires démontrés visuellement :

![Image](https://scipy-lectures.org/_images/numpy_indexing.png)
_Source : [Scipy Lectures](https://scipy-lectures.org/intro/numpy/array_object.html)_

### Comment créer des tableaux Numpy – Autres méthodes

Numpy fournit également des fonctions pratiques pour créer des tableaux de formes souhaitées avec des valeurs fixes ou aléatoires. Consultez la [documentation officielle](https://jovian.ai/outlink?url=https%3A%2F%2Fnumpy.org%2Fdoc%2Fstable%2Freference%2Froutines.array-creation.html) ou utilisez la fonction `help` pour en savoir plus.

```
# Tous zéros
np.zeros((3, 2))

# array([[0., 0.],
#        [0., 0.],
#        [0., 0.]])

# Tous uns
np.ones([2, 2, 3])

# array([[[1., 1., 1.],
#         [1., 1., 1.]],
#
#        [[1., 1., 1.],
#         [1., 1., 1.]]])

# Matrice identité
np.eye(3)

# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])

# Vecteur aléatoire
np.random.rand(5)

# array([0.92929562, 0.11301864, 0.64213555, 0.8600434 , 0.53738656])

# Matrice aléatoire
np.random.randn(2, 3) # rand vs. randn - quelle est la différence ?

# array([[ 0.09906435, -1.64668094,  0.08073528],
#        [ 0.1437016 ,  0.80715712,  1.27285476]])

# Valeur fixe
np.full([2, 3], 42)

# array([[42, 42, 42],
#        [42, 42, 42]])

# Plage avec début, fin et pas
np.arange(10, 90, 3)

# array([10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58,
#        61, 64, 67, 70, 73, 76, 79, 82, 85, 88])

# Nombres équidistants dans une plage
np.linspace(3, 27, 9)

# array([ 3.,  6.,  9., 12., 15., 18., 21., 24., 27.])
```

### Exercices

Essayez les exercices suivants pour vous familiariser avec les tableaux Numpy et pratiquer vos compétences :

* Devoir sur les fonctions de tableaux Numpy : [https://jovian.ml/aakashns/numpy-array-operations](https://jovian.ai/outlink?url=https%3A%2F%2Fjovian.ml%2Faakashns%2Fnumpy-array-operations)
* (Optionnel) 100 exercices numpy : [https://jovian.ml/aakashns/100-numpy-exercises](https://jovian.ai/outlink?url=https%3A%2F%2Fjovian.ml%2Faakashns%2F100-numpy-exercises)

### Résumé et lectures complémentaires

Avec cela, nous terminons notre discussion sur le calcul numérique avec Numpy. Nous avons couvert les sujets suivants dans cette partie du tutoriel :

* Comment passer des listes Python aux tableaux Numpy
* Comment opérer sur les tableaux Numpy
* Les avantages de l'utilisation des tableaux Numpy par rapport aux listes
* Tableaux Numpy multidimensionnels
* Comment travailler avec des fichiers de données CSV
* Opérations arithmétiques et diffusion
* Indexation et découpage des tableaux
* Autres façons de créer des tableaux Numpy

Consultez les ressources suivantes pour en savoir plus sur Numpy :

* [Tutoriel officiel](https://numpy.org/devdocs/user/quickstart.html)
* [Cours Numpy sur freeCodeCamp](https://www.freecodecamp.org/news/the-ultimate-guide-to-the-numpy-scientific-computing-library-for-python/)
* [Numpy avancé (exploration des internes)](http://scipy-lectures.org/advanced/advanced_numpy/index.html)

### Questions de révision pour vérifier votre compréhension

Essayez de répondre aux questions suivantes pour tester votre compréhension des sujets couverts dans ce notebook :

1. Qu'est-ce qu'un vecteur ?
2. Comment représentez-vous les vecteurs en utilisant une liste Python ? Donnez un exemple.
3. Qu'est-ce qu'un produit scalaire de deux vecteurs ?
4. Écrivez une fonction pour calculer le produit scalaire de deux vecteurs.
5. Qu'est-ce que Numpy ?
6. Comment installez-vous Numpy ?
7. Comment importez-vous le module `numpy` ?
8. Que signifie importer un module avec un alias ? Donnez un exemple.
9. Quel est l'alias couramment utilisé pour `numpy` ?
10. Qu'est-ce qu'un tableau Numpy ?
11. Comment créez-vous un tableau Numpy ? Donnez un exemple.
12. Quel est le type des tableaux Numpy ?
13. Comment accédez-vous aux éléments d'un tableau Numpy ?
14. Comment calculez-vous le produit scalaire de deux vecteurs en utilisant Numpy ?
15. Que se passe-t-il si vous essayez de calculer le produit scalaire de deux vecteurs qui ont des tailles différentes ?
16. Comment calculez-vous le produit élément par élément de deux tableaux Numpy ?
17. Comment calculez-vous la somme de tous les éléments dans un tableau Numpy ?
18. Quels sont les avantages de l'utilisation des tableaux Numpy par rapport aux listes Python pour opérer sur des données numériques ?
19. Pourquoi les opérations sur les tableaux Numpy ont-elles de meilleures performances par rapport aux fonctions et boucles Python ?
20. Illustrez la différence de performance entre les opérations sur les tableaux Numpy et les boucles Python à l'aide d'un exemple.
21. Qu'est-ce que les tableaux Numpy multidimensionnels ?
22. Illustrez comment vous créeriez des tableaux Numpy avec 2, 3 et 4 dimensions.
23. Comment inspectez-vous le nombre de dimensions et la longueur le long de chaque dimension dans un tableau Numpy ?
24. Les éléments d'un tableau Numpy peuvent-ils avoir différents types de données ?
25. Comment vérifiez-vous les types de données des éléments d'un tableau Numpy ?
26. Quel est le type de données d'un tableau Numpy ?
27. Quelle est la différence entre une matrice et un tableau Numpy 2D ?
28. Comment effectuez-vous la multiplication de matrices en utilisant Numpy ?
29. À quoi sert l'opérateur `@` dans Numpy ?
30. Qu'est-ce que le format de fichier CSV ?
31. Comment lisez-vous des données à partir d'un fichier CSV en utilisant Numpy ?
32. Comment concaténez-vous deux tableaux Numpy ?
33. Quel est le but de l'argument `axis` de `np.concatenate` ?
34. Quand deux tableaux Numpy sont-ils compatibles pour la concaténation ?
35. Donnez un exemple de deux tableaux Numpy qui peuvent être concaténés.
36. Donnez un exemple de deux tableaux Numpy qui ne peuvent pas être concaténés.
37. Quel est le but de la fonction `np.reshape` ?
38. Que signifie "remodeler" un tableau Numpy ?
39. Comment écrivez-vous un tableau numpy dans un fichier CSV ?
40. Donnez quelques exemples de fonctions Numpy pour effectuer des opérations mathématiques.
41. Donnez quelques exemples de fonctions Numpy pour effectuer la manipulation de tableaux.
42. Donnez quelques exemples de fonctions Numpy pour effectuer l'algèbre linéaire.
43. Donnez quelques exemples de fonctions Numpy pour effectuer des opérations statistiques.
44. Comment trouvez-vous la bonne fonction Numpy pour une opération ou un cas d'utilisation spécifique ?
45. Où pouvez-vous voir une liste de toutes les fonctions et opérations de tableaux Numpy ?
46. Quels sont les opérateurs arithmétiques supportés par les tableaux Numpy ? Illustrez avec des exemples.
47. Qu'est-ce que la diffusion de tableaux ? Comment est-elle utile ? Illustrez avec un exemple.
48. Donnez quelques exemples de tableaux qui sont compatibles pour la diffusion.
49. Donnez quelques exemples de tableaux qui ne sont pas compatibles pour la diffusion.
50. Quels sont les opérateurs de comparaison supportés par les tableaux Numpy ? Illustrez avec des exemples.
51. Comment accédez-vous à un sous-tableau ou une tranche spécifique à partir d'un tableau Numpy ?
52. Illustrez l'indexation et le découpage de tableaux dans les tableaux Numpy multidimensionnels avec quelques exemples.
53. Comment créez-vous un tableau Numpy avec une forme donnée contenant tous des zéros ?
54. Comment créez-vous un tableau Numpy avec une forme donnée contenant tous des uns ?
55. Comment créez-vous une matrice identité d'une forme donnée ?
56. Comment créez-vous un vecteur aléatoire d'une longueur donnée ?
57. Comment créez-vous un tableau Numpy avec une forme donnée avec une valeur fixe pour chaque élément ?
58. Comment créez-vous un tableau Numpy avec une forme donnée contenant des éléments initialisés aléatoirement ?
59. Quelle est la différence entre `np.random.rand` et `np.random.randn` ? Illustrez avec des exemples.
60. Quelle est la différence entre `np.arange` et `np.linspace` ? Illustrez avec des exemples.

Vous êtes prêt à passer à la section suivante de ce tutoriel.

## Comment analyser des données tabulaires en utilisant Python et Pandas

![Image](https://i.imgur.com/zfxLzEv.png)

Suivez et exécutez le code ici : [https://jovian.ai/aakashns/python-pandas-data-analysis](https://jovian.ai/aakashns/python-pandas-data-analysis).

Cette section couvre les sujets suivants :

* Comment lire un fichier CSV dans un dataframe Pandas
* Comment récupérer des données à partir de dataframes Pandas
* Comment interroger, trier et analyser des données
* Comment fusionner, regrouper et agréger des données
* Comment extraire des informations utiles à partir de dates
* Tracé de base en utilisant des graphiques en ligne et en barre
* Comment écrire des dataframes dans des fichiers CSV

### Comment lire un fichier CSV en utilisant Pandas

[Pandas](https://jovian.ai/outlink?url=https%3A%2F%2Fpandas.pydata.org%2F) est une bibliothèque Python populaire utilisée pour travailler avec des données tabulaires (similaires aux données stockées dans une feuille de calcul). Elle fournit des fonctions d'assistance pour lire des données à partir de divers formats de fichiers comme CSV, feuilles de calcul Excel, tables HTML, JSON, SQL, et plus encore. 

Téléchargeons un fichier `italy-covid-daywise.txt` qui contient des données jour par jour sur le Covid-19 pour l'Italie au format suivant :

```
date,new_cases,new_deaths,new_tests
2020-04-21,2256.0,454.0,28095.0
2020-04-22,2729.0,534.0,44248.0
2020-04-23,3370.0,437.0,37083.0
2020-04-24,2646.0,464.0,95273.0
2020-04-25,3021.0,420.0,38676.0
2020-04-26,2357.0,415.0,24113.0
2020-04-27,2324.0,260.0,26678.0
2020-04-28,1739.0,333.0,37554.0
...

```

Ce format de stockage de données est connu sous le nom de _valeurs séparées par des virgules_ ou CSV. Voici un rappel au cas où vous auriez besoin d'une définition de ce qu'est le format CSV :

> **CSV** : Un fichier de valeurs séparées par des virgules (CSV) est un fichier texte délimité qui utilise une virgule pour séparer les valeurs. Chaque ligne du fichier est un enregistrement de données. Chaque enregistrement se compose d'un ou plusieurs champs, séparés par des virgules. Un fichier CSV stocke généralement des données tabulaires (nombres et texte) en texte brut, auquel cas chaque ligne aura le même nombre de champs. (Wikipedia)

Nous allons télécharger ce fichier en utilisant la fonction `urlretrieve` du module `urllib.request`.

```py
from urllib.request import urlretrieve

urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/italy-covid-daywise.csv', 'italy-covid-daywise.csv')
```

Pour lire le fichier, nous pouvons utiliser la méthode `read_csv` de Pandas. Tout d'abord, installons la bibliothèque Pandas.

```py
!pip install pandas --upgrade --quiet
```

Nous pouvons maintenant importer le module `pandas`. Par convention, il est importé avec l'alias `pd`.

```py
import pandas as pd

covid_df = pd.read_csv('italy-covid-daywise.csv')
```

Les données du fichier sont lues et stockées dans un objet `DataFrame` – l'une des structures de données principales de Pandas pour stocker et travailler avec des données tabulaires. Nous utilisons généralement le suffixe `_df` dans les noms de variables pour les dataframes.

```py
type(covid_df)
# pandas.core.frame.DataFrame

covid_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-108.png)

Voici ce que nous pouvons dire en regardant le dataframe :

* Le fichier fournit quatre comptes jour par jour pour le COVID-19 en Italie
* Les métriques rapportées sont les nouveaux cas, les décès et les tests
* Les données sont fournies pour 248 jours : du 12 décembre 2019 au 3 septembre 2020

Gardez à l'esprit que ce sont des chiffres officiellement rapportés. Le nombre réel de cas et de décès peut être plus élevé, car tous les cas ne sont pas diagnostiqués.

Nous pouvons afficher certaines informations de base sur le dataframe en utilisant la méthode `.info`.

```py
covid_df.info()
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-109.png)

Il semble que chaque colonne contienne des valeurs d'un type de données spécifique. Vous pouvez afficher des informations statistiques pour les colonnes numériques (moyenne, écart-type, valeurs minimales/maximales et le nombre de valeurs non vides) en utilisant la méthode `.describe`.

```py
covid_df.describe()
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-110.png)

La propriété `columns` contient la liste des colonnes au sein du dataframe.

```py
covid_df.columns
# Index(['date', 'new_cases', 'new_deaths', 'new_tests'], dtype='object')
```

Vous pouvez également récupérer le nombre de lignes et de colonnes dans le dataframe en utilisant la méthode `.shape`.

```py
covid_df.shape
# (248, 4)
```

Voici un résumé des fonctions et méthodes que nous avons examinées jusqu'à présent :

* `pd.read_csv` – Lire les données d'un fichier CSV dans un objet Pandas `DataFrame`
* `.info()` – Voir les informations de base sur les lignes, les colonnes et les types de données
* `.describe()` – Voir les informations statistiques sur les colonnes numériques
* `.columns` – Obtenir la liste des noms de colonnes
* `.shape` – Obtenir le nombre de lignes et de colonnes sous forme de tuple

### Comment récupérer des données d'un Data Frame dans Pandas

La première chose que vous pourriez vouloir faire est de récupérer des données de ce data frame, comme les comptes d'un jour spécifique ou la liste des valeurs dans une colonne particulière. 

Pour ce faire, vous devez comprendre la représentation interne des données dans un data frame. Conceptuellement, vous pouvez penser à un dataframe comme un dictionnaire de listes : les clés sont les noms de colonnes, et les valeurs sont des listes/tableaux contenant les données des colonnes respectives.

```py
# Le format Pandas est similaire à ceci
covid_data_dict = {
    'date':       ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases':  [1444, 1365, 996, 975, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_tests': [53541, 42583, 54395, None, None]
}
```

Représenter les données dans le format ci-dessus présente quelques avantages :

* Toutes les valeurs d'une colonne ont généralement le même type de valeur, il est donc plus efficace de les stocker dans un seul tableau.
* Récupérer les valeurs pour une ligne particulière nécessite simplement d'extraire les éléments à un indice donné de chaque tableau de colonnes.
* La représentation est plus compacte (les noms de colonnes sont enregistrés une seule fois) par rapport à d'autres formats qui utilisent un dictionnaire pour chaque ligne de données (voir l'exemple ci-dessous).

```py
# Le format Pandas n'est pas similaire à ceci
covid_data_list = [
    {'date': '2020-08-30', 'new_cases': 1444, 'new_deaths': 1, 'new_tests': 53541},
    {'date': '2020-08-31', 'new_cases': 1365, 'new_deaths': 4, 'new_tests': 42583},
    {'date': '2020-09-01', 'new_cases': 996, 'new_deaths': 6, 'new_tests': 54395},
    {'date': '2020-09-02', 'new_cases': 975, 'new_deaths': 8 },
    {'date': '2020-09-03', 'new_cases': 1326, 'new_deaths': 6},
]
```

Avec l'analogie du dictionnaire de listes en tête, vous pouvez maintenant deviner comment récupérer des données à partir d'un data frame. Par exemple, nous pouvons obtenir une liste de valeurs à partir d'une colonne spécifique en utilisant la notation d'indexation `[]`.

```py
covid_data_dict['new_cases']
# [1444, 1365, 996, 975, 1326]

covid_df['new_cases']
# 0         0.0
# 1         0.0
# 2         0.0
# 3         0.0
# 4         0.0
#         ...  
# 243    1444.0
# 244    1365.0
# 245     996.0
# 246     975.0
# 247    1326.0
# Name: new_cases, Length: 248, dtype: float64
```

Chaque colonne est représentée en utilisant une structure de données appelée `Series`, qui est essentiellement un tableau numpy avec quelques méthodes et propriétés supplémentaires.

```py
type(covid_df['new_cases'])
# pandas.core.series.Series
```

Comme les tableaux, vous pouvez récupérer une valeur spécifique avec une série en utilisant la notation d'indexation `[]`.

```py
covid_df['new_cases'][246]
# 975.0

covid_df['new_tests'][240]
57640.0
```

Pandas fournit également la méthode `.at` pour récupérer l'élément à une ligne et une colonne spécifiques directement.

```py
covid_df.at[246, 'new_cases']
# 975.0

covid_df.at[240, 'new_tests']
# 57640.0
```

Au lieu d'utiliser la notation d'indexation `[]`, Pandas permet également d'accéder aux colonnes comme propriétés du dataframe en utilisant la notation `.`. Cependant, cette méthode ne fonctionne que pour les colonnes dont les noms ne contiennent pas d'espaces ou de caractères spéciaux.

```py
covid_df.new_cases
# 0         0.0
# 1         0.0
# 2         0.0
# 3         0.0
# 4         0.0
#         ...  
# 243    1444.0
# 244    1365.0
# 245     996.0
# 246     975.0
# 247    1326.0
# Name: new_cases, Length: 248, dtype: float64
```

De plus, vous pouvez également passer une liste de colonnes dans la notation d'indexation `[]` pour accéder à un sous-ensemble du dataframe avec uniquement les colonnes données.

```py
cases_df = covid_df[['date', 'new_cases']]
cases_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-111.png)

Le nouveau dataframe `cases_df` est simplement une "vue" du dataframe original `covid_df`. Les deux pointent vers les mêmes données dans la mémoire de l'ordinateur. Changer une valeur à l'intérieur de l'un d'eux changera également les valeurs respectives dans l'autre. 

Le partage de données entre les dataframes rend la manipulation de données dans Pandas extrêmement rapide. Vous n'avez pas à vous soucier de la surcharge de copie de milliers ou de millions de lignes chaque fois que vous souhaitez créer un nouveau dataframe en opérant sur un existant.

Parfois, vous pourriez avoir besoin d'une copie complète du dataframe, auquel cas vous pouvez utiliser la méthode `copy`.

```py
covid_df_copy = covid_df.copy()
```

Les données dans `covid_df_copy` sont complètement séparées de `covid_df`, et changer les valeurs à l'intérieur de l'un d'eux n'affectera pas l'autre.

Pour accéder à une ligne spécifique de données, Pandas fournit la méthode `.loc`.

```py
covid_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-112.png)

```py
covid_df.loc[243]
# date          2020-08-30
# new_cases         1444.0
# new_deaths           1.0
# new_tests        53541.0
# Name: 243, dtype: object
```

Chaque ligne récupérée est également un objet `Series`.

```py
type(covid_df.loc[243])
# pandas.core.series.Series
```

Nous pouvons utiliser les méthodes `.head` et `.tail` pour afficher les premières ou dernières lignes de données.

```py
covid_df.head(5)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-113.png)

```py
covid_df.tail(4)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-114.png)

Remarquez ci-dessus que tandis que les premières valeurs dans les colonnes `new_cases` et `new_deaths` sont `0`, les valeurs correspondantes dans la colonne `new_tests` sont `NaN`. Cela est dû au fait que le fichier CSV ne contient aucune donnée pour la colonne `new_tests` pour des dates spécifiques (vous pouvez vérifier cela en regardant dans le fichier). Ces valeurs peuvent être manquantes ou inconnues.

```py
covid_df.at[0, 'new_tests']
# nan

type(covid_df.at[0, 'new_tests'])
# numpy.float64
```

La distinction entre `0` et `NaN` est subtile mais importante. Dans cet ensemble de données, cela représente le fait que les nombres de tests quotidiens n'ont pas été signalés à des dates spécifiques. L'Italie a commencé à signaler les tests quotidiens le 19 avril 2020. Ils avaient déjà effectué 935 310 tests avant le 19 avril.

Nous pouvons trouver le premier index qui ne contient pas de valeur `NaN` en utilisant la méthode `first_valid_index` d'une colonne.

```py
covid_df.new_tests.first_valid_index()
# 111
```

Regardons quelques lignes avant et après cet index pour vérifier que les valeurs passent de `NaN` à des nombres réels. Nous pouvons faire cela en passant une plage à `loc`.

```py
covid_df.loc[108:113]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-115.png)

Nous pouvons utiliser la méthode `.sample` pour récupérer un échantillon aléatoire de lignes du dataframe.

```py
covid_df.sample(10)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-116.png)

Remarquez que même si nous avons pris un échantillon aléatoire, l'index original de chaque ligne est préservé. C'est une propriété utile des dataframes.

Voici un résumé des fonctions et méthodes que nous avons examinées dans cette section :

* `covid_df['new_cases']` – Récupération des colonnes sous forme de `Series` en utilisant le nom de la colonne
* `new_cases[243]` – Récupération des valeurs d'une `Series` en utilisant un index
* `covid_df.at[243, 'new_cases']` – Récupération d'une seule valeur d'un dataframe
* `covid_df.copy()` – Création d'une copie profonde d'un dataframe
* `covid_df.loc[243]` - Récupération d'une ligne ou d'une plage de lignes de données du dataframe
* `head`, `tail`, et `sample` – Récupération de plusieurs lignes de données du dataframe
* `covid_df.new_tests.first_valid_index` – Trouver le premier index non vide dans une série

### Comment analyser les données des Data Frames dans Pandas

Essayons de répondre à quelques questions sur nos données.

**Q : Quel est le nombre total de cas et de décès signalés liés au Covid-19 en Italie ?**

Similaire aux tableaux Numpy, une série Pandas supporte la méthode `sum` pour répondre à ces questions.

```py
total_cas = covid_df.new_cases.sum()
total_deces = covid_df.new_deaths.sum()

print('Le nombre de cas signalés est {} et le nombre de décès signalés est {}.'.format(int(total_cas), int(total_deces)))
# Le nombre de cas signalés est 271515 et le nombre de décès signalés est 35497.
```

**Q : Quel est le taux de mortalité global (ratio des décès signalés aux cas signalés) ?**

```py
taux_mortalite = covid_df.new_deaths.sum() / covid_df.new_cases.sum()

print("Le taux de mortalité signalé global en Italie est de {:.2f} %.".format(taux_mortalite*100))
# Le taux de mortalité signalé global en Italie est de 13.07 %.
```

**Q : Quel est le nombre total de tests effectués ? Un total de 935 310 tests ont été effectués avant que les nombres de tests quotidiens ne soient signalés.**

```py
tests_initiaux = 935310
total_tests = tests_initiaux + covid_df.new_tests.sum()

total_tests
# 5214766.0
```

**Q : Quelle fraction de tests a donné un résultat positif ?**

```py
taux_positifs = total_cas / total_tests

print('{:.2f}% des tests en Italie ont conduit à un diagnostic positif.'.format(taux_positifs*100))
# 5.21% des tests en Italie ont conduit à un diagnostic positif.
```

Essayez de poser et de répondre à quelques questions supplémentaires sur les données.

### Comment interroger et trier les lignes dans Pandas

Supposons que nous voulons seulement regarder les jours où il y a eu plus de 1 000 cas signalés. Nous pouvons utiliser une expression booléenne pour vérifier quelles lignes satisfont ce critère.

```py
hauts_nouveaux_cas = covid_df.new_cases > 1000

hauts_nouveaux_cas
# 0      False
# 1      False
# 2      False
# 3      False
# 4      False
#        ...  
# 243     True
# 244     True
# 245    False
# 246    False
# 247     True
# Name: new_cases, Length: 248, dtype: bool
```

L'expression booléenne retourne une série contenant des valeurs booléennes `True` et `False`. Vous pouvez utiliser cette série pour sélectionner un sous-ensemble de lignes à partir du dataframe original, correspondant aux valeurs `True` dans la série.

```py
covid_df[hauts_nouveaux_cas]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-117.png)

Le dataframe contient 72 lignes, mais seules les cinq premières et dernières lignes sont affichées par défaut avec Jupyter pour plus de concision. Nous pouvons modifier certaines options d'affichage pour voir toutes les lignes.

```py
hauts_cas_df = covid_df[covid_df.new_cases > 1000]

hauts_cas_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-118.png)

Le dataframe contient 72 lignes, mais seules les cinq premières et dernières lignes sont affichées par défaut avec Jupyter pour plus de concision. Nous pouvons modifier certaines options d'affichage pour voir toutes les lignes.

```py
from IPython.display import display
with pd.option_context('display.max_rows', 100):
    display(covid_df[covid_df.new_cases > 1000])
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-119.png)
_Ceci n'est qu'une partie du dataframe. Consultez le reste [ici](https://jovian.ai/embed?url=https://jovian.ai/aakashns/python-pandas-data-analysis)._

Nous pouvons également formuler des requêtes plus complexes impliquant plusieurs colonnes. Par exemple, essayons de déterminer les jours où le ratio des cas signalés aux tests effectués est supérieur au `taux_positifs` global.

```py
taux_positifs
# 0.05206657403227681

haut_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > taux_positifs]

haut_ratio_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-120.png)

Le résultat de l'exécution d'une opération sur deux colonnes est une nouvelle série.

```py
covid_df.new_cases / covid_df.new_tests
# 0           NaN
# 1           NaN
# 2           NaN
# 3           NaN
# 4           NaN
#          ...   
# 243    0.026970
# 244    0.032055
# 245    0.018311
# 246         NaN
# 247         NaN
# Length: 248, dtype: float64
```

Nous pouvons utiliser cette série pour ajouter une nouvelle colonne au dataframe.

```py
covid_df['taux_positifs'] = covid_df.new_cases / covid_df.new_tests

covid_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-121.png)

Cependant, gardez à l'esprit qu'il faut parfois quelques jours pour obtenir les résultats d'un test, donc nous ne pouvons pas comparer le nombre de nouveaux cas avec le nombre de tests effectués le même jour. Toute inférence basée sur cette colonne `taux_positifs` est susceptible d'être incorrecte. 

Il est essentiel de surveiller ces relations subtiles qui ne sont souvent pas transmises dans le fichier CSV et nécessitent un contexte externe. Il est toujours bon de lire la documentation fournie avec l'ensemble de données ou de demander plus d'informations.

Pour l'instant, supprimons la colonne `taux_positifs` en utilisant la méthode `drop`.

```py
covid_df.drop(columns=['taux_positifs'], inplace=True)
```

Pouvez-vous comprendre le but de l'argument `inplace` ?

#### **Comment trier les lignes en utilisant les valeurs des colonnes dans Pandas**

Vous pouvez également trier les lignes par une colonne spécifique en utilisant `.sort_values`. Triage pour identifier les jours avec le plus grand nombre de cas, puis enchaînement avec la méthode `head` pour lister seulement les dix premiers résultats.

```py
covid_df.sort_values('new_cases', ascending=False).head(10)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-122.png)

Il semble que les deux dernières semaines de mars aient eu le plus grand nombre de cas quotidiens. Comparons cela aux jours où le plus grand nombre de décès ont été enregistrés.

```py
covid_df.sort_values('new_deaths', ascending=False).head(10)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-123.png)

Il semble que les décès quotidiens aient atteint un pic environ une semaine après le pic des nouveaux cas quotidiens.

Regardons également les jours avec le plus petit nombre de cas. Nous pourrions nous attendre à voir les premiers jours de l'année sur cette liste.

```py
covid_df.sort_values('new_cases').head(10)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-124.png)

Il semble que le nombre de nouveaux cas le 20 juin 2020 était de `-148`, un nombre négatif ! Pas quelque chose que nous aurions attendu, mais c'est la nature des données du monde réel. Cela pourrait être une erreur de saisie de données, ou le gouvernement a peut-être émis une correction pour tenir compte d'une erreur de comptage dans le passé. 

Pouvez-vous fouiller dans les articles de presse en ligne et découvrir pourquoi le nombre était négatif ?

Regardons quelques jours avant et après le 20 juin 2020.

```py
covid_df.loc[169:175]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-125.png)

Pour l'instant, supposons que c'était effectivement une erreur de saisie de données. Nous pouvons utiliser l'une des approches suivantes pour traiter la valeur manquante ou défectueuse :

1. La remplacer par `0`.
2. La remplacer par la moyenne de l'ensemble de la colonne
3. La remplacer par la moyenne des valeurs des dates précédente et suivante
4. Supprimer entièrement la ligne

L'approche que vous choisissez nécessite un certain contexte sur les données et le problème. Dans ce cas, puisque nous traitons des données ordonnées par date, nous pouvons procéder avec la troisième approche.

Vous pouvez utiliser la méthode `.at` pour modifier une valeur spécifique au sein du dataframe.

```py
covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases'])/2
```

Voici un résumé des fonctions et méthodes que nous avons examinées dans cette section :

* `covid_df.new_cases.sum()` – Calcul de la somme des valeurs dans une colonne ou une série
* `covid_df[covid_df.new_cases > 1000]` – Interrogation d'un sous-ensemble de lignes satisfaisant les critères choisis en utilisant des expressions booléennes
* `df['pos_rate'] = df.new_cases/df.new_tests` – Ajout de nouvelles colonnes en combinant des données de colonnes existantes
* `covid_df.drop('positive_rate')` – Suppression d'une ou plusieurs colonnes du dataframe
* `sort_values` – Tri des lignes d'un dataframe en utilisant les valeurs des colonnes
* `covid_df.at[172, 'new_cases'] = ...` – Remplacement d'une valeur au sein du dataframe

### Comment travailler avec les dates dans Pandas

Alors que nous avons examiné les chiffres globaux pour les cas, les tests, le taux de positivité, et plus encore, il serait également utile d'étudier ces chiffres sur une base mensuelle. 

La colonne `date` pourrait être utile ici, car Pandas fournit de nombreuses utilités pour travailler avec les dates.

```py
covid_df.date
# 0      2019-12-31
# 1      2020-01-01
# 2      2020-01-02
# 3      2020-01-03
# 4      2020-01-04
#           ...    
# 243    2020-08-30
# 244    2020-08-31
# 245    2020-09-01
# 246    2020-09-02
# 247    2020-09-03
# Name: date, Length: 248, dtype: object
```

Le type de données de la date est actuellement `object`, donc Pandas ne sait pas que cette colonne est une date. Nous pouvons la convertir en une colonne `datetime` en utilisant la méthode `pd.to_datetime`.

```py
covid_df['date'] = pd.to_datetime(covid_df.date)

covid_df['date']
# 0     2019-12-31
# 1     2020-01-01
# 2     2020-01-02
# 3     2020-01-03
# 4     2020-01-04
#          ...    
# 243   2020-08-30
# 244   2020-08-31
# 245   2020-09-01
# 246   2020-09-02
# 247   2020-09-03
# Name: date, Length: 248, dtype: datetime64[ns]
```

Vous pouvez voir qu'elle a maintenant le type de données `datetime64`. Nous pouvons maintenant extraire différentes parties des données dans des colonnes séparées, en utilisant la classe `DatetimeIndex` ([voir la documentation](https://jovian.ai/outlink?url=https%3A%2F%2Fpandas.pydata.org%2Fpandas-docs%2Fversion%2F0.23.4%2Fgenerated%2Fpandas.DatetimeIndex.html)).

```py
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

covid_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-126.png)

Vérifions les métriques globales pour le mois de mai. Nous pouvons interroger les lignes pour mai, choisir un sous-ensemble de colonnes et utiliser la méthode `sum` pour agréger les valeurs de chaque colonne sélectionnée.

```py
# Interroger les lignes pour mai
covid_df_may = covid_df[covid_df.month == 5]

# Extraire le sous-ensemble de colonnes à agréger
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]

# Obtenir la somme par colonne
covid_may_totals = covid_df_may_metrics.sum()

covid_may_totals
# new_cases       29073.0
# new_deaths       5658.0
# new_tests     1078720.0
# dtype: float64

type(covid_may_totals)
# pandas.core.series.Series
```

Nous pouvons également combiner les opérations ci-dessus en une seule instruction.

```py
covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()
# new_cases       29073.0
# new_deaths       5658.0
# new_tests     1078720.0
# dtype: float64
```

Comme autre exemple, vérifions si le nombre de cas signalés le dimanche est plus élevé que le nombre moyen de cas signalés chaque jour. Cette fois, nous pourrions vouloir agréger les colonnes en utilisant la méthode `.mean`.

```py
# Moyenne globale
covid_df.new_cases.mean()

# 1096.6149193548388

# Moyenne pour les dimanches
covid_df[covid_df.weekday == 6].new_cases.mean()

# 1247.2571428571428
```

Il semble que plus de cas aient été signalés le dimanche par rapport aux autres jours.

Essayez de poser et de répondre à quelques questions supplémentaires liées aux dates sur les données.

### Comment regrouper et agréger des données dans Pandas

Ensuite, nous pourrions vouloir résumer les données jour par jour et créer un nouveau dataframe avec des données mois par mois. Nous pouvons utiliser la fonction `groupby` pour créer un groupe pour chaque mois, sélectionner les colonnes que nous souhaitons agréger, et les agréger en utilisant la méthode `sum`.

```py
covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()

covid_month_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-127.png)

Le résultat est un nouveau dataframe qui utilise les valeurs uniques de la colonne passée à `groupby` comme index. Le regroupement et l'agrégation sont une méthode puissante pour résumer progressivement les données dans des dataframes plus petits.

Au lieu d'agréger par somme, vous pouvez également agréger par d'autres mesures comme la moyenne. Calculons le nombre moyen de nouveaux cas quotidiens, de décès et de tests pour chaque mois.

```py
covid_month_mean_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()

covid_month_mean_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-128.png)

Outre le regroupement, une autre forme d'agrégation est la somme cumulative ou cumulative des cas, des tests ou des décès jusqu'à la date de chaque ligne. Nous pouvons utiliser la méthode `cumsum` pour calculer la somme cumulative d'une colonne en tant que nouvelle série. 

Ajoutons trois nouvelles colonnes : `total_cases`, `total_deaths` et `total_tests`.

```py
covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests
```

Nous avons également inclus le nombre initial de tests dans `total_test` pour tenir compte des tests effectués avant le début du rapport quotidien.

```py
covid_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-129.png)

Remarquez comment les valeurs `NaN` dans la colonne `total_tests` restent inchangées.

### Comment fusionner des données de plusieurs sources dans Pandas

Pour déterminer d'autres métriques comme les tests par million, les cas par million, et ainsi de suite, nous avons besoin de plus d'informations sur le pays, notamment sa population. 

Téléchargeons un autre fichier `locations.csv` qui contient des informations liées à la santé pour de nombreux pays, y compris l'Italie.

```py
urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 'locations.csv')

locations_df = pd.read_csv('locations.csv')
locations_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-130.png)

```py
locations_df[locations_df.location == "Italy"]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-131.png)

Nous pouvons fusionner ces données dans notre dataframe existant en ajoutant plus de colonnes. Cependant, pour fusionner deux dataframes, nous avons besoin d'au moins une colonne commune. Ajoutons une colonne `location` dans le dataframe `covid_df` avec toutes les valeurs définies sur `"Italy"`.

```py
covid_df['location'] = "Italy"

covid_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-132.png)

Nous pouvons maintenant ajouter les colonnes de `locations_df` dans `covid_df` en utilisant la méthode `.merge`.

```py
merged_df = covid_df.merge(locations_df, on="location")

merged_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-133.png)
_Consultez le dataframe complet [ici](https://jovian.ai/embed?url=https://jovian.ai/aakashns/python-pandas-data-analysis)._

Les données de localisation pour l'Italie sont ajoutées à chaque ligne dans `covid_df`. Si le dataframe `covid_df` contenait des données pour plusieurs emplacements, alors les données de localisation du pays respectif seraient ajoutées pour chaque ligne.

Nous pouvons maintenant calculer des métriques comme les cas par million, les décès par million et les tests par million.

```py
merged_df['cases_per_million'] = merged_df.total_cases * 1e6 / merged_df.population
merged_df['deaths_per_million'] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df['tests_per_million'] = merged_df.total_tests * 1e6 / merged_df.population

merged_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-134.png)
_Consultez le dataframe complet [ici](https://jovian.ai/embed?url=https://jovian.ai/aakashns/python-pandas-data-analysis)._

### Comment écrire des données dans des fichiers dans Pandas

Après avoir terminé votre analyse et ajouté de nouvelles colonnes, vous devez écrire les résultats dans un fichier. Sinon, les données seront perdues lorsque le notebook Jupyter s'arrêtera. 

Avant d'écrire dans un fichier, créons d'abord un dataframe contenant uniquement les colonnes que nous souhaitons enregistrer.

```py
result_df = merged_df[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_tests', 
                       'cases_per_million', 
                       'deaths_per_million', 
                       'tests_per_million']]
                       
result_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-135.png)

Pour écrire les données du dataframe dans un fichier, nous pouvons utiliser la fonction `to_csv`.

```py
result_df.to_csv('results.csv', index=None)
```

La fonction `to_csv` inclut également une colonne supplémentaire pour stocker l'index du dataframe par défaut. Nous passons `index=None` pour désactiver ce comportement. Vous pouvez maintenant vérifier que le fichier `results.csv` est créé et contient les données du dataframe au format CSV :

```py
date,new_cases,total_cases,new_deaths,total_deaths,new_tests,total_tests,cases_per_million,deaths_per_million,tests_per_million
2020-02-27,78.0,400.0,1.0,12.0,,,6.61574439992122,0.1984723319976366,
2020-02-28,250.0,650.0,5.0,17.0,,,10.750584649871982,0.28116913699665186,
2020-02-29,238.0,888.0,4.0,21.0,,,14.686952567825108,0.34732658099586405,
2020-03-01,240.0,1128.0,8.0,29.0,,,18.656399207777838,0.47964146899428844,
2020-03-02,561.0,1689.0,6.0,35.0,,,27.93498072866735,0.5788776349931067,
2020-03-03,347.0,2036.0,17.0,52.0,,,33.67413899559901,0.8600467719897585,
...
```

### Bonus : Tracé de base avec Pandas

Nous utilisons généralement une bibliothèque comme `matplotlib` ou `seaborn` pour tracer des graphiques dans un notebook Jupyter. Cependant, les dataframes et séries Pandas fournissent une méthode pratique `.plot` pour un traçage rapide et facile.

Traçons un graphique en ligne montrant comment le nombre de cas quotidiens varie au fil du temps.

```py
result_df.new_cases.plot();
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-137.png)

Bien que ce graphique montre la tendance générale, il est difficile de dire où le pic s'est produit, car il n'y a pas de dates sur l'axe des X. Nous pouvons utiliser la colonne `date` comme index pour le dataframe pour résoudre ce problème.

```py
result_df.set_index('date', inplace=True)

result_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-138.png)

Remarquez que l'index d'un dataframe n'a pas besoin d'être numérique. Utiliser la date comme index nous permet également d'obtenir les données pour une date spécifique en utilisant `.loc`.

```py
result_df.loc['2020-09-01']
# new_cases             9.960000e+02
# total_cases           2.696595e+05
# new_deaths            6.000000e+00
# total_deaths          3.548300e+04
# new_tests             5.439500e+04
# total_tests           5.214766e+06
# cases_per_million     4.459996e+03
# deaths_per_million    5.868661e+02
# tests_per_million     8.624890e+04
# Name: 2020-09-01 00:00:00, dtype: float64
```

Traçons les nouveaux cas et les nouveaux décès par jour sous forme de graphiques en ligne.

```py
result_df.new_cases.plot()
result_df.new_deaths.plot();
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-139.png)

Nous pouvons également comparer les cas totaux par rapport aux décès totaux.

```py
result_df.total_cases.plot()
result_df.total_deaths.plot();
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-140.png)

Voyons comment le taux de mortalité et les taux de tests positifs varient au fil du temps.

```py
taux_mortalite = result_df.total_deaths / result_df.total_cases

taux_mortalite.plot(title='Taux de Mortalité');
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-141.png)

```py
taux_positifs = result_df.total_cases / result_df.total_tests

taux_positifs.plot(title='Taux Positif');
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-142.png)

Enfin, traçons quelques données mensuelles en utilisant un graphique à barres pour visualiser la tendance à un niveau plus élevé.

```py
covid_month_df.new_cases.plot(kind='bar');
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-143.png)

```py
covid_month_df.new_tests.plot(kind='bar')
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-144.png)

### Exercices Pandas

Essayez les exercices suivants pour vous familiariser avec les dataframes Pandas et pratiquer vos compétences :

* [Devoir sur les dataframes Pandas](https://jovian.ml/aakashns/pandas-practice-assignment)
* [Exercices supplémentaires sur Pandas](https://github.com/guipsamora/pandas_exercises)
* [Essayez de télécharger et d'analyser certaines données de Kaggle](https://www.kaggle.com/datasets)

### Résumé et lectures complémentaires

Nous avons couvert les sujets suivants dans ce tutoriel :

* Comment lire un fichier CSV dans un dataframe Pandas
* Comment récupérer des données à partir de dataframes Pandas
* Comment interroger, trier et analyser des données
* Comment fusionner, regrouper et agréger des données
* Comment extraire des informations utiles à partir de dates
* Tracé de base en utilisant des graphiques en ligne et en barre
* Comment écrire des dataframes dans des fichiers CSV

Consultez les ressources suivantes pour en savoir plus sur Pandas :

* [Guide de l'utilisateur pour Pandas](https://pandas.pydata.org/docs/user_guide/index.html)
* [Python pour l'analyse de données (livre de Wes McKinney - créateur de Pandas)](https://www.oreilly.com/library/view/python-for-data/9781491957653/)

### Questions de révision pour vérifier votre compréhension

Essayez de répondre aux questions suivantes pour tester votre compréhension des sujets couverts dans ce notebook :

1. Qu'est-ce que Pandas ? Qu'est-ce qui le rend utile ?
2. Comment installez-vous la bibliothèque Pandas ?
3. Comment importez-vous le module `pandas` ?
4. Quel est l'alias courant utilisé lors de l'importation du module `pandas` ?
5. Comment lisez-vous un fichier CSV en utilisant Pandas ? Donnez un exemple.
6. Quels sont les autres formats de fichiers que vous pouvez lire en utilisant Pandas ? Illustrez avec des exemples.
7. Qu'est-ce que les dataframes Pandas ?
8. Comment les dataframes Pandas diffèrent-ils des tableaux Numpy ?
9. Comment trouvez-vous le nombre de lignes et de colonnes dans un dataframe ?
10. Comment obtenez-vous la liste des colonnes dans un dataframe ?
11. Quel est le but de la méthode `describe` d'un dataframe ?
12. Comment les méthodes `info` et `describe` des dataframes sont-elles différentes ?
13. Un dataframe Pandas est-il conceptuellement similaire à une liste de dictionnaires ou à un dictionnaire de listes ? Expliquez avec un exemple.
14. Qu'est-ce qu'une `Series` Pandas ? Comment est-elle différente d'un tableau Numpy ?
15. Comment accédez-vous à une colonne d'un dataframe ?
16. Comment accédez-vous à une ligne d'un dataframe ?
17. Comment accédez-vous à un élément à une ligne et une colonne spécifiques d'un dataframe ?
18. Comment créez-vous un sous-ensemble d'un dataframe avec un ensemble spécifique de colonnes ?
19. Comment créez-vous un sous-ensemble d'un dataframe avec une plage spécifique de lignes ?
20. Le fait de changer une valeur dans un dataframe affecte-t-il les autres dataframes créés en utilisant un sous-ensemble des lignes ou des colonnes ? Pourquoi en est-il ainsi ?
21. Comment créez-vous une copie d'un dataframe ?
22. Pourquoi devriez-vous éviter de créer trop de copies d'un dataframe ?
23. Comment affichez-vous les premières lignes d'un dataframe ?
24. Comment affichez-vous les dernières lignes d'un dataframe ?
25. Comment affichez-vous une sélection aléatoire de lignes d'un dataframe ?
26. Qu'est-ce que l'"index" dans un dataframe ? Comment est-il utile ?
27. Que représente une valeur `NaN` dans un dataframe Pandas ?
28. En quoi `Nan` est-il différent de `0` ?
29. Comment identifiez-vous la première ligne non vide dans une série ou une colonne Pandas ?
30. Quelle est la différence entre `df.loc` et `df.at` ?
31. Où pouvez-vous trouver une liste complète des méthodes supportées par les objets Pandas `DataFrame` et `Series` ?
32. Comment trouvez-vous la somme des nombres dans une colonne d'un dataframe ?
33. Comment trouvez-vous la moyenne des nombres dans une colonne d'un dataframe ?
34. Comment trouvez-vous le nombre de nombres non vides dans une colonne d'un dataframe ?
35. Quel est le résultat obtenu en utilisant une colonne Pandas dans une expression booléenne ? Illustrez avec un exemple.
36. Comment sélectionnez-vous un sous-ensemble de lignes où la valeur d'une colonne spécifique répond à une condition donnée ? Illustrez avec un exemple.
37. Quel est le résultat de l'expression `df[df.new_cases > 100]` ?
38. Comment affichez-vous toutes les lignes d'un dataframe pandas dans une sortie de cellule Jupyter ?
39. Quel est le résultat obtenu lorsque vous effectuez une opération arithmétique entre deux colonnes d'un dataframe ? Illustrez avec un exemple.
40. Comment ajoutez-vous une nouvelle colonne à un dataframe en combinant des valeurs de deux colonnes existantes ? Illustrez avec un exemple.
41. Comment supprimez-vous une colonne d'un dataframe ? Illustrez avec un exemple.
42. Quel est le but de l'argument `inplace` dans les méthodes de dataframe ?
43. Comment triez-vous les lignes d'un dataframe en fonction des valeurs dans une colonne particulière ?
44. Comment triez-vous un dataframe pandas en utilisant des valeurs de plusieurs colonnes ?
45. Comment spécifiez-vous si vous souhaitez trier par ordre croissant ou décroissant lors du tri d'un dataframe Pandas ?
46. Comment changez-vous une valeur spécifique au sein d'un dataframe ?
47. Comment convertissez-vous une colonne de dataframe en type de données `datetime` ?
48. Quels sont les avantages de l'utilisation du type de données `datetime` au lieu de `object` ?
49. Comment extrayez-vous différentes parties d'une colonne de date comme le mois, l'année, le mois, le jour de la semaine, et ainsi de suite dans des colonnes séparées ? Illustrez avec un exemple.
50. Comment agrégez-vous plusieurs colonnes d'un dataframe ensemble ?
51. Quel est le but de la méthode `groupby` d'un dataframe ? Illustrez avec un exemple.
52. Quelles sont les différentes manières dont vous pouvez agréger les groupes créés par `groupby` ?
53. Que signifie une somme cumulative ou cumulative ?
54. Comment créez-vous une nouvelle colonne contenant la somme cumulative ou cumulative d'une autre colonne ?
55. Quelles sont les autres mesures cumulatives supportées par les dataframes Pandas ?
56. Que signifie fusionner deux dataframes ? Donnez un exemple.
57. Comment spécifiez-vous les colonnes qui doivent être utilisées pour fusionner deux dataframes ?
58. Comment écrivez-vous des données d'un dataframe Pandas dans un fichier CSV ? Donnez un exemple.
59. Quels sont les autres formats de fichiers dans lesquels vous pouvez écrire à partir d'un dataframe Pandas ? Illustrez avec des exemples.
60. Comment créez-vous un graphique en ligne montrant les valeurs au sein d'une colonne d'un dataframe ?
61. Comment convertissez-vous une colonne d'un dataframe en son index ?
62. L'index d'un dataframe peut-il être non numérique ?
63. Quels sont les avantages de l'utilisation d'un dataframe non numérique ? Illustrez avec un exemple.
64. Comment créez-vous un graphique à barres montrant les valeurs au sein d'une colonne d'un dataframe ?
65. Quels sont les autres types de graphiques supportés par les dataframes et séries Pandas ?

Vous êtes prêt à passer à la section suivante du tutoriel.

## Visualisation de données en utilisant Python, Matplotlib et Seaborn

![Image](https://i.imgur.com/9i806Rh.png)

Lien vers le notebook : [https://jovian.ai/aakashns/python-matplotlib-data-visualization](https://jovian.ai/aakashns/python-matplotlib-data-visualization)

La visualisation de données est la représentation graphique des données. Elle implique la production d'images qui communiquent les relations entre les données représentées aux spectateurs. 

La visualisation des données est une partie essentielle de l'analyse des données et de l'apprentissage automatique. Nous utiliserons les bibliothèques Python [Matplotlib](https://jovian.ai/outlink?url=https%3A%2F%2Fmatplotlib.org) et [Seaborn](https://jovian.ai/outlink?url=https%3A%2F%2Fseaborn.pydata.org) pour apprendre et appliquer certaines techniques populaires de visualisation de données. Nous utiliserons les mots _graphique_, _tracé_ et _courbe_ de manière interchangeable dans ce tutoriel.

Pour commencer, installons et importons les bibliothèques. Nous utiliserons le module `matplotlib.pyplot` pour les graphiques de base comme les graphiques en ligne et en barre. Il est souvent importé avec l'alias `plt`. Nous utiliserons le module `seaborn` pour des graphiques plus avancés. Il est couramment importé avec l'alias `sns`.

```py
!pip install matplotlib seaborn --upgrade --quiet

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
```

Remarquez que nous incluons également la commande spéciale `%matplotlib inline` pour nous assurer que nos graphiques sont affichés et intégrés dans le notebook Jupyter lui-même. Sans cette commande, parfois les graphiques peuvent apparaître dans des fenêtres pop-up.

### Comment créer un graphique en ligne en Python

Le graphique en ligne est l'une des techniques de visualisation de données les plus simples et les plus largement utilisées. Un graphique en ligne affiche des informations sous forme de série de points de données ou de marqueurs connectés par des lignes droites. 

Vous pouvez personnaliser la forme, la taille, la couleur et d'autres éléments esthétiques des lignes et des marqueurs pour une meilleure clarté visuelle.

Voici une liste Python montrant le rendement des pommes (tonnes par hectare) sur six ans dans un pays imaginaire appelé Kanto.

```py
rendement_pommes = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
```

Nous pouvons visualiser comment le rendement des pommes change au fil du temps en utilisant un graphique en ligne. Pour dessiner un graphique en ligne, nous pouvons utiliser la fonction `plt.plot`.

```py
plt.plot(rendement_pommes)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-145.png)

L'appel de la fonction `plt.plot` dessine le graphique en ligne comme prévu. Il retourne également une liste des graphiques dessinés `[<matplotlib.lines.Line2D at 0x7ff70aa20760>]`, affichée dans la sortie. Nous pouvons inclure un point-virgule (`;`) à la fin de la dernière instruction dans la cellule pour éviter d'afficher la sortie et afficher uniquement le graphique.

```py
plt.plot(rendement_pommes);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-146.png)

Améliorons ce graphique étape par étape pour le rendre plus informatif et beau.

#### **Comment personnaliser l'axe des X dans MatPlotLib**

L'axe des X du graphique montre actuellement les indices des éléments de la liste de 0 à 5. Le graphique serait plus informatif si nous pouvions afficher l'année pour laquelle nous traçons les données. Nous pouvons faire cela en utilisant deux arguments `plt.plot`.

```py
annees = [2010, 2011, 2012, 2013, 2014, 2015]
rendement_pommes = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]

plt.plot(annees, rendement_pommes)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-147.png)

#### **Étiquettes des axes dans MatPlotLib**

Nous pouvons ajouter des étiquettes aux axes pour montrer ce que chaque axe représente en utilisant les méthodes `plt.xlabel` et `plt.ylabel`.

```py
plt.plot(annees, rendement_pommes)
plt.xlabel('Année')
plt.ylabel('Rendement (tonnes par hectare)');
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-148.png)

#### **Comment tracer plusieurs lignes dans MatPlotLib**

Vous pouvez invoquer la fonction `plt.plot` une fois pour chaque ligne à tracer pour tracer plusieurs lignes dans le même graphique. Comparons les rendements des pommes et des oranges à Kanto.

```py
annees = range(2000, 2012)
pommes = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]

plt.plot(annees, pommes)
plt.plot(annees, oranges)
plt.xlabel('Année')
plt.ylabel('Rendement (tonnes par hectare)');
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-149.png)

#### **Titre du graphique et légende dans MatPlotLib**

Pour différencier plusieurs lignes, nous pouvons inclure une légende dans le graphique en utilisant la fonction `plt.legend`. Nous pouvons également définir un titre pour le graphique en utilisant la fonction `plt.title`.

```py
plt.plot(annees, pommes)
plt.plot(annees, oranges)

plt.xlabel('Année')
plt.ylabel('Rendement (tonnes par hectare)')

plt.title("Rendements des cultures à Kanto")
plt.legend(['Pommes', 'Oranges']);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-150.png)

#### **Comment utiliser les marqueurs de ligne dans MatPlotLib**

Nous pouvons également montrer des marqueurs pour les points de données sur chaque ligne en utilisant l'argument `marker` de `plt.plot`. 

Matplotlib fournit de nombreux marqueurs différents comme un cercle, une croix, un carré, un losange, et plus encore. Vous pouvez trouver la liste complète des types de marqueurs ici : [https://matplotlib.org/3.1.1/api/markers_api.html](https://jovian.ai/outlink?url=https%3A%2F%2Fmatplotlib.org%2F3.1.1%2Fapi%2Fmarkers_api.html) .

```py
plt.plot(annees, pommes, marker='o')
plt.plot(annees, oranges, marker='x')

plt.xlabel('Année')
plt.ylabel('Rendement (tonnes par hectare)')

plt.title("Rendements des cultures à Kanto")
plt.legend(['Pommes', 'Oranges']);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-151.png)

#### **Comment styliser les lignes et les marqueurs dans MatPlotLib**

La fonction `plt.plot` supporte de nombreux arguments pour styliser les lignes et les marqueurs :

* `color` ou `c` – Définir la couleur de la ligne ([couleurs supportées](https://jovian.ai/outlink?url=https%3A%2F%2Fmatplotlib.org%2F3.1.0%2Fgallery%2Fcolor%2Fnamed_colors.html))
* `linestyle` ou `ls` – Choisir entre une ligne solide ou en pointillés
* `linewidth` ou `lw` – Définir la largeur d'une ligne
* `markersize` ou `ms` – Définir la taille des marqueurs
* `markeredgecolor` ou `mec` – Définir la couleur de bordure pour les marqueurs
* `markeredgewidth` ou `mew` – Définir la largeur de bordure pour les marqueurs
* `markerfacecolor` ou `mfc` – Définir la couleur de remplissage pour les marqueurs
* `alpha` – Opacité du tracé

Consultez la documentation pour `plt.plot` pour en savoir plus : [https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot](https://jovian.ai/outlink?url=https%3A%2F%2Fmatplotlib.org%2Fapi%2F_as_gen%2Fmatplotlib.pyplot.plot.html%23matplotlib.pyplot.plot) .

```py
plt.plot(annees, pommes, marker='s', c='b', ls='-', lw=2, ms=8, mew=2, mec='navy')
plt.plot(annees, oranges, marker='o', c='r', ls='--', lw=3, ms=10, alpha=.5)

plt.xlabel('Année')
plt.ylabel('Rendement (tonnes par hectare)')

plt.title("Rendements des cultures à Kanto")
plt.legend(['Pommes', 'Oranges']);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-152.png)

L'argument `fmt` fournit un raccourci pour spécifier la forme du marqueur, le style de ligne et la couleur de ligne. Vous pouvez le fournir comme troisième argument à `plt.plot`.

```py
fmt = '[marker][line][color]'

plt.plot(annees, pommes, 's-b')
plt.plot(annees, oranges, 'o--r')

plt.xlabel('Année')
plt.ylabel('Rendement (tonnes par hectare)')

plt.title("Rendements des cultures à Kanto")
plt.legend(['Pommes', 'Oranges']);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-153.png)

Vous pouvez utiliser la fonction `plt.figure` pour changer la taille de la figure.

```py
plt.plot(annees, oranges, 'or')
plt.title("Rendement des oranges (tonnes par hectare)");
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-154.png)

#### **Comment changer la taille de la figure dans MatPlotLib**

Vous pouvez utiliser la fonction `plt.figure` pour changer la taille de la figure.

```py
plt.figure(figsize=(12, 6))

plt.plot(annees, oranges, 'or')
plt.title("Rendement des oranges (tonnes par hectare)");
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-155.png)

#### **Comment améliorer les styles par défaut en utilisant Seaborn**

Une manière facile de rendre vos graphiques beaux est d'utiliser certains styles par défaut de la bibliothèque Seaborn. Vous pouvez les appliquer globalement en utilisant la fonction `sns.set_style`. Vous pouvez voir une liste complète des styles prédéfinis ici : [https://seaborn.pydata.org/generated/seaborn.set_style.html](https://jovian.ai/outlink?url=https%3A%2F%2Fseaborn.pydata.org%2Fgenerated%2Fseaborn.set_style.html) .

```py
sns.set_style("whitegrid")
plt.plot(annees, pommes, 's-b')
plt.plot(annees, oranges, 'o--r')

plt.xlabel('Année')
plt.ylabel('Rendement (tonnes par hectare)')

plt.title("Rendements des cultures à Kanto")
plt.legend(['Pommes', 'Oranges']);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-156.png)

```
sns.set_style("darkgrid")

plt.plot(annees, pommes, 's-b')
plt.plot(annees, oranges, 'o--r')

plt.xlabel('Année')
plt.ylabel('Rendement (tonnes par hectare)')

plt.title("Rendements des cultures à Kanto")
plt.legend(['Pommes', 'Oranges']);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-157.png)

```py
plt.plot(annees, oranges, 'or')
plt.title("Rendement des oranges (tonnes par hectare)");
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-158.png)

Vous pouvez également modifier les styles par défaut directement en modifiant le dictionnaire `matplotlib.rcParams`. En savoir plus : [https://matplotlib.org/3.2.1/tutorials/introductory/customizing.html#matplotlib-rcparams](https://jovian.ai/outlink?url=https%3A%2F%2Fmatplotlib.org%2F3.2.1%2Ftutorials%2Fintroductory%2Fcustomizing.html%23matplotlib-rcparams) .

```py
import matplotlib

matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
```

### Graphiques en nuage de points dans MatPlotLib

Dans un graphique en nuage de points, les valeurs de 2 variables sont tracées comme des points sur une grille à deux dimensions. De plus, vous pouvez également utiliser une troisième variable pour déterminer la taille ou la couleur des points. Essayons un exemple.

Le [jeu de données des fleurs Iris](https://jovian.ai/outlink?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FIris_flower_data_set) fournit des mesures d'échantillons de sépales et de pétales pour trois espèces de fleurs. Le jeu de données Iris est inclus avec la bibliothèque Seaborn et vous pouvez le charger sous forme de dataframe Pandas.

```py
# Charger les données dans un dataframe Pandas
flowers_df = sns.load_dataset("iris")

flowers_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-159.png)

```py
flowers_df.species.unique()
# array(['setosa', 'versicolor', 'virginica'], dtype=object)
```

Essayons de visualiser la relation entre la longueur des sépales et la largeur des sépales. Notre premier instinct pourrait être de créer un graphique en ligne en utilisant `plt.plot`.

```py
plt.plot(flowers_df.sepal_length, flowers_df.sepal_width);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-160.png)

La sortie n'est pas très informative car il y a trop de combinaisons des deux propriétés dans le jeu de données. Il ne semble pas y avoir de relation simple entre elles.

Nous pouvons utiliser un graphique en nuage de points pour visualiser comment la longueur des sépales et la largeur des sépales varient en utilisant la fonction `scatterplot` du module `seaborn` (importé sous `sns`).

```py
sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-161.png)

#### **Comment ajouter des nuances dans MatPlotLib**

Remarquez comment les points dans le graphique ci-dessus semblent former des groupes distincts avec quelques valeurs aberrantes. Nous pouvons colorier les points en utilisant l'espèce de fleur comme `hue`. Nous pouvons également agrandir les points en utilisant l'argument `s`.

```py
sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-162.png)

L'ajout de nuances rend le graphique plus informatif. Nous pouvons immédiatement dire que les iris Setosa ont une longueur de sépale plus petite mais une largeur de sépale plus grande. En revanche, l'inverse est vrai pour les iris Virginica.

#### **Comment personnaliser les figures Seaborn**

Puisque Seaborn utilise les fonctions de traçage de Matplotlib en interne, nous pouvons utiliser des fonctions comme `plt.figure` et `plt.title` pour modifier la figure.

```py
plt.figure(figsize=(12, 6))
plt.title('Dimensions des sépales')

sns.scatterplot(x=flowers_df.sepal_length, 
                y=flowers_df.sepal_width, 
                hue=flowers_df.species,
                s=100);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-163.png)

#### **Comment tracer des données en utilisant des dataframes Pandas avec Seaborn**

Seaborn a un support intégré pour les dataframes Pandas. Au lieu de passer chaque colonne comme une série, vous pouvez fournir des noms de colonnes et utiliser l'argument `data` pour spécifier un dataframe.

```py
plt.title('Dimensions des sépales')
sns.scatterplot(x='sepal_length', 
                y='sepal_width', 
                hue='species',
                s=100,
                data=flowers_df);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-164.png)

### Histogrammes dans MatPlotLib

Un histogramme représente la distribution d'une variable en créant des bins (intervalles) le long de la plage de valeurs et en montrant des barres verticales pour indiquer le nombre d'observations dans chaque bin.

Par exemple, visualisons la distribution des valeurs de la largeur des sépales dans le jeu de données Iris. Nous pouvons utiliser la fonction `plt.hist` pour créer un histogramme.

```py
# Charger les données dans un dataframe Pandas
flowers_df = sns.load_dataset("iris")

flowers_df.sepal_width
# 0      3.5
# 1      3.0
# 2      3.2
# 3      3.1
# 4      3.6
#       ... 
# 145    3.0
# 146    2.5
# 147    3.0
# 148    3.4
# 149    3.0
# Name: sepal_width, Length: 150, dtype: float64
```

```py
plt.title("Distribution de la largeur des sépales")
plt.hist(flowers_df.sepal_width);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-165.png)

Nous pouvons immédiatement voir que les largeurs des sépales se situent dans la plage 2.0 - 4.5, et environ 35 valeurs sont dans la plage 2.9 - 3.1, qui semble être le bin le plus peuplé.

#### **Comment contrôler la taille et le nombre de bins**

Nous pouvons contrôler le nombre de bins ou la taille de chacun en utilisant l'argument bins.

```py
# Spécification du nombre de bins
plt.hist(flowers_df.sepal_width, bins=5);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-166.png)

```py
import numpy as np

# Spécification des limites de chaque bin
plt.hist(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25));
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-167.png)

```py
# Bins de tailles inégales
plt.hist(flowers_df.sepal_width, bins=[1, 3, 4, 4.5]);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-168.png)

#### **Comment gérer plusieurs histogrammes dans MatPlotLib**

Similaire aux graphiques en ligne, nous pouvons dessiner plusieurs histogrammes dans un seul graphique. Nous pouvons réduire l'opacité de chaque histogramme afin que les barres d'un histogramme ne cachent pas celles des autres.

Dessinons des histogrammes séparés pour chaque espèce de fleurs.

```py
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']

plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-169.png)

Nous pouvons également empiler plusieurs histogrammes les uns sur les autres.

```py
plt.title('Distribution de la largeur des sépales')

plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
         bins=np.arange(2, 5, 0.25), 
         stacked=True);

plt.legend(['Setosa', 'Versicolor', 'Virginica']);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-170.png)

### Graphiques à barres dans MatPlotLib

Les graphiques à barres sont assez similaires aux graphiques en ligne, c'est-à-dire qu'ils montrent une séquence de valeurs. Cependant, une barre est affichée pour chaque valeur, plutôt que des points connectés par des lignes. Nous pouvons utiliser la fonction `plt.bar` pour dessiner un graphique à barres.

```py
annees = range(2000, 2006)
pommes = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

plt.bar(annees, oranges);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-171.png)

Comme les histogrammes, nous pouvons empiler des barres les unes sur les autres. Nous utilisons l'argument `bottom` de `plt.bar` pour y parvenir.

```py
plt.bar(annees, pommes)
plt.bar(annees, oranges, bottom=pommes);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-172.png)

#### **Graphiques à barres avec des moyennes dans Seaborn**

Regardons un autre jeu de données d'exemple inclus avec Seaborn appelé `tips`. Le jeu de données contient des informations sur le sexe, l'heure de la journée, la facture totale et le montant du pourboire pour les clients visitant un restaurant sur une semaine.

```py
tips_df = sns.load_dataset("tips");

tips_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-173.png)

Nous pourrions vouloir dessiner un graphique à barres pour visualiser comment le montant moyen de la facture varie selon les différents jours de la semaine. Une façon de faire cela serait de calculer les moyennes par jour puis d'utiliser `plt.bar` (essayez-le comme exercice).

Cependant, puisque c'est un cas d'utilisation très courant, la bibliothèque Seaborn fournit une fonction `barplot` qui peut automatiquement calculer les moyennes.

```py
sns.barplot(x='day', y='total_bill', data=tips_df);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-174.png)

Les lignes coupant chaque barre représentent la quantité de variation dans les valeurs. Par exemple, il semble que la variation dans la facture totale soit relativement élevée le vendredi et faible le samedi.

Nous pouvons également spécifier un argument `hue` pour comparer les graphiques à barres côte à côte en fonction d'une troisième caractéristique, par exemple le sexe.

```py
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-175.png)

Vous pouvez rendre les barres horizontales simplement en échangeant les axes.

```py
sns.barplot(x='total_bill', y='day', hue='sex', data=tips_df);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-176.png)

### Cartes thermiques dans Seaborn

Une carte thermique est utilisée pour visualiser des données bidimensionnelles comme une matrice ou un tableau en utilisant des couleurs. La meilleure façon de la comprendre est en regardant un exemple. 

Nous allons utiliser un autre jeu de données d'exemple de Seaborn, appelé `flights`, pour visualiser le trafic mensuel de passagers dans un aéroport sur 12 ans.

```py
flights_df = sns.load_dataset("flights").pivot("month", "year", "passengers")

flights_df
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-177.png)

`flights_df` est une matrice avec une ligne pour chaque mois et une colonne pour chaque année. Les valeurs montrent le nombre de passagers (en milliers) qui ont visité l'aéroport un mois spécifique d'une année. Nous pouvons utiliser la fonction `sns.heatmap` pour visualiser le trafic à l'aéroport.

```py
plt.title("Nombre de passagers (en milliers)")
sns.heatmap(flights_df);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-178.png)

Les couleurs plus vives indiquent un trafic plus élevé à l'aéroport. En regardant le graphique, nous pouvons déduire deux choses :

* Le trafic à l'aéroport une année donnée tend à être le plus élevé autour de juillet et août.
* Le trafic à l'aéroport un mois donné tend à augmenter d'année en année.

Nous pouvons également afficher les valeurs réelles dans chaque bloc en spécifiant `annot=True` et en utilisant l'argument `cmap` pour changer la palette de couleurs.

```py
plt.title("Nombre de passagers (en milliers)")
sns.heatmap(flights_df, fmt="d", annot=True, cmap='Blues');
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-179.png)

### Images dans MatPlotLib

Nous pouvons également utiliser Matplotlib pour afficher des images. Téléchargeons une image depuis Internet.

```py
from urllib.request import urlretrieve

urlretrieve('https://i.imgur.com/SkPbq.jpg', 'chart.jpg');
```

Avant d'afficher une image, elle doit être lue en mémoire à l'aide du module `PIL`.

```py
from PIL import Image

img = Image.open('chart.jpg')
```

Une image chargée à l'aide de PIL est simplement un tableau numpy tridimensionnel contenant les intensités de pixels pour les canaux rouge, vert et bleu (RVB) de l'image. Nous pouvons convertir l'image en un tableau à l'aide de `np.array`.

```
img_array = np.array(img)

img_array.shape
# (481, 640, 3)
```

Nous pouvons afficher l'image PIL à l'aide de `plt.imshow`.

```py
plt.imshow(img);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-180.png)

Nous pouvons désactiver les axes et les lignes de grille et afficher un titre à l'aide des fonctions pertinentes.

```py
plt.grid(False)
plt.title('Un mème de science des données')
plt.axis('off')
plt.imshow(img);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-181.png)

Pour afficher une partie de l'image, nous pouvons simplement sélectionner une tranche du tableau numpy.

```py
plt.grid(False)
plt.axis('off')
plt.imshow(img_array[125:325,105:305]);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-182.png)

### Comment tracer plusieurs graphiques dans une grille dans MatPlotLib et Seaborn

Matplotlib et Seaborn supportent également le traçage de plusieurs graphiques dans une grille, en utilisant `plt.subplots`, qui retourne un ensemble d'axes pour le traçage.

Voici une seule grille montrant les différents types de graphiques que nous avons couverts dans ce tutoriel.

```py
fig, axes = plt.subplots(2, 3, figsize=(16, 8))

# Utiliser les axes pour le traçage
axes[0,0].plot(annees, pommes, 's-b')
axes[0,0].plot(annees, oranges, 'o--r')
axes[0,0].set_xlabel('Année')
axes[0,0].set_ylabel('Rendement (tonnes par hectare)')
axes[0,0].legend(['Pommes', 'Oranges']);
axes[0,0].set_title('Rendements des cultures à Kanto')


# Passer les axes dans seaborn
axes[0,1].set_title('Longueur des sépales vs. Largeur des sépales')
sns.scatterplot(x=flowers_df.sepal_length, 
                y=flowers_df.sepal_width, 
                hue=flowers_df.species, 
                s=100, 
                ax=axes[0,1]);

# Utiliser les axes pour le traçage
axes[0,2].set_title('Distribution de la largeur des sépales')
axes[0,2].hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
         bins=np.arange(2, 5, 0.25), 
         stacked=True);

axes[0,2].legend(['Setosa', 'Versicolor', 'Virginica']);

# Passer les axes dans seaborn
axes[1,0].set_title('Factures de restaurant')
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df, ax=axes[1,0]);

# Passer les axes dans seaborn
axes[1,1].set_title('Trafic aérien')
sns.heatmap(flights_df, cmap='Blues', ax=axes[1,1]);

# Tracer une image en utilisant les axes
axes[1,2].set_title('Mème de science des données')
axes[1,2].imshow(img)
axes[1,2].grid(False)
axes[1,2].set_xticks([])
axes[1,2].set_yticks([])

plt.tight_layout(pad=2);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-183.png)

Voir cette page pour une liste complète des fonctions supportées : [https://matplotlib.org/3.3.1/api/axes_api.html#the-axes-class](https://jovian.ai/outlink?url=https%3A%2F%2Fmatplotlib.org%2F3.3.1%2Fapi%2Faxes_api.html%23the-axes-class) .

#### **Graphiques par paires avec Seaborn**

Seaborn fournit également une fonction d'assistance `sns.pairplot` pour tracer automatiquement plusieurs graphiques différents pour des paires de caractéristiques au sein d'un dataframe.

```py
sns.pairplot(flowers_df, hue='species');
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-184.png)
_Voir la sortie complète [ici](https://jovian.ai/embed?url=https://jovian.ai/aakashns/python-matplotlib-data-visualization/)._

```py
sns.pairplot(tips_df, hue='sex');
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-185.png)

### Résumé et lectures complémentaires

Nous avons couvert les sujets suivants dans ce tutoriel :

* Comment créer et personnaliser des graphiques en ligne en utilisant Matplotlib
* Comment visualiser les relations entre deux variables ou plus en utilisant des graphiques en nuage de points
* Comment étudier les distributions de variables en utilisant des histogrammes et des graphiques à barres
* Comment visualiser des données bidimensionnelles en utilisant des cartes thermiques
* Comment afficher des images en utilisant `plt.imshow` de Matplotlib
* Comment tracer plusieurs graphiques Matplotlib et Seaborn dans une grille

Dans ce tutoriel, nous avons couvert certains des concepts fondamentaux et des techniques populaires pour la visualisation de données en utilisant Matplotlib et Seaborn. La visualisation de données est un domaine vaste et nous avons à peine effleuré la surface ici. Consultez ces références pour en apprendre et découvrir davantage :

* Fiche de référence sur la visualisation de données : [https://jovian.ml/aakashns/dataviz-cheatsheet](https://jovian.ai/outlink?url=https%3A%2F%2Fjovian.ml%2Faakashns%2Fdataviz-cheatsheet)
* Galerie Seaborn : [https://seaborn.pydata.org/examples/index.html](https://jovian.ai/outlink?url=https%3A%2F%2Fseaborn.pydata.org%2Fexamples%2Findex.html)
* Galerie Matplotlib : [https://matplotlib.org/3.1.1/gallery/index.html](https://jovian.ai/outlink?url=https%3A%2F%2Fmatplotlib.org%2F3.1.1%2Fgallery%2Findex.html)
* Tutoriel Matplotlib : [https://github.com/rougier/matplotlib-tutorial](https://jovian.ai/outlink?url=https%3A%2F%2Fgithub.com%2Frougier%2Fmatplotlib-tutorial)

### Questions de révision pour vérifier votre compréhension

Essayez de répondre aux questions suivantes pour tester votre compréhension des sujets couverts dans ce notebook :

1. Qu'est-ce que la visualisation de données ?
2. Qu'est-ce que Matplotlib ?
3. Qu'est-ce que Seaborn ?
4. Comment installez-vous Matplotlib et Seaborn ?
5. Comment importez-vous Matplotlib et Seaborn ? Quels sont les alias courants utilisés lors de l'importation de ces modules ?
6. Quel est le but de la commande magique `%matplotlib inline` ?
7. Qu'est-ce qu'un graphique en ligne ?
8. Comment tracez-vous un graphique en ligne en Python ? Illustrez avec un exemple.
9. Comment spécifiez-vous les valeurs pour l'axe des X d'un graphique en ligne ?
10. Comment spécifiez-vous les étiquettes pour les axes d'un graphique ?
11. Comment tracez-vous plusieurs graphiques en ligne sur les mêmes axes ?
12. Comment affichez-vous une légende pour un graphique en ligne avec plusieurs lignes ?
13. Comment définissez-vous un titre pour un graphique ?
14. Comment affichez-vous des marqueurs sur un graphique en ligne ?
15. Quelles sont les différentes options pour styliser les lignes et les marqueurs dans les graphiques en ligne ? Illustrez avec des exemples.
16. Quel est le but de l'argument `fmt` de `plt.plot` ?
17. Où pouvez-vous voir une liste de tous les arguments acceptés par `plt.plot` ?
18. Comment changez-vous la taille de la figure en utilisant Matplotlib ?
19. Comment appliquez-vous les styles par défaut de Seaborn globalement pour tous les graphiques ?
20. Quels sont les styles prédéfinis disponibles dans Seaborn ? Illustrez avec des exemples.
21. Qu'est-ce qu'un graphique en nuage de points ?
22. En quoi un graphique en nuage de points est-il différent d'un graphique en ligne ?
23. Comment dessinez-vous un graphique en nuage de points en utilisant Seaborn ? Illustrez avec un exemple.
24. Comment décidez-vous quand utiliser un graphique en nuage de points par rapport à un graphique en ligne ?
25. Comment spécifiez-vous les couleurs des points sur un graphique en nuage de points en utilisant une variable catégorielle ?
26. Comment personnalisez-vous le titre, la taille de la figure, la légende, etc. pour les graphiques Seaborn ?
27. Comment utilisez-vous un dataframe Pandas avec `sns.scatterplot` ?
28. Qu'est-ce qu'un histogramme ?
29. Quand devez-vous utiliser un histogramme par rapport à un graphique en ligne ?
30. Comment dessinez-vous un histogramme en utilisant Matplotlib ? Illustrez avec un exemple.
31. Que sont les "bins" dans un histogramme ?
32. Comment changez-vous les tailles des bins dans un histogramme ?
33. Comment changez-vous le nombre de bins dans un histogramme ?
34. Comment affichez-vous plusieurs histogrammes sur les mêmes axes ?
35. Comment empilez-vous plusieurs histogrammes les uns sur les autres ?
36. Qu'est-ce qu'un graphique à barres ?
37. Comment dessinez-vous un graphique à barres en utilisant Matplotlib ? Illustrez avec un exemple.
38. Quelle est la différence entre un graphique à barres et un histogramme ?
39. Quelle est la différence entre un graphique à barres et un graphique en ligne ?
40. Comment empilez-vous des barres les unes sur les autres ?
41. Quelle est la différence entre `plt.bar` et `sns.barplot` ?
42. Que représentent les lignes coupant les barres dans un graphique à barres Seaborn ?
43. Comment affichez-vous des graphiques à barres côte à côte ?
44. Comment dessinez-vous un graphique à barres horizontal ?
45. Qu'est-ce qu'une carte thermique ?
46. Quel type de données est le mieux visualisé avec une carte thermique ?
47. Que fait la méthode `pivot` d'un dataframe Pandas ?
48. Comment dessinez-vous une carte thermique en utilisant Seaborn ? Illustrez avec un exemple.
49. Comment changez-vous le schéma de couleurs d'une carte thermique ?
50. Comment affichez-vous les valeurs originales du jeu de données sur une carte thermique ?
51. Comment téléchargez-vous des images à partir d'une URL en Python ?
52. Comment ouvrez-vous une image pour traitement en Python ?
53. Quel est le but du module `PIL` en Python ?
54. Comment convertissez-vous une image chargée à l'aide de PIL en un tableau Numpy ?
55. Combien de dimensions a un tableau Numpy pour une image ? Que représente chaque dimension ?
56. Que sont les "canaux de couleur" dans une image ?
57. Qu'est-ce que le RVB ?
58. Comment affichez-vous une image en utilisant Matplotlib ?
59. Comment désactivez-vous les axes et les lignes de grille dans un graphique ?
60. Comment affichez-vous une portion d'une image en utilisant Matplotlib ?
61. Comment tracez-vous plusieurs graphiques dans une grille en utilisant Matplotlib et Seaborn ? Illustrez avec des exemples.
62. Quel est le but de la fonction `plt.subplots` ?
63. Que sont les graphiques par paires dans Seaborn ? Illustrez avec un exemple.
64. Comment exportez-vous un graphique dans un fichier image PNG en utilisant Matplotlib ?
65. Où pouvez-vous apprendre les différents types de graphiques que vous pouvez créer en utilisant Matplotlib et Seaborn ?

Félicitations pour être arrivé à la fin de ce tutoriel ! Vous pouvez maintenant appliquer ces compétences pour analyser des jeux de données réels provenant de sources comme [Kaggle](https://kaggle.com/datasets). 

Si vous poursuivez une carrière en science des données et en apprentissage automatique, envisagez de rejoindre le [Bootcamp Zero to Data Science de Jovian](https://zerotodatascience.com). Il s'agit d'un programme à temps partiel de 20 semaines où vous complèterez 7 cours, 12 devoirs de codage et 4 projets réels. Vous recevrez également 6 mois de soutien de carrière pour vous aider à trouver votre premier emploi en science des données.

%[https://www.jovian.ai/zero-to-data-science-bootcamp]
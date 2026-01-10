---
title: Le Guide Ultime du Package NumPy pour le Calcul Scientifique en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-06T17:18:57.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-the-numpy-scientific-computing-library-for-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/numpy.png
tags:
- name: numpy
  slug: numpy
- name: Python
  slug: python
seo_title: Le Guide Ultime du Package NumPy pour le Calcul Scientifique en Python
seo_desc: 'By Nick McCullum

  NumPy (pronounced "numb pie") is one of the most important packages to grasp when
  you’re starting to learn Python.

  The package is known for a very useful data structure called the NumPy array. NumPy
  also allows Python developers to q...'
---

Par Nick McCullum

NumPy (prononcé "numb pie") est l'un des packages les plus importants à maîtriser lorsque vous commencez à [apprendre Python](https://courses.nickmccullum.com/courses/enroll/python-for-finance/).

Ce package est connu pour une structure de données très utile appelée le tableau NumPy. NumPy permet également aux développeurs Python d'effectuer rapidement une grande variété de calculs numériques.

Ce tutoriel vous enseignera les fondamentaux de NumPy que vous pouvez utiliser pour construire des applications numériques Python dès aujourd'hui.

## **Table des Matières**

Vous pouvez sauter à une section spécifique de ce tutoriel NumPy en utilisant la table des matières ci-dessous :

* [Introduction à NumPy](#heading-introduction-a-numpy)
* [Tableaux NumPy](#heading-tableaux-numpy)
* [Méthodes et Opérations NumPy](#heading-methodes-et-operations-numpy)
* [Indexation et Affectation NumPy](#heading-indexation-et-affectation-numpy)
* [Réflexions Finales et Offre Spéciale](#heading-reflexions-finales-et-offre-speciale)

## **Introduction à NumPy**

Dans cette section, nous allons introduire la [bibliothèque NumPy](https://nickmccullum.com/advanced-python/numpy/) en Python.

### **Qu'est-ce que NumPy ?**

NumPy est une bibliothèque Python pour le calcul scientifique. NumPy signifie Numerical Python. Voici la description officielle de la bibliothèque depuis [son site web](https://numpy.org/) :

« NumPy est le package fondamental pour le calcul scientifique avec Python. Il contient entre autres :

* un objet de tableau N-dimensionnel puissant
* des fonctions sophistiquées (broadcasting)
* des outils pour intégrer du code C/C++ et Fortran
* des capacités utiles d'algèbre linéaire, de transformée de Fourier, et de nombres aléatoires

En plus de ses utilisations scientifiques évidentes, NumPy peut également être utilisé comme un conteneur multi-dimensionnel efficace de données génériques. Des types de données arbitraires peuvent être définis. Cela permet à NumPy de s'intégrer de manière transparente et rapide avec une grande variété de bases de données.

NumPy est sous licence [BSD](https://numpy.org/license.html#license), permettant une réutilisation avec peu de restrictions. »

NumPy est une bibliothèque Python si importante qu'il existe d'autres bibliothèques (y compris pandas) qui sont entièrement construites sur NumPy.

### **Le Principal Avantages de NumPy**

Le principal avantage de NumPy est qu'il permet une génération et une manipulation de données extrêmement rapides. NumPy a sa propre structure de données intégrée appelée `array` qui est similaire à la liste Python normale, mais peut stocker et manipuler des données beaucoup plus efficacement.

### **Ce Que Nous Allons Apprendre Sur NumPy**

Les praticiens avancés de Python passeront beaucoup plus de temps à travailler avec pandas qu'avec NumPy. Néanmoins, étant donné que pandas est construit sur NumPy, il est important de comprendre les aspects les plus importants de la bibliothèque NumPy.

Au cours des prochaines sections, nous aborderons les informations suivantes sur la bibliothèque NumPy :

* Tableaux NumPy
* Indexation et Affectation NumPy
* Méthodes et Opérations NumPy

### **Passons à la Suite**

Passons à l'apprentissage des tableaux NumPy, la structure de données centrale que tout praticien NumPy doit connaître.

## **Tableaux NumPy**

Dans cette section, nous allons apprendre sur les [tableaux NumPy](https://nickmccullum.com/advanced-python/numpy-arrays/).

### **Qu'est-ce que les Tableaux NumPy ?**

Les tableaux NumPy sont le principal moyen de stocker des données en utilisant la bibliothèque NumPy. Ils sont similaires aux listes normales en Python, mais ont l'avantage d'être plus rapides et d'avoir plus de méthodes intégrées.

Les tableaux NumPy sont créés en appelant la méthode `array()` de la bibliothèque NumPy. Dans la méthode, vous devez passer une liste.

Un exemple de tableau NumPy de base est montré ci-dessous. Notez que bien que j'exécute l'instruction `import numpy as np` au début de ce bloc de code, elle sera exclue des autres blocs de code de cette section pour des raisons de concision.

```
import numpy as np

sample_list = [1, 2, 3]

np.array(sample_list)

```

La dernière ligne de ce bloc de code donnera un résultat qui ressemble à ceci.

```
array([1,2,3])

```

Le wrapper `array()` indique que ce n'est plus une liste Python normale. Au lieu de cela, c'est un tableau NumPy.

### **Les Deux Différents Types de Tableaux NumPy**

Il existe deux types différents de tableaux NumPy : les vecteurs et les matrices.

Les vecteurs sont des tableaux NumPy à une dimension, et ressemblent à ceci :

```
my_vector = np.array(['this', 'is', 'a', 'vector'])

```

Les matrices sont des tableaux à deux dimensions et sont créées en passant une liste de listes dans la méthode `np.array()`. Un exemple est ci-dessous.

```
my_matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

np.array(my_matrix)

```

Vous pouvez également étendre les tableaux NumPy pour traiter des tableaux à trois, quatre, cinq, six dimensions ou plus, mais ils sont rares et largement en dehors du cadre de ce cours (après tout, il s'agit d'un cours sur la programmation Python, et non sur l'algèbre linéaire).

### **Tableaux NumPy : Méthodes Intégrées**

Les tableaux NumPy viennent avec un certain nombre de méthodes intégrées utiles. Nous allons passer le reste de cette section à discuter de ces méthodes en détail.

#### **Comment Obtenir une Plage de Nombres en Python en Utilisant NumPy**

NumPy a une méthode utile appelée `arange` qui prend deux nombres et vous donne un tableau d'entiers qui sont supérieurs ou égaux (`>=`) au premier nombre et inférieurs (`<`) au second nombre.

Un exemple de la méthode `arange` est ci-dessous.

```
np.arange(0,5)

#Retourne array([0, 1, 2, 3, 4])

```

Vous pouvez également inclure une troisième variable dans la méthode `arange` qui fournit une taille de pas pour la fonction à retourner. Passer `2` comme troisième variable retournera chaque 2ème nombre dans la plage, passer `5` comme troisième variable retournera chaque 5ème nombre dans la plage, et ainsi de suite.

Un exemple de l'utilisation de la troisième variable dans la méthode `arange` est ci-dessous.

```
np.arange(1,11,2)

#Retourne array([1, 3, 5, 7, 9])

```

### **Comment Générer des Uns et des Zéros en Python en Utilisant NumPy**

Lors de la programmation, vous aurez parfois besoin de créer des tableaux de uns ou de zéros. NumPy a des méthodes intégrées qui vous permettent de faire l'une ou l'autre de ces choses.

Nous pouvons créer des tableaux de zéros en utilisant la méthode `zeros` de NumPy. Vous passez le nombre d'entiers que vous souhaitez créer comme argument de la fonction. Un exemple est ci-dessous.

```
np.zeros(4)

#Retourne array([0, 0, 0, 0])

```

Vous pouvez également faire quelque chose de similaire en utilisant des tableaux à trois dimensions. Par exemple, `np.zeros(5, 5)` crée une matrice 5x5 qui contient tous des zéros.

Nous pouvons créer des tableaux de uns en utilisant une méthode similaire nommée `ones`. Un exemple est ci-dessous.

```
np.ones(5)

#Retourne array([1, 1, 1, 1, 1])

```

#### **Comment Diviser Équitablement une Plage de Nombres en Python en Utilisant NumPy**

Il existe de nombreuses situations dans lesquelles vous avez une plage de nombres et vous souhaitez diviser équitablement cette plage de nombres en intervalles. La méthode `linspace` de NumPy est conçue pour résoudre ce problème. `linspace` prend trois arguments :

1. Le début de l'intervalle
2. La fin de l'intervalle
3. Le nombre de sous-intervalles dans lesquels vous souhaitez que l'intervalle soit divisé

Un exemple de la méthode `linspace` est ci-dessous.

```
np.linspace(0, 1, 10)

#Retourne array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

```

#### **Comment Créer une Matrice Identité en Python en Utilisant NumPy**

Toute personne ayant étudié l'algèbre linéaire sera familière avec le concept de 'matrice identité', qui est une matrice carrée dont les valeurs diagonales sont toutes `1`. NumPy a une fonction intégrée qui prend un argument pour construire des matrices identité. La fonction est `eye`.

Des exemples sont ci-dessous :

```
np.eye(1)

#Retourne une matrice identité 1x1

np.eye(2) 

#Retourne une matrice identité 2x2

np.eye(50)

#Retourne une matrice identité 50x50

```

#### **Comment Créer des Nombres Aléatoires en Python en Utilisant NumPy**

NumPy a un certain nombre de méthodes intégrées qui vous permettent de créer des tableaux de nombres aléatoires. Chacune de ces méthodes commence par `random`. Voici quelques exemples :

```
np.random.rand(sample_size)

#Retourne un échantillon de nombres aléatoires entre 0 et 1.

#La taille de l'échantillon peut être un entier (pour un tableau à une dimension) ou deux entiers séparés par des virgules (pour un tableau à deux dimensions).

np.random.randn(sample_size)

#Retourne un échantillon de nombres aléatoires entre 0 et 1, suivant la distribution normale.

#La taille de l'échantillon peut être un entier (pour un tableau à une dimension) ou deux entiers séparés par des virgules (pour un tableau à deux dimensions).

np.random.randint(low, high, sample_size)

#Retourne un échantillon d'entiers qui sont supérieurs ou égaux à 'low' et inférieurs à 'high'

```

#### **Comment Redimensionner les Tableaux NumPy**

Il est très courant de prendre un tableau avec certaines dimensions et de transformer ce tableau en une forme différente. Par exemple, vous pourriez avoir un tableau à une dimension avec 10 éléments et vouloir le transformer en un tableau à deux dimensions de 2x5.

Un exemple est ci-dessous :

```
arr = np.array([0,1,2,3,4,5])

arr.reshape(2,3)

```

Le résultat de cette opération est :

```
array([[0, 1, 2],

       [3, 4, 5]])

```

Notez que pour utiliser la méthode `reshape`, le tableau original doit avoir le même nombre d'éléments que le tableau que vous essayez de redimensionner.

Si vous êtes curieux de connaître la forme actuelle d'un tableau NumPy, vous pouvez déterminer sa forme en utilisant l'attribut `shape` de NumPy. En utilisant notre structure de variable `arr` précédente, un exemple de la façon d'appeler l'attribut `shape` est ci-dessous :

```
arr = np.array([0,1,2,3,4,5])

arr.shape

#Retourne (6,) - notez qu'il n'y a pas de second élément puisque c'est un tableau à une dimension

arr = arr.reshape(2,3)

arr.shape

#Retourne (2,3)

```

Vous pouvez également combiner la méthode `reshape` avec l'attribut `shape` sur une seule ligne comme ceci :

```
arr.reshape(2,3).shape

#Retourne (2,3)

```

#### **Comment Trouver la Valeur Maximale et Minimale d'un Tableau NumPy**

Pour conclure cette section, apprenons quatre méthodes utiles pour identifier les valeurs maximale et minimale dans un tableau NumPy. Nous travaillerons avec ce tableau :

```
simple_array = [1, 2, 3, 4]

```

Nous pouvons utiliser la méthode `max` pour trouver la valeur maximale d'un tableau NumPy. Un exemple est ci-dessous.

```
simple_array.max()

#Retourne 4

```

Nous pouvons également utiliser la méthode `argmax` pour trouver l'index de la valeur maximale dans un tableau NumPy. Cela est utile lorsque vous souhaitez trouver l'emplacement de la valeur maximale mais que vous ne vous souciez pas nécessairement de sa valeur.

Un exemple est ci-dessous.

```
simple_array.argmax()

#Retourne 3

```

De même, nous pouvons utiliser les méthodes `min` et `argmin` pour trouver la valeur et l'index de la valeur minimale dans un tableau NumPy.

```
simple_array.min()

#Retourne 1

simple_array.argmin()

#Retourne 0

```

### **Passons à la Suite**

Dans cette section, nous avons discuté de divers attributs et méthodes des tableaux NumPy. Nous allons suivre en travaillant sur quelques problèmes pratiques de tableaux NumPy dans la section suivante.

## **Méthodes et Opérations NumPy**

Dans cette section, nous allons travailler sur [différentes opérations incluses dans la bibliothèque NumPy](https://nickmccullum.com/advanced-python/numpy-methods-operations/).

Tout au long de cette section, nous supposerons que la commande `import numpy as np` a déjà été exécutée.

### **Le Tableau Utilisé Dans Cette Section**

Pour cette section, je travaillerai avec un tableau de longueur 4 créé en utilisant `np.arange` dans tous les exemples.

Si vous souhaitez comparer mon tableau avec les résultats utilisés dans cette section, voici comment j'ai créé et imprimé le tableau :

```
arr = np.arange(4)

arr

```

Les valeurs du tableau sont ci-dessous.

```
array([0, 1, 2, 3])

```

### **Comment Effectuer des Opérations Arithmétiques en Python en Utilisant NumPy**

NumPy facilite grandement les opérations arithmétiques avec des tableaux. Vous pouvez effectuer des opérations arithmétiques en utilisant le tableau et un seul nombre, ou vous pouvez effectuer des opérations arithmétiques entre deux tableaux NumPy.

Nous explorons chacune des principales opérations mathématiques ci-dessous.

#### **Addition**

Lorsque vous ajoutez un seul nombre à un tableau NumPy, ce nombre est ajouté à chaque élément du tableau. Un exemple est ci-dessous :

```
2 + arr

#Retourne array([2, 3, 4, 5])

```

Vous pouvez ajouter deux tableaux NumPy en utilisant l'opérateur `+`. Les tableaux sont additionnés sur une base élément par élément (ce qui signifie que les premiers éléments sont additionnés ensemble, les deuxièmes éléments sont additionnés ensemble, et ainsi de suite).

Un exemple est ci-dessous.

```
arr + arr

#Retourne array([0, 2, 4, 6])

```

#### **Soustraction**

Comme l'addition, la soustraction est effectuée sur une base élément par élément pour les tableaux NumPy. Vous pouvez trouver des exemples pour un seul nombre et un autre tableau NumPy ci-dessous.

```
arr - 10

#Retourne array([-10,  -9,  -8,  -7])

arr - arr

#Retourne array([0, 0, 0, 0])

```

#### **Multiplication**

La multiplication est également effectuée sur une base élément par élément pour les nombres uniques et les tableaux NumPy.

Deux exemples sont ci-dessous.

```
6 * arr

#Retourne array([ 0,  6, 12, 18])

arr * arr

#Retourne array([0, 1, 4, 9])

```

#### **Division**

À ce stade, vous n'êtes probablement pas surpris d'apprendre que la division effectuée sur les tableaux NumPy est faite sur une base élément par élément. Un exemple de division de `arr` par un seul nombre est ci-dessous :

```
arr / 2

#Retourne array([0. , 0.5, 1. , 1.5])

```

La division a une exception notable par rapport aux autres opérations mathématiques que nous avons vues dans cette section. Puisque nous ne pouvons pas diviser par zéro, le faire provoquera le remplissage du champ correspondant par une valeur `nan`, qui est l'abréviation Python pour « Not A Number ». Jupyter Notebook imprimera également un avertissement qui ressemble à ceci :

```
RuntimeWarning: invalid value encountered in true_divide

```

Un exemple de division par zéro avec un tableau NumPy est montré ci-dessous.

```
arr / arr

#Retourne array([nan,  1.,  1.,  1.])

```

Nous apprendrons comment gérer les valeurs `nan` plus en détail plus tard dans ce cours.

### **Opérations Complexes dans les Tableaux NumPy**

De nombreuses opérations ne peuvent pas simplement être effectuées en appliquant la syntaxe normale à un tableau NumPy. Dans cette section, nous allons explorer plusieurs opérations mathématiques qui ont des méthodes intégrées dans la bibliothèque NumPy.

#### **Comment Calculer les Racines Carrées en Utilisant NumPy**

Vous pouvez calculer la racine carrée de chaque élément dans un tableau en utilisant la méthode `np.sqrt` :

```
np.sqrt(arr)

#Retourne array([0., 1., 1.41421356, 1.73205081])

```

De nombreux autres exemples sont ci-dessous (notez que vous ne serez pas testé sur ceux-ci, mais il est toujours utile de voir les capacités de NumPy) :

```
np.exp(arr)

#Retourne e^élément pour chaque élément dans le tableau

np.sin(arr)

#Calcule le sinus trigonométrique de chaque valeur dans le tableau

np.cos(arr)

#Calcule le cosinus trigonométrique de chaque valeur dans le tableau

np.log(arr)

#Calcule le logarithme en base dix de chaque valeur dans le tableau

```

### **Passons à la Suite**

Dans cette section, nous avons exploré les différentes méthodes et opérations disponibles dans la bibliothèque NumPy Python. Nous allons tester vos connaissances de ces concepts dans les problèmes pratiques présentés ensuite.

## **Indexation et Affectation NumPy**

Dans cette section, nous allons explorer [l'indexation et l'affectation dans les tableaux NumPy](https://nickmccullum.com/advanced-python/numpy-indexing-assignment/).

### **Le Tableau Que J'Utiliserai Dans Cette Section**

Comme précédemment, j'utiliserai un tableau spécifique dans cette section. Cette fois, il sera généré en utilisant la méthode `np.random.rand`. Voici comment j'ai généré le tableau :

```
arr = np.random.rand(5)

```

Voici le tableau réel :

```
array([0.69292946, 0.9365295 , 0.65682359, 0.72770856, 0.83268616])

```

Pour faciliter la lecture de ce tableau, je vais arrondir chaque élément du tableau à 2 décimales en utilisant la méthode `round` de NumPy :

```
arr = np.round(arr, 2)

```

Voici le nouveau tableau :

```
array([0.69, 0.94, 0.66, 0.73, 0.83])

```

### **Comment Retourner un Élément Spécifique d'un Tableau NumPy**

Nous pouvons sélectionner (et retourner) un élément spécifique d'un tableau NumPy de la même manière que nous pourrions le faire avec une liste Python normale : en utilisant des crochets.

Un exemple est ci-dessous :

```
arr[0]

#Retourne 0.69

```

Nous pouvons également référencer plusieurs éléments d'un tableau NumPy en utilisant l'opérateur deux-points. Par exemple, l'index `[2:]` sélectionne chaque élément à partir de l'index 2. L'index `[:3]` sélectionne chaque élément jusqu'à et excluant l'index 3. L'index `[2:4]` retourne chaque élément de l'index 2 à l'index 4, en excluant l'index 4. Le point final supérieur est toujours exclu.

Quelques exemples d'indexation en utilisant l'opérateur deux-points sont ci-dessous.

```
arr[:]

#Retourne le tableau entier : array([0.69, 0.94, 0.66, 0.73, 0.83])

arr[1:]

#Retourne array([0.94, 0.66, 0.73, 0.83])

arr[1:4] 

#Retourne array([0.94, 0.66, 0.73])

```

### **Affectation d'Éléments dans les Tableaux NumPy**

Nous pouvons attribuer de nouvelles valeurs à un élément d'un tableau NumPy en utilisant l'opérateur `=`, tout comme les listes Python régulières. Voici quelques exemples (notez que tout cela fait partie d'un seul bloc de code, ce qui signifie que les attributions d'éléments sont reportées d'étape en étape).

```
array([0.12, 0.94, 0.66, 0.73, 0.83])

arr

#Retourne array([0.12, 0.94, 0.66, 0.73, 0.83])

arr[:] = 0

arr

#Retourne array([0., 0., 0., 0., 0.])

arr[2:5] = 0.5

arr

#Retourne array([0. , 0. , 0.5, 0.5, 0.5])



```

### **Référencement de Tableaux dans NumPy**

NumPy utilise un concept appelé 'référencement de tableau' qui est une source très courante de confusion pour les personnes qui sont nouvelles dans la bibliothèque.

Pour comprendre le référencement de tableau, considérons d'abord un exemple :

```

new_array = np.array([6, 7, 8, 9])

second_new_array = new_array[0:2]

second_new_array

#Retourne array([6, 7])

second_new_array[1] = 4

second_new_array 

#Retourne array([6, 4]), comme prévu

new_array 

#Retourne array([6, 4, 8, 9]) 

#qui est DIFFÉRENT de sa valeur originale de array([6, 7, 8, 9])

#Qu'est-ce que c'est que ça ?

```

Comme vous pouvez le voir, modifier `second_new_array` a également changé la valeur de `new_array`.

Pourquoi est-ce que c'est comme ça ?

Par défaut, NumPy ne crée pas de copie d'un tableau lorsque vous référencez la variable de tableau originale en utilisant l'opérateur d'affectation `=`. Au lieu de cela, il pointe simplement la nouvelle variable vers l'ancienne variable, ce qui permet à la deuxième variable de modifier la variable originale - même si ce n'est pas votre intention.

Cela peut sembler bizarre, mais cela a une explication logique. Le but du référencement de tableau est de conserver la puissance de calcul. Lorsque vous travaillez avec de grands ensembles de données, vous manqueriez rapidement de RAM si vous créiez un nouveau tableau chaque fois que vous souhaitez travailler avec une tranche du tableau.

Heureusement, il existe une solution au référencement de tableau. Vous pouvez utiliser la méthode `copy` pour copier explicitement un tableau NumPy.

Un exemple de cela est ci-dessous.

```
array_to_copy = np.array([1, 2, 3])

copied_array = array_to_copy.copy()

array_to_copy

#Retourne array([1, 2, 3])

copied_array

#Retourne array([1, 2, 3])

```

Comme vous pouvez le voir ci-dessous, apporter des modifications au tableau copié ne modifie pas l'original.

```
copied_array[0] = 9

copied_array

#Retourne array([9, 2, 3])

array_to_copy

#Retourne array([1, 2, 3])

```

Jusqu'à présent dans cette section, nous n'avons exploré que la manière de référencer des tableaux NumPy à une dimension. Nous allons maintenant explorer l'indexation des tableaux à deux dimensions.

### **Indexation des Tableaux NumPy à Deux Dimensions**

Pour commencer, créons un tableau NumPy à deux dimensions nommé `mat` :

```
mat = np.array([[5, 10, 15],[20, 25, 30],[35, 40, 45]])

mat

"""

Retourne :

array([[ 5, 10, 15],

       [20, 25, 30],

       [35, 40, 45]])

"""

```

Il existe deux façons d'indexer un tableau NumPy à deux dimensions :

* `mat[row, col]`
* `mat[row][col]`

Je préfère personnellement indexer en utilisant la nomenclature `mat[row][col]` car elle est plus facile à visualiser étape par étape. Par exemple :

```
#D'abord, obtenons la première ligne :

mat[0]

#Ensuite, obtenons le dernier élément de la première ligne :

mat[0][-1]

```

Vous pouvez également générer des sous-matrices à partir d'un tableau NumPy à deux dimensions en utilisant cette notation :

```
mat[1:][:2]

"""

Retourne :

array([[20, 25, 30],

       [35, 40, 45]])

"""

```

Le référencement de tableau s'applique également aux tableaux à deux dimensions dans NumPy, alors assurez-vous d'utiliser la méthode `copy` si vous souhaitez éviter de modifier involontairement un tableau original après avoir sauvegardé une tranche de celui-ci dans un nouveau nom de variable.

### **Sélection Conditionnelle en Utilisant les Tableaux NumPy**

Les tableaux NumPy supportent une fonctionnalité appelée `sélection conditionnelle`, qui vous permet de générer un nouveau tableau de valeurs booléennes qui indiquent si chaque élément du tableau satisfait une instruction `if` particulière.

Un exemple de cela est ci-dessous (j'ai également recréé notre variable `arr` originale puisque cela fait un moment que nous ne l'avons pas vue) :

```
arr = np.array([0.69, 0.94, 0.66, 0.73, 0.83])

arr > 0.7

#Retourne array([False,  True, False,  True,  True])

```

Vous pouvez également générer un nouveau tableau de valeurs qui satisfont cette condition en passant la condition dans les crochets (comme nous le faisons pour l'indexation).

Un exemple de cela est ci-dessous :

```
arr[arr > 0.7]

#Retourne array([0.94, 0.73, 0.83])

```

La sélection conditionnelle peut devenir significativement plus complexe que cela. Nous explorerons plus d'exemples dans les problèmes pratiques associés à cette section.

### **Passons à la Suite**

Dans cette section, nous avons exploré l'indexation et l'affectation des tableaux NumPy en détail. Nous allons solidifier vos connaissances de ces concepts en travaillant sur une série de problèmes pratiques dans la section suivante.

## **Réflexions Finales et Offre Spéciale**

Merci d'avoir lu cet article sur NumPy, qui est l'un de mes packages Python préférés et une bibliothèque incontournable pour tout développeur Python.

**Ce tutoriel est un extrait de mon cours** **[Python Pour la Finance et la Science des Données](https://courses.nickmccullum.com/courses/enroll/python-for-finance/). Si vous êtes intéressé à apprendre plus de compétences de base en Python, le cours est à 50% de réduction pour les 50 premiers lecteurs de freeCodeCamp qui s'inscrivent - [cliquez ici pour obtenir votre cours à prix réduit maintenant](https://courses.nickmccullum.com/courses/enroll/python-for-finance/)!**
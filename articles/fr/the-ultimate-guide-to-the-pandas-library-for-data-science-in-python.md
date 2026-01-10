---
title: Le Guide Ultime de la Bibliothèque Pandas pour la Science des Données en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-08T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-the-pandas-library-for-data-science-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/pandas-logo.png
tags:
- name: Data Science
  slug: data-science
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: Le Guide Ultime de la Bibliothèque Pandas pour la Science des Données en
  Python
seo_desc: 'By Nick McCullum

  Pandas (which is a portmanteau of "panel data") is one of the most important packages
  to grasp when you’re starting to learn Python.

  The package is known for a very useful data structure called the pandas DataFrame.
  Pandas also allow...'
---

Par Nick McCullum

Pandas (qui est un mot-valise de "panel data") est l'un des packages les plus importants à maîtriser lorsque vous commencez à [apprendre Python](https://courses.nickmccullum.com/courses/enroll/python-for-finance/).

Ce package est connu pour une structure de données très utile appelée pandas DataFrame. Pandas permet également aux développeurs Python de manipuler facilement des données tabulaires (comme des feuilles de calcul) au sein d'un script Python.

Ce tutoriel vous enseignera les fondamentaux de pandas que vous pouvez utiliser pour construire des applications Python basées sur les données dès aujourd'hui.

## Table des Matières

Vous pouvez sauter à une section spécifique de ce tutoriel pandas en utilisant la table des matières ci-dessous :

* [Introduction à Pandas](#heading-introduction-a-pandas)
* [Séries Pandas](#heading-series-pandas)
* [DataFrames Pandas](#heading-dataframes-pandas)
* [Comment Gérer les Données Manquantes dans les DataFrames Pandas](#heading-comment-gerer-les-donnees-manquantes-dans-les-dataframes-pandas)
* [La Méthode `groupby` de Pandas](#the-pandas--groupby--method)
* [Qu'est-ce que la Fonctionnalité `groupby` de Pandas ?](#quest-ce-que-la-fonctionnalite-groupby-de-pandas)
* [La Méthode `concat` de Pandas](#the-pandas--concat--method)
* [La Méthode `merge` de Pandas](#the-pandas--merge--method)
* [La Méthode `join` de Pandas](#the-pandas--join--method)
* [Autres Opérations Courantes dans Pandas](#heading-autres-operations-courantes-dans-pandas)
* [Entrée et Sortie de Données Locales (I/O) dans Pandas](#entree-et-sortie-de-donnees-locales--i-o--dans-pandas)
* [Entrée et Sortie de Données Distantes (I/O) dans Pandas](#entree-et-sortie-de-donnees-distantes--i-o--dans-pandas)
* [Réflexions Finales et Offre Spéciale](#heading-reflexions-finales-et-offre-speciale)

## **Introduction à Pandas**

Pandas est une bibliothèque Python largement utilisée, construite sur NumPy. Une grande partie du reste de ce cours sera dédiée à l'apprentissage de pandas et à son utilisation dans le monde de la finance.

### **Qu'est-ce que Pandas ?**

[Pandas](https://nickmccullum.com/advanced-python/pandas) est une bibliothèque Python créée par [Wes McKinney](https://wesmckinney.com/), qui a développé pandas pour faciliter le travail avec des ensembles de données en Python pour son travail dans la finance.

Selon [le site web de la bibliothèque](https://pandas.pydata.org/), pandas est _"un outil d'analyse et de manipulation de données open source rapide, puissant, flexible et facile à utiliser, construit sur le langage de programmation [Python](https://www.python.org/)."_

Pandas signifie "panel data". Notez que pandas est généralement stylisé en minuscules, bien qu'il soit considéré comme une bonne pratique de mettre une majuscule à la première lettre au début des phrases.

Pandas est une bibliothèque open source, ce qui signifie que tout le monde peut consulter son code source et faire des suggestions en utilisant des pull requests. Si vous êtes curieux à ce sujet, visitez le dépôt de code source de pandas sur GitHub.

### **Le Principal Avantages de Pandas**

Pandas a été conçu pour travailler avec des données bidimensionnelles (similaires aux feuilles de calcul Excel). Tout comme la bibliothèque NumPy avait une structure de données intégrée appelée `array` avec des attributs et méthodes spéciaux, la bibliothèque pandas a une structure de données bidimensionnelle intégrée appelée `DataFrame`.

### **Ce Que Nous Allons Apprendre Sur Pandas**

Comme nous l'avons mentionné plus tôt dans ce cours, les praticiens avancés de Python passeront beaucoup plus de temps à travailler avec pandas qu'avec NumPy.

Au cours des prochaines sections, nous couvrirons les informations suivantes sur la bibliothèque pandas :

* Séries Pandas
* DataFrames Pandas
* Comment Gérer les Données Manquantes dans Pandas
* Comment Fusionner des DataFrames dans Pandas
* Comment Joindre des DataFrames dans Pandas
* Comment Concaténer des DataFrames dans Pandas
* Opérations Courantes dans Pandas
* Entrée et Sortie de Données dans Pandas
* Comment Enregistrer des DataFrames Pandas en tant que Fichiers Excel pour les Utilisateurs Externes

## **Séries Pandas**

Dans cette section, nous explorerons les [Séries pandas](https://nickmccullum.com/advanced-python/pandas-series/), qui sont un composant central de la bibliothèque pandas pour la programmation Python.

### **Qu'est-ce que les Séries Pandas ?**

Les Séries sont un type spécial de structure de données disponible dans la bibliothèque Python pandas. Les Séries pandas sont similaires aux tableaux NumPy, sauf que nous pouvons leur donner un index nommé ou datetime au lieu d'un simple index numérique.

### **Les Imports Nécessaires pour Travailler avec les Séries Pandas**

Pour travailler avec les Séries pandas, vous devrez importer à la fois NumPy et pandas, comme suit :

```

import numpy as np

import pandas as pd


```

Pour le reste de cette section, je supposerai que ces deux imports ont été exécutés avant d'exécuter les blocs de code.

### **Comment Créer une Série Pandas**

Il existe plusieurs façons de créer une Série pandas. Nous les explorerons toutes dans cette section.

Tout d'abord, créons quelques variables de départ - spécifiquement, nous créerons deux listes, un tableau NumPy et un dictionnaire.

```

labels = ['a', 'b', 'c']

my_list = [10, 20, 30]

arr = np.array([10, 20, 30])

d = {'a':10, 'b':20, 'c':30}


```

La façon la plus simple de créer une Série pandas est de passer une liste Python standard dans la méthode `pd.Series()`. Nous le faisons avec la variable `my_list` ci-dessous :

```

pd.Series(my_list)


```

Si vous exécutez cela dans votre Jupyter Notebook, vous remarquerez que la sortie est assez différente de celle d'une liste Python normale :

```

0    10

1    20

2    30

dtype: int64


```

La sortie affichée ci-dessus est clairement conçue pour présenter deux colonnes. La deuxième colonne contient les données de `my_list`. Qu'est-ce que la première colonne ?

L'un des principaux avantages de l'utilisation des Séries pandas par rapport aux tableaux NumPy est qu'elles permettent l'étiquetage. Comme vous l'avez peut-être deviné, cette première colonne est une colonne d'étiquettes.

Nous pouvons ajouter des étiquettes à une Série pandas en utilisant l'argument `index` comme ceci :

```

pd.Series(my_list, index=labels)

#Rappel - nous avons créé la liste 'labels' plus tôt dans cette section


```

La sortie de ce code est ci-dessous :

```

a    10

b    20

c    30

dtype: int64


```

Pourquoi voudriez-vous utiliser des étiquettes dans une Série pandas ? Le principal avantage est qu'il permet de référencer un élément de la Série en utilisant son étiquette au lieu de son index numérique. Pour être clair, une fois les étiquettes appliquées à une Série pandas, vous pouvez utiliser soit son index numérique, soit son étiquette.

Un exemple de cela est ci-dessous.

```

Series = pd.Series(my_list, index=labels)

Series[0]

#Retourne 10

Series['a']

#Retourne également 10


```

Vous avez peut-être remarqué que la capacité à référencer un élément d'une Série en utilisant son étiquette est similaire à la façon dont nous pouvons référencer la `valeur` d'une paire `clé`-`valeur` dans un dictionnaire. En raison de cette similarité dans leur fonctionnement, vous pouvez également passer un dictionnaire pour créer une Série pandas. Nous utiliserons le `d={'a': 10, 'b': 20, 'c': 30}` que nous avons créé précédemment comme exemple :

```

pd.Series(d)


```

La sortie de ce code est :

```

a    10

b    20

c    30

dtype: int64


```

Il n'est peut-être pas encore clair pourquoi nous avons exploré deux nouvelles structures de données (tableaux NumPy et Séries pandas) qui sont si similaires. Dans la prochaine section de cette section, nous explorerons le principal avantage des Séries pandas par rapport aux tableaux NumPy.

### **Le Principal Avantages des Séries Pandas par Rapport aux Tableaux NumPy**

Bien que nous ne l'ayons pas rencontré à l'époque, les tableaux NumPy sont fortement limités par une caractéristique : chaque élément d'un tableau NumPy doit être du même type de structure de données. En d'autres termes, les éléments d'un tableau NumPy doivent être tous des chaînes, ou tous des entiers, ou tous des booléens - vous voyez le point.

Les Séries pandas ne souffrent pas de cette limitation. En fait, les Séries pandas sont très flexibles.

Par exemple, vous pouvez passer trois des fonctions intégrées de Python dans une Série pandas sans obtenir d'erreur :

```

pd.Series([sum, print, len])


```

Voici la sortie de ce code :

```

0      <built-in function sum>

1    <built-in function print>

2      <built-in function len>

dtype: object


```

Pour être clair, l'exemple ci-dessus est hautement impratique et n'est pas quelque chose que nous exécuterions jamais en pratique. C'est cependant un excellent exemple de la flexibilité de la structure de données des Séries pandas.

## **DataFrames Pandas**

NumPy permet aux développeurs de travailler avec des tableaux NumPy unidimensionnels (parfois appelés vecteurs) et des tableaux NumPy bidimensionnels (parfois appelés matrices). Nous avons exploré les Séries pandas dans la dernière section, qui sont similaires aux tableaux NumPy unidimensionnels.

Dans cette section, nous allons plonger dans les [DataFrames pandas](https://nickmccullum.com/advanced-python/pandas-dataframes/), qui sont similaires aux tableaux NumPy bidimensionnels - mais avec beaucoup plus de fonctionnalités. Les DataFrames sont la structure de données la plus importante dans la bibliothèque pandas, alors prenez des notes tout au long de cette section.

### **Qu'est-ce qu'un DataFrame Pandas ?**

Un DataFrame pandas est une structure de données bidimensionnelle qui a des étiquettes pour ses lignes et ses colonnes. Pour ceux qui sont familiers avec Microsoft Excel, Google Sheets ou d'autres logiciels de tableur, les DataFrames sont très similaires.

Voici un exemple de DataFrame pandas affiché dans un Jupyter Notebook.

![Exemple de DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe.png)

Nous allons maintenant passer par le processus de recréation de ce DataFrame étape par étape.

Tout d'abord, vous devrez importer les bibliothèques NumPy et pandas. Nous l'avons déjà fait, mais au cas où vous ne seriez pas sûr, voici un autre exemple de la façon de le faire :

```

import numpy as np

import pandas as pd


```

Nous devrons également créer des listes pour les noms des lignes et des colonnes. Nous pouvons le faire en utilisant des listes Python standard :

```

rows = ['X','Y','Z']

cols = ['A', 'B', 'C', 'D', 'E']


```

Ensuite, nous devrons créer un tableau NumPy qui contient les données contenues dans les cellules du DataFrame. J'ai utilisé la méthode `np.random.randn` de NumPy pour cela. J'ai également enveloppé cette méthode dans la méthode `np.round` (avec un deuxième argument de `2`), qui arrondit chaque point de données à 2 décimales et rend la structure de données beaucoup plus facile à lire.

Voici la fonction finale qui a généré les données.

```

data = np.round(np.random.randn(3,5),2)


```

Une fois cela fait, vous pouvez envelopper toutes les variables constituantes dans la méthode `pd.DataFrame` pour créer votre premier DataFrame !

```

pd.DataFrame(data, rows, cols)


```

Il y a beaucoup à déballer ici, alors discutons de cet exemple un peu plus en détail.

Tout d'abord, il n'est pas nécessaire de créer chaque variable en dehors du DataFrame lui-même. Vous auriez pu créer ce DataFrame en une ligne comme ceci :

```

pd.DataFrame(np.round(np.random.randn(3,5),2), ['X','Y','Z'], ['A', 'B', 'C', 'D', 'E'])


```

Cela dit, déclarer chaque variable séparément rend le code beaucoup plus facile à lire.

Deuxièmement, vous vous demandez peut-être s'il est nécessaire de mettre les lignes dans la méthode `DataFrame` avant les colonnes. Il est effectivement nécessaire. Si vous essayiez d'exécuter `pd.DataFrame(data, cols, rows)`, votre Jupyter Notebook générerait le message d'erreur suivant :

```

ValueError: Shape of passed values is (3, 5), indices imply (5, 3)


```

Ensuite, nous explorerons la relation entre les Séries pandas et les DataFrames pandas.

### **La Relation Entre les Séries Pandas et les DataFrames Pandas**

Prenons un autre regard sur le DataFrame pandas que nous venons de créer :

![Exemple de DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe.png)

Si vous deviez décrire verbalement une Série pandas, une façon de le faire pourrait être "un ensemble de colonnes étiquetées contenant des données où chaque colonne partage le même ensemble d'index de lignes".

De manière intéressante, chacune de ces colonnes est en fait une Série pandas ! Nous pouvons donc modifier notre définition du DataFrame pandas pour qu'elle corresponde à sa définition formelle :

"Un ensemble de Séries pandas qui partage le même index."

### **Indexation et Assignation dans les DataFrames Pandas**

Nous pouvons en fait appeler une Série spécifique à partir d'un DataFrame pandas en utilisant des crochets, tout comme nous appelons un élément à partir d'une liste. Quelques exemples sont ci-dessous :

```

df = pd.DataFrame(data, rows, cols)

df['A']

"""

Retourne :

X   -0.66

Y   -0.08

Z    0.64

Name: A, dtype: float64

"""

df['E']

"""

Retourne :

X   -1.46

Y    1.71

Z   -0.20

Name: E, dtype: float64

"""


```

Et si vous vouliez sélectionner plusieurs colonnes à partir d'un DataFrame pandas ? Vous pouvez passer une liste de colonnes, soit directement dans les crochets - comme `df[['A', 'E']]` - soit en déclarant la variable en dehors des crochets comme ceci :

```

columnsIWant = ['A', 'E']

df[columnsIWant]

#Retourne le DataFrame, mais seulement avec les colonnes A et E


```

Vous pouvez également sélectionner un élément spécifique d'une ligne spécifique en utilisant des crochets enchaînés. Par exemple, si vous vouliez l'élément contenu dans la ligne A à l'index X (qui est l'élément dans la cellule en haut à gauche du DataFrame), vous pourriez y accéder avec `df['A']['X']`.

Quelques autres exemples sont ci-dessous.

```

df['B']['Z']

#Retourne 1.34

df['D']['Y']

#Retourne -0.64


```

### **Comment Créer et Supprimer des Colonnes dans un DataFrame Pandas**

Vous pouvez créer une nouvelle colonne dans un DataFrame pandas en spécifiant la colonne comme si elle existait déjà, puis en lui assignant une nouvelle Série pandas.

Par exemple, dans le bloc de code suivant, nous créons une nouvelle colonne appelée 'A + B' qui est la somme des colonnes A et B :

```

df['A + B'] = df['A'] + df['B']

df 

#La dernière ligne imprime le nouveau DataFrame


```

Voici la sortie de ce bloc de code :

![Comment Ajouter Une Colonne À Un DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe-add-column.png)

Pour supprimer cette colonne du DataFrame pandas, nous devons utiliser la méthode `pd.DataFrame.drop`.

Notez que cette méthode supprime par défaut les lignes, et non les colonnes. Pour basculer les paramètres de la méthode pour qu'elle opère sur les colonnes, nous devons lui passer l'argument `axis=1`.

```

df.drop('A + B', axis = 1)


```

![Exemple de DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe.png)

Il est très important de noter que cette méthode `drop` ne modifie pas réellement le DataFrame lui-même. Pour preuve, imprimez à nouveau la variable `df`, et remarquez comment elle contient toujours la colonne `A + B` :

```

df


```

![Comment Ajouter Une Colonne À Un DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe-add-column.png)

La raison pour laquelle `drop` (et de nombreuses autres méthodes de DataFrame !) ne modifie pas la structure de données par défaut est de vous empêcher de supprimer accidentellement des données.

Il existe deux façons de faire en sorte que pandas écrase automatiquement le DataFrame actuel.

La première consiste à passer l'argument `inplace=True`, comme ceci :

```

df.drop('A + B', axis=1, inplace=True)


```

La seconde consiste à utiliser un opérateur d'assignation qui écrase manuellement la variable existante, comme ceci :

```

df = df.drop('A + B', axis=1)


```

Les deux options sont valides, mais je trouve que j'utilise plus fréquemment la deuxième option car elle est plus facile à retenir.

La méthode `drop` peut également être utilisée pour supprimer des lignes. Par exemple, nous pouvons supprimer la ligne `Z` comme suit :

```

df.drop('Z')


```

![Comment Supprimer Une Ligne D'un DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe-remove-rows.png)

### **Comment Sélectionner Une Ligne D'un DataFrame Pandas**

Nous avons déjà vu que nous pouvons accéder à une colonne spécifique d'un DataFrame pandas en utilisant des crochets. Nous allons maintenant voir comment accéder à une ligne spécifique d'un DataFrame pandas, avec l'objectif similaire de générer une Série pandas à partir de la structure de données plus grande.

Les lignes de DataFrame peuvent être accessibles par leur étiquette de ligne en utilisant l'attribut `loc` avec des crochets. Un exemple est ci-dessous.

```

df.loc['X']


```

Voici la sortie de ce code :

```

A   -0.66

B   -1.43

C   -0.88

D    1.60

E   -1.46

Name: X, dtype: float64


```

Les lignes de DataFrame peuvent être accessibles par leur index numérique en utilisant l'attribut `iloc` avec des crochets. Un exemple est ci-dessous.

```

df.iloc[0]


```

Comme vous vous en doutez, ce code a la même sortie que notre dernier exemple :

```

A   -0.66

B   -1.43

C   -0.88

D    1.60

E   -1.46

Name: X, dtype: float64


```

### **Comment Déterminer Le Nombre De Lignes et Colonnes dans un DataFrame Pandas**

Il existe de nombreux cas où vous voudrez connaître la forme d'un DataFrame pandas. Par forme, je fais référence au nombre de colonnes et de lignes dans la structure de données.

Pandas a un attribut intégré appelé `shape` qui nous permet d'accéder facilement à cela :

```

df.shape

#Retourne (3, 5)


```

### **Découpage des DataFrames Pandas**

Nous avons déjà vu comment sélectionner des lignes, des colonnes et des éléments à partir d'un DataFrame pandas. Dans cette section, nous explorerons comment sélectionner un sous-ensemble d'un DataFrame. Plus précisément, sélectionnons les éléments des colonnes `A` et `B` et des lignes `X` et `Y`.

Nous pouvons en fait aborder cela de manière étape par étape. Tout d'abord, sélectionnons les colonnes `A` et `B` :

```

df[['A', 'B']]


```

Ensuite, sélectionnons les lignes `X` et `Y` :

```

df[['A', 'B']].loc[['X', 'Y']]


```

Et nous avons terminé !

### **Sélection Conditionnelle en Utilisant un DataFrame Pandas**

Si vous vous souvenez de notre discussion sur les tableaux NumPy, nous avons pu sélectionner certains éléments du tableau en utilisant des opérateurs conditionnels. Par exemple, si nous avions un tableau NumPy appelé `arr` et que nous voulions uniquement les valeurs du tableau qui étaient supérieures à 4, nous aurions pu utiliser la commande `arr[arr > 4]`.

Les DataFrames Pandas suivent une syntaxe similaire. Par exemple, si nous voulions savoir où notre DataFrame a des valeurs supérieures à 0,5, nous pourrions taper `df > 0.5` pour obtenir la sortie suivante :

![Exemple de Sélection Conditionnelle de DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe-condition-selection.png)

Nous pouvons également générer un nouveau DataFrame pandas qui contient les valeurs normales où l'instruction est `True`, et des valeurs `NaN` - qui signifie Not a Number - où l'instruction est fausse. Nous faisons cela en passant l'instruction dans le DataFrame en utilisant des crochets, comme ceci :

```

df[df > 0.5]


```

Voici la sortie de ce code :

![Sélection Conditionnelle Booléenne de DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe-conditional-selection-boolean.png)

Vous pouvez également utiliser la sélection conditionnelle pour retourner un sous-ensemble du DataFrame où une condition spécifique est satisfaite dans une colonne spécifiée.

Pour être plus précis, supposons que vous vouliez le sous-ensemble du DataFrame où la valeur dans la colonne `C` était inférieure à 1. Cela n'est vrai que pour la ligne `X`.

Vous pouvez obtenir un tableau des valeurs booléennes associées à cette instruction comme ceci :

```

df['C'] < 1


```

Voici la sortie :

```

X     True

Y    False

Z    False

Name: C, dtype: bool


```

Vous pouvez également obtenir les valeurs réelles du DataFrame par rapport à cette commande de sélection conditionnelle en tapant `df[df['C'] < 1]`, qui affiche uniquement la première ligne du DataFrame (puisque c'est la seule ligne où l'instruction est vraie pour la colonne `C` :

![Sélection Conditionnelle de DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe-conditional-selection-dataframe.png)

Vous pouvez également enchaîner plusieurs conditions lors de l'utilisation de la sélection conditionnelle. Nous le faisons en utilisant l'opérateur `&` de pandas. Vous ne pouvez pas utiliser l'opérateur `and` normal de Python, car dans ce cas, nous ne comparons pas deux valeurs booléennes. Au lieu de cela, nous comparons deux Séries pandas qui contiennent des valeurs booléennes, ce qui explique pourquoi le caractère `&` est utilisé à la place.

En guise d'exemple de sélection conditionnelle multiple, vous pouvez retourner le sous-ensemble de DataFrame qui satisfait `df['C'] > 0` et `df['A']> 0` avec le code suivant :

```

df[(df['C'] > 0) & (df['A']> 0)]


```

![Sélection Conditionnelle Multiple de DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe-multiple-conditional-selection.png)

### **Comment Modifier l'Index d'un DataFrame Pandas**

Il existe plusieurs façons de modifier l'index d'un DataFrame pandas.

La plus basique consiste à réinitialiser l'index à ses valeurs numériques par défaut. Nous le faisons en utilisant la méthode `reset_index` :

```

df.reset_index()


```

Notez que cela crée une nouvelle colonne dans le DataFrame appelée `index` qui contient les anciennes étiquettes d'index :

![Réinitialiser l'Index du DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe-reset-index.png)

Notez que, comme les autres opérations de DataFrame que nous avons explorées, `reset_index` ne modifie pas le DataFrame original sauf si vous (1) le forcez en utilisant l'opérateur d'assignation `=` ou (2) spécifiez `inplace=True`.

Vous pouvez également définir une colonne existante comme index du DataFrame en utilisant la méthode `set_index`. Nous pouvons définir la colonne `A` comme index du DataFrame en utilisant le code suivant :

```

df.set_index('A')


```

Les valeurs de `A` sont maintenant dans l'index du DataFrame :

![Définir l'Index du DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe-set-index.png)

Il y a trois choses à noter ici :

* `set_index` ne modifie pas le DataFrame original sauf si vous (1) le forcez en utilisant l'opérateur d'assignation `=` ou (2) spécifiez `inplace=True`.
* À moins que vous n'exécutiez d'abord `reset_index`, l'exécution d'une opération `set_index` avec `inplace=True` ou un opérateur d'assignation `=` forcé écrasera définitivement vos valeurs d'index actuelles.
* Si vous souhaitez renommer votre index avec des étiquettes qui ne sont pas actuellement contenues dans une colonne, vous pouvez le faire en (1) créant un tableau NumPy avec ces valeurs, (2) en ajoutant ces valeurs comme nouvelle ligne du DataFrame pandas, et (3) en exécutant l'opération `set_index`.

### **Comment Renommer les Colonnes dans un DataFrame Pandas**

La dernière opération de DataFrame que nous discuterons est comment renommer leurs colonnes.

Les colonnes sont un attribut d'un DataFrame pandas, ce qui signifie que nous pouvons les appeler et les modifier en utilisant un simple opérateur point. Par exemple :

```

df.columns

#Retourne Index(['A', 'B', 'C', 'D', 'E'], dtype='object'


```

L'opérateur d'assignation est le meilleur moyen de modifier cet attribut :

```

df.columns = [1, 2, 3, 4, 5]

df


```

![Nommer les Colonnes du DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe/pandas-dataframe-name-columns.png)

## **Comment Gérer les Données Manquantes dans les DataFrames Pandas**

Dans un monde idéal, nous travaillerions toujours avec des ensembles de données parfaits. Cependant, ce n'est jamais le cas en pratique. Il existe de nombreux cas où, en travaillant avec des données quantitatives, vous devrez supprimer ou modifier des données manquantes. Nous explorerons des stratégies pour [gérer les données manquantes dans Pandas](https://nickmccullum.com/advanced-python/missing-data-pandas/) tout au long de cette section.

### **Le DataFrame Que Nous Utiliserons Dans Cette Section**

Nous utiliserons l'attribut `np.nan` pour générer des valeurs `NaN` tout au long de cette section.

```

Np.nan

#Retourne nan


```

Dans cette section, nous utiliserons le DataFrame suivant :

```

df = pd.DataFrame(np.array([[1, 5, 1],[2, np.nan, 2],[np.nan, np.nan, 3]]))

df.columns = ['A', 'B', 'C']

df


```

![Un DataFrame Pandas Avec Des Données Manquantes](https://nickmccullum.com/images/advanced-python/missing-data/pandas-dataframe-missing-data.png)

### **La Méthode `dropna` de Pandas**

Pandas a une méthode intégrée appelée `dropna`. Lorsqu'elle est appliquée à un DataFrame, la méthode `dropna` supprimera toutes les lignes qui contiennent une valeur NaN.

Appliquons la méthode `dropna` à notre DataFrame `df` comme exemple :

```

df.dropna()


```

![Un DataFrame Pandas Après Utilisation de Dropna](https://nickmccullum.com/images/advanced-python/missing-data/pandas-dataframe-drop-na.png)

Notez que, comme les autres opérations de DataFrame que nous avons explorées, `dropna` ne modifie pas le DataFrame original sauf si vous (1) le forcez en utilisant l'opérateur d'assignation `=` ou (2) spécifiez `inplace=True`.

Nous pouvons également supprimer toutes les colonnes qui ont des valeurs manquantes en passant l'argument `axis=1` à la méthode `dropna`, comme ceci :

```

df.dropna(axis=1)


```

![Un DataFrame Pandas Après Utilisation de Dropna Sur Ses Colonnes](https://nickmccullum.com/images/advanced-python/missing-data/pandas-dataframe-drop-na-columns.png)

### **La Méthode `fillna` de Pandas**

Dans de nombreux cas, vous voudrez remplacer les valeurs manquantes dans un DataFrame pandas au lieu de les supprimer complètement. La méthode `fillna` est conçue pour cela.

Par exemple, remplaçons chaque valeur manquante dans notre DataFrame par le `?` :

```

df.fillna('?')


```

![Un DataFrame Pandas Après Utilisation de Fillna](https://nickmccullum.com/images/advanced-python/missing-data/pandas-dataframe-fill-na.png)

Évidemment, il n'y a pratiquement aucune situation où nous voudrions remplacer les données manquantes par un emoji. Ce n'était qu'un exemple amusant.

Au lieu de cela, plus couramment, nous remplacerons une valeur manquante par soit :

* La valeur moyenne de l'ensemble du DataFrame
* La valeur moyenne de cette ligne du DataFrame

Nous démontrerons les deux ci-dessous.

Pour remplir les valeurs manquantes avec la valeur moyenne de l'ensemble du DataFrame, utilisez le code suivant :

```

df.fillna(df.mean())


```

Pour remplir les valeurs manquantes dans une colonne particulière avec la valeur moyenne de cette colonne, utilisez le code suivant (celui-ci est pour la colonne `A`) :

```

df['A'].fillna(df['A'].mean())


```

## **La Méthode `groupby` de Pandas**

Dans cette section, nous discuterons de l'utilisation de la fonctionnalité [pandas groupby](https://nickmccullum.com/advanced-python/pandas-dataframes-groupby/).

## **Qu'est-ce que la Fonctionnalité `groupby` de Pandas ?**

Pandas est livré avec une fonctionnalité intégrée `groupby` qui vous permet de regrouper des lignes en fonction d'une colonne et d'effectuer une fonction d'agrégation sur elles. Par exemple, vous pourriez calculer la somme de toutes les lignes qui ont une valeur de `1` dans la colonne `ID`.

Pour toute personne familiarisée avec le langage SQL pour interroger des bases de données, la méthode `groupby` de pandas est très similaire à une [instruction SQL groupby](https://nickmccullum.com/sql/sql-group-by/).

Il est plus facile de comprendre la méthode `groupby` de pandas en utilisant un exemple. Nous utiliserons le DataFrame suivant :

```

df = pd.DataFrame([ ['Google', 'Sam', 200],

                    ['Google', 'Charlie', 120],

                    ['Salesforce','Ralph', 125],

                    ['Salesforce','Emily', 250],

                    ['Adobe','Rosalynn', 150],

                    ['Adobe','Chelsea', 500]])

df.columns = ['Organization', 'Salesperson Name', 'Sales']

df


```

![Un Exemple de DataFrame Pandas Que Nous Utiliserons Pour Démontrez Groupby](https://nickmccullum.com/images/advanced-python/pandas-groupby/pandas-dataframe-groupby.png)

Ce DataFrame contient des informations de ventes pour trois organisations distinctes : Google, Salesforce et Adobe. Nous utiliserons la méthode `groupby` pour obtenir des données de ventes résumées pour chaque organisation spécifique.

Pour commencer, nous devrons créer un objet `groupby`. Il s'agit d'une structure de données qui indique à Python quelle colonne vous souhaitez utiliser pour regrouper le DataFrame. Dans notre cas, il s'agit de la colonne `Organization`, donc nous créons un objet `groupby` comme ceci :

```

df.groupby('Organization')


```

Si vous voyez une sortie qui ressemble à ceci, vous saurez que vous avez créé l'objet avec succès :

```

<pandas.core.groupby.generic.DataFrameGroupBy object at 0x113f4ecd0>


```

Une fois que l'objet `groupby` a été créé, vous pouvez appeler des opérations sur cet objet pour créer un DataFrame avec des informations résumées sur les groupes `Organization`. Quelques exemples sont ci-dessous :

```

df.groupby('Organization').mean()

#La moyenne (ou moyenne) de la colonne des ventes

df.groupby('Organization').sum()

#La somme de la colonne des ventes

df.groupby('Organization').std()

#L'écart type de la colonne des ventes


```

Notez que puisque toutes les opérations ci-dessus sont numériques, elles ignoreront automatiquement la colonne `Salesperson Name`, car elle ne contient que des chaînes.

Voici quelques autres fonctions d'agrégation qui fonctionnent bien avec la méthode `groupby` de pandas :

```

df.groupby('Organization').count()

#Compte le nombre d'observations

df.groupby('Organization').max()

#Retourne la valeur maximale

df.groupby('Organization').min()

#Retourne la valeur minimale


```

## **Utilisation de `groupby` Avec La Méthode `describe`**

Un outil très utile lors du [travail avec des DataFrames pandas](https://nickmccullum.com/advanced-python/pandas-common-operations/) est la méthode `describe`, qui retourne des informations utiles pour chaque catégorie avec laquelle la fonction `groupby` travaille.

Cela s'apprend mieux à travers un exemple. J'ai combiné les méthodes `groupby` et `describe` ci-dessous :

```

df.groupby('Organization').describe()


```

Voici à quoi ressemble la sortie :

![Un Exemple de DataFrame Pandas Que Nous Utiliserons Pour Démontrez Groupby](https://nickmccullum.com/images/advanced-python/pandas-groupby/pandas-dataframe-groupby-describe.png)

## **La Méthode `concat` de Pandas**

Dans cette section, nous apprendrons [comment concaténer des DataFrames pandas](https://nickmccullum.com/advanced-python/how-to-concatenate-pandas-dataframes/). Ce sera une section brève, mais c'est un concept important néanmoins. Commençons !

### **Les DataFrames Que Nous Utiliserons Dans Cette Section**

Pour démontrer comment fusionner des DataFrames pandas, j'utiliserai les 3 DataFrames d'exemple suivants :

```

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],

                        'B': ['B0', 'B1', 'B2', 'B3'],

                        'C': ['C0', 'C1', 'C2', 'C3'],

                        'D': ['D0', 'D1', 'D2', 'D3']},

                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],

                        'B': ['B4', 'B5', 'B6', 'B7'],

                        'C': ['C4', 'C5', 'C6', 'C7'],

                        'D': ['D4', 'D5', 'D6', 'D7']},

                         index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],

                        'B': ['B8', 'B9', 'B10', 'B11'],

                        'C': ['C8', 'C9', 'C10', 'C11'],

                        'D': ['D8', 'D9', 'D10', 'D11']},

                        index=[8, 9, 10, 11])


```

### **Comment Concaténer des DataFrames Pandas**

Toute personne ayant suivi mon cours d'introduction à Python se souviendra que la concaténation de chaînes signifie ajouter une chaîne à la fin d'une autre chaîne. Un exemple de concaténation de chaînes est ci-dessous.

```

str1 = "Hello "

str2 = "World!"

str1 + str2

#Retourne 'Hello World!'


```

La concaténation de DataFrame est assez similaire. Cela signifie ajouter un DataFrame à la fin d'un autre DataFrame.

Pour que nous puissions effectuer une concaténation de chaînes, nous devrions avoir deux DataFrames avec les mêmes colonnes. Un exemple est ci-dessous :

```

pd.concat([df1, df2, df3])


```

![Exemple de Concaténation de DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-dataframe-concatenation/pandas-dataframe-concatenation.png)

Par défaut, pandas concaténera le long de `axis=0`, ce qui signifie qu'il ajoute des lignes, et non des colonnes.

Si vous souhaitez ajouter des lignes, passez simplement `axis=0` comme nouvelle variable dans la fonction `concat`.

```

pd.concat([df1,df2,df3],axis=1)


```

Dans notre cas, cela crée un DataFrame très laid avec de nombreuses valeurs manquantes :

![Exemple de Concaténation de DataFrame Pandas le Long des Colonnes](https://nickmccullum.com/images/advanced-python/pandas-dataframe-concatenation/pandas-dataframe-concatenation-columns.png)

## **La Méthode `merge` de Pandas**

Dans cette section, nous apprendrons comment [fusionner des DataFrames pandas](https://nickmccullum.com/advanced-python/how-to-merge-pandas-dataframes/).

### **Les DataFrames Que Nous Utiliserons Dans Cette Section**

Dans cette section, nous utiliserons les deux DataFrames pandas suivants :

```

import pandas as pd

leftDataFrame = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],

                     'A': ['A0', 'A1', 'A2', 'A3'],

                     'B': ['B0', 'B1', 'B2', 'B3']})

   

rightDataFrame = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],

                          'C': ['C0', 'C1', 'C2', 'C3'],

                          'D': ['D0', 'D1', 'D2', 'D3']})    


```

Les colonnes `A`, `B`, `C` et `D` contiennent des données réelles, tandis que la colonne `key` contient une clé commune aux deux DataFrames. Pour `fusionner` deux DataFrames signifie les connecter le long d'une colonne qu'ils ont tous deux en commun.

### **Comment Fusionner des DataFrames Pandas**

Vous pouvez fusionner deux DataFrames pandas le long d'une colonne commune en utilisant les colonnes `merge`. Pour toute personne familiarisée avec le langage de programmation SQL, cela est très similaire à l'exécution d'un `inner join` en SQL.

Ne vous inquiétez pas si vous n'êtes pas familier avec SQL, car la syntaxe `merge` est en fait très simple. Elle ressemble à ceci :

```

pd.merge(leftDataFrame, rightDataFrame, how='inner', on='key')


```

Décomposons les quatre arguments que nous avons passés à la méthode `merge` :

1. `leftDataFrame` : Il s'agit du DataFrame que nous souhaitons fusionner à gauche.
2. `rightDataFrame` : Il s'agit du DataFrame que nous souhaitons fusionner à droite.
3. `how=inner` : Il s'agit du type de fusion que l'opération effectue. Il existe plusieurs types de fusions, mais nous ne couvrirons que les fusions internes dans ce cours.
4. `on='key'` : Il s'agit de la colonne sur laquelle vous souhaitez effectuer la fusion. Puisque `key` était la seule colonne commune entre les deux DataFrames, c'était la seule option que nous pouvions utiliser pour effectuer la fusion.

## **La Méthode `join` de Pandas**

Dans cette section, vous apprendrez [comment joindre des DataFrames pandas](https://nickmccullum.com/advanced-python/how-to-join-pandas-dataframes/).

### **Les DataFrames Que Nous Utiliserons Dans Cette Section**

Nous utiliserons les deux DataFrames suivants dans cette section :

```

leftDataFrame = pd.DataFrame({  'A': ['A0', 'A1', 'A2', 'A3'],

                                'B': ['B0', 'B1', 'B2', 'B3']},

                                index =['K0', 'K1', 'K2', 'K3'])

   

rightDataFrame = pd.DataFrame({ 'C': ['C0', 'C1', 'C2', 'C3'],

                                'D': ['D0', 'D1', 'D2', 'D3']},

                                index = ['K0', 'K1', 'K2', 'K3'])  


```

Si ceux-ci vous semblent familiers, c'est parce qu'ils le sont ! Ce sont presque les mêmes DataFrames que ceux que nous avons utilisés lors de l'apprentissage de la fusion des DataFrames pandas. Une différence clé est que, au lieu que la colonne `key` soit sa propre colonne, elle est maintenant l'index du DataFrame. Vous pouvez penser à ces DataFrames comme étant ceux de la dernière section après avoir exécuté `.set_index(key)`.

### **Comment Joindre des DataFrames Pandas**

Joindre des DataFrames pandas est très similaire à la fusion de DataFrames pandas, sauf que les clés sur lesquelles vous souhaitez combiner sont dans l'index au lieu d'être contenues dans une colonne.

Pour joindre ces deux DataFrames, nous pouvons utiliser le code suivant :

```

leftDataFrame.join(rightDataFrame)


```

## **Autres Opérations Courantes dans Pandas**

Cette section explorera les [opérations courantes dans la bibliothèque Python pandas](https://nickmccullum.com/advanced-python/pandas-common-operations/). Le but de cette section est d'explorer les opérations pandas importantes qui n'ont pas trouvé leur place dans les sections que nous avons discutées jusqu'à présent.

### **Le DataFrame Que Nous Utiliserons Dans Cette Section**

J'utiliserai le DataFrame suivant dans cette section :

```

df = pd.DataFrame({'col1':['A','B','C','D'],

                   'col2':[2,7,3,7],

                   'col3':['fgh','rty','asd','qwe']})


```

### **Comment Trouver des Valeurs Uniques dans une Série Pandas**

Pandas a une excellente méthode appelée `unique` qui peut être utilisée pour trouver des valeurs uniques dans une Série pandas. Notez que cette méthode ne fonctionne que sur les Séries et non sur les DataFrames. Si vous essayez d'appliquer cette méthode à un DataFrame, vous rencontrerez une erreur :

```

df.unique()

#Retourne AttributeError: 'DataFrame' object has no attribute 'unique'


```

Cependant, puisque les colonnes d'un DataFrame pandas sont chacune une Série, nous pouvons appliquer la méthode `unique` à une colonne spécifique, comme ceci :

```

df['col2'].unique()

#Retourne array([2, 7, 3])


```

Pandas a également une méthode séparée `nunique` qui compte le nombre de valeurs uniques dans une Série et retourne cette valeur sous forme d'entier. Par exemple :

```

df['col2'].nunique()

#Retourne 3


```

Intéressamment, la méthode `nunique` est **exactement la même** que `len(unique())` mais c'est une opération suffisamment courante pour que la communauté pandas ait décidé de créer une méthode spécifique pour ce cas d'utilisation.

### **Comment Compter l'Occurrence de Chaque Valeur Dans une Série Pandas**

Pandas a une fonction appelée `counts_value` qui vous permet de compter facilement le nombre de fois que chaque observation se produit. Un exemple est ci-dessous :

```

df['col2'].value_counts()

"""

Retourne :

7    2

2    1

3    1

Name: col2, dtype: int64

"""


```

### **Comment Utiliser la Méthode `apply` de Pandas**

La méthode `apply` est l'une des méthodes les plus puissantes disponibles dans la bibliothèque pandas. Elle vous permet d'appliquer une fonction personnalisée à chaque élément d'une Série pandas.

Par exemple, imaginez que nous avions la fonction suivante `exponentify` qui prend un entier et l'élève à la puissance de lui-même :

```

def exponentify(x):

    return x**x


```

La méthode `apply` vous permet d'appliquer facilement la fonction `exponentify` à chaque élément de la Série :

```

df['col2'].apply(exponentify)

"""

Retourne :

0         4

1    823543

2        27

3    823543

Name: col2, dtype: int64

"""


```

La méthode `apply` peut également être utilisée avec des fonctions intégrées comme `len` (bien qu'elle soit définitivement plus puissante lorsqu'elle est utilisée avec des fonctions personnalisées). Un exemple de la fonction `len` utilisée en conjonction avec `apply` est ci-dessous :

```

df['col3'].apply(len)

"""

Retourne

0    3

1    3

2    3

3    3

Name: col3, dtype: int64

"""

```

### **Comment Trier un DataFrame Pandas**

Vous pouvez filtrer un DataFrame pandas par les valeurs d'une colonne particulière en utilisant la méthode `sort_values`. Par exemple, si vous souhaitiez trier par `col2` dans notre DataFrame `df`, vous exécuteriez la commande suivante :

```

df.sort_values('col2')


```

La sortie de cette commande est ci-dessous :

![Pandas DataFrame Sort Values](https://nickmccullum.com/images/advanced-python/common-operations-pandas/pandas-dataframe-sort-values.png)

Il y a deux choses à noter à partir de cette sortie :

1. Comme vous pouvez le voir, chaque ligne conserve son index, ce qui signifie que l'index est maintenant désordonné.
2. Comme pour les autres méthodes de DataFrame, cela ne modifie pas réellement le DataFrame original sauf si vous le forcez à le faire en utilisant l'opérateur d'assignation `=` ou en passant `inplace = True`.

## **Entrée et Sortie de Données Locales (I/O) dans Pandas**

Dans cette section, nous commencerons à explorer [l'entrée et la sortie de données avec la bibliothèque Python pandas](https://nickmccullum.com/advanced-python/pandas-data-input-output/).

### **Le Fichier Avec Lequel Nous Travaillerons Dans Cette Section**

Nous travaillerons avec différents fichiers contenant les prix des actions pour Facebook (FB), Amazon (AMZN), Google (GOOG) et Microsoft (MSFT) dans cette section. Pour télécharger ces fichiers, téléchargez l'intégralité du dépôt GitHub pour ce cours [ici](https://github.com/nicholasmccullum/advanced-python). Les fichiers utilisés dans cette section peuvent être trouvés dans le dossier `stock_prices` du dépôt.

Vous voudrez enregistrer ces fichiers dans le même répertoire que votre Jupyter Notebook pour cette section. La manière la plus simple de le faire est de télécharger le dépôt GitHub, puis d'ouvrir votre Jupyter Notebook dans le dossier `stock_prices` du dépôt.

### **Comment Importer des Fichiers `.csv` en Utilisant Pandas**

Nous pouvons importer des fichiers `.csv` dans un DataFrame pandas en utilisant la méthode `read_csv`, comme ceci :

```

import pandas as pd

pd.read_csv('stock_prices.csv')


```

Comme vous le verrez, cela crée (et affiche) un nouveau DataFrame pandas contenant les données du fichier `.csv`.

![Un Exemple d'Entrée de Données dans un DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-data-input-output/pandas-data-input-output-example.png)

Vous pouvez également assigner ce nouveau DataFrame à une variable pour y faire référence plus tard en utilisant l'opérateur d'assignation `=` normal :

```

new_data_frame = pd.read_csv('stock_prices.csv')


```

Il existe un certain nombre de méthodes `read` incluses avec la bibliothèque de programmation pandas. Si vous essayez d'importer des données à partir d'un document externe, il est probable que pandas ait une méthode intégrée pour cela.

Quelques exemples de différentes méthodes `read` sont ci-dessous :

```

pd.read_json()

pd.read_html()

pd.read_excel()


```

Nous explorerons certaines de ces méthodes plus tard dans cette section.

Si nous voulions importer un fichier `.csv` qui n'est pas directement dans notre répertoire de travail, nous devons modifier légèrement la syntaxe de la méthode `read_csv`.

Si le fichier est dans un dossier plus profond que celui dans lequel vous travaillez actuellement, vous devez spécifier le chemin complet du fichier dans l'argument de la méthode `read_csv`. Par exemple, si le fichier `stock_prices.csv` était contenu dans un dossier appelé `new_folder`, alors nous pourrions l'importer comme ceci :

```

new_data_frame = pd.read_csv('./new_folder/stock_prices.csv')


```

Pour ceux qui ne sont pas familiers avec la notation de répertoire, le `.` au début du chemin de fichier indique le répertoire actuel. De même, un `..` indique un répertoire au-dessus du répertoire actuel, et un `...` indique _deux_ répertoires au-dessus du répertoire actuel.

Cette syntaxe (en utilisant des périodes) est exactement celle que nous utilisons pour référencer (et importer) des fichiers qui sont au-dessus de notre répertoire de travail actuel. Par exemple, ouvrez un Jupyter Notebook à l'intérieur du dossier `new_folder`, et placez `stock_prices.csv` dans le dossier parent. Avec cette disposition de fichiers, vous pourriez importer le fichier `stock_prices.csv` en utilisant la commande suivante :

```

new_data_frame = pd.read_csv('../stock_prices.csv')


```

Notez que cette syntaxe de répertoire est la même pour tous les types d'importations de fichiers, donc nous ne reverrons pas comment importer des fichiers à partir de différents répertoires lorsque nous explorerons différentes méthodes d'importation plus tard dans ce cours.

### **Comment Exporter des Fichiers `.csv` en Utilisant Pandas**

Pour démontrer comment enregistrer un nouveau fichier `.csv`, créons d'abord un nouveau DataFrame. Plus précisément, remplissons un DataFrame avec 3 colonnes et 50 lignes de données aléatoires en utilisant la méthode `np.random.randn` :

```

import pandas as pd

import numpy as np

df = pd.DataFrame(np.random.randn(50,3))


```

Maintenant que nous avons un DataFrame, nous pouvons l'enregistrer en utilisant la méthode `to_csv`. Cette méthode prend en argument le nom du nouveau fichier.

```

df.to_csv('my_new_csv.csv')


```

Vous remarquerez que si vous exécutez le code ci-dessus, le nouveau fichier `.csv` commencera par une colonne non étiquetée qui contient l'index du DataFrame. Un exemple est ci-dessous (après avoir ouvert le `.csv` dans Microsoft Excel) :

![Un Exemple d'Entrée de Données dans un DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-data-input-output/pandas-data-csv-output.png)

Dans de nombreux cas, cela est indésirable. Pour supprimer la colonne d'index vide, passez `index=False` comme deuxième argument à la méthode `to_csv`, comme ceci :

```

new_data_frame.to_csv('my_new_csv.csv', index = False)


```

Le nouveau fichier `.csv` n'a pas la colonne d'index non étiquetée :

![Un Exemple d'Entrée de Données dans un DataFrame Pandas](https://nickmccullum.com/images/advanced-python/pandas-data-input-output/pandas-data-csv-output-index-false.png)

Les méthodes `read_csv` et `to_csv` rendent très facile l'importation et l'exportation de données à partir de fichiers `.csv` en utilisant pandas. Nous verrons plus tard dans cette section que pour chaque méthode `read` qui nous permet d'importer des données, il existe généralement une fonction `to` correspondante qui nous permet d'enregistrer ces données !

### **Comment Importer des Fichiers `.json` en Utilisant Pandas**

Si vous n'avez pas d'expérience dans le travail avec de grands ensembles de données, vous n'êtes peut-être pas familier avec le type de fichier JSON.

JSON signifie JavaScript Object Notation. Les fichiers JSON sont très similaires aux dictionnaires Python.

Les fichiers JSON sont l'un des types de données les plus couramment utilisés parmi les développeurs de logiciels car ils peuvent être manipulés en utilisant pratiquement tous les langages de programmation.

Pandas a une méthode appelée `read_json` qui facilite l'importation de fichiers JSON en tant que DataFrame pandas. Un exemple est ci-dessous.

```

json_data_frame = pd.read_json('stock_prices.json')


```

Nous apprendrons comment exporter des fichiers JSON ensuite.

### **Comment Exporter des Fichiers `.json` en Utilisant Pandas**

Comme je l'ai mentionné précédemment, il existe généralement une méthode `to` pour chaque méthode `read`. Cela signifie que nous pouvons enregistrer un DataFrame dans un fichier JSON en utilisant la méthode `to_json`.

Par exemple, prenons le DataFrame généré aléatoirement `df` de plus tôt dans cette section et enregistrons-le en tant que fichier JSON dans notre répertoire local :

```

df.to_json('my_new_json.json')


```

Nous apprendrons comment travailler avec des fichiers Excel - qui ont l'extension de fichier `.xlsx` - ensuite.

### **Comment Importer des Fichiers `.xlsx` en Utilisant Pandas**

La méthode `read_excel` de Pandas facilite l'importation de données à partir d'un document Excel dans un DataFrame pandas :

```

new_data_frame = pd.read_excel('stock_prices.xlsx')


```

Contrairement aux méthodes `read_csv` et `read_json` que nous avons explorées plus tôt dans cette section, la méthode `read_excel` peut accepter un deuxième argument. La raison pour laquelle `read_excel` accepte plusieurs arguments est que les feuilles de calcul Excel peuvent contenir plusieurs feuilles. Le deuxième argument spécifie quelle feuille vous essayez d'importer et est appelé `sheet_name`.

Par exemple, si notre `stock_prices` avait une deuxième feuille appelée `Sheet2`, vous importeriez cette feuille dans un DataFrame pandas comme ceci :

```

new_data_frame.to_excel('stock_prices.xlsx', sheet_name='Sheet2')


```

Si vous ne spécifiez aucune valeur pour `sheet_name`, alors `read_excel` importera par défaut la première feuille de la feuille de calcul Excel.

Lors de l'importation de documents Excel, il est très important de noter que pandas n'importe que des données. Il ne peut pas importer d'autres fonctionnalités Excel comme le formatage, les formules ou les macros. Essayer d'importer des données à partir d'un document Excel qui possède ces fonctionnalités peut faire planter pandas.

### **Comment Exporter des Fichiers `.xlsx` en Utilisant Pandas**

L'exportation de fichiers Excel est très similaire à l'importation de fichiers Excel, sauf que nous utilisons `to_excel` au lieu de `read_excel`. Un exemple est ci-dessous en utilisant notre DataFrame généré aléatoirement `df` :

```

df.to_excel('my_new_excel_file.xlsx')


```

Comme `read_excel`, `to_excel` accepte un deuxième argument appelé `sheet_name` qui vous permet de spécifier le nom de la feuille que vous enregistrez. Par exemple, nous aurions pu nommer la feuille du nouveau fichier `.xlsx` `My New Sheet!` en le passant dans la méthode `to_excel` comme ceci :

```

df.to_excel('my_new_excel_file.xlsx', sheet_name='My New Sheet!')


```

Si vous ne spécifiez pas de valeur pour `sheet_name`, alors la feuille sera nommée `Sheet1` par défaut (comme lorsque vous créez un nouveau document Excel en utilisant l'application réelle).

## **Entrée et Sortie de Données Distantes (I/O) dans Pandas**

Dans la dernière section de ce cours, nous avons appris comment importer des données à partir de fichiers `.csv`, `.json` et `.xlsx` qui étaient enregistrés sur notre ordinateur local. Nous allons suivre en vous montrant comment vous pouvez importer des fichiers sans les enregistrer d'abord sur votre machine locale. Cela s'appelle l'importation à distance.

### **Qu'est-ce que l'Importation à Distance et Pourquoi est-elle Utile ?**

L'importation à distance signifie apporter un fichier dans votre script Python sans avoir ce fichier enregistré sur votre ordinateur.

À première vue, il peut ne pas être clair pourquoi nous pourrions vouloir nous engager dans l'importation à distance. Cependant, cela peut être très utile.

La raison pour laquelle l'importation à distance est utile est que, par définition, cela signifie que le script Python continuera à fonctionner même si le fichier importé n'est pas enregistré sur votre ordinateur. Cela signifie que je peux envoyer mon code à des collègues ou amis et qu'il fonctionnera toujours correctement.

Tout au long du reste de cette section, je démontrerai [comment effectuer des importations à distance dans pandas](https://nickmccullum.com/advanced-python/remote-data/) pour les fichiers `.csv`, `.json` et `.xlsx`.

### **Comment Importer des Fichiers `.csv` à Distance**

Tout d'abord, naviguez jusqu'au [dépôt GitHub](https://github.com/nicholasmccullum/advanced-python/) de ce cours. Ouvrez le dossier `stock_prices`. Cliquez sur le fichier `stock_prices.csv`, puis cliquez sur le bouton pour le fichier `Raw`, comme indiqué ci-dessous.

![Exemple de Fichier GitHub Raw](https://nickmccullum.com/images/advanced-python/pandas-remote-data/raw-github-file.png)

Cela vous amènera à une nouvelle page qui contient les données du fichier `.csv` contenu dans `stock_prices.csv`.

Pour importer ce fichier distant dans votre script Python, vous devez d'abord copier son URL dans votre presse-papiers. Vous pouvez le faire soit (1) en surlignant l'URL entière, en cliquant avec le bouton droit sur le texte sélectionné et en cliquant sur `copier`, soit (2) en surlignant l'URL entière et en tapant CTRL+C sur votre clavier.

L'URL ressemblera à ceci :

```

[https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.csv](https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.csv)


```

Vous pouvez passer cette URL dans la méthode `read_csv` pour importer le jeu de données dans un DataFrame pandas sans enregistrer le jeu de données sur votre ordinateur d'abord :

```

pd.read_csv('https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.csv')


```

### **Comment Importer des Fichiers `.json` à Distance**

Nous pouvons importer des fichiers `.json` à distance de manière similaire aux fichiers `.csv`.

Tout d'abord, obtenez l'URL brute de GitHub. Elle ressemblera à ceci :

```

https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.json


```

Ensuite, passez cette URL dans la méthode `read_json` comme ceci :

```

pd.read_json('https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.json')


```

### **Comment Importer des Fichiers `.xlsx` à Distance**

Nous pouvons importer des fichiers `.xlsx` à distance de manière similaire aux fichiers `.csv` et `.json`. Notez que vous devrez cliquer à un endroit légèrement différent sur l'interface GitHub. Plus précisément, vous devrez cliquer avec le bouton droit sur 'View Raw' et sélectionner 'Copy Link Address', comme indiqué ci-dessous.

![Exemple de Fichier GitHub Raw](https://nickmccullum.com/images/advanced-python/pandas-remote-data/raw-excel-file.png)

L'URL brute ressemblera à ceci :

```

https://github.com/nicholasmccullum/advanced-python/blob/master/stock_prices/stock_prices.xlsx?raw=true


```

Ensuite, passez cette URL dans la méthode `read_excel`, comme ceci :

```

pd.read_excel('https://github.com/nicholasmccullum/advanced-python/blob/master/stock_prices/stock_prices.xlsx?raw=true')


```

### **Les Inconvénients de l'Importation à Distance**

L'importation à distance signifie que vous n'avez pas besoin d'enregistrer d'abord le fichier importé sur votre ordinateur local, ce qui est un avantage incontestable.

Cependant, l'importation à distance présente également deux inconvénients :

1. Vous devez avoir une connexion Internet pour effectuer des importations à distance
2. Le ping de l'URL pour récupérer le jeu de données est assez chronophage, ce qui signifie que l'exécution d'importations à distance ralentira la vitesse de votre code Python

## **Réflexions Finales et Offre Spéciale**

Merci d'avoir lu cet article sur Pandas, qui est l'un de mes packages Python préférés et une bibliothèque incontournable pour chaque développeur Python.

**Ce tutoriel est un extrait de mon cours** **[Python Pour la Finance et la Science des Données](https://courses.nickmccullum.com/courses/enroll/python-for-finance/). Si vous êtes intéressé à apprendre plus de compétences de base en Python, le cours est à 50% de réduction pour les 50 premiers lecteurs de freeCodeCamp qui s'inscrivent - [cliquez ici pour obtenir votre cours à prix réduit maintenant](https://courses.nickmccullum.com/courses/enroll/python-for-finance/)!**
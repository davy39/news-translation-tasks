---
title: Comment itérer sur les lignes avec Pandas – Parcourir un DataFrame
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-28T18:35:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-iterate-over-rows-with-pandas-loop-through-a-dataframe
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-How-to-Iterate-Over-Rows-with-Pandas
seo_title: Comment itérer sur les lignes avec Pandas – Parcourir un DataFrame
---

Loop-Through-a-Dataframe.png
tags:
- name: analyse de données
  slug: analyse-de-donnees
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nCet article propose un guide complet sur la manière de parcourir un DataFrame Pandas en Python. \nJe commencerai par présenter la bibliothèque Pandas et la structure de données DataFrame. J'expliquerai les caractéristiques essentielles de Pandas, comment..."
---

Par Shittu Olumide

Cet article propose un guide complet sur la manière de parcourir un DataFrame Pandas en Python. 

Je commencerai par présenter la bibliothèque Pandas et la structure de données DataFrame. J'expliquerai les caractéristiques essentielles de Pandas, comment parcourir les lignes d'un dataframe, et enfin comment parcourir les colonnes d'un dataframe.

## Qu'est-ce que Pandas ?

Pandas est une bibliothèque Python open-source populaire utilisée pour le nettoyage, l'analyse et la manipulation de données. En plus des fonctions permettant d'effectuer des opérations sur ces jeux de données, elle propose des structures de données pour stocker et manipuler efficacement des jeux de données volumineux et complexes. 

Voici quelques-unes des caractéristiques essentielles de Pandas :

* **Objets DataFrame et Series** : Pandas propose deux structures de données principales, les DataFrames et les Series. Elles permettent aux utilisateurs de stocker et de manipuler respectivement des données tabulaires et des données de séries temporelles. Ces structures de données sont très efficaces et peuvent gérer facilement de grands jeux de données.
* **Nettoyage et préparation des données** : Pandas offre une large gamme de fonctions et de méthodes pour nettoyer et préparer les données, notamment la gestion des valeurs manquantes, la suppression des doublons et la transformation des données.
* **Analyse et visualisation des données** : Pandas propose des fonctions puissantes pour effectuer des analyses de données, notamment des fonctions statistiques et des fonctions de groupement et d'agrégation. Il s'intègre également bien avec d'autres bibliothèques d'analyse et de visualisation de données en Python, telles que Matplotlib et Seaborn.
* **Entrée et sortie de données** : Pandas propose des fonctions pour lire et écrire des données dans divers formats, y compris CSV, Excel, les bases de données SQL, et plus encore.

## Qu'est-ce qu'un Dataframe Pandas ?

Dans Pandas, un dataframe est une structure de données étiquetée à deux dimensions. Il est comparable à une feuille de calcul ou à une table SQL, où les données sont organisées en lignes et en colonnes avec une variété de types de données dans chaque colonne.

Comme les dataframes offrent un moyen simple de stocker, manipuler et analyser des données, ils sont fréquemment utilisés dans les applications de science des données et d'analyse de données. Les dataframes offrent de nombreuses fonctionnalités, notamment le pivotage, le groupement, l'indexation et le filtrage, qui facilitent l'exécution d'opérations complexes sur les données.

## Comment parcourir les lignes d'un Dataframe

Vous pouvez parcourir les lignes d'un dataframe en utilisant la méthode `iterrows()` de Pandas. Cette méthode nous permet d'itérer sur chaque ligne d'un dataframe et d'accéder à ses valeurs.

Voici un exemple :

```py
import pandas as pd

# créer un dataframe
data = {'name': ['Mike', 'Doe', 'James'], 'age': [18, 19, 29]}
df = pd.DataFrame(data)

# parcourir les lignes en utilisant iterrows()
for index, row in df.iterrows():
    print(row['name'], row['age'])

```

Sortie :

```bash
Mike 18
Doe 19
James 29

```

Dans cet exemple, nous créons d'abord un dataframe avec deux colonnes, `name` et `age`. Nous parcourons ensuite chaque ligne du dataframe en utilisant `iterrows()`, qui renvoie un tuple contenant l'index de la ligne et un objet Series qui contient les valeurs pour cette ligne.

À l'intérieur de la boucle, nous pouvons accéder aux valeurs de chaque colonne en utilisant le nom de la colonne comme index sur l'objet row. Par exemple, pour accéder à la valeur de la colonne `name`, nous utilisons `row['name']`.

## Comment parcourir les colonnes d'un Dataframe

Parcourir les colonnes d'un dataframe est une tâche courante dans l'analyse et la manipulation de données. C'est cependant différent de la façon dont nous parcourons les lignes. 

Voici un exemple :

```py
import pandas as pd

# Créer un dataframe d'exemple
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Parcourir les colonnes à l'aide d'une boucle for
for col in df.columns:
    print(col)

```

Sortie :

```bash
A
B
C

```

Tout d'abord, nous importons la bibliothèque Pandas à l'aide de l'instruction `import pandas as pd`.

Ensuite, nous créons un dataframe d'exemple à l'aide de la fonction `pd.DataFrame()`, qui prend en entrée un dictionnaire de noms de colonnes et de valeurs.

Ensuite, nous parcourons les colonnes du dataframe en utilisant une boucle for et l'attribut `df.columns`, qui renvoie une liste de noms de colonnes.

À l'intérieur de la boucle, nous affichons simplement le nom de chaque colonne à l'aide de la fonction `print()`.

## Cas d'utilisation pour le parcours d'un Dataframe

Le parcours d'un dataframe est une technique importante dans l'analyse et la manipulation de données, car il nous permet d'effectuer des opérations sur chaque ligne ou colonne du dataframe. 

Vous parcourrez des dataframes dans les activités suivantes :

* Nettoyage et transformation des données.
* Analyse de données.
* Visualisation de données.
* Feature Engineering (Ingénierie des caractéristiques).

## Conclusion

En parcourant les lignes d'un dataframe, nous pouvons effectuer des opérations sur chaque ligne, comme le filtrage ou la transformation des données. 

Mais il est important de noter que le parcours des lignes dans un dataframe peut être lent et inefficace pour les grands jeux de données. En général, il est souvent préférable d'utiliser des opérations vectorisées ou des fonctions `apply()` pour effectuer des opérations sur les dataframes, car ces méthodes sont optimisées pour la performance.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !
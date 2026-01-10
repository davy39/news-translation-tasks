---
title: Comment utiliser Pandas pour le nettoyage et le prétraitement des données
subtitle: ''
author: Oluwadamisi Samuel
co_authors: []
series: null
date: '2024-01-30T14:55:00.000Z'
originalURL: https://freecodecamp.org/news/data-cleaning-and-preprocessing-with-pandasbdvhj
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Cream-Neutral-Minimalist-New-Business-Pitch-Deck-Presentation--1-.png
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: Comment utiliser Pandas pour le nettoyage et le prétraitement des données
seo_desc: 'Steve Lohr of The New York Times said: "Data scientists, according to interviews
  and expert estimates, spend 50 percent to 80 percent of their time mired in the
  mundane labor of collecting and preparing unruly digital data, before it can be
  explored ...'
---

Steve Lohr du New York Times a déclaré : "Les scientifiques des données, selon des interviews et des estimations d'experts, passent de 50 % à 80 % de leur temps à effectuer le travail fastidieux de collecte et de préparation de données numériques indisciplinées, avant de pouvoir les explorer pour en extraire des informations utiles."

Cette déclaration est à 100 % exacte, car elle englobe une série d'étapes qui garantissent que les données utilisées pour les projets de science des données, d'apprentissage automatique et d'analyse sont complètes, précises, non biaisées et fiables.

La qualité de votre ensemble de données joue un rôle pivot dans le succès de votre analyse ou de votre modèle. Comme le dit l'adage, "garbage in, garbage out", la qualité et la fiabilité de votre modèle et de votre analyse dépendent fortement de la qualité de vos données.

Les données brutes, collectées à partir de diverses sources, sont souvent désordonnées, contiennent des erreurs, des incohérences, des valeurs manquantes et des valeurs aberrantes. Le nettoyage et le prétraitement des données visent à identifier et à rectifier ces problèmes pour garantir des résultats précis, fiables et significatifs lors de la construction de modèles et de l'analyse de données, car des conclusions erronées pourraient être coûteuses.

C'est là que Pandas entre en jeu, c'est un outil merveilleux utilisé dans le monde des données pour effectuer à la fois le nettoyage et le prétraitement des données. Dans cet article, nous allons approfondir les concepts essentiels du nettoyage et du prétraitement des données en utilisant la puissante bibliothèque Python, Pandas.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Introduction](#heading-introduction)
    
* [Qu'est-ce que le nettoyage des données ?](#heading-quest-ce-que-le-nettoyage-des-donnees)
    
* [Qu'est-ce que le traitement des données ?](#heading-quest-ce-que-le-traitement-des-donnees)
    
* [Comment importer les bibliothèques nécessaires](#heading-comment-importer-les-bibliotheques-necessaires)
    
* [Comment charger l'ensemble de données](#heading-comment-charger-lensemble-de-donnees)
    
* [Analyse exploratoire des données (EDA)](#heading-analyse-exploratoire-des-donnees-eda)
    
* [Comment gérer les valeurs manquantes](#heading-comment-gerer-les-valeurs-manquantes)
    
* [Comment supprimer les enregistrements en double](#heading-comment-supprimer-les-enregistrements-en-double)
    
* [Types de données et conversion](#heading-types-de-donnees-et-conversion)
    
* [Comment encoder les variables catégorielles](#heading-comment-encoder-les-variables-categorielles)
    
* [Comment gérer les valeurs aberrantes](#heading-comment-gerer-les-valeurs-aberrantes)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

* Une compréhension de base de Python.
    
* Compréhension de base du nettoyage des données.
    

## Introduction

Pandas est une bibliothèque populaire open-source de manipulation et d'analyse de données pour Python. Elle fournit des fonctions faciles à utiliser nécessaires pour travailler avec des données structurées de manière transparente.

Pandas s'intègre également de manière transparente avec d'autres bibliothèques Python populaires, telles que NumPy pour le calcul numérique et Matplotlib pour la visualisation de données. Cela en fait un atout puissant pour les tâches basées sur les données.

Pandas excelle dans la gestion des données manquantes, le remodelage des ensembles de données, la fusion et la jointure de plusieurs ensembles de données, et l'exécution d'opérations complexes sur les données, ce qui le rend exceptionnellement utile pour le nettoyage et la manipulation des données.

Au cœur de Pandas, deux structures de données clés sont introduites : `Series` et `DataFrame`. Une `Series` est un objet de type tableau unidimensionnel qui peut contenir n'importe quel type de données, tandis qu'un `DataFrame` est un tableau bidimensionnel avec des axes étiquetés (lignes et colonnes). Ces structures permettent aux utilisateurs de manipuler, nettoyer et analyser les ensembles de données de manière efficace.

## Qu'est-ce que le nettoyage des données ?

Avant de nous lancer dans notre aventure de données avec Pandas, prenons un moment pour expliquer le terme "nettoyage des données". Imaginez cela comme un détox numérique pour votre ensemble de données, où nous rangeons et priorisons la précision par-dessus tout.

Le nettoyage des données implique d'identifier et de rectifier les erreurs, les incohérences et les valeurs manquantes au sein d'un ensemble de données. C'est comme préparer vos ingrédients avant de cuisiner ; vous voulez que tout soit en ordre pour obtenir l'analyse ou la visualisation parfaite.

Pourquoi se soucier du nettoyage des données ? Eh bien, imaginez essayer d'analyser les tendances des ventes lorsque certaines entrées sont manquantes, ou travailler avec un ensemble de données qui contient des enregistrements en double faussant vos calculs. Pas idéal, n'est-ce pas ?

Dans ce détox numérique, nous utilisons des outils comme Pandas pour nous débarrasser des incohérences, redresser les erreurs et laisser la véritable clarté de vos données briller.

## Qu'est-ce que le traitement des données ?

Vous vous demandez peut-être, "Le nettoyage des données et le prétraitement des données signifient-ils la même chose ?" La réponse est non – ils ne le sont pas.

Imaginez ceci : vous tombez sur un ancien coffre au trésor enterré dans les sables numériques de votre ensemble de données. Le nettoyage des données est comme déterrer soigneusement ce coffre, enlever les toiles d'araignée et s'assurer que ce qui se trouve à l'intérieur est authentique et fiable.

Quant au prétraitement des données, vous pouvez le considérer comme la prise de ce trésor découvert et la préparation de son contenu pour une exposition publique. Cela va au-delà du nettoyage ; il s'agit de transformer et d'optimiser les données pour des analyses ou des tâches spécifiques.

Le nettoyage des données est la phase initiale de l'affinage de votre ensemble de données, le rendant lisible et utilisable avec des techniques comme la suppression des doublons, la gestion des valeurs manquantes et la conversion des types de données, tandis que le prétraitement des données est similaire à la prise de ces données affinées et à leur mise à l'échelle avec des techniques plus avancées telles que l'ingénierie des caractéristiques, l'encodage des variables catégorielles et la gestion des valeurs aberrantes pour obtenir des résultats meilleurs et plus avancés.

L'objectif est de transformer votre ensemble de données en un chef-d'œuvre affiné, prêt pour l'analyse ou la modélisation.

## Comment importer les bibliothèques nécessaires

Avant de nous lancer dans le nettoyage et le prétraitement des données, importons la bibliothèque `Pandas`.

Pour gagner du temps et de la frappe, nous importons souvent Pandas sous le nom de `pd`. Cela nous permet d'utiliser le plus court `pd.read_csv()` au lieu de `pandas.read_csv()` pour lire les fichiers CSV, rendant notre code plus efficace et lisible.

```py
import pandas as pd
```

## Comment charger l'ensemble de données

Commencez par charger votre ensemble de données dans un DataFrame Pandas.

Dans cet exemple, nous utiliserons un ensemble de données hypothétique nommé **votre_dataset.csv**. Nous chargerons l'ensemble de données dans une variable appelée `df`.

```py
#Remplacez 'votre_dataset.csv' par le nom ou le chemin du fichier de l'ensemble de données
df = pd.read_csv('votre_dataset.csv')
```

## Analyse exploratoire des données (EDA)

L'EDA vous aide à comprendre la structure et les caractéristiques de votre ensemble de données. Certaines fonctions Pandas nous aident à obtenir des informations sur notre ensemble de données. Nous appelons ces fonctions en appelant la variable de l'ensemble de données plus la fonction.

Par exemple :

* `df.head()` affichera les 5 premières lignes de l'ensemble de données. Vous pouvez spécifier le nombre de lignes à afficher entre parenthèses.
    
* `df.describe()` donne quelques données statistiques comme les percentiles, la moyenne et l'écart type des valeurs numériques de la Série ou du DataFrame.
    
* `df.info()` donne le nombre de colonnes, les étiquettes de colonnes, les types de données des colonnes, l'utilisation de la mémoire, l'index de plage et le nombre de cellules dans chaque colonne (valeurs non nulles).
    

Voici un exemple de code ci-dessous :

```py
#Afficher les premières lignes de l'ensemble de données
print(df.head())

#Statistiques récapitulatives
print(df.describe())

#Informations sur l'ensemble de données
print(df.info())
```

## Comment gérer les valeurs manquantes

En tant que débutant dans ce domaine, les valeurs manquantes posent un stress significatif car elles se présentent sous différents formats et peuvent nuire à votre analyse ou modèle.

Les modèles d'apprentissage automatique ne peuvent pas être entraînés avec des données qui ont des valeurs manquantes ou "NAN" car elles peuvent altérer votre résultat final lors de l'analyse. Mais ne vous inquiétez pas, Pandas fournit des méthodes pour gérer ce problème.

Une façon de faire cela est de supprimer complètement les valeurs manquantes. Extrait de code ci-dessous :

```py
#Vérifier les valeurs manquantes
print(df.isnull().sum())

#Supprimer les lignes avec des valeurs manquantes et les placer dans une nouvelle variable "df_cleaned"
df_cleaned = df.dropna()

#Remplir les valeurs manquantes avec la moyenne pour les données numériques et les placer dans une nouvelle variable appelée df_filled
df_filled = df.fillna(df.mean())
```

Mais si le nombre de lignes ayant des valeurs manquantes est grand, alors cette méthode sera inadéquate.

Pour les données numériques, vous pouvez simplement calculer la moyenne et l'entrer dans les lignes ayant des valeurs manquantes. Extrait de code ci-dessous :

```py
#Remplacer les valeurs manquantes par la moyenne de chaque colonne
df.fillna(df.mean(), inplace=True)

#Si vous voulez remplacer les valeurs manquantes dans une colonne spécifique, vous pouvez le faire de cette manière :
#Remplacez 'column_name' par le nom réel de la colonne
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

#Maintenant, df ne contient plus de valeurs manquantes, et les NaN ont été remplacés par la moyenne de la colonne
```

## Comment supprimer les enregistrements en double

Les enregistrements en double peuvent fausser votre analyse en influençant les résultats de manière à ne pas montrer avec précision les tendances et les schémas sous-jacents (en produisant des valeurs aberrantes).

Pandas aide à identifier et à supprimer les valeurs en double de manière facile en les plaçant dans de nouvelles variables.

Extrait de code ci-dessous :

```py
#Identifier les doublons
print(df.duplicated().sum())

#Supprimer les doublons
df_no_duplicates = df.drop_duplicates()
```

## Types de données et conversion

La conversion des types de données dans Pandas est un aspect crucial du prétraitement des données, vous permettant de vous assurer que vos données sont dans le format approprié pour l'analyse ou la modélisation.

Les données provenant de diverses sources sont généralement désordonnées et les types de données de certaines valeurs peuvent être dans le mauvais format, par exemple, certaines valeurs numériques peuvent être au format 'float' ou 'string' au lieu du format 'integer', et un mélange de ces formats conduit à des erreurs et à des résultats incorrects.

Vous pouvez convertir une colonne de type `int` en `float` avec le code suivant :

```py
#Convertir 'Column1' en float
df['Column1'] = df['Column1'].astype(float)

#Afficher les types de données mis à jour
print(df.dtypes)
```

Vous pouvez utiliser `df.dtypes` pour afficher les types de données des colonnes.

## Comment encoder les variables catégorielles

Pour les algorithmes d'apprentissage automatique, avoir des valeurs catégorielles dans votre ensemble de données (valeurs non numériques) est crucial pour garantir le meilleur modèle car elles sont tout aussi importantes.

Celles-ci pourraient être des noms de marques de voitures dans un ensemble de données de voitures pour prédire les prix des voitures. Mais les algorithmes d'apprentissage automatique ne peuvent pas traiter ce type de données, il doit donc être converti en données numériques avant de pouvoir être utilisé.

Pandas fournit la fonction `get_dummies` qui convertit les valeurs catégorielles en format numérique (format binaire) de sorte qu'elles soient reconnues par l'algorithme comme un espace réservé pour les valeurs et non comme des données hiérarchiques pouvant subir une analyse numérique. Cela signifie simplement que les nombres auxquels le nom de la marque est converti ne sont pas interprétés comme 1 est supérieur à 0, mais cela indique à l'algorithme que 1 et 0 sont des espaces réservés pour les données catégorielles. L'extrait de code est montré ci-dessous :

```py
#Pour convertir les données catégorielles de la colonne "Car_Brand" en données numériques
df_encode = pd.get_dummies(df, columns=[Car_Brand])

#Les données catégorielles sont converties en format binaire de données numériques
```

## Comment gérer les valeurs aberrantes

Les valeurs aberrantes sont des points de données significativement différents de la majorité des données, elles peuvent fausser les mesures statistiques et affecter négativement les performances des modèles d'apprentissage automatique.

Elles peuvent être causées par une erreur humaine, des valeurs NaN manquantes, ou pourraient être des données exactes qui ne corrèlent pas avec le reste des données.

Il existe plusieurs méthodes pour identifier et supprimer les valeurs aberrantes, elles sont :

* Supprimer les valeurs NaN.
    
* Visualiser les données avant et après la suppression.
    
* Méthode du score Z (pour les données normalement distribuées).
    
* Méthode IQR (Intervalle interquartile) pour des données plus robustes.
    

L'IQR est utile pour identifier les valeurs aberrantes dans un ensemble de données. Selon la méthode IQR, les valeurs qui tombent en dessous de Q1−1.5×IQR ou au-dessus de Q3+1.5×IQR sont considérées comme des valeurs aberrantes.

Cette règle est basée sur l'hypothèse que la plupart des données dans une distribution normale devraient tomber dans cette plage.

Voici un extrait de code pour la méthode IQR :

```py
#En utilisant les calculs de médiane et d'IQR, les valeurs aberrantes sont identifiées et ces points de données doivent être supprimés
Q1 = df["column_name"].quantile(0.25)
Q3 = df["column_name"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[df["column_name"].between(lower_bound, upper_bound)]
```

## Conclusion

Le nettoyage et le prétraitement des données sont des composants intégraux de tout projet d'analyse, de science ou d'apprentissage automatique. Pandas, avec ses fonctions polyvalentes, facilite ces processus de manière efficace.

En suivant les concepts décrits dans cet article, vous pouvez vous assurer que vos données sont bien préparées pour l'analyse et la modélisation, conduisant finalement à des résultats plus précis et fiables.
---
title: Comment gérer les données manquantes dans un ensemble de données
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-06-24T21:14:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-missing-data-in-a-dataset
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/randy-fath-G1yhU1Ej-9A-unsplash--1-.jpeg
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
seo_title: Comment gérer les données manquantes dans un ensemble de données
seo_desc: 'Missing values are common when working with real-world datasets – not the
  cleaned ones available on Kaggle, for example.

  Missing data could result from a human factor (for example, a person deliberately
  failing to respond to a survey question), a pro...'
---

Les valeurs manquantes sont courantes lorsque l'on travaille avec des ensembles de données réels – pas ceux nettoyés disponibles sur Kaggle, par exemple.

Les données manquantes peuvent résulter d'un facteur humain (par exemple, une personne refusant délibérément de répondre à une question d'enquête), d'un problème dans les capteurs électriques, ou d'autres facteurs. Et lorsque cela se produit, vous pouvez perdre des informations significatives.

Maintenant, il n'existe pas de méthode parfaite pour gérer les valeurs manquantes qui vous donnera un résultat précis quant à la valeur manquante. Mais il existe plusieurs techniques que vous pouvez utiliser et qui vous donneront des performances décents.

Dans cet article, nous allons examiner comment gérer les données manquantes de la bonne manière (la bonne manière signifiant sélectionner la technique appropriée pour le scénario que notre ensemble de données pourrait représenter).

Rappelez-vous qu'aucune de ces méthodes n'est parfaite – elles introduisent encore certains biais, comme favoriser une classe par rapport à une autre – mais elles sont utiles.

Avant de commencer, j'aimerais commencer par une citation de George Box pour étayer la déclaration précédente :

> Tous les modèles sont des approximations : Essentiellement, tous les modèles sont faux, mais certains sont utiles.

Maintenant, sans plus attendre, commençons.

## Quels types de données manquantes existent-ils ?

Vous vous demandez peut-être si les valeurs manquantes ont des types. Oui, elles en ont – et dans le monde réel, ces valeurs manquantes peuvent être divisées en trois catégories.

Comprendre ces catégories vous donnera quelques informations sur la manière d'aborder la ou les valeurs manquantes dans votre ensemble de données.

Parmi les catégories, on trouve :

* Manquantes complètement au hasard (MCAR).

* Manquantes au hasard (MAR).

* Non manquantes au hasard (NMAR).

### Données manquantes qui sont manquantes complètement au hasard (MCAR)

Ce sont des données qui sont manquantes complètement au hasard. C'est-à-dire que la raison de la valeur manquante est indépendante des données. Il n'y a pas de motif discernable à ce type de données manquantes.

Cela signifie que vous ne pouvez pas prédire si la valeur était manquante en raison de circonstances spécifiques ou non. Elles sont simplement manquantes complètement au hasard.

### Données manquantes qui sont manquantes au hasard (MAR)

Ces types de données sont manquantes au hasard mais pas complètement manquantes. La raison de la valeur manquante est déterminée par les données que vous voyez.

Prenons par exemple que vous avez construit une montre intelligente qui peut suivre le rythme cardiaque des gens toutes les heures. Ensuite, vous avez distribué la montre à un groupe d'individus à porter afin de collecter des données pour analyse.

Après avoir collecté les données, vous avez découvert que certaines données étaient manquantes, ce qui était dû au fait que certaines personnes étaient réticentes à porter la montre la nuit. Par conséquent, nous pouvons conclure que la raison de la valeur manquante était causée par les données observées.

### Données manquantes qui ne sont pas manquantes au hasard (NMAR)

Ce sont des données qui ne sont pas manquantes au hasard et sont également connues sous le nom de données ignorables. En d'autres termes, la raison de la valeur manquante des données manquantes est déterminée par la variable d'intérêt.

Un exemple courant est une enquête dans laquelle on demande aux étudiants combien de voitures ils possèdent. Dans ce cas, certains étudiants peuvent délibérément ne pas compléter l'enquête, ce qui entraîne des valeurs manquantes.

## Comment devez-vous gérer les données manquantes ?

Comme nous venons de l'apprendre, ces techniques ne peuvent pas être si précises pour déterminer la valeur manquante. Elles semblent avoir certains biais.

La gestion des valeurs manquantes se divise généralement en deux catégories. Nous allons examiner les plus courantes dans chaque catégorie. Les deux catégories sont les suivantes :

* Suppression

* Imputation

## **Comment gérer les données manquantes avec la suppression**

L'une des méthodes les plus répandues pour traiter les données manquantes est la suppression. Et l'une des méthodes les plus couramment utilisées dans l'approche de suppression est la méthode de suppression liste par liste.

### Qu'est-ce que la suppression liste par liste ?

Dans la méthode de suppression liste par liste, vous supprimez un enregistrement ou une observation dans l'ensemble de données s'il contient certaines valeurs manquantes.

Vous pouvez effectuer une suppression liste par liste sur l'une des catégories de valeurs manquantes mentionnées précédemment, mais l'un de ses inconvénients est la perte potentielle d'informations.

La règle générale pour savoir quand effectuer une suppression liste par liste est lorsque le nombre d'observations avec des valeurs manquantes dépasse le nombre d'observations sans valeurs manquantes. Cela est dû au fait que l'ensemble de données ne contient pas beaucoup d'informations pour alimenter les valeurs manquantes, il est donc préférable de supprimer ces valeurs ou de jeter l'ensemble de données entièrement.

Vous pouvez implémenter la suppression liste par liste en Python en utilisant simplement la méthode `.dropna` de Pandas comme ceci :

```javascript
df.dropna(axis=1, inplace=True)
```

## **Comment gérer les données manquantes avec l'imputation ?**

Une autre méthode générale fréquente pour traiter les données manquantes consiste à remplir la valeur manquante avec une valeur substituée.

Cette méthodologie englobe diverses méthodes, mais nous nous concentrerons sur les plus répandues ici.

### Connaissance préalable d'un nombre idéal

Cette méthode consiste à remplacer la valeur manquante par une valeur spécifique. Pour l'utiliser, vous devez avoir une connaissance du domaine de l'ensemble de données. Vous utilisez cela pour remplir les valeurs MAR et MCAR.

Pour l'implémenter en Python, vous utilisez la méthode `.fillna` dans Pandas comme ceci :

```javascript
df.fillna(inplace=True)
```

### Imputation par régression

La méthode d'imputation par régression inclut la création d'un modèle pour prédire la valeur observée d'une variable en fonction d'une autre variable. Ensuite, vous utilisez le modèle pour remplir la valeur manquante de cette variable.

Cette technique est utilisée pour les catégories MAR et MCAR lorsque les caractéristiques de l'ensemble de données dépendent les unes des autres. Par exemple, en utilisant un modèle de régression linéaire.

### Imputation simple

Cette méthode implique l'utilisation d'un résumé numérique de la variable où la valeur manquante s'est produite (c'est-à-dire en utilisant le résumé de la tendance centrale de la caractéristique ou de la variable, tel que la moyenne, la médiane et le mode).

Lorsque vous utilisez cette stratégie pour remplir les valeurs manquantes, vous devez évaluer la distribution de la variable pour déterminer quel résumé de la tendance centrale appliquer.

Vous utilisez cette méthode dans la catégorie MCAR. Et vous l'implémentez en Python en utilisant le transformateur `SimpleImputer` dans la bibliothèque Scikit-learn.

```javascript
from sklearn.impute import SimpleImputer
# Spécifiez la stratégie pour qu'elle soit la classe médiane
fea_transformer = SimpleImputer(strategy="median")
values = fea_transformer.fit_transform(df[["Distance"]])
pd.DataFrame(values)
```

![Image](https://lh5.googleusercontent.com/LA7UBjLpFXy3YUZ7RG1k9eyk8Y9jQTHEP3v1RarmMD1sHmmry0NDcZAUj1Yf7PxByjmalnxug-TvamDss85jmFiwQ8bSQ5IPPlpgVBNg2XkSUFCoyF_vKkPVUpQBT1_dva29EKKLxdyuE9IomA align="left")

### Imputation KNN

L'imputation KNN est une approche plus équitable que la méthode d'imputation simple. Elle fonctionne en remplaçant les données manquantes par la moyenne des voisins les plus proches.

Vous pouvez utiliser l'imputation KNN pour les catégories MCAR ou MAR. Et pour l'implémenter en Python, vous utilisez le transformateur d'imputation KNN dans ScikitLearn, comme vu ci-dessous :

```javascript
from sklearn.impute import KNNImputer
# Je spécifie le voisin le plus proche à 3 
fea_transformer = KNNImputer(n_neighbors=3)
values = fea_transformer.fit_transform(df[["Distance"]])
pd.DataFrame(values)
```

![Image](https://lh5.googleusercontent.com/EcAOhM2hrcL1nNyLTbry-76ADhEJ8aJliuae4SEaRzNxzN031BgBNT03iMv4PjoqkaTU2TmCwMuIY_M0ZGbvZCzKvQ-8PO_1h03LjjdFMZj_ZuW9zhNwq1TKQD3WZHKcry2_MpPD6ul-ykYpFg align="left")

### Comment utiliser les algorithmes d'apprentissage

La dernière stratégie que nous mentionnerons dans cet article est l'utilisation d'algorithmes d'apprentissage automatique pour gérer les données manquantes.

Certains algorithmes d'apprentissage nous permettent d'ajuster l'ensemble de données avec des valeurs manquantes. L'algorithme de l'ensemble de données recherche ensuite des motifs dans l'ensemble de données et les utilise pour remplir les valeurs manquantes. De tels algorithmes incluent XGboost, Gradient Boosting, et autres. Mais une discussion plus approfondie est hors du cadre de cet article.

## Conclusion et pour aller plus loin

Dans cet article, nous avons couvert certaines des techniques les plus répandues que vous utiliseriez au quotidien pour gérer les données manquantes.

Mais l'apprentissage ne s'arrête pas ici. Il existe plusieurs autres techniques disponibles pour nous aider à remplir notre ensemble de données, mais la clé est de comprendre les mécanismes sous-jacents de ces techniques afin que nous puissions gérer correctement les valeurs manquantes. Merci d'avoir lu.
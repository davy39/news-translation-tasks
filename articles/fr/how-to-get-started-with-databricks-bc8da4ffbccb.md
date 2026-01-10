---
title: Comment commencer avec Databricks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T19:53:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-databricks-bc8da4ffbccb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lUuQIivP0nMh5bp4S1cH4w.png
tags:
- name: coding
  slug: coding
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment commencer avec Databricks
seo_desc: 'By Shubhi Asthana

  When I started learning Spark with Pyspark, I came across the Databricks platform
  and explored it. This platform made it easy to setup an environment to run Spark
  dataframes and practice coding. This post contains some steps that ca...'
---

Par Shubhi Asthana

Lorsque j'ai commencé à apprendre Spark avec PySpark, je suis tombée sur la plateforme Databricks et je l'ai explorée. Cette plateforme a facilité la configuration d'un environnement pour exécuter des DataFrames Spark et pratiquer la programmation. Cet article contient quelques étapes qui peuvent vous aider à commencer avec Databricks.

Databricks est une plateforme qui s'exécute sur Apache Spark. Elle dispose commodément d'un système de Notebooks. On peut facilement provisionner des clusters dans le cloud, et elle intègre également un espace de travail intégré pour l'exploration et la visualisation.

Vous pouvez également planifier n'importe quel Notebook existant ou du code Spark développé localement pour passer du prototype à la production sans réingénierie.

#### **1.** **Créer un compte Databricks**

Pour commencer avec le tutoriel, accédez à ce [lien](https://databricks.com/try-databricks) et sélectionnez l'édition Community gratuite pour ouvrir votre compte. Cette option comprend un cluster unique avec jusqu'à 6 Go de stockage gratuit. Elle vous permet de créer un Notebook de base. Vous aurez besoin d'une adresse e-mail valide pour vérifier votre compte.

Vous observerez cet écran une fois que vous vous êtes connecté avec succès à votre compte.

![Image](https://cdn-media-1.freecodecamp.org/images/T5Id1J2mYNuzdylVfh7qdQEGTJ2z9rSPNgNJ)

#### **2.** **Créer un nouveau Cluster**

Nous commençons par créer un nouveau cluster pour exécuter nos programmes. Cliquez sur « Cluster » sur la page principale et saisissez un nouveau nom pour le cluster.

Ensuite, vous devez sélectionner la version de « Databricks Runtime ». Databricks Runtime est un ensemble de composants principaux qui s'exécutent sur les clusters gérés par Databricks. Il inclut Apache Spark, mais ajoute également un certain nombre de composants et de mises à jour pour améliorer l'utilisabilité et les performances de l'outil.

Vous pouvez sélectionner n'importe quelle version de Databricks Runtime — j'ai sélectionné la version 3.5 LTS (inclut Apache Spark 2.2.1, Scala 2.11). Vous avez également le choix entre Python 2 et 3.

![Image](https://cdn-media-1.freecodecamp.org/images/TiwHYkwFNaPIngJIbuEKzYz0uXmCrrS9JjPK)

Il faudra quelques minutes pour créer le cluster. Après un certain temps, vous devriez voir un cluster actif sur le tableau de bord.

![Image](https://cdn-media-1.freecodecamp.org/images/zgpWHAUlMLLmbLVzqs4i771NHXnJiUCeRKBx)

#### **3.** **Créer un nouveau Notebook**

Allons-y et créons un nouveau Notebook sur lequel vous pourrez exécuter votre programme.

Depuis la page principale, cliquez sur « Nouveau Notebook » et saisissez un nom pour le Notebook. Sélectionnez le langage de votre choix — j'ai choisi Python ici. Vous pouvez voir que Databricks supporte plusieurs langages, y compris Scala, R et SQL.

![Image](https://cdn-media-1.freecodecamp.org/images/wScJ0OtrJQ7kOxB55xI61KKMMaiNFqN6HE-Z)

Une fois les détails saisis, vous observerez que la disposition du Notebook est très similaire à celle de Jupyter Notebook. Pour tester le Notebook, importons pyspark.

![Image](https://cdn-media-1.freecodecamp.org/images/rHGMB336-8ZgsSsU74gVkwXaWUUuOqOvQyLH)

La commande s'est exécutée en 0,15 seconde et donne également le nom du cluster sur lequel elle s'exécute. Si des erreurs surviennent dans le code, elles s'afficheront sous la boîte de commande.

Vous pouvez cliquer sur l'icône du clavier en haut à droite de la page pour voir les raccourcis spécifiques au système d'exploitation.

Les raccourcis les plus importants ici sont :

* Maj+Entrée pour exécuter une cellule
* Ctrl+Entrée continue d'exécuter la même cellule sans passer à la cellule suivante

Notez que ces raccourcis sont pour Windows. Vous pouvez vérifier les raccourcis spécifiques à votre système d'exploitation en cliquant sur l'icône du clavier.

#### **4.** **Télécharger des données vers Databricks**

Rendez-vous dans la section « Tables » sur la barre de gauche, et cliquez sur « Créer une Table ». Vous pouvez télécharger un fichier, ou vous connecter à une source de données Spark ou à une autre base de données.

Téléchargeons ici le fichier de données iris couramment utilisé (si vous n'avez pas le jeu de données, utilisez ce [lien](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/))

Une fois les données téléchargées, créez la table avec une interface utilisateur afin de visualiser la table et de la prévisualiser sur votre cluster. Comme vous pouvez le voir, vous pouvez observer les attributs de la table. Spark essaiera de détecter le type de données de chacune des colonnes et vous permet également de les modifier.

![Image](https://cdn-media-1.freecodecamp.org/images/nluVnzMiIciV8XZYf8Nn8UTCvViBPGdgL4iX)

Maintenant, je dois mettre des en-têtes pour les colonnes afin de pouvoir identifier chaque colonne par son en-tête au lieu de `_c0`, `_c1`, etc.

J'ai mis leurs en-têtes comme Sepal Length, Sepal Width, Petal Length, Petal Width et Class. Ici, Spark a détecté le type de données des quatre premières colonnes incorrectement comme une chaîne, alors je l'ai changé pour le type de données souhaité — Float.

![Image](https://cdn-media-1.freecodecamp.org/images/dkATzKU4XJHtvVHWqdKXRYiLImxALzBQYQJC)

#### **5.** **Comment accéder aux données depuis un Notebook**

Spark est un framework qui peut être utilisé pour analyser des big data en utilisant SQL, le machine learning, le traitement de graphes ou l'analyse de streaming en temps réel. Nous allons travailler avec SparkSQL et les DataFrames dans ce tutoriel.

Commençons à travailler avec les données dans le Notebook. Les données que nous avons téléchargées sont maintenant mises en format tabulaire. Nous avons besoin d'une requête SQL pour lire les données et les mettre dans un DataFrame.

Tapez `df = sqlContext.sql("SELECT * FROM iris_data")` pour lire les données iris dans un DataFrame.

![Image](https://cdn-media-1.freecodecamp.org/images/yBMfdLYAfxCopo30gJIXKlcUbqMwDbaEOnTi)

Pour afficher les cinq premières lignes du DataFrame, je peux simplement exécuter la commande :

`display(df.limit(5))`

![Image](https://cdn-media-1.freecodecamp.org/images/r5DtlOuE64Pyt6w8ar--LIVyW2uTsPcAzTNU)

Remarquez une icône de graphique à barres en bas. Une fois que vous cliquez, vous pouvez visualiser les données que vous avez importées dans Databricks. Pour afficher le graphique à barres des données complètes, exécutez `display(df)` au lieu de `display(df.limit(5))`.

![Image](https://cdn-media-1.freecodecamp.org/images/ERVu7Dpv3jYJUO4RbnWCbeK1hrDA9-lET7HV)

Le bouton déroulant vous permet de visualiser les données dans différents graphiques comme des barres, des camemberts, des nuages de points, etc. Il vous donne également des options de traçage pour personnaliser le graphique et visualiser uniquement des colonnes spécifiques.

![Image](https://cdn-media-1.freecodecamp.org/images/oD6ZqA4Mfxa162PzDkM4l6-ziVMBvAT12k47)

Vous pouvez également afficher des figures matplotlib et ggplot dans Databricks. Pour une démonstration, voir [Matplotlib et ggplot dans les Notebooks Python](https://docs.databricks.com/user-guide/visualizations/matplotlib-and-ggplot.html).

Pour afficher toutes les colonnes des données, tapez simplement `df.columns`

![Image](https://cdn-media-1.freecodecamp.org/images/PBHqV97bqMjJNXnYsaPj4rgcwnAoDEtWTR4u)

Pour compter le nombre total de lignes dans le DataFrame (et voir combien de temps il faut pour un scan complet depuis le disque distant/S3), exécutez `df.count()`.

![Image](https://cdn-media-1.freecodecamp.org/images/Eu2ZtzIYJCXkakliIgs9QsBD4oeFT61BMdkP)

#### **6. Convertir un DataFrame Spark en DataFrame Pandas.**

Maintenant, si vous êtes à l'aise avec l'utilisation des DataFrames pandas et que vous souhaitez convertir votre DataFrame Spark en pandas, vous pouvez le faire en utilisant la commande

```
import pandas as pd
pandas_df = df.toPandas()
```

Maintenant, vous pouvez utiliser les opérations pandas sur le DataFrame `pandas_df`.

![Image](https://cdn-media-1.freecodecamp.org/images/PXuhlDuKFERt9tG3nHsgecOJE0UWm5c11GG-)

#### **7. Visualiser l'interface utilisateur Spark**

L'interface utilisateur Spark contient une multitude d'informations nécessaires pour déboguer les travaux Spark. Il y a un ensemble de visualisations, alors voyons-les en un clin d'œil.

Pour accéder à l'interface utilisateur Spark, vous devez aller en haut de la page où se trouvent certaines options de menu comme « Fichier », « Affichage », « Code », « Autorisations », et autres. Vous trouverez le nom du cluster en haut à côté de « Attaché » et un bouton déroulant à côté. Cliquez sur le bouton déroulant et sélectionnez « Visualiser l'interface utilisateur Spark ». Un nouvel onglet s'ouvrira avec de nombreuses informations sur votre Notebook.

![Image](https://cdn-media-1.freecodecamp.org/images/CR65Njc5eSEyIzGoE5uHCkz6onnOHyiSubNE)

La vue de l'interface utilisateur fournit de nombreuses informations sur chaque travail exécuté sur le cluster, les étapes, l'environnement et les requêtes SQL exécutées. Cette interface utilisateur peut être utile pour les utilisateurs afin de déboguer leurs applications. De plus, cette interface utilisateur offre une bonne visualisation des statistiques de streaming Spark. Pour en savoir plus sur chaque aspect de l'interface utilisateur Spark, consultez ce [lien](https://databricks.com/blog/2015/06/22/understanding-your-spark-application-through-visualization.html).

Une fois que vous avez terminé avec le Notebook, vous pouvez le publier ou exporter le fichier dans différents formats, de sorte que quelqu'un d'autre puisse l'utiliser via un lien unique. J'ai [joint mon Notebook au format HTML](https://cdn.rawgit.com/sasthan/Tutorial_databricks/7f01b3e1/Notebook_1.html).

#### Conclusion

Ceci est un aperçu rapide de la manière dont vous pouvez commencer rapidement avec Databricks et exécuter vos programmes. L'avantage d'utiliser Databricks est qu'il offre un service complet pour construire des applications d'analyse, d'entreposage de données et de machine learning. L'ensemble du cluster Spark peut être géré, surveillé et sécurisé en utilisant un modèle d'auto-service de Databricks.

Voici quelques liens intéressants pour les [Data Scientists](https://docs.databricks.com/spark/latest/gentle-introduction/for-data-scientists.html) et pour les [Data Engineers](https://docs.databricks.com/spark/latest/gentle-introduction/for-data-engineers.html). De plus, voici un [tutoriel](https://www.youtube.com/watch?v=K14plpZgy_c) que j'ai trouvé très utile et qui est idéal pour les débutants.
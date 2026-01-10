---
title: Tutoriel Weka – Machine Learning basé sur une interface graphique avec Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-27T20:37:30.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-using-weka
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/weka-1.png
tags:
- name: Data Science
  slug: data-science
- name: Java
  slug: java
- name: Machine Learning
  slug: machine-learning
seo_title: Tutoriel Weka – Machine Learning basé sur une interface graphique avec
  Java
seo_desc: "By Pier Paolo Ippolito\nNowadays, programming languages such as Python\
  \ and R are undoubtedly some of the most in-demand languages in Data Science and\
  \ Machine Learning. \nBut is it also possible to perform common Machine Learning\
  \ and Data Science tasks ..."
---

Par Pier Paolo Ippolito

De nos jours, les langages de programmation tels que Python et R sont sans aucun doute parmi les langages les plus demandés en Science des Données et en Machine Learning. 

Mais est-il également possible d'effectuer des tâches courantes de Machine Learning et de Science des Données sans nécessairement être compétent en codage ? 

Bien sûr que oui ! Weka est un package open-source basé sur une interface graphique. Il peut être utilisé afin d'effectuer des tâches courantes de Science des Données simplement en utilisant l'interface graphique.

## Bases

Weka peut être facilement installé sur n'importe quel type de plateforme en suivant les instructions à ce [lien](https://waikato.github.io/weka-wiki/downloading_weka/). Le seul prérequis est d'avoir Java 8.0 installé sur votre machine locale.

Une fois que vous avez installé Weka, vous disposerez d'un ensemble de techniques standard de traitement des données et d'inférence telles que :

* **Prétraitement des données** : une fois que vous avez chargé un jeu de données, Weka vous permet d'explorer rapidement ses attributs et ses instances. De plus, différentes techniques de filtrage sont disponibles afin de, par exemple, convertir des données catégorielles en données numériques ou effectuer une [sélection de caractéristiques](https://towardsdatascience.com/feature-selection-techniques-1bfab5fe0784) afin de réduire la dimensionnalité de notre jeu de données (par exemple, pour accélérer les temps d'entraînement et les performances). 
* **Algorithmes de Classification et de Régression** : une collection de différents algorithmes tels que Naive Bayes Gaussien, Arbres de Décision, K-Nearest Neighbour, techniques d'Ensemble, et diverses variantes de régression linéaire.
* **Clustering** : cette technique peut être utilisée afin d'identifier les principales catégories dans nos données de manière non supervisée. Certains algorithmes disponibles dans la collection Weka sont le Clustering K-Means et l'Expectation Maximisation.
* **Découverte d'Associations** : découvrir des règles dans notre jeu de données afin d'identifier plus facilement des motifs et des connexions entre les différentes caractéristiques.
* **Visualisation de Données** : une suite de techniques intégrées de visualisation de données pour visualiser rapidement les corrélations entre les caractéristiques et représenter les motifs de machine learning appris tels que les Arbres de Décision et le Clustering K-Means.

Une autre caractéristique intéressante de Weka est la possibilité d'installer de nouveaux packages au fur et à mesure qu'ils sont créés. 

Un exemple de package supplémentaire que vous pouvez installer est AutoML. AutoML peut en fait être particulièrement utile pour les débutants qui pourraient trouver difficile d'identifier quel modèle de Machine Learning pourrait être le meilleur à utiliser pour une tâche spécifique. 

En utilisant le package AutoML de Weka, vous pouvez facilement tester différents modèles de Machine Learning à la volée. Il vous permet également de régler automatiquement ses [hyper-paramètres](https://towardsdatascience.com/hyperparameters-optimization-526348bb8e2d) afin d'augmenter les performances. 

Enfin, pour les utilisateurs plus expérimentés, Weka offre également une interface en ligne de commande pour utiliser le code Java. Cela peut être particulièrement utile surtout si vous travaillez avec de grandes quantités de données.

## Exemple

Nous allons maintenant parcourir un exemple simple afin de démontrer comment commencer avec Weka. 

Tout d'abord, nous pouvons commencer notre analyse en ouvrant Weka Explorer et en ouvrant notre jeu de données (dans cet exemple, le jeu de données Iris).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-153.png)
_Figure 1 : Importation et Visualisation des données_

Sélectionnez l'onglet Classifier, choisissez Naive Bayes comme notre classificateur, et cliquez sur start. Vous verrez que nous pouvons rapidement atteindre une précision de classification de 96 % sans avoir à écrire de code !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-154.png)
_Figure 2 : Résultats de la Classification Naive Bayes_

## Conclusion

Au cas où vous cherchiez plus d'informations sur la façon de commencer avec Weka, [cette série YouTube](https://www.youtube.com/watch?v=cKxRvEZd3Mw&list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal) par Google Developers est un excellent point de départ.

### Contactez-moi

Si vous souhaitez rester informé de mes derniers articles et projets, [suivez-moi sur Medium](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) et abonnez-vous à ma [liste de diffusion](http://eepurl.com/gwO-Dr?source=post_page---------------------------). Voici quelques-uns de mes détails de contact :

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Blog Personnel](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Site Web Personnel](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Profil Medium](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

Photo de couverture [de cet article](https://www.techiexpert.com/list-of-data-mining-tools/).
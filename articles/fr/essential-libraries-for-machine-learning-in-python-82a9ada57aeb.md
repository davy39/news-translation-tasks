---
title: Bibliothèques essentielles pour le Machine Learning en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-03T15:12:06.000Z'
originalURL: https://freecodecamp.org/news/essential-libraries-for-machine-learning-in-python-82a9ada57aeb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SltpaprT6Vc6IhQqVsYKtA.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Bibliothèques essentielles pour le Machine Learning en Python
seo_desc: 'By Shubhi Asthana

  Python is often the language of choice for developers who need to apply statistical
  techniques or data analysis in their work. It is also used by data scientists whose
  tasks need to be integrated with web apps or production environm...'
---

Par Shubhi Asthana

Python est souvent le langage de choix pour les développeurs qui doivent appliquer des techniques statistiques ou des analyses de données dans leur travail. Il est également utilisé par les data scientists dont les tâches doivent être intégrées avec des applications web ou des environnements de production.

Python se distingue vraiment dans le domaine du machine learning. Sa combinaison de syntaxe cohérente, de temps de développement plus court et de flexibilité le rend bien adapté au développement de modèles sophistiqués et de moteurs de prédiction qui peuvent être directement intégrés dans des systèmes de production.

L'un des plus grands atouts de Python est son vaste ensemble de bibliothèques.

Les bibliothèques sont des ensembles de routines et de fonctions écrites dans un langage donné. Un ensemble robuste de bibliothèques peut faciliter la tâche des développeurs pour effectuer des tâches complexes sans réécrire de nombreuses lignes de code.

Le machine learning repose largement sur les mathématiques. Plus précisément, l'optimisation mathématique, les statistiques et les probabilités. Les bibliothèques Python aident les chercheurs/mathématiciens qui sont moins équipés en connaissances de développement à "faire du machine learning" facilement.

Voici quelques-unes des bibliothèques les plus couramment utilisées en machine learning :

#### **Scikit-learn pour travailler avec des algorithmes classiques de ML**

![Image](https://cdn-media-1.freecodecamp.org/images/saQHUdhXbYflEmnDMhN5Qewekg0h6KPx9oIT)

[Scikit-learn](http://scikit-learn.org/stable/user_guide.html) est l'une des bibliothèques ML les plus populaires. Elle supporte de nombreux algorithmes d'apprentissage supervisé et non supervisé. Exemples : régressions linéaires et logistiques, arbres de décision, clustering, k-means, etc.

Elle s'appuie sur deux bibliothèques de base de Python, NumPy et SciPy. Elle ajoute un ensemble d'algorithmes pour des tâches courantes de machine learning et de data mining, y compris le clustering, la régression et la classification. Même des tâches comme la transformation de données, la sélection de caractéristiques et les méthodes d'ensemble peuvent être implémentées en quelques lignes.

Pour un novice en ML, Scikit-learn est un outil plus que suffisant pour travailler, jusqu'à ce que vous commenciez à implémenter des algorithmes plus complexes.

#### **Tensorflow pour le Deep Learning**

![Image](https://cdn-media-1.freecodecamp.org/images/5M9fILVJO06e0zPLStKihIlOYxsLUw8f3kI9)

Si vous êtes dans le monde du machine learning, vous avez probablement entendu parler, essayé ou implémenté une forme d'algorithme de deep learning. Sont-ils nécessaires ? Pas tout le temps. Sont-ils cool quand ils sont bien faits ? Oui !

Ce qui est intéressant avec [Tensorflow](https://www.tensorflow.org/), c'est que lorsque vous écrivez un programme en Python, vous pouvez le compiler et l'exécuter sur votre CPU ou GPU. Vous n'avez donc pas à écrire au niveau C++ ou CUDA pour exécuter sur des GPU.

Il utilise un système de nœuds multicouches qui vous permet de configurer, former et déployer rapidement des réseaux de neurones artificiels avec de grands ensembles de données. C'est ce qui permet à Google d'identifier des objets dans des photos ou de comprendre des mots parlés dans son application de reconnaissance vocale.

#### **Theano est également pour le Deep Learning**

![Image](https://cdn-media-1.freecodecamp.org/images/e-jPhWk8t0PSdEJeLtt9F32FroB1fiLfZbEo)

[Theano](http://www.deeplearning.net/software/theano/) est une autre bonne bibliothèque Python pour le calcul numérique, et est similaire à NumPy. Theano vous permet de définir, optimiser et évaluer des expressions mathématiques impliquant des tableaux multidimensionnels de manière efficace.

Ce qui distingue Theano, c'est qu'il tire parti du GPU de l'ordinateur. Cela lui permet d'effectuer des calculs intensifs en données jusqu'à 100 fois plus rapidement que lorsqu'ils sont exécutés sur le CPU seul. La vitesse de Theano le rend particulièrement précieux pour le deep learning et d'autres tâches computationnellement complexes.

La dernière version de la bibliothèque Theano a été publiée l'année dernière — 2017, version 1.0.0 avec de nombreuses nouvelles fonctionnalités, changements d'interface et améliorations.

#### **Pandas pour l'extraction et la préparation des données**

Pandas est une bibliothèque très populaire qui fournit des structures de données de haut niveau simples à utiliser et intuitives.

Elle dispose de nombreuses méthodes intégrées pour le regroupement, la combinaison de données et le filtrage, ainsi que pour l'analyse de séries temporelles.

Pandas peut facilement récupérer des données à partir de différentes sources comme des bases de données SQL, des fichiers CSV, Excel, JSON et manipuler les données pour effectuer des opérations dessus. Il existe deux structures principales dans la bibliothèque :

* "Series" — unidimensionnelle

![Image](https://cdn-media-1.freecodecamp.org/images/XOnqsPFM6zmV3Yy6Sgs5palSmfHxMJLK-JYz)

* "Data Frames" — bidimensionnelle.

![Image](https://cdn-media-1.freecodecamp.org/images/c6PpmB9g6ixbMmmYm8YfhmT7bc4Vx2IepqTe)

Pour plus de détails sur l'utilisation des Series et Dataframes, consultez mon autre [article de blog](https://medium.freecodecamp.org/series-and-dataframe-in-python-a800b098f68).

#### **Matplotlib pour la visualisation des données**

![Image](https://cdn-media-1.freecodecamp.org/images/NqFp4qWaItpXVSCaxGyIMQbmZRaKFn6Pcbrd)

_Image source : [https://github.com/nschloe/matplotlib2tikz](https://github.com/nschloe/matplotlib2tikz" rel="noopener" target="_blank" title=")_

Le meilleur et le plus sophistiqué ML est sans signification si vous ne pouvez pas le communiquer à d'autres personnes.

Alors, comment tirez-vous réellement de la valeur de toutes ces données que vous avez ? Comment inspirez-vous vos analystes d'affaires et leur racontez-vous des "histoires" pleines d'"insights" ?

C'est là que [Matplotlib](https://matplotlib.org/tutorials/index.html) vient à la rescousse. C'est une bibliothèque Python standard utilisée par chaque data scientist pour créer des graphiques et des figures en 2D. Elle est assez bas niveau, ce qui signifie qu'elle nécessite plus de commandes pour générer des graphiques et des figures esthétiques que certaines bibliothèques avancées.

Cependant, l'autre côté de la médaille est la flexibilité. Avec suffisamment de commandes, vous pouvez créer à peu près n'importe quel type de graphique que vous souhaitez avec Matplotlib. Vous pouvez construire des graphiques divers, allant des histogrammes et des nuées de points aux graphiques en coordonnées non cartésiennes.

Elle supporte différents backends GUI sur tous les systèmes d'exploitation, et peut également exporter des graphiques vers des formats vectoriels et graphiques courants comme PDF, SVG, JPG, PNG, BMP, GIF, etc.

#### **Seaborn est une autre bibliothèque de visualisation de données**

![Image](https://cdn-media-1.freecodecamp.org/images/03MXWUZOfFO2MzbzTQntDwMZcLVe79gpJuos)

_Image source : [seaborn.pydata.org/](https://seaborn.pydata.org/" rel="noopener" target="_blank" title=")_

[Seaborn](https://seaborn.pydata.org/tutorial.html) est une bibliothèque de visualisation populaire qui s'appuie sur les fondations de Matplotlib. C'est une bibliothèque de plus haut niveau, ce qui signifie qu'il est plus facile de générer certains types de graphiques, y compris les cartes thermiques, les séries temporelles et les graphiques en violon.

### Conclusion

Il s'agit d'une collection des bibliothèques Python les plus importantes pour le Machine Learning. Ces bibliothèques valent la peine d'être examinées et d'être familières si vous prévoyez de travailler avec Python et la science des données.

Ai-je oublié une bibliothèque ML Python importante ? Si oui, n'hésitez pas à la mentionner dans les commentaires ci-dessous. Bien que j'aie essayé de couvrir les bibliothèques les plus utiles, je n'ai peut-être pas couvert certaines autres qui méritent d'être examinées.

Des questions ou des commentaires ? J'adorerais avoir de vos nouvelles — n'hésitez pas à laisser un commentaire ou à me contacter sur T[witter](https://twitter.com/shubhi_asthana)/[Linkedin](https://www.linkedin.com/in/shubhi-asthana/).
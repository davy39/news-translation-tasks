---
title: Comment programmer un réseau de neurones pour prédire le cancer du sein en
  seulement 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T21:02:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-program-a-neural-network-to-predict-breast-cancer-in-only-5-minutes-23289d62a4c1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0lFXCmgwXLznglp8N4dx0g.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Cancer
  slug: cancer
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: Python
  slug: python
seo_title: Comment programmer un réseau de neurones pour prédire le cancer du sein
  en seulement 5 minutes
seo_desc: 'By Andrew Li

  It’s that simple.


  Stop wasting time reading this caption because this tutorial is only supposed to
  take 5 minutes! ⏳

  Minute One — Introduction:

  This is a high-level tutorial intended for those new to machine learning and artificial
  inte...'
---

Par Andrew Li

#### C'est aussi simple que cela.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0lFXCmgwXLznglp8N4dx0g.png)
_Arrêtez de perdre du temps à lire cette légende car ce tutoriel ne doit prendre que 5 minutes ! ⏳_

#### Minute Une — Introduction :

Ce tutoriel de haut niveau est destiné à ceux qui sont nouveaux dans le domaine de l'apprentissage automatique et de l'intelligence artificielle et suppose que vous avez :

1. Python 2 ou 3 installé
2. Au moins une expérience de codage de niveau débutant
3. 5 minutes

Ce tutoriel passera les détails de bas niveau et mathématiques des réseaux de neurones et se concentrera sur la création d'un réseau de neurones pour prédire le cancer du sein en seulement 5 minutes !

Nous utiliserons l'implémentation du réseau de neurones de la bibliothèque `scikit-learn` pour prédire si quelqu'un a un cancer du sein en utilisant les données de l'ensemble de données "Breast Cancer Wisconsin" de l'UC Irvine. Les propriétés des noyaux cellulaires (par exemple, la texture ou la surface) pour une masse mammaire seront entrées dans le réseau de neurones et ensuite une prédiction de savoir si la masse est maligne ou bénigne sera produite par le réseau de neurones.

#### Minute Deux — Mise en route :

Si vous n'avez pas encore installé `scikit-learn`, exécutez `pip install scikit-learn` dans votre terminal. Cela devrait installer `scikit-learn` et toutes les bibliothèques prérequises dont nous aurons besoin.

Ouvrez un IDE ou un éditeur et créez un fichier vide appelé `neuralnet.py` ou un nom que vous préférez. Ensuite, nous importerons l'implémentation du réseau de neurones, l'ensemble de données sur le cancer du sein, et une fonction pour diviser nos données en ensembles d'entraînement et de test à alimenter dans notre réseau de neurones.

Pour référence au fur et à mesure, voici la documentation pertinente de `scikit-learn` :

1. [Documentation pour l'ensemble de données sur le cancer du sein (`load_breast_cancer`)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)
2. [Documentation pour la fonction de prétraitement (`train_test_split`)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
3. [Documentation pour l'implémentation du réseau de neurones (`MLPClassifier`)](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier)

#### Minute Trois — Prétraitement :

Avant d'être prêts à effectuer l'apprentissage automatique sur l'ensemble de données sur le cancer du sein, le prétraitement des données est d'abord nécessaire. Nous commençons par charger nos données et ensuite sauvegarder les propriétés de la masse mammaire (une liste de listes contenant des valeurs numériques) sous `attributes` et si la masse mammaire est maligne ou bénigne (une liste de 0 et de 1) sous `labels`. Le contenu de chaque index de chaque liste correspond, par exemple, une masse mammaire avec des attributs à `attributes[0]` est définie comme étant soit maligne soit bénigne à `labels[0]`.

Ensuite, nous divisons nos données en ensembles d'entraînement (pour entraîner le réseau de neurones) et de test (pour tester la performance du réseau de neurones). L'ensemble d'entraînement se compose de `attributes_train` et `labels_train` et l'ensemble de test se compose de `attributes_test` et `labels_test`. Nous attribuons un tiers de notre ensemble de données à notre ensemble de test, ce qui signifie que les deux tiers restants sont dans l'ensemble d'entraînement.

#### Minute Quatre — Le Réseau de Neurones :

Maintenant que nos données ont été divisées en ensembles d'entraînement et de test, nous sommes prêts à procéder à la partie réseau de neurones de ce tutoriel ! Après avoir instancié un réseau de neurones perceptron multicouche, nous entraînons notre réseau de neurones avec notre ensemble d'entraînement en utilisant la fonction `fit`, évaluons la précision de notre réseau de neurones avec la fonction `score`, et imprimons la précision.

Essayez d'exécuter le réseau de neurones via le terminal avec `python neuralnetworktutorial.py` environ 10 fois (cela ne devrait prendre qu'une seconde à chaque fois) et notez les résultats !

#### Minute Cinq — Optimisation des Résultats :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1nii9kIpEgdBDtb6BzGM6w.png)
_Résultats pour le MLPClassifier par défaut_

Il y a de grandes chances que vous voyiez une grande variation dans la performance du réseau de neurones. Lorsque nous avons divisé nos données en ensembles d'entraînement et de test, les données ont été mélangées en utilisant une graine aléatoire, ce qui explique les fluctuations dans nos résultats ; avec seulement 569 entrées dans notre ensemble de données, le réseau de neurones n'est pas toujours entraîné avec un ensemble d'entraînement (379 entrées) qui est représentatif de l'ensemble de données, causant un surapprentissage.

De plus, lorsque nous avons instancié un nouveau réseau de neurones avec `neuralnet = MLPClassifier()` dans notre code, nous avons laissé le constructeur vide, ce qui signifie que le réseau de neurones a été construit avec des paramètres par défaut définis par `scikit-learn`, conduisant à un réseau de neurones non optimisé.

Nous pouvons corriger cela soit en entraînant et en testant sur un ensemble de données plus grand, soit en tirant le meilleur parti de notre situation en ajustant les paramètres de l'ensemble de données.

En tentant cette dernière option, j'ai choisi de changer le solveur d'optimisation des poids de `adam` par défaut à `lbfgs`, en bref parce que la documentation mentionne que `lbfgs` performe le mieux sur les petits ensembles de données. J'ai également changé la fonction d'activation dans la couche cachée de `relu` à `logistic` après quelques expérimentations, et enfin augmenté l'`alpha` de 0,0001 à 10,0 pour prévenir le surapprentissage, que je soupçonnais être la raison derrière les fluctuations drastiques de notre précision sur plusieurs exécutions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*z4xhEuBoCtcZldn-64VB8w.png)
_Résultats pour le MLPClassifier ajusté_

Cela semble beaucoup mieux ! Il y a encore quelques baisses de précision, mais nous sommes capables d'atteindre une précision beaucoup plus élevée de manière constante avec des baisses substantiellement plus petites de la précision sur plusieurs exécutions. Les ajustements que nous avons faits étaient simples et basiques, laissant de la place pour plus d'optimisation, mais cela sera pour une autre fois.

#### Conclusion

Ce que vous avez appris s'étend à n'importe quel ensemble de données et à n'importe quelle implémentation d'algorithme d'apprentissage automatique trouvée dans `scikit-learn` ; j'ai choisi de démontrer en utilisant un réseau de neurones pour prédire le cancer du sein parce que les deux sujets mentionnés sont actuellement des domaines d'intérêt majeurs dans les STEM.

Essayer un autre algorithme est aussi simple que de remplacer les lignes qui importent et instancient l'implémentation du réseau de neurones par des lignes important et instanciant une implémentation d'algorithme différente comme suit :

Il existe de nombreuses ressources en ligne pour cultiver votre compréhension de l'apprentissage automatique et de l'intelligence artificielle si vous n'avez pas accès à des cours en personne sur ces sujets. Si beaucoup de l'apprentissage automatique dans ce tutoriel vous a dépassé, ne vous inquiétez pas, [cet article de cours intensif est très informatif](https://medium.com/fintechexplained/neural-networks-activation-function-to-back-propagation-understanding-neural-networks-bdd036c3f29f). Si ce tutoriel vous a semblé trop de haut niveau, je recommande [ce cours Coursera enseigné par Andrew Ng](https://www.coursera.org/learn/machine-learning) que beaucoup de mes collègues ont trouvé utile, qui se concentre sur les mathématiques et la théorie derrière l'apprentissage automatique ainsi que sur les implémentations de bas niveau.

**Merci d'avoir lu et n'oubliez pas d'applaudir et de me suivre sur Medium pour plus de tutoriels et de commentaires axés sur la technologie !**

**Retrouvez-moi également sur [Twitter](https://twitter.com/andrewyinli) !**
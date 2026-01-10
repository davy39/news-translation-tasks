---
title: Comment Pytorch donne une vue d'ensemble avec l'apprentissage profond
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-05T21:08:16.000Z'
originalURL: https://freecodecamp.org/news/how-pytoch-gives-the-big-picture-with-deep-learning-e4a0f372f4b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lMTOQkDLUcOOwX4WJ-7tFw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: Comment Pytorch donne une vue d'ensemble avec l'apprentissage profond
seo_desc: 'By Déborah Mesquita

  Some time ago we saw how to classify texts with neural networks. The article covered
  the following topics:


  What is a machine learning model

  What is a neural network

  How the neural network learns

  How to manipulate data and pass it...'
---

Par Débora Mesquita

Il y a quelque temps, nous avons vu [comment classifier des textes avec des réseaux de neurones](https://medium.freecodecamp.org/big-picture-machine-learning-classifying-text-with-neural-networks-and-tensorflow-d94036ac2274). L'article couvrait les sujets suivants :

* Qu'est-ce qu'un modèle d'apprentissage automatique
* Qu'est-ce qu'un réseau de neurones
* Comment le réseau de neurones apprend
* Comment manipuler les données et les passer aux entrées du réseau de neurones
* Comment exécuter le modèle et obtenir les résultats pour la prédiction

Dans l'article d'aujourd'hui, nous allons construire le même réseau, mais au lieu d'utiliser [TensorFlow](https://www.tensorflow.org/), nous allons utiliser [**Pytorch**](http://pytorch.org/). Nous nous concentrerons uniquement sur le code. Donc, si vous avez besoin d'une introduction aux réseaux de neurones, il est bon de consulter l'[article précédent](https://medium.freecodecamp.org/big-picture-machine-learning-classifying-text-with-neural-networks-and-tensorflow-d94036ac2274). :)

Nous allons créer un modèle d'apprentissage automatique qui classe les textes en catégories. Le jeu de données est [20 Newsgroups](http://qwone.com/~jason/20Newsgroups/), qui contient 18 000 messages sur 20 sujets différents. Nous n'utiliserons que 3 catégories : comp.graphics, sci.space et rec.sport.baseball.

### Qu'est-ce que Pytorch ?

> Pytorch est un package de calcul scientifique basé sur Python qui est un remplaçant pour [NumPy](http://www.numpy.org/), et utilise la puissance des unités de traitement graphique. C'est aussi une plateforme de recherche en apprentissage profond qui offre une flexibilité et une vitesse maximales.

La plus grande différence entre Pytorch et Tensorflow est que Pytorch peut créer des graphiques à la volée. Cela rend le débogage beaucoup plus facile (et amusant !).

![Image](https://cdn-media-1.freecodecamp.org/images/0*nntIflaBvptIerl8.gif)
_Une introduction à la dynamique de Pytorch_

Lorsque vous exécutez une ligne de code, elle est exécutée. Il n'y a pas de vue asynchrone du monde. Lorsque vous la placez dans un débogueur, ou recevez des messages d'erreur et des traces de pile, les comprendre est simple. La trace de pile pointe exactement là où votre code a été défini.

### Construction du réseau

D'accord, voyons comment les choses fonctionnent dans Pytorch.

#### Les bases

Comme d'habitude, nous avons des **tensors**, qui sont des matrices multidimensionnelles contenant des éléments d'un seul type de données.

Le package **torch** contient des structures de données pour les tensors multidimensionnels et des opérations mathématiques.

* [**torch.nn**](http://pytorch.org/docs/master/nn.html) est une bibliothèque de réseaux de neurones profondément intégrée avec autograd, et conçue pour une flexibilité maximale
* [**torch.autograd**](http://pytorch.org/tutorials/beginner/former_torchies/autograd_tutorial.html) est une bibliothèque de différentiation automatique basée sur des bandes qui prend en charge toutes les opérations de tensors différentiables dans torch

#### Étape 1 : Définir le réseau

Avec TensorFlow, chaque opération de couche doit être explicitement nommée :

Avec Pytorch, nous utilisons **torch.nn**. Nous devons multiplier chaque nœud d'entrée avec un poids, et aussi ajouter un biais. La classe `**torch.nn.Linear**` fait le travail pour nous.

* `**torch.nn.Linear**` applique une transformation linéaire aux données entrantes, _y_=_Ax_+_b_

La classe de base pour tous les modules de réseaux de neurones est **torch.nn.Module**. La méthode `**forward**`(*input) définit le calcul effectué à chaque appel, et toutes les sous-classes doivent la redéfinir.

Cool, non ?

#### Étape 2 : Mettre à jour les poids

La manière dont le réseau de neurones "apprend" est en mettant à jour les valeurs des poids. Avec Pytorch, nous utilisons le package **torch.autograd** pour cela.

**Torch.autograd.Variable** enveloppe un tensor et enregistre les opérations qui lui sont appliquées. Cela est très pratique et nous permet de travailler avec la descente de gradient de manière très simple. Examinons de plus près la documentation.

Une variable est **une enveloppe légère autour d'un objet Tensor qui contient également le gradient** et une référence à la fonction qui l'a créée. Cette référence nous permet de tracer toute la chaîne d'opérations qui a créé les données.

![Image](https://cdn-media-1.freecodecamp.org/images/0*VXak2OuzwdAUYt2c.png)
_Variable_

Nous n'avons pas spécifié les tensors de poids comme nous l'avons fait avec TensorFlow car la classe `**torch.nn.Linear**` a une variable **weight** avec la forme (out_features x in_features).

* `**torch.nn.Linear**`(in_features, out_features, bias=True)

Pour calculer le gradient, nous allons utiliser la méthode [Adaptive Moment Estimation (Adam)](http://sebastianruder.com/optimizing-gradient-descent/index.html#adam). **Torch.optim** est un package qui implémente divers algorithmes d'optimisation.

Pour utiliser `[**torch.optim**](http://pytorch.org/docs/master/optim.html#module-torch.optim)`, vous devez construire un objet optimiseur qui contiendra l'état actuel et mettra également à jour les paramètres en fonction des gradients calculés.

Pour construire un `[**optimizer**](http://pytorch.org/docs/master/optim.html#torch.optim.Optimizer)**,**` vous devez lui donner un itérable qui contient les paramètres (tous doivent être des `[**variable**](http://pytorch.org/docs/master/autograd.html#torch.autograd.Variable)**s**` ) à optimiser. Ensuite, vous pouvez spécifier des options spécifiques à un optimiseur, telles que le taux d'apprentissage, la décroissance des poids, etc.

Construisons notre optimiseur :

La méthode `**parameters()**` de **torch.nn.Module** retourne un itérateur sur les paramètres du module. Pour calculer la perte, nous allons utiliser `**torch.nn.CrossEntropyLoss**`

Une chose importante à propos de `**torch.nn.CrossEntropyLoss**` est que l'entrée doit être un tensor 2D de taille (minibatch, n) et la cible attend un index de classe (0 à nClasses-1) comme cible pour chaque valeur d'un tensor 1D de taille minibatch. Par exemple :

Nous devons donc modifier la fonction `get_batch()` de l'article précédent pour qu'elle fonctionne comme dans l'exemple ci-dessus.

Maintenant, mettons à jour les poids et voyons la magie des variables.

La méthode **torch.autograd.backward** calcule la somme des gradients pour les variables données. Comme le dit la documentation, cette fonction accumule les gradients dans les feuilles, **vous devrez donc peut-être les mettre à zéro avant de les appeler**. Pour mettre à jour les paramètres, tous les optimiseurs implémentent une méthode `[**step()**](http://pytorch.org/docs/master/optim.html#torch.optim.Optimizer.step)`. Les fonctions peuvent être appelées une fois les gradients calculés, par exemple, vous pouvez utiliser `[**backward(**](http://pytorch.org/docs/master/autograd.html#torch.autograd.Variable.backward)**)**` pour les appeler.

Dans la [terminologie des réseaux de neurones](http://stackoverflow.com/questions/4752626/epoch-vs-iteration-when-training-neural-networks), une époque est égale à une passe avant (obtenir les valeurs de sortie), et une passe arrière (mettre à jour les poids) est égale à **_tous_** les exemples d'entraînement. Dans notre réseau, la fonction `get_batch()` nous donne le nombre de textes avec la taille du lot.

En mettant tout cela ensemble, nous obtenons ceci :

Et c'est tout.

Je n'aurais jamais pensé dire cela à propos d'un morceau de code, mais c'est magnifique.

N'est-ce pas ?

Maintenant, testons le modèle :

Et c'est tout.

Vous avez créé un modèle utilisant un réseau de neurones pour classer des textes en catégories.

Félicitations. ?

Vous pouvez voir le notebook avec le **code final** [ici](https://github.com/dmesquita/understanding_pytorch_nn).

Avez-vous trouvé cet article utile ? Je fais de mon mieux pour écrire un article approfondi chaque mois, vous pouvez [recevoir un email lorsque j'en publie un nouveau](https://goo.gl/forms/SLrJDrGtxgAoILkt1).
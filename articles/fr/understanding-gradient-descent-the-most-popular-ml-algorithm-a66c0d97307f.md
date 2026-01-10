---
title: Comment comprendre la descente de gradient, l'algorithme de ML le plus populaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T20:01:00.000Z'
originalURL: https://freecodecamp.org/news/understanding-gradient-descent-the-most-popular-ml-algorithm-a66c0d97307f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*7B2PZ9AB2_3tRLR1.
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Mathematics
  slug: mathematics
- name: 'tech '
  slug: tech
seo_title: Comment comprendre la descente de gradient, l'algorithme de ML le plus
  populaire
seo_desc: 'By Keshav Dhandhania

  Gradient Descent is one of the most popular and widely used algorithms for training
  machine learning models.

  Machine learning models typically have parameters (weights and biases) and a cost
  function to evaluate how good a partic...'
---

Par Keshav Dhandhania

La descente de gradient est l'un des algorithmes les plus populaires et largement utilisés pour l'entraînement des modèles de machine learning.

Les modèles de [machine learning](https://www.commonlounge.com/discussion/9325cf512f514e21815ec4c2e2e6e0e3) ont généralement des paramètres (poids et biais) et une fonction de coût pour évaluer la qualité d'un ensemble particulier de paramètres. De nombreux problèmes de machine learning se réduisent à trouver un ensemble de poids pour le modèle qui minimise la fonction de coût.

Par exemple, si la prédiction est _p_, la cible est _t_, et notre métrique d'erreur est l'erreur quadratique, alors la fonction de coût _J(W) = (p - t)²_.

Notez que la valeur prédite _p_ dépend de l'entrée _X_ ainsi que du modèle de machine learning et des valeurs (courantes) des paramètres _W_. Pendant l'entraînement, notre objectif est de trouver un ensemble de valeurs pour _W_ tel que _(p - t)²_ soit petit. Cela signifie que notre prédiction _p_ sera proche de la cible _t_.

![Image](https://cdn-media-1.freecodecamp.org/images/e3K6cr03JGW1Lg2OaO8k5uWDvZRb4HhC6mnZ)
_Illustration de la descente de gradient pour la régression linéaire_

La descente de gradient est une méthode itérative. Nous commençons avec un ensemble de valeurs pour nos paramètres de modèle (poids et biais), et nous les améliorons lentement.

Pour améliorer un ensemble donné de poids, nous essayons d'avoir une idée de la valeur de la fonction de coût pour des poids similaires aux poids actuels (en calculant le gradient). Ensuite, nous nous déplaçons dans la direction qui réduit la fonction de coût.

En répétant cette étape des milliers de fois, nous minimiserons continuellement notre fonction de coût.

### Pseudocode pour la descente de gradient

La descente de gradient est utilisée pour minimiser une fonction de coût _J(W)_ paramétrée par les paramètres du modèle _W_.

Le gradient (ou dérivée) nous indique l'inclinaison ou la pente de la fonction de coût. Par conséquent, pour minimiser la fonction de coût, nous nous déplaçons dans la direction opposée au gradient.

1. **Initialiser** les poids _W_ de manière aléatoire.
2. **Calculer les gradients** _G_ de la fonction de coût par rapport aux paramètres. Cela se fait en utilisant la différentiation partielle : _G = ∂J(W)/∂W_. La valeur du gradient _G_ dépend des entrées, des valeurs actuelles des paramètres du modèle et de la fonction de coût. Vous pourriez avoir besoin de réviser le sujet de la différentiation si vous calculez le gradient à la main.
3. **Mettre à jour les poids** d'une quantité proportionnelle à G, c'est-à-dire _W_ = _W - ηG_
4. Répéter jusqu'à ce que le coût _J_(_w_) cesse de diminuer, ou qu'un autre critère de **terminaison** prédéfini soit atteint.

Dans l'étape 3, _η_ est le **taux d'apprentissage** qui détermine la taille des pas que nous faisons pour atteindre un minimum. Nous devons être très prudents avec ce paramètre. Des valeurs élevées de _η_ peuvent dépasser le minimum, et des valeurs très basses atteindront le minimum très lentement.

Un choix populaire pour le critère de terminaison est que le coût _J_(_w_) cesse de diminuer sur un ensemble de validation.

### Intuition pour la descente de gradient

Imaginez que vous êtes bandé des yeux dans un terrain accidenté, et votre objectif est d'atteindre l'altitude la plus basse.

L'une des stratégies les plus simples que vous pouvez utiliser est de sentir le sol dans toutes les directions, et de faire un pas dans la direction où le sol descend le plus rapidement.

Si vous continuez à répéter ce processus, vous pourriez vous retrouver au lac, ou encore mieux, quelque part dans la grande vallée.

![Image](https://cdn-media-1.freecodecamp.org/images/N0IZ9olG1n4CmlzSTFF4XUmb5aS9CRsbMBo7)
_Source : [Cours de Stanford d'Andrej Karpathy, Lecture 3](http://bit.ly/2e7pXyx" rel="noopener" target="_blank" title=")_

Le terrain accidenté est analogue à la fonction de coût, et minimiser la fonction de coût est analogue à essayer d'atteindre des altitudes plus basses.

Vous êtes bandé des yeux, car nous n'avons pas le luxe d'évaluer (ou de "voir") la valeur de la fonction pour chaque ensemble possible de paramètres.

Sentir la pente du terrain autour de vous est analogue à calculer le gradient, et faire un pas est analogue à une itération de mise à jour des paramètres.

Au fait — en aparté — ce tutoriel fait partie du [Cours gratuit de Data Science](https://www.commonlounge.com/discussion/367fb21455e04c7c896e9cac25b11b47) et du [Cours gratuit de Machine Learning](https://www.commonlounge.com/discussion/33a9cce246d343dd85acce5c3c505009/main) sur [Commonlounge](https://www.commonlounge.com/). Les cours incluent de nombreux devoirs pratiques et projets. Si vous êtes intéressé par l'apprentissage de la Data Science / ML, je vous recommande vivement de le consulter.

### Variantes de la descente de gradient

Il existe plusieurs variantes de la descente de gradient, selon la quantité de données utilisée pour calculer le gradient.

La principale raison de ces variations est l'efficacité computationnelle. Un ensemble de données peut contenir des millions de points de données, et calculer le gradient sur l'ensemble des données peut être coûteux en termes de calcul.

* La **descente de gradient par lots** calcule le gradient de la fonction de coût par rapport au paramètre _W_ pour **l'ensemble des données d'entraînement**. Puisque nous devons calculer les gradients pour l'ensemble des données pour effectuer une seule mise à jour des paramètres, la descente de gradient par lots peut être très lente.
* La **descente de gradient stochastique (SGD)** calcule le gradient pour chaque mise à jour en utilisant un **seul point de données d'entraînement** _x_i_ (choisi au hasard). L'idée est que le gradient calculé de cette manière est une approximation stochastique du gradient calculé en utilisant l'ensemble des données d'entraînement. Chaque mise à jour est maintenant beaucoup plus rapide à calculer que dans la descente de gradient par lots, et sur de nombreuses mises à jour, nous irons dans la même direction générale.
* Dans la **descente de gradient par mini-lots**, nous calculons le gradient pour chaque petit mini-lot de données d'entraînement. C'est-à-dire que nous divisons d'abord les données d'entraînement en petits lots (par exemple _M_ échantillons par lot). Nous effectuons une mise à jour par mini-lot. _M_ est généralement dans la plage de 30 à 500, selon le problème. Habituellement, la descente de gradient par mini-lots est utilisée parce que l'infrastructure de calcul — compilateurs, CPU, GPU — est souvent optimisée pour effectuer des additions de vecteurs et des multiplications de vecteurs.

Parmi celles-ci, SGD et la descente de gradient par mini-lots sont les plus populaires.

Dans un scénario typique, nous faisons plusieurs passes sur les données d'entraînement avant que le critère de terminaison soit atteint. Chaque passe est appelée une _époque_. De plus, notez que puisque l'étape de mise à jour est beaucoup plus efficace sur le plan computationnel dans SGD et la descente de gradient par mini-lots, nous effectuons généralement 100 à 1000 mises à jour entre les vérifications du critère de terminaison.

### Choix du taux d'apprentissage

Typiquement, la valeur du taux d'apprentissage est choisie manuellement. Nous commençons généralement avec une petite valeur telle que 0,1, 0,01 ou 0,001 et nous l'adaptons en fonction de si la fonction de coût diminue très lentement (augmenter le taux d'apprentissage) ou si elle explose / est erratique (diminuer le taux d'apprentissage).

Bien que le choix manuel d'un taux d'apprentissage soit encore la pratique la plus courante, plusieurs méthodes telles que l'optimiseur Adam, AdaGrad et RMSProp ont été proposées pour choisir automatiquement un taux d'apprentissage approprié.

_Co-écrit par Keshav Dhandhania et Savan Visalpara._

_Originalement publié dans le cadre du [Cours gratuit de Machine Learning](https://www.commonlounge.com/discussion/33a9cce246d343dd85acce5c3c505009/main) et du [Cours gratuit de Data Science](https://www.commonlounge.com/discussion/367fb21455e04c7c896e9cac25b11b47) sur [www.commonlounge.com](https://www.commonlounge.com/discussion/69a34ad6029549f39087d00d052607ab/main)._
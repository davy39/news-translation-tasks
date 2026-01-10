---
title: Une introduction illustrative au discriminant linéaire de Fisher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T16:41:19.000Z'
originalURL: https://freecodecamp.org/news/an-illustrative-introduction-to-fishers-linear-discriminant-9484efee15ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XfBJ8NEwSB_zW8Up1V71mQ.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Une introduction illustrative au discriminant linéaire de Fisher
seo_desc: 'By Thalles Silva

  To deal with classification problems with two or more classes, most Machine Learning
  (ML) algorithms work the same way.

  Usually, they apply some kind of transformation to the input data with the effect
  of reducing the original input ...'
---

Par Thalles Silva

Pour traiter les problèmes de classification avec deux classes ou plus, la plupart des algorithmes de Machine Learning (ML) fonctionnent de la même manière.

Généralement, ils appliquent une sorte de transformation aux données d'entrée avec pour effet de réduire les dimensions d'entrée originales à un nombre plus petit. Le but est de projeter les données dans un nouvel espace. Ensuite, une fois projetées, l'algorithme tente de classer les points en trouvant une séparation linéaire.

Pour les problèmes avec de petites dimensions d'entrée, la tâche est quelque peu plus facile. Prenons l'ensemble de données suivant comme exemple.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_foduk2DnEvxttu8tFpvixw.png)

Supposons que nous voulons classer correctement les cercles rouges et bleus.

Il est clair qu'avec un simple modèle linéaire, nous n'obtiendrons pas un bon résultat. Il n'existe aucune combinaison linéaire des entrées et des poids qui mappe les entrées à leurs classes correctes. Mais que se passerait-il si nous pouvions transformer les données de sorte à pouvoir tracer une ligne qui sépare les deux classes ?

C'est ce qui se passe si nous élevons au carré les deux vecteurs de caractéristiques d'entrée. Maintenant, un modèle linéaire classera facilement les points bleus et rouges.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_AtB5d3c9ShP4s4ayAP3pBw.png)

Cependant, parfois nous ne savons pas quel type de transformation nous devrions utiliser. En fait, trouver la meilleure représentation n'est pas un problème trivial. Il existe de nombreuses transformations que nous pourrions appliquer à nos données. De même, chacune d'entre elles pourrait aboutir à un classificateur différent (en termes de performance).

Une solution à ce problème est d'apprendre la bonne transformation. Cela est connu sous le nom d'**apprentissage de représentation** et c'est exactement ce que font les algorithmes de Deep Learning.

La magie est que nous n'avons pas besoin de "deviner" quel type de transformation donnerait la meilleure représentation des données. L'algorithme le découvrira.

Cependant, gardez à l'esprit que, qu'il s'agisse d'apprentissage de représentation ou de transformations artisanales, le schéma est le même. Nous devons modifier les données d'une manière ou d'une autre afin qu'elles puissent être facilement séparables.

Faisons quelques pas en arrière et considérons un problème plus simple.

Nous allons explorer comment le **discriminant linéaire de Fisher** (FLD) parvient à classer des données multidimensionnelles en plusieurs classes. Mais avant de commencer, n'hésitez pas à ouvrir ce [notebook Colab](https://github.com/sthalles/fishers-linear-discriminant/blob/master/Fishers_Multiclass.ipynb) et à suivre.

# Le discriminant linéaire de Fisher

Une façon de voir les problèmes de classification est à travers le prisme de la réduction de dimension.

Pour commencer, considérons le cas d'un problème de classification à deux classes (**K=2**). Points bleus et rouges dans **R²**. En général, nous pouvons prendre n'importe quel vecteur d'entrée de dimension D et le projeter vers le bas en dimensions D'. Ici, **D** représente les dimensions d'entrée originales tandis que **D'** est la dimension de l'espace projeté. Tout au long de cet article, considérons **D'** inférieur à **D**.

Dans le cas de la projection à une dimension (la ligne numérique), c'est-à-dire **D'=1**, nous pouvons choisir un seuil **t** pour séparer les classes dans le nouvel espace. Étant donné un vecteur d'entrée **x** :

* si la valeur prédite **y >= t** alors, **x** appartient à la classe C1 (classe 1).
* sinon, il est classé comme C2 (classe 2).

Notez que le vecteur **y** (prédictions) est égal à la combinaison linéaire des entrées **x** et des poids **W → y**=**W**ᵀ**x.**

Prenons l'ensemble de données ci-dessous comme exemple jouet. Nous voulons réduire les dimensions des données originales de **D=2** à **D'=1**. En d'autres termes, nous voulons une transformation T qui mappe les vecteurs en 2D à 1D — T(**v**) = ℝ² →ℝ¹.

Tout d'abord, calculons les vecteurs moyens **m1** et **m2** pour les deux classes.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_Ky__i4qZwyy-WUSF8_wU4A.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_l6CxIZBax3YI3h1AvvSoFg.png)

Notez que **N1** et **N2** désignent le nombre de points dans les classes C1 et C2 respectivement. Maintenant, considérons l'utilisation des moyennes de classe comme mesure de séparation. En d'autres termes, nous voulons projeter les données sur le vecteur **W** reliant les 2 moyennes de classe.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_aVKRo9LPaHGROakZuEc4wg.png)

Il est important de noter que tout type de projection vers une dimension plus petite peut impliquer une certaine perte d'information. Dans ce scénario, notez que les deux classes sont clairement séparables (par une ligne) dans leur espace d'origine.

Cependant, après la reprojection, les données présentent une sorte de chevauchement de classe — montré par l'ellipse jaune sur le graphique et l'histogramme ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_ygJYUt-FURz9KawGQYhWfQ.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_3FX4Gdm6P6SO628pmgtvqw.png)

C'est là que le discriminant linéaire de Fisher entre en jeu.

L'idée proposée par Fisher est de maximiser une fonction qui donnera une grande séparation entre les moyennes de classe projetées, tout en donnant une petite variance au sein de chaque classe, minimisant ainsi le chevauchement des classes.

En d'autres termes, FLD sélectionne une projection qui maximise la séparation des classes. Pour ce faire, il maximise le rapport entre la variance inter-classe et la variance intra-classe.

En bref, pour projeter les données vers une dimension plus petite et éviter le chevauchement des classes, FLD maintient 2 propriétés.

* Une grande variance parmi les classes de l'ensemble de données.
* Une petite variance au sein de chacune des classes de l'ensemble de données.

Notez qu'une grande variance inter-classe signifie que les moyennes de classe projetées doivent être aussi éloignées que possible. Au contraire, une petite variance intra-classe a pour effet de garder les points de données projetés plus proches les uns des autres.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_v8kk5kYy2179bxiV3gPPBA.png)

Pour trouver la projection avec les propriétés suivantes, FLD apprend un vecteur de poids **W** avec le critère suivant.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_M9GOo_qFMXT1YNwXIzb9nA.png)

Si nous substituons les vecteurs moyens **m1** et **m2** ainsi que la variance **s** comme donné par les équations (1) et (2), nous arrivons à l'équation (3). Si nous prenons la dérivée de (3) par rapport à **W** (après quelques simplifications), nous obtenons l'équation d'apprentissage pour **W** (équation 4).

C'est-à-dire, **W** (notre transformation souhaitée) est directement proportionnel à l'inverse de la matrice de covariance **intra-classe** fois la différence des moyennes de classe.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_Zlaz-JKRa4F7MSNig28A7g.png)

Comme prévu, le résultat permet une séparation parfaite des classes avec un simple seuillage.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_6kKqxE3YVcVWYF3MjwpPRQ.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_HK16495yDOpGYFsJCErdUQ.png)

## Le discriminant linéaire de Fisher pour plusieurs classes

Nous pouvons généraliser FLD pour le cas de plus de **K>2** classes. Ici, nous avons besoin de formes de généralisation pour les matrices de covariance **intra-classe** et **inter-classe**.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_ihSnoJLR0lh8wqjJ-MKHmw.png)

Pour la matrice de covariance intra-classe **SW**, pour chaque classe, prenez la somme de la multiplication matricielle entre les valeurs d'entrée centralisées et leur transposée. Équations 5 et 6.

Pour estimer la covariance inter-classe **SB**, pour chaque classe **k=1,2,3,…,K**, prenez le **produit extérieur** de la moyenne de classe locale **mk** et de la moyenne globale **m**. Ensuite, mettez-le à l'échelle par le nombre d'enregistrements dans la classe **k** — équation 7.

La maximisation du critère FLD est résolue via une eigendecomposition de la multiplication matricielle entre l'inverse de **SW** et **SB**. Ainsi, pour trouver le vecteur de poids **W**, nous prenons les **D'** vecteurs propres qui correspondent à leurs plus grandes valeurs propres (équation 8).

En d'autres termes, si nous voulons réduire nos dimensions de données de **D=784** à **D'=2**, le vecteur de transformation **W** est composé des 2 vecteurs propres qui correspondent aux **D'=2** plus grandes valeurs propres. Cela donne une forme finale de **W = (N,D')**, où **N** est le nombre d'enregistrements d'entrée et **D'** les dimensions réduites de l'espace des caractéristiques.

## Construction d'un discriminant linéaire

Jusqu'à présent, nous avons utilisé le discriminant linéaire de Fisher uniquement comme méthode de réduction de dimension. Pour vraiment créer un discriminant, nous pouvons modéliser une **distribution gaussienne multivariée** sur un vecteur d'entrée de dimension D **x** pour chaque classe **K** comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_A4shtkbvUU8RLnXJ3J14lA.png)

Ici, **_μ_** (la moyenne) est un vecteur de dimension D. **Σ** (sigma) est une matrice **DxD** — la matrice de covariance. Et |**Σ**| est le déterminant de la covariance. Le déterminant est une mesure de la manière dont la matrice de covariance **Σ** étire ou rétrécit l'espace.

En Python, cela ressemble à ceci.

```py
# Retourne les paramètres des distributions gaussiennes
def gaussian(self, X):
  means = {}
  covariance = {}
  priors = {}  # p(Ck)
  for class_id, values in X.items():
    proj = np.dot(values, self.W)
    means[class_id] = np.mean(proj, axis=0)
    covariance[class_id] = np.cov(proj, rowvar=False)
    # estime les priors en utilisant les fractions des points de données de l'ensemble d'entraînement dans chacune des classes.
    priors[class_id] = values.shape[0] / self.N
  return means, covariance, priors

# modélise une distribution gaussienne multivariée pour la distribution de vraisemblance de chaque classe P(x|Ck)
def gaussian_distribution(self, x, u, cov):
  scalar = (1. / ((2 * np.pi) ** (x.shape[0] / 2.))) * (1 / np.sqrt(np.linalg.det(cov)))
  x_sub_u = np.subtract(x, u)
  return scalar * np.exp(-np.dot(np.dot(x_sub_u, inv(cov)), x_sub_u.T) / 2.)
```

Les paramètres de la distribution gaussienne : **_μ_** et Σ, sont calculés pour chaque classe **k=1,2,3,…,K** en utilisant les données d'entrée projetées. Nous pouvons inférer les probabilités a priori des classes _P(Ck)_ en utilisant les fractions des points de données de l'ensemble d'entraînement dans chacune des classes (ligne 11).

Une fois que nous avons les paramètres gaussiens et les a priori, nous pouvons calculer les densités conditionnelles de classe _P(_**_x_**_|Ck)_ pour chaque classe **k=1,2,3,…,K** individuellement. Pour ce faire, nous projetons d'abord le vecteur d'entrée de dimension D **x** vers un nouvel espace **D'**. Gardez à l'esprit que **D' < D**. Ensuite, nous évaluons l'équation 9 pour chaque point projeté. Enfin, nous pouvons obtenir les probabilités a posteriori des classes _P(Ck|_**_x_**_)_ pour chaque classe **k=1,2,3,…,K** en utilisant l'équation 10.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_eThiSZ1eGLHDSnlblV-W0A.png)

L'équation 10 est évaluée à la ligne 8 de la fonction de score ci-dessous.

```py
def score(self,X,y):
  proj = self.project(X)
  gaussian_likelihoods = []
  classes = sorted(list(self.g_means.keys()))
  for x in proj:
    row = []
    for c in classes:  # nombre de classes
      res = self.priors[c] * self.gaussian_distribution(x, self.g_means[c], self.g_covariance[c])  # Calcule les probabilités a posteriori P(Ck|x) d'une classe k étant donné un point x
      row.append(res)

    gaussian_likelihoods.append(row)

  gaussian_likelihoods = np.asarray(gaussian_likelihoods)
  # assigne x à la classe avec la plus grande probabilité a posteriori
  predictions = np.argmax(gaussian_likelihoods, axis=1)
  return np.sum(predictions == y) / len(y)
```

Nous pouvons alors assigner le vecteur d'entrée **x** à la classe **k** avec la plus grande probabilité a posteriori.

## Test sur MNIST

En utilisant MNIST comme ensemble de données de test jouet. Si nous choisissons de réduire les dimensions d'entrée originales **D=784** à **D'=2**, nous obtenons environ _56%_ de précision sur les données de test. Si nous augmentons les dimensions de l'espace projeté à **D'=3**, cependant, nous atteignons près de _74%_ de précision. Ces 2 projections facilitent également la visualisation de l'espace des caractéristiques résultant.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_dxfQmK5xIW-snl26vKPNeQ.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/02/1_n3Le7S8gf9bs9PFEUG0PBQ.png)

Quelques points clés à retenir de cet article.

* Le discriminant linéaire de Fisher, en essence, est une technique de réduction de dimension, et non un discriminant.
* Pour la classification binaire, nous pouvons trouver un seuil optimal **t** et classer les données en conséquence.
* Pour les données multiclasses, nous pouvons (1) modéliser une distribution conditionnelle de classe en utilisant une gaussienne. (2) Trouver les probabilités a priori des classes _P(Ck)_, et (3) utiliser **Bayes** pour trouver les probabilités a posteriori des classes _p(Ck|x)_.
* Pour trouver la direction optimale pour projeter les données d'entrée, Fisher a besoin de données supervisées.
* Étant donné un ensemble de données avec **D** dimensions, nous pouvons le projeter vers le bas jusqu'à **au plus** **D'** égal à **D-1** dimensions.

Cet article est basé sur le **chapitre 4.1** de [Pattern Recognition and Machine Learning](http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf). Livre de Christopher Bishop.

**Merci d'avoir lu.**
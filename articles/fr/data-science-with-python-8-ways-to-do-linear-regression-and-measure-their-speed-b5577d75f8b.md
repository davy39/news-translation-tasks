---
title: 'Data science avec Python : 8 façons de réaliser une régression linéaire et
  de mesurer leur rapidité'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T14:35:15.000Z'
originalURL: https://freecodecamp.org/news/data-science-with-python-8-ways-to-do-linear-regression-and-measure-their-speed-b5577d75f8b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Jl23jqcBMGdi26d1yUcfng.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: 'Data science avec Python : 8 façons de réaliser une régression linéaire
  et de mesurer leur rapidité'
seo_desc: 'By Tirthajyoti Sarkar

  In this article, we discuss 8 ways to perform simple linear regression using Python
  code/packages. We gloss over their pros and cons, and show their relative computational
  complexity measure.

  For many data scientists, linear reg...'
---

Par Tirthajyoti Sarkar

Dans cet article, nous abordons 8 façons de réaliser une régression linéaire simple en utilisant du code/des packages Python. Nous passons en revue leurs avantages et inconvénients, et montrons leur mesure de complexité computationnelle relative.

Pour de nombreux data scientists, la [régression linéaire](https://en.wikipedia.org/wiki/Linear_regression) est le point de départ de nombreux projets de modélisation statistique et d'analyse prédictive. L'importance de l'ajustement (précis et rapide) d'un modèle linéaire à un large ensemble de données ne peut être surestimée. [Comme souligné dans cet article](https://towardsdatascience.com/machine-learning-with-python-easy-and-robust-method-to-fit-nonlinear-data-19e8a1ddbd49), le terme « _LINÉAIRE_ » dans le modèle de régression linéaire fait référence aux coefficients, et non au degré des caractéristiques (features).

Les caractéristiques (ou variables indépendantes) peuvent être de n'importe quel degré ou même des fonctions transcendantes comme exponentielles, logarithmiques, sinusoïdales. Ainsi, un grand nombre de phénomènes naturels peuvent être modélisés (approximativement) à l'aide de ces transformations et d'un modèle linéaire, même si la relation fonctionnelle entre la sortie et les caractéristiques est hautement non linéaire.

D'autre part, Python s'impose rapidement comme le [langage de programmation de choix par défaut](https://www.quora.com/Why-is-Python-a-language-of-choice-for-data-scientists) pour les data scientists. Par conséquent, il est crucial pour un data scientist de connaître toutes les différentes méthodes lui permettant d'ajuster rapidement un modèle linéaire à un ensemble de données assez important et d'évaluer l'importance relative de chaque caractéristique dans le résultat du processus.

> Cependant, n'y a-t-il qu'une seule façon d'effectuer une analyse de régression linéaire en Python ? En cas de multiples options disponibles, comment choisir la méthode la plus efficace ?

En raison de la grande popularité de la [bibliothèque d'apprentissage automatique scikit-learn](http://scikit-learn.org/stable/), une approche courante consiste souvent à appeler la [classe Linear Model](http://scikit-learn.org/stable/modules/linear_model.html) de cette bibliothèque et à ajuster les données. Bien que cela puisse offrir des avantages supplémentaires en appliquant d'autres [fonctionnalités de pipeline d'apprentissage automatique](http://scikit-learn.org/stable/modules/pipeline.html) (par exemple, la normalisation des données, la régularisation des coefficients du modèle, l'alimentation du modèle linéaire vers un autre modèle en aval), ce n'est souvent pas la méthode la plus rapide ou la plus propre lorsqu'un analyste de données a juste besoin d'un moyen simple et rapide de déterminer les coefficients de régression (et quelques statistiques de base associées).

Il existe des méthodes plus rapides et plus propres. Mais toutes n'offrent pas la même quantité d'informations ou la même flexibilité de modélisation.

Bonne lecture.

L'intégralité du code de base pour les différentes méthodes de régression linéaire [est disponible ici sur mon dépôt GitHub](https://github.com/tirthajyoti/PythonMachineLearning/blob/master/Linear_Regression_Methods.ipynb). La plupart d'entre elles sont basées sur le [package SciPy](https://docs.scipy.org/doc/scipy/reference/tutorial/general.html).

**SciPy est une collection d'algorithmes mathématiques et de fonctions de commodité construite sur l'extension [Numpy](http://www.numpy.org/) de Python**. Elle ajoute une puissance significative à la session Python interactive en fournissant à l'utilisateur des commandes et des classes de haut niveau pour manipuler et visualiser les données.

Laissez-moi aborder chaque méthode brièvement,

#### Méthode : Scipy.polyfit( ) ou numpy.polyfit( )

![Image](https://cdn-media-1.freecodecamp.org/images/hfbGMo4HrTuJcSRo4qa44VtKDNNhyzuXKTPP)

Il s'agit d'une [fonction d'ajustement polynomial](https://en.wikipedia.org/wiki/Curve_fitting) par moindres carrés assez générale qui accepte l'ensemble de données et une fonction polynomiale de n'importe quel degré (spécifié par l'utilisateur), et renvoie un tableau de coefficients qui minimise l'erreur quadratique. [Une description détaillée de la fonction est donnée ici](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.polyfit.html). Pour une régression linéaire simple, on peut choisir le degré 1. Si vous souhaitez ajuster un modèle de degré supérieur, vous pouvez construire des caractéristiques polynomiales à partir des données de caractéristiques linéaires et les ajuster également au modèle.

#### Méthode : Stats.linregress( )

![Image](https://cdn-media-1.freecodecamp.org/images/b779UD6x0A3Cm0SSWbV3enZRtAOUHX-yUgnv)

Il s'agit d'une [fonction de régression linéaire](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html) hautement spécialisée disponible dans le module stats de Scipy. Elle est assez restreinte dans sa flexibilité car elle est optimisée pour calculer une régression linéaire par les moindres carrés pour deux ensembles de mesures uniquement. Ainsi, vous ne pouvez pas ajuster un modèle linéaire généralisé ou une régression multivariée en l'utilisant. Mais, en raison de sa nature spécialisée, c'est l'une des méthodes les plus rapides lorsqu'il s'agit de régression linéaire simple. Outre le coefficient ajusté et le terme d'ordonnée à l'origine, elle renvoie également des statistiques de base telles que le [coefficient R² et l'erreur standard](http://blog.minitab.com/blog/adventures-in-statistics-2/regression-analysis-how-do-i-interpret-r-squared-and-assess-the-goodness-of-fit).

#### Méthode : Optimize.curve_fit( )

![Image](https://cdn-media-1.freecodecamp.org/images/9-o8vrHLjq8UXFitRkmjW0nmX4pP8qt7760Y)

C'est dans la même lignée que la méthode Polyfit, mais de nature plus générale. Cette [puissante fonction du module scipy.optimize](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) peut ajuster n'importe quelle fonction définie par l'utilisateur à un ensemble de données en effectuant une minimisation par les moindres carrés.

Pour une régression linéaire simple, on peut simplement écrire une fonction linéaire mx+c et appeler cet estimateur. Il va sans dire que cela fonctionne également pour la régression multivariée. Elle renvoie un tableau de paramètres de fonction pour lesquels la mesure des moindres carrés est minimisée ainsi que la matrice de covariance associée.

#### Méthode : numpy.linalg.lstsq

![Image](https://cdn-media-1.freecodecamp.org/images/y1mmJ89I4qGmcXqXfgySvUy30-xUWdaUKTko)

C'est la [méthode fondamentale de calcul de la solution des moindres carrés pour un système d'équations linéaires par factorisation de matrice](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq). Elle provient du module d'algèbre linéaire très pratique du package numpy. Sous le capot, elle résout l'équation _a x = b_ en calculant un vecteur _x_ qui minimise la norme euclidienne 2 _|| b — a x ||²_.

L'équation peut être sous-déterminée, bien déterminée ou surdéterminée (c'est-à-dire que le nombre de lignes linéairement indépendantes de _a_ peut être inférieur, égal ou supérieur à son nombre de colonnes linéairement indépendantes). Si _a_ est carrée et de plein rang, alors _x_ (à l'exception de l'erreur d'arrondi) est la solution « exacte » de l'équation.

Vous pouvez effectuer une régression simple ou multivariée avec cela et obtenir les coefficients calculés et les résidus. Une petite astuce est qu'avant d'appeler cette fonction, vous devez ajouter une colonne de 1 aux données x pour calculer l'ordonnée à l'origine. Il s'avère que c'est l'une des méthodes les plus rapides à essayer pour les problèmes de régression linéaire.

#### Méthode : Statsmodels.OLS ( )

[Statsmodels est un excellent petit package Python](http://www.statsmodels.org/dev/index.html) qui fournit des classes et des fonctions pour l'estimation de nombreux modèles statistiques différents, ainsi que pour la réalisation de tests statistiques et l'exploration de données statistiques. Une liste exhaustive de statistiques de résultats est disponible pour chaque estimateur. Les résultats sont testés par rapport aux packages statistiques existants pour garantir l'exactitude.

Pour la régression linéaire, on peut utiliser la fonction OLS ou [Ordinary-Least-Square](https://en.wikipedia.org/wiki/Ordinary_least_squares) (Moindres Carrés Ordinaires) de ce package et obtenir des informations statistiques complètes sur le processus d'estimation.

Une petite astuce à retenir est que vous devez ajouter manuellement une constante aux données x pour calculer l'ordonnée à l'origine, sinon par défaut, il ne rapportera que le coefficient. Ci-dessous se trouve l'instantané du résumé complet des résultats du modèle OLS. **Il est aussi riche que n'importe quel langage statistique fonctionnel comme R ou Julia.**

![Image](https://cdn-media-1.freecodecamp.org/images/VOOaaJLawtV26YLC0v9KJTRAZ-tUlmdhLMjj)

#### Méthode : Solution analytique utilisant la méthode de l'inverse matricielle

Pour les problèmes de régression linéaire bien conditionnés (au moins là où le nombre de points de données > nombre de caractéristiques), une solution matricielle simple sous forme fermée existe pour calculer les coefficients qui garantit la minimisation par les moindres carrés. Elle est donnée par,

![Image](https://cdn-media-1.freecodecamp.org/images/qUJvZv5IkUlQBz1HpmZmJQINgfTy9YHNN1nP)

La dérivation détaillée et la discussion sur cette solution sont [abordées ici](https://en.wikipedia.org/wiki/Linear_least_squares_(mathematics)).

On a deux choix ici :

(a) utiliser l'inverse matricielle multiplicative simple.

(b) calculer d'abord la [matrice pseudo-inverse généralisée de Moore-Penrose](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse) des données x, puis effectuer un produit scalaire avec les données y. Parce que ce deuxième processus implique une [décomposition en valeurs singulières (SVD)](https://en.wikipedia.org/wiki/Singular-value_decomposition), il est plus lent mais il peut bien fonctionner pour des ensembles de données mal conditionnés.

#### Méthode : sklearn.linear_model.LinearRegression( )

C'est la [méthode par excellence](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) utilisée par la majorité des ingénieurs en apprentissage automatique et des data scientists. Bien sûr, pour les problèmes du monde réel, elle n'est probablement jamais très utilisée et est remplacée par des algorithmes validés par croisement et régularisés tels que la [régression Lasso](https://en.wikipedia.org/wiki/Lasso_(statistics)) ou la [régression Ridge](https://en.wikipedia.org/wiki/Tikhonov_regularization). Mais le cœur essentiel de ces fonctions avancées réside dans ce modèle.

#### Mesurer la vitesse et la complexité temporelle de ces méthodes

En tant que data scientist, on doit toujours rechercher des méthodes/fonctions précises mais rapides pour effectuer le travail de modélisation des données. Si la méthode est intrinsèquement lente, elle créera un goulot d'étranglement d'exécution pour les grands ensembles de données.

Un bon moyen de déterminer l'évolutivité est d'exécuter les modèles pour des tailles d'ensembles de données croissantes, d'extraire les temps d'exécution pour tous les lancements et de tracer la tendance.

[Voici le code de base pour cela](https://github.com/tirthajyoti/PythonMachineLearning/blob/master/Linear_Regression_Methods.ipynb). Et voici le résultat. En raison de leur simplicité, stats.linregress et les méthodes d'inverse matricielle simple sont les plus rapides, même jusqu'à 10 millions de points de données.

![Image](https://cdn-media-1.freecodecamp.org/images/DY-jV0gYYTXDUS2BsE-s0F-LwenVeKmNBHPJ)

#### Résumé

En tant que data scientist, on doit toujours explorer plusieurs options pour résoudre la même tâche d'analyse ou de modélisation et choisir la meilleure pour son problème particulier.

Dans cet article, nous avons abordé 8 façons de réaliser une régression linéaire simple. La plupart d'entre elles sont également évolutives vers une modélisation de régression multivariée et polynomiale plus généralisée. Nous n'avons pas listé l'ajustement R² pour ces méthodes car elles sont toutes très proches de 1.

Pour une régression à variable unique, avec des millions de points de données générés artificiellement, le coefficient de régression est très bien estimé.

L'objectif de cet article est principalement d'aborder la vitesse relative/complexité computationnelle de ces méthodes. Nous avons montré la mesure de la complexité computationnelle de chacune d'elles en testant sur un ensemble de données synthétisé de taille croissante (jusqu'à 10 millions d'échantillons). Étonnamment, la solution analytique simple par inverse matricielle fonctionne assez rapidement par rapport au modèle linéaire largement utilisé de scikit-learn.

Si vous avez des questions ou des idées à partager, veuillez contacter l'auteur à [**tirthajyoti[AT]gmail.com**](mailto:tirthajyoti@gmail.com). Vous pouvez également consulter les [**dépôts GitHub**](https://github.com/tirthajyoti) de l'auteur pour d'autres extraits de code amusants en Python, R ou MATLAB et des ressources d'apprentissage automatique. Si vous êtes, comme moi, passionné par l'apprentissage automatique/la science des données/les semi-conducteurs, n'hésitez pas à [m'ajouter sur LinkedIn](https://www.linkedin.com/in/tirthajyoti-sarkar-2127aa7/) ou à [me suivre sur Twitter.](https://twitter.com/tirthajyotiS)
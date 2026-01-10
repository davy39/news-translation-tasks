---
title: 'Apprentissage automatique : une introduction à l''erreur quadratique moyenne
  et aux droites de régression'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-16T06:45:02.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-mean-squared-error-regression-line-c7dde9a26b93
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m_GKsrB2EfnLwwug3ASrtw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Mathematics
  slug: mathematics
- name: statistics
  slug: statistics
- name: 'tech '
  slug: tech
seo_title: 'Apprentissage automatique : une introduction à l''erreur quadratique moyenne
  et aux droites de régression'
seo_desc: 'By Moshe Binieli

  Introduction

  This article will deal with the statistical method mean squared error, and I’ll
  describe the relationship of this method to the regression line.

  The example consists of points on the Cartesian axis. We will define a math...'
---

Par Moshe Binieli

### **Introduction**

Cet article traitera de la méthode statistique **erreur quadratique moyenne**, et je décrirai la relation de cette méthode avec la **droite de régression**.

L'exemple est constitué de points sur l'axe cartésien. Nous allons définir une fonction mathématique qui nous donnera la ligne droite qui passe au mieux entre tous les points sur l'axe cartésien.

Et de cette manière, nous apprendrons le lien entre ces deux méthodes, et à quoi ressemble le résultat de leur connexion ensemble.

### Explication générale

Voici la définition de [Wikipedia](https://en.wikipedia.org/wiki/Mean_squared_error) :

> En statistiques, l'erreur quadratique moyenne (EQM) d'un estimateur (d'une procédure pour estimer une quantité non observée) mesure la moyenne des carrés des erreurs — c'est-à-dire, la différence quadratique moyenne entre les valeurs estimées et ce qui est estimé. L'EQM est une fonction de risque, correspondant à la valeur attendue de la perte d'erreur quadratique. Le fait que l'EQM soit presque toujours strictement positive (et non nulle) est dû à l'aléatoire ou au fait que l'estimateur ne tient pas compte d'informations qui pourraient produire une estimation plus précise.

### La structure de l'article

* Avoir une idée de l'idée, visualisation graphique, équation de l'erreur quadratique moyenne.
* La partie mathématique qui contient des manipulations algébriques et une dérivée de fonctions à deux variables pour trouver un minimum. Cette section est **pour ceux qui veulent comprendre comment** nous obtenons les formules mathématiques plus tard, vous pouvez la sauter si cela ne vous intéresse pas.
* Une explication des formules mathématiques que nous avons reçues et le rôle de chaque variable dans la formule.
* Exemples

### Avoir une idée de l'idée

Supposons que nous avons sept points, et notre objectif est de trouver une ligne qui **minimise** les distances quadratiques à ces différents points.

Essayons de comprendre cela.

Je vais prendre un exemple et je vais tracer une ligne entre les points. Bien sûr, mon dessin n'est pas le meilleur, mais c'est juste à des fins de démonstration.

![Image](https://cdn-media-1.freecodecamp.org/images/MNskFmGPKuQfMLdmpkT-X7-8w2cJXulP3683)
_Points sur un graphique simple._

Vous pourriez vous demander, qu'est-ce que ce graphique ?

* les **points violets** sont les points sur le graphique. Chaque point a une coordonnée x et une coordonnée y.
* La **ligne bleue** est notre ligne de prédiction. C'est une ligne qui passe par tous les points et les ajuste de la meilleure manière. Cette ligne contient les points prédits.
* La **ligne rouge** entre chaque point violet et la ligne de prédiction sont les **erreurs**. Chaque erreur est la distance du point à son point prédit.

Vous devriez vous souvenir de cette équation de vos jours d'école, **_y=Mx+B_**, où **M** est la [pente](https://en.wikipedia.org/wiki/Slope) de la ligne et **B** est l'[ordonnée à l'origine](https://en.wikipedia.org/wiki/Y-intercept) de la ligne.

Nous voulons trouver M ([pente](https://en.wikipedia.org/wiki/Slope)) et B ([ordonnée à l'origine](https://en.wikipedia.org/wiki/Y-intercept)) qui **minimisent** l'erreur quadratique !

Définissons une équation mathématique qui nous donnera l'erreur quadratique moyenne pour tous nos points.

![Image](https://cdn-media-1.freecodecamp.org/images/hmZydSW9YegiMVPWq2JBpOpai3CejzQpGkNG)
_Formule générale pour l'erreur quadratique moyenne._

Analysons ce que cette équation signifie réellement.

* En mathématiques, le caractère qui ressemble à un E bizarre est appelé sommation (sigma grec). Il s'agit de la somme d'une séquence de nombres, de i=1 à n. Imaginons cela comme un tableau de points, où nous passons par tous les points, du premier (i=1) au dernier (i=n).
* Pour chaque point, nous prenons la coordonnée y du point, et la coordonnée y'. La coordonnée y est notre point violet. Le point y' se situe sur la ligne que nous avons créée. Nous soustrayons la valeur de la coordonnée y de la valeur de la coordonnée y', et nous calculons le carré du résultat.
* La troisième partie consiste à prendre la somme de toutes les valeurs (y-y')², et à la diviser par n, ce qui donnera la moyenne.

Notre objectif est de minimiser cette moyenne, ce qui nous fournira la meilleure ligne qui passe par tous les points.

### Du concept aux équations mathématiques

Cette partie est **pour les personnes qui veulent comprendre comment nous avons obtenu les équations mathématiques**. Vous pouvez passer à la partie suivante si vous le souhaitez.

Comme vous le savez, l'équation de la ligne est y=mx+b, où m est la [pente](https://en.wikipedia.org/wiki/Slope) et b est l'[ordonnée à l'origine](https://en.wikipedia.org/wiki/Y-intercept).

Prenons chaque point sur le graphique, et nous ferons notre calcul (y-y')². 
Mais qu'est-ce que y', et comment le calculons-nous ? Nous ne l'avons pas comme partie des données.

Mais nous savons que, pour calculer y', nous devons utiliser notre équation de ligne, y=mx+b, et mettre le x dans l'équation.

De là, nous obtenons l'équation suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/wSige6ZLxM-QaVt3fRWXIAzsHvX7wdcJ4XOy)

Réécrivons cette expression pour la simplifier.

![Image](https://cdn-media-1.freecodecamp.org/images/JFi5pzT7YtJ-0Fkx59jP0hCNHzc8tvsrXgPg)

Commençons par ouvrir toutes les parenthèses dans l'équation. J'ai coloré la différence entre les équations pour faciliter la compréhension.

![Image](https://cdn-media-1.freecodecamp.org/images/vWLTze9HzNDSg4LRM5dbpkYUpkXkhTW6TnRl)

Maintenant, appliquons une autre manipulation. Nous allons prendre chaque partie et les mettre ensemble. Nous allons prendre tous les y, et (-2ymx) et etc, et nous allons les mettre tous côte à côte.

![Image](https://cdn-media-1.freecodecamp.org/images/y3gkwSWxwAOcxfxMILLV0teW1273PFtFiqW4)

À ce stade, nous commençons à être désordonnés, alors prenons la moyenne de toutes les valeurs quadratiques pour y, xy, x, x².

Définissons, pour chacune, un nouveau caractère qui représentera la moyenne de toutes les valeurs quadratiques.

Prenons un exemple, prenons toutes les valeurs y, et divisons-les par n puisque c'est la moyenne, et appelons cela y(HeadLine).

![Image](https://cdn-media-1.freecodecamp.org/images/L3NWDFs1LUKgQU223EAFXXUXX3OTFWR0gLtE)

Si nous multiplions les deux côtés de l'équation par n, nous obtenons :

![Image](https://cdn-media-1.freecodecamp.org/images/jyiOt9MVCg460395d6mkHlrmK9ssfr8nQGJC)

Ce qui nous mènera à l'équation suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/bv3wucYBgHc3Zch115zMYjhH-zYe5VgwjMAH)

Si nous regardons ce que nous avons obtenu, nous pouvons voir que nous avons une surface 3D. Elle ressemble à un verre, qui monte brusquement vers le haut.

Nous voulons trouver M et B qui minimisent la fonction. Nous allons faire une dérivée partielle par rapport à M et une dérivée partielle par rapport à B.

Puisque nous cherchons un point minimum, nous allons prendre les dérivées partielles et les comparer à 0.

![Image](https://cdn-media-1.freecodecamp.org/images/88voRjo799rIopVP8YjsHlNhrBSJ8REg26hY)
_Formule des dérivées partielles_

![Image](https://cdn-media-1.freecodecamp.org/images/6t-4Uq4Y4GMGg9mYWPUUmHHsmaTvxuDPZCj3)
_Dérivées partielles_

Prenons les deux équations que nous avons reçues, isolons la variable b des deux, puis soustrayons l'équation supérieure de l'équation inférieure.

![Image](https://cdn-media-1.freecodecamp.org/images/-I3Ly2wOtJf9WiecfOjvFiY6U9DXB4PJBQ6t)
_Différente écriture des équations après la dérivation par parties_

Soustrayons la première équation de la deuxième équation

![Image](https://cdn-media-1.freecodecamp.org/images/6WzsJxr0jSG8XPYz-F2dSmINqnexxJLxWsxi)
_Fusionner deux équations ensemble_

Débarrassons-nous des dénominateurs de l'équation.

![Image](https://cdn-media-1.freecodecamp.org/images/Ac05NR92faqptoFE35F2XFcKjllJhJPdwGnE)
_Équation finale pour trouver M._

Et voilà, voici l'équation pour trouver M, prenons cela et écrivons l'équation de B.

![Image](https://cdn-media-1.freecodecamp.org/images/pjxjeSICBJNckegf3WXCHtfrf7dyIxVfqbBB)
_Équation finale pour trouver B._

### Équations pour la pente et l'ordonnée à l'origine

Fournissons les équations mathématiques qui nous aideront à trouver la [pente](https://en.wikipedia.org/wiki/Slope) et l'[ordonnée à l'origine](https://en.wikipedia.org/wiki/Y-intercept) requises.

![Image](https://cdn-media-1.freecodecamp.org/images/290zZ8roKAfKNCrfq1LN7QuTooJjbH19Isiv)
_Équations de la pente et de l'ordonnée à l'origine_

Vous vous demandez probablement, qu'est-ce que ces équations bizarres ?

Elles sont en fait simples à comprendre, alors parlons-en un peu.

![Image](https://cdn-media-1.freecodecamp.org/images/KTFy4uhGXnGSrCoyInhSWfHH4VTEnAJyncpm)
_Somme de x divisée par n_

![Image](https://cdn-media-1.freecodecamp.org/images/lQSFx0h7KiRB0uOcriwpFrmhsev3kt4cCUU5)
_Somme de x² divisée par n_

![Image](https://cdn-media-1.freecodecamp.org/images/LYZL8LPc8vyZ0wPV2J2sp-pXiuCzvslY8EAQ)
_Somme de xy divisée par n_

![Image](https://cdn-media-1.freecodecamp.org/images/0E27klUj208HeeecnRKR9Eokb2PmKfUNoO-O)
_Somme de y divisée par n_

Maintenant que nous comprenons nos équations, il est temps de tout rassembler et de montrer quelques exemples.

### Exemples

Un grand merci à [Khan Academy](https://www.khanacademy.org/) pour les exemples.

#### Exemple #1

Prenons 3 points, (1,2), (2,1), (4,3).

![Image](https://cdn-media-1.freecodecamp.org/images/IudmVD0mo4BMYqPEjFyETchb5GGsDv5ikxwB)
_Points sur le graphique._

Trouvons M et B pour l'équation y=mx+b.

![Image](https://cdn-media-1.freecodecamp.org/images/KFDixcE4WidM6Pez8RNDwOgBorpnj1QuLw5S)
_Somme des valeurs x et division par n_

![Image](https://cdn-media-1.freecodecamp.org/images/Rqkh4dC9zZ11V4McMwJFspxv5UySTiI9Sv1L)
_Somme des valeurs y et division par n_

![Image](https://cdn-media-1.freecodecamp.org/images/tkUVYMlF-9qDaK69dWj0bFy1ApEK4DHw05vK)
_Somme des valeurs xy et division par n_

![Image](https://cdn-media-1.freecodecamp.org/images/80W3OcjPxF9ek2HIjv0VYnwCEhpzURavMAlj)
_Somme des valeurs x² et division par n_

Après avoir calculé les parties pertinentes pour notre équation M et notre équation B, mettons ces valeurs dans les équations et obtenons la [pente](https://en.wikipedia.org/wiki/Slope) et l'[ordonnée à l'origine](https://en.wikipedia.org/wiki/Y-intercept).

![Image](https://cdn-media-1.freecodecamp.org/images/Hri9luC8oVUAgZLnLoDgey4X0T6LEZwIFMav)
_Calcul de la pente_

![Image](https://cdn-media-1.freecodecamp.org/images/H4Ss6UYBdSfJgx63lz93uXaubcE3-6e1niFS)
_Calcul de l'ordonnée à l'origine_

Prenons ces résultats et mettons-les dans l'équation de la ligne y=mx+b.

![Image](https://cdn-media-1.freecodecamp.org/images/S9EESO6mBvglt1o--YlQZQFqhNGPg4we6Kju)

Maintenant, traçons la ligne et voyons comment la ligne passe à travers les lignes de telle manière qu'elle minimise les distances quadratiques.

![Image](https://cdn-media-1.freecodecamp.org/images/DlKy-Eekc0SdHpcOeQPGJobo7jYLfTh0pI8Q)
_Ligne de régression qui minimise l'EQM._

#### Exemple #2

Prenons 4 points, (-2,-3), (-1,-1), (1,2), (4,3).

![Image](https://cdn-media-1.freecodecamp.org/images/MrlSNVYUJEh-4OcRGXEe3hbeU10wjTH-vmDB)
_Points sur le graphique._

Trouvons M et B pour l'équation y=mx+b.

![Image](https://cdn-media-1.freecodecamp.org/images/MqNv9HXhu7koehCq1WgBSH2Mje3VoHUM6Dsb)
_Somme des valeurs x et division par n_

![Image](https://cdn-media-1.freecodecamp.org/images/I8bZESRhxejhmNWbxMlusVlxfCgnrJPbn2En)
_Somme des valeurs y et division par n_

![Image](https://cdn-media-1.freecodecamp.org/images/YwF2k-wP1YkSiPUoZZ5kV99p5xpS4VeBtlxP)
_Somme des valeurs xy et division par n_

![Image](https://cdn-media-1.freecodecamp.org/images/Sbo7-PaRePrfBM1sOME5du5GDQ-1r1ntdoD1)
_Somme des valeurs x² et division par n_

Comme précédemment, mettons ces valeurs dans nos équations pour trouver M et B.

![Image](https://cdn-media-1.freecodecamp.org/images/LUideJM-zrCgulLv83Gh08ySgcChQXY6BpxC)
_Calcul de la pente_

![Image](https://cdn-media-1.freecodecamp.org/images/F9K53LF0Dp3kjIYYC3UJoLfGJqICCIhtqTMo)
_Calcul de l'ordonnée à l'origine_

Prenons ces résultats et mettons-les dans l'équation de la ligne y=mx+b.

![Image](https://cdn-media-1.freecodecamp.org/images/0o5OFw2QwtBJYntrz4vRJn9ywrdsumLxH5rg)

Maintenant, traçons la ligne et voyons comment la ligne passe à travers les lignes de telle manière qu'elle minimise les distances quadratiques.

![Image](https://cdn-media-1.freecodecamp.org/images/yAMNsNJmTBdZ2MKPbD8JX-es3d-5Oj4OIHRl)
_Ligne de régression qui minimise l'EQM_

### En conclusion

Comme vous pouvez le voir, l'idée est simple. Nous devons simplement comprendre les parties principales et comment nous travaillons avec elles.

Vous pouvez travailler avec les formules pour trouver la ligne sur un autre graphique, et effectuer un calcul simple et obtenir les résultats pour la [pente](https://en.wikipedia.org/wiki/Slope) et l'[ordonnée à l'origine](https://en.wikipedia.org/wiki/Y-intercept).

C'est tout, simple, n'est-ce pas ? ?

Tous les commentaires et retours sont les bienvenus — si nécessaire, je corrigerai l'article.

N'hésitez pas à me contacter directement sur LinkedIn — [Cliquez ici](http://www.linkedin.com/in/moshe-binieli-22b11a137).
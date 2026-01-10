---
title: Qu'est-ce qu'une valeur aberrante ? Définition et comment trouver des valeurs
  aberrantes en statistiques
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-24T20:32:36.000Z'
originalURL: https://freecodecamp.org/news/what-is-an-outlier-definition-and-how-to-find-outliers-in-statistics
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/rupert-britton-l37N7a1lL6w-unsplash.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: statistics
  slug: statistics
seo_title: Qu'est-ce qu'une valeur aberrante ? Définition et comment trouver des valeurs
  aberrantes en statistiques
seo_desc: 'Outliers are an important part of a dataset. They can hold useful information
  about your data.

  Outliers can give helpful insights into the data you''re studying, and they can
  have an effect on statistical results. This can potentially help you disover...'
---

Les valeurs aberrantes sont une partie importante d'un ensemble de données. Elles peuvent contenir des informations utiles sur vos données.

Les valeurs aberrantes peuvent donner des informations utiles sur les données que vous étudiez, et elles peuvent avoir un effet sur les résultats statistiques. Cela peut potentiellement vous aider à découvrir des incohérences et à détecter toute erreur dans vos processus statistiques.

Ainsi, savoir comment trouver des valeurs aberrantes dans un ensemble de données vous aidera à mieux comprendre vos données.

Il existe plusieurs façons de trouver des valeurs aberrantes en statistiques.

Cet article expliquera comment détecter les valeurs aberrantes numériques en calculant l'écart interquartile.

Je donne un exemple d'un ensemble de données très simple et comment calculer l'écart interquartile, afin que vous puissiez suivre si vous le souhaitez.

Commençons !

## Qu'est-ce qu'une valeur aberrante en statistiques ? Une définition

En termes simples, une valeur aberrante est un point de données extrêmement élevé ou extrêmement bas par rapport au point de données le plus proche et au reste des valeurs coexistantes voisines dans un graphique de données ou un ensemble de données avec lequel vous travaillez.

Les valeurs aberrantes sont des valeurs extrêmes qui se distinguent grandement de l'ensemble général des valeurs dans un ensemble de données ou un graphique.

Ci-dessous, à l'extrême gauche du graphique, il y a une valeur aberrante.

La valeur du mois de janvier est significativement inférieure à celle des autres mois.


![Screenshot-2021-08-24-at-3.07.05-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-24-at-3.07.05-PM.jpeg)

## Comment identifier une valeur aberrante dans un ensemble de données

Très bien, comment procédez-vous pour trouver des valeurs aberrantes ?

Une valeur aberrante doit satisfaire l'une des deux conditions suivantes :


```
valeur_aberrante < Q1 - 1.5(IQR)
```

```
valeur_aberrante > Q3 + 1.5(IQR)
```

La règle pour une valeur aberrante basse est qu'un point de données dans un ensemble de données doit être inférieur à `Q1 - 1.5xIQR`.
  
Cela signifie qu'un point de données doit être inférieur de plus de 1,5 fois l'écart interquartile *en dessous* du premier quartile pour être considéré comme une valeur aberrante basse.

La règle pour une valeur aberrante haute est que si un point de données dans un ensemble de données est supérieur à `Q3 - 1.5xIQR`, c'est une valeur aberrante haute.
 
Plus précisément, le point de données doit être supérieur de plus de 1,5 fois l'écart interquartile *au-dessus* du troisième quartile pour être considéré comme une valeur aberrante haute.

Comme vous pouvez le voir, il y a certaines valeurs individuelles que vous devez d'abord calculer dans un ensemble de données, comme l'`IQR`. Mais pour trouver l'`IQR`, vous devez trouver les premier et troisième quartiles, qui sont respectivement `Q1` et `Q3`. 

Alors, voyons ce que chacun de ceux-ci fait et décomposons comment trouver leurs valeurs dans un ensemble de données impair et pair.


## Comment trouver les quartiles supérieur et inférieur dans un ensemble de données impair

Pour commencer, disons que vous avez cet ensemble de données :

```
25,14,6,5,5,30,11,11,13,4,2
```

La première étape consiste à **trier les valeurs par ordre numérique croissant**, du plus petit au plus grand nombre.

```
2,4,5,5,6,11,11,13,14,25,30
```

La valeur la plus basse (**MIN**) est `2` et la plus haute (**MAX**) est `30`.

### Comment calculer `Q2` dans un ensemble de données impair

L'étape suivante consiste à trouver la **médiane** ou *quartile 2 (Q2)*.

Cet ensemble particulier de données a un nombre impair de valeurs, avec un total de `11` scores.

Trouver la médiane dans un ensemble de données signifie que vous trouvez la valeur du milieu – le nombre unique du milieu dans l'ensemble.

Dans les ensembles de données impairs, il n'y a qu'un seul nombre du milieu.

Puisqu'il y a `11` valeurs au total, une façon facile de faire cela est de diviser l'ensemble en deux parties égales, chaque côté contenant `5` valeurs.

La valeur médiane aura `5` valeurs d'un côté et `5` valeurs de l'autre.

`(2,4,5,5,6)`, **`11`** ,`(11,13,14,25,30)`

La médiane est `11` car c'est le nombre qui sépare la première moitié de la deuxième moitié.

Une autre façon de vérifier si vous avez raison est de faire ceci :

 `(nombre_total_de_scores + 1) / 2`.
 
Cela donne `(11 + 1) /2 = 6`, ce qui signifie que vous voulez le nombre à la `6ème` place de cet ensemble de données – qui est `11`.

Donc `Q2 = 11`.
 
### Comment calculer `Q1` dans un ensemble de données impair

Ensuite, pour trouver le *quartile inférieur*, `Q1`, nous devons trouver la médiane de la première moitié de l'ensemble de données, qui se trouve du côté gauche.

Pour rappel, l'ensemble de données initial est :

`(2,4,5,5,6)`, **`11`** ,`(11,13,14,25,30)`


La première moitié de l'ensemble de données, ou la *moitié inférieure*, n'inclut pas la médiane :

```
2,4,5,5,6
```

Cette fois, il y a à nouveau un ensemble impair de scores – spécifiquement, il y a `5` valeurs.

Vous voulez à nouveau diviser cet ensemble en deux, avec un nombre égal de deux valeurs de chaque côté. Vous obtiendrez un nombre unique, qui sera le nombre du milieu des `5` valeurs.

Choisissez la valeur du milieu qui se distingue :

`(2,4)`,**`5`**,`(5,6)`

Dans ce cas, c'est `Q1 = 5`.

Pour vérifier, vous pouvez également faire `nombre_total_de_valeurs + 1 / 2`, similaire à l'exemple précédent :

`(5 + 1) /2 =  3`.

Cela signifie que vous voulez le nombre à la 3ème place, qui est `5`.

### Comment calculer `Q3` dans un ensemble de données impair

Pour trouver le *quartile supérieur*, Q3, le processus est le même que pour `Q1` ci-dessus. Mais dans ce cas, vous prenez la deuxième moitié du côté droit de l'ensemble de données, au-dessus de la médiane et sans inclure la médiane elle-même :


`(2,4,5,5,6)`, **`11`** ,`(11,13,14,25,30)`

```
11,13,14,25,30
```

Vous divisez cette moitié de l'ensemble impair de nombres en deux pour trouver la médiane et ensuite la valeur de `Q3`. 

Vous voulez à nouveau le nombre à la 3ème place comme vous l'avez fait pour la première moitié.

`(11,13)`,**`14`**,`(25,30)`


Donc `Q3 = 14`.

### Comment calculer `IQR` dans un ensemble de données impair

Maintenant, l'étape suivante consiste à calculer l'IQR, qui signifie Interquartile Range.

C'est la différence/distance entre le quartile inférieur (Q1) et le quartile supérieur (Q3) que vous avez calculés ci-dessus.

Pour rappel, la formule à utiliser est la suivante :

```
IQR = Q3 - Q1
```

Pour trouver l'IQR de l'ensemble de données ci-dessus :

```
IQR= 14 - 5
IQR = 9
```

### Comment trouver une valeur aberrante dans un ensemble de données impair

Pour récapituler jusqu'à présent, l'ensemble de données est celui ci-dessous :

```
2,4,5,5,6,11,11,13,14,25,30
```

et jusqu'à présent, vous avez calculé le résumé à cinq nombres :

```
MIN = 2
Q1 = 5
MED = 11
Q3 = 14
MAX = 30
```

Enfin, voyons s'il y a des valeurs aberrantes dans l'ensemble de données.

Pour rappel, une valeur aberrante doit répondre aux critères suivants :

```
valeur_aberrante < Q1 - 1.5(IQR)
```

Ou 

```
valeur_aberrante > Q3 + 1.5(IQR)
```

Pour voir s'il y a une valeur aberrante basse, vous devez calculer la première partie et voir s'il y a un nombre dans l'ensemble qui satisfait la condition.

```
valeur_aberrante < Q1 - 1.5(IQR)
valeur_aberrante < 5 - 1.5(9)
valeur_aberrante < 5 - 13.5 
valeur_aberrante < - 8.5
```

Il n'y a pas de valeurs aberrantes basses, puisque aucun nombre n'est inférieur à `-8.5` dans l'ensemble de données.

Ensuite, pour voir s'il y a des valeurs aberrantes élevées :

```
valeur_aberrante > Q3  + 1.5(IQR)=
valeur_aberrante > 14 + 1.5(9)
valeur_aberrante > 14 + 13.5
valeur_aberrante > 27,5
```

Et il y a un nombre dans l'ensemble de données qui est supérieur à `27,5` :

`2,4,5,5,6,11,11,13,14,25,`**`30`**

Dans ce cas, `30` est la valeur aberrante dans l'ensemble de données existant.

## Comment trouver les quartiles supérieur et inférieur dans un ensemble de données pair

Que se passe-t-il lorsque vous avez un ensemble de données qui consiste en un ensemble pair de données ?

Il n'y a pas seulement une médiane (Q2) qui se distingue, ni un quartile supérieur (Q1) ou un quartile inférieur (Q3) qui se distingue.

Ainsi, le processus de calcul des quartiles et ensuite de recherche d'une valeur aberrante est un peu différent.


### Comment calculer `Q2` dans un ensemble de données pair

Disons que vous avez cet ensemble de données avec `8` nombres :

`10,15,20,26,28,30,35,40`

Cette fois, les nombres sont déjà triés du plus bas au plus haut.

Pour trouver le nombre **médian** dans un ensemble de données pair, vous devez trouver la valeur qui serait entre les *deux* nombres qui sont au milieu. Vous les additionnez et les divisez par `2`, comme ceci :

`10,15,20`,**`26,28`**,`30,35,40`

```
26 + 28 = 54
54 / 2 = 27
```


### Comment calculer `Q1` dans un ensemble de données pair

Pour calculer les quartiles supérieur et inférieur dans un ensemble de données pair, vous gardez tous les nombres dans l'ensemble de données (contrairement à l'ensemble impair où vous avez retiré la médiane).

Cette fois, l'ensemble de données est coupé en deux.

`10,15,20,26 | 28,30,35,40`

Pour trouver `Q1`, vous divisez la première moitié de l'ensemble de données en deux, ce qui vous laisse avec un ensemble pair restant :

`10,15 | 20,26 `

Pour trouver la médiane de cette moitié, vous prenez les deux nombres du milieu et les divisez par deux :

```
Q1 = (15 + 20)/2
Q1 =  35 / 2
Q1 = 17,5
```

### Comment calculer `Q3` dans un ensemble de données pair

Pour trouver `Q3`, vous devez vous concentrer sur la deuxième moitié de l'ensemble de données et diviser cette moitié en deux :

`28,30,35,40` -> `28,30 | 35,40`

Les deux nombres du milieu sont `30` et `35`.

Vous les additionnez et les divisez par deux, et le résultat est :

```
Q3 = (30 + 35)/2
Q3 =  65 / 2
Q3 = 32,5
```


### Comment calculer l'`IQR` dans un ensemble de données pair

La formule pour calculer l'IQR est exactement la même que celle que nous avons utilisée pour le calculer pour l'ensemble de données impair.

```
IQR = Q3 - Q1
IQR = 32,5 - 17,5
IQR = 15
```

### Comment trouver une valeur aberrante dans un ensemble de données pair

Pour récapituler, jusqu'à présent, le résumé à cinq nombres est le suivant :


```
MIN = 10
Q1 = 17,5
MED = 27
Q3 = 32,5
MAX = 40
```

Pour calculer les valeurs aberrantes dans l'ensemble de données :

```
valeur_aberrante < Q1 - 1.5(IQR)
```

Ou

```
valeur_aberrante > Q3 + 1.5(IQR)
```

Pour trouver les valeurs aberrantes basses, vous calculez `Q1 - 1.5(IQR)` et voyez s'il y a des valeurs inférieures au résultat.


```
valeur_aberrante < 17,5 - 1.5(15)=
valeur_aberrante < 17,5 - 22,5
valeur_aberrante < -5
```

Il n'y a pas de valeurs dans l'ensemble de données qui sont inférieures à `-5`.

Enfin, pour trouver les valeurs aberrantes élevées, vous calculez ` Q3 - 1.5(IQR)` et voyez s'il y a des valeurs dans l'ensemble de données qui sont supérieures au résultat

```
valeur_aberrante > 32.5 + 1.5(15)=
valeur_aberrante > 32.5 + 22.5
valeur_aberrante > 55
```

Il n'y a pas de valeurs supérieures à `55`, donc cet ensemble de données n'a pas de valeurs aberrantes.

## Conclusion

Dans cet article, vous avez appris comment trouver l'écart interquartile dans un ensemble de données et, de cette manière, calculer les valeurs aberrantes.

Si vous êtes intéressé à en apprendre davantage sur les statistiques et les bases de la science des données, consultez ce [cours universitaire gratuit de 8 heures](https://www.youtube.com/watch?v=xxpc-HPKN28) sur la chaîne YouTube de freeCodeCamp.

Merci pour votre lecture et bon apprentissage.
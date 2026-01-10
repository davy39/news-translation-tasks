---
title: Pearson, valeurs p et graphiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-02T16:16:40.000Z'
originalURL: https://freecodecamp.org/news/pearson-p-values-and-plots-d5eed2fd6d1a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Mk8UtVD2OeVn4KuI.jpg
tags:
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pearson, valeurs p et graphiques
seo_desc: 'By Michelle Jones

  What is a p-value?


  If your experiment needs statistics, you ought to have done a better experiment.
  — Ernest Rutherford


  The use of p-values in research is very common. Peer reviewed journal articles are
  chock-full of them. It seem...'
---

Par Michelle Jones

### Qu'est-ce qu'une valeur p ?

> Si votre expérience nécessite des statistiques, vous auriez dû faire une meilleure expérience. — Ernest Rutherford

L'utilisation des valeurs p dans la recherche est très courante. Les articles de revues évalués par des pairs en sont remplis. Il semble que chaque scientifique et leur chien bavant les utilisent.

D'accord, sans chercher la réponse :

> quelle est la définition d'une valeur p ?

Soyez honnête, je ne dirai à personne votre réponse. Je promets. C'est notre secret. Nous reviendrons régulièrement à cette question au cours de mes prochains articles.

Nous commençons notre voyage avec Pearson.

### Karl Pearson

En 1900, Karl Pearson a publié [son article](http://www.medicine.mcgill.ca/epidemiology/hanley/tmp/proportion/Pearson1900.pdf) qui discutait du concept des valeurs p. La majeure partie de l'article est constituée d'exemples détaillés sous la forme que nous connaissons comme le test du chi-carré. Ainsi, l'accent de l'article est mis sur les fréquences de comptes, et le degré auquel les comptes observés diffèrent (en termes de Pearson, dévient) des comptes attendus. En termes statistiques, chaque déviation (n) est une erreur.

Sa définition de P était la suivante :

> la probabilité qu'un système complexe de n erreurs se produise avec une fréquence aussi grande ou plus grande que celle du système observé (p.158)

En d'autres termes, étant donné les comptes attendus, à quel point nos comptes observés **et** les comptes qui sont encore plus différents sont-ils probables ?

#### Deux principaux types de tests du chi-carré

Il y a un point clé à noter concernant le test du chi-carré de Fisher. Oui, sa méthode détermine si les comptes observés diffèrent des comptes attendus. Cependant, il a directement comparé les comptes observés à leurs comptes attendus sur la base d'une distribution sous-jacente prédéterminée. Il s'agit d'un test d'adéquation. Les types de questions qu'il posait étaient :

* cet ensemble de résultats de lancers de dés suit-il une distribution binomiale ?
* cet ensemble de comptes de pétales de 222 boutons d'or correspond-il à une courbe de biais spécifique ?

Cela est complètement différent de la manière dont nous utilisons normalement un test du chi-carré, où nous comparons deux groupes, plutôt qu'un groupe à une distribution prédéfinie :

* les cas et les témoins (par exemple, fumeurs/non-fumeurs) diffèrent-ils significativement en termes d'incidence de la maladie (par exemple, cancer du poumon) ?
* les hommes et les femmes votent-ils pour les mêmes candidats politiques ?

Dans notre cas normal, les comptes attendus (et donc la distribution) sont directement dérivés des marges du tableau de contingence. Dans cette deuxième méthode, nous effectuons le test du chi-carré d'indépendance. (Il existe un autre type de test du chi-carré qui utilise essentiellement la même analyse que celle-ci, mais c'est une technicalité que nous ignorerons.)

Revenons au test du chi-carré d'adéquation.

### Lancer de dés

Travaillons à travers le premier exemple de Pearson en utilisant **R**. Le R de base est suffisant pour cela. Nous utiliserons R pour calculer la valeur du chi-carré (_χ²_) nous-mêmes. Enfin, nous additionnerons les comptes théoriques et observés pour vérifier que les nombres sont ceux que nous attendons du tableau de l'article.

#### Description de l'expérience

Les données proviennent d'une expérience où douze dés ont été lancés 26 306 fois. À chaque lancer, le nombre de dés montrant un 5 ou un 6 était compté. (J'imagine que c'était un pauvre étudiant diplômé qui a tiré le mauvais sort.)

Avec 12 dés, la plage de nombres possibles à chaque lancer va de zéro (aucun dé ne montre un 5 ou un 6) à douze (tous les dés montrent un 5 ou un 6).

#### Distribution binomiale

Les valeurs pour les dés lancés suivent une distribution binomiale. Nous utilisons cette distribution pour les données de comptage. Pour ceux qui s'intéressent à la relation entre la distribution binomiale et le test du chi-carré, [voici une explication accessible](http://davidquigley.com/talks/2015/biostatistics/module_07.1.html).

Les valeurs attendues pour chaque valeur possible dans la plage de 0 à 12 peuvent être calculées en utilisant la fonction `dbinom` dans R. Par exemple, la probabilité d'obtenir **zéro** dé montrant un 5 ou un 6 lorsque 12 dés sont lancés est

```
dbinom(0,12,1/3)[1] 0.007707347
```

Nous multiplions la probabilité par le nombre total d'essais pour obtenir le compte attendu pour aucun 5 **et** aucun 6 sur les 26 306 essais

```
dbinom(0,12,1/3)*26306[1] 202.7495
```

Que nous arrondissons à 203. Nous pouvons répéter ce processus pour les valeurs de 1 à 12. Cependant, lorsque nous atteignons 12, nous obtenons le problème suivant.

```
dbinom(12,12,1/3)[1] 1.881676e-06
```

```
dbinom(12,12,1/3)*26306[1] 0.04949938
```

Notre probabilité et le compte associé sont extrêmement proches de 0. Plus sur cela ci-dessous.

#### Créer le data.frame

Nous allons construire le data.frame au fur et à mesure que nous lisons les valeurs.

```
PearsonChiSquare <- data.frame(Face5or6=c(0,1,2,3,4,5,6,7,8,9,10,11,12),                                  Theoretical=c(203,1217,3345,5576,6273,5018,2927,1254,392,87,13,1,0),                                  Observed=c(185,1149,3265,5475,6114,5194,3067,1331,403,105,14,4,0))
```

Revenons au problème avec nos données, qui ne se manifestera que lorsque nous effectuerons le test du chi-carré. Remarquez les 0 comptes théoriques et attendus pour tous les 12 dés montrant 5 ou 6 ? Le test du chi-carré ne nous donnera pas de résultat lorsqu'il y a une division par 0.

Que pouvons-nous faire ? La méthode la plus simple pour traiter ce problème est de supprimer la dernière ligne du data.frame. Dans notre cas, cela revient exactement à combiner les catégories 11 et 12 (la méthode normale lorsque les comptes de cellules sont très petits). Notre compte d'essai reste le même. Nos probabilités sous-jacentes s'additionnent presque à 1. Nous ferons une petite correction pour cela.

Nous supprimons la ligne où la valeur théorique est 0. J'aurais pu résoudre ce problème en ne lisant tout simplement pas les valeurs 0. Cependant, supprimer une ligne de data.frame en fonction d'une valeur est une tâche courante dans R. Ce code peut être généralisé à toute instance où vous devez supprimer une ou plusieurs lignes sur la base d'une valeur spécifique d'une variable.

```
#as group of 12 has 0 theoretical and 0 observed counts, drop this observationPearsonChiSquare <- PearsonChiSquare[!(PearsonChiSquare$Theoretical==0),]
```

Maintenant, nous construisons notre colonne de probabilités théoriques sur la base des données restantes. Rappelez-vous, la probabilité d'avoir douze dés avec des 5 ou des 6 était très faible, mais n'était pas nulle. Ainsi, les probabilités calculées pour chaque ligne de nos données restantes différeront légèrement des probabilités que Pearson utilisait.

```
PearsonChiSquare$probs <- with(PearsonChiSquare, Theoretical/sum(Theoretical))
```

Pourquoi devons-nous créer une colonne de probabilités ? Parce que nous effectuons un test d'adéquation. Nous comparons chaque compte observé à la probabilité de ce compte, en supposant une distribution binomiale.

#### Test du chi-carré

Maintenant, nous sommes prêts à effectuer notre test du chi-carré. La sortie est affichée ci-dessous la commande.

```
chisq.test(x=PearsonChiSquare$Observed, p=PearsonChiSquare$probs)
```

```
Chi-squared test for given probabilities
```

```
data:  PearsonChiSquare$ObservedX-squared = 43.876, df = 11, p-value = 7.641e-06
```

La fonction calcule automatiquement le nombre de degrés de liberté (df) à partir de nos données. Le calcul du nombre de df dans le test du chi-carré est très simple. Il est (lignes -1) x (colonnes-1).

Nous avons 12 catégories (plage de 0 à 11 = 12 catégories). Nous avons deux colonnes (comptes observés, probabilités binomiales). Nos df sont donc (121) x (21) = 11 x 1 = 11.

Comment nous en sommes-nous sortis pour la valeur _χ²_ ? Surtout puisque nous avons supprimé une ligne de données ?

Pearson a calculé _χ²_=43.87241. Nous avons obtenu très proche ! Il a calculé P=0.000016. Il a soutenu que son résultat donnait 62 499 contre 1 contre les valeurs observées provenant d'une distribution binomiale. En mettant notre résultat en notation décimale, nous avons obtenu P=0.0000076.

Notre valeur p est très petite. Nous rejetons l'hypothèse nulle selon laquelle nos résultats observés proviennent d'une distribution binomiale.

#### Qu'est-ce qui cause la différence ?

La raison de cela est le biais positif envers le lancer d'un 5 ou 6 (sauf dans le cas extrême de tous les 5 ou 6). Nous pouvons dupliquer ce biais en calculant les écarts des valeurs observées par rapport aux valeurs théoriques, en dupliquant davantage le travail de Pearson.

Le code ci-dessous effectue ce calcul puis écrit les valeurs dans la console.

```
PearsonChiSquare$Deviation <- with(PearsonChiSquare,Observed-Theoretical)
```

```
PearsonChiSquare[, c("Face5or6","Deviation")]
```

```
   Face5or6 Deviation1         0       -182         1       -683         2       -804         3      -1015         4      -1596         5       1767         6       1408         7        779         8        1110        9        1811       10         112       11         3
```

Comme vous pouvez le voir, les comptes observés pour les essais où cinq dés ou moins montraient un 5 ou un 6 sont inférieurs aux attentes (ce sont toutes des valeurs négatives). Inversement, les comptes observés pour les essais où six dés ou plus montraient un 5 ou un 6 sont supérieurs aux attentes (ce sont toutes des valeurs positives).

#### Interprétation de la valeur p

En paraphrasant, Pearson a dit que la valeur p est la probabilité de résultats qui sont **aussi improbables ou plus improbables** que celui rencontré. Notre valeur p est la probabilité d'obtenir notre valeur _χ²_ **et** toute valeur _χ²_ plus grande.

Pourquoi la valeur p n'est-elle pas liée uniquement aux comptes que nous avons ajustés ? La valeur p provient d'une [fonction de densité cumulative](https://en.wikipedia.org/wiki/Cumulative_distribution_function). La probabilité d'obtenir nos résultats exacts, ou tout compte spécifié, est très proche de 0. Pour la statistique du chi-carré, nous évaluons l'intégrale où **notre valeur _χ²_ est la borne inférieure**. Pour les très intéressés, [voici une description des mathématiques](http://mathworld.wolfram.com/Chi-SquaredDistribution.html).

### Visualisation des valeurs p du chi-carré dans R

#### Notre distribution du chi-carré

Nous pouvons visualiser la distribution du chi-carré dans R. Dessiner la distribution de probabilité pour la distribution du chi-carré lorsqu'il y a 11 degrés de liberté. Rappelez-vous, notre test avait 11 degrés de liberté. Comme vous pouvez le voir, j'utilise [mon package préféré](https://cran.r-project.org/web/packages/ggplot2/index.html) pour cela.

```
library("ggplot2")ggplot(data.frame(x=c(0,50)), aes(x=x))+        stat_function(fun=dchisq, args=list(df=11))+        labs(title="Distribution de probabilité du chi-carré pour 11 df",             x="Valeur du chi-carré",             y="Probabilité")
```

Cela produit le graphique suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/dsRpSaqpezu8B0q5NK7JON7pnLLJ8Fyq0jOs)

Nous lisons les probabilités associées aux valeurs _χ²_ de droite à gauche. Comme vous pouvez le voir sur le graphique, la probabilité d'obtenir une valeur _χ²_ supérieure à 40 est extrêmement faible. Nous savons qu'elle est inférieure à 0,000 car la ligne est plate à ce point. Les probabilités peuvent devenir très petites, mais elles ne peuvent pas atteindre zéro.

#### Distribution du chi-carré de Pearson

Et si nous avions les 12 degrés de liberté originaux de Pearson, parce que nous n'avons pas supprimé ce groupe (et supposons que nous avons triché sur le problème du 0) ? Superposons les distributions de probabilité pour 12 degrés de liberté sur la distribution que nous avons déjà tracée.

```
ggplot(data.frame(x=c(0,50)), aes(x=x))+        stat_function(fun=dchisq, args=list(df=11), aes(colour="11 df"))+        stat_function(fun=dchisq, args=list(df=12), aes(colour="12 df"))+        scale_colour_manual(name="", values=c("black","blue"))+        labs(title="Distribution de probabilité du chi-carré pour 11 et 12 df",             x="Valeur du chi-carré",             y="Probabilité")
```

Ce qui produit le graphique :

![Image](https://cdn-media-1.freecodecamp.org/images/7Z9mNgluv46n13ddCoPrGEMKcC5IsHKAOh8G)

Nous pouvons voir que la différence entre notre valeur _χ²_ et la valeur _χ²_ de Pearson est négligeable, considérée par rapport à la distribution de probabilité _χ²_ pertinente.

En termes pratiques, la valeur _χ²_ doit être assez petite pour accepter l'hypothèse nulle. L'hypothèse nulle, dans ce cas, est que les données observées proviennent d'une distribution binomiale.

#### Affichage de la zone de rejet pour des valeurs p spécifiques

Nous pouvons montrer comment la valeur p change lorsque la valeur _χ²_ est diminuée. Cela montre également comment la valeur _χ²_ agit comme la borne inférieure sur la zone de rejet. Si nous voulons rejeter à P ≤ 0,025, nous pouvons montrer la zone de rejet sur le graphique.

```
RejectionArea   <- data.frame(x=seq(0,50,0.1))RejectionArea$y <- dchisq(RejectionArea$x,11)
```

```
library(ggplot2)ggplot(RejectionArea) +   geom_path(aes(x,y)) + geom_ribbon(data=RejectionArea[RejectionArea$x>qchisq(0.025,11,lower.tail = FALSE),],                 aes(x, ymin=0, ymax=y),fill="red")+  labs(title="Distribution de probabilité du chi-carré pour 11 df montrant la zone de rejet\npour p<=0.025",       x="Valeur du chi-carré",       y="Probabilité")
```

![Image](https://cdn-media-1.freecodecamp.org/images/JwWxyr86rPkSTEB6QEGfFCvygPKdbmseXDor)

Nous pouvons montrer cela pour toute valeur p que nous aimons. Voici la zone de rejet lorsque nous définissons p ≤0.05.

![Image](https://cdn-media-1.freecodecamp.org/images/tT19koAqkTwhYmrNDPggMBls1lLpIbNxyr-J)

Comment avons-nous changé la zone de rejet dans le graphique ? Nous avons utilisé `qchisq(0.05,11,lower.tail=FALSE` au lieu de `qchisq(0.025,11,lower.tail=FALSE`. Tout le reste du code est resté exactement le même.

### À venir !

Je vais écrire des articles séparés sur les approches de Fisher et de Neyman-Pearson des valeurs p. Ces deux approches postdatent Pearson. Encore une fois, j'utiliserai R pour démontrer les concepts afin que vous puissiez suivre.

Comme toujours, n'hésitez pas à modifier le code comme vous le souhaitez.
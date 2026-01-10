---
title: Types de données en statistiques - Données nominales, ordinales, par intervalles
  et par ratios expliqués avec des exemples
subtitle: ''
author: Abigail Rennemeyer
co_authors: []
series: null
date: '2019-11-05T19:06:00.000Z'
originalURL: https://freecodecamp.org/news/types-of-data-in-statistics-nominal-ordinal-interval-and-ratio-data-types-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f97740569d1a4ca4367.jpg
tags:
- name: data
  slug: data
- name: statistics
  slug: statistics
seo_title: Types de données en statistiques - Données nominales, ordinales, par intervalles
  et par ratios expliqués avec des exemples
seo_desc: 'If you''re studying for a statistics exam and need to review your data
  types this article will give you a brief overview with some simple examples.

  Because let''s face it: not many people study data types for fun or in their real
  everyday lives.

  So let...'
---

Si vous étudiez pour un examen de statistiques et que vous devez réviser les types de données, cet article vous donnera un bref aperçu avec quelques exemples simples.

Car soyons honnêtes : peu de gens étudient les types de données pour le plaisir ou dans leur vie quotidienne.

Alors, plongeons-nous dans le sujet.

## Données quantitatives vs qualitatives - quelle est la différence ?

En bref : quantitatif signifie que vous pouvez le compter et qu'il est numérique (pensez **quantité** - quelque chose que vous pouvez compter). Qualitatif signifie que vous ne pouvez pas, et qu'il n'est pas numérique (pensez **qualité** - données catégorielles à la place).

Boom ! Simple, non ?

Il y a une autre distinction que nous devons clarifier avant de passer aux types de données réels, et elle concerne les données quantitatives (nombres) : les données discrètes vs. continues.

Les **données discrètes** impliquent des nombres entiers (entiers - comme 1, 356, ou 9) qui ne peuvent pas être divisés en fonction de leur nature.

Comme le nombre de personnes dans une classe, le nombre de doigts sur vos mains, ou le nombre d'enfants que quelqu'un a. Vous ne pouvez pas avoir 1,9 enfant dans une famille (malgré ce que le [recensement pourrait dire](https://www.statista.com/statistics/718084/average-number-of-own-children-per-family/)).

Les **données continues**, en revanche, sont l'opposé. Elles peuvent être divisées autant que vous le souhaitez, et mesurées à plusieurs décimales.

Comme le poids d'une voiture (peut être calculé à plusieurs décimales), la température (32,543 degrés, et ainsi de suite), ou la vitesse d'un avion.

Maintenant, passons aux choses sérieuses.

## Types de données qualitatives

### Données nominales

Les données nominales sont utilisées pour étiqueter des variables sans aucune valeur quantitative. Les exemples courants incluent masculin/féminin (bien que quelque peu dépassé), la couleur des cheveux, les nationalités, les noms des personnes, et ainsi de suite.

En anglais simple : ce sont essentiellement des étiquettes (et nominal vient de "nom" pour vous aider à vous souvenir). Vous avez **les cheveux bruns (ou les yeux bruns)**. Vous êtes **Américain**. Votre nom est **Jane**.

Exemples :

De quelle couleur sont vos cheveux ?

* Brun
* Blond
* Noir
* Arc-en-ciel licorne

Quelle est votre nationalité ?

* Américain
* Allemand
* Kényan
* Japonais

Remarquez que ces variables ne se chevauchent pas. En tout cas pour les statistiques, vous ne pouvez pas avoir à la fois des cheveux bruns et arc-en-ciel licorne. Et elles ne sont vraiment liées que par la catégorie principale dont elles font partie.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/rainbow-hair.jpg)
_Une anomalie statistique...([hétérochromie](latest-hairstyles.com">source</a>). Peut-être que la couleur des yeux aurait été un meilleur exemple. Excluant <a href="https://en.wikipedia.org/wiki/Heterochromia_iridum). On ne peut pas gagner ici._

### Données ordinales

Le point clé avec les données ordinales est de se souvenir que ordinal ressemble à ordre - et c'est l'ordre des variables qui compte. Pas tant les différences entre ces valeurs.

Les échelles ordinales sont souvent utilisées pour mesurer la satisfaction, le bonheur, et ainsi de suite. Avez-vous déjà répondu à l'un de ces sondages, comme celui-ci ?

"Quelle est la probabilité que vous recommandiez nos services à vos amis ?"

* Très probable
* Probable
* Neutre
* Peu probable
* Très peu probable

Voyez-vous, nous ne savons pas vraiment quelle est la différence entre très peu probable et peu probable - ou si c'est la même quantité de probabilité (ou, d'improbabilité) qu'entre probable et très probable. Mais ce n'est pas grave. Nous savons simplement que probable est plus que neutre et peu probable est plus que très peu probable. Tout est dans l'ordre.

## Types de données quantitatives

### Données par intervalles

Les données par intervalles sont amusantes (et utiles) car elles concernent à la fois l'ordre **et** la différence entre vos variables. Cela vous permet de mesurer l'écart type et la [tendance centrale](https://en.wikipedia.org/wiki/Central_tendency).

L'exemple préféré de tous pour les données par intervalles est la température en degrés Celsius. 20 degrés C est plus chaud que 10, et la différence entre 20 degrés et 10 degrés est de 10 degrés. La différence entre 10 et 0 est également de 10 degrés.

Si vous avez besoin d'aide pour vous souvenir de ce que sont les échelles d'intervalles, pensez simplement à la signification de l'intervalle : **l'espace entre**. Donc, non seulement vous vous souciez de l'ordre des variables, mais aussi des valeurs entre elles.

Il y a un petit problème avec les intervalles, cependant : il n'y a pas de "zéro vrai". Un zéro vrai n'a pas de valeur - il n'y a rien de cette chose - mais 0 degré C a définitivement une valeur : il fait assez froid. Vous pouvez également avoir des nombres négatifs.

Si vous n'avez pas de zéro vrai, vous ne pouvez pas calculer les ratios. Cela signifie que l'addition et la soustraction fonctionnent, mais que la division et la multiplication ne fonctionnent pas.

### Données par ratios

Heureusement, il y a les données par ratios. Elles résolvent tous nos problèmes.

Les données par ratios nous informent sur l'ordre des variables, les différences entre elles, et elles ont ce zéro absolu. Ce qui permet d'effectuer et de tirer toutes sortes de calculs et d'inférences.

Les données par ratios sont très similaires aux données par intervalles, sauf que zéro signifie aucun. Pour les données par ratios, il n'est pas possible d'avoir des valeurs négatives.

Par exemple, la taille est une donnée par ratio. Il n'est pas possible d'avoir une taille négative. Si la taille d'un objet est zéro, alors il n'y a pas d'objet. Cela est différent de quelque chose comme la température. À la fois 0 degré et -5 degrés sont des températures complètement valides et significatives.

Maintenant que vous avez une compréhension de base de ces types de données, vous devriez être un peu plus prêt à affronter cet examen de statistiques.
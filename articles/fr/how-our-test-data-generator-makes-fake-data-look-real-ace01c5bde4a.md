---
title: Comment notre générateur de données de test rend les fausses données réalistes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-27T20:45:56.000Z'
originalURL: https://freecodecamp.org/news/how-our-test-data-generator-makes-fake-data-look-real-ace01c5bde4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*b_U1vc4pLeXRqExfxlwH8g.jpeg
tags:
- name: data
  slug: data
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Software Testing
  slug: software-testing
- name: technology
  slug: technology
seo_title: Comment notre générateur de données de test rend les fausses données réalistes
seo_desc: 'By Tom Winter

  We recently released DataFairy, a free tool that generates test data. But first,
  let me tell you the story of how it came about.

  This is the story of how we turned a fun open source side project into something
  that has turned out to be ...'
---

Par Tom Winter

Nous avons récemment publié [DataFairy](https://devskiller.com/datafairy/?utm_source=Medium&utm_medium=referral&utm_campaign=FreeCodeCamp&utm_term=Thomas&utm_content=How%20our%20test%20data%20generator%20makes%20fake%20data%20look%20real), un outil gratuit qui génère des données de test. Mais d'abord, laissez-moi vous raconter l'histoire de sa création.

C'est l'histoire de comment nous avons transformé un projet open source amusant en quelque chose qui s'est avéré vraiment utile.

Ce n'est pas une question de fausses nouvelles ou de tromper les masses. Mais le fait reste que pour les développeurs, les testeurs de logiciels, et vraiment quiconque ayant déjà donné une démonstration, les fausses données sont essentielles et sont surprenamment difficiles à inventer sur le moment.

Notre histoire avec les fausses données commence lorsque nous avons développé notre outil SaaS, [Devskiller](https://devskiller.com/?utm_source=Medium&utm_medium=referral&utm_campaign=FreeCodeCamp&utm_term=Thomas&utm_content=How%20our%20test%20data%20generator%20makes%20fake%20data%20look%20real). Comme toutes les applications, nous avions besoin d'utilisateurs. Nous ne cherchions même pas des utilisateurs payants à ce stade. Nous avions simplement besoin de profils de candidats pour notre application. Ce dont nous avions besoin, c'étaient des données factices qui paraissent réelles.

### Nous avions besoin d'un générateur de données de test

Nous avions besoin de fausses données pour plusieurs raisons :

**1. Nous devions vérifier si notre système fonctionnait**

Cela signifiait que nous devions créer plusieurs profils factices différents pour voir si le système les stockait et les affichait correctement.

**2. Nous devions vendre notre produit**

Nous devions faire des démonstrations pour nos premiers clients potentiels. Nous voulions montrer à nos clients à quoi ressemblerait le système après 6 mois d'invitation et de test de centaines de candidats.

Notre première idée a été de chercher un générateur de données de test disponible. Mais le problème est que les données sont difficiles à falsifier de manière convaincante. Demandez simplement à ce gars,

ou à lui,

### Beaucoup de données sont validées algorithmiquement

Si c'était facile de créer des données convaincantes, nous n'aurions probablement pas besoin d'un outil. Mais générer des données peut être délicat pour plusieurs raisons.

Les fausses données ne sont pas simplement des nombres aléatoires. Prenons l'exemple d'un numéro de carte de crédit. La plupart des numéros de carte de crédit sont basés sur ce qu'on appelle un [algorithme de Luhn](https://www.fivecentnickel.com/how-do-you-know-if-a-credit-card-number-is-valid/). Pour expliquer cela, nous allons utiliser l'exemple d'une carte Visa :

![Image](https://cdn-media-1.freecodecamp.org/images/0*K5n41Cr9qmjfLHN6)
_Photo par Dom J de [Pexels](https://www.pexels.com/photo/business-bank-chip-credit-card-45111/" rel="noopener" target="_blank" title=")_

### Comment vérifier si un numéro de carte de crédit est valide

Avant de commencer, il est important de savoir que tous les numéros de carte Visa commencent par un 4. De plus, ils ont tous soit 16, soit 13 chiffres.

Prenons ce numéro de carte Visa :

![Image](https://cdn-media-1.freecodecamp.org/images/0*KcSus6ZmvPhsKWnS)
_Source : [React Credit Cards](https://github.com/amarofashion/react-credit-cards" rel="noopener" target="_blank" title=")_

La première chose à faire pour valider le numéro est de doubler les chiffres alternés en commençant par le premier chiffre de la séquence.

```
4574487405351567
```

```
(4x2), (7x2), (4x2), (7x2), (0x2), (3x2), (1x2), (6x2)
```

```
8, 14, 8, 14, 0, 6, 2, 12
```

Si le doublement que vous venez de faire résulte en un nombre à deux chiffres, additionnez-les pour obtenir un nombre à un seul chiffre.

```
8, 5, 8, 5, 0, 6, 2, 3
```

Vous devez ensuite revenir au numéro de carte de crédit original et remplacer les chiffres que vous avez doublés par la nouvelle valeur.

```
8554885405652537
```

Cela pourrait être soit la valeur doublée, soit le tableau de valeurs avec les chiffres additionnés. Maintenant, additionnez le tout.

```
8+5+5+4+8+8+5+4+0+5+6+5+2+5+3+7=80
```

Puis vérifiez si la somme est divisible par 10. Dans ce cas, c'est le cas, donc le numéro est valide.

Vous avez besoin d'un algorithme computationnel pour valider les numéros de carte de crédit à grande échelle. Mais les numéros de carte de crédit sont relativement faciles à générer correctement. Nous n'avions pas seulement besoin de morceaux individuels de données vérifiables, nous avions besoin de profils complets.

### Les profils vérifiables nécessitent différents types de données qui se relient logiquement

Les numéros de carte de crédit sont relativement faciles à générer, car ils ne se rapportent qu'à eux-mêmes. Mais les numéros d'identité personnelle se rapportent souvent à d'autres informations sur une personne. Prenons le numéro d'identité personnel suédois, appelé personnummer.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Kkq3ODgzKa7BlQp0)
_Photo par [Unsplash](https://unsplash.com/photos/FMtCI4zIVGk?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jonathan Brinkhorst</a> sur <a href="https://unsplash.com/search/photos/sweden?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="): La Suède est un pays pratique_

Pour ceux qui ne savent pas, les personnummers sont conçus pour payer les impôts, un peu comme un numéro de sécurité sociale américain. Mais ils sont également utilisés pour accéder à des services comme les soins de santé et les écoles, ainsi qu'à des services non gouvernementaux comme les cotes de crédit.

Le format d'un personnummer est légèrement différent de celui d'une carte de crédit. C'est un numéro à 10 chiffres divisé en une section de six chiffres et une section de quatre chiffres reliés par un tiret.

_Fait intéressant : Les Suédois de plus de 100 ans remplacent le tiret dans leur personnummer par un [signe plus](https://www.oecd.org/tax/automatic-exchange/crs-implementation-and-assistance/tax-identification-numbers/Sweden-TIN.pdf)._

Les six premiers chiffres du personnummer sont simples et correspondent à l'anniversaire de la personne en utilisant un format YYMMDD. Parmi les quatre chiffres suivants, les trois premiers sont un numéro de série. Le troisième chiffre du numéro de série est impair pour les hommes et pair pour les femmes. Le dernier chiffre est un chiffre de contrôle.

Ainsi, si vous prenez le personnummer :

```
6011289235
```

Vous savez qu'il s'agit d'un homme né le 28 novembre 1960.

```
60(année)11(mois)28(jour)-(moins de 100 ans)92(nombres uniques)3(numéro unique impair pour homme)5(chiffre de contrôle)
```

Pour calculer le chiffre de contrôle, multipliez les chiffres individuels du numéro d'identité par les chiffres correspondants du nombre 212121212.

```
(6x2)(0x1)(1x2)(1x1)(2x2)(8x1)(9x2)(2x1)(3x2)
```

```
12, 0, 2, 1, 4, 8, 18, 2, 6
```

Tout comme avec la carte Visa ci-dessus, si le produit de l'un de ces nombres résulte en un nombre à deux chiffres, additionnez simplement les deux chiffres ensemble.

```
3, 0, 2, 1, 4, 8, 9, 2, 6
```

Additionnez tous les produits restants ensemble.

```
3+0+2+1+4+8+9+2+6=35
```

Pour obtenir le chiffre de contrôle, soustrayez le dernier chiffre des produits additionnés de 10 (l'exception est que si le dernier chiffre est zéro, le chiffre de contrôle est également zéro).

```
105=5
```

Ainsi, si vous deviez générer un profil de cette personne, il ne pourrait pas s'agir d'une femme née le 10 avril 1916. Son personnummer devrait être quelque chose comme : 160410+1244. En d'autres termes, vous ne pourriez pas simplement inventer un numéro aléatoire et vous attendre à ce qu'il fonctionne avec n'importe quel profil factice que vous avez généré.

### Nous avions besoin de données de test logiques

Les données devaient se relier les unes aux autres de manière logique, puisque le personnummer n'est pas le seul morceau de données construit sur des informations externes. La plupart des types de numéros d'identification se rapportent à d'autres informations d'une manière ou d'une autre. Nous n'avons tout simplement pas pu trouver un générateur de données de test qui ferait cela, alors nous avons décidé de construire le nôtre. Il semble que nous n'étions pas les seuls à avoir ce problème.

### JFairy

En tant que contributeurs réguliers de la communauté open source, nous avons décidé que la meilleure façon de générer les données de test dont nous avions besoin était de construire notre propre bibliothèque. Appelée [JFairy](https://github.com/Devskiller/jfairy), notre objectif était qu'elle génère des ensembles de données qui soient tous vérifiables et logiquement connectés.

De cette façon, nous pourrions peupler notre application avec des utilisateurs. Nos données utilisateur ne pouvaient pas être du charabia, sinon elles ne pourraient pas être imputées. Nous avons donc mis la bibliothèque au travail et elle a performé mieux que nous aurions pu l'espérer. Elle génère même des personnes réelles de temps en temps. Nous l'avons découvert parce que nous avons utilisé [Gravatar](https://en.gravatar.com/) pour afficher les photos des candidats. Nous avons été surpris lorsqu'une vraie photo est apparue sur notre compte de test.

![Image](https://cdn-media-1.freecodecamp.org/images/0*6llBF0wPjlBrVGm8)
_Source : [Tenor](https://media1.tenor.com/images/28855054c8ba5225bddc536a5862025b/tenor.gif?itemid=11386682" rel="noopener" target="_blank" title=")_

Cela s'est avéré vraiment utile lorsque nous avons commencé à présenter notre application. Nous voulions montrer à des clients entreprises un compte avec 300 différents candidats de test sur la plateforme. Si nous n'avions pas construit JFairy, nous aurions peut-être tous essayé d'utiliser l'application quelques fois, mais nous n'étions que cinq dans l'équipe. Il aurait été impratique pour nous cinq de créer 300 profils factices logiquement connectés.

Les données générées par JFairy se sont avérées si convaincantes que les nouveaux clients étaient perplexes quant à l'origine de toutes ces personnes à tester. En fait, ils nous ont demandé si nous pouvions les aider à trouver de nouveaux développeurs, car clairement nous étions en contact avec un certain nombre de personnes ayant des antécédents techniques, dont certaines avaient des compétences validées.

### Nous devions laisser la communauté open source jeter un coup d'œil à JFairy

Nous avons réalisé que cela devenait quelque chose de plus grand que nous, alors nous avons décidé de mettre le système en open source. La première raison est que nous sommes tous des utilisateurs passionnés de code open source. Nous savons qu'il est important de redonner à cette communauté afin de recevoir en retour. Mais en plus de cela, l'open source peut apporter de réels avantages au produit. En mettant notre projet à disposition de nombreux développeurs différents, nous pouvons obtenir de nouvelles idées que nous n'aurions jamais envisagées.

Les contributions les plus notables ont été l'inclusion de nouvelles langues. Nous avons seulement construit JFairy pour générer des données pour les anglophones et les polonophones. Après tout, nous sommes plutôt limités par les langues que nous connaissons bien. Mais bien sûr, cela pourrait être un outil utile pour des personnes de nombreux pays différents. Grâce aux contributions open source, nous avons pu ajouter le support pour les données en espagnol, français, allemand, suédois et chinois.

Nous avons également réalisé que, bien que nous atteignions un excellent groupe d'utilisateurs parmi les développeurs de logiciels, Jfairy avait des applications bien au-delà d'une communauté dont les membres savent coder. Nous avons donc décidé de capitaliser sur le succès de la bibliothèque et de créer une application qui pourrait soutenir son utilisation pour plus d'applications et plus de personnes.

### Data Fairy donne à tous accès aux fausses données

JFairy s'est avéré super utile pour les développeurs qui savaient coder, mais ils n'étaient pas les seules personnes à utiliser les données générées par JFairy. Les testeurs de logiciels doivent pouvoir peupler leurs systèmes pour voir s'ils fonctionnent. Les commerciaux et les marketeurs ont besoin de données pour rendre leurs démonstrations réalistes. Pour rendre JFairy utile au plus grand nombre, nous devions rendre ses fausses données faciles d'accès.

![Image](https://cdn-media-1.freecodecamp.org/images/0*rPmzovhZ6hMsNbfS)

Avec cet objectif en tête, nous avons construit [DataFairy](https://devskiller.com/datafairy/?utm_source=Medium&utm_medium=referral&utm_campaign=FreeCodeCamp&utm_term=Thomas&utm_content=How%20our%20test%20data%20generator%20makes%20fake%20data%20look%20real). DataFairy est une application alimentée par JFairy afin que vous puissiez accéder à nos fausses données sans avoir à apprendre à coder au préalable. Les données sont présentées dans une interface de notebook soignée. Pour obtenir plus d'un faux profil, vous pouvez soit générer un nouveau profil, soit exporter une liste groupée de jusqu'à 100 profils vers un fichier CSV. C'est un moyen gratuit et facile de peupler votre logiciel avec des données valides et logiquement connectées.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vPgSlW63nRjOUYYF)

### Nos plans pour l'avenir de DataFairy

DataFairy peut toujours être amélioré et de nouvelles fonctionnalités peuvent y être ajoutées. En plus de nos propres efforts, nous voulons rester fidèles aux principes de la communauté open source. Nous continuons à solliciter de nouvelles langues que nous pouvons ajouter à notre liste et nous avons un projet ouvert sur [GitHub](https://github.com/Devskiller/jfairy). Nous aimerions également que les utilisateurs ajoutent éventuellement des données d'exemple. Cela nous aidera à construire une communauté de participants qui aideront DataFairy à grandir et à devenir plus utile pour plus de personnes.

Que vous ayez besoin de télécharger de grands lots de données logiquement validées ou que vous souhaitiez simplement vous amuser en lisant les profils qui apparaissent, consultez [DataFairy](https://devskiller.com/datafairy/?utm_source=Medium&utm_medium=referral&utm_campaign=FreeCodeCamp&utm_term=Thomas&utm_content=How%20our%20test%20data%20generator%20makes%20fake%20data%20look%20real).
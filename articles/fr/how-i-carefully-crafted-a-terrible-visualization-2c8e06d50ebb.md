---
title: Comment j'ai soigneusement conçu une véritable terrible visualisation de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-13T08:48:03.000Z'
originalURL: https://freecodecamp.org/news/how-i-carefully-crafted-a-terrible-visualization-2c8e06d50ebb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q-tJ3MgDqZqH5eU7CsJzWQ.png
tags:
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Design
  slug: design
- name: 'tech '
  slug: tech
seo_title: Comment j'ai soigneusement conçu une véritable terrible visualisation de
  données
seo_desc: 'By Krist Wongsuphasawat

  Yes, you read that right. I am going to explain how I put together a really bad
  visualization, intentionally.

  Andy Kirk of visualisingdata.com posted an interesting contest challenging everyone
  to come up with the “best worst ...'
---

Par Krist Wongsuphasawat

Oui, vous avez bien lu. Je vais expliquer comment j'ai assemblé une très mauvaise visualisation, intentionnellement.

Andy Kirk de [visualisingdata.com](http://www.visualisingdata.com/) a publié un concours intéressant défiant tout le monde de venir avec le **"meilleur pire viz."** Bien sûr, l'une des motivations pour moi de faire cela est de gagner une copie de son livre. Mais le concours lui-même est aussi un exercice réfléchissant.

En parlant de visualisations extrêmement mauvaises, les stéréotypes impliquent souvent des _camemberts 3D_, des _palettes de couleurs arc-en-ciel_ et de terribles choix de polices, de mises en page et de couleurs.

À mon avis, les mauvaises visualisations n'ont pas à être juste cela. L'objectif que j'avais en tête était de créer une pièce qui semble totalement inoffensive, mais qui torturera votre cerveau jusqu'à ce que vous réalisiez à quel point l'ensemble est absurde et ridicule.

J'ai collecté des données à partir de visualisations présentées sur [viz.wtf](http://viz.wtf/) et j'ai dessiné chaque marque pour représenter l'une des visualisations et ses propriétés. Exemples de questions pour exercer votre glande WTF sont :

* Quelle est la couleur la plus courante pour ces visualisations ?
* Où sont les camemberts ?
* Pouvez-vous indiquer la pièce la moins populaire ?
* À quelle fréquence le 3D est-il utilisé ?
* Y a-t-il un motif quelconque ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q-tJ3MgDqZqH5eU7CsJzWQ.png)

Avant de lire la section suivante, essayez de comprendre par vous-même tout ce qui ne va pas avec ce graphique.

### Concept

L'idée principale était de créer des conflits de perception et de perturber la pensée cognitive des spectateurs.

Les mauvaises visualisations ont généralement des incompatibilités entre les encodages visuels et les données, comme l'encodage de zones non comparables (camembert 3D) pour des valeurs numériques. Ces incompatibilités laissent les spectateurs avec peu de choses à faire, à part se gratter la tête, puis abandonner la visualisation parce qu'il faut trop d'efforts pour la comprendre.

Je voulais porter le mauvais au niveau supérieur, et j'ai été inspiré par l'une de mes réponses préférées des questions de Stack Overflow, "[What is the best comment in source code you have ever encountered?](http://stackoverflow.com/questions/184618/what-is-the-best-comment-in-source-code-you-have-ever-encountered)"

> #define TRUE FALSE  
> //Happy debugging suckers

Mon objectif était de faire quelque chose qui semble pouvoir être interprété, mais qui crée de très forts conflits avec nos connaissances antérieures qui sont presque impossibles à surmonter. Pour ce faire, j'ai choisi des choix très directs d'encodage, comme utiliser la couleur pour représenter la couleur, et la position pour représenter la position, puis j'ai défini les mappages de manière contre-intuitive afin de semer le chaos complet dans l'esprit des spectateurs.

### Données

Je cherchais un bon ensemble de données pour essayer l'idée, mais je n'en ai pas trouvé un qui me plaisait vraiment. Puis j'ai eu l'idée qu'il serait récursivement mauvais de créer une mauvaise visualisation, de mauvaises visualisations, alors j'ai collecté manuellement des données à partir de [viz.wtf](http://viz.wtf/)

### Voici tous les crimes que j'ai commis pour ce graphique :

1. J'ai utilisé la couleur pour représenter la couleur, mais je n'ai pas garanti qu'elles seraient de la même couleur. En conséquence, le _vert_ est le nouveau _noir_.
2. Je n'ai pas non plus ajouté assez de couleurs uniques, donc il y a des doublons. Par exemple, à la fois le _rouge_ et le _bleu_ sont représentés par le _vert_. (Ce n'était pas intentionnel au début, mais ensuite cela a empiré les choses alors je l'ai gardé.)
3. Il y avait un cas spécial pour la couleur "mixte", car je ne pouvais pas décider quelle couleur utiliser pour l'encoder. En conséquence, chacune de ces visualisations "mixte" a reçu une couleur sélectionnée aléatoirement.
4. J'ai utilisé la position pour représenter la position, mais j'ai veillé à ce qu'elles ne correspondent jamais. Avec cela, la droite est à gauche.
5. J'ai utilisé des formes pour représenter les types de graphiques, mais j'ai veillé à ce qu'elles ne correspondent jamais. Avec cela, un graphique à barres est un cercle, tandis qu'un camembert ressemble à une barre.
6. J'ai utilisé la taille pour encoder la popularité, mais j'ai utilisé une échelle inverse où la plus grande taille signifie zéro.
7. J'ai rendu les étiquettes des axes plus compliquées qu'elles n'en avaient besoin. Pas de 3D ? Vrai ou faux ?
8. Je fais tourner chaque grand nombre selon sa valeur en degrés. Celui-ci est un encodage sans but.
9. Les cercles autour des grands nombres ne signifient rien. Ils n'indiquent pas de limites.
10. Si vous additionnez tous les nombres, il y a en fait 102 visualisations, et non 100.
11. J'ai ajouté un dinosaure. Parce que je pouvais.
12. Enfin, il y avait un lien vers les données brutes, fièrement partagées au format PDF.

Si vous repérez d'autres aspects terribles de cette visualisation que j'ai négligés, n'hésitez pas à laisser une réponse ci-dessous, ou à tweeter à mon intention.
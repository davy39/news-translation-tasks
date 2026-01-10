---
title: Un voyage statistique à travers l'émotion de Stranger Things
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-06T23:30:23.000Z'
originalURL: https://freecodecamp.org/news/a-statistical-curiosity-voyage-through-the-emotion-of-stranger-things-e7bc8b2a6395
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Qx2KFtAHgHE1qdODWC_1iQ.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: netflix
  slug: netflix
- name: statistics
  slug: statistics
- name: stranger things
  slug: stranger-things
seo_title: Un voyage statistique à travers l'émotion de Stranger Things
seo_desc: 'By Jordan Dworkin

  Like a few million other people, I spent the weekend of Oct. 27, 2017, watching
  Stranger Things 2, and the following week dealing with minor withdrawal.

  To cope, and to transition back into my research, I decided to apply the statis...'
---

Par Jordan Dworkin

Comme [quelques millions](https://www.theringer.com/2017/11/2/16600190/stranger-things-season-2-ratings) d'autres personnes, j'ai passé le week-end du 27 octobre 2017 à regarder Stranger Things 2, et la semaine suivante à gérer un léger [syndrome de sevrage](https://twitter.com/search?f=tweets&vertical=default&q=stranger%20things%20withdrawal&src=typd).

Pour faire face à cela et pour revenir à mes recherches, j'ai décidé d'appliquer les [paddles](https://i.pinimg.com/originals/3f/38/e3/3f38e374b22804b066db9b05e2ca15b8.jpg) statistiques de l'analyse des sentiments et de l'analyse de réseau aux scripts des Saisons 1 et 2, et de considérer ce que les résultats pourraient dire sur la structure émotionnelle de chaque épisode de la série.

Pour commencer à comprendre l'émotion de Stranger Things, j'ai téléchargé les [scripts](https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=stranger-things-2016) et attribué une valeur numérique à chaque mot en fonction de sa [valence positive ou négative](http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010). L'aspect le plus simple de l'émotion à examiner est la valence moyenne de chaque épisode. Cette métrique est obtenue en prenant la moyenne des valeurs de sentiment de tous les mots d'un épisode, indépendamment de l'ordre dans lequel ils sont prononcés.

![Image](https://cdn-media-1.freecodecamp.org/images/kwJtS8k8uvPcirGMqc5a8RfOsjcsaeFskcUI)

Ces valeurs sont généralement ce à quoi on pourrait s'attendre d'une série sur des enfants disparus et des monstres interdimensionnels, la plupart des épisodes montrant plus d'émotion négative que positive.

La découverte la plus intéressante semble être le degré auquel l'épisode de Chicago [moins bien reçu](https://www.vanityfair.com/hollywood/2017/10/stranger-things-recap-season-2-episode-7-eleven-mother-chicago-kali-millie-bobby-brown) — numéro 15 — se distingue comme étant plus de deux fois plus négatif que tout autre. Cela peut être dû à une combinaison de son intrigue sombre et de l'absence de tout soulagement comique de la part du groupe de Hawkins.

Cependant, il manque beaucoup d'informations temporelles à ces moyennes, alors examinons comment le ton émotionnel change au fil du temps dans les épisodes.

Une façon de faire cela est d'utiliser la technique de la fenêtre glissante. Pour cette version d'une fenêtre glissante, nous allons prendre la moyenne des 40 mots entourant un mot central, puis continuer à décaler d'un mot et prendre une nouvelle moyenne. Cela donne une trajectoire lisse de la valence émotionnelle au cours de chaque épisode.

![Image](https://cdn-media-1.freecodecamp.org/images/oC6734sYhtT4O-vo14xa0KiPcnf0SpLwhEmO)

Bien qu'il soit difficile d'apprendre beaucoup en regardant simplement les trajectoires, quelques choses se distinguent.

Premièrement, avec une seule exception (vous l'avez deviné, l'épisode de Chicago), même les épisodes les plus sombres ont généralement quelques scènes qui sont riches en sentiment positif.

Deuxièmement, sur les 17 épisodes, seulement trois se terminent sur une note positive : la finale de la Saison 1, la première de la Saison 2 et la finale de la Saison 2.

Troisièmement, il y a beaucoup de variation dans la façon dont ces épisodes sont structurés, et ils ne semblent pas suivre un schéma émotionnel clair. Approfondissons ce dernier point et voyons si nous pouvons caractériser une partie de cette variation.

Comme base de comparaison, nous pouvons vérifier si la saison dans laquelle un épisode apparaît contient suffisamment d'informations pour expliquer les similitudes et les différences entre les trajectoires émotionnelles.

![Image](https://cdn-media-1.freecodecamp.org/images/DfqKzPW9y0QQlnw1p34MHoe98W0Zh7m7VJtd)

Sans surprise, ce n'est pas le cas `(_p_ = .34)`. En général, les Saisons 1 et 2 présentent une grande variabilité dans les structures de leurs épisodes. Les trajectoires moyennes ont tendance à osciller autour du neutre.

Pour trouver une meilleure classification, conceptualisons d'abord les relations entre les épisodes comme un réseau en calculant la corrélation temporelle pour chaque paire d'épisodes. Dans ce contexte, les nœuds sont des épisodes et les arêtes représentent le degré auquel les paires montrent des schémas émotionnels similaires.

Une fois ce réseau construit, nous pouvons appliquer des [méthodes](https://perso.uclouvain.be/vincent.blondel/research/louvain.html) empruntées à la [théorie des graphes](https://en.wikipedia.org/wiki/Graph_theory) pour trouver des communautés dans nos données. Dans ce cas, trois groupes distincts d'épisodes sont révélés, et la similitude intra-groupe est plus grande que ce à quoi on pourrait s'attendre par hasard `(_p_ < .0`01).

Maintenant que nous avons trouvé nos communautés d'intérêt, cartographions-les sur les trajectoires émotionnelles pour voir si elles capturent davantage de variabilité.

![Image](https://cdn-media-1.freecodecamp.org/images/lWSAXg5ZoxJyfhB5GMdkxkkBGXjK8jbm8vzb)

Contrairement à la division par saison, ces trajectoires moyennes de groupe semblent décrire trois schémas distincts. Elles semblent également bien correspondre à leurs trajectoires d'épisodes sous-jacentes.

En regardant les schémas moyens, nous pouvons voir que le groupe 1 contient des épisodes qui commencent et se terminent avec une émotion neutre et ont des fluctuations lentes au milieu, le groupe 2 contient des épisodes qui commencent avec une émotion négative et montent progressivement vers une fin positive, et le groupe 3 contient des épisodes qui commencent sur une note positive et oscillent vers le bas vers une fin plus sombre.

En plus de tracer les communautés de schémas émotionnels, examinons la structure complète du réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/NdIqaLtutbYB3GOBa6-N6ue77aXNbI4WGS2Y)

La première chose qui saute aux yeux est que chaque groupe contient un nombre approximativement égal d'épisodes de la Saison 1 et de la Saison 2. Cela soutient la découverte précédente selon laquelle la saison n'est pas un bon prédicteur de la similitude des épisodes. Nous pouvons également voir que l'épisode 15 se distingue à nouveau des autres. Cette fois parce qu'il est plus faiblement connecté au reste du graphe que n'importe quel autre épisode.

Peut-être plus intéressant encore, le réseau révèle que les épisodes tendent à être moins similaires à ceux qui les précèdent et les suivent que ce à quoi on pourrait s'attendre par hasard `(_p_ = .03)`. De plus, les transitions des épisodes 1→2, 2→3 et 3→4 ont trois des cinq plus grands changements de structure émotionnelle des 16 transitions qui se sont produites dans la série.

Ensemble, ces résultats suggèrent que varier la trajectoire émotionnelle d'un épisode à l'autre peut être une stratégie pour [accrocher les téléspectateurs](https://www.vanityfair.com/hollywood/2016/09/netflix-episode-that-got-you-hooked).

Les futurs épisodes continueront-ils à montrer ces changements de structure émotionnelle ? Suivront-ils les trois mêmes trajectoires émotionnelles dominantes ? Les futures tentatives de création d'épisodes audacieusement différents seront-elles mieux reçues que Chicago ? Considérez cela comme plus de [questions sans réponse](https://www.theringer.com/tv/2017/11/6/16604702/stranger-things-season-3-questions) pour la Saison 3.

**_Observations diverses [certains spoilers à venir]_**

* Point émotionnel le plus élevé de la série : Noël chez les Byers dans la finale de la Saison 1.

```
Qu'est-ce que tu - Qu'est-ce que tu fais ? [Jonathan] Je documente.Oh, pourquoi ? - Parce que - [Joyce rit] - Ça a l'air génial. - [Joyce] Oh, c'est juste trop cuit. - Et regarde, les pommes de terre sont liquides.- [Jonathan] Maman. - [Joyce] Elles sont si liquides.- [Jonathan rit] Maman, ça va être génial.
```

* Point émotionnel le plus bas de la série #1 : Scène de poursuite pour ouvrir la Saison 2.

```
[Klaxons] Merde ! Merde ! Merde ! Merde ! Merde ! [Rires] [Soupirs] D'accord. D'accord.[Sirènes de police] - Fils de pute ! On en a plus ! - [Mick] Oh, merde ! Ils descendent la 7ème.
```

* Point émotionnel le plus bas de la série #2 : Steve contre Billy dans la finale de la Saison 2.

```
[Steve] Sors de là.[Dustin] Oui ! Botte-lui le cul, Steve ! - [Mike] Attrape-le ! - [Dustin] Tue ce fils de pute ! - [Dustin] Maintenant ! Maintenant ! - [Mike] Attrape ce connard ! - [Dustin] Tue ce fils de pute ! - [Lucas] Steve ! - [Max] Billy ! - [Mike] Putain ! Merde !
```

* Mention honorable pour la meilleure scène qui n'a pas pu être comptée en raison du manque de dialogue : Billy dans le miroir.

```
[Billy se pavane]
```

Pour ceux qui sont intéressés, le code de ce projet est disponible publiquement [ici](https://www.dropbox.com/s/6hvtd9m8d9dvl86/EmotionOfStrangerThings.R?dl=0).
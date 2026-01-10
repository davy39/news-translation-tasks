---
title: J'ai analysé les données de chaque épisode de Ultimate Beastmaster de Netflix
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-29T04:59:58.000Z'
originalURL: https://freecodecamp.org/news/i-crunched-the-data-from-every-episode-of-netflixs-ultimate-beastmaster-71e91e471574
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pa3ZXPlXVGBZok_qoexcIQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Life lessons
  slug: life-lessons
- name: sports
  slug: sports
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: J'ai analysé les données de chaque épisode de Ultimate Beastmaster de Netflix
seo_desc: 'By Kande Bonfim

  There’s a new show on Netflix called Ultimate Beastmaster. It’s basically a clone
  of American Ninja Warrior: strong people running through crazy hard obstacle courses.

  I decided to dive in and give the show the full data science treat...'
---

Par Kande Bonfim

Il y a une nouvelle émission sur Netflix appelée Ultimate Beastmaster. C'est essentiellement un clone de American Ninja Warrior : des personnes fortes parcourant des parcours d'obstacles extrêmement difficiles.

J'ai décidé de plonger dans les données et d'appliquer un traitement complet de science des données à l'émission. Attention, si vous n'avez pas encore regardé l'émission, **il y a des spoilers ici**.

C'est parti.

### Les participants

Il y a **10 épisodes**. **9** d'entre eux présentent **12 nouveaux participants chacun**. **108 personnes** sautant comme des fous en essayant de devenir le prochain **Ultimate Beastmaster** pendant que vous mangez un sachet familial de Cheetos.

Le graphique suivant donne une vue d'ensemble de ce qui s'est passé dans l'émission. **J'exclus la finale ici, car nous en parlerons séparément plus tard dans cet article.**

![Image](https://cdn-media-1.freecodecamp.org/images/RbyZfyraQX0dRfMsjClCjW0PjFYP96nZ8Nw8)
_Le Ultimate Scatterplot_

Maintenant, plongeons dans les données.

#### Genre

Malheureusement, il y a encore une énorme différence entre le nombre d'hommes et de femmes dans _Ultimate Beastmaster_. Seulement **22 femmes** ont affronté la bête. **Cela représente 20,4 % des concurrents.**

C'est encore pire : toutes les femmes ont été éliminées au premier (81 %) et au deuxième niveau (13 %). La seule exception était la jeune étudiante ?? Si**lke Sollfrank (1**8 ans) qui a été éliminée au niveau 3. C'est tout. **Aucune femme en finale.** ?

![Image](https://cdn-media-1.freecodecamp.org/images/XYwzjvaesGvfUcrRQLwMubJc9rfjNYaYB-SI)
_?? Mi**mi Bonny était l'une des 5 femmes éliminées sur Throat Erosion où les concurrents doivent utiliser un trampoline industriel pour sauter et attraper un levier libérant un mur d'escalade. Cet obstacle a éliminé uniquement des femmes._

**Cela m'a fait réfléchir à la manière dont l'émission devrait gérer certains avantages que le corps masculin moyen a sur celui des femmes dans cette compétition. Certains obstacles étaient bien trop difficiles à surmonter si vous êtes plus petit que la moyenne.**

![Image](https://cdn-media-1.freecodecamp.org/images/egTuXWCMEdvy6UgtbgIMILIXiUcIsg6g3cI-)
_Ce n'est pas une onde musicale. C'est un histogramme._

#### Âge

**L'âge des participants varie de 18 à 40 ans** (moyenne de 29,1 ans). **Les cinq plus jeunes sont allemands (aucune idée pourquoi).**

**Les Beastmasters — les gagnants de chaque épisode — ont entre 20 et 35 ans** (28,1 ans en moyenne). Être trop jeune ou trop vieux n'aide pas.**

![Image](https://cdn-media-1.freecodecamp.org/images/AZTwswy4QZOAk37Qg12FtWmtAvmpF6IVlhgS)
_Oui, aucun Japonais en finale… ???_

#### La finale

**?? Les États-Unis ont apporté 3 beastmasters. ?? L'Allemagne et ?? La Corée du Sud, 2. Mais il n'a fallu qu'un seul ?? Brésilien pour remporter le prix Ultimate Beastmaster.**

**Oui, je suis Brésilien aussi, et maintenant je me sens mieux après le 7x1 que l'Allemagne nous a infligé lors de la Coupe du Monde.**

### Points

![Image](https://cdn-media-1.freecodecamp.org/images/oqBK9E9HUbcOrYpYuZrufAt0sfEwUb5YVFAK)

![Image](https://cdn-media-1.freecodecamp.org/images/mMkIVHhV73tqcyRie7B78PWYb0QuGinAThdP)
_Points acquis par chaque concurrent tout au long de l'émission._

**Notez qu'il y a une tendance douce à la baisse de votre score une fois que vous êtes plus âgé.**

> **Corrélation entre l'âge et les points : -0,24**

### Entonnoir de compétition

![Image](https://cdn-media-1.freecodecamp.org/images/fvvS6isat1bauHbT1WATABJFmisqF-rfduQh)
_**? Éliminé — ? Classifié**_

### Les niveaux

**Examinons de plus près chaque niveau de la compétition et leurs principales causes d'échec.**

### Niveau 1

![Image](https://cdn-media-1.freecodecamp.org/images/Mwopr9Bq3nZJbcm2O0UQLvCqmve4d5p3fO2i)
_Principales causes d'échec classées par position au niveau 1._

**Seulement 5 (4,6 %) participants ont réussi à accomplir le premier niveau. Les parties les plus difficiles du parcours sont :**

1. **Energy Coils** 30,6 %
2. **Mag Wall** 27,8 %
3. **Faceplant** 22,2 %

**Brandon Douglass ?? est le SEUL à avoir échoué à Brain Matter.** Il est la petite ligne rouge dans le graphique.

**Le temps moyen passé sur ce parcours est de 2'54 et pour le réussir, il est de 5'29. ?? Fe**lipe Camargo est le plus rapide à le terminer : 5'**10 ?. Et le plus rapide à échouer est aussi un concurrent brésilien : ?? Karine Abrahim a échoué en 0'18.**

**39,3 est la moyenne des points par personne sur ce parcours et elle varie de 10 à 70 points. Personne n'a obtenu tous les 80 points disponibles dans ce niveau.**

### Niveau 2

![Image](https://cdn-media-1.freecodecamp.org/images/GhCt1PUXocBYGvlGjdpZVMQM3j8eKeI5W3Dc)
_Principales causes d'échec classées par position au niveau 2._

**?? Taeho Kwon était le seul à avoir complété le deuxième niveau (il l'a fait en 4'**28).**

**Principales causes d'échec :**

1. **Dreadmills** 27,8 %
2. **Spinal Ascent** 22,2 %
3. **Stomach Churn** 19,4 %

**Points :** de **20 à 220** (**109,1 en moyenne**).

**Temps :** de **1'01 à 9'53** (**4'08 en moyenne**).

### Niveau 3

![Image](https://cdn-media-1.freecodecamp.org/images/iwaqGm6KvKNgd3QmxnssjPVcYg6uStgvQv1z)
_Principales causes d'échec classées par position au niveau 3._

**?? He**eyong Park était le seul à avoir accompli ce niveau (il l'a fait en 6'**19).**

**Principales causes d'échec :**

1. **Ejector ⚠️** 40 %
2. **Bungee Beds** 20 %
3. **The Extractor** 13,3 %

**Points :** de **90 à 340** (**186,6 en moyenne**).

**Temps :** de **0'03 à 12'48** (**2'17 en moyenne**).

### Quel pays a gagné ?

**Et si Ultimate Beastmaster était une compétition entre les pays plutôt qu'entre les individus ? Quel pays a obtenu le meilleur résultat ?**

**En prenant le score moyen par pays, nous pouvons obtenir le résultat : ?? La Corée du Sud a remporté l'Ultimate Beastmaster !**

**`+-----------------+-------------+----------+`**  
**`|    Pays         | Points Moy. | Position |`**  
**`+-----------------+-------------+----------+`**  
**`| ??Corée du Sud  |       117,2 | 1er      |`**  
**`| ??Allemagne     |         110 | 2ème     |`**  
**`| ??États-Unis    |       105,5 | 3ème     |`**  
**`| ??Mexique       |       100,5 | 4ème     |`**  
**`| ??Brésil        |        96,1 | 5ème     |`**  
**`| ??Japon         |        69,4 | 6ème     |`**  
**`+-----------------+-------------+----------+`**

### Les finalistes

**`+------------------+-----+--------------------------+---------+`**  
**`|       nom        | âge |           métier         | pays    |`**  
**`+------------------+-----+--------------------------+---------+`**  
**`| Felipe Camargo   |  24 | Grimpeur professionnel   | Brésil  |`**  
**`| David Manthei    |  20 | Étudiant en architecture | Allemagne|`**  
**`| Philip Meyer     |  23 | Soldat                  | Allemagne|`**  
**`| Roberto Perez    |  25 | Étudiant                | Mexique |`**  
**`| Heeyong Park     |  34 | Grimpeur de glace        | Corée   |`**  
**`| Hyunho Kim       |  30 | Entraîneur de Crossfit   | Corée   |`**  
**`| Steven Tucker    |  29 | Instructeur d'escalade   | EUA     |`**  
**`| Jonathan Collins |  33 | Entraîneur et mannequin  | EUA     |`**  
**`| Ken Corigliano   |  35 | Major de l'Air Force     | EUA     |`**  
**`+------------------+-----+--------------------------+---------+`**

**On peut clairement voir pourquoi les finalistes ont obtenu le titre de Beastmaster. Leur moyenne de points est de 265 contre 88,7 pour les autres concurrents.**

### Le jeu de données

**Cet article est basé sur les données que j'ai recueillies, et elles sont disponibles pour une expansion supplémentaire si vous souhaitez aider ou simplement essayer quelques analyses. De plus, le jeu de données est disponible sur [Kaggle](https://www.kaggle.com/kandebonfim/ultimate-beastmaster).**

**Découvert quelque chose de nouveau ?** Mon twitter est [@kandebonfim](https://twitter.com/kandebonfim).
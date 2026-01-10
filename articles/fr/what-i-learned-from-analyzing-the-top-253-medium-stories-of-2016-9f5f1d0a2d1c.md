---
title: Ce que j'ai appris en analysant les 252 meilleures histoires de Medium en 2016
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2017-01-06T22:15:26.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-analyzing-the-top-253-medium-stories-of-2016-9f5f1d0a2d1c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FoYx_zJMp43-h15bW-9dMw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Life lessons
  slug: life-lessons
- name: medium
  slug: medium
- name: social media
  slug: social-media
- name: writing
  slug: writing
seo_title: Ce que j'ai appris en analysant les 252 meilleures histoires de Medium
  en 2016
seo_desc: 'Medium may be struggling to find a sustainable business model, but they
  have years worth of funding left, and more readers than ever.


  According to SimilarWeb, Medium had more than 84 million visits last month.

  Medium isn’t going away any time soon. ...'
---

Medium peut avoir du mal à trouver un modèle économique durable, mais ils ont encore des années de financement devant eux et plus de lecteurs que jamais.

![Image](https://cdn-media-1.freecodecamp.org/images/nDPRlKTnO15cvgvALzG1PhvqXcc5uIp4IkxQ)
_Selon SimilarWeb, Medium a enregistré plus de 84 millions de visites le mois dernier._

Medium ne va pas disparaître de sitôt. Alors, concentrons-nous plutôt sur la manière dont vous pouvez écrire des histoires que les lecteurs trouveront utiles ici en 2017.

J'ai récupéré les 252 meilleures histoires de 2016 — toutes ayant au moins 2 500 recommandations de la part des lecteurs de Medium — et analysé le jeu de données.

Pour mettre les choses en perspective, les écrivains ont publié 7 500 000 histoires sur Medium l'année dernière. Ainsi, ce jeu de données représente les 0,00336 % d'histoires les plus populaires de 2016.

Ensemble, ces 252 histoires ont accumulé 1 033 961 recommandations. C'est beaucoup de cœurs verts.

Voici quelques choses que j'ai apprises en travaillant avec ce jeu de données et qui peuvent vous aider à atteindre un public plus large pour vos écrits en 2017.

### Insight #1 : Vous n'avez pas besoin d'être célèbre pour réussir sur Medium

169 écrivains différents ont publié l'une de ces 252 meilleures histoires. Certains de ces écrivains avaient plusieurs histoires à succès.

Voici les personnes qui ont écrit plus d'une histoire parmi les 252 meilleures :

```
+----------------------+---------+---------------------+|         Nom          | Histoires | Écrit surtout sur  |+----------------------+---------+---------------------+| Benjamin Hardy       |      17 | Amélioration de soi || Quincy Larson        |      16 | Technologie         || Jon Westenberg       |      13 | Vie                 || Darius Foroux        |       7 | Leçons de vie       || Julie Zhuo           |       4 | Design              || Sarah Cooper         |       4 | Satire              || Jonathan Z. White    |       3 | Design              || Bill Sourour         |       3 | Programmation       || Jessica Semaan       |       3 | Leçons de vie       || Jason Fried          |       3 | Business            || Thomas Oppong        |       3 | Vie                 || Larry Kim            |       3 | Productivité        || Gary Vaynerchuk      |       3 | Entrepreneuriat    || Chris Dixon          |       3 | Technologie         || Amanda Rosenberg     |       3 | Humour              || Andy Raskin          |       2 | Marketing           || Charles Scalfani     |       2 | Programmation       || Chris Messina        |       2 | Design              || James Altucher       |       2 | Vie                 || John Fawkes          |       2 | Productivité        || John Saito           |       2 | Design              || Marc Cenedella       |       2 | Business            || Tobias Van Schneider |       2 | Design              |+----------------------+---------+---------------------+
```

La seule personne de cette liste que je connaissais avant de lire son travail ici sur Medium est Chris Dixon, un blogueur tech bien connu.

Vous pouvez reconnaître certains de ces noms si vous êtes dans leur domaine, mais je doute que vous reconnaissiez ces personnes si vous les croyez au supermarché. Ils peuvent être « célèbres sur Internet », mais ils sont loin d'être des noms connus de tous.

Si vous pouvez écrire des histoires régulièrement utiles et progressivement construire un lectorat, vous pouvez également figurer sur cette liste.

### Insight #2 : Medium est un endroit sérieux

Voici les tags les plus courants parmi ces 252 meilleures histoires :

```
+------------------+-------------+------------+|       Tag        |   Histoires | Pourcentage |+------------------+-------------+------------+| Startup          |          62 | 25%        || Tech             |          47 | 19%        || Life Lessons     |          45 | 18%        || Entrepreneurship |          37 | 15%        || Design           |          34 | 13%        || Self improvement |          31 | 12%        || Productivity     |          26 | 10%        || Politics         |          21 | 8%         || Programming      |          18 | 7%         || UX               |          18 | 7%         || JavaScript       |          10 | 4%         || Web Development  |          10 | 4%         |+------------------+-------------+------------+
```

Les sujets suivants — qui sont la base de la plupart des magazines populaires — n'apparaissent aucune fois :

* sports
* fitness
* voitures
* mariages
* jeux vidéo
* maisons
* nourriture
* célébrités
* finance

« Humour » apparaît 9 fois, et « satire » 5 fois. Mais c'est à peu près tout.

Il semble que la plupart des gens lisent Medium pour :

* se motiver
* en apprendre davantage sur leur domaine

À en juger par ce jeu de données, le stéréotype des lecteurs de Medium comme étant des développeurs-concepteurs-entrepreneurs n'est pas si éloigné de la vérité.

### Insight #3 : Vous devriez absolument essayer de faire publier votre histoire dans une publication

```
+----------------------+---------+-----+----------------+|      Publication     | Histoires |  %  |     Sujet      |+----------------------+---------+-----+----------------+| Pas dans une publication |      67 | 26% | n/a            || The Mission          |      52 | 21% | Productivité   || Free Code Camp       |      30 | 12% | Technologie     || Signal VS Noise      |       7 | 3%  | Startups       || Hi My name is Jon    |       4 | 2%  | Jon Westenberg || Slackjaw             |       4 | 2%  | Humour          || Startup Grind        |       4 | 2%  | Startups       || Year of Looking Glass|       4 | 2%  | Julie Zhuo     || The Startup          |       4 | 2%  | Startups       || Be Yourself          |       3 | 1%  | Vie           || Art of Practicality  |       3 | 1%  | Productivité   || Conquer Corp America |       3 | 1%  | Productivité   || Personal Growth      |       2 | 1%  | Productivité   || The Coffeelicious    |       2 | 1%  | Startups       || Development Set      |       2 | 1%  | Éducation      || UX Design            |       2 | 1%  | UX             |+----------------------+---------+-----+----------------+
```

Une grande majorité des 252 meilleures histoires ont été publiées dans l'une des publications de Medium.

Si vous y réfléchissez un instant, cela a parfaitement du sens. Ces histoires sont apparues non seulement dans les fils d'actualité des lecteurs qui suivaient leurs auteurs, mais aussi dans ceux des lecteurs qui suivaient la publication.

Et certaines de ces publications ont [beaucoup de followers](http://toppub.xyz/).

### Insight #4 : Les histoires personnelles fonctionnent mieux

Voici une analyse lexicale des mots les plus courants dans les titres des 252 meilleures histoires. J'ai filtré les mots vides comme « the » et « of ».

```
+-------+-----------------+| Compte |      mot        |+-------+-----------------+|    42 |  vous           ||    39 |  je             ||    30 |  comment        ||    24 |  votre          ||    16 |  à propos       ||    15 |  mon            ||    14 |  personnes      ||    14 |  vie            ||    12 |  pourquoi       ||    11 |  design         ||    10 |  moi            ||     9 |  trump          ||     9 |  lire           ||     9 |  apprendre      ||     8 |  temps          ||     7 |  nouveau        ||     7 |  lettre         ||     6 |  vous-même      ||     6 |  vivre          ||     6 |  travail        ||     6 |  mieux          ||     5 |  année          ||     5 |  blanc          ||     5 |  silicon valley ||     5 |  arrêter        ||     5 |  jamais         ||     5 |  plus           ||     5 |  f***           ||     5 |  gratuit        ||     5 |  apps           ||     4 |  monde          ||     4 |  travail        ||     4 |  sites web      ||     4 |  web            ||     4 |  réussi         ||     4 |  plus intelligent||     4 |  ouvert         ||     4 |  javascript     ||     4 |  difficile      ||     4 |  guide          ||     4 |  f******        ||     4 |  code           ||     3 |  souhait        ||     3 |  technologie    ||     3 |  startup        ||     3 |  secret         ||     3 |  quitter        ||     3 |  productivité   ||     3 |  programmation  ||     3 |  puissant       ||     3 |  medium         ||     3 |  amour          ||     3 |  futur          ||     3 |  développement  ||     3 |  développeur    ||     3 |  designer       ||     3 |  carrière       ||     3 |  business       |+-------+-----------------+
```

Les mots « vous » et « je » étaient de loin les plus courants, ce qui suggère que s'adresser directement au lecteur en tant que personne individuelle est une meilleure stratégie d'écriture que d'écrire à la troisième personne.

Les mots les plus courants en dehors des 100 [mots les plus courants de la langue anglaise](https://en.wikipedia.org/wiki/Most_common_words_in_English) étaient « vie » et « design ».

En parlant d'anglais, toutes les histoires des 252 meilleures, à l'exception de trois, étaient écrites en anglais.

### Insight #5 : Vous n'avez pas besoin de jurer pour attirer l'attention des gens

Beaucoup de gens se plaignent de l'abondance de jurons dans les titres de Medium.

Bien qu'ils soient certainement présents, le mot « F » et ses variantes n'apparaissent que 13 fois dans les titres des 252 meilleures histoires, et le mot « S » n'apparaît que 3 fois.

### Insight #6 : Les « listacles » existent toujours, mais ils ne dominent pas Medium

Seulement 23 des 252 meilleures histoires étaient explicitement des « listacles » — des histoires basées sur des points à puces.

Ces histoires ont des titres qui suivent le modèle « [nombre] choses que vous devriez faire avant [temps] ».

Divulgation complète : l'un de ces listacles est mon histoire sur [Linux qui fête ses 25 ans](https://medium.freecodecamp.com/linux-is-25-yay-lets-celebrate-with-25-rad-facts-about-linux-c8d8ac30076d#.tzo9h78jr).

Mais dans l'ensemble, je dirais que le déclin des listacles est une bonne chose.

Mon conseil personnel aux écrivains est de se concentrer sur des histoires qui approfondissent un seul sujet.

### Insight #7 : 7 minutes est toujours une longueur d'histoire idéale

![Image](https://cdn-media-1.freecodecamp.org/images/HzH8seT2kuP-Kn3NVOUqcEfvFvfF6AV4MZzr)

Les 252 meilleures histoires avaient une longueur moyenne de 6,7 minutes — la même longueur que l'équipe de science des données de Medium avait déterminée comme optimale [dès 2014](https://medium.com/data-lab/the-optimal-post-is-7-minutes-74b9f41509b#.gjnp22pis).

### Insight #8 : Inclure des images.

Seulement 16 des meilleures histoires n'avaient aucune image.

Le nombre médian d'images incluses dans une histoire était de 3.

Ne vous inquiétez pas de trop en faire avec les images. 11 % des histoires utilisaient 10 images ou plus, et deux d'entre elles utilisaient plus de 50 images.

### Insight #9 : Avoir beaucoup de followers aide définitivement

Le nombre médian de followers que ces auteurs avaient à la fin de l'année était de 6 809.

Même si vous n'avez pas encore beaucoup de followers, il y a encore de l'espoir de figurer parmi les meilleures histoires de 2017. 29 des auteurs avaient moins de 2 000 followers, un nombre que vous pouvez atteindre en quelques mois si vous arrivez à écrire quelques histoires populaires.

La meilleure façon d'inciter les gens à vous suivre est de leur rappeler de le faire.

Si quelqu'un lit jusqu'au bout de votre article, il est juste (et bien dans les conditions d'utilisation de Medium) de lui rappeler de vous suivre.

### Insight #10 : Ne désactivez pas les réponses.

Seulement 6 des meilleures histoires avaient désactivé les réponses.

Imaginez que quelqu'un lit votre histoire et pense à quelque chose d'intéressant à ajouter. Il fait défiler jusqu'au bas de votre histoire pour découvrir qu'il ne peut pas partager ses pensées parce que vous avez désactivé les réponses.

Va-t-il recommander votre histoire ? Pas moi en tout cas.

Ne freinez pas le discours autour de votre histoire. Permettez à vos lecteurs de vous répondre.

### Maintenant, retournons à l'écriture

Un grand merci à [Levent Aşkan](https://www.freecodecamp.org/news/what-i-learned-from-analyzing-the-top-253-medium-stories-of-2016-9f5f1d0a2d1c/undefined), qui a pris le temps de compiler ces 252 meilleures histoires de Medium. Vous pouvez lire son histoire à leur sujet [ici](https://medium.com/startup-grind/mediums-most-recommended-stories-of-2016-171efdd705c5#.jlfo409vs).

Merci également à [Kande Bonfim](https://www.freecodecamp.org/news/what-i-learned-from-analyzing-the-top-253-medium-stories-of-2016-9f5f1d0a2d1c/undefined) pour avoir approfondi le jeu de données de Levent.

Et si vous êtes intéressé à obtenir plus de lecteurs en 2016, consultez mes [conseils pour écrire des histoires sur Medium que les gens liront](https://medium.freecodecamp.com/how-to-write-medium-stories-people-will-actually-read-92e58a27c8d8#.n4ps93qhe).

[**Comment écrire des histoires sur Medium que les gens liront réellement**](https://medium.freecodecamp.com/how-to-write-medium-stories-people-will-actually-read-92e58a27c8d8)  
[_Plus de 30 millions de personnes utilisent Medium chaque mois. Ils viennent ici à la recherche de quelque chose qui vaut la peine d'être lu. Quelque chose..._medium.freecodecamp.com](https://medium.freecodecamp.com/how-to-write-medium-stories-people-will-actually-read-92e58a27c8d8)

Et mon guide de style non officiel pour [Medium](https://medium.freecodecamp.com/a-style-guide-for-writing-on-medium-fcbad27492ea#.hxj5qm1vw) :

[**Un guide de style pour écrire sur Medium**](https://medium.freecodecamp.com/a-style-guide-for-writing-on-medium-fcbad27492ea)  
[_Après avoir passé plus de 1 000 heures à écrire et éditer des histoires pour notre publication Medium, j'ai décidé de créer..._medium.freecodecamp.com](https://medium.freecodecamp.com/a-style-guide-for-writing-on-medium-fcbad27492ea)

Santé, et bon écriture !

**Je n'écris que sur la programmation et la technologie. Si vous [me suivez sur Twitter](https://twitter.com/ossia), je ne perdrai pas votre temps. ?**
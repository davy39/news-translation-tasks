---
title: 'Comment Reddit déploie des fonctionnalités à grande échelle : un entretien
  avec son VP Engineering'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-24T22:44:07.000Z'
originalURL: https://freecodecamp.org/news/how-reddit-builds-features-at-scale-an-interview-with-the-vp-of-engineering-f92b67974fd6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_RcsvyMHhZmrnS0MAzrQig.jpeg
tags:
- name: leadership
  slug: leadership
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 'Comment Reddit déploie des fonctionnalités à grande échelle : un entretien
  avec son VP Engineering'
seo_desc: 'By Iris Nevins

  Reddit’s VP of Engineering, Nick Caldwell, recently sat down with the Breaking Into
  Startups Crew to talk about leadership, company culture, machine learning, time
  management, and more.

  For those who don’t know how awesome Reddit is, i...'
---

Par Iris Nevins

Le VP Engineering de Reddit, [Nick Caldwell](https://breakingintostartups.com/68-nick-caldwell-vp-engineering-reddit), s'est récemment entretenu avec l'équipe de [Breaking Into Startups](https://breakingintostartups.com/) pour discuter de leadership, de culture d'entreprise, de machine learning, de gestion du temps, et plus encore.

Pour ceux qui ne savent pas à quel point [Reddit](https://www.reddit.com/) est génial, c'est un forum en ligne avec 1,1 million de communautés actives. Ces communautés se composent de forums de discussion sur à peu près tous les sujets imaginables, des « [vieilles dames faisant des tartes](https://www.reddit.com/r/OldLadiesBakingPies/) » et des « [animaux qui sont des crétins](https://www.reddit.com/r/AnimalsBeingJerks/) » à « [tout sur la science](https://www.reddit.com/r/EverythingScience/) » et la « [mode](https://www.reddit.com/r/fashion/) ».

Reddit est le 4ème site web le plus populaire aux États-Unis et le 7ème site web le plus populaire au monde. Plus particulièrement, Reddit compte des centaines de millions d'utilisateurs, ce qui signifie que ses problèmes logiciels sont assez uniques.

![Image](https://cdn-media-1.freecodecamp.org/images/BePA3KNzmU0n5KAQiMkpKVykoQtDI-hGbyXg)
_?? Regardez la [visite vidéo complète du siège de Reddit à San Francisco ?](https://www.facebook.com/BreakingIntoStartups/videos/508857829458678/\" rel=\"noopener\" target=\"_blank\" title=\")_

Par exemple, Reddit a récemment tenté de « mieux communiquer l'échelle de Reddit » à ses utilisateurs en [construisant un système](https://redditblog.com/2017/05/24/view-counting-at-reddit/) qui affiche le nombre de vues qu'un post a reçu plutôt que seulement les upvotes.

Certains posts reçoivent des millions de vues, ce qui signifie que compter les vues avec précision est très délicat. Reddit doit non seulement maintenir un décompte exact en temps réel, mais aussi garder une trace de si un utilisateur spécifique a déjà visité le post ou non.

Pour les posts ayant des millions de vues, il serait très coûteux en mémoire et en CPU de stocker des millions d'identifiants d'utilisateurs dans un ensemble (set), puis de vérifier cet ensemble à chaque nouvelle vue. Les ingénieurs de Reddit ont pu déterminer qu'une approche de comptage basée sur [HyperLogLog](http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf) (HLL) nécessiterait 0,15 % de la mémoire que le stockage de millions d'ID utilisateur exigerait.

Ce sont les types de problèmes intéressants auxquels les ingénieurs de Reddit sont confrontés alors que l'entreprise et sa plateforme continuent de croître.

![Image](https://cdn-media-1.freecodecamp.org/images/-ukcpXbce3v4gxWd0Mihuc83txEMxrsVbbnb)
_Affichage de l'ancien profil utilisateur (à gauche) et nouvelle page de profil (à droite), pour u/Kn0thing._

Voici un autre exemple du rôle que joue la taille de Reddit dans le travail de ses ingénieurs. Reddit a récemment créé des pages de profil en utilisant une nouvelle stack frontend. Ils ont décidé que pendant leur période bêta, les utilisateurs pourraient choisir d'adopter la nouvelle expérience de profil. Cela signifiait qu'il fallait trouver comment router les requêtes à travers différentes stacks, permettant à certains utilisateurs d'être dirigés vers la page de profil originale et à d'autres d'être dirigés vers la nouvelle page de profil.

Les ingénieurs de Reddit ont découvert que l'utilisation de [VCL personnalisé dans Fastly](https://docs.fastly.com/guides/vcl/guide-to-vcl) leur permettait de réaliser cela. En août 2017, ils ont pu [« router dynamiquement 75 000 profils d'utilisateurs »](https://redditblog.com/2017/08/04/dynamically-routing-requests-across-different-stacks-with-vcl/) pendant la bêta (apprenez-en plus sur la nouvelle stack front-end de Reddit [ici](https://redditblog.com/2017/06/30/why-we-chose-typescript/)).

### Rencontrez Nick, développeur devenu VP Engineering

![Image](https://cdn-media-1.freecodecamp.org/images/Q0cvyA1NDq4ic-YB-i0hcPse369a75-M4LcQ)
_L'[entretien complet de Nick Caldwell avec le podcast Breaking Into Startups](https://soundcloud.com/breakingintostartups/nick-caldwell-vp-of-engineering-at-reddit\" rel=\"noopener\" target=\"_blank\" title=\") ?_

Nick Caldwell gère une centaine d'ingénieurs qui résolvent des problèmes complexes comme ceux-ci chaque jour. Alors, comment Nick est-il devenu VP Engineering chez Reddit ? Son histoire commence dans l'enfance.

Les parents de Nick, un défenseur public et une enseignante, l'ont exposé à des idées, des livres et à la technologie informatique, mais surtout — à la connaissance qu'il y avait plus de possibilités que ce qu'il pouvait voir dans son environnement immédiat.

Quand Nick a développé un intérêt pour l'informatique, son père lui a offert un livre intitulé _C++ In 12 Easy Lessons._ Mais il a fallu bien plus que ce livre pour apprendre le C++.

Nick avait un fort intérêt pour l'informatique, une nature orientée vers les objectifs et le désir de fréquenter une école bien dotée en ressources. Cela l'a mené vers un programme d'excellence en sciences et technologie. Après cela, il a étudié le machine learning au MIT dans les années 90, décrochant son premier emploi en informatique pendant sa première année.

![Image](https://cdn-media-1.freecodecamp.org/images/3jtwU1HxpMAyP5aV-EjcuPtZlkpE2J0Sy52U)

Nick note que pour ceux d'entre nous qui en sont aux premières étapes de leur carrière d'ingénieur logiciel, le plus important est de choisir un domaine qui nous passionne (sa spécialité en machine learning a fortement contribué à sa capacité à trouver du travail).

Une fois que nous avons choisi une spécialité, nous devons « affiner notre art » et « passer beaucoup de temps à nous débattre avec des défis de codage complexes ».

Si nous décidons de suivre une voie de management, l'étape suivante est de devenir engineering manager, où l'on fait « un peu moins de code au quotidien » afin de se concentrer davantage sur l'aspect « humain » d'une équipe.

De là, on peut devenir directeur, ce qui signifie gérer plusieurs engineering managers et coordonner les ressources. Après cela, on devient VP Engineering, ce qui signifie gérer plusieurs directeurs tout en se concentrant sur la stratégie commerciale et la direction d'une entreprise.

Tout au long de l'[entretien](https://breakingintostartups.com/68-nick-caldwell-vp-engineering-reddit), Nick mentionne certains des défis spécifiques de la gestion d'ingénieurs, comme décider qui va diriger un certain projet ou décider quels projets potentiels s'alignent le mieux avec la mission de l'entreprise. Il traite de choses comme la « dette technique », les périodes soudaines de fort trafic et les systèmes d'opérations complexes.

Il a fallu 13 ans à Nick pour gravir les échelons du leadership et son autodiscipline a joué un rôle important. Nick ne prend qu'un seul grand repas par jour car cela lui donne plus de temps pour faire d'autres choses. Il accorde également la priorité à la fixation d'objectifs et tient même un document qui suit tous ses objectifs depuis une dizaine d'années.

S'élever au niveau de management de Nick signifie échanger du temps passé à coder contre une influence sur les décisions commerciales, la culture d'entreprise et les processus de recrutement.

Nick parle du « snoos day », un excellent ajout à la culture d'entreprise de Reddit. Deux jours par trimestre, les ingénieurs de toute l'entreprise peuvent travailler sur des projets personnels et parfois ils produisent des [projets](https://redditblog.com/2017/08/10/snoos-day-a-reddit-tradition/) qui ont un impact positif sur toute l'entreprise. Les managers et les dirigeants ont le pouvoir de mettre en œuvre des choses comme celle-ci. Pour donner le ton. Pour changer l'environnement.

Je me suis souvent demandé si je prendrais ou non une voie de management. Est-ce que je préférerais développer mes compétences techniques jusqu'à ma retraite ou devenir un leader qui construit et accompagne les programmeurs vers l'excellence — un leader qui influence positivement la direction d'une entreprise entière ?

Je ne sais pas quel chemin je prendrai, mais Nick rend le leadership assez significatif et gratifiant.

[L'entretien de Breaking Into Startups](https://breakingintostartups.com/68-nick-caldwell-vp-engineering-reddit) regorge de bien plus de choses que ce que j'ai couvert ici, vous devriez donc absolument consulter l'entretien de Nick, et quand vous aurez fini, faites savoir à Breaking Into Startups ce que vous en pensez.

![Image](https://cdn-media-1.freecodecamp.org/images/6LdXVOezLNGZd1gMLclYylnX8rTj3OusSt6S)
_L'[entretien complet de Nick Caldwell avec le podcast Breaking Into Startups](https://soundcloud.com/breakingintostartups/nick-caldwell-vp-of-engineering-at-reddit\" rel=\"noopener\" target=\"_blank\" title=\") ?_

Je suis Iris Nevins, une ingénieure logiciel autodidacte. Si vous aimez mon article, n'hésitez pas à le partager et à m'envoyer quelques claps. =)

Vous pouvez suivre mes histoires [ici](https://medium.com/@cosmosiris). Et n'hésitez pas à [m'envoyer un e-mail](mailto:nevinsiris@gmail.com).
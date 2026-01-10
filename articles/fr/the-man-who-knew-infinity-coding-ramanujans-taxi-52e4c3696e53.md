---
title: 'L''Homme Qui Connaissait l''Infini : Coder le Taxi de Ramanujan'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-11T03:07:43.000Z'
originalURL: https://freecodecamp.org/news/the-man-who-knew-infinity-coding-ramanujans-taxi-52e4c3696e53
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OtfAhkXJxkyvlqBHP88Viw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Functional Programming
  slug: functional-programming
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
seo_title: 'L''Homme Qui Connaissait l''Infini : Coder le Taxi de Ramanujan'
seo_desc: 'By Geoffrey Bourne

  Have you see the movie (or read the book) The Man Who Knew Infinity?

  This new movie — which stars Dev Patel and Jeremy Irons — explores Indian mathematician
  Srinivasa Ramanujan and his profound understanding, ingenuity, and love of...'
---

Par Geoffrey Bourne

Avez-vous vu le film (ou lu le livre) [The Man Who Knew Infinity](http://www.imdb.com/title/tt0787524/) ?

Ce nouveau film — qui met en vedette Dev Patel et Jeremy Irons — explore la vie du mathématicien indien Srinivasa Ramanujan et sa profonde compréhension, son ingéniosité et son amour des mathématiques.

Le film m'a inspiré à la fois sur le plan intellectuel et émotionnel. Mais ce qui a vraiment attiré mon attention, c'est une scène particulière de cinq secondes.

La scène se déroule en 1918. Le mentor et ami de Ramanujan, G.H. Hardy, fait remarquer qu'il vient de prendre le taxi numéro 1729 et trouve ce nombre « plutôt ennuyeux ».

Ramanujan répond avec passion : « Non, Hardy, c'est un nombre très intéressant ! C'est le plus petit nombre exprimable comme la somme de deux cubes de deux manières différentes. »

Ramanujan était capable de voir au-delà du simple numéro de taxi et de plonger dans les profondeurs de l'expression derrière celui-ci : a³ + b³ = c³ + d³… mieux connu sous le nom de [nombre de taxi de Ramanujan](https://en.wikipedia.org/wiki/Taxicab_number). J'ai trouvé ce problème fascinant et je me suis demandé à quoi ressemblerait l'implémentation du code. Je ne réalisais pas qu'il y avait tant de couches d'optimisation à cet oignon algorithmique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HgjCp6zNl5q1C5VSJXESjg.jpeg)
_Le taxi que Ramanujan a pris — du moins dans le film_

#### Première Tentative d'Implémentation du Taxi de Ramanujan

J'ai commencé par une implémentation directe écrite en Scala. Le code, avec les mesures de performance, peut être trouvé sur [GitHub](https://github.com/gbourne1/Ramanujan_Taxi) :

Nous commençons par une implémentation brute-force en parcourant toutes les combinaisons pour trouver où a³ + b³ = c³ + d³. Nous obtenons une performance O(n⁴) en raison des quatre boucles utilisées pour calculer toutes les valeurs de a³, b³, c³ et d³ égales ou inférieures au paramètre n, qui délimite notre champ de recherche.

Cette implémentation brute-force, avec une performance O(n⁴), est plutôt médiocre. Alors, comment pouvons-nous faire mieux ?

#### Nous Pouvez Faire Mieux

La première question à se poser est : devons-nous toujours calculer toutes les valeurs de a³, b³, c³ et d³ ? Rappelez-vous, l'équation que nous utilisons est a³ + b³ = c³ + d³. Si nous résolvons pour d³, nous obtenons d³ = a³ + b³ - c³. Ainsi, une fois que nous connaissons a³, b³ et c³, nous pouvons calculer la valeur de d³ directement au lieu de parcourir toutes les valeurs de d³.

Ma prochaine implémentation, encore en Scala, remplace la quatrième boucle par le calcul d³ = a³ + b³ — c³ :

La deuxième version a une performance O(n³) puisque nous pouvons sauter cette boucle finale. Génial !

#### La Troisième Fois est la Bonne

Nous n'avons pas encore terminé. Il y a une troisième, et la meilleure à ce jour, amélioration à considérer. Et si nous n'avions pas besoin de résoudre pour toutes les valeurs non seulement de d³, mais aussi de c³ ? Quelques points à comprendre :

1. Si nous calculons toutes les valeurs de a³ et b³ égales ou inférieures à n, nous avons essentiellement toutes les valeurs possibles non seulement de a³ et b³, mais aussi de c³ et d³.
2. La somme de a³ + b³ est égale à la somme de c³ + d³.
3. Si la somme du point #2 ci-dessus pour une paire donnée d'entiers (a³, b³) correspond à la somme d'une autre paire d'entiers (a³, b³), nous avons en essence trouvé la paire c³ et d³.

Si nous stockons chaque combinaison de la somme de a³ + b³ et la paire correspondante (a³, b³), toute somme qui a deux paires signifie que nous avons trouvé a³ + b³ = c³ + d³ où la première paire de la liste peut être considérée comme (a³, b³) et la suivante (c³, d³).

Par exemple, si nous parcourons les combinaisons de a³ + b³, nous stockerons la somme 1729 avec la paire (1³, 12³). En continuant à itérer, nous verrons une autre somme de 1729 apparaître, mais cette fois avec la paire (9³, 10³). Parce que nous avons deux paires différentes dont la somme est 1729, nous avons trouvé un nombre de taxi de Ramanujan qui résout a³ + b³ = c³ + d³.

Dans la troisième version, nous utilisons une Hashmap pour stocker la somme (clé) et la liste correspondante de paires sous forme d'ensemble trié (valeur). Si la liste contient plus d'une paire, nous avons un gagnant !

Cette implémentation a une performance O(n²) puisque nous n'avons besoin que de deux boucles pour calculer les combinaisons pour a³ et b³. Très génial !

Je soupçonne qu'il existe une quatrième optimisation où nous n'avons besoin de calculer que les valeurs de a³ et de dériver b³ de a³ (la boucle 'b' est juste un décalage de la boucle 'a') avec une performance O(n).

De plus, un autre défi consiste à réécrire les implémentations selon un modèle de programmation fonctionnelle. Je vous laisse explorer cela.

#### Un Film Extraordinaire, un Homme Extraordinaire

Après avoir regardé The Man Who Knew Infinity, j'ai été émerveillé par le génie de Ramanujan. En implémentant son algorithme de taxi — avec ses plusieurs optimisations de performance — j'ai entrevu la beauté qu'il voyait dans « Non, Hardy, c'est un nombre très intéressant ! »

Le nombre de taxi de Ramanujan, âgé de près d'un siècle, continue de faire de nouvelles découvertes. Des mathématiciens de l'Université Emory ont [découvert](http://phys.org/news/2015-10-mathematicians-magic-key-ramanujan-taxi-cab.html) que le nombre 1729 est lié aux courbes elliptiques et aux surfaces K3 — des objets importants aujourd'hui dans la théorie des cordes et la physique quantique.

Je pense que nous n'avons fait qu'effleurer la surface du nombre de taxi de Ramanujan et du génie incroyable de cet homme.

**À propos de l'auteur :** [Geoffrey Bourne](https://www.freecodecamp.org/news/the-man-who-knew-infinity-coding-ramanujans-taxi-52e4c3696e53/undefined) est le PDG de [RETIRETY](https://www.retirety.com) — aidant les personnes à la retraite ou proches de la retraite à trouver une meilleure façon de prendre leur retraite.

#### Merci d'avoir lu !

### Si vous avez aimé cet article, n'hésitez pas à cliquer sur le bouton d'applaudissements ci-dessous ? pour aider les autres à le trouver !
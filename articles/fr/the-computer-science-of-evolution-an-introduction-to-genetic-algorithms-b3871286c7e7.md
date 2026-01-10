---
title: 'La Science Informatique de l''Évolution : une Introduction aux Algorithmes
  Génétiques'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T20:49:44.000Z'
originalURL: https://freecodecamp.org/news/the-computer-science-of-evolution-an-introduction-to-genetic-algorithms-b3871286c7e7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*J3BtJTlHKnx3152UKoTgYg.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: evolution
  slug: evolution
- name: Genetics
  slug: genetics
- name: 'Science '
  slug: science
- name: 'tech '
  slug: tech
seo_title: 'La Science Informatique de l''Évolution : une Introduction aux Algorithmes
  Génétiques'
seo_desc: 'By Ben Mmari

  Being a computer scientist with an interest in evolution and biological processes,
  the topic of genetic algorithms, and more broadly, evolutionary computation is to
  me what a candy shop is to a 5-year-old: Heaven. The mere possibility of...'
---

Par Ben Mmari

En tant qu'informaticien passionné par l'évolution et les processus biologiques, le sujet des algorithmes génétiques, et plus largement, de la computation évolutive, est pour moi ce qu'est une confiserie pour un enfant de 5 ans : le Paradis. La simple possibilité de pouvoir fusionner deux de mes intérêts de manière si harmonieuse a été extrêmement exaltante, et il serait dommage de garder cette connaissance et cette excitation pour moi seul.

Ainsi, dans le but de tester certaines de mes connaissances acquises jusqu'à présent, et de partager mes découvertes avec le reste du monde, j'ai décidé de rédiger une série d'articles sur ce sujet.

Dans cet article, je vais fournir une brève introduction aux algorithmes génétiques et expliquer comment ils imitent les mêmes processus naturels qui se déroulent sur Terre depuis des milliards d'années.

#### **La vie sur Terre**

Au cours des 3,5 derniers milliards d'années, la nature, le temps, l'évolution et la sélection naturelle ont collaboré ensemble pour produire **toutes** les formes de vie spécialisées que nous voyons sur Terre aujourd'hui : comme la plante carnivore Dionée attrape-mouche ; le poisson-volant de l'Atlantique ; les chauves-souris utilisant l'écholocation ; les girafes au long cou ; les guépards super-rapides ; les abeilles danseuses ; et bien sûr, moi-même, l'Homo sapiens rusé.

![Image](https://cdn-media-1.freecodecamp.org/images/LmZm7DjfgyLwH3RpgYrQCnWCIj0L7xB9zYvG)
_La Dionée attrape-mouche est une plante carnivore qui se nourrit principalement d'insectes et d'araignées._

![Image](https://cdn-media-1.freecodecamp.org/images/tbRcMzxleAYOcEE8r-69ZP2n6lLGunkP4QYe)
_Certaines chauves-souris utilisent l'écholocation pour naviguer et chasser leurs proies et, contrairement à la croyance populaire, les chauves-souris ne sont pas aveugles ; une espèce de chauves-souris connue sous le nom de Renards volants a même une meilleure vue que les humains._

![Image](https://cdn-media-1.freecodecamp.org/images/9m1HytKWrGc6wd46E5ijI2zanCsYY8OWW1Kr)
_Les poissons-volants ne peuvent pas voler de la même manière que les oiseaux, cependant, ces poissons peuvent faire des bonds puissants et auto-propulsés hors de l'eau où leurs longues nageoires en forme d'ailes leur permettent de planer sur des distances considérables au-dessus de la surface de l'eau._

Il va sans dire que la vie sur Terre est l'une des expériences, sinon la plus réussie, jamais menée dans notre univers ; et au vu des résultats impressionnants de cette expérience, il est clair que l'évolution est sur la bonne voie.

Récemment, nous, les humains — l'un des nombreux produits finaux de ce processus — avons réalisé que nous pouvions également tirer parti de cette approche ingénieuse de résolution progressive de problèmes, et depuis les années 1950, les informaticiens, les généticiens, les mathématiciens et les biologistes ont tenté d'imiter ces processus biologiques par le biais de simulations informatiques. Dans le but de produire des solutions optimales pour des problèmes difficiles et non triviaux, de manière efficace.

![Image](https://cdn-media-1.freecodecamp.org/images/LdDYa7txaI3r3aOW2UnrS-U1yyIQaBhR0RzF)

#### **L'horloger aveugle**

L'un des premiers livres que j'ai rencontrés et qui a suscité mon intérêt pour le domaine de la biologie évolutive était [L'Horloger Aveugle](https://www.goodreads.com/book/show/117047.The_Blind_Watchmaker), de Richard Dawkins. Dans ce livre, Richard Dawkins explique comment des mécanismes complexes comme [l'écholocation](https://en.wikipedia.org/wiki/Animal_echolocation) (un processus que les chauves-souris utilisent pour naviguer, chasser et se nourrir, également connu sous le nom de bio-sonar), des structures complexes comme les toiles d'araignée (que les araignées utilisent pour attirer et capturer leurs proies), et des instruments complexes comme l'œil humain (ces deux objets sphériques que vous utilisez actuellement pour lire cet article) sont simplement le résultat de milliers, voire de millions d'années d'évolution et d'adaptation.

![Image](https://cdn-media-1.freecodecamp.org/images/M35jP6QH4Qor2PeQHTErVdrxHexZe1ALKB1j)
_L'évolution progressive de l'œil humain. Ce qui a commencé comme de simples cellules photosensibles a évolué vers un instrument complexe que nous tenons souvent pour acquis. Les premiers animaux ayant quelque chose ressemblant à un œil vivaient il y a environ 550 millions d'années. Et, selon les calculs d'un [scientifique](https://www.pbs.org/wgbh/evolution/library/01/1/l_011_01.html" rel="noopener" target="_blank" title="), il ne faudrait que 364 000 ans pour qu'un œil de type caméra évolue à partir d'une tache sensible à la lumière._

Même si ces merveilles de la nature donnent l'impression d'avoir été construites avec un but dès le départ (c'est-à-dire par un "créateur" conscient), elles sont en réalité simplement le résultat d'itérations sur des essais et des erreurs, accompagnées d'une pression de sélection en constante évolution (c'est-à-dire un changement de climat, d'habitat, ou du comportement et des capacités des prédateurs ou des proies). Ainsi, bien qu'elles puissent sembler et se comporter comme le résultat d'un génie précis et prospectif, elles sont en réalité le résultat d'un processus complètement aveugle, un processus qui ne sait pas à l'avance quelle serait la solution "parfaite".

#### **Qu'est-ce que les algorithmes génétiques et pourquoi en avons-nous besoin ?**

Les algorithmes génétiques sont une technique utilisée pour générer des solutions de haute qualité pour des problèmes d'optimisation et de recherche, basés sur des processus biologiques fondamentaux. Ces algorithmes sont utilisés dans des situations où la gamme possible de solutions est très large, et où les approches plus basiques de résolution de problèmes comme la recherche exhaustive/la force brute consommeraient trop de temps et d'efforts.

![Image](https://cdn-media-1.freecodecamp.org/images/1GLH7oZafaBQavO5i0FCqqhifqkG5fRNXT39)

Le [problème du voyageur de commerce](https://en.wikipedia.org/wiki/Travelling_salesman_problem) pose la question suivante : "Étant donné une liste de villes et les distances entre chaque paire de villes, quel est le trajet le plus court possible qui visite chaque ville et revient à la ville d'origine ?" C'est un problème NP-difficile en optimisation combinatoire.

Nous pouvons utiliser des algorithmes génétiques pour fournir des solutions de haute qualité à ce problème, à un coût beaucoup plus faible que les techniques de résolution de problèmes plus primitives, comme la recherche exhaustive, qui nécessiterait de permuter à travers toutes les solutions possibles.

#### **Comment fonctionnent les algorithmes génétiques ?**

![Image](https://cdn-media-1.freecodecamp.org/images/GWo8z30RJKWLiKSH7UOgqT8UOfFGuC0cASCq)

Un algorithme fonctionne en itérant à travers un certain nombre d'étapes, jusqu'à ce qu'il atteigne un point de terminaison prédéfinie. Chaque itération de l'algorithme génétique produit une nouvelle génération de solutions possibles, qui, en théorie, devrait être une amélioration par rapport à la génération précédente.

Les étapes sont les suivantes :

1. Créer une population initiale de N solutions possibles (la soupe primordiale)

La première étape de l'algorithme est de créer un groupe initial de solutions qui servent de solutions de base dans la génération 0. Chaque solution dans cette population initiale portera un ensemble de chromosomes, qui sont composés d'une collection de gènes, où chaque gène est assigné à l'une des variables possibles du problème. Il est important que les solutions dans la population initiale soient créées avec des gènes assignés aléatoirement, afin d'avoir un haut degré de variation génétique.

2. Classer les solutions de la population par aptitude (survie du plus apte, partie 1).

À cette étape, l'algorithme doit être capable de déterminer ce qui rend une solution plus "apte" qu'une autre solution. Cela est déterminé par la fonction d'aptitude. Le but de la fonction d'aptitude est d'évaluer la viabilité génétique des solutions au sein de la population, en plaçant celles avec les traits génétiques les plus viables, favorables et supérieurs en haut de la liste.

Dans le problème du voyageur de commerce, la fonction d'aptitude pourrait être un calcul de la distance totale parcourue par la solution. Où une distance plus courte équivaut à une aptitude plus élevée.

3. Éliminer les solutions les plus faibles (survie du plus apte, partie 2)

À cette étape, l'algorithme supprime les solutions moins aptes de la population. Le "plus apte" ne signifie pas nécessairement le plus fort, le plus rapide ou le plus féroce, comme les humains ont tendance à l'assumer. La survie du plus apte signifie simplement que plus un organisme est équipé pour survivre dans son environnement, plus il est susceptible de vivre assez longtemps pour se reproduire et transmettre ses gènes à la génération suivante.

Les étapes 3 et 4 sont collectivement connues sous le nom de **sélection**.

4. Faire reproduire les solutions les plus fortes (survie du plus apte, partie 3)

Les solutions restantes sont ensuite appariées les unes avec les autres afin de s'accoupler et de reproduire une descendance. Au cours de ce processus, dans sa forme la plus basique, chaque parent contribuera à un % de ses gènes (dans la nature, c'est un partage 50/50) à chacun de ses descendants, où P1(G)% + P2(G)% = 100%. Le processus de détermination des gènes des parents qui seront hérités par la descendance est connu sous le nom de **croisement**.

5. Muter les gènes de la descendance (**mutation**)

La descendance contiendra un pourcentage des gènes de la "mère" et un pourcentage des gènes du "père", et occasionnellement, il y aura une "mutation" d'un ou plusieurs de ces gènes. Une mutation est essentiellement une anomalie génétique, une erreur de copie qui fait qu'un ou plusieurs des gènes de la descendance diffèrent des gènes hérités de ses parents. Dans les algorithmes génétiques, dans certains cas, une mutation augmentera l'aptitude de la descendance, dans d'autres cas, elle la réduira.

Il est important de noter qu'il n'est pas nécessaire d'avoir une mutation avec chaque descendance, la fréquence de mutation requise peut également être un paramètre de l'algorithme.

Dans les algorithmes génétiques, la sélection, le croisement et la mutation sont connus sous le nom d'**opérateurs génétiques**.

6. Terminaison

Les étapes 2 à 5 seront répétées jusqu'à ce qu'un point de terminaison prédéfinie soit atteint. Ce point de terminaison peut être l'un des suivants :

1. Temps/ressources maximales allouées atteintes.
2. Un nombre fixe de générations s'est écoulé.
3. L'aptitude de la solution dominante ne peut pas être surpassée par les générations futures.

#### **Convergence de la solution**

1. Optimum global

Dans la situation idéale, la solution la plus apte aura la valeur d'aptitude la plus élevée possible, c'est-à-dire qu'elle sera la solution optimale, ce qui signifie qu'il n'y aura pas besoin de continuer avec l'algorithme et de produire des générations supplémentaires.

2. Optimum local

Dans certains cas, si les paramètres de l'algorithme ne sont pas raisonnables, la population peut tendre vers une convergence prématurée sur une solution moins optimale, qui n'est pas l'optimum global que nous recherchons, mais plutôt un optimum local. Une fois ici, continuer l'algorithme et produire des générations supplémentaires peut être futile.

![Image](https://cdn-media-1.freecodecamp.org/images/SQpPAJ72-NY7p7kJKotoBiWWYNJmJt-UmeGQ)
_Optimum global vs optimum local_

#### **Que se passerait-il s'il n'y avait pas de mutations ?**

À première vue, les mutations peuvent sembler être une partie inutile et sans importance du processus. Mais sans cet aspect fondamental de randomisation, l'évolution par sélection naturelle serait complètement restreinte à la variété génétique définie par la population initiale, et il n'y aurait pas de nouveaux traits introduits dans la population après cela. Cela entraverait gravement les capacités de résolution de problèmes de la nature, et la vie sur Terre ne pourrait pas s'« adapter » à son environnement, du moins pas physiquement.

Si c'était le cas dans notre algorithme génétique, à un moment donné dans notre simulation, les générations futures de la population ne pourraient pas explorer une partie de l'espace de solutions que leurs prédécesseurs n'ont pas explorée. Une simulation sans aucune mutation restreindrait gravement la variation génétique au sein de la population, et dans la plupart des cas — selon la population initiale — nous empêcherait d'atteindre un optimum global.

![Image](https://cdn-media-1.freecodecamp.org/images/3QFDQk2FY1jiPsvblLEuPuxzqjFMNAeawGIn)
_Sans mutations, nous n'aurions pas de mutants, et sans mutants, nous n'aurions pas la franchise des X-Men._

#### **Que se passerait-il si la taille de la population n'était pas suffisamment grande ?**

Je suis récemment allé au sanctuaire faunique de Jukani à Plettenberg, où j'ai eu le privilège de rencontrer un tigre blanc. C'était un animal vraiment majestueux. Il était grand, il avait l'air féroce, et il était aussi aveugle à 80 % et empirant progressivement avec les années.

Pourquoi était-il aveugle ? Parce qu'il est le produit de générations de consanguinité. Ces tigres blancs ne sont produits que lorsque deux tigres porteurs d'un gène récessif contrôlant la couleur du pelage sont accouplés ensemble. Ainsi, afin d'assurer la continuation de ces tigres en captivité, les gens ont élevé ces tigres au sein d'une population très limitée afin de les exhiber dans des cirques, de les parader dans des zoos, ou de les garder comme animaux de compagnie.

Mais l'un des effets négatifs de la consanguinité est que vous limitez sévèrement la variation génétique au sein de l'espèce, ce qui augmente progressivement les chances que des traits récessifs nuisibles soient transmis à la descendance.

![Image](https://cdn-media-1.freecodecamp.org/images/RMBs4EciPnnoKCCfrTNr4BDKJPvNKu32dRtS)
_Le tigre blanc que j'ai rencontré au sanctuaire faunique de Jukani en avril 2019. Il a l'air majestueux, mais il souffre._

Même dans la nature, la consanguinité peut encore être un problème majeur. Au cours des dernières décennies, la population de rhinocéros en Afrique du Sud a été considérablement impactée en raison du braconnage, et si la taille de la population atteint un nombre suffisamment bas, cela signifierait que le maintien de la diversité génétique de ces espèces de rhinocéros menacées serait extrêmement difficile. Ainsi, même si le braconnage ne les mène pas complètement à l'extinction, la consanguinité pourrait le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/H3GecodM44iYchyZsSdQj1QXAusXk5oprVt-)
_Photo par [Unsplash](https://unsplash.com/photos/xtvo0ffGKlI?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">redcharlie</a> sur <a href="https://unsplash.com/search/photos/black-rhino?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")._

Bien sûr, les humains ne sont pas étrangers à la consanguinité. Un résultat célèbre de la consanguinité continue au sein de notre propre espèce est [Charles (Carlos) II d'Espagne](http://blogs.discovermagazine.com/gnxp/2009/04/inbreeding-the-downfall-of-the-spanish-hapsburgs/#.XJO9wFMzY0o).

« Le roi des Habsbourg Carlos II d'Espagne était tristement dégénéré avec une tête difforme énorme. Sa mâchoire des Habsbourg était si proéminente que ses deux rangées de dents ne pouvaient pas se rencontrer ; il était incapable de mâcher. Sa langue était si grande qu'il pouvait à peine parler. Son intellect était de même handicapé. »

![Image](https://cdn-media-1.freecodecamp.org/images/C4vGkUhe7UQOphhhbebMTt72DJNpuhy8nd6v)
_Le roi des Habsbourg Charles II d'Espagne. Son père était l'oncle de sa mère, faisant de Charles leur fils, petit-neveu et cousin germain respectivement._

La « consanguinité » dans notre algorithme génétique signifie essentiellement l'élevage de solutions ayant une constitution génétique très similaire, ce qui, heureusement, dans ce cas, ne entraînerait pas de descendance avec une prédisposition à des anomalies physiques. Mais si **la population est très petite** et si **toutes les solutions partagent une constitution génétique très similaire**, alors l'aptitude des générations futures de la population sera sévèrement restreinte. Ce qui signifie qu'il pourrait falloir beaucoup plus de temps pour converger vers une solution globalement optimale, si nous y arrivons un jour.

La consanguinité n'est pas toujours une mauvaise chose, cela dépend simplement de l'étape de la simulation dans laquelle vous vous trouvez. Dans les étapes très avancées de la simulation, alors que la population converge vers un optimum global/local, il est évidemment très difficile d'éviter la consanguinité, car, dans certains cas, beaucoup des solutions dominantes seront très similaires les unes aux autres, et partageront donc beaucoup des mêmes traits génétiques.

#### Conclusion

D'accord, cela devrait couvrir les bases. Si vous avez des questions, des demandes ou des mutations génétiques à contribuer, n'hésitez pas à laisser un commentaire ci-dessous.

Dans le prochain article, nous plongerons dans du code pour voir comment chacun des opérateurs génétiques décrits ci-dessus se déroule dans le monde de la programmation. J'ai utilisé le langage de programmation Ruby pour la simulation logicielle sur laquelle j'ai travaillé, et j'y montre comment, en seulement quelques générations, un algorithme génétique peut produire un mot ou une phrase prédéfinie à partir d'une collection initiale de charabia complet. Tout le code sera hébergé sur GitHub.
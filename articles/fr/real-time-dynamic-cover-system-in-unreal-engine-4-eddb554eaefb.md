---
title: Comment créer un système de couverture dynamique en temps réel dans Unreal
  Engine 4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-28T05:05:35.000Z'
originalURL: https://freecodecamp.org/news/real-time-dynamic-cover-system-in-unreal-engine-4-eddb554eaefb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LPJ8CNMaM5F7sM2F0Az4uQ.png
tags:
- name: gaming
  slug: gaming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment créer un système de couverture dynamique en temps réel dans Unreal
  Engine 4
seo_desc: 'By David Nadaski

  Introduction

  A cover system enables A.I. units to avoid direct fire, taking cover behind various
  objects on the map. Using a cover system enhances a game’s level of realism and
  introduces essential tactical elements to any genre. Suc...'
---

Par David Nadaski

### Introduction

Un système de couverture permet aux unités d'IA d'éviter les tirs directs en se mettant à couvert derrière divers objets sur la carte. L'utilisation d'un système de couverture améliore le niveau de réalisme d'un jeu et introduit des éléments tactiques essentiels à tout genre. Ces systèmes sont composés de deux modules distincts : la génération de couverture et la recherche de couverture. La génération de couverture est généralement statique et est effectuée avant le début du jeu, tandis que la recherche de couverture se fait en temps réel pendant le jeu.

Dans cet article, je remets en question la nature statique des systèmes de couverture en décrivant comment construire un module de génération de couverture entièrement dynamique et en temps réel à partir de zéro dans Unreal Engine 4, ainsi qu'en fournissant l'implémentation d'un module de recherche de couverture.

![Image](https://cdn-media-1.freecodecamp.org/images/DlSbdGNop6lrtKNpXWf7eEGB8NuQwsZvLPvn)

Créer un système de couverture robuste peut sembler intimidant au premier abord, mais une fois que vous réalisez qu'il s'agit simplement d'un ensemble de techniques simples assemblées, la tâche à accomplir semblera beaucoup moins intimidante.

Que vous créiez un jeu de stratégie en temps réel (RTS) de nouvelle génération ou que vous souhaitiez utiliser cela dans un jeu de tir à la première personne (FPS), j'espère que vous trouverez les informations de cet article utiles. Je recommande de télécharger le projet de démonstration et de voir comment tout cela fonctionne une fois assemblé.

Le projet inclut une implémentation entièrement fonctionnelle de toutes les techniques discutées ci-dessus, complète avec un code source bien commenté.

[**Téléchargez le projet de démonstration et le code source.**](https://horugame.com/real-time-dynamic-cover-system-for-unreal-engine-4/)

### Outils et prérequis

Le tutoriel utilise Unreal Engine 4 (UE4) version 4.18, mais il devrait également fonctionner avec des versions plus anciennes du moteur. Le projet d'exemple et le code source ont été écrits en C++. Vous avez besoin d'une compréhension de base de UE4, C++ et des Blueprints de UE4 pour comprendre le projet d'exemple et le code source.

### Conception

Lors de la conception d'un système de couverture, les trois défis les plus importants auxquels vous serez confrontés sont les suivants :

* Génération de données
* Persistance des données
* Utilisation des données

Puisque cet article se concentre sur la création d'un système de couverture dynamique en temps réel où la couverture peut devenir disponible ou disparaître complètement à l'exécution, il est essentiel d'appliquer une approche optimisée à ces trois aspects.

Je couvre deux méthodes de génération de données : **le parcours des bords du navmesh** et **le balayage 3D des objets**.

![Image](https://cdn-media-1.freecodecamp.org/images/Ka-wFYzYUt3SsPIfZbjWPLDu5kUcgM0055AB)
_Balayage 3D des objets_

![Image](https://cdn-media-1.freecodecamp.org/images/xQfw9mgSSFXxYz47O4qGjsRI24Bthfc8vU71)
_Parcours des bords du navmesh_

Si vos données de couverture sont générées de manière synchrone, cela provoque un ralentissement notable des performances de votre jeu, entraînant des retards dans le gameplay. Je démontre comment utiliser les excellentes **API multithread** d'Unreal Engine pour paralléliser la génération des données de couverture, en tirant parti du traitement multicœur généralement trouvé dans le matériel de jeu moderne.

De même, si l'accès aux données de couverture est trop lent, votre jeu ralentit considérablement, consommant de grandes quantités de cycles CPU et/ou GPU pour les requêtes de couverture. Pour éviter cela, il est préférable d'utiliser une **structure de données** conçue pour la recherche concurrente en temps réel de données spatiales : **l'octree**. L'utilisation appropriée des octrees permet également de **stocker des données de couverture personnalisées**, par exemple le matériau de couverture (pierre vs foin), la hauteur, la santé, etc., avec un accès rapide et efficace.

Les optimisations d'utilisation des données — lorsque vos unités décident activement quel point de couverture utiliser en temps réel — minimisent le nombre de raycasts et garantissent la disponibilité des facilités de recherche spatiale (octrees) ainsi que la prise en charge des requêtes de récupération directe (tableaux ou cartes).

Pour projeter comment une unité peut sortir de la couverture pour ouvrir le feu, il est nécessaire de cartographier ses **capacités de regard ou d'inclinaison**. Un char ne peut pas regarder hors de la couverture — un fantassin le peut. La meilleure façon que j'ai trouvée pour accomplir cela sans utiliser trop de raycasts est de définir des "décalages d'inclinaison" sur les unités. Ce sont simplement des floats qui sont ajoutés à l'emplacement de l'unité lors du test de collision depuis la couverture.

La dernière fonctionnalité est les **mises à jour dynamiques en temps réel** — chaque fois qu'un nouvel objet est généré dans le jeu, nous générons des points de couverture autour (et à l'intérieur) de celui-ci en utilisant le système d'événements d'Unreal via des délégués. Cela garantit que nous ne gaspillons pas de ressources sur Tick, ce qui peut ralentir considérablement le jeu si l'on n'y prend pas garde. Nous **nous connectons aux événements de mise à jour des tuiles du navmesh de Recast** et mettons à jour les points de couverture dans les tuiles correspondantes uniquement lorsque cela est nécessaire.

Malgré tout le jargon technique, c'est en fait merveilleusement simple : quelques boucles for triviales et quelques pages manquantes de la documentation UE4. Alors commençons !

### Génération de données — Deux avenues

Il existe plusieurs stratégies pour générer des données de couverture, et je couvre les deux plus importantes : premièrement, une technique similaire au balayage 3D, puis une approche de parcours des bords du navmesh.

Le balayage 3D des objets repose sur une grille 3D créée autour d'un objet. Vous avez généralement 3 boucles for principales pour faire le gros du travail, une pour chaque axe. Vous itérez sur les points de la grille qui sont à une distance constante et vérifiez si vous touchez quelque chose avec un raycast.

**Balayage 3D des objets :**

* Distribue les points de couverture de manière plus uniforme que le parcours des bords
* Prend en charge les objets incompatibles avec le navmesh, mais fournissant une couverture, par exemple, les "champs de force"
* A une chance minimale d'erreurs
* Est plus lent (en raison du grand nombre de points de grille)
* Gère mal les paysages

L'approche basée sur le navmesh repose principalement sur les données du navmesh et ne traite pas des objets en tant que tels : si un point sur la carte n'est PAS couvert par des polygones de navmesh, cela signifie qu'il est occupé par quelque chose de suffisamment grand pour fournir une couverture.

**Parcours des bords du navmesh :**

* Est considérablement plus rapide
* Gère facilement la topologie de paysage accidenté
* Ne peut pas gérer les champs de force et similaires
* Est quelque peu plus sujet aux erreurs : limites de tuiles, points non appariés
* Ne distribue pas les points de couverture de manière aussi uniforme

Je couvre ces points plus en détail au fur et à mesure, alors plongeons dans les détails du balayage 3D des objets !

### Génération de points de couverture basée sur les objets

Plutôt que de scanner le navmesh pour les trous, nous scannons les objets eux-mêmes. Imaginez cela comme scanner un objet en 3D : vous le découpez le long des axes X, Y, Z, divisez les tranches en une grille et utilisez des raycasts pour déterminer où le périmètre de l'objet — ou la circonférence 3D — rencontre le sol. Cela fonctionne également bien pour les objets de forme irrégulière, comme les formes en C, les anneaux, les châteaux — vous l'appelez.

Une grille de balayage 3D ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/MSl98wqCkYSpIysifmij0t55tnYrTJjZVms-)
_Les marqueurs orange représentent les points de grille 3D dans et autour d'un objet._

Cela est essentiellement accompli par 3 boucles for très simples qui divisent simplement la boîte de délimitation de l'acteur en une grille 3D. Mais il y a beaucoup de points sur la grille, et certains d'entre eux ne sont même pas proches de notre objet, donc nous devons les filtrer.

Et pourquoi ne pas utiliser simplement une grille 2D, pourriez-vous demander ? À cause de deux choses :

1. Les objets à plusieurs étages (pensez aux maisons avec plusieurs étages)
2. Les objets tournés sur des sols inclinés

![Image](https://cdn-media-1.freecodecamp.org/images/G2P7buWCfWvpihCK1NzjQXbZOox9DlcqQkNg)
_Un navmesh à plusieurs étages._

![Image](https://cdn-media-1.freecodecamp.org/images/sPnuEQ25EPclXOHulXrqnmL0p5Cbf1vK1QUf)
_Objet tourné sur un sol incliné._

Pour filtrer les points de grille invalides, nous lançons un rayon depuis chaque point vers le bas dans la direction -Z pour déterminer s'il est suffisamment proche du plan de sol le plus proche. Si c'est le cas, alors nous le marquons comme valide et continuons vers le suivant, lançant finalement des rayons vers le bas depuis chaque point.

Heureusement, le raycasting est très bon marché, donc nous n'avons pas à nous soucier des objets individuels — c'est seulement lorsque nous en avons une multitude à l'exécution que nous pourrions commencer à avoir des problèmes, mais nous allons traverser ce pont quand nous y arriverons.

![Image](https://cdn-media-1.freecodecamp.org/images/TRsU-6yS0DdSkBKxW6EFf4eDZVXrrdJbf2Lq)
_Trouver des plans de sol avec des raycasts._

_Bleu : plus proche du sol que le point de grille en dessous_  
_Rouge : plus éloigné du sol que le point de grille en dessous_

Puisque nous ne conservons que les bleus, nous avons beaucoup moins de points à nous soucier dans la prochaine passe : vérifier l'écart minimal du sol et la hauteur minimale de la couverture.

![Image](https://cdn-media-1.freecodecamp.org/images/wpV0azs6C9kizvk73S93cNKYt7q9njyvOuGH)

![Image](https://cdn-media-1.freecodecamp.org/images/rTwxSC7tRJ9kCfYxZ8mYVS89ucTa2SfjPsXM)
_Vérification de l'écart minimal du sol._

_Rouge : trop proche de l'objet_  
_Vert : suffisamment éloigné de l'objet pour que la plus petite unité puisse passer en dessous_

![Image](https://cdn-media-1.freecodecamp.org/images/yQ2eFbtZiaoybhuL0ejzr7yTcZOEvkfKbToJ)
_Vérification de la hauteur minimale de la couverture._

_Rouge : trop court_  
_Bleu : suffisamment grand ou vide_

Voici à quoi cela ressemble depuis la vue orthographique du dessus :

![Image](https://cdn-media-1.freecodecamp.org/images/1wr1uHVe-1p4EpJorZcS-Pmu-F8-ksPjB80b)

![Image](https://cdn-media-1.freecodecamp.org/images/o7pzwbcaSELzpCzFEu61GxF3fhSHiQaHgPxK)
_Rouge : points de grille bloquants ; Vert : points de grille libres_

Ce que nous cherchons finalement, ce sont les endroits les plus proches des marqueurs rouges sur le navmesh. Ceux-ci sont représentés par un sous-ensemble des marqueurs blancs ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/sHDkYVTKSo9Kg8znEZ5etKsqjUreROrl49IF)

![Image](https://cdn-media-1.freecodecamp.org/images/MQiTx3cITAcp5SrcCHmFLOk1wktVnieJAQyT)
_Avec le navmesh superposé par-dessus._

Les points de couverture finaux sont représentés par les marqueurs violets ci-dessous. Nous itérons sur les marqueurs rouges (ci-dessus) et choisissons ces marqueurs blancs qui sont les plus proches des rouges qui tombent sur le navmesh :

![Image](https://cdn-media-1.freecodecamp.org/images/I2bRmLIeKBU94g7hrI2RhcZ-lfsQgUxllnDy)

![Image](https://cdn-media-1.freecodecamp.org/images/RNvC4EFuXIZU-v7TfZo0EWbMpzNOkbesjR8g)
_Violet : points de couverture finaux_

Notre résultat final ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/vd6Mdqi-8XszwuX09jNfpYOaJCOXT8kL5voV)

![Image](https://cdn-media-1.freecodecamp.org/images/ciO-DnyaCt5RjHSXIkv4iX9x9igxSg9qiaUr)
_Violet : points de couverture finaux_

Voici à quoi ressemble un acteur à plusieurs étages, tourné et mis à l'échelle sur un navmesh incliné :

![Image](https://cdn-media-1.freecodecamp.org/images/AXRTSEF258LzANwaM19H03Guj4wpUutar2q3)

![Image](https://cdn-media-1.freecodecamp.org/images/kMq26KeSZH9zyF9w0yLQ2mHQqBigEVnF0R5s)
_Remarquez le niveau de conformité aux boîtes de collision — l'approche du navmesh est moins conforme_

Comme vous pouvez le voir sur les images ci-dessus, cette technique prend en charge à la fois la rotation et la mise à l'échelle sur l'objet de couverture, ainsi que sur le plan de sol. Elle convient à tout type de géométrie, et vous n'avez plus besoin de faire placer manuellement un seul marqueur dans la scène par les concepteurs de niveaux.

Puisque ce type de génération de points automatisée se prête bien à l'exécution multithread, nous allons lancer toute la logique à l'intérieur d'une tâche asynchrone que nous instruisons UE4 de mettre dans un pool de threads. Le meilleur, c'est que tout cela est supporté directement par le moteur !

Pour le faire fonctionner avec n'importe quel type d'acteur, nous créons un composant personnalisé _UActorComponent_ et lançons nos tâches de balayage 3D à partir de là. Appelons-le _UCoverGeneratorComponent_. **Ajoutez ce composant à tout acteur de type champ de force**. Ne l'utilisez pas pour les objets réguliers — le générateur basé sur le navmesh que je décris ensuite est notre solution polyvalente parfaite.

### Parcours des bords du Navmesh

Il est temps de passer au générateur le plus puissant, celui qui couvre 90 % des besoins de votre système de couverture. Alors sans plus attendre, commençons à parcourir les bords !

![Image](https://cdn-media-1.freecodecamp.org/images/23NZu58Y0ZKSguS4wMvM5QPnoCwmGBmxYeAb)

La génération de couverture via le parcours des bords est en fait un processus très simple : prenez deux sommets, lancez un rayon perpendiculaire à l'arête résultante dans les deux directions, voyez si le rayon a heurté quelque chose et si oui, alors nous avons trouvé une couverture.

![Image](https://cdn-media-1.freecodecamp.org/images/z2NF2JL9s8LtuntfwMGnoCiT9qqX9S88CKs8)
_Rayons perpendiculaires (jaunes)_

Nous pouvons compliquer les choses en termes de nombre de rayons en introduisant la détection de rebords ou de falaises :

![Image](https://cdn-media-1.freecodecamp.org/images/5Dc31YtWBxa7iEu1wBKCyOPkSGU3XVzluuQ0)
_Détection de rebords_

Cela ajoute cependant au moins 4 rayons supplémentaires par sommet du navmesh, donc nous en sommes maintenant à 6 au total : 2 pour les rayons perpendiculaires au sol, 4 pour la détection de rebords. Nous pouvons même aller plus loin et implémenter une tolérance de pente pour ces belles falaises, afin que la topologie accidentée comme les paysages soit correctement scannée :

![Image](https://cdn-media-1.freecodecamp.org/images/Ofl-lgdoOs-JtHH6p8NWdSvMYYr69remCqRE)
_Tolérance de rebord en action._

Mais cela ajoute au moins un rayon supplémentaire par côté, ce qui nous amène à 8 rayons au total dans le pire des cas. C'est à vous de décider si cette fonctionnalité vaut le coût de performance pour votre projet ou non — j'ai tendance à la laisser activée, car la plupart de la génération se fait de toute façon entièrement de manière asynchrone, et le jeu peut commencer même pendant que le système de couverture est occupé à inspecter tous ces jolis rebords que j'ai placés.

![Image](https://cdn-media-1.freecodecamp.org/images/PiM1x9Ixy1XMaakdFBvfNmB-0lr3QzwqfEwf)
_Étape 1 — Détection des bords_

![Image](https://cdn-media-1.freecodecamp.org/images/dwN5MLnXpuZIctfVSCSVOHYpOe5l5566VV7L)
_Étape 2 — Génération de points_

### Vitesse

Parcourir quelques bords est considérablement moins coûteux que de découper même un objet relativement petit en points de grille. Imaginez que la plupart des points de grille vous coûtent au moins un raycast, et qu'il pourrait y en avoir des milliers sur un simple maillage. Plus la boîte de délimitation est grande — plus il est coûteux de travailler avec le balayage 3D.

D'autre part, le nombre de polygones de navmesh sur un objet complexe ne dépassera pas quelques centaines, donc l'objet peut être aussi grand que vous le souhaitez. Sa boîte de délimitation n'a aucune influence sur son nombre de polygones de navmesh. Si vous avez beaucoup d'espace praticable sur votre objet, il sera probablement fusionné en quelques polygones. Si vous avez de nombreux détails minuscules sur la surface, il pourrait ne pas avoir de navmesh du tout. Et même si vous parvenez à construire un actif monstrueux, son nombre de polygones de navmesh est probablement insignifiant par rapport au nombre de points de grille 3D qu'il faudrait pour le scanner.

### Topologie de paysage accidenté

Les paysages sont là où les navmeshes, et par extension Recast, l'implémentation open-source de recherche de chemin intégrée dans UE4, excellent.

![Image](https://cdn-media-1.freecodecamp.org/images/jHd7kjTSskjGLICUq8oMeuuZEG4INLRUNh0B)
_Topologie de paysage._

Le problème avec les paysages et l'approche de balayage 3D des objets est que, souvent, elle identifie incorrectement les points de couverture comme appartenant au paysage au lieu de leur objet de couverture prévu. Ce n'est pas un problème lors de l'utilisation de la génération basée sur le navmesh, et c'est la principale raison — outre les gains de performance — pour laquelle nous utilisons cette technique partout où nous pouvons.

### Champs de force (Boucliers)

![Image](https://cdn-media-1.freecodecamp.org/images/QsDidhO8WYWMzO8uLysksWIDIR7CNqxj4hEl)
_Un champ de force._

Les champs de force sont quelque chose que Recast ne traverse pas, et sont donc le seul point fort du scanner d'objets 3D. Puisqu'ils sont des objets dynamiques qui n'affectent pas du tout le navmesh, j'ai créé un indicateur booléen dans la structure de données des points de couverture pour indiquer si un point appartient à l'un de ceux-ci. Ils sont indiqués par des marqueurs jaunes dans le projet de démonstration. Pensez au bouclier de Reinhardt dans Overwatch, mais un qui ne bouge pas. Cela permet aux unités de tirer à travers eux tout en étant protégées des tirs ennemis.

### Erreurs

L'approche basée sur le navmesh n'est pas sans ses inconvénients, et pour la plupart, cela se manifeste par des arêtes inutiles apparaissant sur les limites des tuiles de Recast. Il n'y a pas grand-chose que nous puissions faire à leur sujet, sauf les éliminer pendant la génération de couverture.

![Image](https://cdn-media-1.freecodecamp.org/images/q58D5y6sAPnmNPlRlYKaYt5Hb5VMawrW7uHV)
_Sommets en excès sur le navmesh._

Comme vous pouvez le voir, il y a plusieurs sommets en excès présents, mais la plupart d'entre eux sont éliminés pendant la génération des points de couverture. La principale façon de les traiter est de lancer des rayons dans les deux directions perpendiculaires aux axes XY de leur arête et de le faire à partir d'une hauteur fixe. Si rien n'est touché, alors notre point est simplement un sommet de limite de tuile et peut être éliminé en toute sécurité. Ceux-ci apparaissent également sur vos objets, mais la même technique d'élimination s'applique.

L'autre type d'erreur vient du fait que Recast ne distingue pas entre les espaces fermés et ouverts, ce qui signifie qu'il génère un navmesh à l'intérieur des objets solides également :

![Image](https://cdn-media-1.freecodecamp.org/images/z9QJakiSmkItybW-uk2aaia-1EG67s93JKaT)
_Navmesh à l'intérieur d'un objet solide._

Cela n'est évidemment pas bon, et la seule façon de contourner cela est de placer des volumes de modification de nav dans votre carte partout où vous avez des maillages solides plus grands.

![Image](https://cdn-media-1.freecodecamp.org/images/T-OMpcIKMBeXDieAxcEeyJOyg4iYeZKMm3Bc)

Cela entraîne une génération correcte de navmesh pour la plupart. Mais notez qu'il existe des cas où vous ne pourrez tout simplement pas cacher complètement ces navmeshes intérieurs. Ce n'est pas grave, car notre système de couverture filtre automatiquement les points de couverture inaccessibles, donc cela ne entraînera qu'une petite perte de performance. Les requêtes de recherche de chemin de navmesh ont tendance à être relativement coûteuses par rapport au reste de notre code de recherche de couverture, donc vous devriez toujours viser à minimiser le nombre d'îlots de navmesh inaccessibles.

![Image](https://cdn-media-1.freecodecamp.org/images/st4TteEhSRZWmCncxf5ELlwdulMsFiVw0kU4)
_Volume de modification de nav en action._

Ensuite, nous examinons comment stocker nos points de couverture dans une structure de données qui fournit un accès rapide et optimisé aux données spatiales : l'octree.

### Persistance des données — L'Octree

C'est comme croiser un poulpe avec un arbre : facile à imaginer, mais difficile à grimper. Un octree n'est rien de plus qu'une manière sophistiquée de dire "diviser le cube en 8 cubes plus petits, rincer et répéter". De même, un quadtree est simplement cela — un carré divisé en quatre carrés plus petits qui à leur tour sont divisés en quatre carrés encore plus petits, et ainsi de suite. En stockant toute notre carte de points de couverture dans un octree, nous pouvons garantir que nos requêtes spatiales sont toujours aussi efficaces qu'elles peuvent l'être.

![Image](https://cdn-media-1.freecodecamp.org/images/IaEWLaOkM6NA-Axt5jns4Rfd5TshpeOEm8Vm)
_Un cube, subdivisé en 8 cubes plus petits_

La bonne nouvelle est que la plupart du travail a déjà été fait pour nous par Epic, car UE4 dispose d'une implémentation d'octree entièrement fonctionnelle. La mauvaise nouvelle : presque aucune documentation. Ne craignez rien cependant, cela ne deviendra pas trop compliqué et nous pouvons toujours regarder _FNavigationOctree_ pour voir comment Epic a utilisé leur monstre.

Une particularité de l'octree est que chaque fois que vous souhaitez supprimer des données existantes, vous devez passer un identifiant d'élément. Mais ces identifiants ne sont pas stockés dans l'octree — nous devons mettre en place notre propre installation de stockage pour eux.

En suivant les étapes de _FNavigationOctree_, nous utilisons une simple _TMap<const FVector, FOctreeElementId> ElementToID_, où le _FVector_ est l'emplacement d'un point de couverture et _FOctreeElementId_ est la classe intégrée d'Epic qui inclut une référence au nœud dans lequel se trouve l'élément, ainsi que son index. Nous encapsulons également tous les appels d'accès à la carte dans des méthodes wrapper thread-safe. Des choses assez standard.

Le rayon (taille) de notre octree devrait imiter celui de notre navmesh. Mais pour simplifier, nous le définissons simplement à 64000, ce qui est également la valeur que _UNavigationSystem_ utilise en interne pour le navmesh par défaut.

### Mises à jour dynamiques en temps réel

L'une des fonctionnalités clés de notre système de couverture est la capacité de répondre aux changements de l'environnement en temps réel, ainsi que de pouvoir traiter de nouvelles géométries à la volée.

Cela est accompli en se connectant à l'événement de mise à jour des tuiles de Recast, ce que nous faisons en sous-classant _ARecastNavMesh_ et en remplaçant sa méthode _OnNavMeshTilesUpdated_. La fonctionnalité à l'intérieur de la méthode remplacée est très basique, mais indispensable : notifier un délégué multicast dynamique personnalisé chaque fois qu'une tuile a été mise à jour. Nous nous abonnons ensuite au délégué depuis notre classe principale du système de couverture, _UCoverSystem_ (un singleton), et lançons des tâches de génération de points de couverture en conséquence.

Nous appelons notre sous-classe _AChangeNotifyingRecastNavMesh_ et nous la connectons au jeu via un mode de jeu personnalisé. Le mode de jeu remplace la méthode _PostActorCreated()_ déclarée dans _AActor_ et utilise _SpawnActor()_ pour instancier notre _AChangeNotifyingRecastNavMesh_, comme suit :

```
void ACoverDemoGameModeBase::PostActorCreated(){
    Super::PostActorCreated();
    GetWorld()->SpawnActor<AChangeNotifyingRecastNavMesh>(AChangeNotifyingRecastNavMesh::StaticClass());
}
```

Puisqu'il peut y avoir plusieurs tuiles qui sont mises à jour dans un seul événement, et que certaines des tuiles recevraient également plusieurs mises à jour dans un laps de temps relativement court, nous découpons notre logique de génération de tâches pour ne pas mettre à jour la même tuile deux fois en succession rapide.

Vous devez également aller dans _Project Settings ==> Navigation System ==> Agents ==> Supported Agents_ et ajouter une nouvelle entrée dont la _Navigation Data Class_ et _Preferred Nav Data_ doivent toutes deux être définies sur _ChangeNotifyingRecastNavMesh_, comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/fLAlYje59IEg8jFxAY2FX9HaGd239gp3o8Jq)
_Agents supportés._

Vous devez également décocher _Auto Create Navigation Data_ sous _Navigation System_ :

![Image](https://cdn-media-1.freecodecamp.org/images/936IkiugrW8zyK9LAHlAUNc57tQb1gte4PVj)
_Création automatique des données de navigation._

Vous devrez peut-être redémarrer l'éditeur pour voir les nouveaux paramètres appliqués.

### Configuration de collision

La couverture ne doit pas être générée autour des unités comme les pions et les véhicules, alors excluez-les en définissant un canal de traçage personnalisé. Nous pouvons y faire référence en C++ comme _ECC_GameTraceChannel1_.

Allez dans _Project Settings... ==> Engine ==> Collision_ et cliquez sur le bouton _New Trace Channel..._.  
_Nom : NonUnits  
Réponse par défaut :_ Ignorer

![Image](https://cdn-media-1.freecodecamp.org/images/7PZUa0qI5hTXqSfcmajpBDFv4C0oe2jPWEup)
_Création d'un nouveau canal de traçage_

Maintenant, développez la section _Preset_ sous _Trace Channels_ et double-cliquez sur chacun des présélections suivants pour définir leur réponse contre notre nouveau canal de traçage _NonUnits_. Laissez ceux non listés ci-dessous intacts — ils sont déjà définis sur _Ignore_ par défaut et c'est ce que nous voulons.

Cochez la case _Block_ dans la ligne _NonUnits_ dans toutes les présélections suivantes :

* BlockAll
* BlockAllDynamic
* Destructible
* InvisibleWall
* InvisibleWallDynamic

![Image](https://cdn-media-1.freecodecamp.org/images/KK0K4sa9UmENj9n2Q5pm8XtPXqV9-bmUIMmd)
_Configuration de collision de blocage_

Ensuite, cochez la case _Overlap_ dans la ligne _NonUnits_ dans toutes les présélections suivantes :

* OverlapAll
* OverlapAllDynamic

![Image](https://cdn-media-1.freecodecamp.org/images/LIuogmB92rP4zjnVpw3qq5fij8U5lotQWFFV)
_Configuration de collision de chevauchement_

Ensuite, définissez un nouveau canal d'objet appelé "Shield" ou "Force Field" :

![Image](https://cdn-media-1.freecodecamp.org/images/pQ62nUjFJ-bxw0JbiLMpGd1L5kI198wctIUw)
_Canal d'objet de collision personnalisé_

Et enfin, créez une présélection de collision personnalisée nommée "NonBlockingShield" ou "NonBlockingForceField" :

![Image](https://cdn-media-1.freecodecamp.org/images/fNHu9d6vTH8MC9tFpDMJ0AtpLOUVko-pScCr)
_Présélection de collision personnalisée_

### Recherche de couverture en temps réel

Maintenant que vous avez vos points de couverture dans votre petit octree élégant, et que tout est efficace et multithread avec votre navmesh personnalisé transmettant toutes les mises à jour de tuiles... Tout est bon, alors maintenant c'est le moment de commencer à utiliser ces données !

Vos unités veulent chercher une couverture, probablement des dizaines d'unités à la fois si vous faites un RTS — mieux encore, un RTS axé sur les tactiques (techniquement un RTT) — alors comment devraient-elles aborder cela au mieux ? Eh bien, c'est facile : il suffit d'interroger l'octree, de choisir un point qui convient à leurs besoins, de réserver l'endroit choisi et de s'y déplacer.

Je recommande de créer un service ou une tâche _CoverFinder_, la classe parente étant soit _UBTService_ soit _UBTTaskNode_. Si vous optez pour une tâche, alors vous pouvez ajouter un décorateur Cooldown pour qu'elle ne soit invoquée que toutes les x secondes, et qu'elle ne spamme pas votre octree et navmesh avec des requêtes, ou PhysX avec des raycasts.

Vous pouvez également créer un service _UCoverFinder_ de _UBTService_, à la place. J'ai créé les deux classes pour vous dans le projet de démonstration, mais vous devez noter que je spamme le système avec des requêtes de couverture, donc vous voudrez ajuster l'intervalle de tick de _UCoverFinder_ dans votre arbre de comportement pour qu'il consomme moins de ressources dans votre jeu.

### Évaluation de la couverture

![Image](https://cdn-media-1.freecodecamp.org/images/kKjbQSTIEQweJNZKVjSGipqiRznxECXb7YZ8)
_Évaluation de la couverture en temps réel._

Le chercheur de couverture évalue les points de couverture qui se trouvent entre une distance définie de l'unité ennemie cible. Dans le projet de démonstration de couverture, je les appelle respectivement leur portée d'attaque minimale et maximale. Le chercheur interroge l'octree pour les points dans une boîte de délimitation dont l'étendue est celle de la portée d'attaque maximale, puis filtre les points qui sont plus proches de l'ennemi que la portée d'attaque minimale. Appelons cela la _portée optimale_ de notre unité.

Il itère ensuite sur les points de couverture dans sa portée optimale jusqu'à ce qu'il trouve le premier où les conditions suivantes sont vraies :

* L'unité ne peut pas toucher l'ennemi directement depuis la couverture
* L'unité peut toucher l'ennemi en regardant ou en s'inclinant hors de la couverture
* La ligne de mire vers l'ennemi n'est pas bloquée par d'autres unités
* L'unité peut atteindre le point de couverture via la recherche de chemin sur le navmesh

Pour vérifier si notre unité peut toucher l'ennemi en regardant ou en s'inclinant hors de la couverture, nous utilisons deux raycasts qui sont pilotés par le paramètre de capacité d'inclinaison (ou de regard) de l'unité. Ce n'est qu'un simple décalage flottant qui est ajouté à l'emplacement de l'unité dans une direction perpendiculaire à celle qu'elle fait face.

![Image](https://cdn-media-1.freecodecamp.org/images/E74iYhIu9WCFMeWB0Wx3YmfJO6fuLjbOA81N)
_Test de collision en s'inclinant hors de la couverture. Jaune essayant de toucher bleu._

_Flèche bleu clair : ne peut pas toucher l'ennemi en s'inclinant_  
_Flèche orange : peut toucher l'ennemi en s'inclinant_

Dans la capture d'écran ci-dessus, une unité jaune a identifié un endroit où elle peut toucher en toute sécurité l'unité bleue, donc elle se déplace vers le point de couverture correspondant alors que l'unité bleue se précipite pour se mettre à couvert.

![Image](https://cdn-media-1.freecodecamp.org/images/pCopiHuMisZEdEiikkscvYEgDXGGqLNtFdEk)
_Jaune occupe une position de couverture sûre._

La vérification des deux côtés de l'unité est effectuée deux fois : une fois depuis une position debout, et si cela échoue, depuis une position accroupie. Cela entraîne 4 raycasts dans le pire des cas — debout : gauche, debout : droite, accroupi : gauche, accroupi : droite.

La même procédure est répétée pour chaque point de couverture jusqu'à ce qu'un bon soit trouvé, entraînant _<points de couverture mauvais> x 5 raycasts au total._

Avec les champs de force, c'est un peu différent : la seule exigence est que l'unité doit pouvoir toucher son ennemi directement depuis le point de couverture. En d'autres termes, aucune vérification d'inclinaison/regard n'est effectuée, mais il y a une vérification supplémentaire nécessaire : l'unité doit pénétrer à travers le bouclier.

Pour cela, nous devons utiliser notre présélection de collision personnalisée _NonBlockShield_ qui utilise notre canal d'objet _Shield_ en interne. Donc, cela entraîne 2 raycasts au total : un contre _NonUnits_ et l'autre contre _Shields_, et les deux doivent réussir pour que la couverture de type champ de force soit acceptable.

### Statistiques

Le système de couverture est livré avec son propre groupe de statistiques, nommé de manière appropriée _STATGROUP_CoverSystem_. Il collecte les informations suivantes :

* Temps passé à trouver une couverture (compteur de cycles)
* Nombre total d'appels à FindCover, qui équivaut au nombre total de tâches générées (dword)
* Temps total passé à trouver une couverture dans le jeu (float)
* Temps passé à générer une couverture (compteur de cycles)
* Nombre total d'appels de génération de couverture (inclut le parcours des bords et le balayage 3D des objets)
* Temps total passé à générer une couverture (inclut les deux méthodes)
* Nombre de tâches actives (dword)

Pour le voir en action, tapez _stat CoverSystem_ dans la console.

### Profilage

Puisque des statistiques personnalisées sont configurées, il est très facile de profiler le système de couverture. Il suffit d'écrire _stat startfile_ et _stat stopfile_ dans la console et de visualiser le fichier journal résultant en utilisant le _Session Frontend_ sous _Window => Developer Tools._

![Image](https://cdn-media-1.freecodecamp.org/images/mCZOaV2TuJVfLKeR1-JdG4gDChyQnGRRM106)
_Statistiques de profilage._

![Image](https://cdn-media-1.freecodecamp.org/images/6BRhlhApuzo1KPLpXuZOO2a8I91l4cWTBw1j)
_Détails du profilage._

### Conclusion

En résumé, un système de couverture robuste utilise deux techniques distinctes pour la génération de couverture : le balayage 3D des objets et le parcours des bords du navmesh. Le premier est idéal pour les couvertures de type champ de force (boucliers statiques), tandis que le second fonctionne bien pour tout le reste (paysages, objets, etc.).

Le balayage des objets implique de découper les acteurs en grilles 3D, tandis que le parcours des bords du navmesh utilise les polygones de navmesh existants pour parcourir une zone, avec un support optionnel pour la détection de rebords.

Les deux techniques stockent les données dans des octrees, qui fournissent des facilités de recherche spatiale efficaces.

Les mises à jour dynamiques en temps réel sont activées en s'abonnant et en découplant les événements de mise à jour des tuiles de Recast.

La recherche de points de couverture en temps réel est rendue plus polyvalente en définissant des "décalages de regard" ou "d'inclinaison" pour les unités.

Vous pouvez augmenter les performances de génération de couverture en désactivant la détection de rebords, ce qui réduit le nombre de raycasts.

Vous devez prendre quelques mesures supplémentaires pour que la technique basée sur le navmesh fonctionne au mieux, comme placer des volumes de modification de nav sur la carte partout où vous avez des objets plus grands avec des navmeshes à l'intérieur. Certains paramètres de projet sont également nécessaires, par exemple des canaux d'objet personnalisés, des canaux de traçage et des collisions.

![Image](https://cdn-media-1.freecodecamp.org/images/vQXqU3lyM1bu-g5oVPOIT6qDWUIThhuorOdG)

Je suis sûr que vous en avez assez de moi maintenant, alors pourquoi ne pas télécharger le projet de démonstration et plonger dans le code source qui inclut une implémentation entièrement fonctionnelle de toutes les techniques discutées ci-dessus. Si quelque chose n'est pas clair ou si vous êtes bloqué, n'hésitez pas à me le faire savoir dans la section des commentaires ci-dessous !

[**Téléchargez le projet de démonstration et le code source.**](https://horugame.com/real-time-dynamic-cover-system-for-unreal-engine-4/)

Si vous avez aimé ce tutoriel, [**abonnez-vous à notre newsletter**](https://horugame.com/#newsletter) et soyez informé des nouveaux tutoriels et articles.
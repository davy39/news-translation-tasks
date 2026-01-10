---
title: Jouer à des jeux de stratégie avec l'algorithme Minimax
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-10T22:08:34.000Z'
originalURL: https://freecodecamp.org/news/playing-strategy-games-with-minimax-4ecb83b39b4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JEazGnr-TCr60IwXlwwpDg.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Jouer à des jeux de stratégie avec l'algorithme Minimax
seo_desc: 'By Grant Bartel

  In this lesson, we’ll explore a popular algorithm called minimax. We’ll also learn
  some of its friendly neighborhood add-on features like heuristic scores, iterative
  deepening, and alpha-beta pruning. Using these techniques, we can cr...'
---

Par Grant Bartel

Dans cette leçon, nous explorerons un algorithme populaire appelé **minimax**. Nous apprendrons également certaines de ses fonctionnalités complémentaires comme les **scores heuristiques**, **l'approfondissement itératif** et **l'élagage alpha-bêta**. En utilisant ces techniques, nous pouvons créer un agent de jeu plus flexible et puissant. Il sera capable de rivaliser dans de nombreux défis, y compris le jeu de stratégie Isolation.

Dans mon précédent article [How To Win Sudoku](https://towardsdatascience.com/how-to-win-sudoku-3a82d05a57d), nous avons appris comment enseigner aux ordinateurs à résoudre le puzzle Sudoku. Si vous ne l'avez pas lu, allez-y et donnez-lui une lecture rapide. Mais ce n'était vraiment qu'un moyen de nous familiariser avant de plonger dans des méthodes plus sophistiquées d'agents de jeu. Surtout celles qui peuvent faire des coups stratégiques contre un adversaire !

![Image](https://cdn-media-1.freecodecamp.org/images/wajB64X1fKid61TSJeJ9XREpDVgwGpJAwh2n)
_[https://boardgamegeek.com/image/784001/isolation](https://boardgamegeek.com/image/784001/isolation" rel="noopener" target="_blank" title=")_

### Ne vous retrouvez pas isolé

Isolation (ou Isola) est un jeu de stratégie tour par tour où deux joueurs tentent de confiner leur adversaire sur un plateau de 7x7 similaire à un damier. Finalement, ils ne peuvent plus faire de mouvement (d'où l'isolement).

Chaque joueur a une pièce, qu'il peut déplacer comme une reine aux échecs — haut-bas, gauche-droite et en diagonale. Il y a trois conditions sous lesquelles les pièces peuvent être déplacées —

1. Ils ne peuvent pas placer leur pièce sur une case déjà visitée.
2. Ils ne peuvent pas traverser les cases déjà visitées (se faufiler en diagonale est OK).
3. Ils ne peuvent pas traverser la pièce de l'autre joueur.

![Image](https://cdn-media-1.freecodecamp.org/images/9pqGE4lgNVqh59q3uMMeVTKZz1RLLFO7wuFP)
_[https://www.cs.umb.edu/~yunxu/isola/final.jpg](https://www.cs.umb.edu/~yunxu/isola/final.jpg" rel="noopener" target="_blank" title=")_

Dans l'image ci-dessus, vous pouvez voir à partir des carrés noirs que les deux joueurs ont placé leurs pièces sur diverses parties du plateau. Mais au fur et à mesure que le jeu progresse, il montre que le joueur jaune a encore trois mouvements possibles. En haut et à droite, une case à droite, et deux cases à droite. Mais le joueur bleu n'a plus d'options. Par conséquent, le joueur jaune est le gagnant ici.

Maintenant, cela peut sembler un jeu simple — et pour être honnête, c'est le cas. Ce n'est pas comme si nous jouions au [poker](http://www.sciencemag.org/news/2017/03/artificial-intelligence-goes-deep-beat-humans-poker) ou à [Starcraft](https://www.wired.com/story/googles-ai-declares-galactic-war-on-starcraft-/). Pourtant, il y a encore un nombre énorme de mouvements possibles que chaque joueur peut faire à tout moment pendant le jeu.

**Dans les puzzles comme Sudoku, il y a une "réponse" que nous voulons résoudre. Mais il n'y a pas de réponse lorsqu'il s'agit de jeux de stratégie.**

Nous jouons contre un autre adversaire — comme une personne, un ordinateur ou un chat [détective](http://theoatmeal.com/comics/scrambles). Cela nécessite de la stratégie et une certaine réflexion sur la façon dont le jeu peut évoluer au fur et à mesure.

De tels jeux peuvent évoluer et produire un nombre absurde de résultats possibles. Nous devons donc réfléchir à la manière de choisir le meilleur mouvement possible, sans passer le temps qu'il a fallu aux chats pour peupler la Terre.

![Image](https://cdn-media-1.freecodecamp.org/images/q3iY9-wgBQ6tjLNkru7xi7yFN5Q83rZ5Yiss)

D'accord, plus de chats !

### Le puissant Minimax et ses amis

Maintenant que vous savez comment jouer à Isolation, examinons comment nous pouvons utiliser l'algorithme **minimax** ; un pilier de la communauté de l'IA. Nous examinerons également les **scores heuristiques**, **l'approfondissement itératif** et **l'élagage alpha-bêta**. Ensemble avec ceux-ci, nous pouvons construire un agent IA compétitif.

#### Minimax

L'algorithme [minimax](https://en.wikipedia.org/wiki/Minimax) est très populaire pour enseigner aux agents IA comment jouer à des jeux de stratégie tour par tour. La raison en est qu'il prend en compte tous les mouvements possibles que les joueurs peuvent faire à tout moment pendant le jeu. Avec ces informations, il tente ensuite de minimiser l'avantage du joueur adversaire tout en maximisant celui de l'agent à chaque tour où l'agent IA a l'occasion de jouer.

Maintenant, à quoi cela ressemble-t-il ?

Eh bien, similaire à la façon dont un agent IA jouerait à un jeu comme Sudoku, nous pouvons modéliser les prochains mouvements possibles que chaque joueur peut faire via un **arbre de recherche**. Cependant, nous devrons utiliser un arbre de recherche avec des largeurs variables — ou en d'autres termes, la largeur d'un niveau d'arbre. La raison en est qu'il y a un nombre variable de mouvements que chaque joueur peut faire à tout moment pendant le jeu.

![Image](https://cdn-media-1.freecodecamp.org/images/AGGA-1CKnqliKNdm7aGYO69svaVU7CiOkoMd)
_Programme de Nanodiplôme en IA d'Udacity_

L'arbre montré ci-dessus représente les prochains mouvements disponibles pendant une partie d'Isolation. Il a une grille de 2x3, avec la case en bas à droite étant inaccessible. Comme vous pouvez le voir, les deux joueurs sont un cercle bleu et une croix rouge.

Le haut de l'arbre (le nœud racine) illustre un mouvement fait par le joueur rouge. Le niveau du milieu illustre les prochains mouvements possibles par le joueur bleu. Et le troisième niveau illustre les mouvements possibles par le joueur rouge, étant donné le mouvement précédent fait par le joueur bleu.

> Chaque état de jeu ou nœud dans l'arbre contient des informations sur quel joueur a le plus à gagner de tout mouvement potentiel.

**Maintenant, vous vous demandez peut-être, qu'est-ce que ces triangles sous chaque mouvement ?**

Le triangle vers le bas représente un emplacement dans l'arbre où minimax **minimisera** l'avantage de l'adversaire. Alors que les triangles vers le haut sont les emplacements où minimax **maximise** l'avantage de l'agent.

Mais minimax ne peut connaître l'avantage de chaque joueur que s'il connaît les chemins dans l'arbre qui mènent à une victoire pour chaque joueur. Cela signifie que minimax doit parcourir jusqu'au fond de l'arbre pour chaque série possible de mouvements. Ensuite, il doit attribuer un score (par exemple, +1 pour une victoire et -1 pour une défaite), et propager ces nombres à travers l'arbre. De cette façon, chaque état de jeu ou nœud dans l'arbre contient des informations sur quel joueur a le plus à gagner de tout mouvement potentiel.

![Image](https://cdn-media-1.freecodecamp.org/images/Vegh4XBfJe4fp5gVsqdFmG203vSCpSGd254E)
_Programme de Nanodiplôme en IA d'Udacity_

Dans cette image, nous pouvons faire quelques observations. D'abord, minimax attribue un nombre aux résultats finaux du jeu aux **nœuds feuilles**. Ensuite, il les propage vers le haut à travers l'arbre, en effectuant des minimisations et des maximisations en cours de route. Une fois que minimax a fini de remplir l'arbre, chaque fois que c'est le tour de l'agent IA, il saura quels mouvements mèneront probablement à une victoire ou à une défaite.

Le deuxième niveau après le nœud racine montre les prochains mouvements possibles pour le joueur bleu (notre agent IA). Notre agent veut maximiser les scores disponibles pendant son tour. Il choisirait donc le mouvement représenté dans le nœud le plus à droite suivant le nœud racine. Super cool !

Mais est-il logique d'attribuer simplement un +1 ou un -1 aux résultats du jeu ? Ne devrait-on pas prendre en compte comment le jeu est gagné ou perdu ?

Alerte spoiler : la réponse est oui !

#### Scores heuristiques

Dans le monde des jeux de stratégie, un score heuristique est essentiellement une valeur subjective que nous attribuons à un certain état du jeu. Cette valeur est basée sur notre compréhension de la manière dont le jeu est gagné et perdu. En choisissant un score heuristique bien pensé, nous sommes en mesure d'enseigner à notre agent IA comment mieux sélectionner ses prochains mouvements tout en jouant au jeu Isolation.

Maintenant, il y a probablement un nombre illimité de scores heuristiques que nous pourrions inventer. Mais ici, nous ne regarderons que quelques-uns d'entre eux, à part le **score naïf (NS)** de +1 et -1.

Une idée pourrait être de compter tous les prochains mouvements possibles que chaque joueur a à tout moment, puisque plus de mouvements possibles signifient moins de chances d'être isolé. Nous appellerons cela le **score de mouvement ouvert (OMS)**.

Une autre idée pourrait être d'utiliser la valeur obtenue à partir de l'OMS et de soustraire le nombre de prochains mouvements possibles que l'adversaire a. La raison en est que chaque joueur veut augmenter son nombre de mouvements tout en diminuant celui de son adversaire. Nous appellerons cela le **score amélioré (IS)**.

![Image](https://cdn-media-1.freecodecamp.org/images/V7lXXWBQzH31cFXIZV1oxFbRiz4SHmms0Hvw)

La figure ci-dessus montre les taux de victoire sur de nombreuses parties simulées d'Isolation jouées entre des agents IA utilisant différents scores heuristiques. Maintenant, vous pouvez voir à quel point nos scores ont différé pendant le jeu réel. Mais il y avait certains scores heuristiques qui ont surpassé ceux que nous avons inventés.

Intéressamment, les deux premiers sont presque exactement les mêmes que le score amélioré. Nous les appellerons **score amélioré agressif (AIS)** et **score amélioré super agressif (SAIS)**. Mais il y a une légère différence entre ces scores et l'original. Les deux premiers scores appliquent un facteur de deux et trois à la valeur que vous soustrayez (le nombre de mouvements disponibles pour l'adversaire) lors du calcul du score amélioré.

Vous pouvez découvrir un facteur "agressif" optimal à appliquer lors du calcul de ce score !

Une autre alerte spoiler — de meilleures valeurs existent.

Mais que se passe-t-il si nous inventons un score heuristique qui prend beaucoup de temps à calculer ? Que se passe-t-il si l'arbre est énorme ? Notre agent IA aura-t-il assez de temps pour trouver ses prochains meilleurs mouvements, tout en restant suffisamment réactif pendant le jeu ?

#### Approfondissement itératif

Maintenant, nous savons que notre agent IA peut modéliser tous les mouvements possibles en utilisant un arbre de recherche et le score heuristique correspondant de ses nœuds. Mais malheureusement, lorsque nous jouons à Isolation, notre arbre sera massif. Il faudrait plus de temps pour rechercher dans l'arbre et calculer ces valeurs qu'il n'y a d'années depuis le big bang !

![Image](https://cdn-media-1.freecodecamp.org/images/aBySVRQoSxm5I-E7pw7oXECgY88ostXFQtPu)

Entrez [**l'approfondissement itératif**](http://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/) — la stratégie de gestion du temps de référence pour les agents de jeu. En utilisant cette méthode, nous pouvons réduire le temps de calcul et de recherche à un temps maximum de notre choix. De cette façon, notre agent IA peut répondre au moins aussi rapidement qu'un humain.

Mais comment fonctionne l'approfondissement itératif ?

Il permet à minimax de se déplacer niveau par niveau et de calculer les scores heuristiques jusqu'à une certaine limite de temps. Une fois cette limite de temps atteinte, l'agent IA est forcé d'utiliser le meilleur mouvement qu'il a découvert tout en descendant de plus en plus profondément dans l'arbre.

![Image](https://cdn-media-1.freecodecamp.org/images/oscgGSWYXIVsggg3MxtLDDXykhXSrdI7RIxs)
_[https://chessprogramming.wikispaces.com/Iterative+Deepening/](https://chessprogramming.wikispaces.com/Iterative+Deepening/" rel="noopener" target="_blank" title=")_

Cela fournit un aperçu de la difficulté que cela peut représenter. Créer un agent IA suffisamment intelligent et réactif pour les jeux de stratégie peut être assez délicat, même pour les sorciers de l'IA. Surtout si de tels jeux contiennent un monde de possibilités.

Malheureusement, le nombre de mouvements que l'agent IA peut "imaginer" à l'avance est limité. Il est donc possible qu'il prenne une décision qui mène à sa perte. C'est un phénomène bien connu appelé l'[**effet horizon**](https://en.wikipedia.org/wiki/Horizon_effect). Mais nous devons encore examiner l'algorithme de réduction de temps arguably le plus efficace utilisé lors de la recherche dans les arbres.

#### Élagage alpha-bêta

![Image](https://cdn-media-1.freecodecamp.org/images/D5TuzHem0b2X99bb0GBWu7gZBKuVx3K0gJy4)
_[http://desperateexes.com/wp-content/uploads/2016/09/the-california-raisins.jpg](http://desperateexes.com/wp-content/uploads/2016/09/the-california-raisins.jpg" rel="noopener" target="_blank" title=")_

D'accord, ce sont des raisins secs et non des pruneaux, mais quand même — comment cela a-t-il pu être une chose ? Je veux dire, sérieusement, un groupe de blues de raisins secs ?

Vous avez peut-être déjà deviné que l'[élagage alpha-bêta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) n'a rien à voir avec les pruneaux, et plus à voir avec la réduction de la taille (élagage) de notre arbre de recherche. Lorsque nous avons un très grand arbre de recherche, il s'avère qu'il n'est pas toujours nécessaire de parcourir chaque nœud lors de l'utilisation de minimax.

**Nous devons donner à minimax la capacité d'arrêter de rechercher une région particulière de l'arbre lorsqu'il trouve le minimum ou le maximum garanti de ce niveau particulier.**

Si nous pouvons faire cela, cela peut grandement réduire le temps de réponse de notre agent IA et améliorer les performances.

**Comment fonctionne l'élagage alpha-bêta ?**

L'algorithme minimax se déplace dans l'arbre en utilisant la [recherche en profondeur d'abord](https://en.wikipedia.org/wiki/Depth-first_search). Cela signifie qu'il parcourt l'arbre de gauche à droite, et va toujours le plus profond possible. Il découvre ensuite les valeurs qui doivent être attribuées aux nœuds directement au-dessus, sans jamais regarder les autres branches de l'arbre.

**L'élagage alpha-bêta permet à minimax de prendre des décisions aussi bonnes que celles que minimax pourrait prendre seul, mais avec un niveau de performance plus élevé.**

Considérez l'image suivante, dans laquelle nous avons un arbre avec divers scores attribués à chaque nœud. Certains nœuds sont ombrés en rouge, indiquant qu'il n'est pas nécessaire de les examiner.

![Image](https://cdn-media-1.freecodecamp.org/images/YvMTXyxnOdhUmf5OBuSlfH0gA0-SUDSCeQDK)
_[https://en.wikipedia.org/wiki/Alpha-beta_pruning](https://en.wikipedia.org/wiki/Alpha-beta_pruning" rel="noopener" target="_blank" title=")_

En bas à gauche de l'arbre, minimax regarde les valeurs 5 et 6 au niveau max du bas. Il détermine que 5 doit être attribué au niveau min juste au-dessus. Cela a du sens.

Mais, après avoir regardé 7 et 4 de la branche du niveau max de droite, il réalise que le nœud du niveau min ci-dessus doit se voir attribuer une valeur maximale de 4. Puisque le deuxième niveau max juste au-dessus du premier niveau min prendra le maximum entre 5 et au plus 4, il est clair qu'il choisira 5. Ensuite, il continuerait à parcourir l'arbre pour effectuer le même ensemble exact d'opérations dans les autres branches de l'arbre.

Ci-dessous se trouve la représentation algorithmique de minimax avec l'élagage alpha-bêta.

![Image](https://cdn-media-1.freecodecamp.org/images/7jl7qin7LiPOyWwmRo2JDiDUph6SZRBwhs0E)
_Programme de Nanodiplôme en IA d'Udacity_

L'utilisation de cette méthode fournit un moyen facile de réduire l'espace de recherche de notre agent IA. De cette façon, l'élagage alpha-bêta permet à minimax de prendre de bonnes décisions que minimax pourrait faire seul, mais avec un niveau de performance plus élevé.

### Isola-ter

Nous avons exploré comment construire notre propre agent IA capable de jouer au jeu Isolation à un niveau assez compétitif. En utilisant l'algorithme minimax, nous avons vu comment l'agent IA peut modéliser le jeu et prendre des décisions basées sur un score heuristique. Nous avons également appris à déterminer une heuristique bien définie pour notre tâche donnée (Isolation).

Mais nous avons également découvert qu'il serait beaucoup trop intensif en calcul de laisser minimax fonctionner sans contrôle. Nous avons donc dû utiliser des techniques comme l'approfondissement itératif et l'élagage alpha-bêta. Celles-ci forceront notre agent IA à trouver le prochain mouvement dans un délai raisonnable. Mais que se passe-t-il si nous voulons que notre agent IA ait un taux de victoire plus élevé tout en étant au moins aussi réactif qu'un humain ?

Eh bien, il existe d'autres techniques que nous pourrions explorer pour augmenter le taux de victoire de notre agent ainsi que son temps de réponse. Nous avons effleuré l'idée de régler les paramètres de notre score heuristique (vous souvenez-vous du "facteur agressif" ?). Nous pourrions même inventer un score heuristique mieux adapté pour jouer à Isolation.

Il existe également des propriétés réfléchissantes liées aux mouvements possibles sur le plateau d'Isolation. Celles-ci deviennent évidentes lorsque nous analysons l'arbre de recherche entièrement peuplé, ce qui nous permettrait de supprimer potentiellement de nombreuses branches de l'arbre de recherche. De plus, si nous améliorions notre matériel, notre agent IA serait plus rapide — et pourrait ainsi explorer plus de possibilités.

Si vous souhaitez entrer dans les détails de la mise en œuvre de cela vous-même, jetez un coup d'œil au code que j'ai écrit pour résoudre ce problème pour mon [Nanodiplôme en Intelligence Artificielle d'Udacity](https://www.udacity.com/course/artificial-intelligence-nanodegree--nd889). Vous pouvez le trouver sur [mon dépôt GitHub](https://github.com/grantathon/AIND-Isolation).

_Je suis Grant et je suis un professionnel indépendant du SEO et du contenu. Si vous cherchez à augmenter le trafic de recherche organique de votre marque, je peux vous aider avec votre [SEO fintech](https://www.writefintech.com/). Santé !_
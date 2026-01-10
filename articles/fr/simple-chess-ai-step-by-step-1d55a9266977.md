---
title: Un guide étape par étape pour créer une IA d'échecs simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-30T19:26:08.000Z'
originalURL: https://freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eP0V-xfRWfW3QHJhALJ5RA.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chess
  slug: chess
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Un guide étape par étape pour créer une IA d'échecs simple
seo_desc: 'By Lauri Hartikka

  Let’s explore some basic concepts that will help us create a simple chess AI:


  move-generation

  board evaluation

  minimax

  and alpha beta pruning.


  At each step, we’ll improve our algorithm with one of these time-tested chess-programmi...'
---

Par Lauri Hartikka

Explorons quelques concepts de base qui nous aideront à créer une IA d'échecs simple :

* génération de mouvements
* évaluation de la position
* minimax
* et l'élagage alpha-bêta.

À chaque étape, nous améliorerons notre algorithme avec l'une de ces techniques éprouvées de programmation d'échecs. Je montrerai comment chacune affecte le style de jeu de l'algorithme.

Vous pouvez consulter l'algorithme final de l'IA ici sur [GitHub](https://github.com/lhartikk/simple-chess-ai).

### Étape 1 : Génération de mouvements et visualisation de l'échiquier

Nous utiliserons la bibliothèque [chess.js](https://github.com/jhlywa/chess.js) pour la génération de mouvements, et [chessboard.js](https://github.com/oakmac/chessboardjs/) pour visualiser l'échiquier. La bibliothèque de génération de mouvements implémente essentiellement toutes les règles des échecs. Sur cette base, nous pouvons calculer tous les mouvements légaux pour un état donné de l'échiquier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_Z_qtrm9ayf_UhycYudE3g.png)
_Une visualisation de la fonction de génération de mouvements. La position de départ est utilisée comme entrée et la sortie est tous les mouvements possibles à partir de cette position._

L'utilisation de ces bibliothèques nous aidera à nous concentrer uniquement sur la tâche la plus intéressante : créer l'algorithme qui trouve le meilleur mouvement.

Nous commencerons par créer une fonction qui retourne simplement un mouvement aléatoire parmi tous les mouvements possibles :

Bien que cet algorithme ne soit pas un joueur d'échecs très solide, c'est un bon point de départ, car nous pouvons effectivement jouer contre lui :

![Image](https://cdn-media-1.freecodecamp.org/images/1*GzOiJRh6Z3FOC3xmPEmKrQ.gif)
_Les noirs jouent des mouvements aléatoires. Jouable sur [https://jsfiddle.net/lhartikk/m14epfwb/](https://jsfiddle.net/lhartikk/m14epfwb/" rel="noopener" target="_blank" title=")4_

### Étape 2 : Évaluation de la position

Essayons maintenant de comprendre quel côté est le plus fort dans une certaine position. La manière la plus simple d'y parvenir est de compter la force relative des pièces sur l'échiquier en utilisant le tableau suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*e4p9BrCzJUdlqx7KVGW9aA.png)

Avec la fonction d'évaluation, nous sommes en mesure de créer un algorithme qui choisit le mouvement qui donne l'évaluation la plus élevée :

La seule amélioration tangible est que notre algorithme capturera maintenant une pièce s'il le peut.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fTWDdJ2m3L72X6rqce9_tQ.gif)
_Les noirs jouent avec l'aide de la fonction d'évaluation simple. Jouable sur [https://jsfiddle.net/lhartikk/m5q6fgtb/1/](https://jsfiddle.net/lhartikk/m5q6fgtb/1/" rel="noopener" target="_blank" title=")_

### Étape 3 : Arbre de recherche utilisant Minimax

Ensuite, nous allons créer un arbre de recherche à partir duquel l'algorithme peut choisir le meilleur mouvement. Cela est fait en utilisant l'algorithme [Minimax](https://en.wikipedia.org/wiki/Minimax).

Dans cet algorithme, l'arbre récursif de tous les mouvements possibles est exploré jusqu'à une profondeur donnée, et la position est évaluée aux "feuilles" de l'arbre.

Après cela, nous retournons soit la plus petite soit la plus grande valeur de l'enfant au nœud parent, selon qu'il s'agit des blancs ou des noirs de jouer. (C'est-à-dire que nous essayons soit de minimiser soit de maximiser le résultat à chaque niveau.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UA5VlNs7s4gl80VknA099w.jpeg)
_Une visualisation de l'algorithme minimax dans une position artificielle. Le meilleur mouvement pour les blancs est **b2-c3**, car nous pouvons garantir que nous pouvons atteindre une position où l'évaluation est **-50**_

Avec minimax en place, notre algorithme commence à comprendre certaines tactiques de base des échecs :

![Image](https://cdn-media-1.freecodecamp.org/images/1*xRfitY19MvJW3ynGKWhQ5A.gif)
_Minimax avec un niveau de profondeur de 2. Jouable sur : [https://jsfiddle.net/k96eoq0q/1/](https://jsfiddle.net/k96eoq0q/1/" rel="noopener" target="_blank" title=")_

L'efficacité de l'algorithme minimax dépend fortement de la profondeur de recherche que nous pouvons atteindre. C'est quelque chose que nous améliorerons dans l'étape suivante.

### Étape 4 : Élagage alpha-bêta

L'[élagage alpha-bêta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) est une méthode d'optimisation de l'algorithme minimax qui nous permet de négliger certaines branches dans l'arbre de recherche. Cela nous aide à évaluer l'arbre de recherche minimax beaucoup plus profondément, tout en utilisant les mêmes ressources.

L'élagage alpha-bêta est basé sur la situation où nous pouvons arrêter d'évaluer une partie de l'arbre de recherche si nous trouvons un mouvement qui conduit à une situation pire qu'un mouvement précédemment découvert.

L'élagage alpha-bêta n'influence pas le résultat de l'algorithme minimax — il le rend simplement plus rapide.

L'algorithme alpha-bêta est également plus efficace si nous visitons **d'abord** les chemins qui mènent à de bons mouvements.

![Image](https://cdn-media-1.freecodecamp.org/images/1*96QEzhnsOkNqz7swB0qx8w.jpeg)
_Les positions que nous n'avons pas besoin d'explorer si l'élagage alpha-bêta est utilisé et que l'arbre est visité dans l'ordre décrit._

Avec l'élagage alpha-bêta, nous obtenons un gain significatif pour l'algorithme minimax, comme le montre l'exemple suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*k3DrkWLNq33ei_t-094qpg.png)
_Le nombre de positions qui doivent être évaluées si nous voulons effectuer une recherche avec une profondeur de 4 et la position "racine" est celle qui est montrée._

Suivez [ce lien](https://jsfiddle.net/Laa0p1mh/3/) pour essayer la version améliorée avec alpha-bêta de l'IA d'échecs.

### Étape 5 : Fonction d'évaluation améliorée

La fonction d'évaluation initiale est assez naïve car nous ne comptons que le matériel qui se trouve sur l'échiquier. Pour l'améliorer, nous ajoutons à l'évaluation un facteur qui prend en compte la position des pièces. Par exemple, un cavalier au centre de l'échiquier est meilleur (car il a plus d'options et est donc plus actif) qu'un cavalier sur le bord de l'échiquier.

Nous utiliserons une version légèrement ajustée des tables de valeurs de pièces qui sont initialement décrites dans le [chess-programming-wiki](https://chessprogramming.wikispaces.com/Simplified+evaluation+function).

![Image](https://cdn-media-1.freecodecamp.org/images/1*iG6FUYZpU0_RKlqHnC8XxA.png)
_Les tables de valeurs de pièces visualisées. Nous pouvons diminuer ou augmenter l'évaluation, selon l'emplacement de la pièce._

Avec l'amélioration suivante, nous commençons à obtenir un algorithme qui joue aux échecs de manière "décente", au moins du point de vue d'un joueur occasionnel :

![Image](https://cdn-media-1.freecodecamp.org/images/1*sX_XwfPrOQ6c62iuVZ75fw.gif)
_Évaluation améliorée et élagage alpha-bêta avec une profondeur de recherche de 3. Jouable sur [https://jsfiddle.net/q76uzxwe/1/](https://jsfiddle.net/q76uzxwe/1/" rel="noopener" target="_blank" title=")_

### Conclusions

La force d'un algorithme de jeu d'échecs, même simple, est qu'il ne commet pas d'erreurs stupides. Cela dit, il manque toujours de compréhension stratégique.

Avec les méthodes que j'ai introduites ici, nous avons été en mesure de programmer un algorithme de jeu d'échecs qui peut jouer aux échecs de base. La partie "IA" (génération de mouvements exclue) de l'algorithme final ne fait que 200 lignes de code, ce qui signifie que les concepts de base sont assez simples à implémenter. Vous pouvez consulter la version finale sur [GitHub](https://github.com/lhartikk/simple-chess-ai).

Certaines améliorations supplémentaires que nous pourrions apporter à l'algorithme seraient par exemple :

* [l'ordre des mouvements](https://chessprogramming.wikispaces.com/Move+Ordering)
* une génération de mouvements plus rapide
* et une évaluation spécifique pour la [fin de partie](https://chessprogramming.wikispaces.com/Endgame).

Si vous voulez en savoir plus, consultez le [chess programming wiki](https://chessprogramming.wikispaces.com/). C'est une ressource utile pour explorer au-delà de ces concepts de base que j'ai introduits ici.

Merci d'avoir lu !
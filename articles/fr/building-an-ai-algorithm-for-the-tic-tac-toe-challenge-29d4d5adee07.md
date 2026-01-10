---
title: Construire un algorithme d'IA pour le défi du Morpion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-08T16:57:27.000Z'
originalURL: https://freecodecamp.org/news/building-an-ai-algorithm-for-the-tic-tac-toe-challenge-29d4d5adee07
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tTQJFNpKFOOiH8dN_2tyEQ.png
tags:
- name: AI
  slug: ai
- name: algorithms
  slug: algorithms
- name: Games
  slug: games
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: Construire un algorithme d'IA pour le défi du Morpion
seo_desc: 'By Ben Carp

  As part of the freeCodeCamp curriculum, I was challenged build a Tic-Tac-Toe web
  app. It was a real pleasure.

  The app includes an ultimate computer player. It can optimize any given situation
  on the Tic-Tac-Toe board. The outcome surprise...'
---

Par Ben Carp

Dans le cadre du programme [freeCodeCamp](https://www.freecodecamp.org/), j'ai été défié de créer une application web de [Morpion](https://en.wikipedia.org/wiki/Tic-tac-toe). Ce fut un vrai plaisir.

L'application inclut un joueur informatique ultime. Il peut optimiser n'importe quelle situation sur le plateau de Morpion. Le résultat m'a surpris.

Même dans un jeu aussi simple, le joueur informatique m'a appris de nouveaux coups. Quant au code que j'ai écrit, il est quelque peu unique et intéressant à explorer.

### Essayez-le

Visitez [ce lien](https://carpben.github.io/TicTacToe/) et choisissez de jouer contre l'ordinateur. **Je vous défie de gagner**. Vous pourriez trouver… que vous ne pouvez pas.

Pourtant, si vous êtes solide en défense, vous pourriez découvrir que l'ordinateur n'est pas non plus capable de gagner. J'ai appris par expérience que le Morpion a une stratégie simple de **non-défaite**.

Cela signifie que si vous parvenez à faire match nul, vous faites les bons choix défensifs. L'ordinateur optimise toujours ses coups. Ainsi, le meilleur résultat qu'il peut obtenir contre un joueur comme vous pourrait n'être qu'un match nul.

### Étapes principales de la solution

### 1. Structure de données du plateau

```
_gameBoard: [["", "", ""], ["", "", ""], ["", "", ""]]
```

Le tableau du plateau contient 3 tableaux, chacun représentant une ligne. Chaque tableau de ligne contient 3 éléments de caractère ou de chaîne.

Ces éléments sont soit :

* "" comme une chaîne vide, représentant une cellule vide
* "X" représentant le joueur X
* "O" représentant le joueur O

### 2. Fonction getResult

[Commence à la ligne 59](https://github.com/carpben/TicTacToe/blob/ea8a67918f0ab97bca40e4383839e95695da803f/tictactoe.js#L59)

À tout état donné, le plateau sera dans l'un et un seul de ces états possibles :

* Incomplet
* Le joueur X a gagné
* Le joueur O a gagné
* Ou un match nul

La fonction `getResult` reçoit un tableau de plateau, itère sur toutes les lignes, à travers toutes les colonnes et les deux diagonales. Elle vérifie la succession des symboles. Ensuite, elle nous informe de l'état actuel de ce plateau.

### 3. Fonction getBestMove

Ici, cela devient plus difficile. Lorsque le plateau est vide, il est très difficile d'identifier le meilleur coup possible. Jetez un œil à ce plateau.

![Image](https://cdn-media-1.freecodecamp.org/images/3okj6K22mhQqi0VJoAwKW23J0AZY9xKkQySi)

Quel est le meilleur coup possible ?

![Image](https://cdn-media-1.freecodecamp.org/images/xu9JhJ-N68f882smavEXgfBywu-IQfq2WCol)

Lorsque le plateau se remplit, le meilleur coup possible saute aux yeux.

![Image](https://cdn-media-1.freecodecamp.org/images/LHO7ANdiMFvs6tqGSSyiHl6STARjTp2FV-Xx)

Utilisons ce plateau rempli comme point de départ. Décidons que le prochain coup est le nôtre, et que notre symbole est un "X".

Essayons d'identifier le meilleur coup possible avec les outils que nous avons déjà. Il y a 3 cellules vides qui correspondent à 3 coups possibles. Vérifions le résultat pour chacune de ces options.

Nous pouvons faire cela en itérant sur les coups possibles, et pour chacun d'eux :

* Créer un nouveau plateau
* Ajouter notre symbole à la cellule vide correspondante
* Envoyer ce plateau à la fonction `getResult`

![Image](https://cdn-media-1.freecodecamp.org/images/VaQNTkO611PiBnEONSqdd5--gPfziHmB1iYq)
_**Coup 1**_

![Image](https://cdn-media-1.freecodecamp.org/images/rUDb6QBuLy-uXD8KZRnDHV4fwpvOnwubd7nv)
_**Coup 2**_

![Image](https://cdn-media-1.freecodecamp.org/images/4uTqBhc4Pqs7crCWRHYimAAI1Uz12aLRpRO8)
_**Coup 3**_

Parmi les 3 plateaux de la figure ci-dessus, lorsque nous envoyons le deuxième plateau à la fonction `getResult`, nous recevrons notre trophée.

Veuillez vous concentrer pour les prochaines étapes essentielles :

1. Nous devons noter les coups possibles afin de pouvoir les comparer. Décidons que si un coup donne un plateau gagnant, nous le noterons 1. S'il donne un plateau perdant, il recevra la note de -1. Un match nul recevra une note de 0.
2. Le coup 2 recevra une note de 1. Lorsque nous trouvons un coup noté 1, nous pouvons ignorer tous les autres coups possibles. Il n'y a pas de meilleur coup possible qu'une victoire certaine.
3. Mais pour comprendre, comment noterions-nous les coups 1 ou 3, ou tout autre coup avec un résultat incomplet ?

Concentrons-nous sur le coup 3. La solution est d'envoyer le plateau correspondant de manière récursive à la fonction `getBestMove`.

Vous pourriez penser, "Mais attendez ! Notre adversaire joue le prochain coup." C'est exact. Découvrons quelle note notre adversaire obtient pour son meilleur coup futur.

Notre adversaire n'a que deux coups possibles :

![Image](https://cdn-media-1.freecodecamp.org/images/4VXz6eihd2q6j8VGWkyXUEDuveO3dyYAdTTj)
_**Coup 3-1**_

![Image](https://cdn-media-1.freecodecamp.org/images/vCTQa3YBtWcnsJTt35ccsE0JqUGdcwcYEV5d)
_**Coup 3-2**_

Le coup 3-1 gagnera la partie en faveur de notre adversaire. Puisque nous utilisons la même fonction `getBestMove`, le coup 3-1 recevra une note de 1.

Cela pourrait être un peu confus car notre victoire et notre défaite recevront toutes deux des notes de 1. Nous devons nous rappeler que cet appel de fonction appartient à notre adversaire, et sa victoire est notre défaite et vice versa.

Nous devons nier toute note retournée à la fonction `getBestMove` par la fonction `getBestMove`.

Le coup 3-1 reçoit une note de 1. La fonction `getBestMove` retourne une note de 1, et nous pouvons noter le coup 3 avec un -1.

![Image](https://cdn-media-1.freecodecamp.org/images/1aKK0EZA8un2I2t8eWiqqibrzz0U69nADWXk)

De cette manière, la fonction `getBestMove` continue à explorer les coups et les coups consécutifs. Ce processus se poursuivra jusqu'à ce que :

1. Il trouve un coup noté 1, auquel cas il retournera le coup immédiatement
2. Il continuera jusqu'à ce que chaque coup possible ait une note. Les coups possibles (avec des notes de 0 et -1) sont stockés dans un tableau
3. Le tableau sera alors :
   [a] randomisé
   [b] trié du plus haut au plus bas
   [c] le premier élément sera retourné

Ces étapes garantissent que :

1. Un coup perdant sera évité sauf s'il est la seule option
2. Le joueur informatique peut jouer de manière variée

#### Notes finales :

1. Il existe des préoccupations légitimes concernant les [risques](https://en.wikipedia.org/wiki/Friendly_artificial_intelligence) que l'intelligence artificielle (IA) apporte avec elle.
   Utilisons l'IA pour le bénéfice de tous.
   Le meilleur logiciel d'IA possible est celui qui peut nous empêcher de mal utiliser l'IA.
2. J'ai consulté [Assaf Weinberg](https://twitter.com/assafweinberg?lang=en) lors du processus d'écriture de l'application

Voir [mon code](https://github.com/carpben/TicTacToe/blob/master/tictactoe.js) sur GitHub.
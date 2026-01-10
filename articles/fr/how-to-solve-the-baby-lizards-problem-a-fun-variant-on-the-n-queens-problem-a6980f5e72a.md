---
title: Comment résoudre le problème des Bébés Lézards — une variante amusante du problème
  des N-Reines
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-19T05:56:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-the-baby-lizards-problem-a-fun-variant-on-the-n-queens-problem-a6980f5e72a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3i2Y2ipYM-aQ_0VSeQ9eoQ.png
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Comment résoudre le problème des Bébés Lézards — une variante amusante
  du problème des N-Reines
seo_desc: 'By Sachin Malhotra

  This problem statement was an assignment as a part of my coursework for the Masters
  program at USC. I had loads of fun while solving it and I decided to share my learnings
  with the community.

  Let’s start with the problem statement....'
---

Par Sachin Malhotra

Cet énoncé de problème était un devoir dans le cadre de mon travail de cours pour le programme de Master à l'USC. J'ai pris beaucoup de plaisir à le résoudre et j'ai décidé de partager mes apprentissages avec la communauté.

Commençons par l'énoncé du problème.

### Le Problème

Vous êtes un soigneur dans la maison des reptiles. L'un de vos lézards rares vient d'avoir plusieurs bébés. Votre travail est de trouver une place pour chaque bébé lézard dans une nurserie. Cependant, il y a un hic : les bébés lézards ont des langues très longues.

Un bébé lézard peut sortir sa langue et manger n'importe quel autre bébé lézard avant que vous n'ayez le temps de le sauver. Ainsi, vous voulez vous assurer qu'aucun bébé lézard ne peut manger un autre bébé lézard dans la nurserie (burp).

Pour chaque bébé lézard, vous pouvez le placer à un endroit sur une grille. **De là, ils peuvent sortir leur langue vers le haut, le bas, la gauche, la droite et en diagonale également.** Leurs langues sont très longues et peuvent atteindre le bord de la nurserie depuis n'importe quel emplacement.

La figure 1 montre de quelles manières un bébé lézard peut en manger un autre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_iiDKlitAjMADtVqlQyapA.png)
_Figure 1 (A) le bébé lézard peut attaquer n'importe quel autre lézard dans un carré rouge. Ainsi, on peut voir qu'un bébé lézard peut manger un autre lézard au-dessus, en dessous, à gauche, à droite ou en diagonale. (B) Dans cet exemple de configuration, les deux lézards peuvent se manger mutuellement. Votre algorithme essaiera d'éviter cela._

En plus des bébés lézards, votre nurserie peut avoir quelques arbres plantés. Vos lézards ne peuvent pas sortir leur langue à travers les arbres, et vous ne pouvez pas déplacer un lézard à l'emplacement d'un arbre.

Ainsi, un arbre bloquera tout lézard de manger un autre lézard s'il est sur le chemin. De plus, l'arbre vous empêchera de déplacer le lézard à cet emplacement.

La figure 2 montre quelques dispositions valides différentes de lézards :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FBI0AkIOTLeN2EASiZ25Zw.png)
_Figure 2 Les deux nurseries ont des dispositions valides de bébés lézards de sorte qu'ils ne peuvent pas se manger les uns les autres. (A) sans arbres, aucun lézard n'est en position d'en manger un autre. (B) Deux arbres sont introduits de sorte que le lézard dans la dernière colonne ne peut pas manger le lézard dans la deuxième ou la quatrième colonne._

Étant donné une disposition d'arbres, nous devons produire une nouvelle disposition de lézards de sorte qu'aucun bébé lézard ne puisse en manger un autre. Vous ne pouvez pas déplacer aucun des arbres.

Vous pouvez trouver l'ensemble du code pour cela [ici](https://github.com/edorado93/Save-The-Lizards).

### Similarité avec N-Reines

Ce problème est très similaire au classique [Problème des N-Reines](https://en.wikipedia.org/wiki/Eight_queens_puzzle). Récapitulons certaines des contraintes du problème des N-Reines.

* Il ne peut y avoir qu'une seule reine par ligne et par colonne.
* Il ne peut y avoir qu'une seule reine par diagonale et anti-diagonale.
* En considérant les 2 contraintes ci-dessus, nous ne pouvons pas placer plus de reines que le nombre de lignes ou le nombre de colonnes.

Maintenant, nous ajoutons une petite variante qui dit que nous avons des arbres à certains endroits dans la nurserie (lisez échiquier), et les reines (lézards) de chaque côté d'un arbre ne peuvent pas s'attaquer mutuellement. Cela change beaucoup de choses.

* Maintenant, nous pouvons avoir plusieurs lézards par ligne, par colonne.
* De même, nous pouvons avoir plusieurs lézards dans une seule diagonale ou anti-diagonale.
* Nous pouvons placer plus de lézards que le nombre de lignes ou de colonnes.

Bien que le problème semble très similaire au puzzle standard de placement de N reines sur un échiquier N*N, la solution et la complexité s'avèrent très différentes.

Aucune des versions optimisées des N-Reines ne s'applique directement à ce problème, car beaucoup des optimisations reposent sur le fait simple qu'une solution au problème des N-Reines peut être représentée comme une permutation des indices de colonnes, simplement parce que nous n'avons qu'un seul lézard par ligne, colonne, diagonale et anti-diagonale. Nous brisons cette hypothèse, et les optimisations s'effondrent.

Ainsi, dans cet article, nous allons discuter d'une solution très optimisée basée sur le backtracking.

### Backtracking++

La solution de backtracking pour ce problème fonctionne de manière similaire à la solution de backtracking pour le problème standard des N-Reines.

La solution pour ce problème est basée sur l'idée suivante.

Étant donné une cellule `[i, j]`, nous pouvons soit placer un lézard, soit ne pas placer de lézard. L'un de nos choix peut mener à une solution. Nous essayons donc les deux.

Le plus grand invariant dans cet algorithme est que nous nous déplaçons toujours de gauche à droite sur le plateau.

Supposons qu'il y a un arbre à l'emplacement [3,4]. Son effet de masquage (le cas échéant) ne sera visible qu'une fois que nous aurons dépassé la cellule [3,4] dans notre récursion et que nous avancerons. Pas avant cela.

Avant d'arriver au pseudocode réel du problème, il y a quelques autres composants de l'algorithme que je voudrais expliquer. Cela rendra la compréhension du pseudocode beaucoup plus simple.

### La Vérification de Sécurité et le Conundrum O(1)

Si vous avez jeté un coup d'œil à [mon article précédent](https://medium.freecodecamp.org/lets-backtrack-and-save-some-queens-1f9ef6af5415) qui discute des différentes solutions algorithmiques au puzzle des N-Reines, vous comprendrez peut-être quel est le vrai problème.

Nous obtenons une amélioration de vitesse d'environ 5X sur un échiquier de 14 * 14 où nous devons placer 14 reines, après avoir converti la fonction de vérification de sécurité en O(1) au lieu de O(N). Il valait donc la peine de passer du temps à trouver un algorithme qui nous dirait en temps constant s'il est sûr de placer une reine sur une cellule donnée [i, j].

Pour référence, voyons comment nous l'avons fait dans le cas des N-Reines normales.

Nous avons utilisé certaines structures de données supplémentaires pour nous dire si une reine avait été placée dans une certaine diagonale, anti-diagonale, ligne ou colonne en temps O(1) et en utilisant celles-ci, nous pouvions dire s'il était sûr de placer une reine sur une cellule donnée [i, j].

Cependant, si vous avez lu attentivement l'énoncé du problème, nous pouvons maintenant avoir des arbres à certains endroits sur le plateau et s'il y a un arbre entre la cellule actuelle et un lézard attaquant (il peut être sur une ligne, une colonne, ou l'une des deux diagonales), alors il est en fait sûr de placer un lézard sur la cellule actuelle. Cela est dû au fait que l'arbre masque l'attaque, rendant la cellule sûre pour un nouveau lézard.

Cela change beaucoup de choses, n'est-ce pas ?.

Commençons par les structures de données dont nous avons besoin pour l'implémentation.

### Les Structures de Données Utilisées

Passons-les en revue une par une.

* `tree_locations` — il s'agit simplement d'un dictionnaire qui nous indique si une cellule donnée [i, j] contient un arbre. Cela est rempli dès le début de notre solveur.
* Les quatre structures de données rows, columns, diagonals et anti-diagonals sont utilisées pour nous indiquer simplement s'il y a un lézard dans les `r, c, r — c, r + c` respectifs. Pour ce problème, cependant, elles représentent des valeurs entières plutôt que des booléens. 
Ces quatre structures de données stockent soit 1 soit -1 selon que nous plaçons un lézard à une cellule actuelle [i, j] ou que nous rencontrons un arbre à une cellule donnée [i, j].   
Ainsi, la récursion passe d'une cellule à une autre et peut soit rencontrer un arbre à une cellule donnée [i, j], soit rencontrer une cellule vide dans laquelle nous devons appeler la fonction `is_cell_safe` pour vérifier si nous pouvons placer un lézard.  
Je reviendrai plus tard sur la manière dont les valeurs sont mises à jour dans ces quatre structures de données, à savoir `rows`, `columns`, `diagonals` et `anti-diagonals`.
* `is_there_queen_in_this_column` — il s'agit d'un dictionnaire qui stocke simplement le nombre de lézards que nous avons placés dans une colonne donnée. Cela est utilisé dans le cadre d'une heuristique d'élagage employée pour réduire la taille de l'espace de recherche.
* `next_position_same_column` — cela nous indique pour chaque [i, j] quel est le prochain emplacement dans la même colonne où nous pourrions essayer de placer un nouveau lézard. Dans le problème normal des N-Reines, nous ne pouvons placer qu'une seule reine dans une colonne, mais dans ce cas, nous pouvons avoir plusieurs reines (lézards).   
Ainsi, après avoir placé un lézard à la cellule [i, j], nous avons besoin de l'emplacement du premier arbre dans la même colonne et disons que c'est [k, j]. Le prochain emplacement disponible pour placer un lézard dans cette colonne serait alors [k+1, j]. Ce tableau est utilisé dans le cadre de cette optimisation.
* Enfin, `is_there_a_tree_ahead` est un dictionnaire qui nous indique s'il y a un arbre quelque part sur le plateau après cette colonne (y compris cette colonne également). Cela est également rempli une fois dans le cadre du prétraitement initial. Cela est également utilisé dans le cadre de l'heuristique d'élagage mentionnée ci-dessus lors de la description de `is_there_queen_in_this_column`.

### La Fonction de Prétraitement

La fonction de prétraitement est appelée initialement avant que notre algorithme ne commence son exécution et tout ce qu'elle fait est de remplir certaines des structures de données discutées ci-dessus.

* La fonction `trees_populator` est assez simple. Elle remplit les dictionnaires `tree_locations` et `is_there_a_tree_ahead`.
* La fonction `find_next_largest` considère chaque colonne comme composée de 0 et de 2, où un 0 représente une cellule vide et un 2 représente un arbre. Pour chaque cellule, elle trouve le prochain élément le plus grand ou, en d'autres termes, l'arbre le plus proche de cet emplacement dans cette colonne. Nous appelons la fonction `find_next_largest` pour chaque colonne sur le plateau.

Pour une meilleure compréhension de cet algorithme, consultez [cet aperçu](http://www.geeksforgeeks.org/next-greater-element/).

### Fonction `is_cell_safe`

Une valeur positive dans l'un des dictionnaires `row`, `column`, `diagonal`, `anti-diagonal` signifie qu'il y a un lézard qui attaquerait potentiellement un autre lézard que nous essayons de placer à [row, column].

Cette fonction ressemble beaucoup à celle que nous avons utilisée pour les N-Reines normales. La partie importante est la manière dont nous mettons à jour les valeurs dans ces structures de données.

### Marquer Visité, Démarquer Visité et Hash Util

La fonction `hash_util` est une fonction commune utilisée pour mettre à jour les valeurs pour les quatre structures de données (à savoir `rows`, `columns`, `diagonals` et `anti-diagonals`).

Cette fonction est appelée à la fois lorsque nous marquons un lézard ou un arbre, ou lorsque nous démarquons l'un ou l'autre. Le marquage et le démarquage sont simplement des traitements avant un appel récursif et l'annulation de ce que nous avons traité, après la fin de l'appel récursif.

Rappelez-vous l'invariant discuté dans ce problème : nous nous déplaçons de gauche à droite sur le plateau. Une fois que nous avons rencontré un arbre à un certain emplacement (i, j) pendant la récursion, il protégera les lézards les uns des autres pour toutes les cellules [i+1, j] et toutes les colonnes k > j.

La variable `result` est très importante ici. Par exemple, nous avons rencontré un arbre à [3,0] et il y avait un lézard à [1,0]. Maintenant, en avançant, cet arbre masque l'effet du lézard à [1,0] — au moins pour cette colonne — et nous devons prendre en compte cet effet quelque part.

Ainsi, dans ce cas :

* `is_marking` = `True`,
* `is_tree` = `True`,
* `dictionary` = `column`,
* `dictionary[col]` > 0 (Nous stockons 1 chaque fois que nous plaçons un lézard dans cette colonne). Cela est dû au fait que nous avons déjà placé un lézard dans la colonne 0 (à 1,0) et qu'il n'y avait pas d'arbre découvert précédemment qui masquerait l'effet du lézard pour la cellule [3,0] dans notre exemple.
* `value_to_add` = -1 (Pour un arbre, c'est -1, pour un lézard, c'est 1)

Ainsi, maintenant, `dictionary[col]` = -1 et nous retournons 1 comme résultat, ce qui signifie que rencontrer un arbre dans la (ligne, colonne) donnée a en fait eu un certain effet de masquage. Nous devons enregistrer cet effet de masquage car cela serait utilisé au moment de l'annulation après la récursion.

Considérons maintenant deux autres fonctions qui forment le principal composant de l'algorithme.

#### Marquer Visité

Nous appelons cette fonction dans deux cas. L'un est lorsque nous rencontrons un arbre, et l'autre est lorsque nous voulons placer un lézard. Ainsi, nous avons utilisé une variable booléenne pour nous indiquer pourquoi cette fonction a été appelée.

Dans le cas d'un arbre, nous définissons la valeur à -1, sinon c'est +1. Ensuite, nous mettons à jour les quatre structures de données. La logique est la même pour les quatre. Seule la clé change pour chacune.

Rappelez-vous, `row — col` est utilisé pour identifier de manière unique une diagonale et `row + col` est utilisé pour identifier de manière unique une anti-diagonale.

Notez également que nous stockons le quadruple des valeurs de retour pour les quatre structures de données dans le dictionnaire `did_tree_affect`. Cela nous permet de savoir si rencontrer un arbre à l'emplacement (ligne, colonne) a eu un effet quelconque, c'est-à-dire un masquage. Ces données sont utilisées lors de l'opération d'annulation.

#### Démarquer Visité

Nous savons qu'une valeur positive dans l'un des quatre dictionnaires signifie que la cellule donnée n'est pas sûre pour placer un lézard.

L'opération d'annulation est assez simple pour **un lézard**. Si nous appelons la fonction `unmark_visited` pour un lézard, cela signifie que la cellule était suffisamment sûre avant que nous y placions un lézard, nous mettons donc simplement une valeur de -1 dans les quatre dictionnaires. (Rappelez-vous, une valeur positive dans l'un des rows, columns, diagonals ou antidiagonals briserait la fonction `is_cell_safe` pour cette cellule)

Dans le cas où la fonction `unmark_visited` a été appelée pour un arbre, nous récupérons les valeurs de `did_tree_affect` pour la [ligne, colonne] donnée et utilisons ces valeurs pour restaurer les dictionnaires. Le sens de cela est que supposons que nous avons rencontré un arbre à la [ligne, colonne] donnée et qu'il a masqué l'effet du lézard pour la diagonale et la colonne en avançant. Voir la figure suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WmD5HS5AIdMrSB3-n6oipg.png)
_Les deux cellules surlignées sont masquées par l'Arbre. Cependant, il n'y a pas d'effet de masquage généré par l'Arbre pour la ligne et l'anti-diagonale._

Lorsque nous devons annuler la vue de l'arbre dans la récursion, nous devons essentiellement annuler son effet de masquage. C'est à cela que sert le dictionnaire `did_tree_affect`.

Maintenant que nous avons toutes nos structures de données en place, nous pouvons enfin examiner la fonction DFS réelle qui effectue tout le travail lourd pour trouver une solution.

### Solveur de Backtracking

Le code semble compliqué et le post deviendrait extrêmement long si je commençais à l'expliquer en détail. Je pourrais être en mesure de clarifier les doutes dans la section des commentaires. Pour l'instant, j'écrirai une version détaillée du pseudocode pour compléter.

```
1. Commencer à la cellule (0, 0)
```

```
2. Pour une cellule donnée (i, j)     a. Si tous les lézards ont été placés, imprimer la solution et retourner True.
```

```
b. Vérifier si la cellule actuelle contient un arbre.          b1. Appeler la fonction mark_visited pour mettre à jour les 4 dictionnaires avec les effets de masquage possibles dus à cet arbre.
```

```
c. Si la cellule actuelle n'est pas un arbre et qu'un lézard peut être placé         c1. Appeler mark visited pour [i, j] en tant que lézard.         c2. Ajouter [i, j] à l'ensemble des solutions.          c3. Incrémenter la colonne j comme contenant un lézard de plus.         c4. Trouver le prochain numéro de ligne pour la récursion dans la colonne j. S'il y a un tel numéro de ligne, disons r, alors récurser sur [r, j]. Sinon, récurser sur [0, j+1]         c5. Démarquer la cellule actuelle. Appeler la fonction unmark_visited pour [i, j]         c6. Décrémenter la colonne j car elle contient maintenant un lézard de moins.
```

```
d. Nous pouvons vouloir avoir une branche dans notre solution récursive où nous n'avons pas placé de lézard à [i, j] et avons simplement avancé. OU, nous n'avons pas pu placer de lézard à [i, j] et nous devons maintenant avancer.          d1. si [i + 1] < n, récurser sur [i+1, j]         d2. sinon [HEURISTIQUE D'ÉLAGAGE]              d2.1 vérifier si                    * nous n'avons placé aucun lézard dans la colonne actuelle.                   * il n'y a pas d'arbre dans la colonne actuelle et au-delà.                    * le nombre de lézards restants à placer est supérieur au nombre de colonnes restantes.                    * Si oui aux 3, alors BACKTRACKER.              d2.2 Sinon, récurser sur [0, j+1]
```

```
e. Si la cellule actuelle était en fait un arbre, alors appeler unmark_visited pour annuler ses effets.
```

C'est le pseudocode le plus approprié que j'ai pu concevoir pour le solveur basé sur DFS. C'est exactement ainsi que la fonction `dfs` est structurée.

Avec cette logique, le plus grand cas de test que j'ai pu résoudre était de placer 97 000 lézards sur un plateau de 1000 * 1000. Cela a pris environ 2 secondes pour s'exécuter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Pbn-wAU4pWiRQIee8vCGTg.jpeg)
_[http://bit.ly/2j6x5KQ](http://bit.ly/2j6x5KQ" rel="noopener" target="_blank" title=")_

Maintenant, je vous dis que cela peut sembler être un grand exploit, mais ce n'est pas vraiment le cas. Cela a été assez facile pour l'algorithme. La question pour vous est de comprendre le pourquoi de cela. Faites-le moi savoir dans la section des commentaires !

De plus, si vous trouvez une autre approche plus simple pour résoudre le problème, j'adorerais en discuter également. Faites-le moi savoir dans la section des commentaires.

J'espère que vous avez aimé l'article et que vous vous êtes amusé autant que moi en résolvant ce problème. Si vous avez aimé cet article, partagez l'amour (❤) autant que possible. Santé !
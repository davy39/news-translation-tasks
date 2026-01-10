---
title: Faisons du backtracking et sauvons quelques reines
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T19:49:49.000Z'
originalURL: https://freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uHVAfKRI6gPxiAmzCTnRCg.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Game Development
  slug: game-development
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Faisons du backtracking et sauvons quelques reines
seo_desc: 'By Sachin Malhotra

  That’s a weird looking title, that probably doesn’t make sense right now. But trust
  me, this is a pretty long post and is really fun!

  What is Backtracking ?

  Backtracking is a standard problem solving technique based on recursion.

  A...'
---

Par Sachin Malhotra

C'est un titre un peu étrange, qui n'a probablement pas beaucoup de sens pour l'instant. Mais croyez-moi, cet article est assez long et vraiment amusant !

#### Qu'est-ce que le backtracking ?

Le [backtracking](https://en.wikipedia.org/wiki/Backtracking) est une technique standard de résolution de problèmes basée sur la [récursion](https://medium.freecodecamp.org/recursion-recursion-recursion-4db8890a674d).

Un algorithme de backtracking tente de construire une solution à un problème informatique de manière incrémentale. Chaque fois que l'algorithme doit choisir entre plusieurs alternatives pour le composant suivant de la solution, il essaie simplement toutes les options possibles de manière récursive.

Le [parcours en profondeur](https://en.wikipedia.org/wiki/Depth-first_search) (DFS - Depth First Search) utilise le concept de backtracking à sa base même. Ainsi, en DFS, nous essayons essentiellement d'explorer tous les chemins à partir d'un nœud donné de manière récursive jusqu'à ce que nous atteignions l'objectif. Après avoir exploré une branche particulière d'un arbre en DFS, nous pouvons nous retrouver dans deux états possibles.

* Nous avons trouvé l'état final, auquel cas nous sortons simplement.
* Ou bien, nous n'avons pas trouvé l'état final et nous avons atteint une impasse. Dans ce scénario, nous **_revenons au dernier point de contrôle (backtrack)_** et nous essayons ensuite une branche différente.

Pour une introduction détaillée à l'algorithme de parcours en profondeur, consultez

[**Plongée au cœur d'un graphe : parcours DFS**](https://medium.com/basecs/deep-dive-through-a-graph-dfs-traversal-8177df5d0f13)  
[_Pour le meilleur ou pour le pire, il y a toujours plus d'une façon de faire quelque chose. Heureusement pour nous, dans le monde du logiciel et…_medium.com](https://medium.com/basecs/deep-dive-through-a-graph-dfs-traversal-8177df5d0f13)

et pour une introduction détaillée au backtracking et à la récursion en général, consultez les deux articles suivants.

[**Le backtracking expliqué**](https://medium.com/@andreaiacono/backtracking-explained-7450d6ef9e1a)  
[_Le backtracking est l'un de mes algorithmes préférés en raison de sa simplicité et de son élégance ; il n'a pas toujours de grandes…_medium.com](https://medium.com/@andreaiacono/backtracking-explained-7450d6ef9e1a)[**Comment fonctionne la récursion — expliqué avec des organigrammes et une vidéo**](https://medium.freecodecamp.org/how-recursion-works-explained-with-flowcharts-and-a-video-de61f40cb7f9)  
[_« Pour comprendre la récursion, il faut d'abord comprendre la récursion. »_medium.freecodecamp.org](https://medium.freecodecamp.org/how-recursion-works-explained-with-flowcharts-and-a-video-de61f40cb7f9)

Maintenant que nous sommes tous des pros du backtracking et de la récursion, voyons ce que les « Reines » ont à voir avec tout cela.

### Le célèbre problème des N-reines

Le [positionnement des reines](http://www.drdobbs.com/jvm/optimal-queens/184406068) sur un échiquier est un problème classique en mathématiques et en informatique.

Le [problème des reines](https://en.wikipedia.org/wiki/Eight_queens_puzzle) (également connu sous le nom de problème des huit reines) a été publié pour la première fois en 1848. Il consiste à placer huit reines sur un échiquier 8x8, de telle sorte qu'aucune reine ne puisse en attaquer une autre.

La reine se trouve être la pièce la plus puissante de l'échiquier, principalement en raison de la liberté de mouvement dont elle dispose.

La reine peut se déplacer dans 8 directions différentes, comme illustré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*t_J-RtgpiipfiXhHs8uywg.jpeg)
_8 directions pour le mouvement de la reine._

C'est cette liberté de mouvement qui rend le problème des N-reines extrêmement difficile.

Voici un bref aperçu de la suite de cet article. Nous allons discuter de 4 algorithmes différents pour résoudre le problème :

* La solution par force brute.
* La solution basée sur le backtracking.
* La solution basée sur les permutations.
* Enfin, la solution apparemment folle utilisant la magie binaire (Bit Magic).

Je recommande vivement de lire les solutions dans cet ordre. Cependant, n'hésitez pas à sauter une solution si vous la connaissez déjà.

L'intégralité du code pour les solutions discutées ci-dessous est disponible [ici](https://github.com/edorado93/Save-The-Queens/tree/master).

### La solution par force brute

```
tant qu'il y a de la vie sur terre :    essayer un agencement possible des reines.
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Nclg6kDeZ7jWal80xCVt-Q.jpeg)
_[https://i.ytimg.com/vi/keCgNXlq3Vo/maxresdefault.jpg](https://i.ytimg.com/vi/keCgNXlq3Vo/maxresdefault.jpg" rel="noopener" target="_blank" title=")_

Nous avons un échiquier 8x8, ce qui signifie que nous avons 64 emplacements différents pour placer les reines. Nous devons calculer C(64, 8), ou le [nombre de combinaisons](http://www.mathwords.com/c/combination_formula.htm) de 64 objets, pris 8 à la fois.

```
C(n,r) = n! / (r!(n−r)!)
```

Nous obtenons environ **4,5 milliards de combinaisons différentes pour placer les 8 reines sur un échiquier 8x8.**

L'algorithme de force brute est le suivant :

```
tant qu'il reste des configurations non essayées {
   générer la configuration suivante
   si les reines ne s'attaquent pas dans cette configuration alors
   {
      afficher cette configuration ;
   }
}
```

Cela fait beaucoup de permutations à vérifier pour un processeur standard. Nous pourrions utiliser une sorte de solution multi-processeurs (car la vérification d'une permutation est indépendante d'une autre).

Mais pourquoi faire cela alors que nous avons de meilleurs algorithmes pour résoudre ce problème ?

### Le backtracking

Nous pouvons faire mieux que la solution naïve par force brute pour ce problème. Considérez le pseudo-code suivant pour la solution basée sur le backtracking :

```
1) Commencer par la colonne la plus à gauche
2) Si toutes les reines sont placées
    incrémenter le compteur de solutions et revenir
3) Essayer toutes les rangées de la colonne actuelle. Faire ce qui suit pour chaque rangée essayée.
    a) Si la reine peut être placée en toute sécurité dans cette rangée alors marquer ce [rangée, colonne] comme faisant partie de la solution et vérifier récursivement si le placement de la reine ici mène à une solution.
```

```
    b) Si le placement de la reine dans [rangée, colonne] mène à une solution alors
   incrémenter le compteur de solutions et revenir
```

```
    c) Si le placement de la reine ne mène pas à une solution alors démarquer ce [rangée, colonne] (Backtrack) et aller à l'étape (a) pour essayer d'autres rangées.
```

```
4) Si toutes les rangées ont été essayées et que rien n'a fonctionné, revenir pour déclencher le backtracking.
```

Le pseudo-code semble assez simple, et vous pouvez consulter le code basé sur Python pour cela [ici](http://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/). Je ne fournirai pas de description détaillée de l'algorithme de backtracking ici.

J'aimerais toutefois discuter d'une optimisation pour réduire la complexité temporelle de la vérification de la possibilité de placer une reine dans une case du plateau.

Une partie importante de l'algorithme est celle où nous devons vérifier si une reine peut être placée dans une case `[i, j]`. Cette étape prend beaucoup de temps. Regardons une manière brute de le faire, puis une version optimisée.

Cela a une [**complexité** **temporelle**](https://www.youtube.com/watch?v=KSNx22U4uWE) **de O(N),** et cela sera appelé plusieurs fois pour chaque case du plateau.

Nous pouvons cependant utiliser des structures de données supplémentaires pour accélérer la vérification de validité du placement d'une reine sur une case `[i, j]`. Cela ramènera la complexité à `O(1)` — en d'autres termes, un temps constant. C'est une réduction énorme !

Les points clés de ce morceau de code sont les suivants :

* Tous les éléments d'une diagonale particulière (du haut à gauche vers le bas à droite) ont la même valeur pour `row - column`.
* Tous les éléments d'une anti-diagonale particulière (du haut à droite vers le bas à gauche) ont la même valeur pour `row + column`.

Cette optimisation ramène la complexité de `isSafe` à `O(1)`**.** Hourra ! 💡

Maintenant que nous en avons terminé avec les algorithmes de base pour les N-reines, passons à d'autres plus compliqués qui s'exécutent beaucoup plus rapidement que ceux décrits ci-dessus.

### Permutations et N-reines

L'idée derrière cet algorithme est assez simple. Considérez les faits suivants concernant le placement de chaque reine :

* On ne peut placer qu'une seule reine par rangée.
* La même chose peut être dite pour chaque colonne.
* Cela signifie que toutes les solutions réussies ne seront que des **permutations des indices de colonne.**
* Chaque rangée successive a une position candidate de moins pour le placement de la reine.

En suivant cette logique, l'espace du problème se réduit à seulement **8! = 40 320.**

Cela donne beaucoup moins d'options à essayer pour trouver les solutions à notre problème.

Regardons le pseudo-code pour cette approche :

```
* Commencer par une permutation initiale des reines alignées le long de l'une des diagonales. 
```

```
* Pour positionner une reine sur la rangée j
    * Si j a atteint N, vous avez une solution valide. Traitez-la comme valide.
    * Boucler sur k de j à N
       * Échanger board[j] et board[k].
        * Vérifier si une reine peut être placée sur (rangée, board[rangée])
           * Si oui, alors placer une reine et faire la récursion pour la rangée j+1
       * Annuler le placement d'une reine sur (rangée, board[rangée])
   * Annuler les échanges effectués.   
```

Pour plus de clarté, regardons également le code :

**Note :** `board[i]` stocke le numéro de la colonne où une reine a été placée dans la rangée `i`. Par conséquent, la valeur de la case est donnée par `(i, board[i])`.

Cette optimisation accélère considérablement le calcul, en raison de l'espace du plateau fortement réduit à considérer lors du placement des reines.

L'accélération devient plus évidente à mesure que nous augmentons la taille du plateau, et donc le nombre de reines à placer.

De plus, la vérification de validité pour une case particulière devient plus simple, car nous n'avons plus qu'à vérifier les diagonales et les anti-diagonales.

### Voyons un peu de magie binaire !

Cette solution particulière au problème est quelque chose qui était pratiquement du chinois pour moi la première fois que je l'ai examinée.

C'est compréhensible cependant, car après tout, c'est de la **magie** **binaire !**

Mais heureusement, j'ai trouvé cet incroyable [article de blog](http://gregtrowbridge.com/a-bitwise-solution-to-the-n-queens-problem-in-javascript/) expliquant l'intégralité de l'algorithme ligne par ligne. Le code est en JavaScript. Je vais décrire la même chose mais pour le code en Python. Lisez l'article qui vous convient le mieux :)

La meilleure façon d'expliquer cet algorithme est de présenter le code d'abord ✨

![Image](https://cdn-media-1.freecodecamp.org/images/1*yAqiXTpbu-6mRHQ5SjYn5Q.jpeg)
_[http://mymemes.biz/wp-content/uploads/2017/10/meme-magic-59df0f3650800.jpg](http://mymemes.biz/wp-content/uploads/2017/10/meme-magic-59df0f3650800.jpg" rel="noopener" target="_blank" title=")_

L'algorithme fonctionne en utilisant la même idée de base que celle discutée précédemment. Nous n'avons besoin de vérifier que trois choses avant de placer une reine sur une certaine case :

1. La colonne de la case ne contient pas d'autres reines
2. La diagonale gauche de la case ne contient pas d'autres reines
3. La diagonale droite de la case ne contient pas d'autres reines

Le code peut ressembler à une boîte noire qui semble simplement fonctionner. C'est ce que j'ai ressenti la première fois que j'ai lu ce morceau de code incroyablement rapide.

Essayons de le décomposer ligne par ligne.

#### Ligne #1

Vous remarquerez que la fonction accepte 4 paramètres :

1. column
2. left_diagonal
3. right_diagonal
4. queens_placed

Le paramètre `**queens_placed**` est explicite. Nous devons suivre le nombre de reines que nous avons placées jusqu'à présent pour que la récursion se termine à un moment donné.

Les trois variables `column`, `left_diagonal` et `right_diagonal` sont essentiellement des entiers, mais elles sont traitées comme une séquence de bits pour les besoins de cet algorithme. Ces variables nous aident à déterminer les positions ouvertes sur la rangée actuelle pour le placement d'une reine.

Regardons l'image ci-dessous :

* `ld` = left_diagonal
* `cols` = column
* `rd` = right_diagonal

![Image](https://cdn-media-1.freecodecamp.org/images/1*u0D6tQbzP98BCTD54GfV9A.png)
_[http://gregtrowbridge.com/a-bitwise-solution-to-the-n-queens-problem-in-javascript/](http://gregtrowbridge.com/a-bitwise-solution-to-the-n-queens-problem-in-javascript/" rel="noopener" target="_blank" title=")_

Ignorez la variable `poss` pour l'instant. Nous y reviendrons plus tard.

#### Lignes #2–6

Ces lignes de code gèrent simplement le cas de base de la récursion. Lorsque nous avons placé `N` reines sur notre plateau N par N, nous incrémentons le compteur de solutions et affichons la solution si le drapeau approprié a été défini lors de l'exécution (voir le code complet pour ce drapeau).

#### Ligne #8

Cela trouve les `valid_spots` restants sur la rangée actuelle. C'est essentiellement la variable `poss` illustrée dans l'image ci-dessus.

```
valid_spots = self.all_ones & ~(column | left_diagonal | right_diagonal)
```

Par exemple, disons qu'après un certain nombre d'itérations, nous avons :

```
left_diagonal = 00011000
column = 11001001 
right_diagonal = 00011100
```

Le code `(column | left_diagonal | right_diagonal)` effectue simplement une opération « OU » (OR), et aboutit à la séquence de bits 11011101.

Ensuite, l'ajout du `~` devant cette expression provoque l'inversion de la séquence de bits résultante (ainsi tous les zéros deviennent des uns et vice versa), et `valid_spots` serait défini sur 00100010.

Ainsi, pour la rangée actuelle, les colonnes numéros 0, 1, 3, 4, 5 et 7 ne sont pas disponibles. Nous ne pouvons placer une reine que sur les colonnes numéros 2 et 6. Ce sont les deux seuls emplacements que nous essaierons.

#### Ligne #10

```
current_spot = -valid_spots & valid_spots
```

Cette ligne trouve le premier bit non nul et le stocke dans `current_spot`. C'est donc essentiellement trouver le premier emplacement vide où nous pouvons placer notre reine (à partir de la colonne la plus à droite).

C'est précisément ce qui rend l'algorithme si rapide. Nous avons utilisé des opérateurs binaires pour nous indiquer directement les positions vides qui sont totalement sûres pour placer nos reines. Par conséquent, cela conduit à une accélération majeure comme vous le verrez plus tard.

#### Lignes #11 et 12

La ligne #11 ajoute simplement la reine placée au `current_spot` à notre ensemble de solutions afin que nous puissions l'afficher plus tard.

La ligne #12 marque le `current_spot` comme indisponible. Rappelez-vous, effectuer un [XOR](https://en.wikipedia.org/wiki/XOR_swap_algorithm) sur les mêmes bits conduit à 0.

#### Ligne #13

C'est probablement la ligne de code la plus importante pour cet algorithme (et aussi la plus déroutante). Ici, nous propageons simplement les effets que nous avons introduits vers la rangée suivante.

Nous avons placé une reine au `current_spot` et nous voulons maintenant mettre à jour nos variables `column`, `left_diagonal` et `right_diagonal` pour inclure ces changements alors que nous passons à la rangée suivante.

```
self.solve((column | current_spot), (left_diagonal | current_spot) >> 1, (right_diagonal | current_spot) << 1, queens_placed + 1)
```

**NOTE :** `a | b` signifie un OU bit à bit pour les variables `a` et `b`. De plus, `a << 1` est un opérateur de décalage à gauche. De même, `a >> 1` est l'opérateur de décalage à droite.

Ainsi, appeler `(right_diagonal | current_spot) << 1` signifie simplement : combiner `right_diagonal` et `current_spot` avec une opération OU, puis décaler tout le résultat vers la gauche d'une position.

Par exemple — disons que `right_diagonal` avait la valeur `00011100`. Et disons que nous avons fait occuper à la reine le dernier emplacement tel que le dernier 1 dans l'entier `valid_spots` `00100010`.

Alors le `current_spot` deviendrait `00000010` et le combiner par un OU avec la `right_diagonal` nous donnerait `00011110`. Nous le décalons à gauche pour obtenir `00111100` et c'est exactement l'effet que nous voulons pour la diagonale droite.

L'anti-diagonale se déplace du haut à droite vers le bas à gauche. Le décalage à gauche sur les bits produit cet effet.

Pour plus de clarté, essayez de faire cette opération sur papier :

![Image](https://cdn-media-1.freecodecamp.org/images/1*u0D6tQbzP98BCTD54GfV9A.png)
_Juste pour que vous n'ayez pas à remonter dans l'article 🚀_

Nous commençons avec des 0 pour les trois variables, ce qui signifie que toutes les positions sont disponibles dans la première rangée pour placer les reines.

Vient maintenant la partie amusante (enfin, de quoi vous étonner 😉), les comparaisons de vitesse.

### Statistiques

Regardons les statistiques d'un outil que Google a construit pour résoudre le problème des N-reines.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZDMBCDEaUvQmcL1TO-GJDg.png)
_[https://developers.google.com/optimization/cp/queens](https://developers.google.com/optimization/cp/queens" rel="noopener" target="_blank" title=")_

Voici les statistiques pour les 4 approches différentes que nous avons discutées pour les N-reines :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3vDf0vC_7O1W-RK94ZS5HQ.png)
_Tous les temps sont en ms._

![Image](https://cdn-media-1.freecodecamp.org/images/1*-J6QjokBFXvZDOYkTGBTyQ.png)
_Tous les temps sont en ms._

La dernière solution impliquant des opérateurs bit à bit est clairement plus performante que les résultats rapportés par [celui de Google](https://developers.google.com/optimization/cp/queens). 😎

De plus, une chose intéressante à noter ici est l'effet qu'une légère optimisation a eu sur les résultats. Rappelez-vous l'optimisation où nous avons converti la vérification `is_cell_safe` d'une solution en `O(N)` à une vérification en `O(1)`. Cela nous montre clairement comment de si petits changements peuvent apporter d'énormes impacts sur les performances.

Si vous avez lu jusqu'au bout, je suis sûr que votre curiosité algorithmique a été satisfaite ! Mais attention, ce n'est que la partie émergée de l'iceberg 🧊.

J'ai un autre article de prévu bientôt où nous aborderons un problème similaire aux N-reines mais avec une légère variante.

Félicitations à [Rahul Gupta](https://www.freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415/undefined) pour ses précieuses contributions au code et à l'article.
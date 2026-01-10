---
title: Si vous avez des boucles lentes en Python, vous pouvez les corriger… jusqu'à
  ce que vous ne puissiez plus
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-02T18:12:10.000Z'
originalURL: https://freecodecamp.org/news/if-you-have-slow-loops-in-python-you-can-fix-it-until-you-cant-3a39e03b6f35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t5vZrkc3PdQZ78RX7Jx8Lg.jpeg
tags:
- name: numpy
  slug: numpy
- name: optimization
  slug: optimization
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Si vous avez des boucles lentes en Python, vous pouvez les corriger… jusqu'à
  ce que vous ne puissiez plus
seo_desc: 'By Maxim Mamaev

  Let’s take a computational problem as an example, write some code, and see how we
  can improve the running time. Here we go.

  Setting the scene: the knapsack problem

  This is the computational problem we’ll use as the example:

  The knapsa...'
---

Par Maxim Mamaev

Prenons un problème de calcul comme exemple, écrivons du code et voyons comment nous pouvons améliorer le temps d'exécution. C'est parti.

### Mise en scène : le problème du sac à dos

Voici le problème de calcul que nous utiliserons comme exemple :

Le problème du sac à dos est un problème bien connu en optimisation combinatoire. Dans cette section, nous allons passer en revue sa version la plus courante, le **problème du sac à dos 0-1**, et sa solution par programmation dynamique. Si vous êtes familier avec le sujet, vous pouvez [passer cette partie](#heading-installation).

Vous disposez d'un sac à dos d'une capacité **C** et d'une collection de **N** objets. Chaque objet a un poids **w[i]** et une valeur **v[i]**. Votre tâche est de remplir le sac à dos avec les objets les plus précieux. En d'autres termes, vous devez maximiser la valeur totale des objets que vous mettez dans le sac à dos, sous contrainte : le poids total des objets pris **ne doit pas** dépasser la capacité du sac à dos.

Une fois que vous avez une solution, le poids total des objets dans le sac à dos est appelé « poids de la solution », et leur valeur totale est la « valeur de la solution ».

Le problème a de nombreuses applications pratiques. Par exemple, vous avez décidé d'investir 1600 $ dans les actions FAANG (le nom collectif pour les actions de Facebook, Amazon, Apple, Netflix et Google aka Alphabet). Chaque action a un prix actuel et une estimation de prix pour un an. En 2018, ils étaient les suivants :

```
========= ======= ======= =========Société   Symbole  Prix   Estimation========= ======= ======= =========Alphabet  GOOG    1030    1330Amazon    AMZN    1573    1675Apple     AAPL    162     193 Facebook  FB      174     216 Netflix   NFLX    312     327========= ======= ======= =========
```

Pour simplifier l'exemple, nous supposerons que vous ne mettrez jamais tous vos œufs dans le même panier. Vous êtes prêt à acheter **au plus** une action de chaque société. Quelles actions achetez-vous pour maximiser votre profit ?

C'est un problème de sac à dos. Votre budget (1600 $) est la **capacité (C)** du sac. Les actions sont les objets à emballer. Les prix actuels sont les **poids (w)**. Les estimations de prix sont les **valeurs**. Le problème semble trivial. Cependant, la solution n'est pas évidente au premier abord — devez-vous acheter une action d'Amazon, ou une action de Google plus une de chaque combinaison d'Apple, Facebook ou Netflix ?

Bien sûr, dans ce cas, vous pouvez faire des calculs rapides à la main et arriver à la solution : vous devriez acheter Google, Netflix et Facebook. Ainsi, vous dépensez 1516 $ et espérez gagner 1873 $.

Maintenant, vous croyez avoir découvert un Eldorado. Vous cassez votre tirelire et collectez 10 000 $. Malgré votre excitation, vous restez ferme avec la règle « une action — un achat ». Par conséquent, avec ce budget plus large, vous devez élargir vos options. Vous décidez de considérer toutes les actions de la liste NASDAQ 100 comme candidates pour l'achat.

L'avenir n'a jamais été plus brillant, mais soudain vous réalisez que, pour identifier votre portefeuille d'investissement idéal, vous devrez vérifier environ 2⁹⁰⁰ combinaisons. Même si vous êtes super optimiste sur l'imminence et l'ubiquité de l'économie numérique, toute économie nécessite — au moins — un univers où elle fonctionne. Malheureusement, dans quelques billions d'années, lorsque votre calcul se terminera, notre univers n'existera probablement plus.

#### Algorithme de programmation dynamique

Nous devons abandonner l'approche de force brute et programmer une solution intelligente. Les petits problèmes de sac à dos (et le nôtre en est un petit, croyez-le ou non) sont résolus par programmation dynamique. L'idée de base est de commencer par un problème trivial dont nous connaissons la solution, puis d'ajouter de la complexité étape par étape.

Si vous trouvez les explications suivantes trop abstraites, voici une [illustration annotée](https://github.com/mmamaev/looping_python/blob/master/ks_dp_example.pdf) de la solution à un très petit problème de sac à dos. Cela vous aidera à visualiser ce qui se passe.

Supposons que, étant donné les **i** premiers objets de la collection, nous connaissons les valeurs de solution **s(i, k)** pour toutes les capacités de sac à dos **k** dans la plage de 0 à **C**.

En d'autres termes, nous avons cousu **C+1** sacs à dos « auxiliaires » de toutes les tailles de 0 à **C**. Ensuite, nous avons trié notre collection, pris le premier **i** objet et mis de côté tous les autres. Et maintenant, nous supposons que, par une certaine magie, nous savons comment emballer de manière optimale chacun des sacs de cet ensemble de travail de **i** objets. Les objets que nous choisissons dans l'ensemble de travail peuvent être différents pour différents sacs, mais pour l'instant, nous ne nous intéressons pas aux objets que nous prenons ou sautons. C'est seulement la valeur de la solution **s(i, k)** que nous enregistrons pour chacun de nos nouveaux sacs cousus.

Maintenant, nous récupérons l'objet suivant, le **(i+1)**ème, de la collection et l'ajoutons à l'ensemble de travail. Trouvons les valeurs de solution pour tous les sacs à dos auxiliaires avec cet nouvel ensemble de travail. En d'autres termes, nous trouvons **s(i+1, k)** pour tous **k=0..C** étant donné **s(i, k)**.

Si **k** est inférieur au poids du nouvel objet **w[i+1]**, nous ne pouvons pas prendre cet objet. En effet, même si nous prenions **uniquement** cet objet, il ne rentrerait pas seul dans le sac à dos. Par conséquent, **s(i+1, k) = s(i, k)** pour tous **k < w[i+1]**.

Pour les valeurs **k >= w[i+1]**, nous devons faire un choix : soit nous prenons le nouvel objet dans le sac à dos de capacité **k**, soit nous le sautons. Nous devons évaluer ces deux options pour déterminer laquelle nous donne plus de valeur dans le sac.

Si nous prenons le **(i+1)**ème objet, nous acquérons la valeur **v[i+1]** et consommons une partie de la capacité du sac à dos pour accommoder le poids **w[i+1]**. Cela nous laisse avec la capacité **k−w[i+1]** que nous devons remplir de manière optimale en utilisant (certains des) **i** premiers objets. Ce remplissage optimal a la valeur de solution **s(i, k−w[i+1])**. Ce nombre nous est déjà connu car, par hypothèse, nous connaissons toutes les valeurs de solution pour l'ensemble de travail de **i** objets. Par conséquent, la valeur candidate de la solution pour le sac à dos **k** avec l'objet **i+1** pris serait :

**s(i+1, k | i+1 pris) = v[i+1] + s(i, k−w[i+1])**.

L'autre option est de sauter l'objet **i+1**. Dans ce cas, rien ne change dans notre sac à dos, et la valeur candidate de la solution serait la même que **s(i, k)**.

Pour décider du meilleur choix, nous comparons les deux candidats pour les valeurs de solution :

**s(i+1, k | i+1 pris) = v[i+1] + s(i, k−w[i+1])**

**s(i+1, k | i+1 sauté) = s(i, k)**

Le maximum de ces deux devient la solution **s(i+1, k)**.

En résumé :

```
si k < w[i+1] :    s(i+1, k) = s(i, k)sinon :    s(i+1, k) = max(v[i+1] + s(i, k-w[i+1]), s(i, k))
```

Maintenant, nous pouvons résoudre le problème du sac à dos étape par étape. Nous commençons avec l'ensemble de travail vide **(_i=0_)**. Évidemment, **s(0, k) = 0** pour tout **k**. Ensuite, nous faisons des étapes en ajoutant des objets à l'ensemble de travail et en trouvant les valeurs de solution **s(i, k)** jusqu'à ce que nous arrivions à **s(i+1=N, k=C)**, qui est la valeur de solution du problème original.

Notez que, de cette manière, nous avons construit la grille des **_NxC_** valeurs de solution.

Cependant, malgré avoir appris la valeur de la solution, nous ne savons pas exactement quels objets ont été pris dans le sac à dos. Pour le découvrir, nous retraçons la grille. En partant de **s(i=N, k=C)**, nous comparons **s(i, k)** avec **s(i−1, k)**.

Si **s(i, k) = s(i−1, k)**, le **i**ème objet n'a pas été pris. Nous réitérons avec **i=i−1** en gardant la valeur de **k** inchangée. Sinon, le **i**ème objet a été pris et pour l'étape d'examen suivante, nous réduisons le sac à dos de **w[i]** — nous avons défini **i=i−1, k=k−w[i]**. 

De cette manière, nous examinons tous les objets du **N**ième au premier, et déterminons lesquels ont été mis dans le sac à dos. Cela nous donne la solution au problème du sac à dos.

### Code et analyse

Maintenant que nous avons l'algorithme, nous allons comparer plusieurs implémentations, en commençant par une implémentation directe. Le code est disponible sur [GitHub](https://github.com/mmamaev/looping_python/blob/master/ks_dp_solvers.py).

Les données sont la liste **Nasdaq 100**, contenant les prix actuels et les estimations de prix pour cent actions (en 2018). Notre budget d'investissement est de 10 000 $.

Rappelons que les prix des actions ne sont pas des nombres ronds en dollars, mais incluent des cents. Par conséquent, pour obtenir une solution précise, nous devons tout compter en cents — nous voulons définitivement éviter les nombres à virgule flottante. Ainsi, la capacité de notre sac à dos est de 10 000 $ x 100 cents = 1 000 000 cents, et la taille totale de notre problème **N x C** = 1 000 000.

Avec un entier prenant 4 octets de mémoire, nous nous attendons à ce que l'algorithme consomme environ 400 Mo de RAM. Donc, la mémoire ne sera pas une limitation. C'est le temps d'exécution qui nous préoccupe.

Bien sûr, toutes nos implémentations donneront la même solution. Pour votre référence, l'investissement (le poids de la solution) est de 999 930 cents (9 999,30 $) et le rendement attendu (la valeur de la solution) est de 1 219 475 cents (12 194,75 $). La liste des actions à acheter est plutôt longue (80 sur 100 objets). Vous pouvez l'obtenir en exécutant le code.

Et, s'il vous plaît, rappelez-vous que **ceci est un exercice de programmation, pas un conseil en investissement**. Au moment où vous lisez cet article, les prix et les estimations auront changé par rapport à ce qui est utilisé ici comme exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SEihq9zvMPCd8qLZHaUHIg.jpeg)
_Crédit : [Martin von Rotz](https://www.snapwi.re/user/mavoro" rel="noopener" target="_blank" title=")_

#### Boucles "for" classiques

L'implémentation directe de l'algorithme est donnée ci-dessous.

Il y a deux parties.

Dans la première partie (lignes 3-7 ci-dessus), deux boucles `for` imbriquées sont utilisées pour construire la grille de solution.

La boucle externe ajoute des objets à l'ensemble de travail jusqu'à ce que nous atteignions **N** (la valeur de **N** est passée dans le paramètre `items`). La ligne des valeurs de solution pour chaque nouvel ensemble de travail est initialisée avec les valeurs calculées pour l'ensemble de travail précédent.

La boucle interne pour chaque ensemble de travail itère les valeurs de `k` à partir du poids de l'`item` nouvellement ajouté jusqu'à **C** (la valeur de **C** est passée dans le paramètre `capacity`).

Notez que nous n'avons pas besoin de commencer la boucle à partir de **k=0**. Lorsque `k` est inférieur au poids de `item`, les valeurs de solution sont toujours les mêmes que celles calculées pour l'ensemble de travail précédent, et ces nombres ont déjà été copiés dans la ligne actuelle par initialisation.

Lorsque les boucles sont terminées, nous avons la grille de solution et la valeur de la solution.

La deuxième partie (lignes 9-17) est une seule boucle `for` de **N** itérations. Elle retrace la grille pour trouver quels objets ont été pris dans le sac à dos.

Par la suite, nous nous concentrerons exclusivement sur la première partie de l'algorithme car elle a une complexité temporelle et spatiale de **O(N*C)**. La partie de rétroaction nécessite seulement **O(N)** temps et ne dépense aucune mémoire supplémentaire — sa consommation de ressources est relativement négligeable.

Il faut **180 secondes** pour que l'implémentation directe résolve le problème du sac à dos **Nasdaq 100** sur mon ordinateur.

À quel point est-ce mauvais ? D'un côté, avec les vitesses de l'âge moderne, nous ne sommes pas habitués à attendre trois minutes pour qu'un ordinateur fasse quelque chose. D'un autre côté, la taille du problème — cent millions — semble effectivement intimidante, donc, peut-être, trois minutes sont acceptables ?

Pour obtenir un benchmark, programmons le même algorithme dans un autre langage. Nous avons besoin d'un langage compilé à typage statique pour garantir la vitesse de calcul. Non, pas C. Ce n'est pas tendance. Nous allons rester à la mode et écrire en Go :

Comme vous pouvez le voir, le code Go est assez similaire à celui en Python. J'ai même copié-collé une ligne, la plus longue, telle quelle.

Quel est le temps d'exécution ? **400 millisecondes** ! En d'autres termes, Python s'est avéré 500 fois plus lent que Go. L'écart sera probablement encore plus grand si nous essayions en C. C'est définitivement un désastre pour Python.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lmi8rlKeei1hcMRkeShzIw.jpeg)
_Citation de J. K. Rowling dans « Harry Potter et la Chambre des Secrets » [Source de l'image originale ici](https://pixabay.com/en/snail-rainy-day-spring-animal-slow-3385348/" rel="noopener" target="_blank" title=")._

Pour découvrir ce qui ralentit le code Python, exécutons-le avec [line profiler](https://github.com/rkern/line_profiler). Vous pouvez trouver la sortie du profileur pour cette implémentation et les suivantes de l'algorithme sur [GitHub](https://github.com/mmamaev/looping_python/blob/master/ks_dp_solvers_profiles.txt).

Dans le solveur direct, 99,7 % du temps d'exécution est passé dans deux lignes. Ces deux lignes comprennent la boucle interne, qui est exécutée 98 millions de fois :

Je m'excuse pour les lignes excessivement longues, mais le profileur de ligne ne peut pas gérer correctement les sauts de ligne au sein de la même instruction.

J'ai entendu dire que l'opérateur `for` de Python est lent, mais, intéressamment, la plupart du temps n'est pas passé dans la ligne `for` mais dans le corps de la boucle.

Nous pouvons décomposer le corps de la boucle en opérations individuelles pour voir si une opération particulière est trop lente :

Il semble qu'aucune opération particulière ne se distingue. Les temps d'exécution des opérations individuelles au sein de la boucle interne sont à peu près les mêmes que les temps d'exécution des opérations analogues ailleurs dans le code.

Remarquez comment la décomposition du code a augmenté le temps d'exécution total. La boucle interne prend maintenant 99,9 % du temps d'exécution. Plus votre code Python est « stupide » (décomposé en opérations élémentaires), plus il devient lent. Intéressant, n'est-ce pas ?

#### Fonction intégrée map

Rendons le code plus optimisé et remplaçons la boucle interne `for` par une fonction intégrée `map()` :

Le temps d'exécution de ce code est de **102 secondes**, soit 78 secondes de moins que l'implémentation directe. En effet, `map()` fonctionne de manière notable, mais pas écrasante, plus rapidement.

#### Compréhension de liste

Vous avez peut-être remarqué que chaque exécution de la boucle interne produit une liste (qui est ajoutée à la grille de solution comme une nouvelle ligne). La manière Pythonique de créer des listes est, bien sûr, la compréhension de liste. Essayons-la au lieu de `map()`.

Cela s'est terminé en **81 secondes**. Nous avons réalisé une autre amélioration et réduit le temps d'exécution de moitié par rapport à l'implémentation directe (180 sec). Hors contexte, cela serait salué comme un progrès significatif. Hélas, nous sommes encore à des années-lumière de notre benchmark de 0,4 sec.

#### Tableaux NumPy

Enfin, nous avons épuisé les outils intégrés de Python. Oui, j'entends le rugissement du public scandant « NumPy ! NumPy ! » Mais pour apprécier l'efficacité de NumPy, nous devrions l'avoir mis en contexte en essayant `for`, `map()` et la compréhension de liste au préalable.

D'accord, maintenant c'est l'heure de NumPy. Donc, nous abandonnons les listes et mettons nos données dans des tableaux numpy :

Soudain, le résultat est décourageant. Ce code s'exécute 1,5 fois plus lentement que le solveur de compréhension de liste vanilla (**123 sec** contre 81 sec). Comment cela peut-il être ?

Examinons les profils de ligne pour les deux solveurs.

L'initialisation de `grid[0]` en tant que tableau numpy (ligne 274) est trois fois plus rapide que lorsqu'il s'agit d'une liste Python (ligne 245). À l'intérieur de la boucle externe, l'initialisation de `grid[item+1]` est 4,5 fois plus rapide pour un tableau NumPy (ligne 276) que pour une liste (ligne 248). Jusqu'à présent, tout va bien.

Cependant, l'exécution de la ligne 279 est 1,5 fois plus lente que son analogue sans numpy dans la ligne 252. Le problème est que la compréhension de liste crée une **liste** de valeurs, mais nous stockons ces valeurs dans un **tableau NumPy** qui se trouve du côté gauche de l'expression. Par conséquent, cette ligne ajoute implicitement une surcharge de conversion d'une liste en un tableau NumPy. Avec la ligne 279 représentant 99,9 % du temps d'exécution, tous les avantages précédemment notés de numpy deviennent négligeables.

Mais nous avons toujours besoin d'un moyen pour **itérer** à travers les tableaux afin de faire les calculs. Nous avons déjà appris que la compréhension de liste est l'outil d'itération le plus rapide. (Au fait, si vous essayez de construire des tableaux NumPy dans une boucle `for` classique en évitant la conversion de liste en tableau NumPy, vous obtiendrez le temps d'exécution impressionnant de 295 sec.) Donc, sommes-nous bloqués et NumPy est-il inutile ? Bien sûr que non.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0yrZox6O3EEEKregnri0Vw.jpeg)
_Crédit : [Taras Makarenko](https://www.pexels.com/@taras-makarenko-188506" rel="noopener" target="_blank" title=")_

#### Utilisation correcte de NumPy

Le simple fait de stocker des données dans des tableaux NumPy ne suffit pas. La véritable puissance de NumPy réside dans les fonctions qui effectuent des calculs sur des tableaux NumPy. Elles prennent des tableaux comme paramètres et retournent des tableaux comme résultats.

Par exemple, il existe une fonction `where()` qui prend trois tableaux comme paramètres : `condition`, `x` et `y`, et retourne un tableau construit en choisissant des éléments soit dans `x`, soit dans `y`. Le premier paramètre, `condition`, est un tableau de booléens. Il indique où choisir : si un élément de `condition` est évalué à `True`, l'élément correspondant de `x` est envoyé en sortie, sinon l'élément de `y` est pris.

Notez que la fonction NumPy fait tout cela en un seul appel. Le parcours des tableaux est caché sous le capot.

Voici comment nous utilisons `where()` comme substitut de la boucle interne `for` dans le premier solveur ou, respectivement, la compréhension de liste du dernier :

Il y a trois morceaux de code qui sont intéressants : la ligne 8, la ligne 9 et les lignes 10-13 comme numérotées ci-dessus. Ensemble, ils remplacent la boucle interne qui itérerait à travers toutes les tailles possibles de sacs à dos pour trouver les valeurs de solution.

Jusqu'à ce que la capacité du sac à dos atteigne le poids de l'objet nouvellement ajouté à l'ensemble de travail (`this_weight`), nous devons ignorer cet objet et définir les valeurs de solution à celles de l'ensemble de travail précédent. C'est assez simple (ligne 8) :

```
grid[item+1, :this_weight] = grid[item, :this_weight]
```

Ensuite, nous construisons un tableau auxiliaire `temp` (ligne 9) :

```
temp = grid[item, :-this_weight] + this_value
```

Ce code est analogue à, mais beaucoup plus rapide que :

```
[grid[item, k - this_weight] + this_value  for k in range(this_weight, capacity+1)]
```

Il calcule les valeurs de solution potentielles si le nouvel objet était pris dans chacun des sacs à dos qui peuvent accommoder cet objet.

Remarquez comment le tableau `temp` est construit en ajoutant un **scalaire** à un tableau. C'est une autre fonction puissante de NumPy appelée « broadcasting ». Lorsque NumPy voit des opérandes avec des dimensions différentes, il essaie d'étendre (c'est-à-dire de « broadcaster ») l'opérande de faible dimension pour correspondre aux dimensions de l'autre. Dans notre cas, le scalaire est étendu à un tableau de la même taille que `grid[item, :-this_weight]` et ces deux tableaux sont additionnés ensemble. En conséquence, la valeur de `this_value` est ajoutée à chaque élément de `grid[item, :-this_weight]` — aucune boucle n'est nécessaire.

Dans la partie suivante (lignes 10-13), nous utilisons la fonction `where()` qui fait exactement ce que l'algorithme exige : elle compare deux valeurs de solution potentielles pour chaque taille de sac à dos et sélectionne celle qui est la plus grande.

```
grid[item + 1, this_weight:] =                 np.where(temp > grid[item, this_weight:],             temp,             grid[item, this_weight:])
```

La comparaison est effectuée par le paramètre `condition`, qui est calculé comme `temp > grid[item, this_weight:]`. Il s'agit d'une opération élément par élément qui produit un tableau de valeurs booléennes, une pour chaque taille d'un sac à dos auxiliaire. Une valeur **Vraie** signifie que l'objet correspondant doit être emballé dans le sac à dos. Par conséquent, la valeur de la solution prise dans le tableau est le deuxième argument de la fonction, `temp`. Sinon, l'objet doit être ignoré, et la valeur de la solution est copiée à partir de la ligne précédente de la grille — le troisième argument de la fonction `where()`.

Enfin, le moteur de distorsion est engagé ! Ce solveur s'exécute en **0,55 sec**. Cela représente 145 fois plus rapide que le solveur basé sur la compréhension de liste et 329 fois plus rapide que le code utilisant la boucle `for`. Bien que nous n'ayons pas dépassé le solveur écrit en Go (0,4 sec), nous nous en sommes approchés.

#### Certaines boucles doivent rester

Attendez, mais qu'en est-il de la boucle externe `for` ?

Dans notre exemple, le code de la boucle externe, qui ne fait pas partie de la boucle interne, n'est exécuté que 100 fois, donc nous pouvons nous en sortir sans le modifier. Cependant, d'autres fois, la boucle externe peut s'avérer aussi longue que la boucle interne.

Pouvons-nous réécrire la boucle externe en utilisant une fonction NumPy de manière similaire à ce que nous avons fait pour la boucle interne ? La réponse est non.

Malgré le fait que les deux soient des boucles `for`, les boucles externes et internes sont assez différentes dans ce qu'elles font.

La boucle interne produit un tableau 1D basé sur un autre tableau 1D dont les éléments sont **tous connus** lorsque la boucle commence. C'est cette disponibilité préalable des données d'entrée qui nous a permis de substituer la boucle interne par `map()`, la compréhension de liste ou une fonction NumPy.

La boucle externe produit un tableau 2D à partir de tableaux 1D dont les éléments **ne sont pas** connus lorsque la boucle commence. De plus, ces tableaux composants sont calculés par un algorithme récursif : nous ne pouvons trouver les éléments du **(i+1)**ème tableau qu'après avoir trouvé le **i**ème.

Supposons que la boucle externe puisse être présentée comme une fonction :

`grid = g(row0, row1, … rowN)`

Tous les paramètres de la fonction doivent être évalués avant que la fonction ne soit appelée, mais seul `row0` est connu à l'avance. Puisque le calcul de la **(i+1)**ème ligne dépend de la disponibilité de la **i**ème, nous avons besoin d'une boucle allant de `1` à `N` pour calculer tous les paramètres `row`. Par conséquent, pour substituer la boucle externe par une fonction, nous avons besoin d'une autre boucle qui évalue les paramètres de cette fonction. Cette autre boucle est exactement la boucle que nous essayons de remplacer.

L'autre moyen d'éviter la boucle externe `for` est d'utiliser la récursivité. On peut facilement écrire la fonction récursive `calculate(i)` qui produit la **i**ème ligne de la grille. Pour faire le travail, la fonction doit connaître la **(i-1)**ème ligne, donc elle s'appelle elle-même comme `calculate(i-1)` puis calcule la **i**ème ligne en utilisant les fonctions NumPy comme nous l'avons fait auparavant. Toute la boucle externe peut alors être remplacée par `calculate(N)`. Pour compléter le tableau, un solveur de sac à dos récursif peut être trouvé dans le code source accompagnant cet article sur [GitHub](https://github.com/mmamaev/looping_python/blob/master/ks_dp_solvers.py).

Cependant, l'approche récursive n'est clairement pas évolutive. Python n'est pas optimisé pour la récursivité terminale. La profondeur de la pile de récursivité est, par défaut, limitée à l'ordre de mille. Cette limite est sûrement conservative, mais lorsque nous exigeons une profondeur de millions, un débordement de pile est très probable. De plus, l'expérience montre que la récursivité ne fournit même pas un avantage de performance par rapport à un solveur basé sur NumPy avec la boucle externe `for`.

C'est là que nous épuisons les outils fournis par Python et ses bibliothèques (à ma connaissance). Si vous avez absolument besoin d'accélérer la boucle qui implémente un algorithme récursif, vous devrez recourir à Cython, ou à une version de Python compilée JIT, ou à un autre langage.

### Points clés

![Image](https://cdn-media-1.freecodecamp.org/images/1*YvnvnzC2wMwZ_EF3qFHBcg.png)
_Temps d'exécution des solveurs de problème de sac à dos_

* Effectuez des calculs numériques avec des fonctions NumPy. Elles sont deux ordres de grandeur plus rapides que les outils intégrés de Python.
* Parmi les outils intégrés de Python, la compréhension de liste est plus rapide que `map()`, qui est significativement plus rapide que `for`.
* Pour les algorithmes profondément récursifs, les boucles sont plus efficaces que les appels de fonctions récursives.
* Vous ne pouvez pas remplacer les boucles récursives par `map()`, la compréhension de liste ou une fonction NumPy.
* Le code « stupide » (décomposé en opérations élémentaires) est le plus lent. Utilisez des fonctions et outils intégrés.
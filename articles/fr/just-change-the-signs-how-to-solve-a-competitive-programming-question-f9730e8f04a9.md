---
title: 'Changer les signes : comment utiliser la programmation dynamique pour résoudre
  une question de programmation compétitive'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-01T22:00:05.000Z'
originalURL: https://freecodecamp.org/news/just-change-the-signs-how-to-solve-a-competitive-programming-question-f9730e8f04a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kdC2W2WKEjPIG1pRCk0qmg.png
tags:
- name: algorithms
  slug: algorithms
- name: Competitive programming
  slug: competitive-programming
- name: Dynamic Programming
  slug: dynamic-programming
- name: Problem Solving
  slug: problem-solving
- name: technology
  slug: technology
seo_title: 'Changer les signes : comment utiliser la programmation dynamique pour
  résoudre une question de programmation compétitive'
seo_desc: 'By Sachin Malhotra

  If you’re a competitive programmer like I am, one of the best feelings in the world
  is seeing your program getting accepted on first try on one of the most famous programming
  platforms, CodeChef.

  I was an avid competitive programme...'
---

Par Sachin Malhotra

Si vous êtes un programmeur compétitif comme moi, l'un des meilleurs sentiments au monde est de voir votre programme accepté du premier coup sur l'une des plateformes de programmation les plus célèbres, [CodeChef](https://www.codechef.com/).

J'étais un programmeur compétitif passionné pendant mes études de premier cycle, puis j'ai perdu le contact avec cela en travaillant comme développeur @Hike. Cependant, j'ai récemment replongé dans ce monde aventureux de la programmation, grâce à mon ami [Divya Godayal](https://www.freecodecamp.org/news/just-change-the-signs-how-to-solve-a-competitive-programming-question-f9730e8f04a9/undefined).

Le [CodeChef May 2018 Long Challenge](https://www.codechef.com/MAY18) s'est terminé il y a environ une heure, et j'ai décidé d'écrire cet article pour décrire l'une des questions de la compétition.

Sans perdre plus de temps, passons à cela.

![Image](https://cdn-media-1.freecodecamp.org/images/Y6UspCo7zHVxvZE-xRG3pERSJQy4CfD6EGU3)

### Comprendre l'énoncé du problème

Examinons quelques exemples pour mieux comprendre ce que l'énoncé du problème demande.

Considérons la séquence de nombres suivante.

```
4 3 1 2
```

La question nous demande d'effectuer une certaine opération (éventuellement 0 fois, laissant la séquence inchangée). Nous pouvons négativer une certaine sous-séquence de nombres et obtenir une nouvelle séquence.

```
-4 3 1 24 -3 1 -24 3 -1 24 3 1 -2-4 -3 1 2 etc.
```

La question indique que la séquence résultante doit satisfaire la contrainte suivante :

**La somme des éléments de toute sous-chaîne de longueur supérieure à 1 est strictement positive.**

Clairement, les séquences suivantes ne sont pas valides :

```
-4 3 1 24 -3 1 -2 4 3 1 -2 -4 -3 1 2 -4 -3 -1 -24 3 -1 -2
```

Nous n'avons que 2 sous-séquences valides qui peuvent être obtenues en effectuant l'opération mentionnée ci-dessus. **Note :** nous n'avons pas écrit toutes les sous-séquences possibles. Cela serait 2^n, soit 16 dans ce cas, car pour chaque nombre nous avons deux options. Soit le négativer, soit ne pas le faire.

Ainsi, les deux séquences valides sont :

```
4 3 1 2
```

et

```
4 3 -1 2
```

La séquence originale sera toujours l'une des séquences valides car tous les nombres qu'elle contient sont positifs.

La question nous demande maintenant de trouver la séquence avec la somme minimale. Ainsi, pour l'exemple que nous avons considéré, la séquence requise serait `4 3 -1 2`.

### Une approche gloutonne fonctionnerait-elle ?

Une approche gloutonne dans cette question serait, si possible, de négativer un nombre tout en satisfaisant les contraintes données, alors nous devrions négativer ce nombre. Cependant, cette approche ne donnerait pas toujours les bons résultats. Considérons l'exemple suivant.

```
4 1 3 2
```

Ici, il est possible d'avoir ces trois ensembles valides de nombres :

```
4 1 3 2           4 -1 3 2           4 1 3 -2
```

Clairement, les deux nombres 2 et 1 peuvent être négativés. Mais pas les deux en même temps. Si nous négativons un nombre de manière gloutonne — c'est-à-dire, si un nombre peut être négativé, alors nous le négativons — alors il est possible que nous finissions par négativer le nombre 1. Ensuite, vous ne pourrez pas négativer le nombre 2. Cela nous donnerait une solution sous-optimale.

Ainsi, cette approche gloutonne ne fonctionnerait pas ici. Nous devons **"essayer un choix spécifique de négativer ou non un nombre et voir quel choix nous donne la solution optimale"**.

Cela ressemble à de la programmation dynamique.

### La bonne vieille programmation dynamique

L'une des techniques algorithmiques les plus intéressantes qui existent, et probablement l'une des plus redoutées, est la programmation dynamique. C'est la technique que nous allons utiliser pour résoudre ce problème particulier.

Deux des étapes les plus importantes dans tout problème de programmation dynamique sont :

1. Identifier la relation récurrente.
2. Déterminer ce qu'il faut [**mémoïser**](https://www.interviewcake.com/concept/java/memoization)**. (pas memoRize :P)**

L'approche basée sur la DP ici est divisée en deux parties de base.

* L'une est la récursion principale que nous utilisons pour trouver la **somme minimale de l'ensemble final**. Notez que la programmation dynamique n'est pas directement utilisée pour obtenir l'ensemble final, juste la somme de l'ensemble final de nombres. Ainsi, notre approche de programmation dynamique trouverait correctement la somme pour l'exemple donné ci-dessus comme 8. `4 + 3 + (-1) + 2 = 8`.
* Ce dont nous avons vraiment besoin, c'est l'ensemble final modifié de nombres où certains (éventuellement aucun) des nombres sont négativés. Nous utilisons le concept de **pointeur parent** et de **retour en arrière** pour trouver l'ensemble réel de nombres.

Passons à notre relation de récursion pour notre approche de programmation dynamique.

Avant de décrire la relation récurrente, une observation importante à faire ici est que si un nombre a été négativé, **alors aucun nombre adjacent ne peut être négatif**. C'est-à-dire que deux nombres adjacents ne peuvent pas être négatifs car cela donnerait une sous-chaîne de longueur 2 dont la somme est négative, et cela n'est pas autorisé selon la question.

Pour la relation de récurrence, nous avons besoin de deux variables. L'une est le numéro d'index de l'endroit où nous nous trouvons dans le tableau, et l'autre est une valeur booléenne qui nous indique si le nombre précédent (un à gauche du nombre précédent) est négativé ou non. Ainsi, si l'index actuel est `i`, alors la valeur booléenne nous indiquera si le nombre à `i — 2` était négativé ou non. Vous connaîtrez l'importance de cette variable booléenne dans le paragraphe suivant.

Nous devons savoir en `O(1)` si un nombre **peut** être négativé ou non. Puisque nous suivons une récursion avec une solution basée sur la mémoïsation, chaque fois que nous sommes à un index `i` dans la récursion, nous sommes sûrs que les nombres à droite (`i+ 1` et au-delà) n'ont pas été traités jusqu'à ce point. Cela signifie que tous sont encore positifs.

Le choix de savoir si le nombre à l'index `i` peut être négativé dépend du côté droit (s'il y en a un) et du côté gauche (s'il y en a un). Le côté droit est facile. Tout ce que nous devons vérifier est si

```
number[i] < number[i + 1]
```

car si ce n'est pas vrai, alors l'addition de ces deux donnerait une valeur négative pour la sous-chaîne `[i, i + 1]` rendant ainsi l'opération invalide.

Maintenant vient la partie délicate. Nous devons voir si la négation du nombre à `i` provoquera une sous-chaîne de somme négative à gauche ou non. Lorsque nous atteignons l'index `i` dans notre récursion, nous avons déjà traité les nombres avant celui-ci, et certains ont pu être négativés également.

Ainsi, supposons que nous avons cet ensemble de nombres `4 1 2 1` et que nous avons négativé le premier `1` et que nous traitons maintenant le dernier nombre (`1`).

```
4 -1 2 [1]
```

Le dernier nombre entre crochets est celui que nous traitons actuellement. En ce qui concerne le côté droit, puisque il n'y en a pas, nous pouvons le négativer. Nous devons vérifier si la négation de ce 1 à l'index 3 (indexation basée sur 0) provoquerait une sous-chaîne à gauche de somme ≤ 0. Comme vous pouvez le voir, cela produirait une telle sous-chaîne.

```
-1 2 -1
```

Cette sous-chaîne aurait une somme de 0, et cela est invalide selon la question. Après avoir négativé une sous-séquence de nombres, les sous-chaînes dans l'ensemble final doivent avoir une somme strictement positive. Toutes les sous-chaînes de longueur > 1.

Nous ne pouvons pas appliquer directement l'approche suivante ici :

```
if number[i] < number[i - 1], alors il est bon de procéder à la négation.
```

car, bien que `1 <`; 2, si nous négativons également ce dernier 1, nous aurons un ensemble invalide de nombres comme vu ci-dessus. Ainsi, cette approche simple ou cette vérification ne fonctionnera pas ici.

Voici la variable booléenne qui nous indique si, étant donné un index `i`, le nombre à `i — 2` était négativé ou non. Considérons les deux scénarios.

* Oui, le nombre à l'index `i — 2` était négativé comme dans l'exemple juste présenté. Dans ce cas, la négation du nombre à `i — 2` aurait une réduction de capacité pour le nombre à `i — 1`. Dans l'exemple `4 1 2 1`, la négation du 1 à l'index 1 (indexation basée sur 0) réduirait la capacité du nombre 2 (à l'index 2) de 1. Nous faisons référence aux valeurs restantes des nombres comme capacités ici. Nous devons considérer cette capacité réduite lors de la vérification pour voir si un nombre peut être négativé ou non.

```
number[i] < reducedCapacityOfNumberAt(i - 1)
```

* Dans le cas où le nombre à l'index `i — 2` n'était pas négativé, le nombre à `i — 1` est à sa pleine capacité. La simple vérification

```
number[i] < number[i - 1]
```

serait suffisante pour voir si nous pouvons négativer le nombre à l'index `i`.

Regardons le code pour la récursion contenant toutes les idées discutées ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/a4tshHUm1WyoHHO0hK-050EfDySLR3KHVwzY)

C'est bien et joli. Mais ce n'est que de la récursion, et le titre dit programmation dynamique. Cela signifie qu'il y aurait des sous-problèmes chevauchants. Regardons l'arbre de récursion pour voir s'il y en a.

![Image](https://cdn-media-1.freecodecamp.org/images/-6EItwtVtgzqUHrsbEJODoMoxV2woN6iN7Nv)

Comme vous pouvez le voir, il y a des sous-problèmes chevauchants dans l'arbre de récursion. C'est pourquoi nous pouvons utiliser la mémoïsation.

La mémoïsation est aussi simple que :

```
""" Cela vient en haut. Nous vérifions si l'état représenté par le tuple de l'index et de la variable booléenne est déjà mis en cache """
```

```
if(memo[i][is_prev_negated] != INF) {    return memo[i][is_prev_negated];}
```

```
...... CODE
```

```
# Mettre en cache la somme minimale à partir de cet index.memo[i][is_prev_negated] = min(pos, neg);
```

```
# Le pointeur parent est utilisé pour trouver l'ensemble final de #sparent[i][is_prev_negated] = min(pos, neg) == pos ? 1 : -1;
```

Comme souligné précédemment, cette approche récursive retournerait la somme minimale de l'ensemble de nombres possible après avoir effectué l'ensemble valide de modifications.

La question, cependant, nous demande d'imprimer réellement l'ensemble final de nombres qui donne la somme minimale après avoir effectué de telles modifications. Pour cela, nous devons utiliser un pointeur parent qui nous indiquerait à chaque index et à la valeur de la variable booléenne `is_prev_negated` quelle action optimale a été prise.

```
parent[i][is_prev_negated] = min(pos, neg) == pos ? 1 : -1;
```

Ainsi, nous stockons simplement 1 ou -1 selon que la négation du nombre à l'index i (si possible !) nous a donné la somme minimale ou si le choix de l'ignorer a donné la somme minimale.

### Retour en arrière

Maintenant vient la partie où nous faisons un retour en arrière pour trouver la solution à notre problème original. Notez que la décision pour le tout premier nombre est ce qui propage la récursion plus loin. Si le premier nombre était négativé, le deuxième nombre serait positif et la décision du troisième nombre pourrait être trouvée en utilisant `parent[2][true]`. De même, si le premier nombre n'était pas négativé, alors nous passons au deuxième nombre et sa décision peut être trouvée en utilisant `parent[1][false]` et ainsi de suite. Regardons le code.

![Image](https://cdn-media-1.freecodecamp.org/images/-rimpa-Iqfb1y22u7qbQZgjxkU-A2ziBQZrW)

### Une meilleure approche

Si vous regardez la complexité spatiale de la solution suggérée, vous verrez qu'il s'agit d'une solution de programmation dynamique à deux dimensions car l'état de la récursion est représenté par deux variables, c'est-à-dire l'index `i` représentant quel nombre du tableau nous considérons et ensuite la variable booléenne `is_prev_negated`. Ainsi, la complexité spatiale et la complexité temporelle seraient O(n*2) ce qui est essentiellement O(n).

Cependant, il existe également une approche légèrement meilleure pour résoudre ce problème, comme suggéré par [Divya Godayal](https://www.freecodecamp.org/news/just-change-the-signs-how-to-solve-a-competitive-programming-question-f9730e8f04a9/undefined). Ce problème peut même être résolu par une solution basée sur la programmation dynamique à une dimension.

Essentiellement, la variable booléenne `is_prev_negated` nous aide à décider si nous pouvons négativer un nombre donné à l'index `i` ou non en ce qui concerne le côté gauche du tableau, c'est-à-dire `tous les nombres de 0 .. i-1` car le côté droit est de toute façon sûr car tous les nombres de ce côté sont positifs (car la récursion ne les a pas encore atteints). Ainsi, pour le côté droit, nous avons simplement vérifié le nombre à `i+1` mais pour le côté gauche de l'index `i`, nous avons dû utiliser la variable booléenne `is_prev_negated`.

Il s'avère que nous pouvons simplement sauter cette variable booléenne et simplement regarder devant pour décider si un nombre peut être négativé ou non. Ce qui signifie simplement que si vous êtes à un index `i`, vous vérifiez si cet élément ainsi que l'élément à `i+2` ont la capacité d'absorber l'élément à `i+1`, c'est-à-dire.

```
numbers[i] + numbers[i+2] >= numbers[i+1  (SWALLOW)
```

S'il y a une telle possibilité, alors nous sautons directement à `i+3` si nous négativons l'élément à `i` car l'élément à `i+1` et `i+2` ne peuvent pas être négatifs dans un tel scénario.

Dans le cas où la condition d'absorption n'est pas satisfaite et que nous finissons par négativer le nombre à l'index `i`, alors nous sauterions à l'index `i+2` car dans tous les cas, deux nombres consécutifs ne peuvent pas être négativés. Ainsi, si le nombre à `i` était négativé, alors le nombre à `i+1` doit être positif. La vérification d'absorption est de voir si le nombre à `i+2` devrait définitivement être positif ou si nous pouvons exercer le choix de le négativer ou non.

Jetez un coup d'œil au code pour une meilleure compréhension.

![Image](https://cdn-media-1.freecodecamp.org/images/xfOALns0BeiZRPCX-3eL6gpcwxRQu4DCn0W7)

Ainsi, une seule variable, c'est-à-dire l'index, est utilisée pour définir l'état de la récursion. Ainsi, la complexité temporelle et spatiale a été réduite de moitié par rapport à ce qu'elle était dans la solution précédente.

J'espère que vous avez pu comprendre le fonctionnement de l'algorithme décrit ci-dessus et comment la technique de programmation dynamique s'intègre dans ce problème. Je pense que c'est un problème intéressant, car vous devez non seulement utiliser la programmation dynamique mais aussi le concept de pointeur parent pour retracer les étapes à travers la solution optimale et obtenir la réponse requise dans la question.
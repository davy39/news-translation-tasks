---
title: 'Permutation vs Combinaison : Quelle est la différence entre la formule de
  permutation et la formule de combinaison ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-21T21:46:28.000Z'
originalURL: https://freecodecamp.org/news/permutation-vs-combination-what-is-the-difference-between-the-permutation-formula-and-the-combination-formula
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e91740569d1a4ca3dca.jpg
tags:
- name: algorithms
  slug: algorithms
- name: beginners guide
  slug: beginners-guide
- name: combinatorics
  slug: combinatorics
- name: education
  slug: education
- name: Math
  slug: math
seo_title: 'Permutation vs Combinaison : Quelle est la différence entre la formule
  de permutation et la formule de combinaison ?'
seo_desc: "By Neil Kakkar\nHere's the short version.\nLet's take ringing bells in\
  \ a church as an example. \nA permutation is an ordering of the bells. You're figuring\
  \ out the best order to ring them in.\nA combination is the choice of bells. You're\
  \ choosing the bel..."
---

Par Neil Kakkar

Voici la version courte.

Prenons le son des cloches dans une église comme exemple. 

Une permutation est un ordre des cloches. Vous essayez de trouver le meilleur ordre pour les sonner.

Une combinaison est le choix des cloches. Vous choisissez les cloches à sonner. Si vous avez trop de cloches, vous devez d'abord les choisir, puis penser à les ordonner.

Cela donne lieu à l'identité familière : `(n P r) = (n C r) * r!`

La façon d'ordonner `r` éléments parmi `n` est de d'abord choisir `r` éléments parmi `n`, puis d'ordonner les `r` éléments (`r!` )

Et, cela signifie que `(n P r) = n! / (n-r)!` et `(n C r) = n! / ( (n-r)! * r! )` 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/ncr.jpg)

**Mais voulez-vous savoir comment vous en souvenir pour toujours ?**

Je suis un grand fan de la [pensée par premiers principes](https://neilkakkar.com/A-framework-for-First-Principles-Thinking.html). Pour comprendre un problème, il faut en saisir le cœur et raisonner à partir de là.

Ne pas faire cela est généralement source de confusion : si je ne comprends pas comment les choses fonctionnent, je ne sais pas où accrocher les concepts. Mon cadre mental n'est pas complet, alors je décide de simplement m'en souvenir.

Comme vous pouvez l'imaginer, ce n'est pas idéal. Alors, de temps en temps, je m'adonne à un exercice consistant à déduire les choses de la source et à construire une intuition sur leur fonctionnement.

Cette fois-ci, nous construisons une intuition pour les permutations et les combinaisons.

Par exemple, savez-vous pourquoi la formule d'une combinaison est (n C r) ? D'où cela vient-il ? Et pourquoi utilise-t-on des factoriels ici ?

Commençons par la source. Les factoriels, les permutations et les combinaisons sont nés de mathématiciens jouant ensemble, un peu comme Steve Jobs et Steve Wozniak ont fondé Apple en jouant ensemble dans leur garage.

Tout comme Apple est devenue une entreprise rentable à part entière, le simple factoriel, `!`, est devenu l'atome d'un domaine entier des mathématiques : la [combinatoire](https://en.wikipedia.org/wiki/Combinatorics).

Oubliez tout, commençons à réfléchir depuis le bas.

Le premier cas d'utilisation intéressant connu venait des églises au 17ème siècle.

Vous êtes-vous déjà demandé comment les cloches sont sonnées dans les églises ? Il y a une machine qui les "sonne" dans l'ordre. Nous sommes passés aux machines parce que les cloches sont trop grandes. De plus, il y a des tonnes de cloches.

Comment les gens ont-ils trouvé la meilleure séquence pour les sonner ? Et s'ils voulaient changer les choses ? Comment pouvaient-ils trouver le meilleur son ? Chaque clocher avait jusqu'à 16 cloches !

Vous ne pouviez pas changer la rapidité à laquelle vous pouviez sonner une cloche - les machines ne sonnaient qu'une cloche par seconde. La seule chose que vous pouviez faire était de [changer](https://en.wikipedia.org/wiki/Change_ringing) l'ordre des cloches. Ainsi, ce défi consistait à trouver le meilleur ordre. 

Pourrions-nous, en cours de route, également trouver tous les ordres possibles ? Nous voulons connaître tous les ordres possibles pour savoir s'il vaut la peine de tous les essayer.

Un sonneur de cloches, [Fabian Stedman](https://en.wikipedia.org/wiki/Fabian_Stedman), a relevé ce défi.

Il a commencé avec 2 cloches. Quels étaient les différents ordres dans lesquels il pouvait sonner ces cloches ?[1]

1 et 2.
ou
2 et 1.

Cela avait du sens. Il n'y avait pas d'autre façon.

Et avec 3 cloches ?

1, 2, et 3.  
1, 3, et 2.

Ensuite, en commençant par la deuxième cloche,

2, 1, et 3.  
2, 3, et 1.

Ensuite, en commençant par la troisième cloche,

3, 1, et 2.  
3, 2, et 1.

Total, 6.

Il a alors réalisé que cela était très similaire à deux cloches !

S'il fixait la première cloche, alors le nombre de façons d'ordonner les deux cloches restantes était *toujours* deux. 

Combien de façons pouvait-il fixer la première cloche ? N'importe laquelle des 3 cloches pouvait être celle-là !

D'accord, il a continué. Il est ensuite passé à 5 cloches.

C'est à ce moment-là qu'il a réalisé que faire les choses à la main était fastidieux. Vous n'avez que tant de temps dans la journée, vous devez sonner les cloches, vous ne pouvez pas rester coincé à dessiner toutes les cloches possibles. Y avait-il un moyen de trouver cela rapidement ?

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5bells-2.jpg)

Il est revenu à son intuition.

S'il avait 5 cloches et qu'il fixait la première cloche, tout ce qu'il avait à faire était de trouver comment ordonner 4 cloches.

Pour 4 cloches ? Eh bien, s'il avait 4 cloches et qu'il fixait la première cloche, tout ce qu'il avait à faire était de trouver comment ordonner 3 cloches.

Et il savait comment faire cela !

Ainsi, l'ordonnancement de 5 cloches = 5 * ordonnancement de 4 cloches.

Ordonnancement de 4 cloches = 4 * ordonnancement de 3 cloches

Ordonnancement de 3 cloches = 3 * ordonnancement de 2 cloches.

.. Vous voyez le schéma, n'est-ce pas ?

> Fait amusant : C'est la clé d'une technique de programmation appelée [récursion](https://en.wikipedia.org/wiki/Recursion). 

Il l'a fait aussi. Bien que cela lui ait pris beaucoup plus de temps, car personne près de lui n'avait déjà découvert cela.[2]

Ainsi, il a compris que l'ordonnancement de 5 cloches = `5 * 4 * 3 * 2 * 1`.

Cette formule d'ordonnancement, en 1808, est devenue connue sous le nom de factorielle.

Nous pensons à la notation factorielle comme à la base, mais l'idée existait bien avant qu'elle n'ait un nom. Ce n'est que lorsque le mathématicien français Christian Kramp a remarqué qu'elle était utilisée dans quelques endroits qu'il l'a nommée la factorielle.

Cet ordonnancement des cloches est appelé une permutation.

> Une permutation est un ordonnancement d'éléments.



Lorsque l'on apprend quelque chose, je pense qu'il est utile de regarder les choses sous tous les angles pour solidifier la compréhension.

Et si nous essayions de dériver la formule ci-dessus directement, sans essayer de réduire le problème à un nombre plus petit de cloches ?  
  
Nous avons 5 espaces, n'est-ce pas ?

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells.jpg)

Combien de façons pouvons-nous choisir la première cloche ? `5`, car c'est le nombre de cloches que nous avons.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_1filled.jpg)

  
La deuxième cloche ? Eh bien, nous avons utilisé une cloche lorsque nous l'avons placée dans la première position, donc il nous reste 4 cloches.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_2filled.jpg)

  
La troisième cloche ? Eh bien, nous avons choisi les deux premières, donc il ne reste que 3 cloches parmi lesquelles choisir.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_3filled.jpg)

  
La quatrième cloche ? Seulement 2 cloches restantes, donc 2 options.   
La cinquième cloche ? Une seule restante, donc 1 option.  


![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_5filled.jpg)

Et voilà, le nombre total d'ordonnancements est `5 * 4 * 3 * 2 * 1`

Ainsi, nous avons notre première formule générale. 

> Le nombre de façons d'ordonner `N` éléments est `N!`


# La Permutation

Maintenant, nous sommes confrontés à un problème différent. Le roi a ordonné que de nouvelles cloches soient fabriquées pour chaque église. Certaines sont agréables, d'autres sont correctes, d'autres vous rendront sourd. Mais chacune est unique. Chaque cloche produit son propre son. Une cloche assourdissante entourée de belles cloches peut sonner majestueuse.

Mais, notre clocher ne contient toujours que 5 cloches, donc nous devons trouver le meilleur ordonnancement parmi les 8 cloches que les habiles fabricants de cloches ont fabriquées.

En utilisant la logique ci-dessus, nous pouvons procéder.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesFor8Bells-1.jpg)

Pour la première cloche, nous pouvons choisir n'importe laquelle des 8 cloches.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_1filled_8bells.jpg)

  
Pour la deuxième cloche, nous pouvons choisir n'importe laquelle des 7 cloches restantes... et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/5spacesForBells_5filled_8bells.jpg)

  
À la fin, nous obtenons `8 * 7 * 6 * 5 * 4` ordonnancements possibles de 8 cloches dans 5 espaces.

Si vous êtes familier avec la version formule de (n P r), qui est `n! / (n-r)!`, ne vous inquiétez pas, nous allons également la dériver bientôt !

Une mauvaise façon de la dériver est de multiplier à la fois le numérateur et le dénominateur par 3! dans notre exemple ci-dessus -

nous obtenons `8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 / 3 * 2 * 1` = ` 8! / 3!`.

Mais cela ne nous aide pas à comprendre pourquoi cette formule fonctionne. Avant d'y arriver, examinons le choix des choses, ou la Combinaison.

# La Combinaison

Maintenant que nous savons comment ordonner les choses, nous pouvons découvrir comment les choisir !

Considérons le même problème. Il y a un clocher avec 5 cloches, et vous avez 8 cloches. Cependant, pour l'instant, vous ne voulez pas déterminer l'ordre des cloches (rappelons que c'est ce qu'est une permutation).

Au lieu de cela, vous voulez choisir les 5 meilleures cloches, et laisser quelqu'un d'autre avec un meilleur goût pour la musique déterminer l'ordre. En effet, nous divisons le problème en deux parties : d'abord, nous déterminons quelles cloches choisir. Ensuite, nous déterminons comment ordonner les cloches choisies.

Comment choisissez-vous les cloches ? C'est la "combinaison" des permutations et combinaisons.

La combinaison est une sélection. Vous êtes sélectif. Vous choisissez 5 cloches parmi les 8 que vos artisans ont fabriquées.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/8bells_inline.jpg)

Puisque nous savons comment ordonner les cloches, nous allons utiliser cette information pour déterminer comment choisir les cloches. Cela semble impossible ? Attendez de voir les belles mathématiques impliquées.

Imaginons que toutes les cloches sont alignées.

Avant de trouver toutes les façons de choisir les cloches, concentrons-nous sur une façon de choisir les cloches.

Une façon est de choisir n'importe lesquelles des 5 au hasard. Cela ne nous aide pas beaucoup à résoudre le problème, alors essayons une autre façon.

Nous mettons les cloches en ligne et choisissons les 5 premières. C'est une façon de choisir les cloches.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/8bells_inline_choose5.jpg)

Remarquez que, même si nous échangeons les positions des 5 premières cloches, le choix ne change pas. Ce sont toujours les mêmes 5 cloches uniques.

Cela est également vrai pour les trois dernières cloches.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/8bells_inline_choose5_permute.jpg)

Maintenant, le beau truc mathématique - pour cette façon de choisir les 5 cloches, quels sont tous les ordonnancements de 8 cloches où nous choisissons exactement ces 5 cloches ? D'après l'image ci-dessus, ce sont tous les ordonnancements des 5 cloches (`5!`) et tous les ordonnancements des 3 cloches restantes (`3!`).

Ainsi, pour chaque façon de choisir 5 cloches, nous avons (`5! * 3!`) ordonnancements de 8 cloches.

Quels sont les ordonnancements totaux possibles de 8 cloches ? `8!`.

Rappelons que pour chaque choix des 5 premières cloches, nous avons (`5! * 3!`) ordonnancements de 8 cloches qui donnent le même choix.

Alors, si nous multiplions le nombre de façons de choisir les 5 premières cloches par tous les ordonnancements possibles d'un choix, nous devrions obtenir le nombre total d'ordonnancements. 

```
Façons de choisir 5 cloches * ordonnancements d'un choix = Ordonnancements totaux
```

Donc, 

```
Façons de choisir 5 cloches = les ordonnancements totaux possibles / ordonnancements totaux d'un choix.
```

En mathématiques, cela devient :

```
(8 C 5) = 8! / ( 5! * 3!)
```
Et voilà, nous avons trouvé une explication intuitive pour choisir 5 choses parmi 8.


Maintenant, nous pouvons généraliser cela. Si nous avons N choses, et que nous voulons en choisir R, cela signifie que nous traçons une ligne à R.

Ce qui signifie que les éléments restants seront `N-R`. Donc, pour un choix de `R` éléments, nous avons `R! * (N-R)!` ordonnancements qui donnent les mêmes `R` éléments.


![Image](https://www.freecodecamp.org/news/content/images/2019/12/nSpacesForBells.jpg)

Pour toutes les façons de choisir `R` éléments, nous avons `N! / (R! * (N-R)!)` possibilités.


> Le nombre de façons de choisir `r` éléments parmi `n` est `(n C r) = n! / (r! * (n-r)!)`


En termes familiers, (n C r) se prononce également `n choisir r`, ce qui aide à solidifier l'idée que les combinaisons sont pour choisir des éléments.

# La Permutation - revisitée

Maintenant que la combinaison est faite, revenons à la partie 2 de notre travail. Notre cher ami a choisi les 5 meilleures cloches en déterminant toutes les combinaisons possibles de 5 cloches.

C'est maintenant à nous de trouver la mélodie parfaite en déterminant le nombre d'ordonnancements.

Mais, c'est la partie facile. Nous savons déjà comment ordonner 5 éléments. C'est `5!`, et nous avons terminé.

Ainsi, pour permuter (ordonner) 5 éléments parmi 8, nous choisissons d'abord 5 éléments, puis nous ordonnons les 5 éléments.

En d'autres termes, 

```
(8 P 5) = (8 C 5) * 5!
```

Et si nous développons la formule, `(8 P 5) = (8! / ( 5! * 3!)) * 5!`

`(8 P 5) = 8! / 3!`.

Et, nous avons fait le tour complet de notre formule originale, dérivée correctement.

> Le nombre de façons d'ordonner `r` éléments parmi `n` est `(n P r) = n! / (n-r)!`

# Différence entre permutation et combinaison

J'espère que cela rend la différence entre les permutations et les combinaisons cristalline.

Les permutations sont des ordonnancements, tandis que les combinaisons sont des choix.

Pour ordonner N éléments, nous avons trouvé deux façons intuitives de déterminer la réponse. Les deux mènent à la réponse, `N!`.

Pour permuter 5 éléments parmi 8, vous devez d'abord choisir les 5 éléments, puis les ordonner. Vous choisissez en utilisant `(8 C 5)`, puis vous ordonnez les 5 en utilisant `5!`.

Et l'intuition pour choisir `R` parmi `N` est de déterminer tous les ordonnancements (`N!`) et de diviser par les ordonnancements où les premiers `R` et les derniers `N-R` restent les mêmes (`R!` et `(N-R)!`).

Et, c'est tout ce qu'il y a à savoir sur les permutations et les combinaisons.

Toutes les permutations et combinaisons avancées utilisent cela comme base. Combinaison avec remplacement ? Même idée. Permutation avec des éléments identiques ? Même idée, seul le nombre d'ordonnancements change, car certains éléments sont identiques.

Si vous êtes intéressé, nous pouvons aborder les cas complexes dans un autre exemple. Faites-le moi savoir [sur Twitter](https://twitter.com/neilkakkar).

> Consultez plus de publications sur [mon blog](https://neilkakkar.com/), et rejoignez la [liste de diffusion hebdomadaire](https://neilkakkar.com/subscribe/).

## Notes de fin

1. C'est ainsi que j'imagine qu'il a compris les choses. Ne le prenez pas comme une leçon d'histoire.
2. Les Indiens l'avaient, au 12ème siècle, 400 ans avant lui.
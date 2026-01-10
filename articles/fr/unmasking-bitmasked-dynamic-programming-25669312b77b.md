---
title: Démasquer la programmation dynamique par masquage de bits
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-03T16:38:18.000Z'
originalURL: https://freecodecamp.org/news/unmasking-bitmasked-dynamic-programming-25669312b77b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h4NHSLyn2d1I1hNTCsYDhw.png
tags:
- name: algorithms
  slug: algorithms
- name: leetcode
  slug: leetcode
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Démasquer la programmation dynamique par masquage de bits
seo_desc: 'By Sachin Malhotra

  How to go from Fearing it to Conquering it!



  There are no coincidences in this world.

  — Grand Master Oogway


  Well, Master Oogway, no disrespect, coincidences do occur and I think they are just
  God’s way of remaining anonymous. Not...'
---

Par Sachin Malhotra

#### Comment passer de la peur à la conquête !

![Image](https://cdn-media-1.freecodecamp.org/images/1*h4NHSLyn2d1I1hNTCsYDhw.png)

> Il n'y a pas de coïncidences dans ce monde.

> ** Grand Maître Oogway**

Eh bien, Maître Oogway, sans vouloir manquer de respect, les coïncidences existent et je pense qu'elles sont simplement la manière qu'a Dieu de rester anonyme. Ce n'est pas seulement moi qui le pense, Albert Einstein le croit aussi ?.

111, ce n'est pas vraiment mon _nombre chanceux_, pour ainsi dire.

Cependant, ce nombre m'a rempli de joie et d'extase lorsque je l'ai vu comme mon rang sur la page des classements du concours [LeetCode](https://leetcode.com/contest/weekly-contest-111) numéro 111.

Quelle coïncidence !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lhw6zJiM5sZwaQ7Z7VlOLQ.png)

C'est le meilleur classement dans un concours hebdomadaire que j'ai réussi à obtenir jusqu'à présent sur la plateforme. Le numéro du concours et le classement étaient évidemment une pure coïncidence.

Le concours consiste généralement en un problème facile, deux problèmes de niveau moyen et un problème difficile.

Plus souvent qu'autrement, le problème difficile est quelque chose qui nécessite beaucoup de connaissances algorithmiques et de pratique préalable pour pouvoir le résoudre pendant le concours. Le problème final de ce concours n'a pas fait exception à cette règle.

Pourquoi dis-je qu'il était très difficile ? Jetez un coup d'œil au nombre de personnes qui ont réussi à le résoudre pendant le concours.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YLg5aPTagh8k4L9M9FkVOw.png)

Comme le suggère le titre de l'article, ce problème devait être résolu en utilisant la programmation dynamique basée sur le masquage de bits.

La _programmation dynamique_ est l'un des domaines algorithmiques les plus redoutés. Elle nécessite beaucoup de pratique pour développer une intuition sur une solution basée sur la programmation dynamique pour un problème. J'ai toujours considéré cela comme une amélioration d'une solution récursive à un problème. L'idée principale derrière la programmation dynamique en termes profanes est :

> Éviter les calculs répétés en mettant en cache les résultats.

Le _masquage de bits_ en tant que sujet en programmation informatique est quelque chose que j'ai (et je suis sûr que de nombreux autres développeurs aussi) craint pendant longtemps. C'est l'un de ces sujets qui vous déséquilibrera sûrement lors d'un entretien et vous vaudra un rejet.

Les programmeurs ont généralement tendance à éviter de pratiquer des problèmes liés à ce sujet simplement parce qu'il est difficile de développer une intuition à ce sujet.

Les optimisations liées aux manipulations de bits se produisent dans les endroits les plus inattendus. Avec un peu de pratique, j'ai pu surmonter la _peur_, pour ainsi dire, de travailler sur des problèmes de programmation basés sur le masquage de bits.

Dans cet article, en plus de décrire la solution du problème que j'ai mentionné ci-dessus en détail, je vais également passer en revue quelques bases du masquage de bits et quelques problèmes de programmation où il peut être utile.

Comme pour toute nouvelle chose que vous apprenez, il est très difficile de retenir les concepts théoriques liés au masquage de bits. La rétention est meilleure lorsqu'elle vient par la pratique. C'est le principal objectif de cet article. Jetons un coup d'œil rapide à la table des matières avant de commencer l'article principal.

### Prenez un _peu_ de chocolat chaud et soyez prêt pour ...

* [0 1 Qu'est-ce que la manipulation de bits ? 0 1](https://medium.com/p/25669312b77b#ea86)
* [Les bases ](https://medium.com/p/25669312b77b#ee57)
* [Compter le nombre de bits définis](https://medium.com/p/25669312b77b#c94f)
* [Masquage et démasquage d'un bit spécifique](https://medium.com/p/25669312b77b#245e)
* [? Nombre manquant ?](https://medium.com/p/25669312b77b#927e)
* [?? Compter les bits ?? ??](https://medium.com/p/25669312b77b#14da)
* [ Produit maximum des longueurs de mots ](https://medium.com/p/25669312b77b#e86c)
* [Représentation de l'ensemble utilisant le masquage de bits](https://medium.com/p/25669312b77b#a050)
* [??Partitionner le tableau en K sous-ensembles de somme égale ??](https://medium.com/p/25669312b77b#a510)
* [? Trouver la plus courte superchaîne ?](https://medium.com/p/25669312b77b#1c4c)
* [Conclusion ??](https://medium.com/p/25669312b77b#322f)
* [Références ?](https://medium.com/p/25669312b77b#0017)

### 0 1 Qu'est-ce que la manipulation de bits ? 0 1

> Un bit est pour le monde informatique ce qu'un atome est pour la vie humaine.

Un bit est essentiellement la plus petite unité de stockage dans un ordinateur. C'est la seule unité qu'un ordinateur comprend.

La seule information qu'un bit peut stocker est formée de deux états différents : 0 et 1. Tout type de calcul qu'un ordinateur effectue est essentiellement une forme de manipulation de bits.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7BiK3Ininix3obYJgNXSJA.png)

Regardons une définition de [_Wikipedia_](https://en.wikipedia.org/wiki/Bit_manipulation) pour la manipulation de bits :

> La manipulation de bits est l'acte de manipuler algorithmiquement des bits ou d'autres morceaux de données plus courts qu'un mot. Les tâches de programmation informatique qui nécessitent une manipulation de bits incluent le contrôle de périphériques de bas niveau, les algorithmes de détection et de correction d'erreurs, la compression de données, les algorithmes de chiffrement et l'optimisation. Pour la plupart des autres tâches, les langages de programmation modernes permettent au programmeur de travailler directement avec des abstractions au lieu des bits qui représentent ces abstractions.

En termes d'implémentation, l'une des optimisations de bas niveau les plus utiles et efficaces pour un algorithme est la manipulation de bits.

Dans certains cas, la manipulation de bits peut contourner la boucle sur une structure de données et donner des améliorations de vitesse multiples. Le seul inconvénient de telles optimisations est la lisibilité et la maintenance du code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S9DTvKGpg1JcOF15XYAATQ.png)
_Qui a écrit ce morceau de code de merde (lire : ultra-rapide) ?_

C'est un morceau de code effrayant [code](https://medium.freecodecamp.org/lets-backtrack-and-save-some-queens-1f9ef6af5415) 

### Les bases 

Au cœur de la manipulation de bits se trouvent les opérateurs bit à bit :

* Et (&)
* Ou (|)
* Non (~)
* XOR (^)

Ce sont les opérateurs fondamentaux que nous utilisons pour effectuer certaines opérations compliquées de manipulation de bits. Par conséquent, il est très important de se rafraîchir la mémoire sur ces opérateurs et leurs tables de vérité avant de passer à des choses plus intéressantes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*deg14AeGo8SQWq8uwCVZmQ.png)
_Source : [https://www.topcoder.com](https://www.topcoder.com" rel="noopener" target="_blank" title=")_

Les tables de vérité montrent les résultats pour ces opérateurs lorsqu'ils opèrent sur 2 bits représentés par `A` et `B`. L'ordinateur doit traiter bien plus qu'un seul bit de données.

Les données traitées par le système sont généralement en octets ou en kilooctets ou plus. Comment ces opérateurs fonctionnent-ils sur des opérandes représentés par, par exemple, 8 bits ou 16 bits ? Dans un tel scénario, les opérations sont les mêmes, sauf qu'elles opèrent sur chaque bit des arguments. Considérons un exemple simple pour clarifier cela.

```
A = 11101010B = 00110101
```

```
+-+-+-+-  ET  -+-+-+-+A & B = 00100000
```

```
+-+-+-+-  OU   -+-+-+-+A | B = 11111111
```

```
+-+-+-+-  NON  -+-+-+-+~A    = 00010101
```

```
+-+-+-+-  XOR  -+-+-+-+A ^ B = 11011111
```

En plus de ces 4 opérateurs de base, il existe deux autres ensembles d'opérateurs bit à bit qui s'avèrent très pratiques. Presque tous les problèmes que nous allons examiner dans cet article en feront usage pour donner un énorme coup de pouce à la vitesse de calcul. Il s'agit des opérateurs de décalage à gauche `&l`t;< et de décalage à droite >>.

Simplement dit, l'opérateur de décalage à gauche signifie multiplier un nombre par 2 et l'opérateur de décalage à droite signifie diviser un nombre par 2.

Regardons une simple animation pour montrer pourquoi ces opérateurs sont appelés `décalage à gauche` et `décalage à droite` respectivement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GtkdWOFKMEGrzvYzsK9pZg.gif)
_Opération de décalage à gauche en action._

Pour démontrer l'opération de décalage à gauche, nous commençons par le nombre décimal `1` et le multiplions ensuite par 2. Comme vous pouvez le voir dans la représentation binaire des nombres résultants, le seul `1` dans la représentation continue de se décaler vers la gauche, une étape à la fois. C'est pourquoi on l'appelle l'opération de _décalage à gauche_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EM9AEq3brodEgJRL-annkQ.gif)
_Opération de décalage à droite en action._

De la même manière, pour démontrer l'opération de décalage à droite, nous commençons par le nombre décimal `128` et le divisons ensuite par 2. Comme vous pouvez le voir dans la représentation binaire des nombres résultants, le seul `1` dans la représentation continue de se décaler vers la droite, une étape à la fois. C'est pourquoi on l'appelle l'opération de _décalage à droite_.

Maintenant que nous sommes tous familiarisés avec les opérateurs binaires de base, passons à quelques cas d'utilisation simples pour ces opérateurs. Nous allons examiner quelques exemples ci-dessous. Ce ne sont pas des problèmes de programmation en eux-mêmes, cependant, ils sont souvent utilisés comme blocs de construction dans de nombreux algorithmes.

### Cas d'utilisation de base ?

#### Compter le nombre de bits définis

L'une des utilités de base des opérateurs que nous avons vus ci-dessus est de compter le nombre de bits définis dans une représentation binaire donnée.

Cela peut ne pas sembler un cas d'utilisation important pour le moment, mais nous entrerons dans plus de détails plus tard et cela commencera à sembler plus significatif. Pour l'instant, comptons simplement le nombre de bits définis aussi efficacement que possible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dcghg6rp6ycXUFxBJI1oFA.gif)
_Source : [giphy](https://giphy.com/gifs/cRMgB2wjHhVN2tDD2z" rel="noopener" target="_blank" title=")_

La première méthode que nous allons examiner pour cela est un _peu_ intuitive. Elle utilise l'opérateur bit à bit `AND`. En commençant par le bit le moins significatif, nous vérifions simplement si le bit à chaque position est défini ou non et incrémentons un compteur en conséquence.

L'opérateur AND retourne `True` si et seulement si les deux bits sont `True`. Regardons le code pour cela.

Une autre façon de faire cela est de faire un `AND` du nombre avec `lui-même-1` jusqu'à ce que le nombre devienne zéro. Le nombre d'étapes nécessaires pour atteindre 0 sera le nombre de bits définis dans le nombre original.

La raison pour laquelle cela fonctionne est que chaque fois que nous faisons un `AND` du nombre avec `lui-même-1`, un bit est supprimé du nombre. Cela continue jusqu'à ce que le nombre devienne zéro.

#### Masquage et démasquage d'un bit spécifique

Supposons que nous voulons _masquer un bit spécifique_ dans une représentation binaire. Cela signifie simplement éteindre le bit ou transformer un `1  0`. De manière similaire, le _démasquage_ signifie simplement l'opération inverse sur un bit spécifique.

Vous vous demandez peut-être pourquoi cela est utile. L'un des cas d'utilisation les plus importants pour le masquage (ou le démasquage) d'un bit est dans les opérations liées aux ensembles.

Nous pouvons représenter un ensemble d'éléments comme un entier `X-bit`, où `X` est le nombre d'éléments dans l'ensemble. Masquer un bit signifierait la suppression de cet élément de l'ensemble. Pour une application pratique de cela, soyez patient et continuez à lire ?.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j9hCDIKxF8t6tBelC2y0og.gif)
_Source : [giphy](https://giphy.com/gifs/k-kindergarten-behTrfrYhb3iw" rel="noopener" target="_blank" title=")_

Le XOR est un opérateur très polyvalent et il est parfait pour la tâche de masquage et de démasquage.

```
1 ^ ?  00 ^ ?  1
```

> Le XOR produit 1 lorsque les deux bits sont opposés et un 0 lorsque les deux bits sont identiques.

Essentiellement, nous pouvons utiliser la même variable de _masquage_ pour réaliser l'opération de définition / non-définition correspondant à un bit particulier (l'entier dans le ? est appelé la variable de masquage).

```
A ^ (1 << i)
```

L'opération ci-dessus conduira au masquage du bit à l'index `i` si à l'origine ce bit était _défini_ dans `A` et la même opération conduira au démasquage du bit à l'index `i` si à l'origine il était _non défini_ dans `A`.

Nous avons déjà vu comment détecter si un bit est défini ou non lorsque nous avons examiné les moyens de compter le nombre de bits définis dans une représentation binaire donnée.

Une chose importante à noter ici est l'index. Habituellement, pour les structures de données dans les langages de programmation de haut niveau, chaque fois que nous faisons référence à un index spécifique, nous entendons l'index d'un élément particulier dans cette structure de données en commençant par l'extrémité gauche.

Ce à quoi nous faisons référence à un index ci-dessus est à partir de l'extrémité _droite_ (le bit le moins significatif dans la représentation binaire a l'index 0).

Cela suffit pour les bases pour l'instant. Passons à quelques problèmes de programmation réels. Cela aidera à solidifier ce que nous avons appris jusqu'à présent dans l'article et aussi à développer une intuition pour résoudre des problèmes en utilisant la manipulation de bits en général.

### ? Nombre manquant ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*29-nQPqWtIGG8enJCzhtiA.png)
_Source : [LeetCode](https://leetcode.com/problems/missing-number/description/" rel="noopener" target="_blank" title=")_

Il existe plusieurs façons de résoudre ce problème. Nous pouvons trier la liste donnée de nombres puis itérer de `0..n` et trouver facilement le nombre manquant. Cela nous donnera une solution `O(NlogN)`.

Une autre façon de résoudre ce problème est d'utiliser un dictionnaire. Nous ajoutons simplement tous les éléments de notre liste à un dictionnaire puis nous pouvons simplement rechercher le nombre manquant. C'est une solution en temps linéaire mais elle utilise un espace supplémentaire.

Regardons comment nous pouvons obtenir une solution en espace `O(1)` et en temps `O(N)` comme un boss ? en utilisant la manipulation de bits.

Nous allons utiliser la propriété `XOR` ici pour résoudre ce problème. Comme mentionné précédemment, XOR évalue à `True` lorsque les bits d'entrée sont différents et il évalue à `False` lorsqu'il est présenté avec les mêmes bits. Nous nous intéressons au dernier scénario. Que pensez-vous que ce qui suit évalue à ?

```
A ^ A
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*GOxqtc8ix6rJToOxHdi24Q.gif)
_Source : [tenor](https://tenor.com/view/bottaro-zero-nothing-trani-ok-gif-12693830" rel="noopener" target="_blank" title=")_

`XORer` un nombre avec lui-même nous donne 0. C'est l'idée principale derrière notre approche ici.

Donc, ce que nous allons faire, c'est XORer tous les nombres de notre liste. Appelons la valeur que nous obtenons après cela `A`.

Nous allons XORer tous les nombres de `0..n` ensemble. Appelons cette valeur `B`.

En faisant cela, tous les nombres présents dans le tableau original seront XORés avec leurs homologues et évalueront à 0. Le seul nombre restant à la fin sera le nombre manquant.

```
A ^ B = nombre manquant
```

### ?? Compter les bits ?? ??

![Image](https://cdn-media-1.freecodecamp.org/images/1*z3uANN-CgpBiY5QBoBxtJQ.png)
_Source : [LeetCode](https://leetcode.com/problems/counting-bits/description/" rel="noopener" target="_blank" title=")_

C'est l'un de ces problèmes où écrire la réponse pour divers cas de test et observer les résultats pour les motifs aide vraiment. Donc, nous allons faire exactement cela et utiliser le motif que nous trouvons pour arriver directement à l'algorithme final.

Regardons le nombre de 1 dans la représentation binaire des 16 premiers nombres.

```
0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  160  1  1  2  1  2  2  3  1  2   2   3   2   3   3   4   1
```

Le motif formé ci-dessus est le suivant :

> Un nombre pair, E, a le même nombre de bits que celui de E / 2  
> Un nombre impair, O, a un bit de plus que celui de O / 2

C'est tout ce qu'il y a à voir dans les résultats ci-dessus. C'est l'algorithme dans son intégralité. Tout ce que nous avons à faire est d'itérer sur les nombres de `0..n` et d'utiliser les deux règles ci-dessus et nous avons résolu le problème comme un boss ?.

Si vous avez prêté attention à l'idée centrale de la programmation dynamique discutée au début de l'article, vous savez que cela, en essence, est un problème de programmation dynamique.

Nous utilisons le résultat d'un sous-problème précédent (nombre plus petit) pour calculer la réponse (nombre de bits définis) pour le sous-problème actuel.

À première vue, nous n'avons pas vraiment besoin de manipulation de bits pour résoudre ce problème. Il peut être résolu par de simples clauses `if-else` et une boucle `for`.

Donc, ce n'est pas _vraiment_ un problème de type masquage de bits + programmation dynamique.

Regardons une solution simple basée sur les idées ci-dessus.

C'est une manière parfaitement bonne de résoudre ce problème. Pour chaque index, `i`, nous vérifions le nombre de bits dans le nombre `i / 2` et ajoutons également `1` si le nombre actuel est impair.

Nous pouvons, cependant, le résoudre de manière plus geek, pour ainsi dire en utilisant la manipulation de bits. Les deux opérations effectuées sont :

1. division par 2 et
2. vérifier si le nombre est pair ou non.

Nous avons déjà vu l'utilisation de l'opérateur de décalage à droite, `&g`t;>, pour la division par 2.

Quant à la deuxième opération, nous pouvons simplement vérifier si le bit le moins significatif est défini ou non. Si vous remarquez, tous les nombres impairs ont leur bit le moins significatif défini. Alors que les nombres pairs ne l'ont pas.

Nous avons déjà vu comment vérifier si un bit particulier est défini ou non en utilisant l'opérateur `AND`. Regardons une version plus geek ? du code ci-dessus.

Si vous regardez les temps d'exécution des deux programmes, ils sont presque les mêmes. Une grande partie du temps est consommée par la construction du tableau de sortie.

Les opérations bit à bit sont toujours optimisées et sont plus rapides que d'autres constructions de programmation de haut niveau.

###  Produit maximum des longueurs de mots 

![Image](https://cdn-media-1.freecodecamp.org/images/1*-mkPWdUBpw3hcwVtKS0o0A.png)
_Source : [LeetCode](https://leetcode.com/problems/maximum-product-of-word-lengths/description/" rel="noopener" target="_blank" title=")_

Il y a une bonne nouvelle et une mauvaise nouvelle. La bonne nouvelle est qu'une version légèrement optimisée de l'algorithme de force brute fera accepter votre code sur la plateforme.

La méthode de force brute consiste à vérifier toutes les paires de mots et pour chaque paire, vérifier s'il y a des caractères communs entre eux. Pour toutes ces paires qui n'ont pas de caractères communs, enregistrer la valeur maximale de `len(word1) * len(word2)`.

La mauvaise nouvelle est que cet algorithme est extrêmement lent. Regardons le pourcentage de solutions sur LeetCode que cet algorithme de force brute est capable de battre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Htoctoz6g0CFKJPVTxj0jQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ifXouPVw0R1oz1gdJrF_Lg.gif)
_Source : [giphy](http://giphy.com" rel="noopener" target="_blank" title=")_

Honte à toi, Sachin !

Ce n'est pas le genre de statistiques que vous voulez voir pour votre soumission. Si vous êtes quelqu'un qui veut simplement _résoudre_ un problème, alors votre travail ici est terminé. Rien de plus à faire. Mais, si vous êtes comme moi et si vous voulez faire arrêter ce chien ?, alors continuez à lire !

Regardons la complexité temporelle de cet algorithme de force brute avant de passer à une solution beaucoup plus optimisée utilisant la manipulation de bits.

Nous considérons toutes les paires possibles de mots à partir du tableau donné. En considérant qu'il y a `N` mots dans le tableau donné, nous obtiendrons une complexité `O(N)` dès le départ.

En plus de cela, nous avons un dictionnaire contenant des ensembles de caractères pour chacun des mots dans le dictionnaire. En considérant la taille de l'alphabet à 26 (uniquement les alphabets minuscules), chaque ensemble peut potentiellement être de taille `26`.

Pour chaque paire de mots, nous effectuons une intersection d'ensembles pour vérifier si les deux mots ont des caractères communs ou non. L'intersection d'ensembles prend un temps linéaire et donc, la complexité globale pour cet algorithme serait de `O(26N)` qui est essentiellement `O(N)`.

Il s'avère que nous ne pouvons pas nous débarrasser de la partie où nous devons considérer chaque paire de mots à partir du tableau donné. Donc, nous ne pouvons pas nous débarrasser de la partie `O(N)` de l'algorithme.

La portion dont nous pouvons nous débarrasser, cependant, est la partie où nous comparons deux mots et voyons s'ils ont des caractères communs. Cette constante `26` ralentit beaucoup l'algorithme.

Une chose importante à noter ici est que la question se soucie simplement des caractères communs et **pas de leur fréquence ou de leur ordre.**

> Et si nous utilisions simplement un masque de bits pour représenter les caractères dans un mot ?

Ce que nous pouvons faire ici, c'est d'avoir un masque de bits composé de 26 bits pour représenter les caractères appartenant à un mot particulier. Regardons une telle représentation pour quelques mots pour clarifier les choses.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MpHyWl7f6Kgoi5EDKlMczA.png)
_Bitmaps pour les trois mots : hello, algorithm, et tweet._

J'espère que la figure ci-dessus clarifie ce que nous entendons par un masque de bits représentant un mot correspondant. Une fois que nous avons ces masques de bits pour tous les mots, il ne reste plus qu'à vérifier si deux mots ont des caractères communs ou non.

Si deux mots avaient des caractères communs, alors les bits correspondants à ces caractères seraient définis dans les masques de bits des deux mots.

Par conséquent, tout ce que nous avons à faire est de faire un `ET` bit à bit des masques de bits représentant deux mots et de vérifier si nous obtenons un 0 ou non. Si nous obtenons un 0, cela impliquerait aucune intersection et c'est précisément ce que nous recherchons.

```
Par exemple, considérons deux mots "hello" et "jack" 
```

```
Le masque de bits correspondant à "hello" aura les bits pour 'h', 'e', 'l', et 'o' définis.
```

```
Le masque de bits correspondant à "jack" aura les bits pour 'j', 'a', 'c', et 'k' définis. 
```

```
Puisque ces mots n'ont aucun caractère en commun, le ET bit à bit de leurs masques de bits donnera un 0. 
```

```
S'il y avait eu des caractères communs entre eux, alors leurs deux masques de bits auraient des bits définis aux mêmes index (correspondant aux lettres communes) et donc nous obtiendrions un ET bit à bit non nul.
```

Regardons le code pour cette modification dans l'algorithme que nous venons de discuter.

Les opérations bit à bit sont super rapides. Regardons la performance de cet algorithme sur la plateforme LeetCode pour corroborer la rapidité de la manipulation de bits.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7vAqZlPpq8qo8u7NyuoV8g.png)

Pas mal, n'est-ce pas ? Nous avons amélioré le temps d'exécution de notre programme de _1820 ms à 712 ms maintenant_. C'est une énorme amélioration, n'est-ce pas ? Il s'avère que nous pouvons améliorer cet algorithme encore davantage.

> L'amélioration peut être faite grâce au fait que deux mots différents peuvent avoir le même masque de bits.

Par exemple, `hello` et `llohhel` auraient tous deux le même masque de bits. Nous pouvons stocker le _mot le plus long pour un masque de bits donné puisque tout ce qui nous importe est de maximiser le produit des longueurs de mots._

Regardons le code après avoir incorporé cette amélioration.

En faisant cette optimisation, le temps d'exécution passe à **208ms ???**

![Image](https://cdn-media-1.freecodecamp.org/images/1*RoD7oopyw_564B0OaaTtaA.gif)
_Source : [giphy](https://giphy.com/gifs/3o6ZtiLpjhjv9HVUti" rel="noopener" target="_blank" title=")_

### **Représentation de l'ensemble utilisant le masquage de bits**

**Nous avons introduit une idée dans le problème précédent qui sera cruciale dans les deux problèmes suivants que nous allons discuter. Essentiellement, nous avons utilisé l'idée du masquage de bits pour représenter les éléments appartenant à un ensemble.**

**Dans l'article précédent, nous avons considéré un ensemble de 26 alphabets et nous l'avons représenté en utilisant un masque de bits contenant 26 bits. Un 0 à un index particulier dans le masque représenterait l'exclusion de l'ensemble tandis qu'un 1 représenterait l'inclusion dans l'ensemble.**

**Cette idée est très cruciale pour les problèmes de programmation dynamique qui traitent des sous-problèmes impliquant un sous-ensemble de nombres. Nous ne pouvons pas vraiment mettre en cache un sous-ensemble de nombres. Un ensemble n'est pas une structure de données hachable.**

**`Par exemple, supposons que nous avons un tableau de nombres [4, 3, 6]`**  
**`Regardons tous les sous-ensembles possibles de ce tableau.[]`**  
**`[4]`**  
**`[3]`**  
**`[6]`**  
**`[4, 3]`**  
**`[4, 6]`**  
**`[3, 6]`**  
**`[4, 3, 6]Pour les problèmes de programmation dynamique où les états intermédiaires sont définis par ces sous-ensembles, nous avons besoin d'une manière efficace en mémoire de réaliser la mise en cache.`**

**Que faisons-nous dans un tel scénario ?**

**C'est là que les masques de bits interviennent. Ils sont des moyens efficaces en mémoire de représenter des sous-ensembles d'éléments. Jetons un coup d'œil à la manière dont nous pouvons représenter les sous-ensembles ci-dessus en utilisant des masques de bits.**

**`Puisque nous avons 3 éléments dans notre tableau donné, [4, 3, 6], nous pouvons utiliser un nombre de 3 bits pour représenter chacun de ces éléments. Un sous-ensemble vide serait représenté par 000. Regardons chacun des sous-ensembles avec leurs représentations binaires.000 -->> []`**  
**`001 -->> [6]`**  
**`010 -->> [3]`**  
**`011 -->> [3, 6]`**  
**`100 -->> [4]`**  
**`101 -->> [4, 6]`**  
**`110 -->> [4, 3]`**  
**`111 -->> [4, 3, 6]`**

**Selon les contraintes du problème, nous pouvons utiliser un masque de bits. Par exemple, dans le problème précédent, l'ensemble de l'alphabet était limité à une taille de 26. De nombreux problèmes de programmation qui ont des tailles de tableau petites et impliquent une programmation dynamique qui vous oblige à hacher des sous-ensembles, sont généralement une indication d'une approche basée sur le masquage de bits.**

**Un masque de 26 bits, par exemple dans le problème précédent, est essentiellement un entier et nous pouvons simplement mettre en cache cet entier dans un dictionnaire. Cela économise l'empreinte mémoire de l'algorithme et réduit considérablement la complexité temporelle de l'algorithme puisque la manipulation de bits est très efficace. Nous pouvons facilement inclure et exclure des éléments du sous-ensemble en masquant et démasquant les bits correspondants du masque.**

**Regardons un autre problème basé sur cette idée avant de discuter enfin du problème vedette de cet article.**

### **??Partitionner le tableau en K sous-ensembles de somme égale ??**

![Image](https://cdn-media-1.freecodecamp.org/images/1*RHsAK8OQJ6nGGu7MqrQccw.png)
_Source : [LeetCode](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/" rel="noopener" target="_blank" title=")_

**C'est juste l'une de ces questions qui vous supplie d'utiliser le masquage de bits. Remarquez la taille du tableau. Il ne contient que 16 éléments. Si nous considérons un masque de bits pour représenter les éléments dans un tableau, nous aurions un entier de 16 bits entre nos mains.**

**Cela signifie que pour représenter tous les sous-ensembles possibles d'un tableau donné, nous aurions 2 entiers possibles. Nous n'avons pas vraiment besoin de sous-ensembles _réels_. Tout ce dont nous avons besoin est un masque de bits nous indiquant les éléments appartenant à ce sous-ensemble. Sur la base de cette idée, regardons une approche basée sur la programmation dynamique pour résoudre le problème ci-dessus.**

**L'énoncé du problème nous demande simplement si une partition en k sous-ensembles de somme égale est possible ou non. Il ne nous demande pas de retourner la _partition réelle_. Cela rend le problème beaucoup plus simple.**

**Nous ne nous soucions pas de savoir à quelle partition un élément appartient tant que la somme globale d'une partition est égale à `total_sum / k`.**

**Comme nous l'avons mentionné dans les paragraphes ci-dessus, nous utiliserons un masque de bits pour représenter les éléments du tableau.**

**Nous utiliserons les états de bits individuels du masque pour identifier quels nombres ont déjà été assignés à une partition et lesquels restent encore à assigner. Nous ne pouvons assigner un nombre à une partition que si, après l'avoir ajouté à cette partition, la somme totale reste `<= total_sum` / k .**

**Si la somme, `S`, de tous les éléments du tableau est divisible par `k`, nous devons compléter `k  1` partitions puisque la dernière partition se mettra automatiquement en place. Dans le cas où la somme totale n'est pas divisible par `k` , alors une telle partition de somme égale n'est pas possible.**

#### **Pourquoi la programmation dynamique ?**

**Avant de regarder le code pour ce problème basé sur les idées que nous avons discutées ci-dessus, il est important de comprendre comment la programmation dynamique s'intègre dans le tableau. Nous avons déjà vu pourquoi le masquage de bits serait utile. Mais où exactement la programmation dynamique s'intègre-t-elle ?**

**La récursion est un choix naturel pour le problème puisque nous avons un ensemble de `N` éléments et nous devons les partitionner en `k` sous-ensembles différents, tous ayant une somme égale.**

**Puisque nous ne savons pas vraiment à quelle partition un nombre devrait appartenir, nous devons essayer toutes les options. Cela signifie que, pour une partition donnée, nous essayons d'ajouter tous les nombres disponibles de manière récursive (dans les limites de la somme de la partition) et voyons quel choix nous mène à une réponse.**

**La récursion serait basée sur les trois variables suivantes :**

1. **le `nombre de partitions` restantes.**
2. **le `masque` représentant les éléments dans le tableau original qui sont _non assignés_.**
3. **et la somme `courante de la partition`.**

**Comme nous le savons tous, pour qu'un problème soit classé comme un problème de programmation dynamique, il doit avoir les deux propriétés suivantes :**

1. **_Structure optimale sous-jacente_ ~ ce qui signifie simplement que le problème original doit pouvoir être divisé en sous-problèmes et que les solutions optimales aux sous-problèmes doivent pouvoir être utilisées pour trouver la solution optimale au problème principal.**
2. **_Sous-problèmes chevauchants_ ~ ce qui signifie qu'il y a plusieurs appels récursifs aux mêmes sous-problèmes et pour éviter les calculs répétés, nous pouvons **_mettre en cache_** les résultats de nos sous-problèmes.**

**Regardons l'arbre de récursion pour ce problème afin de comprendre si nous avons des sous-problèmes chevauchants. Nous avons déjà satisfait la première propriété.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*uc66c1lYHTXfbnMLca2bXA.png)
_Le tuple **(K, 12, 3)** est l'état de récursion qui se répète. K est le nombre de partitions restantes qui, dans notre exemple, est 2. 12 est la somme de la partition actuelle. 3 est le masque de bits. Si vous considérez la représentation binaire de 3, vous obtiendrez 0011. Cela implique les deux éléments 5 et 7 de l'ensemble [8, 16, 5, 7] et donc la somme 12._

**Dans l'arbre de récursion ci-dessus, nous considérons K = 2. Cela signifie que nous avons besoin de 2 partitions, chacune de somme **18**. Puisque nous n'atteignons jamais **18** dans l'arbre ci-dessus, le **K** ne se réduit jamais. Ce n'est qu'une partie de l'arbre de récursion et la version complète.**

**Nous pouvons clairement voir deux états de récursion se répéter. Nous obtenons le même masque `0011` deux fois. Nous pouvons simplement stocker le résultat une fois et le réutiliser plus tard.**

**Maintenant, regardons le code basé sur le masquage de bits + la programmation dynamique.**

**Nous sommes enfin prêts à examiner le problème principal de cet article. Le problème qui n'est pas aussi simple dans son application de masquage de bits que le problème actuel et le précédent.**

### **? Trouver la plus courte superchaîne ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*y3YKYQucMnTApO-_p8er2g.png)
_Source : [LeetCode](https://leetcode.com/problems/find-the-shortest-superstring/description/" rel="noopener" target="_blank" title=")_

**Quelle est, selon vous, la manière la plus simple de former une _superchaîne_ ?**

**Vous prenez simplement n'importe quelle permutation des mots donnés et toutes ces permutations seront des superchaînes valides.**

**Cependant, la question ne nous demande pas de former _n'importe quelle_ superchaîne. Elle nous demande de former la **superchaîne la plus courte couvrant tous les mots.**

**Pour ce problème, nous allons explorer l'idée de **_chaînage_** des mots ensemble. Intuitivement, vous pouvez considérer l'idée de chaînage comme une union d'ensembles.**

**Considérons deux ensembles différents d'éléments puis regardons l'ensemble combiné contenant tous leurs éléments ensemble, c'est-à-dire l'ensemble union.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*X_PLM3rVNzJ6Oph9AFdJYQ.png)
_Les éléments répétés ne sont considérés qu'une seule fois dans l'union._

**Comme nous pouvons le voir ci-dessus, chaque fois que nous faisons une union sur deux ensembles, les éléments communs n'apparaissent qu'une seule fois. Nous adopterons une idée similaire avec le chaînage de deux mots ensemble.**

**Essentiellement, lors du chaînage des mots `A` et `B` ensemble, nous ne considérerons la portion commune entre le **_suffixe de A et le préfixe de B qu'une seule fois._** Regardons la représentation diagrammatique du chaînage de deux mots.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hCEiJ1aKvFBBmNkKbPi9jQ.png)

**C'est un concept important qui sera utile pour résoudre ce problème. Afin d'éviter les calculs répétés de trouver la **_portion commune entre deux mots qui sont chaînés ensemble,_** nous allons faire un peu de prétraitement.**

**Nous allons trouver la longueur du suffixe de `A` qui chevauche le préfixe de `B` où `A et B` sont chaînés ensemble. Nous allons faire cela pour toutes les paires de mots dans notre liste donnée. En Python, étant donné une chaîne `S`, nous pouvons utiliser `S[i:]` pour obtenir tous les suffixes et `S[:i]` pour obtenir tous les préfixes. Nous utilisons cela pour notre prétraitement ci-dessous.**

**Maintenant que l'idée de chaînage est claire, nous pouvons passer à la partie suivante du problème où nous expliquons pourquoi ce problème peut être résolu de manière récursive.**

#### **Pourquoi la récursion ?**

**Maintenant que nous sommes familiers avec le concept de chaînage, nous savons que chaque fois que nous chaînons deux mots ensemble, le nouveau mot formé peut être plus court que les longueurs combinées des deux mots originaux.**

**En étendant cette idée à tous les mots de la liste donnée, nous devons former une superchaîne qui sera formée en chaînant un mot après l'autre jusqu'à ce que nous ayons terminé avec tous les mots.**

**La question importante ici est, dans quel ordre les mots doivent-ils être chaînés ?**

**Pour les trois mots `aabc` , `hjaa`, et `chuj`, l'ordre de chaînage `hjaa  aabc  chuj = hjaabchuj` est meilleur que `aabc  hjaa  chuj = aabchjaachuj` puisque le premier donne une superchaîne de longueur 9 par opposition à 12 dans le second ordre.**

**Ainsi, l'ordre de chaînage détermine la longueur globale de la superchaîne formée.**

> **Nous allons _essayer tous les arrangements possibles_ pour les superchaînes en utilisant la liste donnée de mots et choisir la plus courte.**

#### **Cela semble légitime, mais pourquoi la programmation dynamique ? ?**

**Au lieu de nous appuyer sur un arbre de récursion pour expliquer le besoin de programmation dynamique, nous allons examiner un exemple qui expliquera la même idée.**

**Supposons que nous avons un ensemble de 5 mots `[A, B, C, D, E]` et que nous devons former la superchaîne la plus courte qui contient tous les mots.**

**Nous savons déjà que nous résolvons ce problème de manière récursive. Supposons qu'au milieu de notre récursion, nous avons déjà décidé de l'ordre de chaînage des trois premiers mots. Disons que cet ordre était `B  A  C` . Maintenant, nous devons trouver la meilleure façon de chaîner **D et E après C afin que la longueur globale de la superchaîne soit minimisée.**

**Disons que dans notre récursion, nous avons trouvé que `C  E  D` était le meilleur ordre de chaînage. Nous ne savons pas encore si la superchaîne formée via `B  A  C  E  D` est la plus courte. Cependant, nous savons que `C  E  D` est le meilleur ordre de chaînage pour les trois mots `C, D, et E` .**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Job9SHPwsLUh3QBmMA-GRQ.gif)
_Je sais que c'est devenu fatigant, mais continuez à lire ?_

**Supposons maintenant que nous avons arrangé les trois premiers mots un peu différemment dans notre récursion (un chemin de récursion séparé) et que nous avons maintenant `A  B  C` et que nous devons récurser **à nouveau** pour trouver le meilleur arrangement possible pour `E et D` . Cependant, nous savons déjà d'après ce qui précède que le meilleur arrangement possible est `C  E  D` . Pourquoi recalculer cela ? C'est là que la programmation dynamique entre en jeu.**

**C'est tout ? Continuez. Expliquez encore.**

**Non, regardons maintenant le code Python qui rassemble toutes ces idées.**

**Oh oh ! Où diable est le masquage de bits dans tout cela ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*YwOzvCoyJTdC59nj_vWmzA.gif)

#### **Ok ok, passons au masquage de bits ?**

**Reformulons le problème d'une manière légèrement différente qui rendra le besoin de masquage de bits très clair.**

**Étant donné un ensemble de `N` éléments, nous devons trouver un arrangement approprié pour eux qui minimisera une certaine métrique. Puisque nous nous appuyons sur la programmation dynamique, nous allons _mettre en cache_ les résultats des sous-problèmes.**

**Nos sous-problèmes seront représentés par le sous-ensemble de ces N éléments. Comme nous l'avons vu dans cet article et surtout dans les deux problèmes précédents, il est difficile de mettre en cache des sous-ensembles tels quels.**

**Dans le cas où les contraintes du problème sont petites, nous pouvons représenter les éléments de la liste en utilisant un masque de bits et l'utiliser à des fins de mise en cache.**

> **Après tout, un masque de bits n'est qu'un nombre.**

**Passons enfin au code pour trouver la superchaîne la plus courte étant donné un ensemble de N mots.**

* **Ligne 3 ~** Le masque initial est composé de tous des 1. Cela implique que tous les mots sont disponibles pour le chaînage. Si le masque devient 0, cela signifie qu'il ne reste aucun mot pour le chaînage. Donc, la longueur de la superchaîne serait 0. C'est le cas de base.
* **Ligne 7 ~** Si vous avez prêté attention à l'exemple impliquant 5 mots `[A, B, C, D, E]` d'avant, vous savez que l'opportunité de mise en cache se présente lorsque nous avons les deux mots `D et E` à chaîner ensemble **_après C._**   
**_Ainsi, nous devons connaître le mot précédent dans la superchaîne jusqu'à présent afin d'attacher le reste des mots. Par conséquent, `prev_i`, qui représente l'index dans le tableau original du mot précédent dans la superchaîne, est également utilisé à des fins de mise en cache en plus du masque._**
* **Ligne 12, 15 ~** Nous vérifions toujours l'ensemble donné de mots et ne considérons que ceux-ci comme _options pour l'étape actuelle dans notre récursion_ qui n'ont pas été utilisés précédemment. Nous utilisons le masquage de bits pour cela. Pour voir si un mot a été utilisé ou non, nous vérifions simplement si le bit à l'index correspondant dans le masque est _non défini_ ou non.
* **Ligne 18 ~** Utilise le prétraitement que nous avons fait plus tôt. Pour le mot à chaîner / attacher au mot à l'index `prev_i` , nous connaissons la quantité de chevauchement entre les deux. Ainsi, si nous décidons de considérer le mot à l'index `i` comme le prochain mot dans notre récursion, la quantité de longueur qu'il ajoutera à notre superchaîne serait `len(A[i])  chevauchement entre les mots A[prev_i] et A[i]`

**Tout cela est bien et bon, mais l'énoncé original ne demandait-il pas la superchaîne elle-même et pas seulement la longueur de la superchaîne la plus courte ?**

**Est-ce que j'évite de résoudre l'ensemble du problème ? Bien sûr que non !**

![Image](https://cdn-media-1.freecodecamp.org/images/1*R45bEuJSmmUTZ10jOM4gdQ.gif)
_Source : [giphy](https://giphy.com/gifs/no-smh-scooby-doo-EriPNV1whwKac" rel="noopener" target="_blank" title=")_

**La fonction `recurse` retourne simplement la _longueur_ de la superchaîne la plus courte et non la superchaîne elle-même. L'énoncé du problème, cependant, nous demande de trouver la superchaîne la plus courte.**

**Si vous regardez attentivement le code, vous remarquerez un dictionnaire `parent`. À chaque étape de notre récursion, nous avons plusieurs options de mots qui peuvent être chaînés à la superchaîne actuelle (l'étendant ainsi). Nous utilisons le dictionnaire parent pour stocker le mot à chaque étape qui a donné la **_meilleure_** réponse (longueur la plus courte).**

**Pour un masque donné  qui nous indique quels mots ont déjà été chaînés ensemble  et un mot précédent donné (`prev_i`), le dictionnaire `parent` stocke le mot suivant dans la superchaîne qui donne la réponse optimale.**

**Nous utiliserons ce dictionnaire pour faire un retour en arrière et former la _superchaîne la plus courte_.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*IJ2Sm-YM_0ReJAhi907r5w.png)

**En fin de compte, c'est l'une des meilleures vues pour un programmeur compétitif, surtout si c'est pour un problème difficile dans une compétition chronométrée.**

### **Conclusion ??**

* **Les opérations sur les bits sont très efficaces et elles sont généralement effectuées en parallèle via des instructions système optimisées.**
* **C'est difficile, mais pas impossible, d'écrire du code propre et compréhensible impliquant des manipulations de bits.**
* **`ET` , `OU` , et `NON` sont les trois opérateurs bit à bit fondamentaux.**
* **Les opérateurs de `décalage à gauche &l`t;< et de `décalage à droite >> sont utilisés pour la multiplication ou la division par 2.**
* **L'opérateur `XOR` est un opérateur polyvalent qui peut être utilisé dans de nombreux problèmes de programmation différents. Il retourne `True` uniquement lorsque les deux bits sont opposés et `False` sinon.**
* **Les solutions basées sur la programmation dynamique impliquent une sorte de mise en cache pour les résultats des sous-problèmes. Les sous-problèmes sont représentés par un ensemble de variables. Ces variables ne sont pas nécessairement des types de données primitifs.**
* **Le masquage de bits est très utile dans les problèmes de programmation dynamique lorsque nous devons traiter des sous-ensembles et que la taille de la liste/tableau est petite. Un masque (ayant tous des 0 ou tous des 1) peut représenter les éléments de l'ensemble et définir ou annuler un bit peut signifier l'inclusion et l'exclusion de l'ensemble.**
* **Si la taille du tableau/liste/ensemble est, disons, autour de 20, alors vous auriez 2 **_possibles_** masques de bits, ce qui revient à presque un million d'entre eux. Ce n'est pas toujours le cas que vous rencontrerez _tous_ ces masques de bits dans un cas de test. Cependant, c'est le nombre maximum possible.**
* **Nous devons être prudents quant à l'utilisation du masquage de bits. Nous ne pouvons pas avoir un masque de 100 bits car cela serait calculatoirement intractable.**
* **Pour qu'une solution soit éligible à la programmation dynamique, elle doit satisfaire les propriétés de sous-structure optimale et de sous-problèmes chevauchants. Habituellement, grâce à une certaine pratique, vous pouvez commencer à identifier si le problème en question aura une solution basée sur la DP ou non.**

### **Références ?**

* **[https://www.hackerearth.com/practice/notes/bit-manipulation/](https://www.hackerearth.com/practice/notes/bit-manipulation/)**
* **[https://blog.bitsrc.io/bitmask-there-is-space-at-the-bottom-5a741d18c4e3](https://blog.bitsrc.io/bitmask-there-is-space-at-the-bottom-5a741d18c4e3)**
* **[https://bit.ly/2QRTIpj](https://bit.ly/2QRTIpj)**
* **[https://bit.ly/2CCUCxn](https://bit.ly/2CCUCxn)**
* **[https://www.geeksforgeeks.org/bitmasking-and-dynamic-programming-set-1-count-ways-to-assign-unique-cap-to-every-person/](https://www.geeksforgeeks.org/bitmasking-and-dynamic-programming-set-1-count-ways-to-assign-unique-cap-to-every-person/)**
* **[https://www.geeksforgeeks.org/bitmasking-dynamic-programming-set-2-tsp/](https://www.geeksforgeeks.org/bitmasking-dynamic-programming-set-2-tsp/)**
* **[https://codeforces.com/blog/entry/17973](https://codeforces.com/blog/entry/17973)**

**C'est été un long article et l'un que j'ai absolument adoré écrire. Si vous avez lu jusqu'ici, alors vous avez probablement trouvé cet article vraiment utile. Faites passer un peu d'amour en le partageant autant que possible et détruisez ce bouton d'applaudissements ! ?**

**Oh, si vous aimeriez lire plus d'articles aussi géniaux, tous illuminés avec des animations et de belles images explicatives, consultez notre [cuisine](https://github.com/DivyaGodayal/CoderChef-Kitchen/) nouvellement ouverte.**

**Croyez-moi, nous avons quelques recettes délicieuses pour vous et avec la saison des vacances sur nous, je suis sûr que vous les aimerez.**

**Je vous souhaite à tous un joyeux Noël et une bonne année !**
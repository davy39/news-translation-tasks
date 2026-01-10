---
title: La récursivité démystifiée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-12T15:10:43.000Z'
originalURL: https://freecodecamp.org/news/recursion-demystified-99a2105cb871
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yNNmaPaMjbto_oSlcO7hvQ.png
tags:
- name: algorithms
  slug: algorithms
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Recursion
  slug: recursion
- name: technology
  slug: technology
seo_title: La récursivité démystifiée
seo_desc: 'By Sachin Malhotra


  In order to understand recursion, you must first understand recursion.


  Crazy, isn’t it ?

  Well, I hope that by the end of this article you will feel much more confident about
  what recursion is and mainly, how we can come up with a...'
---

Par Sachin Malhotra

> Pour comprendre la récursivité, vous devez d'abord comprendre la récursivité.

Fou, n'est-ce pas ?

Eh bien, j'espère qu'à la fin de cet article, vous vous sentirez beaucoup plus confiant quant à ce qu'est la récursivité et surtout, comment nous pouvons trouver une solution récursive à un problème.

### Qu'est-ce que la récursivité ?

Comment expliquez-vous la récursivité à un enfant de 4 ans ? C'est une question d'entretien assez célèbre, et il existe de nombreuses réponses disponibles sur le web. Nous ne répondrons pas à cette question car elle est trop grand public.

Si vous êtes aussi intelligent que moi ??, vous expliqueriez la récursivité à quelqu'un d'un an plus jeune que vous. Faites-leur expliquer la récursivité à quelqu'un d'un an plus jeune qu'eux. Continuez jusqu'à ce que vous ayez un enfant de 5 ans expliquant la récursivité à un enfant de 4 ans. Fini. [Source : re[ddit].](https://www.reddit.com/r/programmerchat/comments/3ua9ie/how_would_you_explain_recursion_to_a_6_year_old/)

En termes de programmation, la récursivité est

> Une fonction qui s'appelle elle-même.

La fonction ci-dessus ne fait pas de travail utile en tant que tel, mais elle démontre la récursivité. La relation récursive ci-dessus serait

```
T(N) = T(N - 1) + O(1)
```

Cela signifie simplement que l'exécution de l'appel à `random_function(n)` ne peut pas se poursuivre tant que l'appel à `random_function(n-1)` n'est pas terminé et ainsi de suite.

Essentiellement, nous retardons l'exécution de l'état actuel de la fonction jusqu'à ce qu'un autre appel à la même fonction soit terminé et ait retourné son résultat.

Le compilateur sauvegarde l'état de l'appel de la fonction maintenant et passe ensuite à l'appel de la fonction suivante et ainsi de suite. Ainsi, le compilateur sauvegarde les états des fonctions sur une pile et utilise celle-ci pour les calculs et le retour en arrière.

![Image](https://cdn-media-1.freecodecamp.org/images/R18bQubZemC9gl-KFaWAo1otGfKuLe0kQnVq)
_Pile de récursivité d'un ensemble d'appels de fonctions._

Essentiellement, si un problème peut être décomposé en sous-problèmes similaires qui peuvent être résolus individuellement, et dont les solutions peuvent être combinées pour obtenir la solution globale, alors nous disons qu'il peut exister une solution récursive au problème.

Au lieu de nous accrocher à cette définition apparemment ancienne de la récursivité, nous allons examiner un grand nombre d'applications de la récursivité. Ensuite, espérons que les choses seront claires.

### Factorielle d'un nombre

Voyons comment nous pouvons trouver la factorielle d'un nombre. Avant cela, voyons ce que représente la factorielle d'un nombre et comment elle est calculée.

```
factorial(N) = 1 * 2 * 3 * .... * N - 1 * N
```

En termes simples, la factorielle d'un nombre est simplement le produit des termes de 1 au nombre N multipliés les uns par les autres.

Nous pouvons simplement avoir une boucle `for` de 1 à N et multiplier tous les termes de manière itérative et nous aurons la factorielle du nombre donné.

Mais, si vous regardez de près, il existe une structure récursive inhérente à la factorielle d'un nombre.

```
factorial(N) = N * factorial(N - 1)
```

C'est comme déleser le calcul à un autre appel de fonction opérant sur une version plus petite du problème original. Voyons comment cette relation se déroulerait pour vérifier si la solution ici correspond à celle fournie par la boucle `for`.

![Image](https://cdn-media-1.freecodecamp.org/images/GI5JbLskVQ9-JsBKIGMb0iJkce07QD35RPK9)
_Montrant les étapes de haut en bas pour la fonction récursive factorielle_

![Image](https://cdn-media-1.freecodecamp.org/images/YLIPyQSiQNTjGreR9hZGTsLKBkApoO7C5KG9)
_Vérification que la fonction récursive définie produit le résultat correct_

Il est donc clair, d'après les deux figures ci-dessus, que la fonction récursive que nous avons définie précédemment,

```
factorial(N) = N * factorial(N - 1)
```

est effectivement correcte. Jetez un coup d'œil à l'extrait de code Python utilisé pour trouver la factorielle d'une fonction, de manière récursive.

Cet exemple était assez simple. Considérons un exemple légèrement plus grand mais standard pour démontrer le concept de récursivité.

### Suite de Fibonacci

Vous devez déjà être familier avec la célèbre suite de Fibonacci. Pour ceux d'entre vous qui n'ont pas entendu parler de cette suite ou n'ont pas vu d'exemple auparavant, regardons.

```
1 1  2   3     5           8                       13 ..... 
```

Regardons la formule pour calculer le n^ième nombre de Fibonacci.

```
F(n) = F(n - 1) + F(n - 2) où F(1) = F(2) = 1
```

Clairement, cette définition de la suite de Fibonacci est récursive par nature, puisque le n^ième nombre de Fibonacci dépend des deux nombres de Fibonacci précédents. Cela signifie diviser le problème en sous-problèmes plus petits, et donc la récursivité. Jetez un coup d'œil au code pour cela :

Chaque problème récursif doit avoir deux choses nécessaires :

1. La relation de récurrence définissant les états du problème et comment le problème principal peut être décomposé en sous-problèmes plus petits. Cela inclut également le cas de base pour arrêter la récursivité.
2. Un arbre de récursivité qui montre les premiers appels, sinon tous, à la fonction considérée. Jetez un coup d'œil à l'arbre de récursivité pour la relation récursive des suites de Fibonacci.

![Image](https://cdn-media-1.freecodecamp.org/images/zPWLCACHuYlGSDPqXtfhADCZjxbAX8vC0vAU)
_Arbre de récursivité montrant la séquence des appels pour la relation de récurrence de Fibonacci._

L'arbre de récursivité nous montre que les résultats obtenus du traitement des deux sous-arbres de la racine N peuvent être utilisés pour calculer le résultat pour l'arbre enraciné en N. De même pour les autres nœuds.

Les feuilles de cet arbre de récursivité seraient `fibonacci(1)` ou `fibonacci(2)` qui représentent tous deux les cas de base pour cette récursivité.

Maintenant que nous avons une compréhension très basique de la récursivité, de ce qu'est une relation de récurrence, et de l'arbre de récursivité, passons à quelque chose de plus intéressant.

Exemples !

Je crois fermement en la résolution d'un nombre innombrable d'exemples pour un sujet donné en programmation pour devenir un maître de ce sujet. Les deux exemples que nous avons considérés (Factorielle d'un nombre et la suite de Fibonacci) avaient des relations de récurrence bien définies. Regardons quelques exemples où la relation de récurrence pourrait ne pas être si évidente.

### Hauteur d'un arbre

Pour garder les choses simples pour cet exemple, nous ne considérerons qu'un arbre binaire. Donc, un arbre binaire est une structure de données arborescente dans laquelle chaque nœud a au plus deux enfants. Un nœud de l'arbre est désigné comme la racine de l'arbre, par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/5FFOf1TV0n-tep2Lj9iHZX17rIzxuBcjLEbW)
_Un arbre enraciné en 'A' avec sa hauteur et le chemin correspondant mis en évidence._

Définissons ce que nous entendons par la hauteur de l'arbre binaire.

> La hauteur de l'arbre serait la longueur du plus long chemin de la racine à la feuille dans l'arbre.

Donc, pour le diagramme d'exemple affiché ci-dessus, en considérant que le nœud étiqueté `A` est la racine de l'arbre, le plus long chemin de la racine à la feuille est `A → C → E → G → I`. Essentiellement, la hauteur de cet arbre est `5` si nous comptons le nombre de nœuds et `4` si nous comptons simplement le nombre d'arêtes sur le chemin le plus long.

Maintenant, oubliez tout l'arbre et concentrez-vous uniquement sur les portions mises en évidence dans le diagramme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/JqcfdTySjGqaALQd-yMA3q8GaAmhNCDxQ3PC)
_Arbre enraciné au nœud A et ses deux sous-arbres avec leurs hauteurs respectives._

La figure ci-dessus nous montre que nous pouvons représenter un arbre sous la forme de ses sous-arbres. Essentiellement, la structure à gauche du nœud A et la structure à droite de A est également un arbre binaire en soi, juste plus petit et avec différents nœuds racines. Mais ce sont néanmoins des arbres binaires.

Quelles informations pouvons-nous obtenir de ces deux sous-arbres qui nous aideraient à trouver la hauteur de l'arbre principal enraciné en A ?

Si nous connaissions la hauteur du sous-arbre gauche, disons `h1`, et la hauteur du sous-arbre droit, disons `h2`, alors nous pouvons simplement dire que le `maximum des deux + 1` pour le nœud A nous donnerait la hauteur de notre arbre. N'est-ce pas ?

En formalisant cette relation récursive,

```
hauteur(racine) = max(hauteur(racine.gauche), hauteur(racine.droite)) + 1
```

Donc, c'est la définition récursive de la hauteur d'un **arbre binaire**. L'accent est mis sur binaire ici, car nous avons utilisé seulement deux enfants du nœud `racine` représentés par `racine.gauche` et `racine.droite`. Mais il est facile d'étendre cette relation récursive à un arbre n-aire. Jetons un coup d'œil à cela dans le code.

Le problème ici a été grandement simplifié car nous avons laissé la récursivité faire tout le travail difficile pour nous. Nous avons simplement utilisé des réponses **optimales** pour nos sous-problèmes afin de trouver une solution à notre problème original.

Regardons un autre exemple qui peut être résolu sur des lignes similaires.

### Nombre de nœuds dans un arbre

Ici encore, nous considérerons un arbre binaire pour simplifier, mais l'algorithme et l'approche peuvent être étendus à tout type d'arbre essentiellement.

Le problème est en soi très explicite. Étant donné la racine d'un arbre binaire, nous devons déterminer le nombre total de nœuds dans l'arbre. Cette question et l'approche que nous allons développer ici sont très similaires à la précédente. Nous devons simplement apporter des changements minuscules et nous aurons le nombre de nœuds dans l'arbre binaire.

Jetez un coup d'œil au diagramme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/MTQeKDsBSS0YmxfVS9sGsamrHi0BHRhgHmIU)

Le diagramme dit tout. Nous savons déjà qu'un arbre peut être décomposé en sous-arbres plus petits. Ici encore, nous pouvons nous demander,

> Quelles informations pouvons-nous obtenir de ces deux sous-arbres qui nous aideraient à trouver le nombre de nœuds dans l'arbre enraciné en A ?

Eh bien, si nous connaissions le nombre de nœuds dans le sous-arbre gauche et le nombre de nœuds dans le sous-arbre droit, nous pouvons simplement les additionner et ajouter un pour le nœud racine et cela nous donnerait le nombre total de nœuds.

En formalisant cela, nous obtenons,

```
nombre_de_nœuds(racine) = nombre_de_nœuds(racine.gauche) +        nombre_de_nœuds(droite) + 1
```

Si vous regardez cette récursivité et la précédente, vous trouverez qu'elles sont extrêmement similaires. La seule chose qui varie est ce que nous faisons avec les informations que nous avons obtenues de nos sous-problèmes et comment nous les avons combinées pour obtenir une réponse.

Maintenant que nous avons vu quelques exemples faciles avec un arbre binaire, passons à quelque chose de moins trivial.

### Tri par fusion

Étant donné un tableau de nombres comme

```
4 2 8 9 1 5 2
```

nous devons trouver une technique de tri qui les trie soit par ordre croissant soit décroissant. Il existe de nombreuses techniques de tri célèbres pour cela comme [Quick Sort](https://en.wikipedia.org/wiki/Quicksort), [Heap Sort](https://en.wikipedia.org/wiki/Heapsort), [Radix Sort](https://en.wikipedia.org/wiki/Radix_sort) et ainsi de suite. Mais nous allons spécifiquement examiner une technique appelée le Tri par fusion.

Il est possible que beaucoup d'entre vous soient familiers avec le [paradigme Diviser pour régner](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm), et cela pourrait sembler redondant. Mais restez avec moi et continuez à lire !

L'idée ici est de le décomposer en sous-problèmes.

C'est de cela que parle l'article, n'est-ce pas ? ?

Et si nous avions deux moitiés triées du tableau original. Pouvez-nous les utiliser d'une manière ou d'une autre pour trier l'ensemble du tableau ?

C'est l'idée principale ici. La tâche de trier un tableau peut être décomposée en deux sous-tâches plus petites :

* trier deux moitiés différentes du tableau
* puis utiliser ces moitiés triées pour obtenir le tableau trié original

Maintenant, la beauté de la récursivité est que vous n'avez pas besoin de vous soucier de la manière dont nous allons obtenir deux moitiés triées et de la logique qui ira dans cela. Puisque c'est de la récursivité, le même appel de méthode à `merge_sort` trierait les deux moitiés pour nous. Tout ce que nous devons faire est de nous concentrer sur ce que nous devons faire une fois que nous avons les moitiés triées avec nous.

Passons en revue le code :

À ce stade, nous avons fait confiance et nous sommes appuyés sur notre bon ami la récursivité et nous avons supposé que `left_sorted_half` et `right_sorted_half` contiendraient en fait les deux moitiés triées du tableau original.

Donc, quoi ensuite ?

La question est de savoir comment les combiner d'une manière ou d'une autre pour donner l'ensemble du tableau.

Le problème se réduit maintenant simplement à fusionner deux tableaux triés en un seul. C'est un problème assez standard et peut être résolu par ce que l'on appelle l'approche "à deux doigts".

Jetez un coup d'œil au pseudo-code pour une meilleure compréhension.

```
soit L et R nos deux moitiés triées. soit ans le tableau combiné, trié
```

```
l = 0 // Le pointeur pour la moitié gaucher = 0 // Le pointeur pour la moitié droitea = 0 // Le pointeur pour le tableau ans
```

```
tant que l < L.length et r < R.length {      si L[l] < R[r] {           ans[a] = L[l]           l++       } sinon {           ans[a] = R[r]           r++      }}
```

```
copier la portion restante du tableau L ou R, celui qui était le plus long, dans ans.
```

Ici, nous avons deux pointeurs (doigts), et nous les positionnons au début des moitiés individuelles. Nous vérifions lequel est le plus petit (c'est-à-dire quelle valeur pointée par le doigt est la plus petite), et nous ajoutons cette valeur à notre tableau combiné trié. Nous faisons ensuite avancer le pointeur (doigt) respectif. À la fin, nous copions la portion restante du tableau le plus long et l'ajoutons à l'arrière du tableau `ans`.

Donc, le code combiné pour le tri par fusion est le suivant :

Nous allons faire une dernière question en utilisant la récursivité et faites-moi confiance, c'est une question difficile et assez confuse. Mais avant de passer à cela, je vais répéter les étapes que je suis chaque fois que je dois penser à une solution récursive pour un problème.

### Étapes pour trouver une solution récursive

1. Essayez de décomposer le problème en sous-problèmes.

![Image](https://cdn-media-1.freecodecamp.org/images/H8nqGHngKfV4gCq8wEKUezxfMgeviX7neNBG)
_Source : [https://www.weheartswift.com/compute-2-power-n/](https://www.weheartswift.com/compute-2-power-n/" rel="noopener" target="_blank" title=")_

2. Une fois que vous avez compris les sous-problèmes, réfléchissez à quelles informations de l'appel aux sous-problèmes vous pouvez utiliser pour résoudre la tâche en cours. Par exemple, la factorielle de `N — 1` pour trouver la factorielle de `N`, la hauteur des sous-arbres gauche et droit pour trouver la hauteur de l'arbre principal, et ainsi de suite.

![Image](https://cdn-media-1.freecodecamp.org/images/c-U0TqgndRDro6q4jOc4EoS4qpl3s1HO4CXm)

3. Gardez votre calme et faites confiance à la récursivité ! Supposez que vos appels récursifs aux sous-problèmes retourneront les informations dont vous avez besoin de la manière la plus optimale.

![Image](https://cdn-media-1.freecodecamp.org/images/ei-mU1SjP7yuCMDBTIcl-mizedpie6li24V6)
_Source : [https://neildanson.files.wordpress.com/2014/02/keep-calm-it-just-works.png](https://neildanson.files.wordpress.com/2014/02/keep-calm-it-just-works.png" rel="noopener" target="_blank" title=")_

4. La dernière étape de ce processus consiste à utiliser les informations que nous venons d'obtenir des sous-problèmes pour trouver la solution au problème principal. Une fois que vous avez cela, vous êtes prêt à coder votre solution récursive.

Maintenant que nous avons toutes les étapes alignées, passons à notre dernier problème dans cet article. Il s'appelle [Sum of Distances in a Tree.](https://leetcode.com/problems/sum-of-distances-in-tree/description/)

### Somme des distances dans un arbre

Regardons ce que la question nous demande de faire ici. Considérons l'arbre suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/ZsJI0v3ck7tDFqAtETvWCUUzaE5T0FG4J55h)
_Exemple d'arbre montrant la sortie attendue de notre programme pour les différents nœuds._

Dans l'exemple ci-dessus, la somme des chemins pour le nœud A (le nombre de nœuds sur **chaque chemin** de `A` à chaque autre sommet dans l'arbre) est 9. Les chemins individuels sont mentionnés dans le diagramme lui-même avec leurs longueurs respectives.

De même, considérons la somme des distances pour le nœud C.

```
C --> A --> B (Longueur 2)C --> A (Longueur 1)C --> D (Longueur 1)C --> E (Longueur 1)C --> D --> F (Longueur 2)Somme des distances (C) = 2 + 1 + 1 + 1 + 2 = 7
```

Cela est connu comme la somme des distances telle que définie pour un seul nœud A ou C. Nous devons calculer ces distances pour chacun des nœuds de l'arbre.

Avant de résoudre ce problème générique, considérons une version simplifiée du même problème. Il dit que nous devons simplement calculer la somme des distances pour un nœud donné, mais nous ne considérerons que l'arbre enraciné au nœud donné pour les calculs.

Donc, pour le nœud C, cette version simplifiée du problème nous demanderait de calculer :

```
C --> D (Longueur 1)C --> E (Longueur 1)C --> D --> F (Longueur 2)Somme simplifiée des distances (C) = 1 + 1 + 2 = 4
```

C'est un problème beaucoup plus simple à résoudre de manière récursive et s'avérerait utile pour résoudre le problème original.

Considérons l'arbre simple suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/YGukie9COnJbj9YzCMPkILqssoRzZ98XsKjj)
_L'arbre simple que nous considérerons pour l'instant. Sont également mentionnées deux valeurs que nous calculerions pour chaque nœud._

Les nœuds B et C sont les enfants de la racine (c'est-à-dire, A).

Nous essayons de voir quelles informations nous pouvons utiliser des sous-problèmes (les enfants) pour calculer la réponse pour la racine `A`.

**Note** : ici, nous voulons simplement calculer la somme des chemins pour un nœud X donné à tous ses successeurs dans son propre sous-arbre (l'arbre enraciné au nœud X).

Il n'y a pas de chemins descendants du nœud B, et donc la somme des chemins est 0 pour le nœud `B` dans cet arbre. Regardons le nœud `C`. Donc, ce nœud a 3 successeurs différents en `F, D et E`. La somme des distances est la suivante :

```
C --> D (Chemin contenant juste 1 arête, donc somme des distances = 1)C --> D --> F (Chemin contenant 2 arêtes, donc somme des distances = 2)C --> E (Chemin contenant juste 1 arête, donc somme des distances = 1)
```

La somme de tous les chemins du nœud `C` à tous ses descendants est 4, et le nombre de tels chemins descendants est 3.

Notez la différence ici. La `somme_des_distances` ici compte le nombre d'arêtes dans chaque chemin — avec chaque arête se répétant plusieurs fois, probablement à cause de leur occurrence sur différents chemins — contrairement à `nombre_de_chemins`, qui compte, eh bien, le nombre de chemins ?.

Si vous regardez de près, vous réaliserez que le nombre de chemins descendants sera toujours le nombre de nœuds dans l'arbre que nous considérons (sauf la racine). Donc, pour l'arbre enraciné en C, nous avons 3 chemins, un pour le nœud D, un pour E, et un pour F. Cela signifie que le nombre de chemins d'un nœud donné aux nœuds successeurs est simplement le nombre total de nœuds descendants puisque c'est un arbre. Donc, pas de cycles ou d'arêtes multiples.

Maintenant, considérons le nœud A. Regardons tous les nouveaux chemins qui sont introduits à cause de ce nœud A. Oubliez le nœud B pour l'instant et concentrez-vous simplement sur le nœud enfant C correspondant à A. Les nouveaux ensembles de chemins que nous avons sont :

```
A --> C (Chemin contenant juste 1 arête, donc somme des distances = 1)A --> (C --> D)    (Chemin contenant 2 arêtes, donc somme des distances = 2)A --> (C --> E)    (Chemin contenant 2 arêtes, donc somme des distances = 2)A --> (C --> D --> F) (Chemin contenant 3 arêtes, donc somme des distances = 3)
```

À l'exception du premier chemin `A → C`, tous les autres sont les mêmes que ceux pour le nœud C, sauf que nous les avons simplement modifiés et incorporé un nœud supplémentaire `A`.

![Image](https://cdn-media-1.freecodecamp.org/images/FNIs7JAIXeg5R5upghwVCgMqEDtzN6zGr6e1)
_Somme des distances pour le nœud A ainsi que la contribution du nœud C._

Si vous regardez le diagramme ci-dessus, vous verrez un tuple de valeurs à côté de chacun des nœuds A, B et C.

```
(X, Y) où X est le nombre de chemins originaires de ce nœud et allant vers les descendants. Y est la somme des distances pour l'arbre enraciné au nœud donné. 
```

Puisque le nœud B n'a pas d'autres enfants, le seul chemin qu'il contribue est le chemin `A -->`; B `vers` le tuple de A (5, 9) ci-dessus. Donc parlons de C.

C avait trois chemins allant vers ses successeurs. Ces trois chemins (étendus par un nœud supplémentaire pour A) deviennent également trois chemins de A vers ses successeurs, entre autres.

```
N-Chemins[A] = (N-Chemins[C] + 1) + (N-Chemins[B] + 1)
```

C'est exactement la relation que nous recherchons en ce qui concerne le nombre de chemins (= nombre de nœuds successeurs dans l'arbre). Le 1 est dû au nouveau chemin de la racine à son enfant, c'est-à-dire `A -->`; C dans notre cas.

```
N-Chemins[A] = 3 + 1 + 0 + 1 = 5
```

En ce qui concerne la somme des distances, jetez un coup d'œil au diagramme et aux équations que nous venons d'écrire. La formule suivante devient très claire :

```
Somme-Dist[A] = (N-Chemins[C] + 1 + Somme-Dist[C]) + (N-Chemins[B] + 1 + Somme-Dist[B])
```

```
Somme-Dist[A] = (3 + 1 + 4 + 0 + 1 + 0) = 9
```

L'essentiel ici est `N-Chemins[C] + Somme-Dist[C]`. Nous les additionnons parce que tous les chemins de C à ses descendants deviennent finalement les chemins de A à ses descendants — sauf qu'ils commencent à A et passent par C, et donc chacune des longueurs de chemin est augmentée de 1. Il y a `N-Chemins[C]` chemins au total originaires de C et leur longueur totale est donnée par `Somme-Dist[C]`.

D'où le tuple correspondant à A = (5, 9). Le code Python pour l'algorithme que nous avons discuté ci-dessus est le suivant :

#### Le cas curieux du dictionnaire Visité :/

Si vous regardez le code ci-dessus de près, vous verrez ceci :

```
# Empêche la récursivité d'entrer dans un cycle.        self.visited[vertex] = 1
```

Le commentaire dit que ce dictionnaire `visited` est pour empêcher la récursivité d'entrer dans un cycle.

Si vous avez prêté attention jusqu'à présent, vous savez que nous traitons ici d'un `arbre`.

La définition d'une structure de données arborescente n'autorise pas l'existence de cycles. Si un cycle existe dans la structure, alors ce n'est plus un arbre, cela devient un graphe. Dans un arbre, il y a exactement un chemin entre toute paire de sommets. Un cycle signifierait qu'il y a plus d'un chemin entre une paire de sommets. Regardez les figures ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/oZr1Yj2zZaKRIHvge-IExVi7l4T9XyoyWzBU)
_Arbre vs Graphe. Montrant le cycle._

La structure de gauche est un arbre. Il n'a pas de cycles. Il y a un chemin unique entre deux sommets quelconques.

La structure de droite est un graphe, il existe un cycle dans le graphe et donc il y a plusieurs chemins entre toute paire de sommets. Pour ce graphe, il se trouve que toute paire de sommets a plus d'un chemin. Ce n'est pas nécessaire pour tous les graphes.

Presque toujours, on nous donne le nœud `racine` de l'arbre. Nous pouvons utiliser le nœud racine pour parcourir tout l'arbre **sans avoir à nous soucier des cycles en tant que tels_._**

Cependant, si vous avez lu l'énoncé du problème attentivement, il ne dit rien sur la racine de l'arbre.

Cela signifie qu'il n'y a pas de racine désignée pour l'arbre donné dans la question. Cela pourrait signifier qu'un arbre donné peut être visualisé et traité de tant de manières différentes selon ce que nous considérons comme la racine. Jetez un coup d'œil à plusieurs structures pour le même arbre mais avec différents nœuds racines.

![Image](https://cdn-media-1.freecodecamp.org/images/ocjHUA5ax4tYR1h3nZ1erX8dK1owrqa-bK1E)
_Multiples orientations du même arbre avec différentes racines._

Tant d'interprétations et de relations parent-enfant différentes sont possibles pour un **arbre non enraciné_._**

Donc, nous commençons avec le nœud `0` et faisons un parcours DFS de la structure donnée. Dans le processus, nous fixons les relations parent-enfant. Étant donné les arêtes dans le problème, nous construisons une structure de type graphe non orienté que nous convertissons en structure d'arbre. Regarder le code devrait clarifier certains de vos doutes :

Chaque nœud aurait un parent. La racine n'aura pas de parent, et de cette manière, le nœud `0` deviendra la racine de notre arbre. Notez que nous ne faisons pas ce processus séparément et ensuite nous calculons la `somme des distances vers le bas`. Étant donné un arbre, nous essayions de trouver, pour chaque nœud, la somme simplifiée des distances pour l'arbre enraciné à ce nœud.

Donc, la conversion du graphe en arbre se fait en une seule itération ainsi que la découverte de la somme des distances vers le bas pour chaque nœud.

J'ai reposté le code afin que le dictionnaire `visited` ait beaucoup plus de sens maintenant. Donc, une seule récursivité faisant tout cela pour nous. Bien !

#### Mettre tout ensemble

Maintenant que nous avons notre structure d'arbre définie, ainsi que les valeurs de `somme des distances allant vers le bas` définies pour nous, nous pouvons utiliser toutes ces informations pour résoudre le problème original de [Sum of Distances in a Tree.](https://leetcode.com/problems/sum-of-distances-in-tree/description/)

Comment faisons-nous cela ? Il est préférable d'expliquer cet algorithme à l'aide d'un exemple. Nous allons donc considérer l'arbre ci-dessous et nous allons exécuter l'algorithme pour un seul nœud. Jetons un coup d'œil à l'arbre que nous allons considérer.

![Image](https://cdn-media-1.freecodecamp.org/images/6JSzAk9Fqrl3w0azXxiCENYfTPXUqHF2q37a)
_L'arbre que nous allons considérer pour notre explication en continuant._

Le nœud pour lequel nous voulons trouver la somme des distances est `4`. Maintenant, si vous vous souvenez du problème plus simple que nous essayions de résoudre plus tôt, vous savez que nous avons déjà deux valeurs associées à chacun des nœuds :

1. `distances_vers_le_bas` qui est la somme des distances pour ce nœud **en ne considérant que l'arbre en dessous_._**
2. `nombre_de_chemins_vers_le_bas` qui est le nombre de chemins / nœuds dans l'arbre enraciné au nœud considéré.

Regardons la version annotée de l'arbre ci-dessus. L'arbre est annoté avec des tuples `(distances_vers_le_bas, nombre_de_chemins_vers_le_bas)`.

![Image](https://cdn-media-1.freecodecamp.org/images/r174UD-oYvBjEBAyj6cGjV3HnC4E01QYzP71)
_Exemple d'arbre avec des valeurs annotées pour tous les nœuds._

Appelons la valeur que nous voulons calculer pour chaque nœud `sod` qui signifie somme des distances, ce qui est ce que la question nous demande initialement de calculer.

Supposons que nous avons déjà calculé la réponse pour le nœud parent de `4` dans le diagramme ci-dessus. Nous avons donc maintenant les informations suivantes pour le nœud étiqueté `2` (le nœud parent) disponibles :

`(sod, distances_vers_le_bas, nombre_de_chemins_vers_le_bas)` = `(13, 4, 3)`

Faisons tourner l'arbre donné et visualisons-le de manière à ce que `2` soit essentiellement la racine de l'arbre.

![Image](https://cdn-media-1.freecodecamp.org/images/dTd8yp8IaZyBSz6STq8fKbl9Qrj5PoHMjBZC)
_Arbre tourné montrant que l'arbre enraciné à 4 doit être supprimé._

Maintenant, nous voulons supprimer la contribution de l'arbre enraciné à `4` de `sod(2)`. Considérons tous les chemins du nœud parent `2` à tous les autres nœuds sauf ceux de l'arbre enraciné à `4`.

```
2 --> 5 (1 arête)2 --> 1 (1 arête)2 --> 1 -->7 (2 arêtes)2 --> 1 --> 7 --> 9 (3 arêtes)2 --> 1 --> 7 --> 10 (3 arêtes)
```

```
Nombre de nœuds considérés = 6Somme des chemins restants c'est-à-dire sod(2) rem = 1 + 1 + 2 + 3 + 3 = 10
```

Voyons comment nous pouvons utiliser les valeurs que nous avons déjà calculées pour obtenir ces valeurs mises à jour.

```
* N = 8 (Nombre total de nœuds dans l'arbre. Cela restera le même pour chaque nœud. )* sod(2) = 13
```

```
* distances_vers_le_bas[4] = 1* nombre_de_chemins_vers_le_bas[4] = 1
```

```
* (distances_vers_le_bas[4] n'inclut pas le nœud 4 lui-même)N - 1 - distances_vers_le_bas[4] = 8 - 1 - 1 = 6
```

```
* sod(2) - 1 - distances_vers_le_bas[4] - nombre_de_chemins_vers_le_bas[4] = 13 - 1 - 1 - 1 = 10
```

Si vous vous souvenez de cela à partir de la fonction que nous avons définie précédemment, vous remarquerez que la contribution d'un nœud `enfant` aux deux valeurs `distances_vers_le_bas et nombre_de_chemins_vers_le_bas` est `n_chemins + 1` et `n_chemins + s_chemins + 1` respectivement. Naturellement, c'est ce que nous soustrayons pour obtenir l'arbre restant.

`sod(4)` représente la somme des arêtes sur tous les chemins originaires du nœud `4` dans l'arbre ci-dessus. Voyons comment nous pouvons le trouver en utilisant les informations que nous avons calculées jusqu'à présent.

`distances_vers_le_bas[4]` représente la réponse pour l'arbre enraciné au nœud `4` mais il ne considère que les chemins allant à ses successeurs, c'est-à-dire tous les nœuds de l'arbre enraciné à `4`. Pour notre exemple, le successeur de `4` est le nœud `6`. Donc, cela ajoutera directement à la réponse finale. Appelons cette valeur `propre_réponse`. Maintenant, comptabilisons tous les autres chemins.

```
4 --> 2 (1 arête)4 --> 2 --> 5 (1 + 1 arête)4 --> 2 --> 1 (1 + 1 arête)4 --> 2 --> 1 -->7 (1 + 2 arêtes)4 --> 2 --> 1 --> 7 --> 9 (1 + 3 arêtes)4 --> 2 --> 1 --> 7 --> 10 (1 + 3 arêtes)propre_réponse = 1
```

```
sod(4) = 1 + 1 + 2 + 2 + 3 + 4 + 4 = 17
```

```
sod(4) = propre_réponse + (N - 1 - distances_vers_le_bas[4]) + (sod(2) - 1 - distances_vers_le_bas[4] - nombre_de_chemins_vers_le_bas[4]) = 1 + 6 + 10 = 17
```

Avant de devenir fou et de commencer à faire cela, regardons le code et rassemblons toutes les choses que nous avons discutées dans l'exemple ci-dessus.

La relation récursive pour cette partie est la suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/SjqAkL8ty1q5KLF8JN7J-IgZys3GdrZq29us)
_Relation récursive pour la Somme des Distances, dans son intégralité._

### Ai-je juste vu « MEMOIZATION » dans le code ?

Oui, en effet !

Considérons l'exemple d'arbre suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/kThqJU4NZlzO5pgOSxMVe8M8x7s923hmtNZf)
_Exemple d'un arbre déséquilibré, également des appels récursifs pour le sommet 5_

La question nous demande de trouver la somme des distances pour tous les nœuds de l'arbre donné. Donc, nous ferions quelque chose comme ceci :

```
for i in range(N):    ans.append(find_distances(N))
```

Mais, si vous regardez l'arbre ci-dessus, l'appel récursif pour le nœud `5` finirait par calculer les réponses pour tous les nœuds de l'arbre. Donc, nous n'avons pas besoin de recalculer les réponses pour les autres nœuds encore et encore.

Par conséquent, nous finissons par stocker les valeurs déjà calculées dans un dictionnaire et les utiliser dans les calculs ultérieurs.

Essentiellement, la récursivité est basée sur le parent d'un nœud, et plusieurs nœuds peuvent avoir le même parent. Donc, la réponse pour le parent ne doit être calculée qu'une seule fois et ensuite être utilisée encore et encore.

Si vous avez réussi à lire l'article jusqu'ici (pas nécessairement d'une traite ?), vous êtes génial ?.

![Image](https://cdn-media-1.freecodecamp.org/images/O1NJkPAlOvAAmbOZxela4BQclXF2HP75wLf0)
_Source : [http://doodlecats.com/youre-awesome](http://doodlecats.com/youre-awesome" rel="noopener" target="_blank" title=")_

Si vous avez trouvé cet article utile, partagez-le autant que possible et répandez le ?. Santé !
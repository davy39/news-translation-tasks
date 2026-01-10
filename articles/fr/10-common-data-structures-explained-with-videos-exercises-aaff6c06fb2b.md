---
title: 10 structures de données courantes expliquées avec des vidéos + exercices
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2017-07-05T21:04:06.000Z'
originalURL: https://freecodecamp.org/news/10-common-data-structures-explained-with-videos-exercises-aaff6c06fb2b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*I5vtdhUqmRJ1zI1e.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: technology
  slug: technology
seo_title: 10 structures de données courantes expliquées avec des vidéos + exercices
seo_desc: '“Bad programmers worry about the code. Good programmers worry about data
  structures and their relationships.” — Linus Torvalds, creator of Linux

  Update _My video course about Algorithms is now live! Check out Algorithms in Motion
  from Manning Publica...'
---

> « Les mauvais programmeurs s'inquiètent du code. Les bons programmeurs s'inquiètent des structures de données et de leurs relations. » — Linus Torvalds, créateur de Linux

> ****Mise à jour**** _Mon cours vidéo sur les algorithmes est maintenant disponible ! Consultez [Algorithms in Motion de Manning Publications](https://www.manning.com/livevideo/algorithms-in-motion?a_aid=algmotion&a_bid=9022d293). Obtenez 39 % de réduction sur mon cours en utilisant le code '39carnes' ! Ou vous pouvez obtenir 50 % de réduction sur mon [cours Deep Learning in Motion](https://www.manning.com/livevideo/grokking-deep-learning-in-motion?a_aid=algmotion&a_bid=5d7bc0ba) avec le code 'vlcarnes2'._

Les structures de données sont une partie essentielle du développement logiciel et l'un des sujets les plus courants pour les questions d'entretien d'embauche des développeurs.

La bonne nouvelle est qu'elles sont essentiellement des formats spécialisés pour organiser et stocker des données.

Je vais vous enseigner 10 des structures de données les plus courantes — juste ici dans cet article court.

J'ai intégré des vidéos que j'ai créées pour chacune de ces structures de données. J'ai également lié des exemples de code pour chacune d'elles, qui montrent comment les implémenter en JavaScript.

Et pour vous donner un peu de pratique, j'ai lié des défis du [curriculum de freeCodeCamp](https://www.freecodecamp.org).

Notez que certaines de ces structures de données incluent la complexité temporelle en notation Big O. Cela n'est pas inclus pour toutes car la complexité temporelle dépend parfois de la manière dont elle est implémentée. Si vous souhaitez en savoir plus sur la notation Big O, consultez mon [article à ce sujet](https://medium.freecodecamp.org/big-o-notation-simply-explained-with-illustrations-and-video-87d5a71c0174) ou [cette vidéo](https://www.youtube.com/watch?v=KSNx22U4uWE&index=39&list=PLWKjhJtqVAbmfoj2Th9fvxhHIeqFO7wOy) par [Briana Marie](https://www.freecodecamp.org/news/10-common-data-structures-explained-with-videos-exercises-aaff6c06fb2b/undefined).

Notez également que même si je montre comment implémenter ces structures de données en JavaScript, pour la plupart d'entre elles, vous n'aurez jamais besoin de les implémenter vous-même, sauf si vous utilisiez un langage de bas niveau comme C.

JavaScript (comme la plupart des langages de haut niveau) a des implémentations intégrées de nombreuses structures de données.

Néanmoins, savoir comment implémenter ces structures de données vous donnera un énorme avantage dans votre recherche d'emploi en tant que développeur, et pourrait s'avérer utile lorsque vous essayez d'écrire du code haute performance.

### Listes chaînées

Une liste chaînée est l'une des structures de données les plus basiques. Elle est souvent comparée à un tableau, car de nombreuses autres structures de données peuvent être implémentées avec un tableau ou une liste chaînée. Chacune a ses avantages et ses inconvénients.

![Image](https://cdn-media-1.freecodecamp.org/images/0*I2krMHdnjzUqidwf.png)
_Représentation d'une liste chaînée_

Une liste chaînée est composée d'un groupe de nœuds qui représentent ensemble une séquence. Chaque nœud contient deux choses : les données réelles stockées (qui peuvent être de n'importe quel type de données) et un pointeur (ou lien) vers le nœud suivant dans la séquence. Il existe également des listes doublement chaînées où chaque nœud a un pointeur vers l'élément suivant et l'élément précédent dans la liste.

Les opérations les plus basiques dans une liste chaînée sont l'ajout d'un élément à la liste, la suppression d'un élément de la liste et la recherche d'un élément dans la liste.

[Voir le code pour une liste chaînée en JavaScript ici.](https://codepen.io/beaucarnes/pen/ybOvBq?editors=0012)

#### Complexité temporelle des listes chaînées

|Algorithme|Moyenne|Pire cas|
|:--------|-------|----------|
|Espace    |0(n)   |0(n)      |
|Recherche   |0(n)   |0(n)      |
|Insertion   |0(1)   |0(1)      |
|Suppression   |0(1)   |0(1)      |

#### Défis freeCodeCamp

* [Travailler avec des nœuds dans une liste chaînée](https://learn.freecodecamp.org/coding-interview-prep/data-structures/work-with-nodes-in-a-linked-list)
* [Créer une classe de liste chaînée](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-a-linked-list-class)
* [Supprimer des éléments d'une liste chaînée](https://learn.freecodecamp.org/coding-interview-prep/data-structures/remove-elements-from-a-linked-list)
* [Rechercher dans une liste chaînée](https://learn.freecodecamp.org/coding-interview-prep/data-structures/search-within-a-linked-list)
* [Supprimer des éléments d'une liste chaînée par index](https://learn.freecodecamp.org/coding-interview-prep/data-structures/remove-elements-from-a-linked-list-by-index)
* [Ajouter des éléments à un index spécifique dans une liste chaînée](https://learn.freecodecamp.org/coding-interview-prep/data-structures/add-elements-at-a-specific-index-in-a-linked-list)
* [Créer une liste doublement chaînée](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-a-doubly-linked-list)
* [Inverser une liste doublement chaînée](https://learn.freecodecamp.org/coding-interview-prep/data-structures/reverse-a-doubly-linked-list)

### Piles

Une pile est une structure de données de base où vous ne pouvez insérer ou supprimer des éléments qu'au sommet de la pile. C'est un peu similaire à une pile de livres. Si vous voulez regarder un livre au milieu de la pile, vous devez d'abord enlever tous les livres au-dessus.

La pile est considérée comme LIFO (Last In First Out) — ce qui signifie que le dernier élément que vous mettez dans la pile est le premier élément qui en sort.

![Image](https://cdn-media-1.freecodecamp.org/images/0*kAUG_JFNvKLpPs-7.png)
_Représentation d'une pile_

Il y a trois opérations principales qui peuvent être effectuées sur les piles : insérer un élément dans une pile (appelé 'push'), supprimer un élément de la pile (appelé 'pop'), et afficher le contenu de la pile (parfois appelé 'pip').

[Voir le code pour une pile en JavaScript ici.](http://codepen.io/beaucarnes/pen/yMBGbR?editors=0012)

#### Complexité temporelle des piles

|Algorithme|Moyenne|Pire cas|
|:--------|-------|---------:|
|Espace    |0(n)   |0(n)      |
|Recherche   |0(n)   |0(n)      |
|Insertion   |0(1)   |0(1)      |
|Suppression   |0(1)   |0(1)      |

#### Défis freeCodeCamp

* [Comprendre le fonctionnement d'une pile](https://learn.freecodecamp.org/coding-interview-prep/data-structures/learn-how-a-stack-works)
* [Créer une classe de pile](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-a-stack-class)

### Files d'attente

Vous pouvez penser à une file d'attente comme une ligne de personnes dans un magasin d'alimentation. La première personne dans la ligne est la première à être servie. Tout comme une file d'attente.

![Image](https://cdn-media-1.freecodecamp.org/images/0*INQFkmoG8FWYuNCG.png)
_Représentation d'une file d'attente_

Une file d'attente est considérée comme FIFO (First In First Out) pour démontrer la manière dont elle accède aux données. Cela signifie qu'une fois qu'un nouvel élément est ajouté, tous les éléments qui ont été ajoutés avant doivent être retirés avant que le nouvel élément puisse être retiré.

Une file d'attente a seulement deux opérations principales : enqueue et dequeue. Enqueue signifie insérer un élément à l'arrière de la file d'attente et dequeue signifie retirer l'élément de devant.

[Voir le code pour une file d'attente en JavaScript ici.](http://codepen.io/beaucarnes/pen/QpaQRG?editors=0012)

#### Complexité temporelle des files d'attente

|Algorithme|Moyenne|Pire cas|
|:--------|-------|----------|
|Espace    |0(n)   |0(n)      |
|Recherche   |0(n)   |0(n)      |
|Insertion   |0(1)   |0(1)      |
|Suppression   |0(1)   |0(1)      |

#### Défis freeCodeCamp

* [Créer une classe de file d'attente](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-a-queue-class)
* [Créer une classe de file d'attente prioritaire](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-a-priority-queue-class)
* [Créer une file d'attente circulaire](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-a-circular-queue)

### Ensembles

![Image](https://cdn-media-1.freecodecamp.org/images/1*R0EJij5oyOxP8gJ2jXm5Jw.png)
_Représentation d'un ensemble_

La structure de données ensemble stocke des valeurs sans ordre particulier et sans valeurs répétées. En plus de pouvoir ajouter et supprimer des éléments d'un ensemble, il existe quelques autres fonctions importantes d'ensemble qui fonctionnent avec deux ensembles à la fois.

* Union — Cela combine tous les éléments de deux ensembles différents et retourne cela comme un nouvel ensemble (sans doublons).
* Intersection — Étant donné deux ensembles, cette fonction retourne un autre ensemble qui contient tous les éléments faisant partie des deux ensembles.
* Différence — Cela retourne une liste d'éléments qui sont dans un ensemble mais PAS dans un ensemble différent.
* Sous-ensemble — Cela retourne une valeur booléenne qui montre si tous les éléments d'un ensemble sont inclus dans un ensemble différent.

[Voir le code pour implémenter un ensemble en JavaScript ici.](http://codepen.io/beaucarnes/pen/dvGeeq?editors=0012)

#### Défis freeCodeCamp

* [Créer une classe d'ensemble](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-a-set-class)
* [Supprimer d'un ensemble](https://learn.freecodecamp.org/coding-interview-prep/data-structures/remove-from-a-set)
* [Taille de l'ensemble](https://learn.freecodecamp.org/coding-interview-prep/data-structures/size-of-the-set)
* [Effectuer une union sur deux ensembles](https://learn.freecodecamp.org/coding-interview-prep/data-structures/perform-a-union-on-two-sets)
* [Effectuer une intersection sur deux ensembles de données](https://learn.freecodecamp.org/coding-interview-prep/data-structures/perform-an-intersection-on-two-sets-of-data)
* [Effectuer une différence sur deux ensembles de données](https://learn.freecodecamp.org/coding-interview-prep/data-structures/perform-a-difference-on-two-sets-of-data)
* [Effectuer une vérification de sous-ensemble sur deux ensembles de données](https://learn.freecodecamp.org/coding-interview-prep/data-structures/perform-a-subset-check-on-two-sets-of-data)
* [Créer et ajouter à des ensembles en ES6](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-and-add-to-sets-in-es6)
* [Supprimer des éléments d'un ensemble en ES6](https://learn.freecodecamp.org/coding-interview-prep/data-structures/remove-items-from-a-set-in-es6)
* [Utiliser .has et .size sur un ensemble ES6](https://learn.freecodecamp.org/coding-interview-prep/data-structures/use--has-and--size-on-an-es6-set)
* [Utiliser Spread et Notes pour l'intégration ES5 Set()](https://learn.freecodecamp.org/coding-interview-prep/data-structures/use-spread-and-notes-for-es5-set-integration)

### Cartes

Une carte est une structure de données qui stocke des données en paires clé/valeur où chaque clé est unique. Une carte est parfois appelée tableau associatif ou dictionnaire. Elle est souvent utilisée pour des recherches rapides de données. Les cartes permettent les opérations suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gu_lK-CJmho9llQAVD01Kw.png)
_Représentation d'une carte_

* l'ajout d'une paire à la collection
* la suppression d'une paire de la collection
* la modification d'une paire existante
* la recherche d'une valeur associée à une clé particulière

[Voir le code pour implémenter une carte en JavaScript ici.](https://codepen.io/beaucarnes/pen/jBjobG?editors=0012)

#### Défis freeCodeCamp

* [Créer une structure de données de carte](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-a-map-data-structure)
* [Créer une carte JavaScript ES6](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-an-es6-javascript-map)

### Tables de hachage

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ic9dWfQsehh74OidwUZgkA.png)
_Représentation d'une table de hachage et d'une fonction de hachage_

Une table de hachage est une structure de données de carte qui contient des paires clé/valeur. Elle utilise une fonction de hachage pour calculer un index dans un tableau de compartiments ou d'emplacements, à partir duquel la valeur souhaitée peut être trouvée.

La fonction de hachage prend généralement une chaîne comme entrée et produit une valeur numérique. La fonction de hachage doit toujours donner le même numéro de sortie pour la même entrée. Lorsque deux entrées sont hachées vers la même sortie numérique, cela s'appelle une collision. L'objectif est d'avoir peu de collisions.

Ainsi, lorsque vous entrez une paire clé/valeur dans une table de hachage, la clé est traitée par la fonction de hachage et transformée en un nombre. Cette valeur numérique est ensuite utilisée comme la clé réelle sous laquelle la valeur est stockée. Lorsque vous essayez d'accéder à la même clé à nouveau, la fonction de hachage traitera la clé et retournera le même résultat numérique. Le nombre sera ensuite utilisé pour rechercher la valeur associée. Cela fournit un temps de recherche très efficace O(1) en moyenne.

[Voir le code pour une table de hachage ici.](https://codepen.io/beaucarnes/pen/VbYGMb?editors=0012)

#### Complexité temporelle des tables de hachage

|Algorithme|Moyenne|Pire cas|
|:--------|-------|----------|
|Espace    |0(n)   |0(n)      |
|Recherche   |0(1)   |0(n)      |
|Insertion   |0(1)   |0(n)      |
|Suppression   |0(1)   |0(n)      |

#### Défis freeCodeCamp

* [Créer une table de hachage](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-a-hash-table)

### Arbre binaire de recherche

![Image](https://cdn-media-1.freecodecamp.org/images/0*x5o1G1UpM1RfLpyx.png)
_Arbre binaire de recherche_

Un arbre est une structure de données composée de nœuds. Il a les caractéristiques suivantes :

1. Chaque arbre a un nœud racine (en haut).
2. Le nœud racine a zéro ou plusieurs nœuds enfants.
3. Chaque nœud enfant a zéro ou plusieurs nœuds enfants, et ainsi de suite.

Un _arbre binaire de recherche_ ajoute ces deux caractéristiques :

1. Chaque nœud a jusqu'à deux enfants.
2. Pour chaque nœud, ses descendants gauches sont inférieurs au nœud actuel, qui est inférieur aux descendants droits.

Les arbres binaires de recherche permettent une recherche, un ajout et une suppression rapides des éléments. La manière dont ils sont configurés signifie que, en moyenne, chaque comparaison permet aux opérations de sauter environ la moitié de l'arbre, de sorte que chaque recherche, insertion ou suppression prend un temps proportionnel au logarithme du nombre d'éléments stockés dans l'arbre.

[Voir le code pour un arbre binaire de recherche en JavaScript ici.](https://codepen.io/beaucarnes/pen/ryKvEQ?editors=0011)

#### Complexité temporelle de la recherche binaire

|Algorithme|Moyenne|Pire cas|
|:--------|-------|----------|
|Espace    |0(n)   |0(n)      |
|Recherche   |0(log n)   |0(n)      |
|Insertion   |0(log n)   |0(n)      |
|Suppression   |0(log n)   |0(n)      |

#### Défis freeCodeCamp

* [Trouver la valeur minimale et maximale dans un arbre binaire de recherche](https://learn.freecodecamp.org/coding-interview-prep/data-structures/find-the-minimum-and-maximum-value-in-a-binary-search-tree)
* [Ajouter un nouvel élément à un arbre binaire de recherche](https://learn.freecodecamp.org/coding-interview-prep/data-structures/add-a-new-element-to-a-binary-search-tree)
* [Vérifier si un élément est présent dans un arbre binaire de recherche](https://learn.freecodecamp.org/coding-interview-prep/data-structures/check-if-an-element-is-present-in-a-binary-search-tree)
* [Trouver la hauteur minimale et maximale d'un arbre binaire de recherche](https://learn.freecodecamp.org/coding-interview-prep/data-structures/find-the-minimum-and-maximum-height-of-a-binary-search-tree)
* [Utiliser la recherche en profondeur dans un arbre binaire de recherche](https://learn.freecodecamp.org/coding-interview-prep/data-structures/use-depth-first-search-in-a-binary-search-tree)
* [Utiliser la recherche en largeur dans un arbre binaire de recherche](https://learn.freecodecamp.org/coding-interview-prep/data-structures/use-breadth-first-search-in-a-binary-search-tree)
* [Supprimer un nœud feuille dans un arbre binaire de recherche](https://learn.freecodecamp.org/coding-interview-prep/data-structures/delete-a-leaf-node-in-a-binary-search-tree)
* [Supprimer un nœud avec un enfant dans un arbre binaire de recherche](https://learn.freecodecamp.org/coding-interview-prep/data-structures/delete-a-node-with-one-child-in-a-binary-search-tree)
* [Supprimer un nœud avec deux enfants dans un arbre binaire de recherche](https://learn.freecodecamp.org/coding-interview-prep/data-structures/delete-a-node-with-two-children-in-a-binary-search-tree)
* [Inverser un arbre binaire](https://learn.freecodecamp.org/coding-interview-prep/data-structures/invert-a-binary-tree)

### Trie

Le trie (prononcé 'try'), ou arbre de préfixes, est un type d'arbre de recherche. Un trie stocke des données en étapes où chaque étape est un nœud dans le trie. Les tries sont souvent utilisés pour stocker des mots pour une recherche rapide, comme une fonction d'auto-complétion de mots.

![Image](https://cdn-media-1.freecodecamp.org/images/0*lqKJ7WnpvZ4fbUYd.png)
_Représentation d'un trie_

Chaque nœud dans un trie de langage contient une lettre d'un mot. Vous suivez les branches d'un trie pour épeler un mot, une lettre à la fois. Les étapes commencent à se ramifier lorsque l'ordre des lettres diverge des autres mots dans le trie, ou lorsqu'un mot se termine. Chaque nœud contient une lettre (donnée) et un booléen qui indique si le nœud est le dernier nœud d'un mot.

Regardez l'image et vous pouvez former des mots. Commencez toujours par le nœud racine en haut et travaillez vers le bas. Le trie montré ici contient les mots ball, bat, doll, do, dork, dorm, send, sense.

[Voir le code pour un trie en JavaScript ici.](https://codepen.io/beaucarnes/pen/mmBNBd?editors=0011)

#### Défis freeCodeCamp

* [Créer un arbre de recherche trie](https://learn.freecodecamp.org/coding-interview-prep/data-structures/create-a-trie-search-tree)

### Tas binaire

Un tas binaire est un autre type de structure de données d'arbre. Chaque nœud a au plus deux enfants. De plus, c'est un arbre complet. Cela signifie que tous les niveaux sont complètement remplis jusqu'au dernier niveau et que le dernier niveau est rempli de gauche à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lu5E1YaakS3JFcCqOsiniw.png)
_Représentations de tas min et max_

Un tas binaire peut être soit un tas min soit un tas max. Dans un tas max, les clés des nœuds parents sont toujours supérieures ou égales à celles des enfants. Dans un tas min, les clés des nœuds parents sont inférieures ou égales à celles des enfants.

L'ordre entre les niveaux est important, mais l'ordre des nœuds au même niveau n'est pas important. Sur l'image, vous pouvez voir que le troisième niveau du tas min a les valeurs 10, 6 et 12. Ces nombres ne sont pas dans l'ordre.

[Voir le code pour un tas en JavaScript ici.](https://codepen.io/beaucarnes/pen/JNvENQ?editors=0011)

#### Complexité temporelle des tas binaires

|Algorithme|Moyenne|Pire cas|
|:--------|-------|----------|
|Espace    |0(n)   |0(n)      |
|Recherche   |0(1)   |0(log n)      |
|Insertion   |0(log n)   |0(log n)      |
|Suppression   |0(1)   |0(1)      |

#### Défis freeCodeCamp

* [Insérer un élément dans un tas max](https://learn.freecodecamp.org/coding-interview-prep/data-structures/insert-an-element-into-a-max-heap)
* [Supprimer un élément d'un tas max](https://learn.freecodecamp.org/coding-interview-prep/data-structures/remove-an-element-from-a-max-heap)
* [Implémenter le tri par tas avec un tas min](https://learn.freecodecamp.org/coding-interview-prep/data-structures/implement-heap-sort-with-a-min-heap)

### Graphe

Les graphes sont des collections de nœuds (également appelés sommets) et des connexions (appelées arêtes) entre eux. Les graphes sont également connus sous le nom de réseaux.

Un exemple de graphes est un réseau social. Les nœuds sont des personnes et les arêtes sont des amitiés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fYG3B8hi4O2kk6aHvFB5mg.png)

Il existe deux principaux types de graphes : dirigés et non dirigés. Les graphes non dirigés sont des graphes sans direction sur les arêtes entre les nœuds. Les graphes dirigés, en revanche, sont des graphes avec une direction dans leurs arêtes.

Deux façons courantes de représenter un graphe sont une liste d'adjacence et une matrice d'adjacence.

![Image](https://cdn-media-1.freecodecamp.org/images/1*01PEzMXTsl9UOnqiGpfnWw.png)
_Graphe de matrice d'adjacence_

Une liste d'adjacence peut être représentée comme une liste où le côté gauche est le nœud et le côté droit liste tous les autres nœuds auxquels il est connecté.

Une matrice d'adjacence est une grille de nombres, où chaque ligne ou colonne représente un nœud différent dans le graphe. À l'intersection d'une ligne et d'une colonne se trouve un nombre qui indique la relation. Les zéros signifient qu'il n'y a pas d'arête ou de relation. Les uns signifient qu'il y a une relation. Les nombres supérieurs à un peuvent être utilisés pour montrer différents poids.

Les algorithmes de parcours sont des algorithmes pour parcourir ou visiter des nœuds dans un graphe. Les principaux types d'algorithmes de parcours sont la recherche en largeur et la recherche en profondeur. L'une des utilisations est de déterminer à quel point les nœuds sont proches d'un nœud racine. Voyez comment implémenter la recherche en largeur en JavaScript dans la vidéo ci-dessous.

[Voir le code pour la recherche en largeur sur un graphe de matrice d'adjacence en JavaScript.](https://codepen.io/beaucarnes/pen/XgrXvw?editors=0011)

#### Complexité temporelle de la recherche binaire

|Algorithme|Temps|
|:--------|-------|
| Stockage       | O(|V|+|E|) |
| Ajouter un sommet    | O(1)       |
| Ajouter une arête      | O(1)       |
| Supprimer un sommet | O(|V|+|E|) |
| Supprimer une arête   | O(|E|)     |
| Requête         | O(|V|)     |

#### Défis freeCodeCamp

* [Liste d'adjacence](https://learn.freecodecamp.org/coding-interview-prep/data-structures/adjacency-list)
* [Matrice d'adjacence](https://learn.freecodecamp.org/coding-interview-prep/data-structures/adjacency-matrix)
* [Matrice d'incidence](https://learn.freecodecamp.org/coding-interview-prep/data-structures/incidence-matrix)
* [Recherche en largeur](https://learn.freecodecamp.org/coding-interview-prep/data-structures/breadth-first-search)
* [Recherche en profondeur](https://learn.freecodecamp.org/coding-interview-prep/data-structures/depth-first-search)

### Plus

Le livre _Grokking Algorithms_ est le meilleur livre sur le sujet si vous êtes nouveau dans les structures de données/algorithmes et n'avez pas de formation en informatique. Il utilise des explications faciles à comprendre et des illustrations amusantes, dessinées à la main (par l'auteur qui est un développeur principal chez Etsy) pour expliquer certaines des structures de données présentées dans cet article.

[**Grokking Algorithms: An illustrated guide for programmers and other curious people**](https://www.amazon.com/gp/product/1617292230/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=bcar08-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1617292230&linkId=83471c93327ff24766dd812f9799f95a)  
[_Résumé Grokking Algorithms est un guide illustré et convivial qui vous apprend à appliquer des algorithmes courants à...www.amazon.com](https://www.amazon.com/gp/product/1617292230/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=bcar08-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1617292230&linkId=83471c93327ff24766dd812f9799f95a)

Ou vous pouvez consulter mon cours vidéo basé sur ce livre : [Algorithms in Motion de Manning Publications](https://www.manning.com/livevideo/algorithms-in-motion?a_aid=algmotion&a_bid=9022d293). Obtenez 39 % de réduction sur mon cours en utilisant le code '39carnes' !

![Image](https://cdn-media-1.freecodecamp.org/images/0*3yaoPZXjRmbBm2ef.png)
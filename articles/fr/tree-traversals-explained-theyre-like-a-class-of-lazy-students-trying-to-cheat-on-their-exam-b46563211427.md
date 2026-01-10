---
title: 'Les parcours d''arbres expliqués : Ils sont comme une classe d''étudiants
  paresseux essayant de tricher à leur examen'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-14T11:48:22.000Z'
originalURL: https://freecodecamp.org/news/tree-traversals-explained-theyre-like-a-class-of-lazy-students-trying-to-cheat-on-their-exam-b46563211427
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tCYpJPPIECnHUWw9BR_vrg.png
tags:
- name: algorithms
  slug: algorithms
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
- name: Trees
  slug: trees
seo_title: 'Les parcours d''arbres expliqués : Ils sont comme une classe d''étudiants
  paresseux essayant de tricher à leur examen'
seo_desc: 'By Sachin Malhotra

  Imagine that you are enrolled in a math class at one of the most prestigious universities
  of the world.

  You have an exam coming up real soon. Obviously, you want to perform well on the
  exam.

  The thing about this university is that ...'
---

Par Sachin Malhotra

Imaginez que vous êtes inscrit à un cours de mathématiques dans l'une des universités les plus prestigieuses du monde.

Vous avez un examen qui approche très bientôt. Évidemment, vous voulez bien performer à l'examen.

Le problème avec cette université, c'est qu'elle a un ensemble de professeurs maladroits. Donc, tricher est vraiment simple. Vous pouvez facilement copier sur le gars assis derrière et devant vous sans vous faire prendre.

Les professeurs, afin de prendre le contrôle de ce problème, ont proposé deux solutions :

* Le nombre d'étudiants assis dans une classe n'est jamais fixe. Et les personnes assises dans une classe passant le test changent d'un test à l'autre.
* L'arrangement des sièges est publié cinq minutes avant l'examen. L'arrangement des sièges est alphabétique. Mais comme les étudiants ne sont jamais fixes et que de nouveaux peuvent être ajoutés ou d'anciens retirés d'une classe de manière aléatoire, l'arrangement doit être explicitement publié pour que les étudiants sachent exactement où ils doivent s'asseoir.

Disons que vous êtes l'un de ces étudiants paresseux qui veulent tricher, malgré les conséquences. Cinq minutes avant l'examen, lorsque l'arrangement des sièges est publié, comment trouvez-vous qui est assis devant vous et qui est derrière vous le plus rapidement possible ?

Vous ne pourrez pas tricher si vous ne parlez pas à ces deux personnes au préalable et ne stratégisez pas, n'est-ce pas ?

### L'arrangement des sièges

Donc, les professeurs ont publié l'arrangement des sièges pour le premier test jamais conduit de cette manière. Disons qu'il y avait N étudiants. Si ces étudiants devaient rester les mêmes d'un test à l'autre, alors il aurait été très facile de tricher, n'est-ce pas ? Parce que l'arrangement des sièges est toujours fait alphabétiquement.

Par conséquent, les professeurs continuent d'ajouter ou de retirer des étudiants de cette liste d'un test à l'autre, et ne publient ces modifications qu'avant chaque test. De cette façon, les étudiants ne pourraient jamais savoir de manière déterministe avant un test qui serait assis devant ou derrière eux.

Considérons ce problème en termes algorithmiques. On nous donne une liste de N éléments où les éléments dans ce cas sont les noms des étudiants. Cette liste varie d'un examen à l'autre, de sorte que de nouveaux éléments peuvent être ajoutés à la liste ou que des éléments existants peuvent être retirés de la liste.

Étant donné la liste des modifications à un moment donné T et un nom N, nous devons déterminer les éléments B et A, tels que B viendrait juste avant N et A viendrait juste après N si la liste devait être triée.

Maintenant, regardons quelles structures de données sont disponibles pour nous et laquelle conviendrait le mieux à ce problème.

### Oh Array, mon vieux ami, vas-tu m'aider ?

Utiliser un tableau semble être une approche plutôt directe.

* Nous pouvons simplement mettre tous les noms sur la liste publiée dans un tableau.
* Ensuite, nous trions tous les noms (la liste des noms publiée peut être arrangée de manière aléatoire) lexicographiquement
* Et puis nous pouvons trouver notre nom dans la liste en utilisant une procédure de recherche binaire. Cela nous donnerait le prédécesseur et le successeur.

Cela semble être une approche viable pour résoudre ce problème. Le problème en question, cependant, est que les étudiants ne sont jamais fixes d'un examen à l'autre. Et donc la liste qui a été publiée pour le tout premier examen varierait dynamiquement lorsque de nouveaux étudiants étaient ajoutés et que d'anciens étaient retirés.

Nous pouvons trier la liste pour la toute première fois, puis continuer à ajouter de nouveaux éléments et à retirer les anciens en conséquence.

Cependant, la complexité de l'ajout ou de la suppression d'un élément d'un tableau est de l'ordre de `O(n)`. Puisque le nombre d'étudiants pourrait être très grand, et que nous ne savons pas combien de modifications il y aurait avant un nouveau test, cela prendrait beaucoup de temps et le test commencerait avant que nous puissions résoudre le problème. Rappelez-vous que les modifications sont publiées juste cinq minutes avant le test.

Alors, quelle autre structure de données avons-nous où l'insertion et la suppression peuvent être faites très rapidement ?

### Hmmmm, peut-être que Linked List est mon vrai ami après tout

En ce qui concerne une liste chaînée, elle a ses propres problèmes lorsqu'il s'agit de ce type de situation. Initialement, nous devons trier la liste des éléments lexicographiquement. Puisque cela est une opération ponctuelle, car elle n'est à faire que pour le premier examen, le temps pris ici n'a pas vraiment d'importance.

À partir de l'examen suivant, seules les modifications sont publiées. L'ajout ou la suppression d'un élément d'une liste chaînée est une opération en temps constant, à condition de connaître l'emplacement de cet élément dans la liste.

Trouver un élément dans une liste chaînée est une opération en temps linéaire — cela prend `O(n)`. Je sais qu'il existe des concepts comme les [skip lists](https://en.wikipedia.org/wiki/Skip_list), mais pourquoi plonger dans quelque chose comme cela lorsque nous pouvons résoudre ce problème de manière beaucoup plus efficace en utilisant un autre type de structure de données ?

### Entrez les arbres binaires de recherche, le nouveau venu en ville

Regardons comment nous pouvons modéliser nos données en utilisant un arbre binaire de recherche (BST). Ensuite, nous verrons comment un BST peut nous aider à résoudre le problème que nous nous sommes initialement fixé.

Un arbre binaire de recherche est essentiellement un arbre binaire avec une manière spéciale d'ordonner les nœuds.

**Pour un nœud avec la clé _k_, chaque clé dans le sous-arbre gauche est inférieure à _k_ et chaque clé dans le sous-arbre droit est supérieure à _k_.**

Dans notre cas, les clés seront les noms des étudiants.

Considérons l'exemple suivant pour voir comment un arbre binaire de recherche est construit. Cela devrait apporter une plus grande clarté à la structure de données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fvAa2lIvPcl3pEF0EwjT_g.png)
_[http://btechsmartclass.com/DS/images/BST%20Construction.png](http://btechsmartclass.com/DS/images/BST%20Construction.png" rel="noopener" target="_blank" title=")_

Construire un arbre binaire de recherche n'est pas suffisant. Nous devons nous assurer qu'il est [équilibré](http://www.stoimen.com/blog/2012/07/03/computer-algorithms-balancing-a-binary-search-tree/). La raison pour laquelle nous disons qu'un arbre binaire de recherche doit être équilibré est que, s'il ne l'est pas, alors nous pouvons avoir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4rHcryjV-ySjXORcxzqQeA.png)
_Un arbre binaire de recherche incliné à gauche._

Cela est connu comme un arbre binaire de recherche incliné. Si une telle chose se produit, alors le BST se transforme essentiellement en une liste chaînée et cela ne nous est d'aucune utilité. Par conséquent, nous avons cette notion de garder un BST équilibré afin que nous ne rencontrions pas ce problème.

La notion d'équilibré est définie différemment par différentes approches, comme les arbres Red Black ou AVL. Une explication plus approfondie de ces arbres est hors du cadre de cet article.

Revenons à l'organisation de nos données dans un BST équilibré : les clés de notre BST seraient les noms des étudiants, et la correspondance lexicographique serait utilisée pour déterminer la structure du BST.

Supposons qu'il y avait un million d'étudiants passant le test. Si notre arbre binaire de recherche est équilibré, alors la complexité de l'exécution de toute opération est limitée par `O(log(n))`. **Donc, pour 1 million de nœuds, le nombre maximum de nœuds à scanner serait de seulement 14.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*WX_no1yjkuvyro78viF21w.png)

C'est une grande réduction de complexité simplement en organisant les données d'une certaine manière. C'est l'avantage de représenter les données dans un **arbre binaire de recherche équilibré**.

Le principal problème avec l'approche basée sur les tableaux était que nous ne pouvions pas insérer ou supprimer efficacement un élément du tableau. Et le problème avec l'approche de la liste chaînée était qu'il n'y avait aucun moyen efficace pour nous de trouver un élément dans la liste chaînée même si elle était triée.

En ce qui concerne un arbre binaire de recherche équilibré, la complexité temporelle pour insérer, supprimer ou rechercher un élément est limitée par `O(log(n))`. Et c'est précisément ce qui rend cette structure de données extrêmement excitante.

Cependant, nous n'avons toujours pas résolu notre problème initial. Étant donné le nom d'un étudiant, nous voulons trouver l'étudiant assis juste derrière et juste devant lui. Cela revient à trouver le **successeur et le prédécesseur dans l'ordre dans l'arbre binaire de recherche donné.**

### Parcours en ordre et ordre trié dans un BST

Une propriété intéressante des arbres binaires de recherche est que nous pouvons récupérer les éléments dans l'ordre trié (même inversé) en effectuant un parcours en ordre sur l'arbre binaire de recherche.

Donc, le successeur en ordre d'un nœud X est l'élément qui vient juste après X dans le parcours en ordre sur le BST donné. Pour notre problème de tricherie, ce successeur en ordre serait l'étudiant assis devant nous.

Le prédécesseur en ordre d'un nœud X est l'élément qui vient juste avant X dans le parcours en ordre (ou l'élément qui vient juste après X dans le **inverse** du parcours en ordre) sur le BST donné. Pour notre problème de tricherie, ce prédécesseur en ordre serait l'étudiant assis juste derrière nous.

### Successeur en ordre dans un BST

Il y a deux cas différents que nous devons gérer lors de la recherche du successeur en ordre d'un nœud dans un BST.

**Le premier cas** est lorsque le fils droit existe pour le nœud dont nous essayons de trouver le successeur en ordre. Considérons l'exemple suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HT_4eHf-yWORRyajZGfbqg.png)

Ici, nous voulions trouver le successeur en ordre du nœud mis en évidence 8. Puisqu'il a un fils droit, le **successeur en ordre serait le nœud le plus à gauche dans l'arbre avec un fils droit, ou 15 comme racine**. Donc ce nœud serait 10 dans ce cas.

**Le deuxième cas** est lorsqu'il n'y a pas de fils droit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*z6Q879IxNa5B6jRC6s1CaQ.png)

Dans ce cas, le successeur en ordre a deux possibilités :

1. L'une est lorsque le nœud considéré est le fils gauche de son parent. Dans ce cas, le successeur en ordre serait le parent lui-même. Donc pour notre cas donné, le successeur en ordre serait 10.
2. Le deuxième cas est lorsque le nœud actuel est le fils droit de son parent. Et il n'a pas de fils droit. Donc c'est le nœud le plus à droite dans le BST et il n'a pas de successeur en ordre.

Gérer le premier cas est assez simple pour un arbre binaire de recherche. Pour le deuxième cas, où le nœud donné n'a pas de fils droit (ou de pointeurs parent), nous devrons nous appuyer sur notre bon vieux mécanisme de récursion et effectuer un parcours en ordre jusqu'à ce que nous déterminions le parent de notre nœud donné.

Donc, la complexité du pire cas peut être O(n) si le cas ci-dessus se produit.

En utilisant cet algorithme, nous pouvons rapidement trouver l'étudiant qui sera assis juste devant nous à l'examen.

### Prédécesseur en ordre dans un BST

C'est exactement l'inverse du cas précédent.

Encore une fois, nous devons gérer deux cas différents lors de la recherche du prédécesseur en ordre d'un nœud dans un BST. Regardez les diagrammes suivants et essayez de relier les deux cas mentionnés ici.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8LEzigzWixE_psr5BDeqdA.png)

C'est le cas où le nœud a un fils gauche. Nous devons trouver le fils le plus à droite de l'arbre enraciné à ce fils gauche — le nœud le plus à droite dans l'arbre enraciné à 2.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MXJ1lCqihi0bmcfelm5WFA.png)

Pas de fils gauche. Donc nous devons trouver le parent.

Si vous regardez de près, j'ai simplement inversé l'ordre de parcours ici et le reste du code est le même qu'avant. (NOTE : ce code est utilisé lorsqu'il n'y a pas de fils gauche du nœud pour lequel nous voulons trouver le prédécesseur en ordre).

**Le prédécesseur en ordre devient le successeur en ordre inverse.**

Eh bien, maintenant que vous savez comment vous devriez organiser la liste d'arrangement des sièges de la classe, allez obtenir de bonnes notes 😉. Je plaisante ! Tricher est mauvais — ne le faites jamais !

J'espère que vous avez compris l'idée principale derrière les différentes utilisations des structures de données et comment trouver le successeur et le prédécesseur en ordre dans un BST.

EDIT : Kudos à [Divya Godayal](https://www.freecodecamp.org/news/tree-traversals-explained-theyre-like-a-class-of-lazy-students-trying-to-cheat-on-their-exam-b46563211427/undefined) pour avoir pointé un ensemble de grandes erreurs dans le premier brouillon et aussi pour avoir assuré que l'article coule bien :) :)
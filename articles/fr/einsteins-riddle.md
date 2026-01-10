---
title: Comment résoudre l'énigme des cinq maisons d'Einstein
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-09-08T15:36:22.000Z'
originalURL: https://freecodecamp.org/news/einsteins-riddle
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Capture.JPG
tags:
- name: logic
  slug: logic
- name: puzzles
  slug: puzzles
seo_title: Comment résoudre l'énigme des cinq maisons d'Einstein
seo_desc: 'I recently learned about a logic puzzle online that apparently only 2%
  of people can solve.

  There are a few different incarnations of it – some have slightly different wording,
  different names, or change the items in the riddle slightly. But they are...'
---

J'ai récemment découvert une énigme logique en ligne que seulement 2 % des gens peuvent résoudre.

Il existe plusieurs versions de cette énigme – certaines ont des formulations légèrement différentes, des noms différents ou changent légèrement les éléments de l'énigme. Mais elles reposent toutes sur le même problème de base.

L'énigme elle-même est utilisée comme référence dans l'évaluation des [problèmes de satisfaction de contraintes](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem) pour les algorithmes informatiques.

## Qu'est-ce que l'énigme d'Einstein ?

Même l'origine de cette énigme est un peu floue. Elle est célèbre sous le nom d'**Énigme d'Einstein** car elle aurait été créée par Einstein lorsqu'il était jeune, pour s'amuser. D'autres disent qu'elle était utilisée par Einstein pour sélectionner les étudiants en doctorat les plus intelligents qu'il superviserait.

Mais certaines sources en ligne affirment qu'elle a en réalité été inventée par l'auteur d'_Alice au pays des merveilles_, [Lewis Carroll](https://en.wikipedia.org/wiki/Lewis_Carroll).

Il est peu probable qu'elle ait été écrite par Einstein, mais cela n'a pas vraiment d'importance. Ce qui compte, c'est qu'avec une compréhension de base des tables de vérité (et un peu de patience), vous pouvez la résoudre, vous aussi.

## Comment résoudre l'énigme d'Einstein

Je vais maintenant vous donner une liste d'indices, et vous devrez répondre à une question à la fin de ces indices.

Pour être parfaitement clair, tous les indices sont suffisants pour la résoudre. Vous n'avez pas besoin d'hints supplémentaires, et il n'y a pas d'hypothèses que je m'attends à ce que vous connaissiez.

> Il y a 5 maisons peintes de cinq couleurs différentes.  
> Dans chaque maison vit une personne de nationalité différente.  
> Ces cinq propriétaires boivent un certain type de boisson, fument une certaine marque de cigare et possèdent un certain animal de compagnie.  
> Aucun propriétaire n'a le même animal de compagnie, ne fume la même marque de cigare ou ne boit la même boisson.

* Le Britannique vit dans la maison rouge
* Le Suédois a des chiens comme animaux de compagnie
* Le Danois boit du thé
* La maison verte est à gauche de la maison blanche
* La personne qui fume des Pall Malls élève des oiseaux
* Le propriétaire de la maison jaune fume des Dunhill
* Le propriétaire de la maison verte boit du café
* L'homme vivant dans la maison du centre boit du lait
* Le Norvégien vit dans la première maison (la plus à gauche)
* L'homme qui fume des Blends vit à côté de celui qui a des chats
* L'homme qui a des chevaux vit à côté de l'homme qui fume des Dunhill
* Le propriétaire qui fume des BlueMaster boit de la bière
* L'Allemand fume des Princes
* Le Norvégien vit à côté de la maison bleue
* L'homme qui fume des Blends a un voisin qui boit de l'eau

Maintenant, pour résoudre l'énigme, **dites-moi qui possède le poisson** ?

Je l'ai résolue, mais cela m'a pris quelques tentatives et un peu de gribouillage sur papier.

## Comment j'ai abordé le problème

Pour résoudre le problème, la première chose que j'ai faite a été d'essayer de regrouper les indices. Il y a deux références à la maison verte dans les indices, alors j'ai essayé de "résoudre" et de considérer ces deux indices ensemble lorsque c'était possible.

J'ai également rempli immédiatement la boisson de la maison centrale, car un indice vous le dit directement, et j'ai pu remplir immédiatement la nationalité de la maison la plus à gauche.

J'ai essentiellement dessiné une grille très basique et éliminé ou rempli les possibilités en me basant initialement uniquement sur les indices. Ensuite, au fur et à mesure que je remplissais plus d'informations, j'ai pu ajouter plus de détails sur les autres maisons.

Je ne veux pas continuer avec les hints si vous voulez résoudre cela par vous-même, mais c'est un point de départ.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-29.png)
_Une capture d'écran d'une partie d'un tableau 5x5 avec toutes les différentes possibilités de Nationalité, Couleur, Boisson, Animal de compagnie et Cigare fumé qui peuvent être supprimées en cliquant._

Pour essayer de faciliter la tâche à quiconque souhaite la résoudre ou vérifier sa réponse, j'ai créé un site basique que vous pouvez trouver ici : [http://einsteins-riddle.com/](http://einsteins-riddle.com/) – la capture d'écran ci-dessus est une partie de la grille sur le site.

Sur ce site, vous trouverez un tableau avec toutes les options présentées sous forme de boutons cliquables. La grille est initialement remplie avec toutes les possibilités, et au fur et à mesure que vous en apprenez plus, vous pouvez éliminer des possibilités jusqu'à ce qu'il ne reste finalement qu'une seule option.

En bas se trouve un bouton "Vérifier la réponse" qui évaluera ce qu'il reste sur votre grille.

Essayez de la résoudre et voyez comment vous vous en sortez ! Si vous préférez le faire sur papier, n'hésitez pas.

Je vous souhaite bonne chance 😊

Si cela vous bloque et que vous voulez savoir comment la résoudre, vous pouvez trouver la solution [ici](https://udel.edu/~os/riddle-solution.html).

## Pourquoi les tables de vérité sont-elles utiles ?

J'aime essayer de résoudre ces problèmes de tables de vérité, car cela aide à améliorer la clarté de ma pensée.

Parfois, lorsque je code et que je dois soigneusement considérer des états booléens complexes dans mon code (pas **ceci**, et pas **cela OU ceci** et **cela** (et pas **ceux-là**)), je pense que ces énigmes m'aident à raisonner plus clairement pour simplifier mon code.

Elles m'aident également à planifier techniquement mon approche d'un problème, depuis le tout début jusqu'à la solution finale.

Je commence avec un ensemble de base de exigences et sans idée de la façon dont elles s'emboîtent. Mais au fur et à mesure que j'avance, je peux suivre un processus de collecte de faits, de vérification des cas limites, de vérification/test de ma logique par rapport aux exigences et enfin de soumission de mon travail. Toutes ces étapes se traduisent exactement par le développement logiciel.

Chaque fois que vous avez un ensemble compliqué d'états qui vous confond, dessinez une table de vérité basique. Ou représentez le problème comme vous le souhaitez. Le décomposer en problèmes de plus en plus petits vous permettra de résoudre presque n'importe quoi.

## **Conclusion**

J'espère que cette énigme a été un casse-tête agréable, et que vous l'avez résolue autant ou aussi peu que cela vous a amusé.

Je partage mes écrits sur [Twitter](https://twitter.com/kealanparr) si vous avez aimé cet article et souhaitez en voir plus.
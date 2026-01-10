---
title: Comment optimiser vos Pull Requests pour des revues de code efficaces
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-04T22:24:06.000Z'
originalURL: https://freecodecamp.org/news/optimize-pull-requests-for-reviewer-happiness
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b42740569d1a4ca2abb.jpg
tags:
- name: best practices
  slug: best-practices
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Comment optimiser vos Pull Requests pour des revues de code efficaces
seo_desc: "By Chang Wang\nImagine reading a novel, but having the chapters sliced\
  \ up and reordered alphabetically by title. Or what if you were watching a movie,\
  \ but the scenes were reordered alphabetically by their first words of spoken dialog?\
  \ \nPuzzling a narr..."
---

Par Chang Wang

Imaginez lire un roman, mais avec les chapitres découpés et réordonnés par ordre alphabétique de titre. Ou que se passerait-il si vous regardiez un film, mais que les scènes étaient réordonnées par ordre alphabétique des premiers mots de dialogue prononcés ?

Reconstituer une narration à partir de ces pièces mélangées peut sembler amusant, mais l'intérêt s'estomperait rapidement si la révision et la compréhension de ces histoires faisaient partie de vos responsabilités quotidiennes.

## Narrations mélangées dans le code

La vue "Files changed" pour les Pull Requests sur Github liste les changements par ordre alphabétique selon le chemin du fichier. C'est parfait pour les petites branches de fonctionnalités (feature branches) que nous visons, mais il y a souvent des changements complexes avec des pièces interdépendantes qui entraînent inévitablement de grands diffs sur plusieurs fichiers. Ces changements peuvent être accablants pour les relecteurs qui utilisent la vue des fichiers triés par ordre alphabétique.

Au lieu de cela, les relecteurs peuvent visualiser ces changements dans des morceaux plus petits et plus isolés (c'est-à-dire commit par commit). Le message de chaque commit peut transmettre ce que le changement est censé accomplir. Et les commits en séquence transmettent une narration logique expliquant pourquoi ces changements étaient nécessaires pour cette branche de fonctionnalité. Tout cela rend le travail du relecteur beaucoup plus facile et agréable.

## Préparer un historique de commits clair

L'utilisation approfondie du staging partiel (partial-staging), de l'amendement (amending) et du rebasage (rebasing) sont autant d'outils qui aideront à obtenir un historique de commits propre que vos relecteurs apprécieront.

Évitez de créer des commits au périmètre flou. Vous avez peut-être oublié de committer des changements qui auraient dû être logiquement regroupés et avez continué à éditer le fichier. C'est normal, cela arrive tout le temps. Ce n'est pas parce qu'un fichier contient des changements que tous ces changements doivent être committés.

Vous n'avez pas non plus à annuler les changements qui ne sont pas liés. Vous pouvez utiliser le staging interactif pour choisir quels morceaux d'un fichier doivent être mis en staging pour le commit et lesquels doivent être laissés pour un futur commit.

Rebasez de manière agressive pour éviter de créer des commits dont les changements seront plus tard modifiés de manière significative, voire supprimés.

Il peut être frustrant pour un relecteur de passer du temps à comprendre ce qui a changé dans un commit, pour découvrir ensuite qu'il a essentiellement perdu son temps sur du code mort quelques commits plus tard. Amendez/fixez/squashez (Amend/fixup/squash) ces changements avant de demander une revue !

Si cela semble fastidieux, ce qui est une réaction raisonnable puisque Git n'est guère connu pour son UX, je recommande vivement d'envisager une interface graphique Git (Git GUI) qui peut rendre une grande partie de cela [indolore](https://share.getcloudapp.com/OAubWjJJ).

## Demander une revue

Après avoir demandé à des collègues de revoir la Pull Request, **arrêtez de rebaser vos commits !** Poussez plutôt les changements demandés par les relecteurs dans de nouveaux commits.

"Mais cela ne va-t-il pas à l'encontre de l'objectif de maintenir un historique de commits propre ?"

Maintenir un historique de commits propre n'était pas l'objectif final, mais plutôt un moyen de rendre vos changements plus faciles à comprendre et à réviser pour les autres. Une fois qu'une revue a commencé, modifier vos commits rend en fait vos nouveaux changements _plus difficiles_ à réviser.

Supposons que vous ayez ouvert une Pull Request avec ces commits :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-263.png)
_(pseudo commits à des fins de démonstration (facilité de référence) ; ne numérotez pas réellement vos messages de commit)_

Un relecteur laisse ensuite un commentaire sur un élément lié aux changements effectués dans le premier commit. Si vous modifiez ce commit et effectuez un force push, vos anciens commits disparaissent de la Pull Request, et tous les commits depuis ceux qui ont été rebasés apparaîtront comme de nouveaux commits suite à cette revue.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-266.png)
_Tous les commits apparaissent comme nouveaux_

Qu'est-ce qui a changé depuis la dernière fois qu'un relecteur a regardé la Pull Request ?
Quels commits ont été modifiés et nécessitent donc une attention particulière, et lesquels n'ont pas bougé et peuvent être ignorés ?

La seule façon de le savoir est de regarder tous les commits qui ont été poussés de force (force pushed) et d'essayer de se rappeler si ce que vous voyez maintenant est différent de ce qu'il y avait auparavant.

Si vous essayez de cliquer sur le fichier qui a été commenté pour voir si le commentaire a été pris en compte, ou pour obtenir plus de contexte sur le code autour de la zone où le commentaire a été fait, vous serez accueilli par ce charmant télescope :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screen-Recording-2020-04-29-at-11.10-PM.gif)

Pour en revenir à l'analogie de la lecture d'un roman – imaginez en être à la moitié, le laisser de côté pendant un jour ou deux, et quand vous le reprenez, on vous dit que des passages importants dans les parties que vous avez lues ont changé, et que la seule façon de savoir exactement ce qui a changé est de tout relire depuis le début. Pas amusant.

Alternativement, voici à quoi ressembleraient les changements si vous poussiez de nouveaux commits séparés à la place :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-265.png)
_Pouvez-vous dire ce qui est nouveau ?_

Vous devriez toujours rebaser par rapport à master, mais tant que les commits qui ont déjà été revus n'ont pas changé de manière significative, vos relecteurs n'auront pas besoin de tous les parcourir à nouveau. Envisagez d'ajouter un commentaire après un force-push avec un lien vers le commit le plus récemment révisé afin que les relecteurs puissent reprendre là où ils s'étaient arrêtés.

## Changements approuvés !

Au moment où votre PR a été approuvée, votre branche comporte probablement maintenant quelques commits qui semblent un peu désordonnés. Je recommande de faire un squash-merge et de ne pas s'en inquiéter. L'objectif de clarté a été atteint. Les messages de commit des PR fusionnées en squash (squash-merged) contiendront des liens vers les Pull Requests où les commits squashed peuvent être retrouvés.

Je ne sais pas si le squash merging est toujours controversé en 2020, au cas où il le serait encore – React le fait 🤷‍♂️

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-270.png)
_Si Dan Abramov sautait d'un pont, le feriez-vous ? (Oui. La bonne réponse est "oui")_

Cependant, vous estimez peut-être fermement que les commits d'une PR sont suffisamment significatifs et importants pour justifier d'être fusionnés dans master en tant que commits séparés. Si c'est le cas, c'est à ce moment-là que vous pouvez vous en donner à cœur joie sur le rebasage jusqu'à ce que tous les diffs soient fusionnés (squashed) dans les commits parfaits avant de fusionner sans squash.

## tldr :

* chaque commit dans une PR doit raconter une histoire de ce que ce commit change, et idéalement aussi ce qui a motivé le changement
* rebasez agressivement avant d'ouvrir la pull/merge request et de solliciter des relecteurs
* après le début de la revue, _arrêtez de modifier les commits de votre branche et poussez-en de nouveaux_
* après approbation, effectuez un squash merge (ou squashez sélectivement les commits puis fusionnez)

## À garder à l'esprit

Comme la deuxième partie de ce flux de travail est fortement influencée par la manière dont Github gère les commits rebasés, il se peut qu'un jour ces préoccupations soient traitées par la plateforme et que ce flux de travail ne soit plus nécessaire. D'ici là, merci de penser à optimiser vos commits pour vos relecteurs :)

### Ressources connexes :

[Stacked Git](http://www.procode.org/stgit/doc/tutorial.html) est un outil de gestion des historiques de commits que j'ai trouvé plus intuitif que le rebasage interactif via CLI. Le tutoriel peut sembler intimidant, mais c'est peut-être un problème de conception lié au fait d'avoir tout mis (y compris les instructions d'utilisation d'Emacs) sur une seule page. C'est en fait assez facile à apprendre et à utiliser petit à petit.

Please let me know ([@CheapSteak](https://twitter.com/CheapSteak)) if you either have objections to this approach, or suggestions on how it could be improved.
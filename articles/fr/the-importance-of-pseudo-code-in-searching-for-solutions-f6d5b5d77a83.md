---
title: L'Importance du Pseudo-code dans la Recherche de Solutions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-13T20:28:06.000Z'
originalURL: https://freecodecamp.org/news/the-importance-of-pseudo-code-in-searching-for-solutions-f6d5b5d77a83
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nOgcKHfPr41FTbaKc1rmkw.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: L'Importance du Pseudo-code dans la Recherche de Solutions
seo_desc: 'By Gordon Davidescu

  So you sign up for Free Code Camp and start plowing through lesson after lesson
  them like an industrial lawn mower. Everything is going great, until all of a sudden
  you hit one of the big code challenges — and you freeze.

  You don’...'
---

Par Gordon Davidescu

Vous vous inscrivez à Free Code Camp et commencez à parcourir les leçons les unes après les autres comme une tondeuse industrielle. Tout se passe bien, jusqu'à ce que soudainement, vous tombiez sur l'un des grands défis de code — et vous bloquez.

Vous ne savez pas par où commencer. Le défi demande tellement de vous. Vous n'êtes même pas sûr de savoir comment faire tout ce qu'il vous demande.

Prenons le défi [Tic Tac Toe](https://www.freecodecamp.com/challenges/build-a-tic-tac-toe-game) par exemple. C'est un jeu, il doit être jouable, il doit permettre de choisir un côté. Et, bien sûr, il doit aussi être gagnable (et perdable).

Je pense que cela arrive à beaucoup de personnes qui fréquentent Free Code Camp, même si elles ont une expérience préalable en programmation. Cela m'est arrivé plusieurs fois pendant mon bref passage en tant que majeur en informatique.

En bref, il est facile d'être submergé. Et en l'absence d'une personne à qui demander « Par où dois-je même commencer ? », vous pourriez désespérer et ne rien faire. Rien d'autre que jouer au dernier jeu du type _cliquez sur ce cookie_ jusqu'à ce que l'inspiration frappe.

#### Entrez le pseudo-code

Au lieu de ne rien faire, essayez d'utiliser le pseudo-code. Il vous aidera à créer une carte de par où commencer et comment procéder au mieux.

Qu'est-ce que le pseudo-code ? En bref, c'est quelque chose que vous écrivez qui n'est pas du code _réel_ dans un langage de programmation, mais que, si quelqu'un le lisait, il serait clair ce qui se passe.

Demandez à n'importe quel enfant comment fonctionne le tic-tac-toe et il pourra vous le dire. (À l'opposé du jeu de Patrick _tic tac_. Seule une personne ayant un fils de cinq ans qui a vu cet épisode de Bob l'éponge quelques fois peut l'expliquer).

Vous avez votre plateau. Un joueur est X. Un joueur est O. L'un d'eux commence. Et puis l'autre. Chacun place son symbole dans les cases inoccupées. Ils continuent à alterner les tours jusqu'à ce que l'un d'eux ait trois à la suite, ou que le plateau soit plein et que personne ne gagne. Nouvelle partie.

Maintenant, voyons comment cela se déroule en pseudo-code. Voici ce que j'écrirais :

```
Dessiner un plateau à l'écran — trois cases de large par trois cases de haut. Si l'une des cases est cliquée avant qu'une nouvelle partie ne commence, faire apparaître un avertissement que leur partie n'a pas encore commencé Bouton : nouvelle partie.
```

```
Lorsqu'on clique, variable joueur = x ou o selon ce qu'ils ont cliqué.
```

```
Au clic sur une case :Si il y a un X ou un O dans la case, ne rien faire.Si il n'y a ni X ni O dans la case, changer l'espace du plateau avec le joueur.  Si la rangée du haut ou la rangée du milieu ou la rangée du bas ou la première colonne ou la colonne du milieu ou l'une des diagonales sont toutes des pièces du joueur --      Annoncer que le joueur gagne !     Demander si le joueur veut rejouer !     Si oui, recommencer depuis le début !   Si le joueur n'a pas gagné et que le plateau n'est pas plein, laisser l'ordinateur jouer son tour.      Tour de l'ordinateur :      De la première case à la dernière case, vérifier s'il y a deux pièces du joueur dans la première, la deuxième ou la dernière rangée ou colonne ou diagonale et, lorsqu'elles sont trouvées, placer une pièce de l'ordinateur dans le troisième espace inoccupé.      Si aucune de ces situations n'est trouvée :          De la première case à la dernière case, vérifier chacune pour voir si elle est vide.          Dès qu'une case vide est trouvée, y placer la pièce de l'ordinateur.          Si la rangée du haut ou la rangée du milieu ou la rangée du bas ou la première colonne ou la colonne du milieu ou l'une des diagonales sont toutes des pièces de l'ordinateur --      Annoncer que l'ordinateur gagne !     Demander si le joueur veut rejouer !     Si oui, recommencer depuis le début !   Si l'ordinateur n'a pas gagné et que le plateau n'est pas plein, recommencer depuis le début avec le tour du joueur.
```

```
Si le plateau est plein, partie terminée ! Nouvelle manche ? Demander au joueur.
```

C'est tout. C'est tout le jeu, décomposé en quatre étapes de base. Maintenant vient la partie vraiment amusante, pour ainsi dire — la recherche.

Puisque vous avez maintenant une carte de la façon dont l'application va fonctionner, vous pouvez examiner chacune des étapes et faire des recherches sur la manière de la réaliser.

Tout d'abord, comment dessiner un plateau en HTML avec des sections cliquables ?

Il devient rapidement évident que vous devriez probablement utiliser la balise <div> en HTML. Certains diraient d'utiliser 'onclick' en JavaScript. D'autres utiliseraient jQuery.

Comment l'ordinateur sait-il qu'il y a deux pièces de l'adversaire à la suite ? Eh bien, cela ne dépend-il pas de la manière dont vous stockez les valeurs des X et des O sur le plateau derrière la scène visuelle ?

Bien sûr. C'est l'une des nombreuses questions que vous pourrez vous poser (et à notre ami _Professeur Google_) une fois que vous connaissez la carte de votre application, pour ainsi dire.

Il existe de nombreuses façons de faire de l'intelligence artificielle pour l'ordinateur — comment faire en sorte que l'ordinateur décide où il va placer sa pièce lorsqu'il est à son tour ? J'ai choisi de le rendre principalement défensif (en ce sens qu'il cherche d'abord à voir s'il peut bloquer le joueur) avant de passer à l'offensive.

Ce n'est qu'une façon d'aborder le problème — demandez-vous, comment choisirais-je quelle case utiliser pour placer ma pièce.

Une fois que vous avez tout pensé, il ne s'agit plus que de traduire ce que vous avez conçu du pseudo-code en code réel. Ayant décomposé votre application en morceaux gérables, vous pouvez rapidement évaluer ce qui doit être fait.

Bon pseudo-codage (et bon codage réel, une fois que vous l'aurez maîtrisé).

_Vous voyez ce cœur là-bas ? Donnez-lui un clic ! Merci d'avance._
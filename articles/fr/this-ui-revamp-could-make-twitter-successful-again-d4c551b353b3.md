---
title: Comment améliorer Twitter ? Une refonte de l'interface utilisateur serait un
  bon point de départ.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-09T06:57:52.000Z'
originalURL: https://freecodecamp.org/news/this-ui-revamp-could-make-twitter-successful-again-d4c551b353b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*O3YZrr_LO--eNZykWD17KQ.png
tags:
- name: Design
  slug: design
- name: social media
  slug: social-media
- name: 'tech '
  slug: tech
- name: Twitter
  slug: twitter
- name: UX
  slug: ux
seo_title: Comment améliorer Twitter ? Une refonte de l'interface utilisateur serait
  un bon point de départ.
seo_desc: 'By Daryll Santos

  It’s no secret that Twitter has been struggling to grow its user base. To fix this,
  they’ve laid out a long-term strategy to turn around its business by focusing on
  five areas:


  Its core service

  Live-streaming video

  The site’s “creat...'
---

Par Daryll Santos

Ce n'est un secret pour personne que Twitter a du mal à développer sa base d'utilisateurs. Pour remédier à cela, ils ont élaboré une stratégie à long terme pour redresser leur entreprise en se concentrant sur cinq domaines :

1. Leur service principal
2. La vidéo en direct
3. Les "créateurs et influenceurs" du site
4. La sécurité
5. Les développeurs

Deux éléments de cette déclaration ont retenu mon attention : 1) se concentrer sur leur service principal (tweeter) et 2) la vidéo en direct (Periscope).

Ces éléments ont retenu mon attention car récemment, j'ai convaincu un ami de rejoindre Twitter. Lorsqu'il est arrivé sur le fil d'actualité, ses premières questions ont été "comment tweeter ?" et "comment passer en direct ?".

Étant donné que ce sont des fonctionnalités clés de Twitter, je pense qu'elles devraient être les choses les plus intuitives à faire, même pour un nouvel utilisateur.

### Objectifs

1. **Rendre le tweeting intuitif** : Tweeter est la force motrice derrière Twitter ; c'est le pilier qui anime leur produit. Ainsi, dès qu'un nouvel utilisateur termine le processus d'inscription, il devrait savoir immédiatement comment tweeter.
2. **Rendre le passage en direct plus intuitif** : [Twitter a dépensé 86,6 millions de dollars pour Periscope](http://www.recode.net/2015/5/11/11562534/twitter-paid-over-86-million-for-periscope-and-niche) pour offrir à ses utilisateurs la possibilité de diffuser des vidéos en direct via leur application mobile. C'est aussi un [énorme marché](https://medium.com/looklivecam/on-demand-livestreaming-960a492d69d1#.z9u58217s), et il n'est pas surprenant que Facebook l'attaque si agressivement. Dans cette optique, pourquoi cette fonctionnalité n'est-elle pas plus accessible ? Par exemple, je me souviens d'une fois où mon ami était à un concert et essayait de diffuser en direct un artiste montant sur scène. Il a manqué ce moment parce qu'il n'a pas pu passer en direct assez rapidement.
3. ***Bonus* Mettre à jour le fil d'actualité Twitter** : J'ai toujours trouvé que le fil d'accueil était un peu trop serré. Quelques changements mineurs l'amélioreraient considérablement. Cela fait aussi un moment qu'ils ne l'ont pas mis à jour, donc une nouvelle apparence serait la bienvenue !

### Personas utilisateurs

Bien sûr, il est toujours important de connaître ses utilisateurs. [37 % des utilisateurs de Twitter ont entre 18 et 29 ans](http://sproutsocial.com/insights/new-social-media-demographics/#twitter), et c'est aussi leur plus grande base d'utilisateurs, ce qui signifie que les utilisateurs de Twitter sont principalement des millennials, accros aux réseaux sociaux et à la diffusion de vidéos en direct. Sachant cela, il est impératif de rendre les fonctionnalités importantes de Twitter (Tweeter et Periscope) plus accessibles pour eux.

![Image](https://cdn-media-1.freecodecamp.org/images/vlzhq00QVvwI9IoRnuk0GIuSI272xDWC-eO2)

### Recherche utilisateur

Pour m'assurer de faire les meilleurs choix de design possibles et valider mes objectifs, j'ai mené une enquête pour cerner les pensées des utilisateurs de Twitter. Plus précisément, je cherchais à découvrir :

1. Le niveau de facilité d'utilisation du tweeting pour les nouveaux utilisateurs
2. La connaissance des utilisateurs de Twitter de la possibilité de passer en direct (Periscope)
3. Le niveau de facilité d'utilisation du direct (Periscope)

#### 1. Facilité d'utilisation pour les nouveaux utilisateurs

J'ai mené une enquête et j'ai découvert que seulement 5/10 utilisateurs (50 %) ont trouvé le tweeting facile à faire dès leur première tentative. Pour leur service principal, le fait qu'il ne soit facile que pour 5/10 personnes semble être un peu préoccupant, car sans lui, il n'y a pas de Twitter. Je pense définitivement qu'une amélioration de l'interface utilisateur pourrait aider à cela.

![Image](https://cdn-media-1.freecodecamp.org/images/hCxRjbIZ9uxFxR8ScJHpe3jDTvbsJG5q4k0n)

#### 2./3. Connaissance de Periscope et niveau de facilité d'utilisation

J'ai été surpris de constater que seulement 43 % (10/23) des utilisateurs de Twitter que j'ai interrogés savaient qu'ils pouvaient diffuser des vidéos en direct ! De plus, il ne s'agissait pas de n'importe quels utilisateurs aléatoires. Il s'agissait de personnes utilisant Twitter depuis des années et appartenant aux groupes d'âge 18-24 et 25-34.

![Image](https://cdn-media-1.freecodecamp.org/images/Pwlj5dbmhWSZcjjoMISBxN1iDM3CrvnjT6Gf)

![Image](https://cdn-media-1.freecodecamp.org/images/BbO06HpvcQ1z8gGC25ugaHhrC8fL1yM1YmAp)
_Peri  what?_

### Analyse technique

Tout d'abord, comprendre la disposition actuelle de Twitter nous informera sur la manière dont il répond aux besoins de ses utilisateurs. J'ai décomposé l'interface utilisateur et l'ai divisée en blocs, car chaque bloc a un but, et dans chaque bloc, nous verrons ce qui peut être amélioré et comment. Examinons cela :

![Image](https://cdn-media-1.freecodecamp.org/images/MjmdyUj71nFQ6h8uVPEfJvE-dujuaAQNiPLR)

* Bloc 1 : C'est essentiellement le fondement de Twitter, car c'est là que les utilisateurs vont pour tweeter. Je pense qu'il peut être amélioré car le bouton Tweet est en dehors de la zone naturelle du pouce (voir le changement 1 ci-dessous).
* Bloc 2 : C'est là que se trouve le fil d'actualité Twitter. Il n'y a rien de mal avec lui, mais je pense qu'une légère amélioration peut le rendre meilleur.
* Bloc 3 : C'est là que les utilisateurs naviguent entre les différentes vues de Twitter. Il n'y a rien de mal avec lui, mais comme les utilisateurs ont constamment les yeux rivés ici, un ajout clé les aiderait probablement à atteindre leurs objectifs à long terme.

### Résultats

#### Changement #1 : Améliorer le service principal : Déplacer et modifier le bouton Tweet

![Image](https://cdn-media-1.freecodecamp.org/images/gEW2dpWH1EBltowlm3dy25z-WhDlDbfj9d0h)
_La zone du pouce_

En déplaçant le bouton Tweet au centre-bas, en ajoutant une étiquette, en augmentant sa taille et en lui donnant une couleur, les utilisateurs sauront exactement à quoi sert ce bouton rien qu'en le regardant. De plus, en lui donnant une couleur de fond, il agit comme un appel à l'action qui dit essentiellement à l'utilisateur "Hé ! Appuie sur moi !".

Surtout, il est dans un emplacement plus facile pour les utilisateurs à appuyer grâce à sa position confortable pour les pouces (voir l'image ci-dessus).

![Image](https://cdn-media-1.freecodecamp.org/images/mxOyEv32QmKgMXwv9ZgGSx8nnT2DGegFfbaH)
_Maintenant, Tweeter est "Naturel" au lieu de "Aïe"._

#### Changement #2 : Améliorer la diffusion vidéo en direct en déplaçant Periscope Live vers le fil d'accueil

En lien avec la concentration de Twitter sur la diffusion en direct (Periscope), l'idée de ce changement m'est venue lorsque j'ai vu mon ami rater ce moment au concert qu'il voulait enregistrer en direct, car il a mis trop de temps à atteindre Periscope. Au moment où il est passé en direct, l'introduction qu'il voulait capturer avait déjà été manquée. Oui, il aurait pu l'activer plus tôt. Mais parfois, les moments de la vie doivent être saisis rapidement.

Le processus actuel en 3 étapes pour passer en direct est le suivant :

1. Appuyer sur le bouton Tweet
2. Attendre que la vue Tweet glisse vers le haut
3. Appuyer sur "Live"

Pour plus de rapidité, cela devrait être :

1. Appuyer sur "Live"

C'est tout. Juste une étape.

Pour ce faire, j'ai dû retirer le bouton Live de la vue Tweet et le ramener à la vue d'accueil. En le ramenant là, il est accessible en seulement 1 étape.

![Image](https://cdn-media-1.freecodecamp.org/images/Vut8yUGFO8S1De6WFxfmMrzrrOEZjwc1XDs-)
_Le direct est pour capturer les moments de la vie, donc il devrait être dans un endroit où vous pouvez y accéder rapidement._

#### Changement #3 : Mettre à jour le fil d'actualité

Le fil d'actualité de Twitter est plutôt bon, mais je pense que quelques changements mineurs peuvent l'améliorer.

* J'ai changé l'icône Twitter pour qu'elle ressemble moins aux boutons à proximité (Messages & Live) car leurs poids semblaient trop similaires. En ayant des poids radicalement différents, il est plus facile pour les utilisateurs de savoir que ce n'est pas un bouton sans avoir à appuyer dessus.
* J'ai ajouté de l'espace entre chaque tweet pour qu'ils soient moins serrés. Cela aide les gens à identifier les conversations sur leurs fils d'actualité plus facilement, puisque les chaînes sont maintenant espacées du reste des Tweets.
* J'ai changé le cadre AVI d'un carré arrondi à un cercle.

![Image](https://cdn-media-1.freecodecamp.org/images/Gul3p5jAyISpM1nvj4oNxhCnJw9Q97r4Kj0Z)

### Conclusion

Twitter est l'une de mes applications préférées et je l'utilise quotidiennement, donc travailler sur ce projet a été amusant pour moi. Je savais aussi que ce serait un excellent moyen pour moi de perfectionner mes capacités de design, étant donné que Twitter est déjà une excellente application mobile.

J'ai construit un ? [prototype interactif ici](https://invis.io/SWA9B1RX2) ? en utilisant Sketch et Invision.

Si vous avez lu jusqu'ici, je vous apprécie ! J'espère avoir écrit quelque chose qui vous a été utile ou intéressant.

> "Le design ne se limite pas à l'apparence et à la sensation. Le design, c'est la façon dont cela fonctionne." — Steve Jobs

Merci d'avoir lu et bon design !
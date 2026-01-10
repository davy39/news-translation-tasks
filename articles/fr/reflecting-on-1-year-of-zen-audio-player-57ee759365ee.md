---
title: Réflexion sur 1 an de Zen Audio Player
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-25T17:49:40.000Z'
originalURL: https://freecodecamp.org/news/reflecting-on-1-year-of-zen-audio-player-57ee759365ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0Um-aajCPexvEbOI-sot8A.png
tags:
- name: Design
  slug: design
- name: music
  slug: music
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: UX
  slug: ux
seo_title: Réflexion sur 1 an de Zen Audio Player
seo_desc: 'By Shakeel Mohamed

  Today marks one year since I made the first commit to the Zen Audio Player (ZAP)
  project on GitHub! After reading Robby Russell’s post about Oh my Zsh, I’ve realized
  ZAP has a lot of potential going into year 2. Over the past year ...'
---

Par Shakeel Mohamed

Aujourd'hui marque un an depuis que j'ai fait le [premier commit](https://github.com/zen-audio-player/zen-audio-player.github.io/commit/262d8a23b59860c936fbb07731edf838cb587adf) pour le projet Zen Audio Player (ZAP) sur GitHub ! Après avoir lu [l'article de Robby Russell sur Oh my Zsh](https://medium.com/@robbyrussell/d-oh-my-zsh-af99ca54212c), j'ai réalisé que ZAP avait beaucoup de potentiel pour l'année 2. Au cours de l'année passée, le projet a évolué de manière que je n'aurais jamais imaginée. À ce jour, nous avons eu 20 contributeurs, et la plupart se sont joints au cours des 4 derniers mois !

![Image](https://cdn-media-1.freecodecamp.org/images/1*0Um-aajCPexvEbOI-sot8A.png)
_Un rendu actuel du site web, réalisé par [Yuri Brunetto](https://github.com/YuriBrunetto" rel="noopener" target="_blank" title=")._

### Une brève chronologie du développement

#### Naissance

L'année dernière, j'ai eu une idée très simple : masquer le lecteur vidéo des vidéos YouTube et simplement écouter l'audio. Je pensais que ce serait quelque chose de relativement facile à faire, et c'était le cas. J'ai assemblé une version fonctionnelle d'un site web en quelques soirées tout en procrastinant sur mon [projet de fin d'études](https://medium.com/@_shakeel/hacker-s-first-logo-designing-in-powerpoint-7eeeb6925097). Mon "innovation" consistait à régler la hauteur du lecteur YouTube suffisamment petite pour que seuls les contrôles soient visibles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UAYPDlzIEZN0BUAv0UTRSQ.png)
_C'était l'intégralité du site web : 1 titre, 1 zone de texte, 1 bouton._

La vie était belle pendant quelques mois. J'écoutais des [mixes de trance progressive](https://www.youtube.com/results?search_query=progressive+trance) au travail sans être gêné par les vignettes/slideshows borderline-NSFW sur la plupart de ces vidéos. Pendant mon temps libre, en soirée et le week-end, j'ai commencé à ajouter des fonctionnalités. Puis, un jour, YouTube a redessiné son lecteur vidéo.

#### API iFrame

Pour [contourner la nouvelle interface utilisateur défavorable de YouTube](https://github.com/zen-audio-player/zen-audio-player.github.io/issues/33) (qui masque automatiquement les contrôles du lecteur), une grande quantité de JavaScript était nécessaire pour manipuler l'API iFrame de YouTube de la manière souhaitée. Les changements que nous avons apportés pour travailler avec l'API iFrame de YouTube (au lieu des intégrations HTML directes) existent toujours dans ZAP aujourd'hui. Nous [travaillons actuellement](https://github.com/zen-audio-player/zen-audio-player.github.io/pull/153) à remplacer la plupart de ce code en utilisant [Plyr](https://plyr.io/). [Sam Potts](https://github.com/SamPotts) a été extrêmement utile en implémentant des fonctionnalités pour nous et nous espérons continuer à collaborer avec lui.

#### Contributeurs !

Un jour d'octobre, sans crier gare, ZAP a reçu sa première [pull request](https://github.com/zen-audio-player/zen-audio-player.github.io/pull/40) de la part de [Matt Stannett](https://github.com/BeigeBadger) ! Avant Matt, le dépôt était en fait sur mon compte GitHub personnel. Après un certain temps, j'ai transféré le dépôt vers l'[organisation GitHub ZAP](https://github.com/zen-audio-player). Travailler avec lui sur quelques changements m'a motivé à passer plus de temps sur ZAP. Son implication initiale m'a inspiré à publier le projet sur [Up For Grabs](http://up-for-grabs.net/), ce qui a conduit à beaucoup plus de contributions que prévu.

#### Nouvelles fonctionnalités

Il m'étonne encore que certaines fonctionnalités aient été implémentées uniquement par des contributeurs à ZAP. Certaines d'entre elles sont :

* Rendu de la description de la vidéo YouTube (avec des hyperliens appropriés)
* Recherche YouTube avec autocomplétion
* Affichage des résultats de recherche et lecture de l'audio de cette vidéo sans quitter le site web ZAP

### Outils

GitHub a été vraiment formidable pour promouvoir [des outils gratuits pour les projets open source](https://github.com/integrations). Les outils suivants ont été extrêmement utiles et continueront à bénéficier à ZAP à l'avenir :

* GitHub Pages — rien de mieux que l'hébergement gratuit pour notre site statique !
* [Gitter](https://gitter.im/zen-audio-player/zen-audio-player.github.io) — notre super salon de discussion intégré à nos autres services
* [Travis CI](https://github.com/zen-audio-player/zen-audio-player.github.io/) — quelqu'un doit bien exécuter les tests
* [Code Climate](https://codeclimate.com) — un excellent service d'analyse automatique de la qualité du code
* [TrackJS](https://trackjs.com/) — utile pour suivre et signaler les erreurs JavaScript des utilisateurs
* [Google Analytics](http://www.google.com/analytics/) / [Keen.IO](https://keen.io/) — pour savoir comment les utilisateurs utilisent le site

### Remerciements

Je suis profondément reconnaissant pour les contributeurs que nous avons eus jusqu'à présent, et j'ai hâte de collaborer avec d'autres à l'avenir. Je veux particulièrement remercier les personnes suivantes :

* [**Matt Stannett**](https://github.com/BeigeBadger) — le premier contributeur, sans lui j'aurais peut-être abandonné le projet il y a des mois !
* [**Ian Spence**](https://github.com/ecnepsnai) — il a acheté le nom de domaine ! [ZenPlayer.audio](https://zenplayer.audio/)
* [**Monica Cheung**](https://github.com/monicacheung) — elle a contribué le plus de code au projet jusqu'à présent, et a ajouté la meilleure fonctionnalité : la recherche YouTube !
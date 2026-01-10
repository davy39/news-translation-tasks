---
title: 'Projet Go Design Something de décembre : Minuteur Pomodoro'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-16T14:03:28.000Z'
originalURL: https://freecodecamp.org/news/december-go-design-something-project-pomodoro-timer-9617ac5d733b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*50luvvhhF28cOaFut3TS_g.png
tags:
- name: Design
  slug: design
- name: education
  slug: education
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: UX
  slug: ux
seo_title: 'Projet Go Design Something de décembre : Minuteur Pomodoro'
seo_desc: 'By K. Anthony

  The end of the year has been sneaking up on me. I realized that I’ve been seriously
  neglecting my Free Code Camp practice.

  Seeing as how I had some free time on my hands, in between taking a pretty good,
  in-depth beginner course on D3.j...'
---

Par K. Anthony

La fin de l'année m'a pris par surprise. Je me suis rendu compte que j'avais sérieusement négligé ma pratique sur [Free Code Camp](http://www.freecodecamp.com).

Comme j'avais un peu de temps libre, entre la prise d'un cours assez bon et approfondi pour débutants sur D3.js, j'ai décidé de m'attaquer à mon prochain projet front-end : le minuteur pomodoro.

### La Présentation

Le projet consistait à rétro-concevoir ce [pen de Geoff Stoerbeck](http://codepen.io/GeoffStorbeck/full/RPbGxZ/). Cela semble simple, n'est-ce pas ?

Faux !

J'ai tout de suite compris que ce projet serait plus complexe que les autres, ce qui explique probablement pourquoi j'ai traîné des pieds. Mais une fois que j'ai commencé, j'ai été super motivé pour résoudre les problèmes que mon idée présentait.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cFmJliPYAmitFNvU26x2zw.jpeg)
_Application Pomodoro par NASA Trained Monkeys_

### Mon Idée

Je me suis inspiré à la fois de la démonstration de Geoff et des applications pomodoro dans l'App Store iOS. [Particulièrement cette offre par NASA Trained Monkeys](https://itunes.apple.com/us/app/pomodoro-timer-focus-on-your/id703145045?mt=8).

La fonctionnalité essentielle était de permettre aux utilisateurs de définir à la fois le temps de session et le temps de pause, puis de démarrer le minuteur. Ils devraient également pouvoir mettre en pause le minuteur et le redémarrer.

Sur le plan esthétique, j'ai vraiment aimé l'idée de remplir le cercle au fur et à mesure que le temps passe dans le pen de référence, mais je voulais ajouter à cette idée en créant de petites barres de progression pour chaque session. J'ai également vraiment aimé l'idée de façonner la barre de progression comme une tomate.

Avec ces deux choses à l'esprit, j'ai décidé de commencer depuis le début et de simplement faire fonctionner quelque chose.

### Trouver des Plugins

Mon premier essai a été de trouver des frameworks qui me permettraient de faire ce que je voulais.

Naturellement, j'ai commencé par la fonctionnalité de base. J'avais besoin de quelque chose qui me permettrait de construire facilement un minuteur. Il n'y a pas de pénurie de plugins de minuteur pour jQuery, mais j'ai pu les parcourir assez facilement, évitant tout ce qui était pré-stylisé.

J'ai expérimenté avec [jQuery Simple Timer de Carlous Souza](http://csouza.me/jQuery-Simple-Timer/). Il avait beaucoup de fonctionnalités que je voulais mais n'avait pas la capacité intégrée de mettre en pause et de redémarrer les minuteurs. J'ai donc continué à chercher jusqu'à ce que je tombe sur [le Timer jQuery de Jason Chavannes](http://jchavannes.com/jquery-timer/demo), qui avait tout ce que je voulais, y compris de bonnes démonstrations et une documentation.

En utilisant le plugin de Jason, j'ai pu faire fonctionner un minuteur de base assez rapidement.

Ma structure imite la démonstration de Geoff, avec deux variables — une pour le temps de pause et une pour le temps de session — que vous pouvez modifier en utilisant les boutons plus et moins.

Une fois que vous avez fait vos sélections, vous cliquez sur le bouton de démarrage et le minuteur de session commence. Une fois que le minuteur de session est terminé, ce div se cache et le div de pause s'affiche et le minuteur de pause commence.

### Barres de Progression

Mon prochain projet était d'essayer d'ajouter des barres de progression. Comme je l'ai dit, je voulais à l'origine essayer d'en créer une en forme de tomate. J'espérais que mes nouvelles connaissances de débutant en SVG pourraient être utiles et je suis même allé jusqu'à créer une petite tomate SVG pratique. (Faites-moi confiance, elle est super mignonne.)

Mais j'ai abandonné cette idée après quelques jours en faveur de simplement faire fonctionner un cercle simple. J'ai dû réfléchir un peu pour réaliser que je voulais que cette image agisse comme une barre de progression. Mais une fois que j'ai eu cette idée, je suis parti à la recherche d'un autre plugin jQuery. Après avoir parcouru quelques options, j'ai trouvé que [le plugin jQuery Circle Progress de Rostyslav Bryzgunov correspondait parfaitement](https://github.com/kottenator).

Le plugin rend super facile la création d'une barre de progression autonome, mais j'avais besoin qu'elle fonctionne dans le cadre de mon application plus large. J'avais besoin de pouvoir la démarrer, la mettre en pause et la reprendre.

Encore une fois, c'est là que j'ai eu beaucoup de problèmes. La documentation du plugin mentionne un moyen d'arrêter l'animation et, à travers des jours d'expérimentation, je suis devenu de plus en plus familier avec les variables impliquées. J'ai pu créer une demi-solution en mettant à jour la propriété animationProgress de l'appel d'animation.

Cependant, j'ai constaté que cela ne fonctionnait que pour la première pause. Si vous repreniez le minuteur, le laissiez fonctionner, le mettiez en pause et essayiez de le reprendre à nouveau, animationProgress restait bloqué à l'ancienne valeur.

Après environ 3 jours, j'ai craqué et j'ai demandé sur StackOverflow. [Comme c'est souvent le cas, j'ai obtenu une réponse rapide qui a fait l'affaire](http://stackoverflow.com/questions/34271707/canvas-animation-progress).

Ainsi, après 89 versions, j'ai enfin pu ajouter la barre de progression à mon application.

### Le Problème

Il doit toujours y avoir un problème, n'est-ce pas ? J'ai découvert que bien que ma barre de progression continuait à avancer, que l'onglet de la fenêtre soit actif ou non. J'avais construit le minuteur de telle manière que le navigateur mettait en pause sa progression lorsque vous ne le regardiez pas. Pas amusant.

Je cherchais un moyen de le réparer lorsque je suis retourné au dépôt GitHub du minuteur et j'ai vu que d'autres personnes avaient soulevé ce problème et que l'auteur du code avait commencé à travailler sur une solution ! Cela signifierait utiliser une branche non canonique du code, mais j'étais partant.

J'ai refactorisé mon code pour utiliser la nouvelle version. J'ai dû réajouter certaines fonctionnalités qui avaient été supprimées, notamment la propriété isActive, et j'ai également dû comprendre comment mettre à jour le nouveau paramètre de compte à rebours. Mais au final, je l'ai fait fonctionner sans problème après environ 5 ou 6 heures de travail.

### Finalisation

J'ai ajouté quelques éléments esthétiques à la fin — principalement des polices et du style. J'ai également pu réajouter ma superbe tomate, bien que sous forme de PNG au lieu de SVG.

Une chose que j'ai découverte est que le code n'est pas tout à fait aussi DRY que je le souhaiterais. La manière dont les fonctions sont écrites, elles ne peuvent pas accéder aux variables globales, donc j'ai dû créer des variables plus d'une fois, dans des portées spécifiques. Cependant, je pense que le code est encore assez lisible. J'ai également pris le temps de commenter le code pour pointer les zones d'intérêt.

Ce projet a été le plus difficile jusqu'à présent, mais je suis fier du résultat.

Probablement la meilleure chose à propos de la méthode que Free Code Camp a choisie pour ces projets est qu'ils ne consistent pas simplement à suivre étape par étape un tutoriel. Vous avez un projet avec une fonctionnalité de référence, mais vous devez comprendre comment faire fonctionner les choses par vous-même.

À la fin, vous ressentez vraiment un sentiment d'accomplissement. De plus, vous avez réellement mis vos nouvelles connaissances en pratique. Vous obtenez également une pièce de portfolio sympa !

### Jetez un coup d'œil

Assez de mes divagations. [Jetez un coup d'œil à la version finale](http://codepen.io/anthkris/full/MaNZWQ/) et faites-moi savoir ce que vous en pensez !

![Image](https://cdn-media-1.freecodecamp.org/images/0*vV4Xl2zl2su-SKyv.png)

_Publié à l'origine sur [www.knanthony.com](http://www.knanthony.com/blog/december-gds-project-pomodoro-timer/) le 16 décembre 2015._
---
title: Trois graphiques controversés de l'état de JavaScript 2018
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T08:53:13.000Z'
originalURL: https://freecodecamp.org/news/three-controversial-charts-from-the-state-of-js-2018-ec9dda45749
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2LVJ87Dqia6wmg6ICFs7gw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Trois graphiques controversés de l'état de JavaScript 2018
seo_desc: 'By Sacha Greif

  You thought stats and graphs were boring? Think again…


  “Controversial” is literally the most overused word on the Internet, with the possible
  exception of “literally”. But this time it’s true: some of the charts in our 2018
  State of J...'
---

Par Sacha Greif

#### Vous pensiez que les stats et les graphiques étaient ennuyeux ? Détrompez-vous…

![Image](https://cdn-media-1.freecodecamp.org/images/1*2LVJ87Dqia6wmg6ICFs7gw.png)

« Controversé » est littéralement le mot le plus galvaudé sur Internet, avec l'exception possible de « littéralement ». Mais cette fois, c'est vrai : certains des graphiques de nos [résultats de l'enquête 2018 sur l'état de JavaScript](http://2018.stateofjs.com) ont généré beaucoup plus de débats que d'autres. Voyons pourquoi !

### L'écart de genre est réel

Je suis sûr que vous avez entendu parler de l'écart de genre dans le domaine de la technologie. Si vous m'aviez posé la question le mois dernier, j'aurais probablement dit quelque chose comme 80/20 % homme/femme. Et vous, quelle serait votre estimation ?

Faites défiler vers le bas pour voir la réponse !

…

Faites défiler vers le bas…

…

Continuez à faire défiler…

…

Un peu plus…

…

![Image](https://cdn-media-1.freecodecamp.org/images/1*oOK0MFT-1HBmwlWDrcSo6Q.png)

Imaginez ma surprise lorsque nos données ont révélé cette mer de points rouges et une répartition de 95/5 % à la place !

Ma première réaction a été de penser qu'il devait y avoir un problème avec notre méthodologie. Après tout, beaucoup de gens découvrent l'enquête via des plateformes comme Hacker News ou Reddit, qui pourraient elles-mêmes avoir des démographies biaisées.

Mais l'[enquête des développeurs de Stack Overflow](https://insights.stackoverflow.com/survey/2018/#developer-profile-gender) a confirmé que nos chiffres n'étaient pas si éloignés :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CLxrnjQUreep9qZs1y8ngw.png)

(Note : il n'a pas été facile de trouver d'autres enquêtes de développeurs pour voir si les nôtres et celles de Stack Overflow étaient des valeurs aberrantes ou non. Si vous en trouvez, faites-le-moi savoir !)

Comme vous pouvez l'imaginer, ce graphique a généré beaucoup de tweets déçus :

Alors, que peut-on faire ? Notre première réaction a été de trouver des moyens de toucher plus de femmes et de minorités, et c'est certainement une bonne première étape. Mais bien que rendre l'enquête elle-même plus inclusive soit nécessaire (et nous avons quelques idées à ce sujet, en commençant par [la traduire dans d'autres langues](https://github.com/StateOfJS/StateOfJS/issues/87)), il est également important de se rappeler qu'une enquête ne reflète que la réalité.

Nous ne voulons pas nous concentrer uniquement sur l'amélioration des chiffres, puis en rester là. L'objectif ultime devrait donc toujours être de rendre l'industrie dans son ensemble aussi accueillante que possible, afin que les futures enquêtes reflètent naturellement cet nouvel état de choses.

### Angular vs Angular

Depuis la grande scission d'Angular en [Angular](http://angular.io) (nouveauté) et [AngularJS](https://angularjs.org/) (ancienne version), parler du framework est devenu délicat.

Et cette année, je dois admettre que nous n'avons pas fait un travail particulièrement bon pour gérer la question.

Tout d'abord, voici comment la question sur Angular a été abordée au cours des 3 années de l'enquête :

* 2016 : posé des questions sur Angular et AngularJS, dans deux questions séparées
* 2017 : posé des questions sur Angular et AngularJS, dans deux questions séparées
* 2018 : posé une question uniquement sur Angular

Voici le graphique résultant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CBbB0aGxHTlduVJbSkmoVw.png)

Ce graphique montre **Angular** pour les trois années. Les données de 2016 et 2017 pour AngularJS ne sont tout simplement pas prises en compte dans le graphique.

Nous pensions que c'était la chose logique à faire : AngularJS est une technologie ancienne et obsolète, nous l'avons donc simplement retirée de l'enquête et avons continué.

Le problème, bien sûr, comme vous pouvez peut-être le deviner d'après le graphique, est que de nombreux répondants n'ont pas vu les choses de cette manière. Certains d'entre eux pensaient que notre question sur Angular concernait également AngularJS, ce qui explique la hausse soudaine des réponses « ne réutiliseraient pas » en 2018.

Cela n'a pas bien passé :

À notre défense, nous avons simplement traité Angular comme n'importe quel autre framework mentionné dans l'enquête, en utilisant son nom officiel (« Angular »). Peut-être aurions-nous dû prendre l'initiative de substituer quelque chose comme « Angular 2+ » à la place, même si ce n'est pas la nomenclature officielle ; ou au moins ajouter une note explicative spéciale pour expliquer la situation.

Dans tous les cas, je conviens que nous avons fait un mauvais travail pour expliquer tout le problème, et pour cela, nous nous excusons.

#### Biais d'échantillonnage

Nous avons également entendu des accusations de biais d'échantillonnage, provenant généralement soit de personnes en statistiques, soit de personnes qui se sont un peu renseignées sur Wikipedia.

Voici quelque chose d'intéressant à noter : les trois membres de l'équipe State of JS sont des utilisateurs de React, et non d'Angular. Il semble que cela nous rendrait plus susceptibles d'avoir accès à un public utilisant React, n'est-ce pas ?

Bien que ce soit certainement une possibilité, la plupart des répondants ont découvert l'enquête via des sources « neutres » comme Reddit ou Hacker News. De plus, à part le problème Angular déjà discuté, nos données semblent correspondre à celles d'autres enquêtes :

À moins que… l'équipe NPM utilise également React ? Oh la conspiration… !

Mais sérieusement, comme vous pouvez l'imaginer, nous faisons déjà tout notre possible pour diffuser l'enquête à un public plus large. Et nous pouvons seulement espérer qu'à mesure que le public de l'enquête grandit d'année en année, tout biais d'échantillonnage que nous pourrions introduire disparaîtra naturellement.

### Devez-vous vraiment éviter Ember.js ?

Notre dernière controverse concerne notre recommandation d'« éviter » certaines technologies.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZNfftX6TKNK7AEFiIYaO5A.png)

Eh bien, il est écrit « AVOID » en majuscules sur le graphique, je ne peux pas le nier.

En tant qu'utilisateur d'Ember, Polymer, ou toute autre technologie qui a le malheur de se retrouver dans ce quadrant « éviter », cela peut vous mettre en colère de manière compréhensible. Juste parce qu'une fraction de développeurs a peut-être eu une mauvaise expérience avec une bibliothèque il y a quelques années ne signifie pas que tout le monde devrait l'éviter !

Je peux certainement comprendre ce sentiment, puisque je suis dans le même bateau que vous. Je suis moi-même un utilisateur assidu de [Meteor](http://meteor.com) : j'ai écrit un livre à ce sujet, je construis même un [framework open-source entier](http://vulcanjs.org) dessus, pourtant j'ai dû accepter que Meteor tombe également dans le quadrant « éviter » :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fsq7YMXDMTD1KbP77o_Lew.png)

_Moi_, je pense que Meteor est génial, mais ce n'est pas seulement une question de ce que _je_ pense, ou de ce que _vous_ pensez. Il s'agit de ce que 20 000 développeurs pensent.

Et oui, passer de « la plupart des développeurs n'utiliseraient plus X » à « vous devriez éviter X » nécessite un saut. Nous pourrions simplement vous donner les données et vous laisser tirer vos propres conclusions.

Mais cela revient à la raison principale pour laquelle nous menons l'enquête en premier lieu : vous aider à prendre des décisions. Si vous connaissez et aimez déjà Ember, Meteor, ou toute autre technologie, alors tant mieux pour vous ! Nous n'avons aucune intention de critiquer votre choix.

Si, en revanche, vous venez chercher des conseils et des orientations, alors nous pensons que la meilleure façon de faire est d'être clair, et peut-être même un peu direct. Dire des choses comme « chaque bibliothèque a ses avantages et ses inconvénients, et vous devriez choisir la meilleure pour vos besoins » ne choquera peut-être personne, mais cela n'aide vraiment personne non plus.

### L'état (de certains aspects) de JavaScript

À la fin de la journée, il est important de se rappeler qu'une enquête ne peut aller que jusqu'à un certain point. Nous faisons de notre mieux pour être représentatifs de l'ensemble de l'écosystème JavaScript, mais 20 000 développeurs ne représentent toujours qu'une infime partie de la communauté.

Nous ne pensons pas que cela signifie qu'il ne vaut pas la peine d'essayer, cependant. Et avec votre aide, nous croyons que nous pouvons continuer à améliorer les choses année après année.

Alors, continuez à nous faire part de vos commentaires, qu'ils soient bons ou mauvais. Et bien sûr, à l'année prochaine !
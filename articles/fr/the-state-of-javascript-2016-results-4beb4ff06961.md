---
title: 'L''État de JavaScript 2016 : Résultats'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-03T14:24:20.000Z'
originalURL: https://freecodecamp.org/news/the-state-of-javascript-2016-results-4beb4ff06961
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BiVvD3saeQQ5EgEBvrm6xg.png
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Startups
  slug: startups
- name: Web Development
  slug: web-development
seo_title: 'L''État de JavaScript 2016 : Résultats'
seo_desc: 'By Sacha Greif

  The Wait Is Over

  I just looked through my inbox, and found a receipt for the awesome React for Beginners
  course dated November 4, 2015. So it’s been almost one full year since I ventured
  into the Wild West of modern JavaScript developm...'
---

Par Sacha Greif

#### L'Attente Est Terminée

Je viens de regarder dans ma boîte de réception et j'ai trouvé un reçu pour le cours génial [React pour Débutants](https://reactforbeginners.com/friend/STATEOFJS) daté du 4 novembre 2015. Cela fait donc presque un an que je me suis aventuré dans le Far West du développement JavaScript moderne.

Je suis maintenant assez confiant dans mes compétences React, mais il semble que dès que je maîtrise un défi, un autre apparaît : devrais-je utiliser [Redux](http://redux.js.org/) ? Ou peut-être me pencher sur [Vue](http://vuejs.org/) à la place ? Ou devenir complètement fonctionnel et sauter sur la vague [Elm](http://elm-lang.org/) ?

Je savais que je ne pouvais pas être le seul à avoir ces questions, alors j'ai décidé de lancer l'enquête [State of JavaScript](http://stateofjs.com) pour obtenir une image plus générale de l'écosystème. Il s'avère que j'ai touché un point sensible : en une semaine, j'avais accumulé **plus de 9000** réponses (sans jeu de mots avec le meme) !

Cela m'a pris un certain temps pour analyser les données, mais les résultats sont enfin en ligne !

#### [Consultez les résultats de l'enquête ici](http://stateofjs.com/)

Et si vous souhaitez en savoir un peu plus sur toute l'entreprise, continuez simplement votre lecture.

### Analyse des Données

Vous vous demandez peut-être pourquoi cela m'a pris tant de temps pour analyser et publier les données. Espérons que cela deviendra clair lorsque vous lirez le rapport.

Je ne voulais pas simplement publier un tas de graphiques sans contexte. Les statistiques brutes sont géniales si vous savez déjà ce que vous cherchez, mais si vous cherchez des conseils, elles peuvent tout aussi bien ajouter au bruit général.

Au lieu de cela, j'ai décidé d'utiliser ces statistiques comme base pour un rapport détaillé sur l'état actuel de JavaScript.

### Les Auteurs

J'avais initialement prévu d'écrire tout cela moi-même, mais j'ai rapidement réalisé que A) cela serait _beaucoup_ de travail et B) je ne voulais pas que le rapport soit trop biaisé par mes propres préconceptions.

J'ai donc demandé à quelques amis développeurs de participer et d'écrire les différentes sections du rapport. Non seulement le rapport global est beaucoup plus objectif – et intéressant – en conséquence, mais j'ai également pu obtenir des experts pour chaque sujet (je serai le premier à admettre qu'il y a des pans entiers du monde JavaScript que je connais peu).

Un énorme merci à tous les auteurs qui ont contribué au rapport : [Tom Coleman](https://twitter.com/tmeasday), [Michael Rambeau](http://michaelrambeau.com/), [Michael Shilman](https://medium.com/@shilman), [Arunoda Susiripala](https://twitter.com/arunoda), [Jennifer Wong](http://mochimachine.org/), et [Josh Owens](http://joshowens.me/).

![Image](https://cdn-media-1.freecodecamp.org/images/49Uk22SyawwAbzFqgUs26BiLSJlx-qhwznMo)

### Les Graphiques

Voici un peu plus d'informations sur les principaux types de graphiques que vous verrez tout au long de l'enquête.

#### Graphique à Barres Empilées

![Image](https://cdn-media-1.freecodecamp.org/images/yN22NPK31J0d8BCyMYP4NntgMat2HzcvuUvl)

Il s'agit du graphique principal pour chaque section. Pour chaque technologie, il montre la répartition des développeurs qui **n'en ont jamais entendu parler**, en ont entendu parler mais **ne sont pas intéressés**/**veulent l'apprendre**, et l'ont utilisée et **ne l'utiliseraient pas**/**l'utiliseraient à nouveau**.

Vous pouvez basculer entre les pourcentages et les nombres absolus ainsi que filtrer par intérêt ou satisfaction. Mais notez que lors du filtrage, les pourcentages sont relatifs à la paire de valeurs actuellement sélectionnée (en d'autres termes, les deux nombres totalisent 100%).

#### Carte Thermique

Je voulais également explorer les corrélations _entre_ chaque technologie.

![Image](https://cdn-media-1.freecodecamp.org/images/mRUJJ8RAVe9k37oXsmRnmha9U0-IzRh0JZp8)

Les cartes thermiques réalisent cela en vous montrant à quel point quelqu'un qui utilise une technologie (définie comme ayant sélectionné « J'ai utilisé X et je l'utiliserais à nouveau ») est susceptible d'utiliser une autre technologie, par rapport à la moyenne.

Le rose signifie très probable, le bleu signifie très improbable. En d'autres termes, une case rose foncé dans la ligne React et la colonne Redux signifie « Les utilisateurs de React sont beaucoup plus susceptibles que la moyenne d'utiliser également Redux ».

### Construit Avec

J'ai décidé de pratiquer ce que je prêchais et de construire l'application de l'enquête elle-même en utilisant des outils JavaScript modernes, notamment React alimenté par l'excellent générateur de site statique [Gatsby](https://github.com/gatsbyjs/gatsby).

Il peut sembler étrange au premier abord d'utiliser React pour ce qui est essentiellement une page HTML statique, mais il s'avère que cela apporte un tas d'avantages : par exemple, vous êtes en mesure d'utiliser l'écosystème vaste de modules de React tel que la grande bibliothèque [Recharts](http://recharts.org).

En fait, je crois que cela pourrait bien s'avérer être une nouvelle approche, _meilleure_, pour développer des sites statiques, et j'espère écrire un article plus détaillé à ce sujet bientôt.

### Partenaires

Enfin, je n'aurais pas pu prendre un mois de congé pour travailler sur ce projet sans le soutien financier de certaines personnes vraiment géniales.

Wes Bos (qui a sorti le susmentionné [React pour Débutants](https://reactforbeginners.com/friend/STATEOFJS) ainsi que le nouveau [ES6 pour Tout le Monde](https://es6.io/friend/stateofjs)) et [egghead.io](http://egghead.io) (qui, à mon avis, est la meilleure ressource disponible pour apprendre le développement JavaScript de pointe) ont accepté de sponsoriser le projet. Merci les gars !

### Soutenez le Projet

Si vous pensez que ce que j'ai fait ici est précieux et que vous souhaitez soutenir le projet, un tweet ou un partage serait grandement apprécié !

* [Tweet](https://twitter.com/intent/tweet/?text=The%20State%20Of%20JavaScript%3A%20discover%20the%20most%20popular%20JavaScript%20technologies%20http%3A%2F%2Fstateofjs.com%20%23stateofjs)
* [Partager sur Facebook](https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fstateofjs.com)

De plus, vous pouvez également contribuer par un don pour [accéder aux données brutes anonymisées](https://gumroad.com/l/hLWTB) (ou entrez simplement « 0 » pour les obtenir gratuitement).

### Qu'est-ce qui suit

Maintenant que l'enquête est terminée et que nous savons tous quelles sont les meilleures technologies, espérons que nous pourrons mettre fin à toute discussion sur la « fatigue JavaScript » ou le « changement incessant » et continuer avec nos vies de programmeurs.

Haha, comme si !

Si une chose est devenue claire pour moi, c'est que les douleurs de croissance que JavaScript traverse en ce moment ne sont que le début. Alors que React vient à peine d'émerger comme le vainqueur des Guerres Front-End de 2015, certains développeurs dénoncent déjà React pour ne pas être assez fonctionnel, et embrassent Elm ou ClojureScript à la place.

En d'autres termes, mon travail ici n'est pas terminé, et j'ai bien l'intention de refaire cette enquête l'année prochaine ! Si vous souhaitez être informé lorsque cela se produira, je vous encourage à [me laisser votre email ici](http://eepurl.com/ccyxCn).

En attendant, je ne peux qu'espérer que ces résultats d'enquête apporteront un peu de clarté dans notre quête sans fin pour donner un sens à l'écosystème JavaScript !
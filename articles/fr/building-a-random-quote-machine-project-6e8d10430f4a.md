---
title: Création d'une Machine à Citations Aléatoires
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-18T22:42:03.000Z'
originalURL: https://freecodecamp.org/news/building-a-random-quote-machine-project-6e8d10430f4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KB1NWVn6GX5hV0eq2W1mFg.jpeg
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Création d'une Machine à Citations Aléatoires
seo_desc: 'By Ayo Isaiah

  I really wasn’t entirely satisfied with my first attempt at building a Random Quote
  Generator on Free Code Camp. It was ugly, and the quotes were too long, so I didn’t
  bother to implement the “tweet” functionality. It just didn’t make a...'
---

Par Ayo Isaiah

Je n'étais vraiment pas entièrement satisfait de ma [première tentative](http://codepen.io/ayoisaiah/full/zrqWje) de construire un Générateur de Citations Aléatoires sur Free Code Camp. C'était laid, et les citations étaient trop longues, donc je ne me suis pas donné la peine d'implémenter la fonctionnalité "tweet". Cela n'avait tout simplement aucun sens de le faire.

Donc, après avoir terminé le [Projet d'Horloge Pomodoro](http://codepen.io/ayoisaiah/full/wMZYvg/), j'ai ressenti un fort désir de revisiter ma Machine à Citations Aléatoires et de recommencer avec une approche différente.

Je voulais un design plus intéressant, avec quelques animations. J'avais aussi cette idée de mettre les citations dans différentes catégories, afin que les utilisateurs puissent voir les citations de leurs catégories préférées.

Mes examens étaient terminés, donc j'avais assez de temps pour le terminer.

#### Logique

J'ai opté pour huit catégories de citations et j'ai recueilli 25 citations pour chacune. Chaque catégorie était un tableau d'objets avec des propriétés de citation et d'auteur, afin que je puisse récupérer chacune facilement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8cQIMMY0gOxMokSnISuR8A.jpeg)

Ensuite, j'ai créé une fonction pour mettre les citations dans le HTML une fois que le bouton de citation suivante est cliqué et une fonction similaire pour le bouton "citation précédente".

![Image](https://cdn-media-1.freecodecamp.org/images/1*tQ62LIlMUibMUXSE_C0m7w.jpeg)

Si vous regardez le code, vous verrez que les citations ne sont pas générées aléatoirement du tout, mais qu'elles itèrent de la première à la dernière et vice versa. C'est un choix de design intentionnel que j'ai fait.

#### Design

Ce qui m'a le plus ennuyé dans cette première tentative, ce n'était même pas vraiment la façon dont cela fonctionnait, mais la façon dont cela ressemblait. Donc le design était ce sur quoi je me suis concentré pour la plupart dans ce projet.

La première chose que j'ai faite a été de lister toutes les choses que je voulais que mon application fasse et comment je voulais qu'elle ressemble. J'ai appris au fil du temps que la meilleure façon d'aborder quoi que ce soit est de le décomposer en étapes simples et actionnables, c'est donc ce que j'ai fait ici en utilisant [Workflowy](https://workflowy.com/invite/2dbe7482.lnx).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z-5Ke6mfVipplnSRmvQWYg.jpeg)

J'ai toujours utilisé le [Skeleton CSS boilerplate](http://getskeleton.com/) chaque fois que je veux faire une mise en page basée sur une grille, donc j'ai continué avec celui-ci pour celui-ci également.

Cette fois-ci, cependant, j'ai utilisé la [version Sass](https://github.com/WhatsNewSaes/Skeleton-Sass) qui a rendu facile le changement de quelques variables et la personnalisation sans toucher aux fichiers originaux.

Une fois cela en place, j'ai commencé à travailler sur la conception de la page d'accueil. Dans mon esprit, je voulais une grille 2x4 avec des cartes pour chaque section et un titre en haut. C'était assez facile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*q76RfxU-6m8kfd8k5ouT9g.png)

Bam ! J'avais ma grille en place. La prochaine chose était de déterminer comment j'allais styliser la page des citations et utiliser des animations pour basculer entre les deux pages.

La page des citations m'a pris un peu plus de temps à terminer. J'avais une barre de navigation en haut pour basculer entre les sections et une boîte au milieu où les citations seraient affichées. Les boutons pour afficher les citations étaient en bas.

Une idée qui m'est venue à l'esprit à ce moment-là était de changer l'image de fond lorsque l'utilisateur se déplace entre les sections. L'image de fond devait correspondre à l'image en vedette dans les cartes de la page d'accueil.

Je voulais aussi que le changement soit fluide avec des animations subtiles, donc j'ai utilisé la propriété de transition CSS à cette fin et cela a bien fonctionné sur Chrome, mais je n'ai pas réussi à le faire fonctionner sur Firefox (si quelqu'un sait comment corriger cela, faites-le moi savoir).

![Image](https://cdn-media-1.freecodecamp.org/images/1*yiOtjvldTXXwVa2A18YxKg.png)

Une fois que j'ai eu les deux mises en page triées, il était temps de lier les deux pages avec une animation. Ma première pensée était d'utiliser des animations CSS, mais je n'ai pas abouti, donc j'ai cherché des animations jQuery à la place. Après quelques expérimentations, j'ai trouvé ce que je voulais. Les fonctions slideUp() et slideDown() étaient parfaites pour ce dont j'avais besoin.

En gros, une fois que vous cliquez sur l'une des sections de la page d'accueil, la page des citations glissera en vue et vous pourrez voir les citations des différentes sections. De même, lorsque vous cliquez sur le bouton d'accueil de la barre de navigation, la page glisse vers le bas pour révéler la page d'accueil.

Donc, c'était ça.

Tout ce que j'ai fait à partir de ce moment-là a été de remplacer les images de remplissage par des images réelles et d'utiliser quelques polices Google pour égayer les choses. Enfin, j'ai fait le bouton tweet.

Vous pouvez voir la [version finale](http://codepen.io/ayoisaiah/full/RaGpoM) sur CodePen.

#### Leçons Apprises

Au cours de ce projet, j'ai appris quelques leçons précieuses :

* Dans certains cas, l'utilisation d'images de fond peut vous donner plus de contrôle et plus de flexibilité avec des images de différentes hauteurs car vous pouvez définir background-size: cover et cela ne déborderait pas du conteneur. De plus, vous pouvez créer des effets de survol sympas comme je l'ai fait avec les images en vedette sur la page d'accueil. Je ne savais pas toujours cela, mais quelqu'un du [groupe Slack CodeNewbie](https://codenewbie.typeform.com/to/uwsWlZ) me l'a fait remarquer.
* J'ai également appris à décomposer mes fichiers Sass en partials et à les importer dans la feuille de style principale. Cela aide à l'organisation et facilite la correction des choses. J'ai une architecture de travail que j'utilise et elle n'est pas parfaite, mais je l'améliorerai avec le temps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*10S5FwEhfRZ7DeE-z1l-IQ.png)

J'adorerais entendre vos réflexions sur mon approche et les choses que je pourrais améliorer, donc un commentaire ou deux seraient grandement appréciés.

#### Prochainement

Je travaillerai sur le projet "[Afficher la Météo Locale](https://www.freecodecamp.com/challenges/show-the-local-weather)" ce week-end et j'espère l'avoir terminé d'ici dimanche. Ce sera ma première vraie expérience avec l'utilisation d'une API et j'espère que je la comprendrai assez rapidement.

J'écrirai un article similaire sur ce projet la semaine prochaine, alors surveillez celui-ci.

Si vous voulez me contacter ou me connecter, vous pouvez me trouver sur [Twitter](https://twitter.com/ayisaiah) ou [m'envoyer un email](mailto:ayisaiah@gmail.com).

Une version de cet article a été publiée sur mon [blog personnel](http://ayoisaiah.github.io/random-quote-generator/)
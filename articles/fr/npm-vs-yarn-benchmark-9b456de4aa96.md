---
title: J'ai comparé Yarn avec les 4 outils CI les plus populaires.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-17T08:18:06.000Z'
originalURL: https://freecodecamp.org/news/npm-vs-yarn-benchmark-9b456de4aa96
coverImage: https://cdn-media-1.freecodecamp.org/images/0*e6JtRXnqMpMRnpAu.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: J'ai comparé Yarn avec les 4 outils CI les plus populaires.
seo_desc: 'By Alberto Varela

  Yarn is a recently launched alternative for npm as Node.js dependency manager. It
  claims to be much faster and reliable than its predecessor. Let see if it’s true.

  If you’re a Javascript developer — and especially if you work with N...'
---

Par Alberto Varela

Yarn est une alternative récemment lancée pour npm en tant que gestionnaire de dépendances Node.js. Il prétend être beaucoup plus rapide et fiable que son prédécesseur. Voyons si c'est vrai.

Si vous êtes un développeur Javascript — et surtout si vous travaillez avec Node.js — vous avez probablement entendu parler de [Yarn](https://yarnpkg.com/) ces derniers jours. Des ingénieurs de Facebook Exponent, Google et Tilde [ont travaillé ensemble](https://code.facebook.com/posts/1840075619545360) [pour construire](http://yehudakatz.com/2016/10/11/im-excited-to-work-on-yarn-the-new-js-package-manager-2/) cette alternative au bien connu [npm](https://www.npmjs.com/), le gestionnaire de paquets intégré de Node.js.

Au cours des dernières années, les développeurs du monde entier ont commencé à se plaindre de la lenteur de npm. L'autre chose qu'ils veulent est un système de dépendances capable d'éviter les incohérences entre les environnements. Ainsi, Yarn se présente comme exactement ce que nous avons toujours voulu : « Fast, Reliable, and Secure Dependency Management » (Gestion des dépendances rapide, fiable et sécurisée).

Il est clair que l'introduction du fichier [yarn.lock](https://yarnpkg.com/en/docs/yarn-lock) et la vérification de la somme de contrôle ajoutent de la cohérence et de l'intégrité à nos paquets entre les environnements, mais... qu'en est-il de la vitesse ? Yarn [prétend qu'il est ultra rapide](https://yarnpkg.com/en/compare). J'ai donc décidé de le comparer à npm dans une variété d'environnements.

### La Méthode

L'outil que j'ai utilisé pour mesurer la vitesse des deux gestionnaires de paquets est la commande Linux `time`. J'ai écrit un petit script Bash — basé sur [ce gist](https://gist.github.com/peterjmit/3864743) créé par Peter Mitchell.

Le script exécute plusieurs installations pour [Angular](https://angular.io/), [Ember](http://emberjs.com/), et [React](https://facebook.github.io/react/) en utilisant à la fois npm et Yarn. Il mesure le temps que prend chaque installation. Ensuite, à la fin, il affiche les métriques moyennes, triées par gestionnaire de paquets et framework. Il effectuera également des installations avec des paquets précachés et avec un cache vide pour voir la différence entre les deux situations.

Vous pouvez voir le script utilisé ici : [https://github.com/artberri/npm-yarn-benchmark](https://github.com/artberri/npm-yarn-benchmark)

### L'Environnement

Une fois que j'avais choisi l'outil de benchmarking, il était temps d'exécuter le script.

J'ai commencé par l'exécuter sur mon propre ordinateur. Ensuite, afin d'obtenir des métriques plus standardisées, j'ai relancé le script en utilisant les outils de Continuous Integration (CI) suivants : Travis, Snap CI, Semaphore et Circle CI.

En raison de la grande quantité d'installations effectuées lors de chaque test, le script a pris un certain temps à se terminer. Afin d'éviter les timeouts dans ces outils CI, j'ai calculé les moyennes de temps sur trois exécutions.

### Les Résultats

Sur mon propre ordinateur :

```
---------------------------------------------------------------------------------------------- RÉSULTATS (secondes) -------------------------------------------------------------------------------------------|                       |     angular2 |        ember |        react |  npm_with_empty_cache |       15.687 |       56.993 |       93.650 |   npm_with_all_cached |        9.380 |       52.380 |       81.213 | yarn_with_empty_cache |        9.477 |       30.757 |       37.497 |  yarn_with_all_cached |        4.650 |       15.090 |       17.730 --------------------------------------------------------------------
```

Dans [Travis](https://travis-ci.org/artberri/npm-yarn-benchmark) :

```
------------------------------------------------------------------------------------------- RÉSULTATS (secondes) ----------------------------------------------------------------------------------------------|                      |     angular2 |        ember |        react | npm_with_empty_cache |       19.720 |       55.090 |       76.233 |  npm_with_all_cached |       14.640 |       40.203 |       56.467 |yarn_with_empty_cache |       13.193 |       34.037 |       43.663 | yarn_with_all_cached |        5.830 |       15.923 |       40.420 --------------------------------------------------------------------
```

Dans [Snap CI](https://snap-ci.com/artberri/npm-yarn-benchmark/) :

```
--------------------------------------------------------------------------------------------- RÉSULTATS (secondes) --------------------------------------------------------------------------------------------|                      |     angular2 |        ember |        react | npm_with_empty_cache |       20.640 |       57.030 |      120.470 |  npm_with_all_cached |       15.753 |       45.273 |       62.597 |yarn_with_empty_cache |       12.227 |       41.997 |       51.863 | yarn_with_all_cached |        7.693 |       23.607 |       24.490 --------------------------------------------------------------------
```

Dans [Semaphore](https://semaphoreci.com/artberri/npm-yarn-benchmark/) :

```
------------------------------------------------------------------------------------------- RÉSULTATS (secondes) ----------------------------------------------------------------------------------------------|                      |     angular2 |        ember |        react | npm_with_empty_cache |       11.057 |       35.287 |       54.203 |  npm_with_all_cached |        7.107 |       24.797 |       31.300 |yarn_with_empty_cache |        6.273 |       17.407 |       22.777 | yarn_with_all_cached |        2.790 |        8.150 |        9.380 --------------------------------------------------------------------
```

Dans [CircleCI](https://circleci.com/gh/artberri/npm-yarn-benchmark) :

```
------------------------------------------------------------------------------------------- RÉSULTATS (secondes) ----------------------------------------------------------------------------------------------|                      |     angular2 |        ember |        react | npm_with_empty_cache |       42.940 |      100.287 |      163.550 |  npm_with_all_cached |       16.990 |       50.083 |       67.000 |yarn_with_empty_cache |       15.907 |       45.547 |       58.113 | yarn_with_all_cached |        7.547 |       26.763 |       27.130 --------------------------------------------------------------------
```

### La Conclusion

Yarn est ultra rapide, entre 2 et 3 fois plus rapide que npm.

Les créateurs de Yarn disent la vérité. C'est génial de voir que Yarn est plus rapide, même lorsque nous comparons le test npm en cache avec un test Yarn non mis en cache.

Sur cette base, je dirais que Yarn est prêt à devenir le gestionnaire de dépendances standard pour Node.js dans les mois à venir.

En passant, le but de cette comparaison n'était pas de benchmarker les outils CI, mais il est intéressant de noter que Semaphore a performé favorablement par rapport aux autres outils que j'ai utilisés dans cet exemple.

J'utilise Yarn depuis le premier jour, et c'est quelque chose que je voulais depuis longtemps.

Je utilise actuellement [Puppet](https://puppet.com/) pour le provisionnement de logiciels dans la plupart de mes projets. Pour cette raison, j'ai créé un module Puppet pour installer Yarn que vous pouvez [essayer ici](https://forge.puppetlabs.com/artberri/yarn).

Merci pour la lecture, et bonne installation !

_Publié à l'origine sur [www.berriart.com](https://www.berriart.com/blog/2016/10/npm-yarn-benchmark/)._
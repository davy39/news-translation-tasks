---
title: Google Chrome a peut-être cassé vos tests sans même que vous le sachiez
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-11T15:05:04.000Z'
originalURL: https://freecodecamp.org/news/google-chrome-might-have-broken-your-tests-without-you-even-knowing-about-it-9d9130a6fd0c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jnZ0lrbFnVqzqCCph67VmA.jpeg
tags:
- name: Google
  slug: google
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Google Chrome a peut-être cassé vos tests sans même que vous le sachiez
seo_desc: 'By Robert Axelsen

  My colleague just discovered that Chrome 58 (released April 19th) has silently muted
  all console.debug() output in their Chrome Dev Tools.

  How? By making changes to the Console UI, from filtering based on type of console
  method to f...'
---

Par Robert Axelsen

Mon collègue vient de découvrir que Chrome 58 (sorti le 19 avril) a silencieusement masqué toute la sortie de `console.debug()` dans leurs outils de développement Chrome.

Comment ? En apportant des modifications à l'**Interface de la Console**, passant du filtrage basé sur le type de méthode de console au filtrage basé sur les niveaux.

Introduire des niveaux n'est pas une mauvaise chose en soi. Mais Google a également choisi de ne plus afficher toute la sortie de la console par défaut. Maintenant, vous ne pouvez voir que le niveau « Info » et en dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/dPUyS-Ev5EwsCRbFz7oXOp0mC6Kg29ab5XUE)

Selon votre projet, il peut également être important de ne plus pouvoir filtrer en affichant uniquement la sortie d'une seule méthode de console.

Par exemple, uniquement `console.log()`. Cela est particulièrement problématique si vous travaillez sur un projet plus grand avec des centaines de types de sortie différents mélangés ensemble.

Comme vous pouvez le voir dans la section des commentaires [dans les notes de mise à jour](https://developers.google.com/web/updates/2017/03/devtools-release-notes), cela n'a pas été bien reçu par les développeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/ToWIG1qympOpdTfuQdkye9VDC5hYgFdR4Dxr)

### Tests en échec

Cela signifie que si votre application ou projet dépend de la sortie de niveau `console.debug()` pour les tests, vos tests ont peut-être échoué depuis plus d'un mois sans même que vous le remarquiez.

Tout cela sans même un avertissement pop-up de Google.

En rendant la journalisation non verbeuse par défaut, je crois que Google a rompu avec les meilleures pratiques ici et a fait une énorme erreur.

De plus, supprimer la possibilité de n'afficher la sortie que sur la base d'une méthode de console spécifique a entraîné une dégradation du flux de travail pour de nombreux développeurs.

### Testez par vous-même

J'ai fait quelques tests avec les méthodes de console suivantes dans les outils de développement Chrome :

```
console.assert(true, {assert: "assert"});console.count('count');console.debug('debug');console.dir({dir: "dir"});console.error('error');console.info('info');console.log('log');console.profile('profile');setTimeout(function(){ console.profileEnd('profile'); }, 1000);console.table('table');console.time('time');setTimeout(function(){ console.timeEnd('time'); }, 1000);console.timeStamp('timeStamp');console.trace('trace');console.warn('warn');
```

Vous pouvez simplement copier-coller ceci dans la console des outils de développement Chrome, appuyer sur Entrée et changer le niveau de filtre pour voir ce qui est affiché dans chaque niveau.

### Quelques captures d'écran pour illustrer

Voici quelques captures d'écran pour illustrer les différences entre les niveaux. Remarquez surtout la première capture d'écran du niveau « Info » par défaut, et le fait que « 3 éléments sont masqués ».

![Image](https://cdn-media-1.freecodecamp.org/images/SSCiXIg2XpzHEnm7CoeSI2V5nWLgVwNJVpAL)
_Chrome 58, sortie de la console des outils de développement Chrome, niveau « Info »._

![Image](https://cdn-media-1.freecodecamp.org/images/Sa15guFLU1CXTtg-aOwtREyQcKF3elpbWf5K)
_Chrome 58, sortie de la console des outils de développement Chrome, niveau « Verbeux »._

![Image](https://cdn-media-1.freecodecamp.org/images/K4dbNwnmgLbuUDWfmO2B5fcvan4ISkriJ0fj)
_Chrome 58, sortie de la console des outils de développement Chrome, niveau « Avertissements »._

![Image](https://cdn-media-1.freecodecamp.org/images/99FBC3jV7bmYGw0hjIZeP612-vPS3iQv9XXa)
_Chrome 58, sortie de la console des outils de développement Chrome, niveau « Erreurs »._

### Avez-vous des pensées ?

Que pensez-vous de ce changement ? Google avait-il tort de faire ce changement ? Ou pensez-vous que c'était une amélioration de l'« Interface de la Console » dans l'ensemble ? Veuillez laisser un commentaire ci-dessous.

_Cet article a été initialement publié sur [« Hello, I Love Code »](http://helloilovecode.com/) et est écrit par [Robert Axelsen](http://rob.ee/), qui est un développeur JavaScript, organisateur de Meetup et passionné d'Open Source basé en Autriche, en Europe._

_Vous pouvez vous connecter avec Robert sur [Twitter](https://twitter.com/Robert_Axelsen), ou mieux le connaître en [visitant son site web.](http://rob.ee/)
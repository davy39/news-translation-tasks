---
title: 'npm cache : le héros méconnu'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-22T21:41:06.000Z'
originalURL: https://freecodecamp.org/news/npm-cache-the-unsung-hero-11e646c09791
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UmRnW6YyI9ygq81OaL8Y-Q.png
tags:
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: 'npm cache : le héros méconnu'
seo_desc: 'By Siddharth Kshetrapal

  I love npm and believe that this package manager is the single biggest reason for
  JavaScript’s massive success these past few years.

  There was a lot of excitement in the JavaScript community when facebook released
  yarn. And fo...'
---

Par Siddharth Kshetrapal

J'adore npm et je pense que ce gestionnaire de paquets est la raison principale du succès massif de JavaScript ces dernières années.

Il y avait beaucoup d'excitation dans la communauté JavaScript lorsque Facebook a publié Yarn. Et pour de bonnes raisons. Les vitesses d'installation de Yarn sont incroyables. Les installations ultérieures sont encore plus rapides car Yarn met en cache les modules installés sur votre machine.

![Image](https://cdn-media-1.freecodecamp.org/images/yAAqrLfduWDgBuRqnlh1xqu7qRiTzMXUjr7f)
_Vitesses d'installation @ 12 Mbps. Yarn = ?_

Mais il y a une fonctionnalité de npm qui ne reçoit pas près de l'attention qu'elle mérite.

Comme Yarn, npm dispose également d'un mécanisme de mise en cache intégré qui peut rendre les installations ultérieures super rapides.

Voici quelques benchmarks :

![Image](https://cdn-media-1.freecodecamp.org/images/oXzMHJNK8dsZwCEAxu2u47WZQwTWOE6MAL08)
_npm + cache est aussi rapide que yarn + cache (si ce n'est plus rapide)_

C'est fou, non ? Et devinez quoi : cette fonctionnalité a toujours été disponible pour vous, mais elle est désactivée par défaut.

### Comment activer le cache npm

```
npm config set cache-min 9999999
```

C'est tout.

Installez maintenant vos paquets comme d'habitude :

```
npm install express
```

Vous pouvez essayer ces benchmarks vous-même en utilisant [ce dépôt](https://github.com/siddharthkp/npm-cache-benchmark) :

[**siddharthkp/npm-cache-benchmark**](https://github.com/siddharthkp/npm-cache-benchmark)
[_npm-cache-benchmark - Benchmark npm cache vs yarn_github.com](https://github.com/siddharthkp/npm-cache-benchmark)

Notez que Yarn ne se limite pas à la vitesse — il possède [d'autres fonctionnalités](https://yarnpkg.com/blog/2016/10/11/introducing-yarn) comme des installations cohérentes, qui le distinguent.

Mais, si la vitesse est une considération importante pour vous — comme c'est le cas pour moi — vous devriez donner une autre chance à npm, cette fois avec le cache.

Merci à [ashley williams](https://www.freecodecamp.org/news/npm-cache-the-unsung-hero-11e646c09791/undefined) pour avoir révisé cet article et à [npm](https://www.freecodecamp.org/news/npm-cache-the-unsung-hero-11e646c09791/undefined) pour être génial.

P.S. Vous devriez absolument [me suivre sur twitter](https://twitter.com/siddharthkp).
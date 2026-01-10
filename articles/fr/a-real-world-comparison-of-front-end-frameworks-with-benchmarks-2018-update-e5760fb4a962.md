---
title: Une comparaison réelle des frameworks front-end avec des benchmarks (mise à
  jour 2018)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-31T05:59:39.000Z'
originalURL: https://freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0aM-p4OCCxRMXroYn0qPVA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une comparaison réelle des frameworks front-end avec des benchmarks (mise
  à jour 2018)
seo_desc: 'By Jacek Schae

  This article is a refresh of A Real-World Comparison of Front-End Frameworks with
  Benchmarks from December 2017.

  In this comparison, we will show how different implementations of almost identical
  RealWorld example apps stack up against...'
---

Par Jacek Schae

Cet article est une mise à jour de [A Real-World Comparison of Front-End Frameworks with Benchmarks](https://medium.freecodecamp.org/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-e1cb62fd526c) de décembre 2017.

Dans cette comparaison, nous allons montrer comment différentes implémentations d'applications exemple presque identiques [RealWorld](https://github.com/gothinkster/realworld) se comparent les unes aux autres.

L'application exemple [RealWorld](https://github.com/gothinkster/realworld) nous offre :

1. **Application Réelle** — Quelque chose de plus qu'un simple "todo". Habituellement, les "todos" ne transmettent pas assez de connaissances et de perspective pour construire des applications _réelles_.
2. **Standardisée** — Un projet qui respecte certaines règles. Fournit une API back-end, un balisage statique, des styles et une spécification.
3. **Écrit ou révisé par un expert** — Un projet réel et cohérent, idéalement construit ou révisé par un expert de cette technologie.

#### Critiques de la dernière version (décembre 2017)

✅ Angular n'était pas en production. L'application de démonstration listée dans le dépôt RealWorld utilisait une version de développement, mais grâce à [Jonathan Faircloth](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962/undefined), elle est maintenant en version de production !

✅ Vue n'était pas listé dans le dépôt RealWorld, et donc n'était pas inclus. Comme vous pouvez l'imaginer, dans le monde du front-end, cela a suscité beaucoup de réactions. Comment avez-vous pu ne pas ajouter Vue ? Qu'est-ce qui ne tourne pas rond chez vous ? Cette fois-ci, Vue.js est inclus ! Merci à [Emmanuel Vilsbol](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962/undefined).

#### Quelles bibliothèques/frameworks comparons-nous ?

Comme dans l'article de décembre 2017, nous avons inclus toutes les implémentations listées dans le dépôt RealWorld. Peu importe qu'elles aient une grande communauté ou non. La seule qualification est qu'elles apparaissent sur la page du [dépôt RealWorld](https://github.com/gothinkster/realworld).

![Image](https://cdn-media-1.freecodecamp.org/images/fe6a0GVWKWXwg0Q4XKm4JoFTKWvvAJEGFUFW)
_Frontends sur [https://github.com/gothinkster/realworld](https://github.com/gothinkster/realworld" rel="noopener" target="_blank" title=") (avril 2018)_

### Quelles métriques examinons-nous ?

1. **Performance** : Combien de temps cette application met-elle à afficher du contenu et à devenir utilisable ?
2. **Taille** : Quelle est la taille de l'application ? Nous ne comparerons que la taille du ou des fichiers JavaScript compilés. Le CSS est commun à toutes les variantes et est téléchargé depuis un CDN (Content Delivery Network). Le HTML est également commun à toutes les variantes. Toutes les technologies compilent ou transpilent en JavaScript, nous ne mesurons donc que la taille de ce ou ces fichiers.
3. **Lignes de code** : Combien de lignes de code l'auteur a-t-il dû écrire pour créer l'application RealWorld basée sur la spécification ? Pour être équitable, certaines applications ont un peu plus de fonctionnalités, mais cela ne devrait pas avoir un impact significatif. Le seul dossier que nous quantifions est `src/` dans chaque application.

### Métrique #1 : **Performance**

Consultez le test [First meaningful paint](https://developers.google.com/web/tools/lighthouse/audits/first-meaningful-paint) avec [Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) intégré à Chrome.

Plus vous affichez rapidement, meilleure est l'expérience pour la personne qui utilise l'application. Lighthouse mesure également [First interactive](https://developers.google.com/web/tools/lighthouse/audits/first-interactive), mais cela était presque identique pour la plupart des applications, et c'est en version bêta.

![Image](https://cdn-media-1.freecodecamp.org/images/n28etYksl006tP2qpK4DU1jbAPzxNrNVsfjp)
_Premier affichage significatif (ms) — plus c'est bas, mieux c'est_

Vous ne verrez probablement pas beaucoup de différence en termes de performance.

### Métrique #2 : Taille

La taille de transfert provient de l'onglet réseau de Chrome. En-têtes de réponse GZIPés plus le corps de la réponse, tels que livrés par le serveur.

Plus le fichier est petit, plus le téléchargement est rapide (et il y a moins à analyser).

Cela dépend de la taille de votre framework ainsi que des dépendances supplémentaires que vous avez ajoutées, et de la capacité de votre outil de construction à créer un bundle compact.

![Image](https://cdn-media-1.freecodecamp.org/images/hKcfeFe6Y00GCEP93hzNHwDgGmxIt-eLeOLu)
_Taille de transfert (KB) — plus c'est bas, mieux c'est_

Vous pouvez voir que Svelte, Dojo 2 et AppRun font un assez bon travail. Je ne peux pas assez vanter Elm — surtout lorsque vous regardez le prochain graphique. J'aimerais voir comment [Hyperapp](https://hyperapp.js.org/) se compare… peut-être la prochaine fois, [Jorge Bucaran](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962/undefined) ?

### Métrique #3 : Lignes de code

En utilisant [cloc](https://github.com/AlDanial/cloc), nous comptons les lignes de code dans le dossier src de chaque dépôt. Les lignes vides et les commentaires ne font **pas** partie de ce calcul. Pourquoi est-ce significatif ?

> Si le débogage est le processus de suppression des bugs logiciels, alors la programmation doit être le processus de les y mettre — Edsger Dijkstra

![Image](https://cdn-media-1.freecodecamp.org/images/5o3DrlKWd-5ntxqFg9cTiLL1tKKdlogLzAwl)
_Nombre de lignes de code — moins c'est mieux_

Moins vous avez de lignes de code, plus la probabilité de trouver une erreur est faible. Vous avez également une base de code plus petite à maintenir.

### En conclusion

Je voudrais dire un grand merci à [Eric Simons](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962/undefined) pour avoir créé le dépôt [RealWorld Example Apps](https://github.com/gothinkster/realworld), et aux nombreux contributeurs qui ont écrit différentes implémentations.

**Mise à jour** : Merci à [Jonathan Faircloth](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962/undefined) pour avoir fourni la version de production d'Angular.

> Et si vous avez trouvé cet article intéressant, vous devriez [me suivre sur Twitter](https://twitter.com/jacekschae) et Medium.
---
title: Une comparaison en conditions réelles des frameworks front-end avec benchmarks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-19T06:15:08.000Z'
originalURL: https://freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-e1cb62fd526c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C_VGnwYj_OAnTVT0ae7KQQ.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une comparaison en conditions réelles des frameworks front-end avec benchmarks
seo_desc: 'By Jacek Schae

  UPDATE: There is a newer version of this article

  A Real-World Comparison of Front-End Frameworks with Benchmarks (2018 update)This
  article is a refresh of A Real-World Comparison of Front-End Frameworks with Benchmarks
  from December 20...'
---

Par Jacek Schae

**MISE À JOUR :** Il existe une version plus récente de cet article

[**Une comparaison en conditions réelles des frameworks front-end avec benchmarks (mise à jour 2018)**](https://medium.freecodecamp.org/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962)  
[*Cet article est une actualisation de « Une comparaison en conditions réelles des frameworks front-end avec benchmarks » de décembre 2017.\_medium.freecodecamp.org*](https://medium.freecodecamp.org/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962)

Au cours des dernières années, nous avons assisté à une explosion des frameworks front-end. Chacun d'entre eux est plus que capable de construire d'excellentes applications web. Alors, comment comparer et décider lequel utiliser pour votre prochain projet ?

Tout d'abord, pour faire une comparaison significative, nous avons besoin de quelques éléments :

1. **Application en conditions réelles (Real World App)** — Quelque chose de plus qu'un « todo ». Généralement, les « todos » ne transmettent pas les connaissances et la perspective nécessaires pour construire de *réelles* applications.
    
2. **Standardisé** — Un projet qui se conforme à certaines règles. Hébergé au même endroit, il fournit une API back-end, un balisage statique, des styles et une spécification.
    
3. **Écrit par un expert** — Un projet cohérent, en conditions réelles, qu'un expert de cette technologie aurait idéalement construit. C'est vrai, du moins la plupart du temps (voir ci-dessous).
    

Alors, comment obtenir un tel projet ? La bonne nouvelle est qu'[Eric Simons](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-e1cb62fd526c/undefined) a déjà créé un projet [RealWorld](https://github.com/gothinkster/realworld). C'est un clone de la plateforme de blogging Medium. Chaque implémentation de ce projet utilise la même structure HTML, le même CSS et la même spécification d'API, mais un Framework ou une bibliothèque différente. En ce qui concerne les connaissances d'expert, c'est vrai la plupart du temps. J'ai écrit une implémentation en ClojureScript et [re-frame](https://github.com/Day8/re-frame) et je ne me considère pas comme un expert. Pour ma défense, un expert a revu mon code — merci à [Daniel Compton](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-e1cb62fd526c/undefined).

Maintenant que nous avons une spécification de base, nous avons besoin d'un ensemble standard de tests/métriques pour les comparer.

1. **Performance.** Combien de temps faut-il à cette application pour afficher le contenu et devenir utilisable ?
    
2. **Taille.** Quelle est la taille de l'application ? Nous ne comparerons que la taille du JavaScript compilé. Le CSS est commun à toutes les variantes et est téléchargé depuis un CDN (Content Delivery Network). Le HTML est également commun à toutes les variantes. Toutes les technologies compilent ou transpilent vers JavaScript, nous ne mesurons donc que ce fichier.
    
3. **Lignes de code.** De combien de lignes de code l'auteur a-t-il eu besoin pour créer l'application RealWorld basée sur la spécification ? Pour être juste, certaines applications ont un peu plus de fioritures, mais cela ne devrait pas avoir d'impact significatif. Le seul dossier que nous quantifions est src/ dans chaque application.
    

Au moment de la rédaction (décembre 2017), le projet RealWorld est disponible dans les frameworks suivants :

* [React / Redux](https://github.com/gothinkster/react-redux-realworld-example-app)
    
* [Elm](https://github.com/rtfeldman/elm-spa-example)
    
* [Angular 4+](https://github.com/gothinkster/angular-realworld-example-app)
    
* [Angular 1.5+](https://github.com/gothinkster/angularjs-realworld-example-app)
    
* [React / MobX](https://github.com/gothinkster/react-mobx-realworld-example-app)
    
* [Crizmas MVC](https://github.com/gothinkster/crizmas-mvc-realworld-example-app)
    
* [CLSJ Keechma](https://github.com/gothinkster/clojurescript-keechma-realworld-example-app)
    
* [AppRun](https://github.com/gothinkster/apprun-realworld-example-app)
    
* [CLJS re-frame](https://github.com/jacekschae/conduit) (C'est celui que j'ai fait. Il n'est pas encore listé sur le projet RealWorld).
    

### Métrique #1 : Performance

Test du [Premier rendu significatif (First meaningful paint)](https://developers.google.com/web/tools/lighthouse/audits/first-meaningful-paint) avec [Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) qui est fourni avec Chrome.

Plus le rendu est rapide, meilleure est l'expérience pour la personne qui utilise l'application. Lighthouse mesure également le [Premier interactif (First interactive)](https://developers.google.com/web/tools/lighthouse/audits/first-interactive), mais c'était presque identique pour la plupart des applications.

![Image](https://cdn-media-1.freecodecamp.org/images/PjhM-gKQrawvRPhnSaEFNAL37OgDtSap3FPw align="left")

*Premier rendu significatif (ms) — plus c'est bas, mieux c'est*

### Métrique #2 : Taille

La taille de transfert provient de l'onglet réseau de Chrome. En-têtes de réponse GZIPés plus le corps de la réponse, tels que livrés par le serveur.

Fichier plus petit = téléchargement plus rapide et moins de choses à analyser.

Cela dépend de la taille de votre Framework, de toutes les dépendances supplémentaires que vous avez ajoutées et de la capacité de votre outil de build à créer un petit bundle.

![Image](https://cdn-media-1.freecodecamp.org/images/XEfqu6RhFdM0M3DKct1wD855Cjsp7MCl8jE4 align="left")

*Taille de transfert (KB) — plus c'est bas, mieux c'est*

### Métrique #3 : Lignes de code

En utilisant [cloc](https://github.com/AlDanial/cloc), nous comptons les lignes de code dans le dossier src de chaque dépôt. Les lignes vides et les commentaires ne font **pas** partie de ce calcul. Pourquoi est-ce significatif ?

> Si le débogage est le processus de suppression des bogues logiciels, alors la programmation doit être le processus d'en introduire — Edsger Dijkstra

Moins vous avez de lignes de code, plus la probabilité d'erreur est faible et plus la base de code à maintenir est petite.

![Image](https://cdn-media-1.freecodecamp.org/images/ON1sQcGZEU9VfuY4BjXHbKI6lvHcBpjTaXRb align="left")

*\\# Lignes de code — moins il y en a, mieux c'est*

### Conclusion

#### Performance

Il s'agit d'une comparaison en conditions réelles et non d'un benchmark dans le vide. Les tests ont été effectués depuis l'Europe (Suisse). Toutes les applications étaient hébergées sur GitHub. Les valeurs peuvent différer pour vous, ce qui est normal. Les tests ont été effectués plusieurs fois pour chaque application, puis moyennés et arrondis. Les résultats étaient assez linéaires lors des comparaisons tout au long de la journée. La plupart des bibliothèques/frameworks sont dans la fourchette d'excellent et bon. Vous ne verrez pas beaucoup de différence en ce qui concerne les performances.

#### Taille

La taille du bundle pour chaque application est toujours la même. Nous comparons des implémentations similaires et regardons comment les tailles de bundle diffèrent. AppRun est incroyable ! J'ai regardé à plusieurs reprises parce que je ne pouvais pas y croire. Elm fait un travail remarquable en ce qui concerne la taille du bundle et surtout quand on regarde les lignes de code.

![Image](https://cdn-media-1.freecodecamp.org/images/olCdKtJHQdBhAnnI3GuQOwIA4Fq-VRBUTqJf align="left")

*Taille du bundle AppRun 18,7 KB*

#### **Lignes de code**

Cela a le plus grand impact sur vous en tant que développeur logiciel. Plus il y a de lignes de code, plus vous devez taper et plus il y a de maintenance. Il y a des compromis ici. Surtout en ce qui concerne les langages typés vs dynamiques. Les types vous donnent plus de sécurité et ont un coût — plus de choses à taper.

#### Typé vs dynamique

**Typé** : Elm, Angular 4+ et AppRun.

**Dynamique** : React | Redux, Angular 1.5, React | MobX, Crizmas MVC, CLJS Keechma et CLJS re-frame.

Alors, lequel est le meilleur ? Ce n'est ni mieux ni pire, c'est différent. Comme le TDD (Test Driven Development), certaines personnes l'adorent, d'autres le détestent. Vous pouvez développer d'excellents logiciels avec ou sans — choisissez celui qui vous convient le mieux.

#### Où sont Vue, Preact, Ember, Svelte, Aurelia et les autres ?

Il semble qu'ils soient en retard à la fête, mais ne vous inquiétez pas. Je ferai un autre tour quand nous les aurons. Il y a déjà des [problèmes ouverts (issues)](https://github.com/gothinkster/realworld/issues) — envisagez de contribuer ! Ou commencez de zéro et ouvrez un nouveau problème.

#### Mot de la fin

Cette comparaison est exactement ce qu'elle prétend être. Elle compare différentes implémentations d'applications web similaires en conditions réelles. Je sais, ce n'est pas parfait. Cela diffère selon la charge du serveur, le trafic réseau et bien d'autres choses qui se produisent dans le monde réel.

Merci à [Daniel Compton](https://www.freecodecamp.org/news/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-e1cb62fd526c/undefined) pour la relecture.

*Si vous avez apprécié cet article et souhaitez être informé de la publication d'articles similaires, n'hésitez pas à me suivre sur Medium et* [*Twitter*](https://twitter.com/jacekschae)*.*
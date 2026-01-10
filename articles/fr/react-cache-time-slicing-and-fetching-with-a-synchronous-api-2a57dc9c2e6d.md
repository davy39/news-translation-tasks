---
title: React-cache, time slicing et récupération avec une API synchrone
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T16:58:56.000Z'
originalURL: https://freecodecamp.org/news/react-cache-time-slicing-and-fetching-with-a-synchronous-api-2a57dc9c2e6d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h8d-4wYLN9wwiEsLAA_5yg.jpeg
tags:
- name: Browsers
  slug: browsers
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: React-cache, time slicing et récupération avec une API synchrone
seo_desc: 'By Marvin Frachet

  Well, this year seems to be the year of React. You’ve probably heard of the new
  killer feature that is coming with the 16.7-alpha.0 — Hooks. You’ve probably also
  heard about some other great and cool stuff like Time Slicing or even ...'
---

Par Marvin Frachet

Eh bien, cette année semble être l'année de React. Vous avez probablement entendu parler de la nouvelle fonctionnalité phare qui arrive avec la version 16.7-alpha.0 — les Hooks. Vous avez probablement aussi entendu parler d'autres fonctionnalités géniales comme le Time Slicing ou même Suspense.

Cet article **ne vise pas** à décrire comment utiliser certaines des nouvelles fonctionnalités, mais plutôt à prouver comment elles ont pu être construites. Juste pour comprendre ce avec quoi nous jouons.

Il est également écrit de la manière dont j'ai découvert la fonctionnalité. Ce n'est probablement pas la manière dont elle a été imaginée, mais c'est ainsi que j'ai compris les points.

Ce que vous trouverez en lisant :

* JavaScript asynchrone et la boucle d'événements
* Effets algébriques dans React, avec exemple
* Fiber et les phases de React

### Pourquoi ai-je écrit cet article ?

Ce qui m'a donné envie d'écrire cet article, c'est cette fonctionnalité spéciale et expérimentale qui permet l'utilisation d'opérations **asynchrones** avec une API **synchrone** :

`const bulbasaur = ApiResource.read()` ?... Quoi ? **Synchrone** ?!

La bibliothèque [react-cache](https://github.com/facebook/react/tree/master/packages/react-cache) crée la possibilité d'utiliser des opérations asynchrones avec une API synchrone. C'est cette fonctionnalité qui m'a donné envie d'apprendre comment React fonctionne sous le capot. Voici une présentation par [Dan Abramov](https://twitter.com/dan_abramov) et [Andrew Clark](https://twitter.com/acdlite) sur cette bibliothèque :

Comment est-ce même possible ? Comment pouvons-nous obtenir des données distantes en utilisant des appels synchrones ?

Plongeons-nous dans cet exemple et essayons de comprendre comment [react-cache](https://github.com/facebook/react/tree/master/packages/react-cache) implémente une telle fonctionnalité et découvrons comment elle peut fonctionner. Cette histoire commence avec l'[architecture fiber](https://github.com/acdlite/react-fiber-architecture).

### Contrôler les opérations JavaScript

L'architecture Fiber permet à React de prendre le contrôle sur l'exécution des tâches. Elle a été construite pour résoudre de multiples problèmes dont React souffrait. En voici deux qui ont retenu mon attention :

* prioriser certains événements, comme les entrées utilisateur par rapport à la récupération de données
* diviser de manière asynchrone le calcul React pour conserver la disponibilité du thread principal et éviter de le bloquer pendant de longs processus de rendu

Tout ce qui déclenche un changement d'état — pas seulement avec React — à l'intérieur d'une application JavaScript est dû à des opérations asynchrones. Cela inclut `setTimeout`, `fetch`, et les écouteurs d'événements.

Les opérations asynchrones sont gérées à travers plusieurs concepts fondamentaux de JavaScript :

* tâches (micro, macro, rendu, etc.)
* boucle d'événements
* pile d'appels

Si vous n'êtes pas familier avec ces concepts, je vous suggère de regarder cette vidéo de [Jake Archibald](https://twitter.com/jaffathecake) :

Grâce à Fiber, les entrées utilisateur sont **résolues** avant d'autres opérations asynchrones comme les appels fetch.

Comment est-ce même possible ?

Eh bien, la présentation d'Archibald ci-dessus a été la première pierre posée sur mon propre chemin d'apprentissage sur le fonctionnement de la boucle d'événements. Il dit que les micro-tâches — générées via l'API Promise, par exemple — sont exécutées et vidées **avant** la prochaine macro-tâche. Ce processus utilise des méthodes basées sur des rappels comme `setTimeout`.

Alors, si vous vous souvenez de ma comparaison « entrée utilisateur versus récupération de données », comment l'équipe a-t-elle fait pour que les résolutions de `fetch` se fassent **après** les résolutions de `onChange` ?

Aucun de ces concepts ne s'inscrit dans la même spécification, [WhatWG](https://fetch.spec.whatwg.org/) / [HTML5](http://w3c.github.io/html/webappapis.html#dom-globaleventhandlers-onclick) / [Ecma-262](https://www.ecma-international.org/ecma-262/6.0/#sec-promise-objects), et sont fournis à partir de différents endroits comme le navigateur ou les moteurs JS.

Je veux dire, comment sommes-nous censés résoudre une `Promise` après un `setTimeout` ?

Cela me semblait absolument fou et il était vraiment difficile de se faire une idée de comment cela pouvait fonctionner. Le fait est que cela se passe à un niveau supérieur.

Plus tard, j'ai regardé l'incroyable présentation de [Brandon Dail](https://twitter.com/aweary) à React Rally. Cela présente les nouvelles fonctionnalités de [Time Slicing et Suspense](https://www.youtube.com/watch?v=nLF0n9SACd4) qui ont été livrées grâce à l'architecture Fiber de React :

Selon Dail, Fiber est comme la pile d'appels JavaScript habituelle où chaque élément de la pile est appelé une **fiber**. Elle est différente de la pile d'appels qui repose sur des **frames** qui représentent des **fonctions (+ métadonnées)**. Plutôt, une fiber représente un **composant (+ métadonnées)**. Considérons une fiber comme une grande boîte autour d'un composant qui sait tout sur lui.

Il y a une différence importante entre ces deux concepts.

D'une part, la pile d'appels est une fonctionnalité qui a été construite au-dessus de la **partie native pilotant le code JavaScript**. Elle vise à empiler chaque appel de fonction JavaScript et à les exécuter par elles-mêmes. Chaque fois que nous appelons une fonction, elle est ajoutée à la pile. Sans la pile d'appels, nous ne pourrions pas avoir des traces de pile d'erreurs claires et détaillées. Et puisque la pile d'appels n'est pas accessible à partir d'un code JavaScript, il est vraiment difficile, voire impossible, de prendre le contrôle sur elle.

D'autre part, les fibers — comme une pile de fibers — représentent le même concept, mais construit en **code JavaScript**. La plus petite unité n'est pas des fonctions, mais un composant. Elle s'exécute en fait dans un univers JavaScript.

Le fait que l'architecture Fiber soit entièrement construite en JavaScript signifie que nous pouvons l'utiliser, y accéder et la modifier. Nous pouvons travailler dessus en utilisant du JavaScript standard.

Ce qui m'a induit en erreur était que je pensais que React utilisait un contournement pour couper la manière interne dont JavaScript fonctionne. **Ce n'est pas le cas**. Les Fibers sont simplement des objets JavaScript qui possèdent des informations sur les composants React et qui peuvent interagir avec leurs cycles de vie. Ils ne peuvent agir que sur les fonctionnalités internes de React.

L'idée n'est **pas** de redéfinir comment JavaScript devrait fonctionner, comme dire que la résolution des micro-tâches de `fetch` devrait être exécutée avant les tâches de rappel. C'est plutôt de déterminer quelles méthodes React **devraient être appelées ou non** dans un contexte spécifique, comme interrompre les différents appels de méthodes de cycle de vie.

Hey attendez ! Vous dites que les fibers peuvent contrôler absolument tout dans une application React ? Mais comment un composant peut-il dire à React d'arrêter de faire quoi que ce soit ?

### Effets algébriques, oui, mais en JavaScript s'il vous plaît

React est capable de contrôler les composants et de savoir si un composant est en cours d'exécution, grâce à l'architecture Fiber. Ce qui manque maintenant, c'est un moyen de dire à React qu'un changement s'est produit pour un composant spécifique, afin qu'il gère ce changement.

C'est là que les **effets algébriques** entrent en jeu.

Les effets algébriques ne sont pas quelque chose qui existe en JavaScript. Je vais essayer de les expliquer avec une explication de haut niveau.

Les effets algébriques sont un concept qui permet d'envoyer des informations quelque part, un peu comme un dispatcher. L'idée est d'appeler une fonction spécifique qui va **interrompre** la fonction actuellement en cours d'exécution à une position précise pour laisser une fonction parente gérer un calcul. Lorsque le calcul parent se termine, il peut reprendre le programme à la position initiale où l'information a été envoyée.

Certains langages comme [OCaml](http://ocamllabs.io/doc/effects.html) ou [Eff](https://www.eff-lang.org/) bénéficient de ces fonctionnalités de manière native. C'est une abstraction vraiment intéressante puisque les détails d'implémentation ne reposent que sur le parent :

Ne serait-ce pas génial d'avoir une telle fonctionnalité en JavaScript ?

L'équipe React a créé une approche similaire dans un contexte React en utilisant le bloc `try/catch` de JavaScript. Selon Dail, c'est le concept le plus proche disponible en JavaScript.

Lancer quelque chose permet d'envoyer des informations à un parent, quelque part. Le premier parent qui attrape l'information est capable de la traiter et de faire des calculs dessus.

#### Un exemple vaut mieux qu'un long discours

Imaginez le code suivant qui essaie de récupérer Bulbasaur **en utilisant une API synchrone** :

Ce morceau de code peut sembler étrange puisqu'il n'est pas très courant de récupérer des données en utilisant une API synchrone. Plongeons-nous dans l'implémentation de la fonction `customFetch` :

Oh attendez ! Cela ne ressemble absolument pas à un fetch ! Je ne comprends pas du tout ce que cette fonction vise à faire...

Eh bien, imaginez quelque chose **autour du composant**, disons une fiber qui ressemble à :

Prenez le temps de lire le code.

Maintenant, plongeons-nous dans l'implémentation de `customFetch` :

La partie importante dans les extraits précédents est le bloc `try/catch`.

Faisons le point sur ce qui se passe à travers ces différents morceaux de code :

* Le composant `Pokemon` appelle la méthode `customFetch`.
* La méthode `customFetch` essaie de lire son cache interne, mais il est vide. Elle lance donc quelque chose / quelque part — effets algébriques.
* Le parent `fiber` attrape cette information, la traite et récupère les données. Ensuite, il remplit le cache de `customFetch` avec les données.
* Un re-rendu se produit dans `Component(args)` et, maintenant, le cache de `customFetch` est plein. Les données sont maintenant disponibles dans le composant en utilisant une API synchrone.

[Jetez un coup d'œil aux détails de l'implémentation de `react-cache` et vérifiez les différents lancers.](https://github.com/facebook/react/blob/d14ba87b1bfed76900d6d25722f069003561e2e3/packages/react-cache/src/ReactCache.js#L158)

Quelque chose a peut-être attiré votre attention pendant ce processus : `render` a été appelé deux fois. Une pour lancer l'erreur — **mettre en pause** le composant — et une pour obtenir les données — **reprendre** le composant. C'est acceptable avec React de déclencher plusieurs appels `render` puisque c'est uniquement une fonction pure — elle n'a aucun effet secondaire par elle-même.

Attendez... Quoi ? `render` n'a aucun effet secondaire ? Qu'en est-il du DOM ?

### Phases de React

Si vous avez travaillé avec React depuis longtemps, vous avez peut-être entendu dire qu'il n'est pas bon de re-rendre plusieurs fois. Avant l'architecture Fiber, chaque fois que nous appelions la fonction de rendu, React effectuait des calculs internes puis modifiait le DOM en conséquence. Par exemple, cela se produisait lors de l'appel de la fonction de rendu via `setState`. Le processus était en ligne :

`setState` → `render` → comparer les nœuds virtuels → mettre à jour les nœuds DOM

Avec Fiber, le processus est un peu différent. Il a introduit un concept de file d'attente et de lots qui permet des modifications DOM à haute performance.

L'idée est assez simple. Nous supposons que les écrans peuvent fonctionner à ~60 images par seconde. À partir de cette hypothèse, et en utilisant les fonctions JavaScript disponibles, il est possible de faire des calculs et des modifications DOM seulement toutes les ~16,7 ms. Avec Fiber, React peut mettre en file d'attente plusieurs modifications et les valider environ 60 fois par seconde.

Ce type de modification a permis à React de se diviser en trois phases avec leurs propres avantages et particularités :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YPcEsrQ0f5qjGP-a5oVj7A.png)
_[Dan Abramov concernant les phases de React](https://twitter.com/dan_abramov/status/981712092611989509/photo/1?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E981712092611989509&amp;ref_url=https%3A%2F%2Fmedium.com%2Fmedia%2Fbda1c34a16e9f8a8e3eb244716a1da72%3FpostId%3D2a57dc9c2e6d" rel="noopener" target="_blank" title=")_

* La phase de rendu est pure et déterministe. Elle n'a pas d'effets secondaires et les différentes fonctions qui la composent peuvent être appelées plusieurs fois. La **phase de rendu est interruptible** — ce n'est pas la fonction `render` qui est en mode pause, mais toute la phase.
* La phase de pré-validation vise à fournir un accès à l'état réel du DOM, comme les positions des barres de défilement, en mode lecture.
* La phase de validation modifie effectivement le DOM et **n'est pas interruptible**. React ne peut pas faire de pause pendant cette phase.

Cet ensemble de trois phases a introduit les capacités de Time Slicing. React est capable de faire une pause pendant la phase de rendu, entre deux appels de fonctions de composants, et de reprendre cette phase lorsque cela est nécessaire.

Dans Fiber, `render` vise uniquement à **obtenir la dernière représentation disponible** d'un composant en fonction de son état interne pour faire des comparaisons et savoir si React doit changer le DOM ou non. Si une modification de validation est requise, elle ajoutera la modification à une file d'attente « en cours de travail ».

L'équipe React a réalisé d'énormes améliorations de performance grâce à React Concurrent (Time Slicing + Suspense) et à l'architecture Fiber. Ils ont créé des contournements pour contrer différents problèmes de navigateur comme la priorisation des événements et la concurrency.

Si nous faisons un pas en arrière, n'est-ce pas ce qu'ils ont montré ? La priorisation semble être le nouveau défi pour les navigateurs et les frameworks front-end.

D'autres équipes travaillent également à améliorer l'état actuel de l'art et proposent même des API futures. Voici la prise de position de Google :
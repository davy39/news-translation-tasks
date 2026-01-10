---
title: 'CSP vs RxJS : ce que vous ne savez pas.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T17:18:15.000Z'
originalURL: https://freecodecamp.org/news/csp-vs-rxjs-what-you-dont-know-1542cd5dd100
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ColTdidsgUyGVesk
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: RxJS
  slug: rxjs
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'CSP vs RxJS : ce que vous ne savez pas.'
seo_desc: 'By Kevin Ghadyani

  What happened to CSP?


  _Photo by [Unsplash](https://unsplash.com/@lamppidotco?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">James Pond on <a href="https://unsplash.com?utm_source=medium&utm_medium=re...'
---

Par Kevin Ghadyani

#### Qu'est-il arrivé à CSP ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*ColTdidsgUyGVesk)
_Photo par [Unsplash](https://unsplash.com/@lamppidotco?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">James Pond</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Vous avez probablement cliqué sur cet article en vous demandant « qu'est-ce que CSP ? ». C'est les **processus séquentiels communicants**. Toujours perplexe ?

CSP est une méthode de communication entre différentes fonctions (générateurs) dans votre code en utilisant un canal partagé.

Qu'est-ce que cela signifie ? Laissez-moi vous l'expliquer directement. Il y a ce concept de canal. Pensez-y comme une file d'attente. Vous pouvez y mettre des choses et en retirer.

Ainsi, avec deux fonctions, vous pouvez en avoir une qui ajoute des choses sur le canal (producteur) et une autre qui retire des choses et effectue un travail (consommateur).

Un cas d'utilisation avancé typique serait plusieurs producteurs et un consommateur. De cette façon, vous pouvez contrôler les données que vous obtenez, mais vous pouvez avoir plusieurs choses qui vous les fournissent.

Contrairement à RxJS, ces canaux sont automatiques. Vous ne recevez pas de valeurs n'importe comment, vous devez les demander.

### Utilisation de CSP

Voici un petit exemple de CSP utilisant la bibliothèque super simple (et morte) [Channel4](https://www.npmjs.com/package/channel4) :

Les canaux CSP s'exécutent de manière asynchrone. Ainsi, dès que cela s'exécute, le message synchrone « TERMINÉ » est d'abord enregistré. Ensuite, nos preneurs de canal sont exécutés dans l'ordre.

La chose la plus intéressante pour moi est la nature bloquante (mais asynchrone) de CSP. Remarquez comment nous avons créé le troisième `take` avant de mettre « C » sur le canal. Contrairement aux deux premières fonctions `take`, la troisième n'a rien à prendre. Dès qu'une chose arrive dans le canal, elle la prend immédiatement.

Notez également que les consommateurs doivent constamment retirer des choses du canal jusqu'à ce que ce canal se ferme. C'est pourquoi « D » n'est jamais enregistré. Vous devez définir un autre `take` pour récupérer la valeur suivante du canal.

Avec les observables, vous recevez des valeurs, vous n'avez donc pas à vous soucier de les retirer manuellement. Si vous souhaitez mettre en mémoire tampon ces valeurs, RxJS fournit plusieurs méthodes de pipeline à cet effet. Pas besoin d'utiliser CSP.

Tout le concept derrière les observables est que chaque écouteur reçoit les mêmes données dès que l'observateur appelle `next`. Avec CSP, c'est comme l'approche IxJS où vous traitez les données par morceaux.

### CSP EST MORT !?

Vous pouvez trouver des implémentations de CSP dans [Go](https://godoc.org/github.com/thomas11/csp) et [Closure](https://github.com/clojure/core.async). En JavaScript, toutes les bibliothèques CSP, à l'exception de quelques-unes, sont mortes et même alors, leur audience est petite ?.

J'ai découvert CSP grâce à [l'excellente conférence de Vincenzo Chianese](https://www.youtube.com/watch?v=r7yWWxdP_nc). Il a recommandé cette bibliothèque haut de gamme appelée [js-csp](https://github.com/ubolonton/js-csp). Malheureusement, elle n'est plus maintenue.

D'après ce qu'il a dit dans sa conférence de 2017, cela semblait être un gros problème. Il a parlé de la façon dont les transducteurs allaient exploser dans quelques mois et de la façon dont js-csp avait déjà un support pour eux.

Il semblait que CSP pouvait fondamentalement changer la façon dont vous développiez des applications asynchrones en JavaScript. Mais rien de tout cela ne s'est jamais produit. Les transducteurs ont disparu ; remplacés par des bibliothèques comme RxJS, et l'engouement autour de CSP s'est dissous.

Vincenzo a noté comment CSP est un tout autre niveau au-dessus des promesses. Il a raison. Le pouvoir que vous obtenez en ayant plusieurs fonctions interagissant de manière asynchrone est incroyable.

Les promesses, par leur nature avide, ne sont même pas dans le même parc. Peu savait-il que les dernières bibliothèques CSP finiraient par supporter les promesses sous le capot ?.

### Alternative à CSP : Redux-Saga

Si vous avez déjà utilisé Redux-Saga, les idées et les concepts autour de CSP vous semblent probablement familiers. C'est parce qu'ils le sont. En fait, Redux-Saga est une implémentation de CSP en JavaScript ; la plus populaire de loin.

Il y a même un concept de « canaux » dans Redux-Sagas : 
[https://github.com/redux-saga/redux-saga/blob/master/docs/advanced/Channels.md](https://github.com/redux-saga/redux-saga/blob/master/docs/advanced/Channels.md)

Les canaux reçoivent des informations d'événements externes, mettent en mémoire tampon des actions vers le magasin Redux et communiquent entre deux sagas. C'est la même façon dont ils sont utilisés dans CSP avec les mêmes fonctions `take` et `put`.

Assez cool de voir une implémentation réelle de CSP en JavaScript, mais étrange que très peu l'aient remarqué. Cela montre à quel point CSP a peu décollé avant de mourir.

### Alternative à CSP : Redux-Observable

Vous avez peut-être entendu parler de quelque chose appelé Redux-Observable. C'est un concept similaire à CSP et Redux-Saga, mais au lieu du style impératif des générateurs, il prend une approche fonctionnelle et utilise des pipelines RxJS appelés « épics ».

Dans Redux-Observable, tout se passe à travers deux sujets : `action$` et `state$`. Ce sont vos canaux.

Au lieu de prendre et de mettre manuellement, vous écoutez des actions spécifiques en tant que consommateur d'un canal d'action ou d'état. Chaque épique a la capacité d'être également un producteur en envoyant des actions à travers le pipeline.

Si vous souhaitez construire une file d'attente dans Redux-Observable comme avec CSP, c'est un peu plus compliqué car il n'y a pas d'opérateur disponible à cet effet, mais c'est entièrement possible.

J'ai créé un repl qui fait exactement cela :

Comparé à notre exemple CSP précédent, voici ce que vous pouvez vous attendre à voir :

L'exemple nécessite uniquement RxJS et tout est dans un seul fichier pour simplifier. Comme vous pouvez le voir, il est beaucoup plus difficile de mettre en file d'attente des éléments dans RxJS de la même manière que vous pourriez le faire avec CSP. C'est entièrement possible, mais nécessite beaucoup plus de code.

Personnellement, j'adorerais voir RxJS ajouter un opérateur comme `bufferWhen` qui vous permet de distribuer des éléments individuels au lieu de l'ensemble du tampon. Ensuite, vous pourriez accomplir le style CSP dans Redux-Observable beaucoup plus facilement.

### Conclusion

CSP était un concept cool, mais il est mort en JavaScript. Redux-Saga et Redux-Observable sont des alternatives dignes.

Même avec la capacité de s'intégrer avec les bibliothèques de transducteurs, RxJS a toujours une longueur d'avance. Sa massive communauté d'éducateurs et d'applications de production le rend difficile à battre.

C'est pourquoi je pense que CSP est mort en JavaScript.

### Plus de lectures

Si vous avez aimé ce que vous avez lu, veuillez consulter mes autres articles sur des sujets similaires qui ouvrent les yeux :

* [Redux-Observable Peut Résoudre Vos Problèmes d'État](https://medium.com/@Sawtaytoes/redux-observable-can-solve-your-state-problems-15b23a9649d7)
* [Redux-Observable sans Redux](https://itnext.io/redux-observable-without-redux-ff4a2b5a4b39)
* [Callbacks : Le Guide Définitif](https://itnext.io/the-definitive-guide-to-callbacks-in-javascript-44a39c065292)
* [Promesses : Le Guide Définitif](https://itnext.io/promises-the-definitive-guide-6a49e0dbf3b7)
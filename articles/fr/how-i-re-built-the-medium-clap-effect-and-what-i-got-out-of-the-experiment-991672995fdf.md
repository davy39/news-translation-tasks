---
title: Comment j'ai (re)construit l'effet d'applaudissements de Medium — et ce que
  j'ai retiré de l'expérience.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-29T10:22:58.000Z'
originalURL: https://freecodecamp.org/news/how-i-re-built-the-medium-clap-effect-and-what-i-got-out-of-the-experiment-991672995fdf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2gzBT_k8M-SrIZ1maT7njQ.gif
tags:
- name: Design
  slug: design
- name: learning
  slug: learning
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment j'ai (re)construit l'effet d'applaudissements de Medium — et ce
  que j'ai retiré de l'expérience.
seo_desc: 'By Emmanuel Ohans

  Four years ago, I read a quote that would change my life forever.

  I don’t remember the surrounding circumstances, but the sun was blazing hot and
  I was on the results page of a Google search.

  A famous Pablo Picasso quote popped up, ...'
---

Par Emmanuel Ohans

Il y a quatre ans, j'ai lu une citation qui allait changer ma vie pour toujours.

Je ne me souviens pas des circonstances exactes, mais le soleil était brûlant et j'étais sur la page de résultats d'une recherche Google.

Une célèbre citation de Pablo Picasso est apparue, et pendant les semaines suivantes, j'y ai été complètement perdu.

> Les bons artistes copient ; les grands artistes volent

> — Pablo Picasso

### Quoi ? Est-ce qu'il voulait vraiment dire ça ?

Alors que de multiples questions tourbillonnaient dans mon esprit, j'ai dû en lire davantage sur qui était Pablo.

Pablo Picasso était un artiste considéré comme l'un des plus influents et des plus grands du 20e siècle. À ce moment-là, je savais qu'il n'était pas un raté qui disait n'importe quoi.

J'ai continué ma vie, mais cette citation ne m'a jamais quitté.

Des années plus tard, j'étais devenu un adepte astucieux de la philosophie du "vol". Elle était si ancrée dans mon subconscient que je pensais écrire un jour un best-seller du New York Times sur le sujet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wukzTeTc2i2-mRahxcjGTw.png)
_La vie est passée. Je n'ai jamais écrit le livre :(_

J'ai appliqué cette règle à presque tout ce que je faisais.

Par exemple, j'ai passé des heures à réécrire plusieurs codepens (créés par d'autres) à la main, tout cela pour apprendre quelque chose en volant. Plus tôt cette année, j'ai vu [Dan Abramov](https://www.freecodecamp.org/news/how-i-re-built-the-medium-clap-effect-and-what-i-got-out-of-the-experiment-991672995fdf/undefined) parler de quelque chose de similaire.

Je n'étais pas fou après tout.

La règle du vol semble être une règle générale pour la maîtrise.

Dans son livre, _Peak: Secrets from the new science of expertise_, Anders Ericsson parle de la boucle de rétroaction et de son importance pour la maîtrise. En fait, c'était la même technique que Benjamin Franklin utilisait pour écrire des livres incroyables. Il était sans doute l'un des meilleurs écrivains américains de son temps.

Cette mentalité et cette méthode d'apprentissage m'ont conduit à tenter de recréer l'effet d'applaudissements de Medium.

### L'expérience

L'applaudissement de Medium a été conçu et construit par des personnes au moins cinq fois plus intelligentes que moi. Mais ce n'était pas la première fois que je recréais le travail des autres. L'applaudissement de Medium n'était qu'un parmi tant d'autres projets.

J'ai toujours trouvé l'applaudissement de Medium si satisfaisant. Plusieurs fois, j'ai applaudi après la marque des 50 juste pour ressentir cette animation satisfaisante.

Construire l'applaudissement de Medium était une expérience intéressante. Le but n'était pas de créer un clone exact, juste quelque chose qui fonctionnait de la même manière.

### La technologie que j'ai utilisée

Pour le contenu, j'ai utilisé le bon vieux HTML et un peu de SVG. J'ai obtenu une icône d'applaudissements du Noun Project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9M0oeCEgOsovOMz2snw5iw.png)
_SVG Créé par Luis Durazo du [Noun Project](https://thenounproject.com/search/?q=clap&amp;i=28959" rel="noopener" target="_blank" title=")_

J'ai ouvert l'icône d'applaudissements dans Illustrator et je l'ai modifiée à ma guise. Je l'ai ensuite optimisée via [SVGOMG](https://jakearchibald.github.io/svgomg/).

J'avais besoin de JavaScript pour l'interactivité. J'ai donc construit l'applaudissement avec vanillaJS, puis je l'ai forké pour le reconstruire via [ReactJS](https://codepen.io/ohansemmanuel/full/zEJpYy/).

Pour les animations, j'ai choisi [LegoMushroom](https://www.freecodecamp.org/news/how-i-re-built-the-medium-clap-effect-and-what-i-got-out-of-the-experiment-991672995fdf/undefined)s mo.js. Cela semblait être le meilleur pour recréer les animations d'applaudissements de Medium. [Mo.js](http://mojs.io) est une bibliothèque d'animation assez intéressante avec une API déclarative. Je la trouve également très conviviale pour les débutants.

### Comment j'ai commencé

Je n'étais pas particulièrement sûr de par où commencer. J'avais une certaine expérience avec SVG, mais pas beaucoup avec mo.js.

À cette époque, il n'y avait pas d'applaudissement de Medium "fonctionnel" sur [codepen](http://codepen.io). Il n'y avait rien à apprendre là-bas.

Alors j'ai volé à nouveau.

"Il doit y avoir quelque chose en ligne dont je peux apprendre", me suis-je dit. Après quelques recherches infructueuses, j'ai trouvé quelque chose.

[Mary Lou](https://www.freecodecamp.org/news/how-i-re-built-the-medium-clap-effect-and-what-i-got-out-of-the-experiment-991672995fdf/undefined)s [Codrops](https://tympanus.net/codrops/) est une ressource incroyable pour des trucs pratiques de frontend. J'ai recherché et trouvé quelques [icônes animées](https://github.com/codrops/Animocons) là-bas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rCTs5mvGAYWofIKz1b4Kfg.gif)
_Les icônes animées de codrops ont été inspirées par ce shot de [Daryl Grinn](https://dribbble.com/daryl" rel="noopener" target="_blank" title=")_

Les icônes n'avaient rien à voir avec l'applaudissement de Medium, mais il y avait certainement quelque chose à apprendre.

Vous savez ce que j'ai fait, n'est-ce pas ?

J'ai construit les icônes animées de codrops à partir de zéro. J'ai copié l'ensemble du code à la main.

Cela m'a donné beaucoup de perspective, et j'ai su comment m'y prendre pour l'applaudissement de Medium par la suite.

### Comment apprendre vraiment vite ?

En dehors de la construction des icônes animées de codrops, je n'avais pas une expérience substantielle avec [mo.js](http://mojs.io)

Ce n'était pas un gros problème. J'avais toujours été excité par la perspective d'apprendre quelque chose de nouveau plus rapidement, et j'avais développé un système pour apprendre les choses rapidement.

En 2012, Scott Young a complété les 33 cours du [programme de sciences informatiques légendaire du MIT](http://www.eecs.mit.edu/academics-admissions/undergraduate-programs/course-6-3-computer-science-and-engineering), de l'algèbre linéaire à la théorie du calcul, en moins d'un an. Il est rapidement devenu mon inspiration.

Ce programme du MIT était censé être un programme de quatre ans, mais d'une manière ou d'une autre, il a réussi à le maîtriser systématiquement en moins de 12 mois.

Je crois en l'apprentissage ultra-rapide. C'est une compétence si importante dans l'économie d'aujourd'hui.

Alors, quel était le plan ?

Tout d'abord, j'avais besoin d'une couverture. Une couverture autour du terrain de mo.js. Comme le dit Scott, vous ne pouvez pas planifier une attaque si vous n'avez pas de carte du terrain.

Tout d'abord, j'ai parcouru les tutoriels officiels de mo.js. J'en ai sauté certains, pour être honnête. J'ai vu une vidéo [youtube](https://youtu.be/yRxWa8lXasI) où Sarah Drasner expliquait comment fonctionnait la bibliothèque mo.js. J'ai regardé la vidéo à 2X vitesse. J'ai également lu le livre de Sarah, [SVG Animations](https://www.amazon.com/SVG-Animations-Implementations-Responsive-Animation/dp/1491939702). Il y avait un chapitre dédié à la bibliothèque mo.js.

Je lis très vite.

Tout ce dont j'avais besoin à ce stade était une couverture sur le fonctionnement de la bibliothèque et ce qui était possible avec elle.

Après cela, je suis passé à la mise en pratique de mes connaissances. Il était temps de construire l'applaudissement de [Medium](https://www.freecodecamp.org/news/how-i-re-built-the-medium-clap-effect-and-what-i-got-out-of-the-experiment-991672995fdf/undefined).

Après avoir passé beaucoup de temps sur les animations, j'ai fini par réussir. Quelque chose qui ne craignait pas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*whZ-_7SaDzmDXwfpkliMFw.jpeg)
_Exemples de configurations pour les animations alimentées par mo.js_

Je me suis bloqué à certains points. J'ai fait des erreurs, et j'ai même passé quelques jours à ajuster des trucs. Mais oui, j'ai réussi à le faire fonctionner.

### Quel est le but ?

Je crois en me challenger continuellement. Me pousser juste au-delà de ce que je pense savoir ou pouvoir faire.

Ce n'était qu'une autre expérience dans ce sens.

### Était-ce une expérience ratée ?

Je ne dirais pas cela.

Le 11 octobre, le pen a été sélectionné et a été vu par plus de 2 000 personnes.

J'ai donné une conférence au ReactJS Summit, à Lagos, sur [SVG et Microinteractions](http://bit.ly/2xVmb45). Là, j'ai parlé des micro-interactions dans le contexte des applications ReactJS, et j'ai pu montrer comment construire l'effet d'applaudissements de Medium.

### Conclusion

J'ai trouvé un nouvel amour pour les micro-interactions, et je crois qu'elles sont les petits géants qui font un grand produit.

Dans l'ensemble, ce fut une expérience intéressante et fructueuse. Je ne le regrette pas. Pas du tout.

Prévois-je de recréer des projets plus ambitieux ? Bien sûr !

Mais hé, c'est une discussion pour un autre jour :)

Continuez à construire, continuez à coder !
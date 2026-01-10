---
title: En défense du JavaScript hyper modulaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-30T00:13:01.000Z'
originalURL: https://freecodecamp.org/news/in-defense-of-hyper-modular-javascript-33934c79e113
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1P-6L0Iuj287sBcgF35yhw.jpeg
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: open source
  slug: open-source
- name: technology
  slug: technology
seo_title: En défense du JavaScript hyper modulaire
seo_desc: 'By Mike Groseclose

  Last week npmgate was a big topic for the JavaScript community. For those of you
  who haven’t been following what happened, here’s the TL;DR:

  A company, named Kik, asked Azer Koçulu to give them the kik project name on npm.
  Azer sai...'
---

Par Mike Groseclose

La semaine dernière, npmgate a été un sujet brûlant pour la communauté JavaScript. Pour ceux qui n'ont pas suivi ce qui s'est passé, voici le TL;DR :

Une entreprise, nommée Kik, a demandé à [Azer Koçulu](https://www.freecodecamp.org/news/in-defense-of-hyper-modular-javascript-33934c79e113/undefined) de leur céder le nom de projet _kik_ sur npm. Azer a refusé (car il l'utilisait déjà). Kik a redemandé, cette fois en menaçant de faire intervenir des avocats pour violation de marque déposée. Azer a refusé catégoriquement et Kik a escaladé le problème à npm. npm a pris le parti de Kik et a transféré la propriété du module à Kik. En réponse, Azer a écrit [J'ai juste libéré mes modules](https://medium.com/@azerbike/i-ve-just-liberated-my-modules-9045c06be67c#.qcyr9y1u3) et a supprimé tous ses packages de npm. L'un des packages qu'il a supprimés était [_left-pad_](https://github.com/azer/left-pad).

La suppression de _left-pad_ de npm a essentiellement cassé le processus d'installation de tout projet l'utilisant comme dépendance. L'impact a été important car il était utilisé par un grand nombre de projets très populaires (Babel, Atom et React, pour n'en nommer que quelques-uns).

Internet a pris feu ?.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FRZsr6bI_k5EhlcC0H0nMQ.gif)

Tout cela a soulevé un certain nombre de questions, dont la plupart peuvent être catégorisées comme suit :

1. Était-ce une violation de marque déposée ? Une question juridique.
2. npm aurait-il dû prendre le parti de Kik ? Une question commerciale.
3. Devrait-on pouvoir désactiver la publication d'un module qui est une dépendance d'un autre module ? Une préoccupation technique.
4. Les modules npm devraient-ils être mutables ? Une préoccupation technique.
5. La communauté devrait-elle utiliser des modules comme left-pad comme dépendances dès le départ ? Une discussion beaucoup plus large.

npm, et leur équipe juridique, seront ceux qui devront finalement résoudre les problèmes commerciaux et juridiques (#1 & #2 ci-dessus). Il leur appartiendra de déterminer si cela constituait vraiment une violation de marque déposée et quelle sera la politique concernant les demandes de ce type à l'avenir.

Pour le point #3 ci-dessus (la possibilité de désactiver la publication d'un module qui est une dépendance d'un autre module publié), npm a fait la déclaration suivante :

> npm a besoin de garanties pour empêcher quiconque de causer autant de perturbations. Si ces garanties avaient été en place hier, ce post-mortem n'aurait pas été nécessaire.

> - @izs de [kik, left-pad, et npm](http://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm)

Bien que [npm-shrinkwrap](https://docs.npmjs.com/cli/shrinkwrap) puisse aider avec certains des problèmes de mutabilité (#4), la seule véritable atténuation que j'ai vue est de regrouper vos dépendances avec votre package publié. [Rich Harris](https://www.freecodecamp.org/news/in-defense-of-hyper-modular-javascript-33934c79e113/undefined) explique cela dans son article [Comment ne pas casser Internet avec ce truc bizarre](https://medium.com/@Rich_Harris/how-to-not-break-the-internet-with-this-one-weird-trick-e3e2d57fee28#.12cx6pe8z).

Cela nous amène donc au point #6, la raison pour laquelle cet article existe :

#### La communauté devrait-elle utiliser des modules comme left-pad comme dépendances dès le départ ?

Pour comprendre pourquoi cela fait même débat, nous devrions d'abord comprendre _left-pad_. Étant donné une chaîne de caractères (str), une longueur (len) et un caractère (ch), _left-pad_ remplira le côté gauche de _str_ avec _ch_ jusqu'à ce que la longueur de la chaîne soit égale à _len_.

Voici l'intégralité du code alimentant _left-pad_ :

L'idée que 17 lignes de code (221 caractères) étaient derrière l'implosion d'Internet a suscité de nombreuses plaintes concernant l'utilisation de packages hyper-modulaires au sein de la communauté JavaScript.

Alors, avec cela, (enfin) je commence.

#### npmgate n'avait rien à voir avec la taille du module left-pad

La taille de _left-pad_ est un leurre. Le nombre de lignes de code qu'il contient est complètement sans rapport avec la discussion sur la manière dont sa suppression de l'écosystème npm a cassé d'autres packages. Cela aurait pu être la suppression de n'importe quel package de l'écosystème qui aurait causé cela.

Azer a supprimé 272 modules lors de son exode de npm. Il est définitivement sûr de dire que _left-pad_ a été écrit par un développeur qui s'est établi dans la communauté.

Ceux qui soutiennent qu'avoir une dépendance comme _left-pad_ ajoute un risque à leur projet soutiennent essentiellement contre le fait d'avoir **toute** dépendance npm externe dans leur projet.

#### Oui, nous pouvons tous écrire des modules comme left-pad à partir de zéro

Mais pourquoi le ferions-nous ?

La raison pour laquelle des bibliothèques utilitaires comme [jQuery](https://jquery.com/) et [lodash](https://lodash.com/docs) ont été créées est d'améliorer l'expérience des développeurs.

Bien sûr, le code derrière _left-pad_ n'est pas très complexe et il pourrait probablement être réécrit par n'importe lequel d'entre nous en quelques minutes. Certains pourraient même apprécier la diversion. Cela dit, le fait de passer du contexte de l'écriture de code pour résoudre le problème en cours à l'écriture d'une méthode qui manipule des chaînes de caractères semble être une mauvaise utilisation du temps et de l'énergie. N'oubliez pas, le fait que nous puissions faire quelque chose ne signifie pas que nous devrions le faire.

Chaque jour, nous devrions nous permettre de nous concentrer sur des problèmes plus grands et meilleurs que la veille.

#### Communauté

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYKTXIsgyO9laDp5GCMsWA.png)
_source [http://www.modulecounts.com/](http://www.modulecounts.com/" rel="noopener" target="_blank" title=")_

Il y a une raison pour laquelle npm surpasse tous les autres gestionnaires de packages en termes de croissance. La barrière à l'entrée pour participer en publiant un package sur npm est extrêmement faible.

Permettre à plus de développeurs de participer au processus, quelle que soit la taille de la contribution, ne peut que renforcer la communauté.

#### JavaScript de libre marché

Les normes ne pourront probablement jamais suivre le rythme et la vitesse à laquelle la communauté JavaScript évolue. Ce n'est pas grave. Dans ce nouveau monde du JavaScript de libre marché, que le meilleur module gagne. Les bons modules devraient se développer à mesure qu'ils obtiennent plus de téléchargements et d'implication de la communauté, tandis que les modules non utilisés ou non soutenus disparaîtront lentement dans l'abysse virtuel. En fait, il existe des cas, comme [bluebird](https://github.com/petkaantonov/bluebird), où la bibliothèque communautaire surpassera la bibliothèque standard (voir [Pourquoi les promesses ES6 natives sont-elles plus lentes et plus gourmandes en mémoire que bluebird ?](http://programmers.stackexchange.com/questions/278778/why-are-native-es6-promises-slower-and-more-memory-intensive-than-bluebird))

Alors, avec tous ces modules, comment savoir quels modules sont sûrs à utiliser ? La vérité est que, comme pour tout logiciel open source, on ne sait jamais avec certitude. Mais voici le test que j'utilise lorsque j'inclus quelque chose de npm dans mon projet :

1. Le package est-il bien documenté ?
2. A-t-il des tests ?
3. Des gens l'utilisent-ils ?
4. La communauté a-t-elle des opinions à ce sujet (généralement, cela ne s'applique qu'aux modules plus grands) ?

#### Ce n'est pas une question de taille, mais de fonctionnalité

La beauté de notre écosystème est que le développement modulaire encapsule la responsabilité et impose une séparation des préoccupations. La taille du module devrait être sans importance pour la discussion, alors que la fonctionnalité est la clé.

La force de tout bon package hyper-modulaire est qu'il aura une interface bien définie, clairement documentée et bien testée. Ne voulons-nous pas que tout notre code soit composé de modules comme celui-ci ?

#### Les modules concernent la composition

> Pensez aux modules node comme à des blocs Lego. Vous ne vous souciez pas nécessairement des détails de leur fabrication. Tout ce que vous devez savoir, c'est comment utiliser les blocs Lego pour construire votre château Lego. — [Sindre Sorhus](https://www.freecodecamp.org/news/in-defense-of-hyper-modular-javascript-33934c79e113/undefined) de [AMA #10](https://github.com/sindresorhus/ama/issues/10#issuecomment-117766328)

En fin de compte, tout cela est une question de composition. Alors, continuons à construire des modules, utilisons ces modules pour construire d'autres modules, et ces modules pour construire des systèmes. Combinons ces systèmes pour commencer à construire des choses qui n'ont jamais été faites auparavant.

Note finale : Je devrais être clair sur le fait que je ne dis pas que **tout** devrait être un petit module. Si quoi que ce soit, j'aimerais voir plus de grandes bibliothèques opinionnées dans la communauté (un autre brain-dump pour un autre jour). En attendant, nous devrions nous rappeler que certaines des choses dont on se plaint actuellement sont les mêmes choses qui ont rendu la communauté JavaScript si formidable.

Merci.
---
title: Quelle est la différence entre un Framework et une Library ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-29T11:59:00.000Z'
originalURL: https://freecodecamp.org/news/frameworks-vs-libraries
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/cover-image-3.png
tags:
- name: Angular
  slug: angular
- name: framework
  slug: framework
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: vue
  slug: vue
seo_title: Quelle est la différence entre un Framework et une Library ?
seo_desc: 'By Yazeed Bzadough

  Buy a house, or cautiously build your own.

  What''s the difference between a framework and library? I''ve had this discussion
  with developers at work and meetups, and the core idea boils down to this.


  You tell libraries what to do, f...'
---

Par Yazeed Bzadough

Acheter une maison, ou construire la vôtre avec prudence.

Quelle est la différence entre un framework et une library ? J'ai eu cette discussion avec des développeurs au travail et lors de meetups, et l'idée centrale se résume à ceci.

> Vous dites aux libraries quoi faire, les frameworks vous disent quoi faire.

## Avantages des Frameworks
En général, un framework vous dit quoi faire. Il a une "bonne manière" de faire les choses et fournit des outils pour vous soutenir.

Deux exemples parfaits sont [Angular](https://angular.io) et [Vue](https://vuejs.org).

![angular-and-vue](https://www.freecodecamp.org/news/content/images/2019/10/angular-and-vue.png)

### Tous les outils sont ici
Ce sont des frameworks créés par des équipes dédiées, et ils sont livrés avec tout ce dont vous avez besoin pour construire des applications à grande échelle.

* Composants
* Gestion d'état basique
* Directives
* Gestion des formulaires
* Routage
* HTTP
* Tests
* Plus (libraries UI, animations, etc.)

### Guides de style officiels
Les équipes respectives fournissent ensuite des guides de style officiels, décrivant les meilleures pratiques de leur framework. Une fois que vous les avez appris, vous êtes immédiatement productif.

![one-tool-to-conquer](https://www.freecodecamp.org/news/content/images/2019/10/one-tool-to-conquer.jpeg)

### Intégration simplifiée
Si vous croyez en la structure et souhaitez investir, un framework est parfait pour votre projet. Former de nouveaux coéquipiers devient également plus facile, car ils n'ont besoin d'apprendre qu'un seul outil principal.

### Chemin de mise à jour clair
En plus de cela, votre chemin de mise à jour est très clair. Il suffit de suivre le calendrier de publication de l'équipe, de lire leurs changements majeurs et de mettre à jour lorsque vous êtes prêt.

## Inconvénients des Frameworks
Ceci est basé sur mon expérience. Je suis sûr d'avoir manqué quelque chose.

### Performance réduite (en quelque sorte)
Par nécessité, un framework est composé de _beaucoup_ de code. Plus de code signifie des temps de téléchargement plus longs et une performance réduite.

Cependant, à mesure que [les frameworks deviennent des compilateurs](https://tomdale.net/2017/09/compilers-are-the-new-frameworks/), je suspecte que cela sera moins un problème.

### Les petites applications n'en ont pas besoin
Une architecture scalable doit répondre à de nombreuses préoccupations comme nous l'avons discuté ci-dessus. Certaines applications sont si simples que l'utilisation d'un framework entier complique les choses. Vous vous retrouvez avec des tonnes de code standard sans beaucoup de bénéfices.

### Aller contre le framework peut être difficile
Cela s'est manifesté lors de mon premier emploi après l'université, où nous avons essayé de compiler du contenu en dehors de la connaissance d'Angular. Le résultat n'était pas joli, mais nous avons accompli la tâche après quelques essais et erreurs, et beaucoup de bleues.

![going-against-frameworks](https://www.freecodecamp.org/news/content/images/2019/10/going-against-frameworks.jpeg)

Bien que j'ai entendu dire que Vue vous permet de l'adopter de manière incrémentielle dans votre application existante. Cela semble prometteur !

### C'est beaucoup à apprendre
Ce point s'applique à toute architecture, cependant. Quel que soit l'outil (ou les outils) que vous utilisez, apprendre tout cela prend du temps. C'est soit un gros outil, soit plusieurs petits.

![almost-understood](https://www.freecodecamp.org/news/content/images/2019/10/almost-understood.jpeg)

### Vous devenez trop à l'aise
Cela s'applique à tout dans la vie – parfois nous devenons trop à l'aise à faire les choses d'une certaine manière. Cela dépend totalement de vos objectifs de carrière, cependant. Peut-être que cet outil vous aide à garder un emploi stable ou à gérer une entreprise efficace en construisant des applications. Si c'est ce que vous voulez, continuez à le faire !

Mais si vous êtes comme beaucoup d'entre nous, la même technologie tous les jours devient un peu monotone. Expérimenter avec d'autres frameworks et libraries est la clé pour garder vos compétences aiguisées.

## Avantages des Libraries
En opposition directe aux frameworks, les libraries sont des utilitaires construits pour un but unique.

* [React](https://reactjs.org) crée des UIs
* [Redux](http://redux.js.org) fournit une gestion d'état
* [JQuery](https://jquery.com) fournit une manipulation DOM multi-navigateurs

La liste continue. Zoomons sur React. Que fait-il ?

![react-logo-small](https://www.freecodecamp.org/news/content/images/2019/10/react-logo-small.png)

> Une bibliothèque JavaScript pour construire des interfaces utilisateur - [Site officiel de React](https://reactjs.org)

### Focus unique
C'est _tout ce qu'il fait_. Leurs guides vous montrent comment utiliser React et c'est principalement tout. L'équipe ne désigne pas officiellement de libraries pour la gestion d'état globale, le routage, HTTP, les services ou les formulaires.

Et c'est leur choix de conception ! C'est une excellente position selon ce que vous cherchez.

### Vous êtes aux commandes
Une library est à 100 % sous votre contrôle. Vous déterminez comment elle est utilisée, et vous naviguez en douceur après avoir investi du temps pour l'apprendre.

![learned-a-lib-quickly](https://www.freecodecamp.org/news/content/images/2019/10/learned-a-lib-quickly.jpeg)

### Ajoutez seulement ce dont vous avez besoin
Si votre application est petite, une seule library peut suffire ! Pas besoin de compliquer les choses. À mesure que l'application grandit, vous pouvez mélanger et assortir des libraries pour construire votre propre architecture. C'est une excellente expérience d'apprentissage !

### Apprenez de nombreux outils différents
Et en parlant de cela, l'utilisation de nombreuses libraries différentes gardera vos compétences JavaScript bien aiguisées. Vous serez toujours en train de lire de la documentation, d'essayer de nouvelles choses et d'élargir vos horizons techniques.

Ce n'est pas tout parfait cependant...

## Inconvénients des Libraries
### Une architecture personnalisée peut ruiner votre application
Les architectures personnalisées sont amusantes au début, mais peuvent être très coûteuses à long terme. Je conseille une extrême prudence si c'est votre première fois à en construire une.

Une bonne architecture augmente la productivité des développeurs et minimise la douleur d'ajouter, de modifier et de supprimer du code.

![when-architecture-scales](https://www.freecodecamp.org/news/content/images/2019/10/when-architecture-scales.jpeg)

Une mauvaise architecture cause de la peur et de la souffrance chaque fois que quelqu'un la touche.

![refactor-or-redo](https://www.freecodecamp.org/news/content/images/2019/10/refactor-or-redo.jpeg)

Les gens choisissent Angular et Vue parce qu'ils ne veulent pas risquer du temps et de l'argent à construire leurs propres règles. Ils apprennent simplement les règles du framework et se concentrent sur le jeu.

Alors que dans le monde React, deux applications à grande échelle varieront dans leur structure. Tout dépend de ce que l'équipe a jugé meilleur.

### Paralysie par l'analyse
Parfois, trop d'options est une mauvaise chose, et nous sommes frappés par la redoutable [paralysie par l'analyse](https://en.wikipedia.org/wiki/Analysis_paralysis). Au lieu de choisir une library et d'avancer, nous passons d'innombrables heures à comparer différentes libraries qui font à peu près la même chose.

![analyze-all-the-libs](https://www.freecodecamp.org/news/content/images/2019/10/analyze-all-the-libs.jpeg)

### C'est toujours beaucoup à apprendre
Framework ou non, une grande application prend toujours du temps à comprendre. C'est une autre raison pour laquelle une architecture solide est importante, car elle facilitera la courbe d'apprentissage.

### Chemin de mise à jour potentiellement chaotique
Si je gagnais de l'argent chaque fois que deux libraries dans mon `package.json` n'étaient pas compatibles après une mise à jour, je serais à la retraite. Assez dit.

![one-does-not-simply-upgrade](https://www.freecodecamp.org/news/content/images/2019/10/one-does-not-simply-upgrade.jpeg)

## Vous voulez un coaching gratuit ?
Si vous souhaitez planifier un appel gratuit pour discuter du développement Front-End, des entretiens, de la carrière ou de toute autre chose [suivez-moi sur Twitter et envoyez-moi un DM](https://twitter.com/yazeedBee).

Après cela, si vous appréciez notre première rencontre, nous pouvons discuter d'un coaching continu pour vous aider à atteindre vos objectifs de développement Front-End !

## Merci d'avoir lu
Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">https://yazeedb.com !</a>

À la prochaine !
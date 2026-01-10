---
title: Quels projets ont besoin de React ? Tous !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-19T03:47:37.000Z'
originalURL: https://freecodecamp.org/news/which-projects-need-react-all-of-them-e7ccb6629ba7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oBgj1FMn9GrUBIxPh_k2HQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Quels projets ont besoin de React ? Tous !
seo_desc: 'By Sacha Greif

  When does a project need React? That’s the question Chris Coyier addressed in a
  recent blog post. I’m a big fan of Chris’ writing, so I was curious to see what
  he had to say.

  In a nutshell, Chris puts forward a series of good and bad r...'
---

Par Sacha Greif

Quand un projet a-t-il besoin de React ? C'est la question que Chris Coyier a abordée dans [un récent article de blog](https://css-tricks.com/project-need-react/). Je suis un grand fan des écrits de Chris, alors j'étais curieux de voir ce qu'il avait à dire.

En résumé, Chris avance une série de bonnes et de mauvaises raisons pour lesquelles on pourrait vouloir utiliser React (ou d'autres bibliothèques JavaScript modernes similaires) sur un projet. Pourtant, bien que je ne sois pas en désaccord avec ses arguments, je me retrouve encore à tirer une conclusion différente.

Alors aujourd'hui, je suis là pour soutenir que la réponse à « Quand un projet a-t-il besoin de React ? » n'est pas « ça dépend. » C'est « **à chaque fois.** »

#### React vs Vue vs Angular vs…

D'abord, clarifions quelque chose : dans son article, Chris a choisi React comme représentant des « bibliothèques front-end » en général, et je ferai de même ici. De plus, React est ce que je connais le mieux grâce à mon travail en cours sur [VulcanJS](http://vulcanjs.org), un framework React et GraphQL.

Cela dit, mes arguments devraient s'appliquer tout aussi bien à toute autre bibliothèque offrant les mêmes fonctionnalités que React.

### Le Pouvoir du Marteau

> « Quand on n'a qu'un marteau, tout ressemble à un clou. »

Ce proverbe a longtemps été utilisé pour condamner quiconque essaie d'appliquer une approche systématique unique à tous les problèmes.

Mais supposons un instant que vous viviez dans un monde rempli de clous (aussi inconfortable que cela puisse paraître), et que votre marteau fidèle puisse résoudre tous les problèmes que vous rencontrez.

Considérez simplement les avantages de pouvoir **réutiliser le même outil à chaque fois** :

* Pas de temps perdu à décider quel outil utiliser.
* Moins de temps passé à apprendre de nouveaux outils.
* Plus de temps pour mieux maîtriser l'outil de votre choix.

Alors, React est-il cet outil ? Je pense que oui !

### Le Spectre de la Complexité

D'abord, abordons l'argument le plus courant contre l'approche « React pour tout ! ». Je citerai directement Chris :

> « Un blog, par exemple, n'a _probablement_ aucun des problèmes et ne correspond à aucun des scénarios qui feraient de React un bon choix. Et parce que ce n'est pas un bon choix, c'est probablement un _mauvais_ choix, car il introduit une technologie compliquée et des dépendances pour quelque chose qui n'en a pas besoin. »

C'est juste. Un simple blog n'a pas _besoin_ de React. Après tout, même si vous avez besoin d'un peu de JavaScript pour connecter un formulaire d'inscription à une newsletter, vous pouvez simplement utiliser jQuery.

Quoi ? Vous devez utiliser ce formulaire à plusieurs endroits sur différentes pages ? Et ne le montrer que sous certaines conditions ? Et l'animer aussi ? Attendez, attendez…

Le point que j'essaie de faire avec ce petit scénario est que la complexité n'est pas un choix binaire tout ou rien. Au lieu de cela, les sites web modernes vivent sur un spectre continu qui va de la page statique à l'application riche monopage.

Donc, peut-être que votre projet est confortablement niché à l'extrémité « simple » du spectre _maintenant_, mais qu'en sera-t-il dans six mois ? N'est-il pas préférable de choisir une technologie qui vous laisse de la place pour grandir, plutôt qu'une qui vous enferme dans de mauvaises pratiques ?

### Les Avantages de React

> « L'optimisation prématurée est la racine de tous les maux » — Donald Knuth

C'est un autre dicton populaire parmi les programmeurs. Après tout, qui a besoin de marteaux et de clous quand du ruban adhésif fait très bien l'affaire !

Mais cela suppose que l'« optimisation prématurée » est un processus long et ardu avec peu d'avantages. Et je ne pense pas que cela s'applique à React.

Bien que React puisse prendre un certain temps pour s'y habituer, une fois que vous avez appris [ses concepts de base](https://medium.freecodecamp.com/the-5-things-you-need-to-know-to-understand-react-a1dbd5d114a3), vous serez tout aussi productif qu'avec les outils front-end classiques.

Peut-être même plus, car React exploite le concept extrêmement puissant de **composants**. Tout comme CSS vous encourage à penser en termes de classes et de styles réutilisables, React vous pousse vers une architecture front-end flexible et modulaire qui présente des avantages pour chaque cas d'utilisation, de la simple page d'accueil statique au tableau de bord interactif back-end.

### JavaScript, JavaScript Partout

Nous vivons dans un monde JavaScript. Ou, comme le dit Chris :

> « Vous avez Node.js côté serveur. Il y a des tonnes de projets qui retirent CSS de l'équation et gèrent les styles via JavaScript. Et avec React, votre HTML est aussi en JavaScript.

> « Tout en JavaScript ! Vive JavaScript ! »

Chris n'est pas tout à fait convaincu, mais moi si. JavaScript en lui-même n'est pas nécessairement parfait, mais avoir accès à tout l'écosystème moderne npm est incroyable.

Installer un plugin jQuery impliquait autrefois de trouver sa page d'accueil, de le télécharger, de le copier dans votre répertoire de projet, d'ajouter une balise `<script>`, et ensuite, espérons-le, de se souvenir de vérifier toutes les quelques semaines pour de nouvelles versions. De nos jours, installer le même plugin en tant que package React est simplement une question de commande `npm install`.

Et avec de nouvelles bibliothèques comme [styled-components](https://medium.freecodecamp.com/a-5-minute-intro-to-styled-components-41f40eb7cd55), même CSS est maintenant traîné, kickant et hurlant, vers le futur.

Croyez-moi, une fois que vous vous habituez à ce monde où tout parle la même langue, il est vraiment difficile de revenir à l'ancienne façon de faire les choses.

### Mais Qu'en est-il des Utilisateurs !

Je sais ce que vous pensez : jusqu'à présent, j'ai essayé de vous vendre les avantages de React pour les développeurs, mais j'ai soigneusement évité toute mention de l'expérience utilisateur finale.

Et cela reste l'argument clé contre les bibliothèques modernes : des sites lents, gonflés de JavaScript, qui mettent des âges à charger une de ces publicités « un truc bizarre ».

Sauf voici un petit secret : **vous pouvez obtenir tous les avantages de React sans aucun JavaScript du tout** !

Ce dont je parle ici, c'est de rendre React **côté serveur**. En fait, des outils comme [Gatsby](https://github.com/gatsbyjs/gatsby) (et bientôt, [Next.js](https://github.com/zeit/next.js/)) vous permettent même de compiler des composants React en fichiers HTML statiques que vous pouvez héberger sur, disons, GitHub pages.

Par exemple, [mon propre site personnel](http://sachagreif.com/) est une application React générée par Gatsby qui ne charge aucun JavaScript du tout (au-delà d'un extrait Google Analytics). J'obtiens tous les avantages de l'utilisation de React en développement (tout-JavaScript, accès à l'écosystème npm, styled-components, etc.) mais j'aboutis à un produit final 100% HTML et CSS.

### Conclusion

Pour résumer, voici les quatre raisons pour lesquelles je pense que React est un choix valable pour _n'importe quel_ projet :

* Il est vraiment difficile de garantir que vous n'aurez _jamais_ besoin de fonctionnalités interactives comme des onglets, des formulaires — même pour les sites les plus simples.
* L'approche basée sur les composants de React a de grands avantages — même pour les sites statiques basés sur du contenu.
* L'accès à l'écosystème JavaScript moderne est un énorme avantage.
* Les outils modernes de rendu côté serveur éliminent pour votre utilisateur final tous les inconvénients de l'utilisation de React.

Alors, qu'en pensez-vous, Chris ? Ai-je fait un cas convaincant ? Ou des doutes subsistent-ils dans votre esprit ?

Et vous, cher lecteur ? Que vous pensiez comme Chris que chaque outil a son utilité, ou que vous soyez d'accord avec moi que le Temps du Marteau est à portée de main, faites-le nous savoir dans les commentaires !

_Cet article a été initialement publié sur [CSS Tricks](https://css-tricks.com/projects-need-react/).
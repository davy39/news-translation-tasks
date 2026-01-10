---
title: J'ai enfin compris les outils de build front-end. Vous pouvez aussi.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-16T16:36:34.000Z'
originalURL: https://freecodecamp.org/news/making-sense-of-front-end-build-tools-3a1b3a87043b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*L4TYDiuYB5-EK8SG2RjHHQ.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: Web Development
  slug: web-development
seo_title: J'ai enfin compris les outils de build front-end. Vous pouvez aussi.
seo_desc: 'By Roneesh

  Front end build tools can be confusing even to experienced developers like me. The
  solution is to understand how they work — and work together — on a conceptual level.

  This article presents my opinionated approach to making sense of front ...'
---

Par Roneesh

Les outils de build front-end peuvent être déroutants même pour les développeurs expérimentés comme moi. La solution est de comprendre comment ils fonctionnent — et comment ils fonctionnent ensemble — à un niveau conceptuel.

Cet article présente mon approche subjective pour comprendre les outils de build front-end. Au lieu de plonger dans le code, je vais vous expliquer mon modèle mental de la façon dont ces outils fonctionnent et ce qu'ils accomplissent.

### Ne soyez pas intimidé par l'état de l'art

Node, NPM, Grunt, Gulp, Bower, Webpack, Browserify, Yeoman, Brunch... il existe tellement d'outils de build front-end qu'il peut sembler impossible de suivre.

La clé est de ne pas se laisser intimider. Tous ces projets sont conçus pour faciliter votre vie.

Pour comprendre le quoi, le pourquoi et le comment de ces outils, vous devez simplement saisir quelques concepts.

#### Concept #1 — La dichotomie centrale des outils de build est « installer vs. faire »

Les outils de build font deux choses :

1. Installer des choses
2. Faire des choses

La première question à se poser lorsqu'on est confronté à un nouvel outil de build est : « Cet outil est-il destiné à installer des choses pour moi, ou à faire des choses pour moi ? »

Les outils « d'installation » comme npm, Bower et Yeoman peuvent installer à peu près n'importe quoi. Ils peuvent installer des bibliothèques front-end comme Angular.js ou React.js. Ils peuvent installer des serveurs pour votre environnement de développement. Ils peuvent installer des bibliothèques de test. Ils vous aident même à installer d'autres outils de build front-end.

En résumé, ils installent à peu près tout ce qui est lié au code et que vous pouvez imaginer.

Les outils « de faire » comme Grunt, Webpack, Require.js, Brunch et Gulp sont beaucoup plus compliqués. Le but des outils « de faire » est d'automatiser toutes les tâches fastidieuses et sujettes aux erreurs dans le développement web. Les choses qu'ils font sont parfois appelées « tâches ».

Pour effectuer ces « tâches », ils utilisent souvent leur propre écosystème de packages et de plugins. Chaque outil écrit des tâches de différentes manières. Ces outils ne font pas tous la même chose. Certains outils « de faire » essaient de gérer n'importe quelle tâche que vous leur lancez (Grunt, Gulp, etc). D'autres se concentrent sur une seule chose, comme la gestion des dépendances JavaScript (Browserify, Require.js, etc).

Parfois, vous finissez par utiliser plusieurs de ces outils dans le même projet.

Voici une courte liste de « tâches » que j'ai automatisées avec ces outils « de faire » :

1. Remplacer une chaîne de texte dans un fichier
2. Créer des dossiers et déplacer des fichiers dans ces dossiers
3. Exécuter mes tests unitaires avec une seule commande
4. Rafraîchir mon navigateur lorsque je sauvegarde un fichier
5. Combiner tous mes fichiers JavaScript en un seul, et tous mes fichiers CSS en un seul
6. Minifier mes fichiers JavaScript et CSS concaténés
7. Modifier l'emplacement des balises <script> sur une page html

Une fois que vous comprenez que les outils installent des choses ou font des choses, les catégoriser devient beaucoup plus facile :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0MT3awKHigXswTwawZo_cA.png)
_Outils de build classés selon qu'ils installent principalement des choses ou en font_

#### Concept #2 — Le grand-parent de tous les outils de build est Node et npm

Node et npm installent et exécutent tous ces outils de build, donc il y a toujours une trace d'eux dans votre projet. Pour cette raison, de nombreux développeurs essaient d'utiliser ces deux outils autant que possible avant de recourir à l'installation d'un outil supplémentaire.

Node et NPM entrent dans notre dichotomie « build » et « do ». Node est l'outil « do », et npm est l'outil « install ».

npm peut installer des bibliothèques comme Angular.js ou React.js. Il peut également installer un serveur pour exécuter votre application localement pour le développement. Il peut même installer des outils pour faire des choses comme minifier votre code.

Node, en revanche, « fait » des choses pour vous, comme exécuter des fichiers JavaScript, des serveurs, et bien plus encore.

Si vous avez besoin d'un point de départ pour apprendre, commencez par Node+npm, et restez là un moment. Lorsque votre projet devient suffisamment grand, vous atteindrez les limites de ce que Node et npm peuvent automatiser pour vous. À ce moment-là, vous pourrez incorporer organiquement un autre outil de build.

#### Concept #3 — Un build est simplement une version de votre application prête pour la production

Les développeurs divisent souvent JavaScript et CSS en fichiers séparés. Les fichiers séparés vous permettent de vous concentrer sur l'écriture de morceaux de code plus modulaires qui font une seule chose. Les fichiers qui font une seule chose diminuent votre charge cognitive. (Si vous pensez que les fichiers séparés sont plus déroutants qu'un seul grand fichier, essayez de travailler dans un fichier de 5000 lignes, et vous changerez rapidement d'avis 😉)

Mais lorsqu'il est temps de passer votre application en production, avoir plusieurs fichiers JavaScript ou CSS n'est pas idéal. Lorsqu'un utilisateur visite votre site, chacun de vos fichiers nécessitera une requête HTTP supplémentaire, rendant votre site plus lent à charger.

Pour remédier à cela, vous pouvez créer un « build » de votre application, qui fusionne tous vos fichiers CSS en un seul fichier, et fait de même avec votre JavaScript. Ainsi, vous minimisez le nombre et la taille des fichiers que l'utilisateur reçoit. Pour créer ce « build », vous utilisez un « outil de build ».

Ci-dessous, une capture d'écran d'une application en développement. Remarquez comment elle a 5 balises <script> et 3 balises <link> ? Si vous regardez sur le côté gauche, remarquez que le dossier DEVELOPMENT contient 10 fichiers à l'intérieur ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dxaal-bYJ8mG1fFLlaQUEg.png)
_Votre application en développement_

Et ci-dessous, la même application après qu'un outil de build ait fait son travail.

Remarquez comment nous n'avons qu'une seule balise script et une seule balise link ? Et maintenant le dossier PRODUCTION n'a que 4 fichiers, contre les 10 du dossier DEVELOPMENT.

L'application est ligne par ligne la même. Nous l'avons simplement compactée en un petit package bien rangé que nous appelons un « build ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*nUhYk9Mot6c6khOJTC4g1w.png)
_Votre application dans sa forme de build_

Vous pourriez vous demander pourquoi un build en vaut la peine, s'il ne fait que sauver à vos utilisateurs quelques millisecondes de temps de chargement. Eh bien, si vous faites un site juste pour vous-même ou pour quelques autres personnes, vous n'avez pas besoin de vous en soucier. Générer un build de votre projet n'est nécessaire que pour les sites à fort trafic (ou les sites que vous espérez être bientôt à fort trafic 😉).

Si vous apprenez simplement le développement, ou si vous ne faites que des sites avec très peu de trafic, générer un build peut ne pas valoir votre temps.

#### Concept #4 — Les lignes entre « installer » et « faire » peuvent être floues

Aucun outil ne fait uniquement l'un ou l'autre. Ils font tous un mélange de « installer » et de « faire ». Mais généralement, un outil tend à faire plus de l'un que de l'autre.

Parfois, un outil « d'installation » exécutera des fichiers. npm le fait souvent. npm peut [exécuter des commandes et des scripts également](https://medium.freecodecamp.com/why-i-left-gulp-and-grunt-for-npm-scripts-3d6853dd22b8) — pas seulement installer des fichiers. Un outil comme Yeoman installe des applications boilerplate pré-construites sur votre ordinateur, mais il génère également dynamiquement de nouveaux fichiers selon les besoins, brouillant la ligne entre installer et faire.

#### Concept #5 — Il n'y a pas une seule combinaison correcte d'outils

La combinaison d'outils que vous utilisez peut être complètement à vous.

Vous pouvez choisir de ne pas utiliser d'outils du tout. Gardez simplement à l'esprit que copier, coller, minifier, démarrer des serveurs, et tout le reste peut rapidement devenir accablant.

Ou vous pouvez simplement utiliser Node et npm ensemble sans outils supplémentaires. C'est idéal pour les débutants, mais à mesure que votre projet grandit, cela peut commencer à sembler trop manuel.

Ou vous pouvez choisir d'utiliser quelques autres outils en plus de Node et npm dans votre projet. Ainsi, votre application utilisera Node+npm comme base, et peut-être Grunt+Bower ou Webpack ou Gulp+Bower.

L'utilisation d'une combinaison d'outils comme ceux-ci en plus de Node+npm vous permet d'automatiser de nombreuses tâches dans votre projet. Le prix à payer est que ces outils ont une courbe d'apprentissage abrupte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y5gyN19hMnG91oVq51kKAw.png)
_Outils de build par ordre de complexité croissante, mais de fastidiosité décroissante_

#### Concept #6 — Les outils de build ont une courbe d'apprentissage abrupte, donc n'apprenez que ce qui est nécessaire

Construire une application est déjà assez difficile. Vous pourriez travailler avec un nouveau langage ou un nouveau framework. Ou vous pourriez avoir une logique métier vraiment complexe. Donc, incorporer un outil de build peut ajouter une couche supplémentaire de complexité à votre projet. Cela est particulièrement vrai lorsqu'il s'agit d'un projet où quelqu'un d'autre a écrit le code associé à l'outil de build.

Mon conseil est de n'apprendre que ce dont vous avez besoin pour faire votre travail et rien d'autre.

La meilleure façon d'apprendre de nouvelles choses est lorsque vous avez une tâche réelle à accomplir. Par exemple, n'apprenez pas à copier des fichiers avec Grunt pour le plaisir. Attendez plutôt que votre projet en ait vraiment besoin, puis trouvez comment faire.

Rappelez-vous : une complexité prématurée vous ralentira.

#### Concept #7 — Tous les outils de build partagent le même objectif : vous rendre heureux en automatisant de nombreuses tâches fastidieuses

Vous utilisez votre outil de build à son plein potentiel lorsque vous atteignez ce que j'appelle le « nirvana de l'outil de build ». C'est lorsque, après avoir sauvegardé un fichier ou exécuté une seule commande, des tonnes de tâches se font « automagiquement » pour vous.

Si votre outil de build nécessite toujours que vous déplaciez manuellement des fichiers, changiez des valeurs ou exécutiez des commandes pour obtenir un nouveau build, alors vous n'avez pas encore atteint le nirvana de l'outil de build.

L'un des plus grands avantages des outils de build est que, simplement en sauvegardant un fichier, vous pouvez déclencher un nouveau build de votre application et l'envoyer à votre navigateur. Cela peut considérablement accélérer votre flux de travail de développement front-end.

Alors, combien d'efforts devez-vous mettre dans la configuration et la mise en place de votre outil de build ? Simple : arrêtez lorsque vous êtes satisfait de ce qu'il fait pour vous.

#### Concept #8 — Ce n'est pas juste vous. La documentation est souvent terrible.

Ce n'est pas vous, je vous le promets. Pour beaucoup de ces outils, la documentation est assez insuffisante. Parfois, il est difficile de comprendre comment effectuer des tâches de base.

Gardez à l'esprit qu'il existe très peu de recettes prédéfinies pour les outils de build. Vous verrez des gens obtenir les mêmes résultats de manières complètement différentes — parfois toutes en réponse à la même question sur StackOverflow !

Bien que cela soit ennuyeux, cela vous présente également une opportunité de faire travailler vos muscles de codeur et de mettre en œuvre quelque chose de créatif.

Après tout, n'est-ce pas pour cela que nous faisons cela ?

_Merci d'avoir lu ceci ! J'espère que ces quelques points rendent l'approche des outils de build moins confuse. Si ce n'est pas le cas, je suis heureux de clarifier toute question (ou de corriger toute erreur que vous trouvez ici), tweetez-moi @[Roneesh](https://www.freecodecamp.org/news/making-sense-of-front-end-build-tools-3a1b3a87043b/undefined)!_

**Et bien sûr, si vous avez aimé ce que vous avez lu, n'oubliez pas de le ❤️ ci-dessous et de le partager avec vos amis. En tant qu'écrivain, cela signifie le monde pour moi !**
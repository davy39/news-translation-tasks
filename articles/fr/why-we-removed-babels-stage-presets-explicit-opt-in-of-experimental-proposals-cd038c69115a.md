---
title: 'Pourquoi nous avons supprimé les préréglages de Stage de Babel : Opt-in explicite
  des propositions expérimentales'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-30T23:12:26.000Z'
originalURL: https://freecodecamp.org/news/why-we-removed-babels-stage-presets-explicit-opt-in-of-experimental-proposals-cd038c69115a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XmHUL5DeySv_dGmvbPqdDQ.png
tags:
- name: Babel
  slug: babel
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: tc39
  slug: tc39
- name: technology
  slug: technology
seo_title: 'Pourquoi nous avons supprimé les préréglages de Stage de Babel : Opt-in
  explicite des propositions expérimentales'
seo_desc: 'By Henry Zhu

  Moving forward with v7, we’ve decided it’s best to stop publishing the Stage presets
  in Babel (for example,@babel/preset-stage-0).

  We didn’t make this decision lightly, and wanted to show the context behind the
  interplay between TC39, Ba...'
---

Par Henry Zhu

En avançant avec la v7, nous avons décidé qu'il était préférable d'arrêter de publier les préréglages de Stage dans Babel (par exemple, `@babel/preset-stage-0`).

Nous n'avons pas pris cette décision à la légère, et nous voulions montrer le contexte derrière l'interaction entre TC39, Babel et la communauté.

### Un peu d'histoire

Un préréglage Babel est une liste partageable de plugins.

Les [préréglages officiels de Stage de Babel](https://babeljs.io/docs/en/next/presets) suivaient le [processus de staging TC39](https://tc39.github.io/process-document/) pour les nouvelles [propositions de syntaxe](https://github.com/tc39/proposals) en JavaScript.

Chaque préréglage (ex. `stage-3`, `stage-2`, etc.) incluait tous les plugins pour ce stage particulier et ceux au-dessus. Par exemple, `stage-2` incluait `stage-3`, et ainsi de suite.

Cela permettait aux utilisateurs qui voulaient utiliser une syntaxe expérimentale de simplement ajouter le préréglage, au lieu de devoir configurer/installer chaque plugin individuellement.

Nous avons en fait [ajouté](https://github.com/babel/babel/pull/2649) les préréglages de Stage peu après la sortie de la v6 de Babel (c'était auparavant un flag de configuration dans la v5). Ci-dessous est un exemple plus ancien.

### Problèmes

Ces préréglages étaient un moyen pratique d'utiliser ce que nous voulions tous : le nouveau, brillant, futur "encore à déterminer" de JavaScript.

En regardant en arrière, cela a très bien fonctionné ! (Peut-être trop bien ?)

### Trop bien fait ?

Des langages comme [CoffeeScript](https://coffeescript.org/) et des outils comme [Traceur](https://github.com/google/traceur-compiler) ont aidé à établir l'idée de compiler JavaScript. Babel a rendu encore plus facile l'utilisation de la nouvelle/syntaxe future et l'intégration avec les outils existants. Les attentes sont passées du scepticisme et de l'inquiétude à une adoption complète de l'expérimental.

Nous ne serions probablement pas là où nous en sommes sans l'adoption généralisée de compilateurs comme Babel : cela a accéléré l'utilisation (et l'enseignement) de ES2015 à un public beaucoup plus large. La croissance de React a encore alimenté l'utilisation, car sa syntaxe JSX, les propriétés de classe et la décomposition/rassemblement d'objets ont conduit les gens à en savoir un peu plus sur ces propositions de syntaxe.

Babel est devenu une configuration unique pour les gens, à ne plus jamais y penser. Il est devenu l'infrastructure sous-jacente, cachée derrière d'autres outils jusqu'à ce qu'il y ait une `SyntaxError`, des problèmes de dépendance ou des problèmes d'intégration. Il suffit d'utiliser `stage-0`.

C'était génial à voir à certains égards, car cela signifiait que ces idées étaient testées dans la nature, même dans des environnements de production. Cependant, cela signifiait également que de nombreuses entreprises, outils et personnes rencontreraient des problèmes si une proposition changeait de manière significative (ou même était abandonnée).

### Allers-retours

Au fil des ans, nous avons soulevé de nombreuses questions pour discuter de ce qu'il fallait faire avec les préréglages de Stage dans [#4914](https://github.com/babel/babel/issues/4914), [#4955](https://github.com/babel/babel/issues/4955), [#7770](https://github.com/babel/babel/issues/7770). J'ai même écrit dans un ancien article sur Babel 7.0 que nous **ne supprimions pas** [les préréglages](https://babeljs.io/blog/2017/12/27/nearing-the-7.0-release) ?.

Cependant, nous avons constaté que le maintien des préréglages de Stage entraînerait des problèmes même pour Babel lui-même :

* C'était un problème courant de demander quelque chose comme : ["Quels préréglages sont nécessaires pour utiliser les fonctions asynchrones ?"](https://github.com/babel/babel/issues/2948) Il n'était pas clair pour les gens de savoir exactement ce que `stage-0` signifiait, et peu de gens regarderaient son `package.json` ou sa source.
* Supprimer un plugin de proposition en Stage 3 (une fois qu'il passe à Stage 4) est en fait un changement cassant. Ce problème est exacerbé lorsque vous essayez d'utiliser `@babel/preset-env` pour ne pas compiler une proposition supportée nativement.

### "ES7 Decorators"

Une partie du problème est précisément autour de la nomination des choses, et comme nous l'entendons souvent, nommer les choses est difficile.

Il y avait beaucoup de noms pour ES6 lui-même : Harmony, ES Next, ES6, ES2015. Lorsque les gens entendent parler de nouvelles idées, il est logique de simplement prendre le dernier numéro et d'attacher le nom à celui-ci.

Il est tout à fait compréhensible que cela se produise sans s'en rendre compte, mais continuer à le faire crée des attentes différentes quant à la manière dont le langage évolue. Ce n'est pas quelque chose dont il faut se sentir coupable — nous apprenons en tant que communauté et nous nous rappelons mutuellement comment fonctionne JavaScript.

[Jay Phelps](https://twitter.com/_jayphelps/status/779770321003962369) a écrit un bel [article](https://medium.com/@jayphelps/please-stop-referring-to-proposed-javascript-features-as-es7-cad29f9dcc4b) sur ce sujet. Il explique qu'il serait préférable de les appeler par le "Stage" où ils se trouvent actuellement : "Stage 2 Decorators", ou simplement "Decorators Proposal".

La raison est que dire "ES7 Decorators" suppose que Decorators est attendu dans ES7. J'ai mentionné cela dans mon [dernier article concernant la compilation de node_modules](https://babeljs.io/blog/2018/06/26/on-consuming-and-publishing-es2015+-packages#staging-process), mais être dans un Stage particulier ne garantit pas grand-chose : une proposition peut stagner, reculer, ou être complètement supprimée.

Nous voulions souligner ce fait lorsque nous avons décidé de [changer les noms](https://babeljs.io/docs/en/next/v7-migration#switch-to-proposal-for-tc39-proposals-blog-2017-12-27-nearing-the-70-releasehtml-renames-proposal) des plugins de proposition de `@babel/plugin-transform-` à `@babel/plugin-proposal-`.

### BabelScript

Avoir des préréglages pour des propositions si tôt dans le processus peut impliquer que ces propositions sont garanties de progresser ou d'avoir une implémentation stable.

[TC39](https://tc39.github.io/process-document/) incite à la prudence lors de l'utilisation de propositions de Stage 2 ou inférieures, car cela pourrait entraîner une pression involontaire de la communauté pour maintenir l'implémentation telle quelle au lieu de l'améliorer par crainte de casser le code existant ou la fragmentation de l'écosystème (par exemple, utiliser un symbole différent comme `#` au lieu de `@` pour les décorateurs).

Les gens plaisantent en disant que les développeurs qui utilisent Babel utilisent "BabelScript" au lieu de JavaScript, impliquant que, d'une certaine manière, une fois qu'un plugin Babel est créé pour une certaine fonctionnalité, cela doit signifier qu'elle est "fixée" ou officiellement partie du langage déjà (ce qui n'est pas vrai). Pour certains, la première pensée des gens lorsqu'ils voient une nouvelle syntaxe/idée (Stage "-1") est de savoir s'il existe un plugin Babel pour celle-ci.

### Définir les attentes

Après que des compilateurs comme Babel ont rendu courante la pratique pour les gens d'écrire en ES2015, il était naturel pour les développeurs de vouloir essayer des "fonctionnalités" encore plus nouvelles et expérimentales. La manière dont cela fonctionnait dans Babel était d'utiliser le flag `stage` dans les versions précédentes ou les préréglages `stage-x`.

Étant le moyen le plus pratique de s'inscrire à toute nouvelle fonctionnalité, cela est rapidement devenu la valeur par défaut pour les gens lors de la configuration de Babel (même si dans Babel v6, cela a été modifié pour ne rien faire par défaut, ce qui a provoqué de nombreuses plaintes).

Il y a eu beaucoup de bonnes discussions même il y a des années, mais ce n'était pas la chose la plus facile à naviguer : nous ne voulions pas pénaliser les utilisateurs qui comprenaient les compromis en mettant des `console.warn` lors de son utilisation, et ne pas avoir l'option du tout semblait déraisonnable à l'époque.

S'inscrire aveuglément à Stage 0 (que nous avions par défaut) ou que les gens choisissent de le faire semble dangereux, mais aussi ne jamais utiliser de propositions est trop prudent. Idéalement, tout le monde devrait pouvoir prendre une décision éclairée sur les types de fonctionnalités qui semblent raisonnables pour eux et les utiliser judicieusement, quel que soit le stage dans lequel ils se trouvent. [Mike Pennisi](https://twitter.com/jugglinmike) a écrit [un excellent article](https://bocoup.com/blog/javascript-developers-watch-your-language) sur ces préoccupations.

Ce n'est pas notre intention de menacer, de précipiter ou de forcer des choses spécifiques dans l'écosystème ou JavaScript, mais de maintenir fidèlement l'implémentation/discussions autour des nouvelles idées.

### Autres considérations

Nous aurions également pu essayer de :

* [Renommer les préréglages](https://github.com/babel/babel/issues/4914) pour mieux signifier le niveau de stabilité (ne résout pas le problème de versionnage)
* Mieux gérer les versions : versionner indépendamment les préréglages et les mettre à jour immédiatement si nécessaire, peut-être utiliser `0.x`
* Avertir/Erreur pour les anciennes versions obsolètes des préréglages

En fin de compte, les gens devraient toujours chercher quelles propositions sont à quel Stage pour savoir lesquelles utiliser si nous gardions les Stages.

### Pourquoi maintenant ?

Pourquoi ne pas l'avoir supprimé plus tôt ? Les préréglages de Stage font partie de Babel depuis des années, et il y avait des préoccupations concernant l'ajout de plus de "complexité" à l'utilisation de Babel. Beaucoup d'outils, de documentation, d'articles et de connaissances ont été construits autour des préréglages de Stage. Auparavant, nous pensions qu'il était préférable de maintenir officiellement les préréglages puisque quelqu'un d'autre les créerait (et le fera) inévitablement.

Nous essayons de déterminer le bon niveau de feedback : si seul le comité décide de ce qui entre dans le langage, cela peut conduire à des fonctionnalités bien spécifiées mais non nécessaires. Mais si la communauté s'attend à ce que les propositions expérimentales en cours soient considérées comme stables ou acceptables à utiliser en production sans conséquence, alors nous aurons d'autres problèmes. Nous voulons tous avancer et procéder avec intention : sans précipitation, mais sans être trop prudents. Babel est le bon endroit pour faire cette expérimentation, mais savoir où se trouvent les limites est nécessaire.

Supprimer les préréglages serait considéré comme une "fonctionnalité", puisque cela signifie que quelqu'un devrait prendre une décision explicite d'utiliser chaque proposition. Cela est raisonnable pour toute proposition, puisque elles ont toutes des niveaux variables d'instabilité, d'utilité et de complexité.

Nous nous attendons pleinement à un certain contrecoup initial de cela, mais nous pensons finalement que la suppression des préréglages de Stage est une meilleure décision pour nous tous à long terme. Cependant, la suppression des valeurs par défaut précédentes ou la suppression des préréglages de Stage ne signifie pas que nous ne nous soucions pas de la facilité d'utilisation, des nouveaux utilisateurs ou de la documentation. Nous travaillons avec ce que nous pouvons pour garder le projet stable, fournir des outils pour améliorer les choses et documenter ce que nous savons.

### Migration

> _Pour une migration plus automatique, nous avons mis à jour [babel-upgrade](https://github.com/babel/babel-upgrade) pour le faire pour vous (vous pouvez exécuter `npx babel-upgrade`)._

En résumé, nous supprimons les préréglages de Stage. À un certain niveau, les gens devront s'inscrire et savoir quels types de propositions sont utilisées au lieu de supposer ce que les gens devraient utiliser, surtout étant donné la nature instable de certaines de ces propositions. Si vous utilisez un autre préréglage ou une chaîne d'outils, (par exemple, [create-react-app](https://github.com/facebook/create-react-app)) il est possible que ce changement ne vous affecte pas directement.

Nous avons obsolète les préréglages de Stage à partir de `7.0.0-beta.52`. Si vous ne voulez pas changer votre configuration maintenant, nous vous suggérons de **figer** les versions à `beta.54` jusqu'à ce que vous puissiez mettre à jour. Après `beta.54`, nous lancerons une erreur avec un message indiquant comment migrer. Et vérifiez que toutes vos versions sont les mêmes pendant la préversion.

En alternative, vous êtes libre de créer votre propre préréglage qui contient les mêmes plugins et de les mettre à jour comme vous le souhaitez. À l'avenir, nous pourrions vouloir travailler sur un `babel-init` qui peut vous aider à configurer les plugins de manière interactive ou mettre à jour `babel-upgrade` lui-même pour lister et ajouter les plugins de Stage actuels. Peut-être que Babel devrait rester un outil de bas niveau et s'appuyer sur d'autres outils de niveau supérieur/cadre comme `create-react-app` pour gérer ces choix pour les gens.

### Prévenir le verrouillage des propositions

[James DiGioia](https://twitter.com/JamesDiGioia) a écrit un [article](https://babeljs.io/blog/2018/07/19/whats-happening-with-the-pipeline-proposal) récemment sur les changements concernant l'utilisation de l'opérateur pipeline (`|&`gt;).

Le point principal de l'article est que la proposition elle-même est en flux et a quelques options à explorer. Parce que nous aimerions implémenter les trois possibilités actuelles en tant que plugins Babel pour les retours de la spécification et des utilisateurs, nous avons cru que la manière dont le plugin est utilisé devrait également changer. C'est une approche relativement nouvelle pour TC39 et Babel !

Auparavant, nous ajoutions le plugin de proposition à la configuration et c'était tout. Maintenant, nous supprimons le comportement par défaut et demandons aux utilisateurs de s'inscrire à un flag qui montre quelle proposition est choisie. Nous clarifions qu'il n'y a pas d'option fixe (ou même favorite) pour le moment.

C'est quelque chose que nous aimerions continuer à faire à l'avenir comme une autre indication que ces propositions sont ouvertes au changement et aux retours de tous. La suppression des préréglages de Stage rend cela encore plus facile, car auparavant nous devions transmettre ces options même si vous n'utilisiez pas la syntaxe.

### Charge de maintenance de l'écosystème

Le "budget de syntaxe" d'un langage ne s'applique pas seulement à la complexité du langage lui-même, mais peut s'étendre à l'outillage. Chaque nouvelle addition de syntaxe apporte une nouvelle [charge](http://jshint.com/blog/new-lang-features/) aux mainteneurs d'autres projets JavaScript.

Une fois qu'une nouvelle syntaxe est proposée, de nombreuses choses doivent être mises à jour : les parseurs (`babylon`), la coloration syntaxique (`language-babel`), les linters (`babel-eslint`), les frameworks de test (`jest`/`ava`), les formateurs (`prettier`), la couverture de code (`istanbul`), les minifieurs (`babel-minify`), et plus encore.

De nombreux problèmes ont été soulevés sur des projets comme `acorn`, `eslint`, `jshint`, `typescript`, et autres pour supporter les propositions de Stage 0 parce qu'elles étaient dans Babel. Il n'y a pas beaucoup de projets qui adhéreraient à une politique les obligeant à supporter toute proposition, car cela serait extrêmement exigeant à maintenir. À bien des égards, il est surprenant que nous tentions même de le gérer dans Babel lui-même, étant donné les mises à jour et les changements constants.

Qui fait ce travail, et est-ce notre responsabilité de nous assurer que tout fonctionne ? Chacun de ces projets (principalement des bénévoles) manque d'aide dans presque tous les aspects, et pourtant nous recevons continuellement des plaintes à ce sujet. Comment devons-nous, en tant que communauté, prendre la responsabilité de gérer notre infrastructure (pas si différente de l'open source dans son ensemble) ?

Babel a pris en charge le fardeau inhabituel de supporter ces fonctionnalités expérimentales. En même temps, il est raisonnable que d'autres projets adoptent une politique plus conservatrice. Si vous souhaitez voir de nouvelles fonctionnalités de langage supportées dans l'écosystème, [contribuez à TC39](https://github.com/tc39/ecma262/blob/master/CONTRIBUTING.md) et à ce projet pour amener ces propositions à Stage 4.

### L'avenir

Le but de ce projet est d'agir comme une partie du processus TC39 : être une ressource pour l'implémentation de nouvelles propositions (Stage 0–2) et recevoir des retours des utilisateurs tout en supportant les anciennes versions de JavaScript. Nous espérons que cet article éclaire davantage sur la manière dont nous essayons, du mieux que nous pouvons, de mieux aligner ce projet dans l'écosystème JavaScript. Nous publierons bientôt une RC pour la v7 !

Si vous appréciez cet article et le travail que nous faisons sur Babel, vous pouvez me soutenir sur [Patreon](https://www.patreon.com/henryzhu), demander à votre entreprise de nous sponsoriser sur [Open Collective](https://opencollective.com/babel), ou mieux encore, impliquer votre entreprise dans Babel dans le cadre de votre travail. Nous apprécierions la propriété collective.

Avec des remerciements à tous les [relecteurs](https://github.com/babel/website/pull/1735) ! N'hésitez pas à donner votre avis sur [Twitter](https://twitter.com/left_pad/status/1022877618348146693?s=20).

_Publié à l'origine sur_ [https://babeljs.io/blog/2018/07/27/removing-babels-stage-presets](https://babeljs.io/blog/2018/07/27/removing-babels-stage-presets)_.
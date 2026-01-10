---
title: Comment Google construit des frameworks web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-10T09:44:29.000Z'
originalURL: https://freecodecamp.org/news/how-google-builds-a-web-framework-5eeddd691dea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QDS-kCgeF8ZJg_JSEwwIeA.jpeg
tags:
- name: angular2
  slug: angular2
- name: Dart
  slug: dart
- name: Google
  slug: google
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment Google construit des frameworks web
seo_desc: 'By Filip Hracek

  It’s public knowledge that Google uses a single repository to share code — all 2
  billion lines of it — and that it uses the trunk-based development paradigm.


  _This is easily one of the largest single code repositories in the world. [...'
---

Par Filip Hracek

Il est [de notoriété publique](http://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext) que Google utilise un seul dépôt pour partager du code — toutes les 2 milliards de lignes — et qu'il utilise le paradigme de développement basé sur le tronc.

![Image](https://cdn-media-1.freecodecamp.org/images/euiRGyI4xZdUqp4RgiYsctfD2fdCo02b28HI)
_Ceci est facilement l'un des plus grands dépôts de code unique au monde. [Source](http://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext" rel="noopener" target="_blank" title=")._

Pour de nombreux développeurs en dehors de l'entreprise, cela est surprenant et contre-intuitif, mais cela fonctionne vraiment bien. (L'article lié ci-dessus donne de bons exemples, donc je ne les répéterai pas ici.)

> La base de code de Google est partagée par plus de 25 000 développeurs logiciels de Google dans des dizaines de bureaux dans des pays du monde entier. Lors d'une journée de travail typique, ils commettent 16 000 changements dans la base de code. ([source](http://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext))

Cet article traite des spécificités de la construction d'un framework web open source ([AngularDart](https://webdev.dartlang.org/angular)) dans ce contexte.

![Image](https://cdn-media-1.freecodecamp.org/images/KnEFivyJP4WX7220Pp-QJL9n5Gj10o4F76BR)
_Les 'utilisateurs humains' signifient les ingénieurs logiciels qui commettent du code chez Google. (Par opposition aux outils de génération de source.) [Source](http://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext" rel="noopener" target="_blank" title=")._

### Une seule version

Lorsque vous employez le développement basé sur le tronc dans un seul énorme dépôt, vous n'avez qu'une seule version de tout. C'est assez évident. Il est toujours bon de le souligner ici, car cela signifie que — chez Google — vous ne pouvez pas avoir une application FooBar qui utilise AngularDart 2.2.1 et une autre application BarFoo qui est sur 2.3.0. Les deux applications doivent être sur la même version — la dernière.

![Image](https://cdn-media-1.freecodecamp.org/images/J-xXNDvHs6JetEFL8n2kbDIS-fq-hbjKQcxt)
_Image illustrative tirée de [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/" rel="noopener" target="_blank" title=")._

C'est pourquoi les Googlers disent parfois que tous les logiciels chez Google vivent sur le fil du rasoir.

Si toute votre âme crie 'danger !' en ce moment, c'est compréhensible. Dépendre du tronc ('master' en terminologie git) d'une bibliothèque avec votre code de production semble effectivement dangereux. Mais il y a un rebondissement à venir.

### 74 mille tests par commit

AngularDart définit 1601 tests ([ici](https://github.com/dart-lang/angular2/tree/master/test)). Mais lorsque vous commettez un changement dans le code AngularDart dans le dépôt Google, il exécute également des tests pour _tous ceux chez Google qui dépendent du framework_. À l'heure actuelle, cela représente environ 74 mille tests (selon l'ampleur de votre changement — une heuristique saute les tests que le système sait que vous n'affectez pas).

![Image](https://cdn-media-1.freecodecamp.org/images/okJEb5P2KBDDDHfjucfSs6ZzwoypOXTuNtiY)

Il est bon d'avoir plus de tests.

Je viens de faire un changement qui ne se manifeste que 5 % du temps, simulant quelque chose comme une condition de course dans l'algorithme de vérification de réinsertion de détection de changement (j'ai ajouté `&& random.nextDouble() >` .05 [à cette instruction if](https://github.com/dart-lang/angular2/blob/v2.1.0/lib/src/core/change_detection/differs/default_iterable_differ.dart#L386)). Il ne s'est pas manifesté dans aucun des 1601 tests lorsque je les ai exécutés (une fois). Mais il a bien cassé un tas de tests clients.

La vraie valeur ici, cependant, est que ce sont des tests d'_applications réelles_. Non seulement ils sont nombreux, mais ils reflètent également comment le framework est utilisé par les développeurs (pas seulement les auteurs du framework). Cela est significatif : les propriétaires de frameworks n'estiment pas toujours correctement comment leur framework est utilisé.

Il aide également que ces applications soient en production, et que des milliards de dollars y transitent chaque mois. Il y a une grande différence entre les applications de démonstration qu'un auteur de framework assemble pendant son temps libre, et les vraies applications de production avec des dizaines ou des centaines d'années-personnes investies. Si le web doit être pertinent à l'avenir, nous devons mieux soutenir le développement de ces dernières.

![Image](https://cdn-media-1.freecodecamp.org/images/D1mbfuT6MEY47oVUPSqBrFm68kfYjduUsa58)

Alors, que se passe-t-il si le framework casse certaines des applications qui sont construites sur lui ?

### Vous le cassez, vous le réparez

Lorsque les auteurs d'AngularDart veulent introduire un changement cassant, _ils doivent aller et le réparer pour leurs utilisateurs_. Puisque tout chez Google vit dans un seul dépôt, il est trivial de découvrir qui ils cassent, et ils peuvent commencer à réparer immédiatement.

Tout changement cassant dans AngularDart inclut également toutes les corrections de ce changement dans toutes les applications Google qui en dépendent. Ainsi, la casse et la correction vont dans le dépôt simultanément et — bien sûr — après une révision de code appropriée par toutes les parties concernées.

Donnons un exemple concret. Lorsque quelqu'un de l'équipe AngularDart fait un changement qui affecte le code dans l'application AdWords, ils vont dans le code source de cette application et le corrigent. Ils peuvent exécuter les tests existants d'AdWords dans le processus, et ils peuvent en ajouter de nouveaux. Ensuite, ils mettent tout cela dans leur liste de changements et demandent une révision. Puisque leur liste de changements touche le code dans le dépôt AngularDart et le dépôt AdWords, le système exige automatiquement l'approbation de la révision de code des deux équipes. Ce n'est qu'alors que le changement peut être soumis.

![Image](https://cdn-media-1.freecodecamp.org/images/mWtgJIIPLEqXbQoE7jEv13OprQl5snHMFmJh)

Cela a l'effet évident de prévenir le développement de framework dans le vide. Les développeurs de framework AngularDart ont accès à des millions de lignes de code qui sont construites avec leur plateforme, et ils touchent régulièrement ce code eux-mêmes. Ils n'ont pas besoin de supposer comment leur framework est utilisé. (La mise en garde évidente est qu'ils ne voient que le code Google et non le code de tous les Workivas, Wrikes et StableKernels du monde qui utilisent également AngularDart.)

Devoir mettre à niveau le code de vos utilisateurs ralentit également le développement. Pas autant que vous pourriez le penser (regardez les progrès d'AngularDart depuis octobre), mais cela ralentit quand même les choses. C'est à la fois bon et mauvais, selon ce que vous attendez d'un framework. Nous y reviendrons.

En tout cas. La prochaine fois que quelqu'un chez Google [dit](https://webdev.dartlang.org/angular/version) qu'une version alpha d'une bibliothèque est stable et en production, maintenant vous savez pourquoi.

### Changements à grande échelle

Que se passe-t-il si AngularDart doit apporter un changement majeur cassant (par exemple, passer de 2.x à 3.0) et que ce changement casse 74 mille tests ? L'équipe va-t-elle tout corriger ? Vont-ils apporter des modifications à _des milliers_ de fichiers sources, dont la plupart n'ont pas été écrits par eux ?

Oui.

L'une des choses cool à avoir un [système de types solide](https://www.dartlang.org/guides/language/sound-dart) est que vos outils peuvent être beaucoup plus utiles. Dans Dart solide, les outils peuvent être sûrs qu'une variable est d'un certain type, par exemple. Pour le refactoring, cela signifie que de nombreux changements peuvent être complètement automatiques, sans besoin de confirmation du développeur.

Lorsque la méthode de la classe Foo change de `bar()` à `baz()`, vous pouvez créer un outil qui parcourt l'intégralité du dépôt Google unique, trouve toutes les instances de _cette_ classe Foo et ses sous-classes, et change toutes les mentions de `bar()` en `baz()`. Avec le système de types solide de Dart, vous pouvez être sûr que cela ne cassera rien. Sans types solides, même un changement aussi simple peut vous causer des problèmes.

![Image](https://cdn-media-1.freecodecamp.org/images/sqEj9IRiu2-jSIqsltS0Wuxx8CzTgNQQnfPJ)
_Une touche et votre code est formaté selon le [guide de style](https://www.dartlang.org/guides/language/effective-dart/style#formatting" rel="noopener" target="_blank" title=") de Dart. En fait, le guide indique : « Les règles officielles de gestion des espaces blancs pour Dart sont **ce que dart_style produit**. »_

Une autre chose qui aide avec les changements à grande échelle est [dart_style](https://github.com/dart-lang/dart_style), le formateur par défaut de Dart. Tout le code Dart chez Google est formaté en utilisant cet outil. Au moment où votre code atteint les réviseurs, il a été auto-formaté en utilisant dart_style, donc il n'y a pas d'arguments sur le fait de mettre la nouvelle ligne ici ou là. Et cela s'applique également aux refactoring à grande échelle.

### Métriques de performance

Comme je l'ai dit ci-dessus, AngularDart bénéficie des tests de ses dépendants. Mais ce ne sont pas seulement des tests. Google est très rigoureux sur la mesure de la performance de ses applications, et donc la plupart (toutes ?) des applications de production ont des suites de benchmarks.

Ainsi, lorsque l'équipe AngularDart introduit un changement qui rend AdWords 1 % plus lent à charger, ils le savent _avant_ de valider le changement. Lorsque l'équipe a [dit](https://www.youtube.com/watch?list=PLOU2XLYxmsILKY-A1kq4eHMcku3GMAyp2&v=8ixOkJOXdMo) en octobre que les applications AngularDart sont devenues 40 % plus petites et 10 % plus rapides depuis août, ils ne parlaient pas de quelques exemples d'applications synthétiques minuscules TodoMVC. Ils parlaient d'applications réelles, critiques pour la mission, en production avec des millions d'utilisateurs et des mégaoctets de code de logique métier.

![Image](https://cdn-media-1.freecodecamp.org/images/SysqQlFJA4f3ktY712-YfEXb1aQZNVTx5VRv)

### Note de côté : Outil de construction hermetique

Vous vous demandez peut-être : comment ce gars savait-il quels tests dans le grand dépôt interne exécuter après avoir introduit le bug aléatoire dans AngularDart ? Surement, il ne choisissait pas à la main les 74 mille tests, et tout aussi sûrement, il n'exécutait pas _tous_ les tests chez Google. La réponse réside dans quelque chose appelé Bazel.

À cette échelle, vous ne pouvez pas avoir une série de scripts shell pour construire des trucs. Les choses seraient aléatoires et prohibitivement lentes. Ce dont vous avez besoin, c'est d'un outil de construction hermetique.

« Hermétique » dans ce contexte est très similaire à « [pure](https://en.wikipedia.org/wiki/Pure_function) » dans le contexte des fonctions. Vos étapes de construction ne peuvent pas avoir d'effets secondaires (comme des fichiers temporaires, des changements dans PATH, etc.), et elles doivent être déterministes (la même entrée conduit toujours à la même sortie). Lorsque c'est le cas, vous pouvez exécuter les constructions et les tests sur n'importe quelle machine à n'importe quel moment et vous obtiendrez une sortie cohérente. Vous n'avez pas besoin de faire `make clean`. Vous pouvez donc envoyer vos constructions/tests à des serveurs de construction et les paralléliser.

![Image](https://cdn-media-1.freecodecamp.org/images/KXMw3tOJf82-JlnAbi0topqlDoVK4UH1Gxxu)

Google a passé des années à développer un tel outil de construction. Il a été open source l'année dernière sous le nom de [Bazel](https://bazel.build/).

Et grâce à cette pièce d'infrastructure, les outils de test internes peuvent déterminer quelles constructions/tests chaque changement affecte, et les exécuter lorsque cela est approprié.

### Que signifie tout cela ?

L'objectif explicite d'AngularDart est d'être le meilleur en termes de productivité, de performance et de fiabilité pour la construction de grandes applications web. Cet article couvre, espérons-le, la dernière partie — la fiabilité — et pourquoi il est important que des applications Google critiques pour la mission comme AdWords et AdSense utilisent le framework. Ce n'est pas seulement l'équipe qui se vante de ses utilisateurs — comme expliqué ci-dessus, avoir de grands utilisateurs internes rend AngularDart moins susceptible d'introduire des changements superficiels. Cela rend le framework plus fiable.

![Image](https://cdn-media-1.freecodecamp.org/images/fbVxJ2-4EeeKKTXhTRoWVEMZrpAVQBeVTgzV)
_Si tout cela semble trop commercial, vous pourriez consulter mes projets AngularDart résolument non commerciaux comme [Prime Finder](https://filiph.github.io/markov/" rel="noopener" target="_blank" title="">Donald Trump automatique</a> (chaîne de Markov) ou <a href="https://filiph.github.io/prime_finder/" rel="noopener" target="_blank" title=")._

Si vous cherchez un framework qui effectue des révisions majeures et introduit des fonctionnalités majeures tous les quelques mois, AngularDart n'est définitivement pas pour vous. Même si l'équipe voulait construire le framework de cette manière, je pense qu'il est clair d'après cet article qu'ils ne pourraient pas. Nous croyons sincèrement, cependant, qu'il y a de la place pour un framework qui est moins tendance mais fiable.

À mon avis, la meilleure prédiction de soutien à long terme pour une pile technologique open-source est qu'elle fait partie intégrante des activités principales du mainteneur principal. Prenez Android, Dagger, MySQL ou Git comme exemples. C'est pourquoi je suis heureux que Dart ait enfin un framework web préféré (AngularDart), une bibliothèque de composants préférée ([AngularDart Components](https://pub.dartlang.org/packages/angular2_components)) et un framework mobile préféré ([Flutter](https://flutter.io/)) — tous utilisés pour construire des applications Google critiques pour les affaires.

_[[Matan Lurey](https://medium.com/@matanlurey) et Kathy Walrath ont contribué à cet article.]_

_[Discuter sur [Reddit](https://www.reddit.com/r/webdev/comments/5t6f8o/how_google_builds_a_web_framework/), [HN](https://news.ycombinator.com/item?id=13614354), [Twitter](https://twitter.com/filiphracek/status/829991585756520448).]_
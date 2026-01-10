---
title: La conception de WebAssembly
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-28T18:14:11.000Z'
originalURL: https://freecodecamp.org/news/the-design-of-webassembly-81f1dcabaddd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xAFAiAxqZVrOVLBTo9tf6w.jpeg
tags:
- name: internet
  slug: internet
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: WebAssembly
  slug: webassembly
seo_title: La conception de WebAssembly
seo_desc: 'By Patrick Ferris

  I love the web. It is a modern-day superpower for the dissemination of information
  and empowerment of the individual. Of course, it has its downsides like trolling
  (largely possible through anonymity) and privacy issues, not to ment...'
---

Par Patrick Ferris

J'adore le web. C'est un superpouvoir moderne pour la diffusion de l'information et l'autonomisation de l'individu. Bien sûr, il a ses inconvénients comme le trolling (largement possible grâce à l'anonymat) et les problèmes de confidentialité, sans parler des problèmes de propriété et de violation de copyright sur le point d'entrer en vigueur avec l'article 13 hautement controversé. Mais, oublions cela pour un instant et émerveillons-nous de l'innovation technologique d'Internet et des navigateurs qui le supportent.

J'ai d'abord appris à coder en Javascript et depuis, beaucoup se sont moqués de moi pour cela. Oui, je sais qu'il y a des parties bizarres comme ce joyau : `[] == ![] // true` mais il est devenu l'un des langages les plus répandus sur la planète grâce à Internet, aux navigateurs et aux interpréteurs qui exécutent le code (V8 de Google et SpiderMonkey de Firefox pour n'en nommer que quelques-uns).

En m'impliquant davantage dans le développement web, j'ai remarqué un nouveau nom sur le bloc : WebAssembly. En tant qu'étudiant en informatique et développeur, je crois que l'une des meilleures façons d'apprendre quelque chose est d'essayer de comprendre pourquoi les ingénieurs qui l'ont construit ont fait ces choix de conception. Voici donc un bref aperçu de certains des principes de conception intéressants de WebAssembly et aussi pourquoi je pense que tout le monde devrait être excité.

#### Pourquoi avons-nous besoin de WebAssembly ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*lNZl5UEb8T84byWotDdV3w.jpeg)

D'accord, tout d'abord, à tous mes fans de Javascript là-bas — non, vous ne devriez pas être inquiets. Lorsque Javascript est apparu pour la première fois, il était conçu pour être utilisé de manière légère mais a depuis évolué pour faire beaucoup de travail lourd. Peut-être était-il utilisé pour manipuler quelques éléments DOM, une vérification côté client dans les formulaires mais pas tout ce qui est tenté d'être fait sur le web maintenant. Certainement pas pour exécuter des jeux complets.

Pourquoi Javascript n'est-il pas si rapide ou génial ? L'une des principales raisons est qu'il s'agit d'un langage interprété. Scanner le code ligne par ligne et l'exécuter, heureusement avec les compilateurs Just-in-Time, l'efficacité s'est massivement améliorée mais il reste encore beaucoup de place pour s'améliorer. Mais même alors, il y a le problème du typage dynamique de Javascript causant un autre plafond de performance.

Alex Danilo a discuté des améliorations que WebAssembly pourrait apporter dans son discours à Google I/O en 2017. Ce qui a vraiment mis en évidence les inefficacités était son exemple de fonction `add(a, b)` et la complexité que les interpréteurs Javascript doivent traverser pour en faire sens.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oaXj5mrSX8ho6XCnWx8dig.jpeg)
_Une simple fonction Javascript — [ECMAScript Rabbit Hole p.263](https://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf" rel="noopener" target="_blank" title=") (assurez-vous de suivre les liens des autres appels de fonction)_

WebAssembly ouvre la porte à la compilation, ce qui ouvre une autre porte à l'optimisation. Sa capacité à prendre le langage source C/C++ lui permet de faire une vérification de type statique qui aide à améliorer la vitesse. C'est ce que les développeurs de la Mozilla Foundation ont réalisé et voulu corriger. Pour résumer cette grande vidéo, Javascript a été conçu pour les humains et les navigateurs ont été laissés pour essayer de le rendre rapide ; WebAssembly a été conçu comme un langage cible pour les compilateurs que les navigateurs pouvaient déjà exécuter rapidement.

La réalisation que nous pourrions avoir deux choix de code exécutés dans les moteurs était une perspective excitante — et les quatre principaux navigateurs (Chrome, Safari, Firefox et IE) ont tous commencé à planifier pour permettre à leurs moteurs d'exécuter Javascript et WebAssembly. Encore une fois, laissez-moi réitérer... WebAssembly ne remplace pas Javascript.

#### Pourquoi compiler le code ?

Compiler le code signifie vraiment le prendre d'un langage (source) et le traduire dans un autre langage (cible). Il s'agit d'une compréhension incroyablement simplifiée de la compilation. La plupart des pipelines de compilation modernes impliquent beaucoup plus d'étapes qui nous permettent de vraiment affiner et optimiser notre code pour le rendre plus rapide et plus économe en énergie.

Les premières étapes incluent généralement des analyseurs lexicaux, syntaxiques et sémantiques pour obtenir le code dans une sorte de langage intermédiaire parfait pour l'optimisation. Ensuite, nous optimisons indépendamment, générons le code cible et optimisons peut-être en fonction du matériel ou de l'environnement.

Tous les projets doivent commencer petit d'abord, et les ingénieurs de Mozilla ont décidé de commencer avec leur langage source étant C/C++ et en utilisant une chaîne d'outils existante appelée LLVM (non un acronyme) ils compileront en utilisant cela.

Initialement, la recherche d'un web mieux performant a commencé avec asm.js (au moins dans le récit de WebAssembly. Voir PNaCL — les tentatives précédentes de Google) un petit sous-ensemble de Javascript qui pourrait être la cible de compilation pour les programmes C/C++ qui utilisaient des annotations et d'autres astuces pour améliorer les performances de Javascript.

Malheureusement, il manquait un principe de conception crucial sous-jacent à ce qui était souhaité : la portabilité. Différents moteurs Javascript ont donné des avis de performance différents, mais c'était une indication claire que cela pourrait être une bonne approche.

Les développeurs de WebAssembly ont décidé que leur représentation cible serait un format binaire qui fournissait une « [représentation dense et linéaire de la syntaxe abstraite](https://webassembly.github.io/spec/core/binary/conventions.html) »... Ce qui est beaucoup de mots, alors décomposons cela.

La partie « dense » fait référence à l'objectif de haut niveau d'atteindre un format efficace en taille et en temps de chargement. Internet consiste à envoyer des données le long de fils, et bien qu'il y ait beaucoup de projets pour améliorer la latence de cela, un moyen infaillible d'y parvenir est d'envoyer moins de données. Un autre aspect important est l'augmentation de la vitesse de décodage grâce à l'indexation de tableau par rapport à la recherche de dictionnaire (si elles utilisaient un format de texte compressé). Lisez plus sur ce choix de conception ici.

#### Qu'est-ce que wat ?

Le format binaire auquel les programmes C et C++ sont compilés sont des fichiers `.wasm`, ceux-ci ont une correspondance 1:1 directement avec un format de texte (quelque peu) lisible par l'homme. Ces fichiers sont étiquetés `.wat`, cet explorateur Wasm est idéal pour comprendre la représentation textuelle et comment elle se rapporte au code original. Prenons un exemple simple.

Il se passe beaucoup de choses ici, alors prenons-le lentement et expliquons les concepts au fur et à mesure.

Tout d'abord, il y a ce mot étrange `module`, d'où vient-il ? Mejin Leechor a donné une excellente conférence sur les modules en Javascript et les décrit comme donnant au code une « structure et des limites ». Cela est très similaire à l'idée des modules WebAssembly (et il y a des plans pour l'avenir pour essayer de s'intégrer avec les modules es6).

Directement de la documentation, nous avons que le module est l'« [unité de code distribuable, chargeable et exécutable dans WebAssembly](https://webassembly.org/docs/modules/) ». Les modules peuvent avoir les sections suivantes, chacune avec sa propre responsabilité unique : import, export, start, global, memory, data, table, elements, function et code. Pour l'instant, regardons simplement ce que nous avons dans notre module.

La première déclaration est `(type $type0 (func (param i32) (result i32)))` . Cela est intimement lié à l'appel de table à la ligne suivante. Nous déclarons un nouveau type avec la signature `func` qui prend un paramètre entier 32 bits et retourne un entier 32 bits. Si nous devions utiliser à nouveau la fonction que nous avons écrite, nous devrions faire un `call_indirect` dans notre `table` et ensuite nous pourrions faire une vérification de type pour nous assurer que tout était correct. Dans le cadre du produit viable minimal, une seule table est autorisée, mais il y a des plans futurs pour permettre plusieurs tables et pour que celles-ci soient indexées.

La déclaration suivante est `(table 0 anyfunc)` . La section table est réservée pour définir zéro ou plusieurs tables. Une table est similaire à une mémoire linéaire dans le sens où ce sont des tableaux redimensionnables qui contiennent des références. Le `0` fait référence au fait que nous n'avons rien dans notre table, mais nous devons encore fournir la seule valeur possible du MVP `anyfunc` (une fonction).

Le problème que les développeurs avaient était lié à la sécurité. Si une fonction voulait appeler une autre fonction, lui donner un accès direct à une fonction stockée dans la mémoire linéaire était non sécurisé. Au lieu de cela, les fonctions sont stockées dans la table, prêtes à être indexées si nécessaire. Lin Clark a écrit un excellent article décrivant les tables (telles qu'utilisées dans les imports) plus en détail et comment elles fournissent une meilleure sécurité.

Nous avons ensuite une déclaration de `(memory 1)` , il s'agit de la mémoire linéaire utilisée par le module et nous déclarons que nous avons besoin de `1` page de mémoire (64 KiB).

La déclaration suivante est `(export "memory" memory)` . Une exportation est quelque chose qui est retourné à l'hôte au moment de l'instantiation. Basiquement, les parties intéressantes que nous voulons du code WebAssembly.

La structure est assez simple `(export <nom-de-lexport> (<type> &l`t;nom/index>)) donc ici nous exportons simplement la mémoire que nous avons déclarée à la ligne précédente. Cela permet un accès direct à la mémoire dans notre code Javascript, en tant qu'ArrayBuffer ce qui améliore considérablement l'efficacité car il n'y a pas d'appels en avant et en arrière à travers la frontière WASM/JS. De même, nous exportons ensuite notre fonction avec (exp`ort "main" $func0) .

Maintenant, la partie légèrement plus intéressante, notre code et sa représentation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ywt3H0EvyqqZwTC_SkvyqQ.jpeg)
_Les différentes parties de la déclaration de fonction dans le format texte WebAssembly_

Avant de continuer, c'est l'occasion parfaite pour introduire un autre composant de conception : la machine à pile.

#### Machines à registres versus machines à pile

Les ordinateurs, dans leur forme la plus simple, consomment des entrées et produisent des sorties. En tant que « machine » exécute un programme, elle peut le faire de plusieurs manières différentes. Deux des principales approches sont les machines à registres et les machines à pile. Dans une machine à registres, les paramètres des fonctions sont conservés dans des emplacements mémoire et sont ensuite manipulés en fonction du programme en cours d'exécution.

Une analogie simple, mais quelque peu erronée, pourrait être une cuisine et la préparation d'une recette. Les ingrédients sont stockés dans différents endroits, vous les prenez et faites quelque chose que vous pourriez mettre de côté pour un autre jour ou consommer immédiatement (yum). C'est loin d'être parfait mais cela devrait vous donner une idée.

Les machines à pile, en revanche, utilisent un modèle différent. Imaginez que vous êtes journaliste ou secrétaire, votre travail est de lire et de répondre aux lettres. Vous « retirez » la lettre du haut de votre pile et commencez à écrire une réponse tandis que quelqu'un d'autre arrive avec plus de travail et « pousse » au sommet de la pile. Ce sont celles que vous allez devoir faire ensuite. Encore une fois, grossièrement simplifié mais cela devrait aider à visualiser les mécanismes.

WebAssembly utilise un modèle de machine à pile pour l'exécution du code. Si vous manquez de lectures intéressantes et que vous êtes intéressé par la sémantique de la programmation, l'article « [Bringing the Web up to Speed with WebAssembly](https://people.mpi-sws.org/~rossberg/papers/Haas,%20Rossberg,%20Schuff,%20Titzer,%20Gohman,%20Wagner,%20Zakai,%20Bastien,%20Holman%20-%20Bringing%20the%20Web%20up%20to%20Speed%20with%20WebAssembly.pdf) » est vraiment bon. Il indique également pourquoi ils ont choisi la représentation de la machine à pile : « L'organisation de la pile est simplement un moyen d'atteindre une représentation de programme compacte, car il a été démontré qu'elle est plus petite qu'une machine à registres » avec référence à cet article qui a trouvé « ... la taille du bytecode de la machine à registres étant seulement 26 % plus grande que celle de la pile correspondante ».

Même si l'approche de la machine à pile n'est pas nécessairement plus rapide, elle offrait un bytecode plus petit ; un objectif de conception incroyablement important pour les transactions basées sur Internet.

Alors, comment pouvons-nous comprendre le format texte comme une machine à pile. Lorsque nous lisons le code ligne par ligne, nous finissons par pousser des arguments sur la pile, puis les retirons, faisons un calcul et repoussons le résultat. Et répétons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*01B21CM64DHEkL6nzv7WPw.jpeg)
_Un petit exemple de WebAssembly et de l'approche implicite de la machine à pile_

Au début, il peut sembler un peu étrange d'avoir un format texte, si à la fin il sera compilé au format binaire pour la compression. Mais, Internet a toujours eu la politique de visualisation de la source et c'est pourquoi les développeurs derrière WebAssembly ont produit le format texte. Pour aller plus loin et éviter les conflits de syntaxe, ils ont utilisé le style s-expression similaire à Lisp.

#### Sécurité et Sandboxing

L'une des plus grandes sources de bugs (et d'exploits) dans les langages non sécurisés est les débordements de tampon. C et C++ sont presque interchangeables avec cette idée et c'est l'un des premiers aspects que l'on vous enseigne lorsque vous apprenez ces langages. En échange de quelques coûts supplémentaires, WebAssembly ajoute ce filet de sécurité en imposant une mémoire de taille fixe et indexée (bien que certaines mémoires puissent être agrandies).

Les variables locales de notre fonction, par exemple `$var0`, ne sont pas référencées par adresse mais sont plutôt indexées, fournissant une couche de sécurité. L'accès est accordé via les commandes `get_local` et `set_local`, ce qui se passe dans l'espace d'index des variables locales.

La sécurité de la mémoire était une priorité absolue lors de la conception de WebAssembly. Directement de la documentation : « [La mémoire linéaire est sandboxée](https://github.com/WebAssembly/design/blob/master/Semantics.md#linear-memory) ; elle n'alias pas d'autres mémoires linéaires, les structures de données internes du moteur d'exécution, la pile d'exécution, les variables locales ou d'autres mémoires de processus. » Lin Clark, encore une fois, a écrit un excellent article décrivant cela.

L'idée de base est comparable à l'objet ArrayBuffer de Javascript — redimensionnable et vérifié. Ce que nous essayons d'atteindre est l'isolation du programme pour empêcher les erreurs et le code malveillant de se propager et de corrompre des données auxquelles ils ne devraient même pas avoir accès.

#### Que peut faire WebAssembly ?

L'un des principaux objectifs finaux pour WebAssembly était de révolutionner ce qui était possible en termes de graphismes sur le web. Les exemples classiques sont [ZenGarden](https://s3.amazonaws.com/mozilla-games/ZenGarden/EpicZenGarden.html) par EpicGames et [Tanks!](https://webassembly.org/demo/Tanks/).

Grâce à sa conception, WebAssembly marque un moment pivot dans le développement web. Internet a un nouvel outil dans son arsenal pour créer des expériences incroyables et partager des informations. WebAssembly offre des tailles de code plus petites, une exécution plus rapide, une meilleure sécurité et beaucoup de place pour l'extensibilité. Avec des idées comme les threads, les primitives single-instruction multiple-data (SIMD) et l'exécution à coût zéro à l'horizon, les capacités de WebAssembly semblent destinées à s'étendre.
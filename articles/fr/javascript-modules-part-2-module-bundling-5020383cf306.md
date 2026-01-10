---
title: 'Modules JavaScript Partie 2 : Regroupement de Modules'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-05T16:42:12.000Z'
originalURL: https://freecodecamp.org/news/javascript-modules-part-2-module-bundling-5020383cf306
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e0eQH_9X8jN7yC6AEqlvdQ.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'Modules JavaScript Partie 2 : Regroupement de Modules'
seo_desc: 'By Preethi Kasireddy

  In Part I of this post, I talked about what modules are, why developers use them,
  and the various ways to incorporate them into your programs.

  In this second part, I’ll tackle what exactly it means to “bundle” modules: why
  we bun...'
---

Par Preethi Kasireddy

Dans la [Partie I](https://medium.freecodecamp.com/javascript-modules-a-beginner-s-guide-783f7d7a5fcc?source=latest---------1) de cet article, j'ai parlé de ce que sont les modules, pourquoi les développeurs les utilisent et les différentes façons de les incorporer dans vos programmes.

Dans cette deuxième partie, je vais aborder ce que signifie exactement "regrouper" des modules : pourquoi nous regroupons les modules, les différentes façons de le faire et l'avenir des modules dans le développement web.

### Qu'est-ce que le regroupement de modules ?

À un niveau élevé, le regroupement de modules est simplement le processus de rassemblement d'un groupe de modules (et de leurs dépendances) en un seul fichier (ou groupe de fichiers) dans le bon ordre.

Comme pour tous les aspects du développement web, le diable est dans les détails. :)

### Pourquoi regrouper les modules ?

Lorsque vous divisez votre programme en modules, vous organisez généralement ces modules dans différents fichiers et dossiers. Il est probable que vous ayez également un groupe de modules pour les bibliothèques que vous utilisez, comme Underscore ou React.

En conséquence, chacun de ces fichiers doit être inclus dans votre fichier HTML principal dans une balise **_<scri_**pt>, qui est ensuite chargée par le navigateur lorsque l'utilisateur visite votre page d'accueil. Avoir des balises **_<scri_**pt> séparées pour chaque fichier signifie que le navigateur doit charger chaque fichier individuellement : un... par... un.

... Ce qui est mauvais pour le temps de chargement de la page.

Pour contourner ce problème, nous regroupons, ou "concaténons" tous nos fichiers en un seul gros fichier (ou quelques fichiers selon le cas) afin de réduire le nombre de requêtes. Lorsque vous entendez les développeurs parler de l'étape de "build" ou du "processus de build", c'est de cela qu'ils parlent.

Une autre approche courante pour accélérer l'opération de regroupement consiste à "minifier" le code regroupé. La minification est le processus de suppression des caractères inutiles du code source (par exemple, les espaces blancs, les commentaires, les caractères de nouvelle ligne, etc.), afin de réduire la taille globale du contenu sans changer la fonctionnalité du code.

Moins de données signifie moins de temps de traitement par le navigateur, ce qui réduit à son tour le temps nécessaire pour télécharger les fichiers. Si vous avez déjà vu un fichier avec une extension "min" comme "[underscore-min.js](https://github.com/jashkenas/underscore/blob/master/underscore-min.js)", vous avez probablement remarqué que la version minifiée est assez petite (et illisible) par rapport à la [version complète](https://github.com/jashkenas/underscore/blob/master/underscore.js).

Des outils comme Gulp et Grunt rendent la concaténation et la minification simples pour les développeurs, garantissant que le code lisible par l'homme reste exposé pour les développeurs tandis que le code optimisé pour les machines est regroupé pour les navigateurs.

### Quelles sont les différentes façons de regrouper les modules ?

La concaténation et la minification de vos fichiers fonctionnent très bien lorsque vous utilisez l'un des modèles de modules standard (discutés dans le [précédent article](https://medium.freecodecamp.com/javascript-modules-a-beginner-s-guide-783f7d7a5fcc#.y8hs0nsne)) pour définir vos modules. Tout ce que vous faites vraiment, c'est rassembler un tas de code JavaScript simple.

Cependant, si vous adhérez à des systèmes de modules _non natifs_ que les navigateurs ne peuvent pas interpréter comme CommonJS ou AMD (ou même des formats de modules _natifs_ ES6), vous devrez utiliser un outil spécialisé pour convertir vos modules en code compatible avec les navigateurs et correctement ordonné. C'est là que Browserify, RequireJS, Webpack et autres "regroupeurs de modules" ou "chargeurs de modules" entrent en jeu.

En plus de regrouper et/ou charger vos modules, les regroupeurs de modules offrent une tonne de fonctionnalités supplémentaires comme la recompilation automatique du code lorsque vous effectuez une modification ou la production de cartes sources pour le débogage.

Parcourons quelques méthodes courantes de regroupement de modules :

### Regroupement de CommonJS

Comme vous le savez d'après la [Partie 1](https://medium.freecodecamp.com/javascript-modules-a-beginner-s-guide-783f7d7a5fcc#.y8hs0nsne), CommonJS charge les modules de manière synchrone, ce qui serait bien sauf que ce n'est pas pratique pour les navigateurs. J'ai mentionné qu'il y avait une solution de contournement à cela — l'une d'entre elles est un regroupeur de modules appelé Browserify. Browserify est un outil qui compile les modules CommonJS pour le navigateur.

Par exemple, supposons que vous avez ce fichier main.js qui importe un module pour calculer la moyenne d'un tableau de nombres :

Dans ce cas, nous avons une dépendance (myDependency). En utilisant la commande ci-dessous, Browserify regroupe de manière récursive tous les modules requis en commençant par main.js dans un seul fichier appelé bundle.js :

Browserify fait cela en analysant l'[AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) pour chaque appel **_require_** afin de parcourir l'ensemble du graphe de dépendances de votre projet. Une fois qu'il a compris comment vos dépendances sont structurées, il les regroupe toutes dans le bon ordre dans un seul fichier. À ce stade, tout ce que vous avez à faire est d'insérer une seule balise **_<scri_**pt> avec votre fichier "bundle.js" dans votre HTML pour vous assurer que tout votre code source est téléchargé en une seule requête HTTP. Bam ! Prêt à être regroupé.

De même, si vous avez plusieurs fichiers avec plusieurs dépendances, vous indiquez simplement à Browserify quel est votre fichier d'entrée et vous vous asseyez pendant qu'il fait sa magie.

Le produit final : des fichiers regroupés prêts pour des outils comme Minify-JS pour minifier le code regroupé.

### Regroupement de AMD

Si vous utilisez AMD, vous voudrez utiliser un chargeur AMD comme RequireJS ou Curl. Un chargeur de modules (par opposition à un regroupeur) charge dynamiquement les modules dont votre programme a besoin pour s'exécuter.

Pour rappel, l'une des principales différences entre AMD et CommonJS est qu'il charge les modules de manière asynchrone. En ce sens, avec AMD, vous n'avez techniquement pas besoin d'une étape de build où vous regroupez vos modules en un seul fichier puisque vous chargez vos modules de manière asynchrone — ce qui signifie que vous téléchargez progressivement uniquement les fichiers strictement nécessaires à l'exécution du programme au lieu de télécharger tous les fichiers en une seule fois lorsque l'utilisateur visite la page pour la première fois.

En réalité, cependant, le surcoût des requêtes à haut volume au fil du temps pour chaque action de l'utilisateur n'a pas beaucoup de sens en production. La plupart des développeurs web utilisent toujours des outils de build pour regrouper et minifier leurs modules AMD pour des performances optimales, en utilisant des outils comme l'optimiseur RequireJS, [r.js](http://requirejs.org/docs/optimization.html), par exemple.

Globalement, la différence entre AMD et CommonJS en matière de regroupement est la suivante : pendant le développement, les applications AMD peuvent se passer d'une étape de build. Au moins, jusqu'à ce que vous poussiez le code en production, moment auquel des optimiseurs comme r.js peuvent intervenir pour le gérer.

Pour une discussion intéressante sur CommonJS vs. AMD, consultez cet article sur le [blog de Tom Dale](http://tomdale.net/2012/01/amd-is-not-the-answer/) :)

### Webpack

En ce qui concerne les regroupeurs, Webpack est le nouveau venu. Il a été conçu pour être agnostique au système de modules que vous utilisez, permettant aux développeurs d'utiliser CommonJS, AMD ou ES6 selon les besoins.

Vous vous demandez peut-être pourquoi nous avons besoin de Webpack alors que nous avons déjà d'autres regroupeurs comme Browserify et RequireJS qui font le travail et le font plutôt bien. Eh bien, pour une chose, Webpack offre des fonctionnalités utiles comme le "code splitting" — une façon de diviser votre base de code en "morceaux" qui sont chargés à la demande.

Par exemple, si vous avez une application web avec des blocs de code qui ne sont nécessaires que dans certaines circonstances, il peut ne pas être efficace de mettre toute la base de code dans un seul fichier massif regroupé. Dans ce cas, vous pourriez utiliser le code splitting pour extraire le code en morceaux regroupés qui peuvent être chargés à la demande, évitant ainsi les problèmes de gros téléchargements initiaux lorsque la plupart des utilisateurs n'ont besoin que du cœur de votre application.

Le code splitting n'est qu'une des nombreuses fonctionnalités convaincantes que Webpack offre, et l'Internet regorge d'articles d'opinion forts sur le fait que Webpack ou Browserify est le meilleur. Voici quelques-unes des discussions les plus équilibrées que j'ai trouvées utiles pour comprendre le problème :

* [https://gist.github.com/substack/68f8d502be42d5cd4942](https://gist.github.com/substack/68f8d502be42d5cd4942)
* [http://mattdesl.svbtle.com/browserify-vs-webpack](http://mattdesl.svbtle.com/browserify-vs-webpack)
* [http://blog.namangoel.com/browserify-vs-webpack-js-drama](http://blog.namangoel.com/browserify-vs-webpack-js-drama)

### Modules ES6

Déjà de retour ? Bien ! Parce que ensuite, je veux parler des modules ES6, qui, à certains égards, pourraient réduire le besoin de regroupeurs à l'avenir. (vous verrez ce que je veux dire dans un instant.) D'abord, comprenons comment les modules ES6 sont chargés.

La différence la plus importante entre les formats de modules JS actuels (CommonJS, AMD) et les modules ES6 est que les modules ES6 sont conçus en gardant à l'esprit l'analyse statique. Ce que cela signifie, c'est que lorsque vous importez des modules, l'import est résolu au moment de la compilation — c'est-à-dire avant que le script ne commence à s'exécuter. Cela nous permet de supprimer les exports qui ne sont pas utilisés par d'autres modules avant d'exécuter le programme. La suppression des exports inutilisés peut entraîner des économies d'espace significatives, réduisant ainsi la charge sur le navigateur.

Une question courante qui se pose est : en quoi cela est-il différent de l'élimination du code mort qui se produit lorsque vous utilisez quelque chose comme UglifyJS pour minifier votre code ? La réponse est, comme toujours, "ça dépend."

_(NOTE : L'élimination du code mort est une étape d'optimisation qui supprime le code et les variables inutilisés — pensez-y comme à la suppression des bagages excédentaires dont votre programme regroupé n'a pas besoin pour s'exécuter, *après* qu'il ait été regroupé)._

Parfois, l'élimination du code mort pourrait fonctionner exactement de la même manière entre UglifyJS et les modules ES6, et d'autres fois non. Il y a un exemple intéressant sur le [wiki de Rollup](https://github.com/rollup/rollup) si vous voulez le consulter.

Ce qui rend les modules ES6 différents, c'est l'approche différente de l'élimination du code mort, appelée "tree shaking". Le tree shaking est essentiellement l'élimination du code mort inversée. Il n'inclut que le code dont votre regroupement a besoin pour s'exécuter, plutôt que d'exclure le code dont votre regroupement n'a pas besoin. Regardons un exemple de tree shaking :

Supposons que nous avons un fichier utils.js avec les fonctions ci-dessous, chacune d'entre elles étant exportée en utilisant la syntaxe ES6 :

Ensuite, supposons que nous ne savons pas quelles fonctions utils nous voulons utiliser dans notre programme, alors nous allons de l'avant et importons tous les modules dans main.js comme suit :

Et puis nous finissons par n'utiliser que la fonction each :

La version "tree shaken" de notre fichier main.js ressemblerait à ceci une fois les modules chargés :

Remarquez comment les seules exports incluses sont celles que nous utilisons : **each**.

Pendant ce temps, si nous décidons d'utiliser la fonction filter au lieu de la fonction each, nous finissons par regarder quelque chose comme ceci :

La version tree shaken ressemble à ceci :

Remarquez comment cette fois-ci **_each_** et **_filter_** sont inclus. C'est parce que **_filter_** est défini pour utiliser **_each_**, donc nous avons besoin des deux exports pour que le module fonctionne.

Assez astucieux, n'est-ce pas ?

Je vous défie de jouer et d'explorer le tree shaking dans le [démo en direct et l'éditeur](http://rollupjs.org/) de Rollup.js.

### Construction de modules ES6

D'accord, nous savons donc que les modules ES6 sont chargés différemment des autres formats de modules, mais nous n'avons pas encore parlé de l'étape de build lorsque vous utilisez des modules ES6.

Malheureusement, les modules ES6 nécessitent encore un travail supplémentaire, car il n'existe pas encore d'implémentation native pour la façon dont les navigateurs chargent les modules ES6.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lpAgpggDLcK1a3MBEbmODg.png)
_[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import" rel="noopener" target="_blank" title=")_

Voici quelques-unes des options pour construire/convertir les modules ES6 pour qu'ils fonctionnent dans le navigateur, avec **#1** étant l'approche la plus courante aujourd'hui :

1. Utilisez un transpileur (par exemple, Babel ou Traceur) pour transpiler votre code ES6 en code ES5 au format CommonJS, AMD ou UMD. Ensuite, passez le code transpilé à travers un regroupeur de modules comme Browserify ou Webpack pour créer un ou plusieurs fichiers regroupés.
2. Utilisez [Rollup.js](http://rollupjs.org/), qui est très similaire à l'option #1 sauf que Rollup s'appuie sur la puissance des modules ES6 pour analyser statiquement votre code ES6 et ses dépendances avant le regroupement. Il utilise le "tree shaking" pour inclure le strict minimum dans votre regroupement. Globalement, le principal avantage de Rollup.js par rapport à Browserify ou Webpack lorsque vous utilisez des modules ES6 est que le tree shaking pourrait rendre vos regroupements plus petits. La mise en garde est que Rollup propose plusieurs formats pour regrouper votre code, y compris ES6, CommonJS, AMD, UMD ou IIFE. Les regroupements IIFE et UMD fonctionneraient dans votre navigateur tels quels, mais si vous choisissez de regrouper en AMD, CommonJS ou ES6, vous devez trouver d'autres méthodes pour convertir ce code dans un format que le navigateur comprend (par exemple, en utilisant Browserify, Webpack, RequireJS, etc.).

### Sauter à travers les cerceaux

En tant que développeurs web, nous devons sauter à travers beaucoup de cerceaux. Ce n'est pas toujours facile de convertir nos beaux modules ES6 en quelque chose que les navigateurs peuvent interpréter.

La question est, quand les modules ES6 s'exécuteront-ils dans le navigateur sans tout ce surcoût ?

La réponse, heureusement, est "plus tôt que tard".

ECMAScript dispose actuellement d'une spécification pour une solution appelée [API de chargement de modules ECMAScript 6](https://github.com/ModuleLoader/es6-module-loader). En bref, il s'agit d'une API programmatique basée sur les promesses qui est censée charger dynamiquement vos modules et les mettre en cache afin que les imports ultérieurs ne rechargent pas une nouvelle version du module.

Cela ressemblera à quelque chose comme ceci :

**myModule.js**

**main.js**

Alternativement, vous pourriez également définir des modules en spécifiant "type=module" directement dans la balise script, comme ceci :

Si vous n'avez pas encore consulté le dépôt pour le polyfill de l'API de chargement de modules, je vous encourage fortement à au moins [jeter un coup d'œil](https://github.com/ModuleLoader/es6-module-loader).

De plus, si vous voulez tester cette approche, consultez [SystemJS](https://github.com/systemjs/systemjs), qui est construit sur le [polyfill de l'API de chargement de modules ES6](https://github.com/ModuleLoader/es6-module-loader). SystemJS charge dynamiquement tout format de module (modules ES6, AMD, CommonJS et/ou scripts globaux) dans le navigateur et dans Node. Il garde une trace de tous les modules chargés dans un "registre de modules" pour éviter de recharger les modules qui ont été précédemment chargés. Sans parler du fait qu'il transpile automatiquement les modules ES6 (si vous définissez simplement une option) et a la capacité de charger tout type de module à partir de tout autre type ! Plutôt pratique.

### Aurons-nous encore besoin de regroupeurs maintenant que nous avons des modules ES6 natifs ?

La popularité croissante des modules ES6 a des conséquences intéressantes :

#### HTTP/2 rendra-t-il les regroupeurs de modules obsolètes ?

Avec HTTP/1, nous ne sommes autorisés qu'une seule requête par connexion TCP. C'est pourquoi le chargement de plusieurs ressources nécessite plusieurs requêtes. Avec HTTP/2, tout change. HTTP/2 est entièrement multiplexé, ce qui signifie que plusieurs requêtes et réponses peuvent se produire en parallèle. En conséquence, nous pouvons servir plusieurs requêtes simultanément avec une seule connexion.

Puisque le coût par requête HTTP est considérablement inférieur à celui de HTTP/1, le chargement d'un tas de modules ne sera pas un énorme problème de performance à long terme. Certains soutiennent que cela signifie que le regroupement de modules ne sera plus nécessaire. C'est certainement possible, mais cela dépend vraiment de la situation.

Pour une chose, le regroupement de modules offre des avantages que HTTP/2 ne prend pas en compte, comme la suppression des exports inutilisés pour économiser de l'espace. Si vous construisez un site web où chaque petite partie de performance compte, le regroupement peut vous donner des avantages incrémentaux à long terme. Cela dit, si vos besoins en performance ne sont pas si extrêmes, vous pourriez potentiellement gagner du temps à un coût minimal en sautant l'étape de build.

Globalement, nous sommes encore assez loin d'avoir une majorité de sites web servant leur code via HTTP/2. Je suis enclin à prédire que le processus de build est là pour rester _au moins_ pour le court terme.

PS : Il y a d'autres différences avec HTTP/2 également, et si vous êtes curieux, voici une [excellente ressource](https://http2.github.io/faq/#what-are-the-key-differences-to-http1x).

#### CommonJS, AMD et UMD deviendront-ils obsolètes ?

Une fois que ES6 deviendra _le_ standard des modules, avons-nous vraiment besoin d'autres formats de modules non natifs ?

J'en doute.

Le développement web a beaucoup à gagner en suivant une méthode standardisée unique pour importer et exporter des modules en JavaScript, sans étapes intermédiaires. Combien de temps faudra-t-il pour atteindre le point où ES6 est le standard des modules ?

Il y a de fortes chances que cela prenne encore un certain temps ;)

De plus, il y a beaucoup de gens qui aiment avoir des "saveurs" parmi lesquelles choisir, donc l'approche "une seule vérité" peut ne jamais devenir une réalité.

### Conclusion

J'espère que cet article en deux parties a aidé à clarifier certains des termes techniques que les développeurs utilisent lorsqu'ils parlent de modules et de regroupement de modules. Allez-y et consultez la [partie I](https://medium.freecodecamp.com/javascript-modules-a-beginner-s-guide-783f7d7a5fcc#.y8hs0nsne) si vous avez trouvé l'un des termes ci-dessus confus.

Comme toujours, parlez-moi dans les commentaires et n'hésitez pas à poser des questions !

Bon regroupement :)
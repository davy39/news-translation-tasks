---
title: 'Présentation de Rekit Studio : un vrai IDE pour le développement React et
  Redux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-08T04:06:02.000Z'
originalURL: https://freecodecamp.org/news/introducing-rekit-studio-a-real-ide-for-react-and-redux-development-baf0c99cb542
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Qi68yRpDTFISfd_SFoy9HQ.png
tags:
- name: Rekit Studio
  slug: rekit-studio
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: 'Présentation de Rekit Studio : un vrai IDE pour le développement React
  et Redux'
seo_desc: 'By Nate Wang

  We’re very excited to announce the stable release of Rekit Studio, a complete IDE
  for React, Redux, and React Router development! Though it’s maybe new to some of
  you, it has helped us build complicated web apps for more than a year.


  Re...'
---

Par Nate Wang

Nous sommes très excités d'annoncer la sortie stable de [Rekit Studio](https://github.com/supnate/rekit), un IDE complet pour le développement React, Redux et React Router ! Bien qu'il soit peut-être nouveau pour certains d'entre vous, il nous a aidés à construire des applications web complexes depuis plus d'un an.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qi68yRpDTFISfd_SFoy9HQ.png)
_Rekit Studio_

La version précédente de Rekit Studio était Rekit Portal, qui n'avait pas la capacité d'éditer du code. Maintenant, grâce à [Monaco Editor](https://microsoft.github.io/monaco-editor/) (qui alimente également [VS Code](https://code.visualstudio.com/)) et à [prettier](https://prettier.io/) (un outil incroyable pour formater le code), Rekit Studio offre une excellente expérience de codage. C'est aussi pourquoi nous l'avons renommé de « portal » à « studio ».

En tant qu'IDE, outre l'édition de code, Rekit Studio offre des capacités de génération de code, de diagrammes de dépendances, de refactorisation, de construction, de tests unitaires et une manière significative de naviguer dans le code.

Vous n'aurez plus à vous soucier de la configuration du projet, de la configuration de webpack ou de l'organisation de votre structure de dossiers. Rekit Studio fournit une manière intégrée de gérer l'ensemble du projet. C'est ce qui rend Rekit Studio différent des autres éditeurs de code comme Sublime Text et VS Code.

### Voir la démonstration rapide

Avant l'introduction, vous pourriez vouloir voir une vidéo de démonstration rapide sur la façon d'utiliser Rekit Studio pour gérer les actions Redux.

À partir de la vidéo, nous pouvons voir que tout ce qui nous intéresse est la logique métier plutôt que le code boilerplate verbeux.

### Essayez-le maintenant

La meilleure façon de suivre l'introduction suivante est d'avoir Rekit Studio en cours d'exécution afin que vous puissiez essayer les fonctionnalités vous-même en temps réel. C'est super facile avec l'une de ces deux méthodes :

1. Accédez à la démonstration en direct : [http://demo.rekit.org](http://demo.rekit.org). Il s'agit d'une instance de Rekit Studio fonctionnant en mode lecture seule. Vous ne pouvez donc pas apporter de modifications au projet qu'il gère (le code de Rekit Studio lui-même !).
2. Créez une application Rekit vous-même en seulement 3 étapes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ziZR8esumzPQzl8dgzZ0lQ.png)

Ensuite, accédez à [http://localhost:6075](http://localhost:6075/) pour votre application. [http://localhost:6076](http://localhost:6076/) pour Rekit Studio par défaut.

Oui, Rekit Studio est un package npm dans votre projet et s'exécute dans un navigateur. Ce mécanisme garantit que chaque application a son propre Rekit Studio afin qu'il n'y ait jamais de problèmes de compatibilité de version.

### Affichez votre code de manière significative

Presque tous les IDE pour le développement front-end affichent les fichiers de la même manière que la structure des dossiers. Les gens se plaignent que la navigation entre les fichiers est frustrante. Pour aggraver les choses, il semble qu'il n'y ait aucun moyen de s'améliorer, car les éditeurs de code ne savent pas quel fichier est un composant, lequel est une action, quel fichier de style appartient à quel composant, où les règles de routage sont définies, et ainsi de suite. Tant que la structure du projet est en style libre, elle ne s'améliorera jamais.

Maintenant, Rekit suit le modèle de la manière dont une application web évolutive est organisée. Et sur cette base, Rekit Studio comprend votre projet. J'ai introduit les pratiques dans [deux](https://medium.com/@nate_wang/a-new-approach-for-managing-redux-actions-91c26ce8b5da) [articles](https://medium.com/@nate_wang/feature-oriented-architecture-for-web-applications-2b48e358afb0) précédents.

Sur la base de ce modèle, Rekit Studio sait quels fichiers sont des composants, lesquels sont des actions, où les règles de routage sont définies, et ainsi de suite. Ensuite, l'explorateur de projet peut afficher la structure du projet de manière significative, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*G-RnJg60bc2JPRqpSR78rg.png)
_Explorateur de projet_

Rekit Studio connaît les caractéristiques de ces éléments de projet, comme quelles actions sont asynchrones (avec la marque bleue « A »), quels composants se connectent au store Redux (avec la marque verte « C »), et quels composants sont gérés par React Router (avec la marque orange « R ») qui sont utilisés dans certaines règles de routage.

Avec cet explorateur de projet, vous pouvez facilement naviguer entre les éléments du projet. Vous pouvez également obtenir plus d'informations sur un élément sans l'ouvrir et regarder le code.

Une chose à souligner est que l'explorateur de projet n'affiche que les fichiers sous le dossier src dans le projet afin qu'il ait de bonnes performances. Donc, si vous voulez éditer des fichiers en dehors du dossier src, comme package.json ou .gitignore, vous pourriez avoir besoin d'un autre éditeur de texte.

### Génération de code

Tout comme d'autres vrais IDE comme Eclipse pour Java ou Visual Studio pour .Net, Rekit Studio aide à créer des boilerplates de code avec son interface intuitive sans aucun coût d'apprentissage. Par exemple, pour créer un composant, faites un clic droit sur un nœud de fonctionnalité dans l'explorateur de projet et cliquez sur `_Ajouter un composant_`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-FDtO-RMwk35KYdN8Rq-A.png)
_Ajouter un composant_

Outre lui donner un nom, vous pouvez définir s'il se connecte au store Redux ou s'il est utilisé dans une règle React Router. Après avoir cliqué sur `Ok`, il génère tout le code et les configurations nécessaires. Vous pouvez voir ce qu'il fait en arrière-plan par le journal des opérations. Il crée un fichier less/scss pour le style, un fichier de test pour les tests, il ajoute une règle React Router pour y accéder par URL (si le chemin d'URL est défini), et ainsi de suite.

Il n'y a pas de magie derrière cela — Rekit Studio vous aide simplement à faire automatiquement ce qui devait être fait manuellement auparavant. Et vous savez toujours ce qui s'est passé en vérifiant les journaux.

Pour créer une action Redux asynchrone, Rekit Studio utilise redux-thunk par défaut pour créer des réducteurs et des actions :

![Image](https://cdn-media-1.freecodecamp.org/images/1*C82XiyrFeWnHvRNpWVxLxg.png)
_Ajouter une action asynchrone_

Alternativement, vous pourriez créer des actions asynchrones en utilisant `redux-saga` en installant le plugin `rekit-plugin-redux-saga`. Voir le chapitre sur les plugins pour plus d'informations.

Tous les noms de fichiers, noms de fonctions ou noms de variables générés par Rekit sont forcés de suivre des règles prédéfinies comme décrit [ici](http://rekit.js.org/docs/namings.html). Donc, même si vous entrez un nom comme `my component` dans le champ de nom, Rekit le convertira en `MyComponent`. Avec cette approche, tous les noms dans le projet sont toujours cohérents.

Ces boilerplates de code sont créés en suivant les meilleures pratiques générales. Vous n'avez besoin que de remplir la logique métier à l'intérieur d'eux sans avoir à écrire de code verbeux manuellement. Une fois le code généré, vous pouvez l'éditer librement.

### La refactorisation est importante

Lors de la création d'une grande application, la refactorisation est très importante pour rendre le code propre, lisible et ensuite maintenable. Certaines des principales parties de la refactorisation sont le renommage, le déplacement et la suppression d'éléments de projet. Avec les technologies front-end modernes, ce travail devient excessivement difficile.

Par exemple, si nous voulons renommer une action asynchrone, cela nécessite généralement de toucher plusieurs fichiers et de modifier des dizaines de codes à différents endroits. Supposons que nous voulons renommer une action asynchrone de `fetchTopics` à `fetchTopicList`, cela nécessite ces modifications :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bj6CG2ZokEb7veblhSVMXg.png)

Cela semble si fou que vous ne voudriez jamais le faire manuellement, n'est-ce pas ? La même douleur existe dans le déplacement et la suppression de composants et d'actions. Sans l'aide de l'outil, cette douleur nous empêchait autrefois de refactoriser notre code. Cela a rendu notre projet difficile à maintenir en peu de temps.

Maintenant, avec Rekit Studio, vous pouvez faire un clic droit sur un composant ou une action pour le déplacer, le renommer ou le supprimer, tout comme vous le faites avec d'autres IDE comme Eclipse pour Java ou Visual Studio pour .Net. Rekit Studio fera tout automatiquement, et vous pouvez vérifier les journaux pour voir ce qu'il fait en arrière-plan.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TQD7FHHOH_4b82oVSk7Exg.png)

### Passez en revue votre projet avec des diagrammes intuitifs

Lorsque votre projet grandit, la relation de dépendance des modules devient compliquée. Cela conduit souvent à des problèmes de régression si vous ne les considérez pas entièrement. Il est bon de toujours garder la relation simple, afin que le code soit toujours compréhensible. Rekit Studio fournit deux types de diagrammes pour vous aider à passer en revue les dépendances :

**1. Le diagramme d'ensemble**
Il est affiché sur la page du tableau de bord (page d'accueil), avec laquelle nous pouvons voir non seulement les dépendances entre les fonctionnalités (un concept de haut niveau des applications Rekit), mais aussi les modules normaux comme les composants et les actions. Vous pourriez ainsi facilement trouver quels modules sont dangereux à refactoriser (avec de nombreuses dépendances) et lesquels sont faciles à refactoriser (avec moins de dépendances).

![Image](https://cdn-media-1.freecodecamp.org/images/1*teOjZ3d7qvPnNbNLsNLmIg.png)

Ce diagramme vous aide également à trouver ces modules inutilisés — par exemple, deux composants de la fonctionnalité `home` ne sont plus utilisés dans le projet comme le montre le diagramme ci-dessus. Vous pouvez les supprimer en toute sécurité. La suppression de code inutile aide à réduire la complexité du projet ainsi que la taille du bundle de l'application.

**2. Diagramme d'élément**

Ouvrez un élément à partir de l'explorateur de projet, puis vous pouvez voir le diagramme de l'élément sous l'onglet diagramme. Il fournit une vue très intuitive de la manière dont un élément est créé ou utilisé par d'autres. C'est la complication d'un module.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wuno2b4rxwKjH3LFoV8oCA.png)

Par exemple, SidePanel est un composant compliqué qui utilise de nombreux autres composants et actions. Et il a des dépendances d'autres fonctionnalités. Peut-être est-ce un composant à refactoriser pour devenir simple et facile à comprendre.

### Construction et tests

En tant qu'IDE, Rekit Studio peut également construire et tester le projet avec des interfaces intuitives. Par défaut, Rekit Studio essaiera d'exécuter la commande `npm run build` pour construire le projet, et exécutera `npm test — [test-file-pattern]` pour exécuter les tests unitaires.

Pour construire le projet, cliquez sur l'élément de menu `Build` dans le menu principal :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6uzaiTyQVqGOW-XS64J3BQ.png)

Ensuite, vous pouvez voir une barre de progression et le résultat de la construction. Avant de déployer sur le serveur de production, vous pouvez également vérifier le résultat de la construction en accédant au serveur dist qui, par défaut, s'exécute à l'adresse suivante : [http://localhost:6077](http://localhost:6077).

Pour exécuter les tests unitaires, vous pouvez soit exécuter tous les tests en cliquant sur l'élément de menu `Run tests` dans le menu principal, soit faire un clic droit sur un fichier/dossier qui contient des tests. Rekit Studio convertira automatiquement la commande pour tester le modèle de fichier :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hsJ24ftjGGslgZ5Fy31z8g.png)

Ci-dessus se trouve le résultat du test de la fonctionnalité `diagram`. Si vous exécutez tous les tests du projet, il générera un rapport de couverture des tests. Vous pouvez y accéder à partir du menu principal :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qcXXiGFt3kswaX99-OLqcg.png)

### Système de plugins

Nous pouvons voir que Rekit Studio peut créer des boilerplates de fonctionnalités, d'actions et de composants. Si vous souhaitez créer de nouveaux éléments comme des sélecteurs, ou si vous souhaitez modifier le boilerplate de code par défaut (comme utiliser `redux-saga` au lieu de `redux-thunk` pour les actions asynchrones), vous pouvez créer des plugins pour le faire.

Voir plus sur le système de plugins [ici](http://rekit.js.org/docs/plugin.html).

### Interface de ligne de commande

Outre Rekit Studio, il existe une autre [interface de ligne de commande](http://rekit.js.org/docs/cli.html) pour gérer un projet Rekit. En fait, Rekit Studio et Rekit CLI utilisent tous deux `rekit-core` pour gérer les éléments du projet. Le système CLI prend en charge plus de types de plugins. Et Rekit Studio sera amélioré à l'avenir pour fournir une interface utilisateur unifiée pour le système de plugins.

### Migration de Rekit Portal à Rekit Studio

Si votre projet existant a été utilisant Rekit Portal, il est super facile de migrer vers Rekit Studio, car Rekit Studio est complètement compatible avec les projets Rekit précédents. Tout ce que vous avez à faire est d'installer Rekit Studio et de mettre à jour le script pour le démarrer dans server.js [ici](https://github.com/supnate/rekit-boilerplate/commit/5186b5c3ec141b5306471c52a8955dfb288598bd).

### Transformation de votre projet en un projet Rekit

Si vous avez créé un projet utilisant React, Redux et React Router, il est possible de le convertir en un projet Rekit afin que vous puissiez utiliser Rekit Studio pour le gérer. Ce n'est pas si difficile, mais le sujet nécessite un autre article pour l'introduire correctement. Je l'écrirai si vous le souhaitez — faites-le moi savoir dans les commentaires. Le point clé est de réorganiser vos fichiers et votre code à la manière Rekit.

### Qu'est-ce qui suit

Rekit Studio est encore dans ses premiers stades, bien que nous l'utilisions pour construire des applications web depuis longtemps maintenant. Nous continuerons à l'améliorer au fur et à mesure que nous l'utiliserons dans notre travail quotidien.

Certains candidats de haute priorité sont listés ci-dessous :

* Meilleure mise en évidence de la syntaxe du code.
* Prise en charge des règles ESlint personnalisées.
* Meilleure complétion automatique du code, comme l'installation des noms de modules.
* Ouverture rapide des fichiers en utilisant Cmd + P.
* Prise en charge de plusieurs fichiers non enregistrés. Actuellement, un seul fichier peut être dans un état non enregistré pour garder votre code en sécurité.
* Ajouter plus de types de diagrammes.
* Permettre aux utilisateurs de créer/renommer/supprimer des fichiers normaux en plus des composants et des actions.
* Intégrer Storybook.
* Prise en charge de TypeScript.
* Prise en charge du rendu côté serveur.

La liste pourrait être longue, et elle dépend de vos retours — nous accueillons tous ceux que vous pourriez avoir.

### Résumé

Bien que la technologie front-end évolue très rapidement, Rekit, en tant que boîte à outils plutôt qu'un framework, a été très stable depuis plus de deux ans. Les pratiques qu'il suit sont indépendantes des technologies. Maintenant, la sortie de Rekit Studio est une nouvelle étape pour nous améliorer notre expérience de codage. Nous espérons que vous l'aimerez aussi !

Enfin, je veux souligner que Rekit ne fournit aucun SDK ou packages npm pour votre application. C'est uniquement un outil pour créer et gérer le projet. Même sans Rekit, vous pouvez utiliser n'importe quel éditeur de texte pour écrire du code et utiliser le terminal pour exécuter des scripts pour un projet Rekit. C'est-à-dire que vous utilisez Rekit, mais vous n'en dépendez pas.
---
title: 'Comment créer une application de bureau Electron en JavaScript : Multithreading,
  SQLite, Modules natifs et autres points sensibles courants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-07T06:13:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-electron-desktop-app-in-javascript-multithreading-sqlite-native-modules-and-1679d5ec0ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DvoIqsg-hw9KaExCOYM89A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 'Comment créer une application de bureau Electron en JavaScript : Multithreading,
  SQLite, Modules natifs et autres points sensibles courants'
seo_desc: 'By Andrew Walsh

  As a framework for developing desktop applications, Electron has a lot to offer.
  It grants full access to Node’s API and ecosphere. It deploys on all major operating
  systems (with a single codebase). And with its web-based architectur...'
---

Par Andrew Walsh

En tant que framework pour développer des applications de bureau, Electron a beaucoup à offrir. Il donne un accès complet à l'API de Node et à son écosystème. Il se déploie sur tous les principaux systèmes d'exploitation (avec une seule base de code). Et avec son architecture basée sur le web, vous pouvez utiliser les dernières fonctionnalités de CSS pour créer des interfaces utilisateur avancées.

Il existe de nombreux articles sur la mise en route avec Electron, mais peu sont dédiés à l'utilisation de SQLite ou à la manière de procéder au multithreading. Nous allons voir comment utiliser Electron pour construire des applications qui gèrent de grandes quantités de données ou exécutent de nombreuses tâches.

En particulier, nous aborderons :

* Comment Electron fonctionne (en bref), et comment son architecture affecte ce que nous pouvons faire
* Le multithreading
* L'utilisation de bases de données locales telles que SQLite, ou l'écriture dans un fichier à l'intérieur d'une application Electron
* Les modules natifs
* Quelques pièges à connaître
* L'emballage d'une application utilisant des modules natifs

### **Comment Electron fonctionne — version abrégée**

![Image](https://cdn-media-1.freecodecamp.org/images/keOEXfrPYcN9EhRMyl2h49AepZe-6YtXRP3J)

Il vaut la peine de répéter les principes clés derrière l'architecture d'Electron. Une application Electron se compose d'au moins deux processus. Le thread principal est le point d'entrée de votre application et effectue tout le travail nécessaire pour afficher votre processus de rendu (ou processus) à vos utilisateurs. Il ne peut y avoir qu'une seule instance du processus principal.

Les processus de rendu utilisent Chromium pour rendre votre application. Tout comme chaque onglet s'exécute dans son propre processus, chaque processus de rendu le fait également. Ils sont chargés en utilisant le constructeur [BrowserWindow](https://github.com/electron/electron/blob/master/docs/api/browser-window.md) de la méthode [loadURL](https://github.com/electron/electron/blob/master/docs/api/browser-window.md#winloadurlurl-options), qui doit pointer vers un fichier HTML local ou distant. Cela signifie que la seule façon de démarrer un processus de rendu est d'utiliser un fichier HTML comme point d'entrée.

#### **Avertissements concernant l'architecture d'Electron**

La simplicité d'Electron est l'un de ses plus grands atouts. Votre processus principal effectue toute configuration nécessaire puis transmet un fichier HTML ou une URL au processus de rendu. Ce fichier peut faire tout ce qu'une application web régulière peut faire — et vous êtes prêt à partir de là.

Mais le fait qu'il ne puisse y avoir qu'un seul processus principal rend flou la manière d'implémenter le multithreading. La documentation d'Electron implique que les processus de rendu sont strictement conçus pour la tâche de rendu des interfaces utilisateur (ce qui, comme nous le verrons, n'est pas vrai).

Il est important de savoir que [faire quoi que ce soit d'intensif en calcul sur le processus principal ralentira](https://medium.com/actualbudget/the-horror-of-blocking-electrons-main-process-351bf11a763c) (ou gelera) vos processus de rendu. Il est crucial que tout travail intensif en calcul soit déplacé hors du thread principal. Il est préférable de le laisser uniquement à la tâche de faire tout ce qui est nécessaire pour démarrer vos processus de rendu. Puisque nous ne pouvons pas faire de travail intensif sur le même processus de rendu qui rend l'interface utilisateur de l'application (car cela affectera également l'UI), nous avons besoin d'une autre approche.

### **Multithreading**

![Image](https://cdn-media-1.freecodecamp.org/images/nSgrPDUeijHdeOrJtPUcNVzOuUPBf125BGO1)

Il existe trois approches générales pour le multithreading dans Electron :

* Utiliser des web workers
* Forker de nouveaux processus pour exécuter des tâches
* Exécuter des processus de rendu (cachés) comme workers

#### **Web workers**

Puisqu'Electron est construit sur Chromium, tout ce qui peut être fait sur un navigateur peut être fait dans un processus de rendu. Cela signifie que vous pouvez utiliser des [web workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) pour exécuter des tâches intensives dans des threads séparés. L'avantage de cette approche est la simplicité et le maintien de l'isomorphisme avec une application web.

Cependant, il y a un très grand avertissement — vous ne pouvez pas utiliser de modules natifs. Techniquement, vous pouvez, mais cela [fera planter votre application](https://github.com/electron/electron/blob/master/docs/tutorial/multithreading.md#native-nodejs-modules). C'est un problème significatif, car toute application nécessitant du multithreading peut également avoir besoin d'utiliser des modules natifs (comme [node-sqlite3](https://github.com/mapbox/node-sqlite3)).

#### **Forker de nouveaux processus**

Electron utilise Node comme runtime, ce qui signifie que vous avez un accès complet aux modules intégrés comme [cluster](https://nodejs.org/api/cluster.html). De nouveaux processus peuvent être forkés pour exécuter des tâches, gardant le travail intensif hors du thread principal.

Le principal problème est que, contrairement aux processus de rendu, les processus enfants ne peuvent pas utiliser les méthodes de la bibliothèque Electron. Cela vous oblige à maintenir un canal de communication avec le processus principal via IPC. Les processus de rendu peuvent utiliser le [module remote](https://github.com/electron/electron/blob/master/docs/api/remote.md) pour dire au processus principal d'effectuer des tâches principales sans cette étape supplémentaire.

Un autre problème est que si vous utilisez des modules ES ou des fonctionnalités TC39 de JavaScript, vous devrez vous assurer que vous exécutez des versions transpilées de vos scripts. Vous devrez également les inclure dans votre application emballée. Ce problème affecte toute application Node qui fork des processus, mais il ajoute une autre couche de complexité à votre processus de construction. Cela peut également devenir délicat lorsque vous équilibrez les exigences de l'emballage de votre application avec l'utilisation d'outils de développement qui utilisent des fonctionnalités telles que le rechargement en direct.

#### **Utiliser des processus de rendu comme threads de travail**

Les processus de rendu sont conventionnellement traités comme étant utilisés pour rendre votre UI. Cependant, ils ne sont pas liés à cette seule tâche. Ils peuvent être cachés et s'exécuter en arrière-plan en [configurant le flag show](https://github.com/electron/electron/blob/master/docs/api/browser-window.md#new-browserwindowoptions) passé à BrowserWindow.

Faire cela présente de nombreux avantages. Contrairement aux web workers, vous avez la liberté d'utiliser des modules natifs. Et contrairement aux processus forkés, vous pouvez toujours utiliser la bibliothèque electron pour dire au processus principal de faire des choses comme ouvrir une boîte de dialogue ou créer des notifications OS.

Un défi lors de l'utilisation d'Electron est [IPC](https://github.com/electron/electron/blob/master/docs/api/ipc-main.md). Bien que simple, il nécessite une quantité importante de code boilerplate et impose la difficulté de déboguer de grands nombres d'écouteurs d'événements. C'est aussi une autre chose que vous devez tester unitairement. En utilisant un processus de rendu comme thread de travail, vous pouvez contourner cela complètement. Tout comme vous le feriez avec un serveur, vous pouvez écouter sur un port local et recevoir des requêtes, vous permettant d'utiliser des outils tels que [GraphQL](https://graphql.org/learn/) + [React Apollo](https://github.com/apollographql/react-apollo). Vous pouvez également utiliser des websockets pour la communication en temps réel. Un autre bonus est que vous n'avez pas besoin d'utiliser ipcRenderer, et pouvez garder vos applications Electron et web isomorphes (si vous souhaitez utiliser une base de code partagée pour une application de bureau et web).

Pour des cas d'utilisation avancés, cette approche peut être combinée avec le clustering pour obtenir le meilleur de tous les mondes. Le seul inconvénient est que vous devrez fournir un fichier HTML comme entrée pour vos processus de rendu workers (ce qui semble un peu être un hack).

### **Comment utiliser SQLite (ou tout ce à quoi vous devez écrire)**

![Image](https://cdn-media-1.freecodecamp.org/images/dtC2ic6Yczjpbr3W9QCkY-rotuXLDfPWmjMe)

Il existe plusieurs approches pour la gestion d'état qui ne nécessitent pas de modules natifs. Par exemple, gérer tout votre état dans le contexte d'un rendu avec Redux.

Cependant, si vous devez gérer de grandes quantités de données, cela ne suffira pas. En particulier, nous allons voir comment utiliser SQLite dans une application Electron.

Pour déployer votre application Electron, vous devrez d'abord l'emballer. Il existe plusieurs outils disponibles pour cela — le plus populaire étant [Electron Builder](https://github.com/electron-userland/electron-builder). Electron utilise le format d'archive ASAR pour regrouper votre application en un seul fichier non compressé. Les archives ASAR sont en lecture seule — ce qui signifie que vous ne pouvez pas écrire de données dedans. Cela signifie que vous ne pouvez pas inclure votre base de données dans votre archive ASAR avec le reste de votre code (dans electron builder, cela serait sous « [files](https://www.electron.build/configuration/configuration) »).

Au lieu de cela, incluez votre base de données dans le répertoire Resources de votre package electron. La structure de fichiers d'une application Electron emballée et où placer votre base de données peut être vue ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Ma0VJabKd0W1PcjbsYYSVnnYkFMwOKdsiSuH)

L'archive ASAR emballée appelée app.asar existe dans ./Contents/Resources. Vous pouvez placer votre base de données, ou tout fichier auquel vous souhaitez écrire mais inclure dans votre application emballée, dans le même répertoire. Cela peut être réalisé avec Electron Builder en utilisant la configuration « [extraResources](https://www.electron.build/configuration/contents) ».

Une autre approche consiste à créer une base de données dans un autre répertoire entièrement. Mais vous devrez tenir compte de la suppression de ce fichier sur toutes les plateformes si les utilisateurs décident de désinstaller votre application.

### **Emballage avec des modules natifs**

La grande majorité des modules Node sont des scripts écrits en JavaScript. Les [modules natifs](https://nodejs.org/api/addons.html#addons_c_addons) sont des modules écrits en C++ qui ont des liaisons pour une utilisation avec Node. Ils agissent comme une interface vers d'autres bibliothèques écrites en C/C++, et sont généralement configurés pour compiler après l'installation.

En tant que modules de bas niveau, ils doivent être compilés pour les architectures et systèmes d'exploitation cibles. Un module natif compilé sur une machine Windows ne fonctionnera pas sur une machine Linux — même si un module régulier le ferait. C'est un problème pour Electron, car nous devons finalement tout emballer dans un exécutable .dmg (OSX), .exe (Windows) ou .deb (Linux).

Les applications Electron utilisant des modules natifs doivent être emballées sur le système qu'elles ciblent. Puisque vous voudrez automatiser ce processus dans un pipeline CI/CD, vous devrez construire vos dépendances natives avant l'emballage. Pour y parvenir, vous pouvez utiliser un outil développé par l'équipe Electron appelé [electron-rebuild](https://github.com/electron/electron-rebuild).

Si vous développez un projet open source non commercial, vous pouvez utiliser [TravisCI](https://travis-ci.org/) (Linux, OSX) et [Appveyor](https://www.appveyor.com/) (Windows) pour construire, tester et déployer automatiquement votre application gratuitement.

La configuration de cela peut être délicate si vous avez des tests d'intégration, car vous devrez installer certaines dépendances pour que les tests headless fonctionnent. Un exemple de configuration pour OSX et Linux avec TravisCI peut être trouvé [ici](https://github.com/AndrewGHC/mail-post/blob/master/.travis.yml), et un exemple de configuration Appveyor [ici](https://github.com/AndrewGHC/mail-post/blob/master/appveyor.yml) (ces exemples sont basés sur la configuration du projet [electron-react-boilerplate](https://github.com/chentsulin/electron-react-boilerplate), avec l'ajout d'OSX et de déploiement).

### **Pièges**

Lorsque votre application Electron est emballée, certaines propriétés intégrées de Node relatives aux chemins peuvent ne pas se comporter comme vous l'attendez et ne se comporteront pas comme elles le font lorsque vous exécutez le binaire préconstruit pour servir votre application.

Des variables telles que __dirname, __filename et des méthodes comme process.cwd ne se comporteront pas comme prévu dans une application emballée (voir les problèmes [ici](https://github.com/electron/electron/issues/3204), [ici](https://github.com/electron/electron/issues/8358), et [ici](https://github.com/electron/electron/issues/2108)). Utilisez [app.getAppPath](https://github.com/electron/electron/blob/master/docs/api/app.md#appgetapppath) à la place.

### **Une note finale sur l'emballage**

Lors du développement d'une application Electron, vous pouvez vouloir utiliser à la fois les modes production (servir du code bundlé avec le binaire préconstruit) et développement (utiliser [webpack-dev-server](https://github.com/webpack/webpack-dev-server) ou [webpack-serve](https://github.com/webpack-contrib/webpack-serve) pour surveiller vos fichiers).

Pour garder votre santé mentale, construisez et servez vos bundles à partir du même répertoire que votre code source. Cela signifie que lorsque vous sélectionnez ces fichiers pour l'emballage, toute hypothèse sur les chemins de fichiers reste cohérente entre ces modes et votre package.

À tout le moins, votre processus principal devra pointer vers le chemin de fichier du fichier HTML de vos processus de rendu. Si vous déplacez ce fichier dans un autre répertoire dans le cadre de votre processus de construction, vous serez obligé de maintenir des hypothèses sur la structure des fichiers et cela peut rapidement devenir une autre couche de complication fastidieuse que vous devez maintenir.

Le débogage des problèmes liés aux chemins de fichiers incorrects dans une application emballée est très beaucoup une question d'essais et d'erreurs.

### **Résumé**

![Image](https://cdn-media-1.freecodecamp.org/images/fwQjnBH2Taw7dUyakJKN8AUoxpwMaV8ZqCde)

Il existe plusieurs approches pour le multithreading dans Electron. Les web workers sont pratiques, mais manquent de la capacité d'utiliser des modules natifs. Forker de nouveaux processus fonctionne comme cela le ferait dans Node, mais le manque de capacité à utiliser la bibliothèque Electron force l'utilisation d'IPC pour les tâches courantes et peut rapidement devenir compliqué. Utiliser des processus de rendu comme workers accorde toute la puissance de tous les outils de serveur Node disponibles comme remplacement pour la communication via IPC, tout en conservant l'accès aux modules natifs et aux méthodes de la bibliothèque de rendu Electron.

Puisqu'Electron emballe les fichiers dans une archive ASAR en lecture seule, tout fichier auquel nous devons écrire (comme une base de données SQLite) ne peut pas être inclus. Au lieu de cela, ceux-ci peuvent être placés dans le répertoire Resources où ils resteront dans l'application emballée.

Enfin, soyez conscient du fait que dans une application emballée, certaines propriétés de Node ne se comportent pas comme vous l'attendez. Et pour la clarté d'esprit, faites correspondre la structure de fichiers de votre application emballée avec votre code source.
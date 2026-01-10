---
title: Comment configurer un projet TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T18:24:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-typescript-project-67b427114884
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wyxuq21keffc5b0d_lMkUw.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
- name: webpack
  slug: webpack
seo_title: Comment configurer un projet TypeScript
seo_desc: 'By David Piepgrass

  A thorough guide for beginners making web apps with React


  _Photo by [Unsplash](https://unsplash.com/photos/ZMraoOybTLQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Art...'
---

Par David Piepgrass

#### Un guide complet pour les débutants créant des applications web avec React

![Image](https://cdn-media-1.freecodecamp.org/images/1*wyxuq21keffc5b0d_lMkUw.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/ZMraoOybTLQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Artem Sapegin</a> sur <a href="https://unsplash.com/search/photos/project?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

En toutes mes années en tant que développeur, je n'ai jamais rencontré une jungle aussi écrasante que Le Monde JavaScript. C'est un monde d'une complexité déconcertante, où la création d'un projet très simple semble nécessiter l'installation de nombreux outils, la modification de plusieurs fichiers texte qui relient tous ces outils ensemble, et l'exécution d'une série de commandes terminal.

Il existe certains outils qui tentent de cacher cette complexité, avec des degrés de succès variables. Mais tant que ces outils n'ont pas une adoption universelle, ils me semblent simplement être encore plus de choses à apprendre en plus de tout le reste.

Pour moi, la plus grande source d'irritation est que la plupart des tutoriels supposent que vous êtes **déjà** familiarisé avec l'écosystème, donc ils ne se donnent pas la peine d'expliquer les bases. Pour empirer les choses, de nombreux tutoriels tentent de vous imposer une série d'outils supplémentaires — comme [Webpack](https://webpack.js.org/), [Bower](https://bower.io/), [NVM](https://github.com/creationix/nvm), et [Redux](https://redux.js.org/) — avec peu d'explications.

C'est ironique, car JavaScript lui-même est déjà installé sur pratiquement tous les ordinateurs du monde, y compris les téléphones. Pourquoi écrire une application de manière "professionnelle" doit-il être si complexe comparé à l'écriture d'un fichier HTML avec un peu de code JavaScript dedans ?

Si, comme moi, vous avez un **besoin inné** de comprendre ce qui se passe et :

* si vous ne supportez pas de copier aveuglément des commandes dans des terminaux et des fichiers texte
* si vous voulez vous assurer d'avoir besoin d'un outil avant de l'installer
* si vous vous demandez pourquoi votre projet basé sur npm fait 50 Mo avant même d'avoir écrit votre première ligne de code

alors bienvenue ! Vous êtes au bon endroit.

D'un autre côté, si vous vouliez commencer à programmer en 5 minutes chrono, je connais une astuce pour cela : sautez l'introduction ici et commencez à lire sur [l'Approche A](https://medium.com/p/67b427114884#682d) dans la Section 2. Ou si vous pensez que je vous donne trop d'informations, sautez simplement les parties que vous ne voulez pas apprendre en cours de route.

Dans ce tutoriel, je supposerai que vous avez **quelque** expérience de programmation avec HTML, CSS et JavaScript, mais **aucune** expérience avec [TypeScript](https://www.typescriptlang.org/), [React](https://reactjs.org/), ou [Node.js](https://nodejs.org/en/).

Je vous donnerai un aperçu de l'écosystème JavaScript tel que je le comprends. Je vous expliquerai pourquoi je pense que TypeScript et React (ou [Preact](https://preactjs.com/)) sont votre meilleur choix pour créer des applications web. Et je vous aiderai à démarrer un projet sans extras inutiles.

Dans la section 2, nous discuterons de la manière et des raisons d'ajouter des extras à votre projet, **si** vous décidez que vous en avez besoin.

### Table des matières

[Section 1 : Aperçu de l'écosystème JavaScript](https://medium.com/p/67b427114884#51cb)

[Section 2 : Configuration réelle du projet](https://medium.com/p/67b427114884#7248)

* [Étapes communes](https://medium.com/p/67b427114884#682d)
* [Approche A : La manière facile](https://medium.com/p/67b427114884#719b)
* [Autres approches](https://medium.com/p/67b427114884#3e81)
* [Approche B : La manière avec le moins d'outils](https://medium.com/p/67b427114884#9220)
* [Approche C : La manière Webpack](https://medium.com/p/67b427114884#9b91)
* [Résumé](https://medium.com/p/67b427114884#0690)

### Section 1 : Aperçu de l'écosystème JavaScript

Pour de nombreux langages de programmation, il existe une certaine manière de faire les choses que tout le monde connaît.

Par exemple, si vous voulez créer une application C#, vous installez [Visual Studio](https://visualstudio.microsoft.com/), créez un projet Windows Forms avec quelques clics de souris, cliquez sur le bouton vert "play" pour exécuter votre nouveau programme, puis commencez à écrire du code pour celui-ci. Le gestionnaire de paquets ([NuGet](https://www.nuget.org/)) est intégré et le débogueur fonctionne simplement. Bien sûr, cela peut prendre quelques heures pour installer l'IDE, et [WPF](https://docs.microsoft.com/en-us/dotnet/framework/wpf/getting-started/introduction-to-wpf-in-vs) est aussi amusant que de se cogner la tête contre un mur de briques, mais au moins **commencer** est facile. (Sauf si vous n'utilisez pas Windows, alors c'est totalement différent, mais je m'égare.)

En JavaScript, en revanche, il existe de nombreuses bibliothèques et outils concurrents pour presque tous les aspects du processus de développement. Ce barrage d'outils peut devenir écrasant avant même d'avoir écrit votre première ligne de code ! Lorsque vous allez sur Google pour chercher "comment écrire une application web", chaque site web que vous visitez semble donner des conseils différents.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IP44ejhk2c78Nt_xUckWbw.png)
_Merci [draw.io](https://draw.io" rel="noopener" target="_blank" title=") pour l'outil de diagramme !_

La seule chose sur laquelle la plupart des gens semblent s'accorder est l'utilisation du Node Package Manager ([NPM](https://www.npmjs.com/)) pour télécharger des bibliothèques JavaScript (à la fois côté serveur et navigateur uniquement). Mais même ici, certaines personnes utilisent [Yarn](https://yarnpkg.com/en/), qui est compatible avec npm, ou éventuellement Bower.

NPM est fourni avec Node.js, un serveur web que vous contrôlez entièrement avec du code JavaScript. NPM est étroitement intégré avec Node. Par exemple, la commande `npm start` exécute `node server.js` par défaut.

Même si vous prévoyez d'utiliser un autre serveur web (ou de ne pas utiliser de serveur web du tout et de simplement double-cliquer sur un fichier HTML), tout le monde semble supposer que vous aurez Node.js installé. Donc vous pouvez aussi bien aller de l'avant et [installer node.js](https://nodejs.org/en/download/) qui vous donne `npm` en bonus.

Node.js n'est pas seulement un serveur web — il peut également exécuter des applications en ligne de commande écrites en JavaScript. En ce sens, le compilateur TypeScript est une application Node.js !

Au-delà de NPM, vous avez plusieurs choix :

#### Quelle version de JavaScript souhaitez-vous utiliser ?

Le nom officiel de JavaScript est en fait ECMAScript, et la version la plus largement déployée est ECMAScript 6 ou ES6 en abrégé. Les anciens navigateurs, notamment Internet Explorer, ne supportent que ES5.

ES6 ajoute de nombreuses fonctionnalités utiles et importantes telles que les modules, let, const, les fonctions fléchées (ou fonctions lambda), les classes, et l'affectation par déstructuration.

ES7 ajoute quelques fonctionnalités supplémentaires, notamment quelque chose appelé async/await.

Si vous n'avez pas besoin de supporter les anciens navigateurs et que votre code n'est pas très volumineux, exécuter votre code directement dans le navigateur est une option attrayante, car vous n'avez pas besoin de "compiler" votre JavaScript avant de l'ouvrir dans le navigateur.

**Mais** il y a de nombreuses raisons d'utiliser une étape de compilation :

* Si vous devez supporter les anciens navigateurs, vous aurez besoin d'un "transpileur" pour pouvoir utiliser les nouvelles fonctionnalités de JavaScript dans les anciens navigateurs. Un transpileur est un compilateur dont le code de sortie est un langage de haut niveau, dans ce cas JavaScript. Je suppose que le transpileur le plus populaire est [Babel](https://babeljs.io/), avec [TypeScript](https://www.typescriptlang.org/) en deuxième position.
* Si vous voulez utiliser le framework populaire React (mais sans TypeScript), vous écriverez probablement du code "JSX" — des fragments de XML à l'intérieur du code JavaScript. JSX n'est pas supporté par les navigateurs et nécessite donc un préprocesseur (généralement Babel).
* Si vous voulez "minifier" votre code pour qu'il utilise moins de bande passante (ou soit obfusqué), vous aurez besoin d'un préprocesseur "minifier". Les [minifiers populaires](http://typescript-react-primer.loyc.net/minification.html) incluent UglifyJS, JSMin, et le Closure Compiler.
* Si vous voulez une vérification de type ou une complétion de code de haute qualité (également connue sous le nom d'IntelliSense), vous voudrez utiliser TypeScript, un sur-ensemble de JavaScript (ce qui signifie que chaque fichier JavaScript est également un fichier TypeScript... ostensiblement). TypeScript supporte à la fois les fonctionnalités ES7 et JSX, et sa sortie est du code ES5 ou ES6. Lorsque TypeScript et le code JSX sont utilisés ensemble, l'extension de fichier doit être `.tsx`. Certaines personnes utilisent un langage différent, similaire en concept à TypeScript, appelé Flow.
* Si vous n'aimez pas JavaScript, vous pourriez essayer un langage totalement différent qui se transpile en JavaScript, comme Elm, ClojureScript, ou Dart.

Heureusement, il est possible d'automatiser la compilation pour que votre code soit recompilé chaque fois que vous enregistrez un fichier.

Ce tutoriel utilise TypeScript, un sur-ensemble de JavaScript avec un système de types complet. Les avantages de TypeScript sont que :

1. Vous obtenez des messages d'erreur du compilateur lorsque vous faites des erreurs liées aux types (au lieu de découvrir les erreurs indirectement lorsque votre programme se comporte mal). Dans les IDE comme Visual Studio Code, vos erreurs sont soulignées en rouge.
2. Vous pouvez obtenir des fonctionnalités de refactorisation. Par exemple, dans Visual Studio Code, appuyez sur `**F2**` pour renommer une fonction ou une variable dans plusieurs fichiers, sans affecter d'autres choses qui ont le même nom.
3. Les types permettent aux IDE de fournir des popups de complétion de code, également connus sous le nom d'IntelliSense, ce qui rend la programmation beaucoup plus facile car vous n'avez pas à mémoriser tous les noms et arguments attendus des fonctions que vous appelez :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hDqFqucAtKLhDzEpACzsFA.png)
_IntelliSense de Visual Studio Code_

**Astuce** : Pour jouer avec TypeScript sans rien installer, [visitez son terrain de jeu](http://www.typescriptlang.org/play/).

#### Client versus serveur

Vous pouvez exécuter du code dans un client (navigateur front-end), un serveur (back-end Node.js), ou les deux. Le client n'est pas sous votre contrôle. L'utilisateur peut utiliser Firefox, Chrome, Safari, Opera, Edge, ou dans le pire des cas, Internet Explorer.

Pour des raisons de sécurité, gardez à l'esprit que l'utilisateur peut modifier le comportement d'un navigateur en utilisant des extensions de navigateur ou les outils de développement `**F12**`. Vous ne pouvez même pas être sûr que votre code s'exécute dans un vrai navigateur.

Les développeurs avaient l'habitude de s'appuyer sur la bibliothèque [jQuery](https://jquery.com/) pour obtenir un comportement cohérent dans différents navigateurs, mais de nos jours, vous pouvez compter sur différents navigateurs pour se comporter de la même manière dans **la plupart** des cas (sauf peut-être Internet Explorer).

Dans ce tutoriel, nous exécuterons tout le code important dans le navigateur, mais nous mettrons également en place un simple serveur Node.js pour servir l'application au navigateur. De nombreux autres serveurs sont disponibles, tels que [Apache](https://httpd.apache.org/), [IIS](https://www.iis.net/), ou un serveur statique comme [Jekyll](https://jekyllrb.com/).

Mais Node.js est devenu une sorte de standard, probablement parce que Node.js et NPM sont regroupés ensemble.

#### Frameworks d'interface utilisateur

HTML et CSS seuls sont excellents pour les articles classiques avec des images, ou des formulaires simples. Si c'est tout ce que vous faites, il n'y a probablement pas besoin de JavaScript du tout. CSS peut même faire certaines choses qui nécessitaient autrefois JavaScript, comme les [menus déroulants](https://www.cssscript.com/pure-css-mobile-compatible-responsive-dropdown-menu/), les pages qui se [reformattent complètement pour les petits navigateurs mobiles ou l'impression](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries), et les [animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations).

Si vous avez besoin de quelque chose de plus complexe que cela, ou si vos pages sont générées dynamiquement à partir de données brutes, vous voudrez probablement utiliser JavaScript avec une bibliothèque ou un framework d'interface utilisateur optionnel. Je vous montrerai [plus tard](http://typescript-react-primer.loyc.net/tutorial-5.html) comment utiliser React, qui a gagné une position de framework UI le plus populaire, et son petit cousin Preact.

Les [alternatives populaires](https://stateofjs.com/2017/front-end/results) "grandes" incluent [Angular 2](https://angular.io/) et [Vue.js](https://vuejs.org/), tandis que les "petites" incluent [D3](https://d3js.org/), [Mithril](https://mithril.js.org/) et un classique ancien appelé jQuery.

Si votre serveur web exécute JavaScript (Node.js), vous pouvez exécuter React sur le serveur pour pré-générer l'apparence initiale de la page.

#### Outils de construction

Plusieurs [outils pour "construire" et "packager" votre code](https://stateofjs.com/2017/build-tools/results) sont disponibles — Webpack, [Grunt](https://gruntjs.com/), [Browserify](http://browserify.org/), [Gulp](https://gulpjs.com/), [Parcel](https://parceljs.org/) — mais toutes ces choses sont optionnelles. Je vous montrerai comment vous en sortir avec juste `npm` et, si vous le souhaitez, Parcel ou Webpack.

#### Variantes de CSS

Dans cet article, nous utiliserons du CSS simple. Si vous allez avoir une étape de compilation de toute façon, vous pourriez vouloir essayer SCSS, une dérivée "améliorée" de CSS avec des fonctionnalités supplémentaires. Ou vous pourriez utiliser SASS, qui est conceptuellement identique à SCSS mais a une syntaxe plus concise.

Dans les deux cas, vous aurez besoin du [préprocesseur Sass](https://sass-lang.com/). Et comme toujours dans le Monde JavaScript, il existe [une série d'alternatives](https://stateofjs.com/2017/css/results/), notamment [LESS](http://lesscss.org/).

#### Tests unitaires

Les bibliothèques de tests unitaires populaires sont [Mocha](https://mochajs.org/), [Jasmine](https://jasmine.github.io/) et [Jest](https://jestjs.io/). [Voir ici pour plus](https://stateofjs.com/2017/testing/results). NPM a une commande spéciale pour les tests, `npm test` (qui est une abréviation de `npm run test`).

#### Autres bibliothèques

Outre Redux, [d'autres](https://stateofjs.com/2017/other-tools/) bibliothèques JavaScript populaires incluent [Lodash](https://lodash.com/), [Ramda](https://ramdajs.com/), [Underscore](https://underscorejs.org/), et [GraphQL](https://graphql.org/).

L'utilitaire de linting le plus populaire est [ESLint](https://eslint.org/).

[Bootstrap](https://getbootstrap.com/) est une bibliothèque CSS populaire mais elle nécessite une partie JavaScript (et c'est vraiment SASS, pas CSS).

Lorsque vous voyez `$` dans le code JavaScript, il fait généralement référence à jQuery. Lorsque vous voyez `_`, il fait généralement référence à Lodash ou Underscore.

Et peut-être vaut-il la peine de mentionner les bibliothèques de templating populaires : [Jade](http://jade-lang.com), [Pug](https://pugjs.org/), [Mustache](https://mustache.github.io/) et [Handlebars](https://handlebarsjs.com/).

#### Applications non web

Je n'en dirai pas plus sur ce sujet, mais TypeScript et JavaScript peuvent être utilisés en dehors du web.

Avec [Electron](https://electronjs.org/), vous pouvez écrire des applications de bureau multiplateformes. Avec [React Native](https://electronjs.org/), vous pouvez écrire des applications JavaScript pour les appareils Android/iOS qui ont une interface utilisateur "native". Vous pouvez également écrire des [applications en ligne de commande avec Node.js](https://scotch.io/tutorials/build-an-interactive-command-line-application-with-nodejs).

#### Types de modules

Pendant très longtemps, tout le code JavaScript s'exécutait dans un seul espace de noms global. Cela a causé des conflits entre des bibliothèques de code non apparentées, donc divers types de "définitions de modules" ont été inventés pour **simuler** ce que d'autres langages appellent des packages ou des modules.

Node.js utilise les modules [CommonJS](https://en.wikipedia.org/wiki/CommonJS), qui impliquent une fonction magique appelée `require('module-name')` pour importer des modules et une variable magique appelée `module.exports` pour créer des modules. Pour écrire des modules qui fonctionnent à la fois dans les navigateurs et Node.js, on peut utiliser la Universal Module Definition ([UMD](https://github.com/umdjs/umd) modules). Les modules qui peuvent être chargés de manière asynchrone utilisent [AMD](https://github.com/amdjs/amdjs-api/wiki/AMD).

ES6 a introduit un système de modules impliquant les mots-clés `import` et `export`, mais Node.js et certains navigateurs ne le supportent toujours pas. Voici un [primer sur les différents types de modules](https://www.jvandemo.com/a-10-minute-primer-to-javascript-modules-module-formats-module-loaders-and-module-bundlers/).

#### Polyfills & Prototypes

En tant que développeur expérimenté, je ne peux penser qu'à deux mots (autres que les noms des bibliothèques et des outils) qui ne sont utilisés que dans le Monde JavaScript : **polyfill** et **prototype**.

Les polyfills sont des aides de compatibilité ascendante. Ce sont des morceaux de code écrits en JavaScript qui vous permettent d'utiliser de nouvelles fonctionnalités dans les anciens navigateurs. Par exemple, l'expression `"food".startsWith('F')` teste si la chaîne de caractères `'food'` commence par F (pour le dossier, c'est `false` - elle commence par `f`, pas `F`). Mais `startsWith` est une nouvelle fonctionnalité de JavaScript qui n'est pas disponible dans les anciens navigateurs.

Vous pouvez "polyfill" avec ce code :

```
String.prototype.startsWith = String.prototype.startsWith ||  function(search, pos) {    return search ===       this.substr(!pos || pos < 0 ? 0 : +pos, search.length);  };
```

Ce code a la forme `X = X || function(...) {...}`, ce qui signifie "si X est défini, définissez X sur lui-même (ne le changez pas), sinon définissez X pour qu'il soit cette fonction." La fonction montrée ici se comporte comme `startsWith` est censé le faire.

Ce code fait référence à l'une des autres choses uniques de JavaScript, l'idée des prototypes. Les prototypes correspondent **approximativement** aux classes dans d'autres langages, donc ce que ce code fait est en fait de changer la définition du type de données intégré `String`. Ensuite, lorsque vous écrivez `'string'.startsWith()`, il appellera ce polyfill (si `String.prototype.startsWith` n'était pas déjà défini). Il existe divers articles pour vous enseigner les prototypes et l'héritage prototypique, comme [celui-ci](https://hackernoon.com/understanding-javascript-prototype-and-inheritance-d55a9a23bde2).

Même certaines fonctionnalités avancées des navigateurs ont des polyfills. Avez-vous entendu parler de [WebAssembly](https://webassembly.org/), qui vous permet d'exécuter du code C et C++ dans un navigateur ? Il existe un [polyfill JavaScript](https://github.com/lukewagner/polyfill-prototype-1) pour cela !

#### Crédit

Je voudrais remercier l'enquête [State of Javascript](https://stateofjs.com/) et [State of JavaScript frameworks](https://www.npmjs.com/npm/the-state-of-javascript-frameworks-2017-part-2-the-react-ecosystem) pour une grande partie des informations ci-dessus ! Pour quelques éléments, j'ai utilisé [npm-stat](https://npm-stat.com/) pour mesurer la popularité. Voir aussi cette [autre nouvelle enquête](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2018-results).

### Section 2 : Configuration réelle du projet

Hey là ! Toujours éveillé ? Maintenant, nous allons faire un tour de l'écosystème des outils JavaScript. Cette partie ne concerne pas React (nous y viendrons [plus tard](http://typescript-react-primer.loyc.net/tutorial-5.html)) mais elle inclut un simple composant React.

C'est un peu une **grande** visite, donc nous parlerons de l'écriture de votre application de trois manières différentes (avec un [résumé](http://typescript-react-primer.loyc.net/tutorial-3.html) ensuite) :

* A. La manière la plus facile (avec Parcel)
* B. La manière avec le moins d'outils (ou la manière DIY)
* C. La manière Webpack

Les six premières étapes sont les mêmes dans les trois approches, alors commençons !

#### Étape 1 : Installer Node.js/npm

Si vous ne l'avez pas encore fait, allez [installer Node.js](https://nodejs.org/en/download/) qui installera également le gestionnaire de paquets en ligne de commande, `npm`.

Si vous voulez déployer votre application sur un autre serveur web, je recommande de vous soucier de la manière de le faire plus tard.

#### Étape 2 : Installer Visual Studio Code ou un autre éditeur

L'une des principales raisons d'utiliser TypeScript au lieu de JavaScript est qu'il supporte les fonctionnalités de complétion de code.

Pour profiter de cet avantage, vous devrez éditer vos fichiers TypeScript `.ts` dans un éditeur compatible tel que [Visual Studio Code](https://code.visualstudio.com/download) — qui est gratuit et multiplateforme. C'est aussi l'éditeur de texte le plus populaire pour les applications JavaScript. Les alternatives incluent [Atom](https://atom.io/) et [Sublime Text](https://www.sublimetext.com/).

Visual Studio Code (VS Code) est orienté dossier : vous ouvrez un dossier dans VS Code et ce dossier sera traité comme le projet "courant". Pendant l'installation (sur Windows, en tout cas), il proposera une case à cocher pour ajouter une action "Ouvrir avec Code" pour les dossiers (répertoires). Je recommande d'utiliser cette option comme moyen facile de démarrer VS Code à partir de n'importe quel dossier :

![Image](https://cdn-media-1.freecodecamp.org/images/0*g75_7UBpUFqxHqwo.png)

Créez un dossier vide pour votre application, puis ouvrez ce dossier dans VS Code. Remarquez que VS Code a un terminal intégré, donc vous n'aurez pas besoin d'une fenêtre de terminal séparée.

#### Étape 3 : Configurer package.json

Le fichier `package.json` représentera la configuration de votre projet. Cela inclut son nom, les commandes de construction, la liste des modules npm utilisés par votre projet, et plus encore.

Si vous ne l'avez pas encore fait, créez un dossier vide pour votre application et ouvrez une fenêtre de terminal dans ce dossier.

Dans le terminal, exécutez `npm init`.

`npm init` vous posera quelques questions afin de produire `package.json`. Laissez un champ vide pour accepter la suggestion par défaut.

Je voulais créer une petite application éducative pour dessiner quelques graphiques démontrant comment la science du climat explique les enregistrements de température du 20ème siècle.

J'ai donc appelé mon application `climate-app` :

```
C:\Dev\climate-app>npm initThis utility will walk you through creating a package.json file.It only covers the most common items, and tries to guess sensible defaults.[....]
```

```
package name: (climate-app)version: (1.0.0)description: Demo to visualize climate dataentry point: (index.js) test command:git repository:keywords:author: David Piepgrasslicense: (ISC) MIT
```

```
About to write to C:\Dev\climate-app\package.json:{  "name": "climate-app",  "version": "1.0.0",  "description": "Demo to visualize climate data",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "author": "David Piepgrass",  "license": "MIT"}
```

```
Is this ok? (yes)
```

Remarquez la référence à `index.js`. Curieusement, ce fichier n'a pas besoin d'exister et nous ne l'utiliserons pas. Il n'est utilisé que [si vous partagez votre code via npm](https://stackoverflow.com/a/27971810/22820).

#### Étape 4 : Installer TypeScript

VS Code [aurait](https://code.visualstudio.com/docs/languages/typescript) un support de langage TypeScript plutôt qu'un **compilateur** TypeScript, donc maintenant nous devons installer le compilateur.

Il existe deux façons d'installer TypeScript avec npm. Soit utilisez

```
npm install --global typescript
```

ou

```
npm install --save-dev typescript
```

Si vous utilisez l'option `--global`, alors le compilateur TypeScript `tsc` sera disponible dans tous les projets sur la même machine. Il sera également disponible en tant que commande terminal, mais il ne sera pas ajouté à votre fichier `package.json`. Par conséquent, si vous partagez votre code avec d'autres, TypeScript ne sera **pas** installé lorsqu'une autre personne obtient votre code et exécute `npm install`.

Si vous utilisez `--save-dev`, TypeScript sera ajouté à `package.json` et installé dans le dossier `node_modules` de votre projet (taille actuelle : 34,2 Mo), mais il ne sera **pas** disponible directement en tant que commande terminal.

Vous pouvez toujours l'exécuter à partir du terminal en tant que `./node_modules/.bin/tsc`, et vous pouvez toujours utiliser `tsc` à l'intérieur de la section `"scripts"` de `npm` dans `package.json`.

**Fait amusant** : le compilateur TypeScript est multiplateforme car il est écrit en TypeScript — et compilé en JavaScript.

#### Étape 5 : Installer React ou Preact

Pour ajouter React à votre projet :

```
npm install react react-domnpm install --save-dev @types/react @types/react-dom
```

**Note** : `--save-dev` marque les choses comme "utilisées pour le développement" tandis que `--save` (qui est la valeur par défaut, et donc optionnelle) signifie "utilisées par le programme lorsqu'il est déployé".

Les paquets `@types` fournissent des informations de type à TypeScript, mais ils ne sont pas utilisés lorsque votre code est en cours d'exécution/déployé.

Si vous oubliez `--save-dev` ou si vous l'utilisez sur le mauvais paquet, **votre projet fonctionnera toujours**. La distinction n'est importante que si vous partagez votre projet en tant que paquet npm.

Alternativement, vous pouvez utiliser Preact, qui est [presque le même](https://preactjs.com/guide/differences-to-react) que React mais plus de 10 fois plus petit. Preact a des définitions de type TypeScript intégrées, donc vous n'avez besoin que d'une seule commande pour l'installer :

```
npm install preact
```

**Astuce** : `npm i` est un raccourci pour `npm install`, et `-D` est un raccourci pour `--save-dev`.

**Note** : ne pas installer `preact` et `@types/react` dans le même projet, ou `tsc` deviendra fou et vous donnera environ 150 erreurs (voir [problème preact #639](https://github.com/developit/preact/issues/639)). Si cela se produit, désinstallez les types React avec `npm uninstall @types/react @types/react-dom`

#### Étape 6 : Écrire du code React

Créez un fichier appelé `app.tsx` avec ce petit programme React :

**Note** : pour que le JSX intégré (HTML/XML) fonctionne, l'extension de fichier doit être `tsx`, et non `ts`.

Si vous avez des difficultés à faire fonctionner votre code, essayez ce code à la place — c'est le programme React le plus simple possible :

```
import * as ReactDOM from 'react-dom';import * as React from 'react';
```

```
ReactDOM.render(React.createElement("h2", null, "Hello, world!"),                document.body);
```

Nous discuterons du fonctionnement du code plus tard. Pour l'instant, concentrons-nous sur son exécution.

Si vous utilisez Preact, modifiez les deux premières lignes comme suit :

```
import * as React from 'preact';import * as ReactDOM from 'preact';
```

Quelques notes sur Preact :

* Il existe une [bibliothèque preact-compat](https://github.com/developit/preact-compat) qui vous permet d'utiliser preact avec zéro changement dans votre code React. Des instructions d'utilisation existent pour les utilisateurs de Webpack/Browserify/Babel/Brunch, et [cette page](https://github.com/parcel-bundler/parcel/pull/850) montre comment utiliser preact-compat avec Parcel.
* Il y a des rumeurs selon lesquelles dans Preact vous devriez écrire `/** @jsx h */` en haut du fichier, ce qui indique à TypeScript d'appeler `h()` au lieu de `React.createElement` par défaut. Dans ce cas, vous **ne devez pas** faire cela ou vous obtiendrez une erreur dans votre navigateur indiquant que `h` n'est pas défini (`React.h`, cependant, est défini). En fait, Preact définit `createElement` comme un alias pour `h`, et puisque notre instruction `import` assigne `'preact'` à `React`, `React.createElement` existe et fonctionne très bien.

#### Optionnel : exécuter des scripts TypeScript

Ce tutoriel est axé sur la création de **pages web** qui exécutent du code TypeScript. Si vous souhaitez exécuter un fichier TypeScript directement à partir de l'invite de commande, le moyen le plus simple est d'utiliser `ts-node` :

```
npm install --global ts-node
```

Après avoir installé `ts-node`, exécutez `ts-node X.ts` où `X.ts` est le nom d'un script que vous souhaitez exécuter. Dans le script, vous pouvez appeler `console.log("Hello")` pour écrire du texte dans le terminal (la lecture de texte à partir d'un utilisateur est [plus compliquée](https://nodejs.org/api/readline.html#apicontent)). Sur les systèmes Linux, vous pouvez mettre un "shebang" en haut du script si vous souhaitez pouvoir exécuter `./X.ts` directement (sans mentionner `ts-node`) :

```
#!/usr/bin/env ts-node
```

**Note** : si vous n'avez pas besoin d'exécuter des fichiers `.ts` à partir d'un terminal, vous n'avez pas besoin d'installer `ts-node`.

### Exécuter votre projet, Approche A : La manière facile

J'ai découvert Parcel lorsque j'avais presque terminé d'écrire cet article. Honnêtement, si je connaissais Parcel dès le début, je n'aurais peut-être pas pris la peine d'écrire sur les autres approches. Ne me lancez pas sur la facilité de Parcel ! Il mérite une médaille !

Il est très volumineux, cependant (81,9 Mo), donc vous devriez l'installer en global :

```
npm install --global parcel-bundler
```

La vérité est que je vous ai menti. Parcel est **si** facile, vous n'avez même pas besoin des six étapes ci-dessus ! Vous avez vraiment seulement besoin des étapes 1, 2 et 6 (installer Node, installer un éditeur, et écrire du code) car Parcel fera les étapes 3, 4, et 5 pour vous automatiquement.

Donc, tout ce que nous devons faire maintenant est de créer un fichier `index.html` qui fait référence à notre fichier `app.tsx`, comme ceci :

Ensuite, ouvrez simplement un terminal dans le même dossier et exécutez la commande `parcel index.html`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*xgfsNFJwzrxfbxEL.png)

Cela ne peut pas s'exécuter directement dans un navigateur, bien sûr, donc Parcel :

1. Compile automatiquement `app.tsx`
2. Installe React ou Preact s'il n'était pas déjà installé, car il remarque que vous l'utilisez
3. Regroupe votre application avec ses dépendances dans un seul fichier appelé `app.dd451710.js` (ou un autre nom amusant)
4. Crée un `index.html` modifié qui fait référence à l'application compilée et regroupée
5. Place ces nouveaux fichiers dans un dossier appelé `dist`.

Et ensuite, il fait tout le reste pour vous :

1. Il exécute votre application sur un mini serveur web à `http://127.0.0.1:1234` — visible sur un navigateur web sur la même machine
2. Il surveille les changements dans votre code (`app.tsx` et `index.html`) et recompile lorsque vous les modifiez
3. Comme si cela ne suffisait pas, lorsque vos fichiers changent, il enverra une commande à votre navigateur web pour **rafraîchir automatiquement !**
4. Mieux encore, il met à jour la page sans la recharger complètement en utilisant sa fonctionnalité [Hot Module Replacement](https://parceljs.org/hmr.html)

Il peut être difficile de configurer une construction conventionnelle qui fait toutes ces choses. Ce tutoriel ne couvre que la manière de faire #1 et #2 dans une construction conventionnelle, avec seulement la recompilation de code (pas HTML).

Pour en savoir plus sur les fonctionnalités de Parcel, consultez la [documentation de Parcel](https://parceljs.org/getting_started.html).

Une limitation de Parcel est qu'il ne effectue pas de vérification de type (votre code est traduit en JavaScript, mais les erreurs de type ne sont pas détectées).

Pour les petits projets, ce n'est pas un gros problème car Visual Studio Code effectue sa propre vérification de type. Il vous donne des lignes ondulées rouges pour indiquer les erreurs et toutes les erreurs sont listées dans le panneau "Problèmes" (appuyez sur `**Ctrl**`+`**Shift**`+`**M**` pour l'afficher). Mais si vous le souhaitez, vous pouvez `npm install parcel-plugin-typescript` pour [un support TypeScript amélioré](https://www.npmjs.com/package/parcel-plugin-typescript#features) incluant la vérification de type ([ne fonctionne pas actuellement pour moi](https://github.com/fathyb/parcel-plugin-typescript/issues/43)).

### Autres approches

Les autres approches sont plus connues et sont des pratiques standard dans la communauté JavaScript. Nous allons créer un dossier avec les fichiers suivants à l'intérieur :

* `**app/**index.html`
* `**app/**app.tsx`
* `package.json`
* `tsconfig.json`
* `server.js`
* `webpack.config.js` (optionnel)

En ce qui concerne la communication avec d'autres personnes qui regardent votre code plus tard, il est utile de séparer le **code front-end** de votre programme de sa **configuration de construction** et de son **serveur d'application**.

Le dossier racine d'un projet tend à devenir encombré de fichiers supplémentaires avec le temps (comme `.gitignore` si vous utilisez git, les fichiers `README` et `LICENSE`, les fichiers `appveyor`/`travis` si vous utilisez [l'intégration continue](https://en.wikipedia.org/wiki/Continuous_integration).) Par conséquent, nous devrions séparer le code de notre front-end dans un dossier différent.

En plus des fichiers **que nous** créons, TypeScript compilera `app.tsx` en `app.js` et `app.js.map`, tandis que `npm` crée un dossier appelé `node_modules` et un fichier appelé `package-lock.json`. Je ne peux pas imaginer pourquoi il s'appelle "lock", mais [cette page explique pourquoi il existe](https://medium.com/@Quigley_Ja/everything-you-wanted-to-know-about-package-lock-json-b81911aa8ab8).

Alors, commencez par créer un dossier `app` et mettez votre `app.tsx` là.

### Exécuter votre projet, Approche B : La manière avec le moins d'outils

Il semble que le projet JavaScript de tout le monde utilise une douzaine d'outils plus l'évier de cuisine. Est-il possible de faire un petit programme sans outils supplémentaires ? Bien sûr que oui ! Voici comment.

#### Étape B1 : Créer tsconfig.json

Créez un fichier texte appelé `tsconfig.json` dans votre dossier racine, et mettez ce code dedans :

Ce fichier marque le dossier comme un projet TypeScript et active les commandes de construction dans VSCode avec `**Ctrl**`+`**Shift**`+`**B**` (la commande `tsc: watch` est utile — elle recompilera automatiquement votre code chaque fois que vous l'enregistrerez.)

**Fait amusant** : `tsc` permet les commentaires dans les fichiers `.json` mais `npm` ne le permet pas.

Ce fichier est très important car si les paramètres ne sont pas corrects, quelque chose peut mal tourner et des erreurs mystérieuses peuvent vous frapper en plein visage. Voici la [documentation de tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html), mais les options du compilateur sont [documentées séparément](https://www.typescriptlang.org/docs/handbook/compiler-options.html).).

#### Étape B2 : Ajouter un script de construction

Pour permettre à `npm` de construire votre code TypeScript, vous devez également ajouter des entrées dans la partie `scripts` de `package.json`. Modifiez cette section pour qu'elle ressemble à ceci :

```
"scripts": {  "test": "echo \"Error: no tests installed\" && exit 1",  "build": "tsc",  "start": "node server.js"},
```

Le script `build` exécute simplement `tsc` qui compile votre code selon les options dans `tsconfig.json`. Pour invoquer ce script, vous écrivez `npm run build` sur la ligne de commande.

"Mais attendez !" vous pourriez penser. "Il est vraiment beaucoup plus facile de taper `tsc` que `npm run build` !" C'est vrai, mais il y a deux raisons de définir un script `build` :

1. Si vous avez installé TypeScript avec `--save-dev` mais pas `--global`, vous ne pouvez pas exécuter `tsc` directement à partir de la ligne de commande car il n'est pas dans le `PATH`.
2. Il y a de bonnes chances que votre processus de construction devienne plus compliqué plus tard. En créant un script de construction, vous pouvez facilement ajouter d'autres commandes au processus de construction plus tard.

**Note** : `npm` exécute le script `prestart` automatiquement chaque fois que quelqu'un exécute le script `start`, donc vous **pourriez** ajouter ce script supplémentaire :

```
"prestart": "npm run build",
```

Cela construirait votre projet chaque fois que vous démarrez votre serveur avec `npm start` ou `npm run start`.

Mais cela présente deux inconvénients :

1. `tsc` est un peu lent
2. si `tsc` trouve des erreurs de type, votre serveur ne démarrera pas

Lorsque TypeScript détecte des erreurs de type, cela ne l'empêche pas d'écrire des fichiers de sortie JavaScript, et vous pourriez trouver qu'il est parfois utile d'exécuter votre code même avec des erreurs de type.

Le comportement par défaut de `npm start` est d'exécuter `node server.js`, donc il semble redondant d'inclure `"start": "node server.js"`. Cependant, si votre serveur est écrit en TypeScript, vous aurez besoin de cette ligne car `server.js` n'existe pas jusqu'à ce que `server.ts` soit compilé. Et si `server.js` n'existe pas, `npm start` donnera l'erreur `missing script: start` à moins que vous n'incluiez cette ligne.

#### Étape B3 : Créer un serveur simple

Pour vous assurer que Node.js fonctionne, créez un fichier texte appelé `server.js` et mettez ce code dedans :

```
const http = require('http');
```

```
http.createServer(function (request, response) {  // Envoyer les en-têtes HTTP et le corps avec le statut 200 (signifiant succès)  response.writeHead(200, {'Content-Type': 'text/html'});  response.end(`    <html><body>      <h1>Hello, world!</h1>      You asked for: ${request.url}    </body></html>`);}).listen(1234);
```

Exécutez `npm start` pour le démarrer, visitez `http://127.0.0.1:1234/index.html` pour vous assurer qu'il fonctionne, puis appuyez sur `**Ctrl**`+`**C**` pour arrêter le serveur.

Pour obtenir IntelliSense pour Node.js, vous devez installer les informations de type pour celui-ci avec cette commande :

```
npm install @types/node --save-dev
```

Ensuite, dans VS Code, tapez `http.` pour vous assurer que cela fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/0*TmTm83d-pJmb6iM5.png)

En coulisses, VS Code utilise le moteur TypeScript pour cela. Cependant, si vous renommez votre fichier en `server.ts`, **IntelliSense ne fonctionne pas** ! TypeScript est-il cassé dans Node.js ? Pas vraiment. TypeScript peut toujours le compiler, il ne comprend tout simplement pas `require` dans un contexte `.ts`. Donc dans les fichiers TypeScript, vous devriez utiliser `import` au lieu de `require` :

```
import * as http from 'http';
```

**Note** : cela est différent de manière déroutante des fichiers `.mjs` de Node, qui nécessitent `import http from 'http';` ([Détails](https://stackoverflow.com/questions/50661510/why-doesnt-fs-work-when-imported-as-an-es6-module))

TypeScript convertit ensuite `import` en `require` dans sa sortie (en raison de l'option `"module": "umd"` dans `tsconfig.json`).

Maintenant, modifions notre serveur pour qu'il puisse servir n'importe quel fichier de notre dossier `/app` :

Vous remarquerez que ce code a une imbrication un peu étrange. C'est parce que les fonctions Node.js sont normalement asynchrones. Lorsque vous appelez des fonctions dans `fs`, au lieu de **retourner** un résultat, elles mettent votre programme en pause jusqu'à ce qu'elles soient terminées, puis elles **appellent** une fonction fournie par vous, envoyant à cette fonction soit une erreur (`err`), soit des informations (`fileInfo`).

Par exemple, au lieu de **retourner** des informations sur un fichier, `fs.stat` **envoie** des informations à un rappel.

Un aspect un peu étrange de ce serveur web est qu'il ignore `[request.method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)`, traitant chaque requête comme si c'était un `GET`. Mais cela fonctionne suffisamment bien pour commencer.

#### Étape B4 (optionnelle) : Utiliser Express

Si vous voulez que votre serveur côté serveur fasse un "routage" plus compliqué que servir quelques fichiers, vous devriez probablement apprendre le framework serveur Node.js le plus populaire : [Express](https://expressjs.com/).

Si nous utilisons Express, notre code serveur sera beaucoup plus court.

Installez-le simplement avec `npm install express` et mettez le code suivant dans `server.js` :

```
const express = require('express');const app = express();
```

```
app.use('/node_modules', express.static('node_modules'));app.use('/', express.static('app'));app.listen(1234, () => console.log(    'Express server running at http://127.0.0.1:1234'));
```

#### Étape B5 : Créer une page web pour contenir votre application

Enfin, dans votre dossier `app`, créez un fichier `index.html` pour charger votre application :

Cette page inclut à la fois React (`react.development.js` et `react-dom.development.js`) et Preact (`preact.dev.js`) donc je n'ai pas besoin de vous donner des instructions séparées pour chacun. Vous pouvez supprimer celui que vous n'utilisez pas, mais la page peut encore se charger avec des éléments de script non résolus.

À ce stade, vous devriez pouvoir construire votre code (`npm run build`), démarrer votre serveur (`npm start`) et visiter `http://127.0.0.1:1234` pour voir votre application !

![Image](https://cdn-media-1.freecodecamp.org/images/0*ZUymOkFeZhtmNjYF.png)

N'oubliez pas que vous pouvez recompiler votre code automatiquement dans VS Code : appuyez sur `**Ctrl**`+`**Shift**`+`**B**` et choisissez `tsc: watch`.

**Note** : Il est important de charger `app.js` à la fin du `body`, sinon React dira `Error: Target container is not a DOM element` car `app.js` appellerait `document.getElementById('app')` avant que l'élément app n'existe.

À ce stade, il est utile de noter que ce code est un peu bricolé. Surtout cette partie :

```
<script>    module = {exports:{}}; exports = {};    window.require = function(name) { return window[name]; };    window['react'] = window['React'];    window['react-dom'] = window['ReactDOM'];</script>
```

À quoi sert-ceci ? La réponse courte est que si votre code contient `import`, TypeScript **ne peut pas** produire du code qui "fonctionne simplement" dans un navigateur, et ceci est l'une des nombreuses solutions possibles à ce problème.

La réponse longue ? Tout d'abord, rappelez-vous que l'écosystème JavaScript a plusieurs systèmes de modules. En ce moment, votre fichier `tsconfig.json` utilise l'option `"module": "umd"`, car `"module": "umd"` et `"module": "commonjs"` sont les seuls modes qui peuvent être utilisés à la fois dans Node.js et un navigateur web.

Je vous ai demandé de créer un fichier `server.js` (et non `server.ts`), mais en utilisant `"module": "umd"` vous pourriez écrire votre code serveur en TypeScript si vous le souhaitez.

UMD est le choix naturel puisque c'est censé faire une définition de module "universelle", mais TypeScript n'essaie pas vraiment d'être universel — il ne tentera tout simplement pas de fonctionner dans un navigateur web sans aide.

Au lieu de cela, il s'attend à trouver des symboles prédéfinis soit pour un système de modules AMD, soit pour un système de modules CommonJS (ou Node.js). Si aucun de ceux-ci n'est défini, le module se termine sans même enregistrer un message d'erreur.

Même si nous **pouvions** utiliser l'option `"module": "es6"`, qui conserve les commandes `import` inchangées dans le fichier de sortie, cela ne fonctionnerait pas car Chrome, d'une manière ou d'une autre, **ne supporte toujours pas** `import` en 2018. De plus, les URL de nos modules ont peu en commun avec la chaîne dans nos instructions `import`, et j'ai appris que les alias de mappage de chemin TypeScript [path mapping aliases](https://www.typescriptlang.org/docs/handbook/module-resolution.html#base-url) ne peuvent pas résoudre le problème car ils ne changent pas la sortie du compilateur.

L'implémentation CommonJS de TypeScript nécessite que `require` soit défini, bien sûr — il est utilisé pour importer des modules. Mais il recherche également `exports` et `module.exports`, même si notre module n'exporte rien. Donc notre petit hack doit définir les trois.

Les versions UMD de React, ReactDOM et Preact définissent des variables globales appelées `React`, `ReactDOM` et `preact` respectivement. Mais les variables "globales" dans un navigateur sont en fait des membres d'un objet spécial appelé `window`. Et en JavaScript, `window.something` signifie exactement la même chose que `window['something']` sauf que vous pouvez utiliser des caractères spéciaux, comme des tirets, dans cette dernière forme. Par conséquent, `window['preact']` et/ou `window['React']` existent déjà. Donc, en définissant une fonction `require` qui retourne simplement `window[name]`, cela permet d'importer React ou Preact.

Cependant, nous devons également créer des alias en minuscules `'react'` et `'react-dom'` car ce sont les noms que nous devons utiliser dans notre code TypeScript (ces noms sont reconnus par le compilateur TypeScript car ce sont les noms des dossiers dans `node_modules`).

Il y a une autre chose dans notre index.html qui est un peu... malheureuse :

```
<script src="node_modules/react/umd/react.development.js"></script><script src="node_modules/react-dom/umd/react-dom.development.js"></script><script src="node_modules/preact/dist/preact.dev.js"></script>
```

Qu'est-ce qui rend ce code moins qu'idéal ?

1. Nous avons déjà des instructions `import` dans notre fichier `app.tsx`, donc il est malheureux que nous ayons besoin d'une **commande séparée** pour charger les modules dans notre `index.html`.
2. Nous faisons spécifiquement référence aux versions de **développement** du code, qui incluent des commentaires et sont beaucoup plus lisibles que les versions minifiées. Mais si nous déployons notre site web à un large public, nous voudrons passer aux versions minifiées pour que les pages se chargent plus rapidement. Il serait bien si nous pouvions faire cela sans perdre les avantages de débogage des versions de développement.
3. Cela suppose que nous pouvons accéder aux fichiers dans `node_modules`, ce qui est une manière inhabituelle de configurer un serveur.

Tous les inconvénients décrits ici nous amènent à vouloir un outil supplémentaire pour nous aider à déployer du code dans notre navigateur web. Nous avons déjà discuté de Parcel, mais le plus populaire est Webpack.

### Exécuter votre projet, Approche C : La manière Webpack

La chose la plus populaire à faire avec les applications front-end est de "packager" tous les modules (React + votre code + tout ce dont vous avez besoin) dans un seul fichier. Cela est comparable à ce qu'ils appellent "lier" dans certains autres langages, comme C++. C'est essentiellement ce pour quoi Parcel et Webpack sont construits (Gulp ne l'est pas — il nécessite des outils supplémentaires installés séparément.)

#### Étapes C1 & C2 : Créer tsconfig.json et server.js

Si vous avez sauté l'approche B, veuillez faire les étapes B1 et B4 maintenant.

#### Étape C3 : Installer webpack

Vous **pourriez** l'installer comme ceci :

```
npm install --save-dev webpack webpack-cli
```

Malheureusement, Webpack est surdimensionné : ces deux paquets ont 735 dépendances pesant 50,9 Mo (13 198 fichiers dans 1 868 dossiers). Et pour une raison quelconque, `webpack-cli` nécessite le paquet Webpack mais ne le marque pas comme une dépendance, donc vous devez installer les deux explicitement.

Et bien que `webpack-cli` soit ostensiblement "juste" l'interface de ligne de commande pour les API de Webpack, il est disproportionnellement grand pour une raison quelconque (Webpack seul n'est que 13,6 Mo).

En raison de sa taille, il est probablement plus judicieux de l'installer en global :

```
npm install --global webpack webpack-cli 
```

Lorsque vous utilisez `--global`, gardez à l'esprit que si vous partagez votre code avec quelqu'un d'autre, l'autre personne n'obtiendra pas Webpack automatiquement lorsqu'elle taper `npm install`, donc vous voudrez expliquer comment installer dans votre fichier `README`.

Si vous changez d'avis et souhaitez passer de `--save-dev` à `--global`, exécutez simplement la commande d'installation `--global` puis utilisez `npm uninstall webpack webpack-cli` pour supprimer la copie locale.

#### Étape C4 : Ajouter des scripts de construction

Pour permettre à `npm` de construire et de servir votre projet, ajoutez des entrées dans la section `"scripts"` de `package.json`.

Vous **pourriez** modifier cette section pour qu'elle ressemble à ceci :

```
"scripts": {  "test": "echo \"Error: no tests installed\" && exit 1",  "build": "tsc && webpack app/app.js -o app/app.bundle.js --mode=production",  "build:dev": "tsc && webpack app/app.js -o app/app.bundle.js --mode=development",  "start": "node server.js"},
```

Avec ces scripts, vous utiliseriez soit `npm run build` pour construire une version de production minifiée, soit `npm run build:dev` pour construire une version de développement avec tous les symboles et commentaires. Cependant, cela est peu pratique, car lorsque vous modifiez votre code, vous devez répéter manuellement la commande `npm run build:dev`.

Dans l'Approche B, nous pouvions utiliser `tsc: watch` dans VS Code, mais cela ne fonctionnera pas cette fois car nous **devons également** exécuter Webpack — et `tsc` ne le sait pas.

Pouvons-nous le configurer pour qu'il se reconstruise automatiquement lorsque notre code change ? Oui, mais nous aurons besoin d'un plugin Webpack pour y parvenir. L'un des plugins qui peut faire le travail s'appelle `awesome-typescript-loader`. Installez-le comme ceci :

```
npm install awesome-typescript-loader --save-dev
```

Ensuite, dans `package.json`, modifiez votre section `"scripts"` pour qu'elle ressemble à ceci :

Cela rend `webpack` entièrement responsable de la construction de notre code TypeScript, et donc nous pouvons utiliser son option `--watch` pour surveiller les changements de code. La commande pour construire et surveiller les changements de code est `npm run watch`.

#### Étape C5 : Démarrer le serveur et Webpack

Vous aurez besoin de deux terminaux séparés, un pour votre système de construction (`npm run watch`) et un pour votre serveur (`npm start`). Si votre serveur est écrit en TypeScript, alors vous devez d'abord exécuter `npm run watch`, sinon cela n'a pas d'importance lequel vous démarrez en premier.

Il est utile de noter que VS Code peut suivre plusieurs terminaux. Vous pouvez créer deux terminaux et exécuter une commande dans chacun, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*VRyly_6gxW6aIN8M.png)

#### Étape C6 : Créer index.html et le charger

Dans l'Approche C, votre fichier `index.html` est beaucoup plus simple que dans l'Approche B :

```
<!DOCTYPE html><html><head>  <title>App</title>  <meta charset="utf-8"/></head><body>  <h1>Mini React app ❤</h1>  <div id="app"></div>  <script src="app.bundle.js"></script></body></html>
```

Visitez `**http://127.0.0.1:1234**` et la page devrait se charger. Vous avez terminé !

#### Étape C7 : Créer un fichier webpack.config.js (optionnel)

Notre commande de construction devient plutôt longue, et est très similaire pour nos trois modes. De plus, nous n'avons configuré que l'extension de fichier `tsx` donc `webpack` ne sait pas encore comment compiler les fichiers `ts`.

La manière la plus populaire d'utiliser Webpack est avec un fichier de configuration spécial, séparé de `package.json`. Le script `"build"` ci-dessus devient le fichier `webpack.config.js` suivant :

```
module.exports = {  entry: __dirname+'/app/app.tsx',  output: {    path: __dirname+'/app',    filename: 'app.bundle.js'  },  module: {    rules: [      { test: /\.(ts|tsx)$/, loader: 'awesome-typescript-loader' }    ]  }};
```

Après avoir créé ce fichier, modifiez vos `scripts` dans `package.json` comme suit :

Comme avant, vous pouvez construire et surveiller les changements avec `npm run watch`, ou utiliser `npm run build` pour une construction de production minifiée.

### Vous avez terminé !

C'est tout ! Cliquez ici pour un [résumé](http://typescript-react-primer.loyc.net/tutorial-3.html) de toutes les étapes ci-dessus et [ici](http://typescript-react-primer.loyc.net/tutorial-4.html) pour continuer à apprendre TypeScript. Des questions ?
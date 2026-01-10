---
title: Gulp ! J'ai amélioré mon flux de travail !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-10-17T22:33:35.000Z'
originalURL: https://freecodecamp.org/news/gulp-i-improved-my-workflow-354d31d25655
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3vp5N6O1BBr79sdNtU6cQg.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: Gulp
  slug: gulp
- name: JavaScript
  slug: javascript
seo_title: Gulp ! J'ai amélioré mon flux de travail !
seo_desc: 'By Stefano Grassi

  yet another hands-on experience with Gulp.js


  _Jökulsárlón, Iceland by [Jeremy Goldberg](https://unsplash.com/jeremy" rel="noopener"
  target="blank" title=")

  Unless you’ve been living under a rock for the past few years, the number o...'
---

Par Stefano Grassi

#### encore une autre expérience pratique avec Gulp.js

![Image](https://cdn-media-1.freecodecamp.org/images/1*3vp5N6O1BBr79sdNtU6cQg.jpeg)
_Jökulsárlón, Islande par [Jeremy Goldberg](https://unsplash.com/jeremy" rel="noopener" target="_blank" title=")_

Sauf si vous avez vécu sous une pierre ces dernières années, le nombre d'outils à la disposition des développeurs front-end a augmenté rapidement. Ce que nous avons maintenant est une large gamme de projets dédiés à accélérer, automatiser et augmenter la qualité de notre flux de travail.

Par exemple, imaginez simplement :

* compiler [SASS](https://www.npmjs.com/package/gulp-sass)/[LESS](https://www.npmjs.com/package/gulp-less)/[PostCSS](https://www.npmjs.com/package/postcss)/[Stylus](https://www.npmjs.com/package/gulp-stylus) en CSS minifié, [sur mesure](https://www.npmjs.com/package/gulp-uncss) pour vos besoins, [auto-préfixé](https://www.npmjs.com/package/gulp-autoprefixer) et en temps réel
* [concaténer](https://www.npmjs.com/package/gulp-concat) et [minifier](https://www.npmjs.com/package/gulp-uglify) vos scripts
* compresser les fichiers HTML créés à partir de [modèles](https://www.npmjs.com/package/gulp-file-include) et de modules atomiques
* [prévisualiser](http://www.browsersync.io/) votre application web à partir d'un serveur virtuel pendant la compilation, avec rafraîchissement automatique et synchronisation sur tous vos appareils
* tester les [performances](https://www.npmjs.com/package/gulp-sitespeedio) de votre site web
* guide de style [auto-mis à jour](https://trulia.github.io/hologram/) du projet
* [compresser](https://www.npmjs.com/package/gulp-imagemin) les images et créer des [sprites](https://www.npmjs.com/package/gulp.spritesmith)

Il y a quelques années, cela ressemblait plus à un rêve disneyen, mais nous vivons dans le futur, alors n'ayez pas peur ! [Grunt](http://gruntjs.com/), [Mimosa](http://mimosa.io/), [Broccoli](http://broccolijs.com/) et [Gulp](http://gulpjs.com/) à la rescousse !

Chaque système a ses propres points forts. J'ai choisi Gulp pour mes besoins, mais assurez-vous de les vérifier tous avant de décider lequel vous convient le mieux.

#### Alors... gulp ? Qu'est-ce que c'est ?

[**gulpjs/gulp**](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md)
[_gulp — Le système de construction en streaming_ github.com](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md)

Comme le précise son site, Gulp est un « [système de construction en streaming](http://gulpjs.com/) », ce qui signifie que vous pouvez définir vos propres tâches à exécuter dans un pipeline, surveiller un dossier pour détecter les changements et les relancer.

Et c'est **super simple**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_PQJkvbZJNE_BjXpvIGCPQ.jpeg)
_C'est ingénieux, si je comprends bien.<br>C'est une montre suisse.<br>Oui, la beauté de cela réside dans sa simplicité._

#### Concepts de base de Gulp

Passons en revue les éléments principaux

**gulp.task**
aka l'action que vous souhaitez accomplir. Gérer le CSS ? Générer les docs ?
Gulp les définit avec [orchestrator](https://github.com/robrich/orchestrator), un module qui nous permet de définir des dépendances et une concurrency maximale

```
gulp.task('somename', function() { // Faire des trucs});
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*MRor084bOQstofwPYVjaFQ.jpeg)

**gulp.watch**
aka les dossiers que vous souhaitez surveiller pour détecter les changements

```
gulp.watch('folder/*.ext', ['firstTask', 'secondTask']);
```

Chaque **stream** provient d'une ou plusieurs sources correspondant à un **glob** spécifique (un motif qu'un fichier doit correspondre)

```
gulp.src(globs[, options])
```

une série de **pipes** (actions)

```
.pipe(concat()),.pipe(minify())
```

et une **destination** définie avec

```
gulp.dest(path[, options])
```

Pour fonctionner, gulp a besoin de deux fichiers principaux, **package.json** et **gulpfile.js.**
_(Pour l'installation de gulp, suivez la documentation officielle)_

#### Gulpfile.js

Dans le **gulpfile**, nous déclarerons les plugins que nous allons utiliser, les tâches que nous voulons exécuter, les dossiers que nous allons surveiller, etc.

#### Package.json

Le fichier **package.json** est utilisé pour stocker toutes les informations concernant les dépendances du projet (gulp inclus !).

![Image](https://cdn-media-1.freecodecamp.org/images/1*p1_LFP4jZEH6b9asHPueyg.jpeg)

* Pour le **créer**

```
$ npm init
```

Vous serez invité à entrer quelques informations de base pour l'en-tête du fichier, comme le nom de l'auteur, le nom du projet, etc.

* Pour **installer** un plugin et enregistrer la dépendance dans le fichier json

```
$ npm install --save-dev yourPluginName
```

* Pour **désinstaller** un plugin et supprimer la dépendance du fichier json

```
$ npm uninstall --save-dev yourPluginName
```

* Si vous devez **installer toutes les dépendances** à partir d'un package.json compilé

```
$ npm install
```

#### Organisation du projet

Voici mon approche pour organiser le dossier d'un projet géré avec Gulp

#### Plugins FTW !

Gulp dispose d'une liste impressionnante de plugins (**1895** au moment où j'écris cet article)

[**registre des plugins gulp.js**](http://gulpjs.com/plugins/)
[_Découvrir les plugins gulp.js_ gulpjs.com](http://gulpjs.com/plugins/)

**À avoir absolument**

* [gulp-load-plugins](https://github.com/jackfranklin/gulp-load-plugins)
Ce plugin charge paresseusement les plugins installés dans votre projet. Vous lui attribuez une variable et vous l'utilisez pour référencer d'autres plugins au lieu de répéter la déclaration de dépendance pour chaque autre plugin.

```
var $ = require('gulp-load-plugins')();
```

```
// Exemple pour gulp-concat.pipe($.concat('main.js'))
```

* [browsersync](http://www.browsersync.io/docs/gulp/)
rafraîchissement de la page à chaque changement sur tous les appareils connectés à la même URL (localhost ou LAN)
* [sitespeed](https://www.sitespeed.io)
mon outil préféré pour les tests de performance
* [uncss](https://github.com/giakki/uncss)
utilisez-vous un framework CSS comme Bootstrap pour une page de destination ?
Vous AVEZ BESOIN de cela.

#### Comment ? Comment mettre à jour les plugins Gulp, demandez-vous ?

```
$ npm install -g npm-check-updates
```

```
$ npm-check-updates -u
```

```
$ rm -fr node_modules
```

```
$ npm install
```

> En gros, cela installe **npm-check-updates** globalement, l'exécute contre votre package.json et met à jour les versions des dépendances.
> Ensuite, vous supprimez simplement le dossier node_modules et réinstallez.

> de : [https://stackoverflow.com/questions/27024431/updating-gulp-plugins](https://stackoverflow.com/questions/27024431/updating-gulp-plugins)

Note : En règle générale, et en dernier recours, il est préférable de **nettoyer** le cache npm avec

```
$ npm cache clean
```

#### _C'est tout, les amis ! Merci d'être arrivé jusqu'à ce point !_

#### _J'espère que je vous ai intéressé suffisamment pour vérifier certains des liens qui remplissent cet article. Ils sont là parce que je voulais montrer mon soutien pour tout le travail formidable que font les autres développeurs pour la communauté._
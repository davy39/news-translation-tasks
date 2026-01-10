---
title: Comment installer Gulp-sass en utilisant la ligne de commande si vous êtes
  débutant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-30T17:23:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-gulp-sass-using-the-command-line-if-youre-a-beginner-17729f53249
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Ua25jOkgtszd4brxFG0pQ.png
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: Gulp
  slug: gulp
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment installer Gulp-sass en utilisant la ligne de commande si vous êtes
  débutant
seo_desc: 'By Simeon Bello

  I intern at a tech firm presently, and few days ago I got a challenge from my boss
  about writing an article. So I decided to write something on Gulp-sass.Setting it
  up can be frustrating sometimes, especially when you are new to it. I...'
---

Par Simeon Bello

Je fais un stage dans une entreprise technologique actuellement, et il y a quelques jours, mon patron m'a lancé un défi concernant la rédaction d'un article. J'ai donc décidé d'écrire quelque chose sur Gulp-sass.   

L'installer peut parfois être frustrant, surtout lorsque vous êtes nouveau dans ce domaine. J'utilise Windows, et chercher un article qui résoudreait mon problème était comme demander à Jack dans Black-ish d'épeler « decrease ».

D'accord, je pense que je me suis un peu emporté là... assez parlé de moi, commençons !

P.S. c'est mon premier article publié et j'espère que vous allez l'aimer. :)

### Installation de node

Tout d'abord, ouvrez la ligne de commande et installez [node.js](https://nodejs.org) sur votre ordinateur. Il est livré avec un gestionnaire de paquets Node (npm) que vous pouvez utiliser pour installer Gulp. Après l'installation, vous pouvez installer Gulp en exécutant `npm install gulp -g`. Le `**-g**` indique à **npm** d'installer Gulp globalement sur votre ordinateur (cela signifie que vous pouvez utiliser les commandes gulp n'importe où sur votre ordinateur.)

Avant de continuer, je suppose que vous êtes familier avec la ligne de commande !

Naviguez jusqu'à votre répertoire de projet et exécutez `npm init`. Cela créera un fichier package.json, appuyez sur Entrée et il ajoutera ce dont vous avez besoin dans le fichier package.json.

Oui, vous vous demandez peut-être ce qu'est un fichier package.json, n'est-ce pas ?  
Un [fichier package.json](https://docs.nodejitsu.com/articles/getting-started/npm/what-is-the-file-package-json/) contient diverses métadonnées pertinentes pour votre projet. Ce fichier donne des informations à npm et lui permet d'identifier le projet ainsi que de gérer les dépendances du projet. Il facilite également l'installation de toutes les tâches utilisées dans un projet Gulp.

Si vous ne comprenez toujours pas, vous avez probablement besoin de Diane pour mieux l'expliquer — quel est mon problème/obsession avec Black-ish ??

Après avoir exécuté `npm-init`, tapez `npm install gulp --save-dev`**,** cela indique à **npm** d'installer Gulp dans votre projet. En utilisant `--save-dev`, nous stockons Gulp comme une dépendance de développement dans le package.json.

### Création d'un Gulpfile

Maintenant que vous avez installé Gulp, vous êtes prêt à installer la première tâche. Vous devez `require` Gulp. Créez un nouveau fichier appelé gulpfile.js dans votre répertoire de projet — Vous pouvez le faire en utilisant n'importe quel éditeur de texte. Commencez par ajouter le code ci-dessous à votre gulpfile.

```
use strict;
```

```
var gulp = require(gulp);
```

### Configuration d'une tâche

Maintenant, vous pouvez installer une **tâche gulp —** dans ce cas, nous installerons Gulp-sass. Cette tâche permet de convertir _Sass en CSS_. Toujours en utilisant la ligne de commande, vous pouvez installer Gulp-sass en exécutant `**npm** install gulp-sass --save-dev`. Après cela, require Gulp-sass dans votre gulpfile.js.

Placez `var sass = require(gulp-sass);` sous la ligne où vous avez requis gulp.

### Structuration de votre projet

Avant d'utiliser les lignes ci-dessous, je suppose également que vous savez comment structurer une application web. Ici, je vais utiliser la structure des applications web courantes.

![Image](https://cdn-media-1.freecodecamp.org/images/Qe0oi9tR9oQ1WTgIJxWTV0VTBnZEHAkHEE2s)

### Compilation de sass/scss

La dernière chose à faire est d'indiquer à gulp quels fichiers il doit convertir et où doit être la destination — où le fichier de sortie sera stocké.

Utilisez ce qui suit ;

```
//compile gulp.task(sass, function () { gulp.src(app/scss/app.scss) .pipe(sass().on(error, sass.logError)) .pipe(gulp.dest(app/css)); });
```

Le fichier dans **gulp.src** sera converti, vous pouvez également sélectionner tous les fichiers .scss dans un répertoire en utilisant `app/scss/*.scss`. Cela sélectionnera tous vos fichiers .scss dans le dossier scss.

Le **gulp.dest** est la sortie. La sortie sera stockée dans le dossier CSS à l'intérieur du dossier app.

### Gulp-watch-sass

Gulp dispose d'une syntaxe watch qui lui permet de surveiller les fichiers sources et ensuite de « surveiller » les modifications apportées à votre code. Il suffit d'ajouter la syntaxe à votre gulpfile.js en tapant :

```
//compile and watch gulp.task(sass:watch, function() { gulp.watch(app/scss/app.scss, [sass]);});
```

C'est à peu près tout ce que vous avez à faire ! Ce n'était pas si stressant, n'est-ce pas ?

Merci d'avoir lu !
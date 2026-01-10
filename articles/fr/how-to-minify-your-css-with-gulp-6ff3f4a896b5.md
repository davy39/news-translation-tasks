---
title: Comment minifier votre CSS avec gulp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-10T17:20:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-minify-your-css-with-gulp-6ff3f4a896b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*buKin7TOLVwnO4affvO8Qg.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: Gulp
  slug: gulp
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment minifier votre CSS avec gulp
seo_desc: 'By Vinicius Gularte

  In this article, I''m going to show a simple way to automatically minify your CSS
  files using gulp. ?

  To start — what is gulp?

  Gulp is a JavaScript task runner that lets you automate tasks such as…


  Bundling and minifying libraries...'
---

Par Vinicius Gularte

Dans cet article, je vais vous montrer une méthode simple pour minifier automatiquement vos fichiers CSS en utilisant gulp. 💡

### **Pour commencer — qu'est-ce que gulp ?**

Gulp est un exécuteur de tâches JavaScript qui vous permet d'automatiser des tâches telles que…

* Regrouper et minifier des bibliothèques et des feuilles de style.
* Rafraîchir votre navigateur lorsque vous enregistrez un fichier.
* Exécuter rapidement des tests unitaires.
* Exécuter des analyses de code.
* Compilation Less/Sass vers CSS.
* Et bien plus encore !

Le flux de travail de gulp fonctionne comme suit :

Nous pouvons créer des tâches que nous souhaitons accomplir. Dans ces tâches, nous chargeons des fichiers sur lesquels nous voulons que gulp travaille (en les modifiant ou non), puis nous les renvoyons vers un dossier de destination.

C'est simple.

Dans ce petit tutoriel, je vais vous apprendre à créer une tâche pour minifier tous les fichiers CSS dans votre dossier. Ensuite, placer les fichiers minifiés dans un autre dossier.

### Commençons

Pour ce tutoriel, assurez-vous d'avoir la dernière version du package npm installée sur votre machine. Si ce n'est pas le cas, vous pouvez le télécharger [**ici**](http://www.npmjs.com).

Une fois npm installé, dans le répertoire de base de votre projet, nous allons installer gulp en utilisant ces commandes :

`npm install gulp-cli -g`

`npm install gulp -D`

Nous allons également utiliser un plugin gulp pour minifier le CSS appelé **gulp-clean-css**, alors installez-le dans le projet avec :

`npm install gulp-clean-css --save-dev`

Très bien, maintenant que les dépendances sont installées dans le projet, créons un fichier appelé **Gulpfile.js**. Ce fichier sera responsable de nos tâches.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RHjTJ_6QntCKKKnuZm_ndA.png)

Nous allons également créer deux dossiers dans ce dépôt. L'un s'appellera styles où nos fichiers de style seront stockés, et un autre appelé dist où les fichiers minifiés seront placés.

À la fin, notre projet aura cette structure :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dLew0FI0XbGbyxKuCIadGA.png)

### Dans Gulpfile.js

Au début du fichier, nous faisons les appels des packages que nous allons utiliser.

Avec les packages appelés, nous allons créer la tâche responsable de la minification de nos fichiers.

Vous vous demandez peut-être — vous êtes déjà capable de minifier vos fichiers ? Oui, en exécutant la commande gulp dans le terminal suivie du nom de la tâche.

Mais exécuter cette commande tout le temps est un peu ennuyeux, n'est-ce pas ? Nous pouvons créer une méthode pour observer les changements dans les fichiers du dossier styles.

De cette manière, exécuter la commande gulp attendra les changements dans les fichiers sélectionnés pour activer la tâche minify-css.

### Conclusion

Ce n'est qu'une petite façon dont gulp peut nous aider dans le développement de nos applications.

Vous pouvez trouver le code de ce projet dans [ce dépôt](https://github.com/ViniciusGularte/MinifiedCssGulp) sur GitHub.

_Merci d'avoir lu, n'hésitez pas à ❤️ et aidez les autres à le trouver._

_À bientôt._ 😊

### Références

[**gulp.js**](https://gulpjs.com/)  
[_En préférant le code à la configuration, les meilleures pratiques de node et une API minimale - gulp simplifie les choses comme..._gulpjs.com](https://gulpjs.com/)[**gulp-clean-css**](https://www.npmjs.com/package/gulp-clean-css)  
[_Minifier le css avec clean-css._www.npmjs.com](https://www.npmjs.com/package/gulp-clean-css)
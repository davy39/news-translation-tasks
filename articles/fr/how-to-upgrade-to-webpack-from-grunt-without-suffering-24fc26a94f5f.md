---
title: Découvrez à quel point il est facile de passer à Webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-13T11:44:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-upgrade-to-webpack-from-grunt-without-suffering-24fc26a94f5f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*H9-QqXnBR8Rr6MhF
tags:
- name: development
  slug: development
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
seo_title: Découvrez à quel point il est facile de passer à Webpack
seo_desc: 'By Yazan Aabed

  I’ve written this article to narrate the adventure that happened to me when upgrading
  an AngularJS project from Grunt to Webpack.


  _Photo by [Unsplash](https://unsplash.com/@tfrants?utm_source=medium&utm_medium=referral"
  rel="noopener"...'
---

Par Yazan Aabed

_J'ai écrit cet article pour raconter l'aventure qui m'est arrivée lors de la mise à niveau d'un projet AngularJS de Grunt à Webpack._

![Image](https://cdn-media-1.freecodecamp.org/images/0*H9-QqXnBR8Rr6MhF)
_Photo par [Unsplash](https://unsplash.com/@tfrants?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Tyler Franta</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Vous pouvez me suivre sur [twitter](https://twitter.com/YazanAabed) ou consulter mes derniers articles sur [mon site yaabed.com](https://www.yaabed.com/). De plus, j'ai ma publication sur [medium blog.yaabed.com](https://medium.com/yazanaabed).

Le problème principal était que 500 éléments étaient placés sur l'objet window. Cela permet d'y accéder n'importe où. Cela fait également de la fenêtre l'outil de navigation pour les modules et les composants. Le projet devient plus couplé, et vous ne savez pas qui les utilise.

Les fichiers sont structurés en utilisant l'architecture modulaire mais sans utiliser `angular.module`. Les fichiers sont divisés en dossiers par nom comme HomePage. Le dossier HomePage contient son contrôleur, son style et sa vue.

La première chose qui m'est venue à l'esprit était de refactoriser toute l'application pour utiliser webpack, les modules, babel et es6. Après des recherches, il est possible de faire cela sans aucune refactorisation de la base de code. Mais il y a de nombreux problèmes à résoudre avant de commencer à ajouter webpack au projet.

### **Problèmes à considérer avant de commencer à travailler**

* Comment résoudre le problème de l'objet window, car webpack montre les fichiers comme un arbre de fichiers qui communiquent entre eux.
* Comment apporter moins de modifications au projet sans problèmes de fusion.
* Comment séparer le développement et la production pour webpack.
* Comment supprimer les dépendances bower, car webpack résout principalement les modules à partir de npm.
* Comment les mises à niveau vers webpack résolvent la grande taille des fichiers JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8cR1c4pTuS145b7KhVrB-Q.jpeg)
_[https://www.pexels.com/photo/technology-computer-desktop-source-code-113850/](https://www.pexels.com/photo/technology-computer-desktop-source-code-113850/" rel="noopener" target="_blank" title=")_

### Commencer à diviser les choses en étapes

#### Mettre à niveau la version de node de 0.10 à la dernière version disponible

Avant de commencer à utiliser webpack, j'avais besoin de mettre à niveau la version de Node avec laquelle webpack v3 fonctionne. Mais Grunt utilise des choses obsolètes — donc lorsque j'ai mis à jour la version de Node, rien n'a fonctionné ! J'ai donc commencé à corriger les erreurs une par une pour m'assurer que la mise à niveau était possible.

Tout d'abord, une erreur s'est produite sur l'ancien `grunt-sass` & `node-sass`. Ils ne sont plus supportés pour cette version de Node. Pour corriger cela, j'ai mis à niveau `grunt-sass` de '0.18.1' à '2.0.0', puis j'ai mis à niveau `node-sass` pour qu'il soit '4.7.2'.

Deuxièmement, essayer de mettre à niveau grunt de '0.4.5' à '1.0.0' n'a pas fonctionné, car les plugins grunt nécessitent grunt@0.4.5 comme dépendance pair. J'ai donc conservé la version 0.4.5.

#### Correction des erreurs affichées sur le serveur node express

J'ai dû corriger les erreurs avec le serveur Node express, car le constructeur bodyParser est obsolète et doit être changé. J'ai changé de

![Image](https://cdn-media-1.freecodecamp.org/images/1*zYHhQhSD4VfTrv8HWp7l4A.png)

à

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ty4Il11Y6pwJodIZcBfdYg.png)

#### Supprimer les choses obsolètes

* L'attribut Debug de `grunt-express` car il est obsolète dans la nouvelle version de node-inspector.
* Supprimer la tâche bower-install du projet.

#### Commencer à ajouter webpack

J'ai ajouté webpack au projet en utilisant `npm install webpack --save-dev`. Ensuite, j'ai ajouté le fichier `webpack.config.json`.

Lorsque j'ai commencé cette étape, je me suis retrouvé bloqué car la structure du projet n'a pas de point d'entrée. Tout le projet dépend d'une seule source qui est la fenêtre. Webpack a besoin d'un point d'entrée pour commencer et d'un point de sortie pour terminer.

Pour résoudre cela, j'ai créé un point d'entrée. J'ai défini tous les fichiers nécessaires et je l'ai nommé de la même manière que dans la configuration de GruntJS pour le concaténer comme l'ancien Build le faisait. Mais cela allait prendre beaucoup de temps, car environ 550 éléments étaient inclus dans index.html.

Pour résoudre ce problème, j'ai utilisé une RegExp `/"(.*?)"/ig` et remplacé les valeurs par `require(src)` pour obtenir les sources de l'attribut src et les convertir en `require(src)`. Je l'ai collé dans `entry.js` dans le même ordre que l'ancien index.html.

Après cela, le résultat était un fichier JS significatif contenant tous les scripts. Mais rien ne fonctionnait ! Après avoir enquêté sur ce qui se passait, il semblait que webpack fonctionnait par défaut comme des modules. Si des exports ou export default sont présents dans le même fichier, rien ne sera exporté vers l'extérieur même si vous l'incluez en utilisant require js.

Avant de chercher un moyen de résoudre cela, j'ai commencé à ajouter module.exports à tous les fichiers nécessitant d'être exportés — avant de comprendre clairement comment webpack fonctionne ! Après deux jours de travail, j'ai trouvé qu'il existe quelque chose appelé loaders qui résout le problème.

En ajoutant cela à `webpack.config.js`, tous les fichiers étaient maintenant disponibles comme l'ancien comportement !

![Image](https://cdn-media-1.freecodecamp.org/images/1*a1w_YDNzXTDVWfIzl5CN1g.png)

Et tout fonctionnait maintenant.

#### Étape suivante

Après avoir fait fonctionner le projet avec Grunt, j'avais besoin de m'assurer que webpack et Grunt fonctionnaient ensemble. J'ai donc fait des tests pour m'assurer que je n'avais rien manqué.

Pour que cela se produise, j'ai créé un nouveau fichier appelé `inject-HTML.files.json`. Ce fichier contient tous les fichiers sources à utiliser avec `usemenPrepare` sur Grunt et webpack pour créer les entrées comme plusieurs éléments sous forme de tableaux pris à partir du JSON des fichiers inject-HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4CHmK7YvGR-5KdKkDb0shQ.jpeg)
_J'adore cette image, écrire du code et boire un peu de café :) [https://www.pexels.com/photo/high-angle-view-of-coffee-cup-on-table-317385/](https://www.pexels.com/photo/high-angle-view-of-coffee-cup-on-table-317385/" rel="noopener" target="_blank" title=")_

#### Mettre à jour l'ancien fichier de configuration Grunt

![Image](https://cdn-media-1.freecodecamp.org/images/1*_ACtb1LBsXQulfYWnZP17g.png)

#### Ajouter des fichiers à concaténer

![Image](https://cdn-media-1.freecodecamp.org/images/1*2AX4IhZxSTV2sFxd2dn8qg.png)

#### Vérifier si Webpack construit, puis supprimer le JS des configurations

![Image](https://cdn-media-1.freecodecamp.org/images/1*YaLaQJvEGZf1-U09ii3t0g.png)

#### Ajouter un nouveau script npm

![Image](https://cdn-media-1.freecodecamp.org/images/1*h72Fb0X9U7Fdt1d3NQ0z-Q.png)

#### Fichier webpack.config.js

![Image](https://cdn-media-1.freecodecamp.org/images/1*o7QEQxqK3HhR4_lMu0zvhA.png)

#### Fichier webpack.prod.js

![Image](https://cdn-media-1.freecodecamp.org/images/1*sZWLlMeMiXaXPdqmOYvXog.png)

### Motivations

#### Maintenabilité et Qualité du Code

* Résoudre le problème de création de fichiers, car le projet grandit rapidement.
* Résoudre le problème qu'il y a trop de choses attachées à la fenêtre sans raison.
* Rendre la base de code plus facile à comprendre.

#### Efficacité du Développement

* Bower est maintenant obsolète.
* Impossible d'utiliser des choses sur les packages npm, car le processus de construction ne le permet pas.

#### Performance

* La taille des fichiers augmente chaque jour, il faut donc introduire une solution pour diviser le code.
* Pouvoir diviser les fichiers et différer le chargement jusqu'à ce qu'il soit nécessaire économise un transfert et un parsing inutiles.

#### Division du Code

* Après utilisation, la division du code webpack sera plus facile à utiliser.
* Diviser les nouvelles fonctionnalités en modules.

Enfin, l'utilisation des packages npm est un changement de jeu. Le but était de rendre la base de code facile pour les autres développeurs. De plus, nous avons prouvé qu'il est possible de mettre à niveau votre système judicieusement même si votre base de code est terrible.

Réécrire toute l'application est une catastrophe, car vous gaspillez potentiellement des années de travail acharné. Au lieu de cela, essayez de rendre votre base de code plus lisible, maintenable et modulaire. Lorsque l'ancien code a besoin d'être refactorisé, vous pouvez le faire étape par étape.

Ne restez pas bloqué avec votre ancienne base de code et dites que vous ne pouvez rien faire avec. Essayez d'apporter des changements par vous-même — vivez avec de nouvelles choses, de nouvelles mises à jour et de nouvelles technologies qui vous rendront heureux.

C'est la première fois que j'écris pour les gens ! Si vous avez aimé cet article, veuillez le partager avec d'autres personnes autour de vous.

**_J'écris sur [blog.yaabed.com](https://medium.com/yazanaabed). Si vous avez apprécié cet article, assurez-vous de le partager avec d'autres personnes. Et n'oubliez pas de cliquer sur le bouton suivre pour plus d'articles comme celui-ci, et [suivez-moi sur twitter](https://twitter.com/YazanAabed)._**

![Image](https://cdn-media-1.freecodecamp.org/images/1*MSPCzn3l6S8PfjbPj0m7jw.jpeg)

> Salut, je m'appelle [Yazan Aabed](https://www.yaabed.com/). J'ai grandi en Palestine. Mon domaine était l'informatique. Je suis un ingénieur Frontend et un amateur de JavaScript 💻. Je travaille principalement avec des frameworks Frontend comme (AngularJs, ReactJS). Vous pouvez m'appeler #Geek 🤓. De plus, j'aime partager mes connaissances avec les autres et apprendre d'eux 🤝. Vous pouvez me trouver sur GitHub, [Medium](https://github.com/YazanAabeed), [Twitter](https://medium.com/@yazanaabed).[.](https://twitter.com/YazanAabed)

[**Académie d'apprentissage de webpack**](https://webpack.academy/)  
[_L'académie d'apprentissage de webpack existe pour fournir un contenu d'apprentissage curaté et de haute qualité, dédié à webpack open source..._webpack.academy](https://webpack.academy/)[**De Grunt et Bower à Webpack, Babel et Yarn — Migration d'un système de construction frontend hérité**](https://medium.com/appifycanada/migrate-to-webpack-from-grunt-bower-legacy-build-system-344526f47873)  
[_Le système de construction que j'avais hérité pour le Portail de données du Consortium international du génome du cancer était assez moderne..._medium.com](https://medium.com/appifycanada/migrate-to-webpack-from-grunt-bower-legacy-build-system-344526f47873)[**Comment passer progressivement à webpack**](https://medium.com/eventmobi/how-to-incrementally-switch-to-webpack-203a1b431f7a)  
[_Ceci est le deuxième d'une série en deux parties sur les raisons et la manière dont nous avons changé notre système de bundling JavaScript d'un système ad hoc..._medium.com](https://medium.com/eventmobi/how-to-incrementally-switch-to-webpack-203a1b431f7a)[**Pourquoi nous sommes passés à webpack**](https://medium.com/eventmobi/why-we-switched-to-webpack-69b7396f3ec5)  
[_Ceci est le premier d'une série en deux parties sur les raisons et la manière dont nous avons changé notre système de bundling JavaScript d'un système ad hoc..._medium.com](https://medium.com/eventmobi/why-we-switched-to-webpack-69b7396f3ec5)[**Les premières étapes de Grunt à Webpack**](https://advancedweb.hu/2016/02/02/the-first-steps-from-grunt-to-webpack/)  
[_Commencer avec Webpack après avoir utilisé Grunt_advancedweb.hu](https://advancedweb.hu/2016/02/02/the-first-steps-from-grunt-to-webpack/)[**Le Voyage vers Webpack - Blog Server Density**](https://blog.serverdensity.com/the-journey-to-webpack/)  
[_Par Kerry Gallagher, de Server Density. Publié le 6 janvier 2016. Au cours des dernières années, nous avons construit le..._blog.serverdensity.com](https://blog.serverdensity.com/the-journey-to-webpack/)

> [[discussion] Comment sommes-nous passés de Grunt à Gulp à Webpack ?](https://www.reddit.com/r/javascript/comments/42z1xl/discussion_how_did_we_go_from_grunt_to_gulp_to/?ref_source=embed&ref=share) de       [javascript](https://www.reddit.com/r/javascript/)
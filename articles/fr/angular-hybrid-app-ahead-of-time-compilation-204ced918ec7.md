---
title: Comment activer la compilation ahead-of-time dans une application hybride Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T08:34:39.000Z'
originalURL: https://freecodecamp.org/news/angular-hybrid-app-ahead-of-time-compilation-204ced918ec7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iF8uCp-Dx8BfuCSgkbHvnQ.jpeg
tags: []
seo_title: Comment activer la compilation ahead-of-time dans une application hybride
  Angular
seo_desc: 'By Kamil Maraz

  And why you’ll want to do this

  Ahead-of-time (AOT) compilation is a big word in the Angular community. Everybody
  wants to get it running. If you are starting with a new project using Angular CLI,
  you’ve won. There is nothing simpler th...'
---

Par Kamil Maraz

#### Et pourquoi vous voudrez faire cela

La compilation ahead-of-time (AOT) est un grand mot dans la communauté Angular. Tout le monde veut la faire fonctionner. Si vous commencez un nouveau projet en utilisant [Angular CLI](https://cli.angular.io/), vous avez gagné. Il n'y a rien de plus simple que d'inclure l'option « --aot » dans votre terminal.

Mais que faire si vous avez une configuration Webpack personnalisée ? Ou si vous utilisez le [module Upgrade](https://angular.io/guide/upgrade) et que vous avez une application hybride Angular ? Voici comment nous avons traité ce problème particulier dans [Admin](https://admin.sli.do) — l'interface d'administration pour les utilisateurs de [Slido](https://slido.com).

![Image](https://cdn-media-1.freecodecamp.org/images/1*iF8uCp-Dx8BfuCSgkbHvnQ.jpeg)

#### Ahead-of-Time vs. Just-in-Time

La différence entre AOT et la compilation Just-in-Time (JIT) réside dans l'étape à laquelle la compilation se produit. Avec AOT, nous parlons de la phase de construction. Cela se produit avant l'exécution de l'application dans le navigateur. La compilation JIT se produit lorsque l'application s'exécute dans le navigateur.

Comme il est indiqué dans le [guide Angular :](https://angular.io/guide/aot-compiler#the-ahead-of-time-aot-compiler)

> « Le compilateur Angular Ahead-of-Time convertit votre code Angular HTML et TypeScript en code JavaScript efficace pendant la phase de construction avant que le navigateur ne télécharge et n'exécute ce code. »

L'un des avantages de l'activation de AOT est un **rendement plus rapide de l'application**. Comme toutes les parties de l'application sont déjà compilées lors du téléchargement par le navigateur, il y a une diminution significative du temps de démarrage de l'application ainsi que des temps de rendu pendant son utilisation.

Un autre avantage peut être une **taille de bundle plus petite**. Lorsque vous utilisez AOT, vous n'avez pas besoin d'inclure [@angular/compiler](https://angular.io/api/core/Compiler) car il n'est plus nécessaire. L'application compilée peut augmenter en taille de bundle, mais cela dépend fortement des spécificités de votre application.

Troisièmement, il y a une bien plus grande possibilité de **repérer les erreurs de compilation dans les templates**, car vous serez notifié par le compilateur pendant la phase de construction. Si vous utilisez Visual Studio Code, vous pouvez utiliser l'extension [Angular Language Service](https://marketplace.visualstudio.com/items?itemName=Angular.ng-template) car elle a les diagnostics AOT activés en temps réel.

#### Étapes nécessaires pour activer AOT

La première étape, comme il se trouve, est d'exécuter _npm install [@ngtools/webpack](https://www.npmjs.com/package/@ngtools/webpack)_.

Ensuite, vous devez configurer Webpack correctement. Dans cette étape, vous voulez configurer AngularCompilerPlugin qui vient avec @ngtools. En utilisant les paramètres de configuration, vous définirez les emplacements des fichiers tsconfig et des fichiers d'entrée. La plupart du temps, vous voulez utiliser des tsconfigs séparés pour JIT et pour AOT. Vous verrez pourquoi dans un instant.

Dans votre tsconfig standard, vous devez exclure le fichier main.aot.ts, qui est le point d'entrée pour les applications compilées avec AOT. Dans ce fichier, vous importerez des fichiers qui ne seront disponibles que pendant la phase de construction. De cette manière, vous pouvez séparer facilement les builds JIT et AOT, sans aucune erreur.

Le tsconfig pour AOT est ordinaire. Il n'y a rien de spécial à son sujet.

Le fichier suivant est là pour démontrer comment nous pouvons séparer les builds entre JIT et AOT. Dans ce cas, JIT est utilisé dans un environnement de développement et AOT est utilisé en production.

AOT utilise platformBrowser au lieu de platformBrowserDynamic. L'étape importante suivante est d'importer les fichiers de factory qui seront disponibles pendant la phase de construction.

#### Améliorations des performances

Dès le début, nous voulions activer AOT pour une raison — avoir de meilleures performances de l'application [Admin](https://admin.sli.do). Voici une courte comparaison de ce qui s'est amélioré et de ce qui est resté le même :

Comme vous pouvez le voir, le temps de chargement initial a considérablement diminué même lorsque la taille du bundle a légèrement augmenté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E9l7k2n4OsqbiQtlg26ANw.png)
_Apdex mesuré avant et après la sortie de AOT en production._

![Image](https://cdn-media-1.freecodecamp.org/images/1*lgQobPbYaeh8duw-2ePnTg.png)
_Les temps de chargement moyens ont diminué même lorsque le débit est resté le même._

![Image](https://cdn-media-1.freecodecamp.org/images/1*LKYyX2rAR0r1p8zaUA2-kA.png)
_Les temps de chargement moyens comparés dans un histogramme superposé (sombre=JIT, clair=AOT)._

#### Conclusion

L'activation de AOT a entraîné une amélioration notable pour tous nos utilisateurs. Les temps de chargement initiaux se sont considérablement améliorés et l'application s'est également accélérée.

Si vous n'avez jamais envisagé d'activer AOT en production, c'est le moment. Avez-vous des questions sur ce sujet ? N'hésitez pas à me contacter.
---
title: Interface en Ligne de Commande Angular Expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/angular-command-line-interface-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d07740569d1a4ca3582.jpg
tags:
- name: Angular
  slug: angular
- name: cli
  slug: cli
- name: command line
  slug: command-line
- name: toothbrush
  slug: toothbrush
seo_title: Interface en Ligne de Commande Angular Expliquée
seo_desc: Angular is closely associated with its command-line interface (CLI). The
  CLI streamlines generation of the Angular file system. It deals with most of the
  configuration behind the scenes so developers can start coding. The CLI also has
  a low learning ...
---

Angular est étroitement associé à son interface en ligne de commande (CLI). Le CLI rationalise la génération du système de fichiers Angular. Il gère la plupart de la configuration en arrière-plan afin que les développeurs puissent commencer à coder. Le CLI a également une courbe d'apprentissage faible, recommandable pour tout nouveau venu souhaitant se lancer directement. En fait, même les développeurs Angular expérimentés s'appuient sur le CLI !

## Installation

L'interface en ligne de commande Angular nécessite [Node.js et Node Packet Manager (NPM)](https://nodejs.org/en/). Vous pouvez vérifier la présence de ces programmes avec la commande terminal : `node -v; npm -v`. Une fois installés, ouvrez un terminal et installez l'interface en ligne de commande Angular avec cette commande : `npm install -g @angular/cli`. Cela peut être exécuté depuis n'importe quel endroit de votre système. Le CLI est configuré pour une utilisation globale avec le drapeau `-g`.

Vérifiez la présence du CLI avec la commande : `ng -v`. Cela affiche plusieurs lignes d'informations. L'une de ces lignes indique la version du CLI installé.

Reconnaissez que `ng` est le bloc de construction de base du CLI. Toutes vos commandes commenceront par `ng`. Il est temps de jeter un coup d'œil à quatre des commandes les plus courantes préfixées par `ng`.

## Commandes Clés

* ng new
* ng serve
* ng generate
* ng build
* ng update

Les termes clés pour chacune de ces commandes sont assez révélateurs. Ensemble, ils comprennent ce dont vous aurez besoin pour démarrer avec Angular. Bien sûr, il y en a beaucoup d'autres. Toutes les commandes sont détaillées dans la [Documentation GitHub du CLI<sup>1</sup>](https://github.com/angular/angular-cli/wiki#additional-commands). Vous constaterez probablement que les commandes listées ci-dessus couvrent les bases nécessaires.

### ng new

`ng new` crée un _nouveau_ système de fichiers Angular. C'est un processus surréaliste. Veuillez naviguer vers un emplacement de fichier souhaitable pour la génération de _nouvelle_ application. Tapez cette commande comme suit, en remplaçant `[name-of-app]` par ce que vous voulez : `ng new [name-of-app]`.

Un système de fichiers sous le dossier `[name-of-app]` devrait apparaître. N'hésitez pas à explorer ce qui s'y trouve. Essayez de ne pas faire de changements pour l'instant. Tout ce dont vous avez besoin pour exécuter votre première application Angular est regroupé dans ce système de fichiers généré.

### ng serve

Pour faire fonctionner l'application, la commande `ng serve` doit être exécutée dans le dossier `[name-of-app]`. N'importe où dans le dossier fera l'affaire. L'interface en ligne de commande Angular doit reconnaître qu'elle se trouve dans un environnement généré avec `ng new`. Elle s'exécutera à condition que cette condition soit remplie. Allez-y et essayez : `ng serve`.

L'application s'exécute sur le port 4200 par défaut. Vous pouvez voir l'application Angular en naviguant vers `localhost:4200` dans n'importe quel navigateur web. Angular fonctionne sur tous les navigateurs. À moins que vous n'utilisiez une ancienne version d'Internet Explorer, l'application s'affichera. Elle affiche le logo officiel Angular ainsi qu'une liste de liens utiles.

D'accord, l'application fonctionne. Elle fonctionne, mais vous devez savoir ce qui se passe sous le capot. Référez-vous au système de fichiers `[name-of-app]`. Naviguez vers `[name-of-app] -> src -> app`. C'est là que se trouvent les fichiers responsables de ce que vous avez vu sur `localhost:4200`.

### ng generate

Les fichiers `.component` définissent un composant Angular, y compris sa logique (`.ts`), son style (`.css`), sa mise en page (`.html`) et ses tests (`.spec.ts`). Le fichier `app.module.ts` se distingue particulièrement. Ensemble, ces deux groupes de fichiers fonctionnent comme `component` et `module`. `component` et `module` sont deux exemples séparés de schémas Angular. Les schémas classent les différents blocs de code orientés but _générables_ avec `ng generate`.

Pour les besoins de cet article, comprenez qu'un `module` exporte et importe des actifs vers et depuis un arbre de composants sous-jacent. Un `component` se préoccupe d'une section de l'interface utilisateur. La logique, le style, la mise en page et les tests de cette unité restent encapsulés dans les divers fichiers `.component`.

Quant à `ng generate`, cette commande peut générer des squelettes pour chacun des [schémas Angular disponibles<sup>2</sup>](https://github.com/angular/angular-cli/wiki/generate#available-schematics). Naviguez vers `[name-of-app -> src -> app]`. Essayez de générer un nouveau `component` en exécutant : `ng generate component [name-of-component]`. Remplacez `[name-of-component]` par ce que vous souhaitez. Un nouveau fichier `[name-of-component]` apparaîtra avec ses fichiers `component` nécessaires.

Vous pouvez voir que `ng generate` accélère le [code boilerplate](https://en.wikipedia.org/wiki/Boilerplate_code) d'Angular. `ng generate` connecte également les choses. Les schémas créés dans le contexte d'un système de fichiers Angular se connectent au module racine du système. Dans ce cas, ce serait le fichier `app.module.ts` à l'intérieur de `[name-of-app -> src -> app]`.

### ng build

Angular est un outil front-end. Le CLI effectue ses opérations au nom du front-end. `ng serve` prend en charge la configuration du serveur back-end. Cela garde le développement entièrement axé sur le front-end. Cela dit, connecter votre propre back-end à l'application Angular doit également être possible.

`ng build` répond à ce besoin. Avant de l'essayer à l'intérieur du système de fichiers. Naviguez vers `[name-of-app] -> angular.json`. Cherchez cette ligne de code : `"outputPath": "dist/my-app"`.

Cette ligne de configuration détermine où `ng build` dépose ses résultats. Les résultats étant l'ensemble de l'application Angular compilée dans un dossier `dist/my-app`. À l'intérieur de ce dossier, il existe `index.html`. L'ensemble de l'application Angular peut fonctionner avec `index.html`. Aucun `ng serve` n'est nécessaire à partir de là. Avec ce fichier, vous pouvez facilement connecter votre back-end.

Essayez-le : `ng build`. Encore une fois, cela doit être exécuté dans le système de fichiers Angular. Basé sur la valeur clé de `"outputPath:"` dans `angular.json`. Un fichier sera généré dans lequel l'application originale est entièrement compilée. Si vous avez gardé `"outputPath:"` le même, l'application compilée sera dans : `[name-of-app] -> dist -> [name-of-app]`.

### ng update

Dans l'interface en ligne de commande Angular, `ng update` effectue automatiquement la mise à jour de tous les packages Angular et npm vers les dernières versions.

Voici la syntaxe et les options qui peuvent être utilisées avec `ng update`.

`ng update [package]`

### Options

* dry-run `--dry-run (alias: -d)`  
Exécute sans apporter de modifications.
* force `--force`  
Si faux, générera une erreur si les packages installés sont incompatibles avec la mise à jour.
* all `--all`  
Mettre à jour tous les packages dans package.json.
* next `--next`  
Utilise la plus grande version, y compris les bêta et les RC.
* migrate-only `--migrate-only`  
Effectue uniquement une migration, ne met pas à jour la version installée.
* from `--from`  
Version à partir de laquelle migrer. Disponible uniquement avec un seul package mis à jour, et uniquement en migration seule.
* to `--to`  
Version jusqu'à laquelle appliquer les migrations. Disponible uniquement avec un seul package mis à jour, et uniquement en migrations seules. Nécessite que from soit spécifié. Par défaut, la version installée détectée.
* registry `--registry`  
Le registre NPM à utiliser.

Ces commandes couvrent les bases. L'interface en ligne de commande d'Angular est une commodité incroyable qui accélère la génération, la configuration et l'expansion des applications. Elle fait tout cela tout en maintenant la flexibilité, permettant au développeur d'apporter les modifications nécessaires.

Veuillez consulter ces liens sur `localhost:4200` si vous ne l'avez pas déjà fait. N'oubliez pas d'exécuter `ng serve` avant de l'ouvrir. Avec une meilleure compréhension du CLI, vous êtes maintenant prêt à en apprendre davantage sur ce qui est généré par ses commandes les plus essentielles.

## Plus d'informations :

* [Les Meilleurs Exemples Angular](https://www.freecodecamp.org/news/the-best-angular-examples/)
* [Les Meilleurs Didacticiels Angular et AngularJS](https://www.freecodecamp.org/news/best-angular-tutorial-angularjs/)
* [Comment Valider les Formulaires Réactifs Angular](https://www.freecodecamp.org/news/how-to-validate-angular-reactive-forms/)
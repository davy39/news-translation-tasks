---
title: Comment commencer avec Angular 6.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-06T16:16:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-angular-6-0-a196cbfb9bbb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mmxWHaqZZtNMs_ggYnx8hg.jpeg
tags:
- name: Angular
  slug: angularjs
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Visual Studio Code
  slug: visual-studio-code
seo_title: Comment commencer avec Angular 6.0
seo_desc: 'By Ankit Sharma

  Learn what’s new and build an app

  Angular has released its latest version, Angular 6.0. In this article, we will understand
  the new features of Angular 6.0 and also set up a new project with the help of Angular
  CLI 6.0 and Visual Stud...'
---

Par Ankit Sharma

#### Apprenez les nouveautés et créez une application

Angular a publié sa dernière version, Angular 6.0. Dans cet article, nous allons comprendre les nouvelles fonctionnalités d'Angular 6.0 et également configurer un nouveau projet à l'aide d'Angular CLI 6.0 et de Visual Studio Code.

### Qu'y a-t-il de nouveau dans Angular 6.0 ?

#### ng update

Une nouvelle commande CLI qui mettra à jour les dépendances de votre projet vers leurs dernières versions.

#### ng add

Une autre nouvelle commande CLI qui facilite l'ajout de nouvelles fonctionnalités à votre projet.

#### Angular Elements

Il s'agit d'une nouvelle fonctionnalité qui nous permet de compiler des composants Angular en composants web natifs que nous pouvons utiliser dans notre application Angular.

#### L'élément <template> est obsolète

Vous ne pouvez plus utiliser <template> dans vos modèles de composants. Vous devez utiliser <ng-template> à la place.

#### Support des bibliothèques

Angular CLI dispose désormais du support pour la création et la construction de bibliothèques. Pour créer un projet de bibliothèque dans votre espace de travail CLI, exécutez la commande suivante : ng generate library <name> (par exemple : ng generate library my-demo-lib)

#### Composants de démarrage Angular Material

Si vous exécutez « ng add @angular/material » pour ajouter material à une application existante, vous pourrez également générer 3 nouveaux composants de démarrage :

* **Material Sidenav**  
 Un composant de démarrage incluant une barre d'outils avec le nom de l'application et la navigation latérale
* **Material Dashboard**  
 Un composant de tableau de bord de démarrage contenant une liste dynamique de cartes en grille
* **Material Data Table**  
 Un composant de table de données de démarrage pré-configuré avec une source de données pour le tri et la pagination

#### Support de l'espace de travail

Angular CLI dispose désormais du support pour les espaces de travail contenant plusieurs projets, tels que plusieurs applications et/ou bibliothèques.

#### Le fichier « .angular-cli.json » est obsolète

Les projets Angular utiliseront désormais « angular.json » au lieu de « .angular-cli.json » pour la configuration de la construction et du projet.

#### Utilisation de RxJS V6

Angular 6 nous permettra également d'utiliser RxJS V6 avec notre application.

#### Fournisseurs « Tree Shakable »

Angular 6.0 nous permet de regrouper les services dans la base de code dans les modules où ils sont injectés. Cela nous aidera à rendre notre application plus petite.

Par exemple : Auparavant, nous utilisions pour référencer nos services comme ci-dessous.

```
// Dans app.module.ts    @NgModule({    ...    providers: [MyService]  })  export class AppModule {}    // Dans myservice.ts     import { Injectable } from '@angular/core';    @Injectable()  export class MyService {    constructor() { }  }
```

Cette approche fonctionnera toujours, mais Angular 6.0 fournit une nouvelle alternative plus facile. Nous n'avons plus besoin d'ajouter des références dans notre NgModule. Nous pouvons injecter la référence directement dans le service. Par conséquent, nous pouvons utiliser le service comme ci-dessous :

```
// Dans myservice.ts    import { Injectable } from '@angular/core';    @Injectable({    providedIn: 'root',  })  export class MyService {    constructor() { }  }
```

Ce sont les nouvelles fonctionnalités/améliorations de la dernière version d'Angular. Passons à la création de notre première application en utilisant Angular 6.0.

### Prérequis

* Installer la dernière version de Node.js depuis [ici](https://nodejs.org/en/download/)
* Installer Visual Studio Code depuis [ici](https://code.visualstudio.com/)

L'installation de Node.js installera également npm sur votre machine. Après avoir installé Node.js, ouvrez l'invite de commande et exécutez la série de commandes suivante pour vérifier la version de Node et npm installée sur votre machine.

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/PpLMXyOskr9A5wpHDndRTG8IkvpRvJ6H9DVb)

Maintenant que nous avons installé Node et npm, l'étape suivante consiste à installer Angular CLI. Exécutez la commande suivante dans une fenêtre de commande. Cela installera Angular 6.0 CLI globalement sur votre machine.

![Image](https://cdn-media-1.freecodecamp.org/images/rskMSFRtqxuqxXA80OYMwHVhnR-3AGrxDsS5)

Ouvrez VS Code et naviguez vers View >> Integrated Terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/-bJC4pD8YZXAZdB2h6ez7WjmdZWcS0D5IpMo)

Cela ouvrira une fenêtre de terminal dans VS Code.

Tapez la séquence de commandes suivante dans la fenêtre du terminal. Ces commandes créeront un répertoire avec le nom « ng6Demo » puis créeront une application Angular avec le nom « ng6App » à l'intérieur de ce répertoire.

* mkdir ng6Demo
* cd ng6Demo
* ng new ng6App

![Image](https://cdn-media-1.freecodecamp.org/images/n7ub05-40gA8P9HxCosSWJDoy5PyYSA0kHoA)

Nous avons créé notre première application Angular 6 en utilisant VS Code et Angular CLI. Exécutez maintenant la commande suivante pour ouvrir le projet.

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/hcwLxqSELFiSmKaGJ9Wbjmlmtm4ThL1ZpNVU)

Cela ouvrira le fichier de code de notre application dans une nouvelle fenêtre VS Code. Vous pouvez voir la structure de fichier suivante dans l'Explorateur de solutions.

![Image](https://cdn-media-1.freecodecamp.org/images/m8PPvMTg1DzehHavw-zrEx16BuG-RIQ5jMSy)

Remarquez que la structure des dossiers est un peu différente de l'ancienne version d'Angular. Nous avons un nouveau fichier « angular.json » au lieu de l'ancien fichier « .angular-cli.json ». Ce fichier de configuration remplira toujours la même tâche qu'avant, mais le schéma a un peu changé.

Ouvrez le fichier package.json et vous pouvez observer que nous avons les derniers packages Angular 6.0.0 installés dans notre projet.

```
{    "name": "ng6-app",    "version": "0.0.0",    "scripts": {      "ng": "ng",      "start": "ng serve",      "build": "ng build",      "test": "ng test",      "lint": "ng lint",      "e2e": "ng e2e"    },    "private": true,    "dependencies": {      "@angular/animations": "^6.0.0",      "@angular/common": "^6.0.0",      "@angular/compiler": "^6.0.0",      "@angular/core": "^6.0.0",      "@angular/forms": "^6.0.0",      "@angular/http": "^6.0.0",      "@angular/platform-browser": "^6.0.0",      "@angular/platform-browser-dynamic": "^6.0.0",      "@angular/router": "^6.0.0",      "core-js": "^2.5.4",      "rxjs": "^6.0.0",      "zone.js": "^0.8.26"    },    "devDependencies": {      "@angular/compiler-cli": "^6.0.0",      "@angular-devkit/build-angular": "~0.6.0",      "typescript": "~2.7.2",      "@angular/cli": "~6.0.0",      "@angular/language-service": "^6.0.0",      "@types/jasmine": "~2.8.6",      "@types/jasminewd2": "~2.0.3",      "@types/node": "~8.9.4",      "codelyzer": "~4.2.1",      "jasmine-core": "~2.99.1",      "jasmine-spec-reporter": "~4.2.1",      "karma": "~1.7.1",      "karma-chrome-launcher": "~2.2.0",      "karma-coverage-istanbul-reporter": "~1.4.2",      "karma-jasmine": "~1.1.1",      "karma-jasmine-html-reporter": "^0.2.2",      "protractor": "~5.3.0",      "ts-node": "~5.0.1",      "tslint": "~5.9.1"    }  }
```

Le nom de notre application Angular est _ng6app_ qui se trouve dans le répertoire _ng6demo_.

Nous allons donc d'abord naviguer vers notre application en utilisant les commandes ci-dessous.

Puis nous utilisons la commande suivante pour démarrer le serveur web.

![Image](https://cdn-media-1.freecodecamp.org/images/aERCZwSg9S74d2ZxBtQxwx50kL2IRfmJjSYy)

Après avoir exécuté cette commande, vous pouvez voir qu'il demande d'ouvrir [_http://localhost:4200_](http://localhost:4200) dans votre navigateur. Ouvrez donc un navigateur sur votre machine et naviguez vers cette URL. Vous pouvez maintenant voir la page suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/IjRPyX7l6pOcgmXtT3ml1WSYRFU09uhDrGAD)

Nous allons maintenant essayer de changer le texte de bienvenue à l'écran. Naviguez vers le fichier _/src/app/app.component.ts_ et remplacez le code par le code ci-dessous.

```
import { Component } from '@angular/core';    @Component({    selector: 'app-root',    templateUrl: './app.component.html',    styleUrls: ['./app.component.css']  })  export class AppComponent {    title = 'Csharp Corner';  }
```

Ouvrez maintenant le navigateur, vous pouvez voir que la page web a été mise à jour avec le nouveau message de bienvenue « Bienvenue chez Csharp Corner ! »

![Image](https://cdn-media-1.freecodecamp.org/images/c5mAy0iqq0fAlCVSgceh51pMHuH7OEoreQXN)

Dans cet article, nous avons appris les nouvelles fonctionnalités d'Angular 6.0. Nous avons installé Angular 6.0 CLI et créé notre première application Angular 6.0 à l'aide de Visual Studio Code. Nous avons également personnalisé le message de bienvenue sur la page web.

Vous pouvez également trouver cet article sur [C# Corner](https://www.c-sharpcorner.com/article/getting-started-with-angular-6/).

Vous pouvez consulter mes autres articles sur Angular [ici](http://ankitsharmablogs.com/category/angular/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)
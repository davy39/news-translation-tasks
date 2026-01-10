---
title: Quoi de neuf dans Angular 7.0 et comment mettre à jour
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-02T15:16:46.000Z'
originalURL: https://freecodecamp.org/news/whats-new-in-angular-7-0-and-how-to-upgrade-f2ed22a79e28
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TzObK_L_fue2CAxYOG-CnA.jpeg
tags:
- name: Angular
  slug: angularjs
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Quoi de neuf dans Angular 7.0 et comment mettre à jour
seo_desc: 'By Ankit Sharma

  Introduction

  Angular has released its latest version, Angular 7.0. In this article, we will explore
  the following points:


  What is new in Angular 7.0

  Creating your first Angular 7.0 application using Angular CLI

  How to update your exi...'
---

Par Ankit Sharma

### Introduction

Angular a publié sa dernière version, Angular 7.0. Dans cet article, nous allons explorer les points suivants :

* Ce qui est nouveau dans Angular 7.0
* Créer votre première application Angular 7.0 en utilisant Angular CLI
* Comment mettre à jour votre application Angular existante vers Angular 7.0

### Qu'est-ce qu'il y a de nouveau dans Angular 7.0 ?

1. Lors de la création d'une nouvelle application Angular, l'Angular CLI demandera à l'utilisateur de sélectionner s'il souhaite ajouter des fonctionnalités comme le routage Angular ou le format de la feuille de style qu'il souhaite utiliser dans son application.
2. Les applications Angular 7.0 utiliseront la fonctionnalité Bundle Budget de Angular CLI. Cela avertira les développeurs si la taille du bundle de l'application dépasse la limite prédéfinie. La valeur par défaut pour l'avertissement est fixée à 2 Mo, et pour les erreurs, elle est de 5 Mo. Cette valeur est configurable et peut être modifiée dans le fichier `angular.json`. Cette fonctionnalité améliore considérablement les performances de l'application.
3. Le Component Dev Kit (CDK) d'Angular Material reçoit également de nouvelles fonctionnalités dans le cadre de cette mise à jour. Les deux nouvelles fonctionnalités du CDK sont :

* **Défilement virtuel** Si vous essayez de charger une grande liste d'éléments, cela peut affecter les performances de l'application. La balise `<cdk-virtual-scroll-viewport>` peut être utilisée pour charger uniquement la partie visible de la liste à l'écran. Elle ne rendra que les éléments qui peuvent tenir sur l'écran. Lorsque l'utilisateur fait défiler la liste, le DOM chargera et déchargera les éléments dynamiquement en fonction de la taille de l'affichage. Cette fonctionnalité ne doit pas être confondue avec le défilement infini, qui est une stratégie différente pour charger les éléments. Vous pouvez en savoir plus sur le défilement virtuel [ici](https://material.angular.io/cdk/scrolling/overview).
* **Glisser-déposer**
Nous pouvons facilement ajouter la fonctionnalité de glisser-déposer à un élément. Elle prend en charge des fonctionnalités telles que le glisser libre d'un élément, le réordonnancement des éléments d'une liste, le déplacement des éléments entre les listes, l'animation, l'ajout d'une poignée de glisser personnalisée et le glisser restreint le long de l'axe X ou Y. Vous pouvez en savoir plus sur le glisser-déposer [ici](https://material.angular.io/cdk/drag-drop/overview).

4. Le `mat-form-field` prendra désormais en charge l'utilisation de l'élément select natif. Cela fournira des performances et une utilisabilité améliorées à l'application. En savoir plus sur cette fonctionnalité [ici](https://material.angular.io/components/select/overview).

5. Angular 7.0 a mis à jour ses dépendances pour prendre en charge Typescript 3.1, RxJS 6.3 et Node 10.

Nous allons maintenant procéder à la création de notre première application Angular 7.

### Prérequis

* Installer la dernière version de Node.js depuis [ici](https://nodejs.org/en/download/)
* Installer Visual Studio Code depuis [ici](https://code.visualstudio.com/)

L'installation de Node.js installera également npm sur votre machine. Après avoir installé Node.js, ouvrez l'invite de commande. Exécutez la série de commandes suivante pour vérifier la version de node et npm installée sur votre machine.

* node -v
* npm -v

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/aMRrmSzH02XbSjMH7iLL9dvL2Rwr5XfDmZt2)

### **Installation d'Angular CLI**

Angular CLI est l'interface de ligne de commande pour Angular. Il nous aide à initialiser, développer et maintenir facilement les applications Angular.

Pour installer Angular CLI, exécutez la commande suivante dans la fenêtre de commande :

```bash
npm i -g @angular/cli
```

Cela installera Angular CLI 7.0 globalement sur votre machine. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/8NjtUfzQgZ5lz5xVnOzj3lrK3NGmVmGgmnYx)

Pour vérifier la version d'Angular CLI installée sur votre machine, exécutez la commande suivante :

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/0XwEnfOjRufctv0XNKSSLF2eDeClji0XyNnS)

### **Créer l'application Angular 7**

Ouvrez Visual Studio Code et naviguez vers `View >> Terminal`. Cela ouvrira la fenêtre du terminal VS Code. Alternativement, vous pouvez également utiliser le raccourci clavier `ctrl + \` pour ouvrir la fenêtre du terminal.

Tapez la séquence de commandes suivante dans la fenêtre du terminal. Ces commandes créeront un répertoire nommé « ng7Demo ». Ensuite, créez une application Angular avec le nom « ng7App » à l'intérieur de ce répertoire.

* mkdir ng7Demo
* cd ng7Demo
* ng new ng7App

Lorsque vous exécutez la commande ng new, l'Angular CLI vous demandera de faire des sélections dans les deux options suivantes :

1. Souhaitez-vous ajouter le routage Angular ? (y/N)
2. Quel format de feuille de style souhaitez-vous utiliser ?

Une fois que vous avez sélectionné les options et appuyé sur Entrée, l'application Angular 7.0 sera créée.

Voir le GIF ci-dessous pour une meilleure compréhension.

![Image](https://cdn-media-1.freecodecamp.org/images/SSJPhveMoVdyPvtAq5QrSiiHSdXqH7mH8djN)

Une fois l'application créée avec succès, exécutez la commande suivante pour ouvrir le projet :

* code .

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/ir01hAZ0pkSePN0SX3A51Ce7QR11SPt7lGcs)

Cela ouvrira le fichier de code de notre application dans une nouvelle fenêtre VS Code. Vous pouvez voir la structure de fichier suivante dans l'Explorateur de solutions.

![Image](https://cdn-media-1.freecodecamp.org/images/2FThBN1bRwDkeqIXvqgAG6A86Kbs5eZjMuXD)

Ouvrez le fichier package.json et vous pouvez observer que nous avons les derniers paquets Angular 7.0.0 installés dans notre projet.

```json
{
  "name": "ng7-app",
  "version": "0.0.0",
  "scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "test": "ng test",
    "lint": "ng lint",
    "e2e": "ng e2e"
  },
  "private": true,
  "dependencies": {
    "@angular/animations": "~7.0.0",
    "@angular/common": "~7.0.0",
    "@angular/compiler": "~7.0.0",
    "@angular/core": "~7.0.0",
    "@angular/forms": "~7.0.0",
    "@angular/http": "~7.0.0",
    "@angular/platform-browser": "~7.0.0",
    "@angular/platform-browser-dynamic": "~7.0.0",
    "@angular/router": "~7.0.0",
    "core-js": "^2.5.4",
    "rxjs": "~6.3.3",
    "zone.js": "~0.8.26"
  },
  "devDependencies": {
    "@angular-devkit/build-angular": "~0.10.0",
    "@angular/cli": "~7.0.1",
    "@angular/compiler-cli": "~7.0.0",
    "@angular/language-service": "~7.0.0",
    "@types/node": "~8.9.4",
    "@types/jasmine": "~2.8.8",
    "@types/jasminewd2": "~2.0.3",
    "codelyzer": "~4.5.0",
    "jasmine-core": "~2.99.1",
    "jasmine-spec-reporter": "~4.2.1",
    "karma": "~3.0.0",
    "karma-chrome-launcher": "~2.2.0",
    "karma-coverage-istanbul-reporter": "~2.0.1",
    "karma-jasmine": "~1.1.2",
    "karma-jasmine-html-reporter": "^0.2.2",
    "protractor": "~5.4.0",
    "ts-node": "~7.0.0",
    "tslint": "~5.11.0",
    "typescript": "~3.1.1"
  }
}
```

### Démonstration d'exécution

Le nom de notre application Angular est _ng7App_ qui se trouve dans le répertoire _ng7Demo_.

Nous allons donc d'abord naviguer vers notre application en utilisant les commandes suivantes.

* cd ng7Demo
* cd ng7App

Maintenant, nous utilisons la commande suivante pour démarrer le serveur web.

* ng serve

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/I9P20l7DxHfFzooUz8JWUhU7bFc4sJUxJE3C)

Après avoir exécuté cette commande, vous pouvez voir qu'elle demande d'ouvrir `_http://localhost:4200_` dans votre navigateur. Ouvrez donc un navigateur sur votre machine et naviguez vers cette URL. Vous pouvez maintenant voir la page suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/lN5VU04tLKYoxfQskGaAnPXuSAVkdm94l0TS)

### Comment mettre à jour vers Angular 7

L'équipe Angular a fourni un guide de mise à jour Angular pour garantir une mise à jour fluide des versions Angular. Naviguez vers [https://update.angular.io/](https://update.angular.io/) pour y accéder. C'est une application auto-explicative et facile à utiliser. Elle vous montrera les étapes à suivre avant la mise à jour, pendant la mise à jour et après la mise à jour. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/DQoXJZqvZgwkWCf0zbqH8S-0V7M9oqWmIDdP)

Si vous souhaitez mettre à jour votre application d'Angular 6 vers Angular 7, exécutez la commande suivante dans le dossier du projet :

```bash
ng update @angular/cli @angular/core
```

### Conclusion

Nous avons appris les nouvelles fonctionnalités d'Angular 7.0. Nous avons également installé Angular CLI 7.0. Pour créer et exécuter une application Angular 7.0, nous avons utilisé Angular CLI et VS Code. Nous avons également exploré la méthode pour mettre à jour une application existante vers Angular 7.0.

### Voir aussi

* [Commencer avec Angular 6.0](https://ankitsharmablogs.com/getting-started-with-angular-6-0/)
* [Comprendre les animations Angular 6](https://ankitsharmablogs.com/understanding-angular-6-animations/)
* [Commencer avec Angular 5 en utilisant Visual Studio Code](https://ankitsharmablogs.com/getting-started-with-angular-5-using-visual-studio-code/)
* [Opérations CRUD avec ASP.NET Core en utilisant Angular 5 et ADO.NET](https://ankitsharmablogs.com/crud-operations-asp-net-core-using-angular-5-ado-net/)
* [ASP.NET Core — CRUD en utilisant Angular 5 et Entity Framework Core](https://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [ASP.NET Core — Utilisation de Highcharts avec Angular 5](https://ankitsharmablogs.com/asp-net-core-using-highcharts-with-angular-5/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)
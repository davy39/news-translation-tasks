---
title: Comment ajouter ESLint à une application Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-15T16:39:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-eslint-to-an-angular-application
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/angular-eslint-cover-hashnode.png
tags:
- name: Angular
  slug: angular
- name: eslint
  slug: eslint
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Comment ajouter ESLint à une application Angular
seo_desc: 'By Rodrigo Kamada

  In this article, we''ll build a web application using the latest version of Angular.
  Then we''ll add ESLint which analyzes the JavaScript code statically to find any
  problems.

  Prerequisites

  Before you start, you need to install and co...'
---

Par Rodrigo Kamada

Dans cet article, nous allons créer une application web en utilisant la dernière version d'[Angular](https://angular.io/). Ensuite, nous ajouterons [ESLint](https://eslint.org/) qui analyse statiquement le code JavaScript pour trouver d'éventuels problèmes.

## Prérequis

Avant de commencer, vous devez installer et configurer les outils suivants (si ce n'est pas déjà fait) pour créer l'application Angular :

* [Git](https://git-scm.com/) : Git est un système de contrôle de version distribué. Nous l'utiliserons pour synchroniser le dépôt.
* [Node.js et npm](https://nodejs.org/) : Node.js est un logiciel d'exécution de code JavaScript basé sur le moteur V8 de Google. npm est un gestionnaire de paquets pour Node.js (Node Package Manager). Nous les utiliserons pour construire et exécuter l'application Angular et installer les bibliothèques.
* [Angular CLI](https://angular.io/cli) : Angular CLI est un outil utilitaire en ligne de commande pour Angular. Nous l'utiliserons pour créer la structure de base de l'application Angular.
* IDE (par exemple [Visual Studio Code](https://code.visualstudio.com/) ou [WebStorm](https://www.jetbrains.com/webstorm/)) : un Environnement de Développement Intégré est un outil avec une interface graphique pour aider au développement d'applications. Nous l'utiliserons pour développer l'application Angular.

## Mise en route

### Créer l'application Angular

Angular est une plateforme de développement pour construire des applications web, mobiles et de bureau en utilisant HTML, CSS et TypeScript (JavaScript). Actuellement, Angular est à la version 14 et Google est le principal mainteneur du projet.

Tout d'abord, créons l'application avec la structure de base Angular en utilisant `@angular/cli` avec le fichier de route et le format de style SCSS.

```
ng new angular-eslint --routing true --style scss
CREATE angular-eslint/README.md (1067 bytes)
CREATE angular-eslint/.editorconfig (274 bytes)
CREATE angular-eslint/.gitignore (548 bytes)
CREATE angular-eslint/angular.json (3136 bytes)
CREATE angular-eslint/package.json (1045 bytes)
CREATE angular-eslint/tsconfig.json (863 bytes)
CREATE angular-eslint/.browserslistrc (600 bytes)
CREATE angular-eslint/karma.conf.js (1431 bytes)
CREATE angular-eslint/tsconfig.app.json (287 bytes)
CREATE angular-eslint/tsconfig.spec.json (333 bytes)
CREATE angular-eslint/.vscode/extensions.json (130 bytes)
CREATE angular-eslint/.vscode/launch.json (474 bytes)
CREATE angular-eslint/.vscode/tasks.json (938 bytes)
CREATE angular-eslint/src/favicon.ico (948 bytes)
CREATE angular-eslint/src/index.html (299 bytes)
CREATE angular-eslint/src/main.ts (372 bytes)
CREATE angular-eslint/src/polyfills.ts (2338 bytes)
CREATE angular-eslint/src/styles.scss (80 bytes)
CREATE angular-eslint/src/test.ts (749 bytes)
CREATE angular-eslint/src/assets/.gitkeep (0 bytes)
CREATE angular-eslint/src/environments/environment.prod.ts (51 bytes)
CREATE angular-eslint/src/environments/environment.ts (658 bytes)
CREATE angular-eslint/src/app/app-routing.module.ts (245 bytes)
CREATE angular-eslint/src/app/app.module.ts (393 bytes)
CREATE angular-eslint/src/app/app.component.scss (0 bytes)
CREATE angular-eslint/src/app/app.component.html (23364 bytes)
CREATE angular-eslint/src/app/app.component.spec.ts (1097 bytes)
CREATE angular-eslint/src/app/app.component.ts (219 bytes)
✓ Packages installés avec succès.
    Initialisation de git réussie.
```

Maintenant, nous allons installer les bibliothèques et ajouter les paramètres ESLint.

```
ng add @angular-eslint/schematics
⏹ Utilisation du gestionnaire de paquets : npm
✓ Version compatible du package trouvée : @angular-eslint/schematics@14.2.5.
✓ Informations du package chargées.

Le package @angular-eslint/schematics@14.2.5 sera installé et exécuté.
Souhaitez-vous continuer ? Oui
✓ Packages installés avec succès.

    Toutes les dépendances @angular-eslint ont été installées avec succès 🎉

    Veuillez consulter https://github.com/angular-eslint/angular-eslint pour savoir comment ajouter la configuration ESLint à votre projet.

    Nous avons détecté que vous avez un seul projet dans votre espace de travail et aucun linter existant configuré, nous configurons donc ESLint pour vous automatiquement.

    Veuillez consulter https://github.com/angular-eslint/angular-eslint pour plus d'informations.

CREATE .eslintrc.json (984 bytes)
UPDATE package.json (1511 bytes)
UPDATE angular.json (3447 bytes)
✓ Packages installés avec succès.
```

Ensuite, nous allons exécuter la commande suivante pour valider l'installation et la configuration d'ESLint :

```
npm run lint

> angular-eslint@1.0.0 lint /home/rodrigokamada/angular-eslint
> ng lint


Linting "angular-eslint"...

Tous les fichiers passent le linting.
```

Et c'est tout ! Le message "_Tous les fichiers passent le linting_" indique qu'aucun problème n'a été trouvé.

Le dépôt de l'application est [disponible ici](https://github.com/rodrigokamada/angular-eslint.).

## Conclusion

Voici ce que nous avons couvert dans cet article :

* Nous avons créé une application Angular.
* Nous avons ajouté ESLint pour analyser et trouver des problèmes avec le code.

Vous pouvez utiliser cela pour vérifier le code de votre application avant de le déployer dans votre environnement.

Merci d'avoir lu et j'espère que vous avez apprécié l'article !

Ce tutoriel a été publié sur mon [blog](https://rodrigo.kamada.com.br/blog/adicionando-o-eslint-em-uma-aplicacao-angular) en portugais.

Pour rester informé chaque fois que je publie de nouveaux articles, suivez-moi sur [Twitter](https://twitter.com/rodrigokamada) et [LinkedIn](https://www.linkedin.com/in/rodrigokamada).
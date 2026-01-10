---
title: 'Comment installer Angular sur Windows : Un guide pour Angular CLI, Node.js
  et les outils de build'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-21T23:39:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-angular-on-windows-a-guide-to-angular-cli-node-js-and-build-tools
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/angular-cli-install.png
tags:
- name: Angular
  slug: angular
- name: Node.js
  slug: nodejs
- name: Windows
  slug: windows
seo_title: 'Comment installer Angular sur Windows : Un guide pour Angular CLI, Node.js
  et les outils de build'
seo_desc: 'By Ahmed Bouchefra


  In this tutorial, we''ll learn how to install Angular CLI in Windows and use it
  to create an Angular project.

  What is Angular CLI?

  Angular CLI is the official tool for initializing and working with Angular projects.
  It saves you fr...'
---

Par Ahmed Bouchefra

![Image](https://www.freecodecamp.org/news/content/images/2019/12/angular-cli-install-1.png)

Dans ce tutoriel, nous allons apprendre comment installer Angular CLI sur Windows et l'utiliser pour créer un projet Angular.

## Qu'est-ce qu'Angular CLI ?

Angular CLI est l'outil officiel pour initialiser et travailler avec des projets Angular. Il vous évite les tracas des configurations complexes et des outils de build comme TypeScript, Webpack, etc.

Après avoir installé Angular CLI, vous devrez exécuter une commande pour générer un projet et une autre pour le servir en utilisant un serveur de développement local afin de tester votre application.

Comme la plupart des outils frontend modernes de nos jours, Angular CLI est construit sur Node.js.

Node.js est une technologie serveur qui vous permet d'exécuter JavaScript sur le serveur et de construire des applications web côté serveur. Cependant, Angular est une technologie frontend, donc même si vous devez installer Node.js sur votre machine de développement, c'est uniquement pour exécuter le CLI.

Une fois que vous avez construit votre application pour la production, vous n'aurez plus besoin de Node.js car les bundles finaux sont simplement du HTML, CSS et JavaScript statiques qui peuvent être servis par n'importe quel serveur ou un CDN.

Cela dit, si vous construisez une application web full-stack avec Angular, vous pourriez avoir besoin de Node.js pour créer la partie backend si vous souhaitez utiliser JavaScript pour le frontend et le backend.

Consultez la stack MEAN – c'est une architecture qui inclut MongoDB, Express (un serveur web et un framework d'API REST construit sur Node.js) et Angular. Vous pouvez lire cet [article](https://www.techiediaries.com/angular-9-8-mean-stack-authentication-tutorial-and-example-with-node-and-mongodb/) si vous souhaitez un tutoriel pas à pas pour commencer.

Dans ce cas, Node.js est utilisé pour construire la partie backend de votre application et peut être remplacé par n'importe quelle technologie côté serveur que vous souhaitez, comme PHP, Ruby ou Python. Mais Angular ne dépend pas de Node.js sauf pour son outil CLI et pour installer des packages depuis npm.

NPM signifie Node Package Manager. C'est un registre pour héberger des packages Node. Ces dernières années, il a également été utilisé pour publier des packages et bibliothèques frontend comme Angular, React, Vue.js et même Bootstrap.

**Note** : vous pouvez télécharger notre **[Livre Angular 8 : Construisez vos premières applications web avec Angular 8](https://www.techiediaries.com/angular-book-build-your-first-web-apps/)** gratuitement.

## Installation d'Angular CLI sur Windows

Tout d'abord, vous devez avoir Node et npm installés sur votre machine de développement. Il existe plusieurs façons de le faire, telles que :

* utiliser NVM (Node Version Manager) pour installer et travailler avec plusieurs versions de Node sur votre système
* utiliser le gestionnaire de packages officiel de votre système d'exploitation
* l'installer depuis le site officiel.

Gardons cela simple et utilisons le site officiel. Rendez-vous simplement sur la [page de téléchargement](https://nodejs.org/en/download/) et téléchargez les binaires pour Windows, puis suivez l'assistant d'installation.

Vous pouvez vérifier que Node est installé sur votre système en exécutant la commande suivante dans une invite de commande, qui doit afficher la version installée de Node :

```bash
$ node -v

```

Ensuite, exécutez la commande suivante pour installer Angular CLI :

```bash
$ npm install @angular/cli

```

Une fois la commande terminée avec succès, vous devriez avoir Angular CLI installé.

## Un guide rapide pour Angular CLI

Après avoir installé Angular CLI, vous pouvez exécuter de nombreuses commandes. Commençons par vérifier la version du CLI installé :

```bash
$ ng version

```

Une deuxième commande que vous pourriez avoir besoin d'exécuter est la commande `help` pour obtenir une aide complète sur l'utilisation :

```bash
$ ng help

```

Le CLI fournit les commandes suivantes :

`add` : Ajoute la prise en charge d'une bibliothèque externe à votre projet.

`build (b)` : Compile une application Angular dans un répertoire de sortie nommé `dist/` au chemin de sortie donné. Doit être exécuté depuis un répertoire de workspace.

`config` : Récupère ou définit les valeurs de configuration d'Angular.

`doc (d)` : Ouvre la documentation officielle d'Angular ([angular.io](https://angular.io/)) dans un navigateur et recherche un mot-clé donné.

`e2e (e)` : Construit et sert une application Angular, puis exécute des tests end-to-end en utilisant Protractor.

`generate (g)` : Génère et/ou modifie des fichiers basés sur un schéma.

`help` : Liste les commandes disponibles et leurs descriptions courtes.

`lint (l)` : Exécute des outils de linting sur le code de l'application Angular dans un dossier de projet donné.

`new (n)` : Crée un nouveau workspace et une application Angular initiale.

`run` : Exécute une cible personnalisée définie dans votre projet.

`serve (s)` : Construit et sert votre application, en la reconstruisant lors des changements de fichiers.

`test (t)` : Exécute des tests unitaires dans un projet.

`update` : Met à jour votre application et ses dépendances. Voir [https://update.angular.io/](https://update.angular.io/)

`version (v)` : Affiche la version d'Angular CLI.

`xi18n` : Extrait les messages i18n du code source.

## Génération d'un projet

Vous pouvez utiliser Angular CLI pour générer rapidement votre projet Angular en exécutant la commande suivante dans votre interface de ligne de commande :

```bash
$ ng new frontend


```

_Note :_ **frontend** _est le nom du projet. Vous pouvez, bien sûr, choisir n'importe quel nom valide pour votre projet. Puisque nous allons créer une application full-stack, j'utilise_ frontend _comme nom pour l'application frontend._

Comme mentionné précédemment, le CLI vous demandera _Souhaitez-vous ajouter le routage Angular ?_, et vous pouvez répondre en entrant `y` (Oui) ou `n` (Non), qui est l'option par défaut. Il vous demandera également le format de feuille de style que vous souhaitez utiliser (comme CSS). Choisissez vos options et appuyez sur `Entrée` pour continuer.

![Structure du projet Angular 8](https://www.techiediaries.com/ezoimgfmt/i.imgur.com/vQaSm5I.png?ezimgfmt=rs:316x265/rscb1/ng:webp/ngcb1)

Après cela, vous aurez votre projet créé avec une structure de répertoires et un ensemble de configurations et de fichiers de code. Il sera principalement en formats TypeScript et JSON. Voyons le rôle de chaque fichier :

* `/e2e/` : contient les tests end-to-end (simulant le comportement de l'utilisateur) du site web
* `/node_modules/` : Toutes les bibliothèques tierces sont installées dans ce dossier en utilisant `npm install`
* `/src/` : contient le code source de l'application. La plupart du travail sera fait ici
* `/app/` : contient les modules et composants
* `/assets/` : contient les actifs statiques comme les images, icônes et styles
* `/environments/` : contient les fichiers de configuration spécifiques à l'environnement (production et développement)
* `browserslist` : nécessaire pour autoprefixer pour la prise en charge CSS
* `favicon.ico` : la favicon
* `index.html` : le fichier HTML principal
* `karma.conf.js` : le fichier de configuration pour Karma (un outil de test)
* `main.ts` : le fichier de démarrage principal à partir duquel le _AppModule_ est bootstrappé
* `polyfills.ts` : les polyfills nécessaires par Angular
* `styles.css` : le fichier de feuille de style global pour le projet
* `test.ts` : il s'agit d'un fichier de configuration pour Karma
* `tsconfig.*.json` : les fichiers de configuration pour TypeScript
* `angular.json` : contient les configurations pour CLI
* `package.json` : contient les informations de base du projet (nom, description et dépendances)
* `README.md` : un fichier markdown qui contient une description du projet
* `tsconfig.json` : le fichier de configuration pour TypeScript
* `tslint.json` : le fichier de configuration pour TSlint (un outil d'analyse statique)

## Servir votre projet

Angular CLI fournit une chaîne d'outils complète pour développer des applications frontend sur votre machine locale. Ainsi, vous n'avez pas besoin d'installer un serveur local pour servir votre projet – vous pouvez simplement utiliser la commande `ng serve` depuis votre terminal pour servir votre projet localement.

Tout d'abord, naviguez dans le dossier de votre projet et exécutez les commandes suivantes :

```bash
$ cd frontend
$ ng serve


```

Vous pouvez maintenant naviguer vers l'adresse [http://localhost:4200/](http://localhost:4200/) pour commencer à utiliser votre application frontend. La page se rechargera automatiquement en direct si vous modifiez un fichier source.

## Génération d'artifacts Angular

Angular CLI fournit une commande `ng generate` qui aide les développeurs à générer des artifacts Angular de base tels que des modules, composants, directives, pipes et services :

```bash
$ ng generate component my-component

```

`my-component` est le nom du composant. Angular CLI ajoutera automatiquement une référence à `components`, `directives` et `pipes` dans le fichier `src/app.module.ts`.

Si vous souhaitez ajouter votre composant, directive ou pipe à un autre module (autre que le module principal de l'application, `app.module.ts`), vous pouvez simplement préfixer le nom du composant avec le nom du module et une barre oblique :

```bash
$ ng g component my-module/my-component

```

`my-module` est le nom d'un module existant.

## Conclusion

Dans ce tutoriel, nous avons vu comment installer Angular CLI sur notre machine Windows et nous l'avons utilisé pour initialiser un nouveau projet Angular à partir de zéro.

Nous avons également vu diverses commandes que vous pouvez utiliser tout au long du développement de votre projet pour générer des artifacts Angular tels que des modules, composants et services.

Consultez nos autres [tutoriels Angular](https://www.techiediaries.com/angular/).

Vous pouvez contacter ou suivre l'auteur via son [site web personnel](https://www.ahmedbouchefra.com/contact), [Twitter](https://twitter.com/ahmedbouchefra), [LinkedIn](https://www.linkedin.com/in/mr-ahmed/) et [Github](https://github.com/techiediaries).
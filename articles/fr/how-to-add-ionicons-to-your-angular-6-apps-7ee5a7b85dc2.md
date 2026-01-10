---
title: Comment ajouter Ionicons à vos applications Angular 6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-06T00:26:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-ionicons-to-your-angular-6-apps-7ee5a7b85dc2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*I_tQfo1PrAT_kum--QcNGw.jpeg
tags:
- name: Ionicons
  slug: ionicons
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment ajouter Ionicons à vos applications Angular 6
seo_desc: 'By Adedoja Adedamola

  I have had to work on a lot of Angular apps recently and Font Awesome has literally
  tired me out. So I decided to use Ionicons off the popular Ionic framework.

  This post shows how to set up Ionicons on your Angular project. We wi...'
---

Par Adedoja Adedamola

J'ai dû travailler sur beaucoup d'applications [**Angular**](https://angular.io/) récemment et Font Awesome m'a littéralement épuisé. J'ai donc décidé d'utiliser [**Ionicons**](http://ionicons.com/) du populaire framework Ionic.

Cet article montre comment installer [**Ionicons**](http://ionicons.com/) sur votre projet Angular. Nous allons suivre les étapes suivantes :

* Installer Angular CLI v6
* Créer une nouvelle application Angular v6
* Installer Ionicons
* Configurer Ionicons pour une utilisation sur votre application Angular v6

#### Installer Angular CLI v6

C'est assez simple — vous installez simplement la dernière version d'Angular via npm.

```
npm install -g @angular/cli@latest
```

Une fois cela fait, vous exécutez `ng --version` pour vérifier la version d'Angular que vous avez installée. Assurez-vous qu'il s'agit de la version Angular CLI 6.0.0 ou supérieure, comme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*se1AfRueItoiUcswhitMEg.png)
_Vérification de la version d'Angular avec ng — version_

#### Créer une nouvelle application Angular v6

À ce stade, vous avez installé Angular CLI globalement sur votre PC. Vous pouvez maintenant créer une nouvelle application Angular. Nous utilisons la commande `ng new nom-de-mon-application-incroyable`, qui nous permet de créer une application Angular.

```
ng new my-ionicons-angular-app --style=scss
```

Le bit SCSS est là pour nous permettre d'utiliser SCSS. Cela prend un peu de temps. Une fois terminé, nous naviguons vers l'application nouvellement créée.

```
cd my-ionicons-angular-app
```

Dès que nous sommes dans le répertoire du projet, nous pouvons démarrer le serveur de développement.

```
ng serve
```

Cela retourne ce qui suit :

```
** Angular Live Development Server écoute sur localhost:4200, ouvrez votre navigateur sur http://localhost:4200/ **
```

L'exécution de l'URL [http://localhost:4200/](http://localhost:4200/) vous montre votre toute nouvelle application. Si vous voyez l'écran ci-dessous, vous êtes prêt à partir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bNZu4fH_Yc3vevGy_SoZ0Q.png)
_Page d'accueil par défaut d'Angular_

#### Installer Ionicons

Comme nous l'avons fait précédemment, nous utilisons npm pour installer Ionicons.

```
npm install ionicons
```

#### Configurer Ionicons pour une utilisation sur votre application Angular v6

Dès qu'il est installé, nous devons indiquer à Angular où et comment le charger. La meilleure façon de le faire est dans notre fichier styles.scss et vous faites cela en ajoutant les lignes suivantes :

```
$ionicons-font-path: "~ionicons/dist/fonts";@import "~ionicons/dist/scss/ionicons.scss";
```

Il devrait être configuré correctement à ce stade. Vous pouvez modifier votre fichier de page d'accueil — app.component.html et utiliser l'icône de police pour ajouter une nouvelle icône comme ceci : `<i class="icon ion-md-heart"></i>`. Vous pouvez également [**consulter**](https://ionicons.com/) la page Ionicons pour une liste des icônes disponibles. Ci-dessous, vous pouvez voir à quoi ressemble ma page d'accueil ainsi que mon fichier app.component.html.

![Image](https://cdn-media-1.freecodecamp.org/images/1*STno4LND04VK8Ft1DLDClw.png)
_Page d'accueil Angular 6 avec un Ionicon_

#### C'est tout !!

Assez facile. J'espère que vous avez réussi jusqu'à la fin. Si vous avez des questions ou si vous voyez quelque chose qui ne va pas ou qui peut être fait mieux, n'hésitez pas à laisser un commentaire ci-dessous ou vous pouvez me contacter sur Twitter [**@TrussDamola**](https://twitter.com/TrussDamola).

Santé !
---
title: Angular 9 pour débutants — Comment installer votre première application avec
  Angular CLI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-22T17:44:59.000Z'
originalURL: https://freecodecamp.org/news/angular-9-for-beginners-how-to-install-your-first-app-with-angular-cli
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Copy-of-Copy-of-Travel-Photography.png
tags:
- name: Angular
  slug: angular
- name: Angular 9
  slug: angular-9
seo_title: Angular 9 pour débutants — Comment installer votre première application
  avec Angular CLI
seo_desc: 'By Cem Eygi

  Angular is one of the most popular JavaScript frameworks created and developed by
  Google. In the last couple of years, ReactJS has gained a lot of interest and has
  become the most popular modern JS library in the industry. But this doesn’...'
---

Par Cem Eygi

Angular est l'un des frameworks JavaScript les plus populaires, créé et développé par Google. Au cours des dernières années, ReactJS a suscité beaucoup d'intérêt et est devenu la bibliothèque JS moderne la plus populaire dans l'industrie. Mais cela ne signifie pas qu'Angular n'est plus important.

Au contraire, Angular est le deuxième framework le plus populaire après React selon Google Trends (dans le monde) :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Ekran-Resmi-2020-04-22-19.31.13.png)
_**ReactJS** est représenté en bleu et **Angular** en rouge (dans le monde)_

En tant que développeur front-end, j'ai travaillé avec Angular. Maintenant, je souhaite aborder certaines fonctionnalités importantes d'Angular dans mes prochains articles :

* **Partie 1 :** Comment installer votre première application avec Angular CLI **(vous êtes actuellement ici)**
* **Partie 2 :** [Composants Angular et interpolation de chaînes](https://www.freecodecamp.org/news/angular-9-for-beginners-components-and-string-interpolation/)
* **Partie 3 :** [Directives et Pipes Angular](https://youtu.be/3-eJ-A9rFEU)
* **Partie 4 :** [Liaison de données unidirectionnelle dans Angular](https://youtu.be/x_vtX3vvE8k)
* **Partie 5 :** [Liaison de données bidirectionnelle dans Angular avec ngModel](https://youtu.be/bKfbzpANUFE)

Dans la première partie de ma série Angular pour débutants, vous allez apprendre ce qu'est Angular et Angular CLI, et comment installer votre première application Angular en utilisant le CLI.

### Prérequis

Avant de commencer à apprendre Angular, je vous recommande de vous familiariser avec les langages suivants si ce n'est pas déjà fait :

* HTML, CSS
* JavaScript / ES6
* TypeScript

**Si vous préférez, vous pouvez regarder la vidéo tutorielle ci-dessous :**

%[https://youtu.be/cpq7cmj9Ih8]

## Qu'est-ce qu'Angular ?

Angular est un framework JavaScript développé et maintenu par Google pour construire des applications front-end. Commençons d'abord par expliquer ce qu'est un framework...

### Qu'est-ce qu'un Framework ?

Un Framework est un package complet avec ses propres fonctionnalités et bibliothèques. Un Framework a ses propres règles, vous n'avez pas beaucoup de flexibilité et le projet est dépendant du Framework que vous utilisez. Angular est un exemple de framework.

Angular a été publié en 2016, mais avant Angular, il y avait AngularJS. L'une des questions les plus posées sur Angular est de savoir quelle est la différence entre AngularJS et Angular ?

## AngularJS vs Angular

Ces 2 versions d'Angular confondent de nombreux développeurs. AngularJS et Angular sont des frameworks complètement différents. Les versions d'Angular (comme 1, 1.2, 1.5, etc.) sont appelées AngularJS et à partir de la version 2 et au-dessus, c'est appelé Angular.

* AngularJS → versions de 1.x
* Angular → version 2 et au-dessus

Ainsi, la version 2 d'Angular est une réécriture complète du framework AngularJS et les versions plus récentes (comme 4, 5, 6 et ainsi de suite) sont des modifications mineures de la version 2 d'Angular.

**Dans cette série d'articles, vous allez apprendre Angular 2+.**

# Qu'est-ce qu'Angular CLI ?

CLI signifie Command Line Interface. Angular a son propre CLI officiel qui nous aide avec beaucoup de choses pendant le processus de développement.

[Angular CLI](https://cli.angular.io/) est utilisé pour automatiser les opérations dans les projets Angular plutôt que de les faire manuellement. Le CLI nous soutient, nous les développeurs, dans un projet Angular du début à la fin.

Par exemple, Angular CLI peut être utilisé pour :

* Configurations, mise en place de l'environnement
* Construction de composants, services, système de routage
* Démarrage, test et déploiement du projet
* Installation de bibliothèques tierces (comme Bootstrap, Sass, etc.)

et bien plus encore. Maintenant, voyons comment installer notre première application Angular en utilisant le CLI étape par étape.

## Étape 1 : Installer NPM (Node Package Manager)

Tout d'abord, nous allons avoir besoin de Node.js. NPM (node package manager, fait partie de Node.js) est un outil pour installer des bibliothèques tierces et des dépendances à notre projet. Si vous ne l'avez pas encore, vous pouvez le télécharger et l'installer [ici](https://nodejs.org/en/). Je l'ai également expliqué étape par étape dans la vidéo tutorielle.

## **Étape 2 : Installer Angular CLI**

Si vous avez Node.js installé, l'étape suivante est d'installer Angular CLI lui-même sur votre ordinateur :

```javascript
npm install -g @angular/cli
```

**g** signifie **installation globale**. Si vous utilisez -g, vous pourrez utiliser le CLI dans n'importe quel projet Angular sur votre ordinateur.

**Astuce :** Tapez `ng v` dans votre interface de ligne de commande (ou terminal) pour vérifier votre version d'Angular.

## Étape 3 : Créer un nouveau projet Angular

Après l'installation, vous pouvez utiliser Angular CLI pour créer un nouveau projet Angular avec la commande suivante :

```javascript
ng new my-first-app
```

Cette commande crée un nouveau projet Angular (nommé my-first-app, vous pouvez utiliser n'importe quel nom) avec toutes les dépendances et fichiers nécessaires. Vous n'avez pas à vous soucier de quoi que ce soit car le CLI le fait automatiquement pour vous.

## Étape 4 : Exécuter l'application

Après avoir installé le CLI et créé une nouvelle application Angular, la dernière étape consiste à démarrer le projet. Pour ce faire, nous devons utiliser la commande suivante :

```javascript
ng serve --open
```

Le drapeau « open » ouvre automatiquement votre fenêtre de navigateur local.

Angular supporte le **live server**, donc vous pouvez voir les changements dans votre environnement local sans rafraîchir la page de votre navigateur. Pour plus de détails et de mises à jour, consultez également la [documentation officielle](https://angular.io/cli).

### Conclusion

Dans cette première partie, nous avons fait une introduction à Angular, à ce qu'est le CLI et à comment installer votre première application Angular. Dans le deuxième article, vous allez apprendre les [Composants Angular et l'interpolation de chaînes](https://www.freecodecamp.org/news/angular-9-for-beginners-components-and-string-interpolation/). Restez à l'écoute :)

**Si vous souhaitez en savoir plus sur le développement web, n'hésitez pas à** [**me suivre sur YouTube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)** !**

Merci d'avoir lu !
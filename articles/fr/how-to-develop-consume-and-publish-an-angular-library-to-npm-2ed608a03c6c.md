---
title: Comment développer, utiliser et publier une bibliothèque Angular sur NPM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-20T17:24:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-consume-and-publish-an-angular-library-to-npm-2ed608a03c6c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QBJcjunNHVVV_SDi-xSspQ.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment développer, utiliser et publier une bibliothèque Angular sur NPM
seo_desc: 'By Omer Kalim Ansari

  Angular is a really popular and powerful JavaScript Framework on which one can built
  Web Apps to serve millions of daily users. It’s an open source framework by Google
  and anyone can collaborate. Likewise, there are thousands of ...'
---

Par Omer Kalim Ansari

Angular est un Framework JavaScript vraiment populaire et puissant sur lequel on peut construire des applications Web pour servir des millions d'utilisateurs quotidiens. C'est un framework open source de Google et tout le monde peut collaborer. De même, il existe des milliers de packages pour Angular disponibles en plug-and-play sur [NPM](https://www.npmjs.com/). Ici, dans cet article, nous allons en créer un aussi ?.

Nous allons commencer cet article comme un tutoriel pour développer une **Bibliothèque de Composants Angular**, l'utiliser dans un projet Angular CLI, et ensuite nous...

## Sommaire

- [Prérequis](#heading-prerequisites)
- [Installation](#heading-installation)
- [Création de la bibliothèque](#heading-creating-the-library)
- [Développement du composant](#heading-developing-the-component)
- [Publication sur NPM](#heading-publishing-to-npm)

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Node.js (version 12 ou supérieure)
- Angular CLI (version 12 ou supérieure)
- Un compte NPM (pour publier la bibliothèque)

## Installation

Pour commencer, nous devons installer Angular CLI. Ouvrez votre terminal et exécutez la commande suivante :

```bash
npm install -g @angular/cli
```

Une fois l'installation terminée, vous pouvez vérifier la version installée en exécutant :

```bash
ng version
```

## Création de la bibliothèque

Pour créer une nouvelle bibliothèque Angular, exécutez la commande suivante :

```bash
ng generate library ma-bibliotheque
```

Cela va générer une nouvelle bibliothèque dans le dossier `projects/ma-bibliotheque`. Vous pouvez maintenant naviguer dans ce dossier pour commencer à développer votre bibliothèque.

## Développement du composant

Pour développer un nouveau composant dans votre bibliothèque, utilisez la commande suivante :

```bash
ng generate component mon-composant --project=ma-bibliotheque
```

Cela va générer un nouveau composant dans votre bibliothèque. Vous pouvez maintenant modifier les fichiers du composant pour ajouter votre logique et vos styles.

## Publication sur NPM

Pour publier votre bibliothèque sur NPM, vous devez d'abord vous connecter à votre compte NPM. Exécutez la commande suivante et suivez les instructions :

```bash
npm login
```

Une fois connecté, naviguez dans le dossier de votre bibliothèque et exécutez la commande suivante pour publier votre bibliothèque :

```bash
npm publish
```

Félicitations ! Vous avez maintenant publié votre bibliothèque Angular sur NPM. Les autres développeurs peuvent maintenant l'installer et l'utiliser dans leurs projets Angular.

## Conclusion

Dans cet article, nous avons appris comment développer, utiliser et publier une bibliothèque Angular sur NPM. Nous avons couvert les étapes de base pour créer une bibliothèque, développer un composant et le publier sur NPM. J'espère que cet article vous a été utile et que vous êtes maintenant prêt à créer vos propres bibliothèques Angular !

💡 **Conseil** : Assurez-vous de bien tester votre bibliothèque avant de la publier sur NPM. Vous pouvez utiliser des outils comme Jest ou Karma pour écrire et exécuter des tests unitaires.

✨ **Bonus** : Si vous voulez aller plus loin, vous pouvez explorer des sujets avancés comme la configuration de votre bibliothèque pour prendre en charge plusieurs thèmes ou la localisation.

Si vous avez des questions ou des commentaires, n'hésitez pas à les laisser ci-dessous. Bon développement ! 🚀
---
title: Angular 9 pour Débutants - Composants et Interpolation de Chaînes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-29T22:23:33.000Z'
originalURL: https://freecodecamp.org/news/angular-9-for-beginners-components-and-string-interpolation
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Copy-of-Copy-of-Travel-Photography-1.png
tags:
- name: Angular
  slug: angular
- name: Angular 9
  slug: angular-9
seo_title: Angular 9 pour Débutants - Composants et Interpolation de Chaînes
seo_desc: 'By Cem Eygi

  In modern web development, many developers prefer to build the UI of a website in
  a component-based way. It''s also supported by all modern frameworks. Understanding
  how components work and how to use them is a big step in learning Angular...'
---

Par Cem Eygi

Dans le développement web moderne, de nombreux développeurs préfèrent construire l'interface utilisateur d'un site web de manière basée sur les composants. Cela est également soutenu par tous les frameworks modernes. Comprendre comment fonctionnent les composants et comment les utiliser est une grande étape dans l'apprentissage d'Angular.

Dans cet article, vous allez apprendre les composants Angular, comment créer et utiliser un composant dans un projet, et ce qu'est l'interpolation de chaînes. Je couvrirai également d'autres fonctionnalités importantes d'Angular dans mes prochains articles :

* **Partie 1 :** [Comment installer votre première application avec Angular CLI](https://www.freecodecamp.org/news/angular-9-for-beginners-how-to-install-your-first-app-with-angular-cli/)
* **Partie 2 :** Composants Angular et Interpolation de Chaînes **(vous êtes ici)**
* **Partie 3 :** [Directives et Pipes Angular](https://youtu.be/3-eJ-A9rFEU)
* **Partie 4 :** [Liaison de Données Unidirectionnelle dans Angular](https://youtu.be/x_vtX3vvE8k)
* **Partie 5 :** [Liaison de Données Bidirectionnelle dans Angular avec ngModel](https://youtu.be/bKfbzpANUFE)

**Si vous préférez, vous pouvez également regarder la version vidéo :**

%[https://youtu.be/wXmw0FxjmTc]

## Qu'est-ce qu'un Composant ?

Les composants sont les blocs de construction les plus basiques d'une application Angular. Nous pouvons penser aux composants comme à des pièces LEGO. Nous créons un composant une fois mais pouvons les utiliser plusieurs fois selon nos besoins dans différentes parties du projet.

Un composant Angular est composé de 3 parties principales :

* Modèle HTML – Vue
* Fichier TypeScript – Modèle
* Fichier CSS – Style

### Pourquoi avons-nous besoin de Composants ?

L'utilisation de composants est bénéfique à bien des égards. Les composants divisent l'interface utilisateur en vues plus petites et rendent les données. Un composant ne doit pas être impliqué dans des tâches comme les requêtes HTTP, les opérations de service, le routage, etc. Cette approche maintient le code propre et sépare la vue des autres parties (voir [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns)).

Une autre raison importante est que les composants divisent le code en morceaux plus petits et réutilisables. Sinon, nous devrions inclure des lignes de code interminables dans un seul fichier HTML, ce qui rend le code beaucoup plus difficile à maintenir.

## Création de Notre Premier Composant Angular

Maintenant, créons notre premier composant. La manière rapide de créer un composant est d'utiliser Angular CLI :

```
ng g c nom-du-composant
```

Cette commande crée un tout nouveau composant avec ses propres fichiers (HTML, CSS et TypeScript) et l'enregistre automatiquement dans le Module de l'Application :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Ekran-Resmi-2020-04-29-10.59.14.png)
_Le Module de l'Application_

> **Note :** Dans Angular, nous devons enregistrer chaque service, composant et module nécessaire dans un fichier de module.

Maintenant, examinons de plus près le modèle de composant (Fichier de Composant TypeScript) :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Ekran-Resmi-2020-04-29-10.57.59.png)
_À l'intérieur du Composant de l'Application_

Il s'agit en fait d'une classe TypeScript, mais pour la définir comme un composant :

* Tout d'abord, nous devons importer **Component** de la bibliothèque **@angular/core**, afin de pouvoir utiliser le décorateur de composant.
* Le décorateur **@Component** marque la classe comme un composant et nous permet d'ajouter les métadonnées suivantes.
* Le **sélecteur** est utilisé pour appeler le composant plus tard sous forme de balise HTML : `<app-root> </app-root>`.
* **TemplateUrl** est le chemin où se trouve la Vue HTML du composant.
* **StyleUrls** (peut y en avoir plus d'un) est l'endroit où se trouvent les fichiers de style du composant.
* Enfin, nous **exportons** la classe (composant) afin de pouvoir l'appeler à l'intérieur du **app.module** ou d'autres endroits dans le projet plus tard.

### Qu'est-ce que l'Interpolation de Chaînes ?

L'une des questions les plus courantes que les gens posent sur Angular est de savoir ce que signifie cette syntaxe avec des accolades. Les composants rendent les données, mais les données peuvent changer avec le temps, elles doivent donc être dynamiques.

Nous utilisons des accolades à l'intérieur d'autres accolades pour rendre les données dynamiques : `{{ data }}` et cette représentation est appelée interpolation de chaînes. Vous pouvez voir l'exemple dans la version vidéo ci-dessus.

## Conclusion

L'une des plus grandes étapes de l'apprentissage d'Angular est de savoir comment créer des composants et les utiliser efficacement. J'espère que vous trouverez cet article utile. Dans la prochaine partie, nous allons examiner les directives Angular comme ng-if, ng-for, ng-class, et plus encore. Restez à l'écoute :)

**Si vous voulez en savoir plus sur le développement web, n'hésitez pas à** [**me suivre sur YouTube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)** !**

Merci d'avoir lu !
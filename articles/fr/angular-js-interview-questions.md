---
title: Questions d'entretien sur AngularJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T20:49:00.000Z'
originalURL: https://freecodecamp.org/news/angular-js-interview-questions
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9df9740569d1a4ca3aa8.jpg
tags:
- name: Angular
  slug: angularjs
- name: interview questions
  slug: interview-questions
- name: toothbrush
  slug: toothbrush
seo_title: Questions d'entretien sur AngularJS
seo_desc: 'Here’s a list of the concepts that are frequently asked about in AngularJS
  interviews.


  What is AngularJS?

  What is the Model View Controller (MVC)?

  Two way data binding

  What is dependency injection and how does it work?

  What is $scope in AngularJS?

  W...'
---

Voici une liste des concepts fréquemment abordés lors des entretiens sur AngularJS.

* Qu'est-ce qu'AngularJS ?
* Qu'est-ce que le Modèle Vue Contrôleur (MVC) ?
* Liaison de données bidirectionnelle
* Qu'est-ce que l'injection de dépendances et comment fonctionne-t-elle ?
* Qu'est-ce que $scope dans AngularJS ?
* Qu'est-ce que $rootScope dans AngularJS ?
* Comment implémenter le routage dans Angular ?
* Expliquer les directives
* Comment créer une directive personnalisée dans Angular ?
* Expliquer la différence entre service et factory
* Expliquer le service $q, deferred et les promesses

# **Exemples de questions et réponses**

### Question : Lister les directives dans AngularJS ? 

Réponse : ngBind, ngModel, ngClass, ngApp, ngInit, ngRepeat

### Question : Qu'est-ce que $scope dans AngularJS ? 

Réponse : $scope dans AngularJS est un objet qui fait référence à un modèle d'application. C'est un objet qui lie la vue (élément DOM) avec le contrôleur. Dans le contrôleur, les données du modèle sont accessibles via l'objet $scope. Comme nous le savons, AngularJS supporte le modèle MV*, l'objet $scope devient le modèle de MV*.

### Question : Qu'est-ce qu'une SPA (Single Page Application) dans AngularJS ? 

Réponse : Les applications monopages (SPA) sont des applications web qui chargent une seule page HTML et mettent à jour dynamiquement cette page à mesure que l'utilisateur interagit avec l'application. 

Les SPA utilisent AJAX et HTML pour créer des applications web fluides et réactives, sans rechargement constant de la page. Cependant, cela signifie que la plupart du travail se fait côté client, en JavaScript. 

Une seule page HTML ici signifie la page de réponse de l'interface utilisateur provenant du serveur. La source peut être ASP, ASP.NET, ASP.NET MVC, JSP, etc. 

Une application web monopage, cependant, est livrée comme une seule page au navigateur et ne nécessite généralement pas que la page soit rechargée lorsque l'utilisateur navigue vers différentes parties de l'application. Cela entraîne une navigation plus rapide, des transferts réseau plus efficaces et de meilleures performances globales pour l'utilisateur final.

### Question : Qu'est-ce que le routage dans AngularJS ? 

Réponse : Le routage est une fonctionnalité centrale dans AngularJS. Cette fonctionnalité est utile pour construire des SPA (Single Page Applications) avec plusieurs vues. Dans les SPA, toutes les vues sont des fichiers HTML différents et nous utilisons le routage pour charger différentes parties de l'application. C'est utile pour diviser l'application de manière logique et la rendre gérable. En d'autres termes, le routage nous aide à diviser notre application en vues logiques et à les lier avec différents contrôleurs.

### Question : Expliquer la directive ng-repeat. 

Réponse : La directive ng-repeat est la fonctionnalité de directive AngularJS la plus utilisée. Elle itère sur une collection d'éléments et crée des éléments DOM. Elle surveille constamment la source de données pour réafficher un modèle en réponse à un changement.

### Question : Quelle est la différence entre ng-If et ng-show/ng-hide. 

Réponse : La directive ng-If ne rend l'élément DOM que si la condition est vraie. Alors que les directives ng-show/ng-hide rendent l'élément DOM mais changent la classe de ng-hide/ng-show pour maintenir la visibilité de l'élément sur la page.

### Question : Comment annuler un timeout avec AngularJS ? 

Réponse : $timeout est l'enveloppe d'AngularJS pour window.setTimeout, vous annulez un timeout en appliquant la fonction :

```text
$timeout.cancel(function (){
  // écrivez votre code.
});
```

### Question : Qu'est-ce que l'injection de dépendances ? 

Réponse : L'injection de dépendances (DI) est un modèle de conception logicielle qui traite de la manière dont les composants obtiennent leurs dépendances. 

Le sous-système d'injection d'AngularJS est responsable de la création des composants, de la résolution de leurs dépendances et de leur fourniture à d'autres composants sur demande.

### Question : Expliquer la directive ng-App. 

Réponse : La directive ng-app démarre une application AngularJS. Elle définit l'élément racine. Elle initialise ou démarre automatiquement l'application lorsque la page web contenant l'application AngularJS est chargée. Elle est également utilisée pour charger divers modules AngularJS dans les applications AngularJS.

### Question : Expliquer la directive ng-init 

Réponse : La directive ng-init initialise les données d'une application AngularJS. Elle est utilisée pour attribuer des valeurs aux variables à utiliser dans l'application. 

Par exemple, dans le code ci-dessous, nous avons initialisé un tableau de pays en utilisant la syntaxe JSON pour définir le tableau de pays.

```html
<div ng-app = "" ng-init = "countries = [{locale:'en-US',name:'United States'}, {locale:'en-GB',name:'United Kingdom'}, {locale:'en-FR',name:'France'}]">
   ...
</div>
```

### Question : Comment partager des données entre les contrôleurs ? 

Réponse : Créez un service AngularJS qui contiendra les données et injectez-le dans les contrôleurs. Utiliser un service est la méthode la plus propre, la plus rapide et la plus facile à tester. 

Cependant, il existe quelques autres façons de mettre en œuvre le partage de données entre les contrôleurs, comme :

* Utiliser des événements
* Utiliser $parent, nextSibling, controllerAs, etc. pour accéder directement aux contrôleurs
* Utiliser le $rootScope pour ajouter les données (ce n'est pas une bonne pratique)

### Question : Quelle est la différence entre les directives ng-if et ng-show/hide ? 

Réponse : ng-if ne créera et n'affichera l'élément DOM que lorsque sa condition est vraie. Si la condition est fausse ou devient fausse, il ne créera pas ou ne détruira pas l'élément créé. 

ng-show/hide générera toujours l'élément DOM mais appliquera la propriété CSS display en fonction de l'évaluation de la condition.

## Plus d'informations sur AngularJS :

* [Angular vs AngularJS](https://www.freecodecamp.org/news/angular-vs-angularjs/)
* [Les meilleurs tutoriels Angular et AngularJS](https://www.freecodecamp.org/news/best-angular-tutorial-angularjs/)
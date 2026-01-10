---
title: Comment convertir une application AngularJS 1.x en une application React —
  un composant à la fois.
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2018-01-24T18:57:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-an-angular-app-to-a-react-app-one-component-at-a-time-ba985eaae66e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yq7TPrTheULIcxwfTD96SA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment convertir une application AngularJS 1.x en une application React
  — un composant à la fois.
seo_desc: Angular and React are both great frameworks/libraries. Angular provides
  a defined structure of MVC (Model, View, Controller). React provides a lightweight
  rendering mechanism based on state change. Often times, developers will have an
  application wit...
---

Angular et React sont tous deux d'excellents frameworks/bibliothèques. Angular fournit une structure définie de MVC (Modèle, Vue, Contrôleur). React fournit un mécanisme de rendu léger basé sur le changement d'état. Souvent, les développeurs auront une application avec du code hérité en AngularJS, mais ils voudront construire de nouvelles fonctionnalités en ReactJS.

Bien qu'il soit possible de mettre à la retraite une application AngularJS et de construire une application ReactJS à partir de zéro, ce n'est pas une solution viable pour les applications à grande échelle. Dans de telles situations, il est plus facile de construire un composant React en isolation et de l'importer dans Angular.

Dans cet article, je vais vous aider à créer un composant React dans une application Angular en utilisant `react2angular`.

### Planifier l'application

Voici ce que nous allons faire —

**Donné** : Une application Angular qui affiche le nom d'une ville et ses principaux sites.

**Objectif** : Ajouter un composant React à l'application Angular. Le composant React affichera une image en vedette d'un site.

**Plan** : Nous allons créer un composant React, passer `imageUrl` via `props`, et afficher l'image en tant que composant React.

Commençons !

### Étape 0 : Avoir une application Angular

Pour les besoins de cet article, gardons la complexité de l'application Angular simple. Je planifie un voyage en Europe en 2018, donc mon application Angular est essentiellement une liste de lieux que je souhaite visiter.

Voici à quoi ressemble notre ensemble de données `bucketlist` :

```js
const bucketlist = [{
  city: 'Venise',
  position: 3,
  sites: ['Grand Canal', 'Pont des Soupirs', 'Piazza San Marco'],
  img: 'https://unsplash.com/photos/ryC3SVUeRgY',
}, {
  city: 'Paris',
  position: 2,
  sites: ['Tour Eiffel', 'Le Louvre', 'Notre-Dame de Paris'],
  img: 'https://unsplash.com/photos/R5scocnOOdM',
}, {
  city: 'Santorin',
  position: 1,
  sites: ['Imerovigli', 'Akrotiri', 'Santorini Arts Factory'],
  img: 'https://unsplash.com/photos/hmXtDtmM5r0',
}];
```

Voici à quoi ressemble `angularComponent.js` :

```js
function AngularComponentCtrl() {
  var ctrl = this;
  ctrl.bucketlist = bucketlist; 
};

angular.module('demoApp').component('angularComponent', {
  templateUrl: 'angularComponent.html',
  controller: AngularComponentCtrl
});
```

et voici `angularComponent.html` :

```html
<div ng-repeat="item in $ctrl.bucketlist" ng-sort="item.position">
  <h2>{{item.city}}</h2>
  <p> Je veux voir <span ng-repeat="sight in item.sights">{{sight}}                 </p></span>
</div>
```

Super simple ! Je pourrais aller à Santorin tout de suite...

![Image](https://cdn-media-1.freecodecamp.org/images/p83cdbYPyyvGn1IrTNnzC-XDpcWuSm7-1VBu)
_Ce moment où vous revenez de vacances et ne pouvez pas attendre les prochaines vacances. Photo par [Unsplash](https://unsplash.com/photos/aapSemzfsOk?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Alexandre Chambon</a> sur <a href="https://unsplash.com/search/photos/santorini?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Étape 1 : Installer les dépendances

Passer du monde Angular à celui de React peut être un vrai casse-tête si votre éditeur n'est pas configuré. Commençons par là. Nous allons d'abord installer la vérification de linting.

```bash
npm install --save eslint babel-eslint
```

Ensuite, installons `react2angular`. Si vous n'avez jamais installé React, vous devrez également installer `react`, `react-dom` et `prop-types`.

```bash
npm install --save react2angular react react-dom prop-types
```

### Étape 2 : Créer un composant React

Maintenant, nous avons déjà un composant Angular qui affiche le nom d'une ville. Ensuite, nous devons afficher l'image en vedette. Supposons pour l'instant que l'image est disponible pour nous via `props` (et nous verrons comment `props` fonctionne dans une minute). Notre composant React ressemble à ceci :

```js
import {Component} from 'react';

class RenderImage extends Component {

  render() {
    const imageUrl = this.props.imageUrl;
    return (
      <div>
        <img src={imageUrl} alt=""/>
      </div>
      );
  }
}
```

### Étape 3 : Passer les props

Rappelez-vous dans l'**Étape 2**, nous avons supposé avoir une image disponible via `props`. Nous allons maintenant remplir `props`. Vous pouvez passer des dépendances à un composant React en utilisant `props`. Gardez à l'esprit que aucune de vos dépendances Angular n'est disponible pour le composant React. Pensez-y de cette manière — le composant React est comme un conteneur connecté à l'application Angular. Si vous avez besoin que le conteneur hérite d'informations du parent, vous devrez le connecter explicitement via `props`.

Ainsi, pour passer des dépendances, nous allons ajouter un composant `renderImage` dans Angular et passer `imageUrl` en tant que paramètre :

```js
 angular.module('demoApp', [])
.component('renderImage', react2angular(RenderImage,['imageUrl']));
```

### Étape 4 : Inclure dans le modèle Angular

Maintenant, vous pouvez simplement importer ce composant dans l'application Angular comme n'importe quel autre composant :

```html
<div ng-repeat="item in $ctrl.bucketlist">
  <h2>{{item.city}}</h2>
  <p> Je veux voir <span ng-repeat="site in item.sites">{{site}}</span>
  <render-image image-url={{item.img}}></render-image>
</div>
```

Ta Da ! C'est magique ! Pas vraiment. C'est du travail acharné et de la sueur. Et du café. Beaucoup de café.

![Image](https://cdn-media-1.freecodecamp.org/images/-L8XanmrOrxeb9YzUIjafJ21x2KRbuSbmaCy)
_Café Café Café. Photo par [Unsplash](https://unsplash.com/photos/02MLReRp3I8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Christiana Rivers</a> sur <a href="https://unsplash.com/search/photos/new-york?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> Maintenant, allez construire quelques composants React, vous brave guerrier !

Un remerciement spécial à [David Gee](https://twitter.com/dvdgee) pour m'avoir présenté `react2angular` et m'avoir aidé à voir la lumière au bout du tunnel lorsque j'étais plongé dans le monde Angular.

Ressources :

1. [Cet article](https://medium.com/@panagiotisvrs/angularjs-migration-to-react-redux-2d3bb3a7cc84) m'a beaucoup aidé.
2. [Documentation officielle de react2angular](https://github.com/coatue-oss/react2angular)

**Si cet article vous a aidé, veuillez cliquer sur le bouton ? pour qu'il atteigne d'autres développeurs.**
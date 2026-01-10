---
title: Angular Views, Routing, et NgModules Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T21:22:00.000Z'
originalURL: https://freecodecamp.org/news/angular-vs-angularjs
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e1f740569d1a4ca3b6e.jpg
tags:
- name: Angular
  slug: angular
- name: Angular
  slug: angularjs
seo_title: Angular Views, Routing, et NgModules Expliqués
seo_desc: "Angular vs AngularJS\nAngularJS (versions 1.x) is a JavaScript-based open\
  \ source framework. It is cross platform and is used to develop Single Page Web\
  \ Application (SPWA). \nAngularJS implements the MVC pattern to separate the logic,\
  \ presentation, and ..."
---

## Angular vs AngularJS

AngularJS (versions 1.x) est un framework open source basé sur JavaScript. Il est multiplateforme et est utilisé pour développer des applications web monopage (SPWA). 

AngularJS implémente le modèle MVC pour séparer la logique, la présentation et les composants de données. Il utilise également l'injection de dépendances pour utiliser les services côté serveur dans les applications côté client.

Angular (versions 2.x et supérieures) est un framework open source basé sur TypeScript utilisé pour développer des applications web front-end. Angular possède les fonctionnalités suivantes comme les génériques, le typage statique, le chargement dynamique, et également certaines fonctionnalités ES6.

## **Historique des versions**

Google a publié la version initiale d'AngularJS le 20 octobre 2010. La première version stable d'AngularJS était la version 1.6.8, publiée le 18 décembre 2017.

La version Angular 2.0 a été publiée le 22 septembre 2014 lors de la conférence ng-Europe.

Après quelques modifications, Angular 4.0 a été publié en décembre 2016. Angular 4 est rétrocompatible avec Angular 2.0. La bibliothèque HttpClient est l'une des nouvelles fonctionnalités d'Angular 4.0.

La version Angular 5 est sortie le 1er novembre 2017. Le support des applications web progressives (PWA) était l'une des améliorations apportées à Angular 4.0.

Et enfin, Angular 6 a été publié en mai 2018. La dernière version stable est [6.1.9](https://blog.angular.io/angular-v6-1-now-available-typescript-2-9-scroll-positioning-and-more-9f1c03007bb6)

## Comment l'installer

Nous pouvons ajouter Angular soit en référençant les sources disponibles, soit en téléchargeant le framework.

### Lien vers la source

AngularJS : Nous pouvons ajouter AngularJS (versions Angular 1.x) en référençant le Content Delivery Network de Google.

```html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js"></script> 
```

Télécharger/installer : Nous pouvons télécharger le framework avec npm, Bower ou composer

**Angular**JS **1.x** :

npm

```shell
npm install angular
```

Puis ajoutez un `<script>` à votre `index.html` :

```html
<script src="/node_modules/angular/angular.js"></script>
```

bower

```shell
bower install angular
```

Puis ajoutez un `<script>` à votre `index.html` :

```html
<script src="/bower_components/angular/angular.js"></script>
```

**Angular** :

Pour plus d'informations concernant la documentation, référez-vous au site officiel d'[AngularJS](https://docs.angularjs.org/api).

Vous pouvez installer **Angular 2.x** et d'autres versions en suivant les étapes de la documentation officielle d'[Angular](https://angular.io/guide/quickstart).

Maintenant, apprenons un peu plus sur Angular, d'accord ?

# **Introduction**

Les vues offrent une couche d'abstraction nécessaire. Elles gardent Angular indépendant des utilitaires spécifiques à la plateforme. En tant que technologie multiplateforme, Angular utilise ses vues pour se connecter à la plateforme.

Pour chaque élément dans le HTML de modèle d'Angular, il y a une vue correspondante. Angular recommande d'interagir avec les plateformes à travers ces vues. Bien que la manipulation directe soit toujours possible, Angular met en garde contre cela. Angular offre sa propre interface de programmation d'application (API) pour remplacer les manipulations natives.

Éviter les vues pour l'API spécifique à la plateforme a ses conséquences. Lors du développement d'Angular dans un navigateur web, les éléments existent en deux endroits : le DOM et la vue. Ne manipuler que le DOM n'a pas d'impact sur la vue.

Puisque Angular n'interface pas avec la plateforme, cela crée une discontinuité. Les vues doivent refléter la plateforme un à un. Sinon, Angular gaspille des ressources à gérer des éléments qui ne correspondent pas. Cela est terrible en cas de suppression d'éléments.

Ces types de divergences rendent les vues inutiles. N'oubliez jamais qu'Angular est avant tout une plateforme de développement universelle. Les vues sont une abstraction nécessaire à cette fin.

En adhérant aux vues, les applications Angular fonctionneront sur toutes les plateformes de développement prises en charge. Les plateformes incluent le Web, Android et Apple iOS.

#### **Note**

À partir de maintenant, cet article suppose un environnement de navigateur web. N'hésitez pas à remplacer mentalement le DOM par quelque chose de plus applicable à votre plateforme préférée.

## Qu'est-ce que les vues ?

Les vues sont presque comme leur propre DOM virtuel. Chaque vue contient une référence à une section correspondante du DOM. À l'intérieur d'une vue se trouvent des nœuds qui reflètent ce qui se trouve dans cette section. Angular attribue un nœud de vue par élément DOM. Chaque nœud contient une référence à un élément correspondant.

Lorsque Angular vérifie les changements, il vérifie les vues. Angular évite le DOM sous le capot. Les vues référencent le DOM en son nom. D'autres mécanismes sont en place pour garantir que les changements de vue se rendent dans le DOM. Inversement, les changements apportés au DOM n'affectent pas les vues.

Encore une fois, les vues sont communes à toutes les plateformes de développement en dehors du DOM. Même si vous développez pour une seule plateforme, les vues sont toujours considérées comme une meilleure pratique. Elles garantissent qu'Angular a une interprétation correcte du DOM.

Les vues peuvent ne pas exister sur les bibliothèques tierces. La manipulation directe du DOM est une issue pour ce type de scénario. Bien sûr, ne vous attendez pas à ce que l'application fonctionne sur plusieurs plateformes.

### Types de vues

Il existe deux principaux types de vues : intégrées et hôtes.

Il existe également des conteneurs de vues. Ils contiennent des vues intégrées et hôtes et sont souvent appelés simplement « vues ».

Chaque classe `@Component` enregistre un conteneur de vues (vue) avec Angular. Les nouveaux composants génèrent un sélecteur personnalisé ciblant un certain élément DOM. La vue s'attache à cet élément partout où il apparaît. Angular sait maintenant que le composant existe en regardant le modèle de vue.

Les vues hôtes s'attachent aux composants créés dynamiquement avec des factories. Les factories fournissent un plan pour l'instanciation des vues. Ainsi, l'application peut instancier la vue hôte du composant pendant l'exécution. Une vue hôte s'attache à un wrapper de composant selon son instanciation. Cette vue stocke des données décrivant les capacités conventionnelles du composant.

`<ng-template></ng-template>` est similaire à l'élément HTML5 `<template></template>`. Le `ng-template` d'Angular fonctionne avec des vues intégrées. Ces vues ne s'attachent pas aux éléments DOM contrairement aux vues hôtes. Elles sont identiques aux vues hôtes en ce sens que les deux types existent à l'intérieur des conteneurs de vues.

Gardez à l'esprit que `ng-template` n'est pas un élément DOM. Il est commenté plus tard, ne laissant rien derrière lui sauf les nœuds de vue intégrés.

La différence dépend des données d'entrée ; les vues intégrées ne stockent aucune donnée de composant. Elles stockent une série d'éléments en tant que nœuds comprenant son modèle. Le modèle constitue tout le innerHTML de `ng-template`. Chaque élément dans la vue intégrée est son propre nœud de vue séparé.

### Vues hôtes et conteneurs

Les vues hôtes _hébergent_ des composants dynamiques. Les conteneurs de vues (vues) s'attachent automatiquement aux éléments déjà dans le modèle. Les vues peuvent s'attacher à n'importe quel élément au-delà de ce qui est unique aux classes de composants.

Pensez à la méthode traditionnelle de génération de composants. Elle commence par créer une classe, la décorer avec `@Component`, et remplir les métadonnées. Cette approche se produit pour tout élément de composant prédéfini du modèle.

Essayez d'utiliser la commande de l'interface de ligne de commande (CLI) Angular : `ng generate component [nom-du-composant]`. Cela donne le résultat suivant.

```typescript
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})
export class ExampleComponent implements OnInit {
  constructor() { }

  ngOnInit() { }
}
```

Cela crée le composant avec le sélecteur `app-example`. Cela attache un conteneur de vue à `<app-example></app-example>` dans le modèle. Si cela était la racine de l'application, sa vue encapsulerait toutes les autres vues. La vue racine marque le début de l'application du point de vue d'Angular.

Créer des composants dynamiquement et les enregistrer dans le modèle de vue Angular nécessite quelques étapes supplémentaires. Les directives structurelles aident à gérer le contenu dynamique (`*ngIf, *ngFor, et *ngSwitch...`). Les directives ne s'adaptent pas aux applications plus grandes cependant. Trop de directives structurelles compliquent le modèle.

C'est là que l'instanciation de composants à partir de la logique de classe existante devient utile. Ces composants doivent créer une vue hôte qui peut s'insérer dans le modèle de vue. Les vues hôtes contiennent des données pour les composants afin qu'Angular reconnaisse leur but structurel.

### Suite des vues hôtes

Chaque composant a une définition de classe. Pourtant, JavaScript ne supporte pas les classes. Les classes sont du sucre syntaxique. Elles produisent des fonctions contenant des factories de composants à la place.

Les factories agissent comme des plans pour les vues hôtes. Elles construisent des vues pour interfacer avec Angular au nom de leurs composants. Les vues hôtes s'attachent aux éléments DOM. Techniquement, n'importe quel élément est acceptable, mais la cible la plus courante est `<ng-component></ng-component>`.

Un conteneur de vue (vue) pour contenir des vues doit d'abord exister. `<ng-container></ng-container>` est un excellent endroit pour attacher un conteneur de vue. Les conteneurs de vue sont du même type de vues qui s'appliquent également aux éléments de classe de modèle.

Quelques aides et références de `@angular/core` fournissent les autres utilitaires nécessaires. L'exemple suivant met tout cela ensemble.

```typescript
// another.component.ts

import { Component } from '@angular/core';

@Component({
  template: `
  <h1>Another Component Content</h1>
  <h3>Dynamically Generated!</h3>
  `
})
export class AnotherComponent { }
```

```typescript
// example.component.ts

import { AfterViewInit, Component, ViewChild,
ViewContainerRef, ComponentFactoryResolver } from '@angular/core';
import { AnotherComponent } from './another.component';

@Component({
  selector: 'app-example',
  template: `
  <h1>Application Content</h1>
  <ng-container #container></ng-container>
  <h3>End of Application</h3>
  `,
  entryComponents: [ AnotherComponent ]
})
export class ExampleComponent implements AfterViewInit {
  @ViewChild("container", { read: ViewContainerRef }) ctr: ViewContainerRef;

  constructor(private resolve: ComponentFactoryResolver) { }

  ngAfterViewInit() {
    const factory = this.resolve.resolveComponentFactory(AnotherComponent);
    this.ctr.createComponent(factory);
  }
}
```

Supposons que AnotherComponent et ExampleComponent sont tous deux déclarés sous le même module. AnotherComponent est une simple classe de composant ajoutée dynamiquement dans la vue de ExampleComponent. Les métadonnées `entryComponents` de ExampleComponent doivent contenir AnotherComponent pour le [bootstrapping](https://angular.io/guide/bootstrapping).

Alors que ExampleComponent fait partie du modèle, AnotherComponent reste détaché. Il se rend dynamiquement dans le modèle à partir de ExampleComponent.

Il y a deux conteneurs de vue présents : `<app-example></app-example>` et `<ng-container></ng-container>`. La vue hôte de cet exemple s'insérera dans `ng-container`.

Le hook de cycle de vie `AfterViewInit` se déclenche après que les requêtes `@ViewChild` soient terminées. En utilisant la _variable de référence de modèle_ `#container`, le `@ViewChild` référence `ng-container` en tant que `ctr`.

`ViewContainerRef` est le type de référence pour les conteneurs de vue (vues). `ViewContainerRef` référence une vue qui supporte l'insertion d'autres vues. `ViewContainerRef` contient plus de méthodes pour gérer ses vues contenues.

Grâce à l'injection de dépendances, le constructeur instancie une instance du service `ComponentFactoryResolver` d'Angular. Ce service extrait la fonction de factory (plan de vue hôte) de AnotherComponent.

Le seul argument de `createComponent` nécessite une factory. La fonction `createComponent` dérive de `ViewContainerRef`. Elle instancie AnotherComponent sous une vue hôte dérivée de la factory du composant.

La vue hôte s'insère ensuite dans le conteneur de vue. `<ng-component></ng-component>` enveloppe le composant à l'intérieur du conteneur de vue. Il a attaché à lui la vue hôte mentionnée précédemment. `ng-component` est la connexion de la vue hôte avec le DOM.

Il existe d'autres moyens de créer une vue hôte dynamiquement à partir d'un composant. D'autres moyens se concentrent souvent sur [l'optimisation](https://blog.angularindepth.com/working-with-dom-in-angular-unexpected-consequences-and-optimization-techniques-682ac09f6866).

Le `ViewContainerRef` contient une API puissante. Il peut gérer n'importe quel nombre de vues, qu'elles soient hôtes ou intégrées dans sa vue. L'API inclut des opérations de vue telles que l'insertion, le déplacement et la suppression. Cela vous permet de manipuler le DOM à travers le modèle de vue d'Angular. C'est la meilleure pratique pour que Angular et le DOM se correspondent.

### Vues intégrées

Note : les vues intégrées s'attachent à d'autres vues sans entrée ajoutée. Les vues hôtes s'attachent à un élément DOM avec des données d'entrée de sa vue hôte le décrivant comme un composant.

Les directives structurelles créent un [`ng-template` entourant un morceau de contenu HTML](https://angular.io/guide/structural-directives#the-asterisk--prefix). L'élément hôte de la directive a un conteneur de vue attaché. Cela permet au contenu de se rendre conditionnellement dans sa mise en page prévue.

Le `ng-template` contient des nœuds de vue intégrés représentant chaque élément dans son innerHTML. `ng-template` n'est en aucun cas un élément DOM. Il se commente lui-même. Les balises définissent l'étendue de sa vue intégrée.

### Suite des vues intégrées

L'instanciation d'une vue intégrée ne nécessite aucune ressource externe au-delà de sa propre référence. La requête `@ViewChild` peut la récupérer.

Avec la référence de modèle, l'appel de `createEmbeddedView` à partir de celle-ci fait l'affaire. Le innerHTML de la référence devient sa propre instance de vue intégrée.

Dans l'exemple suivant, `<ng-container></ng-container>` est un conteneur de vue. `ng-container` est commenté pendant la compilation tout comme `ng-template`. Ainsi, il fournit une sortie pour insérer la vue intégrée tout en gardant le DOM léger.

Le modèle de vue intégrée s'insère à l'emplacement de mise en page de `ng-container`. Cette vue nouvellement insérée n'a pas d'encapsulation de vue supplémentaire en dehors du conteneur de vue. Souvenez-vous de la différence avec les vues hôtes (les vues hôtes s'attachent à leur élément wrapper `ng-component`).

```typescript
import { Component, AfterViewInit, ViewChild,
ViewContainerRef, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-example',
  template: `
  <h1>Application Content</h1>
  <ng-container #container></ng-container> <!-- embed view here -->
  <h3>End of Application</h3>

  <ng-template #template>
    <h1>Template Content</h1>
    <h3>Dynamically Generated!</h3>
  </ng-template>
  `
})
export class ExampleComponent implements AfterViewInit {
  @ViewChild("template", { read: TemplateRef }) tpl: TemplateRef<any>;
  @ViewChild("container", { read: ViewContainerRef }) ctr: ViewContainerRef;

  constructor() { }

  ngAfterViewInit() {
    const view =  this.tpl.createEmbeddedView(null);
    this.ctr.insert(view);
  }
}
```

`@ViewChild` interroge la _variable de référence de modèle_ `#template`. Cela fournit une référence de modèle de type `TemplateRef`. `TemplateRef` contient la fonction `createEmbeddedView`. Elle instancie le modèle en tant que vue intégrée.

Le seul argument de `createEmbeddedView` est pour le contexte. Si vous souhaitez passer des métadonnées supplémentaires, vous pouvez le faire ici sous forme d'objet. Les champs doivent correspondre aux attributs `ng-template` (`let-[context-field-key-name]="value"`). Passer `null` indique qu'aucune métadonnée supplémentaire n'est nécessaire.

Une deuxième requête `@ViewChild` fournit une référence à `ng-container` en tant que `ViewContainerRef`. Les vues intégrées ne s'attachent qu'à d'autres vues, jamais au DOM. Le `ViewContainerRef` référence la vue qui prend la vue intégrée.

Une vue intégrée peut également s'insérer dans la vue du composant de `<app-example></app-example>`. Cette approche positionne la vue à la toute fin de la vue de ExampleComponent. Dans cet exemple cependant, nous voulons que le contenu apparaisse au milieu où se trouve `ng-container`.

La fonction `insert` de `ViewContainerRef` _insère_ la vue intégrée dans le `ng-container`. Le contenu de la vue apparaît à l'emplacement prévu, juste au milieu de la vue de ExampleComponent.

## Conclusion

Manipuler le DOM avec des méthodes spécifiques à la plateforme n'est pas recommandé. Créer et gérer un ensemble serré de vues maintient Angular et le DOM sur la même page. La mise à jour des vues informe Angular de l'état actuel du DOM. Les mises à jour des vues se répercutent également sur ce que le DOM affiche.

Angular fournit une API flexible pour l'interaction avec les vues. Le développement d'applications indépendantes de la plateforme est possible grâce à ce niveau d'abstraction. Bien sûr, la tentation de recourir à des stratégies dépendantes de la plateforme persiste. À moins d'avoir une très bonne raison de ne pas le faire, essayez de vous en tenir à l'API des vues fournie par Angular. Cela donnera des résultats prévisibles sur toutes les plateformes.

# **Routing dans Angular**

Le routage est essentiel. De nombreuses applications web modernes hébergent trop d'informations pour une seule page. Les utilisateurs ne devraient pas avoir à faire défiler tout le contenu d'une application. Une application doit se diviser en sections distinguables.

Les utilisateurs priorisent les informations nécessaires. Le routage les aide à trouver la section de l'application contenant ces informations. Toute autre information utile à d'autres utilisateurs peut exister sur une route entièrement séparée. Avec le routage, les deux utilisateurs peuvent trouver ce dont ils ont besoin rapidement. Les détails non pertinents restent obscurcis derrière des routes non pertinentes.

Le routage excelle dans le tri et la restriction de l'accès aux données de l'application. Les données sensibles ne doivent jamais être affichées aux utilisateurs non autorisés. Entre chaque route, l'application peut intervenir. Elle peut examiner la session de l'utilisateur à des fins d'authentification. Cet examen détermine ce que la route rend si elle doit rendre quoi que ce soit. Le routage donne aux développeurs la chance parfaite de vérifier un utilisateur avant de continuer.

Créer une liste de routes favorise également l'organisation. En termes de développement, cela maintient le développeur dans des sections distinguables. Les utilisateurs en bénéficient également, mais surtout les développeurs lors de la navigation dans le code de l'application. Une liste de routeurs programmatiques peint un modèle précis du front-end de l'application.

En ce qui concerne Angular, le routage occupe sa propre bibliothèque entière au sein du framework. Tous les frameworks front-end modernes supportent le routage, et Angular ne fait pas exception. Le routage se fait côté client en utilisant soit le routage par hachage, soit le routage par emplacement. Les deux styles permettent au client de gérer ses propres routes. Aucune assistance supplémentaire du serveur n'est nécessaire au-delà de la requête initiale.

Le navigateur web se rafraîchit rarement en utilisant le routage côté client. Les utilitaires du navigateur web tels que les favoris, l'historique et la barre d'adresse fonctionnent toujours malgré l'absence de rafraîchissement. Cela permet une expérience de routage fluide qui ne perturbe pas le navigateur. Plus de rechargements de page saccadés lors du routage vers une page différente.

Angular ajoute une couche d'abstraction sur les technologies de base utilisées pour le routage. Cet article vise à expliquer cette abstraction. Il existe deux stratégies de routage dans Angular : l'emplacement de chemin et le hachage. Cet article se concentre sur la stratégie d'emplacement de chemin, car c'est l'option par défaut.

De plus, l'emplacement de chemin peut déprécier le routage par hachage suite à la sortie complète d'[Angular Universal](https://universal.angular.io/). Quoi qu'il en soit, les deux stratégies sont très similaires dans leur implémentation. Apprendre l'une, c'est apprendre l'autre. Il est temps de commencer !

## Configuration du RouterModule

Les utilitaires de routage sont exportés avec `RouterModule` disponible depuis `@angular/router`. Il ne fait pas partie de la bibliothèque principale, car toutes les applications n'ont pas besoin de routage. La manière la plus conventionnelle d'introduire le routage est en tant que [module de fonctionnalité](https://angular.io/guide/feature-modules).

À mesure que la complexité des routes augmente, en avoir un module dédié favorisera la simplicité du module racine. Le garder simple sans compromettre la fonctionnalité constitue une bonne conception pour les modules.

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AComponent } from '../../components/a/a.component';
import { BComponent } from '../../components/b/b.component';

// un tableau de routes à venir !
const routes: Routes = [];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
```

`.forRoot(...)` est une fonction de classe disponible depuis la classe RouterModule. La fonction accepte un tableau d'objets `Route` en tant que `Routes`. `.forRoot(...)` configure les routes pour le chargement immédiat tandis que son alternative `.forChild(...)` configure pour le chargement paresseux.

Le chargement immédiat signifie que les routes chargent leur contenu dans l'application dès le départ. Le chargement paresseux se fait à la demande. L'accent de cet article est mis sur le chargement immédiat. C'est l'approche par défaut pour charger une application. La définition de la classe RouterModule ressemble à quelque chose comme le bloc de code suivant.

```typescript
@NgModule({
  // 20
6 lots de métadonnées ...
})
export class RouterModule {
  forRoot(routes: Routes) {
    // 20
6 configuration pour les routes chargées immédiatement 20
6
  }

  forChild(routes: Routes) {
    // 20
6 configuration pour les routes chargées paresseusement 20
6
  }
}
```

Ne vous inquiétez pas des détails de configuration que l'exemple omet avec des commentaires. Avoir une compréhension générale suffira pour l'instant.

Remarquez comment AppRoutingModule importe le RouterModule tout en l'exportant également. Cela a du sens étant donné qu'AppRoutingModule est un module de fonctionnalité. Il importe dans le module racine en tant que module de fonctionnalité. Il expose les directives, interfaces et services de RouterModule à l'arbre de composants racine.

Cela explique pourquoi AppRoutingModule doit exporter RouterModule. Il le fait pour le bien de l'arbre de composants sous-jacent du module racine. Il a besoin d'accéder à ces utilitaires de routage !

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AComponent } from './components/a/a.component';
import { BComponent } from './components/b/b.component';
import { AppRoutingModule } from './modules/app-routing/app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    AComponent,
    BComponent
  ],
  imports: [
    AppRoutingModule, // module de fonctionnalité de routage
    BrowserModule
  ],
  providers: [],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
```

Le jeton AppRoutingModule est importé depuis le tout début. Son jeton s'insère dans le tableau des imports du module racine. L'arbre de composants racine peut maintenant utiliser la bibliothèque RouterModule. Cela inclut ses directives, interfaces et services comme déjà mentionné. Un grand merci à AppRoutingModule pour l'exportation de RouterModule !

Les utilitaires RouterModule seront utiles pour les composants de la racine. Le HTML de base pour AppComponent utilise une directive : `router-outlet`.

```html
<!-- app.component.html -->

<ul>
  <!-- routerLink(s) ici -->
</ul>
<router-outlet></router-outlet>
<!-- le contenu routé s'ajoute ici (APRÈS L'ÉLÉMENT, PAS DEDANS !) -->
```

`routerLink` est une directive d'attribut de RouterModule. Elle s'attachera à chaque élément de `<ul></ul>` une fois les routes configurées. `router-outlet` est une directive de composant avec un comportement intéressant. Elle agit plus comme un marqueur pour afficher le contenu routé. Le contenu routé résulte de la navigation vers une route spécifique. Habituellement, cela signifie un seul composant tel que configuré dans AppRoutingModule

Le contenu routé se rend juste après `<router-outlet></router-outlet>`. Rien ne se rend à l'intérieur. Cela ne fait pas une grande différence considérable. Cela dit, ne vous attendez pas à ce que `router-outlet` se comporte comme un conteneur pour le contenu routé. Il est simplement un marqueur pour ajouter le contenu routé au Document Object Model (DOM).

## Routage de base

La section précédente établit la configuration de base pour le routage. Avant que le routage réel ne puisse avoir lieu, quelques autres choses doivent être abordées.

La première question à aborder est de savoir quelles routes cette application consommera ? Eh bien, il y a deux composants : AComponent et BComponent. Chacun devrait avoir sa propre route. Ils peuvent se rendre à partir du `router-outlet` de AppComponent en fonction de l'emplacement de la route actuelle.

L'emplacement de la route (ou chemin) définit ce qui s'ajoute à l'[origine d'un site web](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin) (par exemple, [http://localhost:4200](http://localhost:4200/)) via une série de barres obliques (`/`).

```typescript
// 20
6 mêmes imports que précédemment 20
6

const routes: Routes = [
  {
    path: 'A',
    component: AComponent
  },
  {
    path: 'B',
    component: BComponent
  }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
```

`http://localhost:4200/A` rend AComponent à partir du `router-outlet` de AppComponent. `http://localhost:4200/B` rend BComponent. Vous avez besoin d'un moyen de router vers ces emplacements sans utiliser la barre d'adresse. Une application ne devrait pas dépendre de la barre d'adresse d'un navigateur web pour la navigation.

_Le CSS global (Cascading Style-sheets) complète le HTML ci-dessous. Le lien de routage d'une application devrait avoir une apparence agréable. Ce CSS s'applique également à tous les autres exemples._

```css
/* global styles.css */

ul li {
  cursor: pointer;
  display: inline-block;
  padding: 20px;
  margin: 5px;
  background-color: whitesmoke;
  border-radius: 5px;
  border: 1px solid black;
}

ul li:hover {
  background-color: lightgrey;
}
```

```html
<!-- app.component.html -->

<ul>
  <li routerLink="/A">Aller à A !</li>
  <li routerLink="/B">Aller à B !</li>
</ul>
<router-outlet></router-outlet>
```

C'est le routage de base ! Cliquer sur l'un des éléments routerLink route l'adresse web. Il la réassigne sans rafraîchir le navigateur web. Le `Router` d'Angular mappe l'adresse routée aux `Routes` configurées dans AppRoutingModule. Il fait correspondre l'adresse à la propriété `path` d'un seul objet `Route` dans le tableau. La première correspondance gagne toujours, donc les routes de correspondance totale doivent se trouver à la toute fin du tableau `Routes`.

Les routes de correspondance totale empêchent l'application de planter si elle ne peut pas faire correspondre la route actuelle. Cela peut se produire à partir de la barre d'adresse où l'utilisateur peut taper n'importe quelle route. Pour cela, Angular fournit une valeur de chemin générique `**` qui accepte toutes les routes. Cette route rend généralement un composant PageNotFoundComponent affichant « Erreur 404 : Page non trouvée ».

```typescript
// 20
6 PageNotFoundComponent importé avec tout le reste 20
6

const routes: Routes = [
  {
    path: 'A',
    component: AComponent
  },
  {
    path: 'B',
    component: BComponent
  },
  {
    path: '',
    redirectTo: 'A',
    pathMatch: 'full'
  },
  {
    path: '**',
    component: PageNotFoundComponent
  }
];
```

L'objet `Route` contenant `redirectTo` empêche le composant PageNotFoundComponent de se rendre à la suite de `http://localhost:4200`. C'est la route d'accueil de l'application. Pour corriger cela, `redirectTo` redirige la route d'accueil vers `http://localhost:4200/A`. `http://localhost:4200/A` devient indirectement la nouvelle route d'accueil de l'application.

Le `pathMatch: 'full'` indique à l'objet `Route` de correspondre à la route d'accueil (`http://localhost:4200`). Il correspond au chemin vide.

Ces deux nouveaux objets `Route` vont à la fin du tableau puisque la première correspondance gagne. Le dernier élément du tableau (`path: '**'`) correspond toujours, donc il va en dernier.

Il y a une dernière chose à aborder avant de continuer. Comment l'utilisateur sait-il où il se trouve dans l'application par rapport à la route actuelle ? Bien sûr, il peut y avoir du contenu spécifique à la route, mais comment l'utilisateur est-il censé faire ce lien ? Il devrait y avoir une forme de surlignage appliquée aux routerLinks. Ainsi, l'utilisateur saura quelle route est active pour la page web donnée.

C'est une solution facile. Lorsque vous cliquez sur un élément `routerLink`, le `Router` d'Angular lui attribue le _focus_. Ce focus peut déclencher certains styles qui fournissent un retour utile à l'utilisateur. La directive `routerLinkActive` peut suivre ce focus pour le développeur.

```html
<!-- app.component.html -->

<ul>
  <li routerLink="/A" routerLinkActive="active">Aller à A !</li>
  <li routerLink="/B" routerLinkActive="active">Aller à B !</li>
</ul>
<router-outlet></router-outlet>
```

La bonne affectation de `routerLinkActive` représente une chaîne de classes. Cet exemple ne montre qu'une seule classe (`.active`), mais n'importe quel nombre de classes délimitées par des espaces peut s'appliquer. Lorsque le `Router` attribue le _focus_ à un routerLink, les classes délimitées par des espaces s'appliquent à l'élément hôte. Lorsque le focus se déplace, les classes sont automatiquement supprimées.

```css
/* global styles.css */

.active {
  background-color: lightgrey !important;
}
```

Les utilisateurs peuvent maintenant facilement reconnaître comment la route actuelle et le contenu de la page coïncident. Le surlignage `lightgrey` s'applique au routerLink correspondant à la route actuelle. `!important` garantit que le surlignage remplace les styles en ligne.

## Routes paramétrées

Les routes n'ont pas à être entièrement codées en dur. Elles peuvent contenir des variables dynamiques référençables depuis le composant correspondant à l'objet `Route`. Ces variables sont déclarées en tant que paramètres lors de l'écriture du chemin de la route.

Les paramètres de route sont soit optionnels, soit obligatoires pour correspondre à une `Route` particulière. Cela dépend de la manière dont une route écrit ses paramètres. Deux stratégies existent : la paramétrisation matricielle et traditionnelle.

La paramétrisation traditionnelle commence à partir du tableau `Routes` configuré dans AppRoutingModule.

```typescript
const routes: Routes = [
  // 20
6 autres routes 20
6
  {
    path: 'B',
    component: BComponent
  },
  {
    path: 'B/:parameter',
    component: BComponent
  },
  // 20
6 autres routes 20
6
];
```

Concentrez-vous sur les deux routes BComponent. La paramétrisation se produira éventuellement dans les deux routes.

La paramétrisation traditionnelle se produit dans la deuxième `Route` BComponent. `B/:parameter` contient le paramètre `parameter` comme indiqué avec le `:`. Ce qui suit le deux-points marque le nom du paramètre. Le paramètre `parameter` est nécessaire pour que la deuxième `Route` BComponent corresponde.

`parameter` lit la valeur de ce qui est passé dans la route. Le routage vers `http://localhost:4200/B/randomValue` attribuera à `parameter` la valeur de `randomValue`. Cette valeur peut inclure n'importe quoi sauf un autre `/`. Par exemple, `http://localhost:4200/B/randomValue/blahBlah` ne déclenchera pas la deuxième `Route` BComponent. Le composant PageNotFoundComponent se rend à la place.

BComponent peut référencer les paramètres de route à partir de sa classe de composant. Les deux approches de paramétrisation (matricielle et traditionnelle) donnent les mêmes résultats dans BComponent. Avant de voir BComponent, examinez la forme matricielle de la paramétrisation ci-dessous.

```typescript
// app.component.ts

import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  constructor(private router: Router) { }

  routeMatrixParam(value: string) {
    if (value)
      this.router.navigate(['B', { parameter: value }]); // paramètre matriciel
    else
      this.router.navigate(['B']);
  }

  routeAddressParam(value: string) {
    this.router.navigate(['B', value]);
  }
}
```

Le système d'injection de dépendances d'Angular fournit une instanciation du `Router`. Cela permet au composant de router de manière programmatique. La fonction `.navigate(...)` accepte un tableau de valeurs qui se résout en un chemin _routable_. Quelque chose comme `.navigate(['path', 'to', 'something'])` se résout en `http://localhost:4200/path/to/something`. `.navigate(...)` ajoute des marques `/` de délimitation de chemin lors de la normalisation du tableau en un chemin _routable_.

La deuxième forme de paramétrisation se produit dans `routeMatrixParam(...)`. Voyez cette ligne de code : `this.router.navigate(['B', { parameter: value }])`. Cette forme de `parameter` est un paramètre matriciel. Sa valeur est optionnelle pour que la première `Route` BComponent corresponde (`/B`). La `Route` correspond indépendamment de la présence du paramètre dans le chemin.

La fonction `routeAddressParam(...)` résout une route qui correspond à l'approche de paramétrisation `http://localhost:4200/B/randomValue`. Cette stratégie traditionnelle a besoin d'un paramètre pour correspondre à la deuxième route BComponent (`B/:parameter`).

La stratégie matricielle concerne `routeMatrixParam(...)`. Avec ou sans un paramètre matriciel dans son chemin, la première route BComponent correspond toujours. Le paramètre `parameter` passe à BComponent tout comme avec l'approche traditionnelle.

Pour comprendre pleinement le code ci-dessus, voici le HTML de modèle correspondant.

```html
// app.component.html

<ul>
  <li routerLink="/A">Aller à A !</li>
  <li>
    <input #matrixInput>
    <button (click)="routeMatrixParam(matrixInput.value)">Matrice !</button>
  </li>
  <li>
    <input #paramInput>
    <button (click)="routeAddressParam(paramInput.value)">Paramètre !</button>
  </li>
</ul>
<router-outlet></router-outlet>
```

Dans le modèle, les valeurs sont acceptées en tant qu'entrée de texte. L'entrée l'injecte dans le chemin de la route en tant que paramètre. Deux ensembles séparés de cases existent pour chaque stratégie de paramétrisation (traditionnelle et matricielle). Avec toutes les pièces qui s'assemblent, il est temps d'examiner la classe de composant BComponent.

```typescript
// b.component.ts

import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-b',
  template: `
  <p>Paramètre de route : {{ currParam }}</p>
  `
})
export class BComponent implements OnInit {
  currParam: string = "";

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    this.route.params.subscribe((param: ParamMap) => {
      this.currParam = param['parameter'];
    });
  }
}
```

BComponent résulte de l'une des deux routes BComponent dans AppRoutingModule. `ActivatedRoute` s'instancie en un ensemble d'informations utiles concernant la route actuelle. C'est-à-dire, la route qui a provoqué le rendu de BComponent. `ActivatedRoute` s'instancie via l'injection de dépendances ciblant le constructeur de classe.

Le champ `.params` de `ActivatedRoute.params` retourne un `Observable` qui émet les paramètres de route. Remarquez comment les deux approches de paramétrisation différentes aboutissent au paramètre `parameter`. L'`Observable` retourné l'émet en tant que paire clé-valeur à l'intérieur d'un objet `ParamMap`.

Entre les deux approches de paramétrisation, le paramètre `parameter` a été résolu de manière identique. La valeur est émise à partir de `ActivatedRoute.params` malgré l'approche de paramétrisation.

La barre d'adresse distingue les résultats finaux de chaque approche. La paramétrisation matricielle (optionnelle pour la correspondance de `Route`) produit l'adresse : `http://localhost:4200/B;parameter=randomValue`. La paramétrisation traditionnelle (requise pour la correspondance de `Route`) produit : `http://localhost:4200/B/randomValue`.

Dans les deux cas, le même BComponent résulte. La différence réelle : une `Route` BComponent différente correspond. Cela dépend entièrement de la stratégie de paramétrisation. L'approche matricielle garantit que les paramètres sont optionnels pour la correspondance de `Route`. L'approche traditionnelle les exige.

## Routes imbriquées

Les `Routes` peuvent former une hiérarchie. Dans le DOM, cela implique un parent `router-outlet` rendant au moins un enfant `router-outlet`. Dans la barre d'adresse, cela ressemble à ceci : `http://localhost/parentRoutes/childRoutes`. Dans la configuration `Routes`, la propriété `children: []` désigne un objet `Route` comme ayant des routes imbriquées (enfants).

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { NestComponent } from '../../components/nest/nest.component';
import { AComponent } from '../../components/nest/a/a.component';
import { BComponent } from '../../components/nest/b/b.component';

const routes: Routes = [
  {
    path: 'nest',
    component: NestComponent,
    children: [
      { path: 'A', component: AComponent },
      { path: 'B', component: BComponent }
    ]
  }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
```

```typescript
// nest.component.ts

import { Component } from '@angular/core';

@Component({
  selector: 'app-nest',
  template: `
  <ul>
    <li routerLink="./A">Aller à A !</li>
    <li routerLink="./B">Aller à B !</li>
  </ul>
  <router-outlet></router-outlet>
  `
})
export class NestComponent { }
```

NestComponent rend un `router-outlet` après s'être rendu à partir d'un autre `router-outlet` de niveau racine dans AppComponent. Le `router-outlet` du modèle de NestComponent peut rendre soit AComponent (`/nest/A`) soit BComponent (`/nest/B`).

Le AppRoutingModule reflète cette imbrication dans l'objet `Route` de NestComponent. Le champ `children: []` contient un tableau d'objets `Route`. Ces objets `Route` peuvent également imbriquer des routes dans leurs champs `children: []`. Cela peut continuer pour autant de couches de routes imbriquées que nécessaire. L'exemple ci-dessus montre deux couches d'imbrication.

Chaque `routerLink` contient un `./` par rapport à `/`. Le `.` garantit que le routerLink s'ajoute au chemin de la route. Le routerLink remplace complètement le chemin sinon. Après le routage vers `/nest`, `.` s'étend en `/nest`.

Cela est utile pour router vers `/nest/A` ou `/nest/B` à partir de la route `.nest`. `A` et `B` constituent des routes imbriquées de `/nest`. Le routage vers `/A` ou `/B` retourne PageNotFound. `/nest` doit précéder les deux routes.

Jetez un coup d'œil à AppComponent contenant le `router-outlet` de niveau racine dans son modèle. AppComponent est la première couche d'imbrication tandis que NestComponent est la deuxième.

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
  <ul>
    <li routerLink="/nest">Aller aux routes imbriquées !</li>
    <li routerLink="/">Sortir des routes imbriquées !</li>
  </ul>
  <router-outlet></router-outlet>
  `
})
export class AppComponent { }
```

À l'intérieur de l'objet `Route` nest, le `children: []` contient deux autres routes imbriquées. Elles résultent en AComponent et BComponent lors du routage depuis `/nest` comme discuté précédemment. Ces composants sont très simples pour le bien de la démonstration. `<li routerLink="/">...</li>` vous permet de naviguer hors des routes imbriquées pour réinitialiser l'exemple en naviguant vers la route d'accueil.

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-a',
  template: `
  <p>a fonctionne !</p>
  `
})
export class AComponent { }
```

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-b',
  template: `
  <p>b fonctionne !</p>
  `
})
export class BComponent { }
```

Le tableau `children: []` accepte les objets `Route` comme éléments. `children: []` peut s'appliquer à n'importe lequel de ces éléments également. Les enfants de ces éléments peuvent continuer à s'imbriquer. Ce schéma peut continuer pour autant de couches d'imbrication que nécessaire. Insérez un `router-outlet` dans le modèle pour chaque couche de routage imbriqué.

Les techniques de routage s'appliquent indépendamment du niveau d'imbrication d'un objet `Route`. Les techniques de paramétrisation diffèrent sur un seul aspect. Les routes enfants ne peuvent accéder aux paramètres de leurs parents que via `ActivatedRoute.parent.params`. `ActivatedRoute.params` cible le même niveau de routes imbriquées. Cela exclut les routes de niveau parent et leurs paramètres.

Les gardes de `Route` sont particulièrement adaptés au routage imbriqué. Un objet `Route` peut restreindre l'accès à toutes ses routes imbriquées (enfants).

## Routes protégées

Les applications web consistent souvent en des données publiques et privées. Les deux types de données ont tendance à avoir leurs propres pages avec des routes _protégées_. Ces routes permettent/restreignent l'accès en fonction des privilèges de l'utilisateur. Les utilisateurs non autorisés peuvent interagir avec une route protégée. La route doit bloquer l'utilisateur s'il ou elle tente d'accéder à son contenu routé.

Angular fournit un ensemble de gardes d'authentification qui peuvent s'attacher à n'importe quelle route. Ces méthodes se déclenchent automatiquement en fonction de la manière dont l'utilisateur interagit avec la route protégée.

* `canActivate(...)` - se déclenche lorsque l'utilisateur tente d'accéder à une route
* `canActivateChild(...)` - se déclenche lorsque l'utilisateur tente d'accéder aux routes imbriquées (enfants) d'une route
* `canDeactivate(...)` - se déclenche lorsque l'utilisateur tente de quitter une route

Les méthodes de garde d'Angular sont disponibles depuis `@angular/router`. Pour les aider à s'authentifier, elles peuvent optionnellement recevoir quelques paramètres. Ces paramètres ne s'injectent pas via l'injection de dépendances. Sous le capot, chaque valeur est passée en tant qu'argument à la méthode de garde invoquée.

* `ActivatedRouteSnapshot` - disponible pour les trois
* `RouterStateSnapshot` - disponible pour les trois
* `Component` - disponible pour `canDeactivate(...)`

`ActivatedRouteSnapshot` fournit l'accès aux paramètres de route de la route protégée. `RouterStateSnapshot` expose l'adresse web URL (uniform resource locator) correspondant à la route. `Component` référence le composant rendu par la route.

Pour protéger une route, une classe implémentant les méthodes de garde doit d'abord exister en tant que service. Le service peut s'injecter dans AppRoutingModule pour protéger ses `Routes`. La valeur du jeton pour le service peut s'injecter dans n'importe quel objet `Route`.

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AuthService } from '../../services/auth.service';
import { UserService } from '../../services/user.service';

import { PrivateNestComponent } from '../../components/private-nest/private-nest.component';
import { PrivateAComponent } from '../../components/private-nest/private-a/private-a.component';
import { PrivateBComponent } from '../../components/private-nest/private-b/private-b.component';

const routes: Routes = [
  {
    path: 'private-nest',
    component: PrivateNestComponent,
    canActivate: [ AuthService ], // !!!
    canActivateChild: [ AuthService ], // !!!
    canDeactivate: [ AuthService ], // !!!
    children: [
      { path: 'private-A', component: PrivateAComponent },
      { path: 'private-B', component: PrivateBComponent }
    ]
  }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ],
  providers: [
    AuthService,
    UserService
  ]
})
export class AppRoutingModule { }
```

`canActivate`, `canActivateChild`, et `canDeactivate` sont implémentés à partir de AuthService. L'implémentation du service sera montrée sous peu aux côtés de l'implémentation de UserService.

UserService fournit les informations nécessaires pour authentifier un utilisateur. Les implémentations des méthodes de garde de AuthService effectuent l'authentification. AppRoutingModule doit inclure les deux services dans son tableau de fournisseurs. C'est ainsi que l'injecteur du module sait comment les instancier.

Les routes imbriquées existent à partir du chemin `/private-nest`. L'objet `Route` pour `/private-nest` contient quelques nouveaux champs. Leurs noms devraient sembler familiers car ils reflètent leurs méthodes de garde correspondantes.

Chaque champ déclenche l'implémentation de la méthode homonyme à l'intérieur du service lorsqu'il est déclenché. N'importe quel nombre de services peut également remplir ce tableau. L'implémentation de la méthode de chaque service est testée. Elles doivent retourner une valeur booléenne ou un `Observable` qui émet une valeur booléenne.

Voir les implémentations de AuthService et UserService ci-dessous.

```typescript
// user.service.ts

import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

class TheUser {
  constructor(public isLoggedIn: boolean = false) { }

  toggleLogin() {
    this.isLoggedIn = true;
  }

  toggleLogout() {
    this.isLoggedIn = false;
  }
}

const globalUser = new TheUser();

@Injectable({
  providedIn: 'root'
})
export class UserService {
  theUser: TheUser = globalUser;

  constructor(private router: Router) { }

  get isLoggedIn() {
    return this.theUser.isLoggedIn;
  }

  login() {
    this.theUser.toggleLogin();
  }

  logout() {
    this.theUser.toggleLogout();
    this.router.navigate(['/']);
  }
}
```

La même instance de `TheUser` est transmise avec chaque instanciation de UserService. `TheUser` fournit l'accès à `isLoggedIn` déterminant le statut de connexion de l'utilisateur. Deux autres méthodes publiques permettent à UserService de basculer la valeur de `isLoggedIn`. C'est ainsi que l'utilisateur peut se connecter et se déconnecter.

Vous pouvez considérer `TheUser` comme une instance globale. `UserService` est une interface instanciable qui configure cette globale. Les modifications apportées à `TheUser` à partir d'une instanciation de `UserService` s'appliquent à chaque autre instance de `UserService`. `UserService` est implémenté dans AuthService pour fournir l'accès à `isLoggedIn` de `TheUser` pour l'authentification.

```typescript
import { Component, Injectable } from '@angular/core';
import { CanActivate, CanActivateChild, CanDeactivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

import { UserService } from './user.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService implements CanActivate, CanActivateChild, CanDeactivate<Component> {
  constructor(private user: UserService) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    if (this.user.isLoggedIn)
      return true;
    else
      return false;
  }

  canActivateChild(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    return this.canActivate(route, state);
  }

  canDeactivate(component: Component, route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    if (!this.user.isLoggedIn || window.confirm('Quitter le nid ?'))
      return true;
    else
      return false;
  }
}
```

AuthService implémente chaque méthode de garde importée depuis `@angular/router`. Chaque méthode de garde correspond à un champ correspondant dans l'objet `Route` de PrivateNestComponent. Une instance de UserService est instanciée à partir du constructeur de AuthService. AuthService détermine si un utilisateur peut continuer en utilisant `isLoggedIn` exposé par UserService.

Retourner `false` depuis une garde indique à la route de bloquer l'utilisateur. Une valeur de retour de `true` permet à l'utilisateur de continuer vers sa destination de route. Si plus d'un service authentifie, ils doivent tous retourner vrai pour permettre l'accès. `canActivateChild` protège les routes enfants de PrivateNestComponent. Cette méthode de garde tient compte des utilisateurs contournant PrivateNestComponent via la barre d'adresse.

Les paramètres des méthodes de garde sont passés automatiquement lors de l'invocation. Bien que l'exemple ne les utilise pas, ils fournissent des informations utiles depuis la route. Le développeur peut utiliser ces informations pour aider à authentifier l'utilisateur.

AppComponent instancie également UserService pour une utilisation directe dans son modèle. L'instanciation de UserService de AppComponent et AuthService référence la même classe utilisateur (`TheUser`).

```typescript
import { Component } from '@angular/core';

import { UserService } from './services/user.service';

@Component({
  selector: 'app-root',
  template: `
  <ul>
    <li routerLink="/private-nest">Entrer dans le nid secret !</li>
    <li routerLink="/">Quitter le nid secret !</li>
    <li *ngIf="user.isLoggedIn"><button (click)="user.logout()">DÉCONNEXION</button></li>
    <li *ngIf="!user.isLoggedIn"><button (click)="user.login()">CONNEXION</button></li>
  </ul>
  <router-outlet></router-outlet>
  `
})
export class AppComponent {
  constructor(private user: UserService) { }
}
```

UserService gère toute la logique pour AppComponent. AppComponent concerne principalement son modèle. Un UserService est instancié en tant que `user` à partir du constructeur de classe. Les données de `user` déterminent la fonctionnalité du modèle.

## Conclusions

Le routage établit un équilibre entre l'organisation et la restriction des sections de l'application. Une application plus petite, comme un blog ou une page d'hommage, peut ne pas nécessiter de routage. Même dans ce cas, inclure un peu de routage par hachage ne pourrait pas faire de mal. Un utilisateur peut vouloir référencer seulement une partie de la page après tout.

Angular applique sa propre bibliothèque de routage construite sur l'API [history](https://developer.mozilla.org/en-US/docs/Web/API/History_API) de HTML5. Cette API omet le routage par hachage pour utiliser plutôt les méthodes `pushState(...)` et `replaceState(...)`. Elles changent l'URL de l'adresse web sans rafraîchir la page. La stratégie de routage par emplacement de chemin par défaut dans Angular fonctionne de cette manière. Définir `RouterModule.forRoot(routes, { useHash: true })` active le routage par hachage si préféré.

Cet article s'est concentré sur la stratégie de routage par emplacement de chemin par défaut. Indépendamment de la stratégie, de nombreux utilitaires de routage sont disponibles pour router une application. Le `RouterModule` expose ces utilitaires à travers ses exports. Les routes de base, paramétrées, imbriquées et protégées sont toutes possibles en utilisant RouterModule.

# **NgModules**

Les applications Angular commencent à partir du NgModule racine. Angular gère les dépendances d'une application via son système de modules composé de NgModules. Aux côtés des modules JavaScript simples, les NgModules assurent la modularité et l'encapsulation du code.

Les modules fournissent également un niveau supérieur d'organisation du code. Chaque NgModule sectionne son propre bloc de code en tant que racine. Ce module fournit une encapsulation de haut en bas pour son code. L'ensemble du bloc de code peut ensuite être exporté vers n'importe quel autre module. En ce sens, les NgModules agissent comme des gardiens de leurs propres blocs de code.

Les utilitaires documentés d'Angular proviennent de NgModules écrits par Angular. Aucun utilitaire n'est disponible à moins que le NgModule qui le déclare soit inclus dans la racine. Ces utilitaires doivent également être exportés depuis leur module hôte afin que les importateurs puissent les utiliser. Cette forme d'encapsulation permet au développeur de produire ses propres NgModules dans le même système de fichiers.

De plus, il est logique de savoir pourquoi l'interface de ligne de commande (CLI) Angular importe `BrowserModule` depuis `@angular/core`. Cela se produit chaque fois qu'une nouvelle application est générée en utilisant la commande CLI : `ng new [nom-de-l'application]`.

Comprendre le but de l'implémentation peut suffire dans la plupart des cas. Cependant, comprendre comment l'implémentation se connecte à la racine est encore mieux. Tout cela se fait automatiquement en important `BrowserModule` dans la racine.

### Décorateur NgModule

Angular définit ses modules en décorant une classe générique. Le décorateur `@NgModule` indique à Angular le but modulaire de la classe. Une classe NgModule consolide les dépendances racine accessibles/instanciables depuis la portée du module. « Portée » signifiant tout ce qui provient des métadonnées du module.

```typescript
import { NgModule } from '@angular/core';

@NgModule({
  // 20
6 métadonnées 20
6
})
export class AppModule { }
```

### Métadonnées NgModule

Le NgModule racine généré par le CLI inclut les champs de métadonnées suivants. Ces champs fournissent une configuration au bloc de code sur lequel le NgModule préside.

* `declarations: []`
* `imports: []`
* `providers: []`
* `bootstrap: []`

### Déclarations

Le tableau des déclarations inclut tous les composants, directives ou pipes hébergés par un NgModule. Ils sont privés au module sauf s'ils sont explicitement exportés dans ses métadonnées. Étant donné ce cas d'utilisation, les composants, directives et pipes sont surnommés « déclarables ». Un NgModule doit déclarer un déclarable de manière unique. Le déclarable ne peut pas être déclaré deux fois dans des NgModules séparés. Une erreur est générée sinon. Voir l'exemple ci-dessous.

```typescript
import { NgModule } from '@angular/core';
import { TwoComponent } from './components/two.component.ts';

@NgModule({
  declarations: [ TwoComponent ]
})
export class TwoModule { }

@NgModule({
  imports: [ TwoModule ],
  declarations: [ TwoComponent ]
})
export class OneModule { }
```

Angular génère une erreur pour le bien de l'encapsulation NgModule. Les déclarables sont privés au NgModule qui les déclare par défaut. Si plusieurs NgModules ont besoin d'un certain déclarable, ils doivent importer le NgModule déclarant. Ce NgModule doit ensuite exporter le déclarable souhaité afin que les autres NgModules puissent l'utiliser.

```typescript
import { NgModule } from '@angular/core';
import { TwoComponent } from './components/two.component.ts';

@NgModule({
  declarations: [ TwoComponent ],
  exports: [ TwoComponent ]
})
export class TwoModule { }

@NgModule({
  imports: [ TwoModule ] // ce module peut maintenant utiliser TwoComponent
})
export class OneModule { }
```

L'exemple ci-dessus ne générera pas d'erreur. TwoComponent a été déclaré de manière unique entre les deux NgModules. OneModule a également accès à TwoComponent puisqu'il importe TwoModule. TwoModule exporte à son tour le TwoComponent pour une utilisation externe.

### Imports

Le tableau des imports n'accepte que les NgModules. Ce tableau n'accepte pas les déclarables, services ou autre chose que les NgModules. Importer un module fournit l'accès aux déclarables que le module publicise.

Cela explique pourquoi l'importation de `BrowserModule` fournit l'accès à ses divers utilitaires. Chaque utilitaire déclarable déclaré dans `BrowserModule` est exporté depuis ses métadonnées. Lors de l'importation de `BrowserModule`, ces déclarables exportés deviennent disponibles pour le NgModule importateur. Les services ne sont pas exportés du tout puisqu'ils manquent de la même encapsulation.

### Providers

Le manque d'encapsulation des services peut sembler étrange étant donné l'encapsulation des déclarables. Souvenez-vous que les services vont dans le tableau des providers séparément des déclarations ou des exports.

Lorsque Angular compile, il aplatit le NgModule racine et ses imports en un seul module. Les services se regroupent dans un seul tableau de providers hébergé par le NgModule fusionné. Les déclarables maintiennent leur encapsulation via un ensemble de drapeaux de temps de compilation.

Si les providers de NgModule contiennent des valeurs de jeton correspondantes, le module racine importateur prend le pas. Au-delà de cela, le dernier NgModule importé prend le pas. Voir l'exemple suivant. Portez une attention particulière au NgModule important les deux autres. Reconnaissez comment cela affecte la priorité du service fourni.

```typescript
import { NgModule } from '@angular/core';

@NgModule({
  providers: [ AwesomeService ], // 1ère priorité + module importateur
  imports: [
    BModule,
    CModule
  ]
})
export class AModule { }

@NgModule({
  providers: [ AwesomeService ]  // 3ème priorité + premier import
})
export class BModule { }

@NgModule({
  providers: [ AwesomeService ]  // 2ème priorité + dernier import
})
export class CModule { }
```

L'instanciation de AwesomeService depuis la portée de AModule résulte en une instance de AwesomeService telle que fournie dans les métadonnées de AModule. Si les providers de AModule omettent ce service, le AwesomeService de CModule prendrait le pas. Et ainsi de suite pour BModule si les providers de CModule omettent AwesomeService.

## Bootstrap

Le tableau de bootstrap accepte les composants. Pour chaque composant du tableau, Angular insère le composant en tant que sa propre racine du fichier `index.html`. Le NgModule racine généré par le CLI d'une application aura toujours ce champ.

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [ AppComponent ],
  imports: [ BrowserModule ],
  providers: [],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
```

L'élément AppComponent sera injecté dans le HTML de base de l'application (`index.html`). Le reste de l'arbre des composants se déploie à partir de là. La portée du NgModule englobant couvre tout cet arbre plus tous les autres injectés depuis le tableau de bootstrap. Le tableau contient généralement un seul élément. Ce composant représente le module en tant qu'élément unique et son arbre sous-jacent.

## NgModules vs Modules JavaScript

Vous avez vu Angular et les modules JavaScript travailler ensemble dans les exemples précédents. Les déclarations `import..from` les plus élevées constituent le système de modules JavaScript. Les emplacements de fichiers de chaque cible de déclaration doivent exporter une classe, une variable ou une fonction correspondant à la demande. `import { TARGET } from './path/to/exported/target'`.

En JavaScript, les modules sont séparés par fichiers. Les fichiers importent en utilisant les mots-clés `import..from` comme mentionné précédemment. Les NgModules, en revanche, sont séparés par classes et décorés avec `@NgModule`. Ainsi, de nombreux modules Angular peuvent exister dans un seul fichier. Cela ne peut pas se produire avec JavaScript puisque un fichier définit un module.

Certes, les conventions disent que chaque classe décorée avec `@NgModule` devrait avoir son propre fichier. Même ainsi, sachez que les fichiers ne constituent pas leurs propres modules dans Angular. Les classes décorées avec `@NgModule` créent cette distinction.

Les modules JavaScript fournissent des références de jeton aux métadonnées `@NgModule`. Cela se produit en haut d'un fichier hébergeant une classe NgModule. NgModule utilise ces jetons à l'intérieur de ses champs de métadonnées (déclarables, imports, providers, etc.). La seule raison pour laquelle `@NgModule` peut décorer une classe en premier lieu est que JavaScript l'importe depuis le haut du fichier.

```typescript
// Le système de modules JavaScript fournit des jetons
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { AppService } from './app.service';
// Le système de modules JavaScript est strict sur l'endroit où il importe. Il ne peut importer qu'en haut des fichiers.

// Angular NgModule utilise ces jetons dans ses paramètres de métadonnées
@NgModule({ // import { NgModule } from '@angular/core';
  declarations: [
    AppComponent // import { AppComponent } from './app.component';
  ],
  imports: [
    BrowserModule // import { BrowserModule } from '@angular/platform-browser';
  ],
  providers: [
    AppService // import { AppService } from './app.service';
  ],
  bootstrap: [
    AppComponent // import { AppComponent } from './app.component';
  ]
})
export class AppModule { }
// Le système de modules JavaScript exporte la classe. D'autres modules peuvent maintenant importer AppModule.
```

L'exemple ci-dessus n'introduit rien de nouveau. L'accent est mis ici sur les commentaires expliquant comment les deux systèmes modulaires fonctionnent ensemble. JavaScript fournit des références de jeton tandis que NgModule utilise ces jetons pour encapsuler et configurer son bloc de code sous-jacent.

### Modules de fonctionnalités

Les applications se développent avec le temps. Les mettre à l'échelle correctement nécessite une organisation de l'application. Un système solide pour cela rendra le développement ultérieur beaucoup plus facile.

Dans Angular, les schémas garantissent que les sections de code orientées vers un but restent distinguables. Au-delà des schémas de sous-NgModule, il y a les NgModules eux-mêmes. Ils sont également un type de schéma. Ils se tiennent au-dessus des autres dans la liste des schémas à l'exclusion de l'application elle-même.

Le module racine ne doit pas rester seul une fois qu'une application commence à se développer. Les modules de fonctionnalités incluent tout NgModule utilisé aux côtés du NgModule racine. Vous pouvez considérer le module racine comme ayant le champ de métadonnées `bootstrap: []`. Les applications de fonctionnalités garantissent que le module racine ne sature pas ses métadonnées.

Les modules de fonctionnalités isolent une section de code au nom de tout module importateur. Ils peuvent gérer des sections entières de l'application de manière indépendante. Cela signifie qu'il pourrait être utilisé dans n'importe quelle application dont le module racine importe le module de fonctionnalité. Cette tactique fait gagner du temps et des efforts aux développeurs sur le cours de plusieurs applications ! Cela maintient également le NgModule racine de l'application léger.

Dans le NgModule racine d'une application, l'ajout d'un jeton de module de fonctionnalité dans le tableau `imports` de la racine fait l'affaire. Tout ce que le module de fonctionnalité exporte ou fournit devient disponible pour la racine.

```typescript
// ./awesome.module.ts

import { NgModule } from '@angular/core';
import { AwesomePipe } from './awesome/pipes/awesome.pipe';
import { AwesomeComponent } from './awesome/components/awesome.component';
import { AwesomeDirective } from './awesome/directives/awesome.directive';

@NgModule({
  exports: [
    AwesomePipe,
    AwesomeComponent,
    AwesomeDirective
  ]
  declarations: [
    AwesomePipe,
    AwesomeComponent,
    AwesomeDirective
  ]
})
export class AwesomeModule { }
```

```typescript
// ./app.module.ts

import { AwesomeModule } from './awesome.module';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    AwesomeModule,
    BrowserModule
  ],
  providers: [],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
```

```typescript
// ./app.component.ts

import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
  <!-- AwesomeDirective -->
  <h1 appAwesome>Cet élément mute selon la logique de la directive appAwesome.</h1>

  <!-- AwesomePipe -->
  <p>Sortie générique : {{ componentData | awesome }}</p>

  <section>
    <!-- AwesomeComponent -->
    <app-awesome></app-awesome>
  </section>
  `
})
export class AppComponent {
  componentData: string = "Beaucoup de données transformables !";
}
```

`<app-awesome></app-awesome>` (composant), `awesome` (pipe), et `appAwesome` (directive) sont exclusifs à AwesomeModule. Si celui-ci n'avait pas exporté ces déclarables ou si AppModule avait négligé d'ajouter AwesomeModule à ses imports, alors les déclarables de AwesomeModule n'auraient pas été utilisables par le modèle de AppComponent. AwesomeModule est un module de fonctionnalité pour le NgModule racine AppModule.

Angular fournit certains de ses propres modules qui complètent la racine lors de leur importation. Cela est dû au fait que ces modules de fonctionnalité exportent ce qu'ils créent.

### Méthodes statiques de module

Parfois, les modules offrent l'option d'être configurés avec un objet de configuration personnalisé. Cela est réalisé en exploitant des méthodes statiques à l'intérieur de la classe de module.

Un exemple de cette approche est le `RoutingModule` qui fournit une méthode `.forRoot(...)` directement sur le module.

Pour définir votre propre méthode statique de module, vous l'ajoutez à la classe de module en utilisant le mot-clé `static`. Le type de retour doit être `ModuleWithProviders`.

```ts
// configureable.module.ts

import { AwesomeModule } from './awesome.module';
import { ConfigureableService, CUSTOM_CONFIG_TOKEN, Config } from './configurable.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


@NgModule({
  imports: [
    AwesomeModule,
    BrowserModule
  ],
  providers: [
    ConfigureableService
  ]
})
export class ConfigureableModule { 
  static forRoot(config: Config): ModuleWithProviders {
    return {
        ngModule: ConfigureableModule,
        providers: [
            ConfigureableService,
            {
                provide: CUSTOM_CONFIG_TOKEN,
                useValue: config
            }
        ]
    };
  }
}
```

```ts
// configureable.service.ts

import { Inject, Injectable, InjectionToken } from '@angular/core';

export const CUSTOM_CONFIG_TOKEN: InjectionToken<string> = new InjectionToken('customConfig');

export interface Config {
  url: string
}

@Injectable()
export class ConfigureableService {
  constructor(
    @Inject(CUSTOM_CONFIG_TOKEN) private config: Config
  )
}
```

Remarquez que l'objet que la méthode `forRoot(...)` retourne est presque identique à la configuration `NgModule`.

La méthode `forRoot(...)` accepte un objet de configuration personnalisé que l'utilisateur peut fournir lors de l'importation du module.

```ts
imports: [
  ...
  ConfigureableModule.forRoot({ url: 'http://localhost' }),
  ...
]
```

La configuration est ensuite fournie en utilisant un `InjectionToken` personnalisé appelé `CUSTOM_CONFIG_TOKEN` et injectée dans le `ConfigureableService`. Le `ConfigureableModule` doit être importé une seule fois en utilisant la méthode `forRoot(...)`. Cela fournit le `CUSTOM_CONFIG_TOKEN` avec la configuration personnalisée. Tous les autres modules doivent importer le `ConfigureableModule` sans la méthode `forRoot(...)`.

## Exemples de NgModule d'Angular

Angular fournit une variété de modules importables depuis `@angular`. Deux des modules les plus couramment importés sont `CommonModule` et `HttpClientModule`.

`CommonModule` est en fait un sous-ensemble de `BrowserModule`. Les deux fournissent l'accès aux directives structurelles `*ngIf` et `*ngFor`. `BrowserModule` inclut une installation spécifique à la plateforme pour le navigateur web. `CommonModule` omet cette installation. Le `BrowserModule` doit être importé dans le NgModule racine d'une application web. `CommonModule` fournit `*ngIf` et `*ngFor` aux modules de fonctionnalités ne nécessitant pas d'installation de plateforme.

`HttpClientModule` fournit le service `HttpClient`. Souvenez-vous que les services vont dans le tableau des providers des métadonnées `@NgModule`. Ils ne sont pas déclarables. Pendant la compilation, chaque NgModule est consolidé en un seul module. Les services ne sont pas encapsulés contrairement aux déclarables. Ils sont tous instanciables via l'injecteur racine situé à côté du NgModule fusionné.

Revenons au point. Comme tout autre service, `HttpClient` s'instancie dans une classe via son constructeur par injection de dépendances (DI). En utilisant DI, l'injecteur racine injecte une instance de `HttpClient` dans le constructeur. Ce service permet aux développeurs de faire des requêtes HTTP avec l'implémentation du service.

L'implémentation de `HttpClient` est incluse dans le tableau des providers de `HttpClientModule`. Tant que le NgModule racine importe `HttpClientModule`, `HttpClient` s'instanciera depuis l'intérieur de la portée de la racine comme prévu.

## Conclusion

Il est probable que vous ayez déjà profité des NgModules d'Angular. Angular rend très facile l'ajout d'un module dans le tableau des imports du NgModule racine. Les utilitaires sont souvent exportés depuis les métadonnées du module importé. D'où la raison pour laquelle ses utilitaires deviennent soudainement disponibles lors de l'importation dans le NgModule racine.

Les NgModules fonctionnent en étroite collaboration avec les modules JavaScript simples. L'un fournit des jetons tandis que l'autre les utilise pour la configuration. Leur travail d'équipe aboutit à un système modulaire robuste unique au framework Angular. Il fournit une nouvelle couche d'organisation au-dessus de tous les autres schémas, à l'exclusion de l'application.

Espérons que cet article approfondit votre compréhension des NgModules. Angular peut exploiter ce système encore plus loin pour certains des cas d'utilisation les plus exotiques.
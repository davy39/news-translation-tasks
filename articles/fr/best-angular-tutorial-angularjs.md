---
title: Les meilleurs tutoriels sur Angular et AngularJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-23T00:49:00.000Z'
originalURL: https://freecodecamp.org/news/best-angular-tutorial-angularjs
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f1a740569d1a4ca40d5.jpg
tags:
- name: Angular
  slug: angular
- name: Angular
  slug: angularjs
- name: Tutorial
  slug: tutorial
seo_title: Les meilleurs tutoriels sur Angular et AngularJS
seo_desc: AngularJS (versions 1.x) is a JavaScript-based open source Framework. It
  is cross platform and used to develop Single Page Web Applications (SPWAs). AngularJS
  implements the MVC pattern to separate the logic, presentation, and data components.
  It als...
---

AngularJS (versions 1.x) est un Framework open source basé sur JavaScript. Il est multiplateforme et utilisé pour développer des applications web monopage (SPWA). AngularJS implémente le modèle MVC pour séparer la logique, la présentation et les composants de données. Il utilise également l'injection de dépendances pour exploiter les services côté serveur dans les applications côté client.

Angular (versions 2.x et supérieures) est un framework open source basé sur TypeScript pour développer des applications web front-end. Angular dispose de fonctionnalités comme les génériques, le typage statique ainsi que certaines fonctionnalités ES6.

Nous recommandons d'apprendre Angular et de l'utiliser pour de nouveaux projets. AngularJS est principalement utilisé pour les projets hérités.

La meilleure façon d'apprendre Angular est avec le [tutoriel Angular de 6 heures de freeCodeCamp](https://www.youtube.com/watch?v=2OHbjep_WjQ) sur YouTube.

![Image](https://img.youtube.com/vi/2OHbjep_WjQ/maxresdefault.jpg)

# Autres tutoriels sur Angular

## **Angular 1.x**

### **Pages générales**

* [Angular JS](https://angularjs.org/) - La page d'accueil d'Angular JS
* [Guide de style AngularJS](https://github.com/johnpapa/angular-styleguide/tree/master/a1) - Bonnes pratiques détaillées pour le développement Angular

### **Vidéos**

* [Routing in Angular JS](https://www.youtube.com/watch?v=5uhZCc0j9RY) - Routage côté client en 15 minutes
* [Angular ToDo App](https://www.youtube.com/watch?v=WuiHuZq_cg4) - Une application Angular ToDo en 12 minutes

### **Cours**

* [Cours AngularJS sur Egghead.io ($)](https://egghead.io/browse/frameworks/angularjs)

## **Angular 2.x+**

### **Pages générales**

* [Angular](https://angular.io/) - La page d'accueil d'Angular
* [Guide de style Angular](https://angular.io/guide/styleguide) - Bonnes pratiques détaillées pour le développement Angular

### **Pages sur des sujets spécifiques**

* [Directives](http://www.sitepoint.com/practical-guide-angularjs-directives/) - Guide excellent détaillant les directives Angular (Partie 1)

### **Cours**

* [Cours Angular sur Egghead.io ($)](https://egghead.io/browse/frameworks/angular)
* [FrontendMasters - Construire des applications géniales avec Angular](https://frontendmasters.com/courses/building-apps-angular)
* [Ultimate Angular - Todd Motto](https://ultimateangular.com/)
* [Angular 6 (anciennement Angular 2) - Le guide complet ($) Maximilian Schwarzmüller](https://www.udemy.com/the-complete-guide-to-angular-2/)

## **Blogs**

* [Alligator.io](https://alligator.io/angular/)
* [Angular In Depth](https://blog.angularindepth.com/tagged/angular)

## **Historique des versions**

Google a publié la version initiale d'AngularJS le 20 octobre 2010. La première version stable d'AngularJS était la version 1.6.8, publiée le 18 décembre 2017. La version Angular 2.0 a été publiée le 22 septembre 2014 lors de la conférence ng-Europe. L'une des fonctionnalités d'Angular 2.0 est le chargement dynamique.

Après quelques modifications, Angular 4.0 a été publié en décembre 2016. Angular 4 est rétrocompatible avec Angular 2.0. La bibliothèque HttpClient est l'une des fonctionnalités d'Angular 4.0. Angular 5 a été publié le 1er novembre 2017. Le support des applications web progressives était l'une des améliorations d'Angular 4.0. Angular 6 a été publié en mai 2018. La dernière version stable est [6.1.9](https://blog.angular.io/angular-v6-1-now-available-typescript-2-9-scroll-positioning-and-more-9f1c03007bb6)

**Installation** :

Nous pouvons ajouter Angular soit en référençant les sources disponibles, soit en téléchargeant le framework.

**Lien vers la source** :

AngularJS : Nous pouvons ajouter AngularJS (versions Angular 1.x) en référençant le réseau de diffusion de contenu de Google.

```html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js"></script> 
```

Téléchargement/installation : Nous pouvons télécharger le framework avec npm, Bower ou composer.

**Angular 1.x** :

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

Pour plus d'informations concernant la documentation, consultez le site officiel d'[AngularJS](https://docs.angularjs.org/api).

Vous pouvez installer **Angular 2.x** et d'autres versions en suivant les étapes de la documentation officielle d'[Angular](https://angular.io/guide/quickstart).

# **Composants**

#### **Motivation**

Angular contient de nombreux _schematics_ pour construire des applications. Les composants sont l'un de ces schematics. Ils englobent une seule unité de logique concernant une seule partie de l'application. Les composants s'associent souvent à d'autres schematics pour fonctionner plus efficacement.

Parmi tous les schematics, les composants tendent à consommer plus qu'ils ne fournissent. Alors que d'autres schematics comme les directives, les pipes et les services offrent des utilitaires, les composants les utilisent. Ils sont responsables de l'interface de l'application, ce qui explique pourquoi ils consomment des utilitaires.

Les composants simplifient l'application. Canaliser la logique dans une seule section de l'interface visible est leur objectif principal. Pour construire des applications étape par étape, vous devez construire composant par composant. Les composants agissent comme les blocs de construction d'Angular, après tout.

#### **Introduction aux composants**

Comme mentionné, les composants consomment des utilitaires (services/ressources). Ils se situent entre la logique métier et la présentation pour produire une unité cohésive. Angular attache divers mécanismes à chaque composant. Ces attaches identifient une classe comme un composant et définissent ses capacités standard.

Angular doit reconnaître les composants lorsqu'il les rencontre. Pour ce faire, `@Component` doit décorer chaque classe destinée à être un composant. Les décorateurs indiquent à Angular ce qu'est la classe.

Dans le cas d'un composant, il doit savoir comment interagir avec son injecteur, se connecter à un modèle, tirer d'une liste de styles, encapsuler ses styles, et ainsi de suite. Angular prend en charge la plupart des exigences de bas niveau. Les développeurs doivent encore configurer le comportement d'un composant, importer ses dépendances et étendre sa logique.

Pour toutes ces choses, nous avons la classe du composant. La classe garde tout relativement uniforme. Elle encapsule la logique métier du composant.

#### **Classe de composant et métadonnées**

Allez-y et installez l'[interface de ligne de commande (CLI) Angular](https://cli.angular.io/). Vous pouvez en apprendre plus à ce sujet à partir de [cet article](https://guide.freecodecamp.org/angular/command-line-interface). La commande CLI `ng generate component [nom-du-composant]` produit ce qui suit.

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

Ceci est le squelette de base à partir duquel tous les grands composants proviennent. Le décorateur `@Component` est la partie la plus importante. Sans lui, l'exemple ci-dessus devient une classe générique. Angular s'appuie sur les décorateurs pour discerner le type de schéma d'une classe.

`@Component` reçoit des métadonnées sous forme d'un seul objet. Les décorateurs ne sont que des fonctions JavaScript sous le capot. Ils prennent des arguments comme avec l'objet de métadonnées. L'objet de métadonnées configure les dépendances de base d'un composant. Chaque champ joue un rôle.

* `selector:` indique à Angular d'associer le composant à un certain élément dans le modèle HTML de l'application.
* `templateUrl:` accepte l'emplacement du fichier du modèle HTML du composant (c'est là que les données sont affichées).
* `styleUrls:` accepte un tableau d'emplacements de fichiers de feuilles de style (chaînes). Ces feuilles de style ciblent le modèle assigné au composant.

Considérez les métadonnées comme un gros bloc de configuration. Le décorateur les prend afin qu'il puisse générer les données spécifiques au composant. Le décorateur _décore_ la classe sous-jacente avec les données nécessaires au comportement de sa classe. Une classe de _composant_ en l'occurrence.

La signature de la classe est exportée par défaut afin que le composant puisse être importé. `ngOnInit` est également implémenté. `implements` indique à la classe de définir certaines méthodes selon la définition de l'interface. `ngOnInit` est un hook de cycle de vie.

#### **Cycle de vie du composant et détection des changements**

Les composants utilisent toutes sortes d'outils, de services et de fonctionnalités. Une fonctionnalité clé disponible pour les composants est les hooks de cycle de vie. Une explication pour chaque hook existe [dans cet article](https://guide.freecodecamp.org/angular/lifecycle-hooks).

Il y en a huit au total et ils servent tous de fonctions de timing. Ils s'exécutent conditionnellement lorsque le composant passe d'un état à un autre via la [détection des changements](https://blog.angularindepth.com/everything-you-need-to-know-about-change-detection-in-angular-8006c51d206f). Ce processus se produit constamment dans l'arborescence des composants. Il recherche les changements de données qui méritent un nouveau rendu du modèle.

Il est temps de passer à autre chose. Veuillez vous référer aux articles mentionnés précédemment pour plus d'informations sur le cycle de vie des composants. Cela mérite beaucoup plus d'explications.

#### **Données du composant**

Les données pilotent tout. Les composants ne font pas exception. Les composants encapsulent toutes leurs données. Pour recevoir des données externes, un composant doit les déclarer explicitement. Cette forme de confidentialité empêche les informations de s'entrechoquer dans l'arborescence des composants.

Les données déterminent ce qui est affiché de la classe du composant à son modèle. Toute mise à jour des données de la classe mettra à jour (ou devrait le faire) l'affichage du modèle.

Les composants initialiseront souvent un ensemble de membres (ou variables) qui stockent des données. Ils sont utilisés dans toute la logique de la classe du composant pour plus de commodité. Ces informations alimentent la logique résultant dans le modèle et son comportement. Voir l'exemple suivant.

```typescript
// ./components/example/example.component.ts

import { Component, OnInit } from '@angular/core';
import { Post, DATA } from '../../data/posts.data';

@Component({
  selector: 'app-example',
  templateUrl: './example.component.html'
})
export class ExampleComponent implements OnInit {
  username: string;
  totalPosts: number;
  allPosts: Post[];

  deletePost(index: number): void {
    this.allPosts.splice(index, 1);
    this.totalPosts = this.allPosts.length;
  }

  ngOnInit(): void {
    this.username = DATA.author;
    this.totalPosts = DATA.thePosts.length;
    this.allPosts = DATA.thePosts;
  }
}
```

```html
<!-- ./components/example/example.component.html -->

<h1>{{ username }}</h1>
<span>Changer le nom : </span><input [(ngModel)]="username">
<h3>Posts : {{ totalPosts }}</h3>
<ul>
<hr/>
<div *ngFor="let post of allPosts; let i=index">
  <button (click)="deletePost(i)">SUPPRIMER</button>
  <h6>{{ post.title }}</h6>
  <p>{{ post.body }}</p>
  <hr/>
</div>
</ul>
```

Notez les façons dont le composant interagit avec ses données. Il les récupère d'abord depuis `../../data/posts.data` avant de commencer à les transmettre au modèle pour affichage.

Les données apparaissent dans tout le modèle. À l'intérieur des doubles accolades, la valeur d'une variable est mappée de la classe du composant dans les accolades. La boucle `*ngFor` parcourt le tableau de classe `allPosts`. Cliquer sur le bouton supprime un élément spécifique de `allPosts` par son index. Vous pouvez même changer le `username` le plus haut en tapant dans la boîte d'entrée.

Les interactions ci-dessus modifient les données de la classe du composant, ce qui met à jour le modèle HTML du composant. Les composants fournissent la logique de base qui facilite le flux de données. Le modèle HTML rend ces données lisibles pour l'utilisateur.

#### **Modèle de composant**

Le modèle HTML de l'exemple précédent présentait une syntaxe intéressante. La syntaxe n'était pas du HTML réel. C'était le HTML de modèle d'Angular. Certains l'appellent souvent HTML _Plus_, reconnaissable uniquement par le compilateur d'Angular. Le compilateur supporte une syntaxe résultant en la manipulation dynamique du HTML. Cet article l'appellera souvent HTML de modèle ou modèle.

La syntaxe permet aux composants d'injecter des données directement dans le HTML de modèle. L'injection est dynamique. Cela signifie que les données peuvent itérer et s'afficher en tant que HTML sans avoir besoin d'assistance externe. Le compilateur Angular le compile en HTML réel au moment où il atteint le navigateur web.

Pour en savoir plus sur certaines des façons dont les données se lient au modèle, lisez à propos de la [liaison de données dans Angular](https://guide.freecodecamp.org/angular/data-binding). Quelques exemples de liaison de données se sont produits dans l'exemple précédent (`{{ ... }}`). Pour cet article, il suffit de reconnaître que des interactions de données se produisaient entre la classe du composant et son modèle.

#### **Interrogation du modèle**

La gestion des données de l'état du modèle de manière impérative fonctionne correctement. Pourtant, les données pures ne remplissent pas toujours le design prévu d'une application. Interagir plus directement avec le Document Object Model (DOM) peut être nécessaire.

Pour ce faire, le composant doit avoir une référence aux éléments du modèle. Lorsque les données changent, le composant peut manipuler le DOM explicitement. C'est une approche plus déclarative.

Les composants peuvent obtenir des références en utilisant l'interface de programmation d'application (API) DOM du navigateur web. Mauvaise idée cependant. Angular préfère la compatibilité multiplateforme. Pour qu'un composant fonctionne en dehors du navigateur web, il doit utiliser l'API d'Angular au lieu de celle du DOM.

Les composants peuvent interroger leurs modèles en utilisant les décorateurs `@ViewChild` et `ContentChild`. Ils obtiennent des références aux éléments du modèle au nom de la classe du composant.

```typescript
import { Component, ViewChild, ContentChild, ElementRef, Renderer2, AfterContentChecked, AfterViewChecked } from '@angular/core';

@Component({
  selector: 'app-child',
  template: `
  <button (click)="toggleEnlarge()">Basculer Agrandir</button>
  <ng-content></ng-content>
  `
})
export class ChildComponent implements AfterContentChecked {
  @ContentChild("pReference", { read: ElementRef }) pElement: ElementRef;
  textEnlarge: boolean = false;

  constructor(private renderer: Renderer2) { }

  toggleEnlarge() {
    this.textEnlarge = !this.textEnlarge;
  }

  ngAfterContentChecked() {
    if (this.textEnlarge)
      this.renderer.setStyle(this.pElement.nativeElement, 'font-size', '25px');
      else
      this.renderer.setStyle(this.pElement.nativeElement, 'font-size', 'initial');
    }
}

@Component({
  selector: 'app-parent',
  template: `
  <button (click)="toggleHighlight()">Basculer Surligner</button>
  <h1 #hOneRefereance>View Child</h1>
  <app-child>
    <p #pReference>Content Child</p>
  </app-child>
  `
})
export class ParentComponent implements AfterViewChecked {
  @ViewChild("hOneRefereance", { read: ElementRef }) hOneElement: ElementRef;
  textHighlight: boolean = false;

  constructor(private renderer: Renderer2) { }

  toggleHighlight() {
    this.textHighlight = !this.textHighlight;
  }

  ngAfterViewChecked() {
    if (this.textHighlight)
      this.renderer.setStyle(this.hOneElement.nativeElement, 'background-color', 'yellow');
    else
      this.renderer.setStyle(this.hOneElement.nativeElement, 'background-color', 'initial');
  }
}
```

L'exemple ci-dessus contient deux boutons qui basculent un certain style pour chaque élément. Cliquer sur les boutons bascule les valeurs vrai/faux uniques à chaque composant. Ces booléens déterminent si les styles personnalisés s'appliquent. Au lieu que ces valeurs provoquent des changements de manière impérative, les hooks de cycle de vie (`ngAfterViewChecked` et `ngAfterContentChecked`) modifient le DOM de manière déclarative.

L'approche déclarative change explicitement le style via la référence de l'élément. En programmation impérative, les changements du DOM basés sur les données sont implicites. Consultez cet article sur la [programmation impérative et déclarative](https://codeburst.io/declarative-vs-imperative-programming-a8a7c93d9ad2) pour en savoir plus.

La chose principale à remarquer est la façon dont ces références sont extraites du modèle. Dans l'exemple, il y a deux sections du modèle interrogées en utilisant deux décorateurs : `@ViewChild` et `@ContentChild`.

Ils diffèrent dans l'endroit où ils recherchent une référence d'élément, qu'il s'agisse dans le DOM de contenu ou le DOM de vue. Ces deux DOM existent dans le modèle de ParentComponent. Les différencier est important car ils finissent de se rendre à des moments séparés.

C'est pourquoi `@ViewChild` et `@ContentChild` existent tous les deux. Ils fonctionnent ensemble avec leurs hooks de cycle de vie compagnons `ngAfterViewChecked` et `ngAfterContentChecked`. Ces hooks de cycle de vie attendent que leurs requêtes respectives se résolvent avant de s'exécuter.

Une fois résolus, `@ViewChild` et `@ContentChild` fournissent des références à deux éléments. Tous deux existent dans des parties séparées du DOM. Les données booléennes déterminent toujours le résultat. La manière dont ce résultat se traduit dans le DOM est la différence clé par rapport à avant. Le DOM est mis à jour via la manipulation directe de `Renderer2`.

#### **Projection de contenu**

Le DOM de contenu existe dans le innerHTML de l'élément `<app-child></app-child>` de ChildComponent. Il est tout positionné dans le modèle de ParentComponent. Le innerHTML de `app-child` se _projette_ sur le modèle de ChildComponent via `<ng-content></ng-content>`.

Cela exemplifie la projection de contenu. Afficher le contenu d'un composant à un autre en utilisant le innerHTML des balises d'un autre dans le modèle d'un composant afin que l'autre composant puisse extraire ce innerHTML dans son propre modèle via `<ng-content></ng-content>`. _Merci d'avoir lu cette phrase._

D'où ChildComponent référence son élément `<p></p>` en utilisant `@ContentChild`. Le contenu contenu dans `<app-child></app-child>` dans le modèle de ParentComponent constitue le DOM de contenu. ChildComponent référence l'élément avec une requête `@ContentChild`.

Le DOM de vue de ParentComponent se compose de tout ce qui est accessible depuis la vue du composant. Cela n'inclut pas nécessairement tout le modèle étant donné le innerHTML de `<app-child></app-child>`. Encore une fois, cette partie du DOM est interrogée depuis ChildComponent en utilisant `@ContentChild`. Tout le reste est interrogé en utilisant `@ViewChild` depuis la classe ParentComponent.

C'est un excellent moyen pour les composants d'échanger du contenu et d'interroger leur propre contenu indépendamment de leur type de DOM. Les composants peuvent communiquer entre eux et avec d'autres en utilisant la liaison de données. Lisez-en plus à ce sujet dans [cet article](https://guide.freecodecamp.org/angular/data-binding).

#### **Styles des composants**

Les styles sont cruciaux pour la lisibilité et l'interactivité d'un composant. Chaque composant encapsule ses dépendances de feuilles de style. Ainsi, ils ne s'appliquent qu'au modèle HTML du composant. Une technique spéciale introduite par le shadow DOM de HTML rend cela possible.

Une branche de shadow DOM peut exister sur n'importe quel élément. Cette partie du DOM ne peut pas être vue depuis le code source du HTML. Les éléments HTML standard exploitent le shadow DOM pour fournir leurs apparences caractéristiques. Une branche de shadow DOM doit s'ancrer à un composant visible afin qu'elle puisse le styliser et le personnaliser.

L'aspect unique d'une branche de shadow DOM est son encapsulation. Tout ce qui est utilisé pour styliser l'élément racine d'une branche de shadow DOM lui est privé. Aucun autre élément ne peut y accéder.

Angular adopte cette forme d'encapsulation avec les composants. La feuille de style et le modèle d'un composant s'encapsulent ensemble. Aucun autre composant n'a accès à eux. Les conflits de feuilles de style ne peuvent pas se produire.

Angular n'utilise pas le shadow DOM par défaut. Il utilise un système d'émulation qui imite le comportement du shadow DOM. C'est une mesure temporaire puisque certains navigateurs web ne supportent pas encore l'API du shadow DOM.

Les métadonnées `@Component` contiennent le champ `encapsulation`. Cela permet aux développeurs de basculer entre le shadow DOM émulé, le shadow DOM réel ou aucun. Voici les options dans leur ordre respectif :

* `ViewEncapsulation.Emulated` - faux shadow DOM (par défaut)
* `ViewEncapsulation.Native` - vrai shadow DOM (maintenant obsolète depuis Angular 6.0.8)
* `ViewEncapsulation.None` - aucun

`ViewEncapsulation.None` signifie que les feuilles de style du composant sont élevées à la portée globale. Non recommandé étant donné que les composants devraient former leur propre unité privée (encapsulation). Angular le fournit toujours comme une issue de secours pour les situations extrêmes.

#### **Conclusion**

Les composants construisent des applications. Ils sont privés et uniformément séparés les uns des autres, sauf configuration contraire. Les applications tendent à commencer à partir du module racine. Passé cela, les composants forment un arbre allongé définissant le reste de l'application.

Un composant couvre une unité désignée de l'interface de l'application. Cela inclut ses styles, sa logique et sa disposition. D'autres schematics tels que les pipes, les services et les directives sont fréquemment utilisés dans le code des composants. Vous pouvez en apprendre plus sur ces interactions dans certains des autres articles de guide Angular.

N'oubliez pas que les composants doivent [démarrer](https://angular.io/guide/bootstrapping). Cela peut se produire dans le module racine ou les métadonnées du composant. Ainsi, Angular reconnaît le composant où qu'il apparaisse dans l'application.

Vous pouvez toujours en apprendre plus, car les composants portent bien plus de profondeur que ce que cet article pourrait transmettre.
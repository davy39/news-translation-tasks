---
title: Comment utiliser l'animation avec Angular 6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-04T17:40:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-animation-with-angular-6-675b19bc3496
coverImage: https://cdn-media-1.freecodecamp.org/images/1*apXhEl5f3wwTKH4fQYMExA.jpeg
tags:
- name: Angular
  slug: angularjs
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment utiliser l'animation avec Angular 6
seo_desc: 'By Ankit Sharma

  Introduction

  Animation is defined as the transition from an initial state to a final state. It
  is an integral part of any modern web application. Animation not only helps us create
  a great UI but it also makes the application interest...'
---

Par Ankit Sharma

### Introduction

L'animation est définie comme la transition d'un état initial à un état final. C'est une partie intégrante de toute application web moderne. L'animation nous aide non seulement à créer une excellente interface utilisateur, mais elle rend également l'application intéressante et amusante à utiliser. Une animation bien structurée maintient l'utilisateur engagé avec l'application et améliore l'expérience utilisateur.

Angular nous permet de créer des animations qui offrent des performances natives similaires aux animations CSS. Dans cet article, nous allons apprendre comment créer des animations en utilisant Angular 6.

Nous utiliserons Visual Studio Code pour notre démonstration.

### Prérequis

Installez VS Code et Angular CLI.

Si vous êtes nouveau dans Angular, consultez mon article précédent [Getting Started With Angular 6.0](http://ankitsharmablogs.com/getting-started-with-angular-6-0/) pour configurer l'environnement de développement Angular 6 sur votre machine.

### Code Source

Téléchargez le code source depuis [GitHub](https://github.com/AnkitSharma-007/angular-6-animations).

### Comprendre les États d'Animation Angular

L'animation implique la transition d'un état d'un élément à un autre état. Angular définit trois états différents pour un élément :

1. État Void — représente l'état d'un élément qui ne fait pas partie du DOM. Cet état se produit lorsqu'un élément est créé mais pas encore placé dans le DOM ou lorsque l'élément est supprimé du DOM. Cet état est utile lorsque nous voulons créer une animation lors de l'ajout ou de la suppression d'un élément de notre DOM. Pour définir cet état dans notre code, nous utilisons le mot-clé `void`.
2. État générique — C'est aussi connu comme l'état par défaut de l'élément. Les styles définis pour cet état sont applicables à l'élément indépendamment de son état d'animation actuel. Pour définir cet état dans notre code, nous utilisons le symbole `*`.
3. État personnalisé — C'est l'état personnalisé de l'élément et il doit être défini explicitement dans le code. Pour définir cet état dans notre code, nous pouvons utiliser n'importe quel nom personnalisé de notre choix.

### Timing de Transition d'Animation

Pour montrer la transition d'animation d'un état à un autre, nous définissons le timing de transition d'animation dans notre application.

Angular fournit les trois propriétés de timing suivantes :

#### Durée

Cette propriété représente le temps que notre animation prend pour se compléter du début (état initial) à la fin (état final). Nous pouvons définir la durée de l'animation de trois manières suivantes :

* Utiliser une valeur entière pour représenter le temps en millisecondes. Ex. : 500
* Utiliser une valeur de chaîne pour représenter le temps en millisecondes. Ex. : '500ms'
* Utiliser une valeur de chaîne pour représenter le temps en secondes. Ex. : '0.5s'

#### Délai

Cette propriété représente la durée entre le déclencheur de l'animation et le début de la transition réelle. Cette propriété suit également la même syntaxe que la durée. Pour définir le délai, nous devons ajouter la valeur de délai après la valeur de durée dans un format de chaîne — 'Durée Délai'. Le délai est une propriété facultative.

Par exemple :

* '0.3s 500ms'. Cela signifie que la transition attendra 500ms puis s'exécutera pendant 0.3s.

#### Easing

Cette propriété représente comment l'animation accélère ou décélère pendant son exécution. Nous pouvons définir l'easing en l'ajoutant comme troisième variable dans la chaîne après la durée et le délai. Si la valeur de délai n'est pas présente, alors l'easing sera la deuxième valeur. C'est également une propriété facultative.

Par exemple :

* '0.3s 500ms ease-in' — Cela signifie que la transition attendra 500ms puis s'exécutera pendant 0.3s (300ms) avec un effet ease-in.
* '300ms ease-out'. — Cela signifie que la transition s'exécutera pendant 300ms (0.3s) avec un effet ease-out.

### Création de l'application Angular 6

Ouvrez l'invite de commande sur votre machine et exécutez la série de commandes suivante :

* mkdir ngAnimationDemo
* cd ngAnimationDemo
* ng new ngAnimation

Ces commandes créeront un répertoire avec le nom `ngAnimationDemo` puis créeront une application Angular avec le nom `ngAnimation` à l'intérieur de ce répertoire.

Ouvrez l'application ngAnimation en utilisant VS Code. Maintenant, nous allons créer notre composant.

Accédez à `View >> Integrated Terminal`. Cela ouvrira une fenêtre de terminal dans VS Code.

Exécutez la commande suivante pour créer le composant.

```bash
ng g c animationdemo
```

Cela créera notre composant `animationdemo` à l'intérieur du dossier `/src/app`.

Pour utiliser l'animation Angular, nous devons importer `BrowserAnimationsModule` qui est un module spécifique aux animations dans notre application. Ouvrez le fichier app.module.ts et incluez la définition d'importation comme montré ci-dessous :

```ts
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
// autres définitions d'importation

@NgModule({ imports: [BrowserAnimationsModule // autres imports]})
```

#### **Comprendre la Syntaxe d'Animation Angular**

Nous allons écrire notre code d'animation à l'intérieur des métadonnées du composant. La syntaxe pour l'animation est montrée ci-dessous :

```ts
@Component({
// autres propriétés du composant.
  animations: [
    trigger('triggerName'), [
      state('stateName', style())
      transition('stateChangeExpression', [Animation Steps])
    ]
  ]
})
```

Ici, nous allons utiliser une propriété appelée `animations`. Cette propriété prendra un tableau en entrée. Le tableau contient un ou plusieurs « triggers ». Chaque trigger a un nom unique et une implémentation. Les états et transitions pour notre animation doivent être définis dans l'implémentation du trigger.

Chaque fonction d'état a un « stateName » défini pour identifier de manière unique l'état et une fonction de style pour montrer le style de l'élément dans cet état.

Chaque fonction de transition a une `stateChangeExpression` définie pour montrer le changement d'état de l'élément et le tableau correspondant des étapes d'animation pour montrer comment la transition aura lieu. Nous pouvons inclure plusieurs fonctions de trigger à l'intérieur de la propriété d'animation sous forme de valeurs séparées par des virgules.

Ces fonctions trigger, et state et transition sont définies dans le module `@angular/animations`. Par conséquent, nous devons importer ce module dans notre composant.

Pour appliquer une animation sur un élément, nous devons inclure le nom du trigger dans la définition de l'élément. Incluez le nom du trigger suivi du symbole `@` dans la balise de l'élément. Reportez-vous au code exemple ci-dessous :

```ts
<div @changeSize></div>
```

Cela appliquera le trigger `changeSize` à l'élément `<div>`.

Créons quelques animations pour mieux comprendre les concepts d'animation Angular.

### Animation de Changement de Taille

Nous allons créer une animation pour changer la taille d'un élément `<div>` lors d'un clic sur un bouton.

Ouvrez le fichier `animationdemo.component.ts` et ajoutez la définition d'importation suivante :

```
import { trigger, state, style, animate, transition } from '@angular/animations';
```

Ajoutez la définition de propriété d'animation suivante dans les métadonnées du composant :

```ts
animations: [
  trigger('changeDivSize', [
    state('initial', style({
      backgroundColor: 'green',
      width: '100px',
      height: '100px'
    })),
    state('final', style({
      backgroundColor: 'red',
      width: '200px',
      height: '200px'
    })),
    transition('initial=>final', animate('1500ms')),
    transition('final=>initial', animate('1000ms'))
  ]),
]
```

Ici, nous avons défini un trigger `changeDivSize` et deux fonctions d'état à l'intérieur du trigger. L'élément sera vert dans l'état « initial » et sera rouge avec une largeur et une hauteur augmentées dans l'état « final ».

Nous avons défini des transitions pour le changement d'état. La transition de l'état « initial » à l'état « final » prendra 1500ms et de l'état « final » à l'état « initial » prendra 1000ms.

Pour changer l'état de notre élément, nous allons définir une fonction dans la définition de classe de notre composant. Incluez le code suivant dans la classe `AnimationdemoComponent` :

```ts
currentState = 'initial';

changeState() {
  this.currentState = this.currentState === 'initial' ? 'final' : 'initial';
}
```

Ici, nous avons défini une méthode `changeState` qui basculera l'état de l'élément.

Ouvrez le fichier `animationdemo.component.html` et ajoutez le code suivant :

```ts
<h3>Changer la taille de la div</h3>
<button (click)="changeState()">Changer la Taille</button>
<br />
<div [@changeDivSize]=currentState></div>
<br />
```

Nous avons défini un bouton qui invoquera la fonction `changeState` lorsqu'il sera cliqué. Nous avons défini un élément `<div>` et appliqué le trigger d'animation `changeDivSize`. Lorsque nous cliquons sur le bouton, il basculera l'état de l'élément `<div>` et sa taille changera avec un effet de transition.

Avant d'exécuter l'application, nous devons inclure la référence à notre composant `Animationdemo` à l'intérieur du fichier `app.component.html`.

Ouvrez le fichier `app.component.html`. Vous pouvez voir que nous avons du code HTML par défaut dans ce fichier. Supprimez tout le code et mettez le sélecteur de notre composant comme montré ci-dessous :

```ts
<app-animationdemo></app-animationdemo>
```

Pour exécuter le code, lancez la commande `ng serve` dans la fenêtre de terminal de VS Code. Après avoir exécuté cette commande, il demandera d'ouvrir `http://localhost:4200` dans le navigateur. Ouvrez donc un navigateur sur votre machine et accédez à cette URL. Vous pouvez voir une page web comme montré ci-dessous. Cliquez sur le bouton pour voir l'animation.

![Image](https://cdn-media-1.freecodecamp.org/images/aeLhzRqHdU1Gub7GL3WOvtgno7fMuRnwuy4H)
_Changer la taille de la div en utilisant l'animation Angular_

### Animation d'effet Ballon

Dans l'animation précédente, la transition s'est produite dans deux directions. Dans cette section, nous allons apprendre à changer la taille dans toutes les directions. Cela sera similaire à gonfler et dégonfler un ballon, d'où le nom d'animation d'effet ballon.

Ajoutez la définition de trigger suivante dans la propriété d'animation :

```ts
trigger('balloonEffect', [
   state('initial', style({
     backgroundColor: 'green',
     transform: 'scale(1)'
   })),
   state('final', style({
     backgroundColor: 'red',
     transform: 'scale(1.5)'
   })),
   transition('final=>initial', animate('1000ms')),
   transition('initial=>final', animate('1500ms'))
 ]),
```

Ici, au lieu de définir les propriétés de largeur et de hauteur, nous utilisons la propriété de transformation pour changer la taille dans toutes les directions. La transition se produira lorsque l'état de l'élément changera.

Ajoutez le code HTML suivant dans le fichier `app.component.html` :

```ts
<h3>Effet Ballon</h3>
<div (click)="changeState()" 
  style="width:100px;height:100px; border-radius: 100%; margin: 3rem; background-color: green"
  [@balloonEffect]=currentState>
</div>
```

Ici, nous avons défini une div et appliqué le style CSS pour en faire un cercle. Cliquer sur la div invoquera la méthode `changeState` pour basculer l'état de l'élément.

Ouvrez le navigateur pour voir l'animation en action comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/O8B90gJ8NVLnCmA1WStQAlqxeRUHnertm6G6)
_Animation d'effet ballon en utilisant Angular 6_

### Animation de Fondu Entrant et Sortant

Parfois, nous voulons montrer une animation lors de l'ajout ou de la suppression d'un élément du DOM. Nous allons voir comment animer l'ajout et la suppression d'un élément à une liste avec un effet de fondu entrant et sortant.

Ajoutez le code suivant à l'intérieur de la définition de classe `AnimationdemoComponent` pour ajouter et supprimer l'élément dans une liste :

```ts
listItem = [];
list_order: number = 1;

addItem() {
  var listitem = "ListItem " + this.list_order;
  this.list_order++;
  this.listItem.push(listitem);
}
removeItem() {
  this.listItem.length -= 1;
}
```

Ajoutez la définition de trigger suivante dans la propriété d'animation :

```ts
trigger('fadeInOut', [
  state('void', style({
    opacity: 0
  })),
  transition('void <=> *', animate(1000)),
]),
```

Ici, nous avons défini le trigger `fadeInOut`. Lorsque l'élément est ajouté au DOM, c'est une transition de void à l'état générique (*). Cela est noté en utilisant `void => *`. Lorsque l'élément est supprimé du DOM, c'est une transition de l'état générique (*) à void. Cela est noté en utilisant `* => void`.

Lorsque nous utilisons le même timing d'animation pour les deux directions de l'animation, nous utilisons la syntaxe abrégée `<=>`. Comme défini dans ce trigger, l'animation `from void => *` et `* => void` prendra 1000ms pour se compléter.

Ajoutez le code HTML suivant dans le fichier app.component.html.

```ts
<h3>Animation de Fondu Entrant et Sortant</h3>

<button (click)="addItem()">Ajouter à la Liste</button>
<button (click)="removeItem()">Retirer de la Liste</button>

<div style="width:200px; margin-left: 20px">
  <ul>
    <li *ngFor="let list of listItem" [@fadeInOut]>
      {{list}}
    </li>
  </ul>
</div>
```

Ici, nous définissons deux boutons pour ajouter des éléments à la liste et les en retirer. Nous liaisons le trigger fadeInOut à l'élément `<li>`, ce qui montrera un effet de fondu entrant et sortant lors de l'ajout et de la suppression du DOM.

Ouvrez le navigateur pour voir l'animation en action comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/BbxpG-Sr4LlqQChVrxZtdRezMHifTwwM3-M3)
_Animation de fondu entrant et sortant en utilisant Angular 6_

### Animation d'Entrée et de Sortie

Lors de l'ajout au DOM, l'élément entrera sur l'écran depuis la gauche. Lors de la suppression, l'élément quittera l'écran depuis la droite.

La transition de `void => *` et `* => void` est très courante. Par conséquent, Angular fournit des alias pour ces animations :

* pour void => * nous pouvons utiliser ':enter'
* pour * => void nous pouvons utiliser ':leave'

Les alias rendent ces transitions plus lisibles et plus faciles à comprendre.

Ajoutez la définition de trigger suivante dans la propriété d'animation :

```ts
trigger('EnterLeave', [
  state('flyIn', style({ transform: 'translateX(0)' })),
  transition(':enter', [
    style({ transform: 'translateX(-100%)' }),
    animate('0.5s 300ms ease-in')
  ]),
  transition(':leave', [
    animate('0.3s ease-out', style({ transform: 'translateX(100%)' }))
  ])
])
```

Ici, nous avons défini le trigger `EnterLeave`. La transition ':enter' attendra 300ms puis s'exécutera pendant 0.5s avec un effet ease-in. Alors que la transition ':leave' s'exécutera pendant 0.3s avec un effet ease-out.

Ajoutez le code HTML suivant dans le fichier `app.component.html` :

```ts
<h3>Animation d'Entrée et de Sortie</h3>

<button (click)="addItem()">Ajouter à la Liste</button>
<button (click)="removeItem()">Retirer de la Liste</button>

<div style="width:200px; margin-left: 20px">
  <ul>
    <li *ngFor="let list of listItem" [@EnterLeave]="'flyIn'">
      {{list}}
    </li>
  </ul>
</div>
```

Ici, nous définissons deux boutons pour ajouter des éléments à la liste et les en retirer. Nous liaisons le trigger `EnterLeave` à l'élément `<li>` qui montrera l'effet d'entrée et de sortie lors de l'ajout et de la suppression du DOM.

Ouvrez le navigateur pour voir l'animation en action comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/iy70cW0uBOkKv9iGxVGf7xrxjvuVlywgzlsQ)
_Animation d'entrée et de sortie en utilisant Angular 6_

### Conclusion

Dans cet article, nous avons appris les animations Angular 6. Nous avons exploré le concept des états et transitions d'animation. Nous avons également vu quelques animations en action à l'aide d'une application exemple.

Veuillez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/angular-6-animations) et jouez avec pour mieux comprendre.

Si vous préparez des entretiens, lisez mon article sur [C# Coding Questions For Technical Interviews](http://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/).

### Voir Aussi

* [ASP.NET Core — Using Highcharts With Angular 5](http://ankitsharmablogs.com/asp-net-core-using-highcharts-with-angular-5/)
* [ASP.NET Core — CRUD Using Angular 5 And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [CRUD Operations With ASP.NET Core Using Angular 5 And ADO.NET](http://ankitsharmablogs.com/crud-operations-asp-net-core-using-angular-5-ado-net/)
* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [CRUD Using Blazor with MongoDB](http://ankitsharmablogs.com/crud-using-blazor-with-mongodb/)
* [Creating An SPA Using Razor Pages With Blazor](http://ankitsharmablogs.com/creating-a-spa-using-razor-pages-with-blazor/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)
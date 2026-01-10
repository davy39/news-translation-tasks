---
title: Les meilleurs exemples Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-30T00:25:00.000Z'
originalURL: https://freecodecamp.org/news/the-best-angular-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/angular-examples.jpeg
tags:
- name: Angular
  slug: angular
seo_title: Les meilleurs exemples Angular
seo_desc: Angular is a TypeScript-based open source framework used to develop frontend
  web applications. It is the successor of AngularJS and all mentions of Angular refer
  to versions 2 and up. Angular has features like generics, static-typing, and also
  some E...
---

Angular est un framework open source basé sur TypeScript utilisé pour développer des applications web frontend. Il est le successeur d'AngularJS et toutes les mentions d'Angular font référence aux versions 2 et supérieures. Angular possède des fonctionnalités comme les génériques, le typage statique, et aussi certaines fonctionnalités ES6.

## Historique des versions

Google a publié la version initiale d'AngularJS le 20 octobre 2010. La version stable d'AngularJS était la version 1.6.8, publiée le 18 décembre 2017. La dernière version significative d'AngularJS, la version 1.7, a été publiée le 1er juillet 2018, et est actuellement en période de support à long terme de 3 ans. Angular 2.0 a été annoncé pour la première fois le 22 septembre 2014, lors de la conférence ng-Europe. Une nouvelle fonctionnalité d'Angular 2.0 est le chargement dynamique, et la plupart des fonctionnalités principales ont été déplacées vers des modules.

Après quelques modifications, Angular 4.0 a été publié en décembre 2016. Angular 4 est rétrocompatible avec Angular 2.0, et certaines nouvelles fonctionnalités sont la bibliothèque HttpClient et les nouveaux événements du cycle de vie du routeur. Angular 5 est sorti le 1er novembre 2017, dont une fonctionnalité majeure est le support des applications web progressives. Angular 6 est sorti en mai 2018, et Angular 7 en octobre 2018. La dernière version stable est [7.0.0](https://angular.io/guide/releases).

## Installation

La manière la plus simple d'installer Angular est via [Angular CLI](https://cli.angular.io/). Cet outil permet la création de nouveaux projets et la génération de composants, services, modules, etc., selon les meilleures pratiques que l'équipe Angular considère comme standards.

### Angular 2.x et versions supérieures

#### Installer Angular CLI

```shell
npm install -g @angular/cli
```

#### Créer un espace de travail et une application initiale

Vous développez des applications dans le contexte d'un espace de travail Angular. Un espace de travail contient les fichiers pour un ou plusieurs projets. Un projet est l'ensemble des fichiers qui composent une application, une bibliothèque, ou des tests de bout en bout (e2e).

```shell
ng new my-app
```

#### Servir l'application

Angular inclut un serveur afin que vous puissiez facilement construire et servir votre application localement.

1. Naviguez vers le dossier de l'espace de travail (`my-app`)

Lancez le serveur en utilisant la commande CLI `ng serve` avec l'option `--open`

```shell
cd my-app
ng serve --open
```

Hourra, vous avez créé votre première application Angular !!!

# Composants

Angular contient de nombreux _schematics_ pour construire des applications. Les composants sont l'un de ces schematics. Ils englobent une seule unité de logique concernée par une seule partie de l'application. Les composants s'associent souvent avec d'autres schematics pour fonctionner plus efficacement.

Les composants simplifient l'application. Canaliser la logique dans une seule section de l'interface visible est leur objectif principal. Pour construire des applications étape par étape, vous devez construire composant par composant. Les composants agissent après tout comme les blocs de construction d'Angular.

### Classe de composant et métadonnées

La commande CLI `ng generate component [nom-du-composant]` produit ce qui suit.

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

* `selector:` indique à Angular d'associer le composant à un certain élément dans le template HTML de l'application.
* `templateUrl:` accepte l'emplacement du fichier du template HTML du composant (c'est là que les données sont affichées).
* `styleUrls:` accepte un tableau d'emplacements de fichiers de feuilles de style (chaînes). Ces feuilles de style ciblent le template assigné au composant.

Considérez les métadonnées comme un gros bloc de configuration. Le décorateur les prend afin qu'il puisse générer les données spécifiques au composant. Le décorateur _décore_ la classe sous-jacente avec les données nécessaires à son comportement de classe. Une classe de _composant_ en l'occurrence.

La signature de la classe est exportée par défaut afin que le composant puisse être importé. `ngOnInit` est également implémenté. `implements` indique à la classe de définir certaines méthodes selon la définition de l'interface. `ngOnInit` est un hook de cycle de vie.

### Données du composant

Les données pilotent tout. Les composants ne font pas exception. Les composants encapsulent toutes leurs données. Pour recevoir des données externes, un composant doit les déclarer explicitement. Cette forme de confidentialité empêche les informations de se heurter à travers l'arborescence des composants.

Les données déterminent ce qui est affiché de la classe du composant à son template. Toute mise à jour des données de la classe (ou au moins devrait) met à jour l'affichage du template.

Les composants initialisent souvent un ensemble de membres (ou variables) qui stockent des données. Ils sont utilisés dans toute la logique de la classe du composant pour plus de commodité. Ces informations alimentent la logique résultant du template et de son comportement. Voir l'exemple suivant.

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

Notez les façons dont le composant interagit avec ses données. Il les récupère d'abord depuis `../../data/posts.data` avant de commencer à les transmettre au template pour affichage.

Les données apparaissent partout dans le template. À l'intérieur des doubles accolades, la valeur d'une variable est mappée de la classe du composant dans les accolades. La boucle `*ngFor` parcourt le tableau de classe `allPosts`. Cliquer sur le bouton supprime un élément spécifique de `allPosts` par son index. Vous pouvez même changer le `username` en haut en tapant dans la boîte d'entrée.

Les interactions ci-dessus modifient les données de la classe du composant qui, à leur tour, mettent à jour le template HTML du composant. Les composants fournissent la logique de base qui facilite le flux de données. Le template HTML rend ces données lisibles pour l'utilisateur.

## Liaison de données

Les données définissent souvent l'apparence d'une application. Interpréter ces données dans l'interface utilisateur implique la logique de classe (`*.component.ts`) et une vue de template (`*.component.html`). Angular les connecte via la liaison de données. Considérez la liaison de données comme un outil pour l'interaction des composants.

### Composant et Template

Le composant stocke la plupart de sa logique et de ses données à l'intérieur de sa classe décorée avec `@Component`. Ce décorateur définit la classe comme un composant avec un template HTML. Le template du composant représente la classe au sein de l'application. L'accent ici doit être mis entre la classe du composant et le template HTML.

C'est là que la liaison de données se produit. Les propriétés et événements des éléments reçoivent des valeurs. Ces valeurs, définies par la classe du composant, servent l'un des deux rôles. L'un est de produire des données que le template reçoit ensuite. L'autre gère les événements émis par l'élément du template.

![Exemple de Code](https://raw.githubusercontent.com/sosmaniac-FCC/designatedata/master/image4.png)

### Propriétés des éléments

Pour reconnaître les propriétés des éléments liées aux données, Angular utilise une syntaxe de crochets spéciale.

```typescript
// my.component.ts
@Component({
  templateUrl: './my.component.html'
})

export class MyComponent {
  value:type = /* une valeur de type */;
}
```

```html
<!-- my.component.html -->
<any-element [property]="value">innerHTML</any-element>
```

Suivez-moi sur ce point.

`[property]` reflète la propriété dans le nœud d'objet du modèle d'objet de document (DOM) de l'élément. Ne confondez pas les propriétés d'objet avec les attributs d'un élément DOM. Les propriétés et les attributs partagent souvent le même nom et font la même chose. Il y a cependant une distinction claire.

Rappelez-vous que `attr` (attributs) est une seule propriété de l'objet DOM sous-jacent. Il est déclaré à l'instantiation du DOM avec des valeurs d'attributs correspondant à la définition de l'élément. Il conserve la même valeur après cela. Les propriétés ont chacune leur propre champ clé-valeur dans un nœud d'objet DOM. Ces propriétés sont mutables après l'instantiation.

Connaître la différence entre les attributs et les propriétés. Cela conduira à une meilleure compréhension de la manière dont Angular lie les données aux propriétés (liaison de propriétés). Angular ne lie presque jamais les données aux attributs d'un élément. Les exceptions à cela sont très rares. Une dernière fois : Angular lie les données du composant aux propriétés, pas aux attributs !

En revenant à l'exemple, les `[ … ]` dans l'assignation de propriété de l'élément ont une signification spéciale. Les crochets montrent que `property` est lié à `«value»` à droite de l'assignation.

`value` a également une signification spéciale dans le contexte des crochets. `value` seul est une chaîne littérale. Angular la lit et fait correspondre sa valeur aux membres de la classe du composant. Angular substituera la valeur de l'attribut membre correspondant. Cela fait bien sûr référence à la même classe de composant qui héberge le template HTML.

Le flux unidirectionnel des données du composant vers le template est complet. Le membre correspondant à l'assignation droite de la propriété entre crochets fournit la `value`. Notez que les changements de la valeur du membre dans la classe du composant se répercutent jusqu'au template. C'est la détection des changements d'Angular en action. Les changements dans la portée du template n'ont aucun effet sur le membre de la classe du composant.

Point clé à retenir : la classe du composant fournit les données tandis que le template les affiche.

J'ai oublié de mentionner que les valeurs de données peuvent également apparaître dans le `innerHTML` d'un composant. Ce dernier exemple implémente des doubles accolades. Angular reconnaît ces accolades et interpolate les données de la classe du composant correspondantes dans le `innerHTML` de la `div`.

```html
<div>La valeur du membre de la classe du composant 'value' est {{value}}.</div>
```

### Gestion des événements

Si le composant fournit des données, alors le template fournit des événements.

```typescript
// my.component.ts
@Component({
  templateUrl: './my.component.html'
})

export class MyComponent {
  handler(event):void {
      // la fonction fait des choses
  }
}
```

```html
// my.component.html
<any-element (event)="handler($event)">innerHTML</any-element>
```

Cela fonctionne de manière similaire à la liaison de propriétés.

Le `(event)` concerne tout type d'événement valide. Par exemple, l'un des types d'événements les plus courants est `click`. Il est émis lorsque vous _cliquez_ avec votre souris. Peu importe le type, `event` est lié à `«handler»` dans l'exemple. Les gestionnaires d'événements sont généralement des fonctions membres de la classe du composant.

Les `( … )` sont spéciaux pour Angular. Les parenthèses indiquent à Angular qu'un événement est lié à l'assignation droite de `handler`. L'événement lui-même provient de l'élément hôte.

Lorsque l'événement est émis, il transmet l'objet Event sous la forme de `$event`. Le `handler` est mappé à la fonction `handler` de la classe du composant, identiquement nommée. L'échange unidirectionnel de l'élément lié à l'événement vers la classe du composant est complet.

L'émission d'événements depuis le gestionnaire, bien que possible, n'a pas d'impact sur l'élément du template. La liaison est unidirectionnelle après tout.

## Directives

Les directives sont des éléments et des attributs de composant créés et reconnus par Angular. Angular associe l'élément ou l'attribut à sa définition de classe correspondante. `@Directive` ou `@Component` décore ces classes. Les deux indiquent à Angular que la classe se comporte comme une directive.

Certaines directives modifient le style de l'élément hôte. D'autres directives affichent des vues ou s'insèrent dans des vues existantes en tant que vues intégrées. En d'autres termes, elles altèrent la mise en page HTML.

Dans tous les cas, les directives signalent le compilateur Angular. Elles marquent les composants pour modification en fonction de la logique de classe de la directive.

### Directive structurelle

Voici trois exemples de directives structurelles. Chacune a un équivalent logique (`if`, `for`, et `switch`).

* *ngIf
* *ngFor
* *ngSwitchCase et *ngSwitchDefault

**Note importante :** les trois sont disponibles via l'import `CommonModule`. Il est disponible depuis `@angular/common` pour l'importation dans le module racine de l'application.

##### *ngIf

`*ngIf` teste une valeur donnée pour voir si elle est _vraie_ ou _fausse_ basée sur l'évaluation booléenne générale en JavaScript. Si vraie, l'élément et son innerHTML apparaissent. Sinon, ils ne sont jamais rendus dans le modèle d'objet de document (DOM).

```html
<!-- rend "<h1>Bonjour !</h1>" -->
<div *ngIf="true">
  <h1>Bonjour !</h1>
</div>

<!-- ne rend pas -->
<div *ngIf="false">
  <h1>Salut !</h1>
</div>
```

Ceci est un exemple artificiel. Toute valeur de membre de la classe du composant du template peut être substituée à `true` ou `false`.

NOTE : Vous pouvez également faire ce qui suit avec *ngIf pour accéder à la valeur observable

```html
<div *ngIf="observable$ | async as anyNameYouWant">
  {{  anyNameYouWant }}
</div>
```

##### *ngFor

`*ngFor` boucle en fonction d'une expression _microsyntaxique_ assignée à droite. La microsyntaxe dépasse le cadre de cet article. Sachez que la microsyntaxe est une forme abrégée d'expression logique. Elle se produit sous forme de chaîne unique capable de référencer les valeurs des membres de la classe. Elle peut boucler sur des valeurs itérables, ce qui la rend utile pour `*ngFor`.

```html
<ul>
  <li *ngFor="let potato of ['Russet', 'Sweet', 'Laura']; let i=index">
      Pommes de terre {{ i + 1 }}: {{ potato }}
  </li>
  <!-- Sortie
  <li>
      Pommes de terre 1: Russet
  </li>
  <li>
      Pommes de terre 2: Sweet
  </li>
  <li>
      Pommes de terre 3: Laura
  </li>
  -->
</ul>
```

`['Russet', 'Sweet', 'Laura']` est une valeur itérable. Les tableaux sont l'un des itérables les plus courants. Le `*ngFor` génère un nouvel élément `<li></li>` par élément de tableau. Chaque élément de tableau est assigné à la variable `potato`. Tout cela est fait en utilisant la microsyntaxe. Le `*ngFor` définit le contenu structurel de l'élément `ul`. C'est caractéristique d'une directive structurelle.

NOTE : Vous pouvez également faire ce qui suit avec la directive *ngFor pour accéder à la valeur observable (astucieux)

```html
<div *ngFor="let anyNameYouWant of [(observable$ | async)]">
  {{  anyNameYouWant }}
</div>
```

##### *ngSwitchCase et *ngSwitchDefault

Ces deux directives structurelles fonctionnent ensemble pour fournir une fonctionnalité `switch` au HTML du template.

```html
<div [ngSwitch]="potato">
  <h1 *ngSwitchCase="'Russet'">{{ potato }} est une pomme de terre Russet.</h1>
  <h1 *ngSwitchCase="'Sweet'">{{ potato }} est une pomme de terre Sweet.</h1>
  <h1 *ngSwitchCase="'Laura'">{{ potato }} est une pomme de terre Laura.</h1>
  <h1 *ngSwitchDefault>{{ potato }} n'est pas une pomme de terre Russet, Sweet, ni Laura.</h1>
</div>
```

Une seule des expressions `*ngSwitch…` est rendue. Remarquez l'attribut `[ngSwitch]` à l'intérieur de l'élément `div` enveloppant le switch. Cela transmet la valeur de `potato` le long de la chaîne `*ngSwitch...`. Cette chaîne de directives structurelles détermine quel élément `h1` est rendu.

Ainsi, `[ngSwitch]` n'est pas une directive structurelle contrairement aux instructions `*ngSwitch…`. Il transmet la valeur tandis que le bloc switch détermine la mise en page finale du HTML.

Rappelez-vous que la stylisation et le passage de valeurs ne sont pas la responsabilité des directives structurelles. Cela concerne les directives d'attributs. Les directives structurelles déterminent uniquement la mise en page.

# Pipes

Les transformations de données de sortie garantissent que les données sont dans un format souhaitable au moment où elles se chargent sur l'écran de l'utilisateur. Normalement, les données se transforment en arrière-plan. Avec les pipes, la transformation des données peut avoir lieu dans le HTML du template. Les pipes transforment directement les données du template.

Les pipes sont esthétiques et pratiques. Ils aident à garder la classe du composant légère en transformations de base. Pour le dire techniquement, les pipes encapsulent la logique de transformation des données.

### Cas d'utilisation

Angular est préemballé avec un ensemble de base de pipes. Travailler avec quelques-uns d'entre eux développera l'intuition pour gérer le reste. La liste suivante fournit trois exemples.

* AsyncPipe
* DatePipe
* TitleCasePipe

##### AsyncPipe

Cette section nécessite une compréhension de base des Promesses ou des Observables pour être pleinement appréciée. L'AsyncPipe fonctionne sur l'un ou l'autre des deux. AsyncPipe extrait les données des Promesses/Observables en tant que sortie pour ce qui vient ensuite.

Dans le cas des Observables, AsyncPipe s'abonne automatiquement à la source de données. Peu importe d'où viennent les données, l'AsyncPipe s'abonne à l'observable source. `async` est le nom syntaxique de AsyncPipe comme montré ci-dessous.

```html
<ul *ngFor="let potato of (potatoSack$ | async); let i=index">
  <li>Pommes de terre {{i + 1}}: {{potato}}</li>
</ul>
```

Dans l'exemple, `potatoSack$` est un Observable en attente d'un téléchargement de pommes de terre. Une fois les pommes de terre arrivées, soit de manière synchrone soit asynchrone, l'AsyncPipe les reçoit sous forme de tableau _itérable_. L'élément de liste se remplit alors de pommes de terre.

##### DatePipe

La mise en forme des chaînes de date nécessite un peu de bidouillage avec l'objet `Date` de JavaScript. Le DatePipe fournit un moyen puissant de formater les dates en supposant que l'entrée donnée est un format de temps valide.

##### TitleCasePipe

Transforme le texte en casse de titre. Met en majuscule la première lettre de chaque mot, et transforme le reste du mot en minuscules. Les mots sont délimités par tout caractère d'espace blanc, tel qu'un espace, une tabulation ou un caractère de saut de ligne.

```typescript
// example.component.ts

@Component({
  templateUrl: './example.component.html'
})
export class ExampleComponent {
  timestamp:string = '2018-05-24T19:38:11.103Z';
}
```

```html
<!-- example.component.html -->

<div>Heure actuelle : {{timestamp | date:'short'}}</div>
```

Le format du `timestamp` ci-dessus est [ISO 8601<sup>1</sup>](https://en.wikipedia.org/wiki/ISO_8601)—pas le plus facile à lire. Le DatePipe (`date`) transforme le format de date ISO en un format plus conventionnel `jj/mm/aa, hh:mm AM|PM`. Il existe de nombreuses autres options de formatage. Toutes ces options sont dans la [documentation officielle](https://angular.io/api/common/DatePipe).

#### Création de Pipes

Bien qu'Angular n'ait qu'un nombre limité de pipes, le décorateur `@Pipe` permet aux développeurs de créer les leurs. Le processus commence par `ng generate pipe [nom-du-pipe]`, en remplaçant `[nom-du-pipe]` par un nom de fichier préférable. Cette commande produit ce qui suit :

```typescript
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'example'
})
export class ExamplePipe implements PipeTransform {
  transform(value: any, args?: any): any {
      return null;
  }
}
```

Ce modèle de pipe simplifie la création de pipes personnalisés. Le décorateur `@Pipe` indique à Angular que la classe est un pipe. La valeur de `name: 'example'`, dans ce cas étant `example`, est la valeur qu'Angular reconnaît lors de l'analyse du HTML du template pour les pipes personnalisés.

Passons à la logique de la classe. L'implémentation de `PipeTransform` fournit les instructions pour la fonction `transform`. Cette fonction a une signification spéciale dans le contexte du décorateur `@Pipe`. Elle reçoit deux paramètres par défaut.

`value: any` est la sortie que le pipe reçoit. Pensez à `<div>{{ someValue | example }}</div>`. La valeur de someValue est passée au paramètre `value: any` de la fonction `transform`. Il s'agit de la même fonction `transform` définie dans la classe ExamplePipe.

`args?: any` est tout argument que le pipe reçoit optionnellement. Pensez à `<div>{{ someValue | example:[some-argument] }}</div>`. `[some-argument]` peut être remplacé par n'importe quelle valeur. Cette valeur est passée au paramètre `args?: any` de la fonction `transform`. C'est-à-dire, la fonction `transform` définie dans la classe de ExamplePipe.

Ce que la fonction retourne (`return null;`) devient la sortie de l'opération du pipe. Jetez un œil à l'exemple suivant pour voir un exemple complet de ExamplePipe. Selon la variable que le pipe reçoit, il met en majuscules ou en minuscules l'entrée en tant que nouvelle sortie. Un argument invalide ou inexistant amènera le pipe à retourner la même entrée en tant que sortie.

```typescript
// example.pipe.ts

@Pipe({
  name: 'example'
})
export class ExamplePipe implements PipeTransform {
  transform(value:string, args?:string): any {
    switch(args || null) {
      case 'uppercase':
        return value.toUpperCase();
      case 'lowercase':
        return value.toLowerCase();
      default:
        return value;
    }
  }
}
```

```typescript
// app.component.ts

@Component({
  templateUrl: 'app.component.html'
})
export class AppComponent {
  someValue:string = "HeLlO WoRlD!";
}
```

```html
<!-- app.component.html -->

<!-- Affiche "HeLlO WoRlD!" -->
<h6>{{ someValue | example }}</h6>

<!-- Affiche "HELLO WORLD!" -->
<h6>{{ someValue | example:'uppercase' }}</h6>

<!-- Affiche "hello world!" -->
<h6>{{ someValue | example:'lowercase' }}</h6>
```

## Hooks de cycle de vie

Les hooks de cycle de vie sont des méthodes temporisées. Ils diffèrent dans le moment et la raison de leur exécution. La détection des changements déclenche ces méthodes. Elles s'exécutent en fonction des conditions du cycle actuel. Angular exécute constamment la détection des changements sur ses données. Les hooks de cycle de vie aident à gérer ses effets.

Un aspect important de ces hooks est leur ordre d'exécution. Il ne dévie jamais. Ils s'exécutent en fonction d'une série prévisible d'événements de chargement produits à partir d'un cycle de détection. Cela les rend prévisibles. Certains actifs ne sont disponibles qu'après l'exécution d'un certain hook. Bien sûr, un hook ne s'exécute que sous certaines conditions définies dans le cycle actuel de détection des changements.

### Dans l'ordre d'exécution :

### ngOnChanges

`ngOnChanges` se déclenche suite à la modification des membres de classe liés par `@Input`. Les données liées par le décorateur `@Input()` proviennent d'une source externe. Lorsque la source externe modifie ces données de manière détectable, elles passent à nouveau par la propriété `@Input`.

Avec cette mise à jour, `ngOnChanges` se déclenche immédiatement. Il se déclenche également lors de l'initialisation des données d'entrée. Le hook reçoit un paramètre optionnel de type `SimpleChanges`. Cette valeur contient des informations sur les propriétés liées en entrée modifiées.

### ngOnInit

`ngOnInit` se déclenche une fois lors de l'initialisation des propriétés liées en entrée (`@Input`) d'un composant. Le prochain exemple ressemblera au précédent. Le hook ne se déclenche pas lorsque ChildComponent reçoit les données d'entrée. Plutôt, il se déclenche juste après que les données sont rendues dans le template de ChildComponent.

### ngDoCheck

`ngDoCheck` se déclenche à chaque cycle de détection des changements. Angular exécute la détection des changements fréquemment. Effectuer une action quelconque provoquera son cycle. `ngDoCheck` se déclenche avec ces cycles. Utilisez-le avec prudence. Il peut créer des problèmes de performance s'il est mal implémenté.

`ngDoCheck` permet aux développeurs de vérifier leurs données manuellement. Ils peuvent déclencher une nouvelle condition de date d'application de manière conditionnelle. En conjonction avec `ChangeDetectorRef`, les développeurs peuvent créer leurs propres vérifications pour la détection des changements.

### ngAfterContentInit

`ngAfterContentInit` se déclenche après l'initialisation (chargement pour la première fois) du DOM de contenu du composant. Attendre les requêtes `@ContentChild(ren)` est le cas d'utilisation principal du hook.

Les requêtes `@ContentChild(ren)` fournissent des références d'éléments pour le DOM de contenu. En tant que telles, elles ne sont pas disponibles avant que le DOM de contenu ne soit chargé. D'où l'utilisation de `ngAfterContentInit` et de son homologue `ngAfterContentChecked`.

### ngAfterContentChecked

`ngAfterContentChecked` se déclenche après chaque cycle de détection des changements ciblant le DOM de contenu. Cela permet aux développeurs de faciliter la manière dont le DOM de contenu réagit à la détection des changements. `ngAfterContentChecked` peut se déclencher fréquemment et causer des problèmes de performance s'il est mal implémenté.

`ngAfterContentChecked` se déclenche également pendant les phases d'initialisation d'un composant. Il vient juste après `ngAfterContentInit`.

### ngAfterViewInit

`ngAfterViewInit` se déclenche une fois après que le DOM de la vue a fini de s'initialiser. La vue se charge toujours juste après le contenu. `ngAfterViewInit` attend que les requêtes `@ViewChild(ren)` se résolvent. Ces éléments sont interrogés depuis la même vue du composant.

Dans l'exemple ci-dessous, l'en-tête `h3` du BComponent est interrogé. `ngAfterViewInit` s'exécute dès que les résultats de la requête sont disponibles.

### ngAfterViewChecked

`ngAfterViewChecked` se déclenche après tout cycle de détection des changements ciblant la vue du composant. Le hook `ngAfterViewChecked` permet aux développeurs de faciliter la manière dont la détection des changements affecte le DOM de la vue.

### ngOnDestroy

`ngOnDestroy` se déclenche lors de la suppression d'un composant de la vue et du DOM ultérieur. Ce hook offre une chance de nettoyer les extrémités avant la suppression d'un composant.

## Vues

Les vues sont presque comme leur propre DOM virtuel. Chaque vue contient une référence à une section correspondante du DOM. À l'intérieur d'une vue se trouvent des nœuds qui reflètent ce qui se trouve dans cette section. Angular assigne un nœud de vue par élément DOM. Chaque nœud contient une référence à un élément correspondant.

Lorsque Angular vérifie les changements, il vérifie les vues. Angular évite le DOM sous le capot. Les vues référencent le DOM en son nom. D'autres mécanismes sont en place pour garantir que les changements de vue se rendent dans le DOM. Inversement, les changements apportés au DOM n'affectent pas les vues.

Encore une fois, les vues sont courantes sur toutes les plateformes de développement en dehors du DOM. Même si vous développez pour une seule plateforme, les vues sont toujours considérées comme une meilleure pratique. Elles garantissent qu'Angular a une interprétation correcte du DOM.

Les vues peuvent ne pas exister dans les bibliothèques tierces. La manipulation directe du DOM est une issue de secours pour ce type de scénario. Bien sûr, ne vous attendez pas à ce que l'application fonctionne sur plusieurs plateformes.

### Types de vues

Il existe deux principaux types de vues : intégrées et hôtes.

Il existe également des conteneurs de vues. Ils contiennent des vues intégrées et hôtes et sont souvent appelés simplement « vues ».

Chaque classe `@Component` enregistre un conteneur de vues (vue) avec Angular. Les nouveaux composants génèrent un sélecteur personnalisé ciblant un certain élément DOM. La vue s'attache à cet élément où qu'il apparaisse. Angular sait maintenant que le composant existe en regardant le modèle de vue.

### Vues hôtes et conteneurs

Les vues hôtes _hébergent_ des composants dynamiques. Les conteneurs de vues (vues) s'attachent automatiquement aux éléments déjà dans le template. Les vues peuvent s'attacher à n'importe quel élément au-delà de ce qui est unique aux classes de composants.

Pensez à la méthode traditionnelle de génération de composants. Elle commence par créer une classe, la décorer avec `@Component`, et remplir les métadonnées. Cette approche se produit pour tout élément de composant prédéfini du template.

Essayez d'utiliser l'interface de ligne de commande Angular (CLI) : `ng generate component [nom-du-composant]`. Cela produit ce qui suit.

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

Cela crée le composant avec le sélecteur `app-example`. Cela attache un conteneur de vue à `<app-example></app-example>` dans le template. Si cela était la racine de l'application, sa vue encapsulerait toutes les autres vues. La vue racine marque le début de l'application du point de vue d'Angular.

Créer des composants dynamiquement et les enregistrer dans le modèle de vue Angular nécessite quelques étapes supplémentaires. Les directives structurelles aident à gérer le contenu dynamique (`*ngIf, *ngFor, et *ngSwitch…`). Les directives ne s'adaptent pas aux applications plus grandes cependant. Trop de directives structurelles compliquent le template.

C'est là que l'instanciation de composants à partir de la logique de classe existante devient utile. Ces composants doivent créer une vue hôte qui peut s'insérer dans le modèle de vue. Les vues hôtes contiennent des données pour les composants afin qu'Angular reconnaisse leur but structurel.

### Vues intégrées

Les directives structurelles créent un [`ng-template` entourant un morceau de contenu HTML](https://angular.io/guide/structural-directives#the-asterisk--prefix). L'élément hôte de la directive a un conteneur de vue attaché. Cela permet au contenu de se rendre conditionnellement dans sa mise en page prévue.

Le `ng-template` contient des nœuds de vue intégrés représentant chaque élément dans son innerHTML. `ng-template` n'est en aucun cas un élément DOM. Il se commente lui-même. Les balises définissent l'étendue de sa vue intégrée.

L'instanciation d'une vue intégrée ne nécessite aucune ressource externe au-delà de sa propre référence. La requête `@ViewChild` peut récupérer cela.

Avec la référence du template, appeler `createEmbeddedView` depuis celui-ci fait l'affaire. Le innerHTML de la référence devient sa propre instance de vue intégrée.

Dans l'exemple suivant, `<ng-container></ng-container>` est un conteneur de vue. `ng-container` est commenté pendant la compilation tout comme `ng-template`. Ainsi, il fournit une sortie pour insérer la vue intégrée tout en gardant le DOM léger.

La vue intégrée du template s'insère à l'emplacement de mise en page de `ng-container`. Cette vue nouvellement insérée n'a pas d'encapsulation de vue supplémentaire au-delà du conteneur de vue. Rappelez-vous comment cela diffère des vues hôtes (les vues hôtes s'attachent à leur élément wrapper `ng-component`).

```typescript
import { Component, AfterViewInit, ViewChild,
ViewContainerRef, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-example',
  template: `
  <h1>Contenu de l'application</h1>
  <ng-container #container></ng-container> <!-- insérer la vue ici -->
  <h3>Fin de l'application</h3>

  <ng-template #template>
    <h1>Contenu du template</h1>
    <h3>Généré dynamiquement !</h3>
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

`@ViewChild` interroge la _variable de référence de template_ `#template`. Cela fournit une référence de template de type `TemplateRef`. `TemplateRef` contient la fonction `createEmbeddedView`. Elle instancie le template en tant que vue intégrée.

Le seul argument de `createEmbeddedView` est pour le contexte. Si vous souhaitez passer des métadonnées supplémentaires, vous pouvez le faire ici sous forme d'objet. Les champs doivent correspondre aux attributs du `ng-template` (`let-[context-field-key-name]="value"`). Passer `null` indique qu'aucune métadonnée supplémentaire n'est nécessaire.

Une deuxième requête `@ViewChild` fournit une référence à `ng-container` en tant que `ViewContainerRef`. Les vues intégrées ne s'attachent qu'à d'autres vues, jamais au DOM. Le `ViewContainerRef` référence la vue qui prend la vue intégrée.

Une vue intégrée peut également s'insérer dans la vue du composant de `<app-example></app-example>`. Cette approche positionne la vue à la toute fin de la vue de ExampleComponent. Dans cet exemple cependant, nous voulons que le contenu apparaisse au milieu où se trouve `ng-container`.

La fonction `insert` de `ViewContainerRef` _insère_ la vue intégrée dans le `ng-container`. Le contenu de la vue apparaît à l'emplacement prévu, au milieu de la vue de ExampleComponent.

## Routage

Le routage est essentiel. De nombreuses applications web modernes hébergent trop d'informations pour une seule page. Les utilisateurs ne devraient pas avoir à faire défiler tout le contenu d'une application. Une application doit se diviser en sections distinguables. Une meilleure pratique Angular est de charger et configurer le routeur dans un module séparé, de haut niveau, dédié au routage et importé par le module racine AppModule.

Les utilisateurs priorisent les informations nécessaires. Le routage les aide à trouver la section de l'application contenant ces informations. Toute autre information utile à d'autres utilisateurs peut exister sur une route entièrement séparée. Avec le routage, les deux utilisateurs peuvent trouver ce dont ils ont besoin rapidement. Les détails non pertinents restent obscurcis derrière des routes non pertinentes.

Le routage excelle dans le tri et la restriction de l'accès aux données de l'application. Les données sensibles ne devraient jamais être affichées aux utilisateurs non autorisés. Entre chaque route, l'application peut intervenir. Elle peut examiner la session d'un utilisateur à des fins d'authentification. Cet examen détermine ce que la route rend si elle doit rendre quoi que ce soit. Le routage donne aux développeurs la chance parfaite de vérifier un utilisateur avant de continuer.

En ce qui concerne Angular, le routage occupe sa propre bibliothèque entière au sein du framework. Tous les frameworks front-end modernes supportent le routage, et Angular ne fait pas exception. Le routage se fait côté client en utilisant soit le routage par hachage soit le routage par localisation. Les deux styles permettent au client de gérer ses propres routes. Aucune assistance supplémentaire du serveur n'est nécessaire au-delà de la requête initiale.

### Routage de base

Les utilitaires de routage exportent avec `RouterModule` disponible depuis `@angular/router`. Il ne fait pas partie de la bibliothèque principale puisque toutes les applications n'ont pas besoin de routage. La manière la plus conventionnelle d'introduire le routage est en tant que son propre [module de fonctionnalité](https://angular.io/guide/feature-modules).

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

`.forRoot(...)` est une fonction de classe disponible depuis la classe RouterModule. La fonction accepte un tableau d'objets `Route` en tant que `Routes`. `.forRoot(...)` configure les routes pour le chargement impatient tandis que son alternative `.forChild(...)` configure pour le chargement paresseux.

Le chargement impatient signifie que les routes chargent leur contenu dans l'application dès le départ. Le chargement paresseux se fait à la demande. L'accent de cet article est le chargement impatient. C'est l'approche par défaut pour charger une application. La définition de la classe RouterModule ressemble à quelque chose comme le bloc de code suivant.

```typescript
@NgModule({
  // ... beaucoup de métadonnées ...
})
export class RouterModule {
  forRoot(routes: Routes) {
    // ... configuration pour les routes chargées avec impatience ...
  }

  forChild(routes: Routes) {
    // ... configuration pour les routes chargées avec paresse ...
  }
}
```

Ne vous inquiétez pas des détails de configuration que l'exemple omet avec des commentaires. Avoir une compréhension générale suffira pour l'instant.

Remarquez comment AppRoutingModule importe le RouterModule tout en l'exportant également. Cela a du sens étant donné qu'AppRoutingModule est un module de fonctionnalité. Il importe dans le module racine en tant que module de fonctionnalité. Il expose les directives, interfaces et services de RouterModule à l'arborescence des composants racine.

Cela explique pourquoi AppRoutingModule doit exporter RouterModule. Il le fait pour le bien de l'arborescence des composants du module racine. Il a besoin d'accès à ces utilitaires de routage !

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

Le jeton AppRoutingModule est importé depuis le tout début. Son jeton s'insère dans le tableau des imports du module racine. L'arborescence des composants racine peut maintenant utiliser la bibliothèque RouterModule. Cela inclut ses directives, interfaces et services comme déjà mentionné. Un grand merci à AppRoutingModule pour l'exportation de RouterModule !

Les utilitaires RouterModule seront utiles pour les composants de la racine. Le HTML de base pour AppComponent utilise une directive : `router-outlet`.

```html
<!-- app.component.html -->

<ul>
  <!-- routerLink(s) ici -->
</ul>
<router-outlet></router-outlet>
<!-- le contenu routé s'ajoute ici (APRÈS L'ÉLÉMENT, PAS DEDANS !) -->
```

`routerLink` est une directive d'attribut de RouterModule. Elle s'attachera à chaque élément de `<ul></ul>` une fois les routes configurées. `router-outlet` est une directive de composant avec un comportement intéressant. Elle agit plus comme un marqueur pour afficher le contenu routé. Le contenu routé résulte de la navigation vers une route spécifique. Cela signifie généralement un seul composant tel que configuré dans AppRoutingModule

Le contenu routé se rend juste après `<router-outlet></router-outlet>`. Rien ne se rend à l'intérieur. Cela ne fait pas une grande différence considérable. Cela dit, ne vous attendez pas à ce que `router-outlet` se comporte comme un conteneur pour le contenu routé. Il est simplement un marqueur pour ajouter le contenu routé au modèle d'objet de document (DOM).

La première question à aborder est de savoir quelles routes cette application consommera ? Eh bien, il y a deux composants : AComponent et BComponent. Chacun devrait avoir sa propre route. Ils peuvent se rendre depuis le `router-outlet` de AppComponent en fonction de l'emplacement de la route actuelle.

L'emplacement de la route (ou chemin) définit ce qui s'ajoute à l'[origine d'un site web](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin) (par exemple, [http://localhost:4200](http://localhost:4200/)) via une série de barres obliques (`/`).

```typescript
// ... mêmes imports que précédemment ...

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

`http://localhost:4200/A` rend AComponent depuis le `router-outlet` de AppComponent. `http://localhost:4200/B` rend BComponent. Vous avez besoin d'un moyen de router vers ces emplacements sans utiliser la barre d'adresse. Une application ne devrait pas dépendre de la barre d'adresse d'un navigateur web pour la navigation.

_Le CSS global (Cascading Style-sheets) complète le HTML en dessous. Les liens de routage d'une application devraient avoir une apparence agréable. Ce CSS s'applique également à tous les autres exemples._

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

Les routes de correspondance totale empêchent l'application de planter si elle ne peut pas faire correspondre la route actuelle. Cela peut se produire à partir de la barre d'adresse où l'utilisateur peut taper n'importe quelle route. Pour cela, Angular fournit une valeur de chemin générique `**` qui accepte toutes les routes. Cette route affiche généralement un composant PageNotFoundComponent affichant « Erreur 404 : Page non trouvée ».

```typescript
// ... PageNotFoundComponent importé avec tout le reste ...

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

L'objet `Route` contenant `redirectTo` empêche le composant PageNotFoundComponent de se rendre à la suite de `http://localhost:4200`. Il s'agit de la route d'accueil de l'application. Pour corriger cela, `redirectTo` redirige la route d'accueil vers `http://localhost:4200/A`. `http://localhost:4200/A` devient indirectement la nouvelle route d'accueil de l'application.

Le `pathMatch: 'full'` indique à l'objet `Route` de faire correspondre la route d'accueil (`http://localhost:4200`). Il fait correspondre le chemin vide.

Ces deux nouveaux objets `Route` vont à la fin du tableau puisque la première correspondance gagne. Le dernier élément du tableau (`path: '**'`) correspond toujours, donc il va en dernier.

Il y a une dernière chose à aborder avant de continuer. Comment l'utilisateur sait-il où il se trouve dans l'application par rapport à la route actuelle ? Bien sûr, il peut y avoir un contenu spécifique à la route, mais comment l'utilisateur est-il censé faire ce lien ? Il devrait y avoir une forme de surbrillance appliquée aux routerLinks. De cette façon, l'utilisateur saura quelle route est active pour la page web donnée.

C'est une correction facile. Lorsque vous cliquez sur un élément `routerLink`, le `Router` d'Angular lui attribue le _focus_. Ce focus peut déclencher certains styles qui fournissent un retour utile à l'utilisateur. La directive `routerLinkActive` peut suivre ce focus pour le développeur.

```html
<!-- app.component.html -->

<ul>
  <li routerLink="/A" routerLinkActive="active">Aller à A !</li>
  <li routerLink="/B" routerLinkActive="active">Aller à B !</li>
</ul>
<router-outlet></router-outlet>
```

L'assignation droite de `routerLinkActive` représente une chaîne de classes. Cet exemple ne montre qu'une seule classe (`.active`), mais n'importe quel nombre de classes délimitées par des espaces peut s'appliquer. Lorsque le `Router` attribue le _focus_ à un routerLink, les classes délimitées par des espaces s'appliquent à l'élément hôte. Lorsque le focus se déplace, les classes sont automatiquement supprimées.

```css
/* global styles.css */

.active {
  background-color: lightgrey !important;
}
```

Les utilisateurs peuvent maintenant facilement reconnaître comment la route actuelle et le contenu de la page coïncident. La surbrillance `lightgrey` s'applique au routerLink correspondant à la route actuelle. `!important` garantit que la surbrillance remplace les styles en ligne.
---
title: 'Angular Pipes Expliqués : Comment Transformer les Données de Template Directement'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-09T23:26:00.000Z'
originalURL: https://freecodecamp.org/news/angular-pipes-explained-how-to-transform-template-data-directly
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9caa740569d1a4ca3381.jpg
tags:
- name: Angular
  slug: angular
- name: toothbrush
  slug: toothbrush
seo_title: 'Angular Pipes Expliqués : Comment Transformer les Données de Template
  Directement'
seo_desc: 'Pipes

  Motivation

  Output data transformations. They ensure data is in a desirable format by the time
  it loads onto the user’s screen. Normally data transforms behind the scenes. With
  pipes, transforming data can take place in the template HTML. Pipes ...'
---

# **Pipes**

#### **Motivation**

Transformations de données de sortie. Ils garantissent que les données sont dans un format souhaitable au moment où elles se chargent sur l'écran de l'utilisateur. Normalement, les données sont transformées en arrière-plan. Avec les pipes, la transformation des données peut avoir lieu dans le template HTML. Les pipes transforment directement les données du template.

Les pipes sont esthétiques et pratiques. Ils aident à garder la classe du composant légère en transformations de base. Pour le dire techniquement, les pipes encapsulent la logique de transformation des données.

#### **Transformation de Sortie**

Comme mentionné dans la section précédente, les pipes transforment les données en ligne. La syntaxe des pipes est corrélée aux scripts shell. Dans de nombreux scripts, la sortie d'une partie de la commande est _piped_ comme sortie dans la partie suivante comme entrée. Cette même tendance caractérise les pipes Angular.

Dans Angular, il existe de nombreuses façons d'interagir avec les données dans le template HTML. Les pipes peuvent être appliqués partout où les données sont analysées dans le template HTML. Ils peuvent se produire dans la logique microsyntax et les interpolations de variables innerHTML. Les pipes prennent en charge toutes les transformations sans ajouter à la classe du composant.

Les pipes sont également _chaînables_. Vous pouvez intégrer des pipes les uns après les autres pour effectuer des transformations de plus en plus complexes. En tant que transformateurs de données spécialisés, les pipes sont à peine triviaux.

#### **Cas d'Utilisation**

Angular est préemballé avec un ensemble de base de pipes. Travailler avec quelques-uns d'entre eux développera l'intuition pour gérer le reste. La liste suivante fournit deux exemples.

* AsyncPipe
* DatePipe

Ces deux pipes effectuent des tâches simples. Leur simplicité est massivement bénéfique.

##### **AsyncPipe**

Cette section nécessite une compréhension de base des Promesses ou des Observables pour être pleinement appréciée. L'AsyncPipe fonctionne sur l'un ou l'autre des deux. AsyncPipe extrait les données des Promesses/Observables comme sortie pour ce qui vient ensuite.

Dans le cas des Observables, AsyncPipe s'abonne automatiquement à la source de données. Peu importe d'où viennent les données, l'AsyncPipe s'abonne à l'observable source. `async` est le nom syntaxique de AsyncPipe comme montré ci-dessous.

```html
<ul *ngFor="let potato of (potatoSack$ | async); let i=index">
  <li>Pomme de terre {{i + 1}}: {{potato}}</li>
</ul>
```

Dans l'exemple, `potatoSack$` est un Observable en attente d'un téléchargement de pommes de terre. Une fois les pommes de terre arrivées, soit de manière synchrone soit asynchrone, l'AsyncPipe les reçoit comme un tableau _itérable_. L'élément de liste se remplit alors de pommes de terre.

##### **DatePipe**

Formater les chaînes de date prend un certain temps de bidouille avec l'objet `Date` de JavaScript. Le DatePipe fournit un moyen puissant de formater les dates en supposant que l'entrée donnée est un format de temps valide.

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

<div>Heure Actuelle: {{timestamp | date:'short'}}</div>
```

Le format du `timestamp` ci-dessus est [ISO 8601<sup>1</sup>](https://en.wikipedia.org/wiki/ISO_8601)—pas le plus facile à lire. Le DatePipe (`date`) transforme le format de date ISO en un format plus conventionnel `jj/mm/aa, hh:mm AM|PM`. Il existe de nombreuses autres options de formatage. Toutes ces options sont dans la [documentation officielle](https://angular.io/api/common/DatePipe).

#### **Création de Pipes**

Bien qu'Angular n'ait qu'un nombre limité de pipes, le décorateur `@Pipe` permet aux développeurs de créer les leurs. Le processus commence par `ng generate pipe [nom-du-pipe]`, en remplaçant `[nom-du-pipe]` par un nom de fichier préférable. Il s'agit d'une commande [Angular CLI](https://cli.angular.io/). Elle produit ce qui suit.

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

Ce modèle de pipe simplifie la création de pipes personnalisés. Le décorateur `@Pipe` indique à Angular que la classe est un pipe. La valeur de `name: 'example'`, dans ce cas `example`, est la valeur qu'Angular reconnaît lors de l'analyse du template HTML pour les pipes personnalisés.

Passons à la logique de la classe. L'implémentation de `PipeTransform` fournit les instructions pour la fonction `transform`. Cette fonction a une signification spéciale dans le contexte du décorateur `@Pipe`. Elle reçoit deux paramètres par défaut.

`value: any` est la sortie que le pipe reçoit. Pensez à `<div>{{ someValue | example }}</div>`. La valeur de someValue est passée au paramètre `value: any` de la fonction `transform`. Il s'agit de la même fonction `transform` définie dans la classe ExamplePipe.

`args?: any` est tout argument que le pipe reçoit optionnellement. Pensez à `<div>{{ someValue | example:[some-argument] }}</div>`. `[some-argument]` peut être remplacé par une seule valeur. Cette valeur est passée au paramètre `args?: any` de la fonction `transform`. C'est-à-dire, la fonction `transform` définie dans la classe de ExamplePipe.

Ce que la fonction retourne (`return null;`) devient la sortie de l'opération du pipe. Regardez l'exemple suivant pour voir un exemple complet de ExamplePipe. Selon l'argument que le pipe reçoit, il met en majuscules ou en minuscules l'entrée comme nouvelle sortie. Un argument invalide ou inexistant fera en sorte que le pipe retourne la même entrée comme sortie.

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

Comprendre l'exemple ci-dessus signifie que vous comprenez les pipes Angular. Il ne reste plus qu'un sujet à discuter.

#### **Pipes Purs et Impurs**

Tout ce que vous avez vu jusqu'à présent était un pipe _pur_. `pure: true` est défini par défaut dans les métadonnées du décorateur `@Pipe`. La différence entre les deux constitue la détection de changement d'Angular.

Les pipes purs se mettent à jour automatiquement chaque fois que la valeur de leur entrée dérivée change. Le pipe s'exécutera à nouveau pour produire une nouvelle sortie en cas de changement détectable dans la valeur d'entrée. Les changements détectables sont déterminés par la boucle de détection de changement d'Angular.

Les pipes impurs se mettent à jour automatiquement chaque fois qu'un cycle de détection de changement se produit. La détection de changement d'Angular se produit assez souvent. Elle signale si des changements se sont produits dans les données membres de la classe du composant. Si c'est le cas, le template HTML se met à jour avec les données mises à jour. Sinon, rien ne se passera.

Dans le cas d'un pipe impur, il se mettra à jour indépendamment du fait qu'il y ait un changement détectable ou non. Un pipe impur se met à jour chaque fois que les boucles de détection de changement se produisent. Les pipes impurs consomment généralement beaucoup de ressources et sont généralement déconseillés. Cela dit, ils fonctionnent plus comme une issue de secours. Si vous avez jamais besoin d'un pipe sensible à la détection, basculez `pure: false` dans les métadonnées du décorateur `@Pipe`.

#### **Conclusion**

Cela couvre les pipes. Les pipes ont beaucoup de potentiel au-delà du cadre de cet article. Les pipes contribuent à des transformations de données succinctes dans le template HTML de vos composants. Ils sont une bonne pratique dans les situations où les données doivent subir de petites transformations.
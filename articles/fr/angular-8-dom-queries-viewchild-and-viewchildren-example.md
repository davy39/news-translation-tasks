---
title: 'Angular 8 Requêtes DOM : Exemple avec ViewChild et ViewChildren'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-16T11:28:09.000Z'
originalURL: https://freecodecamp.org/news/angular-8-dom-queries-viewchild-and-viewchildren-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca16e740569d1a4ca4e8b.jpg
tags:
- name: Angular
  slug: angular
- name: angular8
  slug: angular8
seo_title: 'Angular 8 Requêtes DOM : Exemple avec ViewChild et ViewChildren'
seo_desc: 'By Ahmed Bouchefra

  The @ViewChild and @ViewChildren decorators in Angular provide a way to access and
  manipulate DOM elements, directives and components. In this tutorial, we''ll see
  an Angular 8 example of how to use the two decorators.

  You can use V...'
---

Par Ahmed Bouchefra

Les décorateurs `@ViewChild` et `@ViewChildren` dans Angular fournissent un moyen d'accéder et de manipuler des éléments DOM, des directives et des composants. Dans ce tutoriel, nous verrons un exemple Angular 8 de l'utilisation de ces deux décorateurs.

Vous pouvez utiliser `ViewChild` si vous avez besoin d'interroger un élément du DOM et `ViewChildren` pour plusieurs éléments.

Nous utiliserons un IDE de développement en ligne disponible sur [https://stackblitz.com/](https://stackblitz.com/), vous n'avez donc pas besoin de configurer votre machine de développement locale pour Angular pour l'instant.

Rendez-vous sur Stackblitz, connectez-vous avec votre compte GitHub et choisissez un espace de travail Angular :

![Angular Stackblitz](https://www.diigo.com/file/image/badcbccczobcaepapszdrpoesap/The+online+code+editor+for+web+apps.+Powered+by+Visual+Studio+Code.+-+StackBlitz.jpg)

Vous devriez voir un IDE en ligne avec un projet Angular 8.

![Exemple Angular 8 ViewChild](https://www.diigo.com/file/image/badcbccczobcaepdsrzdrpoescs/angular-hcnsej+-+StackBlitz.jpg)

Notre projet Angular contient le composant `App` habituel et un composant enfant appelé `HelloComponent`, défini dans le fichier `src/app/hello.component.ts` avec le code suivant :

```ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'hello',
  template: `<h1>Hello !</h1>`,
  styles: [`h1 { font-family: Lato; }`]
})
export class HelloComponent  {
  @Input() name: string;
}

```

Le composant accepte une propriété `name` et utilise un template en ligne qui affiche simplement la valeur passée via la propriété name du composant parent.

Dans le décorateur du composant, nous avons utilisé _hello_ comme sélecteur pour le composant, donc dans le template HTML du composant `App` défini dans le fichier `src/app/app.component.html`, nous incluons le composant enfant en utilisant le code suivant :

```html
<hello name=""></hello>
<p>
  Start editing to see some magic happen :)
</p>

```

Après avoir exécuté notre application Angular, le composant hello est rendu et fait partie du DOM, nous pouvons donc l'interroger comme n'importe quel élément DOM normal.

## **Qu'est-ce que ViewChild dans Angular ?**

ViewChild est un décorateur qui crée une requête de vue ou DOM. Selon la [documentation](https://angular.io/api/core/ViewChild#description)

Un décorateur de propriété qui configure une requête de vue. Le détecteur de changements recherche le premier élément ou la directive correspondant au sélecteur dans le DOM de la vue. Si le DOM de la vue change et qu'un nouvel enfant correspond au sélecteur, la propriété est mise à jour.

Le décorateur prend les métadonnées suivantes :

* `selector` - le sélecteur de l'élément à interroger. Cela peut être un type de directive ou un nom.
* `read` - lire un jeton différent des éléments interrogés.
* `static` - Ceci est nouveau dans Angular 8 et indique si les résultats de la requête doivent être résolus avant l'exécution de la détection des changements.

`ViewChild` peut prendre les sélecteurs suivants :

* Classes avec les décorateurs `@Component` ou `@Directive`, c'est-à-dire des composants et des directives,
* Variables de référence de template,
* Fournisseurs,
* `TemplateRef`

Maintenant, retournons à notre fichier `src/app/app.component.ts` et voyons comment nous pouvons interroger le composant enfant en utilisant `ViewChild`. Tout d'abord, modifiez le code en conséquence :

```ts
import { Component, ViewChild, AfterViewInit } from '@angular/core';

import { HelloComponent } from './hello.component';

@Component({
  selector: 'my-app',
  templateUrl: './app.component.html',
  styleUrls: [ './app.component.css' ]
})
export class AppComponent implements AfterViewInit {
  name = 'Angular';
  @ViewChild(HelloComponent, {static: false}) hello: HelloComponent;

  ngAfterViewInit() {
    console.log('Hello ', this.hello.name); 
  }
}

```

Dans la console, vous devriez obtenir **Hello Angular** :

![Image](https://www.diigo.com/file/image/badcbccczobcaoaaaazdrpoobqo/angular-hcnsej+-+StackBlitz.jpg)

Maintenant, expliquons le code.

Tout d'abord, nous avons importé `HelloComponent`, `ViewChild` et `AfterViewInit` du package `@angular/core` :

```ts
import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { HelloComponent } from './hello.component';

```

Ensuite, nous créons une requête appelée `hello` qui prend `HelloComponent` comme sélecteur et a static égal à false :

```ts
@ViewChild(HelloComponent, {static: false}) hello: HelloComponent;

```

Dans Angular 8, le timing pour `ContentChild` et `ViewChild` doit être spécifié explicitement.

Voir : [Pourquoi dois-je spécifier `{static: false}` ? N'est-ce pas la valeur par défaut ?](https://angular.io/guide/static-query-migration#why-do-i-have-to-specify-static-false-isnt-that-the-default)

Ensuite, dans le hook de cycle de vie `ngAfterViewInit()`, nous pouvons utiliser la requête pour accéder à l'élément DOM du composant hello. Dans notre exemple, nous avons accédé à la propriété name du composant, après son montage dans le DOM, qui contient la chaîne _Angular_ :

```ts
  ngAfterViewInit() {
    console.log('Hello ', this.hello.name); 
  }

```

Nous pouvons accéder à n'importe quelles propriétés et même méthodes du composant interrogé.

**Note** : Les requêtes de vue sont définies avant que le callback `ngAfterViewInit` ne soit appelé.

## **Interrogation d'éléments HTML standard avec des références de template**

Nous pouvons également interroger des éléments HTML standard en utilisant `ViewChild` et des variables de référence de template. Retournez à notre fichier `src/app/app.component.html` et modifiez-le comme suit :

```html
<hello name=""></hello>

<p #pRef>
  Start editing to see some magic happen :)
</p>

```

Nous avons simplement ajouté la référence de template `pRef` à notre élément paragraphe. Maintenant, modifions notre code pour accéder au composant en utilisant sa référence. Retournez au fichier `src/app/app.component.ts` et modifiez-le en conséquence :

```ts
import { Component, ViewChild, AfterViewInit, ElementRef } from '@angular/core';

import { HelloComponent } from './hello.component';

@Component({
  selector: 'my-app',
  templateUrl: './app.component.html',
  styleUrls: [ './app.component.css' ]
})
export class AppComponent implements AfterViewInit {
  name = 'Angular';
  @ViewChild(HelloComponent, {static: false}) hello: HelloComponent;

  @ViewChild('pRef', {static: false}) pRef: ElementRef;

    ngAfterViewInit() {
    console.log(this.pRef.nativeElement.innerHTML); 
    this.pRef.nativeElement.innerHTML = "DOM mis à jour avec succès !!!"; 
  }
}

```

Nous importons `ElementRef` et nous créons une configuration de requête pour accéder à l'élément DOM `<p>` avec la référence de template `#pRef` comme suit :

```ts
  @ViewChild('pRef', {static: false}) pRef: ElementRef;

```

Ensuite, dans la méthode `ngAfterViewInit()`, nous pouvons accéder et modifier l'élément DOM natif en utilisant l'objet `nativeElement` de `ElementRef` :

```ts
  @ViewChild('pRef', {static: false}) pRef: ElementRef;

    ngAfterViewInit() {
    console.log(this.pRef.nativeElement.innerHTML);
    this.pRef.nativeElement.innerHTML = "DOM mis à jour avec succès !!!"; 
  }

```

![Image](https://www.diigo.com/file/image/badcbccczobcaorpcazdrpoorep/angular-hcnsej+-+StackBlitz.jpg)

Voici l'exemple en direct depuis ce [lien](https://stackblitz.com/edit/angular-8-viewchild-example).

## **Qu'est-ce que ViewChildren dans Angular ?**

`ViewChildren` est un autre décorateur de propriété qui est utilisé pour interroger le DOM pour plusieurs éléments et retourner une [QueryList](https://angular.io/api/core/QueryList).

Selon la [documentation](https://angular.io/api/core/ViewChildren) :

Vous pouvez utiliser ViewChildren pour obtenir la QueryList des éléments ou des directives du DOM de la vue. Chaque fois qu'un élément enfant est ajouté, supprimé ou déplacé, la liste de requêtes sera mise à jour, et l'observable des changements de la liste de requêtes émettra une nouvelle valeur.

Voyons un exemple.

Allez dans le fichier `src/app/app.component.html` et mettez-le à jour comme suit :

```html
<hello  name="Angular 6"  ></hello>
<hello  name="Angular 7"  ></hello>
<hello  name="Angular 8"  ></hello>

```

Nous affichons simplement le composant hello trois fois. Interrogeons maintenant le DOM. Ouvrez le fichier `src/app/app.component.ts` et modifiez-le comme suit :

```ts
import { Component, ViewChildren, AfterViewInit, QueryList } from '@angular/core';

import { HelloComponent } from './hello.component';

@Component({
  selector: 'my-app',
  templateUrl: './app.component.html',
  styleUrls: [ './app.component.css' ]
})
export class AppComponent implements AfterViewInit {
  name = 'Angular';
  @ViewChildren(HelloComponent) hellos: QueryList<any>;

  ngAfterViewInit() {

     this.hellos.forEach(hello => console.log(hello));

  }
}

```

Vous devriez voir cette sortie dans la console :

![Exemple Angular 5 ViewChildren](https://www.diigo.com/file/image/badcbccczobcapaodrzdrpoospd/angular-8-viewchildren-example+-+StackBlitz.jpg)

Maintenant, expliquons le code.

Tout d'abord, nous importons `ViewChildren`, `AfterViewInit` et `QueryList` du package `@angular/core`.

Ensuite, nous créons une configuration de requête pour accéder à plusieurs éléments DOM :

```ts
@ViewChildren(HelloComponent) hellos: QueryList<any>;

```

`@ViewChildren` retourne une `QueryList` qui stocke une liste d'éléments. Lorsque l'état change, Angular mettra automatiquement à jour cette liste de requêtes.

Enfin, dans la méthode `ngAfterViewInit()`, nous pouvons itérer sur la liste de requêtes et logger chaque élément DOM :

```ts
  ngAfterViewInit() {
     this.hellos.forEach(hello => console.log(hello));
  }

```

Vous pouvez trouver l'exemple en direct depuis ce [lien](https://stackblitz.com/edit/angular-8-viewchildren-example).

## **Conclusions**

Dans ce tutoriel, nous avons vu comment accéder et modifier le DOM dans Angular 8 en utilisant les décorateurs `ViewChild` et `ViewChildren` ainsi que quelques autres API comme `QueryList` et `ngAfterViewInit()`.

Cet [article](https://www.techiediaries.com/angular-dom-queries-viewchild/) a été initialement publié sur [techiediaries](https://www.techiediaries.com/).
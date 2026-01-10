---
title: Modèles de directives structurelles Angular – Ce qu'ils sont et comment les
  utiliser
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2022-08-18T15:21:47.000Z'
originalURL: https://freecodecamp.org/news/angular-structural-directive-patterns-what-they-are-and-how-to-use-them
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-pawe--l-1320737.jpg
tags:
- name: Angular
  slug: angular
seo_title: Modèles de directives structurelles Angular – Ce qu'ils sont et comment
  les utiliser
seo_desc: 'There are two types of  directives in Angular. Attribute directives modify
  the appearance or behavior of DOM elements. Structural directives add or remove
  elements from the DOM.

  Structural directives are one of the most powerful features of Angular, ...'
---

Il existe deux types de directives dans Angular. Les **directives d'attribut** modifient l'apparence ou le comportement des éléments du DOM. Les **directives structurelles** ajoutent ou suppriment des éléments du DOM.

Les directives structurelles sont l'une des fonctionnalités les plus puissantes d'Angular, et pourtant elles sont souvent mal comprises.

Si vous êtes intéressé à en apprendre davantage sur les directives structurelles, continuez à lire pour découvrir ce qu'elles sont, pourquoi elles sont utiles et comment les utiliser efficacement dans vos projets dès aujourd'hui.

## Ce que vous allez apprendre

Dans ce tutoriel, vous apprendrez les modèles de directives structurelles Angular. Vous apprendrez ce qu'elles sont et comment les utiliser.

À la fin de cet article, vous aurez une meilleure compréhension de ces directives et de la manière de les utiliser dans vos propres projets.

## Que sont les directives structurelles Angular ?

Les directives structurelles Angular sont des directives qui changent la structure du DOM. Elles peuvent ajouter, supprimer ou remplacer des éléments. Les directives structurelles ont un `*` devant leur nom.

Dans Angular, il existe trois directives structurelles standard :

* `*ngIf` – inclut conditionnellement un modèle en fonction de la valeur d'une expression retournée par un booléen.
* `*ngFor` – simplifie l'itération sur un tableau.
* `*ngSwitch` – rend chaque vue correspondante.

Voici un exemple de directive structurelle. La syntaxe ressemble à ceci :

```
<element ng-if="Condition"></element>
```

La condition doit être évaluée à vrai ou faux.

```html
<div *ngIf="worker" class="name">{{worker.name}}</div>
```

Angular génère un élément `<ng-template>` et applique la directive `*ngIf` à celui-ci. Cela le transforme en une liaison de propriété entre crochets, par exemple `[ngIf]`. Le reste de la `<div>`, y compris son attribut de classe, est ensuite inséré dans le `<ng-template>` :

Voici un exemple :

```html
<ng-template [ngIf]="worker">
  <div class="name">{{worker.name}}</div>
</ng-template>
```

## Comment fonctionnent les directives structurelles Angular ?

Pour utiliser les directives structurelles, vous ajoutez un élément avec la directive dans votre modèle HTML. L'élément sera alors ajouté, supprimé ou remplacé en fonction de la condition ou de l'expression que vous définissez dans la directive.

### Exemples de directives structurelles

Commençons par ajouter un peu de code HTML de base.

Votre fichier `app.component.html` doit contenir le code suivant :

```html
<div style="text-align:center">
  <h1>
    Bienvenue
  </h1>
</div>
<h2> <app-illustrations></app-illustrations></h2>
```

### Comment utiliser la directive `*ngIf`

Vous utilisez `*ngIf` pour afficher ou supprimer un élément en fonction de la condition donnée. `ngIf` est assez similaire à `if-else` utilisé dans d'autres langages de programmation.

Si l'expression est évaluée à faux, la directive `*ngIf` supprime l'élément HTML. Si l'instruction `if` retourne vrai, une copie de l'élément est ajoutée au DOM.

**Exemple de `*ngIf` :**

Tout d'abord, créez des composants d'illustration dans votre application Angular de démarrage. Ensuite, ouvrez votre fichier de composant d'illustration `HTML` et ajoutez le code suivant :

```html
<h1>
	<button (click)="toggleOn =!toggleOn">Illustration ng-if</button>
  </h1>
  <div *ngIf="!toggleOn">
  <h2>Bonjour</h2>
  <p>Bonjour à vous, cliquez sur le bouton pour voir</p>
  </div>
  <hr>
  <p>Aujourd'hui, c'est lundi et ceci est un élément de texte factice pour vous faire sentir mieux</p>
  <p>Comprendre la directive ngIf avec la clause else</p>
```

Ensuite, ajoutez la variable booléenne suivante dans le fichier `.ts` :

```html
toggleOn: boolean=true;
```

Nous avons une balise div qui contient les salutations. Si la valeur de toggleOn est false, la directive ngIf est affichée. Après cela, nous avons ajouté quelques paragraphes factices.

Le basculement vous permet de démontrer `*ngif` en cachant et en affichant les `divs`.

Le code complet de l'illustration peut être trouvé [ici](https://github.com/gatwirival/Structural-directives/tree/main/ngif-illustration).

### Comment utiliser la directive `*ngFor`

Nous utilisons la directive `*ngfor` pour itérer à travers les valeurs d'un tableau. Cela est similaire à une boucle for dans d'autres langages de programmation ou frameworks.

**Exemple de `*ngFor` :**

Générez une application Angular en utilisant `ng new myapp`, puis créez des composants d'illustration. Ouvrez le fichier `HTML` et ajoutez le code suivant :

```
<ul>

    <li *ngFor="let wok of workers">{{ wok }}</li>

</ul>
```

Ensuite, ajoutez le code ci-dessous à votre fichier TypeScript du composant d'illustration :

```ts
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-illustrations',
  templateUrl: './illustrations.component.html',
  styleUrls: ['./illustrations.component.css']
})
export class IllustrationsComponent implements OnInit {
  workers: any = [

    'travailleur 1',

    'travailleur 2',

    'travailleur 3',

    'travailleur 4',

    'travailleur 5',

  ]

  constructor() { }

  ngOnInit(): void {
  }

}
```

Nous avons une liste non ordonnée, où nous utilisons une boucle for pour itérer à travers le tableau d'éléments. Ainsi, la propriété supplémentaire `*ngFor` a été utilisée avec l'élément. Elle accepte un tableau et rend chaque élément jusqu'à ce qu'elle atteigne la dernière valeur de la collection.

Le code complet de l'illustration peut être trouvé [ici](https://github.com/gatwirival/Structural-directives/tree/main/ngfor-illustration).

### Comment utiliser la directive `*ngSwitch`

Nous utilisons `ngSwitch` pour rendre l'élément selon une seule condition suivie des différentes instructions de cas. La directive `*ngSwitch` est similaire au cas de commutation.

**Exemple de *ngSwitch :**

```html
<div [ngSwitch]="Myshopping">
  <p *ngSwitchCase="'cups'">tasses</p>
  <p *ngSwitchCase="'veg'">Légumes</p>
  <p *ngSwitchCase="'clothes'">Pantalons</p>
  <p *ngSwitchDefault>Mes Achats</p>
</div>
```

Ensuite, ajoutez la variable de chaîne suivante dans le fichier `.ts` :

```
  Myshopping: string = '';

```

Nous avons une variable appelée `Myshopping` avec une valeur par défaut, qui est utilisée dans le modèle pour rendre certains éléments qui répondent aux conditions.

Lorsque la condition reste vraie, les éléments pertinents sont rendus dans le DOM et le reste des éléments est ignoré.

Le code complet de l'illustration peut être trouvé [ici](https://github.com/gatwirival/Structural-directives/tree/main/ngfor-illustration).

S'il n'y a pas de correspondances, la vue avec la directive NgSwitchDefault est rendue comme le montre la sortie de notre code.

## Quand devez-vous utiliser les directives structurelles Angular ?

Si vous souhaitez ajouter ou supprimer un élément du DOM, vous utiliseriez une directive structurelle. Vous pouvez également les utiliser pour changer les styles CSS d'un élément, ou pour ajouter des écouteurs d'événements. Vous pouvez même les utiliser pour créer de nouveaux éléments qui n'étaient pas là auparavant !

La meilleure règle est : _Si vous pensez à manipuler le DOM, alors il est temps pour une directive structurelle._

## Conclusion

Les directives structurelles sont une partie importante d'Angular, et vous pouvez les utiliser de nombreuses manières.

Espérons que ce tutoriel vous a donné une meilleure compréhension de la façon d'utiliser ces directives et quand utiliser chaque modèle.
---
title: Comment garder votre flux de données Angular propre et efficace
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2022-08-03T15:18:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-your-angular-data-flow-tidy-and-efficient
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-isaque-pereira-394377.jpg
tags:
- name: Angular
  slug: angular
seo_title: Comment garder votre flux de données Angular propre et efficace
seo_desc: "Developing large-scale Angular applications can feel like trying to ride\
  \ a bicycle with your eyes closed and both hands tied behind your back. \nThe data\
  \ flow in an Angular application can be extremely complex, especially when dealing\
  \ with bidirection..."
---

Développer des applications Angular à grande échelle peut sembler comme essayer de faire du vélo les yeux fermés et les deux mains attachées dans le dos. 

Le flux de données dans une application Angular peut être extrêmement complexe, surtout lorsqu'il s'agit de liaison de données bidirectionnelle, de mises à jour asynchrones, de formulaires et de routage. 

La clé pour gérer cette complexité est d'écrire un code clair et concis qui est facile à lire et à comprendre. Que vous construisiez une application d'entreprise ou une simple application web, cela est crucial. 

Dans ce tutoriel, nous allons passer en revue quelques bonnes pratiques pour vous aider à vous assurer que votre application suit la voie Angular et ne fuit pas l'état entre les composants ou ne fait pas de travail inutile lors de la gestion des changements de vue. 

Cela vous aidera à créer des applications Angular complexes qui sont facilement compréhensibles et maintenables par d'autres développeurs de votre équipe. Commençons !

## Ce que vous allez apprendre

Dans cet article, nous allons explorer quelques bonnes pratiques pour garder votre flux de données propre et efficace dans les applications Angular. Nous allons aborder des sujets comme la communication entre composants, la liaison de données, et plus encore. 

À la fin de cet article, vous aurez une meilleure compréhension de la manière de garder vos données fluides dans les applications Angular.

## Utilisez les composants intégrés chaque fois que possible

Angular offre une large gamme de composants intégrés que vous pouvez utiliser dans vos applications. Ces composants sont conçus pour être efficaces et faciles à utiliser, alors profitez-en lorsque vous le pouvez. 

Les composants intégrés peuvent aider à réduire la quantité de code que vous devez écrire, rendant votre application plus efficace dans l'ensemble. De plus, l'utilisation de composants intégrés peut aider à garder votre flux de données propre en réduisant le potentiel d'erreurs.

Une erreur courante que les développeurs commettent est d'oublier d'ajouter un écouteur d'événement sur un contrôle d'entrée après avoir mis à jour sa valeur avec une mise à jour de modèle. 

Par exemple, les composants de validation de formulaire intégrés implémentent automatiquement cette vérification pour vous, réduisant considérablement ce type d'erreur.  

Enfin, avec les composants intégrés, il est plus facile de partager des mises à jour dans différentes parties de votre application puisque ils utilisent tous les mêmes APIs.

## Utilisez les Pipes pour filtrer, pas seulement pour transformer

Les pipes sont un excellent moyen de filtrer les données dans Angular. En utilisant des pipes, vous pouvez spécifier de manière déclarative comment vous voulez que vos données soient transformées sans avoir à écrire de code dans la classe de composant.

Vous pouvez apprendre à utiliser les pipes pour filtrer en jouant avec le code GitHub suivant [code](https://github.com/gatwirival/filter-pipe). Dans le code ci-dessous, nous créons un pipe de filtre personnalisé :

```js
import { Pipe, PipeTransform } from '@angular/core';
import { User } from './model';

@Pipe({
  name: 'filter',
  pure: false,
})
export class FilterPipe implements PipeTransform {
  transform(value: User[], filterString: string, property: string): User[] {
    console.log('pipe run');
    if (value.length === 0 || !filterString) {
      return value;
    }
    let filteredUsers: User[] = [];
    for (let user of value) {
      if (user[property].toLowerCase().includes(filterString.toLowerCase())) {
        filteredUsers.push(user);
      }
    }
    return filteredUsers;
  }
}
```

Cela rend votre code plus lisible et plus facile à maintenir. De plus, il est facile de tester les pipes, donc vous pouvez être confiant qu'ils font ce que vous attendez.

## Considérez l'utilisation de Redux

[Redux](https://www.freecodecamp.org/news/learn-redux-toolkit-the-recommended-way-to-use-redux/) est un excellent moyen de gérer les données dans les applications Angular. Il aide à garder votre code organisé et propre et peut rendre le débogage et les tests beaucoup plus faciles.

Redux est également facile à utiliser avec d'autres bibliothèques et frameworks, donc vous pouvez commencer rapidement.

Si vous voulez apprendre les bases de Redux, [voici un guide utile pour débutants](https://www.freecodecamp.org/news/redux-for-beginners/).

## Profitez de l'injection de dépendances 

Le système d'injection de dépendances d'Angular est l'une de ses meilleures fonctionnalités, rendant la modularisation et la réutilisation du code faciles. 

Lors de l'utilisation des services Angular, il est préférable de les garder légers et concentrés sur une seule tâche. Cela aidera à maintenir un flux de données propre et à éviter la duplication de code.

Pour créer un `service injectable`, utilisez la commande suivante :

```js
ng generate service workers/worker
```

```js
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class WorkerService {

  constructor() { }
}
```

Le décorateur `@Injectable()` indique à Angular que cette classe peut être utilisée dans le système DI.

## Les liaisons bidirectionnelles nuisent à la lisibilité et à la maintenabilité

Bien que les liaisons bidirectionnelles soient très pratiques, elles peuvent rapidement rendre votre base de code désordonnée. Lorsque vous avez trop de liaisons bidirectionnelles, il devient difficile de suivre le flux de données à travers votre application. Cela peut conduire à des bugs inattendus et à des erreurs difficiles à trouver. 

### Exemple de liaison bidirectionnelle

```html
<input [(ngModel)]="data"  type="text">
  
<hr>
  
<h3> Apprenez la programmation de {{data}}</h3>
```

```ts
import { Component } from "@angular/core";
  
@Component({
  selector: "my-app",
  templateUrl: "./app.component.html",
})
export class AppComponent {
  data = "FreeCodeCamp";
}
```

Vous obtiendrez le résultat suivant [résultat](https://angular-ivy-dmmxji.stackblitz.io) à partir du code ci-dessus

La [liaison bidirectionnelle](https://angular.io/guide/two-way-binding#adding-two-way-data-binding) est une combinaison de crochets et de parenthèses. Cette syntaxe combine les crochets de liaison de propriété, [], avec les parenthèses de liaison d'événement ().

### Utilisez la liaison unidirectionnelle à la place 

Pour garder votre flux de données propre et efficace, utilisez des liaisons unidirectionnelles chaque fois que possible. Les liaisons unidirectionnelles rendent explicite d'où viennent les données et où elles vont, ce qui rend beaucoup plus facile le raisonnement sur votre code.

### Exemple de liaison unidirectionnelle

```html
<button (click)="myFunction()">Alerte</button>
```

```ts
import { Component } from '@angular/core';

@Component({
  selector: 'my-app',

  template: `<button (click)='myFunction()' >alertez-moi</button>`,
})
export class AppComponent {
  myFunction(): void {
    alert('Afficher l\'alerte !');
  }
}

```

Lorsque vous exécutez le code ci-dessus, vous verrez un bouton `alerte`. Lorsque vous cliquez sur ce bouton, il invoquera la méthode `myFunction()` du composant. Cela exécutera ensuite la méthode `alert()`, affichant une boîte d'alerte avec le texte `Afficher l'alerte` comme montré dans l'exemple suivant [exemple](https://angular-ivy-ptdtve.stackblitz.io) à partir du code ci-dessus.

## Écrivez du code testable

Lorsque vous écrivez du code, gardez toujours à l'esprit à quel point il sera facile ou difficile de le tester.  

En général, essayez de rendre votre code aussi modulaire que possible afin de pouvoir isoler et tester facilement des morceaux individuels. 

Écrivez des tests unitaires pour autant de votre code que possible. Cela aidera à garantir que votre code fonctionne comme prévu et attrapera toute erreur tôt.

## Conclusion

Il existe de nombreuses façons de garder votre flux de données organisé dans une application Angular. La clé est de trouver ce qui fonctionne le mieux pour vous et votre équipe et d'être cohérent avec cela. 

En suivant ces bonnes pratiques, vous pouvez vous assurer que votre application fonctionne de manière fluide et efficace.
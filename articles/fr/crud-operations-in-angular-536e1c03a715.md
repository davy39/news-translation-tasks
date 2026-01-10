---
title: Comment effectuer des opérations CRUD dans Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T19:44:54.000Z'
originalURL: https://freecodecamp.org/news/crud-operations-in-angular-536e1c03a715
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AEkUsVpJZRA-b3PXBsPtYA.png
tags:
- name: Angular
  slug: angular
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment effectuer des opérations CRUD dans Angular
seo_desc: 'By Zafar Saleem

  As you may have seen in my previous blog, it is possible to make CRUD operations
  in vanilla JavaScript. However, it can be a hard decision to choose vanilla JavaScript
  as it gets messier at some point. Moreover, adding event listeners...'
---

Par Zafar Saleem

Comme vous avez pu le voir dans mon [blog précédent](https://medium.com/@zafarsaleem/crud-operations-using-vanilla-javascript-cd6ee2feff67), il est possible de réaliser des opérations CRUD en JavaScript vanilla. Cependant, il peut être difficile de choisir le JavaScript vanilla car cela devient désordonné à un moment donné. De plus, ajouter des écouteurs d'événements à des éléments DOM ajoutés dynamiquement est une corvée, comme nous l'avons vu. Cela devient encore plus compliqué pour les projets à grande échelle.

![Image](https://cdn-media-1.freecodecamp.org/images/AKq8adQYM9qhNlt897Wd2nRfzGZkMttJDbz6)

Une solution consiste à utiliser des frameworks modernes tels qu'Angular, React, etc. Cet article de blog repose sur le même concept que l'exemple précédent, mais en utilisant Angular.

Ce blog suppose que vous avez déjà installé Angular-cli sur votre machine. Une fois que vous l'avez, créez une nouvelle application en utilisant la commande ci-dessous.

```
ng new ngTodo
```

Attendez quelques secondes une fois le projet créé, puis accédez à ce projet. La première chose dont nous avons besoin est de créer un nouveau composant en utilisant la commande ci-dessous.

```
ng generate component todo
```

Cela créera un dossier nommé todo à l'intérieur du dossier src/app. Ce dossier contient les fichiers todo.component.ts, todo.component.html, todo.component.css et todo.component.spec.ts.

Tout le JavaScript sera écrit dans le fichier .ts. En fait, le code de modèle TypeScript (c'est pourquoi l'extension de fichier est .ts) va dans le fichier todo.component.html, les styles dans todo.component.css, et todo.component.spec.ts est pour les tests.

Pour commencer, la première chose à faire est d'ajouter ce composant à l'intérieur du fichier "app.component.html" comme ceci :

```
<app-todo></app-todo>
```

Maintenant, lorsque vous exécutez "ng serve" et chargez l'application dans le navigateur, le composant todo sera chargé.

Il est maintenant temps de se diriger vers le fichier todo.component.ts.

Il devrait y avoir un code standard écrit par angular-cli. Tout notre code va à l'intérieur de la classe TodoComponent.

```
import { Component, OnInit } from '@angular/core';
```

```
@Component({
```

```
  selector: 'app-todo',
```

```
  templateUrl: './todo.component.html',
```

```
  styleUrls: ['./todo.component.css']
```

```
})
```

```
export class TodoComponent implements OnInit {
```

```
  constructor() { }
```

```
  ngOnInit() { }
```

```
}
```

Expliquons d'abord le code standard ci-dessus. Tout d'abord, nous importons le décorateur Component et l'interface OnInit depuis le noyau d'Angular. Voici la définition d'un décorateur.

> Le décorateur marque une classe comme un composant Angular et nous permet de définir des métadonnées de configuration qui déterminent comment le composant doit être traité, instancié et utilisé à l'exécution.

Alors que

> L'interface est un crochet de cycle de vie qui est appelé après qu'Angular a initialisé toutes les propriétés liées aux données d'une directive. Définissez une méthode `ngOnInit()` pour gérer toute tâche d'initialisation supplémentaire.

Ensuite, nous exportons la classe TodoComponent pour la rendre disponible à l'importation dans le reste du projet. Pour cet exemple, nous n'aurons besoin que de ce composant pour être importé dans _app.module.ts_ afin d'initier le composant.

Puisque nous avons créé ce composant en utilisant angular-cli, cette partie est déjà prise en charge. Si vous regardez dans le fichier _app.module.ts_, vous verrez que la classe TodoComponent est importée et ajoutée au tableau des déclarations. Ajoutons maintenant un peu de code.

Tout comme dans notre exemple précédent, ajoutez une propriété _mockData_ à la classe comme ci-dessous.

```
import { Component, OnInit } from '@angular/core';
```

```
@Component({  selector: 'app-todo',  templateUrl: './todo.component.html',  styleUrls: ['./todo.component.css']})export class TodoComponent implements OnInit {
```

```
  // mockData array the includes list of objects with items  mockData: any = [    {      id: '1',      title: 'Acheter du lait.',      done: false,      date: new Date()    }, {      id: '2',      title: 'Réunion avec Ali.',      done: false,      date: new Date()    }, {      id: '3',      title: 'Pause café.',      done: false,      date: new Date()    }, {      id: '4',      title: 'Aller courir.',      done: false,      date: new Date()    }  ];
```

```
  constructor() { }
```

```
  ngOnInit() { }
```

```
}
```

Comme vous pouvez le voir, nous avons également ajouté le type "any" à _mockData_. TypeScript apporte une fonctionnalité de typage strict à JavaScript, mais dans ce cas, cela n'a vraiment pas d'importance. Si vous omettez cette partie, cela devrait encore fonctionner.

Ajoutons quelques propriétés supplémentaires à cette classe qui seront utilisées plus tard.

```
import { Component, OnInit } from '@angular/core';
```

```
@Component({  selector: 'app-todo',  templateUrl: './todo.component.html',  styleUrls: ['./todo.component.css']})export class TodoComponent implements OnInit {
```

```
  mockData: any = [    {      id: '1',      title: 'Acheter du lait.',      done: false,      date: new Date()    }, {      id: '2',      title: 'Réunion avec Ali.',      done: false,      date: new Date()    }, {      id: '3',      title: 'Pause café.',      done: false,      date: new Date()    }, {      id: '4',      title: 'Aller courir.',      done: false,      date: new Date()    }  ];
```

```
  // propriétés pour afficher/masquer le formulaire d'édition, définir la valeur mise à jour et l'id.  show: boolean = false;  value: string;  id: number;
```

```
  constructor() {}
```

```
  ngOnInit() { }
```

```
}
```

La propriété _show_ est utilisée pour afficher editForm, la propriété _value_ est utilisée pour définir la valeur du titre de l'édition, tandis que _id_ est utilisé pour assigner l'id de l'élément actuellement édité. Nous verrons cela plus tard.

Avant d'aller plus loin dans la discussion, ajoutons un modèle html que nous allons utiliser.

```
<div class="sections">  <div class="edit-popup" *ngIf="show">    <input type="text" name="" class="edit-item" value="{{value}}" #item>    <button class="btn-update" (click)="update(item.value)">Mettre à jour</button>  </div>
```

```
<input type="text" name="" class="item" #item>  <button class="btn-add-item" (click)="create(item.value)">Ajouter</button>
```

```
<ul>    <li *ngFor="let item of mockData">      <span [ngClass]="{'done': item.done}">{{item.title}}</span>      <button (click)="remove(item.id)">Supprimer</button>      <button (click)="edit(item.id, item.title)">Éditer</button>      <button (click)="setTaskComplete(item.id)">Terminer</button>    </li>  </ul></div>
```

C'est là qu'un certain nombre de différences peuvent être observées. La première chose qui est noticeable est "edit-popup". Il a une directive conditionnelle _*ngIf_ qui affiche et masque ce morceau de code html en fonction de la valeur de "show" qui est soit vraie soit fausse. C'est la propriété qui provient du TodoComponent que nous avons configuré précédemment.

Ensuite, placez simplement la valeur (titre) en utilisant les accolades {{}} à l'intérieur du champ de texte d'entrée. Enfin, ajoutez un événement de clic qui appellera la fonction de mise à jour et passera la valeur du champ d'entrée comme argument.

Ensuite, il y a la liste ul qui affiche tous les éléments. Comme vous pouvez le voir, l'élément li a _*ngFor_ qui est une _directive de répétition_. Il parcourt _mockData_ et à l'intérieur, nous accédons à l'objet actuel et affichons son titre.

La directive [ngClass] ajoute la classe done à l'élément li en fonction de la valeur de done et de la propriété de l'élément. Si elle est vraie, ajoutez la classe _done_ qui met _line-trough_ sur l'élément li pour indiquer que cette tâche a été réalisée.

Il a également ses boutons qui sont les boutons Supprimer, Éditer et Terminer. Et chacun d'eux a des événements de clic qui appellent sa fonction respective et passent l'id de l'élément actuel. Dans la fonction d'édition, en plus de l'id, le titre est également passé comme argument.

Donc, c'est tout pour le modèle. Revenons au TodoComponent. Ici, nous n'avons pas besoin de fonction de rendu que nous avions en JavaScript vanilla. La liste _mockData_ et la directive _*ngFor_ font le travail de rendu. Donc la partie R de CRUD est faite. Exécutez le serveur angular en utilisant "ng serve" et chargez l'application dans votre navigateur. Vous devriez obtenir des résultats similaires à ceux ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/QSyMwWAPA9ByneSoPvW99Of54yvlRyswwMd2)

Créons maintenant la fonction qui est le C dans CRUD.

```
import { Component, OnInit } from '@angular/core';
```

```
@Component({  selector: 'app-todo',  templateUrl: './todo.component.html',  styleUrls: ['./todo.component.css']})export class TodoComponent implements OnInit {
```

```
mockData: any = [    {      id: '1',      title: 'Acheter du lait.',      done: false,      date: new Date()    }, {      id: '2',      title: 'Réunion avec Ali.',      done: false,      date: new Date()    }, {      id: '3',      title: 'Pause café.',      done: false,      date: new Date()    }, {      id: '4',      title: 'Aller courir.',      done: false,      date: new Date()    }];
```

```
  show: boolean = false;  value: string;  id: number;
```

```
  constructor() {}
```

```
  // Fonction de création pour créer un nouvel élément.  create(item) {    this.mockData.push({      id: Date.now(),      title: item,      done: false,      date: new Date()    });  }
```

```
  ngOnInit() { }
```

```
}
```

La fonction Create est déclenchée lorsque le bouton _AJOUTER_ est cliqué depuis le modèle. Cela est très facile à comprendre et à suivre. Tout d'abord, elle accède au tableau _mockData_ en utilisant le mot-clé _this_ et pousse un nouvel objet avec les propriétés appropriées (comme id, title, done et date, etc.). Cela fera le travail.

![Image](https://cdn-media-1.freecodecamp.org/images/zzLuC0H1CH6JDjGApYbadiUTrx7fhOeBXQRH)

Actualisez votre navigateur et tapez "Ceci est un nouvel élément" et appuyez sur le bouton AJOUTER — vous obtiendrez un résultat similaire à celui ci-dessus.

Maintenant, continuons avec la fonction _remove/supprimer_ qui est la partie D de CRUD.

```
import { Component, OnInit } from '@angular/core';
```

```
@Component({  selector: 'app-todo',  templateUrl: './todo.component.html',  styleUrls: ['./todo.component.css']})export class TodoComponent implements OnInit {
```

```
  mockData: any = [    {      id: '1',      title: 'Acheter du lait.',      done: false,      date: new Date()    }, {      id: '2',      title: 'Réunion avec Ali.',      done: false,      date: new Date()    }, {      id: '3',      title: 'Pause café.',      done: false,      date: new Date()    }, {      id: '4',      title: 'Aller courir.',      done: false,      date: new Date()    }  ];
```

```
  show: boolean = false;  value: string;  id: number;
```

```
  constructor() {}
```

```
  create(item) {    this.mockData.push({      id: Date.now(),      title: item,      done: false,      date: new Date()    });  }
```

```
  // fonction de suppression/suppression va ici.  remove(id) {    this.mockData = this.mockData.filter(item => {      if (item.id !== id) {        return item;      }    });  }
```

```
  ngOnInit() { }
```

```
}
```

Encore une fois très simple. Filtrez à travers _mockData_ et trouvez l'élément actuel en utilisant l'id de l'élément à supprimer et l'id de l'élément actuel de _mockData_. Et retournez tous les éléments sauf celui qui correspond à cet élément.

Actualisez votre navigateur et supprimez le premier élément de la liste. Il devrait être supprimé de l'écran comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/2QgjFS4Li0Z-IccXwx5w-w7BkLNys-Hsi8Xg)

Pour la mise à jour, encore une fois, c'est [la même chose que l'exemple en JavaScript vanilla](https://medium.com/@zafarsaleem/crud-operations-using-vanilla-javascript-cd6ee2feff67) : l'édition fait partie de deux étapes. Tout d'abord, affichez le formulaire d'édition, puis mettez à jour l'élément. Affichons d'abord le formulaire d'édition qui est "edit-popup" :

```
import { Component, OnInit } from '@angular/core';
```

```
@Component({  selector: 'app-todo',  templateUrl: './todo.component.html',  styleUrls: ['./todo.component.css']})export class TodoComponent implements OnInit {
```

```
  mockData: any = [    {      id: '1',      title: 'Acheter du lait.',      done: false,      date: new Date()    }, {      id: '2',      title: 'Réunion avec Ali.',      done: false,      date: new Date()    }, {      id: '3',      title: 'Pause café.',      done: false,      date: new Date()    }, {      id: '4',      title: 'Aller courir.',      done: false,      date: new Date()    }  ];
```

```
  show: boolean = false;  value: string;  id: number;
```

```
  constructor() {}
```

```
  create(item) {    this.mockData.push({      id: Date.now(),      title: item,      done: false,      date: new Date()    });  }
```

```
  remove(id) {    this.mockData = this.mockData.filter(item => {      if (item.id !== id) {        return item;      }    });  }
```

```
  // cette fonction fait la même chose que renderEditForm dans le blog précédent.  edit(id, title) {    this.show = true;    this.value = title;    this.id = id;  }
```

```
  ngOnInit() { }
```

```
}
```

La fonction ci-dessus définit simplement certains attributs de _TodoComponent_ — c'est-à-dire, définir _this.show_ sur true qui affiche le formulaire. Définir la valeur de _this.value_ sur le titre de l'élément à mettre à jour, et définir _this.id_ sur l'id de l'élément. Tous ces attributs peuvent ensuite être accessibles dans le modèle et nous pouvons les utiliser en conséquence.

Maintenant, appuyez sur le bouton ÉDITER pour le premier élément et vous devriez pouvoir voir le formulaire d'édition apparaître en haut de la page :

![Image](https://cdn-media-1.freecodecamp.org/images/joLwZFcW6zlnWe5dYiLXsxdrF9kLOHwHi2XV)

Il est maintenant temps d'écrire la fonction de mise à jour qui effectue réellement les opérations de mise à jour — c'est la partie U de CRUD.

```
import { Component, OnInit } from '@angular/core';
```

```
@Component({  selector: 'app-todo',  templateUrl: './todo.component.html',  styleUrls: ['./todo.component.css']})export class TodoComponent implements OnInit {
```

```
  mockData: any = [    {      id: '1',      title: 'Acheter du lait.',      done: false,      date: new Date()    }, {      id: '2',      title: 'Réunion avec Ali.',      done: false,      date: new Date()    }, {      id: '3',      title: 'Pause café.',      done: false,      date: new Date()    }, {      id: '4',      title: 'Aller courir.',      done: false,      date: new Date()    }  ];
```

```
  show: boolean = false;  value: string;  id: number;
```

```
  constructor() {}
```

```
  create(item) {    this.mockData.push({      id: Date.now(),      title: item,      done: false,      date: new Date()    });  }
```

```
  remove(id) {    this.mockData = this.mockData.filter(item => {      if (item.id !== id) {        return item;      }    });  }
```

```
  edit(id, title) {    this.show = true;    this.value = title;    this.id = id;  }
```

```
  // fonction qui effectue la mise à jour   update(title) {    this.mockData.map(item => {      if (item.id === this.id) {        item['title'] = title;      }    });
```

```
    this.show = false;  }
```

```
  ngOnInit() { }
```

```
}
```

Cette fonction obtient le titre, c'est-à-dire la valeur du champ de texte d'entrée mis à jour, comme argument. Ensuite, elle parcourt _mockData_ et place une vérification pour trouver l'élément qui doit être mis à jour en fonction de son id. Une fois trouvé, remplacez la propriété title par celle éditée et définissez _this.show_ sur false pour masquer le formulaire d'édition.

Avec cette partie, lorsque vous appuyez sur le bouton METTRE À JOUR, après avoir entré le titre mis à jour, vous devriez voir le titre mis à jour comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/MmOTIR5oWV85-AlFuzMSdRaZGGiIhefQrkoo)

La partie finale consiste à marquer la tâche comme terminée, dont la fonction est ci-dessous.

```
import { Component, OnInit } from '@angular/core';
```

```
@Component({  selector: 'app-todo',  templateUrl: './todo.component.html',  styleUrls: ['./todo.component.css']})export class TodoComponent implements OnInit {
```

```
  mockData: any = [    {      id: '1',      title: 'Acheter du lait.',      done: false,      date: new Date()    }, {      id: '2',      title: 'Réunion avec Ali.',      done: false,      date: new Date()    }, {      id: '3',      title: 'Pause café.',      done: false,      date: new Date()    }, {      id: '4',      title: 'Aller courir.',      done: false,      date: new Date()    }  ];
```

```
  show: boolean = false;  value: string;  id: number;
```

```
  constructor() {}
```

```
  create(item) {    this.mockData.push({      id: Date.now(),      title: item,      done: false,      date: new Date()    });  }
```

```
  remove(id) {    this.mockData = this.mockData.filter(item => {      if (item.id !== id) {        return item;      }    });  }
```

```
  edit(id, title) {    this.show = true;    this.value = title;    this.id = id;  }
```

```
  update(title) {    this.mockData.map(item => {      if (item.id === this.id) {        item['title'] = title;      }    });
```

```
    this.show = false;  }
```

```
  setTaskComplete(id) {    this.mockData.map(item => {      if (item.id === id) {        item['done'] = true;      }    });  }
```

```
  ngOnInit() {  }
```

```
}
```

Cela fait à peu près la même chose : parcourt _mockData_ et trouve l'élément à marquer comme terminé en fonction de l'id, et définit sa propriété done sur true.

Enfin, ajoutez un peu de CSS dans le fichier todo.component.css ci-dessous.

```
.done {  text-decoration: line-through;}
```

Le CSS ci-dessus ajoute un trait de soulignement à tout élément qui a la classe done, dans ce cas, les tâches qui sont terminées.

Après cela, appuyez sur quelques boutons Terminer et vous devriez voir quelque chose de similaire à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/kUm7vgCciG88hvmxRAS1RE44BW3Wv1d9Cl16)

Vous pouvez voir la différence entre cet exemple et le précédent utilisant JavaScript vanilla. Angular nous permet d'écrire une approche qui est facile à comprendre, à maintenir et à mettre à l'échelle. Cela est bénéfique dans les applications à grande échelle. JavaScript vanilla fait le travail, mais devient vraiment compliqué une fois que l'application grandit.

Pour obtenir tout le code écrit dans cet exemple, allez-y et clonez le dépôt ci-dessous.

[https://github.com/zafar-saleem/ngTodo](https://github.com/zafar-saleem/ngTodo)
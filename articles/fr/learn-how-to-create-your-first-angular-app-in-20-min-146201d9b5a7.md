---
title: Apprenez à créer votre première application Angular en 20 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-09T18:45:43.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-create-your-first-angular-app-in-20-min-146201d9b5a7
coverImage: https://cdn-media-1.freecodecamp.org/images/0*WzYWvtV9CbhkCorg.
tags:
- name: angular2
  slug: angular2
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Apprenez à créer votre première application Angular en 20 minutes
seo_desc: 'By Said Hayani

  Angular is a JavaScript framework, created my Misko Hevery and maintained by Google.
  It’s an MVC (Model View Vontroller). You can visit the official page to learn more
  about it.

  Right now, the latest version of Angular is 5.2.10. There...'
---

Par Said Hayani

Angular est un framework JavaScript, créé par Misko Hevery et maintenu par Google. C'est un MVC (Modèle Vue Contrôleur). Vous pouvez [visiter la page officielle](https://angular.io/) pour en savoir plus.

Actuellement, la dernière version d'Angular est la **5.2.10**. Il existe une [première génération 1.](https://angularjs.org/)x et une [seconde génération 2.x](https://angular.io/), et les deux générations sont totalement différentes dans leurs structures et méthodes. Ne vous inquiétez pas si vous êtes confus quant à la version, car dans cet article, nous utiliserons la seconde génération 2.x

![Image](https://cdn-media-1.freecodecamp.org/images/hq0cvYK9ku0jw7BckSTe1bQyVtDh2PVSZeMu)

#### **Table des matières**

* Ajout d'un élément (apprendre à soumettre un formulaire dans Angular)
* Suppression d'un élément (apprendre à ajouter un événement dans Angular)
* Animation Angular (apprendre à animer les composants)

### Prérequis :

* **Node.js**

Vérifiez si Node.js est installé sur votre ordinateur. [En savoir plus sur l'installation](https://nodejs.org/en/download/package-manager/).

* **npm**

**npm** (gestionnaire de paquets Node) est installé avec Node.js

Vérifiez la version de **Node.js** :

```
node -v
```

**npm** :

```
npm -v
```

**Angular-CLI**

Vous devez avoir la dernière version d'Angular-CLI. En savoir plus sur Angular CLI [**ici**](https://angular.io/guide/quickstart)**,** et trouver les instructions pour l'installation.

Installez Angular-cli :

```
npm install -g @angular/cli
```

Et enfin, vous devez avoir :

* Connaissances de base en JavaScript
* Fondamentaux HTML et CSS

Vous n'avez pas besoin d'avoir des connaissances en Angular.

Maintenant que nous avons l'environnement pour exécuter notre application Angular, commençons !

### Création de notre première application

Nous utiliserons angular-cli pour créer et générer nos composants. Il générera des services, un routeur, des composants et des directives.

Pour créer un nouveau projet Angular avec Angular-cli, exécutez simplement :

```
ng new my-app
```

Le projet sera généré automatiquement. Créons notre application de liste de tâches !

```
ng new todo-app
```

Ensuite, ouvrez les fichiers dans votre éditeur de texte. J'utilise Sublime Text, mais vous pouvez choisir n'importe quel éditeur.

Voici à quoi ressemble la structure de l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/ptdxoFrfKYkg1O7Kjzfm2vfQxlsrM5ggfSoR)

Ne vous inquiétez pas si vous êtes confus quant aux fichiers. Tout notre travail sera dans le dossier **app**. Il contient cinq fichiers :

![Image](https://cdn-media-1.freecodecamp.org/images/icEs5nlfczvJiEgX7j4EUCcevZFnKCOXocqD)

> Remarque : Angular 2 utilise **TypeScript**, dans lequel les fichiers se terminent par l'extension « **.ts** ».

Pour créer une belle interface pour notre application, nous utiliserons le framework [Bootstrap 4](http://getbootstrap.com/).

Incluez le **cdn** de Bootstrap dans **index.html** :

```
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
```

Exécutez l'application dans votre terminal :

```
ng serve
```

L'application s'exécutera sur [http://localhost:4200/](http://localhost:4200/)

![Image](https://cdn-media-1.freecodecamp.org/images/gwml-v8qHlrNVra-yfJOZH1Kdqx2oRnwrWYF)

Tout est bien ?!

Maintenant, faisons un peu de structuration HTML. Nous utiliserons les classes Bootstrap pour créer un formulaire simple.

![Image](https://cdn-media-1.freecodecamp.org/images/ioyTYMvqC7Izykcin7U1OAEE9pIO7Tn9CWGB)

**app.component.html** :

```
<div class="container"> <form>  <div class="form-group">  <h1 class="text-center text-primary">Todo App</h1>   <div class="input-group-prepend">       <input type="text" class="form-control" placeholder="Ajouter Todo" name="todo">    <span class="input-group-text">Ajouter</span>   </div>  </div> </form></div>
```

Dans **app.component.css** :

```
body{ padding: 0; margin: 0;
```

```
}form{ max-width: 25em; margin: 1em auto;}
```

Pour capturer la valeur de l'entrée dans Angular 2, nous pouvons utiliser la directive **ngModel**. Vous pouvez insérer une variable en tant qu'attribut à l'intérieur de l'élément d'entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/9x5e9yWah1OqD5OpVTfMAxz5fzEjn1e3jLjD)

```
<input type="text" #todo class="form-control" placeholder="Ajouter Todo" name="todo" ngModel>
```

Pour créer une variable en tant qu'attribut, utilisez **#** suivi du nom de la variable.

```
<input #myVariable type="text" name="text" ngModel>
```

```
// obtenir la valeur de la variable<p>{{myVariable.value}}</p>
```

Maintenant, obtenez la valeur de la variable « todo » :

```
<p>{{todo.value}}</p>
```

Tout est bien ?!

Maintenant, nous devons stocker la valeur capturée à partir de l'entrée. Nous pouvons créer un tableau vide dans **app.component.ts** à l'intérieur de la classe AppComponent :

```
export class AppComponent {  todoArray=[] }
```

Ensuite, nous devons ajouter un événement de clic à notre bouton qui pousse la valeur capturée dans « **todoArray** ».

![Image](https://cdn-media-1.freecodecamp.org/images/YiBkAM7A8VteVRe3Ok0KBWaVscJ1QRk9ciL9)

**app.component.html** :

```
<span class="input-group-text" (click)="addTodo(todo.value)">Ajouter</span>
```

Dans **app.component.ts** :

```
export class AppComponent { todoArray=[]
```

```
addTodo(value){    this.todoArray.push(value)    console.log(this.todos)  } }
```

> Utilisez console.log(this.todoArray) pour voir la valeur du tableau

#### Récupérer les données de « todoArray »

Maintenant, nous devons récupérer les données stockées dans « todosArray ». Nous utiliserons la directive *[**ngFor**](https://angular.io/guide/structural-directives) pour parcourir le tableau et extraire les données.

app.component.html :

```
<div class="data">  <ul class="list-instyled">   <li *ngFor="let todo of todoArray">{{todo}}</li>  </ul>  </div>
```

Après avoir récupéré les données :

![Image](https://cdn-media-1.freecodecamp.org/images/IdbbBDKFN29rGZisR0ygAKwKdTUPexZ7-hYD)

Les données seront maintenant récupérées automatiquement lorsque nous cliquons sur le bouton d'ajout.

![Image](https://cdn-media-1.freecodecamp.org/images/Yyeff6WTcxF-b39yi6zMtpe9UWzjZ9NhZBWs)

#### Styliser l'application

J'aime utiliser [Google-fonts](https://fonts.google.com) et [Material-icons](https://material.io/icons/), qui sont gratuits.

Incluez Google fonts dans **app.component.css** :

```
/*Google fonts*/@import url('https://fonts.googleapis.com/css?family=Raleway');
```

Et Material-icons dans **index.html** :

```
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```

Après avoir ajouté un peu de style à notre application, elle ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Bb8mPSgYnJuwIEHA3-cRc8yR0q1YId96ppmi)

Pour utiliser les icônes Material :

```
<i class="material-icons>iconName</i>
```

Ajoutez les icônes « delete » et « add » dans **app.component.html** :

```
// mettre l'icône d'ajout dans la div "input-group-text"
```

```
<span class="input-group-text" (click)="addTodo(todo.value)"><i class="material-icons">add</i></span>
```

```
// et l'icône de suppression dans l'élément de liste <li *ngFor="let todo of todoArray">{{todo}}<i class="material-icons">delete</i></li>
```

Pour les styles dans **app.component.css** :

```
/*Google fonts*/@import url('https://fonts.googleapis.com/css?family=Raleway');
```

```
body{ padding: 0; margin: 0;
```

```
}form{ max-width: 30em; margin: 4em auto; position: relative; background: #f4f4f4; padding: 2em 3em;}form h1{    font-family: "Raleway";    color:#F97300; }form input[type=text]::placeholder{   font-family: "Raleway";   color:#666; }form .data{    margin-top: 1em;}form .data li{ background: #fff; border-left: 4px solid #F97300; padding: 1em; margin: 1em auto; color: #666; font-family: "Raleway";}form .data li i{    float: right;    color: #888;    cursor: pointer;}form .input-group-text{    background: #F97300;    border-radius: 50%;    width: 5em;    height: 5em;    padding: 1em 23px;    color: #fff;    position: absolute;    right: 13px;    top: 68px;    cursor: pointer;}form .input-group-text i{    font-size: 2em;}form .form-control{ height: 3em;    font-family: "Raleway";}form .form-control:focus{ box-shadow: 0;}
```

Notre application est presque terminée, mais nous devons ajouter quelques fonctionnalités. Une fonctionnalité de suppression devrait permettre aux utilisateurs de cliquer sur une icône de suppression et de supprimer un élément. Il serait également bien d'avoir l'option d'entrer un nouvel élément avec la touche entrée, au lieu de cliquer sur le bouton d'ajout.

**Suppression d'éléments**

Pour ajouter la fonctionnalité de suppression, nous utiliserons la méthode de tableau « splice » et une boucle for. Nous allons parcourir « todoarray » et extraire l'élément que nous voulons supprimer.

Ajoutez un événement (click) à l'icône de suppression et donnez-lui « todo » comme paramètre :

```
<li *ngFor="let todo of todoArray">{{todo}} <i (click)="deleteItem(todo)" class="material-icons">delete</i></li>
```

Dans **app.component.ts** :

```
/*supprimer un élément*/  deleteItem(){   console.log("supprimer un élément")  }
```

Lorsque vous cliquez sur supprimer, cela devrait apparaître dans la console :

![Image](https://cdn-media-1.freecodecamp.org/images/nWS2NAJXn4iaQL6vqGwiaUBVSY64XUxerN4w)

Maintenant, nous devons parcourir « todoArray » et supprimer l'élément sur lequel nous avons cliqué.

Dans **app.component.ts** :

```
/*supprimer un élément*/  deleteItem(todo){   for(let i=0 ;i<= this.todoArray.length ;i++){    if(todo== this.todoArray[i]){     this.todoArray.splice(i,1)    }   }  }
```

Le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/bJVYplDX6DgQ39ZaN3eYhBcenCi86fqxbov0)

Génial ?!!

#### **Appuyer sur Entrée pour ajouter des éléments**

Nous pouvons ajouter un événement de soumission au formulaire :

```
(ngSubmit)="TodoSubmit()"
```

Nous devons ajouter la variable « #todoForm » au formulaire et lui donner « ngForm » comme valeur. Dans ce cas, nous n'avons qu'un seul champ, donc nous obtiendrons une seule valeur. Si nous avons plusieurs champs, l'événement de soumission retournera les valeurs de tous les champs du formulaire.

**app.component.html**

```
<form #todoForm= "ngForm" (ngSubmit)="todoSubmit(todoForm.value)"></form>
```

dans **app.component.ts**

```
// soumettre le formulaire  todoSubmit(value:any){ console.log(value)  }
```

Vérifiez la console. Elle retournera un objet de valeurs :

![Image](https://cdn-media-1.freecodecamp.org/images/HBlkb6jnVHcHyTGJ1lEff1dcy2ok-T7glk42)

Donc maintenant, nous devons pousser la valeur retournée vers « todoArray » :

```
// soumettre le formulaire  todoSubmit(value:any){     if(value!==""){    this.todoArray.push(value.todo)     //this.todoForm.reset()    }else{      alert('Champ requis **')    }      }
```

Nous y sommes ?. La valeur est insérée sans avoir besoin de cliquer sur le bouton d'ajout, simplement en cliquant sur « entrée » :

![Image](https://cdn-media-1.freecodecamp.org/images/OWpohuUVC7SjOCGfavFkTnoU2D1sR1CgQj8r)

Une dernière chose. Pour réinitialiser le formulaire après la soumission, ajoutez la méthode intégrée « resetForm() » à l'événement de soumission.

```
<form #todoForm= "ngForm" (ngSubmit)="todoSubmit(todoForm.value); todoForm.resetForm()" ></form>
```

Le formulaire sera réinitialisé après chaque soumission maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/0w5t7IIt4Wj4KBolctdZBNFQrwr4ucCLL6or)

#### Ajout d'animations

J'aime ajouter une petite touche d'animations. Pour ajouter une animation, importez les composants d'animation dans votre **app.component.ts** :

```
import { Component,trigger,animate,style,transition,keyframes } from '@angular/core';
```

Ensuite, ajoutez la propriété animations au décorateur « @component » :

```
@Component({  selector: 'app-root',  templateUrl: './app.component.html',  styleUrls: ['./app.component.css'],  animations:[   trigger("moveInLeft",[      transition("void=> *",[style({transform:"translateX(300px)"}),        animate(200,keyframes([         style({transform:"translateX(300px)"}),         style({transform:"translateX(0)"})           ]))]),
```

```
transition("*=>void",[style({transform:"translateX(0px)"}),        animate(100,keyframes([         style({transform:"translateX(0px)"}),         style({transform:"translateX(300px)"})           ]))])             ])
```

```
]})
```

Maintenant, les éléments ont un bel effet lorsqu'ils sont entrés et supprimés.

![Image](https://cdn-media-1.freecodecamp.org/images/4ugLJyeDD6oGnKg6jc47KqRc692d4H376pqr)

### Tout le code

**app.component.ts**

```
import { Component,trigger,animate,style,transition,keyframes } from '@angular/core';
```

```
@Component({  selector: 'app-root',  templateUrl: './app.component.html',  styleUrls: ['./app.component.css'],  animations:[   trigger("moveInLeft",[      transition("void=> *",[style({transform:"translateX(300px)"}),        animate(200,keyframes([         style({transform:"translateX(300px)"}),         style({transform:"translateX(0)"})           ]))]),
```

```
transition("*=>void",[style({transform:"translateX(0px)"}),        animate(100,keyframes([         style({transform:"translateX(0px)"}),         style({transform:"translateX(300px)"})           ]))])             ])
```

```
]})export class AppComponent {  todoArray=[];  todo;  //todoForm: new FormGroup()
```

```
addTodo(value){    if(value!==""){     this.todoArray.push(value)    //console.log(this.todos)   }else{    alert('Champ requis **')  }      }
```

```
/*supprimer un élément*/  deleteItem(todo){   for(let i=0 ;i<= this.todoArray.length ;i++){    if(todo== this.todoArray[i]){     this.todoArray.splice(i,1)    }   }  }
```

```
// soumettre le formulaire  todoSubmit(value:any){     if(value!==""){    this.todoArray.push(value.todo)     //this.todoForm.reset()    }else{      alert('Champ requis **')    }      } }
```

**app.component.html**

```
<div class="container"> <form #todoForm= "ngForm"(submit)="todoSubmit(todoForm.value); todoForm.resetForm()" >  <div class="form-group">  <h1 class="text-center ">Todo App</h1>   <div class="input-group-prepend">       <input type="text" #todo  class="form-control" placeholder="Ajouter Todo" name="todo" ngModel>    <span class="input-group-text" (click)="addTodo(todo.value)">    <i class="material-icons">add</i></span>   </div>  </div>  <div class="data">  <ul class="list-unstyled">   <li [@moveInLeft]  *ngFor="let todo of todoArray">{{todo}} <i (click)="deleteItem(todo)" class="material-icons">delete</i></li>  </ul> </div> </form></div>
```

**app.component.css**

```
/*Google fonts*/@import url('https://fonts.googleapis.com/css?family=Raleway');
```

```
body{ padding: 0; margin: 0;
```

```
}form{ max-width: 30em; margin: 4em auto; position: relative;    background: #f4f4f4;    padding: 2em 3em;    overflow: hidden;}form h1{    font-family: "Raleway";    color:#F97300; }form input[type=text]::placeholder{   font-family: "Raleway";   color:#666; }form .data{    margin-top: 1em;}form .data li{ background: #fff; border-left: 4px solid #F97300; padding: 1em; margin: 1em auto; color: #666; font-family: "Raleway";}form .data li i{    float: right;    color: #888;    cursor: pointer;}form .input-group-text{    background: #F97300;    border-radius: 50%;    width: 5em;    height: 5em;    padding: 1em 23px;    color: #fff;    position: absolute;    right: 13px;    top: 68px;    cursor: pointer;}form .input-group-text i{    font-size: 2em;}form .form-control{ height: 3em;    font-family: "Raleway";}form .form-control:focus{ box-shadow: 0;}
```

Nous avons terminé ?. Vous pouvez trouver les fichiers et le code sur [Github.](https://github.com/hayanisaid/Todo-app-in-Angular)

#### [Voir la démo](https://stackblitz.com/edit/todo-app-in-angular?file=index.html)

### Conclusion

Angular est plus facile que vous ne le pensez. Angular est l'une des meilleures bibliothèques JavaScript, et elle bénéficie d'un excellent support et d'une communauté sympathique. Elle dispose également d'outils qui rendent le travail avec Angular rapide et facile, comme Angular-cli.

Abonnez-vous à cette [liste de diffusion](http://eepurl.com/dk9OJL) pour en savoir plus sur Angular.

[**SaidHayani@ (@hayanisaid1995) | Twitter**](https://twitter.com/hayanisaid1995)  
[_The latest Tweets from SaidHayani@ (@hayanisaid1995). #Web_Developer /#Frontend / #Back_end(#PHP &…_twitter.com](https://twitter.com/hayanisaid1995)

Voici quelques-uns des meilleurs cours en ligne pour apprendre Angular gratuitement :

**Angular 1.x**

* S[haping avec Angular](https://www.codeschool.com/courses/shaping-up-with-angularjs)
* [Apprendre Angular](http://www.learn-angular.org/)

**Angular 2.x** _(recommandé)_

* [Apprendre Angular2 (coursetro](https://coursetro.com/courses/8/Learn-Angular-2-Development-with-our-Free-Course))
* [Liste de lecture YouTube](https://www.youtube.com/playlist?list=PLC3y8-rFHvwg5gEu2KF4sbGvpUqMRSBSW)
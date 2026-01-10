---
title: Comment effectuer des opérations CRUD avec Angular 13
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-14T19:49:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-crud-operations-using-angular-13
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/How-to-Build-a-Weather-Application-using-React--82-.png
tags:
- name: Angular
  slug: angular
- name: crud
  slug: crud
seo_title: Comment effectuer des opérations CRUD avec Angular 13
seo_desc: "By Nishant Kumar\nBuilding a full-stack application can be tough. And the\
  \ base of building such an application is learning how to perform CRUD operations\
  \ – Create, Read, Update, and Delete. \nIt's by using these operations that we manage\
  \ the data flow ..."
---

Par Nishant Kumar

Construire une application full-stack peut s'avérer difficile. Et la base de la construction d'une telle application est d'apprendre à effectuer des opérations CRUD – Créer, Lire, Mettre à jour et Supprimer (Create, Read, Update, and Delete).

C'est en utilisant ces opérations que nous gérons le flux de données entre l'application cliente et le serveur.

Ainsi, dans cet article, vous apprendrez comment effectuer des opérations CRUD dans Angular en utilisant les Services Angular.

Plongeons dans le vif du sujet.

## Mais que sont les services Angular ?

Les services Angular sont des méthodes qui sont déclenchées lorsque nous voulons effectuer une certaine opération dans une application Angular. Dans notre cas, ce sont les méthodes qui effectueront les opérations CRUD. En d'autres termes, nous aurons un service qui créera des données dans la base de données. De la même manière, nous aurons différents services pour lire les données du serveur, mettre à jour les données sur le serveur, ainsi que pour supprimer des données.

## Configuration de base

Créez un dossier appelé Angular CRUD sur votre système. Et à l'intérieur de ce dossier, créez deux fichiers. L'un est le client, et l'autre est le serveur.

Le **client** contiendra notre application Angular, et le **server** contiendra le code backend pour le serveur, construit avec Node, Express et MongoDB.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-185153.jpeg)

Si vous voulez apprendre à concevoir et développer une API RESTful, vous pouvez regarder ma vidéo sur [RESTful APIs - Build a RESTful API using Node, Express, and MongoDB](https://youtu.be/paxagc55loU). Vous pouvez également consulter mon blog sur [How to Build a RESTful API Using Node, Express, and MongoDB](https://www.freecodecamp.org/news/build-a-restful-api-using-node-express-and-mongodb/).

Mais si vous voulez juste le code, vous pouvez simplement le récupérer sur [GitHub](https://github.com/nishant-666/Rest-Api-Express-MongoDB).

Ajoutez ce code backend dans le dossier server, puis lancez-le en utilisant **npm start**. N'oubliez pas d'utiliser **npm install** pour installer les packages au préalable.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-185814.jpeg)

Maintenant, dans le dossier client, ajoutez le code de démarrage pour le projet Angular à partir du dépôt ci-dessous. C'est juste un formulaire qui affiche le nom et l'âge dans la console.

Faites un **`npm i`** ici également avant de lancer le projet. Et pour lancer le projet, faites simplement **`ng serve`**.

Code de démarrage Angular : [https://github.com/nishant-666/Angular-crud/tree/Stater-Code](https://github.com/nishant-666/Angular-crud/tree/Stater-Code)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-190334.jpeg)

Et voici notre résultat qui comporte deux entrées et un bouton de soumission.

## Comment écrire des services pour les opérations CRUD

Maintenant, écrivons les services pour les opérations CRUD. Mais nous devons d'abord générer un composant de service. Appelons ce service **users**.

Pour générer un nouveau service, tapez simplement la commande suivante dans un nouveau terminal :

```
ng g s users
```

Ici, **g** est l'abréviation de generate et **s** est l'abréviation de service, suivi du nom du service, qui est users.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-190732.jpeg)

Et le service a maintenant été créé. Vous pouvez vérifier le service nouvellement créé dans le dossier **app**.

```
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  constructor() { }
}

```

Maintenant, écrivons le code pour le service de lecture qui récupère les données de la base de données. Pour cela, nous avons besoin du **HttpClientModule**, afin d'envoyer ou de recevoir des **requêtes http.**

Nous le ferons dans le fichier **app.module.ts**, car c'est là que se trouvent tous les imports.

```
import { HttpClientModule } from '@angular/common/http';
```

Et ensuite, ajoutez ce **HttpClientModule** dans la liste des imports :

```
imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
 ],
```

Voici l'intégralité du fichier **app.module.ts** pour votre référence :

```
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

```

Maintenant, nous pouvons envoyer des requêtes **http** depuis notre application.

Pour recevoir des données du backend, créons un service. Dans le fichier users.service.ts, importez **HttpClient** et **Observable.** 

```
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
```

Ainsi, nous enverrons des requêtes à l'API backend en utilisant ce **HttpClient**, et nous recevrons les données entrantes en utilisant un **observable.**

Maintenant, créons une instance de HttpClient dans le constructeur.

```
constructor(private http: HttpClient) { }
```

Définissons également l'URL de base pour l'API backend. Si vous vérifiez le dossier server, vous verrez un fichier appelé **index.js.** Et ici, nous avons ce point de terminaison de base **/api**.

```
private baseURL = `http://localhost:3000/api`
```

```
app.use('/api', routes)
```

## Comment créer un service pour récupérer les données

Créez une fonction qui s'exécutera chaque fois que nous envoyons une requête **GET** au serveur.

```
getAllData(): Observable<any> {
   return this.http.get(`${this.baseURL}/getAll`)
}
```

Ce **getAll** est la route pour récupérer toutes les données. Nous ajoutons donc le chemin de la route à la **baseURL**.

Maintenant, nous devons appeler cette fonction partout où nous voulons afficher les données entrantes. Faisons-le dans le fichier **app.component.ts.**

Tout d'abord, importez le service.

```
import { UsersService } from './users.service';
```

Ensuite, créez une instance de ce service dans le constructeur.

```
constructor(
    private userService: UsersService
  ) { }
```

Ensuite, dans **ngOnInit**, appelez la fonction dans le **userService**. De plus, abonnez-vous aux données entrantes en utilisant **subscribe**.

```
ngOnInit() {
    this.userService.getAllData()
      .subscribe(data => {
        console.log(data)
      })
  }
```

Ainsi, ce **ngOnInit** s'exécute au chargement de la page, ce qui est l'équivalent du **Hook useEffect** et de **componentDidMount** dans React.

Et ce subscribe nous renvoie les données entrantes du serveur backend.

Maintenant, vérifions la console.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-192702.jpeg)

Nous n'avons aucune donnée dans la base de données, c'est pourquoi nous obtenons un tableau vide.

## Comment créer un service pour ajouter des données

Maintenant, créons un service pour ajouter des données à la base de données backend en utilisant le serveur backend.

```
postData(data: any): Observable<any> {
    return this.http.post(`${this.baseURL}/post`, data)
}
```

C'est très similaire au service de lecture. La seule différence est qu'il prend deux arguments, pas un. L'un est le point de terminaison, et l'autre est la donnée que nous allons poster. Et nous passerons cette donnée depuis notre **app.component.ts.**

Dans le fichier **app.component.ts**, créez une fonction submitData. Elle doit contenir un objet body qui sera envoyé.

```
 submitData(value: any) {
    let body = {
      name: value.name,
      age: value.age
    }
  }
```

Ensuite, nous posterons ce corps comme ceci :

```
this.userService.postData(body)
  .subscribe(response => {
    	console.log(response)
})
```

Voyez les choses ainsi : nous envoyons le corps dans la fonction userService.postData, et il est reçu à l'autre bout comme argument **data**, dans les services. Et ensuite, nous le postons simplement.

```
postData(data: any): Observable<any> {
    return this.http.post(`${this.baseURL}/post`, data)
}
```

Voici l'intégralité de la fonction submitData pour votre référence :

```
submitData(value: any) {
    let body = {
      name: value.name,
      age: value.age
    }

    this.userService.postData(body)
      .subscribe(response => {
        console.log(response)
      })
  }
```

Maintenant, ajoutons quelques données.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-193534.jpeg)

Ajoutez un nom et un âge, puis cliquez sur Add Data.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-193610.jpeg)

Et ce sera ajouté. Rafraîchissez la page, et vous verrez que le service de lecture de données fonctionne également, car nous recevrons les données entrantes.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-193645.jpeg)

## Comment créer un service pour mettre à jour et supprimer des données

Maintenant, créons les services pour mettre à jour et supprimer des données.

```
updateData(data: any, id: string): Observable<any> {
    return this.http.patch(`${this.baseURL}/update/${id}`, data)
}
```

Ce service **updateData** prend deux arguments. L'un est l'id du document que nous allons mettre à jour, et le second est la nouvelle donnée qui remplacera la donnée précédente. Le **updateData** utilise la méthode patch pour mettre à jour les données.

Nous utiliserons l'id comme paramètre de chemin. Il sera ajouté dans la méthode **http.patch**. Et nous passerons également la nouvelle donnée.

De même, nous avons le service **deleteData**. Celui-ci ne prend que l'id comme argument, et il sera supprimé. Le **deleteData** utilise la méthode `delete` pour supprimer les données.

```
deleteData(id: string): Observable<any> {
    return this.http.delete(`${this.baseURL}/delete/${id}`)
}
```

Importez la fonction updateData dans le fichier **app.component.ts**.

```
updateData(value: any) {
    let body = {
      name: value.name,
      age: value.age
    }

    this.userService.updateData(body, `622ca8c59f6c668226f74f52`)
      .subscribe(response => {
        console.log(response)
      })
  }
```

Ici, nous passons le nouveau corps mis à jour et l'id du document que nous voulons mettre à jour.

```
<form #loginForm="ngForm" (ngSubmit)="updateData(loginForm.value)">
  <div class="main">
    <div class="input-fields">
      <input name="name" ngModel placeholder="Nom" id="name" type="text" class="input-field" />
    </div>
    <div class="input-fields">
      <input name="age" ngModel placeholder="Âge" id="age" type="number" class="input-field" />
    </div>
    <button>Mettre à jour les données </button>
  </div>
</form>
```

De plus, changez également la fonction dans **app.component.html**, dans les balises de formulaire.

Ainsi, si nous ajoutons de nouvelles données dans les champs de saisie, elles remplaceront les anciennes données pour l'id **622ca8c59f6c668226f74f52.** Parce que c'est la donnée et l'id que nous passons.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-194634.jpeg)

Ajoutons ces nouvelles données dans le formulaire, et cliquons sur le bouton Update Data. Vous verrez que les données seront mises à jour et qu'elles apparaîtront dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-194708.jpeg)

Pour supprimer des données, créez une fonction dans app.component.ts appelée **delete,** et ajoutez le service **deleteData** à l'intérieur.

```
delete() {
    this.userService.deleteData(`622c573cf23ce54e445b2bed`)
      .subscribe(response => {
        console.log(response);
      })
  }
```

De plus, changez le texte du bouton HTML et la fonction.

```
<form #loginForm="ngForm" (ngSubmit)="delete()">
  <div class="main">
    <div class="input-fields">
      <input name="name" ngModel placeholder="Nom" id="name" type="text" class="input-field" />
    </div>
    <div class="input-fields">
      <input name="age" ngModel placeholder="Âge" id="age" type="number" class="input-field" />
    </div>
    <button>Supprimer les données </button>
  </div>
</form>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-195125.jpeg)

Ouvrez l'onglet Network dans les Chrome Dev Tools, et cliquez sur le bouton Delete Data. Cela supprimera le document avec l'id **622ca8c59f6c668226f74f52,** car c'est ce que nous passons au service **deleteData**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-195807.jpeg)

Et nous recevrons ce message de confirmation.

## Conclusion

Voilà donc comment nous effectuons des **opérations CRUD** dans Angular 13 en utilisant les Services.

Vous pouvez également consulter ma vidéo sur [Let's perform CRUD Operations with Angular 13 - Full Tutorial for Beginners](https://youtu.be/O-MAtagUJjM)

Récupérez le code complet ici : [https://github.com/nishant-666/Angular-crud/tree/Finished-Code](https://github.com/nishant-666/Angular-crud/tree/Finished-Code)
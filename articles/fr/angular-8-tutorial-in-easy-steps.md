---
title: Comment créer une application Angular 8 à partir de zéro en 11 étapes faciles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-11T22:31:27.000Z'
originalURL: https://freecodecamp.org/news/angular-8-tutorial-in-easy-steps
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/desktop-cropped-1.jpg
tags:
- name: Angular
  slug: angular
- name: angular8
  slug: angular8
- name: Apps
  slug: apps-tag
seo_title: Comment créer une application Angular 8 à partir de zéro en 11 étapes faciles
seo_desc: "By Ahmed Bouchefra\nAngular is one of the three most popular frameworks\
  \ for front-end development, alongside React and Vue.js. The latest version is Angular\
  \ 8 which was released on May 28, 2019. \nThere are many new features and enhancements\
  \ to both th..."
---

Par Ahmed Bouchefra

Angular est l'un des trois frameworks les plus populaires pour le développement front-end, aux côtés de React et Vue.js. La dernière version est Angular 8, sortie le 28 mai 2019. 

Il y a de nombreuses nouvelles fonctionnalités et améliorations à la fois pour l'interface de ligne de commande et le framework lui-même, ce qui entraîne une augmentation des performances et des bundles de production plus petits. Une fonctionnalité intéressante est la commande ng deploy qui permet aux développeurs de construire et de déployer rapidement leurs applications Angular sur des fournisseurs d'hébergement populaires tels que Firebase ou GitHub.

Dans ce tutoriel, nous vous guiderons étape par étape pour construire une application Angular exemple à partir de zéro qui utilise de nombreuses API Angular telles que HttpClient et Material Design.

Voici quelques-unes des choses que nous allons apprendre :

* Comment simuler un serveur API REST qui utilise des données fictives à partir d'un fichier JSON 
* Comment consommer l'API REST à partir de notre application Angular 8 en utilisant `HttpClient`
* Comment gérer les erreurs HTTP en utilisant les opérateurs RxJS `throwError()` et `catchError()`
* Comment réessayer les requêtes HTTP échouées dans des conditions de réseau médiocres et annuler les requêtes en attente en utilisant les opérateurs RxJS `retry()` et `takeUntil()`
* Comment créer et utiliser des composants et services Angular 
* Comment configurer le routage et Angular Material dans notre projet et créer une interface utilisateur professionnelle avec des composants Material Design
* Enfin, nous apprendrons comment déployer l'application sur Firebase en utilisant la commande `ng deploy` disponible dans Angular 8.3+.

Vous apprendrez également par l'exemple :

* Comment simuler rapidement une API REST avec des fonctionnalités du monde réel, telles que la pagination, que vous pouvez consommer à partir de votre application avant de passer à un backend réel lorsqu'il est prêt.
* Comment configurer Angular CLI
* Comment initialiser votre projet Angular 8
* Comment configurer Angular Material
* Comment ajouter des composants et du routage Angular
* Comment générer et utiliser des services Angular
* Comment consommer des API REST avec Angular HttpClient
* Comment construire et déployer votre application Angular sur Firebase.

Ce tutoriel est divisé en les étapes suivantes :

* Étape 1 — Installation d'Angular CLI 8
* Étape 2 — Création de votre projet Angular 8
* Étape 3 — Ajout d'Angular HttpClient
* Étape 4 — Création de composants
* Étape 5 — Ajout du routage
* Étape 6 — Construction de l'interface utilisateur avec les composants Angular Material
* Étape 7 — Simulation d'une API REST
* Étape 8 — Consommation de l'API REST avec Angular HttpClient
* Étape 9 — Gestion des erreurs HTTP
* Étape 10 — Ajout de la pagination
* Étape 11 — Construction et déploiement de votre application Angular sur Firebase

Maintenant, commençons par les prérequis !

> **Note** : vous pouvez télécharger notre **[Livre Angular 8 : Construisez vos premières applications web avec Angular 8](https://www.techiediaries.com/angular-book-build-your-first-web-apps/)** gratuitement.

# Prérequis

Si vous souhaitez suivre ce tutoriel, vous aurez besoin de :

* Des connaissances préalables en TypeScript.
* Une machine de développement avec **Node 8.9+** et **NPM 5.5.1+** installés. Node est requis par Angular CLI. Vous pouvez vous rendre sur [le site officiel](https://nodejs.org/downloads) et télécharger les binaires pour votre système. Vous pouvez également utiliser [NVM](https://github.com/nvm-sh/nvm) — Node Version Manager — un script bash conforme POSIX pour installer et gérer plusieurs versions de Node.js sur votre machine.

Si vous êtes prêt, apprenons par l'exemple comment construire une application Angular 8 qui consomme une API REST en utilisant HttpClient. Nous implémenterons des fonctionnalités du monde réel comme la gestion des erreurs et la nouvelle tentative des requêtes HTTP échouées.

# Étape 1 — Installation d'Angular CLI 8

Commençons par la première étape, où nous installerons la dernière version d'Angular CLI.

![Image](https://www.techiediaries.com/ezoimgfmt/www.diigo.com/file/image/rscqpoqzoceeaeedqzdspasasb/Angular+CLI+8.jpg?ezimgfmt=rs:461x281/rscb1/ng:webp/ngcb1)

[Angular CLI](https://cli.angular.io/) est l'outil officiel pour initialiser et travailler avec des projets Angular. Ouvrez un nouveau terminal et exécutez la commande suivante :

```bash
$ npm install -g @angular/cli

```

Lors de la rédaction de ce tutoriel, **angular/cli v8.3.2** est installé sur notre système.

C'est tout, vous êtes prêt pour la deuxième étape !

# Étape 2 — Création de votre projet Angular 8

Dans cette étape, nous utiliserons Angular CLI pour initialiser notre projet Angular.

Allez dans votre terminal et exécutez ces commandes :

```bash
$ cd ~  
$ ng new angular-example

```

L'interface de ligne de commande vous demandera et vous demandera **si vous souhaitez ajouter le routage Angular.** Dites Oui. Il vous demandera ensuite **quel format de feuille de style vous souhaitez utiliser.** Choisissez **CSS**.

Angular CLI générera les fichiers et dossiers requis, installera les packages à partir de npm, et configurera même automatiquement le routage dans notre projet.

Maintenant, allez dans le dossier racine de votre projet et exécutez le serveur de développement local en utilisant ces commandes :

```bash
$ cd angular-example  
$ ng serve

```

Votre application web Angular sera disponible à l'adresse `[http://localhost:4200/](http://localhost:4200/)`.

![Image](https://www.techiediaries.com/ezoimgfmt/www.diigo.com/file/image/rscqpoqzoceeaposbzdspascea/Angular+CLI+Ng+Serve.jpg?ezimgfmt=rs:710x191/rscb1/ng:webp/ngcb1)

Ouvrez un navigateur web et allez à l'adresse `http://localhost:4200/`. Vous devriez voir cette belle page (À partir d'Angular 8.3+) :

![Image](https://www.techiediaries.com/ezoimgfmt/paper-attachments.dropbox.com/s_F52E295BB9C92BEFE7506DFCE2086C2583C762072AFE2CA1A9CE9AD4DA9FF751_1567465432228_Angulardemo.png?ezimgfmt=rs:710x341/rscb1/ng:webp/ngcb1)

Vous devez laisser le serveur de développement en cours d'exécution et ouvrir un nouveau terminal pour les étapes suivantes.

Vous êtes maintenant prêt pour la troisième étape !

# Étape 3 — Ajout d'Angular HttpClient

Dans cette étape, nous ajouterons `HttpClient` à notre projet exemple.

Ouvrez le fichier `src/app/app.module.ts` et apportez les modifications suivantes :

```ts
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

Nous avons simplement importé [HttpClientModule](https://angular.io/api/common/http/HttpClientModule#description) et l'avons inclus dans le tableau `imports`.

C'est tout - maintenant nous pouvons utiliser le service `HttpClient` dans notre projet Angular pour consommer notre API REST.

Vous êtes prêt pour la cinquième étape !

# Étape 4 — Création de composants UI

Les applications Angular sont composées de composants. Dans cette étape, nous apprendrons à créer quelques composants Angular qui composent notre interface utilisateur.

Ouvrez un nouveau terminal et exécutez la commande suivante :

```bash
$ cd ~/angular-example  
$ ng g component home

```

Vous obtiendrez la sortie suivante dans votre terminal :

```
CREATE src/app/home/home.component.html (19 bytes)  
CREATE src/app/home/home.component.spec.ts (614 bytes)  
CREATE src/app/home/home.component.ts (261 bytes)  
CREATE src/app/home/home.component.css (0 bytes)  
UPDATE src/app/app.module.ts (467 bytes)

```

Nous avons quatre fichiers, tous requis par notre composant.

Ensuite, générez le composant about :

```bash
$ ng g component about

```

Ensuite, ouvrez le fichier `src/app/about/about.component.html` et ajoutez le code suivant :

```html
<p style="padding: 15px;">Ceci est la page à propos qui décrit votre application</p>

```

Vous êtes prêt pour la sixième étape !

# Étape 5 — Ajout du routage

Dans cette étape, nous apprendrons à ajouter le routage à notre exemple.

Allez dans le fichier `src/app/app-routing.module.ts` et ajoutez les routes suivantes :

```ts
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';


const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full'},
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

```

Nous avons importé les composants Angular et nous avons déclaré trois routes.

La première route est pour rediriger le chemin vide vers le composant home, donc nous serons automatiquement redirigés vers la page d'accueil lorsque nous visiterons l'application pour la première fois.

C'est tout. Maintenant que vous avez ajouté le routage, vous êtes prêt pour l'étape suivante !

# Étape 6 — Ajout d'Angular Material

Dans cette étape du tutoriel, nous apprendrons à configurer [Angular Material](https://material.angular.io/) dans notre projet et à construire l'interface utilisateur de notre application en utilisant des composants Material.

Allez dans votre terminal et exécutez cette commande depuis la racine de votre projet :

```bash
$ ng add @angular/material

```

Vous serez invité à choisir le thème, alors choisissons **Indigo/Pink**.

Pour les autres questions - si vous souhaitez **configurer HammerJS pour la reconnaissance des gestes** et si vous souhaitez **configurer les animations du navigateur pour Angular Material** - appuyez sur **Entrée** pour utiliser les réponses par défaut.

Ouvrez le fichier `src/app/app.module.ts` et ajoutez les imports suivants :

```ts
import { MatToolbarModule,
  MatIconModule,
  MatCardModule,
  MatButtonModule,
  MatProgressSpinnerModule } from '@angular/material';

```

Nous avons importé les modules pour ces composants Material Design :

* [MatToolbar](https://material.angular.io/components/toolbar/overview) qui fournit un conteneur pour les en-têtes, les titres ou les actions.
* [MatCard](https://material.angular.io/components/card/overview) qui fournit un conteneur de contenu pour du texte, des photos et des actions dans le contexte d'un seul sujet.
* [MatButton](https://material.angular.io/components/button/overview) qui fournit un élément natif `<button>` ou `<a>` amélioré avec le style Material Design et les ondulations d'encre.
* [MatProgressSpinner](https://material.angular.io/components/progress-spinner/overview) qui fournit un indicateur circulaire de progression et d'activité.

Ensuite, ajoutez ces modules au tableau `imports` :

```ts
@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AboutComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatCardModule,
    MatProgressSpinnerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

```

Ensuite, ouvrez le fichier `src/app/app.component.html` et mettez-le à jour comme suit :

```html
<mat-toolbar color="primary">  
<h1>  
Mon Magasin Angular  
</h1>  
<button mat-button routerLink="/">Accueil</button>  
<button mat-button routerLink="/about">À propos</button></mat-toolbar><router-outlet></router-outlet>

```

Nous avons ajouté une barre de navigation supérieure avec deux boutons qui nous emmènent respectivement aux pages d'accueil et à propos.

# Étape 7 — Simulation d'une API REST

Allez dans une nouvelle interface de ligne de commande et commencez par installer `json-server` depuis npm dans votre projet :

```bash
$ cd ~/angular-example
$ npm install --save json-server 


```

Ensuite, créez un dossier `server` dans le dossier racine de votre projet Angular :

```bash
$ mkdir server
$ cd server


```

Dans le dossier `server`, créez un fichier `database.json` et ajoutez l'objet JSON suivant :

```json
{
    "products": []
}


```

Ce fichier JSON servira de base de données pour votre serveur API REST. Vous pouvez simplement ajouter des données à servir par votre API REST ou utiliser [Faker.js](https://github.com/marak/Faker.js/) pour générer automatiquement de grandes quantités de fausses données réalistes.

Retournez à votre interface de ligne de commande, naviguez depuis le dossier `server`, et installez `Faker.js` depuis npm en utilisant la commande suivante :

```bash
$ cd ..
$ npm install faker --save


```

Au moment de la création de cet exemple, **faker v4.1.0** sera installé.

Maintenant, créez un fichier `generate.js` et ajoutez le code suivant :

```js
var faker = require('faker');

var database = { products: []};

for (var i = 1; i<= 300; i++) {
  database.products.push({
    id: i,
    name: faker.commerce.productName(),
    description: faker.lorem.sentences(),
    price: faker.commerce.price(),
    imageUrl: "https://source.unsplash.com/1600x900/?product",
    quantity: faker.random.number()
  });
}

console.log(JSON.stringify(database));


```

Nous avons d'abord importé faker, puis nous avons défini un objet avec un tableau vide pour les produits. Ensuite, nous avons entré une boucle _for_ pour créer _300_ entrées fictives en utilisant des méthodes faker comme `faker.commerce.productName()` pour générer des noms de produits. [Vérifiez toutes les méthodes disponibles](https://github.com/marak/Faker.js/#api-methods). Enfin, nous avons converti l'objet de la base de données en une chaîne et l'avons enregistré dans la sortie standard.

Ensuite, ajoutez les scripts `generate` et `server` au fichier `package.json` :

```json
  "scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "test": "ng test",
    "lint": "ng lint",
    "e2e": "ng e2e",
    "generate": "node ./server/generate.js > ./server/database.json",
    "server": "json-server --watch ./server/database.json"
  },


```

Ensuite, retournez à votre interface de ligne de commande et exécutez le script generate en utilisant la commande suivante :

```bash
$ npm run generate


```

Enfin, exécutez le serveur API REST en exécutant la commande suivante :

```bash
$ npm run server


```

Vous pouvez maintenant envoyer des requêtes HTTP au serveur comme à n'importe quel serveur API REST typique. Votre serveur sera disponible à l'adresse `http://localhost:3000/`.

Ce sont les points de terminaison de l'API que nous pourrons utiliser via notre serveur API REST JSON :

* `GET /products` pour obtenir les produits
* `GET /products/<id>` pour obtenir un produit unique par id
* `POST /products` pour créer un nouveau produit
* `PUT /products/<id>` pour mettre à jour un produit par id
* `PATCH /products/<id>` pour mettre à jour partiellement un produit par id
* `DELETE /products/<id>` pour supprimer un produit par id

Vous pouvez utiliser les paramètres `_page` et `_limit` pour obtenir des données paginées. Dans l'en-tête `Link`, vous obtiendrez les liens `first`, `prev`, `next` et `last`.

Laissez le serveur API REST JSON en cours d'exécution et ouvrez une nouvelle interface de ligne de commande pour taper les commandes des étapes suivantes.

# Étape 8 — Création d'un service pour consommer l'API REST avec Angular HttpClient

Dans cette étape, nous apprendrons à consommer notre API REST à partir d'Angular en utilisant HttpClient.

Nous devrons créer un service Angular pour encapsuler le code qui nous permet de consommer des données à partir de notre serveur API REST.

Allez dans votre terminal et exécutez la commande suivante :

```bash
$ ng g service api

```

Ensuite, allez dans le fichier `src/app/api.service.ts`, importez et injectez `HttpClient` :

```ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private SERVER_URL = "http://localhost:3000";

  constructor(private httpClient: HttpClient) { }
}

```

Nous avons importé et injecté le service `HttpClient` et défini la variable `SERVER_URL` qui contient l'adresse de notre serveur API REST.

Ensuite, définissez une méthode `get()` qui envoie une requête GET au point de terminaison de l'API REST :

```ts
import { Injectable } from '@angular/core';  
import { HttpClient } from '@angular/common/http';

@Injectable({  
	providedIn: 'root'  
})  
export class ApiService {

	private SERVER_URL = "http://localhost:3000";
	constructor(private httpClient: HttpClient) { }

	public get(){  
		return this.httpClient.get(this.SERVER_URL);  
	}  
}

```

La méthode appelle simplement la méthode `get()` de `HttpClient` pour envoyer des requêtes GET au serveur API REST.

Ensuite, nous devons maintenant utiliser ce service dans notre composant home. Ouvrez le fichier `src/app/home/home.component.ts`, et importez et injectez le service de données comme suit :

```ts
import { Component, OnInit } from '@angular/core';  
import { ApiService } from '../api.service';

@Component({  
	selector: 'app-home',  
	templateUrl: './home.component.html',  
	styleUrls: ['./home.component.css']  
})  
export class HomeComponent implements OnInit {
	products = [];
	constructor(private apiService: ApiService) { }
	ngOnInit() {
		this.apiService.get().subscribe((data: any[])=>{  
			console.log(data);  
			this.products = data;  
		})  
	}
}

```

Nous avons importé et injecté `ApiService`. Ensuite, nous avons défini une variable `products` et appelé la méthode `get()` du service pour récupérer les données du serveur API REST JSON.

Ensuite, ouvrez le fichier `src/app/home/home.component.html` et mettez-le à jour comme suit :

```html
<div style="padding: 13px;">
    <mat-spinner *ngIf="products.length === 0"></mat-spinner>

    <mat-card *ngFor="let product of products" style="margin-top:10px;">
        <mat-card-header>
            <mat-card-title>{{product.name}}</mat-card-title>
            <mat-card-subtitle>{{product.price}} $/ {{product.quantity}}
            </mat-card-subtitle>
        </mat-card-header>
        <mat-card-content>
            <p>
                {{product.description}}
            </p>
            <img style="height:100%; width: 100%;" src="{{ product.imageUrl }}" />
        </mat-card-content>
        <mat-card-actions>
      <button mat-button> Acheter le produit</button>
    </mat-card-actions>
    </mat-card>
</div>

```

Nous avons utilisé le composant `<mat-spinner>` pour afficher un indicateur de chargement lorsque la longueur du tableau `products` est égale à zéro, c'est-à-dire avant que des données ne soient reçues du serveur API REST.

Ensuite, nous avons itéré sur le tableau `products` et utilisé une carte Material pour afficher le `name`, `price`, `quantity`, `description` et `image` de chaque produit.

Voici une capture d'écran de la page d'accueil après la récupération des données JSON :

![Image](https://miro.medium.com/max/301/0*R7qs5jGg_IlOtTWF)

Ensuite, nous verrons comment ajouter la gestion des erreurs à notre service.

# Étape 9 — Ajout de la gestion des erreurs

Dans cette étape, nous apprendrons à ajouter la gestion des erreurs dans notre exemple.

Allez dans le fichier `src/app/api.service.ts` et mettez-le à jour comme suit :

```ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from "@angular/common/http";

import {  throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private SERVER_URL = "http://localhost:3000/products";

  constructor(private httpClient: HttpClient) { }

  handleError(error: HttpErrorResponse) {
    let errorMessage = 'Erreur inconnue !';
    if (error.error instanceof ErrorEvent) {
      // Erreurs côté client
      errorMessage = `Erreur : ${error.error.message}`;
    } else {
      // Erreurs côté serveur
      errorMessage = `Code d'erreur : ${error.status}\nMessage : ${error.message}`;
    }
    window.alert(errorMessage);
    return throwError(errorMessage);
  }

  public sendGetRequest(){
    return this.httpClient.get(this.SERVER_URL).pipe(catchError(this.handleError));
  }
}
```

Voici une capture d'écran d'une erreur exemple sur la console du navigateur :

![Image](https://miro.medium.com/max/442/0*gZUHzXPjrRSSK4ZF)

Dans l'étape suivante, nous verrons comment ajouter la pagination à notre application.

# Étape 10 — Ajout de la pagination

Dans cette étape, nous apprendrons à ajouter la prise en charge de la pagination des données en utilisant l'en-tête Link de la réponse HTTP reçue du serveur API REST.

Par défaut, HttpClient fournit uniquement le corps de la réponse. Mais dans notre application, nous devons analyser l'en-tête Link pour extraire les liens de pagination. Nous devons donc instruire `HttpClient` de nous donner la réponse [HttpResponse](https://angular.io/api/common/http/HttpResponse) complète en utilisant l'option `observe`.

L'en-tête Link en HTTP permet au serveur de pointer un client intéressé vers une autre ressource contenant des métadonnées sur la ressource demandée. [Wikipedia](https://www.w3.org/wiki/LinkHeader)

Ouvrez le fichier `src/app/data.service.ts` et importez l'opérateur RxJS `tap()` :

```ts
import { retry, catchError, tap } from 'rxjs/operators';

```

Ensuite, ajoutez ces variables :

```ts
public first: string = "";  
public prev: string = "";  
public next: string = "";  
public last: string = "";

```

Ensuite, ajoutez la méthode `parseLinkHeader()` qui sera utilisée pour analyser l'en-tête Link et remplir les variables précédentes :

```ts
  parseLinkHeader(header) {
    if (header.length == 0) {
      return ;
    }

    let parts = header.split(',');
    var links = {};
    parts.forEach( p => {
      let section = p.split(';');
      var url = section[0].replace(/<(.*)>/, '$1').trim();
      var name = section[1].replace(/rel="(.*)"/, '$1').trim();
      links[name] = url;

    });

    this.first  = links["first"];
    this.last   = links["last"];
    this.prev   = links["prev"];
    this.next   = links["next"]; 
  }

```

Ensuite, mettez à jour la méthode `sendGetRequest()` comme suit :

```ts
  public sendGetRequest(){
    // Ajoutez des paramètres _page et _limit encodés en URL sécurisés 

    return this.httpClient.get(this.SERVER_URL, {  params: new HttpParams({fromString: "_page=1&_limit=20"}), observe: "response"}).pipe(retry(3), catchError(this.handleError), tap(res => {
      console.log(res.headers.get('Link'));
      this.parseLinkHeader(res.headers.get('Link'));
    }));
  }
```

Nous avons ajouté l'option `observe` avec la valeur `response` dans le paramètre d'options de la méthode `get()` afin de pouvoir avoir la réponse HTTP complète avec les en-têtes. Ensuite, nous utilisons l'opérateur RxJS `tap()` pour analyser l'en-tête Link avant de retourner l'Observable final.

Puisque la méthode `sendGetRequest()` retourne maintenant un Observable avec une réponse HTTP complète, nous devons mettre à jour le composant home. Ouvrez donc le fichier `src/app/home/home.component.ts` et importez `HttpResponse` comme suit :

```ts
import { HttpResponse } from '@angular/common/http';

```

Ensuite, mettez à jour la méthode `subscribe()` comme suit :

```ts
ngOnInit(){

this.apiService.sendGetRequest().pipe(takeUntil(this.destroy$)).subscribe((res: HttpResponse<any>)=>{  
	console.log(res);  
	this.products = res.body;  
})  
}

```

Nous pouvons maintenant accéder aux données à partir de l'objet `body` de la réponse HTTP reçue.

Ensuite, retournez au fichier src/app/data.service.ts et ajoutez la méthode suivante :

```ts
public sendGetRequestToUrl(url: string){  
	return this.httpClient.get(url, { observe: "response"}).pipe(retry(3), 			
	catchError(this.handleError), tap(res => {  
		console.log(res.headers.get('Link'));  
		this.parseLinkHeader(res.headers.get('Link'));
	}));  
}

```

Cette méthode est similaire à `sendGetRequest()` sauf qu'elle prend l'URL à laquelle nous devons envoyer une requête HTTP GET.

Retournez au fichier `src/app/home/home.component.ts` et définissez les méthodes suivantes :

```ts
 public firstPage() {
    this.products = [];
    this.apiService.sendGetRequestToUrl(this.apiService.first).pipe(takeUntil(this.destroy$)).subscribe((res: HttpResponse<any>) => {
      console.log(res);
      this.products = res.body;
    })
  }
  public previousPage() {

    if (this.apiService.prev !== undefined && this.apiService.prev !== '') {
      this.products = [];
      this.apiService.sendGetRequestToUrl(this.apiService.prev).pipe(takeUntil(this.destroy$)).subscribe((res: HttpResponse<any>) => {
        console.log(res);
        this.products = res.body;
      })
    }

  }
  public nextPage() {
    if (this.apiService.next !== undefined && this.apiService.next !== '') {
      this.products = [];
      this.apiService.sendGetRequestToUrl(this.apiService.next).pipe(takeUntil(this.destroy$)).subscribe((res: HttpResponse<any>) => {
        console.log(res);
        this.products = res.body;
      })
    }
  }
  public lastPage() {
    this.products = [];
    this.apiService.sendGetRequestToUrl(this.apiService.last).pipe(takeUntil(this.destroy$)).subscribe((res: HttpResponse<any>) => {
      console.log(res);
      this.products = res.body;
    })
  }
```

Enfin, ouvrez le fichier `src/app/home/home.component.html` et mettez à jour le modèle comme suit :

```html
<div style="padding: 13px;">
    <mat-spinner *ngIf="products.length === 0"></mat-spinner>

    <mat-card *ngFor="let product of products" style="margin-top:10px;">
        <mat-card-header>
            <mat-card-title>#{{product.id}} {{product.name}}</mat-card-title>
            <mat-card-subtitle>{{product.price}} $/ {{product.quantity}}
            </mat-card-subtitle>
        </mat-card-header>
        <mat-card-content>
            <p>
                {{product.description}}
            </p>
            <img style="height:100%; width: 100%;" src="{{ product.imageUrl }}" />
        </mat-card-content>
        <mat-card-actions>
      <button mat-button> Acheter le produit</button>
    </mat-card-actions>
    </mat-card>

</div>
<div>
    <button (click) ="firstPage()" mat-button> Première</button>
    <button (click) ="previousPage()" mat-button> Précédente</button>
    <button (click) ="nextPage()" mat-button> Suivante</button>
    <button (click) ="lastPage()" mat-button> Dernière</button>
</div>
```

Voici une capture d'écran de notre application :

![Image](https://miro.medium.com/max/17/0*c_21mFswM-ZiReUi?q=20)

![Image](https://miro.medium.com/max/297/0*c_21mFswM-ZiReUi)

# Étape 11 — Construction et déploiement de votre application Angular sur Firebase

Retournez à votre interface de ligne de commande. Assurez-vous d'être dans le dossier racine de votre projet Angular et exécutez la commande suivante :

```bash
$ ng add @angular/fire


```

Cela ajoutera la capacité de déploiement Firebase à votre projet.

Au moment de la rédaction de ce tutoriel, **@angular/fire v5.2.1** sera installé.

La commande mettra également à jour le fichier `package.json` de notre projet en ajoutant cette section :

```json
        "deploy": {
          "builder": "@angular/fire:deploy",
          "options": {}
        }


```

L'interface de ligne de commande vous demandera de **Coller le code d'autorisation ici :** et ouvrira votre navigateur web par défaut pour vous demander de donner à Firebase CLI les permissions d'administrer votre compte Firebase.

Après vous être connecté avec le compte Google associé à votre compte Firebase, vous recevrez le code d'autorisation.

Ensuite, vous serez invité à **Veuillez sélectionner un projet : (Utilisez les touches fléchées ou tapez pour rechercher)**. Vous devriez avoir créé un projet Firebase au préalable.

L'interface de ligne de commande créera les fichiers `firebase.json` et `.firebaserc` et mettra à jour le fichier `angular.json` en conséquence.

Ensuite, déployez votre application sur Firebase en utilisant la commande suivante :

```bash
$ ng deploy


```

La commande produira une version optimisée de votre application (équivalente à la commande `ng deploy --prod`). Elle téléchargera les ressources de production sur l'hébergement Firebase.

# Conclusion

Tout au long de ce tutoriel étape par étape, vous avez appris à construire une application Angular à partir de zéro en utilisant la dernière version d'Angular 8.3+.

Vous avez appris à simuler un backend d'API REST pour votre application Angular avec presque zéro ligne de code.

Vous avez appris comment créer un projet en utilisant Angular CLI, ajouter `HttpClient` et Angular Material pour envoyer des requêtes HTTP à votre backend d'API REST simulé, et styliser l'interface utilisateur avec des composants Material Design.

Enfin, vous avez appris à déployer votre application Angular sur Firebase en utilisant la commande `ng deploy` disponible à partir d'Angular 8.3+.

Consultez nos autres [tutoriels Angular](https://www.techiediaries.com/angular).

Vous pouvez contacter ou suivre l'auteur via :

* [Site web personnel](https://www.ahmedbouchefra.com/)
* [Twitter](https://twitter.com/ahmedbouchefra)
* [LinkedIn](https://www.linkedin.com/in/mr-ahmed/)
* [Github](https://github.com/techiediaries)
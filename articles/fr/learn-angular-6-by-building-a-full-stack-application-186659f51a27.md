---
title: Apprendre Angular 6 en construisant une application full-stack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-30T21:34:49.000Z'
originalURL: https://freecodecamp.org/news/learn-angular-6-by-building-a-full-stack-application-186659f51a27
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca8b7740569d1a4ca7fcc.jpg
tags:
- name: Angular
  slug: angular
- name: Apps
  slug: apps-tag
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Apprendre Angular 6 en construisant une application full-stack
seo_desc: 'By Ahmed Bouchefra

  Angular 6 is out! The new features include better performance, new powerful CLI
  additions and a new way to inject services.

  This tutorial is for beginners. You’ll learn Angular by example by building a full-stack
  CRUD — Create, Rea...'
---

Par Ahmed Bouchefra

Angular 6 est sorti ! Les nouvelles fonctionnalités incluent de meilleures performances, de nouvelles additions puissantes à la CLI et une nouvelle façon d'injecter des services.

Ce tutoriel est destiné aux débutants. Vous apprendrez Angular par l'exemple en construisant une application web full-stack CRUD — Create, Read, Update et Delete. Nous utiliserons la dernière version du framework et de la plateforme les plus populaires pour construire des applications client-side mobiles et de bureau. Le nom de ces applications est SPA ou Single Page Applications.

En back-end, nous utiliserons Python avec Django. Django est le framework web pythonique le plus populaire, conçu pour les perfectionnistes avec des délais serrés.

En résumé, vous apprendrez à générer des applications Angular 6, à générer des composants et des services, et à ajouter le routage. Vous apprendrez également à utiliser diverses fonctionnalités telles que **HttpClient** pour envoyer des requêtes AJAX et des appels HTTP et vous abonner aux observables RxJS 6, etc.

À la fin de ce tutoriel Angular *6*, vous apprendrez en construisant une application exemple du monde réel :

* comment installer la dernière version d'Angular CLI,

* comment utiliser Angular 6 CLI pour générer un nouveau projet Angular *6*,

* comment utiliser Angular 6 pour construire une application CRM simple,

* qu'est-ce qu'un composant et une architecture basée sur les composants

* comment utiliser les observables RxJS 6 et les opérateurs (`map()` et `filter()` etc.)

* comment créer des composants Angular 6,

* comment ajouter le routage et la navigation des composants,

* comment utiliser **HttpClient** pour consommer une API REST, etc.

### Le back-end CRUD Django

Nous utiliserons une API CRUD simple construite avec Django et Django REST framework. Comme il s'agit d'un tutoriel Angular, nous ne nous concentrerons pas sur la construction de l'API. Cela fera l'objet d'un tutoriel séparé. Vous pouvez obtenir le code source de l'API back-end à partir de ce [dépôt](https://github.com/techiediaries/django-crm).

Vous pouvez utiliser les commandes suivantes pour démarrer le serveur de développement :

```bash
# Clonez le projet et naviguez dedans
$ git clone https://github.com/techiediaries/django-crm
$ cd django-crm

# Créez un environnement virtuel et installez les packages
$ pipenv install

# Activez l'environnement virtuel
$ pipenv shell 

# Créez et migrez la base de données, puis lancez le serveur de développement local
$ python manage.py migrate
$ python manage.py runserver
```

Votre serveur sera en cours d'exécution sur [`http://localhost:8000`](http://localhost:8000).

Nous utilisons [pipenv](https://github.com/pypa/pipenv), l'outil de gestion de pa[ckage](https://github.com/pypa/pipenv) officiellement recommandé pour [Pyth](https://github.com/pypa/pipenv)on. Vous devez l'avoir installé. Le processus est assez simple selon votre système d'exploitation.

### Exemple CRUD Angular 6

L'application exemple Angular 6 que nous allons construire est le front-end pour une API RESTful CRM. Elle vous permettra de créer des comptes, des leads, des opportunités et des contacts. C'est un exemple parfait pour une application CRUD (Create, Read, Update et Delete) construite en tant que SPA (Single Page Application).

L'application exemple est en cours de développement, nous allons donc la construire à travers une série de tutoriels. Elle sera mise à jour pour contenir des fonctionnalités avancées telles que RxJS 6 et l'authentification JWT. Nous utiliserons également Bootstrap 4 et Angular 6 Material pour construire et styliser les composants UI. Vous avez besoin soit de Bootstrap 4, soit d'Angular Material pour le stylage. Selon votre choix, vous pouvez suivre des tutoriels séparés :

* [Construire l'UI avec Angular 6 Material](https://www.techiediaries.com/angular-material-tutorial-example/)

* [Construire l'UI avec Bootstrap 4](https://www.techiediaries.com/angular-bootstrap-tutorial)

### Installation de l'Angular CLI (v6.0.0)

Assurez-vous d'avoir Node.js installé, puis exécutez la commande suivante dans votre terminal pour installer Angular CLI **v 6.0.0**.

```bash
npm -g install @angular/cli
```

Vous pouvez vérifier la version installée en exécutant la commande suivante :

Voici le résultat que j'obtiens :

```bash
/ \   _ __   __ _ _   _| | __ _ _ __     / ___| |   |_ _|
   / △ \ | '_ \ / _` | | | | |/ _` | '__|   | |   | |    | |
  / ___ \| | | | (_| | |_| | | (_| | |      | |___| |___ | |
 /_/   \_\_| |_|\__, |\__,_|_|\__,_|_|       \____|_____|___|
                |___/


Angular CLI: 6.0.0
Node: 8.11.1
OS: linux x64
Angular: 
... 

Package                      Version
------------------------------------------------------
@angular-devkit/architect    0.6.0
@angular-devkit/core         0.6.0
@angular-devkit/schematics   0.6.0
@schematics/angular          0.6.0
@schematics/update           0.6.0
rxjs                         6.1.0
typescript                   2.7.2
```

Maintenant, vous êtes prêt à créer un projet en utilisant Angular CLI v6. Exécutez simplement la commande suivante dans votre terminal :

La CLI générera automatiquement un ensemble de fichiers communs à la plupart des projets Angular 6. Elle installera également les dépendances requises pour votre projet.

Nous travaillerons principalement dans le dossier `src/app`. Voici la structure de répertoires du projet :

![Image](https://cdn-media-1.freecodecamp.org/images/1OuZ0EA4e-yuoGow6JYttg8exNjtaHttb3Gi align="left")

Vous pouvez servir votre appl[ication localement en exécutant les](https://www.techiediaries.com/angular-material-tutorial-example/)[commandes suivantes :](https://www.techiediaries.com/angular-bootstrap-tutorial)

```bash
# Naviguez dans le dossier de votre projet
$ cd crmapp

# Servez votre application
$ ng serve
```

Votre application sera en cours d'exécution sur [`http://localhost:4200`](http://localhost:4200).

Voici une capture d'écran de la page d'accueil de l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/dW4qMtop93Jypfn7Jp7nZPCxarjTgK6B6EiU align="left")

### Composants dans Angular 6|5|4

Maintenant, qu'est-ce qu'un composant ?

Un composant est une classe TypeScript. Il a un modèle HTML et un ensemble optionnel de styles CSS qui contrôlent une partie de l'écran.

Les composants sont le concept le plus important dans Angular 6. Une application Angular 6 est essentiellement un arbre de composants avec un composant racine (le célèbre *AppComponent*). Le composant racine est celui contenu dans le tableau de bootstrap dans le module principal `NgModule` `app.module.ts`.

Un aspect important des composants est la réutilisabilité. Un composant peut être réutilisé dans toute l'application et même dans d'autres applications. Le code commun et répétable qui effectue une certaine tâche peut être encapsulé dans un composant réutilisable. Ce composant peut être appelé chaque fois que nous avons besoin de la fonctionnalité qu'il fournit.

> *Chaque composant bootstrappé est la base de son propre arbre de composants. L'insertion d'un composant bootstrappé déclenche généralement une cascade de créations de composants qui remplissent cet arbre.* [*Source*](https://angular.io/guide/bootstrapping#the-bootstrap-array)

### Architecture basée sur les composants

Une application Angular est composée de plusieurs composants. Ces composants forment une structure arborescente avec des composants parents et enfants.

Un composant est un bloc indépendant d'un grand système (application web). Il communique avec les autres blocs de construction (composants) du système en utilisant des entrées et des sorties. Un composant a une vue associée, des données et un comportement. Il peut avoir des composants parents et enfants.

Les composants permettent une réutilisabilité maximale, des tests faciles, une maintenance et une séparation des préoccupations.

Voyons maintenant cela en pratique. Rendez-vous dans le dossier de votre projet d'application Angular et ouvrez le dossier `src/app`. Vous trouverez les fichiers suivants :

* `app.component.css` : le fichier CSS pour le composant

* `app.component.html` : la vue HTML pour le composant

* `app.component.spec.ts` : les tests unitaires ou le fichier de spécification pour le composant

* `app.component.ts` : le code du composant (données et comportement)

* `app.module.ts` : le module principal de l'application

À l'exception du dernier fichier qui contient la déclaration du module principal (racine) de l'application, tous ces fichiers sont utilisés pour créer un composant. C'est le **AppComponent** : le composant racine de notre application. Tous les autres composants que nous allons créer ensuite seront des enfants directs ou indirects du composant racine.

### Démystifier le AppComponent (Le composant racine des applications Angular)

Allez-y et ouvrez le fichier `src/app/app.component.ts` et comprenons le code derrière le composant principal/racine de l'application.

Tout d'abord, voici le code :

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'app';
}
```

Nous importons d'abord le décorateur Component de `@angular/core`. Ensuite, nous l'utilisons pour décorer la classe TypeScript *AppComponent*. Le décorateur Component prend un objet avec de nombreux paramètres tels que :

* *selector* : spécifie la balise qui peut être utilisée pour appeler ce composant dans les modèles HTML, tout comme les balises HTML standard

* *templateUrl* : indique le chemin du modèle HTML qui sera utilisé pour afficher ce composant (vous pouvez également utiliser le paramètre *template* pour inclure le modèle en ligne sous forme de chaîne)

* *styleUrls* : spécifie un tableau d'URL pour les feuilles de style CSS du composant

Le mot-clé *export* est utilisé pour exporter le composant afin qu'il puisse être importé depuis d'autres composants et modules dans l'application.

La variable *title* est une variable membre qui contient la chaîne 'app'. Il n'y a rien de spécial à propos de cette variable et elle ne fait pas partie de la définition canonique d'un composant Angular.

Maintenant, voyons le modèle correspondant pour ce composant. Si vous ouvrez `src/app/app.component.html`, voici ce que vous trouverez :

```html
<div style="text-align: center">
  <h1>Welcome to !</h1>
  <img width="300" alt="Angular Logo" src="data:image/svg+xml;...." />
</div>

<h2>Here are some links to help you start:</h2>
<ul>
  <li>
    <h2>
      <a target="_blank" rel="noopener" href="https://angular.io/tutorial"
        >Tour of Heroes</a
      >
    </h2>
  </li>
  <li>
    <h2>
      <a
        target="_blank"
        rel="noopener"
        href="https://github.com/angular/angular-cli/wiki"
        >CLI Documentation</a
      >
    </h2>
  </li>
  <li>
    <h2>
      <a target="_blank" rel="noopener" href="https://blog.angular.io/"
        >Angular blog</a
      >
    </h2>
  </li>
</ul>
```

Le modèle est un fichier HTML normal (presque toutes les balises HTML sont valides pour être utilisées dans les modèles Angular, à l'exception de certaines balises telles que `<script>`, `<html>` et `<body>`) avec l'exception qu'il peut contenir des variables de modèle (dans ce cas, la variable *title*) ou des expressions (`{ {...}}`) qui peuvent être utilisées pour insérer des valeurs dans le DOM de manière dynamique. Cela s'appelle **interpolation** ou **data binding**. Vous pouvez trouver plus d'informations sur les modèles dans la [documentation](https://angular.io/guide/template-syntax).

Vous pouvez également utiliser d'autres composants directement dans les modèles Angular (via la propriété selector) tout comme le HTML normal.

Si vous êtes fam[ilia](https://angular.io/guide/template-syntax)r avec le modèle MVC (Model View Controller), la classe de composant joue le rôle du Controller. Le modèle HTML joue le rôle de la Vue.

### Composants Angular 6 par exemple

Après avoir compris la théorie derrière les composants Angular, créons maintenant les composants pour notre application CRM simple.

Notre API REST, construite avec Django, expose ces endpoints :

* `/api/accounts` : créer ou lire une liste paginée de comptes

* `/api/accounts/<id>` : lire, mettre à jour ou supprimer un compte

* `/api/contacts` : créer ou lire une liste paginée de contacts

* `/api/contacts/<id>` : lire, mettre à jour ou supprimer un contact

* `/api/leads` : créer ou lire une liste paginée de leads

* `/api/leads/<id>` : lire, mettre à jour ou supprimer un lead

* `/api/opportunities` : créer ou lire une liste paginée d'opportunités

* `/api/opportunities/<id>` : lire, mettre à jour ou supprimer une opportunité

Avant d'ajouter le routage à notre application, nous devons d'abord créer les composants de l'application. Sur la base de l'architecture de l'API REST exposée, nous pouvons diviser notre application en ces composants :

* `AccountListComponent` : ce composant affiche et contrôle une liste tabulaire de comptes

* `AccountCreateComponent` : ce composant affiche et contrôle un formulaire pour créer ou mettre à jour des comptes

* `ContactListComponent` : affiche un tableau de contacts

* `ContactCreateComponent` : affiche un formulaire pour créer ou mettre à jour un contact

* `LeadListComponent` : affiche un tableau de leads

* `LeadCreateComponent` : affiche un formulaire pour créer ou mettre à jour un lead

* `OpportunityListComponent` : affiche un tableau d'opportunités

* `OpportunityCreateComponent` : affiche un formulaire pour créer ou mettre à jour une opportunité

Utilisons l'Angular CLI pour créer les composants

```bash
ng generate component AccountList
ng generate component AccountCreate

ng generate component ContactList
ng generate component ContactCreate

ng generate component LeadList
ng generate component LeadCreate

ng generate component OpportunityList
ng generate component OpportunityCreate
```

Voici le résultat de la première commande :

```bash
CREATE src/app/account-list/account-list.component.css (0 bytes) CREATE src/app/account-list/account-list.component.html (31 bytes) CREATE src/app/account-list/account-list.component.spec.ts (664 bytes) CREATE src/app/account-list/account-list.component.ts (292 bytes) UPDATE src/app/app.module.ts (418 bytes)
```

Vous pouvez voir que la commande génère tous les fichiers pour définir un composant et met également à jour `src/app/app.module.ts`.

Si vous ouvrez `src/app/app.module.ts` après avoir exécuté toutes les commandes, vous pouvez voir que tous les composants sont automatiquement ajoutés au tableau *AppModule* `declarations`.:

```typescript
import { BrowserModule } from  '@angular/platform-browser';

import { NgModule } from  '@angular/core';



import { AppComponent } from  './app.component';

import { AccountListComponent } from  './account-list/account-list.component';

import { AccountCreateComponent } from  './account-create/account-create.component';

import { ContactListComponent } from  './contact-list/contact-list.component';

import { ContactCreateComponent } from  './contact-create/contact-create.component';

import { LeadListComponent } from  './lead-list/lead-list.component';

import { LeadCreateComponent } from  './lead-create/lead-create.component';

import { OpportunityListComponent } from  './opportunity-list/opportunity-list.component';

import { OpportunityCreateComponent } from  './opportunity-create/opportunity-create.component';

@NgModule({

declarations: [
    AppComponent,
    AccountListComponent,
    AccountCreateComponent,
    ContactListComponent,
    ContactCreateComponent,
    LeadListComponent,
    LeadCreateComponent,
    OpportunityListComponent,
    OpportunityCreateComponent
],
imports: [
    BrowserModule
],
providers: [],
bootstrap: [AppComponent]
})
export  class  AppModule { }
```

Si vous créez des composants manuellement, vous devez vous assurer de les inclure manuellement afin qu'ils puissent être reconnus comme faisant partie du module.

### Ajout du routage Angular 6

Angular CLI fournit l'option `--routing` (`ng new crmapp --routing`) qui vous permet d'ajouter le routage automatiquement. Nous allons ajouter le routage manuellement. Je veux que vous compreniez les différentes pièces impliquées dans l'ajout du routage des composants à votre application Angular.

En fait, ajouter le routage est assez simple :

* ajoutez un module séparé (qui peut être appelé `AppRoutingModule`) dans un fichier `app-routing.module.ts`, et importez le module en l'incluant dans les `imports` du module principal `AppModule`,

* ajoutez `<router-outlet></router-outlet>` dans `app.component.html` (c'est là que le routeur Angular insérera les composants correspondant au chemin actuel),

* ajoutez des routes (chaque route est un objet avec des propriétés telles que *path* et *component* etc.).

Voici le contenu initial de `app-routing.module.ts` :

```typescript
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

Le tableau *routes* contiendra toutes les routes de l'application. Après avoir créé les composants, nous verrons comment ajouter des routes à ce tableau.

Pour l'instant, nous voulons rediriger le visiteur vers le chemin `/accounts` lorsque l'URL de la page d'accueil est visitée, donc le premier chemin que nous ajouterons est :

```typescript
{ path: '', redirectTo: 'accounts', pathMatch: 'full' },
```

Le *pathMatch* spécifie la stratégie de correspondance. `full` signifie que nous voulons correspondre pleinement au chemin.

Ensuite, ajoutons les autres chemins :

```typescript
{ path:  '', redirectTo:  'accounts', pathMatch:  'full' },
{
    path:  'accounts',
    component:  AccountListComponent
},
{
    path:  'create-account',
    component:  AccountCreateComponent
},
{
    path:  'contacts',
    component:  ContactListComponent
},
{
    path:  'create-contact',
    component:  ContactCreateComponent
},
{
    path:  'leads',
    component:  LeadListComponent
},
{
    path:  'create-lead',
    component:  LeadCreateComponent
},
{
    path:  'opportunities',
    component:  OpportunityListComponent
},
{
    path:  'create-opportunity',
    component:  OpportunityCreateComponent
}

];
```

Maintenant, ouvrez `src/app/app.module.ts` et importez le module de routage, puis ajoutez-le au tableau *imports* :

```typescript
import {AppRoutingModule} from  './app-routing.module';
[...]

@NgModule({

declarations: [

AppComponent,
[...]
],

imports: [
    BrowserModule,
    AppRoutingModule
],
[...]
})
export  class  AppModule { }
```

Enfin, ouvrez `src/app/app.component.html`, puis ajoutez les liens de navigation et le router outlet :

```html
<a [routerLink]="'/accounts'"> Accounts </a>
<a [routerLink]="'/create-account'"> Create Account </a>

<a [routerLink]="'/contacts'"> Contacts </a>
<a [routerLink]="'/create-contact'"> Create Contact </a>

<a [routerLink]="'/leads'"> Leads </a>
<a [routerLink]="'/create-lead'"> Create Lead </a>

<a [routerLink]="'/opportunities'"> Opportunities </a>
<a [routerLink]="'/create-opportunity'"> Create Opportunity </a>

<div>
    <router-outlet></router-outlet>
</div>
```

### **Un exemple de consommation de l'API REST en utilisant Angular 6 HttpClient**

Maintenant que nous avons créé les différents composants et ajouté le routage et la navigation, voyons un exemple de la façon d'utiliser le *HttpClient* d'Angular 6 pour consommer le back-end de l'API RESTful.

Tout d'abord, vous devez ajouter le module *HttpClientModule* au tableau *imports* du module principal de l'application :

```typescript
[..]
import { HttpClientModule } from  '@angular/common/http';

@NgModule({

declarations: [
..
],

imports: [

[..]

HttpClientModule
],
providers: [],
bootstrap: [AppComponent]

})

export  class  AppModule { }
```

### Créer un service/fournisseur Angular 6

Un service est une classe globale qui peut être injectée dans n'importe quel composant. Il est utilisé pour encapsuler le code qui peut être commun entre plusieurs composants en un seul endroit au lieu de le répéter dans divers composants.

Maintenant, créons un service qui encapsule tout le code nécessaire pour interagir avec l'API REST. En utilisant Angular CLI, exécutez la commande suivante :

Deux fichiers : `src/app/api.service.ts` et `src/app/api.service.spec.ts` seront générés. Le premier contient le code pour le service et le second contient les tests.

Ouvrez `src/app/api.service.ts`, puis importez et injectez la classe *HttpClient*.

```typescript
import { Injectable } from  '@angular/core';
import { HttpClient} from  '@angular/common/http';

@Injectable({
providedIn:  'root'
})

export  class  APIService {

    constructor(private  httpClient:  HttpClient) {}

}
```

Angular 6 fournit un moyen d'enregistrer les services/fournisseurs directement dans le décorateur `@Injectable()` en utilisant le nouvel attribut `providedIn`. Cet attribut accepte n'importe quel module de votre application ou `'root'` pour le module principal de l'application. Maintenant, vous n'avez pas à inclure votre service dans le tableau *providers* de votre module.

### Obtenir des contacts/envoyer une requête HTTP GET

Commençons par l'endpoint de l'API des contacts.

* Tout d'abord, nous ajouterons une méthode pour consommer cet endpoint dans notre service API global,

* ensuite, nous injecterons le service API et appellerons la méthode depuis la classe de composant correspondante (`ContactListComponent`)

* et enfin, nous afficherons le résultat (la liste des contacts) dans le modèle de composant.

Ouvrez `src/app/api.service.ts` et ajoutez la méthode suivante :

```typescript
export  class  APIService {
API_URL  =  'http://localhost:8000';
constructor(private  httpClient:  HttpClient) {}
getContacts(){
    return  this.httpClient.get(`${this.API_URL}/contacts`);
}
```

Ensuite, ouvrez `src/app/contact-list/contact-list.component.ts` et injectez le *APIService*, puis appelez la méthode *getContacts()* :

```typescript
import { Component, OnInit } from  '@angular/core';
import { APIService } from  '../api.service';

@Component({
    selector:  'app-contact-list',
    templateUrl:  './contact-list.component.html',
    styleUrls: ['./contact-list.component.css']
})

export  class  ContactListComponent  implements  OnInit {

private  contacts:  Array<object> = [];
constructor(private  apiService:  APIService) { }
ngOnInit() {
    this.getContacts();
}
public  getContacts(){
    this.apiService.getContacts().subscribe((data:  Array<object>) => {
        this.contacts  =  data;
        console.log(data);
    });
}
```

Maintenant, affichons les contacts dans le modèle. Ouvrez `src/app/contact-list/contact-list.component.html` et ajoutez le code suivant :

```html
<h1>
My Contacts
</h1>
<div>
<table  style="width:100%">
<tr>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Phone</th>
    <th>Email</th>
    <th>Address</th>
</tr>
<tr *ngFor="let contact of contacts">
    <td> {{ contact.first_name }}</td>
    <td> {{ contact.last_name }}  </td>
    <td> {{ contact.phone }}</td>
    <td> {{ contact.email }}  </td>
    <td> {{ contact.address }}</td>
</tr>
</table>

</div>
```

Voici une capture d'écran du composant :

![Image](https://cdn-media-1.freecodecamp.org/images/1INs7KMBCncP2iMNdNiw1LBbIJbxpW6vus4E align="left")

### Créer des contacts/envoyer une requête HTTP POST

Maintenant, créons une méthode pour envoyer une requête HTTP Post afin de créer un contact aléatoire. Ouvrez le fichier de service API et ajoutez la méthode suivante :

```typescript
createContact(contact){
    return  this.httpClient.post(`${this.API_URL}/contacts/`,contact);
}
```

Ensuite, appelons cette méthode depuis le `ContactCreateComponent` pour créer un contact. Tout d'abord, ouvrez `src/app/contact-create/contact-create.component.ts` et ajoutez le code suivant :

```typescript
import { Component, OnInit } from  '@angular/core';
import { APIService } from  '../api.service';


@Component({

selector:  'app-contact-create',

templateUrl:  './contact-create.component.html',

styleUrls: ['./contact-create.component.css']

})

export  class  ContactCreateComponent  implements  OnInit {
constructor(private  apiService:  APIService) { }

ngOnInit() {}

createContact(){

var  contact  = {
    account:  1,
    address:  "Home N 333 Apartment 300",
    createdBy:  1,
    description:  "This is the third contact",
    email:  "abbess@email.com",
    first_name:  "kaya",
    isActive: true,
    last_name: "Abbes",
    phone: "00121212101"
};
this.apiService.createContact(contact).subscribe((response) => {
    console.log(response);
});
};
}
}
```

Pour l'instant, nous codons simplement en dur les informations de contact pour des raisons de simplicité.

Ensuite, ouvrez `src/app/contact-create/contact-create.component.html` et ajoutez un bouton pour appeler la méthode de création d'un contact :

```html
<h1> Create Contact </h1> <button (click)="createContact()"> Create Contact </button>
```

### Conclusion

Tout au long de ce **tutoriel Angular 6** pour débutants, nous avons vu, en construisant un exemple CRUD simple du monde réel, comment utiliser différents concepts Angular pour créer une application full-stack CRUD simple avec Angular et Django. Vous pouvez trouver le code source dans ce [dépôt](https://github.com/techiediaries/ng-crm).
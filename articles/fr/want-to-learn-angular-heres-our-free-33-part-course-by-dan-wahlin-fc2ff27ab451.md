---
title: Apprenez Angular dans ce cours gratuit en 33 parties par l'expert Angular Dan
  Wahlin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-16T05:34:57.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-angular-heres-our-free-33-part-course-by-dan-wahlin-fc2ff27ab451
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SaVwtG8cWgCh1WFYsIa2Fw.png
tags:
- name: Angular
  slug: angular
- name: Angular
  slug: angularjs
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Apprenez Angular dans ce cours gratuit en 33 parties par l'expert Angular
  Dan Wahlin
seo_desc: 'By Per Harald Borgen

  According to the Stack Overflow developer survey 2018, Angular is one of the most
  popular frameworks/libraries among professional developers. So learning it increases
  your chances of getting a job as a web developer significantly...'
---

Par Per Harald Borgen

Selon l'enquête des développeurs [Stack Overflow 2018](https://insights.stackoverflow.com/survey/2018/#most-popular-technologies), Angular est l'un des frameworks/bibliothèques les plus populaires parmi les développeurs professionnels. Ainsi, l'apprendre augmente considérablement vos chances de décrocher un emploi en tant que développeur web.

C'est pourquoi nous nous sommes associés à l'un des experts les plus renommés du framework, et avons créé un [cours Angular gratuit](https://scrimba.com/g/gyourfirstangularapp?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gyourfirstangularapp_launch_article) sur Scrimba.

L'instructeur [Dan Wahlin](https://twitter.com/DanWahlin) est un Google Developer Expert qui a fourni des services de formation, d'architecture et de développement pour certaines des plus grandes entreprises du secteur et a créé certains des cours de formation les plus populaires sur Udemy et Pluralsight. Il est également un intervenant régulier lors de conférences pour développeurs à travers le monde.

[Dans ce cours](https://scrimba.com/g/gyourfirstangularapp?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gyourfirstangularapp_launch_article), Dan vous guide à travers la création de votre toute première application Angular en utilisant TypeScript. En complétant le cours, vous ajouterez des compétences précieuses à votre arsenal.

Maintenant, examinons comment le cours est structuré !

### Partie #1 : Aperçu du cours

![Image](https://cdn-media-1.freecodecamp.org/images/1*mHUNNtNB1aF6s1juYuJ7Jw.png)

Dans la vidéo d'introduction, Dan donne un aperçu du cours, des aspects clés d'Angular, et de la manière dont le cours est organisé. Il vous parle également un peu de son parcours, afin que vous soyez familier avec lui avant de plonger dans le code de votre nouvelle application.

### Partie #2 : Aperçu de l'application

Dans cette partie, Dan nous donne un aperçu de l'application que nous allons construire. Elle est conçue pour nous permettre de nous concentrer sur les éléments clés d'Angular. En créant une application pour afficher les données des clients et leurs commandes, nous nous concentrerons sur les aspects clés d'Angular, tels que les Composants, les Modules, les Services et le Routage. De plus, au cours du cours, nous apprendrons des fonctionnalités essentielles que toute application possède, comme le tri et le filtrage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_bYYJCud9vhxaSSvKmqH6Q.png)

### Partie #3 : Angular CLI

Dans cette partie, nous apprenons les bases de l'utilisation de l'outil Angular CLI (interface de ligne de commande) et passons en revue les commandes de base :

```sh
ng --version  
ng --help  
ng new my-app-name  
ng generate [component | directive | pipe | service | class | interface | enum | guard]  
ng build   
ng serve  
ng lint   
ng tests

```

Par exemple, `ng --new my-app-name` créera une nouvelle application Angular vierge pour nous et nous pouvons utiliser `ng -generate` pour créer des parties de notre application.

`ng build` construira tout pour nous, et `ng serve -o` démarrera même un serveur de développement ainsi qu'une fenêtre de navigateur pour visualiser notre application.

### Partie #4 : Aperçu des fichiers du projet

Dans cette vidéo du cours, Dan donne un aperçu de base de la commande CLI pour générer une application Angular vierge et donne un aperçu rapide des fichiers de configuration comme `tslint`, `tsconfig` et `protractor` dans notre dossier d'application.

### Partie #5 : Le grand tableau

Ici, nous apprenons une abstraction utile selon laquelle les Composants sont similaires à des blocs Lego — nous construisons des composants et les utilisons ensuite pour les assembler afin de créer une application. Nous obtenons également un rappel rapide sur la famille de langages JavaScript et apprenons où TypeScript s'intègre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s2TcwSmQM7_BAA25NC3lVQ.png)

Dan nous donne un bon modèle mental à utiliser pour penser à notre code tout en travaillant avec Angular afin que nous puissions imaginer où tout cela s'intègre.

### Partie #6 : Composants et Modules — Aperçu

Sans abstraction, le diagramme pour le code Angular pourrait ressembler à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OTT4yeJg6630S2I43WRGxg.png)

Les Composants sont constitués de code et de modèle HTML et peuvent avoir un sélecteur, afin que nous puissions l'appeler dans notre HTML.

```html
<appcomponent></appcomponent>

```

Chaque Composant se compose de :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-12cVJ5V8OG1SBWI4hraSg.png)

Dan explique ensuite ce que chaque partie est et comment elles s'intègrent dans la manière Angular de développer des composants. L'une des grandes choses à propos d'Angular est qu'il est très prévisible. Une fois que vous avez appris à créer votre premier composant, vous êtes bien parti pour créer des composants supplémentaires.

### Partie #7 : Composants et Modules — Composant App

Dans cette partie du cours, nous examinons un composant `HelloWorld`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYiWpdm6Aqf4PmcbHdSXGg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*wproObAyLBo-EOBM-r3P8A.png)

Dan décompose chaque aspect du composant pour nous et explique comment il est utilisé et comment notre composant est traité par Angular, comment il est ajouté à `app.module` et finalement comment il est rendu sur nos écrans.

Nous apprenons que `selector: 'app-root'` est ce qui nous permet d'appeler plus tard le composant depuis notre HTML en utilisant `<app-root></app-root>`

Nous avons également un aperçu de la liaison de données, que nous apprendrons davantage dans les chapitres suivants.

### Partie #8 : Composants et Modules — Module App

Dans ce screencast, nous passons plus de temps à apprendre le fonctionnement interne de `app.module`, que nous avons abordé dans le cast précédent, et nous apprenons à connaître `NgModule` et `BrowserModule`.

### Partie #9 : Composants et Modules — Ajout d'un Composant Customers

Dans ce cast, Dan nous donne quelques conseils sur la création de composants en utilisant la CLI, puis montre comment créer des composants manuellement. Nous apprenons à structurer un composant en approfondissant nos connaissances de la Partie #6.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C2YJ7m1pbHjXSHC0Fv0baQ.png)

Maintenant, nous intégrons des données pour imiter notre API et apprenons comment les modules nous aident à garder notre code organisé et plus facile à réutiliser.

### Partie #10 : Composants et Modules — Ajout d'un Composant Liste de Customers

Dans cette partie, nous créons un `customers-list.component` qui est un tableau HTML pour afficher notre liste de clients. Nous nous enregistrons rapidement dans `customers.module` et utilisons le sélecteur `<app-customers-list></app-customers-list>` pour afficher notre tableau vide.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CeqVsl_JlKtnPXzgSVismQ.png)

L'étape suivante serait de remplir le tableau avec des données.

### Partie #11 : Composants et Modules — Ajout d'un Composant Zone de Texte de Filtre

Avant d'ajouter des données à notre tableau, Dan nous montre comment ajouter un `filter-textbox.component` à notre tableau et nous renforçons la manière Angular de créer un composant, de l'enregistrer dans un module et de l'utiliser dans notre HTML avec des sélecteurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b9SgU3SuhQINc87r56DDwg.png)

### Partie #12 : Composants et Modules — Ajout d'un Module Partagé et d'Interfaces

Dans cette section, Dan parle de l'utilisation de `shared.module` — un module où nous mettons des composants ou d'autres fonctionnalités que nous voulons partager dans toute notre application, pas seulement dans `customers`.

Nous avons également un rappel rapide sur les interfaces TypeScript et comment elles peuvent être utilisées dans les applications Angular pour fournir une meilleure aide au code et améliorer la productivité.

```ts
export interface ICustomer {  
    id: number;  
    name: string;  
    city: string;  
    orderTotal?: number;  
    customerSince: any;  
}

```

### Partie #13 : Liaison de Données — Aperçu de la Liaison de Données

Dans ce chapitre, nous apprenons la liaison de données, quelques techniques et voyons comment ajouter la liaison de données à notre application.

Nous lions généralement les données dans nos modèles. La liaison de données entre en jeu lorsqu'un composant obtient nos données et les intègre dans un modèle. Nous pouvons obtenir des données dans un modèle en utilisant `Property Binding`, et gérer les événements utilisateur et obtenir des données hors d'un modèle en utilisant `Event Binding`. Angular fournit une manière robuste et propre d'ajouter la liaison de données dans les modèles qui est rapide et facile à retenir.

Dan nous fournit une diapositive pratique pour retenir la syntaxe requise...

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ft7Mj_TaGsUJ4GRdmJNGPQ.png)

...et certaines sur les directives Angular, par exemple, `ngFor`, utilisée pour parcourir les éléments d'une collection et obtenir certaines propriétés des éléments, et `ngIf` pour ajouter et supprimer un élément HTML du DOM.

### Partie #14 : Liaison de Données — Commencer avec la Liaison de Données

Dans ce cast, nous jouons avec `Property Binding` et `Event Binding` pour mieux comprendre comment ils fonctionnent dans Angular, en utilisant les connaissances du chapitre précédent.

Dan montre comment nous pouvons utiliser la propriété `[hidden]` pour afficher un élément `h1` dynamiquement :

```html
<h1 [hidden]="!isVisible">{{ title }}</h1>

```

Et pour lier les événements DOM tels que le clic :

```html
<button (click)="changeVisibility()">Afficher/Masquer</button>

```

### Partie #15 : Liaison de Données — Directives et Interpolation

Ici, nous examinons l'Interpolation. La logique est que nous devons obtenir des données de chaque client pour générer une ligne de tableau dans un tableau de la Partie #10.

C'est la partie où les choses commencent à s'assembler : nous utilisons la directive `ngFor` pour parcourir chaque client dans `filteredCustomers` et interpoler les données d'un client dans une ligne de tableau. Nous apprenons quelques astuces pour rendre les données conditionnellement en utilisant `ngIf`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xMU7cyyy5ooxLJPBct0PEw.png)

À la fin, nous obtenons un joli tableau !

![Image](https://cdn-media-1.freecodecamp.org/images/1*BO_isrPNvKI9u80bXLOnyA.png)

### Partie #16 : Liaison de Données — Liaison d'Événements

`Event Binding` est crucial lorsque nous devons gérer un événement, comme un mouvement de souris ou un clic. Dans ce screencast, Dan nous guide à travers l'ajout de fonctionnalités pour trier les données dans notre tableau. Nous commencerons dans ce chapitre et le terminerons lorsque nous arriverons à la partie Services de notre cours.

Nous créons un gestionnaire d'événements de remplissage dans notre `customer-list.component` :

```ts
sort(prop: string) {  
     // Un service de tri gérera le tri  
}

```

Ajout de la liaison dans `customers-list.component.html` :

```html
<tr>  
    <th (click)="sort('name')">Nom</th>  
    <th (click)="sort('city')">Ville</th>  
    <th (click)="sort('orderTotal')">Total de la commande</th>  
</tr>

```

### Partie #17 : Liaison de Données — Propriétés d'Entrée

Nous avons des données dans un tableau `people` dans notre `customers.component` et nous devons les passer dans notre tableau `filteredCustomers` dans `customers-list.component`, passant effectivement les données d'un composant parent à un enfant.

Pour cela, nous utiliserons la propriété `Input` d'Angular qui repose sur un décorateur nommé Input() :

```ts
@Input() get customers(): ICustomer[] {  
    return this._customers  
}

set customers(value: ICustomer[]) {  
     if (value) {  
     this.filteredCustomers = this._customers = value;  
     this.calculateOrders();  
     }  
}

```

Et nous nous y lions dans le modèle de notre composant parent pour passer les données du parent à l'enfant (app-customers-list dans ce cas) :

```html
<app-customers-list [customers]="people"></app-customers-list>

```

### Partie #18 : Liaison de Données — Travailler avec les Pipes

Wow ! Nous avons fait du bon travail jusqu'à présent !

![Image](https://cdn-media-1.freecodecamp.org/images/1*v51xQi5Ard63tF0-0dd-2Q.png)

Il y a quelques choses qui peuvent sembler un peu étranges — « john » est en minuscules et nous n'avons pas de symbole « $ » pour afficher la devise dans laquelle nous avons nos commandes.

C'est vraiment la façon dont nous avons nos données, donc nous pourrions simplement aller les mettre à jour directement, ou nous pouvons utiliser une fonctionnalité intégrée d'Angular appelée Pipes pour les mettre à jour pour nous !

Certains des pipes les plus simples ressemblent à ceci :

```ts
{{ cust.name | uppercase }} // rend JOHN  
{{ cust.name | titlecase }} // rend John

```

Mais parfois, vous pourriez vouloir avoir votre propre pipe personnalisé et Dan nous montre comment construire un pipe `capitalize` personnalisé (notez qu'Angular en inclut un appelé `titlecase` — mais nous apprenons ici !) et comment le connecter pour l'utiliser dans notre application.

### Partie #19 : Liaison de Données — Ajout du Filtrage

Dans ce cast, Dan nous guide à travers l'ajout de fonctionnalités à notre `filter-textbox.component` de la Partie #11

Nous apprenons davantage sur les propriétés `Output` et `EventEmitter` d'Angular, créons notre gestionnaire d'événements de filtre et le lions à notre zone de texte de filtre :

```html
<filter-textbox (changed)="filter($event)"></filter-textbox>

```

Et voilà, nous pouvons maintenant filtrer sur les noms de nos clients !

![Image](https://cdn-media-1.freecodecamp.org/images/1*8oM5-CM9n7Ic46M4l4IS8w.png)

### Partie #20 : Services et Http — Aperçu des Services

Dans ce chapitre, nous examinons les Services Angular. L'un des points forts d'Angular est qu'il s'agit d'un framework complet qui fournit un support intégré pour gérer l'état et les objets via des services. Nous avons vu les services dans le diagramme précédemment. Puisque nous ne voulons pas que les composants sachent faire trop de choses, nous nous appuierons sur les services pour communiquer avec le serveur, effectuer des validations ou des calculs côté client, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OTT4yeJg6630S2I43WRGxg.png)

Les composants doivent se concentrer sur la présentation des données et la gestion des événements utilisateur. Lorsque des fonctionnalités supplémentaires doivent être effectuées, ils doivent déléguer aux services pour une application plus maintenable et une meilleure réutilisation du code.

C'est exactement ce que fait un Service — une fonctionnalité réutilisable pour l'application qui ne devrait pas être la préoccupation d'un composant.

Heureusement, Dan nous couvre avec une diapositive pratique à garder à l'esprit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dzy9aUGQUu_RXuQ3Wx6RDg.png)

### Partie #21 : Services et Http — Création et Fourniture d'un Service

Dans un chapitre précédent, nous avons vu une importation de `Injectible` qui est un décorateur qui permet quelque chose appelé Injection de Dépendances ou DI en abrégé (une autre fonctionnalité puissante intégrée à Angular).

Nous utiliserons DI pour accéder à un service `HttpClient` que nous utiliserons pour communiquer avec un service RESTful. Nous ajouterons HttpClient à un constructeur de notre `data.service` et le décorateur `@Injectible()` rendra DI possible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6sbs_J-0b6_SH1XqpB7k-g.png)

### Partie #22 : Services et Http — Appel du Serveur avec HttpClient

Dans ce cast, Dan introduit les Observables de `RxJS` — des extensions réactives pour JavaScript, qui ne font pas partie d'Angular mais sont incluses dans tous les projets Angular par défaut.

Nous utiliserons les Observables pour gérer le code asynchrone. En résumé, cela nous permet de démarrer une opération puis de nous abonner aux données qui sont retournées. Une fois les données revenues du serveur, l'abonnement se termine et nous pouvons nous désabonner.

Dan discute du code nécessaire pour appeler le serveur puis s'abonner à la réponse en utilisant le piping et les opérateurs RxJS.

Voici un exemple de la manière dont nous pouvons obtenir des commandes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LZp4nkmFIm4MGJAhQFU4sA.png)

### Partie #23 : Services et Http — Injection d'un Service dans un Composant

Maintenant que nous avons un moyen d'obtenir les données, nous devons injecter le service dans l'un de nos composants. Nous pouvons maintenant changer `this.people` dans `customers.component` pour qu'il ne soit plus codé en dur et appeler un service pour obtenir les données de cette manière.

Nous devons amener notre `data.service` dans `app.module` puis dans `customers.component` nous pouvons :

```ts
import { DataService } from '../core/data.service';

```

Maintenant, nous pouvons injecter notre `DataService` directement dans le constructeur de notre composant :

```ts
constructor(private dataService: DataService) {}

```

### Partie #24 : Services et Http — Abonnement à un Observable

Maintenant, nous pouvons utiliser notre `dataService` injecté, appeler `getCustomers()` et nous abonner à notre `Observable<ICustomer[]>` pour obtenir les données.

Ce qui est assez simple :

```ts
ngOnInit() {  
    this.title = 'Customers';  
    this.dataService.getCustomers()  
        .subscribe((customers: ICustomer[]) =>  
        this.people = customers);

```

Maintenant, nous avons un dernier service à examiner — `SorterService`

### Partie #25 : Services et Http — Utilisation d'un SorterService

Actuellement, si nous cliquons sur nos en-têtes de colonne, rien ne se passerait.

Dan a gentiment fourni un service préécrit pour nous, que nous pouvons utiliser, donc dans ce chapitre, nous allons pratiquer l'intégration d'un service dans nos composants, dans ce cas, `customers-list.component`.

Comme pour les autres services, nous devons l'importer :

```ts
import { SorterService } from '../../core/sorter.service';

```

Ensuite, nous injectons `SorterService` dans notre constructeur :

```ts
constructor(private sorterService: SorterService) {}

```

L'injection de dépendances rend extrêmement facile l'accès au code réutilisable tel que les services de tri ou de données.

Enfin, nous l'utilisons dans notre fonction `sort()` :

```ts
sort(prop: string) {  
    this.sorterService.sort(this.filteredCustomers, prop);  
}

```

### Partie #26 : Routage — Aperçu du Routage

Ce chapitre introduira le Routage, qui est une partie essentielle des applications modernes. Lorsque vous construisez une application Angular, vous souhaitez afficher différents composants lorsque l'utilisateur interagit avec elle. Dans notre cas, lorsqu'un utilisateur clique sur un Client, nous pourrions vouloir lui montrer les Commandes. Le Routage est un moyen très propre d'y parvenir.

Les routes sont utilisées pour associer une URL spécifique à un composant et dans les prochains chapitres, nous nous concentrerons sur la partie supérieure de notre diagramme Angular.

![Image](https://cdn-media-1.freecodecamp.org/images/1*og4k_DGep_esiA5I1ALgzg.png)

Une partie super géniale du routage est que si un utilisateur marque une URL spécifique, cela le ramènera à un composant spécifique et il n'y a pas besoin de logique complexe d'affichage/masquage.

### Partie #27 : Routage — Création d'un Module de Routage avec des Routes

Nous commençons par une routine de module-conteneur familière et créons un `app-routing.module`.

L'objectif principal du `app-routing.module` est de définir les routes dans un tableau :

```ts
const routes: Routes = [  
    { path: '', pathMatch: 'full', redirectTo: '/customers'},  
    { path: '**', redirectTo: '/customers' }  
];

```

Trois propriétés clés de `routes` sont :

* `path` — où va votre utilisateur, donc `path: ''` serait la racine de votre application. `path: '**'` est un joker. Il est généralement placé en dernier et il est là pour couvrir les cas de toute route non spécifiée dans `routes`
* `pathMatch` — comment la route doit correspondre exactement pour qu'un composant spécifique soit affiché
* `redirectTo` — lorsque qu'un chemin est trouvé, c'est là que nous envoyons l'utilisateur. Dans notre cas, nous les envoyons à `/customers`.

### Partie #28 : Routage — Utilisation de Router Outlet

Pour utiliser le Routage dans Angular dans notre modèle `app.component`, nous remplaçons `<app-customers></app-customers>` par `<router-outlet></router-outlet>`. En fin de compte, ce n'est qu'une manière de dire : « Hé, c'est là qu'un composant ira lorsque nous atteindrons notre route ».

Lorsque nous atteignons une route, alors un composant associé à cette route apparaîtra magiquement à la place de `<router-outlet></router-outlet>`.

### Partie #29 : Routage — Ajout d'un Module de Routage Customers et de Routes

Dans ce chapitre, Dan rassemble toutes les choses et nous connectons une route `/customer` à `customers.component`.

Tout d'abord, nous créons un `customers-routing.module` et pointons notre route de la partie #28 vers `customers.component` comme ceci :

```ts
const routes: Routes = [  
    { path: 'customers', component: CustomersComponent }  
];

```

Et maintenant, lorsque nous tapons « customers » dans la barre d'adresse du navigateur Scrimba, nous obtenons notre `customers.component`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*drUS_faas9AzJIvfW-EKxg.png)

### Partie #30 : Routage — Ajout d'un Composant Orders avec des Routes

Dans ce clip, nous allons rapidement passer en revue comment nous avons fait le routage pour afficher les clients, et maintenant il est temps de faire le routage pour afficher leurs commandes.

Il y a un petit piège cependant. Lorsque nous cliquons sur un client, nous devons afficher les données de commande liées à ce client. Nous devons donc passer des données dynamiques dans notre routage.

Nous pouvons y parvenir en passant un `paramètre de route` dans notre `orders-routing.module` comme ceci :

```ts
const routes: Routes = [  
    { path: 'orders/:id', component: OrdersComponent}  
];

```

Notez la syntaxe `/:id`. Dans le routage, le symbole `:` indique que la valeur qui le suit sera remplacée dynamiquement et `id` est simplement une variable, donc elle peut être n'importe quoi comme `:country` ou `:book`.

### Partie #31 : Routage — Accès aux Paramètres de Route

Dans le screencast précédent, nous avons vu comment créer une route `orders/:id` et maintenant `orders.component` doit somehow récupérer cet `id` et afficher les commandes liées au client. Pour ce faire, nous devons accéder au paramètre de route `id`.

Une façon de le faire serait :

```ts
let id = this.route.paramMap.get('id');

```

L'avantage de cette méthode est que nous pouvons nous abonner à `paramMap` et être notifiés lorsque l'une des données dans `id` change. Mais nous n'en avons besoin qu'une seule fois.

Nous pouvons utiliser `snapshot` pour cela :

```ts
let id = this.route.snapshot.paramMap.get('id')

```

`snapshot` prend simplement une sorte de photo instantanée de votre URL et vous la donne, ce qui est parfait car c'est ce dont nous avons besoin dans cette situation.

Mais maintenant nous avons un problème. Notre `id` est une chaîne, mais pour obtenir une commande de notre `DataService`, il doit être un nombre. Nous pouvons le convertir avec `parseInt()`, mais Dan nous apprend une astuce `+` :

```ts
let id = +this.route.snapshot.paramMap.get('id')

```

Maintenant, nous pouvons appeler `DataService` pour obtenir la commande et la rendre dans `orders.component`.

### Partie #32 : Routage — Lien vers les Routes avec la Directive routerLink

La dernière chose que nous voulons faire est d'ajouter un lien sur le nom d'un client, afin que nous puissions cliquer dessus pour voir leurs commandes.

Dans la partie #28, nous avons ajouté `<router-outlet></router-outlet` et maintenant nous devons simplement dire à notre application que nous voulons afficher `orders.component` lorsque nous naviguons vers `/orders/:id`.

Nous pouvons le faire en ajoutant un lien au nom de notre client dans `customers-list.component.html` dans une ligne où nous mappons toutes les données à afficher. Nous avons déjà notre objet client là, donc nous pouvons simplement passer `id` à notre route.

```html
<a [routerLink]="['/orders', cust.id]">  
    {{ cust.name | capitalize }}  
</a>

```

Maintenant, nous pouvons voir les commandes !

![Image](https://cdn-media-1.freecodecamp.org/images/1*M3o56Z9ikhkMt6tLbndzdQ.png)

Mais comment revenons-nous en arrière ? Nous pourrions cliquer sur le bouton « Retour » du navigateur, mais il est beaucoup plus agréable d'avoir un lien d'application pour cela, maintenant que nous connaissons le routage. Ajoutons-le à `customers-list.component.html` tout en bas.

```html
<a routerLink="/customers">Voir tous les clients</a>

```

### Partie #33 : Résumé du Cours

Très bien fait, nous avons maintenant notre application !

Nous pouvons conclure et faire un rapide récapitulatif des choses faites. N'oubliez pas de regarder le screencast réel du cours, car Dan est un excellent enseignant, donc vous vous amuserez beaucoup à suivre le processus à ses côtés !

Merci, Dan !

![Image](https://cdn-media-1.freecodecamp.org/images/1*TwvG-32iqImuHarf1HKUQg.png)

Si vous êtes intéressé à rester à jour sur les technologies front-end et back-end, assurez-vous de [suivre Dan sur Twitter](https://twitter.com/danwahlin) ! 

Bon codage !

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com) — la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gyourfirstangularapp_launch_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gyourfirstangularapp_launch_article)_
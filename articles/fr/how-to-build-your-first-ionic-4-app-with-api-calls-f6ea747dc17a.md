---
title: Comment créer votre première application Ionic 4 avec des appels API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T16:37:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-first-ionic-4-app-with-api-calls-f6ea747dc17a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cun5ECRCb1_QS4BcQI-r7A.png
tags:
- name: Angular
  slug: angular
- name: Apps
  slug: apps-tag
- name: Ionic Framework
  slug: ionic
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
seo_title: Comment créer votre première application Ionic 4 avec des appels API
seo_desc: 'By Simon Grimm

  So you just noticed that Ionic 4 was released and you finally want to get started
  with cross-platform app development? Well, today is your day! We’ll go through building
  your first Ionic 4 application with HTTP Calls to the Open Movie ...'
---

Par Simon Grimm

Vous venez de remarquer qu'Ionic 4 a été publié et vous souhaitez enfin commencer le développement d'applications multiplateformes ? Eh bien, aujourd'hui est votre jour ! Nous allons passer en revue la création de votre première application Ionic 4 avec des appels HTTP à l'[Open Movie Database](http://www.omdbapi.com/) !

Que vous soyez complètement nouveau dans Ionic ou que vous ayez utilisé des versions précédentes, nous allons passer par toutes les bases. Nous allons couvrir comment configurer **une nouvelle application**, **le routage** et même **les appels API pour afficher des données asynchrones** à l'intérieur de notre application.

Si vous voulez apprendre Ionic encore plus rapidement, vous pouvez également [consulter mon Ionic Academy](https://ionicacademy.com/) qui a été conçu pour des développeurs comme vous !

_Prêt_ ? **C'est parti** !

### Installation de notre application Ionic 4

Si vous êtes nouveau dans Ionic, vous devez vous assurer d'avoir installé le [Node Package Manager](https://www.npmjs.com/get-npm). Si vous avez déjà travaillé avec d'autres technologies web, il y a de fortes chances que vous ayez déjà tout ce dont vous avez besoin.

Si vous n'avez pas non plus utilisé Ionic auparavant, vous devez l'installer via npm. Une fois installé, vous êtes enfin prêt à créer votre projet Ionic 4 !

Pour configurer un projet vide, vous pouvez utiliser l'**Ionic CLI** afin que nous obtenions un nouveau projet Ionic 4 avec support Angular (_vous pourriez également utiliser React ou Vue, un meilleur support arrive plus tard cette année_).

Une fois le projet créé, nous **cd** dans le dossier. Nous utilisons le CLI, qui utilise [Angular CLI](https://cli.angular.io/) sous le capot, pour créer de nouvelles pages pour notre application que nous voulons afficher.

```bash
# Installer Ionic si vous ne l'avez pas déjà fait
npm install -g ionic
 
# Créer une nouvelle application Ionic 4 vide avec support Angular
ionic start movieApp blank --type=angular
cd movieApp
 
# Utiliser le CLI pour générer quelques pages et un service
ionic g page pages/movies
ionic g page pages/movieDetails
ionic g service services/movie
```

Vous pouvez maintenant lancer directement votre application en exécutant la commande suivante à l'intérieur de votre projet :

```bash
ionic serve
```

Cela ouvrira le navigateur avec un aperçu de votre application qui se **rechargera automatiquement** dès que vous changerez quelque chose à l'intérieur de votre projet.

En parlant du projet, nous avons un ensemble de fichiers et de dossiers ici, voyons ce que tout cela signifie. Nous allons nous concentrer sur le dossier **src** de notre application puisque nous n'avons pas à nous soucier du reste pour l'instant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UZ96oo9zs_tdZJtOb7uZeA.png)
_Votre projet Ionic 4_

### App

C'est le dossier où nous allons faire toutes les modifications de code qui suivent plus tard dans ce tutoriel. Il contient déjà un dossier **home** qui est essentiellement une page comme nous en avons créé auparavant. J'aime avoir toutes les pages dans leur propre dossier **pages**, donc vous pouvez également supprimer le dossier home pour l'instant.

Le dossier **pages** contient les vues/pages réelles de notre application, ce qui signifie l'élément que nous verrons à l'écran. Pour l'instant, nous avons déjà 2 pages ici, et chaque page que vous créez avec le CLI vient avec 4 fichiers :

* *.module.ts : Le **module Angular** pour une page. Chaque page est essentiellement son propre module (lié à l'architecture Angular) avec des imports et du style
* *.page.html : Le **balisage HTML** pour une page
* *.page.scss : Le **style** pour la page spécifique (plus sur le style global plus tard)
* *.page.spec.ts : Un fichier de **test** ajouté automatiquement pour votre page. Bien si vous voulez configurer des tests unitaires automatisés
* *.page.ts : Le **contrôleur** pour une page qui contient le code JavaScript qui gère la fonctionnalité

Le dossier **services** contient notre service précédemment créé — il s'agit de structurer votre application selon les meilleures pratiques et de séparer les préoccupations entre la vue et les données réelles de votre application. Le service s'occupera de gérer les appels API et retournera simplement les données à notre vue plus tard !

### Assets

Ce dossier contient toutes les images, polices ou autres assets dont vous aurez besoin pour votre application plus tard.

### Environnements

De temps en temps, votre projet peut avoir un environnement de développement, de staging et de production avec différents serveurs que votre application cible. Le dossier environnement aide à configurer des informations pour différents environnements. Nous pouvons ensuite construire notre application Ionic avec un **flag de ligne de commande** et elle prend automatiquement les bonnes valeurs. Très pratique !

### Thème

Ce dossier ne contient que le **variables.scss** qui contient des informations de couleur prédéfinies d'Ionic. Nous pouvons toujours changer ce fichier et même utiliser un outil comme le [Ionic Color Generator](https://beta.ionicframework.com/docs/theming/color-generator) pour créer notre propre version personnalisée de ce fichier !

En dehors du dossier, nous avons également le **global.scss**. Ici, nous pouvons écrire du SCSS qui sera appliqué globalement à notre application. Nous pouvons également le définir pour une seule page dans leurs propres fichiers de style.

### Autres fichiers

Le plus pertinent des autres fichiers pourrait être le **index.html** car, comme avec tout autre site web, ce fichier marque le point d'entrée de notre application ! Pour l'instant, nous n'avons pas besoin de changer quoi que ce soit ici, alors commençons maintenant à entrer dans le code réel.

### Prérequis Routage et Appels HTTP

Avec Ionic 4, nous passons d'un concept de routage propriétaire au [Angular Router](https://angular.io/guide/router) standard. Le balisage peut sembler un peu plus difficile au début, mais cela a en fait du sens.

Pour toutes les connexions à l'intérieur de votre application, vous configurez **les informations de routage** à l'avance — tout comme vous naviguez sur un site web !

Dans notre application, nous avons besoin de 2 routes :

* **/movies** — Naviguer vers notre première page qui devrait afficher une liste de films
* **/movies/:id** — Nous voulons pouvoir afficher les détails pour un film, donc nous ajoutons un paramètre **:id** à la route que nous pouvons résoudre dynamiquement

Nous devons également connecter la page correspondante (_plus spécifique_ : le module de la page) à la route afin qu'Angular sache comment résoudre une route spécifique. Nous fournissons cette information en utilisant **loadChildren** qui ne reçoit en fait qu'une **chaîne de caractères vers le chemin du module**.

Cela signifie que nous n'importons pas vraiment un autre module ici, donc les pages utilisent le **chargement paresseux**. Cela signifie qu'elles ne seront chargées que lorsque nous naviguerons vers elles !

Pour configurer nos informations de routage, ouvrez notre **app/app-routing.module.ts** et modifiez-le comme suit :

```ts
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
 
const routes: Routes = [
  { path: '', redirectTo: 'movies', pathMatch: 'full' },
  { path: 'movies', loadChildren: './pages/movies/movies.module#MoviesPageModule' },
  { path: 'movies/:id', loadChildren: './pages/movie-details/movie-details.module#MovieDetailsPageModule' }
];
 
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

En apportant cette modification, nous avons également déconnecté la page d'accueil qui était initialement dans le projet (et que vous avez peut-être déjà supprimée à ce stade).

Maintenant, l'application chargera notre page de films comme première page, super ! Vous devriez également remarquer ce changement dans votre instance en cours d'exécution `ionic serve`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0pgOz4DuqJnGR1gFFUEfcA.png)

**Astuce :** Si vous voulez avoir une meilleure idée de l'apparence de votre application sur un appareil réel, vous pouvez également exécuter `ionic lab` au lieu de serve, mais vous devez installer le package au préalable :

```bash
# Installer le package Lab

npm i @ionic/lab

# Exécuter votre application avec un aperçu de l'appareil et les styles de plateforme

ionic lab
```

Ce package était précédemment inclus avec chaque nouvelle application mais doit être installé pour Ionic 4 maintenant.

**/Fin de l'astuce**

Nous devons également appliquer une autre modification à notre application car nous voulons effectuer des **appels HTTP**. Par conséquent, nous devons importer un autre module Angular pour effectuer ces requêtes.

La manière de faire cela est la même qu'avec Ionic 3. Nous devons simplement ajouter le `HttpClientModule` à notre fichier de module principal et l'ajouter au **tableau des imports** comme ceci dans notre **app/app.module.ts** :

```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';
 
import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
 
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
 
import { HttpClientModule } from '@angular/common/http';
 
@NgModule({
  declarations: [AppComponent],
  entryComponents: [],
  imports: [BrowserModule, IonicModule.forRoot(), AppRoutingModule, HttpClientModule],
  providers: [
    StatusBar,
    SplashScreen,
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

Avant de plonger dans plus de code Ionic 4, nous devons d'abord configurer le service qui alimente notre application et gère toutes les requêtes HTTP que nous voulons appeler plus tard.

### Faire des requêtes HTTP

Un service est le même qu'un fournisseur dans les versions précédentes et peut être injecté dans notre contrôleur afin d'appeler ses fonctions.

Pour utiliser l'Open Movie Database, vous devez [demander une clé API](http://www.omdbapi.com/apikey.aspx) et l'insérer dans notre service — le processus est gratuit, alors allez-y dès maintenant.

Avec l'API, nous pouvons maintenant rechercher des chaînes et obtenir des résultats sous forme de films, d'épisodes ou même de jeux. De plus, nous pouvons obtenir des informations détaillées pour un objet spécifique de ces résultats, donc un cas d'utilisation parfait pour notre première application Ionic 4 !

Notre service n'a besoin que de 2 fonctions :

* `searchData()` : Cette fonction recherche des résultats pour un titre et un type de recherche spécifiques — une énumération que nous avons définie à l'avance pour représenter les types que nous pouvons passer à l'API en utilisant TypeScript !
* `getDetails()` : Cette fonction retourne les informations détaillées pour un élément spécifique, sera utilisée sur notre page de détails

Les deux fonctions retourneront un `Observable` qui est comme une Promesse sur stéroïdes. Non, sérieusement, c'est comme un flux d'événements auquel nous pouvons nous **abonner**. Expliquer ce concept prendrait un autre article. Pour l'instant, utilisons-le et gardons à l'esprit que nos deux fonctions sont **asynchrones** — elles ne retourneront pas immédiatement les données de l'API.

Maintenant, allez-y et modifiez votre **services/movie.service.ts** comme suit :

```ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
 
// Énumération personnalisée TypeScript pour les types de recherche (optionnel)
export enum SearchType {
  all = '',
  movie = 'movie',
  series = 'series',
  episode = 'episode'
}
 
@Injectable({
  providedIn: 'root'
})
export class MovieService {
  url = 'http://www.omdbapi.com/';
  apiKey = ''; // <-- Entrez votre propre clé ici !
 
  /**
   * Constructeur du Service avec Injection de Dépendances
   * @param http Le HttpClient standard Angular pour faire des requêtes
   */
  constructor(private http: HttpClient) { }
 
  /**
  * Obtenir des données de l'OmdbApi
  * mapper le résultat pour retourner uniquement les résultats dont nous avons besoin
  *
  * @param {string} title Terme de recherche
  * @param {SearchType} type film, série, épisode ou vide
  * @returns Observable avec les résultats de la recherche
  */
  searchData(title: string, type: SearchType): Observable<any> {
    return this.http.get(`${this.url}?s=${encodeURI(title)}&type=${type}&apikey=${this.apiKey}`).pipe(
      map(results => results['Search'])
    );
  }
 
  /**
  * Obtenir les informations détaillées pour un ID en utilisant le paramètre "i"
  *
  * @param {string} id imdbID pour récupérer les informations
  * @returns Observable avec les informations détaillées
  */
  getDetails(id) {
    return this.http.get(`${this.url}?i=${id}&plot=full&apikey=${this.apiKey}`);
  }
}
```

J'ai également ajouté une documentation aux fonctions — [avec un outil comme Compodoc](https://ionicacademy.com/ionic-code-documentation/) vous pourriez maintenant créer une belle documentation !

Très bien, nous sommes enfin prêts pour plus de code Ionic 4 !

### Recherche de films

Nous commençons la fonctionnalité de nos applications avec les choses qui se passent en arrière-plan, puis nous construisons la vue par-dessus.

Donc, pour l'instant, nous devons implémenter la logique pour soumettre un terme de recherche et un type à notre service et recevoir les résultats. Par conséquent, nous **injectons** le service via notre constructeur afin qu'il soit disponible pour la classe.

Dans une autre fonction que nous appelons `searchChanged()`, nous allons maintenant simplement appeler la fonction correspondante de notre service et définir le résultat dans une variable locale `results`. Notre vue gérera plus tard les données provenant de l'API et les affichera en utilisant cette variable.

Nous conservons également 2 autres variables pour le `searchTerm` et le `type` à l'intérieur de notre classe que nous passons au service. Nous nous connecterons également avec eux depuis la vue afin de pouvoir les modifier.

Maintenant, allez-y avec le code pour votre contrôleur à l'intérieur de **pages/movies/movies.page.ts** :

```ts
import { MovieService, SearchType } from './../../services/movie.service';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
 
@Component({
  selector: 'app-movies',
  templateUrl: './movies.page.html',
  styleUrls: ['./movies.page.scss'],
})
export class MoviesPage implements OnInit {
 
  results: Observable<any>;
  searchTerm: string = '';
  type: SearchType = SearchType.all;
 
  /**
   * Constructeur de notre première page
   * @param movieService Le service Movie pour obtenir les données
   */
  constructor(private movieService: MovieService) { }
 
  ngOnInit() { }
 
  searchChanged() {
    // Appeler notre fonction de service qui retourne un Observable
    this.results = this.movieService.searchData(this.searchTerm, this.type);
  }
}
```

Maintenant, la vue qui ressemble beaucoup au code Ionic 3, juste quelques éléments ont changé de noms et de propriétés. Pour tous ceux qui sont nouveaux dans Ionic en général : **Bienvenue à vos premiers composants Ionic** !

Une page peut être séparée en 3 zones : En-tête, contenu, pied de page. Dans notre cas, nous ne voulons pas de pied de page, donc nous définissons uniquement la zone d'en-tête avec un titre et le contenu avec nos éléments réels pour la recherche.

Le premier élément qui affecte la recherche est le `ion-searchbar` qui est une simple entrée que vous avez vue dans de nombreuses applications auparavant pour rechercher un terme.

Nous voulons toujours appeler notre fonctionnalité de recherche lorsque le type ou le terme de recherche change. Nous pouvons faire cela en capturant l'événement (ionChange) de certains de nos éléments.

Ci-dessous, nous avons une liste déroulante de sélection avec des options et la valeur correspondante pour les différents types que nous pourrions renvoyer à l'API.

Vous devriez également avoir remarqué la syntaxe [(ngModel)] grâce à laquelle les deux éléments sont connectés à nos propriétés de contrôleur. Si un côté change, l'autre recevra automatiquement la nouvelle valeur également (également connu sous le nom de _liaison de données bidirectionnelle_).

Donc, nous avons la recherche en place et nous ajoutons maintenant une autre liste avec des éléments sous nos composants précédents.

Pour la liste, nous utilisons une itération sur notre variable results. Parce que cette variable est un Observable (souvenez-vous de l'implémentation dans notre service), nous devons ajouter un Angular Pipe « | async » à celui-ci. La vue s'abonne à l'Observable et gère les changements en conséquence.

Nous ajoutons également le routage directement à cet élément en utilisant **[routerLink]**. Nous construisons le chemin que nous voulons ouvrir lorsque nous cliquons sur l'élément. Nous utilisons la propriété **imdbID** de l'élément afin que nous puissions résoudre les informations sur notre page de détails plus tard.

En dehors de cela, nous créons le balisage pour un élément en utilisant le **Poster** qui est une image, le titre, l'année et enfin aussi une icône cool à la fin basée sur le type de l'élément. Oui, ces icônes cool sont déjà regroupées avec votre application et sont appelées [Ionicons](https://ionicons.com/) !

Avec tout cela à l'esprit, modifiez votre **pages/movies/movies.page.html** comme suit :

```ts
<ion-header>
  <ion-toolbar color="primary">
    <ion-title>Ma recherche de films</ion-title>
  </ion-toolbar>
</ion-header>
 
<ion-content>
 
  <ion-searchbar [(ngModel)]="searchTerm" (ionChange)="searchChanged($event)"></ion-searchbar>
 
  <ion-item>
    <ion-label>Sélectionner le type de recherche</ion-label>
    <ion-select [(ngModel)]="type" (ionChange)="searchChanged($event)">
      <ion-select-option value="">Tous</ion-select-option>
      <ion-select-option value="movie">Film</ion-select-option>
      <ion-select-option value="series">Série</ion-select-option>
      <ion-select-option value="episode">Épisode</ion-select-option>
    </ion-select>
  </ion-item>
 
  <ion-list>
 
    <ion-item button *ngFor="let item of (results | async)" [routerLink]="['/', 'movies', item.imdbID]">
      <ion-avatar slot="start">
        <img [src]="item.Poster" *ngIf="item.Poster != 'N/A'">
      </ion-avatar>
 
      <ion-label text-wrap>
        <h3>{{ item.Title }}</h3>
        {{ item.Year }}
      </ion-label>
 
      <ion-icon slot="end" *ngIf="item.Type == 'movie'" name="videocam"></ion-icon>
      <ion-icon slot="end" *ngIf="item.Type == 'series'" name="tv"></ion-icon>
      <ion-icon slot="end" *ngIf="item.Type == 'game'" name="logo-game-controller-b"></ion-icon>
 
    </ion-item>
 
  </ion-list>
 
</ion-content>
```

D'ici, vous devriez être en mesure de rechercher un terme spécifique à l'intérieur de votre application et d'obtenir une liste de résultats — **c'est déjà une grande victoire** !

![Image](https://cdn-media-1.freecodecamp.org/images/1*0rjz_KjF2aQX6QtlqTFzdw.gif)
_La recherche de titre de film fonctionne !_

Si vous venez d'Ionic 3, vous avez peut-être également remarqué une nouvelle propriété appelée **slot**, alors voici quelques informations à ce sujet :

Les composants Ionic 4 sont construits en utilisant [Stencil](https://stenciljs.com/) (oui, ils ont en fait créé cet outil aussi !) donc ils sont des **composants web** standard — vous pourriez les importer essentiellement partout sur le web ! Ces composants utilisent également l'[API Shadow DOM](https://blog.ionicframework.com/shadow-dom-in-ionic-and-why-its-awesome/) et vivent essentiellement en dehors de la portée de vos éléments DOM réguliers.

**Cela signifie également que le style standard n'affectera parfois pas ces composants comme c'était possible dans les versions précédentes** !

Afin d'obtenir des informations dans ces composants, nous pouvons injecter certaines parties de HTML dans leurs **slots** qui sont définis sur ces éléments. Vous pouvez [voir à quoi ressemble leur implémentation](https://github.com/ionic-team/ionic/blob/caa2c1e980f3e17a9e62911a330fca785ffbc9c9/core/src/components/item/item.tsx#L160-L165) sur l'exemple de l'ion-item que nous avons utilisé ici.

### Présentation des informations détaillées

Assez d'informations de fond, mettons un peu plus de travail dans la page de détails de notre application. Nous avons implémenté une route et nous avons également créé un bouton qui a passé un ID avec cette route afin que la page de détails s'ouvre, mais nous devons accéder à l'ID !

Avec les versions précédentes d'Ionic, nous pouvions facilement passer des objets entiers à de nouvelles pages, ce qui n'est plus une meilleure pratique. Au lieu de cela, nous **passons uniquement de petits morceaux d'informations** (comme un ID) avec l'URL. Sinon, vous vous retrouveriez avec un terme JSON stringifié énorme à l'intérieur de l'URL. Ce n'est pas vraiment quelque chose que nous voulons avoir.

Pour accéder à ce champ ID (que nous avons déjà défini à l'intérieur de notre routage au début), nous pouvons utiliser l'`ActivatedRoute` et ses propriétés.

Donc, après avoir extrait l'ID des paramètres, nous pouvons faire un autre appel à notre service (que nous avons injecté via le constructeur à nouveau) et obtenir les informations détaillées pour l'ID que nous avons obtenu.

Rien de vraiment nouveau, alors ajoutons le code suivant à notre **pages/movie-details/movie-details.page.ts** :

```ts
import { MovieService } from './../../services/movie.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
 
@Component({
  selector: 'app-movie-details',
  templateUrl: './movie-details.page.html',
  styleUrls: ['./movie-details.page.scss'],
})
export class MovieDetailsPage implements OnInit {
 
  information = null;
 
  /**
   * Constructeur de notre page de détails
   * @param activatedRoute Informations sur la route sur laquelle nous nous trouvons
   * @param movieService Le service Movie pour obtenir les données
   */
  constructor(private activatedRoute: ActivatedRoute, private movieService: MovieService) { }
 
  ngOnInit() {
    // Obtenir l'ID qui a été passé avec l'URL
    let id = this.activatedRoute.snapshot.paramMap.get('id');
 
    // Obtenir les informations de l'API
    this.movieService.getDetails(id).subscribe(result => {
      this.information = result;
    });
  }
 
  openWebsite() {
    window.open(this.information.Website, '_blank');
  }
}
```

Nous avons également ajouté une autre fonction pour ouvrir un site web en utilisant l'objet window et les informations des données de l'API que nous avons stockées dans la variable locale `information`.

Maintenant, nous devons simplement créer une vue basée sur les informations JSON de l'API. Il est toujours utile de logger les informations que vous avez obtenues pour voir les clés que vous pouvez utiliser pour afficher certaines valeurs.

Dans notre cas, nous utilisons le [composant Ionic card](https://beta.ionicframework.com/docs/api/card) et ajoutons l'image et quelques éléments avec des informations et plus d'icônes (_ai-je dit que j'aimais vraiment les Ionicons ?_).

Nous avons également ajouté un bouton sous cette carte qui sera affiché si les informations de résultat contiennent la clé du site web. Nous devons simplement ajouter notre fonction à l'événement `(click)` du bouton afin de tout connecter !

Sur une autre note, nous devons également ajouter un `ion-back-button` à l'en-tête de cette page afin d'obtenir une belle petite flèche de retour vers notre page de liste de films précédente. Cela était fait automatiquement dans la v3 mais doit être implémenté manuellement à partir de la v4 !

Maintenant, terminez votre vue de détails en modifiant votre **pages/movie-details/movie-details.page.html** comme suit :

```ts
<ion-header>
  <ion-toolbar color="primary">
    <ion-buttons slot="start">
      <ion-back-button defaultHref="/"></ion-back-button>
    </ion-buttons>
    <ion-title>{{ information?.Genre }}</ion-title>
  </ion-toolbar>
</ion-header>
 
<ion-content padding>
 
  <ion-card *ngIf="information">
    <ion-card-header>
      <ion-card-title>
        {{ information.Title }}
      </ion-card-title>
      <ion-card-subtitle>
        {{ information.Year }}
      </ion-card-subtitle>
    </ion-card-header>
    <ion-card-content text-center>
      <img [src]="information.Poster" class="info-img">
      {{ information.Plot }}
 
      <ion-item lines="none">
        <ion-icon name="star-half" slot="start"></ion-icon>
        <ion-label>{{ information.imdbRating }}</ion-label>
      </ion-item>
 
      <ion-item lines="none">
        <ion-icon name="clipboard" slot="start"></ion-icon>
        <ion-label text-wrap>{{ information.Director }}</ion-label>
      </ion-item>
 
      <ion-item lines="none">
        <ion-icon name="contacts" slot="start"></ion-icon>
        <ion-label text-wrap>{{ information.Actors }}</ion-label>
      </ion-item>
 
      <ion-button expand="full" (click)="openWebsite()" *ngIf="information.Website && information.Website != 'N/A'">
        <ion-icon name="open" slot="start"></ion-icon>
        Ouvrir le site web
      </ion-button>
    </ion-card-content>
  </ion-card>
  
</ion-content>
```

Si vous regardez maintenant votre navigateur, vous remarquerez peut-être que l'image semble beaucoup trop grande car elle prend tout l'espace disponible. Changeons cela grâce à un bon vieux CSS, alors ouvrez votre **pages/movie-details/movie-details.page.scss** et insérez :

```scss
.info-img {
    max-height: 30vh;
    object-fit: contain;
    padding: 10px;
}
```

Maintenant, nos résultats ont l'air beaucoup plus attrayants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FYRipkcDiEjrjZrp2JBDEQ.gif)
_Notre application Ionic 4 terminée_

Nous pouvons rechercher, sélectionner un type de film, plonger dans un résultat de recherche et avoir une application Ionic 4 entièrement fonctionnelle avec des appels HTTP terminée !

### Conclusion

Bien que ce fut une expérience simple de construire notre première application Ionic 4, il y a tant de choses dont nous n'avons pas assez parlé.

Des motifs d'interface utilisateur comme les onglets et le menu latéral, les variables CSS, la mise en page réactive et PWA pour n'en nommer que quelques-uns du côté d'Ionic et Angular.

Et nous n'avons même pas touché le côté Cordova des choses pour construire cette application en une **vraie application mobile native** !

Si vous voulez apprendre à **développer des applications Ionic 4 aussi vite que possible** et les mettre rapidement sur les stores d'applications iOS et Android, vous pouvez [rejoindre l'Ionic Academy aujourd'hui](https://ionicacademy.com/) et profiter de screencasts d'experts, d'une bibliothèque de gains rapides et d'une communauté pour vous soutenir dans votre voyage !

Et bien sûr, je (Simon) suis également présent à l'intérieur pour répondre à toutes vos questions à tout moment.

Vous pouvez également trouver une version vidéo de ce guide ci-dessous !

<iframe width="560" height="315" src="https://www.youtube.com/embed/3QPbBJgNF94" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

_Publié à l'origine sur [ionicacademy.com](https://ionicacademy.com/ionic-4-app-api-calls/) le 24 janvier 2019._
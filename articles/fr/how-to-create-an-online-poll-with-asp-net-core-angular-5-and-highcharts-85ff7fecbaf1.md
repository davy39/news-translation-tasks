---
title: Comment créer un sondage en ligne avec ASP.NET Core, Angular 5 et Highcharts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-03T21:49:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-online-poll-with-asp-net-core-angular-5-and-highcharts-85ff7fecbaf1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WJRoM-l76-dMiuImfuRalA.jpeg
tags:
- name: Angular
  slug: angular
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment créer un sondage en ligne avec ASP.NET Core, Angular 5 et Highcharts
seo_desc: 'By Ankit Sharma

  In this article, we will create an online polling application using ASP.NET Core,
  Angular 5, and the Entity Framework Core. Since this is the season of Indian Premiere
  League cricket in India, we will create an online poll for “Who is...'
---

Par Ankit Sharma

Dans cet article, nous allons créer une application de sondage en ligne en utilisant ASP.NET Core, Angular 5 et Entity Framework Core. Comme c'est la saison de la Indian Premiere League en Inde, nous allons créer un sondage en ligne pour « Qui va gagner l'IPL 2018 ? ». Les résultats du sondage seront affichés sous forme de graphique en colonnes créé avec Highcharts.

Nous utiliserons Visual Studio 2017 et SQL Server 2014.

Jetez un œil à l'application finale.

![Image](https://cdn-media-1.freecodecamp.org/images/L7xDS7yWY8CQda2CeNFcB-kgX5vOC3tMBsdY)

### Prérequis

* Installer le SDK .NET Core 2.0.0 ou supérieur depuis [ici](https://www.microsoft.com/net/core#windowscmd).
* Installer la dernière version de Visual Studio 2017 Community Edition depuis [ici](https://www.visualstudio.com/downloads/).
* Télécharger et installer la dernière version de Node.js depuis [ici](https://nodejs.org/en/download/).
* SQL Server 2008 ou supérieur.

### Code source

Avant de continuer, je vous recommande de récupérer le code source depuis [GitHub](https://github.com/AnkitSharma-007/ASPCore.Angular.HighCharts).

### Création de la table

Nous allons stocker les données des équipes dans la table **IplTeams**. Exécutez les commandes suivantes pour créer la table.

```
CREATE TABLE IplTeams   (  TeamId INTEGER IDENTITY(1,1) PRIMARY KEY,  TeamName VARCHAR(30) NOT NULL,  VoteCount INTEGER NOT NULL  )
```

Maintenant, nous allons insérer les noms des équipes et initialiser le compteur de votes à zéro. Exécutez les instructions d'insertion suivantes.

```
INSERT INTO IplTeams VALUES ('Chennai Super Kings',0)  INSERT INTO IplTeams VALUES ('Delhi Daredevils',0)  INSERT INTO IplTeams VALUES ('Kings XI Punjab',0)  INSERT INTO IplTeams VALUES ('Kolkata Knight Riders',0)  INSERT INTO IplTeams VALUES ('Mumbai Indians',0)  INSERT INTO IplTeams VALUES ('Rajasthan Royals',0)  INSERT INTO IplTeams VALUES ('Royal Challengers Bangalore',0)  INSERT INTO IplTeams VALUES ('Sunrisers Hyderabad',0)
```

### Créer l'application web MVC

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet. Après avoir sélectionné le projet, une boîte de dialogue « Nouveau Projet » s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche.

Ensuite, sélectionnez « Application Web ASP.NET Core » parmi les types de projets disponibles. Donnez le nom du projet **IPLPollDemo** et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous verrez deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez « .NET Core » et « ASP.NET Core 2.0 » dans ces menus déroulants. Ensuite, sélectionnez le modèle « Angular » et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/9CM3t5cdgS3UmU1ekMhYF3WHHIz4b10WlZKi)

Notre projet est maintenant créé.

Comme nous utilisons Highcharts dans notre application, nous devons installer les packages correspondants. Ouvrez le fichier **package.json** et insérez le code suivant :

```
{    "name": "IPLPollDemo",    "private": true,    "version": "0.0.0",    "scripts": {      "test": "karma start ClientApp/test/karma.conf.js"    },    "devDependencies": {      "@angular/animations": "5.2.10",      "@angular/common": "5.2.10",      "@angular/compiler": "5.2.10",      "@angular/compiler-cli": "5.2.10",      "@angular/core": "5.2.10",      "@angular/forms": "5.2.10",      "@angular/http": "5.2.10",      "@angular/platform-browser": "5.2.10",      "@angular/platform-browser-dynamic": "5.2.10",      "@angular/platform-server": "5.2.10",      "@angular/router": "5.2.10",      "@ngtools/webpack": "6.0.0-rc.10",      "@types/chai": "4.1.3",      "@types/highcharts": "^5.0.22",      "@types/jasmine": "2.8.6",      "@types/webpack-env": "1.13.6",      "angular2-router-loader": "0.3.5",      "angular2-template-loader": "0.6.2",      "aspnet-prerendering": "^3.0.1",      "aspnet-webpack": "^2.0.1",      "awesome-typescript-loader": "5.0.0",      "bootstrap": "4.1.1",      "chai": "4.1.2",      "css": "2.2.1",      "css-loader": "0.28.11",      "es6-shim": "0.35.3",      "event-source-polyfill": "0.0.12",      "expose-loader": "0.7.5",      "extract-text-webpack-plugin": "3.0.2",      "file-loader": "1.1.11",      "html-loader": "0.5.5",      "isomorphic-fetch": "2.2.1",      "jasmine-core": "3.1.0",      "jquery": "3.3.1",      "json-loader": "0.5.7",      "karma": "2.0.2",      "karma-chai": "0.1.0",      "karma-chrome-launcher": "2.2.0",      "karma-cli": "1.0.1",      "karma-jasmine": "1.1.1",      "karma-webpack": "3.0.0",      "preboot": "6.0.0-beta.3",      "raw-loader": "0.5.1",      "reflect-metadata": "0.1.12",      "rxjs": "^6.0.0",      "style-loader": "0.21.0",      "to-string-loader": "1.1.5",      "typescript": "2.8.3",      "url-loader": "1.0.1",      "webpack": "4.6.0",      "webpack-hot-middleware": "2.22.1",      "webpack-merge": "4.1.2",      "zone.js": "0.8.26"    },    "dependencies": {      "angular-highcharts": "^5.2.12",      "highcharts": "^6.1.0"    }  }
```

Ici, nous avons ajouté la dépendance Highcharts aux lignes 22, 64 et 65.

**Note importante :** Si vous avez la version 4 d'Angular dans votre fichier **package.json**, copiez alors le code complet ci-dessus pour mettre à jour votre version d'Angular à 5. Si vous utilisez déjà Angular 5, copiez simplement les lignes pour inclure la dépendance Highcharts.

Maintenant, fermez l'instance de Visual Studio et naviguez jusqu'au dossier du projet contenant le fichier **package.json**, puis ouvrez l'invite de commandes. Exécutez la commande « **npm install** » pour installer toutes les dépendances requises. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Après l'exécution réussie de la commande, ouvrez votre projet dans Visual Studio. Vous verrez la structure des dossiers dans l'Explorateur de solutions comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Ici, nous avons nos dossiers **Controllers** et **Views**. Nous ne toucherons pas aux dossiers **Views** pour ce tutoriel, car nous utiliserons Angular pour gérer l'interface utilisateur.

Le dossier **Controllers** contiendra notre contrôleur Web API. Nous nous intéressons au dossier ClientApp où réside le côté client de notre application.

Dans le dossier **ClientApp/app/components**, nous avons déjà quelques composants créés qui sont fournis par défaut avec le modèle Angular dans VS 2017. Ces composants n'affecteront pas notre application, mais pour ce tutoriel, nous supprimerons les dossiers **fetchdata** et **counter** de **ClientApp/app/components**.

### Échafaudage du modèle vers l'application

Nous utilisons l'approche « database first » d'Entity Framework Core pour créer nos modèles. Naviguez vers Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages.

Nous devons installer le package pour le fournisseur de base de données que nous ciblons, qui est SQL Server dans ce cas. Exécutez donc la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.SqlServer
```

Comme nous utilisons les outils Entity Framework pour créer un modèle à partir de la base de données existante, nous installerons également le package d'outils. Exécutez la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.Tools
```

Après avoir installé les deux packages, nous allons échafauder notre modèle à partir des tables de la base de données en utilisant la commande suivante :

```
Scaffold-DbContext "Votre chaîne de connexion ici" Microsoft.EntityFrameworkCore.SqlServer -OutputDir Models -Tables IplTeams
```

**Note :** N'oubliez pas de mettre votre propre chaîne de connexion (à l'intérieur des " ").

Après l'exécution réussie de cette commande, vous verrez qu'un dossier Models a été créé et contient deux fichiers de classe : **myTestDBContext.cs** et **IplTeams.cs**. Nous avons créé avec succès nos Modèles en utilisant l'approche « database first » d'EF Core.

Maintenant, nous allons créer un autre fichier de classe pour gérer les opérations liées à la base de données.

Faites un clic droit sur le dossier **Models** et sélectionnez Ajouter >> Classe. Nommez votre classe **TeamDataAccessLayer.cs** et cliquez sur le bouton Ajouter. À ce stade, le dossier Models aura la structure suivante.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Ouvrez **TeamDataAccessLayer.cs** et insérez le code suivant pour gérer les opérations de la base de données :

```
using Microsoft.EntityFrameworkCore;  using System;  using System.Collections.Generic;  using System.Linq;  using System.Threading.Tasks;    namespace IPLPollDemo.Models  {      public class TeamDataAccessLayer      {          myTestDBContext db = new myTestDBContext();            //Pour obtenir la liste de toutes les équipes de la base de données          public IEnumerable<IplTeams> GetAllTeams()          {              try              {                  return db.IplTeams.ToList();              }              catch              {                  throw;              }          }            //Pour mettre à jour le compteur de votes d'une équipe de un          public int RecordVote(IplTeams iplTeam)          {              try              {                    db.Database.ExecuteSqlCommand("update IplTeams set VoteCount = VoteCount + 1 where TeamID = {0}", parameters: iplTeam.TeamId);                    return 1;              }              catch              {                  throw;              }          }            //Pour obtenir le nombre total de votes           public int GetTotalVoteCount()          {              try              {                  return db.IplTeams.Sum(t => t.VoteCount);              }              catch              {                  throw;              }          }      }  }
```

Dans cette classe, nous avons défini trois méthodes.

1. GetAllTeams — Pour obtenir la liste de toutes les huit équipes de la base de données.
2. RecordVote — Pour mettre à jour le compteur de votes pour chaque équipe après que l'utilisateur a soumis son vote.
3. GetTotalVoteCount — Pour obtenir la somme des votes de toutes les équipes.

Maintenant, nous allons créer notre contrôleur Web API.

### Ajout du contrôleur Web API à l'application

Faites un clic droit sur le dossier **Controllers** et sélectionnez Ajouter >> Nouvel élément.

Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira. Sélectionnez **ASP.NET** dans le panneau de gauche, puis sélectionnez « Classe de contrôleur Web API » dans le panneau des modèles et nommez-le **TeamController.cs**. Cliquez sur Ajouter.

![Image](https://cdn-media-1.freecodecamp.org/images/kIXTfjNgJLHUsxkVQI4OfFD6YrwA56EnGOFf)

Cela créera notre classe de contrôleur Web API **TeamController**. Nous mettrons toute notre logique métier dans ce contrôleur. Nous appellerons les méthodes de **TeamDataAccessLayer** pour récupérer les données et les transmettre à l'interface Angular.

Ouvrez le fichier **TeamController.cs** et insérez le code suivant :

```
using System;  using System.Collections.Generic;  using System.Linq;  using System.Threading.Tasks;  using IPLPollDemo.Models;  using Microsoft.AspNetCore.Mvc;    namespace IPLPollDemo.Controllers  {      [Route("api/Team")]      public class TeamController : Controller      {          TeamDataAccessLayer objTeam = new TeamDataAccessLayer();            [HttpGet]          [Route("GetTeamList")]          public IEnumerable<IplTeams> GetTeamList()          {              return objTeam.GetAllTeams();          }            [HttpGet]          [Route("TotalVotes")]          public int TotalVotes()          {              return objTeam.GetTotalVoteCount();          }            [HttpPut]          [Route("UpdateVoteCount")]          public int UpdateVoteCount([FromBody] IplTeams team)          {              return objTeam.RecordVote(team);          }      }  }
```

### Créer le service Angular

Nous allons créer un service Angular qui convertira la réponse de l'API Web en JSON et la transmettra à notre composant. Faites un clic droit sur le dossier **ClientApp/app** puis Ajouter >> Nouveau dossier et nommez le dossier **Services**.

Faites un clic droit sur le dossier Services et sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira. Sélectionnez Scripts dans le panneau de gauche, puis sélectionnez « Fichier TypeScript » dans le panneau des modèles. Nommez-le **teamservice.service.ts** et cliquez sur Ajouter.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Ouvrez le fichier **teamservice.service.ts** et insérez le code suivant :

```
import { Injectable, Inject } from '@angular/core';  import { Http, Response } from '@angular/http';  import { Observable } from 'rxjs/Observable';  import { Router } from '@angular/router';  import 'rxjs/add/operator/map';  import 'rxjs/add/operator/catch';  import 'rxjs/add/observable/throw';      @Injectable()  export class TeamService {      myAppUrl: string = "";        constructor(private _http: Http, @Inject('BASE_URL') baseUrl: string) {          this.myAppUrl = baseUrl;      }        getTeams() {          return this._http.get(this.myAppUrl + 'api/Team/GetTeamList')              .map((response: Response) => response.json())              .catch(this.errorHandler);      }        getTotalVotes() {          return this._http.get(this.myAppUrl + 'api/Team/TotalVotes')              .map((response: Response) => response.json())              .catch(this.errorHandler);      }        saveVotes(team) {          return this._http.put(this.myAppUrl + 'api/Team/UpdateVoteCount', team)              .map((response: Response) => response.json())              .catch(this.errorHandler);      }        errorHandler(error: Response) {          console.log(error);          return Observable.throw(error);      }  }
```

Dans le constructeur, nous injectons le service HTTP et l'URL de base de l'application pour permettre les appels à l'API Web. Après cela, nous avons défini trois fonctions pour appeler notre API Web et convertir le résultat en format JSON. Nous appellerons ces fonctions depuis nos composants.

À ce stade, vous pourriez obtenir l'erreur « Le paramètre 'employee' a implicitement le type 'any' » dans le fichier **empservice.service.ts**. Si vous rencontrez ce problème, ajoutez la ligne suivante dans le fichier **tsconfig.json** :

"noImplicitAny": false

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Maintenant, nous allons créer nos composants.

### Création des composants Angular

Nous allons ajouter deux composants Angular à notre application :

1. Composant Poll — pour afficher les noms des équipes et un bouton correspondant pour voter pour l'équipe.
2. Composant Result — pour afficher les résultats du sondage.

Faites un clic droit sur le dossier **ClientApp/app/components** et sélectionnez Ajouter >> Nouveau dossier et nommez le dossier **Poll**.

Faites un clic droit sur le dossier **Poll** et sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira. Sélectionnez Scripts dans le panneau de gauche, puis sélectionnez « Fichier TypeScript » dans le panneau des modèles. Nommez-le **IPLPoll.component.ts** et cliquez sur Ajouter. Cela ajoutera un fichier TypeScript à l'intérieur du dossier Poll.

![Image](https://cdn-media-1.freecodecamp.org/images/T80wl97gZYuBRhdG7ICrAKAYa4kElMbCMe9h)

Faites un clic droit sur le dossier **Poll** et sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira. Sélectionnez ASP.NET Core dans le panneau de gauche, puis sélectionnez « Page HTML » dans le panneau des modèles, et nommez-le **IPLPoll.component.html**. Cliquez sur Ajouter. Cela ajoutera un fichier HTML à l'intérieur du dossier Poll.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

De même, créez un dossier **Results** à l'intérieur du dossier **ClientApp/app/components** et ajoutez un fichier TypeScript **PollResult.component.ts** et un fichier HTML **PollResult.component.html**.

Maintenant, notre **ClientApp/app** ressemblera à l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/vzSQEMn9gFpybcRtR-qi8DHxwpFmK2gaHObh)

Ouvrez le fichier **IPLPoll.component.ts** et insérez le code suivant :

```
import { Component, OnInit } from '@angular/core';  import { Http, Headers } from '@angular/http';  import { PercentPipe } from '@angular/common';  import { Router, ActivatedRoute } from '@angular/router';  import { TeamService } from '../../services/teamservice.service'    @Component({      templateUrl: './IPLPoll.component.html',  })    export class IPLPoll {        public teamList: TeamData[];        constructor(public http: Http, private _teamService: TeamService, private _router: Router) {          this.getTeamList();      }        getTeamList() {          this._teamService.getTeams().subscribe(              data => this.teamList = data          )      }        save(team) {            this._teamService.saveVotes(team)              .subscribe((data) => {                  this._router.navigate(['/results']);              })      }  }  export class TeamData {      teamId: number;      teamName: string;      voteCount: number;      voteShare: number;  }
```

Nous avons créé une classe **TeamData** pour contenir les détails de chaque équipe, tels que teamId, teamName, voteCount et voteShare. À l'intérieur de notre classe de composant IPLPoll, nous avons créé une variable de tableau **teamList** de type **TeamData**.

La méthode **getTeamList()** appellera la fonction getTeams de notre service TeamService pour obtenir la liste des équipes de la base de données et l'assignera à la variable teamList. La méthode getTeamList est appelée à l'intérieur du constructeur afin que les données des équipes soient affichées lors du chargement de la page.

La méthode save sera invoquée lorsque l'utilisateur votera pour son équipe préférée. Cela appellera la fonction **saveVotes** de notre service pour mettre à jour le compteur de votes de cette équipe particulière. L'utilisateur sera ensuite redirigé vers le composant PollResults pour voir les résultats du sondage.

Ouvrez le fichier **IPLPoll.component.html** et insérez le code suivant :

```
<h1>Qui va gagner l'IPL 2018 ?</h1>    <h3>Votez pour votre équipe préférée !!! </h3>  <hr />    <p *ngIf="!teamList"><em>Chargement...</em></p>    <table class='table' *ngIf="teamList">      <thead>          <tr>              <th>Nom de l'équipe</th>          </tr>      </thead>      <tbody>          <tr *ngFor="let team of teamList">              <td>{{ team.teamName }}</td>              <td>                  <button (click)="save(team)" class="btn btn-primary"> Vote <i class="glyphicon glyphicon-thumbs-up"></i></button>              </td>          </tr>      </tbody>  </table>
```

Cette page HTML affichera la liste des équipes avec un bouton **Vote** à côté de chaque équipe. Lorsque l'utilisateur clique sur l'un des boutons de vote, cela mettra à jour le compteur de votes et redirigera l'utilisateur vers la page PollResults.

Ouvrez maintenant le fichier **PollResults.component.ts** et insérez le code suivant :

```
import { Component, OnInit } from '@angular/core';  import { Http, Headers } from '@angular/http';  import { PercentPipe } from '@angular/common';  import { Router, ActivatedRoute } from '@angular/router';  import { TeamData } from '../poll/IPLPoll.component';  import { TeamService } from '../../services/teamservice.service';    import { Observable } from 'rxjs/Observable';  import 'rxjs/add/observable/zip';    import { Chart } from 'angular-highcharts';    @Component({      templateUrl: './PollResult.component.html',  })    export class PollResult {        public chart: any;      public totalVotes: number;      public resultList: TeamData[];        constructor(public http: Http, private _teamService: TeamService) {            Observable.zip(this._teamService.getTotalVotes(), this._teamService.getTeams())              .subscribe(([totalVoteCount, teamListData]) => {                  this.totalVotes = totalVoteCount;                  this.resultList = teamListData;                    for (let i = 0; i < teamListData.length; i++) {                      teamListData[i].voteShare = (((teamListData[i].voteCount) / this.totalVotes) * 100);                  }                    this.createCharts();              });      }        createCharts() {          this.chart = new Chart({              chart: {                  type: 'column'              },              title: {                  text: 'Partage des votes pour chaque équipe'              },              xAxis: {                  type: 'category',                  labels: {                      rotation: -45,                      style: {                          fontSize: '13px',                          fontFamily: 'Verdana, sans-serif'                      }                  }              },              yAxis: {                  min: 0,                  title: {                      text: 'Pourcentage de votes'                  }              },              legend: {                  enabled: false              },              tooltip: {                  pointFormat: 'Vote : <b>{point.y:.2f} %</b>'              },                series: [{                  type: 'column',                  data: [                      { name: this.resultList[0].teamName, y: this.resultList[0].voteShare, color: 'rgba(253, 185, 19, 0.85)' },                      { name: this.resultList[1].teamName, y: this.resultList[1].voteShare, color: 'rgba(0, 76, 147, 0.85)' },                      { name: this.resultList[2].teamName, y: this.resultList[2].voteShare, color: 'rgba(170, 69, 69, 0.85)' },                      { name: this.resultList[3].teamName, y: this.resultList[3].voteShare, color: 'rgba(112, 69, 143, 0.85)' },                      { name: this.resultList[4].teamName, y: this.resultList[4].voteShare, color: 'rgba(0, 93, 160, 0.85)' },                      { name: this.resultList[5].teamName, y: this.resultList[5].voteShare, color: 'rgba(45, 77, 157, 0.85)' },                      { name: this.resultList[6].teamName, y: this.resultList[6].voteShare, color: 'rgba(0, 0, 0, 0.85)' },                      { name: this.resultList[7].teamName, y: this.resultList[7].voteShare, color: 'rgba(251, 100, 62, 0.85)' }                  ],              }]            });        }  }
```

Nous récupérons la liste mise à jour des données des équipes de la base de données et le nombre total de votes pour toutes les équipes. Nous calculerons ensuite la part de votes de chaque équipe et invoquerons la méthode **createCharts()** pour créer le graphique des résultats du sondage.

Le pourcentage de part de votes pour chaque équipe est calculé en divisant les votes obtenus par chaque équipe par le nombre total de votes. Nous effectuons toutes ces opérations dans notre constructeur pour afficher le résultat lors du chargement de la page.

La méthode **createCharts()** créera le graphique en colonnes à l'aide de la bibliothèque Highcharts. Le pourcentage de votes est sélectionné comme axe Y et le nom de l'équipe est sélectionné comme axe X. Pour rendre les choses intéressantes, nous définissons la couleur de chaque colonne comme la couleur du maillot de l'équipe correspondante.

Ouvrez le fichier **PollResults.component.html** et insérez le code suivant :

```
<h2>Votre vote a été enregistré avec succès !!! </h2>    <h3>Voici les résultats du vote </h3>  <hr />    <p><b>Total des votes </b> : {{totalVotes}}</p>    <div [chart]="chart"></div>
```

Cette page HTML est simple. Nous affichons les résultats du vote sous forme de graphique en colonnes. Juste au-dessus du graphique, nous affichons également le nombre total de votes.

### Définition d'une route et d'un menu de navigation pour notre application

Ouvrez le fichier **/app/app.shared.module.ts** et insérez le code suivant :

```
import { NgModule } from '@angular/core';  import { CommonModule } from '@angular/common';  import { FormsModule } from '@angular/forms';  import { HttpModule } from '@angular/http';  import { RouterModule } from '@angular/router';  import { ChartModule } from 'angular-highcharts';    import { TeamService } from './services/teamservice.service'  import { AppComponent } from './components/app/app.component';  import { NavMenuComponent } from './components/navmenu/navmenu.component';  import { HomeComponent } from './components/home/home.component';  import { IPLPoll } from './components/Poll/IPLPoll.component';  import { PollResult } from './components/Results/PollResult.component';    @NgModule({      declarations: [          AppComponent,          NavMenuComponent,          HomeComponent,          IPLPoll,          PollResult      ],      imports: [          CommonModule,          HttpModule,          FormsModule,          ChartModule,          RouterModule.forRoot([              { path: '', redirectTo: 'home', pathMatch: 'full' },              { path: 'home', component: HomeComponent },              { path: 'poll', component: IPLPoll },              { path: 'results', component: PollResult },              { path: '**', redirectTo: 'home' }          ])      ],      providers: [TeamService]  })  export class AppModuleShared {  }
```

Ici, nous avons également importé tous nos composants et défini la route pour notre application comme suit :

* home — qui redirigera vers le composant **Home**
* poll — redirige vers le composant **IPLPoll**
* results — redirige vers le composant **PollResults**

Enfin, nous devons définir le menu de navigation pour notre application. Ouvrez le fichier **/app/components/navmenu/navmenu.component.html** et insérez le code suivant :

```
<div class='main-nav'>      <div class='navbar navbar-inverse'>          <div class='navbar-header'>              <button type='button' class='navbar-toggle' data-toggle='collapse' data-target='.navbar-collapse'>                  <span class='sr-only'>Basculer la navigation</span>                  <span class='icon-bar'></span>                  <span class='icon-bar'></span>                  <span class='icon-bar'></span>              </button>              <a class='navbar-brand' [routerLink]="['/home']">IPLPollDemo</a>          </div>          <div class='clearfix'></div>          <div class='navbar-collapse collapse'>              <ul class='nav navbar-nav'>                  <li [routerLinkActive]="['link-active']">                      <a [routerLink]="['/home']">                          <span class='glyphicon glyphicon-home'></span> Accueil                      </a>                  </li>                  <li [routerLinkActive]="['link-active']">                      <a [routerLink]="['/poll']">                          <span class='glyphicon glyphicon-th-list'></span> Sondage IPL                      </a>                  </li>              </ul>          </div>      </div>  </div>
```

Et c'est tout. Nous avons créé notre application de sondage IPL en utilisant Angular 5 et Entity Framework Core.

### Démonstration d'exécution

Appuyez sur F5 pour lancer l'application.

Une page web s'ouvrira comme montré dans l'image ci-dessous. Vous pouvez voir l'URL montrant la route pour notre composant home, et le menu de navigation à gauche montrant le lien de navigation pour la page Sondage IPL.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Cliquez sur Sondage IPL dans le menu de navigation. Il vous redirigera vers le composant Poll montrant tous les noms des équipes avec un bouton de vote à côté d'eux. Remarquez que l'URL contient « /poll ».

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Cliquez sur le bouton de vote pour voter pour votre équipe préférée. Vous serez redirigé vers la page des résultats montrant les résultats du sondage sous forme de graphique en colonnes.

![Image](https://cdn-media-1.freecodecamp.org/images/DLLueoKdpGQQW9sxwmzPxz1Zn2Bn2ptFwsP1)

Comme il s'agit du premier vote, il montre 100 % pour une équipe et 0 % pour les autres. Après avoir soumis quelques votes pour toutes les équipes, nous obtiendrons le graphique des résultats de vote comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

### Conclusion

Nous avons créé un sondage en ligne en utilisant ASP.NET Core, Angular 5 et l'approche « database first » d'Entity Framework Core avec l'aide de Visual Studio 2017 et SQL Server 2014. Nous avons également créé un graphique en colonnes en utilisant Highcharts pour afficher les résultats du sondage.

Récupérez le code source depuis [GitHub](https://github.com/AnkitSharma-007/ASPCore.Angular.HighCharts) et amusez-vous. N'oubliez pas de mettre votre propre chaîne de connexion avant d'exécuter le code.

Vous pouvez également trouver cet article sur [C# Corner](https://www.c-sharpcorner.com/article/asp-net-co-using-highcharts-with-angular-5/).

Vous pouvez consulter mes autres articles sur Angular 5 [ici](http://ankitsharmablogs.com/category/angular-5/)

### Voir aussi

* [ASP.NET Core — CRUD avec React.js et Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-with-react-js-and-entity-framework-core/)
* [ASP.NET Core — CRUD en utilisant Blazor et Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [ASP.NET Core — CRUD en utilisant Angular 5 et Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [Opérations CRUD avec ASP.NET Core en utilisant Angular 5 et ADO.NET](http://ankitsharmablogs.com/crud-operations-asp-net-core-using-angular-5-ado-net/)
* [Démarrer avec Angular 5 en utilisant Visual Studio Code](http://ankitsharmablogs.com/getting-started-with-angular-5-using-visual-studio-code/)
* [Opération CRUD avec ASP.NET Core MVC en utilisant Visual Studio Code et ADO.NET](http://ankitsharmablogs.com/crud-operation-with-asp-net-core-mvc-using-visual-studio-code-and-ado-net/)

_Publié à l'origine sur [ankitsharmablogs.com](http://ankitsharmablogs.com/asp-net-core-using-highcharts-with-angular-5/) le 3 mai 2018._
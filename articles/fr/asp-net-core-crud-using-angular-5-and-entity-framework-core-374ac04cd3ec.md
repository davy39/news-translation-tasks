---
title: Comment déployer des tableaux modifiables en HTML en utilisant Angular 5 et
  Entity Framework Core
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T05:56:43.000Z'
originalURL: https://freecodecamp.org/news/asp-net-core-crud-using-angular-5-and-entity-framework-core-374ac04cd3ec
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W5vbBi1Nah40KGMRIE1GJw.jpeg
tags:
- name: angular 5
  slug: angular-5
- name: entity framework core
  slug: entity-framework-core
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment déployer des tableaux modifiables en HTML en utilisant Angular
  5 et Entity Framework Core
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we are going to create a web application using ASP.NET Core 2.0
  and Angular 5 with the help of the Entity Framework (EF) Core database-first approach.
  We will be creating a sample Employee Record Manageme...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons créer une application web en utilisant **ASP.NET Core 2.0** et **Angular 5** avec l'approche database-first d'Entity Framework (EF) Core. Nous allons créer un système de gestion des dossiers des employés. Pour lire les entrées de l'utilisateur, nous allons utiliser des **formulaires Angular** avec des validations de champs obligatoires côté client. Nous allons également lier une liste déroulante dans le formulaire Angular à une table dans la base de données en utilisant EF Core.

Nous allons utiliser **Visual Studio 2017** et **SQL Server** version 2008 ou supérieure.

### Prérequis

* Installer le SDK .NET Core 2.0.0 ou supérieur depuis [ici](https://www.microsoft.com/net/core#windowscmd).
* Installer la dernière version de Visual Studio 2017 Community Edition depuis [ici](https://www.visualstudio.com/downloads/).
* Télécharger et installer la dernière version de Node.js depuis [ici](https://nodejs.org/en/download/).
* SQL Server 2008 ou supérieur.

### Code Source

Avant de continuer, je vous recommande de récupérer le code source depuis [Github](https://github.com/AnkitSharma-007/CRUD.ASPCore.Angular5.WebAPI.EF).

### Création des tables

Nous allons utiliser deux tables pour stocker nos données.

1. `tblEmployee` : utilisée pour stocker les détails des employés. Elle contient des champs tels que EmployeeID, Name, City, Department et Gender.
2. `tblCities` : celle-ci contient la liste des villes. Elle est utilisée pour remplir le champ _City_ de la table tblEmployee. tblCities contient deux champs, CityID et CityName.

Exécutez les commandes suivantes pour créer les deux tables :

```sql
CREATE TABLE tblEmployee (
  EmployeeID int IDENTITY(1,1) NOT NULL PRIMARY KEY,
  Name varchar(20) NOT NULL ,
  City varchar(20) NOT NULL ,
  Department varchar(20) NOT NULL ,
  Gender varchar(6) NOT NULL
)
GO

CREATE TABLE tblCities (
  CityID int IDENTITY(1,1) NOT NULL PRIMARY KEY,
  CityName varchar(20) NOT NULL
)
GO
```

Maintenant, nous allons mettre quelques données dans la table `tblCities`. Nous allons utiliser cette table pour lier une liste déroulante dans notre application web. La ville souhaitée peut être sélectionnée en utilisant cette liste déroulante. Utilisez les instructions d'insertion suivantes.

```sql
INSERT INTO tblCities VALUES('New Delhi');
INSERT INTO tblCities VALUES('Mumbai');
INSERT INTO tblCities VALUES('Hyderabad');
INSERT INTO tblCities VALUES('Chennai');
INSERT INTO tblCities VALUES('Bengaluru');
```

Maintenant, notre partie base de données est terminée. Nous allons donc procéder à la création de l'application MVC en utilisant Visual Studio 2017.

### Créer l'application web ASP.NET MVC

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet.

Après avoir sélectionné le projet, une boîte de dialogue « Nouveau Projet » s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche.

Ensuite, sélectionnez « Application Web ASP.NET Core » parmi les types de projets disponibles. Donnez le nom du projet « EFNgApp » et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/YVcPWRXi6XvKor9-rq6xKvKl1Q9D5E90SDEi)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez observer deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez « .NET Core » et « ASP.NET Core 2.0 » dans ces menus déroulants. Ensuite, sélectionnez le modèle « Angular » et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/K6YQvZWOFaTVBg9tQW-2ZgTokPtEbaAyxbNC)

Maintenant, notre projet sera créé. Vous pouvez voir la structure des dossiers dans l'Explorateur de solutions dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/iCGpODkNimBqGNlUVEJPy0468-Rnjv7-N1ih)

Ici, nous avons nos dossiers « Controllers » et « Views ». Nous ne toucherons pas au dossier Views pour ce tutoriel, puisque nous allons utiliser Angular pour gérer l'UI.

Le dossier _Controllers_ contiendra notre contrôleur Web API. Le point d'intérêt pour nous est le dossier « ClientApp » où réside le côté client de notre application.

À l'intérieur du dossier « ClientApp/app/components », nous avons déjà quelques composants créés. Ceux-ci sont fournis par défaut avec le modèle Angular dans VS 2017. Ces composants n'affecteront pas notre application, mais pour ce tutoriel, nous allons supprimer les dossiers « fetchdata » et « counter » de ClientApp/app/components.

### Ajout du Modèle à l'Application

Nous utilisons l'approche database-first d'Entity Framework Core pour créer nos modèles. Accédez à Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages.

Nous devons installer le package pour le fournisseur de base de données que nous ciblons, qui est SQL Server dans ce cas. Exécutez maintenant la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.SqlServer
```

Puisque nous utilisons les outils Entity Framework pour créer un modèle à partir de la base de données existante, nous allons également installer le package d'outils. Exécutez la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.Tools
```

Après avoir installé les deux packages, nous allons créer notre modèle à partir des tables de la base de données en utilisant la commande suivante :

```
Scaffold-DbContext "Votre chaîne de connexion ici" Microsoft.EntityFrameworkCore.SqlServer -OutputDir Models -Tables tblEmployee, tblCities
```

**N'oubliez pas** de mettre votre propre chaîne de connexion (à l'intérieur de guillemets doubles « »). Après l'exécution réussie de cette commande, un dossier « Models » sera créé. Ce dossier contient trois fichiers de classe : `myTestDBContext.cs`, `TblCities.cs` et `TblEmployee.cs`. Nous avons créé avec succès nos Modèles en utilisant l'approche database-first d'EF Core.

Maintenant, nous allons créer un autre fichier de classe pour gérer les opérations liées à la base de données.

Faites un clic droit sur le dossier « Models » et sélectionnez Ajouter >> Classe. Nommez votre classe `EmployeeDataAccessLayer.cs` et cliquez sur le bouton « Ajouter ». À ce stade, le dossier « Models » aura la structure suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/bovuU80LNmD-dy2hiWJTqQ5N11RnqoiFv4Oa)

Ouvrez « EmployeeDataAccessLayer.cs » et insérez le code suivant pour gérer les opérations de la base de données.

```
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace EFNgApp.Models
{
  public class EmployeeDataAccessLayer
  {
    myTestDBContext db = new myTestDBContext();

    public IEnumerable<TblEmployee> GetAllEmployees()
    {
      try
      {
        return db.TblEmployee.ToList();
      }
      catch
      {
        throw;
      }
    }

    // Pour ajouter un nouvel enregistrement d'employé
    public int AddEmployee(TblEmployee employee)
    {
      try
      {
        db.TblEmployee.Add(employee);
        db.SaveChanges();
        return 1;
      }
      catch
      {
        throw;
      }
    }

    // Pour mettre à jour les enregistrements d'un employé particulier
    public int UpdateEmployee(TblEmployee employee)
    {
      try
      {
        db.Entry(employee).State = EntityState.Modified;
        db.SaveChanges();
        return 1;
      }
      catch
      {
        throw;
      }
    }

    // Obtenir les détails d'un employé particulier
    public TblEmployee GetEmployeeData(int id)
    {
      try
      {
        TblEmployee employee = db.TblEmployee.Find(id);
        return employee;
      }
      catch
      {
        throw;
      }
    }

    // Pour supprimer l'enregistrement d'un employé particulier
    public int DeleteEmployee(int id)
    {
      try
      {
        TblEmployee emp = db.TblEmployee.Find(id);
        db.TblEmployee.Remove(emp);
        db.SaveChanges();
        return 1;
      }
      catch
      {
        throw;
      }
    }

    // Pour obtenir la liste des villes
    public List<TblCities> GetCities()
    {
      List<TblCities> lstCity = new List<TblCities>();
      lstCity = (from CityList in db.TblCities select CityList).ToList();
      return lstCity;
    }
  }
}
```

Maintenant, nous allons procéder à la création de notre contrôleur Web API.

### Ajout du contrôleur Web API à l'application

Faites un clic droit sur le dossier Controllers et sélectionnez Ajouter >> Nouvel élément.

Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira. Sélectionnez « ASP.NET » dans le panneau de gauche. Ensuite, sélectionnez « Classe de contrôleur Web API » dans le panneau des modèles et donnez le nom `EmployeeController.cs`. Cliquez sur « Ajouter ».

![Image](https://cdn-media-1.freecodecamp.org/images/q623LWrLWzNKZSYDuGzALTxR0OxuLWmYey-G)

Cela créera notre classe de contrôleur Web API « EmployeeController ». Nous allons mettre toute notre logique métier dans ce contrôleur. Nous allons appeler les méthodes de « EmployeeDataAccessLayer » pour récupérer les données et les transmettre à l'interface Angular.

Ouvrez le fichier « EmployeeController.cs » et insérez le code suivant :

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using EFNgApp.Models;
using Microsoft.AspNetCore.Mvc;

namespace EFNgApp.Controllers
{
  public class EmployeeController : Controller
  {
    EmployeeDataAccessLayer objemployee = new EmployeeDataAccessLayer();

    [HttpGet]
    [Route("api/Employee/Index")]
    public IEnumerable<TblEmployee> Index()
    {
      return objemployee.GetAllEmployees();
    }

    [HttpPost]
    [Route("api/Employee/Create")]
    public int Create([FromBody] TblEmployee employee)
    {
      return objemployee.AddEmployee(employee);
    }

    [HttpGet]
    [Route("api/Employee/Details/{id}")]
    public TblEmployee Details(int id)
    {
      return objemployee.GetEmployeeData(id);
    }

    [HttpPut]
    [Route("api/Employee/Edit")]
    public int Edit([FromBody]TblEmployee employee)
    {
      return objemployee.UpdateEmployee(employee);
    }

    [HttpDelete]
    [Route("api/Employee/Delete/{id}")]
    public int Delete(int id)
    {
      return objemployee.DeleteEmployee(id);
    }

    [HttpGet]
    [Route("api/Employee/GetCityList")]
    public IEnumerable<TblCities> Details()
    {
      return objemployee.GetCities();
    }
  }
}
```

Nous avons terminé avec notre logique backend. Maintenant, nous allons coder notre frontend en utilisant Angular 5.

### Créer le Service Angular

Nous allons créer un service Angular qui convertira la réponse de l'API Web en JSON et la transmettra à notre composant.

Faites un clic droit sur le dossier « ClientApp/app » et sélectionnez Ajouter >> Nouveau Dossier et nommez le dossier « Services ».

Faites un clic droit sur le dossier « Services » et sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira. Sélectionnez « Scripts » dans le panneau de gauche. Ensuite, sélectionnez « Fichier TypeScript » dans le panneau des modèles, et donnez le nom `empservice.service.ts`. Cliquez sur « Ajouter ».

![Image](https://cdn-media-1.freecodecamp.org/images/XNeVx14RTmuHKuPLcemx4ZKNwivkQCYLY0kX)

Ouvrez le fichier « empservice.service.ts » et insérez le code suivant :

```
import { Injectable, Inject } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { Router } from '@angular/router';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';

@Injectable()
export class EmployeeService {
  myAppUrl: string = "";

  constructor(private _http: Http, @Inject('BASE_URL') baseUrl: string) {
    this.myAppUrl = baseUrl;
  }

  getCityList() {
    return this._http.get(this.myAppUrl + 'api/Employee/GetCityList')
      .map(res => res.json())
      .catch(this.errorHandler);
  }

  getEmployees() {
    return this._http.get(this.myAppUrl + 'api/Employee/Index')
      .map((response: Response) => response.json())
      .catch(this.errorHandler);
  }

  getEmployeeById(id: number) {
    return this._http.get(this.myAppUrl + "api/Employee/Details/" + id)
      .map((response: Response) => response.json())
      .catch(this.errorHandler)
  }

  saveEmployee(employee) {
    return this._http.post(this.myAppUrl + 'api/Employee/Create', employee)
      .map((response: Response) => response.json())
      .catch(this.errorHandler)
  }

  updateEmployee(employee) {
    return this._http.put(this.myAppUrl + 'api/Employee/Edit', employee)
      .map((response: Response) => response.json())
      .catch(this.errorHandler);
  }

  deleteEmployee(id) {
    return this._http.delete(this.myAppUrl + "api/Employee/Delete/" + id)
      .map((response: Response) => response.json())
      .catch(this.errorHandler);
  }

  errorHandler(error: Response) {
    console.log(error);
    return Observable.throw(error);
  }
}
```

À ce stade, vous pourriez obtenir l'erreur suivante : « Le paramètre 'employee' a implicitement un type 'any' » dans le fichier « empservice.service.ts ».

Si vous rencontrez ce problème, ajoutez la ligne suivante dans le fichier « tsconfig.json ».

"noImplicitAny": false

![Image](https://cdn-media-1.freecodecamp.org/images/d7o16eoU-aQFvrJ34miiRbbQTDUGkUZ5cObG)

Maintenant, nous allons créer nos composants.

### Création des composants Angular

Nous allons ajouter deux composants Angular à notre application :

1. Composant `fetchemployee` : pour afficher toutes les données des employés ou supprimer des données d'employés existantes.
2. Composant `addemployee` : pour ajouter de nouvelles données d'employés ou modifier des données d'employés existantes.

Faites un clic droit sur le dossier « ClientApp/app/components » et sélectionnez Ajouter >> Nouveau Dossier et nommez le dossier « addemployee ».

Faites un clic droit sur le dossier « addemployee », et sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira.

Sélectionnez « Scripts » dans le panneau de gauche, puis sélectionnez « Fichier TypeScript » dans le panneau des modèles. Donnez le nom `addemployee.component.ts`.

Cliquez sur « Ajouter ». Cela ajoutera un fichier TypeScript à l'intérieur du dossier « addemployee ».

![Image](https://cdn-media-1.freecodecamp.org/images/AcmOw3ktlM2vZn8ifpuABDRetETxUyQ0UrsE)

Faites un clic droit sur le dossier « addemployee » et sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira.

Sélectionnez « ASP.NET Core » dans le panneau de gauche, puis sélectionnez « Page HTML » dans le panneau des modèles. Donnez le nom `addemployee.component.html`.

Cliquez sur « Ajouter ». Cela ajoutera un fichier HTML à l'intérieur du dossier « addemployee ».

![Image](https://cdn-media-1.freecodecamp.org/images/k6398O41ak2SjjKxGswS6tb00SvfqIgGtI8q)

De même, créez un dossier « fetchemployee » à l'intérieur du dossier « ClientApp/app/components ».

Ajoutez les fichiers `fetchemployee.component.ts` et `fetchemployee.component.html`.

Maintenant, notre structure « ClientApp/app/components » ressemblera à l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1Ui2XGkgtU7CYRm0Jexoqrz4ZjhI89hYDTul)

Ouvrez `fetchemployee.component.ts` et insérez le code suivant :

```
import { Component, Inject } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Router, ActivatedRoute } from '@angular/router';
import { EmployeeService } from '../../services/empservice.service'

@Component({
  templateUrl: './fetchemployee.component.html'
})

export class FetchEmployeeComponent {
  public empList: EmployeeData[];

  constructor(public http: Http, private _router: Router, private _employeeService: EmployeeService) {
    this.getEmployees();
  }

  getEmployees() {
    this._employeeService.getEmployees().subscribe(
      data => this.empList = data
    )
  }

  delete(employeeID) {
    var ans = confirm("Voulez-vous supprimer l'employé avec l'ID : " + employeeID);
    if (ans) {
      this._employeeService.deleteEmployee(employeeID).subscribe((data) => {
        this.getEmployees();
      }, error => console.error(error))
    }
  }
}

interface EmployeeData {
  employeeId: number;
  name: string;
  gender: string;
  city: string;
  department: string;
}
```

Comprenons ce code.

Tout en haut, nous avons importé les modules Angular et les références à EmployeeService. Après cela, nous utilisons le décorateur `@Component` pour définir l'URL du modèle pour notre composant.

À l'intérieur de la classe `FetchEmployeeComponent`, nous avons déclaré une variable de tableau `empList` de type `EmployeeData`. `EmployeeData` est une interface ayant les propriétés identiques à notre classe `TblEmployeeModel`.

À l'intérieur de la méthode `getEmployees`, nous appelons la méthode `getEmployees` de notre service `EmployeeService`. Cela retournera un tableau d'`Employees` à stocker dans la variable `empList`. La méthode `getEmployees` est appelée à l'intérieur du constructeur, de sorte que les données des employés seront affichées lorsque la page se charge.

Ensuite, nous avons une méthode `delete` qui accepte `employeeID` comme paramètre. Cela invitera l'utilisateur avec une boîte de confirmation. Si l'utilisateur sélectionne « oui », cela supprimera l'employé avec cet `employeeID`.

Ouvrez `fetchemployee.component.html` et insérez le code suivant :

```
<h1>Données des employés</h1>

<p>Ce composant démontre la récupération des données des employés depuis le serveur.</p>
<p *ngIf="!empList"><em>Chargement...</em></p>
<p>
  <a [routerLink]="['/register-employee']">Créer un nouveau</a>
</p>
<table class='table' *ngIf="empList">
  <thead>
    <tr>
      <th>EmployeeId</th>
      <th>Nom</th>
      <th>Genre</th>
      <th>Département</th>
      <th>Ville</th>
    </tr>
  </thead>
  <tbody>
    <tr *ngFor="let emp of empList">
      <td>{{ emp.employeeId }}</td>
      <td>{{ emp.name }}</td>
      <td>{{ emp.gender }}</td>
      <td>{{ emp.department }}</td>
      <td>{{ emp.city }}</td>
      <td>
        <a [routerLink]="['/employee/edit/', emp.employeeId]">Éditer</a> |
        <a [routerLink]="" (click)="delete(emp.employeeId)">Supprimer</a>
      </td>
    </tr>
  </tbody>
</table>
```

Le code de ce fichier HTML est assez simple.

En haut, il y a un lien pour créer un nouvel enregistrement d'employé. Après cela, il y a un tableau pour afficher les données des employés, et deux liens pour éditer et supprimer chaque enregistrement d'employé.

Nous avons terminé avec notre composant `fetchemployee`.

Maintenant, ouvrez `addemployee.component.ts` et insérez le code suivant.

```
import { Component, OnInit } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { NgForm, FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { FetchEmployeeComponent } from '../fetchemployee/fetchemployee.component';
import { EmployeeService } from '../../services/empservice.service';

@Component({
  templateUrl: './AddEmployee.component.html'
})

export class createemployee implements OnInit {
  employeeForm: FormGroup;
  title: string = "Créer";
  employeeId: number;
  errorMessage: any;
  cityList: Array<any> = [];

  constructor(private _fb: FormBuilder, private _avRoute: ActivatedRoute,
    private _employeeService: EmployeeService, private _router: Router) {
    if (this._avRoute.snapshot.params["id"]) {
      this.employeeId = this._avRoute.snapshot.params["id"];
    }

    this.employeeForm = this._fb.group({
      employeeId: 0,
      name: ['', [Validators.required]],
      gender: ['', [Validators.required]],
      department: ['', [Validators.required]],
      city: ['', [Validators.required]]
    })
  }

  ngOnInit() {
    this._employeeService.getCityList().subscribe(
      data => this.cityList = data
    )
    if (this.employeeId > 0) {
      this.title = "Éditer";
      this._employeeService.getEmployeeById(this.employeeId)
        .subscribe(resp => this.employeeForm.setValue(resp)
        , error => this.errorMessage = error);
    }
  }

  save() {
    if (!this.employeeForm.valid) {
      return;
    }
    if (this.title == "Créer") {
      this._employeeService.saveEmployee(this.employeeForm.value)
        .subscribe((data) => {
          this._router.navigate(['/fetch-employee']);
        }, error => this.errorMessage = error)
    }
    else if (this.title == "Éditer") {
      this._employeeService.updateEmployee(this.employeeForm.value)
        .subscribe((data) => {
          this._router.navigate(['/fetch-employee']);
        }, error => this.errorMessage = error)
    }
  }

  cancel() {
    this._router.navigate(['/fetch-employee']);
  }

  get name() { return this.employeeForm.get('name'); }
  get gender() { return this.employeeForm.get('gender'); }
  get department() { return this.employeeForm.get('department'); }
  get city() { return this.employeeForm.get('city'); }
}
```

Ce composant sera utilisé pour ajouter et éditer les données des employés.

Puisque nous utilisons un modèle de formulaire, ainsi qu'une validation côté client pour ajouter et éditer les données des employés, nous avons importé des classes depuis @angular/forms. Le code pour créer le formulaire a été placé à l'intérieur du constructeur afin que le formulaire soit affiché lorsque la page se charge.

Ce composant gérera à la fois les requêtes d'ajout et d'édition. Alors, comment le système différenciera-t-il les deux requêtes ? La réponse est le routage. Nous devons définir deux paramètres de route différents. L'un est pour ajouter des enregistrements d'employés. L'autre est pour éditer des enregistrements d'employés. Ces paramètres de route seront définis dans `app.shared.module.ts` dans la section suivante.

Nous avons déclaré la variable `title` pour afficher en haut de la page et la variable `id` pour stocker l'ID de l'employé passé en paramètre dans le cas d'une requête d'édition. Pour lire l'ID de l'employé depuis l'URL, nous allons utiliser `ActivatedRoute.snapshot` à l'intérieur du constructeur, et définir la valeur de la variable `id`.

À l'intérieur de `ngOnInit`, nous effectuons deux opérations :

1. Nous récupérons la liste des villes en appelant la méthode `getCityList` de notre service. Nous allons lier la liste des villes à une liste déroulante dans notre page HTML. Puisque nous appelons la méthode `getCityList` dans `ngOnInit`, la liste déroulante sera remplie lorsque la page se charge.
2. Nous allons vérifier si l'`id` est défini, puis nous allons changer le titre en « Éditer », obtenir les données pour cet `id` de notre service, et remplir les champs de notre formulaire. La valeur lue depuis la base de données sera retournée en JSON. Elle aura toutes les mêmes propriétés que nous avons déclarées dans notre `FormBuilder`, donc nous utilisons la méthode `setValue` pour remplir notre formulaire.

La méthode save sera appelée lorsque le bouton « Save » de notre formulaire sera cliqué. Les opérations **add** et **edit** appelleront la méthode correspondante de notre service et, en cas de succès, redirigeront vers le composant fetch-employee.

Dans le dernier, nous avons également défini des fonctions getter pour les noms de contrôle de notre formulaire afin d'activer la validation côté client.

Ouvrez `addemployee.component.html` et insérez le code suivant.

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title></title>
</head>
<body>
  <h1>{{title}}</h1>
  <h3>Employé</h3>
  <hr />
  <form [formGroup]="employeeForm" (ngSubmit)="save()" #formDir="ngForm" novalidate>
    <div class="form-group row">
      <label class=" control-label col-md-12" for="Name">Nom</label>
      <div class="col-md-4">
        <input class="form-control" type="text" formControlName="name">
      </div>
      <span class="text-danger" *ngIf="employeeForm.hasError('required', 'name') && formDir.submitted">
        Le nom est requis.
      </span>
    </div>
    <div class="form-group row">
      <label class="control-label col-md-12" for="Gender">Genre</label>
      <div class="col-md-4">
        <select class="form-control" data-val="true" formControlName="gender">
          <option value="">-- Sélectionner le genre --</option>
          <option value="Male">Homme</option>
          <option value="Female">Femme</option>
        </select>
      </div>
      <span class="text-danger" *ngIf="employeeForm.hasError('required', 'gender') && formDir.submitted">
        Le genre est requis
      </span>
    </div>
    <div class="form-group row">
      <label class="control-label col-md-12" for="Department">Département</label>
      <div class="col-md-4">
        <input class="form-control" type="text" formControlName="department">
      </div>
      <span class="text-danger" *ngIf="employeeForm.hasError('required', 'department') && formDir.submitted">
        Le département est requis
      </span>
    </div>
    <div class="form-group row">
      <label class="control-label col-md-12" for="City">Ville</label>
      <div class="col-md-4">
        <select class="form-control" data-val="true" formControlName="city">
          <option value="">--Sélectionner la ville--</option>
          <option *ngFor="let city of cityList"
            value={{city.cityName}}>
            {{city.cityName}}
          </option>
        </select>
      </div>
      <span class="text-danger" *ngIf="employeeForm.hasError('required', 'city') && formDir.submitted">
        La ville est requise
      </span>
    </div>
    <div class="form-group">
      <button type="submit" class="btn btn-default">Enregistrer</button>
      <button class="btn" (click)="cancel()">Annuler</button>
    </div>
  </form>
</body>
</html>
```

Ici, vous pouvez observer que nous avons l'attribut `[formGroup]="employeeForm"`, qui est notre nom de groupe de formulaire défini dans `addemployee.component.ts`. `(ngSubmit)="save()"` invoquera notre méthode `save` lors de la soumission du formulaire.

De plus, chaque contrôle d'entrée a l'attribut `formControlName="xyz"`. Cela est utilisé pour lier `FormControl` au HTML. Nous avons également défini des messages d'erreur pour les vérifications de validation côté client. Ceux-ci seront invoqués uniquement lors de la soumission du formulaire.

Pour lier la liste déroulante, nous utilisons la propriété `cityList` que nous avons remplie à partir de `tblCities`. Elle a été remplie en appelant la méthode `getCityList` de notre service, à l'intérieur de la méthode `ngOnInit` de `addemployee.component.ts`.

### Définition de la route et du menu de navigation pour notre application

À l'intérieur du dossier « app », ouvrez `app.shared.module.ts` et insérez le code suivant :

```
import { NgModule } from '@angular/core';
import { EmployeeService } from './services/empservice.service'
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';

import { AppComponent } from './components/app/app.component';
import { NavMenuComponent } from './components/navmenu/navmenu.component';
import { HomeComponent } from './components/home/home.component';
import { FetchEmployeeComponent } from './components/fetchemployee/fetchemployee.component'
import { createemployee } from './components/addemployee/AddEmployee.component'

@NgModule({
  declarations: [
    AppComponent,
    NavMenuComponent,
    HomeComponent,
    FetchEmployeeComponent,
    createemployee,
  ],
  imports: [
    CommonModule,
    HttpModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      { path: '', redirectTo: 'home', pathMatch: 'full' },
      { path: 'home', component: HomeComponent },
      { path: 'fetch-employee', component: FetchEmployeeComponent },
      { path: 'register-employee', component: createemployee },
      { path: 'employee/edit/:id', component: createemployee },
      { path: '**', redirectTo: 'home' }
    ])
  ],
  providers: [EmployeeService]
})
export class AppModuleShared { }
```

Ici, nous avons également importé tous nos composants et défini la route pour notre application comme suit :

* home : qui redirigera vers le composant `home`
* fetch-employee : pour afficher toutes les données des employés en utilisant le composant `fetchemployee`
* register-employee : pour ajouter un nouvel enregistrement d'employé en utilisant le composant `createemployee`
* employee/edit/:id : pour éditer un enregistrement d'employé existant en utilisant le composant `createemployee`

Une dernière chose est de définir le menu de navigation pour notre application. Dans « /app/components/navmenu/ », ouvrez `navmenu.component.html` et insérez le code suivant.

```
<div class='main-nav'>
  <div class='navbar navbar-inverse'>
    <div class='navbar-header'>
      <button type='button' class='navbar-toggle' data-toggle='collapse' data-target='.navbar-collapse'>
        <span class='sr-only'>Basculer la navigation</span>
        <span class='icon-bar'></span>
        <span class='icon-bar'></span>
        <span class='icon-bar'></span>
      </button>
      <a class='navbar-brand' [routerLink]="['/home']">ASPCoreWithAngular</a>
    </div>
    <div class='clearfix'></div>
    <div class='navbar-collapse collapse'>
      <ul class='nav navbar-nav'>
        <li [routerLinkActive]="['link-active']">
          <a [routerLink]="['/home']">
            <span class='glyphicon glyphicon-home'></span> Accueil
          </a>
        </li>
        <li [routerLinkActive]="['link-active']">
          <a [routerLink]="['/fetch-employee']">
            <span class='glyphicon glyphicon-th-list'></span> Récupérer les employés
          </a>
        </li>
      </ul>
    </div>
  </div>
</div>
```

Et c'est tout. Nous avons créé notre première application ASP.NET Core en utilisant Angular 5 et l'approche database-first d'Entity Framework Core.

### Démonstration d'exécution

Appuyez sur F5 pour lancer l'application.

Une page web s'ouvrira comme montré dans l'image ci-dessous. Remarquez l'URL montrant la route pour notre composant home. Le menu de navigation à gauche montre le lien de navigation pour les pages « Accueil » et « Récupérer les employés ».

![Image](https://cdn-media-1.freecodecamp.org/images/zfm-H3j-jMEE5ZMZQCGdVCUludViC0zJS3kr)

Cliquez sur « Récupérer les employés » dans le menu de navigation. Il redirigera vers le composant `fetchemployee` et affichera toutes les données des employés sur la page.

![Image](https://cdn-media-1.freecodecamp.org/images/hbGnwdxmGM8m9P4Va-xrwBK0BKha0dernmQP)

Puisque nous n'avons ajouté aucune donnée, il est vide.

Cliquez sur « Créer un nouveau » pour naviguer vers la page « /register-employee ». Ajoutez un nouvel enregistrement d'employé comme montré dans l'image ci-dessous. Vous pouvez voir que le champ **Ville** est une liste déroulante, contenant tous les noms de villes que nous avons insérés dans `tblCities`.

![Image](https://cdn-media-1.freecodecamp.org/images/iNzUNhKhYjlpyKyc7WlYFBkyeAnNeNvB6BG9)

Si nous omettons des données dans un champ lors de la création d'un enregistrement d'employé, nous obtiendrons un message d'erreur de validation de champ obligatoire.

![Image](https://cdn-media-1.freecodecamp.org/images/SYafIcJS18WIjKzPWiqJfpEBt9ay7fmBeGoN)

Après avoir inséré les données dans tous les champs, cliquez sur le bouton « Enregistrer ». Le nouvel enregistrement d'employé sera créé, et vous serez redirigé vers la page « /fetch-employee ». Cette page affiche les enregistrements de tous les employés. Ici, nous pouvons également voir les méthodes d'action « Éditer » et « Supprimer ».

![Image](https://cdn-media-1.freecodecamp.org/images/rlUf3JpBh7uj69tQ2Fs9mWA47OKGTSiVxoSt)

Si nous voulons éditer un enregistrement d'employé existant, cliquez sur le lien d'action « Éditer ». Il ouvrira la page « Éditer » comme ci-dessous, où nous pouvons changer les données de l'employé. Remarquez que nous avons passé l'EmployeeId dans le paramètre de l'URL.

![Image](https://cdn-media-1.freecodecamp.org/images/XUU6X3xe7tBTjCrTKRPLNDL7-t7Yaw3E4KFb)

Ici, nous avons changé la `Ville` de l'employé Rahul de Hyderabad à Chennai. Cliquez sur « Enregistrer » pour revenir à la page « fetch-employee » et voir les modifications mises à jour comme indiqué dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/fYGlFUkpv6LrwAMETcSFnSU-nFeMPNBthFTL)

Si nous omettons des champs lors de l'édition des enregistrements des employés, la vue Éditer affichera également un message d'erreur de validation de champ obligatoire comme montré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/MejmWwE9kxJG2rwT7Abkj69Y6gcU3P6ZFrAy)

Maintenant, nous allons effectuer une opération « Supprimer » sur un employé nommé Swati avec l'ID d'employé 2. Cliquez sur le lien d'action « Supprimer ». Cela ouvrira une boîte de confirmation JavaScript demandant une confirmation pour supprimer.

![Image](https://cdn-media-1.freecodecamp.org/images/4phku3XYBQRTKjYWjzhHNaglb7ZDk80nFkHD)

Une fois que nous cliquons sur « OK », Swati qui est l'ID d'employé 2 sera supprimé de notre enregistrement. Vous pouvez voir la liste mise à jour des employés comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/8iRuxCuipFk-moKUTwXdIVgHTQ9WgTt91Xga)

### Autres sources utiles :

* [Opérations CRUD avec ASP.NET Core en utilisant Angular 5 et ADO.NET](http://ankitsharmablogs.com/crud-operations-asp-net-core-using-angular-5-ado-net/)
* [Commencer avec Angular 5 en utilisant Visual Studio Code](http://ankitsharmablogs.com/getting-started-with-angular-5-using-visual-studio-code/)
* [Opération CRUD avec ASP.NET Core MVC en utilisant Visual Studio Code et EF](http://ankitsharmablogs.com/crud-operation-asp-net-core-mvc-using-visual-studio-code-ef/)
* [Opération CRUD avec ASP.NET Core MVC en utilisant ADO.NET et Visual Studio 2017](http://ankitsharmablogs.com/crud-operation-with-asp-net-core-mvc-using-ado-net/)
* [Opération CRUD avec ASP.NET Core MVC en utilisant Visual Studio Code et ADO.NET](http://ankitsharmablogs.com/crud-operation-with-asp-net-core-mvc-using-visual-studio-code-and-ado-net/)
* [ASP.NET Core — Commencer avec Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)

### Conclusion

Nous avons créé avec succès une application ASP.NET Core en utilisant Angular 5 et l'approche database-first d'Entity Framework Core avec l'aide de Visual Studio 2017 et SQL Server 2012. Nous avons utilisé des formulaires Angular pour obtenir des données de l'utilisateur et également lier la liste déroulante à la table de la base de données en utilisant Entity Framework.

Vous pouvez consulter mes autres articles sur ASP .NET Core [ici](http://ankitsharmablogs.com/category/asp-net-core/).

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)
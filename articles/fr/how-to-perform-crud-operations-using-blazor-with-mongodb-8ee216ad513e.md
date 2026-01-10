---
title: Comment effectuer des opérations CRUD avec Blazor et MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T16:04:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-crud-operations-using-blazor-with-mongodb-8ee216ad513e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wQLUVCBOZVZo-PxJLLdrzQ.gif
tags:
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment effectuer des opérations CRUD avec Blazor et MongoDB
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will create a Blazor application using MongoDB as our database
  provider. We will create a Single Page Application (SPA) and perform CRUD operations
  on it. A modal popup will display the form to handle ...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons créer une application Blazor en utilisant MongoDB comme fournisseur de base de données. Nous allons créer une application monopage (SPA) et effectuer des opérations CRUD dessus. Une fenêtre modale affichera le formulaire pour gérer les entrées utilisateur. Le formulaire contient également une liste déroulante, qui sera liée à une collection de base de données.

Nous utiliserons Visual Studio 2017 et MongoDB 4.0.

Regardez l'application finale.

![Image](https://cdn-media-1.freecodecamp.org/images/VtnrpPoR5nyDc5lkeDMM54y45KfjCfL0defG)

### Prérequis

* Installez le SDK .NET Core 2.1 ou supérieur depuis [ici](https://www.microsoft.com/net/learn/get-started-with-dotnet-tutorial#windowscmd)
* Installez Visual Studio 2017 v15.7 ou supérieur depuis [ici](https://www.visualstudio.com/downloads/)
* Installez l'extension ASP.NET Core Blazor Language Services depuis [ici](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)
* Téléchargez et installez MongoDB Community Edition. Vous pouvez trouver le guide d'installation [ici](https://docs.mongodb.com/manual/administration/install-community/).

Les versions de Visual Studio 2017 antérieures à v15.7 ne supportent pas le framework Blazor.

### Code Source

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-CRUD-With-MongoDB).

### Configuration de MongoDB

Après avoir installé MongoDB, nous devons ajouter le chemin des binaires MongoDB à la variable PATH du système. Le chemin d'installation par défaut sur une machine Windows est `C:\Program Files\MongoDB`. Vous devez donc inclure `C:\Program Files\MongoDB\Server\4.0\bin` dans la variable PATH du système. Si vous n'utilisez pas Windows, vous pouvez trouver le processus de configuration des binaires MongoDB dans le lien du guide d'installation fourni dans la section des prérequis ci-dessus.

### Travailler avec MongoDB

Nous devons configurer le chemin où les données seront stockées sur notre machine. Ouvrez l'invite de commandes en tant qu'administrateur et exécutez la commande suivante pour définir le chemin de stockage des données sur votre machine.

```
mongod --dbpath C:\MongoData
```

Vous pouvez fournir le chemin de n'importe quel dossier où vous souhaitez stocker les données. Cette commande se connectera à MongoDB sur le port 27017 (le port par défaut pour la connexion MongoDB). Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/LoKmouJOGBC6qO8YNmPysnVN-V0J7Fa7N6nP)

**Note Importante :**

> _Il est conseillé d'utiliser l'invite de commandes plutôt que PowerShell lors de l'exécution des commandes MongoDB, car toutes les commandes MongoDB ne fonctionnent pas dans PowerShell._

Ouvrez une nouvelle fenêtre d'invite de commandes et exécutez la commande `mongo` pour démarrer le serveur mongo. Voir l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/sZPec9cuTRIYkXI2lNnMtMsrSRIDq0uj8SNz)

Exécutez la commande suivante pour créer la base de données :

```
use EmployeeDB
```

Cela créera notre base de données `EmployeeDB`. Exécutez la commande suivante pour créer une nouvelle collection dans la base de données :

```
db.createCollection('EmployeeRecord')
```

Cela créera une collection `EmployeeRecord` dans notre base de données. MongoDB stocke les données dans des documents de type JSON. Insérons un document d'exemple dans notre collection `EmployeeRecord`. Exécutez la commande suivante.

```
db.EmployeeRecord.insert({'Name':'Ankit','Gender':'Male','Department':'HR','City':'Mumbai'})
```

Vous pouvez observer que nous avons fourni les données au format JSON sous forme de paires clé-valeur. Exécutez la commande suivante pour lister tous les documents de la collection EmployeeRecord.

```
db.EmployeeRecord.find({})
```

Le schéma de la base de données ajoutera une propriété _id à chaque document de la collection. Cette propriété est de type ObjectId et sera générée automatiquement. Nous utiliserons cette propriété _id pour identifier de manière unique un document dans la collection. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/F1PYd2lqR1RAF7g9Y7vB0y0vi4OdKoXwOnjL)

Si vous souhaitez supprimer tous les documents de la collection EmployeeRecord, vous devez exécuter la commande suivante :

```
db.EmployeeRecord.remove({})
```

Nous allons créer une autre collection pour stocker une liste de noms de villes qui sera utilisée pour remplir le champ City de la collection `EmployeeRecord`. Nous lierons également cette collection à une liste déroulante dans notre application web à partir de laquelle l'utilisateur sélectionnera la ville souhaitée.

Exécutez la commande suivante pour créer la collection `Cities`.

```
db.createCollection('Cities')
```

Nous allons insérer cinq noms de villes d'exemple dans cette collection. Pour insérer les documents en masse dans la collection `Cities`, exécutez la commande suivante :

```
db.Cities.insertMany([   { CityName : "New Delhi" },   { CityName : "Mumbai"},   { CityName : "Hyderabad"},   { CityName : "Chennai"},   { CityName : "Bengaluru" }])
```

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/wYdXE-rZ2FscqYR1-pN5f8-cXof9pU-O0ijq)

### Créer une application web Blazor

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet.

Après avoir sélectionné le projet, une boîte de dialogue "Nouveau Projet" s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche. Ensuite, sélectionnez "Application Web ASP.NET Core" parmi les types de projets disponibles. Donnez le nom du projet `BlazorWithMongo` et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/xghuCK555DbyDnK9k6AdshsxqZpyGhyir1S0)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez observer deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez ".NET Core" et "ASP.NET Core 2.0" dans ces menus déroulants. Ensuite, sélectionnez le modèle "Blazor (ASP .NET Core hébergé)" et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/XZgVOb9wpPPpoVgM43XToSbehGqTU2d52Q-7)

Notre solution Blazor sera maintenant créée. Vous pouvez observer que nous avons trois fichiers de projet créés dans cette solution

1. BlazorWithMongo.Client — Il contient le code côté client et les pages qui seront rendues dans le navigateur.
2. BlazorWithMongo.Server — Il contient les codes côté serveur tels que la couche d'accès aux données et l'API web.
3. BlazorWithMongo.Shared — Il contient le code partagé qui peut être accessible à la fois par le client et le serveur. Il contient notre classe de modèle et la classe de contexte de base de données.

### Installation du pilote MongoDB

Pour accéder à MongoDB depuis notre application, nous devons installer le pilote MongoDB en utilisant la console du gestionnaire de packages. Nous allons l'installer dans le projet BlazorWithMongo.Shared afin qu'il soit également accessible au projet Server.

Accédez à Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages. Sélectionnez BlazorWithMongo.Shared dans le menu déroulant Projet par défaut et exécutez la commande suivante :

```
Install-Package MongoDB.Driver
```

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/emAD07arocn53VcdFKVSeNCdf3ipQTH5QBJk)

### Création du Modèle

Nous allons créer notre classe de modèle dans le projet `BlazorWithMongo.Shared`. Cliquez avec le bouton droit sur `BlazorWithMongo.Shared` et sélectionnez Ajouter >> Nouveau Dossier. Nommez le dossier Models. Cliquez à nouveau avec le bouton droit sur le dossier Models et sélectionnez Ajouter >> Classe pour ajouter un nouveau fichier de classe. Donnez le nom de votre classe Employee.cs et cliquez sur Ajouter.

Ouvrez la classe Employee.cs et placez le code suivant à l'intérieur :

```
using System;using System.Collections.Generic;using System.Text;using MongoDB.Bson;using MongoDB.Bson.Serialization.Attributes;namespace BlazorWithMongo.Shared.Models{    public class Employee    {        [BsonId]        [BsonRepresentation(BsonType.ObjectId)]        public string Id { get; set; }        public string Name { get; set; }        public string City { get; set; }        public string Department { get; set; }        public string Gender { get; set; }    }}
```

Nous avons inclus la propriété Id de type ObjectId dans notre définition de classe et l'avons décorée avec l'attribut `[BsonId]`. Cette propriété est requise pour mapper les objets du modèle à la collection MongoDB.

De même, créez un autre fichier de classe `Cities.cs` et placez le code suivant à l'intérieur :

```
using System;using System.Collections.Generic;using System.Text;using MongoDB.Bson;using MongoDB.Bson.Serialization.Attributes;namespace BlazorWithMongo.Shared.Models{    public class Cities    {        [BsonId]        [BsonRepresentation(BsonType.ObjectId)]        public string Id { get; set; }        public string CityName { get; set; }    }}
```

### Création de la classe de contexte de base de données

Ajoutez un nouveau fichier de classe au dossier Models et nommez-le `EmployeeDBContext.cs`. Placez le code suivant à l'intérieur :

```
using MongoDB.Driver;using System;using System.Collections.Generic;using System.Text;namespace BlazorWithMongo.Shared.Models{    public class EmployeeDBContext    {        private readonly IMongoDatabase _mongoDatabase;        public EmployeeDBContext()        {            var client = new MongoClient("mongodb://localhost:27017");            _mongoDatabase = client.GetDatabase("EmployeeDB");        }        public IMongoCollection<Employee> EmployeeRecord        {            get            {                return _mongoDatabase.GetCollection<Employee>("EmployeeRecord");            }        }        public IMongoCollection<Cities> CityRecord        {            get            {                return _mongoDatabase.GetCollection<Cities>("Cities");            }        }    }}
```

Ici, nous avons défini un `MongoClient` qui se connectera à l'instance du serveur MongoDB en utilisant la chaîne de connexion par défaut pour MongoDB. Nous utilisons la méthode GetDatabase pour récupérer l'instance de la base de données. La méthode `EmployeeRecord` est utilisée pour récupérer la collection `EmployeeRecord` de notre base de données et la mapper à la classe de modèle Employee. De même, la méthode `CityRecord` récupérera la collection Cities de la base de données et la mappers à la classe de modèle Cities.

### Création de la couche d'accès aux données pour l'application

Cliquez avec le bouton droit sur le projet `BlazorWithMongo.Server` puis sélectionnez Ajouter >> Nouveau Dossier et nommez le dossier DataAccess. Nous ajouterons notre classe pour gérer les opérations liées à la base de données uniquement dans ce dossier.

Cliquez avec le bouton droit sur le dossier _DataAccess_ et sélectionnez Ajouter >> Classe. Nommez votre classe `EmployeeDataAccessLayer.cs`. Ouvrez `EmployeeDataAccessLayer.cs` et placez le code suivant à l'intérieur :

```
using BlazorWithMongo.Shared.Models;using MongoDB.Driver;using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;namespace BlazorWithMongo.Server.DataAccess{    public class EmployeeDataAccessLayer    {        EmployeeDBContext db = new EmployeeDBContext();        //Pour obtenir tous les détails des employés               public List<Employee> GetAllEmployees()        {            try            {                return db.EmployeeRecord.Find(_ => true).ToList();            }            catch            {                throw;            }        }        //Pour ajouter un nouvel enregistrement d'employé               public void AddEmployee(Employee employee)        {            try            {                db.EmployeeRecord.InsertOne(employee);            }            catch            {                throw;            }        }        //Obtenir les détails d'un employé particulier              public Employee GetEmployeeData(string id)        {            try            {                FilterDefinition<Employee> filterEmployeeData = Builders<Employee>.Filter.Eq("Id", id);                return db.EmployeeRecord.Find(filterEmployeeData).FirstOrDefault();            }            catch            {                throw;            }        }        //Pour mettre à jour les enregistrements d'un employé particulier              public void UpdateEmployee(Employee employee)        {            try            {                db.EmployeeRecord.ReplaceOne(filter: g => g.Id == employee.Id, replacement: employee);            }            catch            {                throw;            }        }        //Pour supprimer l'enregistrement d'un employé particulier              public void DeleteEmployee(string id)        {            try            {                FilterDefinition<Employee> employeeData = Builders<Employee>.Filter.Eq("Id", id);                db.EmployeeRecord.DeleteOne(employeeData);            }            catch            {                throw;            }        }        // Pour obtenir la liste des villes          public List<Cities> GetCityData()        {            try            {                return db.CityRecord.Find(_ => true).ToList();            }            catch            {                throw;            }        }    }}
```

Ici, nous avons défini les méthodes pour effectuer des opérations CRUD sur la base de données EmployeeDB.

### Ajout du contrôleur d'API web à l'application

Cliquez avec le bouton droit sur le dossier `BlazorWithMongo.Server/Controllers` et sélectionnez Ajouter >> Nouvel Élément. Une boîte de dialogue "Ajouter un nouvel élément" s'ouvrira. Sélectionnez Web dans le panneau de gauche, puis sélectionnez "Classe de contrôleur d'API" dans le panneau des modèles et donnez le nom EmployeeController.cs. Cliquez sur Ajouter.

![Image](https://cdn-media-1.freecodecamp.org/images/J1T5eoviTbmZyzQ84E99r7MxOhxQGHQXA2dk)

Cela créera notre classe API _EmployeeController_. Nous appellerons les méthodes de la classe _EmployeeDataAccessLayer_ pour récupérer les données et les transmettre au côté client

Ouvrez le fichier `EmployeeController.cs` et placez le code suivant à l'intérieur :

```
using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;using BlazorWithMongo.Server.DataAccess;using BlazorWithMongo.Shared.Models;using Microsoft.AspNetCore.Mvc;namespace BlazorWithMongo.Server.Controllers{    public class EmployeeController : Controller    {        EmployeeDataAccessLayer objemployee = new EmployeeDataAccessLayer();        [HttpGet]        [Route("api/Employee/Index")]        public IEnumerable<Employee> Index()        {            return objemployee.GetAllEmployees();        }        [HttpPost]        [Route("api/Employee/Create")]        public void Create([FromBody] Employee employee)        {            objemployee.AddEmployee(employee);        }        [HttpGet]        [Route("api/Employee/Details/{id}")]        public Employee Details(string id)        {            return objemployee.GetEmployeeData(id);        }        [HttpPut]        [Route("api/Employee/Edit")]        public void Edit([FromBody]Employee employee)        {            objemployee.UpdateEmployee(employee);        }        [HttpDelete]        [Route("api/Employee/Delete/{id}")]        public void Delete(string id)        {            objemployee.DeleteEmployee(id);        }        [HttpGet]        [Route("api/Employee/GetCities")]        public List<Cities> GetCities()        {            return objemployee.GetCityData();        }    }}
```

Nous avons maintenant terminé le codage pour notre logique backend. Nous allons donc maintenant procéder au codage de notre côté client.

### Création du composant de vue

Nous allons ajouter la page de vue dans le dossier `BlazorWithMongo.Client/Pages`. Par défaut, nous avons les pages "Counter" et "Fetch Data" fournies dans notre application. Ces pages par défaut n'affecteront pas notre application. Pour simplifier ce tutoriel, nous allons supprimer les pages _fetchdata_ et _counter_ de ce dossier.

Cliquez avec le bouton droit sur le dossier `BlazorWithMongo.Client/Pages` puis sélectionnez Ajouter >> Nouvel Élément. Une boîte de dialogue "Ajouter un nouvel élément" s'ouvrira. Sélectionnez "ASP.NET Core" dans le panneau de gauche. Ensuite, sélectionnez "Page Razor" dans le panneau des modèles et nommez-la EmployeeData.cshtml. Cliquez sur Ajouter. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Q6RqbEEXFCYIUCKmXLucA1NaNoQyquSOKdSf)

Cela ajoutera une page `EmployeeData.cshtml` à notre dossier `BlazorSPA.Client/Pages`. Cette page Razor aura deux fichiers : _EmployeeData.cshtml_ et _EmployeeData.cshtml.cs_.

Maintenant, nous allons ajouter du code à ces pages.

### EmployeeData.cshtml

Ouvrez la page `EmployeeData.cshtml` et placez le code suivant à l'intérieur :

```
@page "/fetchemployee"@inherits EmployeeDataModel<h1>Données des employés</h1><h3>Opération CRUD avec Blazor en utilisant MongoDB</h3><br /><div>    <div style="float:left">        <button class="btn btn-primary" onclick="@AddEmp">Ajouter un employé</button>    </div></div><br />@if (empList == null){    <p><em>Chargement...</em></p>}else{    <table class='table'>        <thead>            <tr>                <th>Nom</th>                <th>Genre</th>                <th>Département</th>                <th>Ville</th>            </tr>        </thead>        <tbody>            @foreach (var emp in empList)            {                <tr>                    <td>@emp.Name</td>                    <td>@emp.Gender</td>                    <td>@emp.Department</td>                    <td>@emp.City</td>                    <td>                        <button class="btn btn-info" onclick="@(async () => await EditEmployee(@emp.Id))">Modifier</button>                        <button class="btn btn-danger" onclick="@(async () => await DeleteConfirm(@emp.Id))">Supprimer</button>                    </td>                </tr>            }        </tbody>    </table>    if (isAdd)    {        <div class="modal" tabindex="-1" style="display:block" role="dialog">            <div class="modal-dialog">                <div class="modal-content">                    <div class="modal-header">                        <h3 class="modal-title">@modalTitle</h3>                        <button type="button" class="close" onclick="@closeModal">                            <span aria-hidden="true">X</span>                        </button>                    </div>                    <div class="modal-body">                        <form>                            <div class="form-group">                                <label for="Name" class="control-label">Nom</label>                                <input for="Name" class="form-control" bind="@emp.Name" />                            </div>                            <div class="form-group">                                <label asp-for="Gender" class="control-label">Genre</label>                                <select asp-for="Gender" class="form-control" bind="@emp.Gender">                                    <option value="">-- Sélectionner le genre --</option>                                    <option value="Male">Homme</option>                                    <option value="Female">Femme</option>                                </select>                            </div>                            <div class="form-group">                                <label asp-for="Department" class="control-label">Département</label>                                <input asp-for="Department" class="form-control" bind="@emp.Department" />                            </div>                            <div class="form-group">                                <label asp-for="City" class="control-label">Ville</label>                                <select asp-for="City" class="form-control" bind="@emp.City">                                    <option value="">-- Sélectionner la ville --</option>                                    @foreach (var city in cityList)                                    {                                        <option value="@city.CityName">@city.CityName</option>                                    }                                </select>                            </div>                        </form>                    </div>                    <div class="modal-footer">                        <button class="btn btn-block btn-success" onclick="@(async () => await SaveEmployee())" data-dismiss="modal">Enregistrer</button>                    </div>                </div>            </div>        </div>    }    if (isDelete)    {        <div class="modal" tabindex="-1" style="display:block" role="dialog">            <div class="modal-dialog">                <div class="modal-content">                    <div class="modal-header">                        <h3 class="modal-title">Supprimer un employé</h3>                    </div>                    <div class="modal-body">                        <h4>Voulez-vous supprimer cet employé ??</h4>                        <table class="table">                            <tr>                                <td>Nom</td>                                <td>@emp.Name</td>                            </tr>                            <tr>                                <td>Genre</td>                                <td>@emp.Gender</td>                            </tr>                            <tr>                                <td>Département</td>                                <td>@emp.Department</td>                            </tr>                            <tr>                                <td>Ville</td>                                <td>@emp.City</td>                            </tr>                        </table>                    </div>                    <div class="modal-footer">                        <button class="btn btn-danger" onclick="@(async () => await DeleteEmployee(emp.Id))" data-dismiss="modal">OUI</button>                        <button class="btn btn-warning" onclick="@closeModal">NON</button>                    </div>                </div>            </div>        </div>    }}
```

Comprenons ce code. En haut, nous avons défini la route de cette page comme "fetchemployee". Cela signifie que si nous ajoutons "fetchemployee" à l'URL racine de l'application, nous serons redirigés vers cette page.

Nous héritons également de la classe `EmployeeDataModel`, qui est définie dans le fichier `EmployeeData.cshtml.cs`. Cela nous permettra d'utiliser les méthodes définies dans la classe `EmployeeDataModel`.

Après cela, nous avons défini un bouton pour ajouter un nouvel enregistrement d'employé. Lorsque vous cliquez dessus, ce bouton ouvrira une fenêtre modale pour gérer les entrées utilisateur.

La liste des documents employés retournés par la base de données est stockée dans la variable _empList_. Si la variable n'est pas nulle, nous lierons les valeurs à un tableau pour afficher les documents employés sous forme de tableau. Chaque ligne du tableau a deux liens d'action. _Modifier_ pour modifier le document employé. _Supprimer_ pour supprimer le document employé.

Pour gérer les entrées utilisateur, nous utilisons un formulaire. Nous utilisons un seul formulaire pour les fonctionnalités Ajouter un employé et Modifier un employé. Le formulaire est défini dans une fenêtre modale et la fenêtre modale est affichée à l'écran en fonction de la valeur d'une propriété booléenne isAdd. La valeur de ce drapeau booléen est définie dans la page de code-behind (.cshtml.cs).

La liste déroulante Ville à l'intérieur du formulaire se lie à notre collection Cities dans la base de données à l'aide de la variable _cityList_. La cityList sera remplie au démarrage de l'application.

Le formulaire aura un bouton _Enregistrer_ qui invoquera la méthode `SaveEmployee`. Cette méthode est définie dans le fichier de code-behind pour ajouter ou mettre à jour un document employé.

Similaire à la fenêtre modale _Ajouter_, nous avons également une fenêtre modale _Supprimer_. Ce sera une fenêtre modale en lecture seule et demandera une confirmation pour supprimer un document employé. En cliquant sur "Oui", elle invoquera la méthode `DeleteEmployee` pour supprimer le document employé.

### EmployeeData.cshtml.cs

Ouvrez `EmployeeData.cshtml.cs` et placez le code suivant à l'intérieur :

```
using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;using System.Net.Http;using Microsoft.AspNetCore.Blazor;using Microsoft.AspNetCore.Blazor.Components;using BlazorWithMongo.Shared.Models;namespace BlazorWithMongo.Client.Pages{    public class EmployeeDataModel : BlazorComponent    {        [Inject]        protected HttpClient Http { get; set; }        protected List<Employee> empList;        protected List<Cities> cityList = new List<Cities>();        protected Employee emp = new Employee();        protected string modalTitle { get; set; }        protected Boolean isDelete = false;        protected Boolean isAdd = false;        protected string SearchString { get; set; }        protected override async Task OnInitAsync()        {            await GetEmployee();            await GetCities();        }        protected async Task GetEmployee()        {            empList = await Http.GetJsonAsync<List<Employee>>("api/Employee/Index");        }        protected async Task GetCities()        {            cityList = await Http.GetJsonAsync<List<Cities>>("api/Employee/GetCities");        }        protected void AddEmp()        {            emp = new Employee();            this.modalTitle = "Ajouter un employé";            this.isAdd = true;        }        protected async Task EditEmployee(string ID)        {            emp = await Http.GetJsonAsync<Employee>("/api/Employee/Details/" + ID);            this.modalTitle = "Modifier un employé";            this.isAdd = true;        }        protected async Task SaveEmployee()        {            if (emp.Id != null)            {                await Http.SendJsonAsync(HttpMethod.Put, "api/Employee/Edit", emp);            }            else            {                await Http.SendJsonAsync(HttpMethod.Post, "/api/Employee/Create", emp);            }            this.isAdd = false;            await GetEmployee();        }        protected async Task DeleteConfirm(string ID)        {            emp = await Http.GetJsonAsync<Employee>("/api/Employee/Details/" + ID);            this.isDelete = true;        }        protected async Task DeleteEmployee(string ID)        {            await Http.DeleteAsync("api/Employee/Delete/" + ID);            this.isDelete = false;            await GetEmployee();        }        protected void closeModal()        {            this.isAdd = false;            this.isDelete = false;        }    }}
```

Dans ce fichier, nous avons défini une classe `EmployeeDataModel` qui contiendra toutes les méthodes que nous utiliserons dans la page `EmployeeData.cshtml`. Nous injectons également le service `HttpClient` pour activer les appels d'API web.

Les variables _empList_ et _cityList_ sont définies pour contenir les données de la table Employee et de la table Cities, respectivement. Les variables sont remplies dans OnInitAsync pour s'assurer que les données sont disponibles lorsque la page se charge.

Cliquer sur le bouton "Ajouter un employé" invoquera la méthode `AddEmp`. Elle initialisera une instance vide du modèle Employee et définira la valeur du drapeau booléen _isAdd_ à true. Cela ouvrira une fenêtre modale avec un formulaire, demandant à l'utilisateur d'entrer la valeur pour un nouveau document employé. De même, nous avons défini une méthode `EditEmployee`, qui récupérera l'enregistrement de l'employé en fonction de l'Id pour lequel elle est invoquée. Elle définira également la valeur de _isAdd_ à true pour ouvrir la fenêtre modale afin de modifier le document employé.

La méthode `SaveEmployee` vérifiera si elle est invoquée pour ajouter un nouvel enregistrement d'employé ou pour modifier un enregistrement d'employé existant. Si l'Id n'est pas null, alors c'est une demande de "modification" et nous enverrons une requête PUT à l'API Web pour mettre à jour le document employé existant.

Si l'Id est null, alors c'est une demande de "création" et nous enverrons une requête POST à l'API Web pour créer un nouveau document employé.

Nous récupérerons ensuite la liste mise à jour des documents employés en appelant la méthode `GetEmployee`. Nous définissons également la valeur de _isAdd_ à false, fermant ainsi la fenêtre modale.

La méthode `DeleteConfirm` est invoquée en cliquant sur le bouton Supprimer correspondant à un enregistrement d'employé. Elle définira la valeur du drapeau booléen isDelete à true, ce qui affichera une fenêtre modale de confirmation de suppression. En cliquant sur OUI dans cette fenêtre, la méthode `DeleteEmployee` est invoquée. Elle envoie un appel d'API Web Delete pour supprimer le document employé. Elle définit également le drapeau booléen _isDelete_ à false, fermant ainsi la fenêtre modale.

### Ajout du lien au menu de navigation

La dernière étape consiste à ajouter le lien vers notre page "EmployeeData" dans le menu de navigation. Ouvrez la page `BlazorWithMongo/Shared/NavMenu.cshtml` et placez le code suivant à l'intérieur.

```
<div class="top-row pl-4 navbar navbar-dark">    <a class="navbar-brand" href="">BlazorWithMongo</a>    <button class="navbar-toggler" onclick=@ToggleNavMenu>        <span class="navbar-toggler-icon"></span>    </button></div><div class=@(collapseNavMenu ? "collapse" : null) onclick=@ToggleNavMenu>    <ul class="nav flex-column">        <li class="nav-item px-3">            <NavLink class="nav-link" href="" Match=NavLinkMatch.All>                <span class="oi oi-home" aria-hidden="true"></span> Accueil            </NavLink>        </li>        <li class="nav-item px-3">            <NavLink class="nav-link" href="fetchemployee">                <span class="oi oi-list-rich" aria-hidden="true"></span> Données des employés            </NavLink>        </li>    </ul></div>@functions {bool collapseNavMenu = true;void ToggleNavMenu(){    collapseNavMenu = !collapseNavMenu;}}
```

Ainsi, nous avons créé avec succès une application monopage (SPA) en utilisant Blazor avec l'aide de MongoDB comme fournisseur de base de données.

### Démo d'exécution

Appuyez sur F5 pour lancer l'application.

Une page web s'ouvrira comme montré dans l'image ci-dessous. Le menu de navigation à gauche montre le lien de navigation vers la page des données des employés.

![Image](https://cdn-media-1.freecodecamp.org/images/ss83hFQ3sh7bAKrlYgxPn7V6I4uoQCaWnlsu)

Cliquez sur le lien "Données des employés", il vous redirigera vers la vue EmployeeData. Ici, vous pouvez voir toutes les données des employés sous forme de tableau. Remarquez que l'URL a "fetchemployee" ajouté à celle-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/2pLLNuvyTz2aH8f4BBTCtwVdC6kC-u84QPRm)

Cliquez sur le bouton _Ajouter un employé_ pour ouvrir la fenêtre modale "Ajouter un employé". Entrez les données dans tous les champs et cliquez sur Enregistrer pour créer un nouveau document employé.

![Image](https://cdn-media-1.freecodecamp.org/images/U29tFaA9kmEvateUk-Or3uQCf2xd-3tHpRQ7)

Cela créera un nouveau document employé et affichera les données dans le tableau de vue. Cliquez sur le bouton Modifier correspondant à n'importe quelle ligne du tableau, il ouvrira à nouveau la fenêtre modale pour modifier l'enregistrement de l'employé. Modifiez les champs de saisie et cliquez sur enregistrer pour mettre à jour le document employé.

![Image](https://cdn-media-1.freecodecamp.org/images/nzPHXVURlvoAMEF02Nv817GeNtGbS4o08Fa3)

Si vous cliquez sur le bouton Supprimer correspondant à l'enregistrement de l'employé, il ouvrira une fenêtre de confirmation de suppression demandant une confirmation pour supprimer l'enregistrement de l'employé.

![Image](https://cdn-media-1.freecodecamp.org/images/6BBQF2IqYhIJVdkDdxKTtFliZ0yql3mfkAvt)

Cliquer sur OUI supprimera les données de l'employé et affichera la liste mise à jour des employés en actualisant le tableau de vue.

### Conclusion

Nous avons créé une application monopage (SPA) en utilisant Blazor avec l'aide de MongoDB comme fournisseur de base de données. Nous avons créé un système de gestion d'enregistrements d'employés d'exemple et effectué des opérations CRUD dessus. Pour gérer les entrées utilisateur, nous avons utilisé un formulaire dans une fenêtre modale. Nous avons utilisé Visual Studio 2017 et MongoDB 4.0 pour notre démonstration.

Veuillez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-CRUD-With-MongoDB) et jouez avec pour obtenir une meilleure compréhension.

Obtenez mon livre [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) pour en savoir plus sur Blazor.

Vous pouvez consulter mes autres articles [ici](http://ankitsharmablogs.com/).

Préparation aux entretiens ? Lisez mon article sur [C# Coding Questions For Technical Interviews](http://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/).

### Voir aussi

* [Comprendre Blazor côté serveur](http://ankitsharmablogs.com/understanding-server-side-blazor/)
* [Application monopage utilisant Blazor côté serveur](http://ankitsharmablogs.com/single-page-application-using-server-side-blazor/)
* [Création d'une SPA utilisant des pages Razor avec Blazor](http://ankitsharmablogs.com/creating-a-spa-using-razor-pages-with-blazor/)
* [ASP.NET Core — CRUD utilisant Blazor et Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [Déploiement d'une application Blazor sur IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)
* [Interopérabilité JavaScript dans Blazor](http://ankitsharmablogs.com/javascript-interop-in-blazor/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)